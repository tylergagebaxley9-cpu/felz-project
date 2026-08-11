#!/usr/bin/env python3
"""
makestudybook.py — assemble every original translation into one study volume.

Gathers the files in translations/ into a single book with front matter, a
contents list, and a closing section on method and limits. The translations
themselves are this project's own work, made from the Hebrew, Aramaic and Greek
with no English translation consulted.

Usage:
    ./makestudybook.py > STUDY-BOOK.md
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TR = os.path.join(ROOT, 'translations')

# (file, title, language, one-line note). Order is canonical, not chronological.
ORDER = [
    ('genesis-1.md',  'Genesis 1:1–5',        'Hebrew',
     'Creation. Whether the first word is absolute or construct changes the whole opening.'),
    ('genesis-6.md',  'Genesis 6:1–4',        'Hebrew',
     'The sons of God, the daughters of humankind, the Nephilim.'),
    ('exodus-3.md',   'Exodus 3:13–15',       'Hebrew',
     'The divine name. Hebrew imperfect encodes aspect, not tense.'),
    ('exodus-20-deut-5.md', 'Exodus 20 · Deuteronomy 5', 'Hebrew',
     'The Ten Words, given twice and not matching. Plus the Samaritan commandment no other Bible has.'),
    ('OUR-TRANSLATION.md', 'Deuteronomy 32:8–9', 'Hebrew',
     'The apportioning of the nations. The scrolls and the Greek agree against the Masoretic text.'),
    ('job-1-and-zechariah-3.md', 'Job 1:6–12 · Zechariah 3:1–2', 'Hebrew',
     'הַשָּׂטָן carries the definite article. Hebrew proper names do not.'),
    ('psalm-82.md',   'Psalm 82',             'Hebrew',
     'The divine council. Here the scrolls and the Masoretic text agree exactly.'),
    ('psalm-22.md',   'Psalm 22:16–17',       'Hebrew',
     'The sharpest single-word split in the Psalter. Three witnesses, three readings.'),
    ('isaiah-7-and-14.md', 'Isaiah 7:14 · 14:12–15', 'Hebrew',
     'עַלְמָה is not the word for virgin. "Lucifer" is not in the Hebrew.'),
    ('isaiah-53.md',  'Isaiah 53:11',         'Hebrew',
     'The widest convergence in the project: three scrolls and the Greek carry a word the Masoretic lacks.'),
    ('daniel-7.md',   'Daniel 7:9–14',        'Aramaic',
     'One like a son of man. The prefixed כְּ marks a simile.'),
    ('john-1.md',     'John 1:1–18',          'Greek',
     'The logos, and the μονογενὴς θεός variant checked in the manuscripts.'),
    ('eusebius-HE-3.25.md', 'Eusebius, Church History III.25', 'Greek',
     'The earliest surviving sorting of which books counted. Four categories, not two.'),
]

FRONT = """# ORIGINAL BIBLE STUDIES

### Translated from the Hebrew, Aramaic and Greek — with every meaning the words carry

---

## What this book is

Every passage here was translated directly from the original language. No English
translation was consulted, adapted, or checked against — not the King James, not
any modern version, not an interlinear's English column.

That restriction is the point. A translation built on other translations inherits
their decisions, including the ones nobody flagged. What is used here instead is
**grammatical analysis**: parsing codes, root identification, and the readings of
every manuscript on disk. "Hiphil infinitive construct" is a fact about a word's
form. "In the beginning" is a choice about its meaning. The first is safe to build
on; the second has to be earned from the text.

## How each passage is set out

Every word gets its own entry:

- the pointed original, and the bare consonants beneath it
- the parse code, and what that code means in plain words
- the **root**, and its genuine range of meaning — stated from how the root behaves
  across the language, not copied from a dictionary
- the reason for the rendering chosen here

Then the passage whole, as English that reads properly.

Then — where the witnesses disagree — **every reading translated**, not only the
one that ended up in print.

## Where a word carries more than one meaning

It is marked, and every sense is given. Where the grammar genuinely permits more
than one reading of a sentence, **every reading is laid out and none is declared
the winner.** A translation that resolves an ambiguity silently has made a
decision on your behalf and hidden it.

This happens more than most readers are told. Psalm 82 cannot decide, on grammar
alone, whether its אֱלֹהִים are gods or human judges. John 1:1c cannot settle, on
syntax alone, between three readings of θεὸς ἦν ὁ λόγος. Exodus 3:14's
אֶהְיֶה אֲשֶׁר אֶהְיֶה is an imperfect, and Hebrew imperfect encodes aspect rather
than tense — so "I am" is one option among several, not the reading.

## What the manuscripts show, honestly

Some passages here differ between witnesses. Deuteronomy 32:8 reads "sons of God"
in a Dead Sea scroll and in the Greek, against "sons of Israel" in the Masoretic
manuscript of 1008 CE — two independent older witnesses against one younger.

