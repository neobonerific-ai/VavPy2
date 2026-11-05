import sys, os
base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'plugin.video.vavooto', 'resources'))
sys.path.insert(0, base)

# Kodi 18 mocks
class _Mod(object):
    def __getattr__(self, name):
        def _f(*a, **k): return None
        return _f
for m in ('xbmc', 'xbmcvfs', 'xbmcaddon', 'xbmcgui'):
    sys.modules[m] = _Mod()

import xbmcaddon
class Addon(object):
    def getAddonInfo(self, k): return '/tmp/addon'
    def getSetting(self, k): return ''
xbmcaddon.Addon = lambda *a, **k: Addon()

# infotagger optional
try:
    import infotagger  # noqa
except Exception:
    pass

mods = ['vavoo.utils', 'vavoo.live_proxy', 'vavoo.vjlive', 'vavoo.vjackson',
        'vavoo.stalker', 'vavoo.linear_lite', 'vavoo.vavoo_tv', 'main']
for m in mods:
    __import__(m)
    print('OK import', m)
