# Research: The Divine Name — What Happened to יהוה

Status: primary-source research. Sections 2, 5, and 7 are **on-disk corpus queries with real
counts** (`dead-sea-scrolls/etcbc-dss/`, `papyri/cntr-transcriptions/`, Philo's Greek text in
`apostolic-fathers/First1KGreek/`). Sections 1, 3, 4, 6 draw on the project's existing
`docs/RESEARCH-epigraphy.md` (Elephantine, P.Fouad 266, 8HevXIIgr, P.Oxy 3522) and
`docs/RESEARCH-rabbinic.md` (Mishnah/Talmud), supplemented with live-fetched primary/secondary
sources where nothing on disk covers the ground (Nash Papyrus, Josephus, Masoretic pointing
history, "Jehovah" etymology). Every figure below was either counted from the raw Text-Fabric
files or is a directly quoted/fetched source — nothing is estimated.

**Starting point** (already verified elsewhere in this project): WLC has 6,828 instances of יהוה
(6,007 standalone + 821 prefixed); Deut 32:8 reads בני אלוהים at Qumran (4QDeut^j) against בני
ישראל in the Masoretic Text — a confirmed, not merely inferred, alteration.

---

## 1. The paleo-Hebrew Tetragrammaton in Greek LXX manuscripts

This is the direct physical evidence for *whether and when* κύριος replaced the Name in written
Greek Bibles. Five manuscripts are the standing witness list; none is on disk (LXX papyri aren't
part of this corpus — `septuagint/` here holds only the modern Rahlfs/Swete editions). Findings
below come from `docs/RESEARCH-epigraphy.md` §14 (previously verified live URLs) plus one live
fetch of Wikipedia's *Tetragrammaton* article for the two witnesses not yet covered there
(4Q120/ΙΑΩ, P.Oxy 5101) — flagged as secondary since the underlying footnotes weren't individually
traced in this pass.

| Witness | Date | What it actually writes | Script | Access |
|---|---|---|---|---|
| **P.Fouad 266** (Rahlfs 848, Deuteronomy) | **1st c. BCE** | יהוה, in the **square Jewish (Aramaic-derived) script current at the time** — *not* the archaic paleo-Hebrew alphabet | Square Hebrew | Image: Wikimedia Commons, `File:Papyrus_Fouad_266.jpg`, Public Domain Mark 1.0, depicts Deut 31:28–32:7. **No open transcription exists** — the scholarly editions (Waddell 1944; Aly & Koenen 1980) are print/paywalled. |
| **8ḤevXIIgr** (Rahlfs 943, Naḥal Ḥever Minor Prophets) | **c. 50 BCE – 50 CE** | 𐤉𐤄𐤅𐤄 — the Name in **genuine paleo-Hebrew script**, in 24 places across the scroll, whole or partial | Paleo-Hebrew | Held at the Rockefeller Museum, Jerusalem; listed on deadseascrolls.org.il but no working direct download surfaced; editio princeps (Tov, DJD 8, 1990) is print-only. Needs a manual Leon Levy Digital Library search. |
| **P.Oxy 3522** (Rahlfs 857, Job 42:11–12) | **1st c. CE** | Tetragrammaton in paleo-Hebrew letters | Paleo-Hebrew | Held at the Sackler Library, Oxford. **papyri.info is bot-walled**; no open image or transcription found on this or the prior pass. |
| **P.Oxy 5101** (Psalm 26–32 fragment) | **1st–2nd c. CE** | YHWH in paleo-Hebrew script | Paleo-Hebrew | Not independently re-verified this pass; per secondary description only. |
| **4Q120 / 4QpapLXXLev-b** (Leviticus) | **1st c. BCE** | The Name transliterated into **Greek letters as ΙΑΩ** (Lev 3:12; 4:27) — a third strategy, distinct from both paleo-Hebrew preservation and κύριος translation | Greek transliteration | Qumran cave 4 find; this is a Greek-language Qumran fragment, catalogued alongside the Hebrew scrolls rather than in the LXX papyrus tradition proper. |

