#!/usr/bin/env python3
"""geezroot.py — the Ge'ez root queue. Sibling of corpus.py + rootqueue.py.

WHY THIS EXISTS
---------------
ENOCH-SURVEY.md recorded that Ge'ez could not have a root queue because
morphology is unparsed: the 6,039 "forms" in 1 Enoch are SURFACE forms
including prefixed ወ-, so ኵሉ / ወኵሉ / ወኵሎ / ለኵሎሙ count as four separate
items when they are one word.

Measured against Dillmann (1865): 80 of the 100 commonest Enoch forms appear
in the lexicon exactly. **Every one of the 20 misses is a prefixed or
inflected form** — ወርኢኩ, ወኵሉ, ወይቤለኒ, ለአባግዕ, ወእምድኅረ. A lexicon lists
lemmas, not inflections. So the gap is morphological, not OCR, and stripping
proclitics closes most of it.

This is the same insight that made the Hebrew finite: the unit of work is the
ROOT, not the verse. 306,785 Hebrew words collapsed to 8,640 roots, of which
130 cover 50% of the text.

🛑 EMITS NO ENGLISH. Like analyze.py and enoch.py, this tool cannot produce a
gloss. Dillmann's definitions are LATIN; the Latin is available for a human
to read but is never rendered to English by this tool, because that would
make it a translation-of-a-translation exactly like the Charles path.

Usage:
  ./geezroot.py --coverage         how far proclitic-stripping gets us
  ./geezroot.py --queue N          highest-value undone lemmas
  ./geezroot.py --lemma FORM       every occurrence + every witness form
"""
import argparse
import json
import glob
import pathlib
import re
import sys
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent
GEEZ = ROOT / "ethiopic/ethiopian-bible/public/data/chapters/1En"
LEX = ROOT / "lexicon/dillmann-1865_djvu.txt"

# Ge'ez proclitics. The script is a syllabary, so a "prefix" is one or two
# leading syllable-characters. Ordered longest-first so እም- beats እ-.
#
# ⚠️ These are ORTHOGRAPHIC strips, not a morphological analysis. Ge'ez verbs
# also inflect internally (ይ-/ት-/ን-/እ- imperfect, ተ- passive, አ- causative),
# which stripping cannot reach. This closes the proclitic gap only, and says
# so rather than claiming to be a parser.
PROCLITICS = [
    "ወእም", "ወበ", "ወለ", "ወዘ", "ወከ", "ወይ", "ወት", "ወa",
    "እም", "ዘበ", "ዘለ",
    "ወ", "ለ", "በ", "ዘ", "ከ", "ና", "ሰ",
]


def strip_proclitics(w, known):
    """Return (lemma_candidate, prefix_removed). Prefers a form the lexicon knows."""
    if w in known:
        return w, ""
    for p in PROCLITICS:
        if w.startswith(p) and len(w) > len(p) + 1:
            cand = w[len(p):]
            if cand in known:
                return cand, p
    # no lexicon hit -- still report the longest plausible strip
    for p in PROCLITICS:
        if w.startswith(p) and len(w) > len(p) + 1:
            return w[len(p):], p
    return w, ""


def load_lexicon():
    if not LEX.is_file():
        sys.exit(f"FAILED: lexicon missing at {LEX}\n  see lexicon/README.md")
    t = LEX.read_text(encoding="utf-8", errors="replace")
    return set(re.findall(r"[ሀ-፿]{2,}", t))


def load_corpus():
    """{form: [(ch, vs), ...]} over all 108 chapters."""
    occ = defaultdict(list)
    files = sorted(glob.glob(str(GEEZ / "*.json")))
    if not files:
        sys.exit(f"FAILED: Ge'ez corpus missing at {GEEZ}")
    for f in files:
        d = json.loads(pathlib.Path(f).read_text(encoding="utf-8"))
        ch = int(d["chapter"])
        for v in d["verses"]:
            # `translation` (Charles 1917) deliberately never read.
            for w in v.get("words", []):
                g = w["g"].strip()
                if g:
                    occ[g].append((ch, int(v["num"])))
    return occ


