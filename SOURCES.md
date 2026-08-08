# Sources — every link needed to rebuild the corpus

This repository holds **tools and findings, not texts**. The corpus is ~9.5 GB and
every source is already published upstream, so mirroring it would duplicate the data
and fork away from upstream corrections.

Everything below is linked with its **licence stated**, so you can decide what to take.

## Quick start

```bash
git clone https://github.com/tylergagebaxley9-cpu/felz-project.git
cd felz-project
./fetch.sh                    # 27 git sources, pinned to exact commits in corpus.lock
python3 tools/pull_texts.py   # 246 archive.org text layers (~730 MB)
python3 tools/pull_targums.py # 35 targum books via the Sefaria API
```

Then any finding in `HIGHLIGHTS.md` is reproducible:

```bash
./tools/allwitness.py Ps 145 13     # the missing nun verse
./tools/allwitness.py Deut 32 8     # sons of God / sons of Israel
./tools/diverge.py --all            # systematic DSS vs Masoretic scan
./tools/diverge_lxx.py              # Masoretic vs Septuagint, Psalms
```

Disk: ~9.5 GB for everything. The **text-only tier is under 1 GB** and carries every
finding in `HIGHLIGHTS.md` — see "Minimal set" at the bottom.

---

## ⚠️ Restricted — linked, deliberately not redistributed

These are **excluded from this repository on purpose.** `fetch.sh` will pull the
NC-licensed ones because personal research use is permitted; the copyrighted ones it
will not touch. Read the terms before you use either commercially.

| Source | Licence | Link |
|---|---|---|
| **ETCBC Dead Sea Scrolls** (Abegg transcriptions) | **CC BY-NC 4.0** — non-commercial | https://github.com/ETCBC/dss |
| **Codex Sinaiticus** transcription | **CC BY-NC-SA 3.0** — non-commercial | https://github.com/itsee-birmingham/codex-sinaiticus · https://codexsinaiticus.org |
| Coptic SCRIPTORIUM, PROIEL/Syntacticus treebanks | CC BY-NC-SA | https://github.com/CopticScriptorium/corpora |
| **NA28 / Nestle-Aland 28** | **© Deutsche Bibelgesellschaft** — not free | https://www.die-bibel.de — buy it |
| **BHS / BHQ apparatus** | © Deutsche Bibelgesellschaft | https://www.die-bibel.de |
| **DJD** Dead Sea Scrolls official transcriptions | © Oxford University Press | — |
| **Brill *Coptic Gnostic Library*** (complete Nag Hammadi Coptic) | © Brill | https://brill.com |
| **Codex Tchacos / Gospel of Judas** | © Maecenas Foundation | — |
| **Targum Neofiti** | Vatican MS forbids reproduction; Díez Macho ed. © | — |
| Stuttgart Vulgate · Vetus Latina Database · Leiden Armenian Textbase | © | — |
| **Mechon Mamre** (closest Aleppo Codex proxy) | private study only, **no republication** | https://www.mechon-mamre.org |

> If you keep the NC items, put them in an `NC-LICENSED/` subtree so they never get
> bundled into anything you sell.

---

## Hebrew / Aramaic Old Testament

| Source | Witness | Licence | Link |
|---|---|---|---|
| **morphhb** — Westminster Leningrad Codex + full morphology + Strong's | Leningrad Codex **1008 CE** | CC BY 4.0 | https://github.com/openscriptures/morphhb |
| **unfoldingWord Hebrew Bible** (UHB) | Leningrad 1008 CE | CC BY-SA 4.0 | https://git.door43.org/unfoldingWord/hbo_uhb |
| **STEPBible TAHOT** — Tyndale House tagged Hebrew OT | Leningrad 1008 CE | CC BY 4.0 | https://github.com/STEPBible/STEPBible-Data |
| **Samaritan Pentateuch** (DT-UCPH Text-Fabric) | MS Chester Beatty 751, **12th–13th c.** | free for research | https://github.com/DT-UCPH/sp |
| **Dead Sea Scrolls** — see Restricted above | **c. 250 BCE – 68 CE** | CC BY-NC 4.0 | https://github.com/ETCBC/dss |

## Greek New Testament

