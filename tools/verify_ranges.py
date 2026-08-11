#!/usr/bin/env python3
"""
verify_ranges.py — prove every derived range is honest, or fail loudly.

Run this before trusting any rendering, and before any commit that touches
ranges/. It exits non-zero if anything fails, so it works as a gate.

WHAT IT PROVES
  1. Schema      — every range has a root and at least one sense.
  2. Evidence    — every sense cites at least one verse.
  3. CITATION    — every cited verse REALLY CONTAINS THAT ROOT, checked against
                   the corpus index. This is the one that matters. It makes
                   fabricated evidence impossible rather than discouraged.
  4. Duplicates  — the same sense is not listed twice for one root.
  5. Homographs  — roots that warn about each other both exist.

WHAT IT CANNOT PROVE, STATED PLAINLY
  That a SENSE IS CORRECT. A verse containing a root does not demonstrate that
  the root means what the record claims there. That is judgment, and judgment
  is not mechanically checkable. This tool guarantees that every claim is
  ATTACHED TO CHECKABLE EVIDENCE -- it does not guarantee the claim is right.
  Anyone reading a range is expected to open the verses and disagree.

  This limit is written here rather than glossed over because the whole project
  refuses claims it cannot support, and a validator that implied it certified
  meaning would be exactly such a claim.

WHY IT EXISTS
  The first 13 roots were derived with three bad citations in them, all the same
  fault: quoting from memory of an ENGLISH translation while the Hebrew said
  otherwise. Exod 32:14 was cited for אמר and contains no אמר. Gen 5:3 was cited
  for בן and contains no בן. H0853 was given a sense belonging to H0854, a
  different word with identical consonants. None of it reached disk.

    ./verify_ranges.py           check everything
    ./verify_ranges.py --quiet   only report failures
"""
import json, os, sys, collections
import corpus

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RANGES = os.path.join(ROOT, 'ranges')


def main():
    quiet = '--quiet' in sys.argv

    if not os.path.isdir(RANGES):
        print(f'FAILED: no ranges/ directory at {RANGES}')
        sys.exit(1)

    files = sorted(f for f in os.listdir(RANGES) if f.endswith('.json'))
    if not files:
        print('FAILED: ranges/ is empty — nothing to verify')
        sys.exit(1)

    # where each root actually occurs, straight from the text
    words = corpus.load()
    where = collections.defaultdict(set)
    for w in words:
        if w['r']:
            where[w['r']].add(f'{w["b"]}.{w["c"]}.{w["v"]}')

    recs, fails, checked = {}, [], 0

    for fn in files:
        path = os.path.join(RANGES, fn)
        try:
            rec = json.load(open(path, encoding='utf8'))
        except json.JSONDecodeError as e:
            fails.append(f'{fn}: unreadable JSON — {e}')
            continue

        root = rec.get('root')
        if not root:
            fails.append(f'{fn}: no "root" field')
            continue
        if f'{root}.json' != fn:
            fails.append(f'{fn}: filename does not match root {root!r}')
        recs[root] = rec

        senses = rec.get('senses') or []
        if not senses:
            fails.append(f'{root}: no senses')
            continue

        seen = set()
        for s in senses:
            name = s.get('sense')
            if not name:
                fails.append(f'{root}: a sense has no text')
                continue
            if name in seen:
                fails.append(f'{root}: sense {name!r} listed twice')
            seen.add(name)

            ev = s.get('evidence') or []
            if not ev:
                fails.append(f'{root}: sense {name!r} has NO evidence')
                continue

            for ref in ev:
                checked += 1
                if ref not in where.get(root, set()):
                    fails.append(
                        f'{root}: sense {name!r} cites {ref} — '
                        f'THE ROOT DOES NOT OCCUR THERE')

    # homograph cross-references must resolve
    for root, rec in recs.items():
        for other in (rec.get('unresolved', '') or '').split():
            o = other.strip('.,()')
            if o.startswith('H') and o[1:].rstrip('abc').isdigit():
                if o != root and o not in recs:
                    fails.append(f'{root}: warns about {o}, which has no record')

    total_occ = sum(len(where.get(r, ())) for r in recs)
    corpus_occ = sum(len(v) for v in where.values())

    if not quiet:
        print(f'ranges checked        {len(recs):>8,}')
        print(f'evidence citations    {checked:>8,}')
        multi = sum(1 for r in recs.values() if len(r.get('senses', [])) > 1)
        print(f'roots with >1 meaning {multi:>8,}  '
              f'({100*multi/len(recs):.0f}% of derived)')
        print(f'verses reachable      {total_occ:>8,} of {corpus_occ:,}')
        print()

    if fails:
        print(f'=== {len(fails)} FAILURE(S) ===\n')
        for f in fails:
            print(f'  {f}')
        print('\nNothing here should be trusted until these are fixed.')
        sys.exit(1)

    print(f'ALL {checked:,} CITATIONS VERIFIED across {len(recs)} roots.')
    print('Every sense is attached to a verse that really contains the root.')
    print('This does NOT certify that any sense is correct — see the docstring.')


if __name__ == '__main__':
    main()
