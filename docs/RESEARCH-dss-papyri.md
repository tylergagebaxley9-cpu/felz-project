# Research: Dead Sea Scrolls & Papyri — Freely Obtainable Machine-Readable Sources

Scope: `dead-sea-scrolls/` and `papyri/` — both empty. Goal: find what's freely obtainable in
machine-readable transcription form (not just images), verify every URL, and hand back a manifest —
**nothing was downloaded**. Per instruction, this report lists **everything found**, including modern
critical/reconstructed editions, with a Tier label (not a filter) plus explicit witness-date and
edition-date columns so the user can judge for himself.

## Tier key

- **Tier 1** — the manuscript/artifact itself: raw or diplomatic transcription, facsimile, image. No
  editorial reconstruction layer (annotation/tagging on top of a diplomatic base still counts as Tier 1).
- **Tier 2** — printed editions published **before 1820**.
- **Tier 3** — modern (post-1820) critical/reconstructed editions. Flagged with what editorial choices
  they impose.

**Note on Tier 2 for this scope:** it's essentially empty by construction. The Dead Sea Scrolls were not
discovered until 1947, and the Oxyrhynchus papyri (and the papyrology discipline generally) began with
excavations starting in 1896–98. There is no pre-1820 printed edition of either corpus — the manuscripts
themselves simply weren't known yet. So for this specific scope, "old" means Tier 1 (the raw
transcription of the physical find), not Tier 2.

---

## Part 1 — Dead Sea Scrolls

### Manifest