| Source | Kind | Licence | Link |
|---|---|---|---|
| **CNTR transcriptions** — P1–P141 **plus** Vaticanus, Alexandrinus, Ephraemi, Bezae, Washingtonianus | ORIGINAL manuscripts | CC BY-SA 4.0 | https://github.com/Center-for-New-Testament-Restoration/transcriptions |
| **Codex Bezae** TEI | ORIGINAL, c. 400 CE | CC BY 4.0 | https://github.com/itsee-birmingham/codex-bezae |
| **Codex Zacynthius** | ORIGINAL, 6th c. palimpsest | CC BY 4.0 | https://github.com/itsee-birmingham/codex-zacynthius-xml |
| **SBLGNT** | EDITED, 2010 | free (custom) | https://github.com/LogosBible/SBLGNT |
| **Nestle 1904** + syntax trees | EDITED, 1904 | public domain | https://github.com/biblicalhumanities/Nestle1904 |
| **Byzantine Majority** (Robinson–Pierpont) | EDITED | public domain | https://github.com/byztxt/byzantine-majority-text |
| **unfoldingWord Greek NT** | EDITED | CC BY-SA | https://git.door43.org/unfoldingWord/el-x-koine_ugnt |
| **Textus Receptus** (Stephanus 1550) | PRINTED 1550 | public domain | https://github.com/byztxt/greektext-textus-receptus |
| **Elzevir 1633** | PRINTED 1633 | public domain | https://github.com/byztxt/greektext-elzevir |
| **Scrivener** | reconstructs the TR | public domain | https://github.com/byztxt/greektext-scrivener |

