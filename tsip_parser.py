"""
tsip_parser.py  --  TSIP integration for the Trimble NAV-960

==========================================================================
Overview
==========================================================================
The NAV-960 can be configured to output TSIP (Trimble Standard Interface
Protocol) rather than NMEA.  In TSIP mode the single 0x8F 0xA9 0x17 0x02
streaming packet replaces all NMEA sentences and delivers more data:

    8E A9 17 00  cmd  -- configure lever arms and IMU orientation
    8E A9 17 01  cmd  -- enable IMU-corrected positions and detail stream
    8F A9 17 02  rsp  -- streaming IMU detail message

The rsp packet contains, in one frame:
    - Roll-corrected geodetic position  (Latitude / Longitude / Height)
    - Antenna geodetic position         (LatitudeOriginal / …)
    - ENU velocity                      (EVelocity / NVelocity / UVelocity)
    - Attitude                          (Yaw / Pitch / Roll, degrees)
    - Angular rates                     (YawRate / PitchRate / RollRate, deg/s)
    - Solution quality                  (HDOP, VDOP, sigmas, num sats, …)

This module wraps the py_tsip library (./py_tsip/) which handles all
serial I/O, DLE framing/deframing, baud-rate auto-negotiation, and
packet encoding/decoding.

Usage
-----
    from tsip_parser import NAV960TSIPClient, IMUState

    def on_imu(imu: IMUState):
        print(f"Yaw={imu.yaw:.2f}°  Pitch={imu.pitch:.2f}°  Roll={imu.roll:.2f}°")

    client = NAV960TSIPClient(
        port="COM7",
        lever_arm_x=0.0, lever_arm_y=0.0, lever_arm_z=0.0,
        on_imu_update=on_imu,
    )
    client.start()         # connects (blocks up to connect_timeout seconds)
    # … application loop …
    client.stop()
"""

import copy
import logging
import threading
import time
from dataclasses import dataclass, field
from typing import Callable, Optional

import py_tsip
from py_tsip.tsip_packets import (
    EClientPackets,
    EServerPackets,
    S8ea91700cmd_tup,
    S8ea91701cmd_tup,
)

logger = logging.getLogger(__name__)


# ===========================================================================
# IMU state data container
# ===========================================================================

@dataclass
class IMUState:
    """
    Navigation state decoded from the 0x8F 0xA9 0x17 0x02 TSIP packet.

    Attitude
    --------
    yaw, pitch, roll           : degrees  (NED convention)
    yaw_rate, pitch_rate,
    roll_rate                  : degrees / second

    Position — roll-corrected (the primary output)
    -----------------------------------------------
    latitude, longitude        : decimal degrees  (WGS-84)
    height                     : metres above the WGS-84 ellipsoid

    Position — antenna / original (uncorrected)
    -------------------------------------------
    lat_original, lon_original : decimal degrees
    height_original            : metres above the WGS-84 ellipsoid

    Velocity (ENU local frame)
    --------------------------
    e_vel  : East  component, m/s
    n_vel  : North component, m/s
    u_vel  : Up    component, m/s

    Solution quality
    ----------------
    gps_seconds    : GPS time of week, seconds
    num_satellites : number of satellites used
    hdop, vdop     : dilution of precision (horizontal / vertical)
    e_sigma,
    n_sigma,
    u_sigma        : 1-sigma position error in E/N/U, metres
    correction_age : age of differential correction, seconds
    imu_status     : IMU status flags (device-specific bitmask)
    position_type  : position type code (device-specific)
    station_id     : differential reference station ID
    last_update    : wall-clock time of last packet (time.time())
    """

    # Attitude
    yaw:        Optional[float] = None   # degrees
    pitch:      Optional[float] = None   # degrees
    roll:       Optional[float] = None   # degrees
    yaw_rate:   Optional[float] = None   # deg/s
    pitch_rate: Optional[float] = None   # deg/s
    roll_rate:  Optional[float] = None   # deg/s

    # Roll-corrected position
    latitude:   Optional[float] = None   # degrees
    longitude:  Optional[float] = None   # degrees
    height:     Optional[float] = None   # metres (ellipsoid)

    # Antenna / original position
    lat_original:    Optional[float] = None
    lon_original:    Optional[float] = None
    height_original: Optional[float] = None

    # ENU velocity
    e_vel: Optional[float] = None   # m/s
    n_vel: Optional[float] = None   # m/s
    u_vel: Optional[float] = None   # m/s

    # Solution quality
    gps_seconds:    Optional[float] = None
    num_satellites: Optional[int]   = None
    hdop:           Optional[float] = None
    vdop:           Optional[float] = None
    e_sigma:        Optional[float] = None
    n_sigma:        Optional[float] = None
    u_sigma:        Optional[float] = None
    correction_age: Optional[float] = None

    # Status codes
    imu_status:    Optional[int] = None
    position_type: Optional[int] = None
    station_id:    Optional[int] = None

    # Timestamp
    last_update: Optional[float] = None   # time.time()


