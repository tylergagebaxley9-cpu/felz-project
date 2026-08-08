#!/usr/bin/env python3
"""
diverge.py — systematically compare the Dead Sea Scrolls against the Masoretic
text and flag every place they differ.

Not verse-by-verse checking. This walks every verse where BOTH witnesses have
text and reports:

  CHANGED  — both have the verse, the consonantal text differs
  DSS-ONLY — the scrolls have words the Masoretic text does not
  MT-ONLY  — the Masoretic text has words the scrolls do not

Comparison is on the CONSONANTAL SKELETON only. Vowel points and accents were
added to the Hebrew by the Masoretes c. 7th-10th c. CE — a thousand years after
the scrolls — so comparing them would report differences that are not textual
variants at all. Matres lectionis (ו/י used as vowel letters) are a real but
usually orthographic difference; they are counted separately as SPELLING.

Damage matters: the DSS corpus marks 53,864 signs as missing and 27,168 as
uncertain. A verse that is partly lacunose will look shorter than the Masoretic
text without any scribe having changed anything. Verses whose DSS text is
substantially damaged are reported as FRAGMENTARY, not as variants.

Usage:
    ./diverge.py Deut              # one book
    ./diverge.py Deut 32           # one chapter
    ./diverge.py --all             # every book with DSS coverage
    ./diverge.py Deut --spelling   # include orthographic-only differences
"""
import os, re, sys, unicodedata
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tf as TF

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OSIS = '{http://www.bibletechnologies.net/2003/OSIS/namespace}'
DSSDIR = f'{ROOT}/dead-sea-scrolls/etcbc-dss/tf/2.0'

HEB = re.compile(r'[א-ת]+')          # bare consonants only
MATRES = str.maketrans('', '', 'וי')

# The DSS corpus's `book` feature does NOT use morphhb's names. Two traps:
#   1. Different abbreviations — DSS "Is"/"Ex" vs morphhb "Isa"/"Exod". Without
#      this mapping the scan SILENTLY SKIPS those books, and Isaiah is the
#      largest biblical scroll in the corpus (1QIsaa, 24,078 words).
#   2. For unidentified or non-biblical material the field holds a SCROLL
#      acronym (11Q1, 4Q37, PAM43113, X4…) rather than a book name. Those are
#      not books and must not be counted as such.
DSS_TO_MORPHHB = {
    'Is': 'Isa', 'Ex': 'Exod', 'Ezek': 'Ezek', 'Eccl': 'Eccl',
    'XJudges': 'Judg',
}

def dss_book_name(b):
    """Map a DSS `book` value to a morphhb book name, or None if not a book."""
    if b in DSS_TO_MORPHHB:
        return DSS_TO_MORPHHB[b]
    # scroll acronyms: start with a digit, or match known non-book patterns
    if re.match(r'^\d|^PAM|^X\d|^Mur|^5/6Hev|^XHev', b):
        return None
    return b


def consonants(s):
    """Strip vowels, accents, punctuation — leave the consonantal skeleton."""
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return HEB.findall(s)


def mt_book(book):
    """{(ch,vs): [consonantal words]} for a Masoretic book."""
    p = f'{ROOT}/hebrew-ot/morphhb/wlc/{book}.xml'
    if not os.path.exists(p):
        return {}
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
                words.extend(consonants(w.text))
        out[(parts[1], parts[2])] = words
    return out


_dss = None

def dss_index():
    """{book: {(ch,vs): {scroll: [consonantal words]}}}

    Keyed BY SCROLL. Each scroll is a separate witness and must be compared to
    the Masoretic text on its own. Merging them (the original bug here) makes
    disagreements *between scrolls* look like disagreements with the MT — Deut
    32:8 alone returns 29 words from two scrolls where the MT has ~14.
    """
    global _dss
    if _dss is not None:
        return _dss
    import dssmap
    w2s = dssmap.word_to_scroll(DSSDIR)
    lo, hi = TF.node_range(DSSDIR, 'word')
    bk = TF.load(DSSDIR, 'book', lo, hi)
    cp = TF.load(DSSDIR, 'chapter', lo, hi)
    vr = TF.load(DSSDIR, 'verse', lo, hi)
    gl = TF.load(DSSDIR, 'glyph', lo, hi)
    bib = TF.load(DSSDIR, 'biblical', lo, hi)
    idx = {}
    for n in range(lo, hi + 1):
        b, c, v = bk.get(n), cp.get(n), vr.get(n)
        if not (b and c and v) or not bib.get(n):
            continue
        b = dss_book_name(b)
        if not b:
            continue
        sc = w2s.get(n, '?')
        (idx.setdefault(b, {}).setdefault((str(c), str(v)), {})
            .setdefault(sc, [])).extend(consonants(gl.get(n, '')))
    _dss = idx
    return idx


