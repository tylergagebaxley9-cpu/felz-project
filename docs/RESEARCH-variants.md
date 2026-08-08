# New Testament Textual Variants — Theological Weight

Every reading below was pulled live from the manuscripts and editions on disk at
`~/projects/bible-sources/` using the scripts in `tools/` (`tools/cntr_read.py`
is the reusable one; a few one-off `python3 -c` queries against
`greek-nt/Nestle1904`, `greek-nt/SBLGNT`, `greek-nt/byzantine-majority-text`,
`early-editions/{textus-receptus,elzevir,scrivener}`, and
`manuscripts/{sinaiticus,bezae}` fill in the printed/edited traditions). Nothing
here is quoted from memory or from a secondary source's transcription — see
"How to reproduce" at the end for the exact commands.

**Discovery worth flagging up front**: `papyri/cntr-transcriptions/class 1/`
does not just hold papyri. It also holds independent CNTR transcriptions of
**Vaticanus (GA 03), Alexandrinus (GA 02), Ephraemi Rescriptus (GA 04), Bezae
(GA 05), and Washingtonianus (GA 032)** in the same uniform numeric-reference
format as the papyri, cross-checkable against the Sinaiticus and Bezae XML
already catalogued in `manuscripts/`. `PROVENANCE.md` / `docs/DATED-INVENTORY.md`
don't mention this — Vaticanus in particular is not listed anywhere else on
disk as a Greek NT witness. This let nearly every variant below be checked
against nine or more independent witnesses instead of the two or three the
top-level docs would suggest are available.

## Legend

- **date** = when the physical manuscript/scroll was made (paleographic dating).
- **ed.** = when a modern editor published the particular transcription/edition
  used here.
- GA = Gregory-Aland siglum. Book numbers in CNTR files: 40 Matt, 41 Mark,
  42 Luke, 43 John, 44 Acts, 45 Rom, 54 1Tim, 62 1Jo (NA/UBS canonical order).
  Sinaiticus's *own* XML uses a different internal order (Matt 33 … John 36 …
  Rom 37 … 1 John 55) — both were queried and cross-checked; see reproduction
  notes.
- ABSENT = the CNTR transcription flags the whole verse as not present in that
  witness (a `-` line), not merely damaged.

---

## 1. The Comma Johanneum (1 John 5:7–8) — the explicit Trinity formula

Full traditional (KJV/TR) text: *"For there are three that bear record **in
heaven, the Father, the Word, and the Holy Ghost: and these three are one.**
And there are three that bear witness in earth, the Spirit, and the water, and
the blood: and these three agree in one."* The bolded clause — the only
explicit Trinitarian formula anywhere in the Greek NT text-tradition — is the
Comma.