def build(occ, known):
    """Collapse surface forms onto lemma candidates."""
    lemmas = defaultdict(lambda: {"count": 0, "forms": Counter(), "refs": []})
    for form, refs in occ.items():
        lem, pre = strip_proclitics(form, known)
        e = lemmas[lem]
        e["count"] += len(refs)
        e["forms"][form] += len(refs)
        e["refs"].extend(refs)
    return lemmas


def cmd_coverage(occ, known, lemmas):
    tokens = sum(len(v) for v in occ.values())
    in_lex_surface = sum(len(v) for f, v in occ.items() if f in known)
    in_lex_lemma = sum(e["count"] for l, e in lemmas.items() if l in known)
    print(f"1 Enoch, all 108 chapters")
    print(f"  word tokens                    {tokens:>8}")
    print(f"  distinct SURFACE forms         {len(occ):>8}")
    print(f"  distinct LEMMA candidates      {len(lemmas):>8}   "
          f"({(len(occ)-len(lemmas))*100//max(len(occ),1)}% collapse)")
    print()
    print(f"  tokens whose SURFACE form is in Dillmann   {in_lex_surface:>8}"
          f"  ({in_lex_surface*100//max(tokens,1)}%)")
    print(f"  tokens whose LEMMA is in Dillmann          {in_lex_lemma:>8}"
          f"  ({in_lex_lemma*100//max(tokens,1)}%)")
    print()
    ranked = sorted(lemmas.items(), key=lambda x: -x[1]["count"])
    run = 0
    print("  lemmas needed to cover the text:")
    for n in (25, 50, 100, 200, 400, 800, 1500, 3000):
        run = sum(e["count"] for _, e in ranked[:n])
        print(f"    top {n:>5} lemmas -> {run*100/max(tokens,1):5.1f}%")
    print()
    print("🛑 Proclitic stripping is ORTHOGRAPHIC, not a morphological parse.")
    print("   Internal inflection (ይ-/ት-/ን- imperfect, ተ- passive, አ- causative)")
    print("   is NOT reached. This number is a floor, not the true root count.")


def cmd_queue(lemmas, known, n):
    ranked = sorted(lemmas.items(), key=lambda x: -x[1]["count"])
    tot = sum(e["count"] for _, e in ranked)
    print(f"{'#':>4} {'count':>6} {'%':>6} {'cum':>6}  {'lemma':<16} lex  surface forms")
    run = 0
    for i, (lem, e) in enumerate(ranked[:n], 1):
        run += e["count"]
        mark = "✓" if lem in known else "·"
        forms = " ".join(f for f, _ in e["forms"].most_common(4))
        print(f"{i:>4} {e['count']:>6} {e['count']*100/tot:>5.1f}% {run*100/tot:>5.1f}%  "
              f"{lem:<16} {mark}   {forms}")
    print(f"\n✓ = lemma attested in Dillmann 1865   · = not found (may be OCR or inflection)")


def cmd_lemma(lemmas, occ, known, form):
    lem, _ = strip_proclitics(form, known)
    e = lemmas.get(lem) or lemmas.get(form)
    if not e:
        sys.exit(f"FAILED: no lemma '{form}' in 1 Enoch")
    print(f"LEMMA {lem}    occurrences {e['count']}    "
          f"in Dillmann: {'YES' if lem in known else 'no'}")
    print(f"\nSURFACE FORMS ({len(e['forms'])}):")
    for f, c in e["forms"].most_common():
        print(f"  {c:>5}  {f}")
    print(f"\nREFERENCES ({len(e['refs'])}):")
    refs = sorted(set(e["refs"]))
    for i in range(0, len(refs), 10):
        print("  " + "  ".join(f"{c}:{v}" for c, v in refs[i:i+10]))
    print("\n🛑 No English is emitted. Read Dillmann's LATIN for the sense range,")
    print("   and record every sense with verse evidence -- none preferred.")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--coverage", action="store_true")
    p.add_argument("--queue", type=int)
    p.add_argument("--lemma")
    a = p.parse_args()
    known = load_lexicon()
    occ = load_corpus()
    lemmas = build(occ, known)
    if a.coverage: cmd_coverage(occ, known, lemmas)
    elif a.queue: cmd_queue(lemmas, known, a.queue)
    elif a.lemma: cmd_lemma(lemmas, occ, known, a.lemma)
    else: p.print_help()


if __name__ == "__main__":
    main()
