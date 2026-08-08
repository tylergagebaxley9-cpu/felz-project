# Bible Sources — Original-Language Corpus

Local path: `~/projects/bible-sources/` — ~6.5 GB on disk.

## The honest framing

**No autographs survive.** Nothing written by an original author exists. What this corpus holds:

1. **Diplomatic editions** — faithful transcriptions of the oldest complete manuscripts.
2. **Critical editions** — scholarly reconstructions of the earliest recoverable text from many manuscripts.
3. **Morphology-tagged texts** — every word parsed and lemmatized for study.

Oldest complete witnesses: Hebrew OT = Leningrad Codex, 1008 CE. Greek NT = Codex Sinaiticus / Vaticanus, ~325–360 CE. Oldest NT fragment = P52 (John 18), ~125–175 CE. Oldest Hebrew biblical text = Dead Sea Scrolls, ~250 BCE–68 CE.

---

## Hebrew / Aramaic Old Testament — `hebrew-ot/`

| Dir | What it is |
|---|---|
| `morphhb/` | Open Scriptures Hebrew Bible — Westminster Leningrad Codex, full morphology + Strong's. CC BY 4.0 |
| `hbo_uhb/` | unfoldingWord Hebrew Bible — UHB, USFM, actively corrected. CC BY-SA 4.0 |
| `STEPBible-Data/` | TAHOT — Tyndale House amalgamated Hebrew OT, tagged. CC BY 4.0 |

All three descend from the **Leningrad Codex (B19A, 1008 CE)** — the oldest complete Hebrew Bible.

## Greek New Testament — `greek-nt/`

| Dir | What it is |
|---|---|
| `SBLGNT/` | SBL Greek NT (2010) — modern critical edition, free license |
| `Nestle1904/` | Nestle 1904 — public domain, with syntax trees |
| `el-x-koine_ugnt/` | unfoldingWord Greek NT — based on NA28/Nestle 1904 lineage. CC BY-SA |
| `byzantine-majority-text/` | Robinson–Pierpont Byzantine Majority Text — the alternative textual tradition |

Two rival philosophies represented: **eclectic/Alexandrian** (SBLGNT, Nestle) vs **Byzantine majority** (RP). Comparing them shows exactly where the manuscript tradition disagrees.

## Septuagint (Greek OT) — `septuagint/`

| Dir | What it is |
|---|---|
| `LXX-Rahlfs-1935/` | Rahlfs LXX with apparatus — the standard edition (789 MB) |
| `LXX-Swete/` | Swete's LXX — public domain, Vaticanus-based |
| `GreekResources/` | Lexical + morphological support data |

The LXX is the **Greek translation of the OT made ~250–100 BCE** — older than any surviving Hebrew manuscript except the Dead Sea Scrolls, and the version the NT authors usually quote.

## Aramaic / Syriac — `aramaic-syriac/`

| Dir | What it is |
|---|---|
| `peshitta/` | ETCBC Syriac Peshitta OT |
| `syrnt/` | ETCBC Syriac NT |

Syriac is the closest surviving literary relative of the **Aramaic Jesus actually spoke**.

## Deuterocanon / Apocrypha — `deuterocanon/`

`OpenHebrewBible/` — plus the deuterocanonical books (Tobit, Judith, Wisdom, Sirach, Baruch, 1–2 Maccabees, additions to Daniel/Esther) are **already inside the Rahlfs LXX** in `septuagint/`. Catholic and Orthodox canon; dropped by Protestants at the Reformation.

## Pseudepigrapha — `pseudepigrapha/Online-Critical-Pseudepigrapha/static/docs/`