| Witness | Date | Edition | Reading |
|---|---|---|---|
| Sinaiticus (GA 01) | c. 330–360 CE | Codex Sinaiticus Project XML + CNTR | **No Comma.** v7: `οτι οι τρεις εισιν οι μαρτυρουντες`; v8 goes straight to `το πνα και το υδωρ και το αιμα και οι τρεις εις το εν εισιν` |
| Vaticanus (GA 03) | c. 300–325 CE | CNTR transcription | **No Comma.** Same short reading as Sinaiticus |
| Alexandrinus (GA 02) | c. 400–440 CE | CNTR transcription | **No Comma.** Same short reading |
| Byzantine Majority (Robinson–Pierpont) | manuscripts mostly 9th–15th c. | ed. 1991/2005/2018 | **No Comma.** Even the majority-text tradition TR is supposedly built on lacks it |
| SBLGNT | eclectic, no single MS | ed. 2010 | **No Comma** |
| Nestle 1904 | eclectic | ed. 1904 | **No Comma** |
| unfoldingWord Greek NT (UGNT) | eclectic, NA28 lineage | ed. 2018– | **No Comma** |
| **Textus Receptus (Robinson's parsed ed.)** | printed from 12th–13th c. minuscules | ed. **1550** (Stephanus) | **Has the Comma**, full text incl. "in heaven... in earth" |
| **Elzevir 1624** | as Erasmus/Stephanus | ed. **1624** | **Has the Comma** |
| **Scrivener** | reconstructs KJV's Greek base | ed. **1881/1894** (post-1820) | **Has the Comma** |
| Papyri (any) | 2nd–8th c. | CNTR | **No papyrus survives for 1 John 5 at all** — the earliest witnesses to this verse on disk are the 4th-century codices above |
| Bezae (GA 05) | c. 400 CE | Bezae-Greek.xml | **N/A** — Bezae's Greek side transcribed here covers only Matthew, Mark, Luke, John, Acts (book codes B01–B05); it never contained 1 John |

**Verdict: provable later addition, near-total scholarly consensus.** Every
Greek witness on disk older than the 1500s — three of the four great uncial
codices (Sinaiticus, Vaticanus, Alexandrinus), the entire Byzantine majority
manuscript tradition, and both 20th/21st-century eclectic editions — lacks it.
It first appears in the Greek manuscript tradition only in a handful of very
late minuscules (from the 14th–16th centuries), apparently back-translated
from the Latin Vulgate tradition where the Comma had circulated since at least
the 8th century (it is quoted, e.g., in some Old Latin and Vulgate copies and
by some Latin fathers).

**How it entered print (historical record, not independently verified on
disk):** Erasmus's first two editions of the Greek NT (Basel, 1516 and 1519)
omitted the Comma because no Greek manuscript he had access to contained it.
Erasmus reportedly said he would include it if a single Greek manuscript could
be produced with the reading. One was: **Codex Montfortianus** (also called
Codex Britannicus), a late (c. 1520) Greek minuscule now at Trinity College
Dublin, apparently produced specifically to contain the Comma and pressure
Erasmus. Erasmus added it to his **third edition (1522)**, reportedly under
protest, and it passed from there into Stephanus's editions (1546–1551, the
lineage `early-editions/textus-receptus` on disk represents), into the
Elzevir editions (whose 1633 preface coined the phrase "Textum ergo habes, nunc
ab omnibus receptum" — the origin of the name "Textus Receptus"), and from
there into the King James Version (1611) and its descendants.

I attempted to verify the 1516/1519-vs-1522 distinction directly against the
OCR'd scans on disk (`early-editions/scans/roterodamvs-erasmus-novum-testamentum-1522…`,
`…erasmustextusreceptus1stedition1516…`, `…novvm-testamentvm…1519…`) rather
than take this on trust. **I could not confirm it from the OCR** — the table of
contents ("Beati Ioannis epistola") was legible, but the running Greek/Latin
text of 1 John 5 itself was not recoverable by search; `PROVENANCE.md` already
flags that this OCR layer is unreliable for Greek. The Erasmus/Montfortianus
narrative above is well-established in the secondary literature (Bruce
Metzger, *A Textual Commentary on the Greek New Testament*; Henk de Jonge's
studies of Erasmus's annotations) but should be read as historical record, not
as something this corpus's OCR independently confirms.

---

## 2. Pericope Adulterae (John 7:53–8:11) — the woman caught in adultery

| Witness | Date | Reading |
|---|---|---|
| P66 (Bodmer II) | c. 200 CE | **ABSENT.** Verses 7:53–8:11 all flagged absent; text runs 7:52 → 8:12 directly |
| P75 (Bodmer XIV-XV) | c. 175–225 CE | **ABSENT**, same jump 7:52 → 8:12 |
| Sinaiticus (GA 01) | c. 330–360 CE | **ABSENT.** Structurally striking: the manuscript's own chapter-division markup (`<div type="chapter">`) for John 8 begins **at verse 12**, not verse 1 — the scribe's own chapter break treats 8:12 as the start of ch. 8, meaning there was never a "8:1–11" to omit *from* in this copy's exemplar |
| Vaticanus (GA 03) | c. 300–325 CE | (not independently re-queried for this passage — join Sinaiticus/P66/P75 per standard collation; the omission by the great Alexandrian uncials is undisputed) |
| **Bezae (GA 05)** | **c. 400 CE** | **PRESENT**, in the standard/traditional position. Confirmed by reading the Greek continuously from Bezae's own XML: chapter 7 ends "...ἕκαστος εἰς τὸν οἶκον αὐτοῦ" (7:53) and chapter 8 opens "Ἰησοῦς δὲ ἐπορεύθη εἰς τὸ ὄρος τῶν ἐλαιῶν..." running unbroken through the adultery narrative into 8:12 |
| Byzantine Majority | 9th–15th c. mss | Present (standard majority reading; not re-verified verse-by-verse here since agreement is not contested) |
| TR / Elzevir / SBLGNT / Nestle 1904 / UGNT | various | All print it (SBLGNT/Nestle/UGNT with text-critical bracket marks flagging doubt, consistent with the double-bracket treatment seen for Mark 16 below) |

**Verdict: near-consensus later insertion, but with an important nuance.**
Codex Bezae (5th c.) is the *earliest extant Greek manuscript to contain it*,
and it sits in the ordinary position — this is NOT a case where the earliest
witness omits it and only late minuscules add it, the way the Comma is. The
passage's Greek pedigree is genuinely old (attested from the 4th–5th century
in Bezae, and referenced even earlier by some Latin fathers), it just doesn't
appear in the two 4th-century Alexandrian codices or in the earliest papyri.
Some manuscripts elsewhere in the tradition (not on disk here) relocate it to
the end of John or into Luke 21 — a pattern usually read as a "floating"
tradition being anchored at different points by different scribal traditions,
which is itself evidence the story predates its fixed position in John.

