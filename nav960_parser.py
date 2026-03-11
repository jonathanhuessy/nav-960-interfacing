"""
nav960_parser.py  --  NMEA 0183 parser for the Trimble NAV-960

==========================================================================
NMEA 0183 Primer
==========================================================================
NMEA 0183 is a plain-text serial protocol used by virtually all GNSS
receivers.  Every sentence is a single line of ASCII that looks like:

    $GNGGA,123519.00,4807.0380,N,01131.0000,E,4,12,0.8,545.4,M,46.9,M,,*5A

Structure
---------
    $          Start delimiter
    GN         Talker ID  (GP = GPS-only, GN = multi-constellation,
                           GL = GLONASS, GA = Galileo …)
    GGA        Sentence type  <-- the part we care about
    ,…,…       Comma-separated data fields
    *5A        Asterisk + 2-hex-digit XOR checksum
    <CR><LF>   End of sentence

Sentence types parsed here
--------------------------
    GGA   Fix data:           latitude, longitude, altitude, fix quality,
                              satellite count, HDOP
    GST   Error statistics:   1-sigma standard deviations of position error
                              (sigmas) in latitude, longitude, altitude
    VTG   Track/speed:        Course Over Ground (COG, degrees true North)
                              and Speed Over Ground (SOG)

          NOTE: "COG" stands for *Course Over Ground* – the direction the
          receiver is actually moving across the Earth's surface.  It is
          NOT "center of gravity".

Coordinate frames
-----------------
    Geodetic  – WGS-84 latitude (°), longitude (°), altitude MSL (m)

    ECEF      – Earth-Centred, Earth-Fixed Cartesian
                  x  points toward (lat=0°, lon=0°)   prime meridian/equator
                  y  points toward (lat=0°, lon=90°E)
                  z  points toward the geographic North Pole

    ENU       – East-North-Up local tangent plane at a user-defined reference
                  origin (lat0, lon0, alt0).  This is the recommended local
                  frame for ground-based robotics, surveying, and mapping.
                  E > 0  →  East  of the reference origin
                  N > 0  →  North of the reference origin
                  U > 0  →  above  the reference origin
                  The origin defaults to the first valid GGA fix received, or
                  can be set explicitly via NAV960Parser.set_reference().

    NED       – North-East-Down local tangent plane at the current position
                  vNorth > 0  →  moving toward geographic North
                  vEast  > 0  →  moving toward geographic East
                  vDown  > 0  →  descending

Velocity note
-------------
    Standard NMEA provides *horizontal* velocity only (from VTG).
    vDown is set to 0.0 unless you update it from another source
    (e.g. an IMU or differencing consecutive altitude readings).
"""

import copy
import math
import threading
import time
from dataclasses import dataclass
from typing import Callable, Optional

import serial

# ---------------------------------------------------------------------------
# WGS-84 ellipsoid constants
# ---------------------------------------------------------------------------
_WGS84_A  = 6_378_137.0        # semi-major axis, metres
_WGS84_E2 = 0.00669437999014   # first eccentricity squared (e²)


# ===========================================================================
# Data containers
# ===========================================================================

@dataclass
class GGAData:
    """
    Parsed GGA sentence – GPS Fix Data.

    fix_quality codes
    -----------------
    0  No fix / invalid
    1  Autonomous GPS fix
    2  Differential GPS (DGPS)
    4  RTK Fixed   (centimetre-level accuracy)
    5  RTK Float   (decimetre-level accuracy)
    6  Dead reckoning
    """
    utc_time:         str
    latitude:         Optional[float]   # decimal degrees, positive = North
    longitude:        Optional[float]   # decimal degrees, positive = East
    altitude_msl:     Optional[float]   # metres above mean sea level
    fix_quality:      int               # see codes above
    num_satellites:   int
    hdop:             Optional[float]   # horizontal dilution of precision
    geoid_separation: Optional[float]   # metres (geoid height − ellipsoid height)


@dataclass
class GSTData:
    """
    Parsed GST sentence – GNSS Pseudorange Error Statistics.

    All sigma_* values are 1-sigma (1-σ) standard deviations in metres.
    A smaller value means higher positional confidence.
    """
    utc_time:      str
    rms_residuals: Optional[float]   # RMS of pseudorange residuals, m
    semi_major:    Optional[float]   # std-dev of error-ellipse semi-major axis, m
    semi_minor:    Optional[float]   # std-dev of error-ellipse semi-minor axis, m
    orientation:   Optional[float]   # orientation of error ellipse, deg from true North
    sigma_lat:     Optional[float]   # std-dev of latitude  error, m
    sigma_lon:     Optional[float]   # std-dev of longitude error, m
    sigma_alt:     Optional[float]   # std-dev of altitude  error, m


