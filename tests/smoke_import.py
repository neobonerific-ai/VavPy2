import sys, os
base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'plugin.video.vavooto', 'resources'))
sys.path.insert(0, base)

# Kodi 18 mocks — realistic: unknown attributes raise AttributeError
import types
def _make_mod(name):
    m = types.ModuleType(name)
    # provide __getattr__? ModuleType doesn't, so unknown attr raises AttributeError by default
    return m

for m in ('xbmc', 'xbmcvfs', 'xbmcaddon', 'xbmcgui', 'xbmcplugin'):
    sys.modules[m] = _make_mod(m)

import xbmcaddon
class Addon(object):
    def getAddonInfo(self, k): return '/tmp/addon'
    def getSetting(self, k): return ''
    def setSetting(self, k, v): return None
    def openSettings(self): return None
xbmcaddon.Addon = lambda *a, **k: Addon()
# define translatePath on xbmc only (Kodi 18 style)
import xbmc
xbmc.translatePath = lambda p: p
xbmc.Monitor = lambda *a, **k: _make_mod('monitor')
xbmc.Player = _make_mod('player')
xbmc.getInfoLabel = lambda *a, **k: ''
xbmc.executebuiltin = lambda *a, **k: None
xbmc.getCondVisibility = lambda *a, **k: False
# Window mock
import xbmcgui
class _Win(object):
    def getProperty(self, k): return ''
    def setProperty(self, k, v): return None
xbmcgui.Window = lambda *a, **k: _Win()
xbmcgui.ListItem = lambda *a, **k: _make_mod('item')
xbmcgui.Dialog = lambda *a, **k: _make_mod('dialog')
xbmcgui.DialogProgress = lambda *a, **k: _make_mod('dp')
for m in ('resolveurl', 'httpx', 'urllib3'):
    if m not in sys.modules:
        _m = _make_mod(m)
        if m == 'urllib3':
            setattr(_m, 'disable_warnings', lambda *a, **k: None)
        sys.modules[m] = _m
if 'requests' not in sys.modules:
    _r = _make_mod('requests')
    setattr(_r, 'Session', lambda: _make_mod('session'))
    sys.modules['requests'] = _r
else:
    if not hasattr(sys.modules['requests'], 'Session'):
        setattr(sys.modules['requests'], 'Session', lambda: _make_mod('session'))

mods = ['vavoo.utils', 'vavoo.live_proxy', 'vavoo.vjlive', 'vavoo.vjackson',
        'vavoo.stalker', 'vavoo.linear_lite', 'vavoo.vavoo_tv', 'main']
for m in mods:
    __import__(m)
    print('OK import', m)
