#!/usr/bin/env python3
"""
diverge_lxx.py — screen the Masoretic Psalms against the Septuagint Psalms.

WHAT THIS CAN AND CANNOT DO
---------------------------
Hebrew and Greek cannot be compared word-for-word mechanically. A translator's
choices — one Greek word for two Hebrew, an added article, a paraphrase — are not
textual variants. So this does NOT identify variants. It flags WHERE TO LOOK, by
comparing word counts per verse and finding verses one tradition has and the other
does not. Every hit needs reading by eye; the tool hands you the shortlist.

THE VERSIFICATION TRAP (verified from the data, not assumed)
------------------------------------------------------------
LXX and Hebrew psalm numbers do not line up. Confirmed by inspecting verse counts
and opening words in this corpus on 2026-08-08:

    LXX  9  (39 vv)  =  Hebrew  9 + 10      merged
    LXX 113 (26 vv)  =  Hebrew 114 + 115    merged
    LXX 114 / 115    =  Hebrew 116          split
    LXX 146 / 147    =  Hebrew 147          split
    LXX 148          =  Hebrew 148          back in sync

Between those seams the offset is Hebrew − 1 (Hebrew 23 = LXX 22, verified against
κύριος ποιμαίνει με). Comparing without this mapping compares unrelated psalms.

The merged and split psalms (Hebrew 9, 10, 114, 115, 116, 147) are SKIPPED — their
verse-level alignment needs per-verse offsets not derived here. They are reported
as skipped rather than silently dropped.

LXX Psalm 151 has no Hebrew counterpart at all. It calls itself
`ἔξωθεν τοῦ ἀριθμοῦ` — "outside the number."

Usage:
    ./diverge_lxx.py              # the screen
    ./diverge_lxx.py --ratio 1.5  # flag threshold (default 1.4)
"""
import csv, os, re, sys, unicodedata
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OSIS = '{http://www.bibletechnologies.net/2003/OSIS/namespace}'
HEB = re.compile(r'[א-ת]+')

# Hebrew chapter -> LXX chapter, for 1:1 verse-aligned ranges only.
SKIP = {9, 10, 114, 115, 116, 147}          # merged/split — alignment undefined here


def heb_to_lxx(ch):
    if ch in SKIP:
        return None
    if 1 <= ch <= 8:
        return ch
    if 11 <= ch <= 113:
        return ch - 1
    if 117 <= ch <= 146:
        return ch - 1
    if 148 <= ch <= 150:
        return ch
    return None


def masoretic_psalms():
    p = f'{ROOT}/hebrew-ot/morphhb/wlc/Ps.xml'
    out = {}
    for v in ET.parse(p).getroot().iter(f'{OSIS}verse'):
        oid = v.get('osisID')
        if not oid:
            continue
        parts = oid.split('.')
        if len(parts) != 3:
            continue
        words = []
        for w in v.iter():
            if w.tag.split('}')[-1] in ('w', 'seg') and w.text:
                s = unicodedata.normalize('NFD', w.text)
                s = ''.join(c for c in s if not unicodedata.combining(c))
                words.extend(HEB.findall(s))
        out[(int(parts[1]), int(parts[2]))] = words
    return out


def lxx_psalms():
    base = f'{ROOT}/septuagint/LXX-Rahlfs-1935'
    vsx = sorted((int(r[0]), r[1][1:])
                 for r in csv.reader(open(f'{base}/12-Marvel.Bible/00-versification_original.csv',
                                          encoding='utf8'), delimiter='\t')
                 if len(r) >= 2 and r[1].startswith('†'))
    idx = {ref: (st, vsx[i + 1][0] if i + 1 < len(vsx) else 10**9)
           for i, (st, ref) in enumerate(vsx)}
    words = {}
    for r in csv.reader(open(f'{base}/01_wordlist_unicode/text_accented.csv',
                             encoding='utf8'), delimiter='\t'):
        if len(r) >= 3:
            try:
                words[int(r[0])] = r[2]
            except ValueError:
                pass
    # The LXX versification uses SUB-VERSES ("13a", "13b"). They are merged into
    # their base verse here, otherwise int() throws and the whole scan dies.
    out = {}
    for ref, (a, b) in sorted(idx.items()):
        p = ref.split('.')
        if len(p) != 3 or p[0] != '19':
            continue
        m = re.match(r'^(\d+)', p[2])
        if not m:
            continue
        key = (int(p[1]), int(m.group(1)))
        w = [words[i] for i in range(a, b) if i in words]
        if w:
            out.setdefault(key, []).extend(w)
    return out


def main():
    ratio = 1.4
    if '--ratio' in sys.argv:
        ratio = float(sys.argv[sys.argv.index('--ratio') + 1])

    mt, lxx = masoretic_psalms(), lxx_psalms()
    compared = mt_only = lxx_only = flagged = 0
    rows = []

    for (hch, hv), hw in sorted(mt.items()):
        gch = heb_to_lxx(hch)
        if gch is None:
            continue
        gw = lxx.get((gch, hv))
        if gw is None:
            mt_only += 1
            rows.append((hch, hv, gch, 'MT-ONLY', len(hw), 0))
            continue
        compared += 1
        r = (len(hw) / len(gw)) if gw else 99
        if r >= ratio or (gw and len(gw) / len(hw) >= ratio):
            flagged += 1
            rows.append((hch, hv, gch, 'LENGTH', len(hw), len(gw)))

    # verses the LXX has where the mapped Hebrew verse does not exist
    inv = {}
    for h in range(1, 151):
        g = heb_to_lxx(h)
        if g:
            inv.setdefault(g, h)
    for (gch, gv), gw in sorted(lxx.items()):
        h = inv.get(gch)
        if h and (h, gv) not in mt:
            lxx_only += 1
            rows.append((h, gv, gch, 'LXX-ONLY', 0, len(gw)))

    print(f'\n{"="*76}')
    print('  MASORETIC vs SEPTUAGINT — Psalms screen')
    print(f'{"="*76}')
    print(f'  verses compared        : {compared}')
    print(f'  flagged on length (≥{ratio}x): {flagged}')
    print(f'  in MT, absent from LXX : {mt_only}')
    print(f'  in LXX, absent from MT : {lxx_only}')
    print(f'  psalms skipped (merge/split): {sorted(SKIP)}')
    print(f'  LXX Psalm 151 has no Hebrew counterpart at all')

    print(f'\n  {"Heb":>8}  {"LXX":>6}  {"kind":9} {"MT wds":>7} {"LXX wds":>8}')
    print('  ' + '-' * 48)
    for hch, hv, gch, kind, a, b in rows[:45]:
        print(f'  {f"{hch}:{hv}":>8}  {f"{gch}:{hv}":>6}  {kind:9} {a:7} {b:8}')
    if len(rows) > 45:
        print(f'  … {len(rows)-45} more')

    print('\n  A length flag is NOT a variant. Hebrew and Greek differ in word count')
    print('  for ordinary translational reasons. These are verses to READ, not')
    print('  conclusions. Verify each with:  ./tools/allwitness.py Ps <ch> <vs>')
    print()


if __name__ == '__main__':
    main()