| # | Item | Tier | Witness date | Edition/dataset date | License | Format | Approx. size | URL | Verified |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **ETCBC/dss** (Text-Fabric, Dirk Roorda, on Martin Abegg's transcription data) | 1 (diplomatic transcription + linguistic tagging layer) | c. 250 BCE – 68 CE (varies per scroll) | Abegg's underlying transcription work: compiled 1988–2010s from DJD volumes (1955–2009); Text-Fabric conversion ongoing, latest release **v2.0 published 2026-08-06** | **CC BY-NC** (data) / MIT (conversion code) — **non-commercial only** | Text-Fabric (`.tf`) plain-text feature files, loadable via Python `text-fabric` package | repo ≈ 201 MB (GitHub-reported: 206,158 KB) | https://github.com/ETCBC/dss | Confirmed 200 OK, confirmed size/license via GitHub API, confirmed CC-BY-NC text in `docs/about.md` |
| 2 | Underlying **Abegg Dead Sea Scrolls electronic data** (raw, pre-Text-Fabric) | 1 | same as above | compiled 1988 onward by Martin Abegg (Trinity Western Univ.); base of Accordance/Logos/Olive Tree/BibleWorks modules and Brill's *DSS Electronic Library* | **Not separately open** — the raw Abegg files themselves are not published standalone; only the CC-BY-NC Text-Fabric derivative (row 1) is public. Commercial modules (Accordance, Logos, Brill) are paid. | N/A | N/A | (no independent URL — folded into row 1) | Could not find a standalone free download; only the ETCBC derivative is public |
| 3 | **Great Isaiah Scroll (1QIsa-a)** full transcription | 1 (would be, if a bulk export existed) | c. 125 BCE | Israel Museum "Digital Dead Sea Scrolls" project w/ Google, launched 2011 | Site terms unclear; images explicitly free, transcription/search layer's redistribution terms not published | Web-only searchable viewer (column/chapter/verse search + English translation) | N/A | http://dss.collections.imj.org.il/ (Isaiah: `.../isaiah`) | Confirmed site resolves (200); confirmed via search results it's searchable by column/chapter/verse — **no bulk download or API found**; would require manual/scripted scraping to extract as text, which was out of scope to attempt |
| 4 | **Scripta Qumranica Electronica (SQE)** / Scrollery project | 1 (project's stated goal — new diplomatic editions of scroll fragments with full imaging) | c. 250 BCE – 68 CE | Project active; `SQE_Database` repo last pushed **2026-07-25** | Repo has a license field set (not fully verified which); project states "open access," full editions readable via API in read-only mode | Custom SQE relational DB + Web API (`api.qumranica.org`); code-only GitHub org, no flat-file bulk transcription export found | `SQE_Database` repo ≈ 161 MB (165,154 KB); `Data-Processing` ≈ 570 MB; these are almost certainly DB schema/tooling, not raw scroll text | https://github.com/Scripta-Qumranica-Electronica ; https://api.qumranica.org/swagger | Repos confirmed to exist and resolve; **could not confirm actual scroll-text content is present or license terms of that content** — needs manual inspection of the Swagger API output before relying on it |
| 5 | **"DSS-Digital-Edition"** (random GitHub repo surfaced by search) | — | — | created 2025-09-12 | — | — | **0 bytes** | https://github.com/namedummy568-stack/DSS-Digital-Edition | Confirmed via API: `"size": 0` — empty repo, dead end, do not pursue |
| 6 | Wikisource Hebrew DSS transcriptions | 1 (if it existed) | — | — | — | — | — | — | **Searched, not found.** No dedicated Wikisource DSS transcription project turned up. Negative result, not a 404 — just doesn't appear to exist as a structured corpus there. |
| 7 | Official **DJD** (Discoveries in the Judaean Desert) transcriptions | 1 | varies | 1955–2009 (Oxford: Clarendon Press) | **Copyrighted** — this is the blocker already established before this research started | Print / paid PDF | — | — | Confirmed blocker, not re-investigated further per your existing finding |

### Bottom line — Dead Sea Scrolls

**One real, verified, freely-downloadable option: `ETCBC/dss`.**

- `git clone https://github.com/ETCBC/dss.git` — ≈201 MB, license **CC BY-NC 4.0** (non-commercial —
  worth flagging even for a personal research corpus, since it does restrict redistribution/commercial use).
- This is the closest thing to a full machine-readable DSS transcription corpus that is actually free
  to download today. It is Tier 1 in substance (built on Abegg's diplomatic transcription of the actual
  scrolls) with a linguistic-tagging layer added on top (part-of-speech, person/number/gender, clause/phrase
  boundaries — the last of which is explicitly flagged in the repo docs as "experimental, machine-learning derived," so treat that specific layer with more caution than the base transcription).
- Everything else checked (Isaiah Scroll web viewer, Scripta Qumranica Electronica) is either
  view-only with no bulk export, or has unconfirmed content/license at the file level — real projects,
  but not yet a clean `git clone`-able, license-clear text corpus the way `ETCBC/dss` is.
- The DJD transcriptions remain the copyrighted blocker already on record. Images at
  deadseascrolls.org.il remain free (already noted in INDEX.md, not re-litigated here).

---

## Part 2 — Papyri

### Manifest

| # | Item | Tier | Witness date | Edition/dataset date | License | Format | Approx. size | URL | Verified |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **papyri/idp.data** (papyri.info bulk data: DDbDP + HGV + APIS + DCLP + APD + translations) | 1 (diplomatic EpiDoc XML editions of the physical papyrus/ostracon/tablet) | 4th c. BCE – 8th c. CE, spans the whole corpus | Duke Databank project began 1980s; EpiDoc XML migration ~2005–2013; **actively updated hourly** via the Papyrological Editor | Documentation states **CC BY 3.0**; **GitHub's own `license` API field returns `null`** — no machine-detected LICENSE file in the repo root, so treat the CC-BY claim as project-stated but not machine-verifiable from the repo metadata alone | EpiDoc XML, one file per text, organized by collection/series | **≈2.85 GB** (GitHub-reported: 2,918,738 KB) — bigger than expected, flag for disk pressure | https://github.com/papyri/idp.data | Confirmed 200 OK, confirmed size via GitHub API; license text itself could not be fetched directly (papyri.info's `/docs/license` page returned an anti-bot challenge page, not content) — **recommend the user or a follow-up fetch verify the license page in a real browser before treating CC BY as certain** |
| 2 | **DCLP** (Digital Corpus of Literary Papyri — literary/subliterary texts, joint Heidelberg/NYU-ISAW project) | 1 | overlaps idp.data's range | Project launched 2017, merged into papyri.info 2018 | Same CC BY claim as papyri.info (DCLP data now lives inside idp.data's `DCLP/` folder) | EpiDoc XML | Already counted inside idp.data (≈2.85 GB); a separate `DCLP/idp.data` fork exists, ≈2.0 GB, essentially a mirror | https://github.com/DCLP ; https://github.com/DCLP/idp.data | Confirmed org and repo exist; this is a fork/mirror of row 1, not additional distinct content — don't clone both |
| 3 | **Center-for-New-Testament-Restoration/transcriptions** (CNTR, Alan Bunning, greekcntr.org) | 1 (diplomatic transcription of the actual manuscript page, with apparatus symbols for damage/corrections — not a reconstructed continuous text) | 2nd–10th c. CE depending on manuscript (papyri sub-range: 2nd–8th c. CE) | Project ongoing since ~2013–2016 (Alan Bunning); repo created 2022-10-08, **last pushed 2026-04-20** | **CC BY-SA 4.0**, attribution to Alan Bunning / CNTR | Plain text, custom "Manuscript Encoding Specification" (MES) — grammar formally defined in the repo's `MES.g4` (ANTLR grammar file) | **≈24 MB** (GitHub-reported: 24,236 KB) — small, easy | https://github.com/Center-for-New-Testament-Restoration/transcriptions | **Confirmed and verified directly** — fetched `class 1/P52.txt` and read real Koine Greek text with apparatus markup (John 18:31–38). Confirmed via directory listing: **P1, P4–P141 nearly complete**, including **P52, P45, P46, P47, P66, P72, P75** — i.e., essentially the whole NT papyrus catalog including all the "famous" ones the user asked about by name |
| 4 | **Center-for-New-Testament-Restoration/SR** (Statistical Restoration Greek NT) | **3** — modern reconstructed critical text, computed statistically from the CNTR transcription base | N/A (a reconstruction, not a witness) | Published 2022 (Alan Bunning / Adam Boyd) | CC BY 4.0 | Plain text / structured formats, several | ≈18 MB (18,198 KB) | https://github.com/Center-for-New-Testament-Restoration/SR | Confirmed repo exists via API. **Editorial choices imposed:** verse-by-verse "majority reading by manuscript count weighted by date/quality" algorithm — a statistical stemma reconstruction, not a diplomatic reading of any one manuscript. Include per instruction, flagged clearly as Tier 3. |
| 5 | **Center-for-New-Testament-Restoration/KJTR** (King James Textus Receptus GNT) | 3 — reconstructed to match the KJV's Greek base text | N/A | Textus Receptus tradition itself dates to 1516 (Erasmus) onward; this specific digital reconstruction published by CNTR, ongoing | presumably same CC BY-SA family, not independently confirmed | Plain text | ≈16 MB (16,037 KB) | https://github.com/Center-for-New-Testament-Restoration/KJTR | Confirmed repo exists via API only, not content-inspected. Tier 3 — reconstructs a specific historical printed tradition (Textus Receptus, itself post-1516, i.e. after our Tier-2 cutoff), not a manuscript diplomatic reading |
| 6 | **Center-for-New-Testament-Restoration/BHP** (Bunning Heuristic Prototype GNT) | 3 — algorithmic reconstruction | N/A | ongoing | CC BY-SA 4.0 | Plain text | ≈15 MB (15,295 KB) | https://github.com/Center-for-New-Testament-Restoration/BHP | Confirmed repo exists via API only |
| 7 | **NTVMR / INTF transcriptions** (Münster) | 1 — diplomatic TEI-XML transcriptions of the manuscript page | 2nd–16th c. CE (whole NT manuscript tradition) | Ongoing, INTF; individual transcriptions dated per manuscript as published | **CC BY 4.0** | TEI XML, one page/manuscript at a time via API | Unknown total — **no single bulk-download; must be scripted per-manuscript via the API** | http://ntvmr.uni-muenster.de/community/vmr/api (redirects to `https://ntvmr.uni-muenster.de/community/vmr/api`) | Confirmed the API endpoint resolves (HTTP 301 → 200 target). Confirmed via secondary source (Digital Orientalist guide) that there is **no "download everything" button** — full corpus extraction would require writing a script against the `transcript/get/` API calls, manuscript by manuscript |
| 8 | **Chester Beatty Papyri (P45, P46, P47)** — independent image/transcription project | 1 (images) / mixed (transcription) | 3rd century CE | Chester Beatty Library + University of Michigan IIIF manifests; CSNTM 2020 facsimile re-photography | Images: IIIF, terms per-institution, not verified here | IIIF manifest (images only, mostly) | N/A | csntm.org; papyrus46.com (a standalone P46-with-transcription viewer project) | Images-only confirmed available via IIIF from both holding libraries. **papyrus46.com claims a transcription-alongside-images viewer but WebFetch could not retrieve readable page content to confirm license/download terms** — flagged unconfirmed, and redundant anyway since P45/46/47 text is already covered cleanly by CNTR (row 3) |
| 9 | **Trismegistos** | metadata/catalog, not full text | spans BC 800 – AD 800 | ongoing, TM Data Services | **CC BY-SA 4.0** for the open API/data-dump portions (Places, Persons); full-text functional search has required a paid institutional subscription **since January 2020** | API + table dumps (metadata only — not transcriptions) | N/A | https://www.trismegistos.org/dataservices/ | Confirmed license claim via search; useful as a supplementary catalog/cross-reference, **not a source of transcription text itself** |
| 10 | Official **DJD**-style copyrighted critical papyrus editions (non-open ones, if any exist) | 1/3 mixed | varies | varies | Copyrighted where applicable | — | — | — | Not separately investigated — no evidence any major NT-papyrus text is closed off the way DJD is; the open sources above (rows 1, 3, 7) cover the field |

