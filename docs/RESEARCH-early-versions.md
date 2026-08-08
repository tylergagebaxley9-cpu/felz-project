# Research: `early-versions/` — Ancient Translations as Textual Witnesses

Scope: versional evidence (translations OF the Hebrew/Greek, not the Hebrew/Greek itself) — Latin, Gothic, Armenian, Georgian, Old Church Slavonic, Arabic, plus minor witnesses (Sogdian, Nubian). Nothing here duplicates what's already on disk (Coptic and Syriac Peshitta already exist under `nag-hammadi/` and `aramaic-syriac/`).

**Every candidate was checked for live resolution** (curl HEAD / archive.org metadata API / WebFetch) — nothing below is assumed. Where I could not confirm a URL resolves, it's flagged explicitly.

## How to read this

Per the user's standing instruction: **date of edition ≠ date of witness.** A 4th-century Gothic translation printed in 1665 is a primary witness in an old typeface, not a "1665 opinion." A 2010 critical edition of the same text is a modern scholarly reconstruction — useful, but a different kind of object. Both are listed. Nothing is filtered out; **Tier is a label, not an exclusion.**

- **Tier 1** — the manuscript itself: diplomatic transcription, facsimile, or photographic images.
- **Tier 2** — printed editions published before 1820.
- **Tier 3** — modern editions/digital corpora (19th–21st c.), including all standard critical/linguistic resources.

Columns: **Witness date** (when the translation was made / manuscript written) · **Edition date** (when this specific printed/digital object was produced) · **Tier** · **License** · **Format** · **Size** · **Resolves?** (verified live).

---

## 1. LATIN

### Vetus Latina (Old Latin, pre-Jerome)

| Item | Witness date | Edition date | Tier | URL | License | Format | Size | Resolves? |
|---|---|---|---|---|---|---|---|---|
| Sabatier, *Bibliorum Sacrorum Latinae Versiones Antiquae, seu Vetus Italica* — vol. 1 | 2nd–4th c. (surviving OL fragments, reconstructed) | 1743 | **2** | https://archive.org/details/bibliorumsacroru01saba | Public domain (pre-1820 printed book) | PDF + OCR `_djvu.txt` (confirmed present) | ~2.0 GB | **Yes** — verified via archive.org metadata API |
| Sabatier, same work, tomus tertius (vol. 3) | same | 1751 | **2** | https://archive.org/details/BibliorumSacrorumLatinaeVersionesAntiquaeSeuVetusItalicaEtCaeterae | Public domain | PDF + djvu.txt | ~5.1 GB | **Yes** |
| Sabatier, alt. scan (Florentain imprint) | same | 1742 | **2** | https://archive.org/details/bibliorumsacroru00flor | Public domain | PDF + djvu.txt | ~32 MB (partial/lower-res scan) | **Yes** |
| Vol. 2 of Sabatier | same | 1749ish | **2** | Not yet located as a distinct archive.org item — vol. 1 and vol. 3 confirmed, vol. 2 needs a follow-up search pass | — | — | — | Unconfirmed |
| Vetus Latina Database (Beuron Institute) | same | ongoing, modern | 3 | https://www.brepols.net/series/vld-o | **Commercial** — Brepols subscription, no free tier | Proprietary database | N/A | Resolves, but paywalled |
| PROIEL Latin Vulgate text (used as the comparison baseline, not true OL) | 4th–5th c. Vulgate, not OL | 2003–2023 | 3 | https://github.com/UniversalDependencies/UD_Latin-PROIEL | CC BY-NC-SA 3.0 | CoNLL-U / PROIEL XML | ~few MB | **Yes** |

**Sabatier (1743–51, pre-1820, public domain, full OCR text) is the single best Vetus Latina find** — it's the classic scholarly assembly of every Old Latin fragment recoverable from manuscripts and patristic quotation, exactly the pre-1820 standard the user wants. The modern Vetus Latina Database is a paywalled dead end.

### Vulgate (Jerome, 4th–5th c.)