# ===========================================================================
# TSIP client
# ===========================================================================

class NAV960TSIPClient:
    """
    Connects to a NAV-960 in TSIP mode, configures it, and streams
    IMUState updates via an on_imu_update callback.

    The underlying py_tsip.TsipPortManager handles serial I/O, baud-rate
    auto-negotiation (it sends a serial break to probe the receiver), DLE
    framing, and packet dispatching in its own background thread.

    Quick start
    -----------
        client = NAV960TSIPClient(port="COM7", on_imu_update=my_callback)
        client.start()
        # … your loop …
        client.stop()

    Lever arms
    ----------
    AntLevX/Y/Z are the GNSS antenna lever arms (offsets in metres from the
    IMU body reference point to the antenna phase centre, expressed in the
    body frame).  Leave at 0.0 if the IMU and antenna are co-located or if
    the values are already stored in the receiver.

    The remaining IMU orientation fields (ImuAngleRoll/Pitch/Yaw,
    ImuLevX/Y/Z, ImuRollOffset, ImuPitchOffset) default to 0.0; override
    via the imu_orientation dict if your installation differs from the
    receiver's default.

    Thread safety
    -------------
    The imu_state property returns a shallow copy of the internal state,
    so it is safe to read from any thread without holding a lock.
    """

    def __init__(
        self,
        port: str,
        lever_arm_x: float = 0.0,
        lever_arm_y: float = 0.0,
        lever_arm_z: float = 0.0,
        imu_orientation: Optional[dict] = None,
        on_imu_update: Optional[Callable[[IMUState], None]] = None,
        connect_timeout: float = 15.0,
    ):
        """
        Parameters
        ----------
        port             : serial port name, e.g. 'COM7' or '/dev/ttyUSB0'
        lever_arm_x/y/z  : antenna lever arms in metres (body frame)
        imu_orientation  : optional dict with keys matching S8ea91700cmd_tup
                           fields for non-default IMU mounting angles/offsets
                          (ImuAngleRoll, ImuAnglePitch, ImuAngleYaw,
                           ImuLevX, ImuLevY, ImuLevZ,
                           ImuRollOffset, ImuPitchOffset)
        on_imu_update    : callback invoked on every 8F A9 17 02 packet;
                           receives an IMUState instance
        connect_timeout  : seconds to wait for the port manager to reach
                           connected state before raising RuntimeError
        """
        self.port            = port
        self.lever_arm_x     = lever_arm_x
        self.lever_arm_y     = lever_arm_y
        self.lever_arm_z     = lever_arm_z
        self.imu_orientation = imu_orientation or {}
        self.on_imu_update   = on_imu_update
        self.connect_timeout = connect_timeout

        self._port_manager: Optional[py_tsip.TsipPortManager] = None
        self._imu_state     = IMUState()
        self._lock          = threading.Lock()

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    def start(self):
        """
        Open the serial port, wait for the connection handshake, configure
        the receiver, and begin streaming IMU data.

        Blocks until the connection is established or connect_timeout expires.

        Raises
        ------
        RuntimeError if the port does not connect within connect_timeout.
        """
        logger.info("[TSIP] Opening %s (connect timeout %.0f s)", self.port, self.connect_timeout)
        self._port_manager = py_tsip.TsipPortManager(self.port)

        connected = self._port_manager.WaitForConnection(self.connect_timeout)
        if not connected:
            raise RuntimeError(
                f"[TSIP] Timed out waiting for connection on {self.port} "
                f"after {self.connect_timeout} s"
            )
        print(f"[TSIP] Connected: {self._port_manager.GetConnectionStatus()}")

        # Brief settling time before sending config
        time.sleep(0.2)

        publisher = self._port_manager.GetPublisherGroup()

        # Register for the packets we care about
        packet_list = [
            EServerPackets.e8fa91702rsp,   # streaming IMU detail — our main data source
            EServerPackets.e8fa91700rsp,   # lever-arm config ACK
            EServerPackets.e8fa91701rsp,   # enable-streaming ACK
            EServerPackets.e13rsp,         # format error — sent when we transmit a bad packet
        ]
        publisher.RegisterObserver(packet_list, self)

        # Send configuration
        self._send_lever_arm_config()
        time.sleep(0.1)
        self._enable_imu_streaming()

    def stop(self):
        """Shut down the port manager and background thread."""
        if self._port_manager is not None:
            self._port_manager.Shutdown()
            self._port_manager = None
            logger.info("[TSIP] Disconnected from %s", self.port)

    @property
    def imu_state(self) -> IMUState:
        """Thread-safe snapshot of the latest IMU state."""
        with self._lock:
            return copy.copy(self._imu_state)

    # ------------------------------------------------------------------
    # Observer callback (called by py_tsip background thread)
    # ------------------------------------------------------------------

    def HandlePacket(self, packet_id, packet_data):
        """
        Called by the py_tsip publisher for every registered packet received.

        Routing:
            e8fa91702rsp  →  parse into IMUState, call on_imu_update
            e8fa91700rsp  →  log lever-arm config ACK
            e8fa91701rsp  →  log enable-streaming ACK
            e13rsp        →  log TSIP format error
        """
        if packet_id == EServerPackets.e8fa91702rsp:
            self._apply_imu_detail(packet_data)

        elif packet_id == EServerPackets.e8fa91700rsp:
            logger.info(
                "[TSIP] Lever-arm config ACK: "
                "AntLev=(%.3f, %.3f, %.3f) m  "
                "ImuAngle=(%.2f, %.2f, %.2f) deg",
                packet_data.AntLevX, packet_data.AntLevY, packet_data.AntLevZ,
                packet_data.ImuAngleRoll, packet_data.ImuAnglePitch, packet_data.ImuAngleYaw,
            )
            print(
                f"[TSIP] Lever-arm/IMU config ACK received "
                f"(AntLev: {packet_data.AntLevX:.3f}, "
                f"{packet_data.AntLevY:.3f}, "
                f"{packet_data.AntLevZ:.3f} m)"
            )

        elif packet_id == EServerPackets.e8fa91701rsp:
            logger.info(
                "[TSIP] Enable-streaming ACK: "
                "EnableIMUCorrection=%d  EnableIMUDetailStream=%d",
                packet_data.EnableIMUCorrection, packet_data.EnableIMUDetailStream,
            )
            print(
                f"[TSIP] Enable-streaming ACK received "
                f"(IMUCorrection={packet_data.EnableIMUCorrection}, "
                f"DetailStream={packet_data.EnableIMUDetailStream})"
            )

        elif packet_id == EServerPackets.e13rsp:
            logger.warning("[TSIP] Format error (0x13) received from receiver: %s", packet_data)
            print(f"[TSIP] WARNING: Receiver reported a format error (packet 0x13): {packet_data}")

    # ------------------------------------------------------------------
    # Config command senders
    # ------------------------------------------------------------------

    def _send_lever_arm_config(self):
        """
        Send 8E A9 17 00 to configure lever arms and IMU orientation.

        Fields default to 0.0 except AntLevX/Y/Z which come from the
        constructor arguments.  Override other fields via imu_orientation.
        """
        defaults = {
            "AntLevX":       self.lever_arm_x,
            "AntLevY":       self.lever_arm_y,
            "AntLevZ":       self.lever_arm_z,
            "ImuAngleRoll":  0.0,
            "ImuAnglePitch": 0.0,
            "ImuAngleYaw":   0.0,
            "ImuLevX":       0.0,
            "ImuLevY":       0.0,
            "ImuLevZ":       0.0,
            "ImuRollOffset":  0.0,
            "ImuPitchOffset": 0.0,
        }
        defaults.update(self.imu_orientation)

        cmd = S8ea91700cmd_tup(
            AntLevX       = defaults["AntLevX"],
            AntLevY       = defaults["AntLevY"],
            AntLevZ       = defaults["AntLevZ"],
            ImuAngleRoll  = defaults["ImuAngleRoll"],
            ImuAnglePitch = defaults["ImuAnglePitch"],
            ImuAngleYaw   = defaults["ImuAngleYaw"],
            ImuLevX       = defaults["ImuLevX"],
            ImuLevY       = defaults["ImuLevY"],
            ImuLevZ       = defaults["ImuLevZ"],
            ImuRollOffset  = defaults["ImuRollOffset"],
            ImuPitchOffset = defaults["ImuPitchOffset"],
        )
        self._port_manager.TsipSendClientPacket(EClientPackets.e8ea91700cmd, cmd)
        logger.info(
            "[TSIP] Sent lever-arm config: AntLev=(%.3f, %.3f, %.3f) m",
            self.lever_arm_x, self.lever_arm_y, self.lever_arm_z,
        )

    def _enable_imu_streaming(self):
        """
        Send 8E A9 17 01 to enable IMU-corrected positions and detail streaming.
        """
        cmd = S8ea91701cmd_tup(
            EnableIMUCorrection    = 1,
            EnableIMUDetailStream  = 1,
        )
        self._port_manager.TsipSendClientPacket(EClientPackets.e8ea91701cmd, cmd)
        logger.info("[TSIP] Sent enable-IMU-streaming command")

    # ------------------------------------------------------------------
    # Internal — parse incoming packet into IMUState
    # ------------------------------------------------------------------

    def _apply_imu_detail(self, pkt):
        """
        Convert an e8fa91702rsp namedtuple into an IMUState and publish it.

        S8fa91702rsp_tup fields (format '=dBBddddddfffBBffffffBffffffB'):
            GPSSeconds(d), PositionEngine(B), PositionType(B),
            Latitude(d), Longitude(d), Height(d),
            LatitudeOriginal(d), LongitudeOriginal(d), HeightOriginal(d),
            EVelocity(f), NVelocity(f), UVelocity(f),
            Direction(B), ImuStatus(B),
            Yaw(f), Pitch(f), Roll(f), YawRate(f), PitchRate(f), RollRate(f),
            NumSatellites(B), HDOP(f), VDOP(f), ESigma(f), NSigma(f), USigma(f),
            CorrectionAge(f), StationID(B)
        """
        imu = IMUState(
            gps_seconds    = pkt.GPSSeconds,
            position_type  = pkt.PositionType,
            latitude       = pkt.Latitude,
            longitude      = pkt.Longitude,
            height         = pkt.Height,
            lat_original   = pkt.LatitudeOriginal,
            lon_original   = pkt.LongitudeOriginal,
            height_original= pkt.HeightOriginal,
            e_vel          = pkt.EVelocity,
            n_vel          = pkt.NVelocity,
            u_vel          = pkt.UVelocity,
            imu_status     = pkt.ImuStatus,
            yaw            = pkt.Yaw,
            pitch          = pkt.Pitch,
            roll           = pkt.Roll,
            yaw_rate       = pkt.YawRate,
            pitch_rate     = pkt.PitchRate,
            roll_rate      = pkt.RollRate,
            num_satellites = pkt.NumSatellites,
            hdop           = pkt.HDOP,
            vdop           = pkt.VDOP,
            e_sigma        = pkt.ESigma,
            n_sigma        = pkt.NSigma,
            u_sigma        = pkt.USigma,
            correction_age = pkt.CorrectionAge,
            station_id     = pkt.StationID,
            last_update    = time.time(),
        )

        with self._lock:
            self._imu_state = imu

        if self.on_imu_update:
            self.on_imu_update(imu)
