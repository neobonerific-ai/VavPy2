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
for m in ('resolveurl', 'httpx', 'requests', 'urllib3'):
    if m not in sys.modules:
        sys.modules[m] = _Mod()

import vavoo.live_proxy as lp

# _parse_target_duration
assert lp._parse_target_duration("#EXT-X-TARGETDURATION:6\n") == 6
assert lp._parse_target_duration("#EXT-X-TARGETDURATION: 3.5\n") == 3  # int(float)
assert lp._parse_target_duration("nope") is None

# _media_sequence
assert lp._media_sequence("#EXT-X-MEDIA-SEQUENCE:42\n") == "42"
assert lp._media_sequence("nope") is None

# _od_move_to_end
from collections import OrderedDict
od = OrderedDict([("a",1),("b",2),("c",3)])
lp._od_move_to_end(od, "a")
assert list(od.keys()) == ["b","c","a"], list(od.keys())
# missing key no crash
lp._od_move_to_end(od, "zzz")
print("OK live_proxy helpers")