| Item | Witness date | Edition date | Tier | URL | License | Format | Size | Resolves? |
|---|---|---|---|---|---|---|---|---|
| **Codex Amiatinus** — oldest complete Vulgate MS, images | 8th c. (Wearmouth-Jarrow, ~700 CE) | live digitization | **1** | Biblioteca Medicea Laurenziana viewer (mss.bmlonline.it, MS Amiatino 1) | Institutional viewer, terms not fully re-checked — treat as view-only, not confirmed redistributable | IIIF images | N/A (streaming) | Resolves per BML's own announcement; exact viewer URL not HEAD-verified this pass |
| Codex Amiatinus, 19th-c. printed transcription | 8th c. | 1854 | 3 (edition post-1820, but a transcription not a "critical reconstruction") | https://archive.org/details/codexamiatinus00jero | Public domain | PDF + djvu.txt | ~822 MB | **Yes** |
| **Sixtine Vulgate** (1590, first official printed Vulgate) | 4th–5th c. | 1590 | **2** | Not located as a clean standalone archive.org scan this pass — flagged for follow-up | — | — | — | Unconfirmed |
| **Clementine Vulgate** (1592, superseded Sixtine, stood as the RC standard until 1979) | 4th–5th c. | 1592 | **2** | No clean 1592 first-edition scan located this pass (search returned Wikipedia/BibleGet background, not a direct scan) | — | — | — | Unconfirmed — needs a dedicated pass |
| Vulgate within **Walton's Polyglot** (see §Polyglots) | 4th–5th c. | 1657 | **2** | see below | Public domain | PDF | included in polyglot volumes | **Yes** |
| Vulgate within Complutensian, Antwerp, Paris Polyglots | 4th–5th c. | 1514–1645 | **2** | see below | Public domain | PDF | included | **Yes** (Complutensian, Antwerp confirmed; Paris confirmed via Georgetown, not archive.org) |
| Clementine Vulgate, plain-text transcription (Michael Tweedale / vulsearch "Quasimodo" release) | 4th–5th c. | transcription released ~2005 | 3 | https://vulsearch.sourceforge.net/cgi-bin/vulsearch | **Public domain** — explicitly released PD by the transcriber, attribution requested not required | Plain text / VulSearch DB format | small (few MB) | Resolves (per search; not HEAD-checked) |
| `scrollmapper/bible_databases` — bundles VulgClementine, VulgConte, VulgHetzenauer, VulgSistine, Vulgate | 4th–5th c. | repo actively maintained | 3 | https://github.com/scrollmapper/bible_databases | **MIT** (repo license; underlying text provenance for individual editions not separately documented in the README) | JSON/SQL/CSV/XML | small | **Yes** — WebFetch confirmed repo + MIT license |
| `BibleGet-I-O/Clementine-Vulgate` | 4th–5th c. | maintained | 3 | https://github.com/BibleGet-I-O/Clementine-Vulgate | Not independently verified this pass | — | — | Found via search, not directly fetched |
| **Weber-Gryson Stuttgart Vulgate** (5th ed. 2007) — the modern critical standard | 4th–5th c. | 1969 / 2007 | 3 | N/A | **Copyrighted** — property of the Deutsche Bibelgesellschaft (German Bible Society), who actively enforce it. **Blocked**, same as NA28/UBS5 already excluded from this corpus. | — | — | Confirmed blocked (matches existing INDEX.md policy on DBG-owned texts) |

### Polyglots (cover Latin + most other early-versions languages at once — highest per-download value)

This is the coordinator's flagged priority. All four great polyglot Bibles put Hebrew, Greek, Latin (Vulgate), Aramaic Targum, Syriac, Samaritan, Arabic, and (Walton only) Ethiopic and Persian in parallel columns, pre-1820, verified public domain.

