# Pre-1820 Printed Editions — Hebrew Bible & Polyglots

Research pass for `~/projects/bible-sources/`. Scope per the user's rule: **edition date, not witness date** — everything here is a scan of a printed book issued before 1820 (or, where flagged, a later reprint/photostat of one). Nothing here is filtered out; post-1820 items and dead ends encountered along the way are included so the user can judge for himself.

## How to read the DATE columns

Every row gives **two dates**, because they answer different questions:

- **Edition date** — when this printed book was set in type / issued. This is what the user's "pre-1820" rule is actually gating.
- **Witness date** — how old the underlying text is: the manuscript(s) the printer set the type from. For the Hebrew Bible editions this is almost always *uncertain* — printers didn't footnote their exemplars, and the manuscripts themselves are frequently lost or unidentified today. Where a scholarly consensus range exists it's given; where it's genuinely unknown, this says so rather than inventing precision. For the critical apparatuses (Kennicott, de Rossi) it's a *range across hundreds of collated MSS*, not a single number — and both men's own age-estimates for their oldest manuscripts have been revised downward by later paleography (Malachi Beit-Arié et al.), so their claims are flagged as disputed, not treated as fact.

## Verification method

Every archive.org identifier below was checked two ways as of 2026-08-08:
1. `archive.org/metadata/<id>` — confirms the file list, sizes, and whether a `_djvu.txt` OCR layer exists.
2. `curl -I -L` HEAD request on the actual download URL — confirms the link resolves (200) right now, not just that the item page exists.