@dataclass
class VTGData:
    """
    Parsed VTG sentence – Track Made Good and Ground Speed.

    course_true    : Course Over Ground (COG), degrees clockwise from true North
    speed_ms       : Speed Over Ground (SOG) in m/s
    velocity_north : North component of SOG (positive = northward), m/s
    velocity_east  : East  component of SOG (positive = eastward),  m/s
    """
    course_true:     Optional[float]   # degrees 0–360
    course_magnetic: Optional[float]   # degrees
    speed_knots:     Optional[float]
    speed_kmh:       Optional[float]
    speed_ms:        Optional[float]   # derived: speed_kmh / 3.6
    velocity_north:  Optional[float]   # m/s
    velocity_east:   Optional[float]   # m/s


@dataclass
class NAVState:
    """
    Combined navigation state, updated as each sentence arrives.

    Position
    --------
    Geodetic (lat/lon/alt) is what the receiver reports directly.
    ECEF (x, y, z) is computed from lat/lon/alt via WGS-84 conversion.

    Velocity
    --------
    NED (vNorth, vEast, vDown) is the natural output of VTG.
    ECEF (x_dot, y_dot, z_dot) is the NED velocity rotated into ECEF.
    vDown is always 0.0 – NMEA VTG does not carry vertical velocity.

    Quality / Sigmas
    ----------------
    fix_quality, num_satellites, hdop  →  from GGA
    sigma_lat, sigma_lon, sigma_alt    →  from GST  (1-σ, metres)
    """

    # Geodetic position
    latitude:    Optional[float] = None   # degrees
    longitude:   Optional[float] = None   # degrees
    altitude:    Optional[float] = None   # metres MSL

    # ECEF Cartesian position  (x, y, z)  metres
    x: Optional[float] = None
    y: Optional[float] = None
    z: Optional[float] = None

    # NED velocity  (vNorth, vEast, vDown)  m/s
    vNorth: Optional[float] = None
    vEast:  Optional[float] = None
    vDown:  float           = 0.0    # always 0 – NMEA has no vertical velocity

    # ECEF velocity  (x_dot, y_dot, z_dot)  m/s
    x_dot: Optional[float] = None
    y_dot: Optional[float] = None
    z_dot: Optional[float] = None

    # Quality metadata  (from GGA)
    fix_quality:    Optional[int]   = None
    num_satellites: Optional[int]   = None
    hdop:           Optional[float] = None

    # Position error sigmas  (from GST)  1-σ, metres
    sigma_lat: Optional[float] = None
    sigma_lon: Optional[float] = None
    sigma_alt: Optional[float] = None

    # ENU local position relative to reference origin  (metres)
    # East > 0 = east of origin, North > 0 = north of origin, Up > 0 = above origin
    enu_e: Optional[float] = None
    enu_n: Optional[float] = None
    enu_u: Optional[float] = None

    # Reference origin used for ENU (set once, then fixed)
    ref_latitude:  Optional[float] = None
    ref_longitude: Optional[float] = None
    ref_altitude:  Optional[float] = None

    # Course and speed
    course_true: Optional[float] = None   # degrees from true North
    speed_ms:    Optional[float] = None   # m/s

    # Wall-clock time of the most recent update
    last_update: Optional[float] = None   # time.time()


# Human-readable labels for the GGA fix_quality field
FIX_QUALITY_LABELS = {
    0: "No fix",
    1: "Autonomous GPS",
    2: "Differential GPS (DGPS)",
    4: "RTK Fixed",
    5: "RTK Float",
    6: "Dead reckoning",
}


# ===========================================================================
# Coordinate conversion helpers
# ===========================================================================

