# Provenance labels

Every text in this corpus is marked by **what kind of thing it is**. This is the
single most important piece of metadata here, because "old" and "original" are
not the same claim, and a translation is somebody's interpretation no matter how
early it is.

## The four labels

| Label | Means | Editorial layer |
|---|---|---|
| **ORIGINAL** | Original-language witness. A manuscript, or a diplomatic transcription of one. What the scribe actually wrote, errors included. | none |
| **TRANSLATION** | Someone rendered this out of another language. Old and valuable, but it is already an interpretation. | translator's |
| **EDITED** | A modern reconstruction assembled from many manuscripts. No single manuscript reads this way. | editors' |
| **PRINTED** | A pre-1820 printed edition. Old print, but set from whatever manuscripts the printer happened to have. | printer's/editor's |

> **The trap this guards against:** Erasmus 1516 is a *printed* text from 1516,
> but it was set from 12th–13th century minuscules, and he back-translated the
> last six verses of Revelation out of Latin himself. A 1516 date on the title
> page says nothing about how close the text sits to the source. Always read the
> WITNESS date, not the EDITION date.

---

## ORIGINAL — original-language witnesses

| Text | Witness date | Notes |
|---|---|---|
| `dead-sea-scrolls/etcbc-dss` | **c. 250 BCE – 68 CE** | Oldest biblical text on earth. ⚠️ CC BY-**NC** |
| `papyri/cntr-transcriptions` | 2nd–8th c. CE | P1–P141, incl. **P52 (c. 125–175 CE)** |
| `manuscripts/sinaiticus` | c. 330–360 CE | Oldest complete NT. ⚠️ CC BY-**NC**-SA |
| `manuscripts/bezae` | c. 400 CE | |
| `manuscripts/zacynthius` | 6th c. CE | Palimpsest catena |
| `hebrew-ot/morphhb` (WLC) | **1008 CE** | Leningrad Codex, diplomatic + morphology |
| `hebrew-ot/hbo_uhb`, `STEPBible-Data` | 1008 CE | Same codex, different tagging |
| `samaritan/sp` | 12th–13th c. CE | Independent transmission line |
| `nag-hammadi/corpora` (Coptic) | c. 350 CE | Coptic is the original language of these |

## TRANSLATION — rendered by someone out of another language

| Text | Translated | From | Notes |
|---|---|---|---|
| `septuagint/LXX-Rahlfs-1935` | **c. 250–100 BCE** | Hebrew | **A translation.** Often preserves an older Hebrew than the MT — see Deut 32:8 |
| `septuagint/LXX-Swete` | same | Hebrew | Vaticanus-based |
| `aramaic-syriac/peshitta` | 1st–3rd c. CE | Hebrew | |
| `aramaic-syriac/syrnt` | c. 400–450 CE | Greek | |
| `targums/*` | 2nd–9th c. CE | Hebrew | Aramaic paraphrase, often expansive — not literal |
| `ethiopic/ethiopian-bible` | 4th–6th c. CE | Greek | But **1 Enoch and Jubilees survive complete ONLY here** |
| `nag-hammadi/` Coptic OT/NT | 3rd–4th c. CE | Greek | Distinct from the Coptic-original gnostic texts above |

## EDITED — modern reconstructions

No single manuscript reads this way. Each is a committee's or editor's judgement.

| Text | Editor | Edition date |
|---|---|---|
| `greek-nt/SBLGNT` | Michael Holmes | 2010 |
| `greek-nt/Nestle1904` | Eberhard Nestle | 1904 |
| `greek-nt/el-x-koine_ugnt` | unfoldingWord | 2018– |
| `greek-nt/byzantine-majority-text` | Robinson & Pierpont | 1991/2005/2018 |
| `septuagint/LXX-Rahlfs-1935` (apparatus) | Alfred Rahlfs | 1935 |
| `GRCNA28_DBS_HS` | Nestle-Aland 28th ed. | 2012 |

> ⚠️ **GRCNA28_DBS_HS / LATSEPT_DBS_HS are Deutsche Bibelgesellschaft
> copyrighted editions.** Included at Gage's direction and labeled here so the
> restriction travels with the file. Personal study only — these must never be
> redistributed, published, or bundled into anything sold.

## PRINTED — pre-1820 printed editions

| Edition | Printed | Set from | Warning |
|---|---|---|---|
| `early-editions/textus-receptus` (Stephanus) | 1550 | 12th–13th c. minuscules | |
| `early-editions/elzevir` | 1633 | as Erasmus | |
| `early-editions/scrivener` | 1881 | reconstructs the TR | post-1820 |
| Erasmus, *Novum Instrumentum* | 1516 | ~6 Basel minuscules | **Rev 22:16–21 back-translated from Latin by Erasmus. Those verses are in no Greek manuscript.** |
| Bomberg / ben Chayyim Rabbinic Bible | 1524–25 | Sephardic ben Asher MSS | The standard Hebrew text for 400 years |
| Complutensian Polyglot | 1514–17 | mixed | |
| Antwerp Polyglot | 1568–73 | mixed | |
| Walton's London Polyglot | 1655–57 | mixed | 8 languages in parallel |
| Kennicott | 1776–80 | 600+ Hebrew MSS | Pre-1820 apparatus |
| de Rossi | 1784–88 | Hebrew MSS | Pre-1820 apparatus |
| Holmes & Parsons | 1798–1827 | LXX MSS | vols 3–5 are post-1820 |
| Sixtine LXX | 1587 | **Codex Vaticanus, c. 300–325 CE** | Old print, genuinely old witness |
| Grabe LXX | 1707–20 | **Codex Alexandrinus, c. 400–440** | |

## Also on disk

- `pseudepigrapha/` — 43 texts, ORIGINAL languages, composed c. 300 BCE – 5th c. CE
- `apostolic-fathers/First1KGreek` — ORIGINAL Greek, composed c. 50–160 CE
- `nt-apocrypha/` — PRINTED, Tischendorf 1853/1866 and Lipsius–Bonnet 1891 (all post-1820)
- `early-editions/scans/` — OCR text layers of the PRINTED editions above.
  ⚠️ **OCR quality is poor for Greek and Hebrew running text** (measured: Acts 2:27
  came out of the Erasmus layer as `ὅτὶ Ὀυὰ τγκαταλείψας`, and the Latin column was
  OCR'd through a Greek model). Usable for Latin and for apparatus reference
  numbers; not trustworthy as a translation base.

---

## How to read a disagreement

When two texts differ, the labels tell you what kind of disagreement it is:

- **ORIGINAL vs ORIGINAL** — a real textual variant. Two scribes wrote different things. *(Sinaiticus ends Mark at 16:8; later manuscripts have 16:9–20.)*
- **ORIGINAL vs TRANSLATION** — could be a variant, or could be the translator interpreting. Needs a second witness to settle. *(Deut 32:8: the LXX's "angels of God" was confirmed a real variant only when the Qumran Hebrew turned up reading בני אלוהים.)*
- **ORIGINAL vs EDITED** — the editor made a choice. Their apparatus should say why.
- **PRINTED vs anything** — first ask what manuscripts the printer had. Usually few, usually late.
