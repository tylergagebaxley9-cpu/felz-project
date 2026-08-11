#!/usr/bin/env python3
"""
corpus.py — one index of every word in the Hebrew Old Testament.

Everything downstream reads this instead of re-parsing 39 OSIS files. Each word
carries where it is, what it looks like, its root (Strong's) and its morphology.

WHAT IS DELIBERATELY ABSENT: any English. This index holds the text and the
grammatical facts about it, nothing else. The whole point of the translation
programme is that the English is derived by us, root by root, and recorded in
ranges/ with the evidence that justifies it. See PROVENANCE.md.

    ./corpus.py --build      build the index (~30s, writes .corpus_index.json)
    ./corpus.py --stats      what is in it
    ./corpus.py H0430        every occurrence of one root
"""
import json, os, re, sys, glob, collections, unicodedata
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WLC = os.path.join(ROOT, 'hebrew-ot', 'morphhb', 'wlc')
CACHE = os.path.join(ROOT, 'tools', '.corpus_index.json')
OSIS = '{http://www.bibletechnologies.net/2003/OSIS/namespace}'

# canonical order, so output is stable and reads as a Bible rather than as a dump
ORDER = ['Gen', 'Exod', 'Lev', 'Num', 'Deut', 'Josh', 'Judg', 'Ruth',
         '1Sam', '2Sam', '1Kgs', '2Kgs', '1Chr', '2Chr', 'Ezra', 'Neh',
         'Esth', 'Job', 'Ps', 'Prov', 'Eccl', 'Song', 'Isa', 'Jer', 'Lam',
         'Ezek', 'Dan', 'Hos', 'Joel', 'Amos', 'Obad', 'Jonah', 'Mic',
         'Nah', 'Hab', 'Zeph', 'Hag', 'Zech', 'Mal']


def bare(t):
    """Consonants only — strip vowel points and cantillation."""
    return ''.join(c for c in unicodedata.normalize('NFD', t)
                   if not unicodedata.combining(c))


def roots_of(lemma):
    """morphhb lemma -> Strong's roots. 'c/3068' or '1254 a' or 'b/9005'.

    A word can carry more than one root because prefixes are fused: the lemma
    'c/3068' is the conjunction ve- plus YHWH. Both are returned; the caller
    decides which carries the lexical weight (the LAST one always does).
    """
    out = []
    for part in str(lemma).split('/'):
        m = re.match(r'^([a-z]?)(\d+)([a-z]?)', part.strip())
        if not m:
            continue
        pre, num, suf = m.groups()
        if pre and not num:
            continue
        out.append(f'H{int(num):04d}{suf}')
    return out


def build():
    words, missing = [], []
    for book in ORDER:
        p = os.path.join(WLC, f'{book}.xml')
        if not os.path.exists(p):
            missing.append(book)
            continue
        for v in ET.parse(p).getroot().iter(f'{OSIS}verse'):
            oid = v.get('osisID')
            if not oid:
                continue
            _, ch, vs = oid.split('.')
            pos = 0
            for w in v.iter():
                if w.tag.split('}')[-1] != 'w' or not w.text:
                    continue
                rs = roots_of(w.get('lemma') or '')
                words.append({
                    'b': book, 'c': int(ch), 'v': int(vs), 'i': pos,
                    't': w.text, 'g': bare(w.text),
                    'r': rs[-1] if rs else '',        # lexical root
                    'all': rs,                         # incl. fused prefixes
                    'm': w.get('morph') or '',
                })
                pos += 1
    if missing:
        sys.stderr.write(f'WARNING: missing books {missing}\n')
    return words


def load():
    if os.path.exists(CACHE):
        return json.load(open(CACHE, encoding='utf8'))
    sys.stderr.write('building corpus index (one-off, ~30s)…\n')
    w = build()
    json.dump(w, open(CACHE, 'w', encoding='utf8'))
    return w


def occurrences(words, root):
    return [w for w in words if w['r'] == root]


def main():
    a = sys.argv[1:]
    if '--build' in a:
        if os.path.exists(CACHE):
            os.remove(CACHE)
        w = load()
        print(f'indexed {len(w):,} words')
        return
    w = load()
    if '--stats' in a or not a:
        books = collections.Counter(x['b'] for x in w)
        verses = len({(x['b'], x['c'], x['v']) for x in w})
        rooted = [x for x in w if x['r']]
        print(f'words          {len(w):>9,}')
        print(f'  with a root  {len(rooted):>9,}  '
              f'{100*len(rooted)/len(w):.1f}%')
        print(f'verses         {verses:>9,}')
        print(f'books          {len(books):>9}')
        print(f'distinct roots {len({x["r"] for x in rooted}):>9,}')
        return
    root = a[0].upper()
    if not root.startswith('H'):
        root = f'H{int(root):04d}'
    occ = occurrences(w, root)
    print(f'{root}: {len(occ):,} occurrences')
    for x in occ[:40]:
        print(f'  {x["b"]} {x["c"]}:{x["v"]:<4} {x["t"]:<20} {x["m"]}')
    if len(occ) > 40:
        print(f'  … and {len(occ)-40:,} more')


if __name__ == '__main__':
    main()
