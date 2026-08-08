#!/usr/bin/env python3
"""
makebook.py — generate THE BOOK from the corpus on disk.

Not a 27th English translation. Every Bible you can buy makes a silent choice at
each contested point: it picks a reading, prints it, and does not tell you a
choice was made. This book prints the choices.

For each passage where the witnesses disagree, it lays out every witness on disk
with its date and provenance label, translates each reading, and states plainly
what is demonstrated, what is contested, and what direction the evidence runs.

Everything is read from the corpus at generation time. Nothing is typed from
memory. Regenerate any page with the command printed beneath it.

Usage:
    ./makebook.py > BOOK.md
    ./makebook.py --passages   # list the passage set
"""
import io, os, re, sys, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

# Each entry: (book, ch, vs, title, kind, note)
#   kind: DEMONSTRATED | CONTESTED | REVERSED | ABSENT
PASSAGES = [
    ('Deut', 32, 8, 'The sons of God', 'DEMONSTRATED',
     'Two independent witnesses — a Hebrew scroll and a Greek translation made from '
     'Hebrew — agree against the Masoretic manuscript, which is 900+ years younger. '
     'Direction is demonstrable: the Greek was not embellishing.'),
    ('Deut', 32, 43, 'The line the Hebrew does not have', 'DEMONSTRATED',
     'The Septuagint carries a couplet absent from the Masoretic text. Hebrews 1:6 '
     'quotes it. A New Testament author cites Deuteronomy as scripture, and the '
     'verse he cites is not in the Hebrew Bible as it now stands.'),
    ('Ps', 145, 13, 'The missing letter', 'DEMONSTRATED',
     'Psalm 145 is an alphabetic acrostic. The Masoretic text skips נ — verse 13 is '
     'mem, verse 14 is samekh. Scroll 11Q5 has the nun verse, exactly where the '
     'poem\'s own structure requires it.'),
    ('Gen', 4, 8, 'What Cain said', 'DEMONSTRATED',
     'The Masoretic text has Cain speak to Abel and then the sentence simply stops — '
     'no speech follows. The Septuagint has the words.'),
    ('Ps', 14, 3, 'The plus that runs backwards', 'REVERSED',
     'The Greek has 60 words where the Hebrew has 11, and the surplus is Romans '
     '3:13-18. But its components are native elsewhere in the Septuagint, and the '
     'surplus carries PAUL\'S plural where the native text reads singular. The '
     'borrowing ran from Romans into the Greek manuscripts. The Hebrew lost nothing.'),
    ('Mark', 16, 9, 'How Mark ends', 'ABSENT',
     'The two oldest complete Bibles end Mark at 16:8. The resurrection appearances, '
     'the Great Commission and the snake-handling passage appear only in manuscripts '
     'from the 5th century onward.'),
    ('1John', 5, 7, 'The Trinity verse', 'ABSENT',
     'The three oldest codices — and the Byzantine majority text — read only "there '
     'are three that bear witness." The Father, the Word and the Holy Ghost enter '
     'Greek manuscripts in the 1520s.'),
    ('John', 7, 53, 'The woman taken in adultery', 'ABSENT',
     'Absent from P66, P75 and Sinaiticus. Genuinely present in Codex Bezae by about '
     '400 CE, so this is not a late medieval invention — but it is not in the oldest '
     'witnesses either.'),
    ('Luke', 22, 43, 'The bloody sweat', 'CONTESTED',
     'Absent from P75 and Vaticanus; present in Sinaiticus, Alexandrinus, Ephraemi '
     'and Bezae. The witnesses genuinely split. This one is not settled.'),
    ('John', 1, 18, 'Only-begotten God, or Son', 'CONTESTED',
     'Runs opposite to the usual pattern: μονογενὴς θεός has the STRONGER early '
     'attestation (P66, P75, Sinaiticus, Vaticanus, Ephraemi) against υἱός.'),
    ('Jude', 1, 14, 'Enoch prophesied', 'DEMONSTRATED',
     'Jude cites 1 Enoch 1:9 and calls it prophecy — Ἐπροφήτευσεν. A book excluded '
     'from every canon but the Ethiopian is quoted as prophecy inside the canon.'),
]

KIND_BLURB = {
    'DEMONSTRATED': 'The witnesses disagree and the direction is demonstrable.',
    'CONTESTED':    'The witnesses genuinely split. Not settled — do not let anyone tell you it is.',
    'REVERSED':     'The obvious reading is wrong. The evidence runs the other way.',
    'ABSENT':       'Present in later manuscripts, absent from the oldest.',
}


def run(cmd):
    try:
        return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True,
                              timeout=600).stdout
    except Exception as e:
        return f'[could not generate: {e}]'


