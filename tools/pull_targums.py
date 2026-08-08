#!/usr/bin/env python3
"""
pull_targums.py — fetch Aramaic targums from the Sefaria API.

Guards against the trap this project already hit once: Sefaria returns HTTP 200
with a nearly-empty body for texts it lists but does not actually have (its
"Targum Neofiti" is 8 verses of Genesis 1). So every fetch is checked for
CONTENT, not status code, and anything suspiciously short is reported as
INCOMPLETE rather than written out as if it were the whole book.
"""
import json, os, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'targums')

TORAH = ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy']
PROPHETS = ['Joshua', 'Judges', 'I Samuel', 'II Samuel', 'I Kings', 'II Kings',
            'Isaiah', 'Jeremiah', 'Ezekiel', 'Hosea', 'Joel', 'Amos', 'Obadiah',
            'Jonah', 'Micah', 'Nahum', 'Habakkuk', 'Zephaniah', 'Haggai',
            'Zechariah', 'Malachi']
WRITINGS = ['Psalms', 'Job', 'Proverbs', 'Song of Songs', 'Ruth',
            'Lamentations', 'Ecclesiastes', 'Esther']

# (subdir, sefaria title template, book list)
JOBS = [
    ('jonathan-prophets', 'Targum Jonathan on {}', PROPHETS),
    ('fragment-jerusalem', 'Targum Jerusalem, {}', TORAH),
    ('writings',           'Aramaic Targum to {}',  WRITINGS),
    ('chronicles',         'Aramaic Targum to {}',  ['I Chronicles', 'II Chronicles']),
]

MIN_CHARS = 400          # below this for a whole book = almost certainly a stub


def fetch(title):
    url = f'https://www.sefaria.org/api/texts/{urllib.parse.quote(title)}?context=0&commentary=0'
    req = urllib.request.Request(url, headers={'User-Agent': 'bible-sources/1.0'})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.load(r)


def flatten(x):
    if isinstance(x, str):
        return [x]
    out = []
    for i in x or []:
        out.extend(flatten(i))
    return out


def main():
    ok = incomplete = failed = 0
    notes = []
    for sub, tmpl, books in JOBS:
        d = os.path.join(OUT, sub)
        os.makedirs(d, exist_ok=True)
        for b in books:
            title = tmpl.format(b)
            dest = os.path.join(d, b.replace(' ', '_') + '.json')
            if os.path.exists(dest) and os.path.getsize(dest) > MIN_CHARS:
                continue
            try:
                data = fetch(title)
            except Exception as e:
                failed += 1
                notes.append(f'FAIL       {title}: {str(e)[:60]}')
                print(f'FAIL       {title}: {str(e)[:60]}', flush=True)
                time.sleep(0.3)
                continue

            # Sefaria returns only the FIRST SECTION for a bare book ref.
            # 'lengths' tells us the true shape: [chapters, total_verses].
            lengths = data.get('lengths') or []
            nchap = lengths[0] if lengths else 1
            expect_verses = lengths[1] if len(lengths) > 1 else None

            chapters = {}
            if nchap > 1:
                for c in range(1, nchap + 1):
                    try:
                        cd = fetch(f'{title}.{c}')
                    except Exception as e:
                        notes.append(f'  chapter fail {title}.{c}: {str(e)[:50]}')
                        continue
                    ct = flatten(cd.get('he') or cd.get('text') or [])
                    if ct:
                        chapters[c] = ct
                    time.sleep(0.15)
            else:
                chapters[1] = flatten(data.get('he') or data.get('text') or [])

            text = [t for c in sorted(chapters) for t in chapters[c]]
            chars = sum(len(t) for t in text)
            verses = len([t for t in text if t.strip()])

            # Completeness is judged against the corpus's OWN declared shape,
            # not against a guessed byte threshold.
            short = (expect_verses is not None and verses < expect_verses * 0.5)
            if chars < MIN_CHARS or short:
                incomplete += 1
                exp = f'/{expect_verses} expected' if expect_verses else ''
                notes.append(f'INCOMPLETE {title}: {verses}{exp} verses, {len(chapters)}/{nchap} chapters — not written')
                print(f'INCOMPLETE {title}: {verses}{exp} verses, {len(chapters)}/{nchap} ch — SKIPPED', flush=True)
            else:
                json.dump({'title': title, 'chapters': chapters,
                           'nchap': nchap, 'verses': verses},
                          open(dest, 'w'), ensure_ascii=False)
                ok += 1
                print(f'OK         {title}: {verses} verses, {len(chapters)}/{nchap} chapters', flush=True)
            time.sleep(0.2)

    print('\n' + '=' * 60)
    print(f'written    : {ok}')
    print(f'incomplete : {incomplete}  (stubs, deliberately NOT saved)')
    print(f'failed     : {failed}')
    if notes:
        print('\nnotes:')
        for n in notes:
            print('  ' + n)


if __name__ == '__main__':
    main()
