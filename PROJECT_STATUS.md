# Project Status

Phase: 1 Setup / Arbeitspaket A (Python 2.7 Port) + B (HTTP transport) + D (Tests) — in progress
Branch: kodi18-py2
Commit: 082e064 (Kodi18 compat fallback test + CI step)
Last Run: pending (new push)
Processed Run-IDs: 42041332854, 42042148762, 42043142676, 42044693828, 42045069053, 42048108905, 42049255467, 42050349077, 42050370005, 42052501214, 42053615632, 42053637740, 42054759902, 42054788404, 42056007788, 42056025407, 42057196681, 42058562077, 42059735949, 42060938503, 42061898948, 42062761835, 42062806606, 42063869356, 42063919705
Open tasks: Source inventory, full Python2 port, HTTP transport (HTTPX entfernt done, Caller prüfen), Kodi18 playback, real CI tests, hardware test.

## Entwicklungspakete
- A Vollständiger Python-2.7-Port (in progress)
- B HTTPX/Netzwerktransport (in progress: get_httpx requests-only)
- C Kodi-18-Integration (offen)
- D Funktionstests/CI (offen)
- E Hardwaretest (offen / dokumentieren)

## Nächste konkrete Aufgabe
CI-Run mit HTTP-Transport-Tests abwarten; dann Funktionstests für utils/linear_lite erweitern und Kodi18-Integration (Paket C) angehen.

## Letzter geprüfter Commit
7f7378d (HEAD)

## Tatsächlich bestandene Tests
- compileall (Python 2.7 container) — Syntax OK.
- smoke_import (Kodi18 mocks) — alle 8 Module OK.
- test_kodi18_compat — ListItemInfoTag fallback OK.

## Bekannte Einschränkungen
- CI prüft nur compileall; keine realen Import-/Funktionstests.
- HTTPX entfernt; get_httpx() liefert requests.Session oder False.
- Kein Hardwarezugriff bisher dokumentiert.

## Verarbeitete Run-IDs
42041332854, 42042148762, 42043142676, 42044693828, 42045069053, 42048108905, 42049255467, 42050349077, 42050370005, 42052501214, 42053615632, 42053637740, 42054759902, 42054788404, 42056007788, 42056025407, 42057196681, 42058562077