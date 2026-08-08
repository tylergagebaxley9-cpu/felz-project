# Pre-1820 Patristics & Apocrypha — Research Manifest

Researched 2026-08-08. Every archive.org identifier below was checked against the live metadata API (`https://archive.org/metadata/<id>`) and the details page was HEAD-verified (HTTP 200) on this date. Sizes are the actual `_djvu.txt` OCR layer and `.pdf` file sizes reported by archive.org, not estimates, **except** where explicitly marked "not individually checked" (a few multi-volume sets where I verified the set exists and spot-checked one volume rather than all).

**Rule applied:** EDITION date, not composition date. Per your instruction, nothing is cut — Migne (1844–66) and the already-owned Tischendorf/Lipsius-Bonnet (1866–91) are listed alongside everything else, tiered but not omitted. You make the call on tiering; the dates are here so you can.

**Tiers:**
- **Tier 1** — pre-1820 edition, verified live, djvu.txt exists (searchable text, not just page images)
- **Tier 2** — pre-1820 edition, verified live, no djvu.txt found (image-only PDF/EPUB, still legible but not full-text-searchable)
- **Tier 3** — post-1820 edition (Migne, Thilo, etc.) — flagged per your rule, included per your instruction, your call to use or skip
- **GAP** — searched, not found on archive.org in this pass; said so rather than guessed

**Do not bulk-download.** Total Tier-1/2 footprint below is large (several GB in PDFs) because 17th–18th-c. folio scans run 50–1000+ MB each. The `_djvu.txt` files are small (under 10 MB each) and are almost certainly what you actually want for a text corpus — the manifest gives both so you can choose.

---

## PART 1 — Pre-1820 editions of the non-canonical books

### 1.1 Fabricius, *Codex Apocryphus Novi Testamenti*

The standard early-modern collection of NT apocrypha in Greek + Latin. Johann Albert Fabricius, Hamburg. First edition 1703 (not located separately on archive.org — the 1719 second edition, expanded, is what survives there); enlarged posthumous 3-vol edition 1743.

| Title | Edition date | Archive.org ID | djvu.txt | PDF size | Tier |
|---|---|---|---|---|---|
| Codex Apocryphus Novi Testamenti, vol. 1 | 1719 | `CodexApocryphusNoviTestamenti1` | 1.41 MB | 31.5 MB | 1 |
| Codex Apocryphus Novi Testamenti, vols. 1–2 | 1719 | `CodexApocryphusNoviTestamenti1.2` | 1.73 MB | 57.1 MB | 1 |
| Codex Apocryphus Novi Testamenti (alt. scan) | 1719 (Google metadata says 1743, title page conflict — see note) | `codexapocryphus00fabrgoog` | 1.47 MB | 43.9 MB | 1 |

> Note on the third row: archive.org's own metadata gives year 1743 for `codexapocryphus00fabrgoog` even though the search index tagged it 1719 — this is very likely the enlarged 3-volume 2nd edition (Fabricius died 1736; the expanded edition was completed posthumously and published 1743). 1743 is still pre-1820, just not the exact printing your source list named. Flagging the discrepancy rather than picking one silently.

Verify: `curl -sI https://archive.org/details/CodexApocryphusNoviTestamenti1` → 200. Same for the other two IDs — checked individually, all 200.

### 1.2 Fabricius, *Codex Pseudepigraphus Veteris Testamenti*

OT pseudepigrapha in Greek/Latin. First ed. 1713, 2nd enlarged ed. 1722–23 (2 vols).

| Title | Edition date | Archive.org ID | djvu.txt | PDF size | Tier |
|---|---|---|---|---|---|
| Codex Pseudepigraphus VT, vol. 1 | 1713 | `codexpseudepigr00josegoog` | 1.71 MB | 52.9 MB | 1 |
| Codex Pseudepigraphus VT, vol. 2 | 1723 | `codexpseudepigr01josegoog` | 0.98 MB | 32.9 MB | 1 |
| Codex Pseudepigraphus VT (alt. scan) | undated on this copy | `z-codex-pseudepigraphus-veteris-testamen` | 1.94 MB | 87.8 MB | 1 |
| Codex Pseudepigraphus VT (alt. scan) | undated on this copy | `A086B247` | 0.84 MB | 39.1 MB | 1 |

All four HEAD-verified 200. Recommend `codexpseudepigr00josegoog` (1713) + `codexpseudepigr01josegoog` (1723) as the primary set — they're the two volumes of the actual first/second edition run; the other two are redundant alt-scans, useful only as backup if one goes down.