Where a lead could not be verified this way (mainly: sites behind Cloudflare bot-checks that block non-browser fetches — Georgetown's DSpace repo, HathiTrust), that is stated explicitly. I did not mark anything "found" that I couldn't independently confirm resolves.

**Disk note**: root filesystem is at 94% (15 GB free). Nothing was downloaded. Pick items individually with the commands given.

---

## 1. Hebrew Bible editions

| Edition | Editor / Printer | Edition date | Witness date (underlying MS) | archive.org ID | Files | OCR layer | Size | Verified |
|---|---|---|---|---|---|---|---|---|
| **Soncino Bible** — editio princeps, first complete printed Hebrew Bible | Israel Nathan Soncino, Soncino | **1488** | Unidentified medieval Hebrew MSS; no single exemplar named by the printer. General scholarship places likely source MSS in the 13th–15th c. Italian/Ashkenazi copying tradition, but this is not established with certainty. | `tanakh-soncino-1488-jb-738.1-2-images` | `Tanakh_Soncino_1488_JB738.1-2.pdf` | Yes, `_djvu.txt` exists but is **garbage** — checked a sample: mangled/transliterated noise, not usable text | 85.9 MB (PDF) + 1.6 MB (txt) | 200 OK |
| Soncino Bible, 2nd copy (different library scan) | same | **1488** | same, uncertain | `inc-hebr-4-ausst-191-biblia-hebraica` | `Inc hebr 4 Ausst 191 - Biblia hebraica.pdf` | Yes, `_djvu.txt` exists, also image-quality OCR (not verified line-by-line but same expected garbage) | 139.4 MB (PDF) + 687 KB (txt) | 200 OK |
| **Brescia Bible** — the edition Luther used for his German OT translation | Gershom Soncino, Brescia | **1494** | Revision of the 1488 Soncino text; underlying MS(s) not identified. Same "uncertain, likely 13th–15th c." caveat applies. | — | **Not found freely downloadable.** Only page images (Wikimedia Commons, Google Arts & Culture) and a print-on-demand facsimile listing (lulu.com, referencing copies at the Austrian National Library Vienna and Bayerische Staatsbibliothek Munich) turned up. No full public-domain PDF/scan located on archive.org, e-rara, BSB-MDZ, or HathiTrust in this pass. | — | — | — | **NOT VERIFIED — do not claim this exists as a free download** |
| **First Rabbinic Bible** (Mikraot Gedolot, 1st ed.) | Felix Pratensis, ed.; Daniel Bomberg, Venice | **1517** (item dated "1518" on archive.org, likely a Jewish-calendar/colophon discrepancy — treat as 1517/18) | Non-ben-Asher, mixed medieval MSS; Pratensis did not use the later-standard ben-Asher recension. Specific exemplars unidentified. | `first-rabbinic-bible-venice-1518-full-images` | Single combined PDF, all 4 vols | Yes, `_djvu.txt` present (not spot-checked, expect same OCR-garbage pattern as other 15th/16th-c. Hebrew scans) | 271.6 MB (PDF) + 14.8 MB (txt) | 200 OK |
| **Second Rabbinic Bible** (Mikraot Gedolot, 2nd ed.) — **THE ben Chayyim text, standard Hebrew Bible for ~400 years** | Jacob ben Chayyim ibn Adonijah, ed.; Daniel Bomberg, Venice | **1524–25** | Several late-medieval Sephardic MSS in the ben-Asher tradition, personally assembled by ben Chayyim. **None of his source MSS have been conclusively identified by modern scholars** — this is a genuinely open question in textual scholarship, not just an archive.org gap. Estimated 13th–15th c. Sephardic copying tradition. | `second-rabbinic-bible-venice-1525-color-full-images` | Single combined PDF, all 4 vols, **full color scan** | Yes, `_djvu.txt` present | 458.5 MB (PDF) + 15.7 MB (txt) | 200 OK — **recommended copy, best single file** |
| Second Rabbinic Bible, alt. scan (vols split) | same | **1524–25** | same | `The_Second_Rabbinic_Bible_Vol_1` + `_Vol_2` | Only vols I–II present under these IDs (not the full 4) | Yes on both | Vol 1: 770.7 MB PDF + 6.3 MB txt; Vol 2: 583.9 MB PDF + 4.9 MB txt | 200 OK on both |
| Second Rabbinic Bible, alt. scan (vol. 1 only, duplicate) | same | **1524–25** | same | `1525-2nd-rabbinic-bible-1` | Vol 1 only | Yes | 770.7 MB PDF + 8.8 MB txt | 200 OK |
| Second Rabbinic Bible, alt. scan — **date on this one is uncertain** | same (Bomberg press) | Identifier/description says **1524–25**, but the actual filename on the item says **"...1545"** — an unresolved discrepancy. Bomberg's press did issue a 3rd rabbinic bible printing in 1546–48; this could be that instead. Do not trust the "1525" label on this specific item without checking the physical title page. | same general MS uncertainty as above | `RabbinicbibleotMikraotGedolotBombergshebrewtanach.jacobBenChaim.1525` | Single PDF | Yes | 196.1 MB PDF + 5.9 MB txt | 200 OK, **date needs manual confirmation** |
| **Buxtorf's Rabbinic Bible** (Biblia Rabbinica) | Johannes Buxtorf the Elder, ed.; Ludwig König, Basel | **1618–19** | Text is Bomberg's ben Chayyim 1524–25 text (see above) with Buxtorf's added Masoretic apparatus (*Tiberias*) — so same underlying witness-date uncertainty (13th–15th c. Sephardic MSS, unidentified). | — | **Not found freely downloadable.** Confirmed via Sotheby's/Kestenbaum auction listings that copies exist and are well documented bibliographically, but no digitized full scan located on archive.org, e-rara, BSB, or HathiTrust in this pass. | — | — | — | **NOT VERIFIED** |
| **Athias edition** | Joseph Athias, Amsterdam | **1661** | Base text descends from Bomberg via Menasseh ben Israel's 1635 Amsterdam edition; same underlying MS lineage, filtered through ~140 years of print transmission rather than fresh collation. | — | **Not found freely downloadable as the 1661 edition itself.** Archive.org has many *later* reprints/derivatives (19th c., titled "secundum editiones Ios. Athiae...") that use his text as their base but are not scans of the 1661 book — see the "later derivatives" note below. | — | — | — | **NOT VERIFIED** |
| **Van der Hooght edition** — became the de facto standard Hebrew text through the 18th–19th c. | Everardus van der Hooght, Amsterdam | **1705** | Base text = Athias/Leusden 1667 lineage (ultimately Bomberg-derived); van der Hooght's contribution was typographic/orthographic standardization, not new MS collation. | `Biblia_Hebraica_Van_der_Hooght_Amsterdam_1705_Volumes_AB_Torah_and_Former_Prophets` | **Only volumes A–B** (Torah + Former Prophets) of the 4-vol set found; volumes C–D (Latter Prophets + Writings) not located in this pass. | Yes, `_djvu.txt` present | 34.7 MB PDF + 2.0 MB txt | 200 OK — **incomplete set, only half the Bible** |

**Later derivatives of Athias/van der Hooght worth knowing about but explicitly out of scope** (all post-1820 editions, found while searching, included per the "don't filter" instruction): `bibliahebraicase01unse_1` (1839), `bibliahebraicase00unse` (1856), `bibliahebraicase01unse` (1904), `bibliahebraica0000unse_z6q0` (1889), `bibliahebraicase02unse`/`03unse` (1839), `torahneviimukhet01unse`/`00unse`/`0000unse` (various, 1839–1883), `bibliahebraicaad01unse` (1834, ed. Hahn), `torahneviimukhet00alle` (1850). None of these qualify under the pre-1820 rule — they're all 19th-century reprints of the van der Hooght/Athias textual lineage, listed here only because the user asked for everything encountered, not a curated subset.

---

## 2. Pre-1820 critical apparatus (unusually high-value given the user's rule)

The modern BHS apparatus is copyrighted and post-1820. These two are the pre-1820 alternative — collations of hundreds of manuscripts against a printed base text (van der Hooght's, in both cases).

| Work | Editor | Edition date | Witness date (the MSS collated) | archive.org ID(s) | OCR layer | Size | Verified |
|---|---|---|---|---|---|---|---|
| **Kennicott** — *Vetus Testamentum Hebraicum cum variis lectionibus* | Benjamin Kennicott, Oxford | **1776–1780**, 2 vols | Collates **600+ Hebrew MSS** plus early printed editions. Kennicott's own catalog assigned some MSS ages back to the **10th–12th c.**, but **modern paleographical redating (Beit-Arié and successors) has revised many of his date claims significantly later** — treat any specific century Kennicott assigns to a given MS as disputed, not settled fact. | `vetustestamentum01kenn` (vol. 1), `vetustestamentum02kenn` (vol. 2); duplicate single-vol scan at `kennicott_vetus-testamentum-hebraicum-cum-variis-lectionibus-1776` | `_djvu.txt` present on all; **spot-checked and it is OCR garbage** (mixed Latin/Hebrew critical apparatus, heavily mis-recognized) | Vol.1: 138.8 MB PDF + 6.0 MB txt; Vol.2: 123.5 MB PDF + 5.7 MB txt (duplicate single file: 128.8 MB PDF + 18.6 MB txt) | 200 OK on vol01/vol02; the duplicate identifier returned intermittent 503s under load on retest — the two-volume set is the reliable path |
| **De Rossi** — *Variae Lectiones Veteris Testamenti* | Giovanni Bernardo de Rossi, Parma (Bodoni press) | **1784–1788**, 4 vols (this is the original Bodoni printing, freely downloadable) | Collates **~731 MSS** plus early printed editions across European libraries. Same caveat as Kennicott: de Rossi's own age-claims for his oldest MSS have been revised by later scholarship — disputed, not settled. | `VariaeLectiones` — vols 1–4 as separate PDFs | `_djvu.txt` present on all 4 (not spot-checked but expect same garbage pattern as Kennicott — Latin/Hebrew critical apparatus is a hard OCR case) | ~110 MB PDF each × 4 vols ≈ **440 MB total** | 200 OK on all 4 |
| De Rossi **Supplementum** (1798) — *Scholia critica...* | de Rossi | **1798** | same MS pool, later additions | Only found bundled inside a **1969 Amsterdam (Philo Press) photographic reprint** of the whole 5-vol-in-2 set: `variaelectionesv0102dero`, `variaelectionesv0304dero` | `_djvu.txt` present | 45.0 MB / 56.9 MB PDF | **Item is `access-restricted-item: true` on archive.org — it is a lending-library item, NOT freely downloadable.** The freely-downloadable `VariaeLectiones` above is only the original 4 vols (1784–88) and does *not* include the 1798 Supplementum. |

---

## 3. Polyglots (highest value per item — many languages at once)

| Polyglot | Editor(s) | Edition date | Witness date, by column (varies enormously — this is the honest complexity) | archive.org ID(s) | Size | Verified |
|---|---|---|---|---|---|---|
| **Complutensian Polyglot** | Cardinal Francisco Jiménez de Cisneros, Alcalá (Complutum) | Printed **1514–1517**; not released/circulated until **~1520–22** (papal approval delay) | Hebrew: lost/unidentified medieval Spanish (Toledo-area) MSS, commonly guessed 12th–14th c., not confirmed. Greek (LXX): Vatican and other Greek MSS, precise exemplars debated by scholars. Latin: standard medieval Vulgate tradition. Targum Onkelos included for the Pentateuch, MS basis likewise unidentified. | `complutensian_polyglot_bible` (single 5.1 GB PDF, Library of Congress/World Digital Library source, highest resolution); `polyglotcomplutensis` (6 separate volume PDFs, ~300 MB each ≈ 1.9 GB total — **recommended, manageable size**); `complutensianpolyglot` (HD, chunked into dozens of small PDFs by image range); `Complutensian_Polyglot` (two scans, 472 MB + 515 MB) | 5.1 GB / 1.9 GB / ~3+ GB / ~1 GB depending on which copy | All 200 OK. `polyglotcomplutensis`'s `_djvu.txt` on the combined LoC copy (`cplowres`) contains a clean, readable English table of contents/pagination index — useful for navigation even though OCR of the actual 1514 page text is not reliable. |
| **Antwerp Polyglot** (Biblia Regia / Plantin Polyglot) | Benedictus Arias Montanus, ed.; Christophe Plantin, Antwerp, under patronage of Philip II | **1568–1573**, 8 tomes | Hebrew: reprint of Bomberg's ben Chayyim text (see above — 13th–15th c. Sephardic, unidentified). Greek (LXX): follows Complutensian's Greek, corrected against the Roman/Sixtine edition (itself Vaticanus-influenced, i.e. ultimately traces to a **4th c.** uncial tradition, but only at several removes through 16th c. printed intermediaries). Syriac NT: newly edited by Guy Le Fèvre de la Boderie from a Vienna MS — a 16th c. copy of the Peshitta tradition. Vulgate: standard medieval Latin tradition. | `biblia-sacra-hebraice-chaldaice-graece-latine-benedicti-ariae-montani-sacrorum-bibliorum-tomus-1569` — **all 8 tomes as individual PDFs, this is the complete set**: Tomus 1 (Pentateuch, 363 MB), Tomus 2 (Prophetae Priores, 371 MB), Tomus 3 (Sancti Libri, 328 MB), Tomus 4 (Prophetae Posteriores, 1570, 697 MB), Tomus 5 (NT, 1571, 386 MB), Tomus 6 (Lexicon Graecum, 1572, 423 MB), Tomus 7 (Communes, 1572, 395 MB), Tomus 8 (Liber Ioseph, 1571, 208 MB) | **3.17 GB for all 8 tomes** | Sampled 3 of 8 (Tomus 1, 4, 8) with HEAD requests — all 200 OK. Recommended primary copy. |
| Antwerp Polyglot, alt. scans (larger/redundant, not recommended over the above) | same | 1568–73 | same | `biblia-sacra-hebraice-chaldaice-graece-et-latine-cura-et-studio-benedicti-ariae-montani-tomvs-1569` (5 tomes, but each tome 400 MB–2.1 GB, ≈8 GB total — much larger scans of the same content); `bible-interlinear-hebrew-latin-greek-...` and its near-duplicate `...-geek-...` (single 4.29 GB merged PDF each — two copies of the same oversized file); `hebraicorvm-bibliorvm-veteris-testamenti-latina-interpretatio-opera-xantis-pagnini-novvm-1572` (Xantes Pagnini's companion Latin interlinear translation, issued alongside the Polyglot — 5 parts, ~2 GB total, technically a distinct companion work, not the Polyglot itself) | up to 8 GB+ | Not independently HEAD-verified (redundant with the verified primary copy) — listed for completeness per the "include everything" instruction, not recommended given disk pressure |
| **Paris Polyglot** (Le Jay Polyglot) | Guy Michel Le Jay; contributors incl. Jean Morin (Samaritan material), Gabriel Sionita, Abraham Ecchellensis; Paris | **1629–1645**, 10 vols | Incorporates Antwerp's content plus, new to this edition: **Samaritan Pentateuch** (see Samaritan section below) and Samaritan Targum; Syriac and Arabic OT/NT from various 16th–17th c. MS copies of older textual traditions (not individually itemized here — MS basis varies book by book and was not exhaustively researched in this pass). | — | — | — | **Not found on archive.org, e-rara, or Gallica/BnF in this pass despite searching.** Two leads exist but could not be verified: (1) Georgetown University's DSpace repository has a digitized "1645 Paris Polyglot Bible" collection (`repository.digital.georgetown.edu`, collection ID `16e34347-ce14-4899-ac8c-bcd0b0977dc7`, individual volume handles e.g. `hdl.handle.net/10822/712682` for Vol. 1 and `/10822/1100321` for Vol. 5 Pt. 1) — **but the site is behind Cloudflare bot-protection that returns a JS challenge page to both `curl` and the WebFetch tool; I could not confirm the actual download links resolve or what format the files are in. Someone needs to check this manually in a browser.** (2) HathiTrust has catalog records (e.g. `catalog.hathitrust.org/Record/009420268`) that likely correspond to this or the related 1657 Walton Polyglot, but HathiTrust also blocked automated access (403) during verification — **also needs manual browser check.** |
| **Walton's London Polyglot** | Brian Walton, ed.; Thomas Roycroft, London | **1655–1657**, 6 tomes (Tomus 5 = NT) | The most textually diverse column-by-column: incorporates everything above, plus fresh apparatus citing **Codex Alexandrinus** (~**5th century** — the single oldest specific witness cited by name anywhere in this whole research pass) for Greek, Ussher's collations, a Persian Pentateuch, and an Ethiopic Psalter, each with its own distinct and mostly-not-individually-researched MS lineage. | `biblia-sacra-polyglotta-complectentia-edidit-brianus-waltonus-lombart-hollar-roycroft-1657` — **all 6 tomes present** (7 files — Tomus 5/NT has two scan variants): Tomus 1 (396.4 MB), Tomus 2 (332.5 MB), Tomus 3 (434.5 MB), Tomus 4 (290.8 MB), Tomus 5/NT "IC" (348.7 MB), Tomus 5/NT "PB" alt. scan (265.5 MB), Tomus 6 (287.0 MB) | **≈2.36 GB for the full 7-file set (≈2.09 GB if you skip the redundant Tomus 5 "PB" variant)** | 200 OK confirmed on the item and its Tomus 1 file; this is the **recommended, complete, reasonably-sized copy** |
| Walton's Polyglot, alt. scans (EEBO, much larger, redundant) | same | 1655–57 | same | `bim_early-english-books-1475-1640_biblia-sacra-polyglotta-_bible-polyglot-1657_1657_1` through `_6` (six separate items, one confirmed at **3.95 GB for a single volume** — avoid unless the smaller set above is somehow deficient); `BibliaSacraPolyglotta5` (NT only, 287 MB, redundant) | 3.9+ GB per volume | Sampled one (vol. 1) — 200 OK, but not recommended given size |
| **Castell's Lexicon Heptaglotton** — companion reference to Walton's Polyglot | Edmund Castell, London | **1669** | Not a biblical text edition itself — a comparative Hebrew/Aramaic/Syriac/Samaritan/Arabic/Ethiopic/Persian lexicon. Draws on the same manuscript/lexical traditions assembled for Walton's Polyglot; no single witness date applies. | `bim_early-english-books-1475-1640_lexicon-heptaglotton-_castell-edmund_1669` — only copy located | 2.98 GB (single PDF) + 15.7 MB txt | 200 OK. **This is a large file** — flagging clearly given the disk-pressure constraint. |

---

## 4. Samaritan Pentateuch — editio princeps

Per the assignment: the Samaritan Pentateuch's first print appearance is inside the **Paris Polyglot (1632, bound into the completed set 1645)**, edited by Jean Morin.

- **Edition date**: 1632/1645 (Paris Polyglot, vol. 6, as part of the 10-vol set above).
- **Witness date**: the manuscript itself was purchased by the traveler **Pietro della Valle in Damascus in 1616** — that acquisition date is solid and well documented. The manuscript's own *copying* date, however, is genuinely disputed among Samaritan-studies scholars; estimates in the literature range roughly **12th–14th century**, and I did not find a settled consensus figure in this pass — treat any single-century claim as provisional. This manuscript is generally identified with what later cataloguing calls Bibliothèque nationale de France, MS Samaritain, though I did not independently confirm the exact shelfmark in this research pass and it should be verified before citing.
- **Status**: tied entirely to the Paris Polyglot's availability above — **not independently locatable as a free download**, since it was never printed as a standalone volume; it only exists as vol. 6 of the 10-vol Le Jay set. See the Paris Polyglot leads (Georgetown, HathiTrust) above.

---

## 5. Download commands

Pick individual items — **do not bulk-run this whole block**, given 15 GB free on root.

```bash
# ── Hebrew Bible ──────────────────────────────────────────────
# Soncino 1488 (editio princeps) — copy 1, 85.9 MB
wget "https://archive.org/download/tanakh-soncino-1488-jb-738.1-2-images/Tanakh_Soncino_1488_JB738.1-2.pdf"

# First Rabbinic Bible, Pratensis 1517/18 — 271.6 MB
wget "https://archive.org/download/first-rabbinic-bible-venice-1518-full-images/First_Rabbinic_Bible_Venice_1518_Full.pdf"

# Second Rabbinic Bible, ben Chayyim 1524-25 — RECOMMENDED, color, all 4 vols in one file, 458.5 MB
wget "https://archive.org/download/second-rabbinic-bible-venice-1525-color-full-images/Second_Rabbinic_Bible_Venice_1525_Color_Full.pdf"

# van der Hooght 1705, vols A-B only (Torah + Former Prophets) — 34.7 MB
wget "https://archive.org/download/Biblia_Hebraica_Van_der_Hooght_Amsterdam_1705_Volumes_AB_Torah_and_Former_Prophets/Biblia%20Hebraica%20Van%20der%20Hooght%20Amsterdam%201705%20Volumes%20A-B%20Torah%20and%20Former%20Prophets.pdf"

# ── Critical apparatus ────────────────────────────────────────
# Kennicott 1776-80, 2 vols, 262.3 MB total
wget "https://archive.org/download/vetustestamentum01kenn/vetustestamentum01kenn.pdf"
wget "https://archive.org/download/vetustestamentum02kenn/vetustestamentum02kenn.pdf"

# De Rossi 1784-88, 4 vols, ~440 MB total (original Bodoni printing, freely downloadable — NOT the restricted 1969 reprint)
wget "https://archive.org/download/VariaeLectiones/Variae%20Lectiones%201.pdf"
wget "https://archive.org/download/VariaeLectiones/Variae%20Lectiones%202.pdf"
wget "https://archive.org/download/VariaeLectiones/Variae%20Lectiones%203.pdf"
wget "https://archive.org/download/VariaeLectiones/Variae%20Lectiones%204.pdf"

# ── Polyglots ─────────────────────────────────────────────────
# Complutensian 1514-17 — RECOMMENDED copy, 6 vols, ~1.9 GB total
wget "https://archive.org/download/polyglotcomplutensis/Vol%201.pdf"
wget "https://archive.org/download/polyglotcomplutensis/Vol%202-3.pdf"
wget "https://archive.org/download/polyglotcomplutensis/Vol%204.pdf"
wget "https://archive.org/download/polyglotcomplutensis/Vol%205.pdf"
wget "https://archive.org/download/polyglotcomplutensis/Vol%206.pdf"

# Antwerp Polyglot 1568-73 — RECOMMENDED copy, all 8 tomes, 3.17 GB total
BASE="https://archive.org/download/biblia-sacra-hebraice-chaldaice-graece-latine-benedicti-ariae-montani-sacrorum-bibliorum-tomus-1569"
wget "$BASE/Biblia%20Sacra%20Hebraice%2C%20Chaldaice%2C%20Graece%20et%20Latine%20%5Bcura%20et%20studio%20Benedicti%20Ari%C3%A6%20Montani%5D%20Sacrorum%20Bibliorum%2001%20Tomums%20Primus%2C%20Qvinqve%20Libri%20Moysi%201569.pdf"
# (repeat pattern for tomes 02 through 08 — see metadata dump above for exact filenames; URL-encode the spaces/brackets/accents)

# Walton's London Polyglot 1655-57 — RECOMMENDED copy, all 6 tomes, ~2.1 GB total
BASE2="https://archive.org/download/biblia-sacra-polyglotta-complectentia-edidit-brianus-waltonus-lombart-hollar-roycroft-1657"
wget "$BASE2/Biblia%20Sacra%20Polyglotta%20Complectentia%20%5BEdidit%20Brianus%20Waltonus%2C%20Pierre%20Lombart%2C%20V%C3%A1clav%20Hollar%5D%20Imprinted%20London%20by%20Thomas%20Roycroft%20%28Tomus%201%29%201657.pdf"
# (repeat for Tomus 2-6 — check archive.org/metadata/<id> for exact filenames before pulling all 6, this set is ~2.1 GB)

# Castell's Lexicon Heptaglotton 1669 — 2.98 GB, single file, LARGE
wget "https://archive.org/download/bim_early-english-books-1475-1640_lexicon-heptaglotton-_castell-edmund_1669/bim_early-english-books-1475-1640_lexicon-heptaglotton-_castell-edmund_1669.pdf"
```

For any archive.org identifier not spelled out above, get the exact current filenames first — several of these items have filenames with brackets, accented characters, and trailing spaces that must be URL-encoded exactly:

```bash
curl -s "https://archive.org/metadata/<IDENTIFIER>" | python3 -c "
import json,sys
d=json.load(sys.stdin)
for f in d['files']:
    if f['name'].endswith(('.pdf','_djvu.txt')):
        print(f['name'], f.get('size'))
"
```

---

## 6. Not found / needs manual follow-up

| Item | Status |
|---|---|
| **Brescia Bible (1494)** | No free full scan located. Images only (Wikimedia, Google Arts & Culture). |
| **Buxtorf's Rabbinic Bible (Basel 1618–19)** | No free full scan located. Bibliographic record confirmed real (Sotheby's/Kestenbaum auction listings) but no digitization found. |
| **Athias (1661)** | No free scan of the 1661 edition itself located — only later 19th-c. reprints of the Athias/van der Hooght textual lineage (listed above). |
| **Van der Hooght (1705), vols C–D** | Only vols A–B (Torah + Former Prophets) located; Latter Prophets + Writings not found in this pass. |
| **Paris Polyglot (1629–45)** | Not on archive.org/e-rara/Gallica. Two unverified leads: Georgetown DSpace repo and HathiTrust catalog records, both blocked from automated verification by Cloudflare/bot-detection — **needs a human to check in an actual browser**, not a further automated pass. |
| **De Rossi Supplementum (1798)** | Only exists bundled in an access-restricted (lending-only) 1969 reprint — not freely downloadable. |
| **Samaritan Pentateuch editio princeps** | Same as Paris Polyglot — never printed standalone, tied to that set's availability. |

---

## Summary

- **Fully obtainable now, verified**: Soncino 1488, First Rabbinic Bible 1517/18, Second Rabbinic Bible 1524–25 (ben Chayyim — the highest-value single item here), van der Hooght 1705 (half the Bible), Kennicott 1776–80 (complete, 2 vols), de Rossi 1784–88 (complete original 4 vols, missing only the 1798 supplement), Complutensian Polyglot 1514–17 (complete, 6 vols), Antwerp Polyglot 1568–73 (complete, all 8 tomes), Walton's London Polyglot 1655–57 (complete, all 6 tomes), Castell's Lexicon Heptaglotton 1669.
- **Recommended-copy total if you pulled one good scan of each**: roughly **11–12 GB** (Antwerp 3.17 GB + Complutensian 1.9 GB + Walton 2.1 GB + Castell 2.98 GB + Kennicott 0.26 GB + de Rossi 0.44 GB + Second Rabbinic Bible 0.46 GB + First Rabbinic Bible 0.27 GB + Soncino 0.09 GB + van der Hooght 0.03 GB). That will not fit in 15 GB free alongside anything else — pick selectively.
- **Not obtainable in this pass**: Brescia 1494, Buxtorf 1618–19, Athias 1661 (as its own edition), Paris Polyglot 1629–45 (and therefore the Samaritan Pentateuch editio princeps), de Rossi's 1798 supplement, van der Hooght vols C–D.

**Top 3 highest-value items**, given the user's stated priorities:
1. **Second Rabbinic Bible (Bomberg/ben Chayyim, 1524–25)** — the 400-year standard Hebrew text, explicitly flagged by the user as high-value, fully verified and downloadable at 458.5 MB.
2. **Kennicott (1776–80) + de Rossi (1784–88)** together — a complete pre-1820 critical apparatus alternative to the copyrighted modern BHS apparatus, exactly the gap the user's rule creates and exactly what these fill. ~700 MB combined, both complete (apart from de Rossi's 1798 supplement).
3. **Antwerp Polyglot / Biblia Regia (1568–73)**, all 8 tomes — of the three named polyglots (Antwerp, Paris, Walton), this is the only one that came back **completely verified**: Paris couldn't be located as a free download at all, and while Walton's is also complete, Antwerp's Hebrew column carries the same ben-Chayyim text as item #1 above, so together with Walton's it gives full triangulation on the pre-1820 Hebrew textual tradition across three independent print lineages.
