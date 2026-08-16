> [!important] ✅ AUDIT CLOSED 2026-08-16 — this file passed
> An earlier header on this file claimed **69 Ge'ez forms occur nowhere in the corpus**, implying possible fabrication. **That alarm was mostly my own broken checker and is retracted.**
>
> The checker's comparison pool omitted the **OCP apparatus** (it used only the base Ge'ez JSON), so every legitimate quotation of a manuscript variant registered as an unknown form. With the apparatus included the count falls **68 → 16**. Adjudicated against **Dillmann's *Lexicon Linguae Aethiopicae* (1865)**, now in `lexicon/`, **10 more are attested**, leaving **6**.
>
> **The 6 remaining:** `መየጠ` · `ሥርዓ` · `ረቢዕ` · `ሰጠመ` · `ስብዓት` · `ደኀነ` — all plausible Ge'ez lemma forms, against a 19th-century scan whose Ge'ez OCR is imperfect. Not evidence of fabrication; flagged for a human eye, not withheld.
>
> **What was checked and passed:** no Charles-1917 signature English anywhere · reconstruction marked · multi-sense `( | )` used · ABSENT recorded · Ge'ez fidelity now within noise of the hand-verified `enoch-6.md`.
>
> 🛑 **Standing method note:** three separate times this session a matcher, not the data, was the thing that was wrong — an accent-blind Greek grep, then an apparatus-blind pool, twice. **Prove the matcher against known-good input before its verdict on unknown input means anything.**

# 1 Enoch 4–5 — The Heat of Summer, and the Turn to Judgment

**Translated from the Ge'ez, against the Greek, Qumran Aramaic and Latin witnesses. No English translation consulted.**

Built with `tools/enoch.py`, which drops the Charles-1917 `translation` field bundled in the Ge'ez JSON at parse time, with no flag to re-enable it. See PROVENANCE.md. Companion to `translations/enoch-6.md`; the provenance argument there is not repeated in full here.

---

## 🛑 Provenance chain — read before the text

```
Aramaic (lost, ~7% survives at Qumran)
   └─> Greek (lost, ~44% survives)
          └─> Ge'ez  ← the only complete witness, from late manuscripts
```

⭐ **Chapters 4–5 sit inside the 7%.** Both are attested in Aramaic — 4:1 in *two* scrolls (4Q201 **and** 4Q204), which is rarer still. This is one of the very few places in the book where a Ge'ez reading can be checked against two independent Aramaic copies.

⚠️ **The Greek is absent for the whole of chapter 4** in this apparatus, and resumes *mid-clause* at 5:1 (`πῶς τὰ φύλλα χλωρά …`, with no governing imperative). Measured: the Gizeh text in the OCP apparatus runs continuously through 2:3, gives a single fragment at 3:1 flanked by ellipses (`. . . καταμάθετε καὶ ἴδετε πάντα τὰ δένδρα . . .`), gives **nothing** at 4:1, and picks up again at 5:1 without a finite verb of command. **I cannot determine from this dataset** whether the Akhmim codex physically lacks 4:1 or whether the edition simply does not record it there. Stated, not smoothed.

⚠️ **Latin is ABSENT for both chapters.** The Latin version exists in this corpus only at 1:9, 99:6–7 and 106:1–3.

⚠️ These semantic ranges are **not validator-gated** — `ranges/*.json` and `verify_ranges.py` are Hebrew-only. Same limitation as `enoch-6.md` and `revelation-3.md`.

### Witnesses cited here

| Siglum | Language | What it is |
|---|---|---|
| `p` | Ethiopic | John Rylands Library Ethiopic 23 (Knibb) |
| `Bertalotto` | Ethiopic | declared as an `<ms>` in the apparatus, but in substance an **edited/orthographically corrected transcription of `p`** — see the warning below |
| `4Q201` | Aramaic | Qumran Cave 4, Enoch<sup>a</sup> — attests 4:1, 5:1, 5:2, 5:4, 5:5, 5:6 |
| `4Q202` | Aramaic | Qumran Cave 4, Enoch<sup>b</sup> — attests 5:9 only, and only two letters of it |
| `4Q204` | Aramaic | Qumran Cave 4, Enoch<sup>c</sup> — attests 4:1 and 5:1 |
| `Gizeh` | Greek | Codex Panopolitanus (Akhmim) — 5:1–9 only |
| — | Latin | **ABSENT throughout chapters 4–5** |
| — | Greek `Syncellus` | **ABSENT throughout chapters 4–5** (his excerpts begin at ch. 6) |

🛑 **Flagged as conjecture by the tool and not treated as evidence anywhere below:** `Black` (5:5 ×2), `Dillman Lods Charles Black` (5:5), `Swete Charles Black` (5:6), `F-R` (5:6). Two of the most quotable phrases in chapter 5 rest on these. See §3.

> [!warning] `Bertalotto` is not an independent manuscript
> The apparatus declares `Bertalotto` under `<ms>` alongside `4Q201` and `Gizeh`, with nothing marking the difference. In chapters 4–5 every `p` / `Bertalotto` split but one is a **laryngeal or labiovelar orthography** difference (ዓ/ዐ, ሐ/ሀ, ኃጥአን/ኃጥኣን) — i.e. Bertalotto normalising `p`. The single exception is **5:8** (`ወኣምሂ` vs `ወአሜሃ`), and there Bertalotto is *correcting* `p`, not witnessing against it. **Do not count Bertalotto as a second Ethiopic voice.** Wherever a claim below would need two Ethiopic witnesses, it has only one.

### Reading the Aramaic

- **Brackets `[ ]` are EDITORIAL RECONSTRUCTION, not surviving ink.** In `[‏…ולמ]דׄרךׄ`, only `דרך` is on the parchment.
- The supralinear **dot** (U+05C4) and **circle** (U+05AF) mark letters where *ink is present but the reading is uncertain*. They are categorically different from brackets. I have not been able to determine from this dataset which of the two marks the edition uses for "probable" and which for "possible", so below I treat both alike as **ink, reading uncertain**.

---

## ⭐⭐⭐ FINDING 1 — The promise to the elect: Greek says it three times, Ge'ez once

This is the finding of chapter 5, and it is the place where smoothing would do the most damage.

**Measured, accent-blind (NFD, combining marks stripped), over the Gizeh text of ch. 5:**

| Greek phrase | 5:6 | 5:7 | 5:8 | total |
|---|---|---|---|---|
| `κληρονομήσουσιν τὴν γῆν` — *they shall inherit the earth* | 1 | 1 | 1 | **3** |
| `φῶς` — *light* | 1 | 1 | 2 | **4** |
| `χάρις` — *grace/favour* | 0 | 1 | 1 | **2** |
| `σωτηρία` — *salvation* | 2 | 0 | 0 | **2** |

**Ge'ez, same three verses:** `ይወርስዋ፡ ለምድር` (*inherit the earth*) — **once**, at 5:7. `ብርሃን` (*light*) — **once**, at 5:7.

🛑 **The Ge'ez of chapter 5 contains no word for salvation and no word for forgiveness of sins.** Verified by extracting the complete word-list of the Ge'ez chapter (119 distinct forms): no form of the ደኀነ (*save, deliver*) root, no form of the ሠረየ (*forgive, remit*) root occurs. The Greek 5:6 has both — `λύσις ἁμαρτιῶν` (*release/loosing of sins*) and `σωτηρία` twice.

So the Greek 5:6 carries an entire ~50-word block of promise-and-doom that the Ge'ez 5:6 does not have in any form:

> `καὶ ἔσται αὐτοῖς λύσις ἁμαρτιῶν καὶ πᾶν ἔλεος καὶ εἰρήνη καὶ ἐπιείκεια, ἔσται αὐτοῖς σωτηρία, φῶς ἀγαθόν, καὶ αὐτοὶ κληρονομήσουσιν τὴν γῆν, καὶ πᾶσιν ὑμῖν τοῖς ἁμαρτωλοῖς οὐχ ὑπάρξει σωτηρία, ἀλλὰ ἐπὶ πάντας ὑμᾶς κατάλυσις, κατάρα.`

⚠️ **Which direction this went cannot be decided from the evidence in this corpus.** The Greek may be expanding a shorter text; the Ge'ez may be contracting a fuller one. The Greek's own triple repetition of the inheritance promise across three consecutive verses — including a near-verbatim restatement of the whole of 5:7 at the head of 5:8 — is at least consistent with internal doublets inside Gizeh itself. **I am not choosing.** Both texts are printed in full below.