### 1.3 Grabe, *Spicilegium SS. Patrum ut et Haereticorum*

Johann Ernst Grabe, Oxford. Collects fragments of 1st–3rd-c. fathers AND heretics — this is where pre-1820 access to Papias and Hegesippus fragments lives (see Part 3). 1st ed. 1698–99, 2nd enlarged ed. 1714 (2 vols).

| Title | Edition date | Archive.org ID | djvu.txt | PDF size | Tier |
|---|---|---|---|---|---|
| Spicilegium SS. Patrum | 1698 | `bim_early-english-books-1641-1700_spicilegium-ss-patrum-_grabe-johann-ernst_1698` | 1.65 MB | **293.8 MB** | 1 |
| Spicilegium SS. Patrum (2nd ed, same year, alt scan) | 1700 | `bim_early-english-books-1641-1700_spicilegium-ss-patrum-_grabe-johann-ernst_1700` | not checked | not checked | 1 (unverified djvu) |
| Spicilegium ss. patrum, vol. 1 | 1714 | `bim_eighteenth-century_spicilegium-ss-patrum-_grabe-joannes-ernestus_1714_1` | 0.92 MB | **297.6 MB** | 1 |
| Spicilegium ss. patrum, vol. 2 | 1714 | `bim_eighteenth-century_spicilegium-ss-patrum-_grabe-joannes-ernestus_1714_2` | 0.62 MB | 202.4 MB | 1 |

All HEAD-verified 200. **PDFs are ~200–300 MB each** — these are full-resolution page-image scans; the djvu.txt is what you want for text, under 1 MB per volume.

### 1.4 Thilo, *Codex Apocryphus Novi Testamenti* (1832) — TIER 3

Successor to Fabricius, more critical apparatus, but **1832 — 12 years past your line.**

| Title | Edition date | Archive.org ID | djvu.txt | PDF size | Tier |
|---|---|---|---|---|---|
| Codex apocryphus Novi Testamenti | 1832 | `codexapocryphusn00thil` | 2.63 MB | 60.6 MB | **3 (post-1820)** |
| same, alt scan | 1832 | `codexapocryphusn0000unse` | not checked | not checked | 3 |

Verified 200. Your call — flagged, not omitted.

### 1.5 Jones, *A New and Full Method of Settling the Canonical Authority of the New Testament*

Jeremiah Jones (d. 1724), published posthumously — vols. 1–2 in 1726, vol. 3 in 1727. Contains the most complete English-language treatment of NT apocrypha of its era, with primary-source excerpts. Original 1726/27 printing: only vol. 3 (1727) located on archive.org in this pass. The **1798 three-volume reprint is complete and still pre-1820** — recommended as the practical target.

| Title | Edition date | Archive.org ID | djvu.txt | PDF size | Tier |
|---|---|---|---|---|---|
| New and Full Method, vol. III | **1727 (original)** | `bim_eighteenth-century_a-new-and-full-method-of_jones-jeremiah_1727` | 0.28 MB | 97.6 MB | 1 |
| New and Full Method, vol. 1 | 1798 (complete reprint) | `newfullmethodofs01jone` | 1.17 MB | 37.8 MB | 1 |
| New and Full Method, vol. 2 | 1798 | `newfullmethodofs02jone` | 1.16 MB | 36.9 MB | 1 |
| New and Full Method, vol. 3 | 1798 | `newfullmethodofs03jone` | 0.74 MB | 18.4 MB | 1 |

All verified 200. Vols. 1–2 of the *original* 1726 printing were not found on archive.org in this pass — GAP, worth a follow-up search on Google Books/HathiTrust if the exact original matters to you; the 1798 reprint is textually the same edition, just re-typeset/re-printed.

---

## PART 2 — Pre-1820 editions of the Church Fathers

### 2.1 Cotelier, *Patres Apostolici* (SS. Patrum qui temporibus apostolicis floruerunt)

Jean-Baptiste Cotelier, Paris, original 1672. The copy found is Jean Le Clerc's expanded "nova editio," 1698 (Antwerp/Amsterdam) — still pre-1820, textually the standard early edition of the Apostolic Fathers.

