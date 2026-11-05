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

class _Resp(object):
    def __init__(self, text=''):
        self.text = text
        self.content = text.encode('utf-8') if isinstance(text, unicode) else text
    def raise_for_status(self): return None
    def json(self): return []
class _Session(object):
    def __init__(self):
        self.verify = True; self.timeout = None
    def request(self, *a, **k): return _Resp('')
    def get(self, *a, **k): return _Resp('')
import types
requests_mod = types.ModuleType('requests')
requests_mod.Session = _Session
requests_mod.RequestException = Exception
sys.modules['requests'] = requests_mod
import requests

import vavoo.linear_lite as ll

# _extract_stream_url: m3u8 file
content = "var x = { file: 'https://example.com/live.m3u8?token=1' };"
url = ll._extract_stream_url(content)
assert url == 'https://example.com/live.m3u8?token=1', url
print('OK extract file m3u8')

# html escaped
content2 = "file: https:\\/\\/example.com\\/a.m3u8"
assert ll._extract_stream_url(content2) == 'https://example.com/a.m3u8', ll._extract_stream_url(content2)
print('OK extract escaped')

# no m3u8 -> empty
assert ll._extract_stream_url('file: "https://example.com/video.mp4"') == ''
print('OK extract rejects non-m3u8')

# _nydus_category
assert ll._nydus_category('orf-1') == 'at'
assert ll._nydus_category('SRF1') == 'ch'
assert ll._nydus_category('foo') == 'de'
print('OK nydus category')

# _b64decode roundtrip
import base64
val = base64.b64encode(b'hello').decode('ascii')
assert ll._b64decode(val) == 'hello'
print('OK b64decode')

print('ALL linear_lite tests OK')