What I will say flatly: **a translator working from the Ge'ez and a translator working from the Greek are not translating the same doctrine here.** The Ge'ez promises the elect light, joy, peace, land, wisdom, long life. The Greek promises them, additionally, *forgiveness of sins* and *salvation*, and explicitly denies salvation to the sinners. That is a difference of kind, not of length.

---

## ⭐⭐ FINDING 2 — "You have CHANGED your works" (5:4) — only in the Aramaic

Chapters 2–5 are built on one refrain: the works of heaven, earth and sea **do not change**.

| | 2:1 | 2:2 | 5:2 | 5:3 | **5:4 — the pivot** |
|---|---|---|---|---|---|
| Greek | `οὐκ ἠλλοίωσαν` | `οὐκ ἀλλοιοῦνται` | `οὐκ ἀλλοιοῦνται` | `οὐκ ἀλλοιοῦσιν` | **`οὐκ ἐνεμείνατε`** — *you did not abide* |
| Ge'ez | `ኢይመይጡ` | `ኢይትመየጥ` | `ወኢይትመየጡ` | *(absent)* | **`ኢተዐገሥክሙ`** — *you did not endure* |
| Aramaic | — | — | — | — | **`שניתן עבדׄכן`** — *you have **changed** your works* |

⭐ At the exact hinge of the book's argument, **the Aramaic keeps the verb and both translations drop it.** The accusation in 4Q201 is not "you failed to persevere" — it is the precise inverse of the refrain: *the works of nature do not change; you changed your works.* `שני` is the standard Aramaic verb "to change/alter", and `עבדכן` "your works" answers `τὰ ἔργα` / `ግብር` of the preceding verses.

`שניתן עבדׄכן` is **on the parchment** — `שניתן` fully clear, `עבדכן` with one uncertainty dot on the ד. No brackets. The finding does not rest on reconstruction.

🛑 **Honest limit:** the Aramaic of 5:2–5:3's own "do not change" clauses **does not survive**, so I cannot demonstrate the root-identity *within Aramaic*. What is demonstrable is that the Aramaic accusation uses "change", and that both the Greek and the Ge'ez, which do preserve "change" for nature in 5:2–5:3, switch to a different verb at 5:4. The antithesis is on the surface in Aramaic and merely conceptual in the other two.

> ⚠️ A homograph I am **not** building on: 4Q201's word for "year" at 5:2 is `שׄנה`, the same three consonants as the root of `שניתן` "you have changed". Aramaic has both roots with these letters. Whether any wordplay was felt is **undeterminable**, and I decline to assert one. (Chapter 6's `Ardis`/`Jared` retraction is the standing reason for that caution: shared consonants are not evidence.)

---

## ⭐⭐ FINDING 3 — Two of chapter 5's most quotable phrases are editors' guesses

The tool flags these; they must never be cited as Greek evidence.

### 5:6 — "and all the **sinless** shall rejoice"

| Source | Reading | Status |
|---|---|---|
| **Gizeh (the actual ink)** | `αμαρτοι` | ✅ manuscript — and *as it stands it is not a Greek word*; taken at face value its stem is ἁμαρτ-, "sin" |
| Swete, Charles, Black | `ἀναμάρτητοι` (*sinless*) | 🛑 **conjecture** |
| F-R (Flemming–Radermacher) | `ἀμίαντοι` (*undefiled*) | 🛑 **conjecture** |

🛑 The clause "**and all the sinless shall rejoice**" — the hinge on which the whole Greek salvation block hangs, since it identifies *who* receives the forgiveness and salvation of 5:6 — **has no manuscript reading behind its subject.** Two different editors supply two different words. The manuscript's own letters point, if anything, the other way. **The Ge'ez has no corresponding clause at all**, so there is no independent check.

### 5:5 — "you shall curse your days"

| Source | Reading | Status |
|---|---|---|
| **Gizeh** | `κατηρασασθαι` | ✅ manuscript (unaccented, morphologically incoherent as transmitted) |
| Black | `καταράσεσθε` (*you shall curse*) | 🛑 **conjecture** |
| **Gizeh** | `κατα` | ✅ manuscript |
| Dillman, Lods, Charles, Black | `καὶ τὰ ἔτη` (*and the years*) | 🛑 **conjecture** |

The Greek of 5:5 is transmitted **corrupt at two consecutive points**. Every smooth printed Greek text of this verse is partly editorial. Note that `Charles` appears here as a conjecturer — the same Charles whose English this tool exists to keep out.

---

## ⭐ FINDING 4 — 5:8: "and IF" or "THEN"? A vowel decides whether the promise is conditional

Three Ethiopic forms of the same three-consonant skeleton ʾ‑m‑h open 5:8:

| Source | Form | Sense |
|---|---|---|
| Ge'ez base text | `ወእመሂ` *wäʾəmähi* | **and if / and even if** |
| ms `p` | `ወኣምሂ` *wäʾamhi* | not a normal form; between the other two |
| `Bertalotto` (editorial correction of `p`) | `ወአሜሃ` *wäʾameha* | **then, at that time** |
| Greek Gizeh | `τότε` | **then** |

⭐ **The difference between "*And if* wisdom is given to the elect …" and "*Then* wisdom shall be given to the elect …" is carried entirely by vowel-marking on one consonantal skeleton.** One makes the gift of wisdom a hypothesis; the other makes it an announced fact. The Greek supports "then". The base Ge'ez text as transmitted reads "and if".

⚠️ But `Bertalotto` is not a second manuscript (see the warning above) — it is a corrected reading of `p`. So the Ethiopic evidence for "then" is **one editor agreeing with the Greek**, not a manuscript. Both are printed at 5:8. Neither is preferred.

(`ወአሜሃ` is the same word that opens 6:5, `አሜሃ፡ መሐሉ፡ ኵሎሙ` — "**then** they all swore" — so the sense of the form is fixed elsewhere in the book.)

---

## ⭐ FINDING 5 — 5:1: "for glory and praise" is in Greek AND Aramaic, and missing from the Ge'ez

| Witness | Reading | Status |
|---|---|---|
| Greek Gizeh | `καὶ πᾶς ὁ καρπὸς αὐτῶν εἰς τιμὴν καὶ δόξαν` — *and all their fruit is unto honour and glory* | ✅ |
| Aramaic **4Q204** | `תשבחה` — *praise* | ✅ **full ink, no brackets** |
| Aramaic 4Q201 | `[‏…להד]רׄ תש֯[בחה` — *[for glo]ry, pra[ise]* | ⚠️ heavily reconstructed: only `ר` and `תש` are ink |
| **Ge'ez** | `ወይፈርዩ` — *and they bear fruit*, **full stop** | — |

⭐ Two versions, three manuscripts, one of them with the word clean on the parchment — and **the Ge'ez has no honour, no glory and no praise in 5:1.** The Ge'ez fruit simply grows.

Note the Greek and Aramaic do not agree with each other either: `τιμὴν καὶ δόξαν` (*honour and glory*) is not the same pair as `הדר` + `תשבחה` (*glory/majesty* + *praise*). **All three readings are given below; none is preferred.**

Two further losses in the same verse:
- **`ወአእምሩ` ("and know")** stands in ms `p` but not in the Ge'ez base text. Greek has the pair `διανοήθητε καὶ γνῶτε` (*consider and know*) and then a third verb `νοήσατε`; Aramaic has `[ואת]בוננו` (*[and und]erstand*, with `ואת` reconstructed). **The manuscript preserves a doublet the printed base text has lost.**
- **"his works"** stands in Greek (`τῶν ἔργων αὐτοῦ`) and twice in Aramaic (`עׄבדיה [א]לׄ[ין`, `כׄל֯ עׄב֯ד֯יהׄ אלין` — *all these his works*). The Ge'ez has bare `በእንተ፡ ኵሉ` — *concerning all* — with no noun. Verified: no form of ግብር/ምግባር occurs anywhere in Ge'ez 5:1.

---

## ⭐ FINDING 6 — Two Aramaic scrolls of one verse spell differently (4:1, 5:1)

The Aramaic is not a single text either. Where 4Q201 and 4Q204 overlap:

| | 4Q201 | 4Q204 |
|---|---|---|
| *all of them* | `כ֯לה֯ן` / `כלה֯ן` | `כולהוןׄ` |
| *the trees* | `אי]לניה` | `אילניא` |
| *upon them* (3:1) | — | `עלי]ה֯ון` |
| *of two … and of three* (3:1) | `דתרתין֯ ותלת` | `דתרתין ודתלת` |

