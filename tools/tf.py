#!/usr/bin/env python3
"""
tf.py — minimal reader for Text-Fabric .tf data files.

NOT the `text-fabric` PyPI package (that is a different project and does not
read these files with the same API). This parses the plain-text format directly.

FORMAT: an '@'-prefixed metadata block, one blank line, then data lines:
    "<node>\\t<value>"    explicit node
    "<a>-<b>\\t<value>"   inclusive node range
    "<value>"             implicit: previous node + 1

CRITICAL: an empty value still advances the implicit counter. A parser that
skips blank lines silently misaligns every subsequent node and produces
plausible-looking but wrong output. That bug was hit and fixed here on
2026-08-08; the tell was four different sign types showing identical letter
frequencies. Always cross-check a result against a known quantity.
"""
import os


def stream(path):
    """Yield (node, value) for every data line, including empty values."""
    node = 0
    with open(path, encoding='utf8') as fh:
        for line in fh:                       # skip @metadata
            if not line.strip():
                break
        for line in fh:
            line = line.rstrip('\n')
            if '\t' in line:
                spec, val = line.split('\t', 1)
                if '-' in spec:
                    a, b = (int(x) for x in spec.split('-', 1))
                    for n in range(a, b + 1):
                        yield n, val
                    node = b
                else:
                    node = int(spec)
                    yield node, val
            else:
                node += 1
                yield node, line


def load(tfdir, feature, lo=None, hi=None, keep_empty=False):
    """node -> value for one feature, optionally restricted to [lo, hi]."""
    path = os.path.join(tfdir, f'{feature}.tf')
    out = {}
    for n, v in stream(path):
        if lo is not None and not (lo <= n <= hi):
            continue
        if v or keep_empty:
            out[n] = v
    return out


def node_range(tfdir, otype):
    """(lo, hi) node range for an object type, from otype.tf."""
    for n, v in stream(os.path.join(tfdir, 'otype.tf')):
        pass
    lo = hi = None
    path = os.path.join(tfdir, 'otype.tf')
    with open(path, encoding='utf8') as fh:
        for line in fh:
            if not line.strip():
                break
        for line in fh:
            if '\t' not in line:
                continue
            spec, val = line.rstrip('\n').split('\t', 1)
            if val == otype and '-' in spec:
                a, b = (int(x) for x in spec.split('-', 1))
                return a, b
    raise KeyError(f'otype {otype!r} not found in {path}')
