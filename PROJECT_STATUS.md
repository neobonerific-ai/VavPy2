# Project Status

Phase: 1 Setup / Arbeitspaket A (Python 2.7 Port) — in progress
Branch: kodi18-py2
Commit: (pending)
Last Run: 42057196681 (success on 5e70924)
Processed Run-IDs: 42041332854, 42042148762, 42043142676, 42044693828, 42045069053, 42048108905, 42049255467, 42050349077, 42050370005, 42052501214, 42053615632, 42053637740, 42054759902, 42054788404, 42056007788, 42056025407, 42057196681
Last Run: 42045069053 (success, artifact vavoo-py2/vavoo.zip, 30 files, compileall only)
Open tasks: Source inventory, full Python2 port, HTTP transport, Kodi18 playback, real CI tests, hardware test.

## Entwicklungspakete
- A Vollständiger Python-2.7-Port (offen)
- B HTTPX/Netzwerktransport (offen)
- C Kodi-18-Integration (offen)
- D Funktionstests/CI (offen)
- E Hardwaretest (offen / dokumentieren)

## Nächste konkrete Aufgabe
Fix cgi/html fallback in linear_lite.py (done). Weiter: systematische py2-Port-Prüfung + reale Import-/Funktionstests in CI.

## Letzter geprüfter Commit
5e70924 (HEAD)

## Tatsächlich bestandene Tests
- compileall (Python 2.7 container) — Syntax OK.
- smoke_import (Kodi18 mocks) — alle 8 Module OK.

## Bekannte Einschränkungen
- CI prüft nur compileall; keine realen Import-/Funktionstests.
- HTTPX teilweise entfernt, get_httpx() Aufrufe prüfen.
- Kein Hardwarezugriff bisher dokumentiert.

## Verarbeitete Run-IDs
42041332854, 42042148762, 42043142676, 42044693828, 42045069053, 42048108905, 42049255467, 42050349077, 42050370005, 42052501214, 42053615632, 42053637740, 42054759902, 42054788404, 42056007788, 42056025407, 42057196681