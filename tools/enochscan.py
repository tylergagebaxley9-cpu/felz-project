#!/usr/bin/env python3
"""enochscan.py — systematic witness scan across all 108 chapters of 1 Enoch.

The mechanical half of the Enoch work: find every place the witnesses disagree,
so the judgment half (translation) can be spent where it matters instead of
being spread evenly over a book whose textual condition is wildly uneven.

Modelled on diverge.py (DSS vs MT). Emits no English and makes no judgment
about which reading is right -- it reports WHERE to look.

  --coverage     per-chapter witness matrix for all 108
  --diverge      units where two witnesses of the SAME language disagree
  --absent       verses a version skips inside a chapter it otherwise attests
  --forms N      Ge'ez form frequency (the root queue)
  --unique       readings carried by exactly one manuscript

🛑 NORMALISE BEFORE COMPARING. An accent-blind match against accented Greek
returns zero hits and reads exactly like "no divergence". See enoch-6.md.
"""
import argparse
import json
import pathlib
import sys
import unicodedata
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent
GEEZ = ROOT / "ethiopic/ethiopian-bible/public/data/chapters/1En"
APP = ROOT / "pseudepigrapha/Online-Critical-Pseudepigrapha/static/docs/1En.xml"
TOTAL_CH = 108


def norm(s):
    """NFD, drop combining marks, casefold. Required before ANY comparison."""
    d = unicodedata.normalize("NFD", s)
    return "".join(c for c in d if not unicodedata.combining(c)).casefold().strip()


def load_app():
    """[(ch, vs, version, lang, sigla, text)]"""
    if not APP.is_file():
        sys.exit(f"FAILED: apparatus missing at {APP}")
    rows = []
    for ver in ET.parse(APP).getroot().findall("version"):
        title, lang = ver.get("title"), ver.get("language")
        for d1 in ver.findall(".//text/div"):
            try:
                ch = int(d1.get("number"))
            except (TypeError, ValueError):
                continue
            for d2 in d1.findall("div"):
                try:
                    vs = int(d2.get("number"))
                except (TypeError, ValueError):
                    continue
                for u in d2.findall("unit"):
                    for rd in u.findall("reading"):
                        t = "".join(rd.itertext()).strip()
                        if t:
                            rows.append((ch, vs, title, lang,
                                         (rd.get("mss") or "").strip(), t))
    return rows


def load_geez():
    if not GEEZ.is_dir():
        sys.exit(f"FAILED: Ge'ez missing at {GEEZ}")
    out = {}
    for f in GEEZ.glob("*.json"):
        d = json.loads(f.read_text(encoding="utf-8"))
        ch = int(d["chapter"])
        for v in d["verses"]:
            # `translation` (Charles 1917) deliberately not read.
            out[(ch, int(v["num"]))] = [w["g"].strip()
                                        for w in v.get("words", []) if w["g"].strip()]
    return out


def cmd_coverage(rows, geez):
    per = defaultdict(set)
    for ch, vs, title, *_ in rows:
        per[ch].add(title)
    gch = defaultdict(int)
    for (c, v) in geez:
        gch[c] += 1
    print(f"{'ch':>4} {'Ge`ez v':>8}  {'Eth':>4}{'Grk':>4}{'Aram':>5}{'Lat':>4}   witnesses beyond Ge'ez")
    tiers = Counter()
    for c in range(1, TOTAL_CH + 1):
        w = per.get(c, set())
        e = "x" if "Ethiopic" in w else "."
        g = "x" if "Greek" in w else "."
        a = "x" if "Qumran Aramaic" in w else "."
        l = "x" if "Latin Fragments" in w else "."
        n = sum(1 for k in (g, a, l) if k == "x")
        tiers[n] += 1
        flag = "  <== FOUR TRADITIONS" if a == "x" else ("  <-- Greek check" if g == "x" else "  !! GE'EZ ALONE")
        print(f"{c:>4} {gch.get(c,0):>8}  {e:>4}{g:>4}{a:>5}{l:>4}{flag}")
    print(f"\nchapters with 0 non-Ge'ez witness: {tiers[0]}   1: {tiers[1]}   2: {tiers[2]}   3: {tiers[3]}")
    print(f"🛑 {tiers[0]} of {TOTAL_CH} chapters rest on the Ge'ez ALONE, with nothing to check them against.")