⭐ **4Q204 is consistently the more plene / more standard-Aramaic copy** (`כול` not `כל`; suffix `-הון` not `-הן`; determined state `-א` not `-ה`; the repeated `ד-`). This is worth stating because "the Aramaic" is routinely spoken of as if it were one thing standing behind the Greek. At the two verses where we can check, it is two things.

*(No claim is made here about which is earlier. Orthographic conservatism and orthographic modernisation are both possible and this evidence does not separate them.)*

---

## THE TEXT

> Where the witnesses genuinely differ, all readings are given and none is preferred.
> `( | )` marks a Ge'ez word carrying more than one sense.
> `[ ]` in Aramaic = editorial reconstruction, not ink.

---

# Chapter 4

⚠️ **Chapter 4 is one verse long.** That is the chapter, not a truncation of the source.

### 4:1

**ወዳግመ፡ ጠየቁ፡ መዋዕለ፡ ሐጋይ፡ ከመ፡ ኮነ፡ ፀሓይ፡ ላዕሌሃ፡ በቅድሜሃ፡ ወአንትሙሰ፡ ተኀሥሡ፡ ምጽላለ፡ ወጽላሎተ፡ በእንተ፡ ዋዕየ፡ ፀሓይ፡ ወምድርኒ፡ ትውዒ፡ እሙቀተ፡ ሐሩር፡ ወአንትሙሰ፡ ኢትክሉ፡ ከይዶታ፡ ለምድር፡ ወኢ፡ ኰኵሐ፡ በእንተ፡ ዋዕያ።**

*wädagəmä ṭäyäqu mäwaʿəlä ḥägayə kämä konä ṣ́äḥayə laʿəleha bäqədəmeha wäʾänətəmusä täḫäśəśu məṣəlalä wäṣəlalotä bäʾənətä waʿəyä ṣ́äḥayə wämədərəni təwəʿi ʾəmuqätä ḥärurə wäʾänətəmusä ʾitəkəlu käyədota lämədərə wäʾi kwäkwəḥä bäʾənətä waʿəya*

**And (again | secondly), (observe | examine | consider closely) the days of (the dry season | summer), how the sun is upon it, (before it | in front of it | facing it). And you — you (seek | search out) (shelter | shade) and shadow because of the (burning | scorching heat) of the sun; and the earth also burns with the heat of (scorching heat | fever | drought). And you — you are not able to tread upon the earth, nor upon the (rock | crag | boulder), because of its (burning | heat).**

- 🛑 **`ሐጋይ` *ḥägayə* is structurally untranslatable into "summer."** It is the Ethiopian **dry season**, paired throughout chs. 2–3 with `ክረምት` *kərämət*, the **rainy season**. The Greek at 2:3 has `θερείαν καὶ χειμῶνα` — *summer and winter*, a Mediterranean two-season year. **The Ge'ez has re-seasoned the text into an Ethiopian climate.** Any English word here imports the wrong calendar. The reader should be told the word means "the hot dry half of the year," not "summer."
- `ምጽላለ፡ ወጽላሎተ` — a **figura etymologica**: both nouns are from ጸለለ *ṣälälä*, "to shade." *Shelter-place and shadow.* English can approximate; Greek is absent here so the pair cannot be checked.
- `ዋዕይ` (*burning*) and `ሐሩር` (*scorching heat*) are a **two-word heat pair**, and this pair is confirmed by both Aramaic scrolls — see below.
- `ጠየቁ` is the same imperative that opens 2:1, 3:1 and 5:1. The chapter is one beat in a four-beat sequence of commands to look.

**Witnesses:**
- **Greek — ABSENT.** Not "no variant"; **no Greek text at all** in this apparatus for 4:1. See the provenance note above; whether this is a codex lacuna or an editorial gap **I could not determine**.
- **Latin — ABSENT.**
- Ethiopic `[Bertalotto p]`: `ፀሐይ` for `ፀሓይ` (×2), `ተኃሥሡ` for `ተኀሥሡ`, and **no `ወ` before `አንትሙሰ` and before `ምድርኒ`** — asyndeton where the base text coordinates. All laryngeal-orthography or conjunction-level; nothing semantic.
- ⭐ **Aramaic 4Q201:** `ח֯ז֯וׄ לכן לדׄגׄלי [‏…כוי]ה ושלקה ואנׄתׄןׄ [טלל ומסתר]יןׄ בׄעין מן קדמ֯יה [‏…ולמ]דׄרךׄ ע֯לׄ ע֯פ֯[ר]ה֯ [ועל כפיה] ל֯א תשכחון מ֯ן …`
  — *"**See** for yourselves … [burn]ing and scorching, and **you** — [shade and shelt]er you **seek** from **before it** … [and to **tread**] upon its du[s]t [and upon its rocks] you are **not able**, because of …"*
- ⭐ **Aramaic 4Q204:** `‏… ב֯הׄון כוׄייה ושלקה֯ […‏ ‏…כוי]תאׄ ולמדרךׄ […‏`
  — *"… in them, **burning and scorching** … the burn[ing] and to **tread** …"*

**What the Aramaic settles, and what it does not:**

| Element | Ge'ez | Aramaic | Ink or reconstruction |
|---|---|---|---|
| the heat-pair | `ዋዕይ` + `ሐሩር` | `כויה ושלקה` | ✅ **full ink in 4Q204**, reconstructed in 4Q201 — the pair is secure |
| *to tread* | `ከይዶታ` | `ולמדרך` | ✅ **full ink in 4Q204** |
| *you are not able* | `ኢትክሉ` | `ל֯א תשכחון` | ✅ ink (dot on the ל) |
| *before it* | `በቅድሜሃ` | `מן קדמ֯יה` | ✅ ink — but see the position note |
| *shade and shadow* | `ምጽላለ ወጽላሎተ` | `[טלל ומסתר]יןׄ` | 🛑 **entirely reconstructed except the plural ending `ין`** |
| *and upon the rock* | `ወኢ፡ ኰኵሐ` | `[ועל כפיה]` | 🛑 **100% editorial reconstruction — not one letter is ink** |
| *dust* vs *earth* | `ምድር` (*earth, land*) | `ע֯פ֯[ר]ה֯` (*its **dust***) | ⚠️ ink except the `ר`; different noun from the Ge'ez |
| the opening words | `ወዳግመ፡ ጠየቁ` | `ח֯ז֯וׄ לכן לדׄגׄלי` | ⚠️ `חזו לכן` = *see for yourselves*; **`לדׄגׄלי` I could not determine** |

🛑 **The "rock" agreement is circular and must not be cited.** `[ועל כפיה]` — "and upon its rocks" — has **zero surviving letters**. The most economical account of how an editor arrived at those words is that they were supplied *from the Ge'ez* (or the Greek tradition), which is precisely the text they would then appear to confirm. I flag this rather than list it as a trilingual agreement.

⚠️ **Position divergence:** the Ge'ez puts "before it" in the *sun* clause (*the sun is upon it, before it*). The Aramaic puts `מן קדמיה` in the *seeking* clause (*shade … you seek from before it*). Both readings stand.

⚠️ **`לדׄגׄלי` — undetermined.** Two of its five letters carry the edition's own uncertainty marks. It occupies the slot where the Ge'ez has "the days of the dry season," but I can find no reading of these consonants that yields that, and I will not guess one. This is a hole in the verse, and it is reported as a hole.

---

# Chapter 5

### 5:1

**ጠየቁ፡ እፎ፡ ዕፀው፡ በሐመልማለ፡ አቍጽል፡ ይትከደኑ፡ ወይፈርዩ፡ ወለብዉ፡ በእንተ፡ ኵሉ፡ በከመ፡ ገብረ፡ ለክሙ፡ ለእሎንቱ፡ ኵሎሙ፡ ዘሕያው፡ ለዓለም።**

*ṭäyäqu ʾəfo ʿəṣ́äwə bäḥämäləmalä ʾäqwəṣələ yətəkädänu wäyəfärəyu wäläbəwu bäʾənətä kwəlu bäkämä gäbərä läkəmu läʾəlonətu kwəlomu zäḥəyawə läʿalämə*

