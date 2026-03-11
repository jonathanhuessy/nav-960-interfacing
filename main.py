"""
main.py  --  Entry point for the Trimble NAV-960 NMEA parser

Usage
-----
    # Install dependency first (once):
    pip install -r requirements.txt

    # List available serial ports to find your COM port:
    python main.py --list-ports

    # Run the live parser (replace COM3 with your actual port):
    python main.py --port COM7 --baud 38400

    # Run offline demo with built-in sample sentences (no hardware needed):
    python main.py --demo

    # Run with a fixed ENU reference origin (survey point):
    python main.py --port COM7 --baud 38400 --ref-lat -43.5452608 --ref-lon 172.5922080 --ref-alt 32.791
"""

import argparse
import time

from nav960_parser import (
    FIX_QUALITY_LABELS,
    NAV960Parser,
    NAVState,
    ecef_to_enu,
    lla_to_ecef,
    ned_to_ecef_velocity,
    parse_gga,
    parse_gst,
    parse_vtg,
)


# ===========================================================================
# Display helper
# ===========================================================================

def _fmt(value, fmt: str, unit: str = "") -> str:
    """Format a numeric value, or return '--' if it is None."""
    if value is None:
        return "--"
    return f"{value:{fmt}}{unit}"


def print_state(state: NAVState):
    """Pretty-print the full navigation state to the console."""
    fix_label = FIX_QUALITY_LABELS.get(state.fix_quality or 0, "Unknown")

    print("\n┌─── NAV-960 Update ───────────────────────────────────────────┐")

    print("│  Fix Quality  :", fix_label, f"(code {state.fix_quality})")
    print("│  Satellites   :", _fmt(state.num_satellites, "d"),
          "  HDOP:", _fmt(state.hdop, ".2f"))

    print("│")
    print("│  Position (Geodetic / WGS-84):")
    print("│    Latitude   :", _fmt(state.latitude,  ".8f", " °"))
    print("│    Longitude  :", _fmt(state.longitude, ".8f", " °"))
    print("│    Altitude   :", _fmt(state.altitude,  ".3f",  " m  (MSL)"))

    print("│")
    print("│  Position (ENU local) — East, North, Up relative to origin:")
    if state.ref_latitude is not None:
        print(f"│    Origin     : lat={state.ref_latitude:.8f}°  "
              f"lon={state.ref_longitude:.8f}°  "
              f"alt={state.ref_altitude:.3f} m")
    else:
        print("│    Origin     : not set (waiting for first fix)")
    print("│    E (east)   :", _fmt(state.enu_e, ".4f", " m"))
    print("│    N (north)  :", _fmt(state.enu_n, ".4f", " m"))
    print("│    U (up)     :", _fmt(state.enu_u, ".4f", " m"))

    print("│")
    print("│  Position (ECEF Cartesian) — x, y, z:")
    print("│    x          :", _fmt(state.x, ".3f", " m"))
    print("│    y          :", _fmt(state.y, ".3f", " m"))
    print("│    z          :", _fmt(state.z, ".3f", " m"))

    print("│")
    print("│  Velocity (NED) — vNorth, vEast, vDown:  [m/s]")
    print("│    vNorth     :", _fmt(state.vNorth, ".4f", " m/s"))
    print("│    vEast      :", _fmt(state.vEast,  ".4f", " m/s"))
    print("│    vDown      : 0.0000 m/s  (NMEA VTG carries no vertical velocity)")

    print("│")
    print("│  Velocity (ECEF) — x_dot, y_dot, z_dot:  [m/s]")
    print("│    x_dot      :", _fmt(state.x_dot, ".4f", " m/s"))
    print("│    y_dot      :", _fmt(state.y_dot, ".4f", " m/s"))
    print("│    z_dot      :", _fmt(state.z_dot, ".4f", " m/s"))

    print("│")
    print("│  Error Sigmas — 1-σ standard deviations  (from GST):")
    print("│    σ_lat      :", _fmt(state.sigma_lat, ".4f", " m"))
    print("│    σ_lon      :", _fmt(state.sigma_lon, ".4f", " m"))
    print("│    σ_alt      :", _fmt(state.sigma_alt, ".4f", " m"))

    print("│")
    print("│  Course Over Ground (COG):", _fmt(state.course_true, ".1f", " °  (true North)"))
    print("│  Speed Over Ground  (SOG):", _fmt(state.speed_ms,    ".3f", " m/s"))

    print("└──────────────────────────────────────────────────────────────┘")