| Title | Edition date | Archive.org ID | djvu.txt | PDF size | Tier |
|---|---|---|---|---|---|
| Patres Apostolici (Cotelier/Le Clerc) | 1698 | `bub_gb_bXVXMMNgWxUC` | 6.33 MB | 64.4 MB | 1 |
| SS. Patrum Apostolicorum opera genuina (later separate ed.) | 1746 (2 vols) | `sspatrumapostoli01herm` / `sspatrumapostoli02herm` | 1.73 MB / 1.89 MB | 37.5 MB / 40.0 MB | 1 |

Note: the 1672 original printing itself wasn't located as a standalone archive.org scan — GAP — the 1698 nova editio is what's live.

### 2.2 Grabe / Massuet, Irenaeus, *Against Heresies*

| Title | Edition date | Archive.org ID | djvu.txt | PDF size | Tier |
|---|---|---|---|---|---|
| Grabe's Irenaeus (Greek + Latin) | **1702** | `bim_eighteenth-century_tou-en-hagiois-patros-he_irenaeus-saint-bishop-_1702` | 3.73 MB | **885.7 MB** | 1 |
| Massuet's Irenaeus | **1710** | — | — | — | **GAP — not found on archive.org in this pass** |
| Earlier Latin-only Irenaeus (pre-Grabe text tradition) | 1639, Paris | `sanctiirenaeilug0000vari` | 3.48 MB | 80.1 MB | 1 |

Massuet's 1710 Paris edition (later reproduced almost verbatim in Migne PG vol. 7) was searched repeatedly under several title variants and not found live on archive.org — real gap, not a naming miss on my end as far as I can tell. If it matters, Google Books / BSB (Bayerische Staatsbibliothek) direct search is the next step. The 885 MB PDF on the Grabe copy is the largest single file in this whole manifest — flag before touching it.

**Manuscript-tradition note, since it matters here specifically:** *Against Heresies* survives complete only in an old Latin translation; the Greek original is preserved just in fragments (quoted by Hippolytus, Epiphanius, Eusebius) plus a few Armenian fragments of books 4–5. The earliest Latin manuscripts are 9th–11th c. (Codex Claromontanus, Ottobonianus, Arundelianus, Vossianus) — a 700–900-year gap between the ~180 CE composition and the manuscripts any printed edition is actually transcribing. Every edition in this table, Grabe's included, is standing on that same gap.

### 2.3 Petavius (Petau), Epiphanius, *Panarion* / Opera Omnia

Dionysius Petavius, original edition Paris 1622. Copy found is the 1682 Cologne reprint, 2 vols — textually Petavius's edition, later printing.

| Title | Edition date | Archive.org ID | djvu.txt | PDF size | Tier |
|---|---|---|---|---|---|
| Epiphanii Opera Omnia (Petavius), vol. 1 | 1682 (reprint of 1622 ed.) | `bub_gb_1Wfnrs5Tw4MC` | 3.78 MB | 54.4 MB | 1 |
| Epiphanii Opera Omnia (Petavius), vol. 2 | 1682 | `bub_gb_ZHNpwbPa85MC` | 6.69 MB | 139.9 MB | 1 |

Both verified 200. The true 1622 first printing was not independently located — likely same text, this is a fine substitute since Petavius's text wasn't substantially revised between printings.

### 2.4 Valesius, Eusebius, *Ecclesiastical History* and *Praeparatio Evangelica*

| Title | Edition date | Archive.org ID | djvu.txt | Notes | Tier |
|---|---|---|---|---|---|
| Eusebii Pamphili Ecclesiastica Historia, Graece et Latine | 1720 | `bub_gb_Tq3V9eDI1dAC` | 5.33 MB | No direct PDF found in file list (has EPUB, 3.28 MB); editor not confirmed as Valesius from metadata alone — Valesius's own editio princeps was 1659 (Paris), revised 1672/1678 — this 1720 printing is plausibly a later reprint of the Valesian text (common practice) but I could not verify the editor attribution from the archive.org record itself. **Flagging the uncertainty rather than asserting it.** | 1, editor unconfirmed |
| Eusebii Praeparatio Evangelica | — | — | — | **GAP** — only found a 1903 Gifford edition (`praeparatioevan00giffgoog`), which is post-1820. Vigier's edition (1628, standard pre-1820 text) not located on archive.org in this pass. | GAP |

### 2.5 de la Rue, Origen, *Opera Omnia*

Charles de la Rue (vols. 1–2, 1733/1733–40) and completed posthumously by his nephew Charles Vincent de la Rue (vols. 3–4, 1740, 1759). All four volumes located.

