# Research: `manuscripts/` — primary witnesses + apparatus

Status: research only, nothing downloaded. Root filesystem is under disk pressure — every command below is a manual `git clone` / `wget` for you to run selectively.

Per your update: **nothing filtered out.** Everything found is listed, tiered, and dated. Copyright-blocked items are listed too, marked BLOCKED, so you know they exist.

## Tier key

- **Tier 1** — transcription/facsimile of the manuscript itself. No editorial reconstruction. This is the actual scope of `manuscripts/`.
- **Tier 2** — printed edition published before 1820, transcribing/collating a real manuscript.
- **Tier 3** — modern editorial/reconstructed product (CBGM, ECM, eclectic critical text, statistical restoration). Listed for completeness, clearly marked.

Every row has two dates: **MS date** (the physical artifact) and **Edition date** (the transcription/printing you'd actually be downloading). A 4th-century codex read through a 2009 XML transcription is old evidence in a new wrapper — the two numbers are not the same claim.

All URLs below were checked live (HTTP 200, or a 3xx that resolves — archive.org routinely 302s from `/details/` to a CDN node, that's normal, not a dead link) on 2026-08-08.

---

## 1. Codex Sinaiticus (01, ℵ) — TIER 1, confirmed obtainable

| MS date | Edition date | | |
|---|---|---|---|
| c. 330–360 CE (mainstream palaeographic consensus; some scholars argue as late as 4th c. end) | 2007–2009, updated to v1.94–2.0 | | |

- **Bulk XML (direct download)**: https://codexsinaiticus.org/en/project/transcription_download.aspx
  - Single zip, 4.4 MB compressed / 28.8 MB uncompressed (~28M characters), current build v1.04 dated 2014-03-25 on that page (GitHub mirror is ahead, at v1.94+).
  - Format: Unicode TEI-based XML with project-specific extensions (schema documented in `XMLspecs_sinaiticus.pdf`, linked from the same page).
  - **License: CC BY-NC-SA 3.0** — non-commercial, share-alike. This is stricter than everything else already in the corpus (which is CC BY / CC BY-SA). Flag this if you ever redistribute derived work from it.
- **GitHub mirror (more current)**: https://github.com/itsee-birmingham/codex-sinaiticus
  - Main file `sinaiticus_full_v195.xml`, validated against `tei_all_sinaiticus.dtd`. Actively maintained by ITSEE Birmingham (same license, `license.md` in repo confirms CC BY-NC-SA).
  - `git clone https://github.com/itsee-birmingham/codex-sinaiticus.git`

**Bonus find, same license/team**: **Codex Zacynthius** (Ξ, 040) — palimpsest, the oldest surviving catena manuscript. Overtext (12th–13th c. lectionary) and undertext (6th c. Gospel of Luke catena) transcribed separately, TEI P5, **CC BY 4.0** (more permissive than Sinaiticus).
- `git clone https://github.com/itsee-birmingham/codex-zacynthius-xml.git`

---

## 2. Codex Vaticanus, Alexandrinus, Bezae, Washingtonianus — IGNTP

### Codex Bezae (D05) — TIER 1, confirmed obtainable

| MS date | Edition date |
|---|---|
| c. 400–500 CE (5th c. mainstream; some argue into early 6th — genuinely contested) | 2010s TEI transcription (ITSEE/Cambridge UL), ongoing updates |

- `git clone https://github.com/itsee-birmingham/codex-bezae.git`
- TEI XML, **CC BY 4.0**. Produced with Cambridge University Library (holds the physical MS, Nn.2.41).
- IGNTP project page: https://itseeweb.cal.bham.ac.uk/igntp/bezae.html

### Codex Vaticanus (B03) — TIER 1, obtainable via John transcription set

| MS date | Edition date |
|---|---|
| c. 300–325 CE | IGNTP "Transcriptions of the Majuscules of John" project, ongoing (Parker/ITSEE) |

- Confirmed listed **complete for John** on the IGNTP majuscule-of-John page: https://itseeweb.cal.bham.ac.uk/iohannes/majuscule/transcriptions.html
- Bulk download portal: http://www.iohannes.com (redirects; use https://itseeweb.cal.bham.ac.uk/iohannes/transcriptions/index.html as the live mirror — the `iohannes.com` domain itself timed out / TLS-mismatched when I tested it directly, the `itseeweb.cal.bham.ac.uk` host is the reliable one)
- Format: raw TEI XML, per-manuscript, downloadable individually from the transcription viewer or in the bulk zip IGNTP announced in their 2017 "Open Data" release (350 manuscripts, CC BY 4.0): https://www.birmingham.ac.uk/news-archive/2017/igntp-releases-open-data
- **Caveat**: this covers John only. Vaticanus's other 26 books (rest of NT + nearly all of LXX OT) are **not** covered by IGNTP's diplomatic TEI work — see Tier 2 fallback below.
- **Pauline epistles** (separate IGNTP stream, also Vaticanus + ~200 other witnesses): Galatians (223 MSS) `https://www.epistulae.org/downloads/Galatians_Greek_Transcriptions.zip`, Ephesians (158 MSS) `https://www.epistulae.org/downloads/Ephesians_Greek_transcriptions.zip`, Philippians in progress (49 MSS) `https://www.epistulae.org/downloads/Philippians_Greek_transcriptions.zip` — CC BY 4.0, raw XML.

### Codex Alexandrinus (A02) — TIER 1 partial (John only) + TIER 2 fallback (whole NT)

| MS date | Edition date |
|---|---|
| c. 400–440 CE | IGNTP John transcription: ongoing. Woide facsimile: 1786 |

- IGNTP John majuscule page lists Alexandrinus as **partial** coverage (damaged in John, several leaves lost) — same source/license as Vaticanus above.
- **Tier 2, full NT, pre-1820**: Woide's 1786 facsimile edition — the first complete typographic reproduction of Alexandrinus's NT, letter-for-letter.
  - archive.org: `https://archive.org/details/codexalexandrinu00woid` (confirmed 200)
  - Also a later Cowper 1860 reprint with `_djvu.txt` OCR layer confirmed present: `https://archive.org/stream/CodexAlexandrinus-Cowper/CodexAlexandrinus_djvu.txt`
  - Public domain.

### Codex Washingtonianus (W032) — TIER 1 partial (John only) + no pre-1820 edition (too late a discovery)

| MS date | Edition date |
|---|---|
| c. 400–450 CE (late 4th/early 5th c., some put it up to mid-5th) | IGNTP John transcription: partial coverage confirmed |

- Listed on the same IGNTP majuscule-of-John page as **partial**. Same access path/license as above.
- No pre-1820 printed edition exists — the manuscript wasn't acquired/known until Charles Freer bought it in Egypt in 1906. First scholarly transcription is Henry A. Sanders, 1912 (University of Michigan) — itself now public domain by age, but I did not find a clean digitized *text* (only facsimile page-image scans) in this pass. Worth a follow-up search specifically for a Sanders 1912 archive.org `_djvu.txt` if you want it — I did not chase this thread to the end.

---

## 3. NTVMR / INTF (Münster) — TIER 1 (transcriptions) + TIER 3 (CBGM/ECM)

**Transcriptions — Tier 1, confirmed live**:
- API is real and responding (tested live, HTTP 200): `http://ntvmr.uni-muenster.de/community/vmr/api/transcript/get/?docID=<id>&indexContent=<passage>&fullPage=true&format=teiraw`
- Returns TEI XML per manuscript/passage. License: **CC BY 4.0**.
- **No native bulk/batch export** — you have to loop docIDs yourself (there is no "download everything" button; NTVMR staff have publicly asked users not to hammer the server doing this). Practical for a handful of manuscripts, not for the whole 5,000+ MS corpus.
- Reference guide (confirms API shape, gives worked Python example): https://digitalorientalist.com/2025/04/29/exploring-the-new-testament-virtual-manuscript-room-api/

**CBGM tooling — Tier 3, open source, confirmed obtainable**:
- `git clone https://github.com/SCDH/intf-cbgm.git` — "Genealogical Queries," Münster's own Vue+Flask+Postgres CBGM implementation. Consumes TEI XML in IGNTP/INTF format.
- `git clone https://github.com/jjmccollum/open-cbgm.git` — independent (non-INTF) fast C++ CBGM implementation, MIT-licensed, TEI-compliant.
- Both are *tools*, not manuscript data — you'd feed them the NTVMR/IGNTP TEI files above.

**ECM (Editio Critica Maior) apparatus — mixed, mostly BLOCKED**:
- Print ECM is published by **Deutsche Bibelgesellschaft (German Bible Society)** — explicitly copyrighted, "no downloading or modification without express written consent." This is the item you already declined; confirmed still blocked, no change.
- **Partial carve-out**: at SBL 2017, INTF (Holger Strutwolf) put the **digital ECM apparatus for Acts** online free at `http://ntvmr.uni-muenster.de/nt-transcripts` — unedited collation data, patristic citations, Vetus Latina collations, conjectural emendations. This is browsable/query-able (through the NTVMR web interface, same API as above), not a clean bulk-downloadable dataset, and I could not confirm a distinct license statement for this specific Acts apparatus separate from the general NTVMR CC BY 4.0 — treat it as "probably CC BY 4.0 via the same API, unconfirmed in writing for this specific dataset."
- Everything **beyond Acts** (Synoptics parallels, Catholic Epistles, the rest) — no evidence of a free digital release; treat as BLOCKED same as before.

---

## 4. Hebrew — Aleppo Codex, Leningrad Codex, Sefaria — mostly BLOCKED for transcription (images only)

**Aleppo Codex — TIER 1 target, NOT obtainable as machine-readable text**:

| MS date | — |
|---|---|
| c. 920–930 CE | — |

- `aleppocodex.org` — site explicitly says "new website under construction," not usable right now.
- Checked two live alternatives, **both are page images only, no transcription**:
  - `https://barhama.com/aleppocodex/` and `https://www.mgketer.org/kazms` (Bar-Ilan's Miqra al pi ha-Mesorah project) — confirmed via fetch: photographs only, Israeli copyright law (sections 19/56a) cited on the page, no bulk download offered.
  - Internet Archive full-page-image set: `https://archive.org/details/aleppo-codex-tanakh-full-scan-images` — images, right-to-left ordered, table of contents; still images not text.
- **Conclusion**: there is no freely downloadable *machine-readable transcription* of the Aleppo Codex distinct from what you already have. The WLC (`hebrew-ot/morphhb/`) is the standard proxy — it's a transcription of Leningrad, corrected in places against Aleppo by the Westminster team, but it is not itself an Aleppo transcription. This gap is real; I didn't find a way to close it.

**Leningrad Codex — you already have the standard machine-readable transcription (WLC, in `hebrew-ot/`)**. What's *not* mirrored:
- Actual manuscript facsimile images (as opposed to WLC's derived text) — Sefaria hosts a full high-res color PDF, browsable per-verse via "Resources → Manuscripts": `https://www.sefaria.org/texts/Tanakh`. Images only, not additional transcription data — skip, would duplicate what WLC already encodes as text.
- `tanach.us` (Unicode/XML Leningrad Codex, UXLC) — this is essentially a **parallel independent transcription of Leningrad** (not the same project as WLC/OSHB), with full cantillation + ketiv/qere, TEI-headered. Confirmed downloadable: `https://tanach.us/Pages/Technical.html` (zipped text files). This is worth having as a **second independent transcription of the same 1008 CE codex** to cross-check `morphhb/` against — genuine value-add, distinct from what's on disk. License: check the TEI header in the download (not independently confirmed here — page states terms are in the file itself).

**Sefaria API** — confirmed live, v3 texts API (`developers.sefaria.org`), can pull Tanakh with or without cantillation via `version=hebrew|...` parameter. This is a live API, not a static corpus — lower priority than a static download, and it's serving the same underlying Leningrad-derived text you already have via WLC. Not recommended as a separate acquisition target.

---

## 5. Apparatus / variant data — CNTR is the big one, confirmed and cleanly separable by tier

### CNTR (Center for New Testament Restoration, Alan Bunning) — Tier 1 AND Tier 3 in the SAME repo, cleanly split by folder

`git clone https://github.com/Center-for-New-Testament-Restoration/transcriptions.git`

License: **CC BY-SA 4.0**. Confirmed folder structure via GitHub API:

- **`class 1/`, `class 2/`, `class 3/`** — **TIER 1**. Per-manuscript diplomatic transcriptions, one `.txt` file per Gregory-Aland number (`01.txt` = Sinaiticus, `02.txt` = Alexandrinus, `0160.txt`, `0162.txt`, etc — confirmed 130 files in `class 1/` alone; classes 2/3 presumably later-date or fragmentary MSS). Custom encoding: **Manuscript Encoding Specification (MES)**, not TEI XML — grammar defined in `MES.g4` (ANTLR), documented in `greekcntr.org/resources/technical.pdf`. Every extant Greek NT manuscript up to 400 AD, per project's stated scope.
  - MS dates: span the whole range this corpus cares about, 2nd–5th c. depending on witness.
  - Edition date: transcriptions actively maintained, most recent project overview PDF undated but repo has 125+ commits, ongoing.
- **`critical texts/`** — **TIER 3**, clearly separate, only 5 files: `KJTR.txt`, `RP.txt`, `SR.txt`, `ST.txt`, `WH.txt` (King James TR, Robinson-Pierpont, CNTR's own Statistical Restoration, Stephanus, Westcott-Hort). These are reconstructed eclectic texts, not manuscript witnesses — do not confuse with the class 1/2/3 folders above.

This repo is genuinely valuable and was worth the priority bump — it's the one place giving you raw, manuscript-by-manuscript Greek NT transcriptions in bulk, openly licensed, in a single clone.

### STEPBible-Data — already partially on disk (`hebrew-ot/STEPBible-Data/`), has an apparatus component not yet pulled

- `TAGNT` (Translators Amalgamated Greek NT) — tags every word with which of NA27/28, TR, SBLGNT, Tregelles, Byz, WH it appears in, plus positional/meaning variants.
- `TNTMM` (Translators NT Manuscripts and Meanings) — witness list per meaning-affecting variant, sourced from the UBS apparatus (**note: UBS apparatus underneath is the same GBS-copyrighted family as NA28/ECM** — STEPBible republishes their own derived tagging under CC BY 4.0, but the underlying variant *selection* traces back to UBS scholarship; treat as Tier 3, legally fine per STEPBible's own license grant, just be aware of the lineage).
- Same repo you already have: https://github.com/STEPBible/STEPBible-Data — if these two specific files aren't already synced locally, `git pull` would get them; check `hebrew-ot/STEPBible-Data/` contents before re-cloning.

### OpenGNT — already fully on disk (`pseudepigrapha/OpenGNT/`)

Checked the local README: this is **Tier 3**, not apparatus data in the sense you asked about. It's a single eclectic "NA-equivalent" base text (built from Nestle 1904 + Berean Greek Bible + CNTR's own reconstructed BHP), with variant *markers* embedded for TR/BYZ/WH/SBL but not manuscript-level witness data. Confirms: nothing further to pull from this source for the apparatus goal — CNTR's `transcriptions` repo above is the right target instead.

---

## 6. Pre-1820 apparatus and editions (Tier 2) — the big find from this pass

These are old enough to satisfy the "pre-1820, no editorial reconstruction bias from later criticism" framing, and several are themselves *variant collations*, i.e. genuine old apparatus data:

| Work | MS(s) collated / reproduced | Edition date | Archive.org | Confirmed |
|---|---|---|---|---|
| **Kennicott, *Vetus Testamentum Hebraicum cum variis lectionibus*** | 600+ Hebrew MSS + 70 printed editions, collated against a reference text — **this is itself a pre-1820 critical apparatus**, ~1,400 of 1,800 pages are the collation | 1776–1780 (Oxford, 2 vols) | `https://archive.org/details/kennicott_vetus-testamentum-hebraicum-cum-variis-lectionibus-1776` | 200, djvu text layer resolves |
| **de Rossi, *Variae Lectiones Veteris Testamenti*** | Continuation/expansion of Kennicott's collation project, additional MSS + Samaritan + versions | 1784–1788 (Parma, 4 vols) | `https://archive.org/details/VariaeLectiones` | 200, djvu text layer resolves |
| **Woide, facsimile of Codex Alexandrinus NT** | Codex Alexandrinus (A02), c. 400–440 CE | 1786 | `https://archive.org/details/codexalexandrinu00woid` | 200 |
| **Kipling, *Codex Theodori Bezae Cantabrigiensis*** | Codex Bezae (D05), c. 400–500 CE | 1793 (Cambridge, 2 vols) | `https://archive.org/details/bezaecodexcanta00cambgoog` | 200, djvu text layer resolves |
| **Sixtine (Roman) Septuagint** | Codex Vaticanus (B, LXX portion), c. 300–325 CE | 1587 (Rome, commissioned by Sixtus V) | `https://archive.org/details/LATSEPT_DBS_HS` | 200 |
| **Grabe, *Septuaginta ex Codice Alexandrino*** | Codex Alexandrinus (A02, LXX portion), c. 400–440 CE | 1707–1720 (Oxford, 4 vols) | `https://archive.org/details/1730-the-alexandrian-greek-text-1` (vol. 1 of 4; the other 3 volumes were not individually re-verified this pass) | 200, djvu text layer resolves |
| **Erasmus, *Novum Instrumentum omne*** (1st ed. Textus Receptus) | Late Byzantine minuscules Erasmus had to hand in Basel — not a diplomatic transcription of any single old codex, but the founding printed edition of the whole TR line | 1516 | `https://archive.org/details/erasmustextusreceptus1stedition1516` | 200, djvu text layer resolves |
| **Stephanus 1550 / Elzevir 1633** | Same TR lineage as above, later refinements | 1550 / 1633 | Not individually verified this pass — flagged as a follow-up if you want the Stephanus/Elzevir texts specifically rather than just Erasmus | not checked |

All of these are public domain (pre-1900, most pre-1800). All confirmed to have OCR'd `_djvu.txt` text layers on archive.org where I checked (Kennicott, de Rossi, Kipling, Grabe vol.1, Erasmus) — meaning these are **usable as searchable text right now**, not just page-image scans, though OCR quality on 18th-century Latin/Hebrew/Greek typefaces will be rough and would need cleanup (same caveat your existing `nt-apocrypha/` Tischendorf OCR texts already carry).

**Important honesty note**: Kennicott and de Rossi are collations of *medieval* Hebrew manuscripts (11th–15th c. mostly), not of an ancient witness older than Leningrad — their value is as a large pre-1820 *apparatus*, not as access to an older base text than what you already have.

---

## Manifest — commands, by priority

```bash
# TIER 1 — primary witnesses, do these first

# Codex Sinaiticus (CC BY-NC-SA 3.0 — note non-commercial clause)
git clone https://github.com/itsee-birmingham/codex-sinaiticus.git manuscripts/sinaiticus
# or the official zip (~4.4MB): fetch https://codexsinaiticus.org/en/project/transcription_download.aspx and follow the link on that page

# Codex Zacynthius (bonus, CC BY 4.0)
git clone https://github.com/itsee-birmingham/codex-zacynthius-xml.git manuscripts/zacynthius

# Codex Bezae (CC BY 4.0)
git clone https://github.com/itsee-birmingham/codex-bezae.git manuscripts/bezae

# CNTR manuscript transcriptions — class 1/2/3 = Tier 1, critical texts/ = Tier 3, same repo (CC BY-SA 4.0)
git clone https://github.com/Center-for-New-Testament-Restoration/transcriptions.git manuscripts/cntr-transcriptions

# IGNTP John (Vaticanus/Alexandrinus/Washingtonianus, partial-to-complete per MS) — CC BY 4.0
# no single zip confirmed; pull per-manuscript from the transcription viewer:
#   https://itseeweb.cal.bham.ac.uk/iohannes/transcriptions/index.html
# IGNTP Pauline epistles (Galatians/Ephesians/Philippians) — CC BY 4.0
wget https://www.epistulae.org/downloads/Galatians_Greek_Transcriptions.zip -P manuscripts/igntp-pauline/
wget https://www.epistulae.org/downloads/Ephesians_Greek_transcriptions.zip -P manuscripts/igntp-pauline/
wget https://www.epistulae.org/downloads/Philippians_Greek_transcriptions.zip -P manuscripts/igntp-pauline/

# tanach.us UXLC — independent second transcription of Leningrad Codex
wget -r -np https://tanach.us/Pages/Technical.html   # inspect page for the actual zip link, then fetch that directly

# TIER 2 — pre-1820 editions/apparatus (all public domain, all confirmed resolving)
wget https://archive.org/download/kennicott_vetus-testamentum-hebraicum-cum-variis-lectionibus-1776/kennicott_vetus-testamentum-hebraicum-cum-variis-lectionibus-1776_djvu.txt -P manuscripts/pre-1820/
wget https://archive.org/download/VariaeLectiones/VariaeLectiones_djvu.txt -P manuscripts/pre-1820/
wget https://archive.org/download/codexalexandrinu00woid/codexalexandrinu00woid_djvu.txt -P manuscripts/pre-1820/
wget https://archive.org/download/bezaecodexcanta00cambgoog/bezaecodexcanta00cambgoog_djvu.txt -P manuscripts/pre-1820/
wget https://archive.org/download/1730-the-alexandrian-greek-text-1/1730-the-alexandrian-greek-text-1_djvu.txt -P manuscripts/pre-1820/
wget https://archive.org/download/erasmustextusreceptus1stedition1516/erasmustextusreceptus1stedition1516_djvu.txt -P manuscripts/pre-1820/
# LATSEPT_DBS_HS (Sixtine LXX 1587) — check archive.org item for the actual identifier suffix on its djvu file before fetching

# TIER 3 — modern reconstructions / tooling, lowest priority, listed for completeness
git clone https://github.com/SCDH/intf-cbgm.git manuscripts/tools/intf-cbgm
git clone https://github.com/jjmccollum/open-cbgm.git manuscripts/tools/open-cbgm
# NTVMR API (CC BY 4.0, live, tested) — per-manuscript pull, no bulk endpoint:
# http://ntvmr.uni-muenster.de/community/vmr/api/transcript/get/?docID=<id>&indexContent=<ref>&fullPage=true&format=teiraw
```

---

## BLOCKED — copyrighted, confirmed, no change from your existing decision

| Item | Why blocked | Any open carve-out? |
|---|---|---|
| **ECM (Editio Critica Maior)**, full apparatus | Deutsche Bibelgesellschaft copyright, explicit "no downloading/modification" terms on die-bibel.de | **Partial**: digital ECM Acts apparatus is free-to-query via NTVMR (`nt-transcripts` interface / API), released by INTF at SBL 2017. Everything beyond Acts: no evidence of open release. |
| **NA28 / UBS5 base text and apparatus** | Same publisher, same terms | None found. SBLGNT (already on disk) remains the closest free equivalent, as your INDEX already notes. |
| **Aleppo Codex, machine-readable transcription** | Not blocked by copyright so much as **it doesn't exist publicly** — every source I found is page-images-only (Ben-Zvi Institute site under construction, Bar-Ilan's mgketer.org is images + Israeli copyright notice, Internet Archive is images) | None found this pass. |

---

## Open threads not fully chased (say so rather than guess)

- Codex Washingtonianus: no pre-1820 edition exists (discovered 1906); did not locate a clean digitized *text* of the 1912 Sanders edition, only facsimile images — worth one more targeted search if you want it.
- Grabe's LXX volumes 2–4 (of 4) — only volume 1's archive.org identifier was individually re-verified; the set exists but I didn't re-check all four links.
- Stephanus 1550 / Elzevir 1633 archive.org identifiers — not individually verified this pass, only Erasmus 1516 was.
- tanach.us's exact zip URL and its stated license terms — page structure suggests it's in the TEI header of the download itself, I did not download it to read that header (per your no-bulk-download-during-research constraint).
- NTVMR's specific license for the free-Acts-ECM-apparatus subset — likely CC BY 4.0 via the general NTVMR terms, but I did not find a document stating that explicitly for this one dataset.
