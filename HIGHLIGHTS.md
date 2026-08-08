# Highlights — readings found nowhere else, and readings that were changed

Every entry regenerated from disk on 2026-08-08. Reproduce any of them with the
command shown. Nothing here is quoted from memory or from secondary literature.

**How to read the labels**

- ⭐ **UNIQUE** — present in an original witness, absent from the Bible you can buy
- 🔄 **CHANGED** — the witnesses disagree, and the direction is demonstrable
- ⚠️ **ONE WITNESS ONLY** — a single scroll or manuscript. Real, but a single
  scroll's reading may be that scribe's own error rather than evidence the other
  tradition changed. Two independent witnesses agreeing is what makes a case.

---

## ⭐ Psalm 145 — the missing letter

Psalm 145 is an alphabetic acrostic: each verse opens with the next Hebrew letter.
**The Masoretic text skips נ (nun)** — verse 13 is מ (mem), verse 14 is ס (samekh).
A poem built on the alphabet is missing a rung, and has been in every printed
Hebrew Bible for a thousand years.

**Scroll 11Q5 has it**, in exactly the position the acrostic requires:

> **נאמן אלוהים בדבריו וחסיד בכול מעשיו**
> *"God is faithful in his words, and gracious in all his deeds."*

```bash
./tools/allwitness.py Ps 145 13
```

Two further things visible in the same verse:

1. **11Q5's Psalm 145 carries a refrain after every verse** —
   **ברוך יהוה וברוך שמו לעולם ועד**, *"Blessed be YHWH and blessed be his name
   forever and ever."* Not in the Masoretic text at all. This is a liturgical,
   antiphonal edition of the psalm.
2. **The Tetragrammaton is written in paleo-Hebrew script** inside an
   otherwise square-script scroll — `allwitness.py` marks it `[paleo]`. See
   `docs/RESEARCH-divine-name.md`: 286 of the corpus's Tetragrammata are written
   this way.

---

## 🔄 Deuteronomy 32:8 — sons of God, or sons of Israel

| Witness | Date | Reads |
|---|---|---|
| **Scroll 4Q37** | c. 250 BCE – 68 CE | בני **אלוהים** — "sons of **God**" |
| Septuagint | MS c. 300–325 CE | ἀγγέλων **θεοῦ** — "angels of **God**" |
| Masoretic (Leningrad) | 1008 CE | בני **ישראל** — "sons of **Israel**" |

```bash
./tools/allwitness.py Deut 32 8
./tools/diverge.py Deut 32
```

**Direction is demonstrable here**, because two independent witnesses agree
against the third: a Hebrew scroll and a Greek translation made from a Hebrew
text, both centuries older than the Masoretic manuscript. The Greek was not
embellishing — it was translating a Hebrew text that read אלוהים.

On the older reading, Elyon apportions the nations among divine beings and YHWH
receives Jacob as his share. The Ugaritic material supplies the framework: KTU 1.4
names El's **seventy sons of Athirat** as a fixed divine council — see
`docs/RESEARCH-ane-parallels.md`, marked WIDELY ACCEPTED there.

**What this does not establish:** motive. The text shows the reading changed and
which way. Whether that was theological editing or a scribe harmonising to a
familiar phrase, the manuscripts cannot say.

---

## 🔄 Deuteronomy 32:43 — a line the Hebrew does not have

The Septuagint has a couplet the Masoretic text lacks, including
`προσκυνησάτωσαν αὐτῷ πάντες υἱοὶ θεοῦ` — *"let all the sons of God worship him."*

**Hebrews 1:6 quotes it**: `Καὶ προσκυνησάτωσαν αὐτῷ πάντες ἄγγελοι Θεοῦ`.

A New Testament author cites Deuteronomy as scripture, and the verse he cites is
not in the Hebrew Bible as it now stands.

```bash
./tools/allwitness.py Deut 32 43
./tools/allwitness.py Heb 1 6 --greek-only
```

---

## ⭐ Jude quotes 1 Enoch as prophecy

`Ἐπροφήτευσεν δὲ καὶ τούτοις ἕβδομος ἀπὸ Ἀδὰμ Ἑνώχ` — *"And Enoch, seventh from
Adam, also prophesied…"* Not "as it is written." **Prophesied.**