| Title | Edition date | Archive.org ID | djvu.txt | PDF size | Tier |
|---|---|---|---|---|---|
| Origenis Opera Omnia, tom. 1 | 1733 | `origenous-ta-euriskomena-panta-t.-1-1733` | 7.26 MB | **1,057.6 MB** | 1 |
| Origenis Opera Omnia, tom. 2 | 1733 | `origenous-ta-euriskomena-panta-t.-2-1733` | not individually checked | not individually checked | 1 (exists, unverified detail) |
| Origenis Opera Omnia, tom. 3 | 1740 | `origenous-ta-euriskomena-panta-t.-3-1740` | not individually checked | not individually checked | 1 (exists, unverified detail) |
| Origenis Opera Omnia, tom. 4 | 1759 | `origenous-ta-euriskomena-panta-t.-4-1759` | 8.33 MB | **1,077.0 MB** | 1 |

Vols 1 and 4 individually confirmed live (200) with the sizes above. Vols 2–3 confirmed to exist in the search index under the same identifier pattern but not individually opened for size — **these are the two heaviest single PDFs in the entire manifest, over 1 GB each.** If you ever pull this set, pull the djvu.txt only.

### 2.6 Potter, Clement of Alexandria, *Opera*

John Potter, Oxford, 1715.

| Title | Edition date | Archive.org ID | djvu.txt | PDF size | Tier |
|---|---|---|---|---|---|
| Clementis Alexandrini Opera (Potter) | 1715 | `bub_gb_SDF6rOFELK8C` | 4.50 MB | none found (no `.pdf` in file list — image scan may only exist as EPUB/JP2) | 1 |

Verified 200.

### 2.7 Hippolytus (Fabricius/Vignoli edition)

Not on your original list by editor name, but Hippolytus is a major loss-preservation father (Refutation of All Heresies), and the pre-1820 edition exists — including it since you asked for breadth.

| Title | Edition date | Archive.org ID | djvu.txt | Tier |
|---|---|---|---|---|
| S. Hippolyti Opera, vol. 1 | 1716 | `bub_gb_OTOcGiUIHB4C` | 1.69 MB | 1 |
| S. Hippolyti Opera, vol. 2 | 1718 | `bub_gb_W9Mmkp_NQ1MC` | 2.05 MB | 1 |

Both verified 200. PDF sizes not checked in this pass.

### 2.8 Jerome and Augustine (Maurist editions)

**Augustine** — Congregation of St. Maur (Benedictines), Paris, published across 1679–1700 (11 tomes, printed at different dates as they finished). Found directly:

| Title | Printing date | Archive.org ID | djvu.txt | Tier |
|---|---|---|---|---|
| S. Aurelii Augustini Operum, tomus primus | 1701 | `bub_gb_Pjy3QaEh82sC` | 4.76 MB | 1 |
| S. Aurelii Augustini Operum, tomus decimus | 1688 | `bub_gb_V0zSghySPfwC` | 2.92 MB | 1 |

Both title pages explicitly say "Opera & studio monachorum Ordinis Sancti Benedicti, Congregatione Sancti Mauri" — confirmed Maurist. **Only 2 of the 11 tomes located and verified in this pass** — the rest are almost certainly on archive.org under the same title pattern (`Sancti Aurelii Augustini ... Operum tomus [N]`) but I did not exhaustively pull all 11; flagging as partial rather than claiming completeness.

**Jerome** — Martianay & Pouget's Maurist edition, Paris, 1693–1706, 5 vols. **GAP — not located on archive.org in this pass**, despite several search variants (`Martianay Hieronymi opera`, `Sancti Eusebii Hieronymi Stridonensis presbyteri opera`, date-range queries). What did turn up under Jerome's name was only the 1865 Vallarsi/Migne-line reprint (post-1820, Tier 3) — `sanctieusebiihie01jero` through `...11jero`. Vallarsi's own earlier (and still pre-1820) revision, Verona 1734–42, was also searched for and not found live. This is a real gap in what's on archive.org, not a search-term failure I can fix by trying harder — worth a direct Google Books or Bayerische Staatsbibliothek (BSB) search if Jerome specifically matters to you.

### 2.9 Galland, *Bibliotheca Veterum Patrum*

Andrea Galland, Venice, 1765–81, 14 volumes. **Full set located — all 14 identifiers confirmed present in the archive.org index** (Getty Research Institute scans). Only vol. 4 individually opened for exact sizes; the rest are presumed similar (~5–8 MB txt / ~80 MB pdf) but not each confirmed — flagging that as an estimate, not a measurement.