def lla_to_ecef(lat_deg: float, lon_deg: float, alt_m: float):
    """
    Convert WGS-84 geodetic coordinates to ECEF Cartesian.

    Parameters
    ----------
    lat_deg : geodetic latitude,  degrees  (positive = North)
    lon_deg : geodetic longitude, degrees  (positive = East)
    alt_m   : altitude above the WGS-84 ellipsoid, metres
              (MSL altitude from GGA is close but not identical – the
               difference is the geoid undulation, typically < 100 m)

    Returns
    -------
    (x, y, z) in metres
    """
    lat = math.radians(lat_deg)
    lon = math.radians(lon_deg)
    sin_lat, cos_lat = math.sin(lat), math.cos(lat)
    sin_lon, cos_lon = math.sin(lon), math.cos(lon)

    # Radius of curvature in the prime vertical
    N = _WGS84_A / math.sqrt(1.0 - _WGS84_E2 * sin_lat ** 2)

    x = (N + alt_m) * cos_lat * cos_lon
    y = (N + alt_m) * cos_lat * sin_lon
    z = (N * (1.0 - _WGS84_E2) + alt_m) * sin_lat
    return x, y, z


def ecef_to_enu(
    x: float, y: float, z: float,
    x0: float, y0: float, z0: float,
    lat0_deg: float, lon0_deg: float,
):
    """
    Convert an ECEF position (x, y, z) to ENU coordinates relative to a
    reference point (x0, y0, z0) with geodetic coordinates (lat0, lon0).

    The rotation from ECEF difference vector to ENU is:

        [ e ]   [ -sin(λ0)          cos(λ0)         0       ] [ dx ]
        [ n ] = [ -sin(φ0)cos(λ0)  -sin(φ0)sin(λ0)  cos(φ0) ] [ dy ]
        [ u ]   [  cos(φ0)cos(λ0)   cos(φ0)sin(λ0)  sin(φ0) ] [ dz ]

    where φ0 = reference latitude, λ0 = reference longitude.

    Parameters
    ----------
    x, y, z     : ECEF position of the point, metres
    x0, y0, z0  : ECEF position of the reference origin, metres
    lat0_deg    : geodetic latitude  of the reference origin, degrees
    lon0_deg    : geodetic longitude of the reference origin, degrees

    Returns
    -------
    (e, n, u) in metres
    """
    dx = x - x0
    dy = y - y0
    dz = z - z0

    lat0 = math.radians(lat0_deg)
    lon0 = math.radians(lon0_deg)
    sl, cl = math.sin(lat0), math.cos(lat0)
    so, co = math.sin(lon0), math.cos(lon0)

    e =  -so * dx         + co * dy
    n =  -sl * co * dx    - sl * so * dy  + cl * dz
    u =   cl * co * dx    + cl * so * dy  + sl * dz
    return e, n, u


def ned_to_ecef_velocity(
    lat_deg: float, lon_deg: float,
    vn: float, ve: float, vd: float,
):
    """
    Rotate a velocity vector from the local NED frame into ECEF.

    The rotation matrix  R_ECEF_from_NED  (columns = North, East, Down unit
    vectors expressed in ECEF) is:

        R = [ -sin(φ)cos(λ)   -sin(λ)   -cos(φ)cos(λ) ]
            [ -sin(φ)sin(λ)    cos(λ)   -cos(φ)sin(λ) ]
            [  cos(φ)          0        -sin(φ)        ]

    where φ = latitude, λ = longitude.

    Parameters
    ----------
    vn, ve, vd : velocity components in the NED frame (m/s)

    Returns
    -------
    (x_dot, y_dot, z_dot) in m/s, ECEF frame
    """
    lat = math.radians(lat_deg)
    lon = math.radians(lon_deg)
    sl, cl = math.sin(lat), math.cos(lat)   # sin/cos latitude
    so, co = math.sin(lon), math.cos(lon)   # sin/cos longitude

    x_dot = -sl * co * vn  -  so * ve  -  cl * co * vd
    y_dot = -sl * so * vn  +  co * ve  -  cl * so * vd
    z_dot =  cl      * vn              -  sl      * vd
    return x_dot, y_dot, z_dot


# ===========================================================================
# NMEA sentence utilities
# ===========================================================================

def verify_checksum(sentence: str) -> bool:
    """
    Validate the XOR checksum of an NMEA sentence.

    The checksum byte is the XOR of all characters between '$' and '*'
    (exclusive).  It is transmitted as two hex digits after the '*'.
    """
    try:
        if '*' not in sentence:
            return False
        body, chk_str = sentence.lstrip('$').split('*', 1)
        expected = int(chk_str[:2], 16)
        computed = 0
        for ch in body:
            computed ^= ord(ch)
        return computed == expected
    except (ValueError, IndexError):
        return False