**(Observe | examine | consider closely) how the trees are (covered | clothed) with the (greenness | verdure | fresh green) of leaves, and bear fruit. And (understand | perceive | be discerning) concerning everything — according as he made **for you**, for all these — (he who | that which) lives for ever.**

- `ወለብዉ` *wäläbəwu* — (understand | perceive | grasp | be intelligent). Imperative plural.
- ⚠️ `ገብረ፡ ለክሙ` — *he made **for you***. Neither the Greek nor the Aramaic has "for you" here; both have "**his works**", which the Ge'ez lacks. Reported, not reconciled.
- ⚠️ `ዘሕያው፡ ለዓለም` is **grammatically ambiguous in the Ge'ez**: the relative `ዘ-` can attach to God or to "all these" that precede it. The verse can be read *"…for all these, which live for ever"* or *"…by him who lives for ever."* The Greek removes the ambiguity by naming the subject (`θεὸς ζῶν`, *the living God*); **the Ge'ez does not name God in this verse at all.** Both readings of the Ge'ez are live; I prefer neither.

**Witnesses:**
- Ethiopic `[Bertalotto p]`: `ወይፈዩ` for `ወይፈርዩ` (loss of `ር`); `ወለብው` for `ወለብዉ`; ⭐ **adds `ወአእምሩ`** (*and know*) after `በእንተ፡ ኵሉ`; `ለከመ` for `ለክሙ`.
- **Greek Gizeh:** `πῶς τὰ φύλλα χλωρὰ ἐν αὐτοῖς σκέποντα τὰ δένδρα, καὶ πᾶς ὁ καρπὸς αὐτῶν εἰς τιμὴν καὶ δόξαν. διανοήθητε καὶ γνῶτε περὶ πάντων τῶν ἔργων αὐτοῦ, καὶ νοήσατε ὅτι θεὸς ζῶν ἐποίησεν αὐτὰ οὕτως, καὶ ζῇ εἰς πάντας τοὺς αἰῶνας·`
  — Note the **inversion**: Greek has the *leaves* covering the *trees*; Ge'ez has the *trees* covered with *leaves*. Note also **three** verbs of cognition (`διανοήθητε`, `γνῶτε`, `νοήσατε`) against the base Ge'ez's one and ms `p`'s two.
- **Aramaic 4Q201:** `‏…אי]לניה כ֯לה֯ן …בהן יׄרוקין וחפ֯ין [‏…להד]רׄ תש֯[בחה …ואת]בוננו ב֯כל עׄבדיה [א]לׄ[ין ‏…]ה֯ו֯א ל[עלם] …כׄל֯ עׄב֯ד֯יהׄ אלין`
  — *"[the tr]ees, all of them … in them green things (`יׄרוקין`) and covering (`וחפ֯ין`) … [for glo]ry, pra[ise] … [and und]erstand in all th[ese] his works … he [is] for[ever] … all these his works."*
  ⭐ `יׄרוקין` (*green*) matches Ge'ez `ሐመልማል` and Greek `χλωρά`; `וחפ֯ין` (*covering*) matches Ge'ez `ይትከደኑ` and Greek `σκέποντα`. Both are ink.
  ⚠️ `ל[עלם]` — *for[ever]* — the word **עלם is bracketed and therefore reconstructed here**; but 4Q204 has it clean (next line), so the sense is not resting on the bracket.
- **Aramaic 4Q204:** `‏…] בכו]ל אילניא כולהוןׄ […‏ ‏…] תשבחה  […‏ ‏…] די לכול עלם […‏`
  — *"in al]l the trees, all of them … **praise** … that (is) for all eternity."* `תשבחה` and `די לכול עלם` are **full ink**.
- Latin **ABSENT**.

### 5:2

**ወምግባሩ፡ ቅድሜሁ፡ ለለ፡ ዓመት፡ ዘይከውን፡ ወኵሉ፡ ምግባሩ፡ ይትቀነዩ፡ ሎቱ፡ ወኢይትመየጡ፡ አላ፡ በከመ፡ ሠርዐ፡ አምላክ፡ ከመ፡ ዝ፡ ይትገበር፡ ኵሉ።**

*wäməgəbaru qədəmehu lälä ʿamätə zäyəkäwənə wäkwəlu məgəbaru yətəqänäyu lotu wäʾiyətəmäyäṭu ʾäla bäkämä śärəʿä ʾäməlakə kämä zə yətəgäbärə kwəlu*

**And his (works | deeds | doings) are before him, coming to be year by year. And all his works (serve | are subject to | do bondservice for) him and do not (turn aside | change | alter). But according as God (ordained | appointed | set in order | arranged), just so all is done.**

- `ወኢይትመየጡ` — root መየጠ, *to turn / turn back / change*. The chain verb of chs. 2–5; see Finding 2.
- `ይትቀነዩ` — ቀነየ carries **service** with an edge of **subjection/bondage**: (serve | be subject | be enslaved to).
- `ሠርዐ` — (ordain | appoint | establish | set in order | prescribe).

**Witnesses:**
- Ethiopic: `ለለዓመት` written solid; `p` `ሠርዓ` / `Bertalotto` `ሠርዐ` (orthographic); `ከመዝ` solid.
- **Greek Gizeh:** `καὶ τὰ ἔργα αὐτοῦ πάντα ὅσα ἐποίησεν εἰς τοὺς αἰῶνας ἀπὸ ἐνιαυτοῦ εἰς ἐνιαυτὸν γινόμενα πάντα οὕτως, καὶ πάντα ὅσα ἀποτελοῦσιν αὐτῷ τὰ ἔργα, καὶ οὐκ ἀλλοιοῦνται αὐτῶν τὰ ἔργα, ἀλλ᾽ ὡσπερεὶ κατὰ ἐπιταγὴν τὰ πάντα γίνεται.`
  ⚠️ **Greek has no "God" here** — `κατὰ ἐπιταγήν`, *according to command*, agentless. **The Ge'ez supplies `አምላክ`, "God."**
- ⭐ **Aramaic 4Q201:** `שׄנה [‏…וכ]לה֯ן עבדׄין מׄמׄר֯ה` — *"year … [and] all of them **do his word**."*
  ⭐⭐ **Three different constructions for the same clause, and each names a different agent-relation:**
  - Aramaic: the works are the **subject** and they *do his **word*** (`ממרה`) — an active obedience.
  - Greek: an impersonal passive — *all things come to pass as if by **command***, no possessor named.
  - Ge'ez: *as ***God*** ordained* — a named divine agent and a past act of ordering.

  All three are given. None is preferred. ⚠️ `מׄמׄר֯ה` carries three uncertainty marks — ink present, reading uncertain on מ, מ and ר.
- Latin **ABSENT**.

### 5:3

**ወርእዩ፡ እፎ፡ አብሕርት፡ ወአፍላግ፡ ኅቡረ፡ ይፌጽሙ፡ ኵሎ፡ ግብሮሙ።**

*wärəʾəyu ʾəfo ʾäbəḥərətə wäʾäfəlagə ḫəburä yəfeṣəmu kwəlo gəbəromu*

**And see how the **seas** and the rivers (together | alike | jointly) (complete | accomplish | fulfil | bring to an end) all their work.**

**Witnesses:**
- Ethiopic `[Bertalotto p]`: **omits `ኵሎ`** — "their work," not "all their work."
- **Greek Gizeh:** `ἴδετε πῶς ἡ θάλασσα καὶ οἱ ποταμοὶ ὡς ὁμοίως ἀποτελοῦσιν καὶ οὐκ ἀλλοιοῦσιν αὐτῶν τὰ ἔργα ἀπὸ τῶν λόγων αὐτοῦ.`
  - ⭐ **The Greek has a negative clause the Ge'ez does not have at all:** `καὶ οὐκ ἀλλοιοῦσιν αὐτῶν τὰ ἔργα` — *and they do not change their works.* The Ge'ez says only that they complete their work.
  - ⭐ **The Greek has `ἀπὸ τῶν λόγων αὐτοῦ` — "from his words."** The Ge'ez has nothing corresponding. Note that "word" surfaces one verse earlier in the **Aramaic** (`ממרה`, 5:2) and one verse later in the **Greek** (here), and **never in the Ge'ez of chapter 5**.
  - ⚠️ Greek `ἡ θάλασσα` is **singular** — *the sea*; Ge'ez `አብሕርት` is **plural** — *the seas*.
- Aramaic **ABSENT**. Latin **ABSENT**.

### 5:4

