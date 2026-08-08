# Excluded books — what is on this disk and not in a modern Bible

**Priority index.** Everything here was counted or opened on 2026-08-08. Sizes and
chapter counts are from the files themselves, not from a catalogue.

Four categories, in descending order of how completely we hold them:

1. **HELD COMPLETE** — full text on disk, original language
2. **HELD PARTIAL** — some of it on disk
3. **OBTAINABLE** — located and verified, not yet pulled
4. **LOST** — survives only in quotation, or not at all

---

## 1 · HELD COMPLETE

### Unique to the Ethiopian canon — in no other Bible on earth

Ge'ez text, `ethiopic/ethiopian-bible/public/data/chapters/<book>/<ch>.json`.
**All 11 complete.** 1,076 chapter files total across the collection.

| Book | Ge'ez | Chapters | Note |
|---|---|---:|---|
| **1 Enoch** (ሄኖክ) | `1En` | **108/108** | Quoted as prophecy in **Jude 14–15**. Survives complete only in Ge'ez. Aramaic fragments at Qumran. |
| **Jubilees** (መጽሐፈ ኩፋሌ) | `Jub` | **50/50** | Found at Qumran in Hebrew. Complete only here. |
| **Kebra Nagast** | `KN` | 119/119 | The Ark-to-Ethiopia narrative. Assembled c. 1320 CE. |
| **Testament of Our Lord** | `TestLd` | 60/60 | |
| **Sinodos** | `Sinod` | 36/36 | |
| **3 Meqabyan** | `3Meq` | 21 files | Ethiopian Maccabees — **unrelated to the Greek Maccabees**, in no other canon |
| **4 Baruch** | `4Bar` | 9/9 | |
| **Mysteries of Heaven & Earth** | `MysHE` | 7 files | |
| **Lefafa Sedq** | `Lef` | 7/7 | |
| **Teaching of Mysteries** | `Teach` | 5/5 | |
| **Synaxarion** | `Synax` | 1/1 | |

Also in the Ethiopian canon and held complete: **1 Meqabyan** (36/36),
**Apocalypse of Ezra** (10/10), **Clement** (67/67).

### Pseudepigrapha — 39 texts, original languages

`pseudepigrapha/Online-Critical-Pseudepigrapha/static/docs/*.xml`
*(the directory also holds ~50 timestamped drafts and test files — the 39 below are the real texts)*

| Text | Size | Composed | Note |
|---|---:|---|---|
| **Sibylline Oracles** | 885 KB | 2nd c. BCE – 7th c. CE | layered over ~900 years |
| **Testament of Job** | 964 KB | 1st c. BCE – 1st c. CE | |
| **1 Enoch** | 644 KB | c. 300–100 BCE | Greek/Ge'ez witnesses |
| **Psalms of Solomon** | 552 KB | c. 60–40 BCE | in some LXX manuscripts |
| **2 Baruch** (+ Syriac) | 436+427 KB | c. 100–130 CE | |
| **4 Ezra** | 391 KB | c. 90–100 CE | |
| **Letter of Aristeas** | 222 KB | c. 150–100 BCE | the LXX origin story |
| **Testament of Abraham** (A/B/composite) | 193+127+67 KB | 1st–2nd c. CE | |
| **Jubilees** (2 recensions) | 192+144 KB | c. 160–150 BCE | |
| **4 Maccabees** | 179 KB | 1st c. CE | |
| **Testament of Solomon** | 150 KB | 1st–3rd c. CE | |
| **Life of Adam and Eve** | 134 KB | 1st–5th c. CE | |
| **Joseph and Aseneth** | 134 KB | 1st c. BCE – 2nd c. CE | |
| **Ezekiel the Tragedian** | 128 KB | 2nd c. BCE | a Greek verse drama on the Exodus |
| Lives of the Prophets · History of the Rechabites · Apocryphon of Ezekiel · 3 Baruch · Aristobulus · Artapanus · Eupolemus · Ps-Eupolemus · Theodotus · Philo the Epic Poet · Testament of Adam · Esdras A/B · 4Q548 · Visions of Amram · Eldad & Modad · Cleodemus Malchus | | | |

> ⚠️ `3Macc.xml` is **0 KB** — an empty file. 3 Maccabees is *not* held here.
> It is in the Rahlfs LXX at `septuagint/`.

### Apostolic Fathers — Greek

`apostolic-fathers/First1KGreek/` — 311 author directories.

| Text | Composed | Note |
|---|---|---|
| **Didache** | c. 50–120 CE | possibly older than parts of the NT |
| **Epistle of Barnabas** | c. 70–135 CE | **bound into Codex Sinaiticus** |
| **Shepherd of Hermas** | c. 90–150 CE | **bound into Codex Sinaiticus** |
| 1 Clement | c. 95–97 CE | |
| 2 Clement | c. 140–160 CE | different author |
| Ignatius (7 genuine letters) | c. 108–140 CE | later forged expansions exist — check recension |
| Polycarp, *Philippians* | c. 110–140 CE | |
| **Eusebius, *Historia Ecclesiastica*** | c. 313–325 CE | III.25 = the disputed-books list. Translated: `translations/eusebius-HE-3.25.md` |

> **Eusebius names four of these as candidates** — Hermas, Barnabas, the Didache, and the
> Apocalypse of Peter. Two of them are physically bound into the oldest complete Bible
> we possess, copied within decades of his writing.

### Deuterocanon — inside the LXX

`septuagint/LXX-Rahlfs-1935/` carries **15 standalone books** plus Greek additions to
Esther and Psalm 151: Tobit · Judith · Wisdom · Sirach · Baruch · Epistle of Jeremiah ·
Susanna · Bel and the Dragon · 1–4 Maccabees · 1 Esdras · Psalms of Solomon · Odes.