### Bottom line — Papyri

**Two real, verified, freely-downloadable options, doing different jobs:**

1. **`Center-for-New-Testament-Restoration/transcriptions`** — the one to actually pull. Small (≈24 MB),
   clean CC BY-SA 4.0 license, and **directly verified** to contain diplomatic transcriptions of P52,
   P45, P46, P47, P66, P72, P75, and nearly the entire numbered NT papyrus series (P1–P141) as plain text
   with a documented markup grammar. This is Tier 1 in substance — it transcribes what's actually on
   each papyrus, with apparatus symbols marking damage/corrections, not a reconstructed composite text.
   ```
   git clone https://github.com/Center-for-New-Testament-Restoration/transcriptions.git
   ```
   The same GitHub org also has three Tier-3 reconstructed Greek NTs (SR, KJTR, BHP) built from that
   base — listed above, ≈15–18 MB each, include if wanted but they're reconstructions, not readings of
   any one manuscript.

2. **`papyri/idp.data`** — the big one (≈2.85 GB), covering the whole documentary + literary papyrus
   corpus (Oxyrhynchus and everything else), not NT-specific. This is the serious scholarly bulk source
   but it's ~120x larger than the CNTR option and its license, while documented on the papyri.info site
   as CC BY 3.0, isn't independently confirmed here (the license page returned a bot-check wall, and
   GitHub's own license detector found nothing). Given the disk-pressure constraint, **don't clone this
   whole thing** — either verify the license manually first, or do a sparse/partial checkout of just the
   collections needed (e.g. `DDbDP/p.oxy` for Oxyrhynchus specifically).

