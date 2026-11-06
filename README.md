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
├── .github/workflows/
├── das Add-on-Verzeichnis/
├── tests/
├── .gitignore
└── README.md
```

## CI und Installations-ZIP

CI-Workflow im Verzeichnis `.github/workflows/`. Die Installations-ZIP enthält ausschließlich das Add-on-Verzeichnis mit `addon.xml`.