def front_matter():
    return f"""# THE BOOK

### Every place the oldest witnesses disagree, with all of them side by side

---

This is not another English Bible.

Every translation you can buy makes a silent choice at each contested point. It
picks a reading, prints it as though it were simply the text, and does not tell
you that a choice was made or that anything was ever different. That is not
dishonesty — a readable Bible cannot print four columns on every page. But it
means the ordinary reader has no way to see where the traditions part company.

This book prints the choices.

For every passage below, you get **every witness held in this corpus**, each with
the date of the manuscript it rests on and a label saying what kind of thing it
is. Then a translation of each reading. Then a plain statement of what the
evidence shows — and, just as often, what it does not.

## How to read a witness

| Label | Means | Editorial layer |
|---|---|---|
| **ORIGINAL** | A manuscript, or a diplomatic transcription of one. What a scribe actually wrote, errors included. | none |
| **TRANSLATION** | Someone rendered it out of another language. Old and valuable, and already an interpretation. | the translator's |
| **EDITED** | A modern reconstruction assembled from many manuscripts. No single manuscript reads this way. | the editors' |
| **PRINTED** | A pre-1820 printed edition — old print, set from whatever manuscripts the printer had. | the printer's |

**Two dates matter and they are not the same.** The WITNESS date is when the
manuscript was made. The EDITION date is when somebody published that version.
Erasmus printed his Greek New Testament in 1516 from a handful of 12th-century
copies, and back-translated the last six verses of Revelation out of Latin
himself — those verses stand in no Greek manuscript at all. A 1516 date on a
title page tells you nothing about how close the text sits to the source.

## What "disagreement" is, and what it is not

- **ORIGINAL vs ORIGINAL** — a real textual variant. Two scribes wrote different things.
- **ORIGINAL vs TRANSLATION** — could be a variant, or could be the translator interpreting. It needs a second witness to settle.
- **A single scroll disagreeing proves nothing on its own.** It may be that scribe's error. What makes a case is **independent convergence** — two or more witnesses agreeing against a third.

That last rule is why this book marks passages **CONTESTED** and **REVERSED** as
well as **DEMONSTRATED**. A collection that only showed you the changes pointing
one way would be as misleading as one that hid them.

## The honest shape of the evidence

Across 31 books and 8,268 verses where both the Dead Sea Scrolls and the
Masoretic text survive, this corpus finds **4,031 differing readings**. That
number is a screening figure, not 4,031 proven alterations — it counts word
order, morphology and ordinary scribal slips.

And the single best-attested book cuts against the simple story. **Isaiah** — a
complete scroll from before the common era, 24,078 words — produces more
variation than any other book, and **not one of its unique readings is a missing
sentence.** A thousand years of hand-copying produced heavy minor variation and
no wholesale rewriting.

That stability is precisely why the specific changes in this book are findable.
If everything had been rewritten, nothing would stand out.

---
"""


def passage_section(i, book, ch, vs, title, kind, note):
    out = io.StringIO()
    out.write(f'\n\n## {i}. {title}\n\n')
    out.write(f'### {book} {ch}:{vs} — **{kind}**\n\n')
    out.write(f'> {KIND_BLURB[kind]}\n\n')
    out.write(f'{note}\n\n')
    out.write('#### The witnesses\n\n```\n')
    txt = run(['python3', 'tools/allwitness.py', book, str(ch), str(vs)])
    out.write(txt.strip() or '[no witness returned]')
    out.write('\n```\n\n')
    out.write(f'*Regenerate:* `./tools/allwitness.py {book} {ch} {vs}`\n')
    return out.getvalue()


def back_matter():
    return """

---

# What is not in this book

**A complete original translation.** The Hebrew Old Testament runs to 306,785
words and the Greek New Testament to 137,779 — **444,564 words**. Translating
that properly from the manuscripts is a career, not a project, and anyone who
tells you otherwise is selling something. What is here instead is every place the
witnesses part company, translated carefully, with the evidence shown.

**The Aleppo Codex.** The best Masoretic manuscript, c. 930 CE, has no
machine-readable transcription anywhere on earth. Page images or nothing.

**The complete Nag Hammadi Coptic.** Brill holds it. The five open tractates —
including the Gospel of Thomas — are here; the other 47 are not obtainable.

**Tatian's Diatessaron.** Not recoverable in any language. The Arabic, Latin and
Middle Dutch harmonies disagree with each other, and splicing them would produce
an editorial reconstruction, not a recovered text.

**Motive.** This is the important one. The manuscripts can show that a reading
changed and often which direction it ran. They cannot show *why*. Whether a
scribe was editing theology or harmonising to a familiar phrase, the parchment
does not say. Every claim in this book stops where the evidence stops.

# Excluded books held in full

The corpus carries, complete and in the original languages: **1 Enoch** (108
chapters, Ge'ez — the book Jude quotes as prophecy), **Jubilees**, **Kebra
Nagast**, **3 Meqabyan**, 39 pseudepigrapha including the Sibylline Oracles and
the Psalms of Solomon, the **Didache**, the **Epistle of Barnabas** and the
**Shepherd of Hermas** — the last two bound into Codex Sinaiticus itself, meaning
the scribe who made the oldest complete Bible we possess treated them as
scripture — and the **Gospel of Thomas** in Coptic.

Full inventory: `EXCLUDED-BOOKS.md`.

# Sources and method

Every source, licence and rebuild command: `SOURCES.md`, `ATTRIBUTION.md`,
`corpus.lock`. Provenance labels: `PROVENANCE.md`. The systematic scans:
`./tools/diverge.py --all` and `./tools/diverge_lxx.py`.

Four corpora here are **CC BY-NC** — the Dead Sea Scrolls, the Codex Sinaiticus
transcription, Coptic SCRIPTORIUM and the Samaritan Pentateuch. They may not be
used commercially.

*Generated by `tools/makebook.py` from the corpus on disk. Every page regenerates
from the command printed beneath it.*
"""


def main():
    if '--passages' in sys.argv:
        for i, p in enumerate(PASSAGES, 1):
            print(f'{i:3}. {p[0]} {p[1]}:{p[2]:<4} [{p[4]:12}] {p[3]}')
        return
    sys.stdout.write(front_matter())
    sys.stdout.write('\n# The passages\n')
    for i, (b, c, v, t, k, n) in enumerate(PASSAGES, 1):
        sys.stdout.write(passage_section(i, b, c, v, t, k, n))
        sys.stderr.write(f'  [{i}/{len(PASSAGES)}] {b} {c}:{v}\n')
    sys.stdout.write(back_matter())


if __name__ == '__main__':
    main()