**And some do not differ at all.** Psalm 82's scroll text matches the Masoretic
text word for word, in every verse. Isaiah — the best-attested book, with a
complete pre-Christian scroll — shows heavy minor variation and no large-scale
rewriting anywhere.

Both results are in this book. A collection that printed only the changes would be
as misleading as one that hid them, and it would be easy to dismiss. The stability
of the text is precisely what makes the specific differences findable.

## What this book will not do

- It will not resolve an ambiguity silently.
- It will not state a semantic range it cannot support. Uncertain means uncertain,
  and several words here have roots that are genuinely unknown.
- It will not claim to know **why** a reading changed. Manuscripts show that a text
  differs and often which direction the change ran. They do not record intent. A
  scribe harmonising to a familiar phrase and a scribe editing doctrine leave the
  same mark on the page.

---
"""


def contents():
    out = ['\n## Contents\n']
    n = 0
    for f, title, lang, note in ORDER:
        if not os.path.exists(os.path.join(TR, f)):
            continue
        n += 1
        out.append(f'{n}. **{title}** — *{lang}*  \n   {note}\n')
    return '\n'.join(out), n


def body():
    out = []
    n = 0
    for f, title, lang, note in ORDER:
        p = os.path.join(TR, f)
        if not os.path.exists(p):
            sys.stderr.write(f'  MISSING (not yet translated): {title}\n')
            continue
        n += 1
        text = open(p, encoding='utf8').read()
        # demote the file's own H1 so the book keeps one heading level
        text = re.sub(r'^# ', '### ', text, flags=re.M)
        text = re.sub(r'^## ', '#### ', text, flags=re.M)
        out.append(f'\n\n---\n\n# {n}. {title}\n\n*{lang}. {note}*\n\n{text}')
        sys.stderr.write(f'  [{n}] {title}\n')
    return ''.join(out), n


BACK = """

---

# Method

## Sources used

Analytical data only — the grammatical facts, never anyone's English:

- `hebrew-ot/morphhb` — Westminster Leningrad Codex with morphology (CC BY)
- `hebrew-ot/STEPBible-Data` — parse codes and root identification (CC BY)
- `greek-nt/morphgnt` — morphological tagging of the Greek New Testament
- `dead-sea-scrolls/etcbc-dss` — c. 250 BCE – 68 CE (CC BY-NC)
- `papyri/cntr-transcriptions` — the New Testament manuscripts themselves
- `septuagint/LXX-Rahlfs-1935`, `samaritan/sp`, `targums/`

Full credit in `ATTRIBUTION.md`. Every reading regenerates with
`./tools/allwitness.py <book> <ch> <vs>`.

## What was deliberately not used

No published translation. Also **not** the English glosses in the STEPBible data,
even though they sit in the same files as the parse codes we do use — those glosses
are other translators' work, and building on them would make this a revision of
their translation rather than a translation of the source.

That restriction is enforced by the tooling, not merely promised here.
`tools/analyze.py`, which the translations were made from, **cannot emit an English
gloss at all** — it outputs consonants, parse codes, root identification and the
witness readings, and nothing else. A translator working from it has nothing to copy.

For completeness, because a reader will find it: `tools/gloss.py` in this repo
*does* read those STEPBible glosses. It reports how often each English rendering has
been used for a given root across all 214,133 glossed words of the Hebrew Old
Testament. That is a tool for **seeing other translators' decisions**, and it is the
basis of nothing in this book. The distinction is between surveying how a root has
been rendered and adopting a rendering; only the first happened here.

## Scale, stated plainly

The Hebrew Old Testament is 306,785 words. The Greek New Testament is 137,779.
**444,564 words.** Translating that properly from the manuscripts is a career.

This book covers the passages where the most turns on the wording, done to the
standard above. It grows by adding passages. It will not be padded with fast work
to look complete, and it will not skip a hard word to keep the prose moving.

## Errors found in our own tools while making this

Recorded because they bear on whether the results can be trusted:

- A Text-Fabric parser dropped empty values and silently misaligned every glyph.
  Caught because four different sign types reported identical letter frequencies,
  which is impossible.
- The witness tool **merged all Dead Sea scrolls of a verse into one line**, hiding
  disagreements between them. A translator found Genesis 1:5 — where scroll 4Q2
  reads יום and 4Q7 reads יומם — by going to the raw node tables. Now fixed, and
  the tool flags scroll disagreement automatically.
- A divergence scan silently skipped Isaiah and Exodus because the scrolls corpus
  abbreviates them differently from the Masoretic corpus. It excluded the largest
  biblical scroll in existence while reporting a complete run.

Each produced output that looked correct. This is why every claim here ships with
the command that regenerates it.

*Assembled by `tools/makestudybook.py`. Translations are this project's own work.*
"""


def main():
    sys.stdout.write(FRONT)
    toc, n = contents()
    sys.stdout.write(toc)
    b, n2 = body()
    sys.stdout.write(b)
    sys.stdout.write(BACK)
    sys.stderr.write(f'\nassembled {n2} passages\n')


if __name__ == '__main__':
    main()
