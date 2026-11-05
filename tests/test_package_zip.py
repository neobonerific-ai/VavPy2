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
        arc = os.path.relpath(full, addon_dir)
        z.write(full, arc)
z.close()

# Validate
z2 = zipfile.ZipFile(path)
names = z2.namelist()
assert len(names) > 0, 'zip must not be empty'
# addon.xml must be present at top level
assert 'addon.xml' in names, 'addon.xml missing from zip root'
# no pycache entries
assert not any('__pycache__' in n for n in names), 'pycache leaked into zip'
# all entries readable
bad = z2.testzip()
assert bad is None, 'corrupt zip entry: %s' % bad
z2.close()
os.remove(path)
print('OK package zip (%d entries)' % len(names))