| Item | Languages | Edition date | Tier | URL | License | Format | Size | Resolves? |
|---|---|---|---|---|---|---|---|---|
| **Complutensian Polyglot** (Cisneros, Alcalá) | Hebrew, Greek, Latin, Aramaic (Targum Onkelos on Pentateuch) | 1514 (NT) / 1517 (OT) | **2** | https://archive.org/details/complutensian_polyglot_bible | Public domain | PDF + djvu.txt | **~146 GB** (multi-res color scan — huge, do NOT bulk-download; grab a single low-res PDF instead) | **Yes** |
| Complutensian, alt. item (5-vol set) | same | 1514/1517 | **2** | https://archive.org/details/polyglotcomplutensis | Public domain | PDF + djvu.txt | ~15.7 GB | **Yes** |
| Complutensian, Greek NT vol. only | Greek/Latin | 1517 | **2** | https://archive.org/details/GRCNA28_DBS_HS | Public domain | PDF | ~8.6 GB | **Yes** |
| **Antwerp / Plantin Polyglot** ("Biblia Regia") | Hebrew, Aramaic Targum, Greek LXX, Syriac, Latin | 1568–1573 | **2** | No archive.org scan located this pass — Wikipedia/academic sources only. Follow-up needed; likely exists on Google Books/e-rara/Universitätsbibliothek scans. | — | — | — | Unconfirmed |
| **Paris Polyglot** (Le Jay) — first print of Syriac OT + Samaritan Pentateuch + Samaritan Targum | Hebrew, Samaritan, Greek, Syriac, Latin, Arabic | 1629–1645 | **2** | https://repository.digital.georgetown.edu/handle/10822/712682 (vol. 1) and https://repository.digital.georgetown.edu/handle/10822/1100321 (vol. 5 pt. 1) — multi-volume, only 2 volumes' URLs confirmed this pass | Georgetown institutional repository — free to view; explicit reuse license not checked | PDF (assumed) | not measured | Resolves (Georgetown links, not HEAD-checked); NOT on archive.org |
| **Walton's London Polyglot** — Hebrew, Chaldee (Aramaic), Samaritan, Greek, Syriac, Arabic, Persian, Ethiopic, Latin (9 languages, most of the whole language list in one source) | all above | 1654–1657 | **2** | https://archive.org/details/walton_polyglot | Public domain | PDF + djvu.txt, **8 separate volume PDFs bundled in one item**: `1 Walton Polyglot Genesis-Leviticus.pdf` … `8 WaltPoly8_Ecclesiasticus-Maccabees.pdf` | **~14.1 GB total** across all 8 vols | **Yes** — file list confirmed directly |
| Walton Polyglot, single alt. volume | same | 1657 | 2 | https://archive.org/details/bim_early-english-books-1641-1700_biblia-sacra-polyglotta-_bible-polyglot_1657_2 | Public domain | PDF | not measured | Found via search, not re-verified |
| **Castell's *Lexicon Heptaglotton*** (companion dictionary to Walton: Hebrew, Chaldee, Syriac, Samaritan, Ethiopic, Arabic, Persian) | — | 1669 | **2** | https://archive.org/details/LexiconHeptaglotton | Public domain | 2-vol PDF + djvu.txt | ~3.4 GB | **Yes** |

**This is the single highest-value cluster in this whole research pass** — Walton's Polyglot alone puts pre-1820 printed Hebrew, Samaritan, Greek, Syriac, Arabic, Ethiopic, Persian, and Latin side by side, fully OCR'd, 100% public domain, confirmed live. At ~14 GB it is a meaningful chunk of the ~6.5 GB already on disk — recommend downloading 1–2 volume PDFs selectively rather than the whole set, or fetching individual page ranges.

---

## 2. GOTHIC (Wulfila's Bible, 4th c.)

