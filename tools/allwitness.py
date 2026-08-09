#!/usr/bin/env python3
"""
allwitness.py — one passage, every witness on disk, dated and labelled.

The point of the corpus in one command. Nothing is quoted from memory; every
reading is read out of the source files at run time, so any claim about what a
tradition says can be regenerated and checked.

Each witness prints with:
  * a PROVENANCE label — ORIGINAL (a manuscript), TRANSLATION (someone rendered
    it out of another language), EDITED (a modern reconstruction from many
    manuscripts), PRINTED (a pre-1820 printed edition)
  * the WITNESS date (when the manuscript was made) and, where different, the
    EDITION date (when this version was published)

Silence is meaningful. A witness that is on disk but has no text for the
reference is reported as ABSENT — that is evidence, not a gap.

Usage:
    ./allwitness.py Deut 32 8
    ./allwitness.py Mark 16 9
    ./allwitness.py 1John 5 7
    ./allwitness.py John 7 53 --greek-only
"""
import json, os, re, sys, glob
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tf as TF

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OSIS = '{http://www.bibletechnologies.net/2003/OSIS/namespace}'

# ── book naming ──────────────────────────────────────────────────────────────
# CNTR encodes books as 2-digit numbers, 40=Matthew … 66=Revelation.
CNTR_BOOK = {
    'Matt': 40, 'Mark': 41, 'Luke': 42, 'John': 43, 'Acts': 44, 'Rom': 45,
    '1Cor': 46, '2Cor': 47, 'Gal': 48, 'Eph': 49, 'Phil': 50, 'Col': 51,
    '1Thess': 52, '2Thess': 53, '1Tim': 54, '2Tim': 55, 'Titus': 56,
    'Phlm': 57, 'Heb': 58, 'Jas': 59, '1Pet': 60, '2Pet': 61, '1John': 62,
    '2John': 63, '3John': 64, 'Jude': 65, 'Rev': 66,
}
LXX_BOOK = {
    'Gen': 1, 'Exod': 2, 'Lev': 3, 'Num': 4, 'Deut': 5, 'Josh': 6, 'Judg': 7,
    'Ruth': 8, '1Sam': 9, '2Sam': 10, '1Kgs': 11, '2Kgs': 12, '1Chr': 13,
    '2Chr': 14,
}
# Targum directory + Sefaria book name
TARGUM_BOOKS = {
    'Isa': ('jonathan-prophets', 'Isaiah'), 'Jer': ('jonathan-prophets', 'Jeremiah'),
    'Ezek': ('jonathan-prophets', 'Ezekiel'), 'Josh': ('jonathan-prophets', 'Joshua'),
    'Judg': ('jonathan-prophets', 'Judges'), 'Ps': ('writings', 'Psalms'),
    'Job': ('writings', 'Job'), 'Prov': ('writings', 'Proverbs'),
    'Ruth': ('writings', 'Ruth'), 'Esth': ('writings', 'Esther'),
    'Eccl': ('writings', 'Ecclesiastes'), 'Lam': ('writings', 'Lamentations'),
}
# Key CNTR witnesses, in date order. GA siglum -> (label, date)
CNTR_WITNESSES = [
    ('P52',  'P52 (John frag.)',        'c. 125–175 CE'),
    ('P45',  'P45',                      'c. 250 CE'),
    ('P46',  'P46',                      'c. 175–225 CE'),
    ('P66',  'P66',                      'c. 200 CE'),
    ('P72',  'P72',                      'c. 250–350 CE'),
    ('P75',  'P75',                      'c. 175–225 CE'),
    ('03',   'Codex Vaticanus (B)',      'c. 300–325 CE'),
    ('01',   'Codex Sinaiticus (ℵ)',     'c. 330–360 CE'),
    ('02',   'Codex Alexandrinus (A)',   'c. 400–440 CE'),
    ('04',   'Codex Ephraemi (C)',       'c. 450 CE'),
    ('05',   'Codex Bezae (D)',          'c. 400 CE'),
    ('032',  'Codex Washingtonianus (W)', 'c. 400–450 CE'),
]

_cache = {}


# ── Hebrew: Masoretic ────────────────────────────────────────────────────────
def masoretic(book, ch, vs):
    p = f'{ROOT}/hebrew-ot/morphhb/wlc/{book}.xml'
    if not os.path.exists(p):
        return None
    want = f'{book}.{ch}.{vs}'
    for v in ET.parse(p).getroot().iter(f'{OSIS}verse'):
        if v.get('osisID') != want:
            continue
        return ' '.join(w.text for w in v.iter()
                        if w.tag.split('}')[-1] in ('w', 'seg') and w.text)
    return None