| Jude 14–15 (Greek) | 1 Enoch 1:9 (Ge'ez) |
|---|---|
| Ἰδοὺ ἦλθεν Κύριος ἐν ἁγίαις μυριάσιν αὐτοῦ | ወናሁ መጽአ በትእልፊት ቅዱሳን |
| ποιῆσαι κρίσιν κατὰ πάντων | ከመ ይግበር ፍትሐ ላዕሌሆሙ |
| ἐλέγξαι πάντας τοὺς ἀσεβεῖς | ወይትዋቀሥ ኵሎ ዘሥጋ |
| περὶ πάντων τῶν σκληρῶν ὧν ἐλάλησαν κατ' αὐτοῦ | በእንተ ኵሉ ዘገብሩ … ኃጥኣን ወረሲዓን |

1 Enoch is in **no Bible except the Ethiopian**. It is on this disk complete,
108 chapters, `ethiopic/ethiopian-bible/public/data/chapters/1En/`.

---

## 🔄 Mark 16:9–20 — absent from the two oldest complete Bibles

```bash
./tools/allwitness.py Mark 16 9 --greek-only
```

> ABSENT — extant here but do NOT contain this verse:
> ✗ Codex Vaticanus (c. 300–325 CE) · ✗ Codex Sinaiticus (c. 330–360 CE)

Sinaiticus's Mark has chapters 1–16; chapter 16 has verses 1–8 and stops. The
resurrection appearances, the Great Commission, and the snake-handling passage are
present in Alexandrinus, Ephraemi, Bezae and Washingtonianus — all **5th century
or later**. Codex W adds a further unique interpolation on top (the Freer Logion).

---

## 🔄 1 John 5:7 — the Trinity verse

The three oldest codices read only:

> ὅτι τρεῖς εἰσιν οἱ μαρτυροῦντες — *"there are three that bear witness."*

The words *"in heaven: the Father, the Word, and the Holy Ghost: and these three
are one"* are **not there** — not in Sinaiticus, Vaticanus, Alexandrinus, **nor
even in the Byzantine majority text**. They enter Greek manuscripts in the 1520s.

```bash
./tools/allwitness.py 1John 5 7 --greek-only
```

---

## 🔄 1 Timothy 3:16 — one letter, changed in the manuscript itself

**ΟΣ** ("who was manifest") vs **ΘΣ** ("God was manifest"). In Codex Alexandrinus
the transcription records a **later corrector physically altering ΟΣ to ΘΣ** — the
change is visible in the same manuscript. See `docs/RESEARCH-variants.md`.

---

## ⭐ Numbers 21:12 — a speech of YHWH in one scroll only

⚠️ **ONE WITNESS ONLY — direction runs the other way here.**

**Scroll 4Q27** carries a full divine speech that both the Masoretic text and the
Septuagint lack:

> ויואמר יהוה אל מושה אל תצר את מואב ואל תתגר ב׳ם מלחמה כיא לוא אתן מארצ׳ו
> ירושה כיא לבני לוט נתתי את ער ירושה
>
> *"And YHWH said to Moses: Do not harass Moab, and do not provoke them to war,
> for I will not give you any of his land as a possession, for to the sons of Lot
> I have given Ar as a possession."*

Then both traditions continue: *"From there they set out and camped in the Wadi Zered."*

**Read this cautiously.** The material closely parallels **Deuteronomy 2:9**, and
4Q27 stands alone — the Septuagint sides with the Masoretic text. The likelier
reading is that **this scroll expanded**, harmonising Numbers toward Deuteronomy,
not that the other two traditions cut it. A plus in one witness is not automatically
something that was taken out.

```bash
./tools/allwitness.py Num 21 12
```

---

## 🔄 Psalm 14:3 — the plus that runs BACKWARDS

⚠️ **The obvious reading of this one is wrong. Worth studying as a method case.**

The Masoretic Ps 14:3 has **11 words**. The Septuagint's Ps 13:3 has **60**. It looks
like a textbook case of the Hebrew losing a passage.

```bash
./tools/diverge_lxx.py            # flags it at 11 vs 60
```

The Greek plus is **Romans 3:13–18**, essentially verbatim. But the pieces of it are
**native elsewhere in the Septuagint**:

| Phrase in the plus | Where it actually belongs |
|---|---|
| τάφος ἀνεῳγμένος ὁ λάρυγξ αὐτῶν | LXX Ps **5:10** |
| ἰὸς ἀσπίδων ὑπὸ τὰ χείλη αὐτῶν | LXX Ps **139:4** |
| ἀρᾶς τὸ στόμα … γέμει καὶ πικρίας | LXX Ps **9:28** |
| οὐκ ἔστιν φόβος θεοῦ ἀπέναντι τῶν ὀφθαλμῶν | LXX Ps **35:2** |

**The decisive detail — grammatical number.** LXX Ps 9:28 reads **singular**:
`οὗ ἀρᾶς τὸ στόμα αὐτοῦ γέμει` — *"whose mouth is full of cursing."* Paul needed a
plural for his argument about all humanity and wrote `ὧν τὸ στόμα … αὐτῶν`.
**Ps 13:3 carries Paul's plural, not the native singular.** LXX Ps 35:2 shows the
same: native `αὐτοῦ`, but `αὐτῶν` in the Ps 13:3 plus.

A copyist importing from Psalms would have brought the singular. Only a copyist
importing **from Romans** brings the plural.

**Direction: Romans → Septuagint manuscripts.** Paul assembled a catena from
scattered psalms (and Isaiah 59:7–8), and later Greek manuscripts absorbed his chain
back into Psalm 13:3. **The Hebrew did not lose anything here.**

> This is the counterweight to Deut 32:43 / Hebrews 1:6. There, the New Testament
> quotes something genuinely absent from the Hebrew. Here, it looks identical on the
> surface and the arrow points the other way. **A plus in the Greek is not by itself
> evidence the Hebrew was cut** — you have to find which direction the borrowing ran.

---

## ⭐ Psalm superscriptions absent from the Masoretic text

**Psalm 99:1** — two *independent* scrolls, **4Q92** and **4Q98e**, both carry a
superscription **מזמור לדוד** ("A psalm of David") that the Masoretic text does not.

Two independent witnesses agreeing is materially stronger than one, and this is the
cleanest such case in the scan. **Psalm 33:1** shows the same pattern in 4Q98
(**שיר מזמור לדויד**), there on a single witness.

---

## The systematic scan

```bash
./tools/diverge.py --all
```

Comparing every Dead Sea Scroll against the Masoretic text, **per scroll**, on the
consonantal skeleton only:

Across **31 biblical books**, 8,268 verses where both witnesses have text:

| Category | Readings |
|---|---:|
| **CHANGED** — both have it, the text differs | **4,031** |
| **MT-ONLY** — Masoretic has words the scroll does not | 1,186 |
| **DSS-ONLY** — scroll has words the Masoretic does not | **167** |
| *FRAGMENTARY* — scroll damaged here, **not** a variant | *707* |
| *SPELLING* — vowel-letters only (ו/י), **not** a variant | *1,217* |

Counts are **readings, not verses** — where several scrolls cover one verse, each
scroll is a separate row. That is why Isaiah shows 1,466 changed readings across
1,291 shared verses.

Largest bodies of variation: **Isaiah** 1,291 verses / 1,466 changed ·
**Exodus** 805 / 370 · **Deuteronomy** 679 / 557 · **Psalms** 1,261 / 567.

### The Isaiah result cuts against a simple story

Isaiah is the best-attested book here — 1QIsaa is a *complete* Isaiah from before
the common era, 24,078 words. It produces the most differences of any book, and
**almost every one is small**: a suffix, a conjunction, a spelling, an occasional
single word (4Q56 adds צבאות at 19:19; 4Q56 adds אדני at 26:4; 1QIsaa adds יהודה
at 4:2). Of Isaiah's 24 DSS-ONLY readings, **not one is a missing sentence, let
alone a missing passage.**

So for Isaiah, a thousand years of copying produced heavy minor variation and
**no large-scale rewriting**. That is a real finding and it belongs next to the
others. The picture the evidence actually supports is: **a substantially stable
text carrying specific, locatable, sometimes theologically weighty variants** —
Deut 32:8, Psalm 145's nun verse, the Psalm superscriptions — not wholesale
alteration. Both halves of that sentence are load-bearing.

Vowel points are excluded from the comparison on purpose: the Masoretes added them
c. 7th–10th c. CE, a thousand years after these scrolls, so comparing them would
report differences that are not textual variants at all.

### ⚠️ Read these totals honestly

**2,732 is a screening number, not 2,732 proven alterations.** It counts every
consonantal difference between one scroll and the Masoretic text, which includes
word order, morphological variants, and ordinary scribal slips. **A single scroll
disagreeing is not evidence the Masoretic text was changed** — it may be that
scribe's error.

What raises a reading to real evidence is **independent convergence**: two or more
witnesses agreeing against the third, as with Deut 32:8 (scroll + Septuagint) and
Psalm 99:1 (two scrolls). Those are the cases worth building on.

### Known limits of the scan

- **Multi-scroll merging was a bug here and is fixed.** Before the fix, all scrolls
  of a book were bagged together per verse, so disagreements *between scrolls*
  registered as disagreements with the Masoretic text — inflating DSS-ONLY 4.7×.
  Any future comparison must key by scroll (`tools/dssmap.py`).
- **Book-name mismatch was a second bug, also fixed.** The DSS corpus calls Isaiah
  `Is` and Exodus `Ex`, where morphhb uses `Isa`/`Exod` — so the first complete run
  **silently skipped both**, including the largest biblical scroll in existence. It
  also counted scroll acronyms (`4Q37`, `PAM43113`, `X4`) as if they were books,
  reporting "123 books" for a corpus that has 31. Both fixed in `dss_book_name()`.
  The lesson generalises: a scan that silently skips is worse than one that errors,
  because the output still looks complete.
- The 0.55-length damage threshold is a heuristic. Some fragmentary verses will
  still be miscounted as variants.
- The scan covers **Hebrew only**. A parallel LXX-vs-MT scan is not built yet, and
  `allwitness.py`'s LXX lookup currently maps only Genesis–2 Chronicles, so Psalms
  and the Prophets return no Greek witness.
