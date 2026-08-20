#!/usr/bin/env python3
"""
dillmann.py — look a Ge'ez word up in Dillmann's Lexicon Linguae Aethiopicae
(1865), and print the LATIN.

Why this exists
---------------
The Ge'ez translation work needs a sense range for every word, and the only
open lexicon of Ge'ez is Dillmann 1865 — public domain, but on disk only as an
archive.org OCR layer. The OCR mangles Ge'ez glyphs and interleaves the two
columns, so a bare `grep` returns mostly CITATIONS (the word quoted inside
someone else's entry) rather than the word's own ENTRY.

This tool separates those two cases and ranks what it finds, so a translator
reads the entry and not a scrap of Sirach.

It emits NO ENGLISH. Dillmann defined Ge'ez in Latin; the Latin is what gets
printed, and turning that Latin into English is the translator's judgment call,
recorded in the file with verse evidence. Handing over an English gloss here
would rebuild exactly the dependency `analyze.py` and `enoch.py` are built to
prevent.

Usage
-----
    ./dillmann.py ዐውሎ              # ranked candidate entries
    ./dillmann.py ዐውሎ --all        # every hit, entries and citations alike
    ./dillmann.py ዐውሎ --window 14  # more context per hit
    ./dillmann.py --stem ጸወር       # match any word built on these glyphs
"""
import argparse, re, sys, os

LEX = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   '..', 'lexicon', 'dillmann-1865_djvu.txt')

# Latin words that cluster in a definition and almost never in a bare citation.
# Dillmann's defining vocabulary, not a gloss list — these only score a line,
# they are never printed as anyone's meaning.
DEFINING = re.compile(
    r'\b(?:i\.\s*e\.|scilicet|vel|seu|aut|nomen|verbum|adj|subst|'
    r'esse|fieri|facere|dicere|significat|idem|q\.\s*d\.|'
    r'plur|sing|constr|c\.\s*acc|c\.\s*gen|pass|caus|refl)\b', re.I)

# A citation line points at a source: Gen. 1, 1 / Hen. 22, 3 / Ps. 80, 7
CITATION = re.compile(r'\b[A-Z][a-z]{1,4}\.?\s*\d+\s*,\s*\d+')

# 🛑 The archive.org scan is NOT only Dillmann. A French-glossed Tigre/Amharic
# word-list is bound into the same volume near the end, and it looks exactly
# like a lexicon entry to a scorer. Handing its FRENCH back to a translator who
# asked for Dillmann's LATIN would be the post-1820 layer entering through
# tooling for the fourth time in this repo. Flag it; never score it as an entry.
FRENCH = re.compile(
    r"\b(?:le|la|les|des|une?|du|au|aux|est|pour|dans|avec|qui|que|"
    r"prix|forc[ée]|fixer|convenir|plateaux)\b")

# Dillmann marks sense divisions with lettered/numbered heads.
SENSE_HEAD = re.compile(r'(?:^|\s)(?:[a-h]\)|[1-9]\)|[A-H]\.|I{1,3}\.)\s')


def load():
    if not os.path.exists(LEX):
        sys.exit("FAILED: %s not found. The lexicon is a sparse-checkout path;\n"
                 "        run: git sparse-checkout add lexicon" % LEX)
    with open(LEX, encoding='utf-8', errors='replace') as fh:
        return fh.read().split('\n')


def score(line, target, col):
    """Higher = more likely this line opens the word's own entry."""
    s = 0
    # Headwords sit at or near the start of a line/column.
    if col <= 2:            s += 6
    elif col <= 12:         s += 3
    # Dillmann's headwords are followed by his defining vocabulary.
    if DEFINING.search(line): s += 4
    # Sense divisions (a) b) c)) mean we are inside a real entry.
    if SENSE_HEAD.search(line): s += 3
    # A line that is mostly a scripture reference is a citation, not an entry.
    if CITATION.search(line): s -= 2
    # Long runs of Latin beat scraps.
    latin = len(re.findall(r'[A-Za-z]{4,}', line))
    s += min(latin, 6)
    return s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('word', nargs='?', help="Ge'ez word to look up")
    ap.add_argument('--stem', help='match any word containing these glyphs')
    ap.add_argument('--window', type=int, default=8, help='context lines (default 8)')
    ap.add_argument('--all', action='store_true', help='show citations too, unranked')
    ap.add_argument('--max', type=int, default=6, help='max hits to show (default 6)')
    a = ap.parse_args()

    target = a.stem or a.word
    if not target:
        ap.error('give a word, or --stem')

    lines = load()
    hits = []
    for i, line in enumerate(lines):
        col = line.find(target)
        if col < 0:
            continue
        hits.append((score(line, target, col), i, col))

    if not hits:
        print("NO HIT for %s in Dillmann 1865." % target)
        print("The OCR mangles many Ge'ez glyphs — try --stem with the first")
        print("two or three consonants before concluding the word is absent.")
        return 1

    print("=" * 74)
    print("  DILLMANN 1865 — %s      %d line(s) contain it" % (target, len(hits)))
    print("  Latin only. No English is emitted; the sense range is your call,")
    print("  and every sense you record needs verse evidence.")
    print("=" * 74)

    order = hits if a.all else sorted(hits, key=lambda h: -h[0])[:a.max]
    for rank, (sc, i, col) in enumerate(order, 1):
        fr = FRENCH.search(lines[i]) and not DEFINING.search(lines[i])
        kind = ('⚠️ NOT DILLMANN (French Tigre glossary)' if fr else
                'LIKELY ENTRY' if sc >= 10 else 'possible' if sc >= 6 else 'citation')
        print("\n--- hit %d  [%s, score %d]  line %d, col %d" % (rank, kind, sc, i + 1, col))
        lo, hi = max(0, i - 2), min(len(lines), i + a.window)
        for j in range(lo, hi):
            mark = '>>' if j == i else '  '
            print("  %s %s" % (mark, lines[j]))
    print("\n" + "=" * 74)
    print("  🛑 A hit scored 'citation' is the word quoted inside ANOTHER entry.")
    print("     Do not read its Latin as this word's meaning.")
    print("  🛑 A hit flagged NOT DILLMANN comes from the French Tigre glossary")
    print("     bound into the same scan. It is not Dillmann and not Latin.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
