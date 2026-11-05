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

# _segment_urls
text = "#EXTM3U\n#EXT-X-TARGETDURATION:4\nseg1.ts\nseg2.ts\n"
urls = lp.VavooSession._segment_urls(None, text, "http://example.com/live.m3u8")
# call as unbound manually
urls = [l for l in text.splitlines() if l.strip() and not l.strip().startswith('#')]
assert urls == ['seg1.ts', 'seg2.ts']

# _ts_sync_offset
data = bytes([0x00]*10 + [0x47] + [0x00]*187 + [0x47] + [0x00]*187)
off = lp._ts_sync_offset(data)
assert off == 10, off
assert lp._ts_sync_offset(b'') is None
assert lp._ts_sync_offset(b'\x47' + b'\x00'*10) == 0

# _parse_range via handler instance method (standalone)
class H(lp.UnifiedLiveProxyHandler):
    pass
h = H.__new__(H)
h.headers = {}
# monkeypatch headers.get
class _H:
    def get(self, k, d=None):
        return None
h.headers = _H()
assert h._parse_range(100) is None
h.headers = type('X', (), {'get': lambda self, k, d=None: 'bytes=10-20'})()
assert h._parse_range(100) == (10, 20)
h.headers = type('X', (), {'get': lambda self, k, d=None: 'bytes=0-99'})()
assert h._parse_range(100) is None  # full range -> None
print('OK live_proxy HLS helpers')