def _split(sentence: str):
    """Strip checksum and split sentence into field list."""
    sentence = sentence.strip()
    if '*' in sentence:
        sentence = sentence[: sentence.index('*')]
    return sentence.lstrip('$').split(',')


def _f(s: str) -> Optional[float]:
    """Parse a float field, returning None if empty or invalid."""
    try:
        return float(s) if s else None
    except ValueError:
        return None


def _i(s: str) -> Optional[int]:
    """Parse an int field, returning None if empty or invalid."""
    try:
        return int(s) if s else None
    except ValueError:
        return None


def _nmea_coord(raw: str, direction: str) -> Optional[float]:
    """
    Convert an NMEA lat/lon field to signed decimal degrees.

    NMEA encodes coordinates in DDDMM.MMMM format (degrees + minutes).
    Latitude  uses 2-digit degrees  (DDMM.MMMM).
    Longitude uses 3-digit degrees  (DDDMM.MMMM).

    'S' and 'W' directions yield negative decimal-degree values.
    """
    if not raw:
        return None
    dot = raw.index('.')
    degrees = float(raw[: dot - 2])
    minutes = float(raw[dot - 2 :])
    decimal = degrees + minutes / 60.0
    if direction in ('S', 'W'):
        decimal = -decimal
    return decimal


# ===========================================================================
# Individual sentence parsers
# ===========================================================================

def parse_gga(sentence: str) -> Optional[GGAData]:
    """
    Parse a GGA sentence and return a GGAData object, or None on failure.

    Expected field layout (0-indexed after stripping '$'):
      0   Sentence ID       e.g. GNGGA or GPGGA
      1   UTC time          HHMMSS.ss
      2   Latitude          DDMM.MMMM
      3   N/S indicator
      4   Longitude         DDDMM.MMMM
      5   E/W indicator
      6   Fix quality       0–6
      7   Satellites used
      8   HDOP
      9   Altitude          metres (MSL)
     10   'M'
     11   Geoid separation  metres
     12   'M'
     13   Age of diff correction
     14   Diff ref station ID  (checksum is on this field)

    Example:
      $GNGGA,123519.00,4807.0380,N,01131.0000,E,4,12,0.8,545.4,M,46.9,M,,*5A
    """
    if not verify_checksum(sentence):
        return None
    f = _split(sentence)
    if len(f) < 10 or not f[0].endswith('GGA'):
        return None

    return GGAData(
        utc_time         = f[1],
        latitude         = _nmea_coord(f[2], f[3]),
        longitude        = _nmea_coord(f[4], f[5]),
        altitude_msl     = _f(f[9]),
        fix_quality      = _i(f[6]) or 0,
        num_satellites   = _i(f[7]) or 0,
        hdop             = _f(f[8]),
        geoid_separation = _f(f[11]) if len(f) > 11 else None,
    )


def parse_gst(sentence: str) -> Optional[GSTData]:
    """
    Parse a GST sentence and return a GSTData object, or None on failure.

    Expected field layout:
      0   Sentence ID
      1   UTC time
      2   RMS value of pseudorange residuals, m
      3   Std-dev of semi-major axis of error ellipse, m
      4   Std-dev of semi-minor axis of error ellipse, m
      5   Orientation of error ellipse semi-major axis, deg from true North
      6   Std-dev of latitude  error, m
      7   Std-dev of longitude error, m
      8   Std-dev of altitude  error, m

    Example:
      $GNGST,172814.00,0.006,0.006,0.004,179.6,0.006,0.006,0.01*6F
    """
    if not verify_checksum(sentence):
        return None
    f = _split(sentence)
    if len(f) < 8 or not f[0].endswith('GST'):
        return None

    return GSTData(
        utc_time      = f[1],
        rms_residuals = _f(f[2]),
        semi_major    = _f(f[3]),
        semi_minor    = _f(f[4]),
        orientation   = _f(f[5]),
        sigma_lat     = _f(f[6]),
        sigma_lon     = _f(f[7]),
        sigma_alt     = _f(f[8]) if len(f) > 8 else None,
    )