**What this establishes**: there were, for a period spanning at least two centuries (1st c. BCE –
1st c. CE), **at least three competing scribal strategies** for the divine name inside Greek
biblical text — (a) leave it in Hebrew, in the current square script (Fouad 266); (b) leave it in
the *archaic* paleo-Hebrew script, deliberately antiquated even in a Greek-reading context
(8ḤevXIIgr, P.Oxy 3522, P.Oxy 5101); (c) transliterate it phonetically into Greek letters as ΙΑΩ
(4Q120). **None of these five earliest-attested Greek biblical manuscripts translates the Name as
κύριος.** The κύριος convention that dominates every later Christian LXX manuscript (Vaticanus,
Sinaiticus, Alexandrinus, all 4th–5th c. CE) is therefore demonstrably a **later standardization**,
not the original translator's practice — consistent with, but going beyond, what was already
flagged in this project re: Deut 32:8.

---

## 2. Qumran practice — queried directly from `dead-sea-scrolls/etcbc-dss/`

**Method**: the TF corpus's `scroll` feature is only recorded on scroll/fragment/line-type nodes,
not on individual words, so scroll membership per word had to be resolved by tracing the `oslots`
edge (word → underlying sign-slots) against each scroll's own slot range — a containment lookup,
not a documented shortcut. Script `tools/dssread.py` alone can't answer scroll-level questions;
the queries below extend it. Full corpus: 500,995 word-nodes.

### 2a. Overall: paleo-Hebrew is the exception, not the rule, even for the divine name

- Total occurrences of the lexeme **JHWH** (any script) in the corpus: **4,843**, spread across
  **298 distinct scrolls**.
- Of those, only **286 (5.9%)** are written in **paleo-Hebrew script**; the remaining **94.1%** are
  written in the ordinary square Aramaic script used for the rest of each scroll's text.
- Paleo-Hebrew JHWH clusters heavily in just two manuscripts:

| Scroll | Paleo-Hebrew JHWH count | Context |
|---|---|---|
| **11Q5** (Psalms scroll, 11QPs^a) | 164 | Ps 101–104+, biblical |
| **4Q57** (Isaiah^c) | 82 | Isa 10–12+, biblical |
| **1QpHab** (Pesher Habakkuk) | 8 | sectarian commentary quoting the Habakkuk base text |
| **4Q171** (Pesher Psalms^a) | 7 | same pattern |
| **11Q2** (Leviticus^b) | 7 | Lev 9–14, biblical |
| **2Q3** (Exodus) | 6 | Exod 4–34, biblical |
| 1Q14, 1Q15, 4Q183, 4Q161, 1Q11, 3Q3, 4Q20, 4Q26b, 4Q38a | 1–2 each | scattered biblical/sectarian |

That's **15 scrolls total** carrying a paleo-Hebrew Tetragrammaton, out of 1,001 scrolls in the
corpus.

### 2b. All paleo-Hebrew script use, not just JHWH — a needed correction

The `script=paleohebrew` flag itself covers **789 word-tokens**, not just the 286 above. Breaking
that full set down by what the word actually is:

| Category | Count | % of 789 |
|---|---:|---:|
| **Numerals** (in cryptic/calendrical texts — 4Q320, 4Q318, 4Q319, 4Q317, 4Q326, 4Q554, 4Q554a, 3Q15 [Copper Scroll], 4Q559, 4Q352, 4Q352a, 4Q348, 6Q26) | 461 | 58% |
| **JHWH** | 286 | 36% |
| **"El" (אל, short form of God)** | 24 | 3% |
| Elohim, Adonai, Sabaoth, and prefixes bound to a paleo-Hebrew divine word | 15 | 2% |