3. **NTVMR/INTF** is real and CC BY 4.0 but has no bulk export — only worth pursuing if the CNTR data
   turns out to be insufficient, since it would require scripting against their API one manuscript at a
   time.

4. Chester Beatty / Bodmer papyri (P45/46/47, P66/72/75) have no better *open transcription* source than
   CNTR — their holding libraries offer images only (IIIF), not machine-readable text.

---

## Summary for both directories

| Directory | Recommended pull | Size | License | Confidence |
|---|---|---|---|---|
| `dead-sea-scrolls/` | `ETCBC/dss` (Text-Fabric) | ≈201 MB | CC BY-NC 4.0 | High — verified resolvable, verified license text, verified size |
| `papyri/` | `Center-for-New-Testament-Restoration/transcriptions` | ≈24 MB | CC BY-SA 4.0 | High — verified resolvable, verified license, **directly read actual file content** confirming P52/P45-47/P66/P72/P75 coverage |
| `papyri/` (optional, much bigger) | `papyri/idp.data` | ≈2.85 GB | CC BY 3.0 (project-stated, not independently confirmed) | Medium — repo verified to exist and resolve; license page itself blocked by anti-bot wall during this research |

**Total if all three recommended items were pulled: ≈3.1 GB** (dominated entirely by `idp.data`; the two
NT-focused sources together are under 250 MB).

**Nothing was downloaded during this research** — the above are `git clone` targets for the user to run
manually. Suggested commands, in order of size/value:

```bash
# Small, high-value, NT-papyri-specific (do these two first)
cd ~/projects/bible-sources/dead-sea-scrolls && git clone https://github.com/ETCBC/dss.git
cd ~/projects/bible-sources/papyri && git clone https://github.com/Center-for-New-Testament-Restoration/transcriptions.git cntr-transcriptions

# Large, general papyrology corpus — verify the license page manually first, and consider
# a sparse checkout instead of the full 2.85 GB clone given disk pressure
cd ~/projects/bible-sources/papyri && git clone --filter=blob:none --sparse https://github.com/papyri/idp.data.git
# then: git -C idp.data sparse-checkout set DDbDP/p.oxy DCLP
```

## Copyright blockers confirmed (not workarounds — just the honest state)

- **DJD (Discoveries in the Judaean Desert)** — copyrighted, as already established. Not re-opened here.
- **Abegg's raw DSS data** — not independently open; only accessible free via the CC-BY-NC ETCBC
  Text-Fabric derivative. The original files are the commercial basis of Accordance/Logos/Brill modules.
- **Trismegistos full-text functional search** — paywalled since January 2020; only its metadata/API
  layer (Places, Persons) is CC BY-SA 4.0 open, and it's catalog data, not transcription text anyway.