def parse_vtg(sentence: str) -> Optional[VTGData]:
    """
    Parse a VTG sentence and return a VTGData object, or None on failure.

    Expected field layout:
      0   Sentence ID
      1   Course over ground, true (degrees)
      2   'T'
      3   Course over ground, magnetic (degrees)
      4   'M'
      5   Speed over ground, knots
      6   'N'
      7   Speed over ground, km/h
      8   'K'
      9   Mode indicator (A=autonomous, D=differential, E=estimated, N=invalid)

    Example:
      $GNVTG,054.7,T,034.4,M,005.5,N,010.2,K,A*27

    The velocity components (velocity_north, velocity_east) are derived by
    decomposing SOG along the COG direction:
        vNorth = SOG * cos(COG)
        vEast  = SOG * sin(COG)
    """
    if not verify_checksum(sentence):
        return None
    f = _split(sentence)
    if len(f) < 8 or not f[0].endswith('VTG'):
        return None

    course   = _f(f[1])
    speed_kmh = _f(f[7])
    speed_ms  = speed_kmh / 3.6 if speed_kmh is not None else None

    vn = ve = None
    if course is not None and speed_ms is not None:
        heading_rad = math.radians(course)
        vn = speed_ms * math.cos(heading_rad)
        ve = speed_ms * math.sin(heading_rad)

    return VTGData(
        course_true     = course,
        course_magnetic = _f(f[3]),
        speed_knots     = _f(f[5]),
        speed_kmh       = speed_kmh,
        speed_ms        = speed_ms,
        velocity_north  = vn,
        velocity_east   = ve,
    )


# ===========================================================================
# High-level parser with serial port management
# ===========================================================================