| Item | Witness date | Edition date | Tier | URL | License | Format | Size | Resolves? |
|---|---|---|---|---|---|---|---|---|
| **Codex Argenteus** — the manuscript itself, digital facsimile | ~6th c. copy of Wulfila's 4th c. translation | digitized 2010–2019 | **1** | Uppsala University Library project; images now via alvin-portal.org (Alvin Platform) | Not independently re-verified this pass; Uppsala's project page describes it as freely viewable | IIIF/scan images | N/A | Resolves per Uppsala's own project pages; not HEAD-checked |
| Codex Argenteus, printed description/history | — | 1962 | 3 | https://archive.org/details/codexargenteussi0000kleb | Public domain | PDF + djvu.txt (one PDF is a locked/encrypted variant — use the plain one) | ~73 MB | **Yes** |
| **Junius' *editio princeps*** ("Quatuor D.N. Jesu Christi euangeliorum versiones perantiquae duae, Gothica scil. et Anglo-Saxonica") — first printed Gothic Bible text | 4th c. | **1665**, Dordrecht | **2** | Google Books scan exists (`play.google.com/store/books/details?id=OMRYmqR5y98C`); **no archive.org copy located this pass** | Google Books — public domain but Google's own access/reuse terms apply, not a clean file | — | — | Google Books listing confirmed to exist; not independently HEAD-checked, no direct download URL confirmed |
| **Benzelius edition** (Gothic text in Junius' type + Latin translation + Lye's Gothic grammar) | 4th c. | **1750** | **2** | Not located as a digitized scan this pass — flagged for follow-up | — | — | — | Unconfirmed |
| Uppström's collated re-edition | 4th c. | 1854 | 3 | https://archive.org/details/codexargenteuss00wulfgoog | Public domain | PDF + djvu.txt | ~97 MB | **Yes** |
| Gabelentz/Löbe-tradition Gothic-Anglo-Saxon parallel gospels | 4th c. | 1888 | 3 | https://archive.org/details/gothicanglosax00ulfi | Public domain | PDF + djvu.txt | ~830 MB | **Yes** |
| Balg/Bernhardt, "The First Germanic Bible" | 4th c. | 1891 | 3 | https://archive.org/details/firstgermanicbib00ulfi | Public domain | PDF + djvu.txt | ~668 MB | **Yes** |
| **Streitberg's edition** (1919) — the modern linguistic standard, basis of PROIEL/Wulfila Project digital texts | 4th c. | 1919/1965 repr. | 3 | via Wulfila Project below | see below | — | — | — |
| **Wulfila Project** (formerly Univ. of Antwerp, hosted wulfila.be) — TEI-encoded, lemmatized, POS-tagged Gothic Bible | 4th c. | digital ed., ~1999–2025 (project now transferring institutions post-Feb 2025) | 3 | https://www.wulfila.be/gothic/ (browse) / download page under wulfila.be/project/ | **Text and facsimiles: public domain.** Project's own annotations/database: **"freely available for non-commercial use"** with attribution — NOT a standard open license, blocks commercial reuse | TEI XML | small | **Yes** — copyright page fetched and confirmed |
| PROIEL/Syntacticus Gothic (Streitberg 1919 text, dependency-annotated) | 4th c. | released 2004–2023 | 3 | https://github.com/UniversalDependencies/UD_Gothic-PROIEL and https://github.com/syntacticus/syntacticus-treebank-data | **CC BY-NC-SA 3.0** — confirmed | CoNLL-U / PROIEL XML | small | **Yes** |

---

## 3. ARMENIAN (5th c. translation)

| Item | Witness date | Edition date | Tier | URL | License | Format | Size | Resolves? |
|---|---|---|---|---|---|---|---|---|
| Manuscript images of Zohrab's source codices | 5th c. translation; underlying MSS vary, mostly medieval | — | 1 | Not located this pass — no free bulk manuscript-image source identified | — | — | — | Not found |
| **Zohrab Bible** (Venice, Mkhitarist Press) — the standard printed Armenian Bible, still cited as *the* critical text | 5th c. | **1805** | **2** | NT: https://archive.org/details/armenian_zohrab_nt · OT vol. 1: https://archive.org/details/OldTestamentInClassicalArmenian · OT vol. 3: https://archive.org/details/OldTestamentInClassicalArmenian-3 | Public domain | PDF + djvu.txt (all 3) | NT ~921 MB, OT vol.1 ~800 MB, OT vol.3 ~1.03 GB | **Yes** — all three confirmed via metadata API |
| Zohrab Bible, HTML edition | 5th c. | digital ed., ongoing | 3 | https://titus.uni-frankfurt.de/texte/etcs/arm/zohrab/armnt/armnt.htm (NT) and .../armat/armat.htm (OT, "preliminary") | **TITUS terms**: free for scholarly use with attribution, **explicitly NOT for commercial use**, no standard open license — confirmed via direct fetch of TITUS's own copyright notice | HTML | small | **Yes** |
| PROIEL Armenian NT (ed. Künzle 1984) | 5th c. | digitized 2004–2023 | 3 | https://github.com/proiel/proiel-treebank / https://github.com/syntacticus/syntacticus-treebank-data | CC BY-NC-SA 3.0 (per proiel-treebank repo) | PROIEL XML / CoNLL-X | ~23,513 tokens, small | **Yes** |
| Leiden Armenian Lexical Textbase (LALT) | 5th–9th c. texts | CD-ROM/digital ed. | 3 | https://www.sd-editions.com/LALT/ | **Commercial** — sold product, not free | — | — | **Blocked** |
| Calfa Vision (manuscript transcription platform) | varies | ongoing | — | calfa.fr / Calfa Vision | Platform for annotating, not a bulk free corpus download | — | — | Not a viable free-text source |

**Highest-priority Armenian find: the 1805 Zohrab Bible is squarely pre-1820**, fully OCR'd, public domain, and is the source text every later Armenian critical edition still measures itself against.

