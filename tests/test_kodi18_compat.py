import sys, os
base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'plugin.video.vavooto', 'resources'))
sys.path.insert(0, base)

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
import xbmcgui
xbmcgui.Window = lambda *a, **k: _Mod()
import xbmcvfs
xbmcvfs.translatePath = lambda p: p

for m in ('resolveurl', 'httpx', 'requests', 'urllib3', 'infotagger'):
    if m not in sys.modules:
        sys.modules[m] = _Mod()

import vavoo.utils as utils
assert utils.ListItemInfoTag is None, 'ListItemInfoTag must be None when infotagger missing'
assert utils.tagger is False, 'tagger must be False when infotagger missing'
print('OK kodi18 compat fallback')