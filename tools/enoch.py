#!/usr/bin/env python3
"""enoch.py — 1 Enoch analysis tool. The Enoch sibling of analyze.py.

STRUCTURAL GUARANTEE
--------------------
The Ge'ez chapter JSON (ethiopic/ethiopian-bible) ships a `translation` field
containing **R. H. Charles's 1917 English**. This tool NEVER reads that field.
It is dropped at parse time, in one place, and there is no flag to turn it back
on. A translator working from this output has no English to copy.

This is the same enforcement analyze.py has for the Hebrew: the tool cannot
emit a gloss, so the promise is a property of the code rather than a claim in
prose. See PROVENANCE.md.

WHAT IT DOES EMIT
-----------------
  * the Ge'ez text of the verse (complete book: 108 ch / 1,058 v / 18,490 words)
  * per-word Ge'ez + transliteration (the `gl` gloss field is empty in all
    18,490 tokens — verified — so there is no lexical English in the source)
  * every manuscript reading from the Online Critical Pseudepigrapha apparatus,
    in Ethiopic / Greek / Qumran Aramaic / Latin, labelled by siglum
  * ABSENT where a version exists but does not attest this verse

WITNESS COVERAGE (measured, not estimated)
------------------------------------------
    Ethiopic (OCP)      71/108 ch    543 v    1,634 units
    Greek               48/108 ch    370 v      562 units
    Qumran Aramaic       8/108 ch     35 v       71 units
    Latin                3/108 ch     21 v       33 units

  Base Ge'ez text (ethiopian-bible JSON): 108/108 ch, 1,058 v, 18,490 words.

PROVENANCE CHAIN — state this, never hide it
--------------------------------------------
1 Enoch has NO complete original-language text. It survives whole only in
Ge'ez, which is a translation of Greek, which translated Aramaic. The Ge'ez
manuscripts are late. So for ~93% of the book there is no Aramaic witness at
all, and the Book of Parables (37-71) has zero Aramaic attestation.

Usage:
  ./enoch.py --coverage
  ./enoch.py --chapter 6
  ./enoch.py --verse 1:9          # the verse Jude quotes
  ./enoch.py --forms 40           # most frequent Ge'ez forms (the root queue)
"""
import argparse
import json
import pathlib
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent
GEEZ_DIR = ROOT / "ethiopic/ethiopian-bible/public/data/chapters/1En"
APPARATUS = ROOT / "pseudepigrapha/Online-Critical-Pseudepigrapha/static/docs/1En.xml"

# Ge'ez word separator (U+1361 ETHIOPIC WORDSPACE) and full stop (U+1362).
GEEZ_PUNCT = "፡።​"


# ── Ge'ez base text ──────────────────────────────────────────────────────────

def load_geez():
    """Return {(chapter, verse): {'geez': str, 'words': [(g, translit), ...]}}.

    The `translation` key is dropped HERE and never propagated. This function
    is the only place the raw JSON is touched.
    """
    out = {}
    if not GEEZ_DIR.is_dir():
        sys.exit(f"FAILED: Ge'ez text not checked out at {GEEZ_DIR}\n"
                 f"  fix: git sparse-checkout add "
                 f"ethiopic/ethiopian-bible/public/data/chapters/1En")
    for f in GEEZ_DIR.glob("*.json"):
        d = json.loads(f.read_text(encoding="utf-8"))
        ch = int(d["chapter"])
        for v in d["verses"]:
            words = [(w["g"].strip(), w.get("t", "").strip())
                     for w in v.get("words", []) if w["g"].strip()]
            out[(ch, int(v["num"]))] = {"geez": v.get("geez", ""), "words": words}
            # NOTE: v["translation"] deliberately not read. Do not add it.
    return out


# ── Manuscript apparatus ─────────────────────────────────────────────────────

