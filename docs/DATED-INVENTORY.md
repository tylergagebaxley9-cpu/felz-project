# Dated Inventory — what is already on disk

`~/projects/bible-sources/` — 6.9 GB as of 2026-08-08.

Every item carries **two dates**, because they are not the same thing and conflating them is how people get fooled:

- **Witness** — when the manuscript, scroll or artifact the text rests on was physically made.
- **Edition** — when a modern or early-modern editor published *this particular version* of it.

A 4th-century codex with a 2009 transcription is old evidence in a new wrapper. A 1935 critical edition is a modern editor's reconstruction of a text no single manuscript contains. Both are useful; they are not the same kind of thing.

Where a date is contested among scholars, the range is given rather than a single year.

---

## Hebrew / Aramaic Old Testament — `hebrew-ot/`

| Item | Witness | Edition | Note |
|---|---|---|---|
| `morphhb/` — Open Scriptures Hebrew Bible (WLC + morphology + Strong's) | Leningrad Codex **1008 CE** | ongoing, **2008–present** | Diplomatic — follows the codex, does not reconstruct |
| `hbo_uhb/` — unfoldingWord Hebrew Bible | Leningrad Codex **1008 CE** | **2017–present** | Actively corrected against the codex |
| `STEPBible-Data/` — TAHOT (Tyndale House) | Leningrad Codex **1008 CE** | **2017–present** | Tagged/amalgamated |

All three descend from the same single manuscript: **Leningrad Codex (B19A), 1008 CE** — the oldest *complete* Hebrew Bible in existence.

> The Masoretic tradition these represent was standardised c. 7th–10th c. CE by the Masoretes of Tiberias. The consonantal text is far older; the vowel points and accents are not.

## Greek New Testament — `greek-nt/`

| Item | Witness | Edition | Note |
|---|---|---|---|
| `SBLGNT/` | eclectic — no single MS | **2010** | Modern reconstruction |
| `Nestle1904/` | eclectic | **1904** | Public domain; still post-1820 |
| `el-x-koine_ugnt/` — unfoldingWord Greek NT | eclectic, NA28/Nestle lineage | **2018–present** | Modern reconstruction |
| `byzantine-majority-text/` — Robinson–Pierpont | Byzantine MS majority, mostly **9th–15th c.** copies | **1991 / 2005 / 2018** | The rival tradition |

None of these is a manuscript. All four are editors' judgements about what the manuscripts collectively imply. They disagree with each other in thousands of places, which is precisely why having more than one is worth the disk.

## Septuagint (Greek OT) — `septuagint/`

| Item | Witness | Edition | Note |
|---|---|---|---|
| `LXX-Rahlfs-1935/` (789 MB, w/ apparatus) | mainly Vaticanus **c. 300–325 CE**, Sinaiticus **c. 330–360**, Alexandrinus **c. 400–440** | **1935** | Standard modern edition |
| `LXX-Swete/` | Vaticanus-based, **c. 300–325 CE** | **1887–94** | Public domain, closer to diplomatic |
| `GreekResources/` | — | modern | Lexical/morphological support |

The LXX **translation itself** dates to **c. 250–100 BCE** — Torah first (traditionally c. 250 BCE under Ptolemy II), the rest over the following century and a half. That makes the *translation* older than every surviving Hebrew manuscript except the Dead Sea Scrolls, and it is the version the New Testament authors usually quote.

## Aramaic / Syriac — `aramaic-syriac/`

| Item | Witness | Edition | Note |
|---|---|---|---|
| `peshitta/` — ETCBC Syriac Peshitta OT | translation **1st–3rd c. CE**; MSS from **5th c.** (Codex Ambrosianus 6th–7th c.) | modern digital, **2017–present** | |
| `syrnt/` — ETCBC Syriac NT | translation **c. 400–450 CE** (Peshitta NT) | modern digital | |

Syriac is the closest surviving literary relative of the Aramaic spoken in 1st-century Palestine — a cousin dialect, not the same dialect.

## Targums — `targums/` *(round 2, incomplete)*

| Item | Witness | Edition | Note |
|---|---|---|---|
| `onkelos/` | redacted **c. 2nd–5th c. CE**, Babylonian | modern digital | Only 2.1 MB total on disk |
| `pseudo-jonathan/` | composite; final form **7th–8th c. CE** or later | modern digital | |

Neofiti, Targum Jonathan to the Prophets, the Fragment Targums and the Writings targums are **missing** — an agent is running on them.

## Deuterocanon — `deuterocanon/`

| Item | Witness | Edition |
|---|---|---|
| `OpenHebrewBible/` | Leningrad **1008 CE** lineage | modern |

The deuterocanonical books themselves (Tobit, Judith, Wisdom, Sirach, Baruch, 1–2 Maccabees, additions to Daniel and Esther) are **already inside the Rahlfs LXX**. Composed **c. 300–100 BCE**. Held as scripture by Catholics and Orthodox; removed by Protestants at the Reformation, **1520s–1640s**.

## Pseudepigrapha — `pseudepigrapha/` (43 XML texts)

| Text | Composed | Surviving witness | Note |
|---|---|---|---|
| **1 Enoch** | **c. 300–100 BCE** (Book of Watchers earliest, c. 300 BCE) | Aramaic fragments at Qumran **c. 200–50 BCE**; complete only in Ge'ez, MSS **15th–18th c.** | Quoted as prophecy in **Jude 14–15**; canonical in Ethiopia |
| **Jubilees** | **c. 160–150 BCE** | Hebrew fragments at Qumran; complete only in Ge'ez | Ethiopian canon |
| **4 Ezra** | **c. 90–100 CE** | Latin, Syriac, Ge'ez, Armenian | |
| **2 Baruch** | **c. 100–130 CE** | Syriac (one MS, 6th–7th c.) | |
| **3 & 4 Maccabees** | **1st c. BCE – 1st c. CE** | in LXX MSS | |
| **Psalms of Solomon** | **c. 60–40 BCE** | Greek MSS | |
| **Sibylline Oracles** | **2nd c. BCE – 7th c. CE** (layered) | Greek | Composite over ~900 years |
| **Letter of Aristeas** | **c. 150–100 BCE** | Greek | The LXX origin story |
| Testaments of Abraham / Adam / Job / Solomon, Joseph & Aseneth, Life of Adam and Eve | **1st–5th c. CE** | various | |

Edition: **Online Critical Pseudepigrapha**, modern digital (**2000s–present**), original languages.

## Coptic / Gnostic — `nag-hammadi/corpora/` (2.5 GB)

| Text | Composed | Witness | Note |
|---|---|---|---|
| **Gospel of Thomas** (NH II,2) | **c. 60–140 CE**, heavily contested | Nag Hammadi codex **c. 350 CE**; Greek fragments P.Oxy 1, 654, 655 **c. 200 CE** | 114 sayings, no narrative |
| **Pistis Sophia** | **3rd–4th c. CE** | Askew Codex, **4th c.** | |
| Acts of Pilate / Gospel of Nicodemus | **4th–5th c. CE** | Coptic MSS | |
| Coptic OT/NT — Sahidic & Bohairic | translated **3rd–4th c. CE** | MSS **4th c. onward** | Very early versional witnesses |

Edition: **Coptic SCRIPTORIUM**, modern digital (**2013–present**).

## Apostolic Fathers — `apostolic-fathers/First1KGreek/` (523 MB)

| Text | Composed | Note |
|---|---|---|
| **Didache** | **c. 50–120 CE** | Possibly older than parts of the NT |
| **1 Clement** | **c. 95–97 CE** | |
| **2 Clement** | **c. 140–160 CE** | Not by the same author |
| **Ignatius**, 7 genuine letters | **c. 108–140 CE** | Later forged expansions exist — check which recension |
| **Polycarp**, Philippians | **c. 110–140 CE** | |
| **Shepherd of Hermas** | **c. 90–150 CE** | **Bound into Codex Sinaiticus** |
| **Epistle of Barnabas** | **c. 70–135 CE** | **Bound into Codex Sinaiticus** |
| **Philo** | **c. 20 BCE – 50 CE** | |
| **Eusebius**, *Historia Ecclesiastica* | c. 313–325 CE | Greek, `data/tlg2018/tlg002/` — **III.25 is the disputed-books list** |

> ⚠️ **Josephus is NOT in First1KGreek**, despite INDEX.md claiming it. Verified 2026-08-08: no `tlg0526` directory exists. Philo (`tlg0018`) is present; Josephus is not. Still needed if wanted — *Against Apion* I.37–43 carries his 22-book canon count.

Barnabas and Hermas being physically bound into Sinaiticus (**c. 330–360 CE**) means that scribe, in that place, treated them as scripture. The canon was not closed when that book was made.

Edition: **First1KGreek / Open Greek and Latin**, modern digital (**2015–present**), largely re-keyed from 19th-c. printed editions.

## Samaritan Pentateuch — `samaritan/sp/` (619 MB)

| Witness | Edition |
|---|---|
| **MS Dublin Chester Beatty 751** (Gen 1 – Deut 32:36), **12th–13th c. CE**; **MS Garizim 1** (Deut 32:36b–34) | DT-UCPH Text-Fabric, Samaritanus project (Schorch, Halle-Wittenberg), **2010s–present** |

Diverges from the Masoretic text in **~6,000 places**, and where it disagrees it sometimes sides with the Septuagint against the Hebrew. A genuinely independent line of transmission — the Samaritan and Jewish traditions split no later than the **2nd c. BCE**.

## Ethiopic / Ge'ez — `ethiopic/ethiopian-bible/` — **36 of 81 books**

| Text | Composed | Ge'ez translation | Note |
|---|---|---|---|
| **1 Enoch** | c. 300–100 BCE | **4th–6th c. CE** | Complete **only** in Ge'ez — best witness on earth |
| **Jubilees** | c. 160–150 BCE | 4th–6th c. CE | Complete **only** in Ge'ez |
| **Meqabyan I & III** | uncertain, likely **1st millennium CE** | — | Unrelated to Greek Maccabees; in no other canon |
| **Kebra Nagast** | assembled **c. 1320 CE** | — | |
| Sinodos, Didascalia, Mysteries of Heaven and Earth, Synaxarium, Testament of our Lord | **4th–14th c. CE** | — | |

Edition: **Beta Masaheft** (Universität Hamburg), modern digital, CC BY-SA.
Missing: 2 Meqabyan, Psalms, Jeremiah, Ezekiel, Daniel, most Minor Prophets, the entire NT, and books 37–81.

## NT Apocrypha — `nt-apocrypha/` (OCR'd scans)

| Edition | Edition date | Contains | Composed |
|---|---|---|---|
| Tischendorf, *Evangelia Apocrypha* | **1853, 2nd ed. 1876** | Protevangelium of James, Infancy Gospel of Thomas, Acts of Pilate, Descent into Hell, Pseudo-Matthew | **2nd–6th c. CE** (Protevangelium mid-2nd c.) |
| Tischendorf, *Apocalypses Apocryphae* | **1866** | Apocalypse of Peter, Apocalypse of Paul, Apocalypse of John, Assumption of Moses | **2nd–5th c. CE** (Apoc. Peter c. 100–150) |
| Lipsius–Bonnet, *Acta Apostolorum Apocrypha* | **1891–1903** | Acts of Peter, Paul, John, Andrew, Thomas | **2nd–3rd c. CE** |

All three editions are **post-1820**. Their pre-1820 predecessor is **Fabricius, _Codex Apocryphus Novi Testamenti_ (Hamburg 1703, 2nd ed. 1719)** — an agent is running on it.

---

## Summary — the age gap on disk

| | Oldest witness available | Edition on disk |
|---|---|---|
| Hebrew OT | Dead Sea Scrolls, **c. 250 BCE – 68 CE** (*not on disk*) | Leningrad **1008 CE**, edited **2008+** |
| Greek NT | P52, **c. 125–175 CE**; Sinaiticus/Vaticanus **c. 300–360 CE** | eclectic reconstructions, **1904–2018** |
| Greek OT | Vaticanus **c. 300–325 CE** | Rahlfs **1935**, Swete **1887–94** |
| Samaritan Torah | MS Chester Beatty 751, **12th–13th c.** | **2010s** |

**No autographs survive.** Nothing written by an original author exists anywhere on earth. Every item above is either a copy of a copy, or a modern editor's argument about what those copies collectively point back to.

The single largest gap in the corpus is the top-left cell: the **Dead Sea Scrolls**, the oldest biblical text in existence, are not on disk. An agent is running on what's obtainable.

---

## Disk

**15 GB free, 94% used** (2026-08-08). The corpus is 6.9 GB. Adding the pre-1820 scans is realistic; mirroring manuscript image archives is not — Codex Sinaiticus images alone run to tens of GB.
