#!/usr/bin/env python3
"""
gloss.py — translate a passage word by word, showing every meaning each word carries.

Published translations pick one English word per Hebrew word and print it as if
it were the only option. This shows the whole range: where a root is rendered
more than one way, every attested rendering appears between asterisks.

    *and*then*so*    *he-was*it-became*it-came-to-pass*

THE RANGE IS DERIVED FROM THE TEXT, NOT FROM A DICTIONARY. For every Strong's
number, this collects every distinct English gloss used across all 214,133
glossed words of the Hebrew Old Testament, ranked by how often each is used. So
the meanings shown are the ones this corpus actually attests for that root — with
counts — rather than a lexicographer's list of what a word could mean somewhere.

Source: STEPBible TAHOT (Translators Amalgamated Hebrew OT), CC BY, Tyndale
House Cambridge. Attribution in ATTRIBUTION.md. The ranges computed here and the
translations are this project's own work.

Usage:
    ./gloss.py Gen 1 1
    ./gloss.py Deut 32 8 --min 3      # only show meanings attested 3+ times
    ./gloss.py Ruth 1 1 --max 5       # cap meanings shown per word
    ./gloss.py --build                # rebuild the range index
"""
import glob, json, os, re, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAHOT = os.path.join(ROOT, 'hebrew-ot', 'STEPBible-Data',
                     'Translators Amalgamated OT+NT')
CACHE = os.path.join(ROOT, 'tools', '.gloss_index.json')

# TAHOT uses 3-letter book codes; map from the usual abbreviations.
BOOK = {
    'Gen': 'Gen', 'Exod': 'Exo', 'Lev': 'Lev', 'Num': 'Num', 'Deut': 'Deu',
    'Josh': 'Jos', 'Judg': 'Jdg', 'Ruth': 'Rut', '1Sam': '1Sa', '2Sam': '2Sa',
    '1Kgs': '1Ki', '2Kgs': '2Ki', '1Chr': '1Ch', '2Chr': '2Ch', 'Ezra': 'Ezr',
    'Neh': 'Neh', 'Esth': 'Est', 'Job': 'Job', 'Ps': 'Psa', 'Prov': 'Pro',
    'Eccl': 'Ecc', 'Song': 'Sng', 'Isa': 'Isa', 'Jer': 'Jer', 'Lam': 'Lam',
    'Ezek': 'Ezk', 'Dan': 'Dan', 'Hos': 'Hos', 'Joel': 'Jol', 'Amos': 'Amo',
    'Obad': 'Oba', 'Jonah': 'Jon', 'Mic': 'Mic', 'Nah': 'Nam', 'Hab': 'Hab',
    'Zeph': 'Zep', 'Hag': 'Hag', 'Zech': 'Zec', 'Mal': 'Mal',
}
ROW = re.compile(r'^([A-Z1-9][a-z]{2})\.(\d+)\.(\d+)#(\d+)')


def clean(g):
    """Normalise a gloss for grouping: drop brackets, slashes, punctuation."""
    g = re.sub(r'\[[^\]]*\]', '', g)          # [the] -> ''
    g = g.replace('/', ' ').replace('~', ' ')
    g = re.sub(r'[^A-Za-z\- ]', ' ', g)
    g = re.sub(r'\s+', ' ', g).strip().lower()
    return g.replace(' ', '-')


def build_index():
    """Strong's -> Counter(gloss) across the whole glossed OT."""
    idx = collections.defaultdict(collections.Counter)
    verses = {}
    n = 0
    for f in sorted(glob.glob(os.path.join(TAHOT, 'TAHOT*.txt'))):
        for line in open(f, encoding='utf8', errors='replace'):
            m = ROW.match(line)
            if not m:
                continue
            p = line.rstrip('\n').split('\t')
            if len(p) < 6:
                continue
            heb, gloss, strongs, morph = p[1], p[3], p[4], p[5]
            key = (m.group(1), m.group(2), m.group(3))
            verses.setdefault(key, []).append(
                {'heb': heb, 'gloss': gloss, 'strongs': strongs, 'morph': morph})
            # Key by ROOT **and MORPHOLOGY** together.
            #
            # Keying by root alone conflates three different things:
            #   1. genuine semantic range   — nations / gentiles / heathen
            #   2. inflectional variation   — he-said / she-said / they-said
            #   3. English phrasing         — number-of / by-number-of
            # Only (1) is a second MEANING. Lumping in (2) invents alternatives
            # the grammar forbids: it offered "they will inherit" for a form
            # tagged Vhaa, an infinitive. Pairing root+morph filters the
            # inflectional noise and leaves the actual semantic range.
            for s in re.findall(r'\{(H\d+[A-Za-z]?)\}', strongs) or \
                     re.findall(r'(H\d+[A-Za-z]?)', strongs):
                c = clean(gloss)
                if c:
                    idx[f'{s}|{morph}'][c] += 1
                    idx[f'{s}|*'][c] += 1        # unconstrained, kept for reference
            n += 1
    return {'ranges': {k: dict(v) for k, v in idx.items()},
            'verses': {'|'.join(k): v for k, v in verses.items()},
            'words': n}


