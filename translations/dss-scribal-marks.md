# Scribal marks in the Dead Sea Scrolls

**Source**: `dead-sea-scrolls/etcbc-dss/tf/2.0/` — Martin Abegg's transcriptions,
converted by Jacobs, Naaijer & Roorda. ⚠️ **CC BY-NC 4.0** (non-commercial).
**Witness date**: c. 250 BCE – 68 CE.

Every number below was counted directly from the corpus on 2026-08-08. Nothing here
is quoted from a secondary source.

These are not letters. They are the other things a scribe put on the page — dividers,
deliberate blanks, corrections, numerals, and marks of damage. The corpus records
them as their own node type, so they can be counted.

---

## The sign inventory

The corpus distinguishes **1,430,241 signs** by function:

| Type | Count | What it is | Glyph(s) found |
|---|---:|---|---|
| `cons` | 1,156,780 | consonants — the letters themselves | Hebrew alphabet |
| `empty` | 98,407 | **vacat** — deliberate blank space | (blank) |
| `punct` | 59,854 | punctuation | `׃` sof pasuq ×29,909 · `׃׃` ×18 · unmarked ×29,927 |
| `sep` | 46,453 | word/section separator | `׳` ×46,050 · `־` maqqef ×1 |
| `missing` | 53,864 | **lacuna — text physically gone** | — |
| `unc` | 27,168 | uncertain reading | — |
| `term` | 15,532 | terminal (final-form) letters | ך ם ן ף ץ |
| `numr` | 2,492 | numeral marks | `א֜` ×1,250 · `ך֜` ×263 · `אׅ` ×257 · `י֜` ×164 |
| `add` | 65 | scribal addition | `+` ×65 |
| `foreign` | 16 | **Greek letters inside Hebrew scrolls** | Κ Ε Ν Χ Α Γ Η Θ Δ Ι Τ Ρ Σ |

### What the counts mean

**53,864 signs are `missing`.** That is damage — places where the leather or papyrus
is gone and the letter cannot be read. Against 1,156,780 surviving consonants, roughly
**4.4% of the text is physically absent.** Add 27,168 uncertain readings and about
**7% of the Dead Sea Scrolls is either gone or unsure.** Any edition that prints these
scrolls as continuous text has filled that in by conjecture. The corpus keeps the
distinction; printed translations usually do not.

**98,407 vacats.** A vacat is a blank the scribe left on purpose — a paragraph break,
a section division, a pause. It carries meaning and it is invisible in most modern
printings.

**65 additions marked `+`.** Places where something was inserted, typically above the
line — a scribe or a later corrector fixing the text on the page.

---

## The divine name in paleo-Hebrew

At **word** level, 789 tokens are written in paleo-Hebrew script inside otherwise
square-script scrolls:

| Glyph | Count | Note |
|---|---:|---|
| **יהוה** | **286** | the Tetragrammaton |
| ך֜י֜ · אׅ · א֜ · … | 461 | **numerals, not words** — cryptic/calendrical texts |
| אל | 23 | *El* |
| others | ~19 | |

> ⚠️ **The counting trap**: a naive count of "paleo-Hebrew tokens" returns 789 and
> looks like divine-name usage. **461 of those are numerals in unrelated texts.** The
> real figure for the Name is **286**.

At **sign** level, 3,298 signs are paleo-Hebrew: 2,027 numerals, **1,261 consonants**.
That consonant figure is the internal cross-check — 286 four-letter Tetragrammata plus
the other paleo words comes to ≈1,261. The two levels agree.

---

## Greek letters in the scrolls — UNRESOLVED

Sixteen signs are marked `foreign`, and they are **Greek capitals**. They group into
seven short sequences at word level:

**ΚΕΝ · ΧΑΓ · ΗΝ · ΘΕ · ΔΙ · ΤΡ · ΣΚ**

They sit in a tight node range (140917–141748 at sign level; 1655475–1655779 at word
level), so they come from one document or a small cluster of adjacent ones.

> 🛑 **I could not determine which scroll.** `scroll.tf` is defined on nodes
> 1531341–1606868 (fragment/lex/line/scroll), which does **not** cover word nodes
> (1606869+). Mapping word → line → scroll requires parsing `oslots.tf`, which my
> parser did not handle correctly. Taking the "nearest scroll node below" returns `X4`,
> which is an artifact of the gap, **not an answer**.
>
> This is left open rather than guessed. Anyone resolving it should parse `oslots.tf`
> properly (comma-separated slot lists, one line per non-slot node, implicit numbering
> starting at 1430242).

---

## Method note — a real parsing trap

Text-Fabric `.tf` files use implicit node numbering: a line with no tab means
*previous node + 1*. **A parser that skips empty values silently drifts every
subsequent node**, and the corruption is invisible — it produces plausible-looking
output with the wrong glyph attached to every node.

This happened here. The first run reported identical Hebrew letter-frequency profiles
for `punct`, `sep`, `empty` and `numr` alike — which is impossible, and was the tell.
The fix is to emit every line including empty ones:

```python
def stream(path):
    node = 0
    with open(path, encoding='utf8') as fh:
        for line in fh:              # skip @metadata block
            if not line.strip(): break
        for line in fh:
            line = line.rstrip('\n')
            if '\t' in line:
                spec, val = line.split('\t', 1)
                if '-' in spec:
                    a, b = (int(x) for x in spec.split('-', 1))
                    for n in range(a, b + 1): yield n, val
                    node = b
                else:
                    node = int(spec); yield node, val
            else:
                node += 1; yield node, line     # <- empty line still advances
```

Cross-check any result against a known quantity before trusting it. Here the check was
1,261 paleo-Hebrew consonants ÷ 286 Tetragrammata ≈ 4.4 letters per word.