# ── Hebrew: Dead Sea Scrolls ─────────────────────────────────────────────────
def dss(book, ch, vs):
    """Return the reading PER SCROLL, never merged into one line.

    Merging is not a display nicety — it destroys evidence. Gen 1:5 is carried by
    two scrolls: 4Q2 reads יום ("Day"), 4Q7 reads יומם ("Daytime"). Merged, that
    variant is invisible, and this tool hid it until a translator went to the raw
    node tables and found it. Same hazard documented in dssmap.py; fixed here too.
    """
    d = f'{ROOT}/dead-sea-scrolls/etcbc-dss/tf/2.0'
    if not os.path.isdir(d):
        return None
    if 'dss' not in _cache:
        import dssmap
        lo, hi = TF.node_range(d, 'word')
        _cache['dss'] = (lo, hi,
                         TF.load(d, 'book', lo, hi), TF.load(d, 'chapter', lo, hi),
                         TF.load(d, 'verse', lo, hi), TF.load(d, 'glyph', lo, hi),
                         TF.load(d, 'script', lo, hi), dssmap.word_to_scroll(d))
    lo, hi, bk, cp, vr, gl, sc, w2s = _cache['dss']
    per = {}
    for n in range(lo, hi + 1):
        if bk.get(n) == book and str(cp.get(n)) == str(ch) and str(vr.get(n)) == str(vs):
            g = gl.get(n, '')
            if sc.get(n) == 'paleohebrew':
                g += ' [paleo]'
            per.setdefault(w2s.get(n, '?'), []).append(g)
    if not per:
        return None
    if len(per) == 1:
        only = next(iter(per.items()))
        return f'[{only[0]}] ' + ' '.join(only[1]).strip()
    lines, texts = [], set()
    for scroll, ws in sorted(per.items()):
        t = ' '.join(ws).strip()
        texts.add(t)
        lines.append(f'[{scroll}] {t}')
    head = '\u26a0 SCROLLS DISAGREE\n     ' if len(texts) > 1 else ''
    return head + '\n     '.join(lines)


# ── Hebrew: Samaritan Pentateuch ─────────────────────────────────────────────
def samaritan(book, ch, vs):
    cands = sorted(glob.glob(f'{ROOT}/samaritan/sp/tf/*/'),
                   key=lambda p: [int(x) for x in p.strip('/').split('/')[-1].split('.')])
    if not cands:
        return None
    d = cands[-1]
    if 'sp' not in _cache:
        try:
            lo, hi = TF.node_range(d, 'word')
        except (KeyError, FileNotFoundError):
            return None
        feats = {}
        for f in ('book', 'chapter', 'verse', 'g_cons_utf8', 'g_cons'):
            try:
                feats[f] = TF.load(d, f, lo, hi)
            except FileNotFoundError:
                feats[f] = {}
        _cache['sp'] = (lo, hi, feats)
    lo, hi, feats = _cache['sp']
    txtf = 'g_cons_utf8' if feats.get('g_cons_utf8') else 'g_cons'
    ns = [n for n in range(lo, hi + 1)
          if str(feats['book'].get(n, '')).startswith(book[:3])
          and str(feats['chapter'].get(n)) == str(ch)
          and str(feats['verse'].get(n)) == str(vs)]
    if not ns:
        return None
    return ' '.join(feats[txtf].get(n, '') for n in ns).strip() or None


