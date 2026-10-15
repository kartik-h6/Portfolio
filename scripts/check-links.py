#!/usr/bin/env python3
"""Fail the build if a local src/href points at a file that does not exist.

Written after this repository was bitten twice by the same class of drift: the
MANIFEST describing files that had been deleted, and three <picture> fallbacks
left pointing at PNG originals that were gone. Both were invisible in a browser
(the WebP <source> masked the first, and a modern browser never requests the
<img> URL), which is exactly why a human check missed them twice.

Only local references are checked. Absolute URLs are assumed to be reachable and
are deliberately not fetched — a network check belongs in a separate job, not in
a commit gate.
"""
import os
import re
import sys
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

REF = re.compile(r'(?:src|href)="([^"]+)"')
SKIP = ('http://', 'https://', 'mailto:', 'tel:', 'data:', '#', '//')

# Scanned: every page plus the README, which is rendered on the repository
# landing page and has been the source of a broken reference before.
TARGETS = sorted(glob.glob('*.html')) + ['README.md']

problems = []
for page in TARGETS:
    with open(page, encoding='utf-8') as fh:
        text = fh.read()
    for match in REF.finditer(text):
        url = match.group(1).split('?')[0].split('#')[0]
        if not url or url.startswith(SKIP):
            continue
        if not os.path.exists(url):
            problems.append(f'{page}: {url}')

if problems:
    print('Missing local references:')
    for item in problems:
        print('  ' + item)
    print(f'\n{len(problems)} dangling reference(s).')
    sys.exit(1)

print(f'OK — every local reference resolves across {len(TARGETS)} files.')