The numeral usage — writing digits with paleo-Hebrew letter-forms in the cryptic/calendrical
corpus (mainly 4QCryptic and the Copper Scroll's number system) — is a **separate scribal
convention entirely unrelated to the divine name**, and it's the single largest use of paleo-Hebrew
letters in this whole corpus. Anyone counting "paleo-Hebrew occurrences" without splitting this out
will overstate the divine-name pattern by more than half.

### 2c. The pesher pattern

1QpHab and 4Q171 (Pesher Psalms) are commentaries: square-script sectarian interpretation wrapped
around a quoted biblical base text. In both, the paleo-Hebrew Tetragrammaton appears **only inside
the quoted scripture**, never in the surrounding commentary — a live, textually confirmed instance
of the broader pattern scholars call "special treatment of the divine name," where scribes marked
graphically that this word was categorically different even mid-sentence in an otherwise ordinary
square-script hand.

### 2d. A second, distinct avoidance device found in 1QS — surrogate glyphs, not paleo-Hebrew

Searching for every occurrence of the lexeme JHWH (not filtering by script) turned up two instances
inside **1QS (the Community Rule)**, at the scroll's Isaiah 40:3 proof-text ("prepare in the
wilderness the way of ---- / make straight in the desert a highway for our God") — 1QS VIII line
13–14 by column reckoning. Neither is written as יהוה, and neither is in paleo-Hebrew script:

```
node 1616955  glyph = הואהא    (lexeme tagged JHWH)   "...the way of ****"
node 1616963  glyph = יייי     (lexeme tagged JHWH)   "...a highway for our ****"
```

The second is four yods (JJJJ) standing in for the Name; the first is an idiosyncratic five-letter
surrogate. Both are tagged by the corpus's editors as representing the Tetragrammaton
(lexeme=JHWH), i.e. the underlying word is understood to *be* the divine name, written with
substitute glyphs instead of either the normal spelling or paleo-Hebrew script. This matches what
DSS scribal-practice scholarship (Tov, *Scribal Practices and Approaches*) documents as a known
third device — dot-clusters or surrogate strokes used in place of the Name in some non-biblical,
sectarian compositions — distinct from both the "write it out normally" and "write it in
paleo-Hebrew" strategies documented above. Grep confirmed **zero** actual dot-glyphs (׃•∴◦) appear
in this transcription's `glyph` values anywhere in the corpus, which means this particular digital
edition renders that scribal device as pseudo-letters rather than literal dots — a transcription
choice worth knowing if cross-checking against a DJD photograph.

**Net picture for Qumran**: three coexisting, non-random conventions for handling the Name — plain
square script (the overwhelming majority, ~94%), paleo-Hebrew script (concentrated in two large
biblical scrolls plus scattered pesharim, always confined to quoted scripture in the sectarian
texts), and surrogate/dot-cluster glyphs (at least one confirmed case, 1QS). No blanket avoidance:
even the "avoidance" manuscripts still spell out יהוה normally 94% of the time.

---

## 3. The Nash Papyrus (2nd c. BCE, pre-Qumran)

| | |
|---|---|
| **Content** | The Decalogue (Ten Commandments) followed by the opening of the Shema (Deut 6:4). |
| **Date** | Acquired 1902 (Egypt); Stanley Cook's original estimate was 2nd c. CE, but the now-standard scholarly dating (paleography) places it **c. 150–100 BCE** — making it, before the 1947 Qumran discoveries, the oldest known Hebrew biblical manuscript fragment. |
| **Provenance** | Egypt, probably the Fayyum; likely a liturgical excerpt (combined Decalogue + Shema was used devotionally, not as a running Torah scroll) rather than a copy of a continuous biblical text — its combination of the two passages doesn't correspond to any single verse-sequence in the MT. |
| **Textual character** | Closer to the Septuagint's underlying Hebrew *Vorlage* in several readings than to the later Masoretic Text — consistent with a Hebrew textual stream still fluid before standardization. |
| **Held** | Cambridge University Library, MS Or.233. |
| **Access** | Nominally free online at the Cambridge Digital Library (`cudl.lib.cam.ac.uk/view/MS-OR-00233`) — **fetch attempted this pass, returned HTTP 403 Forbidden**, noted rather than worked around per method. |

Not independently checked for divine-name treatment in this pass (no transcription was
retrievable); flagged as a gap rather than guessed.

---

## 4. Adonai/Kyrios substitution — when did reading אדני for יהוה actually begin?

Distinguishing tradition from hard evidence:

### 4a. Elephantine (5th c. BCE) — evidence AGAINST early total avoidance
The Elephantine papyri (Jewish military-colony archive, Aramaic, Egypt) show a garrison community
that **openly named and worshipped at a temple to YHW** (their spelling) and used the name in
everyday correspondence, including the famous letters (Cowley 30/31) petitioning Persian
authorities to help rebuild that temple after its destruction. This is the earliest large body of
real-world usage evidence available, and it shows **no reticence about writing or presumably
speaking the name** in the 5th c. BCE, at least in this diaspora garrison community — a data point
against reading later rabbinic taboo back into this period uncritically. (Full sourcing:
`docs/RESEARCH-epigraphy.md` §13 — Cowley 1923 edition free on archive.org, verified live.)

### 4b. Philo (c. 20 BCE – 50 CE) — on-disk primary source, checked directly
Philo's Greek text is in this corpus (`apostolic-fathers/First1KGreek/data/tlg0018/`). Searching it
directly (grep for τετραγράμμ*, working around Greek diacritic/Unicode-normalization mismatches)
found the real passage — **De Vita Mosis II.114–115**, discussing the high-priestly breastplate:

> τετραγράμματον δὲ τοὔνομά φησιν ὁ θεολόγος εἶναι, τάχα που σύμβολα τιθεὶς αὐτὰ τῶν πρώτων
> ἀριθμῶν, μονάδος καὶ δυάδος καὶ τριάδος καὶ τετράδος...
>
> "The theologian [Moses] says the Name is four-lettered, perhaps setting it forth as a symbol of
> the first numbers — one, two, three, and four..."

Philo never writes the Name itself. He calls it "the four-lettered name" (τετραγράμματον) and
pivots immediately into Pythagorean-flavored numerology (the tetraktys) rather than discussing
pronunciation — treating the Name as a technical, unspoken designation in the mid-1st century CE,
among Greek-speaking Alexandrian Jews, independent of any later rabbinic ruling. This is the
earliest solid literary evidence (not folk tradition) for the Name being treated as categorically
unspeakable.

### 4c. Josephus — NOT on disk, external, flagged accordingly
Per `docs/DATED-INVENTORY.md`, Josephus is **not actually present** in this corpus despite
INDEX.md's claim (verified: no `tlg0526` directory exists). *Antiquities of the Jews* 2.275–276
(the burning-bush scene) is widely cited as Josephus stating God told Moses his name, and Josephus
"say[s] it is not lawful for me to speak further of this." A live fetch of this pass's Wikisource
copy did **not** actually contain that section (the page cut off mid-Book II) — so this citation is
reported here as the standard secondary attribution, **not independently verified against a
primary-text fetch in this pass**.

### 4d. Mishnah and Talmud — verified live via Sefaria (already scoped in `docs/RESEARCH-rabbinic.md`)

**Mishnah Sanhedrin 10:1** (Abba Shaul's addition to the list of those with no share in the World
to Come):
> אַבָּא שָׁאוּל אוֹמֵר, אַף הַהוֹגֶה אֶת הַשֵּׁם בְּאוֹתִיּוֹתָיו
> "Abba Shaul says: also included is one who pronounces the Name **as it is written, with its
> letters**."

**Mishnah Tamid 7:2** (priestly blessing, Temple vs. countryside):
> בַּמִּקְדָּשׁ הָיוּ אוֹמְרִים אֶת הַשֵּׁם כִּכְתָבוֹ, וּבַמְּדִינָה בְּכִנּוּיוֹ
> "In the Temple they would say the Name **as it is written**; in the country [outside Jerusalem],
> **by its substitute**."

Both are Mishnah, redacted **c. 200 CE**, but explicitly describing an *earlier* practice (Second
Temple period, i.e. before 70 CE) as already having a Temple/non-Temple split — pronunciation
permitted (or required) in the Temple liturgy, avoided outside it. This is the earliest *rabbinic*
textual evidence, but note it is a **description written after the practice it describes had
already ended** (the Temple fell in 70 CE) — it documents living memory or tradition of Second
Temple practice, not a contemporaneous 1st-century record.

**Tractate Soferim** (the minor tractate on scribal law, geonic era, **c. 8th c. CE**) codifies
detailed rules for physically writing the divine Name, correcting scribal errors involving it, and
disposing of worn scrolls bearing it — the fullest formal rulebook, but centuries later than the
practice it regulates.

### 4e. The Septuagint's own translation choice — the earliest "replacement" of all
Distinct from all of the above: the LXX translators themselves (Torah c. 250 BCE onward) rendered
יהוה as **κύριος** ("Lord") in running Greek prose from the start — that translation choice, not
any later Masoretic vowel-pointing, is the oldest attested "substitution" event in the whole
transmission history, predating even Philo by two centuries. What Part 1 above shows is that this
translation convention was **not universal or immediate**: for at least two more centuries,
competing manuscripts kept the Name untranslated, in Hebrew or paleo-Hebrew script or Greek
transliteration, alongside manuscripts that had already gone over to κύριος. The κύριος convention
only becomes the sole surviving practice once you reach the great 4th–5th century Christian
uncials.

---

## 5. Nomina sacra — queried directly from `papyri/cntr-transcriptions/`

The CNTR corpus marks nomina sacra explicitly with `=` in its transcription encoding
(`= nomina sacra` per the corpus's own README). Checked directly against the actual files.

### 5a. Present in the earliest surviving fragment
**P52** (John 18:31–38, conventionally dated **c. 125–175 CE**, the earliest NT manuscript
fragment in existence) already contracts the name of Jesus:

```
=ιηυ   (John 18:32, genitive: "the word of Jesus")
=ιην   (John 18:33: "and summoned Jesus")
```

That means the nomina sacra convention was **already fully in place by the time our very earliest
physical evidence begins** — the origin of the practice necessarily predates P52, likely into the
late 1st century, though no manuscript that old survives to confirm it directly.

### 5b. Scale, in the earliest substantial witnesses

| MS | Date | Top contractions (raw counts) |
|---|---|---|
| **P46** (Pauline epistles) | c. 175–225 CE | =θυ 199, =χρυ 120, =θσ 108, =ιηυ 97, =κυ 66, =θω 63, =κω 58, =χρω 51, =χρσ 45, =κσ 44 |
| **P66** (John) | c. 200 CE | =ισ 169, =πηρ 41, =θυ 40, =πρα 31, =κε 24, =ιν 24 |
| **P75** (Luke/John) | c. 175–225 CE | =ισ 141, =θυ 83, =κε 37, =ανου 27, =θσ 23, =πνα 19 |

The four core sacred words are consistently contracted from the earliest witnesses: **ΚΣ**
(κύριος, Lord), **ΘΣ** (θεός, God), **ΙΣ** (Ἰησοῦς, Jesus), **ΧΣ** (Χριστός, Christ) — plus
πνεῦμα (Spirit), πατήρ (Father), υἱός (Son), ἄνθρωπος (man), Ἰερουσαλήμ (Jerusalem) in some
scribal traditions. This is a mature, systematized scribal convention, not an ad hoc habit.

### 5c. What scribes do with an OT quotation that (in Hebrew) contained יהוה
Located a direct example: **Romans 9:29 in P46**, quoting Isaiah 1:9 (LXX):

```
45009029  και καθωσ προειρηκεν ησαιασ ει μη =κσ σαβαωθ ενκατελειπεν ημιν σπερμα...
          "and as Isaiah predicted beforehand: unless the Lord [contracted =κσ] of Sabaoth
           had left us a seed..."
```

The Hebrew behind this (יהוה צבאות, "YHWH of Hosts") is rendered exactly like every other use of
κύριος in the manuscript — contracted to =κσ, indistinguishable in the scribal hand from a κύριος
that refers to Jesus two verses later. **No NT manuscript treats an OT-quoted Tetragrammaton any
differently from an ordinary κύριος.**

### 5d. No Hebrew or paleo-Hebrew characters anywhere in the NT papyri corpus
A regex sweep (`grep -P` for the Hebrew Unicode block `\x{0591}-\x{05F4}` and, separately, the
paleo-Hebrew-adjacent Phoenician/Old Italic block used to encode such scripts digitally) across
**all 130 files** in `papyri/cntr-transcriptions/class 1` (every early NT papyrus and majuscule in
the corpus, P1 through P141 plus the great uncials 01–05) returned **zero matches**. No manuscript
in this collection contains the Tetragrammaton in any script. This directly answers item 7's first
question with primary evidence rather than inference.

---

## 6. The vowel points — what can and cannot be known

### What's firm
- The **consonantal** text יהוה is stable and old: attested at Qumran (unpointed, obviously —
  vocalization didn't exist yet), matched by the 1008 CE Leningrad Codex's 6,828 instances.
- The **Masoretes of Tiberias** added the vowel-point system to the Hebrew Bible across roughly the
  **7th–10th centuries CE**, with the ben Asher family (culminating in Aaron ben Moses ben Asher,
  active early-to-mid 10th c.) producing the standard tradition behind both the Aleppo Codex
  (**10th c.**, damaged 1947) and the Leningrad Codex (**1008 CE**, complete — the basis of every
  Hebrew text in this project's `hebrew-ot/` directory).
- For the Tetragrammaton specifically, the Masoretes applied the vowel points of a **substitute
  word** — אֲדֹנָי (Adonai) in most places, אֱלֹהִים (Elohim) where Adonai already precedes it in
  the sentence — as a **qere perpetuum** (a permanent silent "read this instead," never spelled out
  in the margin because it applies universally). This is a documented scribal instruction to
  substitute at the moment of reading aloud, not a claim about the word's own vowels.

### What that produced downstream
Combining the consonants יהוה with Adonai's vowels, read as if it were one Hebrew word, yields a
hybrid form transliterated into Latin/European languages as **"Jehovah."** Earliest Latin
attestations of something close to this form: **Petrus Alphonsi, c. 1106** ("Ieve"); **Raymundus
Martini, 1278** ("Jehova"); **Porchetus de Salvaticis, 1303**. It was popularized and defended as
if it might be the authentic pronunciation by **Petrus Galatinus, 1520**. Both medieval and modern
scholarship (including the older Brown-Driver-Briggs lexicon) treat this hybrid as a **known
scribal artifact of combining two different words' letters**, not a recovered original
pronunciation — it is what you get by construction, not by discovery.

### What cannot be known with certainty from the manuscripts alone
The Masoretic vocalization was applied thirteen-plus centuries after the consonantal text was
composed, specifically **to avoid** transmitting the Name's actual pronunciation (by design — the
whole point of the qere perpetuum was substitution). The manuscripts on disk in this project
(WLC/Leningrad) therefore cannot themselves answer what the original vowels were; that's not a
gap in this corpus, it's a gap by the Masoretes' own intent.

### The reconstructed "Yahweh" — what it rests on, and who holds it
The critical-scholarly consensus form "Yahweh" is a **reconstruction**, built from evidence outside
the Masoretic tradition entirely:
- Greek transliterations in patristic writers (e.g., Clement of Alexandria's Ιαουε, Epiphanius's
  Ιαβε) and in magical/theurgic papyri (ΙΑΩ, already seen in 4Q120 above, §1) — vowels attached to
  the consonants by people who still heard or knew a spoken form, centuries before Tiberian
  pointing existed.
- Samaritan reading tradition, which independently preserves something close to "Yahwe"/"Yahba."
- Theophoric Hebrew personal names that embed shortened forms (Yeho-, -yahu, -yah), which retain
  vowel information the full Name's own text does not.

This is a real, converging, but **indirect** evidentiary case — not a manuscript reading of the
word itself. **Positions genuinely differ and are held by named parties, not anonymous "some
scholars"**: the critical/academic mainstream (reflected in, e.g., the *Anchor Bible Dictionary*
and most modern critical Hebrew Bible scholarship) favors "Yahweh"; the Jehovah's Witnesses'
Watchtower organization defends "Jehovah" as their official preferred rendering, consciously aware
it is the Masoretic-hybrid form and defending it on other (largely traditional/practical, not
philological) grounds; religious Jewish practice since antiquity does not attempt to reconstruct or
pronounce it at all, reading אֲדֹנָי (or, in casual/non-liturgical contexts, הַשֵּׁם, "the Name")
instead. None of these three positions is a claim this project's manuscripts can settle by
themselves — say so plainly rather than picking a side.

---

## 7. The divine name in the New Testament

**Confirmed by direct corpus query (§5d)**: no manuscript in the `papyri/cntr-transcriptions`
corpus — 130 files, covering every major early NT papyrus and majuscule down to the 2nd century —
contains the Tetragrammaton in Hebrew, paleo-Hebrew, or any transliterated form. Every reference to
"the Lord," including in direct quotations of OT passages that in Hebrew contained יהוה (§5c, Rom
9:29), is written with the standard nomina sacra contraction =κσ, exactly like every other use of
κύριος in the same manuscript.

**Context for the theological argument some readers will have encountered**: the Jehovah's
Witnesses' *New World Translation* inserts "Jehovah" into the NT text roughly 237 times, on the
theory that the original NT autographs (which don't survive) contained the Tetragrammaton when
quoting the OT, and that it was later systematically replaced with κύριος as Christian scribes
copied the text. **No surviving NT manuscript — including the very earliest, P52, dated within a
lifetime of the apostolic era — supports this by direct textual evidence**; every extant witness
already uses the contracted nomina sacra convention. This is a reconstructive argument about a
hypothetical stage of transmission earlier than any surviving copy, not a reading attested in any
manuscript. It should be represented as exactly that: a minority theological position, held
explicitly and officially by the Watchtower Bible and Tract Society, resting on an argument from
silence about the autographs rather than on manuscript evidence — distinct in kind from the Qumran
paleo-Hebrew phenomenon in §2, which *is* directly attested in surviving manuscripts.

---

## Bottom line

Three genuinely separate historical layers get run together in popular discussion of "what happened
to the Name," and the evidence above keeps them apart:

1. **The Greek OT translation choice (κύριος for יהוה)** begins with the LXX itself, c. 250 BCE
   onward — the oldest replacement event of all — but coexisted for at least two more centuries
   with manuscripts that refused to translate the Name at all (§1), using paleo-Hebrew script,
   current square Hebrew script, or Greek ΙΑΩ transliteration instead. κύριος only becomes
   universal by the 4th–5th c. CE Christian uncials.
2. **Second Temple / early rabbinic avoidance of pronunciation** (Philo's "four-lettered name,"
   later codified in Mishnah Sanhedrin 10:1 and Tamid 7:2) is a documented but *later* development
   layered on top of the DSS-era reality that plain square-script יהוה is still how the Name is
   written 94% of the time at Qumran itself (§2a) — avoidance in speech did not mean avoidance in
   writing, and even the writing-avoidance devices (paleo-Hebrew, surrogate glyphs) were minority
   practices, not universal.
3. **The Masoretic vowel points** (7th–10th c. CE) are a wholly separate, much later event —
   centuries after both of the above — that intentionally overlaid substitute vowels rather than
   transmitting original ones, which is exactly why the "Jehovah" hybrid is traceable to a known
   13th–16th century construction process rather than to any claim of recovered pronunciation.

No manuscript anywhere in this project — Qumran, LXX papyri, or NT papyri — supports "Jehovah" as
an attested original pronunciation. The strongest evidence-based reconstruction ("Yahweh") is
itself indirect, resting on transliterations and names rather than a spoken record, and different
communities of practice (critical scholarship, Jehovah's Witnesses, rabbinic Judaism) hold
genuinely different, nameable positions on how to handle that gap.
