# 1 Enoch — Complete Textual Survey, all 108 chapters

**Mechanical coverage of the whole book.** Built with `tools/enochscan.py` from the Ge'ez base text and the Online Critical Pseudepigrapha apparatus. Emits no English; makes no judgment about which reading is right. Its job is to say **where the judgment work is worth spending** — because the book's textual condition is wildly uneven and translating it at a constant grade would waste most of the effort.

Companion to `translations/enoch-6.md` (the first chapter translated in full).

---

## 🛑 THE HEADLINE: 59 of 108 chapters have no witness but the Ge'ez

| non-Ge'ez witnesses | chapters | share |
|---|---:|---:|
| **none — Ge'ez alone** | **59** | **55%** |
| one (usually Greek) | 40 | 37% |
| two | 8 | 7% |
| three (Greek + Aramaic + Latin) | 1 | 1% |

**More than half of 1 Enoch rests on a single late translation with nothing to check it against.** The chain for those 59 chapters is: lost Aramaic → lost Greek → surviving Ge'ez. No control at any step.

⭐ This is the Enoch analogue of the Round 7 finding that 65.4% of the Hebrew Bible has no scroll witness — and it is worse here, because for the Hebrew Bible the base text is at least *in the original language*.

## Where the witnesses actually are

- **Qumran Aramaic — chapters 1–8 ONLY.** 35 verses. That is the entire original-language witness to the book.
- **Greek — 48 chapters**, concentrated in 1–32 (Gizeh/Akhmim) and 97–107 (Chester Beatty).
- **Latin — 3 chapters**, 18 verses.
- **Ethiopic apparatus — 71 chapters** (the other 37 have the base text but no variant record).
- 🛑 **The Book of Parables (37–71) has no Aramaic and almost no Greek.** The section containing the "Son of Man" material is the least attested part of the book.

## ⚠️ 115 verses the Greek skips *inside* chapters it does attest

| version | ch attested | verses | gaps inside |
|---|---:|---:|---:|
| Ethiopic | 71 | 543 | 0 |
| **Greek** | 48 | 369 | **115** |
| Latin Fragments | 3 | 18 | 26 |
| Qumran Aramaic | 8 | 35 | 6 |

A "gap inside" is a verse the Ge'ez has and the Greek does not, in a chapter the Greek otherwise covers. Those 115 are the **cheapest high-value targets in the book** — each is either something the Ethiopic tradition added or something the Greek lost, and the comparison is already available. Ethiopic having **0** gaps means the apparatus's Ethiopic is complete wherever it reaches.

---

## 🛑🛑 DEFECT FOUND IN OUR OWN TOOL — conjectures were printed as witnesses

The apparatus records **modern editors' emendations in the same `mss` attribute as manuscript sigla, with nothing marking the difference.** Fourteen sigla are used in readings but never declared as `<ms>`:

`Charles` · `Dillman` · `Dindorf` · `Goar` · `Swete` · `Lods` · `Black` · `Bonner` · `Kenyon` · `F-R` · `Gizeh*` · `Syncellus2` · `TertullianB` · `Ε`

Measured impact:
```
total readings            3,003
CONJECTURE-ONLY (no ms)      39   <- printed as manuscript evidence
manuscript + conjecture       6
```
By editor: Black 22 · Bonner 15 · Kenyon 8 · **Charles 4** · Swete 3 · Dindorf 2 · Goar 2 · others 1 each.

🛑 **One of them is Charles** — so the tool built to keep Charles's *English* out was silently presenting Charles's *conjectures* as parchment. `enoch.py` now separates them: a manuscript-backed reading prints normally, a mixed one is flagged `⚠️ +conjecture`, and a conjecture-only reading prints `🛑 CONJECTURE ONLY — not manuscript evidence`.

⭐ **Same lesson, third time:** *an apparatus of editions is not an apparatus of manuscripts* (`revelation-3.md`), *root ID leans on Strong's 1890* (PROVENANCE.md), and now this. The post-1820 layer keeps entering through tooling rather than through text.

## 🛑 CORRECTION — only 3 of the 13 Aramaic scrolls contribute anything

The apparatus **declares** 4Q201, 4Q202, 4Q204, 4Q205, 4Q206, 4Q207, 4Q208, 4Q209, 4Q210, 4Q211, 4Q212 and 4Q247 — but nine of them supply **zero readings**:

```
declared but never used:  4Q205 4Q206 4Q207 4Q208 4Q209 4Q210 4Q211 4Q212 4Q247
actually cited        :  4Q201 (49 unique)  4Q202 (32)  4Q204 (13)
```

⚠️ I previously wrote "all twelve Qumran Enoch scrolls" in the vault and in the first report. **That is wrong in effect** — the Aramaic evidence in this apparatus is *three* scrolls. The astronomical scrolls (4Q208–211, which carry the Astronomical Book) are declared and silent, so the Astronomical Book's Aramaic is not represented here even though it exists.

## Readings unique to a single manuscript

```
p            584     CB185   151     Gizeh2   21     Jude        6
Bertalotto   581     4Q201    49     BL       15     7QEnoch     6
Gizeh        295     Syncellus 48    4Q204    13     Vigilius    5
                     4Q202    32     POxy2069 10     Tertullian  4
                                     V1809     8     Cyprian     7
```
by tradition: Ethiopic 1,165 · Greek 570 · Qumran Aramaic 94 · Latin 35.

---

## The work list, in priority order

**Tier 1 — chapters 1–8.** The only place original-language Aramaic exists. Four traditions comparable. 35 Aramaic verses total. **Chapter 6 done** (`enoch-6.md`); 1–5, 7–8 remain. This tier is small, finite, and irreplaceable.

**Tier 2 — the 115 Greek gaps.** Mechanically identified, spread across the 48 Greek chapters. Each is a concrete Ethiopic-vs-Greek question with the evidence already in hand.

**Tier 3 — chapters 9–36, 97–107.** Ge'ez against Greek, no Aramaic control.

**Tier 4 — the 59 Ge'ez-alone chapters.** Translatable, but nothing can check them. 🛑 **Any output from this tier must say so on its face**, including all of the Book of Parables.

## Ge'ez as a corpus

```
108 chapters · 1,058 verses · 18,490 word tokens · 6,039 distinct forms
top   50 forms ->  21.8%        top  400 forms -> 50.1%
top  100 forms ->  30.1%        top 1500 forms -> 72.0%
top  200 forms ->  39.4%        top 3000 forms -> 83.6%
```
The same steep curve that made the Hebrew finite. ~400 forms settles half the book. But note this is **form frequency, not root frequency** — Ge'ez morphology is not yet parsed, so these are surface forms including prefixed conjunctions (ወ-). A real Ge'ez root queue needs morphological analysis that does not yet exist in this repo.

## What this survey cannot do

- It reports **where** witnesses differ, never **which is right**. That is judgment.
- Ge'ez semantic ranges are **not validator-gated** — `ranges/*.json` and `verify_ranges.py` are Hebrew-only.
- The Aramaic is heavily bracketed. **Brackets are editorial reconstruction, not ink**, and any finding resting on a bracketed letter must say so (see the corrected name table in `enoch-6.md`).
- 🛑 **Normalise before comparing.** An accent-blind grep against accented Greek returns zero hits and reads exactly like "no divergence found." That bug produced two false negatives during the enoch-6 verification pass before it was caught.