**ወአንትሙሰ፡ ኢተዐገሥክሙ፡ ወኢገበርክሙ፡ ትእዛዘ፡ እግዚእ፡ አላ፡ ተዐደውክሙ፡ ወሐመይክሙ፡ ዐቢያተ፡ ወድሩካተ፡ ቃላተ፡ በአፍ፡ ርኵስት፡ ዘዚኣክሙ፡ ላዕለ፡ ዕበየ፡ ዚኣሁ፡ ይቡሳነ፡ ልብ፡ ኢትከውነክሙ፡ ሰላም።**

*wäʾänətəmusä ʾitäʿägäśəkəmu wäʾigäbärəkəmu təʾəzazä ʾəgəziʾə ʾäla täʿädäwəkəmu wäḥämäyəkəmu ʿäbiyatä wädərukatä qalatä bäʾäfə rəkwəsətə zäziʾakəmu laʿəlä ʿəbäyä ziʾahu yəbusanä ləbə ʾitəkäwənäkəmu sälamə*

**But you — you did not (endure | persevere | bear it | show patience), and you did not do the (commandment | ordinance | injunction) of the Lord, but you (transgressed | crossed over | overstepped) and you (slandered | reviled | spoke evil | blasphemed) great and (hard | harsh | rough) words with the unclean mouth that is yours, against his (greatness | majesty). (Dry | withered | hard) of heart — there shall be no peace for you.**

- ⭐ **`ይቡሳነ፡ ልብ` is literally "DRY of heart."** ይቡስ *yəbus* is the ordinary Ge'ez word for **dry / withered / parched** (cognate with Hebrew יָבֵשׁ). The Greek has `σκληροκάρδιοι` — **HARD**-hearted. These are different images, and English "hardhearted" silently deletes the Ge'ez one.
  ⚠️ Whether the Ge'ez word had become a fixed idiom for "obdurate," or whether the translator chose "dry" deliberately against a chapter that opened with green leaves and living trees (3:1 uses `ይቡስ` of **withered trees**), **I cannot determine.** The lexical fact is reported; the resonance is offered as an observation, not a conclusion.
- `ሐመየ` — (slander | revile | speak evil of | blaspheme). Greek `κατελαλήσατε` is the same act.
- `ተዐገሠ` — (endure | be patient | bear | persevere | hold out). **Not** "change." See Finding 2.

**Witnesses:**
- Ethiopic: `አንትሙሰ` without `ወ`; `p` `ኢተዓገሥከሙ` / `Bertalotto` `ኢተዐገሥከሙ` — note **both read `-ከሙ`**, 2ms-looking, against the base text's `-ክሙ` (2mp); `p` `ትእዘዘ` / `Bertalotto` `ትእዛዘ`; `p` `ተዓደውክሙ` / `Bertalotto` `ተዐደውክሙ`; `p` `ዓቢያተ` / `Bertalotto` `ዐቢያተ`; **`ርኩሳት`** (plural) for base `ርኵስት` (fem. sg.); `ዘዚአክሙ`, `ዚአሁ` (orthographic).
- **Greek Gizeh:** `ὑμεῖς δὲ οὐκ ἐνεμείνατε οὐδὲ ἐποιήσατε κατὰ τὰς ἐντολὰς αὐτοῦ, ἀλλὰ ἀπέστητε καὶ κατελαλήσατε μεγάλους καὶ σκληροὺς λόγους ἐν στόματι ἀκαθαρσίας ὑμῶν κατὰ τῆς μεγαλωσύνης αὐτοῦ. **ὅτι κατελαλήσατε ἐν τοῖς ψεύμασιν ὑμῶν**, σκληροκάρδιοι, οὐκ ἔστιν εἰρήνη ὑμῖν.`
  - ⭐ **The clause `ὅτι κατελαλήσατε ἐν τοῖς ψεύμασιν ὑμῶν` — "because you spoke against (him) in your lies" — has no counterpart in the Ge'ez.**
  - ⚠️ Greek `κατὰ τὰς ἐντολὰς αὐτοῦ` (*his* commandments, **plural**) vs Ge'ez `ትእዛዘ፡ እግዚእ` (the commandment **of the Lord**, singular, with the divine title spelled out).
- ⭐ **Aramaic 4Q201:** `ואנׄתׄן֯ שניתן עבדׄכן֯ [‏…ותע]ב֯רון עלוהי רברבן וקשין בׄיום ט֯מׄתכן [‏…לבב]ן לה שלם לכן`
  — *"And you — **you have changed your works** … [and you have trans]gressed against him, great and hard (words) **in the day of your uncleanness** … [hard of hea]rt: **there is no peace for you**."*
  - ⭐ See Finding 2 for `שניתן עבדכן`.
  - ⭐ `רברבן וקשין` = *great and hard* — matching Ge'ez `ዐቢያተ፡ ወድሩካተ` and Greek `μεγάλους καὶ σκληρούς` exactly, and **all on ink**. A clean trilingual agreement.
  - ⭐ **`לה שלם לכן` — "no peace for you" — is unbracketed ink**, and agrees word-for-word with Greek `οὐκ ἔστιν εἰρήνη ὑμῖν` and Ge'ez `ኢትከውነክሙ፡ ሰላም`. This phrase is as securely attested as anything in these two chapters.
  - ⚠️ **`בׄיום ט֯מׄתכן` reads "in the DAY of your uncleanness"**, where Greek and Ge'ez both have **MOUTH** (`ἐν στόματι`, `በአፍ`). `יום` is clear ink; only the preceding `ב` carries an uncertainty mark.
    > 🛑 I note, and refuse to build on, the fact that the Aramaic word for "mouth" (`פום`) differs from `יום` by one letter. **Letter-count similarity is not evidence** — that is exactly the error retracted at 6:6 over `አርዲስ`/`ירד`. The direction of any error, or whether there was one, is **undeterminable here**. Both readings stand.
  - ⚠️ `[לבב]ן` — *hard of hea[rt]* — only the final `ן` is ink. **The Aramaic does not independently attest the heart-image**; it attests one letter of it.
  - Note the Aramaic accusation is `עלוהי` — you transgressed **against him** — where the Ge'ez has an intransitive `ተዐደውክሙ` (*you transgressed*, no object) and the Greek `ἀπέστητε` (*you departed*).
- Latin **ABSENT**.

### 5:5

**ወበእንተ፡ ዝ፡ አንትሙ፡ መዋዕሊክሙ፡ ትረግሙ፡ ወዓመታተ፡ ሕይወትክሙ፡ ታሀጕሉ፡ ወይበዝኅ፡ መርገም፡ ዘለዓለም፡ ወኢይከውነክሙ፡ ሣህል።**

*wäbäʾənətä zə ʾänətəmu mäwaʿəlikəmu tərägəmu wäʿamätatä ḥəyəwätəkəmu tahägwəlu wäyəbäzəḫə märəgämə zäläʿalämə wäʾiyəkäwənäkəmu śahələ*

**And because of this — you, your days you shall curse, and the years of your life you shall (destroy | bring to ruin | cause to perish); and the everlasting curse shall (be multiplied | increase | grow many), and there shall be no (mercy | clemency | pity) for you.**

- ⚠️ `ታሀጕሉ` (base text) is a **causative**: *you destroy / you cause to perish*. ms `p` reads `ተሐጕሉ`, which is naturally read as **passive/reflexive**: *you perish / you are destroyed*. **Who does the destroying flips between the two Ethiopic forms.** Both are given. Greek `ἀπολεῖται` makes *the years* the subject: *the years of your life shall perish*.

**Witnesses:**
- Ethiopic: `ወበእንተዝ` solid; `p` `ተሐጕሉ` / `Bertalotto` `ተሀጕሉ`; `ወኢይከሙነክሙ` (for `ወኢይከውነክሙ` — scribal).
- **Greek Gizeh — TRANSMITTED CORRUPT.** The actual ink is `τοιγὰρ τὰς ἡμέρας ὑμῶν ὑμεῖς` + `κατηρασασθαι` + `κατα` + `τῆς ζωῆς ὑμῶν ἀπολεῖται, καὶ τὰ ἔτη τῆς ἀπωλείας ὑμῶν πληθυνθήσεται ἐν κατάρᾳ αἰώνων, καὶ οὐκ ἔσται ὑμῖν ἔλεος καὶ εἰρήνη.`
  🛑 `καταράσεσθε` (Black) and `καὶ τὰ ἔτη` (Dillman/Lods/Charles/Black) are **CONJECTURES**, not readings. See Finding 3.