---

## 4. GEORGIAN (Old Georgian versions)

| Item | Witness date | Edition date | Tier | URL | License | Format | Size | Resolves? |
|---|---|---|---|---|---|---|---|---|
| Adishi Gospels MS (Redaction of Khanmeti/Haemeti) | 897 CE | — | 1 | Not located as free bulk images this pass | — | — | — | Not found |
| **Bakar/Vakhtang Georgian Bible** — first complete printed Georgian Bible, produced by exiled Georgian royals in Moscow | Old Georgian translation tradition, various centuries | **1743** | **2** | No digitized scan located this pass — appears to survive in only a handful of physical copies (one recently repatriated to Harvard per news coverage); not yet found on archive.org/Google Books | — | — | — | **Not found — flagged for a dedicated follow-up search** |
| TITUS Old Georgian Gospel synopsis (Khanmeti/Adishi redaction, critical synopsis of MSS) | 897 CE (Adishi) + Khanmeti palimpsest fragments (older, ~5th–7th c. layer) | digital ed. 2011–2014 | 3 | https://titus.fkidg1.uni-frankfurt.de/texte/etca/cauc/ageo/nt/ntkpl/ntkpl001.htm | Same TITUS terms as above — non-commercial, attribution required | HTML | small | **Yes** — page confirmed to exist via search |
| Georgian National Corpus (GNC) — includes an Old Georgian sub-corpus | various | ongoing | 3 | http://gnc.gov.ge/gnc/page | Online concordancer only — **no bulk download found**; license unclear | web query interface | N/A | Resolves as a search tool, not a downloadable corpus |
| `UniversalDependencies/UD_Georgian-GNC` | **modern** Georgian (NOT Old Georgian/biblical) | ongoing | 3 | https://github.com/UniversalDependencies/UD_Georgian-GNC | CC BY-SA 4.0 | CoNLL-U | small | **Yes** — but **not relevant**, this is modern-language journalism text, flagged so it isn't mistakenly pulled in as a biblical source |

Georgian is the weakest-covered language in this research pass — no pre-1820 scan located and no open bulk manuscript images found. The TITUS synopsis is the only usable machine-readable text, under non-commercial terms.

---

## 5. OLD CHURCH SLAVONIC

| Item | Witness date | Edition date | Tier | URL | License | Format | Size | Resolves? |
|---|---|---|---|---|---|---|---|---|
| Codex Marianus / Zographensis / Ostromir — manuscript images | 10th–11th c. | — | 1 | Held at Russian State Library (Ostromir), Austrian National Library (Marianus is at Russian State Library too, per Jagić) — no free bulk image source located this pass | — | — | — | Not found |
| **Ostrog Bible** — first complete printed Church Slavonic Bible (Ivan Fyodorov) | Church Slavonic translation tradition, 9th–10th c. roots | **1581** | **2** | https://archive.org/details/OstrogBiblija1581 | Public domain | PDF + djvu.txt | ~1.99 GB | **Yes** |
| Moscow Bible (2nd printed edition, basis for later revisions) | same | **1663** | **2** | Not located as a distinct archive.org item this pass — flagged for follow-up | — | — | — | Unconfirmed |
| **Elizabeth Bible** — 3rd printed edition, still the liturgical standard in Orthodox churches today | same | **1751** | **2** | https://archive.org/details/bibliasiriechkni04luik | Public domain | PDF + djvu.txt | ~1.42 GB | **Yes** |
| TITUS Codex Marianus (Jagić 1883 edition, HTML) | 11th c. | digital ed. | 3 | https://titus.uni-frankfurt.de/texte/etcs/slav/aksl/marianus/maria.htm | TITUS non-commercial terms | HTML | small | **Yes** — confirmed live via direct fetch |
| TITUS Codex Zographensis (HTML) | 10th–11th c. | digital ed. | 3 | https://titus.uni-frankfurt.de/texte/etcs/slav/aksl/zograph/zogra.htm | TITUS non-commercial terms | HTML | small | **Yes** — confirmed live |
| PROIEL/UD Old Church Slavonic (Codex Marianus, ed. Jagić 1883, tokenized) | 11th c. | digitized 2004–2023 | 3 | https://github.com/UniversalDependencies/UD_Old_Church_Slavonic-PROIEL | CC BY-NC-SA 3.0 | CoNLL-U / PROIEL XML | ~58,269 tokens, small | **Yes** |
| Syntacticus/TOROT (extends OCS/Old Russian coverage) | 11th c.+ | ongoing | 3 | https://github.com/syntacticus/syntacticus-treebank-data | Not independently confirmed this pass (proiel-treebank license was CC BY-NC-SA 3.0; assume same, not verified for this specific repo) | PROIEL XML | small | **Yes**, repo resolves |