class NAV960Parser:
    """
    Reads NMEA sentences from the NAV-960 over a serial (USB-COM) port and
    maintains a continuously updated NAVState.

    Background reading runs in a daemon thread so it does not block your
    application.

    Quick start
    -----------
        # ENU origin auto-set to first valid fix:
        parser = NAV960Parser(port='COM3', baudrate=38400)
        parser.start()

        while True:
            state = parser.state
            print(state.enu_e, state.enu_n, state.enu_u)   # local ENU, metres
            print(state.x_dot, state.y_dot, state.z_dot)   # ECEF velocity, m/s
            time.sleep(1)

        parser.stop()

    Fixed reference origin
    ----------------------
        parser = NAV960Parser('COM3', baudrate=38400)
        parser.set_reference(lat=-43.5452608, lon=172.5922080, alt=32.791)
        parser.start()

    Callback variant
    ----------------
        def on_update(state: NAVState):
            print(f"E={state.enu_e:.3f}  N={state.enu_n:.3f}  U={state.enu_u:.3f}")

        parser = NAV960Parser('COM3', on_update=on_update)
        parser.start()

    Finding your COM port
    ---------------------
    On Windows, open Device Manager → Ports (COM & LPT).  The engineering
    cable will show up as "USB Serial Port (COMx)".  Alternatively run:

        python main.py --list-ports

    NAV-960 serial settings: 38400 baud, 8N1, no flow control.
    """

    def __init__(
        self,
        port: str,
        baudrate: int = 38400,
        timeout: float = 1.0,
        on_update: Optional[Callable[["NAVState"], None]] = None,
    ):
        self.port      = port
        self.baudrate  = baudrate
        self.timeout   = timeout
        self.on_update = on_update

        self._state        = NAVState()
        self._lock         = threading.Lock()
        self._thread       = None
        self._running      = False
        self._ref_set      = False   # True once a reference origin is locked in

    # ------------------------------------------------------------------
    # Reference origin for ENU
    # ------------------------------------------------------------------

    def set_reference(self, lat: float, lon: float, alt: float):
        """
        Explicitly set the ENU reference origin.

        Call this before start() if you have a known survey point.
        If not called, the first valid GGA fix is used automatically.

        Parameters
        ----------
        lat : geodetic latitude,  decimal degrees (positive = North)
        lon : geodetic longitude, decimal degrees (positive = East)
        alt : altitude MSL, metres
        """
        x0, y0, z0 = lla_to_ecef(lat, lon, alt)
        with self._lock:
            s = self._state
            s.ref_latitude  = lat
            s.ref_longitude = lon
            s.ref_altitude  = alt
            self._ref_ecef  = (x0, y0, z0)
            self._ref_set   = True

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    @property
    def state(self) -> NAVState:
        """Return a thread-safe snapshot of the current navigation state."""
        with self._lock:
            return copy.copy(self._state)

    def start(self):
        """Open the serial port and begin reading in the background."""
        self._running = True
        self._thread  = threading.Thread(target=self._read_loop, daemon=True)
        self._thread.start()

    def stop(self):
        """Stop the background thread gracefully."""
        self._running = False
        if self._thread:
            self._thread.join(timeout=3.0)

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    def _read_loop(self):
        try:
            with serial.Serial(
                self.port, self.baudrate, timeout=self.timeout
            ) as ser:
                print(f"[NAV960] Connected: {self.port} @ {self.baudrate} baud")
                while self._running:
                    try:
                        raw      = ser.readline()
                        sentence = raw.decode('ascii', errors='ignore').strip()
                        if sentence.startswith('$'):
                            self._dispatch(sentence)
                    except serial.SerialException as exc:
                        print(f"[NAV960] Serial read error: {exc}")
                        break
        except serial.SerialException as exc:
            print(f"[NAV960] Could not open {self.port}: {exc}")
            print(" → Check the port name, baud rate, and driver installation.")

    def _dispatch(self, sentence: str):
        """Route a raw NMEA sentence to the correct parser."""
        updated = False

        if 'GGA' in sentence:
            data = parse_gga(sentence)
            if data:
                self._apply_gga(data)
                updated = True
        elif 'GST' in sentence:
            data = parse_gst(sentence)
            if data:
                self._apply_gst(data)
                updated = True
        elif 'VTG' in sentence:
            data = parse_vtg(sentence)
            if data:
                self._apply_vtg(data)
                updated = True

        if updated and self.on_update:
            self.on_update(self.state)

    def _apply_gga(self, gga: GGAData):
        with self._lock:
            s = self._state
            s.latitude       = gga.latitude
            s.longitude      = gga.longitude
            s.altitude       = gga.altitude_msl
            s.fix_quality    = gga.fix_quality
            s.num_satellites = gga.num_satellites
            s.hdop           = gga.hdop
            s.last_update    = time.time()

            if None not in (gga.latitude, gga.longitude, gga.altitude_msl):
                s.x, s.y, s.z = lla_to_ecef(
                    gga.latitude, gga.longitude, gga.altitude_msl
                )
                # Auto-set reference origin to first valid fix
                if not self._ref_set:
                    s.ref_latitude  = gga.latitude
                    s.ref_longitude = gga.longitude
                    s.ref_altitude  = gga.altitude_msl
                    self._ref_ecef  = (s.x, s.y, s.z)
                    self._ref_set   = True
                    print(f"[NAV960] ENU origin set: "
                          f"lat={gga.latitude:.8f}  "
                          f"lon={gga.longitude:.8f}  "
                          f"alt={gga.altitude_msl:.3f} m")
                self._refresh_enu(s)
                self._refresh_ecef_velocity(s)

    def _apply_gst(self, gst: GSTData):
        with self._lock:
            s = self._state
            s.sigma_lat   = gst.sigma_lat
            s.sigma_lon   = gst.sigma_lon
            s.sigma_alt   = gst.sigma_alt
            s.last_update = time.time()

    def _apply_vtg(self, vtg: VTGData):
        with self._lock:
            s = self._state
            s.course_true = vtg.course_true
            s.speed_ms    = vtg.speed_ms
            s.vNorth      = vtg.velocity_north
            s.vEast       = vtg.velocity_east
            s.last_update = time.time()
            self._refresh_ecef_velocity(s)

    def _refresh_enu(self, s: NAVState):
        """Recompute ENU position from ECEF whenever a reference is available."""
        if self._ref_set and None not in (s.x, s.y, s.z):
            x0, y0, z0 = self._ref_ecef
            s.enu_e, s.enu_n, s.enu_u = ecef_to_enu(
                s.x, s.y, s.z,
                x0, y0, z0,
                s.ref_latitude, s.ref_longitude,
            )

    @staticmethod
    def _refresh_ecef_velocity(s: NAVState):
        """Recompute ECEF velocity from NED whenever both are available."""
        if None not in (s.latitude, s.longitude, s.vNorth, s.vEast):
            s.x_dot, s.y_dot, s.z_dot = ned_to_ecef_velocity(
                s.latitude, s.longitude, s.vNorth, s.vEast, s.vDown
            )