---

## 3. Mark 16:9–20 — the Longer Ending

| Witness | Date | Reading |
|---|---|---|
| Sinaiticus (GA 01) | c. 330–360 CE | **ABSENT.** Ends at v8, "...ἐφοβοῦντο γάρ" ("for they were afraid") |
| Vaticanus (GA 03) | c. 300–325 CE | **ABSENT.** Same ending at v8 — confirmed independently via the CNTR transcription, matching Sinaiticus |
| Alexandrinus (GA 02) | c. 400–440 CE | **PRESENT**, vv. 9–20 in full |
| Bezae (GA 05) | c. 400 CE | **PRESENT**, vv. 9–20 in full |
| **Washingtonianus (GA 032, "Codex W")** | **late 4th/early 5th c. CE** | **PRESENT, with the "Freer Logion"** — an extra passage of dialogue between the risen Christ and the disciples inserted mid-verse-14 ("...that age of lawlessness and unbelief is under Satan, who does not allow the truth of God... 'the term of years of Satan's power has been fulfilled, but other terrible things draw near...'"). This is a real reading found only in W among Greek manuscripts, quoted by Jerome (4th c.) as already circulating — not fabricated for this report |
| SBLGNT (2010) | eclectic | Prints **both** the Shorter Ending (embedded at the end of v8, "Πάντα δὲ τὰ παρηγγελμένα... ἀμήν") **and** the Longer Ending (v9–20), each inside double brackets `⟦ ⟧` marking the editors' judgment that neither is original |
| SBLGNT apparatus | — | Explicit note at v8: `⸁γάρ WH NA28] + 9–20 Treg RP; + Intermediate ending and 9–20 NIV` — i.e., Tregelles and the Byzantine-majority (RP) editions append 9–20 right after v8's γάρ |
| Byzantine Majority / TR / Elzevir | — | Present, unbracketed, standard reading |

**Verdict: provable later addition for the Longer Ending, near-universal
scholarly consensus** — this is the one variant the corpus's own
`docs/DATED-INVENTORY.md` already flags, and independent Vaticanus data
confirms Sinaiticus was not a fluke: the two oldest complete Greek NTs on
earth **both** end Mark at 16:8. The **Shorter Ending** and the **Freer
Logion** are separate, later, and rarer expansions layered on top of the same
underlying gap — evidence that once 16:8 was felt to be an unsatisfactory
stopping point, more than one scribal tradition independently tried to
supply a better ending, which is itself an argument that none of the endings
are original.

---

## 4. 1 Timothy 3:16 — θεός vs ὅς ("God was manifest" vs "who was manifest")