**3 Maccabees, 4 Maccabees and Psalms of Solomon are not even in the Catholic canon.**
All were in Greek Bibles. Removed from Protestant Bibles by the **British and Foreign
Bible Society resolution of 8 May 1826** — primary text located, see
`docs/RESEARCH-canon-formation.md`.

### Gnostic — original Coptic

`nag-hammadi/corpora/` (2.5 GB, Coptic SCRIPTORIUM)

| Text | Composed | Witness |
|---|---|---|
| **Gospel of Thomas** | c. 60–140 CE *(contested)* | Nag Hammadi codex c. 350 CE; Greek fragments P.Oxy 1, 654, 655 (c. 200 CE) |
| **Pistis Sophia** | 3rd–4th c. CE | Askew Codex |
| Acts of Pilate / Gospel of Nicodemus | 4th–5th c. CE | |
| Book of Bartholomew, Mysteries of John | | |

### NT Apocrypha — Greek/Latin critical editions

`nt-apocrypha/` — OCR'd scans, post-1820 editions (Tischendorf 1853/1866, Lipsius–Bonnet 1891):
**Protevangelium of James** · Infancy Gospel of Thomas · Acts of Pilate · Descent into Hell ·
Pseudo-Matthew · **Apocalypse of Peter** · Apocalypse of Paul · Assumption of Moses ·
**Acts of Peter, Paul, John, Andrew, Thomas**.

Pre-1820 predecessor now also on disk: **Fabricius, *Codex Apocryphus Novi Testamenti*
(1703/1719)** in `early-editions/scans/`.

---

## 2 · HELD PARTIAL

| Item | Have | Missing |
|---|---|---|
| **Ethiopian canon** | 36 books | books 37–81 — only manuscript facsimiles exist (Beta Masaheft / EMML). **2 Meqabyan** is not in the open reader. |
| **Nag Hammadi** | 5 tractates | the other 47 — Brill's *Coptic Gnostic Library* holds the complete Coptic, copyrighted |
| **Targums** | 35 books | **Targum Neofiti** — Vatican MS forbids reproduction; Díez Macho's edition copyrighted |

---

## 3 · OBTAINABLE — verified, not yet pulled

| Item | Where | Note |
|---|---|---|
| **Mandaean Book of John** (Drasha d-Yahya) | `archive.org/details/mandaeanbookofjohn` | **Mandaic text facing English**, Häberl & McGrath. De Gruyter permits free non-commercial sharing — verified from the PDF's own statement. The only surviving Gnostic religion; they revere **John the Baptist**. |
| **Qolasta** (Mandaean liturgy) | Digital Library of India scans | main IA copy is lending-gated; DLI scans are open |
| **Haran Gawaita** | alternate IA scan | same pattern |
| Lidzbarski, *Mandäische Liturgien* (1920) | archive.org | fully public domain |
| **Memar Marqah** (Samaritan, 4th c.) | Heidenheim, *Bibliotheca Samaritana* v3 | editio princeps, confirmed by grepping the OCR |
| Samaritan Asatir · Abu'l-Fath Chronicle · Samaritan Book of Joshua · Defter | archive.org | all open |
| **Ephrem, *Commentary on the Diatessaron*** | Chester Beatty MS 709, live IIIF manifest | **the actual Syriac manuscript, c. 500 CE, 82 pages, full resolution** |
| **Old Syriac Gospels** — Sinaitic Palimpsest, Curetonian | Lewis 1910, Burkitt 1904, Cureton 1858 | older than the Peshitta NT |
| Dura-Europos Diatessaron fragment | Kraeling 1935, unrestricted microform mirror | c. 250 CE, the only original-language physical witness |

**Gap:** **Ginza Rabba** — the main Mandaean scripture. Lidzbarski 1925 is a German
*translation*; Petermann's 1867 Mandaic-script edition was not found digitized.

---

## 4 · LOST — quotation only, or gone

| Book | What survives |
|---|---|
| **Book of the Wars of the LORD** | **one line** (Num 21:14). Nothing else ever existed to edit. |
| **Book of Jasher** | two bare citations (Josh 10:13, 2 Sam 1:18). ⚠️ The printed "Book of Jasher" (1751, Jacob Ilive) is a **confirmed 18th-century forgery** — it is not the cited book. |
| **Diatessaron** (Tatian, c. 160–175) | **Tatian's own words are not recoverable in any language.** Best evidence: Dura fragment (c. 250 CE) and Ephrem's commentary. The Arabic, Latin and Middle Dutch harmonies actively disagree with each other. |
| **Gospel of the Hebrews / Ebionites / Nazoreans** | fragments quoted by Jerome and Epiphanius. Eusebius names the Gospel according to the Hebrews as still circulating. |
| **Marcion's Gospel** | reconstructable only from Tertullian's rebuttal — best-covered of the lost gospels |
| **Papias**, *Exposition of the Sayings of the Lord* (c. 95–120) | fragments, via Eusebius and Grabe's *Spicilegium* (1698/1714) |
| **Hegesippus**, *Memoirs* | fragments, same route |
| Book of the Acts of Solomon · Chronicles of the Kings of Israel/Judah · Book of Nathan · Book of Gad the Seer · Prophecy of Ahijah · Visions of Iddo | named inside the OT; **no text survives** |

---

## How to read any of this

```bash
./tools/allwitness.py Deut 32 8        # one passage, every witness, dated
./tools/dssread.py Deut 32 8           # Dead Sea Scrolls
./tools/cntr_read.py 01 41 16 1 20     # Mark 16 in Sinaiticus
```

`allwitness.py` reports **ABSENT** when a manuscript is present but the verse is not.
That silence is evidence, and it is the whole point of holding the witnesses side by side.