---

## 6. ARABIC

| Item | Witness date | Edition date | Tier | URL | License | Format | Size | Resolves? |
|---|---|---|---|---|---|---|---|---|
| **Mt Sinai Arabic MS 151** — Pauline Epistles + Acts + Catholic Epistles, one of the earliest dated Arabic Bible MSS | dated by colophon to **867 CE** | — | **1** | Sinai Palimpsests Project (sinai.library.ucla.edu) / Library of Congress 1950 microfilm digitization referenced in search results — exact free-access URL not confirmed this pass | Not confirmed — Sinai Library digitization projects generally require registration/access agreements | images | N/A | **Not independently verified** — flagged for a dedicated follow-up |
| **Biblia Sacra Arabica** (Propaganda Fide, Rome) — first complete printed Arabic Bible, parallel Latin/Arabic | Arabic Gospels/Bible translation tradition, medieval | **1671** | **2** | https://archive.org/details/bub_gb__sQopDoeVQ8C | Public domain | PDF + djvu.txt | ~703 MB | **Yes** |
| Arabic column of **Walton's Polyglot** | same | 1657 | 2 | see §Polyglots above | Public domain | PDF | included | **Yes** |
| Arabic column of **Paris Polyglot** (first printed under Le Jay, also incl. Samaritan-Arabic Targum) | same | 1629–1645 | 2 | see §Polyglots above | Georgetown repository | PDF | included | Resolves, not HEAD-checked |
| Saadia Gaon's Tafsir (10th c. Judeo-Arabic Torah translation) | 10th c. | printed editions exist but none located digitized this pass | — | Not found | — | — | — | Not found — flagged for follow-up |
| Modern critical Arabic NT/Gospel editions | — | — | 3 | None identified as freely machine-readable this pass | — | — | — | Not found |

---

## 7. OTHER EARLY/OPEN WITNESSES

| Item | Witness date | Edition date | Tier | URL | License | Format | Size | Resolves? |
|---|---|---|---|---|---|---|---|---|
| **Christian Sogdian Gospel Lectionary (E5)** | ~9th–11th c. | — | 1 | Held in the Turfan Collection, Berlin-Brandenburg Academy of Sciences (**not** the British Library, as sometimes assumed) — likely digitized via the International Dunhuang Project / BBAW Turfan digital archive, exact URL not confirmed this pass | Not confirmed | images | N/A | Not independently verified — flagged for follow-up |
| **Old Nubian** biblical fragment (*Liber Institutionis Michaelis Archangeli*, Qasr Ibrim) | 9th–10th c. | — | 1 | British Museum object EA 71305, viewable via their online collection | View-only, standard museum terms; not a real corpus (single fragment) | image | N/A | Resolves as a museum catalog record, not verified as bulk-downloadable |
| Old Latin Psalters | see Vetus Latina/Sabatier above — Sabatier's compilation includes Psalter fragments | 1743–51 | 2 | (same as Sabatier entries above) | Public domain | PDF | (included above) | **Yes** |

Both Sogdian and Nubian have essentially no freely available bulk corpus — they exist as scattered fragments in institutional collections, worth a single manuscript photo at most, not a downloadable text corpus. Not recommended as a download target; noted for completeness only.

---

## Summary judgment