# ===========================================================================
# Callback used in live mode
# ===========================================================================

def on_update(state: NAVState):
    print_state(state)


# ===========================================================================
# Demo mode – parses sample sentences without hardware
# ===========================================================================

# Real sentences logged from the NAV-960 via Teraterm (38400 baud, 8N1).
# These are the actual sentences your device outputs — checksums verified.
SAMPLE_GGA = (
    "$GPGGA,025859.00,4332.711651,S,17235.532483,E,2,32,0.5,32.791,M,11.241,M,4.0,0122*6D"
)
SAMPLE_GST = (
    "$GNGST,123519.00,0.012,0.010,0.007,45.0,0.009,0.011,0.025*7E"
)
SAMPLE_VTG = (
    "$GPVTG,000.0,T,,,000.01,N,000.02,K,D*46"
)


def run_demo():
    print("=" * 66)
    print("  NAV-960 Parser — OFFLINE DEMO (no hardware required)")
    print("=" * 66)

    # --- GGA ---
    print(f"\nSample GGA sentence:\n  {SAMPLE_GGA}")
    gga = parse_gga(SAMPLE_GGA)
    if gga:
        print(f"  UTC time        : {gga.utc_time}")
        print(f"  Latitude        : {gga.latitude:.8f} °")
        print(f"  Longitude       : {gga.longitude:.8f} °")
        print(f"  Altitude (MSL)  : {gga.altitude_msl} m")
        print(f"  Fix quality     : {gga.fix_quality}  "
              f"({FIX_QUALITY_LABELS.get(gga.fix_quality, '?')})")
        print(f"  Satellites      : {gga.num_satellites}")
        print(f"  HDOP            : {gga.hdop}")
        print(f"  Geoid sep.      : {gga.geoid_separation} m")
    else:
        print("  [!] GGA parse failed")

    # --- GST ---
    print(f"\nSample GST sentence:\n  {SAMPLE_GST}")
    gst = parse_gst(SAMPLE_GST)
    if gst:
        print(f"  σ_lat           : {gst.sigma_lat} m  (1-sigma latitude error)")
        print(f"  σ_lon           : {gst.sigma_lon} m  (1-sigma longitude error)")
        print(f"  σ_alt           : {gst.sigma_alt} m  (1-sigma altitude error)")
        print(f"  Error ellipse   : semi-major={gst.semi_major} m, "
              f"semi-minor={gst.semi_minor} m, orient={gst.orientation} °")
    else:
        print("  [!] GST parse failed")

    # --- VTG ---
    print(f"\nSample VTG sentence:\n  {SAMPLE_VTG}")
    vtg = parse_vtg(SAMPLE_VTG)
    if vtg:
        print(f"  Course (true)   : {vtg.course_true} °  (Course Over Ground)")
        print(f"  Course (magnet.): {vtg.course_magnetic} °")
        print(f"  Speed           : {vtg.speed_knots} kn  /  "
              f"{vtg.speed_kmh} km/h  /  {vtg.speed_ms:.4f} m/s")
        print(f"  vNorth          : {vtg.velocity_north:.4f} m/s")
        print(f"  vEast           : {vtg.velocity_east:.4f} m/s")
    else:
        print("  [!] VTG parse failed")

    # --- Combined state ---
    print("\n--- Combined NAVState (all three sentences merged) ---")

    # Simulate what NAV960Parser does internally
    state = NAVState()

    if gga and gga.latitude is not None:
        state.latitude       = gga.latitude
        state.longitude      = gga.longitude
        state.altitude       = gga.altitude_msl
        state.fix_quality    = gga.fix_quality
        state.num_satellites = gga.num_satellites
        state.hdop           = gga.hdop
        state.x, state.y, state.z = lla_to_ecef(
            gga.latitude, gga.longitude, gga.altitude_msl
        )
        # Auto-set ENU origin to this fix (same as real parser does)
        state.ref_latitude  = gga.latitude
        state.ref_longitude = gga.longitude
        state.ref_altitude  = gga.altitude_msl
        ref_ecef = (state.x, state.y, state.z)
        state.enu_e, state.enu_n, state.enu_u = ecef_to_enu(
            state.x, state.y, state.z,
            *ref_ecef,
            state.ref_latitude, state.ref_longitude,
        )
        print(f"  ENU origin auto-set to first fix: "
              f"lat={gga.latitude:.8f}\u00b0  lon={gga.longitude:.8f}\u00b0")
        print(f"  (ENU will be 0,0,0 here — subsequent fixes show displacement)")

    if gst:
        state.sigma_lat = gst.sigma_lat
        state.sigma_lon = gst.sigma_lon
        state.sigma_alt = gst.sigma_alt

    if vtg and vtg.velocity_north is not None:
        state.course_true = vtg.course_true
        state.speed_ms    = vtg.speed_ms
        state.vNorth      = vtg.velocity_north
        state.vEast       = vtg.velocity_east
        if state.latitude is not None:
            state.x_dot, state.y_dot, state.z_dot = ned_to_ecef_velocity(
                state.latitude, state.longitude,
                state.vNorth, state.vEast, state.vDown,
            )

    print_state(state)


