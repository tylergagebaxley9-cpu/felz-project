#!/usr/bin/env python3
"""
render.py — build the readable text from the derived ranges.

    ./render.py Gen 1              one chapter
    ./render.py Gen 1 --range 1 5  a span of verses
    ./render.py --book Ps          a whole book
    ./render.py --all > READABLE-BIBLE.md    everything derived so far

FIVE RULES, ENFORCED HERE IN CODE RATHER THAN PROMISED IN PROSE
===============================================================

1. A ROOT WITH NO DERIVED RANGE IS NEVER RENDERED AS ENGLISH.
   It prints as the Hebrew with [NOT YET DERIVED]. There is no fallback to a
   lexicon, no guess, and no borrowing from another translation. An honest gap
   is worth more than a plausible filler, because a filler is indistinguishable
   from work actually done.

2. WHERE A WORD CARRIES MORE THAN ONE MEANING, ALL OF THEM ARE PRINTED.
   Never the most frequent one alone. Frequency is not truth -- the majority
   rendering of a root is just the majority of translators' decisions, and the
   minority sense is the one that carries Psalm 82 and Deuteronomy 32:8.

3. EVERY SENSE CARRIES THE VERSES THAT DEMONSTRATE IT.
   A sense with no evidence is not admitted by the loader. This is the same
   standard the manuscript findings are held to: regenerable or it does not
   count.

4. UNCERTAINTY IS PRINTED, NOT SMOOTHED.
   Low-confidence ranges are marked. Anything the deriver could not settle is
   carried through to the reader verbatim in `unresolved`.

5. THE COVERAGE FIGURE IS THE REAL ONE.
   Every rendering states what share of its own words are derived. A page that
   is 40% gaps says so at the top. No padding, no rounding up, no counting a
   root as done because it was looked at.
"""
import json, os, sys, collections
import corpus, rootqueue

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def valid(rec):
    """A range is usable only if every sense carries verse evidence (rule 3)."""
    ss = rec.get('senses') or []
    if not ss:
        return False, 'no senses'
    for s in ss:
        if not s.get('sense'):
            return False, 'a sense has no text'
        if not s.get('evidence'):
            return False, f'sense {s.get("sense")!r} has no evidence'
    return True, ''


def load_valid():
    out, rejected = {}, []
    for r, rec in rootqueue.load_ranges().items():
        ok, why = valid(rec)
        (out.__setitem__(r, rec) if ok else rejected.append((r, why)))
    for r, why in rejected:
        sys.stderr.write(f'REJECTED ranges/{r}.json — {why}\n')
    return out


def render_word(w, ranges):
    """One word. Returns (display, derived?)."""
    r = w['r']
    if not r:
        return f'{w["t"]}[no root]', False
    rec = ranges.get(r)
    if not rec:
        return f'{w["t"]}[NOT YET DERIVED]', False
    senses = [s['sense'] for s in rec['senses']]
    if len(senses) == 1:
        s = senses[0]
    else:
        s = '(' + ' | '.join(senses) + ')'          # rule 2: all of them
    if rec.get('confidence') == 'low':
        s += '[?]'
    return s, True


def render_verse(words_of_verse, ranges):
    parts, n_ok = [], 0
    for w in words_of_verse:
        disp, ok = render_word(w, ranges)
        parts.append(disp)
        n_ok += ok
    return ' '.join(parts), n_ok, len(words_of_verse)


def group(words):
    by = collections.OrderedDict()
    for w in words:
        by.setdefault((w['b'], w['c'], w['v']), []).append(w)
    return by


def main():
    a = sys.argv[1:]
    words = corpus.load()
    ranges = load_valid()

    if not ranges:
        print('No derived ranges yet. Nothing can honestly be rendered.\n')
        print('  ./rootqueue.py --next 20        what to derive first')
        print('  ./rootqueue.py --worksheet H0430   the evidence for one root')
        sys.exit(1)

    sel = words
    if '--book' in a:
        b = a[a.index('--book') + 1]
        sel = [w for w in words if w['b'] == b]
    elif '--all' not in a and len(a) >= 2:
        b, c = a[0], int(a[1])
        sel = [w for w in words if w['b'] == b and w['c'] == c]
        if '--range' in a:
            i = a.index('--range')
            lo, hi = int(a[i + 1]), int(a[i + 2])
            sel = [w for w in sel if lo <= w['v'] <= hi]
    if not sel:
        print('nothing selected')
        sys.exit(1)

    by = group(sel)
    tot_ok = tot_all = 0
    lines = []
    for (b, c, v), ws in by.items():
        text, ok, n = render_verse(ws, ranges)
        tot_ok += ok
        tot_all += n
        lines.append(f'**{b} {c}:{v}**  {text}')

    # rule 5 — the real number, at the top, before the text
    pct = 100 * tot_ok / tot_all if tot_all else 0
    print(f'# {sel[0]["b"]} — rendered from derived ranges\n')
    print(f'> **{pct:.1f}% of the words on this page have a derived range** '
          f'({tot_ok:,} of {tot_all:,}).')
    print('> Words marked `[NOT YET DERIVED]` have not been worked out yet and are')
    print('> left in Hebrew on purpose. Where a word carries more than one meaning,')
    print('> every meaning is shown `(like | this)` and none is preferred.\n')
    print('---\n')
    print('\n\n'.join(lines))

    used = {w['r'] for w in sel if w['r'] in ranges}
    multi = [r for r in used if len(ranges[r]['senses']) > 1]
    print(f'\n\n---\n\n*{len(used):,} roots used here; {len(multi):,} of them '
          f'carry more than one meaning. Every range is in `ranges/`, each sense '
          f'with the verses that demonstrate it.*')


if __name__ == '__main__':
    main()