def cmd_diverge(rows):
    """Units where two mss of the SAME language give different text."""
    units = defaultdict(lambda: defaultdict(list))
    for ch, vs, title, lang, sigla, text in rows:
        units[(ch, vs, title)][norm(text)].append(sigla)
    n = 0
    per_ch = Counter()
    for (ch, vs, title), variants in sorted(units.items()):
        if len(variants) < 2:
            continue
        # only report when distinct sigla actually differ
        sig = {s for v in variants.values() for s in v}
        if len(sig) < 2:
            continue
        n += 1
        per_ch[ch] += 1
    print(f"internal divergences (same language, mss disagree): {n}")
    print("\ntop chapters by divergence count:")
    for ch, c in per_ch.most_common(20):
        print(f"  ch {ch:>3}: {c:>4}")
    return per_ch


def cmd_absent(rows, geez):
    """Verses a version skips INSIDE a chapter it otherwise attests."""
    have = defaultdict(set)
    for ch, vs, title, *_ in rows:
        have[title].add((ch, vs))
    chs = defaultdict(set)
    for title, refs in have.items():
        for c, v in refs:
            chs[title].add(c)
    print(f"{'version':<18}{'ch attested':>12}{'verses':>8}{'gaps inside':>13}")
    for title in sorted(have):
        gaps = 0
        for c in chs[title]:
            gv = {v for (cc, v) in geez if cc == c}
            hv = {v for (cc, v) in have[title] if cc == c}
            gaps += len(gv - hv)
        print(f"{title:<18}{len(chs[title]):>12}{len(have[title]):>8}{gaps:>13}")
    print("\n⚠️ 'gaps inside' = verses present in the Ge'ez but skipped by a version")
    print("   in a chapter it DOES attest. Those are the cheapest places to look")
    print("   for something the Ethiopic added or a witness lost.")


def cmd_unique(rows):
    """Readings carried by exactly one manuscript siglum."""
    per_lang = Counter()
    per_ms = Counter()
    for ch, vs, title, lang, sigla, text in rows:
        parts = [s for s in sigla.split() if s]
        if len(parts) == 1:
            per_ms[parts[0]] += 1
            per_lang[title] += 1
    print("readings carried by exactly ONE manuscript:")
    for ms, c in per_ms.most_common():
        print(f"  {ms:<14}{c:>6}")
    print("\nby tradition:")
    for t, c in per_lang.most_common():
        print(f"  {t:<18}{c:>6}")


def cmd_forms(geez, n):
    forms = Counter()
    for words in geez.values():
        forms.update(words)
    tot = sum(forms.values())
    print(f"{len(forms)} distinct Ge'ez forms / {tot} tokens")
    run = 0
    for i, (w, c) in enumerate(forms.most_common(n), 1):
        run += c
        print(f"{i:>4}. {c:>5}  {w:<18} cum {run*100/tot:5.1f}%")


def main():
    p = argparse.ArgumentParser()
    for f in ("coverage", "diverge", "absent", "unique"):
        p.add_argument(f"--{f}", action="store_true")
    p.add_argument("--forms", type=int)
    a = p.parse_args()
    rows, geez = load_app(), load_geez()
    if a.coverage: cmd_coverage(rows, geez)
    elif a.diverge: cmd_diverge(rows)
    elif a.absent: cmd_absent(rows, geez)
    elif a.unique: cmd_unique(rows)
    elif a.forms: cmd_forms(geez, a.forms)
    else: p.print_help()


if __name__ == "__main__":
    main()
