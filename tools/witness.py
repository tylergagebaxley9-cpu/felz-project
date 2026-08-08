#!/usr/bin/env python3
"""
witness.py — pull a single passage from every textual tradition on disk.

Nothing here is quoted from memory. Every reading is read out of the corpus
files at run time, so a claim about what a tradition says can always be
re-derived and checked.

Usage:
    ./witness.py Deut 32 8
    ./witness.py Heb 1 6
    ./witness.py Gen 4 8
"""
import sys, csv, glob, os
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OSIS = '{http://www.bibletechnologies.net/2003/OSIS/namespace}'

# LXX book numbers follow Rahlfs order in 12-Marvel.Bible/00-versification_original.csv
LXX_BOOK = {
    'Gen':1,'Exod':2,'Lev':3,'Num':4,'Deut':5,'Josh':6,'Judg':7,'Ruth':8,
    '1Sam':9,'2Sam':10,'1Kgs':11,'2Kgs':12,'1Chr':13,'2Chr':14,
    'Ps':'?','Isa':'?','Jer':'?',   # verify against book_Rahlfs.csv before trusting
}

NT_FILES = None  # lazy


def masoretic(book, ch, vs):
    """Westminster Leningrad Codex — witness 1008 CE."""
    p = f'{ROOT}/hebrew-ot/morphhb/wlc/{book}.xml'
    if not os.path.exists(p):
        return None
    want = f'{book}.{ch}.{vs}'
    for v in ET.parse(p).getroot().iter(f'{OSIS}verse'):
        if v.get('osisID') != want:
            continue
        words = []
        for w in v.iter():
            tag = w.tag.split('}')[-1]
            if tag in ('w', 'seg') and w.text:
                words.append(w.text)
        return ' '.join(words)
    return None


_lxx_cache = {}

def septuagint(book, ch, vs):
    """Rahlfs 1935 — rests mainly on Vaticanus, c. 300-325 CE."""
    bn = LXX_BOOK.get(book)
    if not isinstance(bn, int):
        return None
    base = f'{ROOT}/septuagint/LXX-Rahlfs-1935'
    if not _lxx_cache:
        vsx = []
        vf = f'{base}/12-Marvel.Bible/00-versification_original.csv'
        if not os.path.exists(vf):
            return None
        for r in csv.reader(open(vf, encoding='utf8'), delimiter='\t'):
            if len(r) >= 2 and r[1].startswith('†'):
                vsx.append((int(r[0]), r[1][1:]))
        vsx.sort()
        idx = {}
        for i, (start, ref) in enumerate(vsx):
            end = vsx[i+1][0] if i+1 < len(vsx) else 10**9
            idx[ref] = (start, end)
        words = {}
        for r in csv.reader(open(f'{base}/01_wordlist_unicode/text_accented.csv',
                                 encoding='utf8'), delimiter='\t'):
            if len(r) >= 3:
                try:
                    words[int(r[0])] = r[2]
                except ValueError:
                    pass
        _lxx_cache['idx'] = idx
        _lxx_cache['words'] = words
    ref = f'{bn}.{ch}.{vs}'
    if ref not in _lxx_cache['idx']:
        return None
    a, b = _lxx_cache['idx'][ref]
    w = _lxx_cache['words']
    return ' '.join(w[i] for i in range(a, b) if i in w)


def nestle(book, ch, vs):
    """Nestle 1904 Greek NT — eclectic, edition 1904."""
    global NT_FILES
    if NT_FILES is None:
        NT_FILES = {}
        for p in glob.glob(f'{ROOT}/greek-nt/Nestle1904/xml/*.xml'):
            try:
                r = ET.parse(p).getroot()
            except ET.ParseError:
                continue
            d = r.find('.//div') if r.tag != 'div' else r
            oid = (d.get('osisID') if d is not None else None) or ''
            if oid:
                NT_FILES[oid] = p
    p = NT_FILES.get(book)
    if not p:
        return None
    want = f'{book}.{ch}.{vs}'
    out = []
    for w in ET.parse(p).getroot().iter('w'):
        oid = w.get('osisId', '')
        if oid.split('!')[0] == want:
            out.append(w.text or '')
    return ' '.join(out) if out else None


WITNESSES = [
    ('Masoretic (Leningrad Codex)',        '1008 CE',          masoretic),
    ('Septuagint (Rahlfs / Vaticanus)',    'c. 300-325 CE',    septuagint),
    ('Greek NT (Nestle 1904)',             'ed. 1904',         nestle),
]


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)
    book, ch, vs = sys.argv[1], sys.argv[2], sys.argv[3]
    print(f'\n=== {book} {ch}:{vs} ===\n')
    found = 0
    for name, date, fn in WITNESSES:
        try:
            t = fn(book, ch, vs)
        except Exception as e:
            print(f'{name:36} [{date:14}]  ERROR: {e}')
            continue
        if t:
            found += 1
            print(f'{name}  [witness {date}]')
            print(f'  {t}\n')
    if not found:
        print('  no witness on disk carries this reference')
        print('  (check the book abbreviation, and LXX_BOOK for OT books)')


if __name__ == '__main__':
    main()