**IGNTP diplomatic transcriptions** (Vaticanus John complete; Alexandrinus, Washingtonianus partial; Paul's epistles) — CC BY 4.0 — https://itseeweb.cal.bham.ac.uk/iohannes/transcriptions/index.html

**Free ECM apparatus for Acts only** (the one open carve-out in NA28's apparatus) — https://ntvmr.uni-muenster.de

## Septuagint

| Source | Rests on | Licence | Link |
|---|---|---|---|
| **Rahlfs 1935** + apparatus, morphology, glosses | mainly Vaticanus **c. 300–325 CE** | free | https://github.com/eliranwong/LXX-Rahlfs-1935 |
| **Swete** | Vaticanus | public domain | https://github.com/sleeptillseven/LXX-Swete |
| GreekResources (lexical/morphological) | — | free | https://github.com/openscriptures/GreekResources |

> ⚠️ The LXX is a **TRANSLATION** (c. 250–100 BCE). Older than every surviving Hebrew
> manuscript except the scrolls, and the version the NT usually quotes — but a
> translation. See `PROVENANCE.md`.

## Excluded books — the ones not in a modern Bible

| Source | Contains | Licence | Link |
|---|---|---|---|
| **Ethiopian Bible** (Beta Masaheft, Univ. Hamburg) | **1 Enoch 108/108 · Jubilees 50/50 · Kebra Nagast · 3 Meqabyan · 1 Meqabyan** — 36 books, 1,076 chapters, Ge'ez with word-level transliteration | CC BY-SA 4.0 | https://github.com/LPettay/ethiopian-bible · https://betamasaheft.eu |
| **Online Critical Pseudepigrapha** | 39 texts: Sibylline Oracles, Testament of Job, Psalms of Solomon, 4 Ezra, 2 Baruch, Letter of Aristeas, Ezekiel the Tragedian | free | https://github.com/OnlineCriticalPseudepigrapha/Online-Critical-Pseudepigrapha |
| **First1KGreek** | **Didache, Barnabas, Shepherd of Hermas**, 1–2 Clement, Ignatius, Polycarp, **Eusebius HE**, Philo | CC BY-SA | https://github.com/OpenGreekAndLatin/First1KGreek |
| **Coptic SCRIPTORIUM** | **Gospel of Thomas**, Pistis Sophia, Coptic OT/NT | CC BY-NC-SA | https://github.com/CopticScriptorium/corpora |
| Peshitta OT · Syriac NT | ETCBC Text-Fabric | free | https://github.com/ETCBC/peshitta · https://github.com/ETCBC/syrnt |
| Targums | Sefaria API — `tools/pull_targums.py` | public domain | https://www.sefaria.org/api/texts/ |

## Verified but not yet pulled

| Item | Why it matters | Link |
|---|---|---|
| **Mandaean Book of John** | Scripture of the only surviving Gnostic religion; they revere **John the Baptist**. **Mandaic facing English.** De Gruyter permits free non-commercial sharing (stated in the PDF) | https://archive.org/details/mandaeanbookofjohn |
| **Ephrem, *Commentary on the Diatessaron*** | The actual Syriac manuscript, **Chester Beatty MS 709, c. 500 CE**, 82 pages, live IIIF | https://chesterbeatty.ie |
| **Hebrew Ben Sira** — all 8 witnesses | Genizah A–F, **Masada c. 100–75 BCE**, Qumran 2Q18 + 11QPsa | https://bensira.org |
| Old Syriac Gospels — Sinaitic Palimpsest, Curetonian | Older than the Peshitta NT | Lewis 1910 · Burkitt 1904 · Cureton 1858, on archive.org |
| Hittite suzerainty treaties CTH 51, CTH 62 | The structural template of Deuteronomy | https://www.hethport.uni-wuerzburg.de |
| Ugaritic corpus (KTU) — **the 70 sons of El** | The framework behind Deut 32:8's *benei elohim* | https://github.com/DT-UCPH/cuc (CC BY-NC 4.0) |

## Pre-1820 printed editions

`docs/PULLABLE.tsv` lists **95 items / 246 files**, all HEAD-verified. `tools/pull_texts.py`
pulls every one (~730 MB of OCR text layers).

Includes: **Walton's London Polyglot 1657** (8 languages parallel) · **Complutensian
1514–17** · **Antwerp 1568–73** · **Bomberg / ben Chayyim 1524–25** (the standard Hebrew
text for 400 years) · **Kennicott 1776–80** and **de Rossi 1784–88** (600+ Hebrew MSS
collated — the free pre-1820 answer to the copyrighted BHS apparatus) · **Holmes &
Parsons 1798–1827** (largest LXX apparatus ever assembled) · **Sixtine LXX 1587** ·
**Grabe LXX 1707–20** · **Erasmus 1516** · Beza 1565/1598 · **Fabricius,
*Codex Apocryphus NT* 1703/19**.

> ⚠️ **These are OCR text layers and the Greek and Hebrew OCR is poor.** Measured: Acts
> 2:27 came out of the Erasmus layer as `ὅτὶ Ὀυὰ τγκαταλείψας`, and the facing **Latin**
> column was OCR'd through a **Greek** model. Usable for Latin prose and apparatus
> reference numbers. **Not** a translation base — use the clean digital Textus Receptus
> and Elzevir repos above instead.

## Manuscript images — free, not mirrored

Codex Sinaiticus https://codexsinaiticus.org · Vaticanus https://digi.vatlib.it ·
Alexandrinus (British Library) · Dead Sea Scrolls https://deadseascrolls.org.il ·
NT Virtual MS Room https://ntvmr.uni-muenster.de · CSNTM https://csntm.org ·
Oxyrhynchus https://papyri.info · Aleppo Codex https://aleppocodex.org ·
Sefaria https://www.sefaria.org

> **The Aleppo Codex (c. 930 CE)** — the best Masoretic manuscript — has **no
> machine-readable transcription anywhere.** Page images only, from every source. This
> is the largest genuine hole in the corpus.

---

## Minimal set — every finding, under 1 GB

If you only want to reproduce `HIGHLIGHTS.md`:

```bash
git clone --depth 1 https://github.com/ETCBC/dss.git dead-sea-scrolls/etcbc-dss
git clone --depth 1 https://github.com/openscriptures/morphhb.git hebrew-ot/morphhb
git clone --depth 1 https://github.com/eliranwong/LXX-Rahlfs-1935.git septuagint/LXX-Rahlfs-1935
git clone --depth 1 https://github.com/Center-for-New-Testament-Restoration/transcriptions.git papyri/cntr-transcriptions
git clone --depth 1 https://github.com/biblicalhumanities/Nestle1904.git greek-nt/Nestle1904
git clone --depth 1 https://github.com/LPettay/ethiopian-bible.git ethiopic/ethiopian-bible
git clone --depth 1 https://github.com/OpenGreekAndLatin/First1KGreek.git apostolic-fathers/First1KGreek
python3 tools/pull_targums.py
```

That gives you: the missing nun verse (11Q5), Deut 32:8 in 4Q37, the Comma Johanneum's
absence, Mark 16:9–20's absence, Jude's quotation of 1 Enoch, Eusebius's canon list,
and both divergence scans.

**Sinaiticus adds 79 MB** — needed only for the Mark 16 and 1 John 5:7 checks, and it
is the CC BY-NC-SA item, so take it knowingly.
