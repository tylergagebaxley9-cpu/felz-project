#!/usr/bin/env python3
"""
dssread.py — read the ETCBC Dead Sea Scrolls Text-Fabric corpus directly,
without the text-fabric library.

TF data format: after the '@'-metadata block and one blank line, each line is
    "<node>\t<value>"     explicit node
    "<a>-<b>\t<value>"    inclusive node range
    "<value>"             implicit: previous node + 1
An empty value means the feature is absent for that node.

Source: Martin Abegg's transcriptions, converted by Jacobs/Naaijer/Roorda.
License: CC BY-NC 4.0  (NON-COMMERCIAL — do not bundle into anything sold)

Usage:
    ./dssread.py Deut 32 8
    ./dssread.py Deut 32 8 --feature glyph
"""
import sys, os

TFDIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                     'dead-sea-scrolls', 'etcbc-dss', 'tf', '2.0')


def load(feature, lo=None, hi=None):
    """node -> value for one feature, optionally restricted to [lo,hi]."""
    path = os.path.join(TFDIR, f'{feature}.tf')
    out = {}
    with open(path, encoding='utf8') as fh:
        # skip metadata block
        for line in fh:
            if not line.strip():
                break
        node = 0
        for line in fh:
            line = line.rstrip('\n')
            if not line:
                continue
            if '\t' in line:
                spec, val = line.split('\t', 1)
                if '-' in spec:
                    a, b = spec.split('-', 1)
                    a, b = int(a), int(b)
                    if val:
                        for n in range(a, b + 1):
                            if (lo is None or lo <= n <= hi):
                                out[n] = val
                    node = b
                else:
                    node = int(spec)
                    if val and (lo is None or lo <= node <= hi):
                        out[node] = val
            else:
                node += 1
                if line and (lo is None or lo <= node <= hi):
                    out[node] = line
    return out


def word_range():
    """(lo,hi) node range for otype 'word', from otype.tf."""
    path = os.path.join(TFDIR, 'otype.tf')
    with open(path, encoding='utf8') as fh:
        for line in fh:
            if not line.strip():
                break
        for line in fh:
            if '\t' not in line:
                continue
            spec, val = line.rstrip('\n').split('\t', 1)
            if val == 'word' and '-' in spec:
                a, b = spec.split('-', 1)
                return int(a), int(b)
    raise SystemExit('could not find word node range in otype.tf')


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)
    book, ch, vs = sys.argv[1], sys.argv[2], sys.argv[3]
    feat = 'glyph'
    if '--feature' in sys.argv:
        feat = sys.argv[sys.argv.index('--feature') + 1]

    lo, hi = word_range()
    bk = load('book', lo, hi)
    cp = load('chapter', lo, hi)
    vr = load('verse', lo, hi)
    gl = load(feat, lo, hi)
    sc = load('scroll', lo, hi)
    bib = load('biblical', lo, hi)

    hits = [n for n in range(lo, hi + 1)
            if bk.get(n) == book and str(cp.get(n)) == str(ch) and str(vr.get(n)) == str(vs)]

    if not hits:
        print(f'no scroll on disk carries {book} {ch}:{vs}')
        return

    groups = {}
    for n in hits:
        groups.setdefault(sc.get(n, '?'), []).append(n)

    print(f'\n=== {book} {ch}:{vs} — Dead Sea Scrolls (witness c. 250 BCE – 68 CE) ===\n')
    for scroll, nodes in sorted(groups.items()):
        nodes.sort()
        text = ' '.join(gl.get(n, '') for n in nodes).strip()
        flag = 'biblical' if bib.get(nodes[0]) else 'non-biblical'
        print(f'  {scroll}  [{flag}, {len(nodes)} words]')
        print(f'    {text}\n')


if __name__ == '__main__':
    main()