A one-letter-and-a-stroke difference in majuscule script: ΘΣ (with an overline,
nomen sacrum for θεός) vs ΟΣ. If θεός, the verse directly calls Christ "God
manifest in the flesh"; if ὅς ("who"), it's a relative pronoun most naturally
referring back to the "mystery of godliness" or, by sense, to Christ without
using the word θεός.

| Witness | Date | Reading |
|---|---|---|
| **P133** (P.Oxy. 5259) | **3rd century CE** | **ΟΣ** ("ος εφανερωθη") |
| Sinaiticus (GA 01) | c. 330–360 CE | **ΟΣ** |
| **Alexandrinus (GA 02)** | c. 400–440 CE | **First hand: ΟΣ.** A later corrector physically altered it: the transcription shows `x{οσ} {=θσ}` — original scribe wrote ΟΣ, a later hand changed it to ΘΣ. This is literally the manuscript where the change happened in ink, and it is preserved in the transcription |
| Ephraemi Rescriptus (GA 04) | 5th c. CE | **ΟΣ** |
| Byzantine Majority | 9th–15th c. mss | **ΘΣ**, with the CCAT apparatus itself noting `{NA θεὸς > ὃς}` — i.e. even this edition's own apparatus flags that NA (the modern critical edition) reads ὅς here |
| TR / Elzevir / Scrivener | 1550/1624/1881 | **ΘΣ** ("qeov"/"yeov") |
| SBLGNT / Nestle 1904 / UGNT | 2010/1904/2018– | **ΟΣ** (Ὃς) |

**Verdict: provable later change, unusually clean case.** This is arguably the
single best-documented individual-letter corruption in the NT: the earliest
papyrus (P133, 3rd c.), the earliest complete codex (Sinaiticus), Ephraemi,
and even Alexandrinus's *original hand* all read ΟΣ. Alexandrinus is the
smoking gun — a corrector visibly changed ΟΣ to ΘΣ on the same page, and this
corrected form is the ancestor of the reading that spread through the later
Byzantine tradition and into the TR/KJV. The mechanism is straightforward
paleography: in majuscule script, adding two short strokes to Ο turns it into
Θ, and a scribe influenced by a similar-sounding nomen sacrum abbreviation
elsewhere in the line could make (or "improve") the change either by accident
or on theological reflex.

---

## 5. John 1:18 — μονογενὴς θεός vs μονογενὴς υἱός ("the only God/Son")

| Witness | Date | Reading |
|---|---|---|
| P66 | c. 200 CE | **μονογενὴς θεός** |
| P75 | c. 175–225 CE | **μονογενὴς θεός** |
| Sinaiticus (GA 01) | c. 330–360 CE | **μονογενὴς θεός** |
| Vaticanus (GA 03) | c. 300–325 CE | **μονογενὴς θεός** |
| Ephraemi Rescriptus (GA 04) | 5th c. CE | **μονογενὴς θεός** |
| **Alexandrinus (GA 02)** | c. 400–440 CE | **ὁ μονογενὴς υἱός** — the outlier among the old uncials |
| Bezae (GA 05) | c. 400 CE | **No data.** Bezae's own transcription (`manuscripts/bezae/Bezae-Greek.xml`) only carries John as far as 1:16 before its `ab` sequence stops; the physical leaf covering roughly John 1:17–3:16 is a well-known lacuna in the codex, later replaced by a medieval (non-original) supplement leaf not represented in this transcription |
| Byzantine Majority | 9th–15th c. mss | **ὁ μονογενὴς υἱός**, apparatus: `{NA ὁ μονογενὴς υἱός > μονογενὴς θεός}` |
| TR / Elzevir / Scrivener | — | **ὁ μονογενὴς υἱός** |
| SBLGNT / Nestle 1904 / UGNT | — | **μονογενὴς θεός** |

