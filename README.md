# nav-960-interfacing

Python tool to interface with a **Trimble NAV-960** GNSS receiver over serial, parse its NMEA 0183 output, and convert position data into multiple coordinate frames useful for robotics, surveying, and navigation.

---

## Table of Contents

- [What this repo does](#what-this-repo-does)
- [Environment setup](#environment-setup)
- [Quick start](#quick-start)
- [CLI reference](#cli-reference)
- [Output fields](#output-fields)
- [Coordinate frames](#coordinate-frames)
- [Module overview](#module-overview)

---

## What this repo does

The NAV-960 outputs **NMEA 0183** sentences over a serial (RS-232 / USB-serial) connection at 38400 baud. This tool:

- Reads those sentences in a background thread via `pyserial`
- Parses three sentence types:
  | Sentence | Contains |
  |----------|----------|
  | **GGA** | Latitude, longitude, altitude (MSL), fix quality, satellite count, HDOP |
  | **GST** | 1-σ position error standard deviations in latitude, longitude, and altitude |
  | **VTG** | Course Over Ground (COG) and Speed Over Ground (SOG) |
- Converts the position into **ECEF** (Earth-Centred Earth-Fixed) and **ENU** (East-North-Up) local frames
- Converts the horizontal velocity from **NED** into the **ECEF** velocity vector
- Fires a callback with a `NAVState` object every time a full update cycle completes
- Supports a **demo mode** that runs entirely offline using built-in sample sentences — no hardware required

---

## Environment setup

### 1. Create a virtual environment

```powershell
python -m venv .venv
```

### 2. Activate it

```powershell
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

`requirements.txt` currently requires:

```
pyserial>=3.5
```

---

## Quick start

### Find your COM port

```powershell
python main.py --list-ports
```

Example output:

```
Device       Description                              HWID
--------------------------------------------------------------------------------
COM7         USB Serial Port                          USB VID:PID=...
```

### Run the live parser

Connect the NAV-960, then:

```powershell
python main.py --port COM7 --baud 38400
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

### Run offline demo (no hardware required)

```powershell
python main.py --demo
```

Parses three real sentences logged from a NAV-960 and prints the full state.

### Fix the ENU reference origin (survey point)

By default, the first valid GGA fix becomes the ENU origin (0, 0, 0). To lock the origin to a known survey point instead:

```powershell
python main.py --port COM7 --baud 38400 --ref-lat -43.5452608 --ref-lon 172.5922080 --ref-alt 32.791
```

All subsequent ENU positions are reported as metres East / North / Up from that fixed point.

---

## CLI reference

| Argument | Default | Description |
|---|---|---|
| `--port PORT` | `COM7` | Serial port name (e.g. `COM3`, `/dev/ttyUSB0`) |
| `--baud BAUD` | `38400` | Serial baud rate |
| `--list-ports` | — | List available serial ports and exit |
| `--demo` | — | Parse built-in sample sentences without hardware |
| `--ref-lat DEG` | *(auto)* | ENU reference latitude in decimal degrees |
| `--ref-lon DEG` | *(auto)* | ENU reference longitude in decimal degrees |
| `--ref-alt M` | *(auto)* | ENU reference altitude in metres MSL |

---

## Output fields

Every update fires a callback with a `NAVState` dataclass containing:

| Field | Unit | Source | Description |
|---|---|---|---|
| `latitude` / `longitude` | ° | GGA | WGS-84 geodetic position |
| `altitude` | m MSL | GGA | Altitude above mean sea level |
| `x` / `y` / `z` | m | computed | ECEF Cartesian position |
| `enu_e` / `enu_n` / `enu_u` | m | computed | East / North / Up from reference origin |
| `vNorth` / `vEast` | m/s | VTG | Horizontal NED velocity |
| `vDown` | m/s | — | Always `0.0` (NMEA carries no vertical velocity) |
| `x_dot` / `y_dot` / `z_dot` | m/s | computed | ECEF velocity vector |
| `fix_quality` | code | GGA | 0=No fix, 1=Autonomous, 2=DGPS, 4=RTK Fixed, 5=RTK Float |
| `num_satellites` | count | GGA | Satellites used in solution |
| `hdop` | — | GGA | Horizontal dilution of precision |
| `sigma_lat` / `sigma_lon` / `sigma_alt` | m | GST | 1-σ position error standard deviations |
| `course_true` | ° | VTG | Course Over Ground from true North |
| `speed_ms` | m/s | VTG | Speed Over Ground |

---

## Coordinate frames

| Frame | Axes | Use case |
|---|---|---|
| **Geodetic (WGS-84)** | lat / lon / alt | Direct receiver output |
| **ECEF** | x, y, z | Global Cartesian; sensor fusion with IMUs |
| **ENU** | East, North, Up | Local navigation, robotics, mapping |
| **NED** | North, East, Down | Velocity from VTG; aviation convention |

The ENU origin is either set automatically to the first valid fix or pinned to a survey point via `--ref-lat / --ref-lon / --ref-alt`.

---

## Module overview

| File | Purpose |
|---|---|
| [main.py](main.py) | CLI entry point; live serial loop, demo mode, pretty-printer |
| [nav960_parser.py](nav960_parser.py) | NMEA parser, coordinate conversions, `NAV960Parser` class, `NAVState` dataclass |
| [requirements.txt](requirements.txt) | Python dependencies (`pyserial`) |