# ── Greek: Septuagint ────────────────────────────────────────────────────────
def septuagint(book, ch, vs):
    bn = LXX_BOOK.get(book)
    if not bn:
        return None
    base = f'{ROOT}/septuagint/LXX-Rahlfs-1935'
    if 'lxx' not in _cache:
        import csv
        vf = f'{base}/12-Marvel.Bible/00-versification_original.csv'
        if not os.path.exists(vf):
            return None
        vsx = sorted((int(r[0]), r[1][1:])
                     for r in csv.reader(open(vf, encoding='utf8'), delimiter='\t')
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
        _cache['lxx'] = (idx, words)
    idx, words = _cache['lxx']
    ref = f'{bn}.{ch}.{vs}'
    if ref not in idx:
        return None
    a, b = idx[ref]
    return ' '.join(words[i] for i in range(a, b) if i in words) or None


# ── Greek NT: OSIS-XML editions ──────────────────────────────────────────────
def _osis_nt(subdir, book, ch, vs):
    key = f'nt:{subdir}'
    if key not in _cache:
        m = {}
        for p in glob.glob(f'{ROOT}/greek-nt/{subdir}/xml/*.xml'):
            try:
                r = ET.parse(p).getroot()
            except ET.ParseError:
                continue
            for d in r.iter():
                if d.tag.split('}')[-1] == 'div' and d.get('osisID'):
                    m[d.get('osisID')] = p
                    break
        _cache[key] = m
    p = _cache[key].get(book)
    if not p:
        return None
    want = f'{book}.{ch}.{vs}'
    out = [w.text or '' for w in ET.parse(p).getroot().iter('w')
           if w.get('osisId', '').split('!')[0] == want]
    return ' '.join(out).strip() or None


def nestle(book, ch, vs):
    return _osis_nt('Nestle1904', book, ch, vs)


# ── Greek NT: CNTR manuscript transcriptions ─────────────────────────────────
MES_STRIP = re.compile(r'[\\|/&%^~+=$\[\]{}]')

def cntr(siglum, book, ch, vs):
    bn = CNTR_BOOK.get(book)
    if not bn:
        return None, None
    for sub in ('class 1', 'class 2', 'class 3'):
        p = f'{ROOT}/papyri/cntr-transcriptions/{sub}/{siglum}.txt'
        if os.path.exists(p):
            break
    else:
        return None, None
    tag = f'{bn:02d}{int(ch):03d}{int(vs):03d}'
    for line in open(p, encoding='utf8', errors='replace'):
        if line.startswith(tag):
            raw = line[len(tag):].strip()
            if raw == '-':
                return None, 'ABSENT'          # verse deliberately not in this MS
            txt = MES_STRIP.sub('', raw)
            txt = re.sub(r'\s+', ' ', txt).strip()
            return (txt or None), None
    return None, 'not extant'                  # MS damaged/lost here, not a verdict


# ── Targums ──────────────────────────────────────────────────────────────────
def targum(book, ch, vs):
    spec = TARGUM_BOOKS.get(book)
    if not spec:
        return None
    sub, name = spec
    p = f'{ROOT}/targums/{sub}/{name.replace(" ", "_")}.json'
    if not os.path.exists(p):
        return None
    d = json.load(open(p, encoding='utf8'))
    ch_l = d.get('chapters', {}).get(str(ch)) or []
    i = int(vs) - 1
    if 0 <= i < len(ch_l):
        t = re.sub(r'<[^>]+>', '', ch_l[i]).strip()
        return t or None
    return None


# ── main ─────────────────────────────────────────────────────────────────────
def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    flags = {a for a in sys.argv[1:] if a.startswith('--')}
    if len(args) != 3:
        print(__doc__)
        sys.exit(1)
    book, ch, vs = args
    greek_only = '--greek-only' in flags

    print(f'\n{"="*74}\n  {book} {ch}:{vs}\n{"="*74}')

    hebrew = [
        ('Dead Sea Scrolls',          'ORIGINAL',    'c. 250 BCE – 68 CE', lambda: dss(book, ch, vs)),
        ('Samaritan Pentateuch',      'ORIGINAL',    'MS 12th–13th c. CE', lambda: samaritan(book, ch, vs)),
        ('Masoretic (Leningrad)',     'ORIGINAL',    '1008 CE',            lambda: masoretic(book, ch, vs)),
        ('Septuagint (Rahlfs)',       'TRANSLATION', 'transl. c. 250–100 BCE; MS c. 300–325 CE; ed. 1935',
                                                                            lambda: septuagint(book, ch, vs)),
        ('Targum',                    'TRANSLATION', 'c. 2nd–9th c. CE',   lambda: targum(book, ch, vs)),
    ]

    shown = 0
    if not greek_only:
        for name, prov, date, fn in hebrew:
            try:
                t = fn()
            except Exception as e:
                print(f'\n  {name}\n     ERROR: {type(e).__name__}: {e}')
                continue
            if t:
                shown += 1
                print(f'\n  {name}  [{prov} · {date}]')
                print(f'     {t}')

    # Greek NT manuscripts
    ms_lines, absent = [], []
    for sig, label, date in CNTR_WITNESSES:
        t, note = cntr(sig, book, ch, vs)
        if t:
            ms_lines.append((label, date, t))
        elif note == 'ABSENT':
            absent.append((label, date))
    for label, date, t in ms_lines:
        shown += 1
        print(f'\n  {label}  [ORIGINAL · {date}]')
        print(f'     {t}')

    for name, prov, date, fn in [
        ('Nestle 1904',        'EDITED',  'ed. 1904', lambda: nestle(book, ch, vs)),
    ]:
        t = fn()
        if t:
            shown += 1
            print(f'\n  {name}  [{prov} · {date}]')
            print(f'     {t}')

    if absent:
        print(f'\n  {"-"*70}')
        print('  ABSENT — these manuscripts are extant here but do NOT contain this verse:')
        for label, date in absent:
            print(f'     ✗ {label}  ({date})')

    if not shown and not absent:
        print('\n  no witness on disk carries this reference')
        print('  (check the book abbreviation; OT books need an LXX_BOOK entry)')
    print()


if __name__ == '__main__':
    main()
