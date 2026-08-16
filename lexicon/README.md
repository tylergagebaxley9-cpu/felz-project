# Ge'ez Lexicon

## `dillmann-1865_djvu.txt` — August Dillmann, *Lexicon Linguae Aethiopicae cum indice Latino* (Leipzig, 1865)

archive.org `lexiconlinguaeae00dilluoft`, **text layer only** (5.3 MB) — never the PDF, per the corpus rule that Kennicott is 17.7 MB as text vs 262 MB as PDF.

**Provenance: PRINTED (1865).** Pre-1820? No — but it is a *lexicon*, not a witness, and it is 25 years older than Strong's (1890), which PROVENANCE.md already names as the one post-1820 work the Hebrew translations lean on. Same category, same disclosure.

### OCR quality — MEASURED, not assumed

```
total characters   4,543,382
Ge'ez              450,894   (~10%)
Latin            1,911,283
distinct Ge'ez forms  58,012
```

⭐ Unlike the archive.org Greek/Hebrew OCR the corpus already rejected as a translation base, **the Ge'ez here survived usably** — 58,012 distinct forms is enough to adjudicate whether a form is a real Ge'ez word.

⚠️ But it is still 19th-century OCR of a dense lexicon. **A form being absent from this file is weak evidence of anything**; a form being present is strong evidence it is real. Use it to *confirm*, never to *convict*.

### What it was pulled for

To adjudicate Ge'ez forms appearing in our translations that do not occur in the 108-chapter 1 Enoch corpus — i.e. to separate legitimate lemma citation from fabrication. First use took the disputed count from **16 → 6**.

### What it unblocks

🛑 The Enoch survey notes there is **no Ge'ez root queue** because morphology is unparsed — the 6,039 "forms" are surface forms including prefixed `ወ-`. This lexicon is the missing piece: with headword extraction it becomes possible to do for Ge'ez what `corpus.py`/`rootqueue.py` do for Hebrew, and settle the book by root instead of by verse.
