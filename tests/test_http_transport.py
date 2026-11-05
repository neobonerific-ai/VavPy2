import sys, os
base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'plugin.video.vavooto', 'resources'))
sys.path.insert(0, base)

# Kodi 18 mocks (same as smoke_import)
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

# requests mock for deterministic test (no network)
class _Resp(object):
    def __init__(self, text):
        self.text = text
        self.content = text
    def get(self, *a, **k): return self

class _Session(object):
    def __init__(self):
        self.verify = True
        self.timeout = None
    def get(self, url, headers=None, **k):
        return _Resp('')

import types
requests_mod = types.ModuleType('requests')
requests_mod.Session = _Session
sys.modules['requests'] = requests_mod

from vavoo.live_proxy import get_httpx
client = get_httpx()
assert client is not False and client is not None, 'get_httpx must return a client'
assert hasattr(client, 'get'), 'client must expose .get'
print('OK http transport client')

# linear_lite imports and degrades gracefully without network
import vavoo.linear_lite as ll
assert ll.get_httpx() is not None
print('OK linear_lite import')