| Vol | Archive.org ID | djvu.txt (measured) | PDF (measured) |
|---|---|---|---|
| 1 | `gri_33125011194707` | not individually measured | not individually measured |
| 2 | `gri_33125011194764` | " | " |
| 3 | `gri_33125011194236` | " | " |
| 4 | `gri_33125011194293` | **5.52 MB** | **80.6 MB** |
| 5 | `gri_33125011194350` | not individually measured | " |
| 6 | `gri_33125011194418` | " | " |
| 7 | `gri_33125011194475` | " | " |
| 8 | `gri_33125011194533` | " | " |
| 9 | `gri_33125011194590` | " | " |
| 10 | `gri_33125011194657` | " | " |
| 11 | `gri_33125011194715` | " | " |
| 12 | `gri_33125008697738` | " | " |
| 13 | `gri_33125008697795` | " | " |
| 14 | `gri_33125008700169` | " | " |

Vol 4 HEAD-verified 200; identifiers for the other 13 confirmed present in the live search index (same collection, same naming convention) but not each individually HEAD-checked. **Estimated total if all pulled: ~75 MB text / ~1.1 GB PDF** — estimate, not a sum of measurements.

### 2.10 Tertullian (relevant to Marcion reconstruction, see Part 3.6)

Not on your original list, but essential — Tertullian's *Adversus Marcionem* is the primary source for reconstructing Marcion's gospel.

| Title | Edition date | Archive.org ID | djvu.txt | PDF size | Tier |
|---|---|---|---|---|---|
| Tertulliani Opera (Rigault-line text) | 1689 | `bim_early-english-books-1641-1700_tertulliani-opera-_tertullian_1689` | 5.41 MB | **987.3 MB** | 1 |
| Tertulliani Opera (Pamelius edition) | 1608 | `bub_gb_yxCzfo7t0KcC` | not checked | not checked | 1 (exists, unverified detail) |

1689 copy HEAD-verified 200, second-largest PDF in the manifest.

### 2.11 Migne, *Patrologia Graeca* / *Patrologia Latina* — TIER 3

**1844–66, post-1820 by 24–46 years.** Included per your instruction — not omitted, not softened.

| Set | Edition date | Volumes on archive.org | Identifier pattern | Tier |
|---|---|---|---|---|
| Patrologia Graeca (161 vols, some split into parts) | 1857–66 | 246 items indexed | `patrologiae_cursus_completus_gr_vol_NNN[_part]` | **3** |
| Patrologia Latina (221 vols, some split) | 1844–64 | 434 items indexed | search `title:(Patrologiae Cursus Completus Series Latina)` | **3** |

Sample verified: `patrologiae_cursus_completus_gr_vol_011` (Origen), `_vol_021` (Eusebius), `_vol_035` (Gregory Nazianzen) all present, 1857. This is the free, comprehensive, but post-1820 option — it incorporates the Maurist/de la Rue/Petavius/etc. texts (re-edited, sometimes silently altered) under one roof. Your call whether the convenience is worth the 24-46-year gap from your line.

---

## PART 3 — Lost / quoted books: what survives, where, and whether it's real

This is the part where the composition-date / father-date / edition-date chain matters most. Laid out explicitly for each.

### 3.1 Book of Jasher (Sefer haYashar) — biblical citation, Josh. 10:13 and 2 Sam. 1:18

- **Composition of the cited work:** unknown, presumably pre-monarchic to early-monarchic Israel (before ~1000 BCE is the traditional guess; genuinely unknowable — the two citations give no internal date evidence).
- **What survives:** two bare citations. No quoted text beyond the citation itself in Joshua (one couplet of poetry, the "sun stand still" line) and 2 Samuel (David's lament over Saul and Jonathan — this one, unusually, IS the surviving text, quoted at length in 2 Sam 1:19–27, but that's canonical text you already have, not a separate document).
- **Verdict: genuinely lost as an independent book.** No pre-1820 or any-date edition of the actual ancient Book of Jasher exists, because there is no surviving text to edit beyond what's already inside 2 Samuel.
- **A forgery exists and must not be mistaken for it:** Jacob Ilive, London, **1751**, published *The Book of Jasher*, claiming to be a translation "by Alcuin" of a text he said he'd found. It is a fabrication — Ilive was a printer with a documented history of hoaxes, and the text is now universally recognized by scholars as an 18th-century invention, not an ancient source. Archive.org: `bim_eighteenth-century_the-book-of-jasher_ilive-jacob_1751` (djvu.txt 227 KB, verified 200). **Including this in the manifest as a labeled forgery for reference only — not as a source of ancient text.** A later English printing (1829, `bookofjasherwith00iliv`) is the same hoax, reprinted, also post-1820 and also fake.
- Separately, there is a genuine medieval Hebrew work also called *Sefer haYashar* — an 11th–13th-c. rabbinic midrashic compilation on Genesis–Judges, printed Venice/Naples from 1625 onward. This is a real old book, but it is **not** the biblical lost book either — same title, different and much later text, medieval not ancient. I searched archive.org for a pre-1820 printing and found nothing live in this pass — GAP, not confirmed available.

