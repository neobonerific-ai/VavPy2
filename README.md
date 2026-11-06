# Kodi 18 Python 2 Port

Schlankes Repository für den Kodi-Add-on-Port auf Python 2.7 / Kodi 18.9 (Leia).

## Zweck

Portierung eines Kodi-Add-ons für Amlogic S812 / AlexELEC 3.3.3 (Kodi 18.9, Python 2.7).

## Unterstützte Hardware und Software

- Amlogic S812 / M8S
- AlexELEC 3.3.3 (Kodi 18.9, Python 2.7)

## Kodi-/Python-Kompatibilität

- Kodi 18.9 / API 2.26.0
- Python 2.7 (kein Python-3-Code im Runtime-Pfad)

## Aufbau des Repositorys

```
.
├── .github/workflows/CI-Workflow-Datei
├── das Add-on-Verzeichnis/
├── tests/
├── .gitignore
├── AGENTS.md
├── HARDWARE_TEST.md
├── PROJECT_STATUS.md
├── README.md
└── UPSTREAM.md
```

## CI und Installations-ZIP

CI-Workflow: `.github/workflows/CI-Workflow-Datei`. Die Installations-ZIP enthält ausschließlich `das Add-on-Verzeichnis/` mit `das Add-on-Verzeichnis/addon.xml`.

## Upstream-Referenz

Der Python-3-Upstream dient lediglich als technische Referenz. Siehe `UPSTREAM.md`.
