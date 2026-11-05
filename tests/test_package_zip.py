import os, sys, zipfile, tempfile

root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
addon_dir = os.path.join(root, 'plugin.video.vavooto')

# Build a zip in temp (mirroring CI step) and validate structure
fd, path = tempfile.mkstemp(suffix='.zip')
os.close(fd)
z = zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED)
for r, _, fs in os.walk(addon_dir):
    for f in fs:
        if '__pycache__' in r or f.endswith('.pyc'):
            continue
        full = os.path.join(r, f)
        arc = 'plugin.video.vavooto/' + os.path.relpath(full, addon_dir)
        z.write(full, arc)
z.close()

# Validate
z2 = zipfile.ZipFile(path)
names = z2.namelist()
assert len(names) > 0, 'zip must not be empty'
# exactly one top-level folder
tops = set(n.split('/')[0] for n in names if '/' in n)
assert tops == {'plugin.video.vavooto'}, 'unexpected top-level: %s' % tops
# addon.xml under addon folder
assert 'plugin.video.vavooto/addon.xml' in names, 'addon.xml missing'
# read addon id
import re
data = z2.read('plugin.video.vavooto/addon.xml').decode('utf-8')
m = re.search(r'id="([^"]+)"', data)
assert m and m.group(1) == 'plugin.video.vavooto', 'bad addon id'
# no pycache entries
assert not any('__pycache__' in n for n in names), 'pycache leaked into zip'
# all entries readable
bad = z2.testzip()
assert bad is None, 'corrupt zip entry: %s' % bad
z2.close()
os.remove(path)
print('OK package zip (%d entries)' % len(names))