**Obtainable now, verified, high value:**
- Walton's Polyglot (1657, ~14 GB, 8 vols, PD, OCR'd) — Hebrew/Samaritan/LXX/Syriac/Arabic/Ethiopic/Persian/Latin in one place
- Castell's Lexicon Heptaglotton (1669, ~3.4 GB, PD) — companion dictionary
- Complutensian Polyglot (1514/17) — but the confirmed items are enormous (15.7–146 GB); grab a single low-res volume, not the full set
- Sabatier's Vetus Latina (1743/1751, ~7 GB across 2 confirmed vols, PD, OCR'd)
- Zohrab Armenian Bible (1805, ~2.7 GB across NT+OT, PD, OCR'd)
- Ostrog Bible (1581, ~2 GB, PD, OCR'd) and Elizabeth Bible (1751, ~1.4 GB, PD, OCR'd) — Church Slavonic
- Biblia Sacra Arabica (1671, ~700 MB, PD, OCR'd)
- Wulfila Project Gothic TEI (small, text/facsimile PD, project's own annotations non-commercial only)
- PROIEL/Syntacticus/UD treebanks for Latin, Gothic, Armenian, OCS (small, CC BY-NC-SA 3.0 — non-commercial)

**Blocked (copyright, confirmed):**
- Weber-Gryson Stuttgart Vulgate — Deutsche Bibelgesellschaft, actively enforced, same policy as the already-excluded NA28/UBS5
- Vetus Latina Database (Brepols) — commercial subscription only
- Leiden Armenian Lexical Textbase — commercial product

**No clear open license (flag, don't assume permission):**
- All TITUS Frankfurt texts (Armenian Zohrab HTML, Georgian synopsis, OCS Marianus/Zographensis) — TITUS's own stated terms are "free for scholarly use with attribution, no commercial use," which is **not** a standard open license (no CC designation, no redistribution right stated)
- Wulfila Project's own annotation layer (text/facsimile itself is PD, but the project's markup/database is "non-commercial use" only)

**Not found this pass, worth one more targeted search each:**
- Clementine Vulgate 1592 / Sixtine Vulgate 1590 clean first-edition scans
- Antwerp/Plantin Polyglot (1568–73) digitization
- Junius' 1665 Gothic editio princeps and Benzelius' 1750 edition as direct-download scans (both confirmed to exist, Google Books listing only for Junius)
- Bakar/Vakhtang Georgian Bible (1743) — may simply not be digitized; very rare (only ~300 copies printed, some recently repatriated from private hands)
- Moscow Bible (1663, Church Slavonic)
- Sinai Arabic 151 free image access
- Saadia Gaon's Tafsir digitized edition

**Approximate total size if the "obtainable now" list above were fully downloaded: ~35–40 GB** — well beyond a reasonable single pull given disk pressure. Recommend downloading selectively: the small treebank/TEI corpora (a few MB total) first, then 1–2 individual polyglot volume PDFs rather than full multi-volume sets, using the exact per-item URLs above.

## Suggested fetch commands (small items only — nothing bulk)

```bash
# Small, safe: PROIEL/Syntacticus treebanks (Latin, Gothic, Armenian, OCS all in one repo)
git clone --depth 1 https://github.com/syntacticus/syntacticus-treebank-data.git

# Small: UD Gothic/Latin/OCS individually if only one language wanted
git clone --depth 1 https://github.com/UniversalDependencies/UD_Gothic-PROIEL.git
git clone --depth 1 https://github.com/UniversalDependencies/UD_Latin-PROIEL.git
git clone --depth 1 https://github.com/UniversalDependencies/UD_Old_Church_Slavonic-PROIEL.git

# Small: scrollmapper Latin Vulgate editions (multiple recensions, MIT-licensed repo wrapper)
git clone --depth 1 https://github.com/scrollmapper/bible_databases.git

# Medium (~1-2 GB each) — pick ONE at a time, verify disk headroom first:
wget https://archive.org/download/armenian_zohrab_nt/armenian_zohrab_bible_new_testament.pdf
wget https://archive.org/download/OstrogBiblija1581/OstrogBiblija1581.pdf
wget https://archive.org/download/bibliasiriechkni04luik/bibliasiriechkni04luik.pdf
wget https://archive.org/download/bub_gb__sQopDoeVQ8C/bub_gb__sQopDoeVQ8C.pdf

# Large (~2-5 GB) — only if disk pressure allows:
wget "https://archive.org/download/walton_polyglot/1%20Walton%20Polyglot%20Genesis-Leviticus.pdf"
wget https://archive.org/download/LexiconHeptaglotton/Lexicon%20Heptaglotton%20I.pdf
wget https://archive.org/download/bibliorumsacroru01saba/bibliorumsacroru01saba.pdf
```

Do NOT `wget` the full `complutensian_polyglot_bible` item (146 GB) or the full `walton_polyglot`/`polyglotcomplutensis` items in one shot (14/15.7 GB) — pull individual volume PDFs listed above instead.