def load_apparatus():
    """Return {(chapter, verse): [(version, language, sigla, reading), ...]}."""
    if not APPARATUS.is_file():
        return {}, []
    root = ET.parse(APPARATUS).getroot()
    app = defaultdict(list)
    versions = []
    for ver in root.findall("version"):
        title, lang = ver.get("title"), ver.get("language")
        versions.append((title, lang))
        for dch in ver.findall(".//text/div"):
            try:
                ch = int(dch.get("number"))
            except (TypeError, ValueError):
                continue
            for dv in dch.findall("div"):
                try:
                    vs = int(dv.get("number"))
                except (TypeError, ValueError):
                    continue
                for unit in dv.findall("unit"):
                    for rd in unit.findall("reading"):
                        text = "".join(rd.itertext()).strip()
                        if text:
                            app[(ch, vs)].append(
                                (title, lang, (rd.get("mss") or "").strip(), text))
    return app, versions


# ── Output ───────────────────────────────────────────────────────────────────

def show_verse(ref, geez, app, versions):
    ch, vs = ref
    rec = geez.get(ref)
    print(f"\n{'=' * 72}\n1 ENOCH {ch}:{vs}\n{'=' * 72}")
    if not rec:
        print("  [no Ge'ez text for this reference]")
        return
    print(f"\nGE'EZ\n  {rec['geez']}")
    print(f"\nWORDS ({len(rec['words'])})")
    for g, t in rec["words"]:
        print(f"  {g:<20} {t}")

    print("\nWITNESSES")
    here = app.get(ref, [])
    seen = {v for v, _, _, _ in here}
    for title, lang in versions:
        rows = [r for r in here if r[0] == title]
        if not rows:
            print(f"  {title:<18} ABSENT — version exists, does not attest this verse")
            continue
        for _, _, sigla, text in rows:
            print(f"  {title:<18} [{sigla or '?'}] {text}")
    if not versions:
        print("  (apparatus not checked out)")


def cmd_coverage(geez, app, versions):
    chs = {c for c, _ in geez}
    print(f"BASE GE'EZ TEXT   {len(chs)} chapters   {len(geez)} verses   "
          f"{sum(len(r['words']) for r in geez.values())} word tokens")
    print(f"\n{'VERSION':<18}{'chapters':>9}{'verses':>8}{'readings':>10}   % of 108 ch")
    per = defaultdict(lambda: [set(), set(), 0])
    for (c, v), rows in app.items():
        for title, _, _, _ in rows:
            per[title][0].add(c)
            per[title][1].add((c, v))
            per[title][2] += 1
    for title, lang in versions:
        c, v, n = per[title]
        print(f"{title:<18}{len(c):>9}{len(v):>8}{n:>10}   {len(c) * 100 // 108:>5}%")
    print("\n🛑 1 Enoch has NO complete original-language text. Ge'ez carries the whole")
    print("   book and is itself a translation (Greek <- Aramaic). The Book of Parables")
    print("   (37-71) has ZERO Aramaic attestation. State this chain in any output.")


def cmd_forms(geez, n):
    forms = Counter()
    for rec in geez.values():
        for g, _ in rec["words"]:
            forms[g] += 1
    tot = sum(forms.values())
    print(f"{len(forms)} distinct Ge'ez forms across {tot} tokens\n")
    run = 0
    for i, (w, c) in enumerate(forms.most_common(n), 1):
        run += c
        print(f"{i:>4}. {c:>5}  {w:<18} cumulative {run * 100 / tot:5.1f}%")


def main():
    p = argparse.ArgumentParser(description="1 Enoch — Ge'ez + manuscript apparatus. Emits no English.")
    p.add_argument("--coverage", action="store_true")
    p.add_argument("--chapter", type=int)
    p.add_argument("--verse", help="CH:VS, e.g. 1:9")
    p.add_argument("--forms", type=int, metavar="N")
    a = p.parse_args()

    geez = load_geez()
    app, versions = load_apparatus()

    if a.coverage:
        cmd_coverage(geez, app, versions)
    elif a.forms:
        cmd_forms(geez, a.forms)
    elif a.verse:
        m = re.match(r"^(\d+):(\d+)$", a.verse)
        if not m:
            sys.exit("FAILED: --verse wants CH:VS, e.g. 1:9")
        show_verse((int(m.group(1)), int(m.group(2))), geez, app, versions)
    elif a.chapter:
        refs = sorted(r for r in geez if r[0] == a.chapter)
        if not refs:
            sys.exit(f"FAILED: no chapter {a.chapter} (book has 108)")
        for ref in refs:
            show_verse(ref, geez, app, versions)
    else:
        p.print_help()


if __name__ == "__main__":
    main()
