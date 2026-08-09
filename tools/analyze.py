#!/usr/bin/env python3
"""
analyze.py — dump the grammatical analysis of a passage, for translation work.

This produces the RAW MATERIAL a translator works from and nothing else:
consonants, parsing codes, root identification, and the readings of every
witness on disk. It deliberately does NOT output an English gloss.

That omission is the point. Gloss files carry other translators' English, and a
translation built on them is a revision of their work, not a translation of the
Hebrew. The parsing codes are different in kind — "hiphil infinitive construct"
is a fact about the form, not a choice about meaning — so they are safe to use
and are what a translator actually needs.

Parse codes (Hebrew, morphhb / OSHM):
  first letter H = Hebrew, A = Aramaic
  V = verb    N = noun    A = adjective   R = preposition   C = conjunction
  T = particle  P = pronoun  S = suffix
  verb stems : q=qal  n=niphal  p=piel  P=pual  h=hiphil  H=hophal  t=hithpael
  verb forms : p=perfect  i=imperfect  w=wayyiqtol  c=infinitive construct
               a=infinitive absolute  v=imperative  r=participle  s=passive ptc
  noun       : c=common p=proper | m/f=gender | s/p/d=number | a=absolute
               c=construct  d=determined

Usage:
    ./analyze.py Deut 32 8
    ./analyze.py Gen 1 1 --range 1 5     # a span of verses
    ./analyze.py Gen 6 2 --witnesses     # include DSS / LXX / Samaritan readings
"""
import os, re, sys, subprocess, unicodedata
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OSIS = '{http://www.bibletechnologies.net/2003/OSIS/namespace}'

STEM = {'q': 'qal', 'n': 'niphal', 'p': 'piel', 'P': 'pual', 'h': 'hiphil',
        'H': 'hophal', 't': 'hithpael', 'o': 'polel', 'r': 'poel'}
FORM = {'p': 'perfect', 'i': 'imperfect', 'w': 'wayyiqtol', 'c': 'infinitive-construct',
        'a': 'infinitive-absolute', 'v': 'imperative', 'r': 'participle',
        's': 'passive-participle', 'j': 'jussive', 'h': 'cohortative'}
POS = {'V': 'verb', 'N': 'noun', 'A': 'adjective', 'R': 'preposition',
       'C': 'conjunction', 'T': 'particle', 'P': 'pronoun', 'S': 'suffix',
       'D': 'adverb'}


def explain(code):
    """Turn a morphhb parse code into plain words. Analysis, not translation."""
    if not code:
        return ''
    c = code[1:] if code[:1] in 'HA' else code
    out = []
    for seg in c.split('/'):
        if not seg:
            continue
        p = POS.get(seg[0], seg[0])
        if seg[0] == 'V' and len(seg) >= 3:
            bits = [p, STEM.get(seg[1], seg[1]), FORM.get(seg[2], seg[2])]
            if len(seg) > 3:
                bits.append(seg[3:])            # person/gender/number
            out.append(' '.join(bits))
        elif seg[0] == 'N' and len(seg) >= 4:
            kind = 'proper' if seg[1] == 'p' else 'common'
            g = {'m': 'masc', 'f': 'fem', 'b': 'both'}.get(seg[2], seg[2])
            n = {'s': 'sing', 'p': 'plur', 'd': 'dual'}.get(seg[3], seg[3])
            st = {'a': 'absolute', 'c': 'CONSTRUCT', 'd': 'determined'}.get(
                seg[4] if len(seg) > 4 else '', '')
            out.append(f'noun {kind} {g} {n} {st}'.strip())
        else:
            out.append(p + (' ' + seg[1:] if len(seg) > 1 else ''))
    return ' + '.join(out)


def bare(t):
    return ''.join(c for c in unicodedata.normalize('NFD', t)
                   if not unicodedata.combining(c))


def verse(book, ch, vs):
    p = f'{ROOT}/hebrew-ot/morphhb/wlc/{book}.xml'
    if not os.path.exists(p):
        return None
    want = f'{book}.{ch}.{vs}'
    for v in ET.parse(p).getroot().iter(f'{OSIS}verse'):
        if v.get('osisID') != want:
            continue
        out = []
        for w in v.iter():
            if w.tag.split('}')[-1] != 'w' or not w.text:
                continue
            out.append({'text': w.text, 'bare': bare(w.text),
                        'lemma': w.get('lemma') or '', 'morph': w.get('morph') or ''})
        return out
    return None


def main():
    flags = sys.argv[1:]
    args, skip = [], False
    for a in flags:
        if skip:
            skip = False
            continue
        if a.startswith('--'):
            if a == '--range':
                skip = True
            continue
        args.append(a)
    if len(args) < 3:
        print(__doc__)
        sys.exit(1)
    book, ch = args[0], int(args[1])
    v0 = int(args[2])
    v1 = int(flags[flags.index('--range') + 1]) if '--range' in flags else v0

    for vs in range(v0, v1 + 1):
        ws = verse(book, ch, vs)
        if not ws:
            continue
        print(f'\n{"="*78}\n  {book} {ch}:{vs}   — grammatical analysis only, no gloss\n{"="*78}')
        for w in ws:
            strongs = re.findall(r'\d+', w['lemma'])
            print(f'\n  {w["text"]}')
            print(f'     consonants : {w["bare"]}')
            print(f'     lemma      : {w["lemma"]}   (Strong\'s {", ".join(strongs) or "-"})')
            print(f'     parse      : {w["morph"]}')
            print(f'     i.e.       : {explain(w["morph"])}')
        if '--witnesses' in flags:
            print(f'\n  --- witnesses ---')
            try:
                r = subprocess.run(['python3', 'tools/allwitness.py', book, str(ch), str(vs)],
                                   cwd=ROOT, capture_output=True, text=True, timeout=300)
                print('\n'.join('  ' + l for l in r.stdout.splitlines()[3:]))
            except Exception as e:
                print(f'  [witnesses unavailable: {e}]')
    print()


if __name__ == '__main__':
    main()
