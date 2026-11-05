import sys, os
base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'plugin.video.vavooto', 'resources'))
sys.path.insert(0, base)

# Kodi 18 mocks
class _Mod(object):
    def __getattr__(self, name):
        def _f(*a, **k): return None
        return _f
for m in ('xbmc', 'xbmcvfs', 'xbmcaddon', 'xbmcgui', 'xbmcplugin'):
    sys.modules[m] = _Mod()

import xbmcaddon
class Addon(_Mod):
    def getAddonInfo(self, k): return '/tmp/addon'
    def getSetting(self, k): return ''
    def setSetting(self, k, v): return None
xbmcaddon.Addon = lambda *a, **k: Addon()
# Window mock
import xbmcgui
xbmcgui.Window = lambda *a, **k: _Mod()
# translatePath passthrough for mocks
import xbmcvfs
xbmcvfs.translatePath = lambda p: p

# Third-party / optional mocks for smoke import
for m in ('resolveurl', 'httpx', 'requests', 'urllib3'):
    if m not in sys.modules:
        sys.modules[m] = _Mod()

mods = ['vavoo.utils', 'vavoo.live_proxy', 'vavoo.vjlive', 'vavoo.vjackson',
        'vavoo.stalker', 'vavoo.linear_lite', 'vavoo.vavoo_tv', 'main']
for m in mods:
    __import__(m)
    print('OK import', m)
