#!/usr/bin/env python3
"""
dssmap.py — map every Dead Sea Scrolls WORD node to the scroll it belongs to.

Why this is needed: `scroll.tf` is defined on nodes 1531341–1606868
(fragment/lex/line/scroll) and NOT on word nodes (1606869+). Any code that
groups DSS words by book/chapter/verse without this mapping silently merges
EVERY scroll of that book into one bag of words.

That bug is not theoretical. Deut 32:8 returns 29 word nodes from two different
scrolls — one reading הנחיל … בני אלוהים, the other reading הנחל and breaking
off early. Bagged together they look like one impossibly long verse, and a
naive MT comparison then reports invented "extra words."

How the mapping works: `oslots.tf` is an @edge feature. Its data lines start at
node 1430242 (the first non-slot node) and use the same implicit numbering as
any .tf file. Scroll nodes (1605868–1606868) each carry a contiguous slot range
like "1-17148", so the scrolls partition the sign slots. A word's slots fall
inside exactly one of those ranges.
"""
import bisect, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tf as TF

FIRST_NONSLOT = 1430242


def _oslots(tfdir):
    """node -> (first_slot, last_slot)."""
    out = {}
    node = FIRST_NONSLOT - 1
    with open(os.path.join(tfdir, 'oslots.tf'), encoding='utf8') as fh:
        for line in fh:
            if not line.strip():
                break
        for line in fh:
            line = line.rstrip('\n')
            if '\t' in line:
                spec, val = line.split('\t', 1)
                node = int(spec.split('-')[-1]) if '-' in spec else int(spec)
            else:
                node += 1
                val = line
            if not val:
                continue
            first = last = None
            for part in val.split(','):
                if '-' in part:
                    a, b = part.split('-', 1)
                    a, b = int(a), int(b)
                else:
                    a = b = int(part)
                first = a if first is None else min(first, a)
                last = b if last is None else max(last, b)
            out[node] = (first, last)
    return out


def word_to_scroll(tfdir):
    """{word_node: scroll_name}"""
    osl = _oslots(tfdir)
    scroll_name = TF.load(tfdir, 'scroll')
    lo_s, hi_s = TF.node_range(tfdir, 'scroll')
    lo_w, hi_w = TF.node_range(tfdir, 'word')

    ranges = []
    for n in range(lo_s, hi_s + 1):
        if n in osl and n in scroll_name:
            a, b = osl[n]
            ranges.append((a, b, scroll_name[n]))
    ranges.sort()
    starts = [r[0] for r in ranges]

    out = {}
    for n in range(lo_w, hi_w + 1):
        sl = osl.get(n)
        if not sl:
            continue
        i = bisect.bisect_right(starts, sl[0]) - 1
        if 0 <= i < len(ranges) and ranges[i][0] <= sl[0] <= ranges[i][1]:
            out[n] = ranges[i][2]
    return out


if __name__ == '__main__':
    d = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                     'dead-sea-scrolls', 'etcbc-dss', 'tf', '2.0')
    m = word_to_scroll(d)
    print(f'mapped {len(m)} word nodes to scrolls')
    import collections
    c = collections.Counter(m.values())
    print(f'distinct scrolls: {len(c)}')
    for k, v in c.most_common(10):
        print(f'   {k:16} {v:7} words')
