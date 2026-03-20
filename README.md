# nav-960-interfacing

Python tool to interface with a **Trimble NAV-960** GNSS/INS receiver over serial. Supports two protocols:

- **NMEA mode** — parses NMEA 0183 sentences for position and velocity (no attitude)
- **TSIP mode** — uses Trimble's binary TSIP protocol to stream roll-corrected position, ENU velocity, attitude (yaw / pitch / roll), and angular rates from the integrated IMU in a single packet

---

## Table of Contents

- [What this repo does](#what-this-repo-does)
- [Choosing a protocol](#choosing-a-protocol)
- [Environment setup](#environment-setup)
- [Quick start — NMEA mode](#quick-start--nmea-mode)
- [Quick start — TSIP mode](#quick-start--tsip-mode)
- [Configuring the NAV-960 for TSIP](#configuring-the-nav-960-for-tsip)
- [Lever arms](#lever-arms)
- [CLI reference](#cli-reference)
- [Output fields — NMEA mode](#output-fields--nmea-mode)
- [Output fields — TSIP mode](#output-fields--tsip-mode)
- [Using the parser in your own code](#using-the-parser-in-your-own-code)
- [Coordinate frames](#coordinate-frames)
- [Module overview](#module-overview)

---

## What this repo does

The NAV-960 is a precision GNSS/INS receiver. Depending on port configuration it outputs either NMEA or TSIP:

| Protocol | Position | Velocity | Attitude | Angular rates |
|----------|----------|----------|----------|---------------|
| **NMEA** | ✓ | horizontal only | ✗ | ✗ |
| **TSIP** | ✓ roll-corrected | ✓ 3-axis ENU | ✓ yaw/pitch/roll | ✓ deg/s |

This tool handles both modes through the same `NAV960Parser` class — switch protocols with `--protocol nmea` or `--protocol tsip`.

---

## Choosing a protocol

The NAV-960 serial port is configured for **either** NMEA or TSIP at a time — both cannot be active on the same port simultaneously. Use the receiver's configuration software (e.g. Trimble TerraSync or the web interface) to set the port to TSIP output before using TSIP mode.

Use **NMEA mode** when you only need position and speed, or when the receiver is already configured for NMEA.

Use **TSIP mode** when you need:
- Attitude (yaw, pitch, roll)
- Angular rates (yaw rate, pitch rate, roll rate)
- Roll-corrected position (IMU aiding)
- Vertical velocity

---

## Environment setup

### 1. Create and activate a virtual environment

```powershell
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

```bash
# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

The only external dependency is `pyserial`. The `py_tsip` library is bundled locally in `./py_tsip/` and requires no separate installation.

---

## Quick start — NMEA mode

### Find your COM port

```powershell
python main.py --list-ports
```

### Run the live NMEA parser

```powershell
python main.py --port COM7
```

The console prints a navigation state block on every update:

```
┌─── NAV-960 Update ───────────────────────────────────────────┐
│  Fix Quality  : Differential GPS (DGPS) (code 2)
│  Satellites   : 32   HDOP: 0.50
│  Position (Geodetic / WGS-84):
│    Latitude   : -43.54526080 °
│    Longitude  : 172.59224720 °
│    Altitude   : 32.791 m  (MSL)
│  Position (ENU local) — East, North, Up relative to origin:
│    E (east)   : 0.0000 m
│    N (north)  : 0.0000 m
│    U (up)     : 0.0000 m
...
└──────────────────────────────────────────────────────────────┘
```

### Fix the ENU reference origin (survey point)

By default the first valid fix becomes the ENU origin. To pin it to a known survey point:

```powershell
python main.py --port COM7 --ref-lat -43.5452608 --ref-lon 172.5922080 --ref-alt 32.791
```

### Run the offline demo (no hardware required)

```powershell
python main.py --demo
```

Parses hardcoded sentences and a synthetic TSIP fixture, printing both output blocks.

---

## Quick start — TSIP mode

> **Prerequisite:** The NAV-960 port must be configured for TSIP output. See [Configuring the NAV-960 for TSIP](#configuring-the-nav-960-for-tsip).

### Basic TSIP run

```powershell
python main.py --port COM7 --protocol tsip
```

On startup the tool:
1. Opens the port and waits for the TSIP connection handshake (baud-rate auto-negotiated by the `py_tsip` library, typically takes a few seconds)
2. Sends `8E A9 17 00` to write the lever-arm and IMU orientation configuration
3. Sends `8E A9 17 01` to enable IMU-corrected positions and the detail stream
4. Prints a TSIP state block on every `8F A9 17 02` packet received:

```
┌─── NAV-960 TSIP Update ──────────────────────────────────────────┐
│  Attitude:
│    Yaw        : 92.345 °
│    Pitch      : -1.230 °
│    Roll       :  0.456 °
│
│  Angular rates:
│    Yaw rate   :  0.0120 °/s
│    Pitch rate : -0.0030 °/s
│    Roll rate  :  0.0010 °/s
│
│  Position (roll-corrected, WGS-84 ellipsoid):
│    Latitude   : -43.54526308 °
│    Longitude  : 172.59219800 °
│    Height     : 21.550 m  (ellipsoid)
│
│  ENU velocity  [m/s]:
│    East  (E)  :  0.0120 m/s
│    North (N)  : -0.0050 m/s
│    Up    (U)  :  0.0010 m/s
│
│  Solution quality:
│    Satellites : 32
│    HDOP       : 0.50   VDOP: 0.80
│    σ_E        : 0.006 m   σ_N: 0.006 m   σ_U: 0.010 m
└──────────────────────────────────────────────────────────────────┘
```

### TSIP with lever arms

If the GNSS antenna is not co-located with the IMU reference point, provide the offsets (metres, body frame):

```powershell
python main.py --port COM7 --protocol tsip --lever-arm-x 0.5 --lever-arm-y 0.0 --lever-arm-z -0.2
```

See [Lever arms](#lever-arms) for a full explanation.

---

## Configuring the NAV-960 for TSIP

The NAV-960 serial port must be set to TSIP output before running in TSIP mode. Depending on your firmware version, use one of:

- **Trimble Toolbox / Connected Community portal** — Port Settings → Output Format → TSIP
- **Trimble AgGPS / Precision-IQ display** — System → GPS Receiver → Port → Protocol: TSIP
- **Web interface** (if fitted) — I/O → Port 1 → Output: TSIP

Set the baud rate to `115200` for TSIP (the `py_tsip` library negotiates the rate automatically via a serial break sequence, so `--baud` is not used in TSIP mode).

To switch back to NMEA, set the port back to `NMEA` output in the same menu.

---

## Lever arms

The **antenna lever arm** (`AntLevX / Y / Z`) is the vector from the IMU body reference point to the GNSS antenna phase centre, expressed in the vehicle body frame:

- **X** — forward/backward (positive = forward)
- **Y** — left/right (positive = right)
- **Z** — up/down (positive = up)

If the antenna and IMU are co-located, leave all lever arms at `0.0` (default).

If the values are already stored in the receiver's non-volatile memory, sending `0.0` will overwrite them — use `--lever-arm-x/y/z` to send the correct values on every connection, or read the stored values first with a `8E A9 17 00` request (not yet automated in this tool; the stored ACK is logged at startup).

The additional IMU orientation fields (`ImuAngleRoll / Pitch / Yaw`, `ImuLevX / Y / Z`, `ImuRollOffset / PitchOffset`) default to `0.0`. If your IMU is mounted at a non-standard orientation, pass a dict to `NAV960TSIPClient(imu_orientation={...})` in your own code.

---

## CLI reference

| Argument | Default | Mode | Description |
|---|---|---|---|
| `--port PORT` | `COM7` | both | Serial port name (`COM3`, `/dev/ttyUSB0`, …) |
| `--baud BAUD` | `38400` | NMEA | Serial baud rate (TSIP auto-negotiates) |
| `--protocol` | `nmea` | — | `nmea` or `tsip` |
| `--list-ports` | — | — | List available serial ports and exit |
| `--demo` | — | — | Run offline demo with sample data, no hardware |
| `--ref-lat DEG` | *(auto)* | NMEA | ENU reference latitude, decimal degrees |
| `--ref-lon DEG` | *(auto)* | NMEA | ENU reference longitude, decimal degrees |
| `--ref-alt M` | *(auto)* | NMEA | ENU reference altitude, metres MSL |
| `--lever-arm-x M` | `0.0` | TSIP | Antenna lever arm X, metres (body frame) |
| `--lever-arm-y M` | `0.0` | TSIP | Antenna lever arm Y, metres (body frame) |
| `--lever-arm-z M` | `0.0` | TSIP | Antenna lever arm Z, metres (body frame) |

---

## Output fields — NMEA mode

Every NMEA update fires a callback with a `NAVState` dataclass:

| Field | Unit | Source | Description |
|---|---|---|---|
| `latitude` / `longitude` | ° | GGA | WGS-84 geodetic position |
| `altitude` | m MSL | GGA | Altitude above mean sea level |
| `x` / `y` / `z` | m | computed | ECEF Cartesian position |
| `enu_e` / `enu_n` / `enu_u` | m | computed | East / North / Up from reference origin |
| `vNorth` / `vEast` | m/s | VTG | Horizontal NED velocity |
| `vDown` | m/s | — | Always `0.0` — NMEA carries no vertical velocity |
| `x_dot` / `y_dot` / `z_dot` | m/s | computed | ECEF velocity vector |
| `fix_quality` | code | GGA | 0=No fix, 1=Autonomous, 2=DGPS, 4=RTK Fixed, 5=RTK Float |
| `num_satellites` | count | GGA | Satellites used in solution |
| `hdop` | — | GGA | Horizontal dilution of precision |
| `sigma_lat` / `sigma_lon` / `sigma_alt` | m | GST | 1-σ position error standard deviations |
| `course_true` | ° | VTG | Course Over Ground from true North |
| `speed_ms` | m/s | VTG | Speed Over Ground |

---

## Output fields — TSIP mode

Every `8F A9 17 02` packet fires a callback with an `IMUState` dataclass. The same fields are also mirrored into `NAVState` (position and velocity) so existing code that reads `parser.state` keeps working.

### Attitude

| Field | Unit | Description |
|---|---|---|
| `yaw` | ° | Heading from true North (0–360) |
| `pitch` | ° | Nose-up positive |
| `roll` | ° | Right-side-down positive |
| `yaw_rate` | °/s | Rate of change of yaw |
| `pitch_rate` | °/s | Rate of change of pitch |
| `roll_rate` | °/s | Rate of change of roll |

### Position

| Field | Unit | Description |
|---|---|---|
| `latitude` / `longitude` | ° | Roll-corrected WGS-84 geodetic position |
| `height` | m | Height above WGS-84 ellipsoid (not MSL) |
| `lat_original` / `lon_original` | ° | Antenna (uncorrected) geodetic position |
| `height_original` | m | Antenna height above WGS-84 ellipsoid |

> **MSL vs ellipsoid height:** TSIP reports height above the WGS-84 ellipsoid; NMEA GGA reports altitude above mean sea level. The difference is the geoid undulation (typically 10–60 m depending on location). Use a geoid model (e.g. EGM2008) to convert if you need MSL in TSIP mode.

### Velocity

| Field | Unit | Description |
|---|---|---|
| `e_vel` | m/s | East velocity (ENU frame) |
| `n_vel` | m/s | North velocity (ENU frame) |
| `u_vel` | m/s | Up velocity (ENU frame) |

### Solution quality

| Field | Unit | Description |
|---|---|---|
| `gps_seconds` | s | GPS time of week |
| `num_satellites` | count | Satellites used |
| `hdop` / `vdop` | — | Horizontal / vertical dilution of precision |
| `e_sigma` / `n_sigma` / `u_sigma` | m | 1-σ ENU position error |
| `correction_age` | s | Age of differential correction |
| `imu_status` | bitmask | IMU health flags (device-specific) |
| `position_type` | code | Solution type (same codes as `fix_quality`) |
| `station_id` | — | Differential reference station ID |

---

## Using the parser in your own code

### NMEA mode

```python
from nav960_parser import NAV960Parser, NAVState

def on_update(state: NAVState):
    print(f"Lat={state.latitude:.8f}  Lon={state.longitude:.8f}  "
          f"Alt={state.altitude:.3f} m")

parser = NAV960Parser(port="COM7", baudrate=38400, on_update=on_update)
parser.set_reference(lat=-43.5452608, lon=172.5922080, alt=32.791)  # optional
parser.start()

# ... your application loop ...

parser.stop()
```

### TSIP mode

```python
from nav960_parser import NAV960Parser, NAVState
from tsip_parser import IMUState

def on_update(state: NAVState):
    # Position and velocity are mirrored from TSIP into NAVState
    print(f"Lat={state.latitude:.8f}  vN={state.vNorth:.4f} m/s")

def on_imu_update(imu: IMUState):
    print(f"Yaw={imu.yaw:.2f}°  Pitch={imu.pitch:.2f}°  Roll={imu.roll:.2f}°")
    print(f"Yaw rate={imu.yaw_rate:.4f} °/s")

parser = NAV960Parser(
    port          = "COM7",
    protocol      = "tsip",
    lever_arm_x   = 0.5,    # metres, body frame
    lever_arm_y   = 0.0,
    lever_arm_z   = -0.2,
    on_update     = on_update,
    on_imu_update = on_imu_update,
)
parser.start()   # blocks until TSIP connection handshake completes

# ... your application loop ...

parser.stop()
```

### Using NAV960TSIPClient directly

For applications that only need TSIP and don't use the NMEA path at all:

```python
from tsip_parser import NAV960TSIPClient, IMUState

def on_imu(imu: IMUState):
    print(f"Yaw={imu.yaw:.2f}°  Pitch={imu.pitch:.2f}°  Roll={imu.roll:.2f}°")

client = NAV960TSIPClient(
    port          = "COM7",
    lever_arm_x   = 0.5,
    lever_arm_y   = 0.0,
    lever_arm_z   = -0.2,
    on_imu_update = on_imu,
    connect_timeout = 15.0,
)
client.start()

# Access the latest state at any time (thread-safe):
imu = client.imu_state

client.stop()
```

---

## Coordinate frames

| Frame | Axes | Notes |
|---|---|---|
| **Geodetic (WGS-84)** | lat / lon / alt | Direct receiver output in both modes |
| **ECEF** | x, y, z | Global Cartesian; useful for sensor fusion |
| **ENU** | East, North, Up | Local tangent plane; robotics and mapping |
| **NED** | North, East, Down | NMEA velocity convention; aviation |

The TSIP packet provides ENU velocity directly. The NMEA path provides NED velocity (from VTG) and derives ECEF velocity from it.

The ENU origin is auto-set to the first valid fix in both modes, or can be pinned via `parser.set_reference()` (NMEA) or `--ref-lat / --ref-lon / --ref-alt` (NMEA CLI).

---

## Module overview

| File / folder | Purpose |
|---|---|
| [main.py](main.py) | CLI entry point; live loop, demo mode, display functions for both protocols |
| [nav960_parser.py](nav960_parser.py) | `NAV960Parser` class, `NAVState` dataclass, NMEA parsers, coordinate conversions |
| [tsip_parser.py](tsip_parser.py) | `NAV960TSIPClient` class, `IMUState` dataclass, startup config commands |
| `py_tsip/` | Bundled Trimble TSIP library — handles serial I/O, DLE framing, packet encoding/decoding (no installation required) |
| [requirements.txt](requirements.txt) | Python dependencies (`pyserial`) |
| `test_py_tsip/` | Original py_tsip source received from colleague; kept for reference |

