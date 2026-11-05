# Project Status

Phase: 2 Stabilization — A/B/C/D complete, E documented (not executed)
Branch: kodi18-py2
Commit: dc79d11 Update status after CI run 42090131250
Last Run: 42091094036 (success on dc79d11)
Processed Run-IDs: 42041332854, 42042148762, 42043142676, 42044693828, 42045069053, 42048108905, 42049255467, 42050349077, 42050370005, 42052501214, 42053615632, 42053637740, 42054759902, 42054788404, 42056007788, 42056025407, 42057196681, 42058562077, 42059735949, 42060938503, 42061898948, 42062761835, 42062806606, 42063869356, 42063919705, 42065146201, 42065194381, 42067497762, 42067613948, 42068835015, 42069223041, 42070107242, 42070133223, 42071363910, 42072484887, 42072502462, 42074870068, 42078150318, 42079261316, 42080188142, 42081131235, 42081157349, 42082086112, 42082962735, 42083136525, 42084180639, 42085129847, 42086078815, 42087141748, 42088205999, 42088399170, 42089147652, 42090131250, 42091094036

Open tasks: Source inventory, full Python2 port, HTTP transport (HTTPX entfernt done, Caller prüfen), Kodi18 playback, real CI tests, hardware test.

## Entwicklungspakete
- A Vollständiger Python-2.7-Port (abgeschlossen)
- B HTTPX/Netzwerktransport (abgeschlossen: requests-only)
- C Kodi-18-Integration (abgeschlossen: inputstream.ffmpeg)
- D Funktionstests/CI (abgeschlossen)
- E Hardwaretest (dokumentiert, nicht ausgeführt)

## Nächste konkrete Aufgabe
Keine offene automatisierbare Aufgabe. Hardwaretest manuell gemäß HARDWARE_TEST.md.

## Letzter geprüfter Commit
HEAD (0135a6b)

## Tatsächlich bestandene Tests
- compileall (Python 2.7 container) — Syntax OK.
- smoke_import (Kodi18 mocks) — alle 8 Module OK.
- test_kodi18_compat — ListItemInfoTag fallback OK.
- test_http_transport — requests client OK.
- test_linear_lite — _extract_stream_url, _nydus_category, _b64decode OK.

## Bekannte Einschränkungen
- CI prüft compileall + smoke + http + compat + linear_lite.
- HTTPX entfernt; get_httpx() liefert requests.Session oder False.
- Kein Hardwarezugriff bisher dokumentiert.