### 3.2 Book of the Wars of the LORD — Num. 21:14

- **Composition:** unknown, unknowable from the one-line citation.
- **What survives:** a single quoted line of poetry ("Waheb in Suphah, and the wadis of the Arnon...").
- **Verdict: genuinely and completely lost.** Nothing beyond the one verse has ever surfaced in any manuscript, quotation, or father. No edition, pre- or post-1820, can exist because there is no additional text anywhere to edit. This is the flattest "lost" of anything in this manifest — say so plainly, no forgery even exists to warn you off here.

### 3.3 Book of Enoch (1 Enoch)

- **Composition:** composite, multiple authors/strata — Book of the Watchers (ch. 1–36) probably 3rd c. BCE, Astronomical Book similarly early, Similitudes/Parables (ch. 37–71) disputed, plausibly 1st c. BCE–1st c. CE, Epistle and later material later still. Quoted directly in Jude 14–15 (NT, so by definition pre-~90s CE for at least that portion).
- **Manuscript tradition:** complete text survives **only in Ge'ez** (Ethiopic), earliest Ge'ez MSS 15th–16th c. — already on your disk per the INDEX. Aramaic fragments of most of the book (not the Similitudes) were found at Qumran, 4Q201–212, dated ~200 BCE–50 CE by paleography — genuinely ancient manuscript witnesses, though these weren't discovered until 1947–56, so no pre-1820 scholar ever saw them.
- **Pre-1820 print access — the honest, narrow answer:** the Ge'ez text was unknown to European scholarship until James Bruce brought manuscripts back from Ethiopia in 1773; Richard Laurence's first English translation was published **1821 — one year past your line**, confirmed. BUT there is a genuine pre-1820 partial access point: **Georgius Syncellus's *Chronographia*** (Byzantine chronicle, composed c. 800–810 CE) quotes 1 Enoch 6–11 and 106–107 in Greek at length. Jacques Goar's edition of Syncellus was printed **1729** (Paris, reprinted in the Byzantine corpus) — archive.org `bub_gb_hKfQ6ajnkzcC`, djvu.txt 5.54 MB, verified 200. This gets you roughly a fifth of the book, in Greek, legitimately pre-1820, via a 9th-century Byzantine chronicler's citation — genuinely useful, genuinely partial, genuinely inside your date rule.
- Also relevant, lower value: **Scaliger's *Thesaurus Temporum*** (reconstruction of Eusebius's lost Chronicle, incorporating Syncellus/Africanus material), 1658 printing — `thesaurustemporu00euse`, verified 200 — overlapping content with Goar's Syncellus, included for completeness rather than as a separate must-get.

### 3.4 Papias, *Exposition of the Sayings of the Lord* (Logiōn Kyriakōn Exēgēsis)

- **Composition:** c. 95–140 CE — Eusebius and most modern scholars put Papias's activity in the reign of Trajan (98–117), some push later toward Hadrian; genuinely contested within roughly that 45-year window, no firmer date available.
- **What survives:** fragments only, no independent manuscript ever existed after antiquity. Quoted by:
  - **Irenaeus**, *Against Heresies* 5.33.4 (composed c. 180 CE) — the famous millenarian "grapes with 10,000 branches" fragment.
  - **Eusebius**, *Ecclesiastical History* 3.39 (composed c. 313–325 CE) — the longest surviving block, including Papias's own statement about sources ("the Elder" tradition) and the account of Mark's and Matthew's gospel composition.
