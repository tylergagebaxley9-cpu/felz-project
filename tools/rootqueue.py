#!/usr/bin/env python3
"""
rootqueue.py — what to translate next, and the evidence to translate it with.

THE UNIT OF WORK IS THE ROOT, NOT THE VERSE. There are 8,640 roots across
306,785 words. Settle a root's range once and it applies everywhere it occurs,
so the work is finite in a way that word-by-word translation is not:

    130 roots -> 50% of the text      1,889 roots -> 90%
    627 roots -> 75%                  3,213 roots -> 95%

WHERE A ROOT MEANS MORE THAN ONE THING, EVERY MEANING IS RECORDED. That is the
point of the whole exercise, not a footnote to it. A sense is only admitted with
verse references that demonstrate it, so a reader can check the range the same
way they can check a manuscript reading.

    ./rootqueue.py --next 20          the 20 highest-value undone roots
    ./rootqueue.py --coverage         how much of the Bible is covered so far
    ./rootqueue.py --worksheet H0430  all evidence needed to derive one root
"""
import json, os, sys, collections
import corpus

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RANGES = os.path.join(ROOT, 'ranges')

# ── The record written for every root ────────────────────────────────────────
# ranges/<STRONGS>.json
#
# {
#   "root":     "H0430",
#   "lemma":    "אלהים",              consonants as they appear
#   "occurrences": 2600,
#   "senses": [                        EVERY meaning, most frequent first
#     {"sense":    "God",
#      "evidence": ["Gen.1.1", "Deut.6.4"],     verses that demonstrate it
#      "when":     "singular verb agreement",   what selects this sense, if
#      "note":     "..."},                      anything does
#     {"sense":    "gods",
#      "evidence": ["Ps.82.1", "Exod.20.3"]}
#   ],
#   "method":     "corpus-distribution",
#   "derived_on": "2026-08-11",
#   "confidence": "high" | "medium" | "low",
#   "unresolved": "what could not be settled from the evidence"
# }
#
# A root with two senses and no way to choose between them KEEPS BOTH. The
# renderer prints both. Nothing is silently resolved -- that rule is inherited
# from STUDY-BOOK.md and is the reason this project exists.
# ─────────────────────────────────────────────────────────────────────────────


def load_ranges():
    out = {}
    if not os.path.isdir(RANGES):
        return out
    for f in os.listdir(RANGES):
        if f.endswith('.json'):
            try:
                d = json.load(open(os.path.join(RANGES, f), encoding='utf8'))
                out[d['root']] = d
            except (json.JSONDecodeError, KeyError) as e:
                sys.stderr.write(f'WARNING: {f} unreadable ({e})\n')
    return out


def freq(words):
    return collections.Counter(w['r'] for w in words if w['r'])


def coverage(words, done=None):
    """Share of word occurrences whose root has a derived range."""
    done = load_ranges() if done is None else done
    f = freq(words)
    total = sum(f.values())
    got = sum(c for r, c in f.items() if r in done)
    return got, total, len(done), len(f)


def worksheet(words, root, limit=60):
    """Every fact needed to derive one root's range. NO ENGLISH ANYWHERE."""
    occ = [w for w in words if w['r'] == root]
    if not occ:
        print(f'{root}: no occurrences')
        return
    forms = collections.Counter(w['g'] for w in occ)
    morphs = collections.Counter(w['m'] for w in occ)
    books = collections.Counter(w['b'] for w in occ)

    print(f'\n{"="*78}\n  {root} — {len(occ):,} occurrences\n{"="*78}')
    print(f'\n  DISTINCT WRITTEN FORMS ({len(forms)}):')
    for g, c in forms.most_common(12):
        print(f'    {g:<22} {c:>6,}')
    print(f'\n  MORPHOLOGY ({len(morphs)} distinct):')
    for m, c in morphs.most_common(12):
        print(f'    {m:<22} {c:>6,}   {corpus_explain(m)}')
    print(f'\n  SPREAD: {len(books)} books; '
          f'{", ".join(f"{b}={c}" for b, c in books.most_common(8))}')

    print(f'\n  OCCURRENCES IN CONTEXT (first {limit}) —')
    print('  the surrounding words are what the sense has to be derived FROM:\n')
    by_verse = collections.defaultdict(list)
    for w in words:
        by_verse[(w['b'], w['c'], w['v'])].append(w)
    seen = 0
    for w in occ:
        if seen >= limit:
            break
        key = (w['b'], w['c'], w['v'])
        line = by_verse[key]
        ctx = ' '.join(('[' + x['t'] + ']') if x['i'] == w['i'] else x['t']
                       for x in line)
        print(f'  {w["b"]} {w["c"]}:{w["v"]:<4} {w["m"]:<16} {ctx}')
        seen += 1
    if len(occ) > limit:
        print(f'\n  … and {len(occ)-limit:,} more occurrences')
    print(f'\n  Write the result to ranges/{root}.json — every sense, each with')
    print('  verse evidence. If two senses cannot be told apart, KEEP BOTH.\n')


def corpus_explain(m):
    try:
        import analyze
        return analyze.explain(m)
    except Exception:
        return ''


def main():
    a = sys.argv[1:]
    words = corpus.load()
    done = load_ranges()

    if '--coverage' in a:
        got, total, nd, nr = coverage(words, done)
        print(f'roots derived     {nd:>8,} of {nr:,}')
        print(f'word occurrences  {got:>8,} of {total:,}')
        print(f'TEXT COVERED      {100*got/total:>7.2f}%')
        if nd:
            multi = sum(1 for d in done.values() if len(d.get('senses', [])) > 1)
            print(f'\nof the {nd:,} derived, {multi:,} carry more than one meaning')
        return

    if '--worksheet' in a:
        i = a.index('--worksheet')
        if i + 1 >= len(a):
            print('need a root, e.g. --worksheet H0430')
            sys.exit(1)
        worksheet(words, a[i + 1].upper())
        return

    n = 20
    if '--next' in a:
        i = a.index('--next')
        if i + 1 < len(a) and a[i + 1].isdigit():
            n = int(a[i + 1])
    f = freq(words)
    total = sum(f.values())
    todo = [(r, c) for r, c in f.most_common() if r not in done]
    print(f'{len(done):,} roots done; {len(todo):,} remain\n')
    print(f'{"root":<10}{"occurs":>8}{"% of text":>11}   running total')
    got = sum(c for r, c in f.items() if r in done)
    run = got
    for r, c in todo[:n]:
        run += c
        print(f'{r:<10}{c:>8,}{100*c/total:>10.2f}%   {100*run/total:>6.2f}%')


if __name__ == '__main__':
    main()