43 XML texts in original languages (Greek, Ge'ez, Syriac, Latin, Slavonic, Hebrew), including:

- **1 Enoch** (`1En.xml`) — quoted directly in Jude 14–15; canonical in the Ethiopian church
- **Jubilees** (`Jub.xml`, `Jubi.xml`) — found at Qumran; Ethiopian canon
- **4 Ezra**, **2 Baruch** (Greek + Syriac), **3 Baruch**, **4 Baruch**
- **3 & 4 Maccabees**, **Psalms of Solomon**, **Sibylline Oracles**
- **Testament of Abraham/Adam/Job/Solomon**, **Joseph and Aseneth**, **Life of Adam and Eve**
- **Letter of Aristeas** — the origin story of the Septuagint

Also `OpenGNT/` — Open Greek NT with full tagging.

## Gnostic / Coptic — `nag-hammadi/corpora/`

Coptic SCRIPTORIUM corpora (2.5 GB), including in **original Coptic**:

- `thomas-gospel/` — **Gospel of Thomas** (Nag Hammadi II,2) — 114 sayings of Jesus, no narrative
- `pistis-sophia/` — Pistis Sophia
- `acts-pilate/`, `book-bartholomew/`, `dormition-john/`, `lament-mary/`
- `bible/`, `bohairic.nt/`, `bohairic.ot/`, `sahidic*` — Coptic biblical translations (3rd–4th c., very early witnesses)
- Dozens of monastic/hagiographic texts

## Apostolic Fathers & early Greek — `apostolic-fathers/First1KGreek/`

First Thousand Years of Greek (523 MB). Contains **Didache, 1–2 Clement, Ignatius, Polycarp, Shepherd of Hermas, Epistle of Barnabas** — plus Josephus and Philo. Barnabas and Hermas are **bound into Codex Sinaiticus itself**, i.e. that scribe considered them scripture.

---

## Samaritan Pentateuch — `samaritan/sp/`

DT-UCPH Text-Fabric dataset (619 MB), from the Samaritanus project (Martin-Luther-Universität Halle-Wittenberg, dir. Stefan Schorch). Transcribed from **MS Dublin Chester Beatty 751** (Gen 1 – Deut 32:36) + **MS Garizim 1** (Deut 32:36b–34). Free for research and education.

The Samaritan community's own Torah — it diverges from the Masoretic text in ~6,000 places, and where it disagrees, it sometimes agrees with the Septuagint against the Hebrew. A genuinely independent line of transmission.

## Ethiopic / Ge'ez — `ethiopic/ethiopian-bible/`

**36 books** of Ge'ez text (sourced from Beta Masaheft, Universität Hamburg, CC BY-SA 4.0). This is **partial, not the full 81-book canon** — but it holds the books that exist *nowhere else*:

`1En` `Jub` `1Meq` `3Meq` `4Bar` `ApEz` `Clem` `Sinod` `Teach` `MysHE` `KN` `Synax` `TestLd`

- **1 Enoch and Jubilees survive complete only in Ge'ez** — the Ethiopic is the best witness on earth for both
- **Meqabyan I & III** (Ethiopian Maccabees) — unrelated to the Greek Maccabees, found in no other canon
- **Kebra Nagast**, **Sinodos**, **Didascalia (Teach)**, **Mysteries of Heaven and Earth**

Missing from this reader: 2 Meqabyan, Psalms, Jeremiah, Ezekiel, Daniel, most Minor Prophets, and the entire NT.

## NT Apocrypha (Greek/Latin) — `nt-apocrypha/`

Public-domain critical editions, plain text:

| File | Edition | Contains |
|---|---|---|
| `evangeliaapocryp00tisc.txt` | Tischendorf, *Evangelia Apocrypha* (1876) | **Protevangelium of James**, Infancy Gospel of Thomas, **Acts of Pilate / Gospel of Nicodemus**, Descent into Hell, Pseudo-Matthew |
| `evangeliaapocry02tiscgoog.txt` | same, alt. scan | — |
| `apocalypsesapocr02tiscuoft.txt` | Tischendorf, *Apocalypses Apocryphae* (1866/1900) | **Apocalypse of Peter**, Apocalypse of Paul, Apocalypse of John, Assumption of Moses |
| `apocalypsesapoc00perkgoog.txt` | same, alt. scan | — |
| `actaapostolorvm01tiscgoog.txt` | Lipsius–Bonnet, *Acta Apostolorum Apocrypha* (1891) | **Acts of Peter, Paul, John, Andrew, Thomas** |

> These are OCR'd scans of 19th-c. printed editions — searchable but with OCR noise, unlike the tagged XML corpora above.

## Not downloaded — and why

| Item | Status |
|---|---|
| **NA28 / UBS5** | Copyrighted (German Bible Society). Not free. SBLGNT is the closest free equivalent. |
| **BHS / BHQ apparatus** | Copyrighted. The base text (WLC) is here; the critical apparatus is not. |
| **Dead Sea Scrolls transcriptions** | Official DJD transcriptions are copyrighted. **Images are free** — see below. |
| **Nag Hammadi — full Coptic (all 52 tractates)** | **Not freely available.** The complete Coptic edition is Brill's *Coptic Gnostic Library* (1975–95), under copyright. naghammadi.org publishes only French translations, explicitly no reproduction. What IS open: Gospel of Thomas, Pistis Sophia, Mysteries of John, Acts of Pilate, Book of Bartholomew — all in `nag-hammadi/corpora/`. |
| **Ethiopic canon books 37–81** | Only 36 of 81 digitized in the open reader. Rest exists mainly in manuscript facsimile at Beta Masaheft / EMML. |
| **2 Meqabyan** | Not in the open Ge'ez reader. |

## Manuscript images — free, online, not mirrored (too large)

- **Codex Sinaiticus** (~350 CE, oldest complete NT) — codexsinaiticus.org — full transcription + images
- **Dead Sea Scrolls** — deadseascrolls.org.il (Leon Levy Digital Library) — free high-res
- **Codex Vaticanus** (~325 CE) — digi.vatlib.it
- **Codex Alexandrinus** (~400 CE) — British Library digitised manuscripts
- **NT Virtual Manuscript Room** — ntvmr.uni-muenster.de — thousands of NT manuscripts
- **CSNTM** — csntm.org — manuscript photography archive
- **Oxyrhynchus Papyri** — papyri.info / POxy
- **Aleppo Codex** (~930 CE, partial) — aleppocodex.org
- **Sefaria** — sefaria.org — Tanakh, Targums, rabbinic corpus, free API

## Licensing

All downloaded material is public domain or openly licensed (CC BY / CC BY-SA / permissive). Attribution requirements live in each repo's LICENSE file — check before redistributing.