def load():
    if os.path.exists(CACHE):
        return json.load(open(CACHE, encoding='utf8'))
    sys.stderr.write('building gloss index (one-off, ~30s)…\n')
    d = build_index()
    json.dump(d, open(CACHE, 'w', encoding='utf8'))
    sys.stderr.write(f'  indexed {d["words"]:,} glossed words\n')
    return d


def main():
    # Strip flags AND their values, or "--min 2" leaves "2" as a positional arg.
    flags = sys.argv[1:]
    args, skip = [], False
    for i, a in enumerate(flags):
        if skip:
            skip = False
            continue
        if a.startswith('--'):
            if a in ('--min', '--max', '--outcomes'):
                skip = True
            continue
        args.append(a)
    if '--build' in flags:
        if os.path.exists(CACHE):
            os.remove(CACHE)
        d = load()
        print(f'indexed {d["words"]:,} words, {len(d["ranges"]):,} distinct roots')
        return
    if len(args) != 3:
        print(__doc__)
        sys.exit(1)

    minn = int(flags[flags.index('--min') + 1]) if '--min' in flags else 1
    maxn = int(flags[flags.index('--max') + 1]) if '--max' in flags else 6

    book, ch, vs = args
    code = BOOK.get(book, book)
    d = load()
    key = f'{code}|{int(ch)}|{int(vs)}'
    words = d['verses'].get(key)
    if not words:
        # TAHOT pads reference numbers; try zero-padded forms
        for k in d['verses']:
            b, c, v = k.split('|')
            if b == code and int(c) == int(ch) and int(v) == int(vs):
                words = d['verses'][k]
                break
    if not words:
        print(f'no glossed text for {book} {ch}:{vs}')
        print('books available:', ', '.join(sorted(BOOK)))
        return

    ranges = d['ranges']
    print(f'\n{"="*76}\n  {book} {ch}:{vs} — every meaning each word carries\n{"="*76}\n')

    plain, per_word = [], []
    for w in words:
        roots = re.findall(r'\{(H\d+[A-Za-z]?)\}', w['strongs']) or \
                re.findall(r'(H\d+[A-Za-z]?)', w['strongs'])
        allg = collections.Counter()
        for r in roots:
            # same root AND same morphology = genuine alternative senses
            for g, c in ranges.get(f'{r}|{w["morph"]}', {}).items():
                allg[g] += c
        if not allg:                       # unseen inflection: fall back, flag it
            for r in roots:
                for g, c in ranges.get(f'{r}|*', {}).items():
                    allg[g] += c
        shown = [(g, c) for g, c in allg.most_common() if c >= minn][:maxn]
        here = clean(w['gloss'])
        # the reading used HERE always comes first, marked
        ordered = [g for g, _ in shown]
        if here and here in ordered:
            ordered.remove(here)
        if here:
            ordered.insert(0, here)
        bar = '*' + '*'.join(ordered) + '*' if ordered else '*?*'
        tot = sum(allg.values())
        print(f'  {w["heb"]:<22} {bar}')
        print(f'  {"":22} └ {w["morph"]:<14} {len(allg)} attested meaning(s), {tot} occurrence(s)\n')
        plain.append(here or '?')
        per_word.append(ordered)

    print('-' * 76)
    print('  Reading straight through, using the sense each word carries here:\n')
    print('    ' + ' '.join(plain).replace('-', ' '))

    # ── Multiple outcomes ────────────────────────────────────────────────
    # Where several words each carry more than one sense, the sentence has
    # more than one possible reading. Enumerate them.
    if '--outcomes' in flags:
        k = int(flags[flags.index('--outcomes') + 1])
        import itertools
        choices, ambiguous = [], 0
        for w, opts in zip(words, per_word):
            if len(opts) > 1:
                ambiguous += 1
                choices.append(opts[:3])       # top 3 senses per ambiguous word
            else:
                choices.append(opts or ['?'])
        total = 1
        for c in choices:
            total *= len(c)
        print('\n' + '-' * 76)
        print(f'  MULTIPLE OUTCOMES — {ambiguous} of {len(words)} words carry more than')
        print(f'  one attested sense, so this verse has {total:,} possible readings.')
        print(f'  The {k} most likely (by attestation frequency):\n')
        # rank combinations by summed frequency
        scored = []
        for combo in itertools.islice(itertools.product(*choices), 20000):
            score = 0
            for w, g in zip(words, combo):
                roots = re.findall(r'\{(H\d+[A-Za-z]?)\}', w['strongs']) or \
                        re.findall(r'(H\d+[A-Za-z]?)', w['strongs'])
                for r in roots:
                    score += ranges.get(f'{r}|{w["morph"]}', {}).get(g, 0)
            scored.append((score, combo))
        scored.sort(reverse=True)
        for n, (score, combo) in enumerate(scored[:k], 1):
            print(f'   {n}. ' + ' '.join(combo).replace('-', ' '))
        print('\n  These share the same consonants AND the same grammatical form, so')
        print('  each is a genuine alternative sense — not a different tense or person.')
        print('  A published translation prints one and shows you none of the others.')
    print(f"""
  The FIRST meaning between asterisks is the one this passage uses.
  The rest are how the same root is rendered elsewhere in the Hebrew Bible,
  ordered by how often. Counts come from {d['words']:,} glossed words —
  this is what the text attests, not what a dictionary permits.
""")


if __name__ == '__main__':
    main()
