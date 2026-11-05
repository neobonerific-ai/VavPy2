import sys, os
sys.argv = ['plugin', '1']
base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'plugin.video.vavooto', 'resources'))
sys.path.insert(0, base)

import types

def _strict(name):
    m = types.ModuleType(name)
    return m

for m in ('xbmc', 'xbmcvfs', 'xbmcaddon', 'xbmcgui', 'xbmcplugin'):
    sys.modules[m] = _strict(m)

import xbmcplugin
xbmcplugin.setResolvedUrl = lambda *a, **k: None
xbmcplugin.endOfDirectory = lambda *a, **k: None

import xbmc
xbmc.translatePath = lambda p: p
xbmc.Monitor = lambda *a, **k: _strict('monitor')
xbmc.Player = type('Player', (object,), {})
xbmc.getInfoLabel = lambda *a, **k: ''
xbmc.executebuiltin = lambda *a, **k: None
xbmc.getCondVisibility = lambda *a, **k: False
xbmc.LOGDEBUG = 0
xbmc.LOGINFO = 1
xbmc.log = lambda *a, **k: None

import xbmcaddon
class Addon(object):
    def getAddonInfo(self, k): return '/tmp/addon'
    def getSetting(self, k): return 'true' if k == 'vavoo' else ''
    def setSetting(self, k, v): return None
    def openSettings(self): return None
xbmcaddon.Addon = lambda *a, **k: Addon()

import xbmcgui
captured = {}
class _Item(object):
    def __init__(self, *a, **k):
        self.props = {}
        self.path = None
        self.mime = None
    def setProperty(self, k, v): self.props[k] = v
    def getProperty(self, k): return self.props.get(k, '')
    def setPath(self, p): self.path = p
    def setMimeType(self, m): self.mime = m
    def setInfo(self, *a, **k): pass
    def setIsPlayable(self, *a, **k): pass
xbmcgui.ListItem = lambda *a, **k: _Item()
class _Win(object):
    def getProperty(self,k): return ''
    def setProperty(self,k,v): return None
xbmcgui.Window = lambda *a, **k: _Win()
xbmcgui.Dialog = lambda *a, **k: _strict('dlg')
xbmcgui.DialogProgress = lambda *a, **k: _strict('dp')
xbmcgui.NOTIFICATION_ERROR = 0

for m in ('resolveurl', 'httpx', 'requests', 'urllib3', 'infotagger'):
    if m not in sys.modules:
        sys.modules[m] = _strict(m)
import requests
requests.Session = lambda: _strict('session')

import vavoo.utils as utils
# patch cache
utils.get_cache = lambda k: (False, None)
utils.addon.getSetting = lambda k: 'true' if k == 'vavoo' else ''
utils.set_cache = lambda *a, **k: None
utils.getSetting = lambda k: 'true' if k in ('vavoo','live_auto_retry') else ''

import vavoo.vjlive as vj
vj.getSetting = utils.addon.getSetting
# mock channel data
vj.getchannels = lambda *a, **k: {'Ch1': [{'source':'vavoo','url':'http://example.com/live.m3u8'}]}
vj.resolve_link = lambda link: ('http://example.com/stream.ts', None)
vj.is_mpeg_ts_url = lambda u: True
vj.test_m3u8 = lambda *a, **k: True

# capture the created ListItem
orig_li = xbmcgui.ListItem
created = []
def _li(*a, **k):
    it = _Item()
    created.append(it)
    return it
xbmcgui.ListItem = _li
vj.ListItem = _li  # if referenced
import vavoo.vjlive as vj
vj.getSetting = utils.addon.getSetting

vj.livePlay('Ch1')

assert created, 'ListItem not created'
it = created[-1]
print('props:', it.props)
assert it.props.get('inputstream') == 'inputstream.ffmpeg'
assert it.props.get('inputstreamaddon') == 'inputstream.ffmpeg'
assert it.props.get('inputstream.ffmpeg.is_realtime_stream') == 'true'
print('OK playback properties (real code executed)')
