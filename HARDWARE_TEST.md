# Hardware test — Amlogic S812 M8S (AlexELEC 3.3.3)

Status: **not executed** (no hardware access in CI environment).

## Target
- Device: Amlogic S812 M8S
- OS: AlexELEC 3.3.3 (Kodi 18 Leia, Python 2.7)
- Addon: plugin.video.vavooto (branch kodi18-py2)

## Manual verification steps
1. Install addon zip from CI artifact.
2. Start Kodi, open addon, verify main menu loads (no import errors).
3. Play a VAVOO live channel -> verify ffmpegdirect inputstream starts (MPEG-TS/HLS).
4. Play a VOD item -> verify inputstream.adaptive starts.
5. Check Kodi log for Python tracebacks.

## Known constraints
- No hardware access available in automated pipeline; results must be reported manually.
