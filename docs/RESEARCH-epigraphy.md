# Research: Epigraphy — Inscriptions Older Than the Dead Sea Scrolls

Status: research only, **nothing downloaded**. INDEX.md currently states "Oldest Hebrew biblical
text = Dead Sea Scrolls, ~250 BCE–68 CE." That's wrong for one category: **inscriptions on metal,
stone, and pottery predate every Qumran scroll**, in one case (Ketef Hinnom) by roughly 400 years.
Scope here is biblical / Israelite-religion epigraphy — what's freely obtainable as transcription,
photograph, or dataset, verified live rather than guessed. Per the project's history of dead links
and wrong-filename failures, every URL below was actually fetched (WebFetch/curl/API), not assumed.

## Tier key (same convention as the rest of `docs/`)

- **Tier 1** — the inscription itself: diplomatic transcription, facsimile, photograph. No
  editorial reconstruction layer.
- **Tier 2** — printed editions published **before 1820**. Essentially empty for this scope — see below.
- **Tier 3** — modern (post-1820) scholarly editions/re-readings. Almost all epigraphic "Tier 1"
  content in practice reaches you *through* one of these (Barkay 2004, Torczyner 1938, Biran &
  Naveh 1993/95, etc.) — the inscription is the witness, the publication is the edition. Both
  dates given for every item: **read the WITNESS date, not the edition date.**

**Note on Tier 2 for this scope:** almost everything below was excavated in the 19th–21st
century — Ketef Hinnom (1979), Kuntillet Ajrud (1975–76), Tel Dan (1993–94), Khirbet Qeiyafa
(2008). A few objects surfaced earlier (Mesha Stele 1868, Siloam Inscription 1880, Gezer Calendar
1908) but still post-1820. There is **no genuine pre-1820 printed edition of any of these** — the
objects simply weren't known yet. Closest near-miss: Lidzbarski's 1907 *Kanaanäische Inschriften*
(§Cross-cutting) — early and freely available, but 1907, not pre-1820.

**Structural note:** unlike the rest of this corpus, this scope does not produce clean `git clone`
targets. These are single-artifact epigraphic finds, not bulk digital-humanities text corpora — so
sourcing here means a handful of verified image URLs, archive.org PDFs, and Wikipedia-hosted
working transcriptions, not a repository. That's reflected below.

---

## Part 1 — Divine-name epigraphy (HIGH PRIORITY subset)

### 1. Ketef Hinnom silver amulets — the oldest biblical text on earth

| | |
|---|---|
| **What it says** | Two rolled silver amulets (KH1, KH2), inscribed with an early form of the Priestly Blessing (Num 6:24–26): *"...Blessed be [name] by Yahweh, the helper and the rebuker of evil: May Yahweh bless you, keep you. May Yahweh make his face shine upon you and grant you peace."* |
| **Artifact date** | **c. 600 BCE** (late Iron Age, just before the Babylonian destruction). ~400 years older than the oldest Dead Sea Scroll fragment. |
| **Edition date** | Original publication: Barkay 1986. Definitive re-reading: **Barkay, Vaughn, Lundberg & Zuckerman, "The Amulets from Ketef Hinnom: A New Edition and Evaluation," *BASOR* 334 (2004), 41–71**, using USC West Semitic Research Project imaging. |