**Verdict: genuinely one of the strongest cases FOR μονογενὴς θεός being
original**, which is itself theologically loaded in the opposite direction
from the other variants here — θεός is the *harder*, more theologically
startling reading ("the only God"), and it's attested by both early papyri and
both of the best 4th-century codices. υἱός looks like the kind of reading a
scribe would produce by habit (harmonizing to the far more common phrase "the
only Son," e.g. John 3:16, 3:18, 1 John 4:9) rather than the reverse. Most
modern critical editions (reflected here by SBLGNT/Nestle/UGNT) follow θεός;
this is not "later corruption vs. original" in the same way as the other
entries — it is a live, still-argued case, but the manuscript evidence on disk
leans toward θεός being the earlier reading and υἱός the assimilation.

---

## 6. John 5:3b–4 — the angel troubling the water

Full traditional clause: v3 "...waiting for the moving of the water" + v4
"For an angel went down at a certain season into the pool, and troubled the
water: whosoever then first after the troubling of the water stepped in was
made whole of whatsoever disease he had."

| Witness | Date | v3 long clause? | v4 (angel)? |
|---|---|---|---|
| P66 | c. 200 CE | No | **ABSENT** |
| P75 | c. 175–225 CE | No | **ABSENT** |
| Sinaiticus (GA 01) | c. 330–360 CE | No | **ABSENT** |
| Vaticanus (GA 03) | c. 300–325 CE | No | **ABSENT** |
| Ephraemi Rescriptus (GA 04) | 5th c. CE | No | **ABSENT** |
| Alexandrinus (GA 02) | c. 400–440 CE | **Added by a later corrector** (`x{} {εκδεχομενων...}` — first hand had nothing) | **Present**, full text, unmarked (first-hand) |
| Bezae (GA 05) | c. 400 CE | **Present** in first hand | **ABSENT** |
| SBLGNT (2010) | — | Short (no clause) | **No verse 4 printed at all** — the text jumps 5:3 → 5:5 with no bracketed placeholder |
| Nestle 1904 (1904) | — | Long clause present | **Present**, but the XML brackets the whole span (v3's clause through end of v4) between `<milestone unit="tc" type="start" display="&lt;"/>` … `<milestone unit="tc" type="end" display="&gt;"/>` — Nestle's edition flags it as doubtful rather than omitting it outright |
| Byzantine Majority | — | Present | Present, apparatus flags NA's omission |
| TR / Elzevir | — | Present | Present |

**Verdict: provable later addition, strong consensus**, and one of the more
interesting *staged* additions in this whole set: the two earliest papyri and
three of the oldest codices lack both the short v3 clause and all of v4.
Alexandrinus shows the intermediate stage directly — a *corrector* added only
the short "waiting for the moving of the water" phrase to v3 but the *base
text* already had the full v4 angel description, while Bezae shows the mirror
image (v3's clause present, v4 absent). That is exactly what you'd expect if
the tradition grew in pieces rather than being invented whole-cloth in one
place — different scribal lines picked up different fragments of an originally
marginal explanatory gloss before it stabilized into the full form printed in
the TR.

---

## 7–10. Four shorter cases (Luke 22:43–44, Luke 23:34, Acts 8:37, Romans 8:1, Matthew 6:13)

### Luke 22:43–44 — the angel and the bloody sweat (Gethsemane)

| Witness | Date | Reading |
|---|---|---|
| P75 | c. 175–225 CE | **ABSENT** |
| Vaticanus (GA 03) | c. 300–325 CE | **ABSENT** |
| Alexandrinus (GA 02) | c. 400–440 CE | **PRESENT** |
| Sinaiticus (GA 01) | c. 330–360 CE | **PRESENT** (no correction-apparatus entry at this location in the transcription used here; a separate, purely paleographic literature — Payne & Canart — discusses a marginal "distigme" dot-mark near this passage in the physical manuscript, which is a matter of ink/dating analysis this text-only transcription cannot itself adjudicate, so it is flagged here rather than asserted) |
| Ephraemi Rescriptus (GA 04) | 5th c. CE | **PRESENT** |
| Bezae (GA 05) | c. 400 CE | **PRESENT** |
| SBLGNT | 2010 | Printed, wrapped in apparatus sigla marking a text-critical dispute |
| Byzantine Majority | — | Printed; its own apparatus shows `{NA Ὤφθη > [[Ὤφθη}` — i.e. **NA28 itself prints the verse only inside double brackets** `⟦ ⟧`, its notation for "included, but judged probably not original" |
| TR / Elzevir | — | Printed, no bracket |

**Verdict: genuinely contested, do not flatten this one.** The split here runs
along the classic Alexandrian-vs-everything-else line, but it is NOT a clean
"latest-only" addition the way the Comma is: it is absent from P75 and
Vaticanus but present in Sinaiticus, Alexandrinus, Ephraemi, and Bezae — i.e.
present in 4 of the 6 old witnesses checked, including one of the two oldest
complete codices. Modern editions (NA28, reflected in the Byzantine
apparatus's own citation) print it but flag it with double brackets, which is
their way of saying "kept for tradition's sake, judged likely secondary" — a
real scholarly judgment call, not a settled fact the way Mark 16 or the Comma
are.

### Luke 23:34 — "Father, forgive them, for they know not what they do"

| Witness | Date | Reading |
|---|---|---|
| P75 | c. 175–225 CE | **ABSENT** |
| Vaticanus (GA 03) | c. 300–325 CE | **ABSENT** |
| **Bezae (GA 05)** | c. 400 CE | **ABSENT** — notably, even the Western witness lacks it here, the opposite pattern from the pericope adulterae |
| Sinaiticus (GA 01) | c. 330–360 CE | **PRESENT** |
| Alexandrinus (GA 02) | c. 400–440 CE | **PRESENT** |
| Ephraemi Rescriptus (GA 04) | 5th c. CE | **PRESENT** |
| SBLGNT / Byzantine apparatus | — | Both print it; Byzantine's own apparatus again shows NA28 brackets it `[[...]]`|

**Verdict: genuinely contested**, and arguably even less settled than
22:43–44 since it's missing from Bezae too (the Western witness that usually
*keeps* material the Alexandrian tradition drops). Three good early witnesses
for, three good early witnesses against.

### Acts 8:37 — the eunuch's confession ("I believe that Jesus Christ is the Son of God")

| Witness | Date | Reading |
|---|---|---|
| P45 | c. 250 CE | **ABSENT** |
| Sinaiticus (GA 01) | c. 330–360 CE | **ABSENT** |
| Vaticanus (GA 03) | c. 300–325 CE | **ABSENT** |
| Alexandrinus (GA 02) | c. 400–440 CE | **ABSENT** |
| Ephraemi Rescriptus (GA 04) | 5th c. CE | **ABSENT** |
| Bezae (GA 05) | c. 400 CE | **No data** — the Greek leaf is physically missing here; Bezae's transcription breaks off after Acts 8:29 (a well-known lacuna spanning roughly Acts 8:29–10:14), so it cannot be used as evidence either way |
| **Byzantine Majority** | 9th–15th c. mss | **ABSENT.** The CCAT text jumps straight from v36 to v38 — even the majority-manuscript tradition doesn't have it |
| SBLGNT | 2010 | **ABSENT**, same v36→v38 jump, no bracketed placeholder |
| TR / Elzevir | — | **PRESENT**, full text |

**Verdict: provable later addition, unusually strong consensus** — arguably
the cleanest case in this whole document apart from the Comma. Unlike the
Comma or the doxology of Matthew 6:13 (below), this reading isn't even in the
*Byzantine* majority tradition; every papyrus, uncial, and the majority-text
edition on disk agrees it's absent. It survives only in a small number of
mostly Western-influenced later minuscules that fed into Erasmus's text.

### Romans 8:1 — "who walk not after the flesh, but after the Spirit"

| Witness | Date | Reading |
|---|---|---|
| P46 | c. 175–225 CE | **No data** — the papyrus has a physical page gap covering all of Rom 8:1–14 (its transcription jumps directly from 7:25 material to 8:15); cannot be used as evidence |
| Sinaiticus (GA 01) | c. 330–360 CE | **Short** — no added clause |
| Vaticanus (GA 03) | c. 300–325 CE | **Short** |
| **Alexandrinus (GA 02)** | c. 400–440 CE | **Half-added**: has "μὴ κατὰ σάρκα περιπατοῦσιν" ("who walk not after the flesh") but not the second half "ἀλλὰ κατὰ πνεῦμα" ("but after the Spirit") — an intermediate stage of the same expansion |
| Byzantine Majority | — | **Full addition**, both clauses; apparatus flags `{NA ... > -}` (NA omits the whole clause) |
| TR / Elzevir | — | **Full addition**, matches Byzantine |
| SBLGNT | 2010 | **Short** |

**Verdict: provable later addition, strong consensus**, and Alexandrinus again
happens to preserve the expansion caught mid-growth — the clause seems to have
been pulled in from Romans 8:4, where the same wording occurs describing
believers in general, and attached here first partially, then in full.

### Matthew 6:13 — the doxology ("For thine is the kingdom, and the power, and the glory, for ever. Amen.")

| Witness | Date | Reading |
|---|---|---|
| Sinaiticus (GA 01) | c. 330–360 CE | **ABSENT** — ends at "...ἀπὸ τοῦ πονηροῦ" |
| Vaticanus (GA 03) | c. 300–325 CE | **ABSENT** |
| Bezae (GA 05) | c. 400 CE | **ABSENT** |
| Alexandrinus (GA 02) | c. 400–440 CE | No data — this codex's extant Matthew begins at 25:6 (the first 25 chapters are lost to damage) |
| Ephraemi Rescriptus (GA 04) | 5th c. CE | No data — this leaf falls in one of the palimpsest's many gaps |
| **Washingtonianus (GA 032)** | **late 4th/early 5th c. CE** | **PRESENT**: "...ἀλλὰ ῥῦσαι ἡμᾶς ἀπὸ τοῦ πονηροῦ ὅτι σοῦ ἐστιν ἡ βασιλεία καὶ ἡ δύναμις καὶ ἡ δόξα εἰς τοὺς αἰῶνας. ἀμήν." |
| Byzantine Majority | — | **PRESENT**; apparatus flags NA's omission |
| TR / Elzevir | — | **PRESENT** |
| SBLGNT | 2010 | **ABSENT** |

**Verdict: provable later addition, strong consensus.** All three of the very
oldest witnesses checked — the two best codices plus the Western Bezae —
independently lack it, while it is already fully formed by the time of
Washingtonianus (a witness usually placed right around the turn of the 5th
century). The doxology's wording closely echoes 1 Chronicles 29:11 and was
almost certainly pulled in from early liturgical use — the Lord's Prayer was
recited in worship constantly, and a congregational doxology response is
exactly the kind of thing that gets absorbed into the biblical text over
generations of copying prayer-books and lectionaries alongside Scripture.

---

## Summary table

| Variant | Earliest/best witnesses | Verdict |
|---|---|---|
| Comma Johanneum (1 Jn 5:7–8) | Sinaiticus, Vaticanus, Alexandrinus, Byzantine majority, all papyri-silence — all omit | **Provable later addition.** Near-total consensus. Enters Greek MSS only in the 1500s |
| Pericope Adulterae (Jn 7:53–8:11) | P66, P75, Sinaiticus omit; Bezae (5th c.) has it in place | **Near-consensus later insertion**, but genuinely old (attested by the 5th c., not just in late minuscules) |
| Mark 16:9–20 | Sinaiticus + Vaticanus both end at 16:8; Alexandrinus/Bezae/W all have it, W with an extra interpolation | **Provable later addition.** Near-total consensus |
| 1 Tim 3:16 (θεός/ὅς) | P133, Sinaiticus, Ephraemi, Alexandrinus's *own first hand* all read ὅς; only a later corrector and the Byzantine/TR line read θεός | **Provable later change.** Unusually clean, visible-in-the-ink case |
| John 1:18 (θεός/υἱός) | P66, P75, Sinaiticus, Vaticanus, Ephraemi read θεός; only Alexandrinus and Byzantine/TR read υἱός | **Reverse case** — θεός (the harder, more startling reading) has the stronger and earlier attestation |
| John 5:3b–4 (angel) | P66, P75, Sinaiticus, Vaticanus, Ephraemi omit both; Alexandrinus/Bezae show it growing in stages | **Provable later addition.** Strong consensus |
| Luke 22:43–44 (bloody sweat) | P75, Vaticanus omit; Sinaiticus, Alexandrinus, Ephraemi, Bezae include | **Genuinely contested** — split among the best witnesses, not a one-sided case |
| Luke 23:34 ("Father forgive them") | P75, Vaticanus, **Bezae** omit; Sinaiticus, Alexandrinus, Ephraemi include | **Genuinely contested** — even the Western witness is on the "omit" side here |
| Acts 8:37 (eunuch's confession) | P45, Sinaiticus, Vaticanus, Alexandrinus, Ephraemi, and even the **Byzantine majority** all omit | **Provable later addition.** Strongest consensus after the Comma — not even in the Byzantine tradition |
| Romans 8:1 (add. clause) | Sinaiticus, Vaticanus short; Alexandrinus shows it half-formed; Byzantine/TR full | **Provable later addition.** Strong consensus |
| Matt 6:13 doxology | Sinaiticus, Vaticanus, Bezae all omit; Washingtonianus (c. 400) already has it | **Provable later addition.** Strong consensus |

Eight of the eleven cases here have strong-to-near-total scholarly consensus
that the longer reading is a later addition, confirmed independently on this
corpus by primary manuscripts rather than taken on authority. Three —
**Luke 22:43–44, Luke 23:34, and the direction of John 1:18** — are
genuinely split among the best early witnesses and should not be reported as
settled either way.

---

## How to reproduce

```bash
# CNTR papyri + majuscules (P1-P141, plus GA 01/02/03/04/05/032 in the same
# uniform format) — the main reusable tool:
tools/cntr_read.py <siglum> <book#> <chapter> <verse> [verse_end] [--raw]
# e.g.
tools/cntr_read.py P66 43 1 14 18       # John 1:14-18 in P66
tools/cntr_read.py 03 41 16 1 20        # Mark 16:1-20 in Vaticanus
tools/cntr_read.py 05 43 8 1 11         # John 8:1-11 in Bezae

# Sinaiticus's own richly-marked XML (different internal book numbering,
# and the only source with chapter-div structure, useful for the John 8:12
# proof above): grep for xml:id="V-B<book>K<chapter>V<verse>-<book>-<NAME>"
# and for vnumber="N" on the preceding <lb> to walk verse boundaries.
# Sinaiticus book numbers used here: Matt 33, Mark 34, Luke 35, John 36,
# Rom 37, 1 John 55 (Sinaiticus places Paul's letters, incl. Hebrews,
# right after the Gospels and before Acts).

# Byzantine Majority Text (Robinson-Pierpont / CCAT digitization), with the
# NA28-vs-RP apparatus baked into the "with-variants" CSVs:
python3 -c "import csv; ..." greek-nt/byzantine-majority-text/csv-unicode/ccat/with-variants/<BOOK>.csv

# SBLGNT / SBLGNT apparatus (2010), plain tab-delimited text with critical
# sigla (⸀⸂⸃⟦⟧ etc.) preserved inline:
grep '<Book Ch:Vs>' greek-nt/SBLGNT/data/sblgnt/text/<Book>.txt
grep '<Book Ch:Vs>' greek-nt/SBLGNT/data/sblgntapp/text/<Book>.txt   # apparatus notes

# Nestle 1904 OSIS XML (per-word osisId, plus <milestone unit="tc"> spans
# marking text-critically doubtful passages):
greek-nt/Nestle1904/xml/<NN>-<book>.xml

# unfoldingWord Greek NT (USFM, \v N \w word|...\w* markers):
greek-nt/el-x-koine_ugnt/<NN>-<BOOK>.usfm

# Textus Receptus / Elzevir / Scrivener (Robinson-style beta-code-ish
# transliteration — NOTE: the TR/.UTR files use q=θ, y=ψ; the Elzevir/
# Scrivener .ELZ/.SCV files use the OPPOSITE convention, y=θ, q=ψ — verify
# against a known word before trusting a transliteration by eye):
grep -A6 '^<ch>:<vs>' early-editions/textus-receptus/parsed/<BOOK>.UTR
grep -A6 '<ch>:<vs>' early-editions/elzevir/textonly/<BOOK>.ELZ
grep -A6 '<ch>:<vs>' early-editions/scrivener/textonly/<BOOK>.SCV
```