- ⭐⭐ **The Aramaic sides with the Greek against the Ge'ez on the subject of the multiplying.** 4Q201, in four units:
  - `אׄדין יומיׄכׄן` — *"**Then** your days"*
  - `תלוט[…` — *"you shall curse"*
  - `ו]שׄני` — *"[and the ye]ars"*
  - `ושנ]י אבׄד֯נכן י֯סׄגין בלׄ[וט …ורחמ]ין [` — *"[and the year]s of **your destruction** shall be **multiplied** in cu[rse … and merc]y"*

  | | what is multiplied |
  |---|---|
  | Ge'ez | **the everlasting curse** (`ወይበዝኅ፡ መርገም፡ ዘለዓለም`) |
  | Greek | **the years of your destruction** (`τὰ ἔτη τῆς ἀπωλείας ὑμῶν πληθυνθήσεται`) |
  | Aramaic | **the years of your destruction** (`ושנ]י אבׄד֯נכן י֯סׄגין`) |

  ⭐ `אבׄד֯נכן` (*your destruction*) and `י֯סׄגין` (*shall be multiplied*) are **ink**, carrying uncertainty dots but no brackets. Greek and Aramaic agree; the Ge'ez has changed the subject of the verb. **All three are printed. None is preferred** — but the reader should know the Ge'ez stands alone here.
  - ⚠️ Aramaic opens with `אׄדין` — ***then***, a temporal marker; Greek has `τοιγάρ` — ***therefore***, an inferential one; Ge'ez has `ወበእንተ፡ ዝ` — ***and because of this***, also inferential. Divergence noted, not resolved.
  - ⚠️ `[…ורחמ]ין` — *[and mer]cy* — only `ין` is ink. The Aramaic does **not** independently attest "mercy."
  - ⚠️ Greek ends `οὐκ ἔσται ὑμῖν **ἔλεος καὶ εἰρήνη**` — *neither mercy **nor peace***. **The Ge'ez has only `ሣህል` (mercy)**; "peace" is not denied here in the Ethiopic.
- Latin **ABSENT**.

### 5:6

**ወበውእቱ፡ መዋዕል፡ ትሁቡ፡ ሰላመ፡ ዚኣክሙ፡ በርግመት፡ ዘለዓለም፡ ለኵሉ፡ ጻድቃን፡ ወኪያክሙ፡ ይረግሙ፡ ኃጥኣን፡ ዘልፈ፡ ወለክሙ፡ ኅቡረ፡ ምስለ፡ ኃጥኣን።**

*wäbäwəʾətu mäwaʿələ təhubu sälamä ziʾakəmu bärəgəmätə zäläʿalämə läkwəlu ṣadəqanə wäkiyakəmu yərägəmu ḫaṭəʾanə zäləfä wäläkəmu ḫəburä məsəlä ḫaṭəʾanə*

**And in those days you shall give your **peace** as an everlasting curse to all the righteous; and the sinners shall curse you (continually | always | perpetually) — and (it shall be) for you together with the sinners.**

- 🛑 **The last clause of the Ge'ez has no predicate.** `ወለክሙ፡ ኅቡረ፡ ምስለ፡ ኃጥኣን` is *"and to you, together with the sinners"* — a dative with nothing governing it. **The Ge'ez sentence does not finish.** I have supplied "(it shall be)" in brackets to make it readable, and I flag that the supplement is mine and has no manuscript basis. The Greek at this point runs on for another forty words (below), which is at least where a predicate could have stood.

**Witnesses:**
- Ethiopic: `ውበእቱ` for `ወበውእቱ` (metathesis); `ዚአክሙ`; `p` `ኃጥአን` / `Bertalotto` `ኃጥኣን` (×2, orthographic).
- ⭐⭐⭐ **Greek Gizeh, in full:** `τότε ἔσται **τὰ ὀνόματα ὑμῶν** εἰς κατάραν αἰώνιον πᾶσιν τοῖς δικαίοις, καὶ **ἐν ὑμῖν καταράσονται πάντες οἱ καταρώμενοι**, καὶ πάντες οἱ ἁμαρτωλοὶ καὶ ἀσεβεῖς **ἐν ὑμῖν ὀμοῦνται**, καὶ πάντες οἱ` [`αμαρτοι` — 🛑 see Finding 3] `χαρήσονται, καὶ ἔσται αὐτοῖς **λύσις ἁμαρτιῶν** καὶ πᾶν ἔλεος καὶ εἰρήνη καὶ ἐπιείκεια, ἔσται αὐτοῖς **σωτηρία, φῶς ἀγαθόν**, καὶ αὐτοὶ **κληρονομήσουσιν τὴν γῆν**, καὶ πᾶσιν ὑμῖν τοῖς ἁμαρτωλοῖς **οὐχ ὑπάρξει σωτηρία**, ἀλλὰ ἐπὶ πάντας ὑμᾶς κατάλυσις, κατάρα.`

  **Three separate divergences, each significant:**

  1. ⭐⭐ **"your NAMES" vs "your PEACE."** Greek `τὰ ὀνόματα ὑμῶν ἔσται εἰς κατάραν` — *your **names** shall become a curse*: the idiom of a name used as a curse-formula. Ge'ez `ትሁቡ፡ ሰላመ፡ ዚኣክሙ፡ በርግመት` — *you shall **give your peace** in a curse*. Different noun, different verb, different picture.
     - Aramaic 4Q201: `‏…שמהתכ]ן֯  עלם ל֯[כל …‏‏…]ו֯לכלׄ[…‏` — *"[your **name**]s … eternal, for [all …"*
     - 🛑 **`שמהתכ` — "your names" — is INSIDE THE BRACKETS. Only the final `ן` is ink.** The apparent Aramaic support for the Greek here is **editorial reconstruction and must not be cited as a witness.** What the parchment actually gives at 5:6 is a plural-suffix `ן`, the word `עלם` (*eternal*), a `ל` + reconstructed `[כל]`, and `ולכל`. That is all.
  2. ⭐⭐ **"they shall SWEAR by you" vs "they shall CURSE you."** Greek: *all the sinners and the impious shall **swear by you*** (`ἐν ὑμῖν ὀμοῦνται`) — you become the oath-formula, as your names became the curse-formula. Ge'ez: *the sinners shall **curse you*** (`ወኪያክሙ፡ ይረግሙ፡ ኃጥኣን`) — they revile you. The Greek makes the sinners *use* you; the Ge'ez makes them *abuse* you.
  3. ⭐⭐⭐ **The whole salvation block is absent from the Ge'ez.** `λύσις ἁμαρτιῶν` (*release of sins*), `σωτηρία` (*salvation*, twice), `φῶς ἀγαθόν` (*good light*), `ἐπιείκεια` (*clemency, forbearance*), `κληρονομήσουσιν τὴν γῆν`, and the explicit denial `οὐχ ὑπάρξει σωτηρία` — **none of it is in the Ge'ez 5:6, and no equivalent of "salvation" or "forgiveness" occurs anywhere in the Ge'ez of chapter 5.** See Finding 1. **This is the single largest divergence in these two chapters and I am not smoothing it in either direction.**
- Latin **ABSENT**.

### 5:7

**ወለኅሩያንሰ፡ ይከውን፡ ብርሃን፡ ወፍሥሓ፡ ወሰላም፡ ወእሙንቱ፡ ይወርስዋ፡ ለምድር፡ ወለክሙሰ፡ ረሲዓን፡ ይከውነክሙ፡ ርግመት።**

*wäläḫəruyanəsä yəkäwənə bərəhanə wäfəśəḥa wäsälamə wäʾəmunətu yəwärəsəwa lämədərə wäläkəmusä räsiʿanə yəkäwənäkəmu rəgəmätə*

**But for the (chosen | elect) there shall be light and (joy | gladness | rejoicing) and peace, and they shall (inherit | take possession of) the earth. But for you, the (wicked | impious | ungodly), there shall be for you a curse.**

- ⭐ `ኅሩያን` *ḫəruyan*, "the chosen," is from ኀረየ *ḫaräyä*, **"to choose."** This is the **same root** the Watchers use at 6:2 — `ንኅረይ፡ ለነ፡ አንስተ`, *"let us **choose** for ourselves women."* The Greek preserves the same link (`ἐκλεκτοῖς` here, `ἐκλεξώμεθα` at 6:2). ⭐ **This is a rare case in 1 Enoch of a wordplay that survives translation intact** — as long as the English does not vary its word. God's *chosen* and the Watchers' *choosing* are one verb in both Ge'ez and Greek. (The Aramaic does not survive at 6:2's verb, so this cannot be traced to the Aramaic.)