def compare(book, chapter=None, spelling=False):
    mt = mt_book(book)
    ds = dss_index().get(book, {})
    if not ds:
        return None
    rows = []
    for key in sorted(set(mt) & set(ds), key=lambda k: (int(k[0]), int(k[1]))):
        if chapter and key[0] != str(chapter):
            continue
        m = mt[key]
        if not m:
            continue
        for scroll, d in sorted(ds[key].items()):
            if not d:
                continue
            # damage heuristic: much shorter than MT = fragmentary, not a variant
            if len(d) < len(m) * 0.55:
                rows.append((key, 'FRAGMENTARY', m, d, scroll))
                continue
            if m == d:
                continue
            # orthographic-only? compare with matres lectionis removed
            if [w.translate(MATRES) for w in m] == [w.translate(MATRES) for w in d]:
                if spelling:
                    rows.append((key, 'SPELLING', m, d, scroll))
                continue
            sm, sd = set(m), set(d)
            only_d, only_m = sd - sm, sm - sd
            kind = 'CHANGED'
            if only_d and not only_m:
                kind = 'DSS-ONLY'
            elif only_m and not only_d:
                kind = 'MT-ONLY'
            rows.append((key, kind, m, d, scroll))
    return rows


def show(book, rows, limit=40):
    counts = {}
    for r in rows:
        counts[r[1]] = counts.get(r[1], 0) + 1
    total = sum(counts.values())
    print(f'\n{"="*74}')
    print(f'  {book} — {total} verses differ    ' +
          '  '.join(f'{k}:{v}' for k, v in sorted(counts.items())))
    print(f'{"="*74}')
    shown = 0
    for (ch, vs), kind, m, d, scroll in rows:
        if kind in ('FRAGMENTARY', 'SPELLING'):
            continue
        if shown >= limit:
            print(f'\n  … {total - shown} more (raise --limit)')
            break
        sm, sd = set(m), set(d)
        add, rem = sd - sm, sm - sd
        print(f'\n  {book} {ch}:{vs}   [{kind}]  scroll {scroll}')
        if add:
            print(f'     only in DSS : {" ".join(sorted(add))}')
        if rem:
            print(f'     only in MT  : {" ".join(sorted(rem))}')
        shown += 1


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    flags = {a for a in sys.argv[1:] if a.startswith('--')}
    spelling = '--spelling' in flags

    if '--all' in flags:
        idx = dss_index()
        grand = {}
        print(f'\nDSS biblical coverage: {len(idx)} books\n')
        print(f'{"book":8} {"shared":>7} {"changed":>8} {"dss-only":>9} '
              f'{"mt-only":>8} {"frag":>6} {"spell":>6}')
        print('-' * 60)
        for b in sorted(idx):
            rows = compare(b, spelling=True)
            if rows is None:
                continue
            c = {}
            for r in rows:
                c[r[1]] = c.get(r[1], 0) + 1
            shared = len(set(mt_book(b)) & set(idx[b]))
            if not shared:
                continue
            print(f'{b:8} {shared:7} {c.get("CHANGED",0):8} {c.get("DSS-ONLY",0):9} '
                  f'{c.get("MT-ONLY",0):8} {c.get("FRAGMENTARY",0):6} {c.get("SPELLING",0):6}')
            for k, v in c.items():
                grand[k] = grand.get(k, 0) + v
        print('-' * 60)
        print('TOTAL  ', '  '.join(f'{k}:{v}' for k, v in sorted(grand.items())))
        print('\nCHANGED / DSS-ONLY / MT-ONLY are real textual differences.')
        print('FRAGMENTARY = the scroll is damaged here, not a variant.')
        print('SPELLING    = matres lectionis only (ו/י as vowel letters).')
        return

    if not args:
        print(__doc__)
        sys.exit(1)
    book = args[0]
    chapter = args[1] if len(args) > 1 else None
    rows = compare(book, chapter, spelling)
    if rows is None:
        print(f'no DSS coverage for {book}')
        print('books with coverage:', ', '.join(sorted(dss_index())))
        return
    show(book, rows)


if __name__ == '__main__':
    main()
