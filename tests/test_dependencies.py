import os, re, sys

root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
addon_dir = os.path.join(root, 'plugin.video.vavooto')
res = os.path.join(addon_dir, 'resources')

# 1. No runtime httpx imports in python sources (HTTPX removed -> requests only)
bad = []
for r, _, fs in os.walk(res):
    for f in fs:
        if not f.endswith('.py'):
            continue
        p = os.path.join(r, f)
        src = open(p).read()
        for line in src.splitlines():
            s = line.strip()
            if s.startswith('#'):
                continue
            if ('import httpx' in s or 'from httpx' in s or 'import httpx,' in s):
                bad.append((p, line))
assert not bad, 'httpx import found: %s' % bad

# 2. addon.xml must declare requests/resolveurl not httpx
addon_xml = open(os.path.join(addon_dir, 'addon.xml')).read()
assert 'httpx' not in addon_xml.lower(), 'addon.xml references httpx'

# 3. All python modules compile (py2 syntax smoke via compile)
import py_compile, tempfile
for r, _, fs in os.walk(res):
    for f in fs:
        if not f.endswith('.py'):
            continue
        p = os.path.join(r, f)
        py_compile.compile(p, doraise=True)

print('OK dependencies (no httpx runtime, addon.xml clean, compile OK)')