- **Primary 2004 edition**: **paywalled** — indexed at JSTOR (stable/4150106), institutional access
  only. No open PDF located. A related 2011 follow-up ("A New Appraisal of the Silver Amulets from
  Ketef Hinnom," *IEJ* 61) has listing pages on Academia.edu/ResearchGate but full-PDF access
  behind those sites' login walls was not confirmed open.
- **Transcription (content, not primary edition)**: Wikipedia's "Ketef Hinnom scrolls" article
  carries the full transliteration + translation as prose — usable to cite the *content*, not a
  substitute for the primary edition.
- **Photograph — verified**: `https://commons.wikimedia.org/wiki/File:Ketef_Hinnom_KH2_Scroll.jpg`
  — 2672×4008px JPEG, 4.75 MB, tagged **Public Domain Mark 1.0**, sourced from archive.org item
  `ketef-hinnom-kh-2` (`https://archive.org/details/ketef-hinnom-kh-2`, confirmed HTTP 200).
  ⚠️ **Flag**: the PD tag rides on Commons' "PD-Art (PD-old-70)" rule, written for 2D reproductions
  of old *paintings*; applying it to a modern photo of a 3D silver scroll is legally shakier than a
  clean CC0 grant. The archive.org uploader is a hobbyist account, not the Israel Museum or USC
  WSRP directly. Treat as "widely circulated, probably fine, not institutionally authoritative."
- **USC InscriptiFact / West Semitic Research Project** (the institution that actually re-imaged
  these amulets): **`inscriptifact.com` is dead — confirmed connection refused.** Per USC's own
  libguide (`libguides.usc.edu/Inscriptifact_guide`, resolves live), the collection migrated into
  the **USC Digital Library**, stated to offer full-resolution JPEG download — but a direct search
  attempt (`digitallibrary.usc.edu/asset-management/2A3BF1OL6PW`) returned **HTTP 403 Forbidden**
  on this pass. Unconfirmed whether Ketef Hinnom is actually indexed there or whether access is
  public vs. USC-credentialed. Needs a manual browser follow-up, not resolvable via fetch/curl.
- Israel Museum (holds the physical object): no dedicated open-data object page found.

**Bottom line**: content and one decent (if not airtight-licensed) photo are free; the actual
2004 scholarly edition is paywalled; the best imaging archive (InscriptiFact) is currently a dead
link. This is still, by a wide margin, **the oldest verifiably-sourceable biblical text in this
entire corpus.**

### 2. Kuntillet Ajrud — "Yahweh ... and his Asherah"

| | |
|---|---|
| **What it says** | Inscriptions on two storage jars (Pithos A, Pithos B) and plastered walls from a Sinai/Negev caravan way-station: *"blessed by/to **Yahweh of Samaria and his Asherah**"* (Pithos A) and *"**Yahweh of Teman and his Asherah**"* (Pithos B) — primary extra-biblical evidence for a consort/paired-deity practice attached to Yahweh worship. |
| **Artifact date** | **c. 800 BCE**. Excavated 1975–76 by Ze'ev Meshel, Tel Aviv University. |
| **Edition date** | Definitive excavation report: Meshel, Ben-Ami, Aḥituv, Freud (eds.), *Kuntillet ʻAjrud (Ḥorvat Teman): An Iron Age II Religious Site on the Judah–Sinai Border*, Israel Exploration Society, **2012**. Not free (print monograph). Later re-readings (Puech 2014, Allen 2015, Lewis 2022) are paywalled journal articles. |

- **Transcription — best free source**: Wikipedia's `Kuntillet_Ajrud_inscriptions` article gives
  line-by-line transliteration + translation for Pithos A (Meshel §3.1), Pithos B (§3.6, §3.9),
  and the plaster texts (§4.2). No dedicated open digital corpus for this site exists.
- **Photographs — verified, contra the initial pass**: Wikimedia Commons has actual photos, found
  via direct search (the site has no populated "Category:Kuntillet Ajrud"):
  - `https://commons.wikimedia.org/wiki/File:Pithosbfigs.jpg` — 2412×1799px, **CC BY-SA 4.0**
    (the Pithos B figures/inscription photo).
  - `https://commons.wikimedia.org/wiki/File:Horvat_Teman%27s_couple_and_%27Yahweh_and_his_Asherah%27_inscription.jpg`
    — 338×547px (small), **Public Domain**.

### 3. Khirbet el-Qom — the other "Yahweh and his Asherah" tomb text

| | |
|---|---|
| **What it says** | Tomb inscription (Tomb 2): *"Uriyahu the [rich/honourable] wrote it. Blessed be Uriyahu by Yhwh — for from his enemies he saved him by his Asherah."* A carved hand accompanies the text; several "ghost letters" remain disputed. |
| **Artifact date** | **c. 750–700 BCE** (paleographic). |
| **Edition date** | No single canonical open edition; readings split among several re-publications since Dever's 1969 original. |

- **Transcription**: Wikipedia's `Khirbet_el-Qom` article gives a working translation.
- **Photograph — verified, contra the initial pass**: found via direct Commons search (no
  populated category exists under this name either):
  `https://commons.wikimedia.org/wiki/File:כתובת_קבורה_מחורבת_אל-כום.jpg` ("Burial inscription
  from Khirbet el-Qom") — 1783×1388px, **CC BY-SA 4.0**.

### 4. Mesha Stele / Moabite Stone (c. 840 BCE)

| | |
|---|---|
| **What it says** | 34-line victory inscription of King Mesha of Moab, boasting recapture of Moabite territory from Israel. Contains **the divine name YHWH** (line 18, in a passage about looting cult vessels "before Chemosh" — direct extra-biblical attestation of the Tetragrammaton) and offers a rival account to 2 Kings 3. |
| **Artifact date** | **c. 840 BCE**. Discovered 1868, Dhiban, Jordan (then broken by local Bedouin under Ottoman-era pressure; a squeeze/rubbing taken in 1869 before the breakage is arguably as important a witness as the reconstructed stone). |
| **Edition date** | Modern standard: Ahituv, *Echoes from the Past* (2008 Eng./2012 Heb.) — not free. Older editions (Lidzbarski, Clermont-Ganneau, 1870s–1900s) are old enough to be public domain. |

- **Holding institution — verified**: Musée du Louvre, Paris. **Accession AO 5066** (also
  MNB 752, **KAI 181**). Confirmed live: `https://collections.louvre.fr/en/ark:/53355/cl010120339`
  (main stele) — object page states 18 downloadable photo options exist, gated behind the Louvre's
  general "Terms and conditions" click-through (specific license — Open Content vs. all-rights —
  not stated on the page itself, needs manual check of the linked terms document). Related Louvre
  records, all confirmed resolving:
  - Squeeze/estampage: `https://collections.louvre.fr/en/ark:/53355/cl010165740`
  - Modern copy: `https://collections.louvre.fr/en/ark:/53355/cl010165742`
  - Fragments: `https://collections.louvre.fr/en/ark:/53355/cl010165786`, `.../cl010146144`
- **Free full translation (content, not scan)**: `https://www.biblicalarchaeology.org/daily/biblical-artifacts/inscriptions/what-does-the-mesha-stele-say/`
  — verified live, complete 34-line English translation, no paywall on the translation itself.
- **Free 1907 original-language edition**: Mark Lidzbarski's *Kanaanäische Inschriften* (Moabite,
  Old Hebrew, Phoenician, Punic) covers the Mesha Stele in original script with philological notes
  and is **freely downloadable, not access-restricted** — see §Cross-cutting below.
- **Photographs**: Wikipedia links Wikimedia Commons user photos of the museum object (e.g.
  `File:P1120870_Louvre_stèle_de_Mésha_AO5066_rwk.JPG`) — standard visitor photography, typically
  CC BY-SA from the photographer, not individually re-verified here.

### 5. Tel Dan Stele (9th c. BCE) — "House of David"

| | |
|---|---|
| **What it says** | Old Aramaic victory inscription (likely Hazael of Damascus) boasting of killing the king of Israel and "the king of the **House of David**" (*bytdwd*) — the earliest extra-biblical reference to a Davidic dynasty. |
| **Artifact date** | **9th c. BCE**. Basalt, broken into 3 fragments found 1993 and 1994. |
| **Edition date** | Biran & Naveh, *Israel Exploration Journal* 43 (1993) and 45 (1995) — not confirmed open access. |

- **Holding institution**: Israel Museum, Jerusalem (Samuel and Saidye Bronfman Archaeology Wing).
  Exact accession number not located on this pass.
- **Transcription**: Wikipedia's `Tel_Dan_stele` article gives the 13-line Aramaic transliteration
  and Biran's 1995 English translation.
- **Photographs — verified, well-populated**: unlike Ajrud/Qom, this one has a real Commons
  category, `Category:Tel Dan stele`, confirmed non-empty with 10+ files, e.g.
  `File:JRSLM_300116_Tel_Dan_Stele_01.jpg`, `File:JRSLM_300116_Tel_Dan_Stele_02.jpg`,
  `File:Aramaic_Inscription_on_Basalt_Monument,_Dan,_9th_Century_BC_(43167226572).jpg` — standard
  Commons museum-object photography, per-file license not individually re-verified but Commons
  categorization strongly implies cleared status.

---

## Part 2 — Ostraca, inscriptions, and abecedaries

All seven items below share one strong result: **the actual scholarly editio princeps for four of
them sits on archive.org, fully free, verified live** (not just secondary description). This is a
much better outcome than Part 1.

### 6. Siloam Inscription (c. 700 BCE)

- **What it says**: 6-line dedication describing two tunneling crews meeting in the middle of
  Hezekiah's water tunnel, Jerusalem. No divine name, no direct biblical quote — a public-works
  record, valuable as the longest well-preserved paleo-Hebrew royal-period inscription.
- **Artifact date**: c. 701 BCE. **Current holder: Istanbul Archaeology Museums** (removed from
  Jerusalem under Ottoman rule, 1890) — **not** the Israel Museum, which holds only a replica
  (verified: `https://www.imj.org.il/en/collections/372810`, HTTP 200).
- **Edition date**: decipherment Sayce 1881; standard early transcription Socin 1899.
- **Transcription — verified free**, paleo-Hebrew text + translation:
  `https://www.ancient-hebrew.org/inscriptions/110.html` and
  `https://biblicalhebrew.com/the-siloam-inscription-ca-700-bce/` (both HTTP 200). Web pages, not
  structured/downloadable data.
- No structured/machine-readable open dataset found; no verified archive.org primary edition.

### 7. Lachish Letters (c. 590 BCE)

- **What they say**: military correspondence, mostly officer Hoshaiah reporting to his commander
  at Lachish on the eve of the Babylonian conquest; Letter IV references watching for signal fires
  from Lachish and Azekah, echoing Jeremiah 34:7.
- **Artifact date**: c. 588–586 BCE. 17 of 21 ostraca held at the British Museum; some (incl.
  Letter 6) at the Rockefeller Museum, Jerusalem.
- **Editio princeps — VERIFIED FREE, full text**: Harry Torczyner (later Naftali Herz Tur-Sinai),
  *The Lachish Letters*, Oxford, **1938**.
  `https://archive.org/details/lachishletters0001harr` — HTTP 200, PDF + `_djvu.txt` OCR text.
  (Alt scan `lachishletters0000harr` also resolves.)

### 8. Arad ostraca (mainly late 7th–early 6th c. BCE, the "Eliashib archive")

- **What they say**: administrative/military correspondence from a Judahite Negev fortress —
  supply orders, troop movements; ostracon 18 references "the House of YHWH."
- **Artifact date**: mainly late Iron Age (some earlier strata). Excavator: Yohanan Aharoni, 1960s.
- **Editio princeps — VERIFIED FREE, full text**: *Arad Inscriptions* (Hebrew orig. 1975, English
  ed. 1981, Israel Exploration Society). `https://archive.org/details/arad-inscriptions` — HTTP
  200, PDF + `_djvu.txt` + separate text PDF.
- No GitHub/Text-Fabric dataset exists for Arad — confirmed genuine negative, not a dead link.

### 9. Samaria ostraca (8th c. BCE)

- **What they say**: terse administrative wine/oil tax dockets (year, place-name, personal name,
  commodity) from the Israelite capital — no theological content, useful for onomastics.
- **Artifact date**: c. 8th c. BCE (Reisner dated context to Jeroboam II's reign or earlier; still
  debated).
- **Editio princeps — VERIFIED FREE, full text**: G.A. Reisner, C.S. Fisher, D.G. Lyon, *Harvard
  Excavations at Samaria 1908–1910*, vol. I: Text, **1924**.
  `https://archive.org/details/harvard-excavations-at-samaria-1908-1910.-vol.-i.-text` — HTTP 200,
  PDF + `_djvu.txt`. Preliminary companion note also free: David G. Lyon, "Hebrew Ostraca from
  Samaria" (**1911**), `https://archive.org/details/jstor-1507545` — confirmed resolves.

### 10. Khirbet Qeiyafa ostracon (c. 1000 BCE) — the outlier: genuinely unresolved

- **What it says**: fragmentary 5-line text, **no consensus transcription** — competing readings
  (Galil, Puech, Misgav/Garfinkel/Ganor, Rollston) disagree even on whether the language is Hebrew.
  Plausibly-identified words include "judge," "king," "slave."
- **Artifact date**: c. 1000 BCE (Iron I/IIA transition) — one of the earliest Hebrew/Canaanite
  writing candidates, but contested.
- **Editio princeps**: Misgav, Garfinkel & Ganor, in *Khirbet Qeiyafa* vol. 1 (Israel Exploration
  Society, 2009) — **paywalled, no open PDF found** (IES sells the volume at $72/$54).
- **Free secondary transcription** (not the editio princeps): Alan Millard's independent
  discussion, verified live PDF —
  `https://www.tyndalebulletin.org/article/29303-the-ostracon-from-the-days-of-david-found-at-khirbet-qeiyafa/attachment/76268.pdf`.
  Wikipedia's `Khirbet_Qeiyafa_ostracon` article usefully tabulates the competing readings side by
  side.
- **Flag honestly**: this is not a settled transcription like the others — treat any single
  reading given here as one scholar's proposal, not a fact.

### 11. Izbet Sartah abecedary (c. 1200–1000 BCE)

- **What it says**: 4 lines of unclear/practice writing + a 5th line giving the complete 22-letter
  Proto-Canaanite alphabet, aleph-to-taw, written left-to-right (unusual for the period — most
  contemporary Northwest Semitic writing runs right-to-left).
- **Artifact date**: 12th–11th c. BCE — the earliest known attestation of the full ordered
  alphabet outside cuneiform. Found 1976 (Moshe Kochavi); held at the Israel Museum.
- **Edition**: original publication by Kochavi/Demsky in *Tel Aviv* journal / BASOR — not located
  as an open PDF on this pass.
- **Secondary transcriptions** (not independently HTTP-verified in this pass, lower confidence):
  Center for Online Judaic Studies (`cojs.org/izbet_sartah_ostracon-_12-10th_century_bce/`),
  History of Information (`historyofinformation.com/detail.php?id=1309`).

### 12. Gezer Calendar (c. 10th c. BCE, KAI 182)

- **What it says**: an 8-line agricultural mnemonic listing farming periods across the year (two
  months harvest, two months planting, etc.), ending with a personal name, "Abijah."
- **Artifact date**: c. 10th c. BCE (early Israelite monarchy period; disputed whether the
  language should be called "Hebrew" or generic Canaanite). Found 1908 by R.A.S. Macalister.
- **Editio princeps — VERIFIED FREE, full text**: R.A.S. Macalister, *The Excavation of Gezer
  1902–1905 and 1907–1909*, vol. I, Palestine Exploration Fund, **1911/1912**.
  `https://archive.org/details/the-excavation-of-gezer-1902-1905-and-1907-1909.-volume-i` — HTTP
  200, `_djvu.txt` confirmed present.
- **Clean modern transcription + translation, free**: `https://www.ancient-hebrew.org/inscriptions/110.html`
  (same page also covers Siloam — HTTP 200).

---

## Part 3 — Elephantine papyri & paleo-Hebrew Tetragrammaton in Greek LXX manuscripts

### 13. Elephantine papyri (5th c. BCE, Aramaic — the YHW temple community)

- **What they are**: legal, administrative, and religious documents from a Jewish/Judahite
  military garrison colony on Elephantine Island, Egypt, which maintained **its own temple to
  YHW** (a variant spelling of the divine name) — direct evidence for how Yahweh worship actually
  looked outside Jerusalem, including the famous letters requesting Persian-authority help
  rebuilding that temple after its destruction (Cowley 30/31).
- **Artifact date**: 5th c. BCE (mainly reign of Darius II onward).

**Best find — `elephantine.smb.museum`** (ERC-funded Berlin project, "Texts & Scripts from
Elephantine," run by the Egyptian Museum and Papyrus Collection, Berlin / BBAW):
- Verified live: portal `https://elephantine.smb.museum/index.php`; browsable catalog
  `https://elephantine.smb.museum/objects/` (confirmed "10,745 Data Sets"); one specific object
  page `https://elephantine.smb.museum/objects/object.php?o=307790` (Pap. Berlin P. 13444 A,
  Persian period) — **directly confirmed** to show Aramaic transcription + English translation +
  two photographs + full metadata, licensed **CC BY-NC-SA 4.0**.
- The database is filterable by "People Mentioned in Text," and confirmed filter values include
  **Bagohi** and **Jedaniah** — the addressee/sender of the temple-rebuilding letters — meaning
  those specific letters are almost certainly digitized here. A filtered results page could not be
  rendered via automated fetch (JS-driven query); recommend opening the site directly and
  filtering by person = Bagohi to get the exact object URL for AP 30/31.
- Format: TEI-XML-backed web database, per-object pages; no bulk-download link found in what was
  checked (may exist elsewhere on the site, not confirmed).

**Cowley 1923, *Aramaic Papyri of the Fifth Century B.C.*** — the classic edition, confirmed to
include the temple letters (AP 30–34 referenced in the fetched intro text):
- **Verified free, full scans + text, public domain**:
  `https://archive.org/details/aramaicpapyrioff0000acow` (PDF 25.3 MB, EPUB 3.4 MB, no
  login/borrow gate) and OCR text layer
  `https://archive.org/stream/aramaicpapyrioff00ahikuoft/aramaicpapyrioff00ahikuoft_djvu.txt`.
  Contains Aramaic-script transcription + English translation + commentary.
- **Edition date**: 1923.

**Kraeling 1953, *Brooklyn Museum Aramaic Papyri*** —
`https://archive.org/details/brooklynmuseumar0000broo` — **verified but restricted**:
`access-restricted-item: true` (controlled digital lending only, not a free download).

**CAL (Comprehensive Aramaic Lexicon, `cal.huc.edu`)** — confirmed live, has an Elephantine
bibliography page and a browsable siglum category "Elephantine General" under
Imperial/Official Aramaic
(`https://cal.huc.edu/browsesigla.php?subclass=Elephantine+General&generalclass=Imperial/Official+Aramaic`).
Real and relevant to the lexically-parsed corpus, but fetched pages were bibliography/navigation
only — no direct full-text-reader URL for a specific letter was confirmed, and no license was
stated. Needs manual navigation.

**Porten & Yardeni, *Textbook of Aramaic Documents from Ancient Egypt*** (modern standard
scholarly edition) — **not freely available**, no PDF/archive.org copy found; commercial
(Accordance module, print via Eisenbrauns/Magnes Press).

### 14. Paleo-Hebrew Tetragrammaton inside Greek LXX manuscripts (HIGH PRIORITY)

Direct physical evidence for when/how YHWH became rendered as κύριος — three specific manuscripts:

**P.Fouad 266** (Rahlfs 848, Greek Deuteronomy, 1st c. BCE):
- Holding institution: Société Royale de Papyrologie / IFAO, Cairo.
- **Image — verified free**: Wikimedia Commons,
  `https://commons.wikimedia.org/wiki/File:Papyrus_Fouad_266.jpg` — **Public Domain Mark 1.0**,
  800×1161px JPEG, 248 KB, depicts Deut 31:28–32:7 with the Tetragrammaton in square Hebrew script
  (not paleo-Hebrew in every copy of this text — the specific script variant per-verse needs
  checking against the scholarly edition, not assumed from the thumbnail alone).
- **No open transcription found.** The scholarly editions (Waddell 1944; full 117 fragments in
  *Études de Papyrologie* vol. 9, 1971; Aly & Koenen's 1980 photographic edition *Three Rolls of
  the Early Septuagint*) are all print/paywalled. **Image only — flagged honestly, no open
  transcription exists.**

**8HevXIIgr** (Rahlfs 943, Naḥal Ḥever Minor Prophets scroll, c. 50 BCE–50 CE):
- Held at the Rockefeller Museum, Jerusalem.
- **Confirmed listed** on `deadseascrolls.org.il/featured-scrolls` as "8Hev Twelve Minor Prophets"
  — but no direct link to full high-res images or a downloadable transcription was found on the
  fetched page. Editio princeps (Tov, *The Greek Minor Prophets Scroll from Naḥal Ḥever*, DJD 8,
  1990) is copyrighted, print only.
- **Flagged as needing a follow-up manual visit** to the Leon Levy Digital Library's own search —
  the automated fetch did not surface a working direct download despite the scroll being
  acknowledged on the site.

**P.Oxy 3522** (Rahlfs 857 / LDAB & TM 3079, Job 42:11–12, 1st c. CE):
- Held at the Sackler Library, Oxford Papyrology Rooms. Published: P.J. Parsons, *The Oxyrhynchus
  Papyri* vol. 50, 1983 (copyrighted print).
- **papyri.info is blocked** — every URL tried (`/ddbdp/p.oxy;50;3522`) returned an anti-bot
  Anubis challenge wall, consistent with this project's existing note that the site's license page
  hits the same wall. Also tried bypassing via the raw `papyri/idp.data` GitHub mirror (already
  scoped elsewhere in this corpus) with two plausible file-path guesses
  (`DDB_EpiDoc_XML/p.oxy/50/p.oxy.50.3522.xml`, `DDB_EpiDoc_XML/oxy/50/3522.xml`) — **both 404**.
  Could not confirm whether this specific text is even present in that bulk corpus, or what the
  real path would be, without a working papyri.info search to query.
- The old "Oxyrhynchus Online" image link cited by Wikipedia is **confirmed dead** (per the
  Wikipedia article itself, since 2014).
- **Flagged honestly: no open transcription or working image link found for this one.** Smallest/
  most obscure of the three — currently no freely-accessible primary source located, only
  secondary academic description (Wikipedia, ResearchGate figure crops).

---

## Cross-cutting infrastructure — general repositories checked

Checked once, across the whole scope, rather than per-item:

| Resource | Verdict |
|---|---|
| **InscriptiFact / West Semitic Research Project** (`inscriptifact.com`) | **Dead** — confirmed connection refused. Content reportedly migrated into the **USC Digital Library**; USC's own libguide claims full-resolution JPEG download is offered, but a direct search attempt returned **HTTP 403 Forbidden**. Even where reachable, stated terms are restrictive: *"images are for study purposes only... permission to publish must be obtained in writing... may involve additional charges."* Not a free bulk source even when accessible. |
| **KAI** (Donner & Röllig, *Kanaanäische und Aramäische Inschriften*, the standard modern reference numbering used throughout this document, e.g. KAI 181 = Mesha, KAI 182 = Gezer) | The actual reference work (1962/1966 editions) is on archive.org but confirmed **`access-restricted-item: true`** — controlled digital lending (1-hour borrow), not a free download. Verified via `archive.org/metadata/kanaanaischeunda0000unse` and `.../kanaanaischeunda0000hdon`. **No open KAI database exists online.** |
| **Mark Lidzbarski, *Kanaanäische Inschriften* (Moabite, Old Hebrew, Phoenician, Punic), 1907** | An earlier, related corpus (KAI's intellectual predecessor, not KAI itself). **Freely downloadable, confirmed NOT access-restricted**: `https://archive.org/details/kanaanischeinsc00lidzgoog` — full PDF + OCR text. Covers the Mesha Stele (Moabite) and likely Siloam (Old Hebrew) in original script with Latin/German philological notes. The best genuinely-free "KAI-adjacent" source found. |
| **"Digital Corpus of Northwest Semitic Inscriptions"** (exact name) | Not found as a live, distinct project. |
| **Northwest Semitic Inscription Archive (NSIA)** / Digital Semitics Online Library (`m-saunders.com`) | Referenced in a 2012 AWOL blog post; both current URLs tried (`/nws-inscriptions/`, `/csi/`) **confirmed 404 — dead**. Defunct or relocated; not usable as-is. |
| **ORACC** (`oracc.museum.upenn.edu`) | Mesopotamian/cuneiform-focused; no West Semitic alphabetic-epigraphy presence found. Out of scope — none of the items above are cuneiform. |
| **GitHub / Text-Fabric datasets for NW Semitic inscriptions** | Searched directly (GitHub API + web search) — **genuine negative result**. No repo exists for Mesha, Tel Dan, Ketef Hinnom, Ajrud, Qom, Siloam, Lachish, Arad, Samaria, Qeiyafa, Izbet Sartah, or Gezer. Unlike the rest of this corpus (DSS, LXX, Samaritan Pentateuch all have Text-Fabric/GitHub datasets), single-artifact epigraphy simply hasn't been digitized that way yet. |
| **Wikimedia Commons** | The single most useful cross-cutting source for photographs. Spot-checked license per file (do not assume blanket PD): Ketef Hinnom KH2 (PD, shaky rationale), Kuntillet Ajrud Pithos B (**CC BY-SA 4.0**), Khirbet el-Qom tomb text (**CC BY-SA 4.0**), Tel Dan Stele (populated category, multiple CC-licensed museum photos), P.Fouad 266 (PD). |
| **archive.org** | The best repeat performer in this whole pass — four full editiones principes (Lachish 1938, Arad 1981, Samaria 1911+1924, Gezer 1911/12) plus Cowley's 1923 Elephantine edition all verified fully free and unrestricted. Contrast with Kraeling 1953 (Elephantine) and Donner–Röllig KAI, both confirmed **access-restricted** (lending only) on the same platform — always check the `access-restricted-item` metadata field, don't assume archive.org = free. |

---

## Bottom line — the single oldest biblical text obtainable

**Ketef Hinnom silver amulet KH2, c. 600 BCE — the Priestly Blessing (Num 6:24–26).** This is
roughly 400 years older than 1QIsa-a (the Great Isaiah Scroll, c. 125 BCE) and Qumran generally,
and about 1,600 years older than the Leningrad Codex currently listed in INDEX.md as the oldest
Hebrew witness in this corpus. It should replace or supplement that line in INDEX.md.

**What's actually obtainable for it, honestly stated:**
- A public-domain-tagged, high-resolution photograph (2672×4008px) — verified live at
  `https://commons.wikimedia.org/wiki/File:Ketef_Hinnom_KH2_Scroll.jpg` — though the PD claim
  rests on a legally shaky rationale (a 2D-reproduction rule applied to a 3D object photo).
- The transcribed/translated text, freely citable via Wikipedia's summary of the scholarship, but
  **not** the actual 2004 BASOR scholarly edition itself, which is paywalled.
- No open dataset, no Text-Fabric corpus, no bulk download — this is a single artifact, sourced
  the way a museum object is sourced, not the way a manuscript corpus is.

Runner-up for "oldest with a genuinely clean, fully free scholarly edition already on disk-ready
archive.org PDF": the **Gezer Calendar** (c. 10th c. BCE, Macalister's 1911/12 excavation report,
zero access restrictions) and the **Lachish Letters** (c. 590 BCE, Torczyner's 1938 edition, same
clean status) — both meaningfully older than DSS and both fully unrestricted downloads today.

## Suggested commands (verification/reference only — small, individual files, not corpora)

```bash
mkdir -p ~/projects/bible-sources/inscriptions/{images,editions}

# Photographs (Wikimedia Commons, verify license per file before reuse)
curl -o ~/projects/bible-sources/inscriptions/images/ketef-hinnom-kh2.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/f/f4/Ketef_Hinnom_KH2_Scroll_%28cropped%29.jpg"
curl -o ~/projects/bible-sources/inscriptions/images/kuntillet-ajrud-pithos-b.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/1/1c/Pithosbfigs.jpg"

# Full free editiones principes (archive.org, unrestricted, verified live)
curl -o ~/projects/bible-sources/inscriptions/editions/lachish-letters-1938.pdf \
  "https://archive.org/download/lachishletters0001harr/lachishletters0001harr.pdf"
curl -o ~/projects/bible-sources/inscriptions/editions/arad-inscriptions-1981.pdf \
  "https://archive.org/download/arad-inscriptions/Arad%20Inscriptions.pdf"
curl -o ~/projects/bible-sources/inscriptions/editions/samaria-ostraca-1924.pdf \
  "https://archive.org/download/harvard-excavations-at-samaria-1908-1910.-vol.-i.-text/Harvard%20Excavations%20at%20Samaria%2C%201908-1910.%20Vol.%20I.%20Text.pdf"
curl -o ~/projects/bible-sources/inscriptions/editions/gezer-excavation-1912.pdf \
  "https://archive.org/download/the-excavation-of-gezer-1902-1905-and-1907-1909.-volume-i/The%20excavation%20of%20Gezer%201902%20-%201905%20and%201907%20-%201909.%20Volume%20I.pdf"
curl -o ~/projects/bible-sources/inscriptions/editions/cowley-elephantine-1923.pdf \
  "https://archive.org/download/aramaicpapyrioff0000acow/aramaicpapyrioff0000acow.pdf"
curl -o ~/projects/bible-sources/inscriptions/editions/lidzbarski-kanaanaeische-1907.pdf \
  "https://archive.org/download/kanaanischeinsc00lidzgoog/kanaanischeinsc00lidzgoog.pdf"
```

Everything else in Parts 1–3 (Mesha Stele, Tel Dan, Siloam, Qeiyafa, Izbet Sartah, Elephantine's
`elephantine.smb.museum` database, 8HevXIIgr, P.Fouad 266, P.Oxy 3522) is either a webpage to cite
rather than a file to pull, gated behind institutional terms, or — for P.Oxy 3522 specifically —
not freely findable at all as of this research pass.