**Witnesses:**
- ⚠️ Ethiopic `[Bertalotto p]` reads **`ረቢዓን`** where the base text has **`ረሲዓን`** (*the wicked*). `ረቢዕ` is "fourth"; *"and to you, the fourth ones, there shall be a curse"* does not yield sense in this context. **I report the manuscript reading and do not emend it.** The Greek `ὑμῖν δὲ τοῖς ἀσεβέσιν` supports the sense "impious," but supporting a sense is not the same as attesting a form.
- **Greek Gizeh:** `καὶ τοῖς ἐκλεκτοῖς φῶς καὶ **χάρις** καὶ εἰρήνη, καὶ αὐτοὶ κληρονομήσουσιν τὴν γῆν, ὑμῖν δὲ τοῖς ἀσεβέσιν ἔσται κατάρα.`
  - ⭐ **Ge'ez `ፍሥሓ` = *joy / gladness*. Greek `χάρις` = *grace / favour*.** These are not the same gift. The Greek word for *joy* is `χαρά` — one letter from `χάρις`, and `χαρά` is what Gizeh itself uses at 5:9 (`τὰ ἔτη τῆς χαρᾶς αὐτῶν`) exactly where the Ge'ez again has `ፍሥሓ`.
    > ⚠️ **Observation, not conclusion.** That the Ge'ez translator's Greek exemplar may have read `χαρά` here is *consistent* with the evidence and is *not established by it*. I am not choosing between "grace" and "joy," and I am not asserting a scribal error in either direction. Both readings are printed. This is exactly the kind of one-letter argument the 6:6 retraction warns against, and it is offered with that warning attached.
- Aramaic **ABSENT**. Latin **ABSENT**.

### 5:8

**ወእመሂ፡ ይትወሀቦሙ፡ ለኅሩያን፡ ጥበብ፡ ወኵሎሙ፡ እሎንቱ፡ የሐይዉ፡ ወኢይደግሙ፡ አብሶ፡ ኢ፡ በረሲዕ፡ ወኢ፡ በትዕቢት፡ አላ፡ ይገንዩ፡ ዘቦሙ፡ ጥበብ።**

*wäʾəmähi yətəwähäbomu läḫəruyanə ṭəbäbə wäkwəlomu ʾəlonətu yäḥäyəwu wäʾiyədägəmu ʾäbəso ʾi bäräsiʿə wäʾi bätəʿəbitə ʾäla yəgänəyu zäbomu ṭəbäbə*

**(And if | Then — see Finding 4) wisdom is given to the (chosen | elect), and all these shall live, and they shall not sin again — neither in (impiety | wickedness | ungodliness) nor in (pride | arrogance | haughtiness) — but those who have wisdom shall (be humble | bow down | submit | give thanks).**

- `ይገንዩ` — ገነየ spans (bow down | be humble | submit | render thanks | worship). **The Ge'ez does not disambiguate**, and the Greek offers no help because it has no corresponding clause.
- `አብሶ` — base text has the verbal noun/gerund (*sinning*); ms `p` has `አበሳ`, the noun *sin/transgression*.

**Witnesses:**
- ⭐ Ethiopic: `p` **`ወኣምሂ`** / `Bertalotto` **`ወአሜሃ`** (*then*) against the base text's **`ወእመሂ`** (*and if*). **See Finding 4 — this determines whether the promise of wisdom is conditional or announced.** `Bertalotto` is a correction, not a second witness.
- Ethiopic also: `አበሳ` for `አብሶ`; `ጥበበ` (accusative) for final `ጥበብ`.
- **Greek Gizeh:** `**τότε** δοθήσεται τοῖς ἐκλεκτοῖς φῶς καὶ χάρις, καὶ αὐτοὶ κληρονομήσουσιν τὴν γῆν. **τότε** δοθήσεται πᾶσιν τοῖς ἐκλεκτοῖς σοφία, καὶ πάντες οὗτοι ζήσονται, καὶ οὐ μὴ ἁμαρτήσονται ἔτι **οὐ κατ᾽ ἀλήθειαν** οὔτε κατὰ ὑπερηφανίαν, καὶ ἔσται ἐν ἀνθρώπῳ πεφωτισμένῳ φῶς καὶ ἀνθρώπῳ ἐπιστήμονι νόημα, καὶ οὐ μὴ πλημμελήσουσιν`
  - ⭐⭐ **Gizeh 5:8 opens by restating the whole of 5:7** — *light and grace to the elect, and they shall inherit the earth* — before beginning the wisdom clause. **The Ge'ez has this once, at 5:7.** This is the third of the three inheritance statements counted in Finding 1, and it is the clearest candidate for an internal doublet inside Gizeh.
  - 🛑 **`οὐ κατ᾽ ἀλήθειαν` — "not according to TRUTH."** As transmitted, the Greek says the elect will not sin again *according to truth*, which reverses the intended sense. The Ge'ez has `ኢ፡ በረሲዕ` — *not in **impiety***. **The apparatus records no conjecture here**, so unlike 5:5 and 5:6 this is not flagged as an editor's guess — it is what the manuscript says. **I print it as it stands and do not emend it to ἀσέβειαν.** The Ge'ez reading is given alongside. That the two disagree at a point where one of them is incoherent is the honest state of the verse.
  - ⭐ **`καὶ ἔσται ἐν ἀνθρώπῳ πεφωτισμένῳ φῶς καὶ ἀνθρώπῳ ἐπιστήμονι νόημα`** — *"and there shall be in an enlightened man, light; and to a man of understanding, insight."* **Absent from the Ge'ez entirely.**
  - ⭐ Conversely, **the Ge'ez `አላ፡ ይገንዩ፡ ዘቦሙ፡ ጥበብ`** — *"but those who have wisdom shall be humble"* — **is absent from the Greek**, which has instead `καὶ οὐ μὴ πλημμελήσουσιν` (*and they shall not offend / err*). **Each version has material the other lacks in this verse.** Neither is "the fuller text."
- Aramaic **ABSENT**. Latin **ABSENT**.

### 5:9

**ወኢይደግሙ፡ አብሶ፡ ወኢይትኴነኑ፡ ኵሎ፡ መዋዕለ፡ ሕይወቶሙ፡ ወኢይመውቱ፡ በመዓት፡ ወኢ፡ በመቅሠፍት፡ አላ፡ ኍልቈ፡ መዋዕለ፡ ሕይወቶሙ፡ ይፌጽሙ፡ ወይልህቅ፡ ሕይወቶሙ፡ በሰላም፡ ወዓመታተ፡ ፍሥሓሆሙ፡ ይበዝኁ፡ በሐሤት፡ ወበሰላም፡ ዘለዓለም፡ ውስተ፡ ኵሉ፡ መዋዕለ፡ ሕይወቶሙ።**

*wäʾiyədägəmu ʾäbəso wäʾiyətəkwenänu kwəlo mäwaʿəlä ḥəyəwätomu wäʾiyəmäwətu bämäʿatə wäʾi bämäqəśäfətə ʾäla ḫwələqwä mäwaʿəlä ḥəyəwätomu yəfeṣəmu wäyələhəqə ḥəyəwätomu bäsälamə wäʿamätatä fəśəḥahomu yəbäzəḫu bäḥäśetə wäbäsälamə zäläʿalämə wəsətä kwəlu mäwaʿəlä ḥəyəwätomu*

**And they shall not sin again, and **they shall not be (judged | condemned | put on trial)** all the days of their life; and they shall not die in (wrath | anger | fury), nor by (plague | scourge | chastisement | calamity). But the number of the days of their life they shall (complete | fulfil | bring to its end), and their life shall (grow | increase | grow old) in peace, and the years of their (joy | gladness) shall be multiplied in (exultation | rejoicing) and in everlasting peace, throughout all the days of their life.**

