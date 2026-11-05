import os, re
base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'plugin.video.vavooto', 'resources'))
files = ['vavoo/vjlive.py', 'vavoo/vjackson.py']
for rel in files:
    p = os.path.join(base, rel)
    src = open(p).read()
    # Leia requires inputstreamaddon (inputstream alone is Kodi19+)
    assert "inputstreamaddon" in src, rel + " missing inputstreamaddon"
    # must not rely on inputstream-only without addon
    assert src.count("setProperty('inputstream',") <= src.count("setProperty('inputstreamaddon'"), rel
print('OK playback properties (inputstreamaddon present)')