# ===========================================================================
# Live mode
# ===========================================================================

def run_live(port: str, baud: int, ref_lat=None, ref_lon=None, ref_alt=None):
    parser = NAV960Parser(port=port, baudrate=baud, on_update=on_update)
    if None not in (ref_lat, ref_lon, ref_alt):
        parser.set_reference(ref_lat, ref_lon, ref_alt)
        print(f"ENU reference origin fixed at: lat={ref_lat}  lon={ref_lon}  alt={ref_alt} m")
    else:
        print("ENU reference origin: will auto-set to first valid fix.")
    parser.start()
    print(f"Listening on {port} at {baud} baud.  Press Ctrl+C to stop.\n")
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n[NAV960] Stopping…")
    finally:
        parser.stop()


# ===========================================================================
# List available serial ports
# ===========================================================================

def list_ports():
    try:
        from serial.tools import list_ports as lp
        ports = sorted(lp.comports(), key=lambda p: p.device)
        if not ports:
            print("No serial ports found.")
            return
        print(f"{'Device':<12} {'Description':<40} {'HWID'}")
        print("-" * 80)
        for p in ports:
            print(f"{p.device:<12} {p.description:<40} {p.hwid}")
    except ImportError:
        print("pyserial is not installed.  Run: pip install -r requirements.txt")


# ===========================================================================
# Entry point
# ===========================================================================

def main():
    ap = argparse.ArgumentParser(
        description="Parse NMEA data from a Trimble NAV-960 over serial.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python main.py --list-ports\n"
            "  python main.py --port COM7 --baud 38400\n"
            "  python main.py --port COM7 --baud 38400 "
            "--ref-lat -43.5452608 --ref-lon 172.5922080 --ref-alt 32.791\n"
            "  python main.py --demo\n"
        ),
    )
    ap.add_argument("--port",       default="COM7",
                    help="Serial port, e.g. COM7  (default: COM7)")
    ap.add_argument("--baud",       type=int, default=38400,
                    help="Baud rate  (default: 38400)")
    ap.add_argument("--list-ports", action="store_true",
                    help="List available serial ports and exit")
    ap.add_argument("--demo",       action="store_true",
                    help="Parse built-in sample sentences without hardware")
    ap.add_argument("--ref-lat",    type=float, default=None,
                    help="ENU reference latitude  (decimal degrees, optional)")
    ap.add_argument("--ref-lon",    type=float, default=None,
                    help="ENU reference longitude (decimal degrees, optional)")
    ap.add_argument("--ref-alt",    type=float, default=None,
                    help="ENU reference altitude  (metres MSL, optional)")
    args = ap.parse_args()

    if args.list_ports:
        list_ports()
    elif args.demo:
        run_demo()
    else:
        run_live(args.port, args.baud, args.ref_lat, args.ref_lon, args.ref_alt)


if __name__ == "__main__":
    main()