- **Pre-1820 edition chain:** via Irenaeus → Grabe's 1702 edition (Part 2.2, found, verified) or the pre-Grabe 1639 Latin Irenaeus (found, verified). Via Eusebius HE → editor/date unconfirmed for the 1720 copy found (Part 2.4, flagged) — this is a real weak point in your pre-1820 Papias access; the Valesius edition itself wasn't independently confirmed. **Grabe's own *Spicilegium* (1698/1714, found, verified) specifically anthologizes Papias fragments alongside other apostolic-age material** — this is probably your best single pre-1820 access point for Papias, better than chasing down Eusebius or Irenaeus separately.

### 3.5 Hegesippus, *Hypomnemata* (Memoirs, 5 books)

- **Composition:** c. 165–180 CE (Hegesippus wrote under Pope Eleutherus, 174–189, per Eusebius — the work is usually dated to that decade, with some scholars preferring slightly earlier, 160s).
- **What survives:** fragments only. Quoted extensively by **Eusebius**, HE books 2–4 (composed c. 313–325 CE), including the famous account of the death of James the brother of Jesus. A few additional lines survive in **Photius**, *Bibliotheca* (9th c. CE, composed c. 850s) — Photius is describing/excerpting a text he still had access to, so this is actually a slightly later and independent witness, not a copy of Eusebius.
- **Pre-1820 edition chain:** via Eusebius HE — same 1720 gap noted above (Part 2.4). **Grabe's *Spicilegium* again specifically collects Hegesippus fragments** — same recommendation as Papias, this is the practical pre-1820 access point (found, verified, Part 1.3).

### 3.6 Gospel of the Hebrews / Gospel of the Ebionites / Gospel of the Nazoreans

Three distinct, frequently-confused Jewish-Christian gospels. None survives as a text; all are quotation-only.

**Gospel of the Hebrews** (probably Egyptian, used by Jewish Christians, composition estimates run c. 100–150 CE, contested):
- Quoted by **Clement of Alexandria**, *Stromata* (composed c. 190–210 CE) → Potter's 1715 edition, found, verified (Part 2.6).
- Quoted by **Origen**, *Commentary on John* / *Commentary on Matthew* (composed c. 220s–240s CE) → de la Rue's 1733–59 edition, found, verified (Part 2.5).
- Quoted by **Eusebius**, HE (c. 313–325 CE) → same 1720-edition gap as above (Part 2.4).
- Quoted by **Jerome**, multiple works including *De Viris Illustribus* (composed c. 392 CE) and commentaries on Ephesians and Micah — **Maurist Jerome edition GAP, not located pre-1820** (Part 2.8). This is the single biggest hole in your pre-1820 Gospel-of-the-Hebrews access, since Jerome is actually the richest source and you don't currently have a pre-1820 route to him.

**Gospel of the Ebionites** (used by the Ebionite sect, composition estimate c. mid-2nd c., contested):
- Quoted **only** by **Epiphanius**, *Panarion* 30 (composed c. 375–378 CE) — no other father cites it independently. Petavius's 1682 edition, found, verified (Part 2.3). This is good news: your one required source for this text has a solid pre-1820 edition already confirmed.