- ⭐ **`ወኢይትኴነኑ` — "and they shall not be judged" — has no counterpart in the Greek.** The Greek runs straight from *they shall not sin* to *all the days of their life*. The Ge'ez inserts an explicit exemption from judgment into the promise to the elect. **Doctrinally loaded, and the Ge'ez stands alone.**
- ⭐ **`ወኢ፡ በመቅሠፍት` — "nor by plague/scourge" — likewise has no Greek counterpart.** Greek has one cause of death (`ἐν ὀργῇ θυμοῦ`, *in wrath of anger*); the Ge'ez has two (`በመዓት` *wrath* and `በመቅሠፍት` *plague/scourge*).
- `ወይልህቅ` — ልህቀ is (to grow | to increase | to grow old | to become great). Greek `αὐξηθήσεται` is *shall be increased*. **The Ge'ez word can equally mean their life shall grow OLD in peace**, which is a different promise from "increase." Both senses given; I prefer neither.

**Witnesses:**
- Ethiopic `[Bertalotto p]`: opens **`ኢይደግሙ`** without `ወ`; `ወኢመውቱ` for `ወኢይመውቱ`; ⭐ **reverses the order to `በመቅሠፍት፡ ወኢበመዓት`** — *plague* first, *wrath* second; `ይበዝኅ` (singular) for `ይበዝኁ` (plural); `በኃሤት` for `በሐሤት` (orthographic).
- **Greek Gizeh:** `οὐδὲ μὴ ἁμάρτωσιν πάσας τὰς ἡμέρας τῆς ζωῆς αὐτῶν, καὶ οὐ μὴ ἀποθάνωσιν ἐν ὀργῇ θυμοῦ, ἀλλὰ τὸν ἀριθμὸν αὐτῶν ζωῆς ἡμερῶν πληρώσουσιν, καὶ ἡ ζωὴ αὐτῶν αὐξηθήσεται ἐν εἰρήνῃ, καὶ τὰ ἔτη τῆς **χαρᾶς** αὐτῶν πληθυνθήσεται ἐν ἀγαλλιάσει καὶ εἰρήνη αἰῶνος` + `ἐν πάσαις ταῖς ἡμέραις τῆς ζωῆς αὐτῶν.`
  - Note `χαρᾶς` (*joy*) here against `χάρις` (*grace*) at 5:7–5:8, in the same Greek manuscript, both rendered `ፍሥሓ` in the Ge'ez. See the caution at 5:7.
- ⚠️ **Aramaic 4Q202:** `‏…יו]מי …‏` — **two letters, `מי`**, reconstructed as `יו]מי`, *"days of."* This is the only Aramaic in the verse and it **carries no independent weight whatever.** Listing it as "the Aramaic attests 5:9" would be misleading; it attests two letters.
- Latin **ABSENT**.

---

## Verification pass — what was checked, and how

Every counted claim was re-checked programmatically against the XML apparatus and the Ge'ez JSON, **NFD-normalised with combining marks stripped before comparison** (the accent-blind-grep failure documented in `enoch-6.md`), and each probe was proven against a known-present string before any null result was accepted.

| Claim | Result |
|---|---|
| `κληρονομήσουσιν τὴν γῆν` occurs 3× in Gizeh ch. 5 (5:6, 5:7, 5:8) | ✅ confirmed, count = 3 |
| `φῶς` 4×, `σωτηρία` 2×, `χάρις` 2× in Gizeh ch. 5 | ✅ confirmed |
| Ge'ez ch. 5 has the inheritance clause once, at 5:7 | ✅ confirmed |
| Ge'ez ch. 5 has **no** salvation root (ደኀነ) and **no** forgiveness root (ሠረየ) | ✅ confirmed against the full 119-form word-list of the chapter |
| Greek **entirely absent** for 4:1 in this apparatus | ✅ confirmed — 0 Greek readings; Gizeh resumes mid-clause at 5:1 |
| Latin absent for all of chs. 4–5 | ✅ confirmed |
| Syncellus absent for all of chs. 4–5 | ✅ confirmed — his readings begin at 6:1 |
| `שניתן עבדכן` (5:4) is ink, not reconstruction | ✅ confirmed — no brackets; one uncertainty dot on the ד of `עבדכן` |
| `שמהתכ]ן` (5:6, "your names") is reconstruction | 🛑 **confirmed reconstruction — only `ן` is ink.** Downgraded from "Aramaic supports the Greek" to "Aramaic supplies one letter" |
| `[ועל כפיה]` (4:1, "and upon its rocks") is reconstruction | 🛑 **confirmed — zero letters of ink.** Excluded from the agreement table as circular |
| `[טלל ומסתר]ין` (4:1, "shade and shelter") is reconstruction | 🛑 confirmed — only `ין` is ink |
| `תשבחה` (5:1, "praise") is ink in 4Q204 | ✅ confirmed — unbracketed |
| `אבדנכן` / `יסגין` (5:5) are ink | ✅ confirmed — uncertainty dots only, no brackets |
| `לה שלם לכן` (5:4, "no peace for you") is ink | ✅ confirmed — unbracketed |
| 5:5 and 5:6 Greek rest on conjecture at 3 points | ✅ confirmed — Black; Dillman/Lods/Charles/Black; Swete/Charles/Black; F-R |
| `Bertalotto` is declared `<ms>` but is an edited transcription of `p` | ⚠️ confirmed by inspection: 11 of 12 `p`/`Bertalotto` splits in chs. 4–5 are pure orthography |
| 4Q204 more plene than 4Q201 at every overlap | ✅ confirmed at `כל`/`כול`, `-הן`/`-הון`, `-ה`/`-א`, `ותלת`/`ודתלת` |

---

## What I could not determine — stated, not smoothed

1. 🛑 **`לדׄגׄלי` (4Q201, 4:1).** Undetermined. Two of five letters carry the edition's uncertainty marks. It sits where the Ge'ez has "the days of the dry season" and I can find no reading of these consonants that yields that. **I did not guess.**
2. 🛑 **Whether the Greek of 4:1 is a codex lacuna or an edition gap.** The apparatus simply has no Greek there. This dataset cannot distinguish the two.
3. 🛑 **The direction of the great 5:6 divergence.** Greek expansion or Ge'ez contraction — the evidence here does not decide it, and Gizeh's own triple inheritance-promise cuts both ways.
4. 🛑 **`ביום` vs "mouth" (5:4).** Both readings stand. I refuse the one-letter argument on the standing 6:6 precedent.
5. 🛑 **`χάρις` vs `χαρά` (5:7).** Same refusal. The Ge'ez has "joy" and Gizeh has "grace"; that is the finding, and no more.
6. 🛑 **Which of the two supralinear marks (U+05C4 dot, U+05AF circle) the edition uses for "probable" and which for "possible."** I treated both alike as *ink present, reading uncertain*, which is the conservative reading of either.
7. ⚠️ **Whether `ይቡሳነ፡ ልብ` ("dry of heart," 5:4) was a dead idiom or a live image.** The lexical fact is certain; the resonance with the green trees of 5:1 and the withered trees of 3:1 is an observation I am not able to promote to a claim.
8. ⚠️ **`ረቢዓን` (ms `p`/Bertalotto, 5:7).** Reported as the manuscript reading. It does not yield sense; I did not emend it.

## What these chapters show about the book

1. **The turn to judgment is where the versions part company hardest.** Chapters 4, 5:1–3 — nature, seasons, sea — show small, ordinary translation losses. From 5:4 onward the divergences become **doctrinal**: who is accused of what (5:4), what is multiplied (5:5), whether the elect are forgiven and saved (5:6), whether they are exempt from judgment (5:9), whether wisdom is promised or merely hypothesised (5:8). **The temptation to smooth is highest exactly where the texts are furthest apart, and that is not a coincidence.**
2. **Neither version is the fuller text.** In 5:6 and 5:8 the Greek has whole clauses the Ge'ez lacks; in 5:8 and 5:9 the Ge'ez has whole clauses the Greek lacks. "Longer = better" fails here as it failed at 6:7.
3. **The Aramaic is worth most where it is *ink*.** `שניתן עבדכן` (5:4) and `אבדנכן יסגין` (5:5) are genuine, load-bearing, unbracketed corrections to the picture the Ge'ez gives. `[שמהתכ]ן` (5:6) and `[ועל כפיה]` (4:1) are not evidence at all — and the second of those would, if quoted uncritically, appear to confirm the very text it was probably reconstructed from.
4. 🛑 **The apparatus mixes editors with manuscripts, and does so at the most quotable verses.** "The sinless shall rejoice" (5:6) has no manuscript subject. "You shall curse your days" (5:5) is corrupt at two points. `Bertalotto` is filed as a manuscript and is a corrected transcription. A reader who trusts the sigla will cite three editors as three witnesses.
