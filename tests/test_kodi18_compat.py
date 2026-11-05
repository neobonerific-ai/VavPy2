import sys, os
base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'plugin.video.vavooto', 'resources'))
sys.path.insert(0, base)

import types

def _strict(name):
    return types.ModuleType(name)

for m in ('xbmc', 'xbmcvfs', 'xbmcaddon', 'xbmcgui', 'xbmcplugin'):
    sys.modules[m] = _strict(m)

# Kodi 18 style: translatePath only on xbmc, NOT on xbmcvfs
import xbmc
called = {'n': 0}
def _tp(p):
    called['n'] += 1
    return '/kodi18' + str(p)
xbmc.translatePath = _tp
xbmc.Monitor = lambda *a, **k: _strict('monitor')
xbmc.Player = _strict('player')
xbmc.getInfoLabel = lambda *a, **k: ''
xbmc.executebuiltin = lambda *a, **k: None
xbmc.getCondVisibility = lambda *a, **k: False

import xbmcaddon
class Addon(object):
    def getAddonInfo(self, k): return '/tmp/addon'
    def getSetting(self, k): return ''
    def setSetting(self, k, v): return None
    def openSettings(self): return None
xbmcaddon.Addon = lambda *a, **k: Addon()

import xbmcgui
class _Win(object):
    def getProperty(self, k): return ''
    def setProperty(self, k, v): return None
xbmcgui.Window = lambda *a, **k: _Win()
xbmcgui.ListItem = lambda *a, **k: _strict('item')
xbmcgui.Dialog = lambda *a, **k: _strict('dialog')
xbmcgui.DialogProgress = lambda *a, **k: _strict('dp')

for m in ('resolveurl', 'httpx', 'requests', 'urllib3', 'infotagger'):
    if m not in sys.modules:
        sys.modules[m] = _strict(m)

import requests
requests.Session = lambda: _strict('session')

# Kodi 18 case: xbmcvfs has no translatePath
import xbmcvfs
assert not hasattr(xbmcvfs, 'translatePath'), 'xbmcvfs.translatePath must not exist in Kodi 18 test'

import vavoo.utils as utils
# ListItemInfoTag None when infotagger missing
assert utils.ListItemInfoTag is None
assert utils.tagger is False

# translatePath must call xbmc.translatePath exactly
called['n'] = 0
res = utils.translatePath('special://foo')
assert res == '/kodi18special://foo', res
assert called['n'] == 1, called

# Kodi 19+ case: xbmcvfs.translatePath exists
xbmcvfs.translatePath = lambda p: '/kodi19' + str(p)
res2 = utils.translatePath('special://bar')
assert res2 == '/kodi19special://bar', res2

print('OK kodi18 compat fallback')