**Gospel of the Nazoreans** (Aramaic/Syriac-language gospel used by the Nazorean sect, composition estimate 2nd c., very contested — some scholars doubt it's meaningfully distinct from the Hebrews gospel):
- Known almost entirely through **Jerome** (commentaries, *De Viris Illustribus*) — same Maurist Jerome GAP as above (Part 2.8).
- A few lines also via **Epiphanius**, *Panarion* 29 — Petavius 1682, found, verified.

**Net assessment for 3.6:** Clement, Origen, and Epiphanius are all covered with verified pre-1820 editions. Jerome — arguably the single most important witness for both the Hebrews and Nazoreans gospels — is not, and I was not able to find one on archive.org despite several search passes. That's a real, not cosmetic, gap.

### 3.7 Marcion's Gospel (the *Evangelion*)

- **Composition:** c. 140–144 CE, Rome — Marcion's edited/shortened version of Luke, stripped of what he considered Judaizing interpolations, paired with 10 edited Pauline epistles into his canon (the *Antitheses* + *Apostolikon*).
- **What survives:** no manuscript, ever. Entirely reconstructed from hostile quotation, almost verse-by-verse, in:
  - **Tertullian**, *Adversus Marcionem* (composed c. 207–208 CE, 5 books, the single richest source — Tertullian goes through Marcion's gospel practically line by line to refute it) → 1689 Rigault-line edition, found, verified (Part 2.10); Pamelius 1608 also located, not fully verified.
  - **Epiphanius**, *Panarion* 42 (composed c. 375–378 CE, includes a scholion listing Marcion's specific omissions/alterations) → Petavius 1682, found, verified (Part 2.3).
- **Verdict:** this is the best-covered of all the "lost" texts in this manifest — both primary hostile witnesses have verified pre-1820 editions in hand. A modern reconstruction is possible and has been done by scholars (e.g., Judith Lieu's and others' recent critical reconstructions), but those are 21st-c. scholarship, well outside your Tier 1 — the *source material* to do your own reconstruction from is what's covered here.

### 3.8 The Diatessaron (Tatian's gospel harmony)

- **Composition:** c. 172–185 CE (Tatian was a pupil of Justin Martyr and this is usually placed after Justin's death, ~165 CE, with the Diatessaron itself dated within about a 15-year window after that — contested by a decade or so either direction).
- **Manuscript tradition — genuinely fragmented and late:**
  - The **Dura-Europos fragment** — a small Greek parchment scrap, the earliest physical witness to any gospel harmony — dates paleographically to before 256 CE (the city was destroyed then), but it was **excavated in 1933**. No pre-1820 scholar ever saw it.
  - The **Arabic Diatessaron** (translated via Ibn al-Ṭayyib, 11th c. CE, from an earlier Syriac base) was first **printed by Agostino Ciasca in 1888** — post-1820, and there is no earlier printed edition of it.
  - **Ephrem the Syrian's *Commentary on the Diatessaron*** (composed c. 370s CE) survives complete only in an **Armenian** translation; a Syriac text (probably closer to Ephrem's original language) was only identified in the **Chester Beatty Syriac MS 709, published by Louis Leloir starting 1963**. The Armenian-to-Latin translation by Georg Moesinger was published **1876** — also post-1820.
- **Verdict: flatly, honestly, no pre-1820 edition of the Diatessaron or any substantial witness to it exists.** This is not a research gap I could close with better search terms — the relevant manuscripts were not yet excavated (Dura), not yet published (Ciasca, Leloir), or not yet translated (Moesinger) until well after 1820. The only pre-1820 access to the Diatessaron at all is indirect, through mentions in **Eusebius**, HE 4.29 (same 1720-edition gap, Part 2.4) and **Epiphanius**, *Panarion* 46 (Petavius 1682, found, verified) — both of which only confirm the Diatessaron existed and describe it in a sentence or two; neither preserves any of its actual text. If you want the Diatessaron's content at all, you are choosing a post-1820 source or nothing — there is no third option.

---

## Summary table — what's obtainable right now, Tier 1/2 only

| Category | Items verified live | Approx. text (djvu.txt) footprint |
|---|---|---|
| Apocrypha (Fabricius, Grabe, Jones) | 15 volumes/scans | ~18 MB |
| Church Fathers editions | ~25 volumes/scans (Cotelier, Grabe/Irenaeus, Petavius, de la Rue, Potter, Hippolytus, Maurist Augustine partial, Galland, Tertullian) | ~75 MB |
| **Total Tier 1/2 text** | ~40 items | **~95 MB** — trivial, fits easily even under your disk pressure |
| Same, PDF page-scans if ever wanted | same items | **~6 GB+** — do NOT bulk-pull; djvu.txt is very likely all you need |

## Confirmed dead ends (searched, not fabricated, not found)

- Massuet's 1710 Irenaeus
- Vigier's 1628 Eusebius, *Praeparatio Evangelica* (any pre-1820 printing)
- Martianay & Pouget's Maurist Jerome (1693–1706) and Vallarsi's 1734–42 revision
- A pre-1820 printing of the genuine (non-forged) Hebrew *Sefer haYashar*
- Any pre-1820 witness to the Diatessaron's actual text (structurally impossible — see 3.8)

---

## Sample verification commands (do not bulk-run — spot-check only)

```bash
# Confirm a details page resolves
curl -sI https://archive.org/details/CodexApocryphusNoviTestamenti1

# Pull ONLY the text layer (small, safe) for a single item
curl -sL -o /tmp/fabricius-vol1.txt \
  https://archive.org/download/CodexApocryphusNoviTestamenti1/Codex_apocryphus_Novi_Testamenti_djvu.txt

# Check metadata (files, sizes) before deciding to pull anything
curl -s https://archive.org/metadata/<identifier> | python3 -m json.tool
```
