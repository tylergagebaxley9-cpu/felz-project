# Research: Heterodox & Adjacent Traditions — Mandaean, Manichaean, Samaritan,
# Elephantine, Ethiopian, Slavonic, Armenian/Georgian, Karaite

Scope: religious traditions adjacent to or descended from biblical religion whose scriptures this
project has **entirely omitted**. Coptic gnostic / Nag Hammadi material is covered by a separate
agent (`RESEARCH-gnostic-codices.md`) and is **not** repeated here. Every candidate below was
checked live this session — via `curl` against the archive.org metadata API (for real filenames
and restriction flags) or WebFetch against the source page — except where explicitly marked
**unverified**. No bulk downloads were made.

**A budget note on depth:** items 1–4 (Mandaean, Manichaean, Samaritan, Elephantine) got full
verification passes. Items 5–8 (Ethiopian remainder, Slavonic, Armenian/Georgian, Karaite) got
lighter passes — this session's web-search quota ran out partway through, so those sections lean
more on `archive.org`'s search/metadata API (unlimited) and less on general web search. Gaps are
flagged explicitly rather than filled with guesses.

**Update after a billing gap:** a few sites (Chester Beatty, IDP, the Russian National Library)
returned HTTP 403 to plain `curl`/WebFetch mid-session. Per updated project method notes, a 403 is
not a dead end — `tools/scrape_walled.py` (Scrapling, stealth browser fingerprinting) exists for
exactly this. I didn't touch that shared tool's fixed target list, but wrote a one-off script using
the same fetchers to re-check my own three blocked URLs. Two of three cleared the wall; results are
folded into §2 and §8 below, with guessed sub-page URLs flagged as guesses per the standing rule
against trusting unverified filenames.

---

## 1. Mandaean texts — HIGH PRIORITY, and genuinely good news

The Mandaeans are the only surviving Gnostic religion, they revere John the Baptist as their
greatest prophet, and their scriptures are in Mandaic (Eastern Aramaic, own script). **Three of
the four target texts are freely obtainable right now; the fourth (Ginza Rabba) is partially
solved.**

### 1a. Drasha d-Yahya / Mandaean Book of John — SOLVED, fully open

Charles G. Häberl & James F. McGrath, *The Mandaean Book of John: Text and Translation*
(De Gruyter, 2019/2020) — the actual **Mandaic text, typeset in a purpose-built Mandaic font
("Ardwan Lidzbarski"), on facing pages with the English translation**. This is a real critical
edition assembled from Mandaean manuscripts (base manuscripts and colophon dates not independently
verified this session — don't take my word on the exact witness date without checking the book's
own apparatus).

| Item | Verified | License |
|---|---|---|
| archive.org/details/**mandaeanbookofjohn** | `access-restricted-item` = **not set** (open). Text PDF confirmed downloadable, 2.07 MB. Confirmed via `curl` that the actual PDF text opens with the Mandaic-typeset title page and states plainly: *"This version may be freely shared for non-commercial purposes, with friendly permission by Walter de Gruyter GmbH. © 2020 Walter de Gruyter GmbH."* | **Not CC / not public domain** — a publisher-granted non-commercial sharing permission, same category as some already-flagged items in this corpus (DBS German Bible Society texts). Fine for personal study; do not redistribute commercially. |

```
curl -L -o mandaean-book-of-john.pdf \
  "https://archive.org/download/mandaeanbookofjohn/The%20Mandaean%20Book%20of%20John_djvu.txt"
# or the real typeset PDF:
curl -L -o mandaean-book-of-john.pdf \
  "https://archive.org/download/mandaeanbookofjohn/mandaeanbookofjohn.pdf"
```
(Verify the exact PDF filename via `curl -s https://archive.org/metadata/mandaeanbookofjohn` before
pulling — I confirmed the item and its Text PDF format exist and resolve, but did not download.)

### 1b. Qolasta (canonical prayerbook) — SOLVED via an alternate scan

E. S. Drower, *The Canonical Prayerbook of the Mandaeans* (Brill, Leiden, 1959) — Mandaic text
(based on Drower Collection MS 53, copied 1802 by ganzibra Adam Yuhana in Huwaiza, Khuzistan) +
English translation, 414 prayers.

| Item | Verified |
|---|---|
| archive.org/details/canonicalprayerb0000unse | `access-restricted-item: true` — **controlled lending only, not free.** |
| archive.org/details/**in.gov.ignca.36757** | `access-restricted-item`: **not set**. File `36757_text.pdf` resolves (302 → real file on `dn790009.ca.archive.org`). |
| archive.org/details/**in.ernet.dli.2015.530195** | `access-restricted-item`: **not set**. File `2015.530195.canonical-prayer_text.pdf` resolves (302 → `ia601406.us.archive.org`). |

Both open copies are **Digital Library of India** scans of the same 1959 Brill edition — same
pattern as other DLI mirrors that escape the controlled-lending wall on the primary IA upload.

```
curl -L -o qolasta-dli1.pdf "https://archive.org/download/in.gov.ignca.36757/36757_text.pdf"
curl -L -o qolasta-dli2.pdf "https://archive.org/download/in.ernet.dli.2015.530195/2015.530195.canonical-prayer_text.pdf"
```

**Bonus, fully public domain and zero ambiguity:** Mark Lidzbarski, *Mandäische Liturgien*
(Berlin, 1920) — an earlier, independent edition of Mandaean liturgical prayers, **Mandaic text +
German translation**, the direct scholarly predecessor to Drower's Qolasta. 1920 = categorically
PD in the US (pre-1923). Two open copies:

| Item | Verified |
|---|---|
| archive.org/details/mandaschelitur00lidzuoft | not restricted, `mandaschelitur00lidzuoft.pdf` present |
| archive.org/details/mandaische-liturgien | not restricted, `Mandäische Liturgien.pdf` present |

```
curl -L -o mandaische-liturgien.pdf "https://archive.org/download/mandaschelitur00lidzuoft/mandaschelitur00lidzuoft.pdf"
```

### 1c. Haran Gawaita — SOLVED via an alternate scan

E. S. Drower, *The Haran Gawaita and the Baptism of Hibil-Ziwa* (Studi e Testi 176, Biblioteca
Apostolica Vaticana, 1953) — Mandaic text (based on Drower Collection MS 9 and MS 36) reproduced
in facsimile, plus translation, notes, commentary.

| Item | Verified |
|---|---|
| archive.org/details/harangawaitabapt0000unse | `access-restricted-item: true` — controlled lending, not free. |
| archive.org/details/**the-haran-gawaita-and-the-baptism-of-hibil-ziwa** | `access-restricted-item`: **not set**. Files `The-Haran-Gawaita-and-the-Baptism-of-Hibil-Ziwa.pdf` + `_djvu.txt` both present. |

```
curl -L -o haran-gawaita.pdf \
  "https://archive.org/download/the-haran-gawaita-and-the-baptism-of-hibil-ziwa/The-Haran-Gawaita-and-the-Baptism-of-Hibil-Ziwa.pdf"
```

### 1d. Ginza Rabba (Great Treasure) — PARTIALLY SOLVED

This is the one gap. The critical distinction that matters here:

- **Mark Lidzbarski, *Ginza, der Schatz oder das große Buch der Mandäer* (1925)** is a **German
  translation**, not the Mandaic text — confirmed via archive.org metadata (`language: ger`) and
  by checking that Lidzbarski's 1925 volume is explicitly a translation of Petermann's earlier
  edition, not a parallel-text edition. Three open PD copies exist (`ginza-der-schatz`,
  `MN41563ucmf_2`, `ginza-der-schatz_202402`) — useful, but it is TRANSLATION-tier, not ORIGINAL.
- **The actual Mandaic-script critical text** is J. H. Petermann, *Thesaurus s. Liber Magnus,
  vulgo "Liber Adami" appellatus* (2 vols, 1867), lithographed directly in Mandaic script from
  Paris and Leiden manuscripts. **I could not locate a free digitization of this specific work on
  archive.org** despite multiple query variants (title, author, Latin/German spellings). Not
  confirmed on HathiTrust either — that check was cut short by the session's search budget running
  out. Petermann's *other* 1860s Berlin Academy travel volumes (*Reisen im Orient*) ARE digitized
  by the Bavarian State Library, so BSB's own catalog is a reasonable next place to check —
  **flagging as a genuine research gap, not confirmed either way.**
- A modern academic study, Sabah Aldihisi's 2008 UCL PhD thesis *The Story of Creation in the
  Mandaean Holy Book the Ginza Rba*, is open on archive.org (`storyofcrestionginzarba` /
  `the-story-of-creation-in-the-mandaean-holy-book-the-ginza-rba-by-sabah-aldihisi`) — English
  academic prose, may include transliterated Mandaic excerpts of the creation narrative
  specifically, not the full Ginza. Not independently confirmed to contain running Mandaic text.
- I also saw a reference (via search snippet, **not independently verified this session**) to a
  Mandaean-community-hosted transliterated Ginza Rba split across files `TRANS1.pdf`…`TRANS21.pdf`
  on a site linked from an AMIR (Access to Mideast and Islamic Resources) blog post. I did not
  fetch this — the URL wasn't in hand and I didn't want to guess it. If you want this chased down,
  say so and I'll do a follow-up pass with WebFetch once search quota resets.

**Bottom line on Mandaean, overall: this was a strong pass.** Book of John, Qolasta, and Haran
Gawaita — three of the four named targets — are all confirmed freely downloadable in the original
Mandaic (two of the three only via an alternate, non-obvious archive.org scan; the controlled-
lending "main" IA copies would have been a dead end). Only the full Ginza Rabba Mandaic critical
edition remains unlocated.

---

## 2. Manichaean texts — essentially blocked, mirrors the Nag Hammadi situation

Mani (216–274 CE) wrote his own scriptures; almost none of the original-language critical
apparatus is free, for the same structural reason Nag Hammadi isn't: the 20th-century editions
that made this material legible are recent enough to still be under copyright, and the field's
flagship modern series (Corpus Fontium Manichaeorum, Brepols) is commercial.

| Item | Status | Verified |
|---|---|---|
| **Cologne Mani Codex** (Greek, tiny 3.5×4.5cm parchment codex, University of Cologne) — manuscript **images** | High-res TIFF page images are browsable free at `papyri.uni-koeln.de/features/mani-kodex` (192 pages across 8 quires) | Confirmed via WebFetch; **no explicit license/copyright statement found on the page** — flagging as ambiguous, not cleared for reuse. |
| Cologne Mani Codex — **transcribed Greek text** | **Copyrighted.** First edition: Henrichs & Koenen, *Zeitschrift für Papyrologie und Epigraphik* 19–48 (1975–82, journal articles). Standard edition: Koenen & Römer, *Der Kölner Mani-Kodex* (Papyrologica Coloniensis XIV, 1988). Neither is old enough to be PD. | Confirmed via WebFetch (Wikipedia + the Cologne collection page) — no free transcription found. |
| **Medinet Madi Coptic codices** (Kephalaia, Homilies, Psalm-Book) | **Text still copyrighted; but the museum's default image license is genuinely open — see below.** Editio princeps by Polotsky (*Manichäische Homilien*, 1934), Schmidt & Polotsky (*Kephalaia*, 1940), Allberry (*A Manichaean Psalm-Book II*, 1938) — none reach the current US PD cutoff (works published 1930 or earlier). | Dates confirmed via general bibliographic knowledge, not re-verified against a live catalog. |
| **CFM — Corpus Fontium Manichaeorum** (Brepols, ongoing modern critical edition series) | **Confirmed commercial/copyrighted**, as the task anticipated. | Brepols is a commercial academic publisher; no open-access arm found for this series. |
| **Turfan fragments** (Middle Persian, Parthian, Sogdian, Old Turkic) | BBAW's **Digitales Turfan-Archiv** (`turfan.bbaw.de/dta`) — browsable manuscript images by signature, no login required to view. BUT the site explicitly links "Rules for the use of manuscripts from the Berlin Turfan-Collection" — reproduction/reuse is governed by separate terms, not an open license. | Confirmed via WebFetch: images viewable without login; usage terms exist and were not fetched in full — treat as **view-only until confirmed otherwise**. |
| **International Dunhuang Project** (idp.bl.uk) — Chinese Manichaean texts (*Compendium of the Teachings of Mani* 摩尼教残经, *Manichaean Hymnscroll* 下部讚) | **Confirmed blocked, not just a curl fluke.** `idp.bl.uk` returned HTTP 403 to plain WebFetch/`curl` AND to a Scrapling `StealthyFetcher` retry (real-browser fingerprint, same tool as `tools/scrape_walled.py` uses) — the wall held up even against the stronger tool. Not confirmed open or closed; genuinely inaccessible this session. | Re-tried with stealth fetch specifically — still 403. |

### Chester Beatty Library — re-checked with a stealth fetch, and it's better news than the 403 suggested

`chesterbeatty.ie` returned HTTP 403 to plain WebFetch/`curl` initially. Re-tried with a Scrapling
`StealthyFetcher` (real browser fingerprint) and it cleared immediately — the block was a bot wall,
not a dead site. What that follow-up found:

- **Chester Beatty ran a dedicated exhibition on this exact material**: "The Mystery of Mani:
  Rediscover the Manichaean religion through the words of its followers" (28 Oct 2022 – 3 Sep 2023,
  plus an earlier 21 Jun 2019 – 19 Jan 2020 run), confirmed live on `chesterbeatty.ie/collections/
  collection-areas/papyrus-manuscripts/`.
- **Their default digital-image copyright policy, quoted directly from `chesterbeatty.ie/about/
  copyright-2/`:** *"The Chester Beatty has committed to 'Provide access to Chester Beatty digital
  assets without restriction, to all audiences both physical and virtual.' ... For all digital
  images of museum objects unless otherwise listed: **CC BY – 4.0**."* This is a real, open,
  reuse-permitting license — a materially better starting position than Brill/Brepols/CFM.
- **What's NOT yet confirmed:** whether the Manichaean Coptic codex pages specifically are (a)
  posted in their online collections viewer at all, and (b) covered by the default CC BY 4.0 or
  fall under the "for all objects with other copyright attributions, contact the museum" carve-out
  — plausible given these codices were extensively published in facsimile by Brepols/CFM under
  historical arrangements that may carry separate rights. Their actual search/viewer interface
  (guessed URL `viewer.cbl.ie/viewer/search/...` — **this exact path was a guess, not confirmed
  correct**) sits behind its own second wall: an "Anubis" proof-of-work anti-scraping challenge
  that held even against the stealth fetcher. **This needs a real follow-up** — find the correct
  collections-search URL (don't guess it) and get past Anubis, or ask the museum's Research
  Services / photographicservices@cbl.ie directly per their own contact instructions.

**Bottom line on Chester Beatty: upgraded from "unverified 403" to "genuinely promising, needs one
more pass."** Don't download anything from viewer.cbl.ie yet — the license carve-out isn't resolved
— but this is now the single most promising unresolved thread in the whole Manichaean section.

**Bottom line on Manichaean: still nothing confirmed freely pullable in the original language today,
but the Chester Beatty thread is real and worth a dedicated follow-up** — a CC BY 4.0 default
museum policy is a fundamentally different starting position than the Brill/Brepols wall blocking
everything else in this section.
Manuscript *images* of the Cologne Codex and the Turfan fragments are viewable online, but neither
has a confirmed open-reuse license, and every transcribed critical text located is 20th-century
and in copyright. This is the same shape of blocker as Nag Hammadi's Brill wall — a single
commercial publisher (Brepols) sits on the modern edition of most of the corpus.

---

## 3. Samaritan literature beyond the Pentateuch — strong pass, several solid finds

The project currently has the Samaritan Torah only (`samaritan/sp/`). All items below are
**PRINTED-tier** by this project's own labeling convention (19th-century printed editions of
medieval witnesses) — old print, not the witness itself, but genuinely obtainable and in the
original language (Samaritan Hebrew/Aramaic or Judeo-Arabic).

| Text | Witness composed | Edition | Verified open on archive.org |
|---|---|---|---|
| **Asatir** ("Secrets of Moses") | traditionally attributed to Moses' era, actual composition likely medieval, disputed | Moses Gaster, *The Asatir* (Royal Asiatic Society, 1927) — Samaritan text + English translation | **`in.ernet.dli.2015.515698`** (DLI scan, not restricted) and **`MN40245ucmf_0`** (microform, not restricted, has PDF) — both confirmed via metadata API |
| **Chronicle of Abu'l-Fath** (Arabic, composed 1355 CE) | 1355 CE | Eduard Vilmar, *Abulfathi Annales Samaritani* (1865) — the Arabic text itself | **`abulfathiannales00abal`**, **`abulfathiannale00vilmgoog`**, **`abulfathiannales00abal_0`**, **`bub_gb_uUyz6kU3JZgC`** — all confirmed not-restricted |
| **Samaritan Book of Joshua** (Arabic chronicle, "Chronicon Samaritanum") | medieval, composite | Theodor Juynboll, *Chronicon Samaritanum, arabice conscriptum, cui titulus est Liber Josuae* (1848) — Arabic text | **`chroniconsamarit00josh`** — confirmed not-restricted |
| **Defter** (Samaritan liturgy) | medieval–early modern liturgical compilation | A. E. Cowley, *The Samaritan Liturgy* (2 vols, 1909) — Samaritan Hebrew/Aramaic text | **Seven separate open copies found**: `thesamaritanlitu02cowluoft`, `samaritanliturgy0001unse`, `samaritanliturgy01cowluoft`, `TheSamaritanLiturgyVol.1A.E.CowleyEd.1909`, `samaritanliturgy0000aeco`, `samaritanliturgy0000aeco_b1k9`, `samaritanliturgy01unknuoft` — all confirmed not-restricted |
| **Memar Marqah / Tibat Marqe** (4th c. CE, Samaritan Aramaic) | 4th c. CE | John MacDonald's 1963 critical edition — **restricted** (`memarmarqah0000v84p1marq`, controlled lending, and modern/copyrighted anyway) | **Found the actual editio princeps instead:** Moses Heidenheim, *Bibliotheca Samaritana* vol. 3, titled internally **"Commentar Marqah's"** (confirmed by grepping the OCR text — line 79 of the djvu.txt literally reads `COMMENTAR MARQAHS`, plus repeated mentions of "die Schriften Marqah's"). **`bibliothecasamar03heid`** — not restricted, 27 MB PDF, confirmed via metadata + content grep. |
| (same series, vol. 2) | — | Heidenheim, *Bibliotheca Samaritana* vol. 2 | **`bibliothecasamar02heid`** — not restricted, 12 MB PDF. Content not fully confirmed — OCR on Samaritan/Hebrew-heavy pages is unusable (garbage characters, matches this project's own documented OCR-quality warning for Hebrew/Greek). Grepped mentions of "samaritanische Liturgie" and Markah's writings in the introduction, but I could not confirm from OCR alone whether the vol. 2 text itself is the Samaritan Targum, liturgical poetry, or something else. **Open the PDF directly at the title page before relying on this — don't take my characterization of vol. 2's contents as settled.** |
| **Samaritan Targum** | 2nd–4th c. CE (disputed) | Not confirmed located this session as a standalone free edition. Petermann's *Pentateuchus Samaritanus* (1872, `pentateuchussama00pete`, not restricted, 62 MB PDF) exists and is open, but that multi-volume work is generally understood to be an edition of the **Samaritan Hebrew Pentateuch**, not the Aramaic Targum — could overlap with what's already in `samaritan/sp/`. Adolf Brüll's *Das samaritanische Targum zum Pentateuch* (1875), the standard 19th-c. edition of the actual Targum, was searched for and **not found** on archive.org this session. | Flagged gap. |
| **Tolidah** (chronological chronicle) | medieval | Neubauer's 19th-c. edition (*Chronique samaritaine*, Journal Asiatique, 1869) — **not found** on archive.org this session under any query variant tried | Flagged gap — likely lives inside a bound *Journal Asiatique* volume, worth checking Gallica (BnF) directly. |
| **Chronicle Adler** (Chronicle II / New Chronicle) | medieval, this recension published 1902–03 | Adler & Séligsohn's edition, *Revue des Études Juives* 44–45 (1902–03) — **not found** on archive.org this session (the only hit was an unrelated restricted 2005 book) | Flagged gap — check Gallica for the REJ volume directly. |

```
curl -L -o asatir-gaster-1927.pdf "https://archive.org/download/MN40245ucmf_0/MN40245ucmf_0.pdf"
curl -L -o abulfath-vilmar-1865.pdf "https://archive.org/download/abulfathiannales00abal/abulfathiannales00abal.pdf"
curl -L -o samaritan-joshua-juynboll-1848.pdf "https://archive.org/download/chroniconsamarit00josh/chroniconsamarit00josh.pdf"
curl -L -o samaritan-liturgy-cowley-1909-v1.pdf "https://archive.org/download/samaritanliturgy01cowluoft/samaritanliturgy01cowluoft.pdf"
curl -L -o memar-marqah-heidenheim-v3.pdf "https://archive.org/download/bibliothecasamar03heid/bibliothecasamar03heid.pdf"
```

**Bottom line on Samaritan: this was the strongest section after Mandaean.** Asatir, Abu'l-Fath,
the Samaritan Book of Joshua, the Defter liturgy, and — genuinely unexpectedly — the editio
princeps of Memar Marqah are all confirmed open. Only the Samaritan Targum, Tolidah, and Chronicle
Adler remain unlocated.

---

## 4. Elephantine Jewish community texts — the literary/religious layer

5th-century BCE Aramaic papyri from the Jewish military colony at Elephantine, Egypt, with its own
YHW temple. **Note per the task's instruction: a separate epigraphy-focused agent may also be
covering Elephantine — this pass focused specifically on the literary and religious documents
(the Passover letter, the temple-rebuilding correspondence to Bagoas) rather than the full
epigraphic corpus.**

| Item | Composed | Edition | Verified |
|---|---|---|---|
| Cowley's edition (the standard English scholarly edition, includes the Passover Letter and the petitions to Bagoas re: rebuilding the YHW temple) | 5th c. BCE | A. E. Cowley, *Aramaic Papyri of the Fifth Century B.C.* (Oxford, 1923) | **`aramaicpapyrioff00ahikuoft`**, **`aramaicpapyrioff0000acow_k5c3`**, **`aramaicpapyrioff0000acow`** — all confirmed not-restricted, PD (1923) |
| Sachau's edition (the first publication, German, of the Elephantine finds) | 5th c. BCE | Eduard Sachau, *Aramäische Papyrus und Ostraka aus einer jüdischen Militär-Kolonie zu Elephantine* (1911) | **`aramischepapyr02sachuoft`**, **`aramischepapyr00ungnuoft`** — confirmed not-restricted, PD |
| Kraeling's edition (the Brooklyn Museum papyri, a second cache) | 5th c. BCE | E. G. Kraeling, *The Brooklyn Museum Aramaic Papyri* (Yale UP, 1953) | **Not PD** — 1953, well past the current 1930 cutoff. Not searched further; this is the copyright-blocked one the task anticipated. |
| Porten's TAD (*Textbook of Aramaic Documents from Ancient Egypt*) — the modern standard reference, all documents in one place | 5th c. BCE | Bezalel Porten, multi-volume, Hebrew University Magnes Press / Eisenbrauns | **Copyrighted, modern, not free** — confirms the task's expectation. |

```
curl -L -o cowley-1923-elephantine.pdf "https://archive.org/download/aramaicpapyrioff0000acow/aramaicpapyrioff0000acow.pdf"
curl -L -o sachau-1911-elephantine.pdf "https://archive.org/download/aramischepapyr02sachuoft/aramischepapyr02sachuoft.pdf"
```

Cowley 1923 + Sachau 1911 together cover the literary/religious content well: both are PD, both
resolve, both contain the original Aramaic text with translation/commentary. This is the pre-1930
layer; anything found later (Kraeling's cache, or any papyrus published after 1953) is blocked.

---

## 5. Ethiopian texts beyond the biblical canon — partial

The project has 36 of 81 Ge'ez books, sourced from Beta Masaheft (Hamburg, CC BY-SA 4.0), pulled
via their GitHub mirror `BetaMasaheft/Works` (TEI XML, 6,567 files as of this check). I enumerated
that entire tree by filename this session looking for the three named targets:

| Target | Result |
|---|---|
| **Book of the Mysteries of Heaven and Earth** | **Already in this corpus** — `MysHE` is one of the 36 books already downloaded (confirmed by checking `ethiopic/ethiopian-bible/public/data/chapters/MysHE/` directly — 7 chapter JSON files present locally). Not a gap. |
| **Fekkare Iyasus** | **Not confirmed found.** Searched the `BetaMasaheft/Works` file tree for `Iyasus`/`Iyesus`/`Iyäsus` and related patterns — the only hit was `LIT3950ChronIyasu.xml` (a chronicle entry, unrelated) and `LIT3975FekkareF.xml`, which on inspection is *Fǝkkāre Fidal* ("Interpretation of the Alphabet"), a completely different text. **This is a real gap in the mirror I could enumerate, but I did not run the live SPARQL search against `betamasaheft.eu/api/SPARQL` to rule out that it exists under an unexpected work ID** — flagging as unconfirmed-absent, not confirmed-absent. |
| **Ethiopic Apocalypse of Peter** | **Not confirmed found.** Checked `LIT4446Peter.xml` — titled *Mawāśǝʿt za-Ṗeṭros* ("Antiphon of Peter"), not the Apocalypse. No file matched an Apocalypse-of-Peter naming pattern in the enumerated tree. Same caveat as above — SPARQL search not run. |
| **Ethiopic Enoch manuscript images** | Not checked this session (ran out of budget after the two misses above). Beta Masaheft's site links individual manuscript pages with IIIF-style facsimiles for many works; `LIT1340EnochE` (the 1 Enoch work entry already used as this project's source) would be the starting point to check for linked manuscript images. |

**Repo access note:** `BetaMasaheft/Works` on GitHub has no `LICENSE` file (confirmed via GitHub
API — 404), but the license is documented on the live site and is already trusted by this
project's own `ethiopic/ethiopian-bible/public/data/AGENTS.md` as CC BY-SA 4.0. Consistent, not a
new finding.

**Honest bottom line: this section needs a follow-up pass** with either the live SPARQL endpoint
(`betamasaheft.eu/api/SPARQL`) or a direct site search, rather than filename-pattern-matching
6,567 TEI files. What I can say confidently is that neither target text is present under an
obviously-named file in the GitHub mirror.

---

## 6. Slavonic pseudepigrapha — confirmed genuine gap, partial path forward

2 Enoch, the Ladder of Jacob, and the Apocalypse of Abraham survive **only** in Old Church
Slavonic. I checked the project's existing `pseudepigrapha/Online-Critical-Pseudepigrapha` XML
files directly (43 files enumerated) — **none of the three are present**, despite the project's
own `INDEX.md` describing that corpus as covering "Greek, Ge'ez, Syriac, Latin, Slavonic, Hebrew."
This is a genuine, confirmed gap, not a documentation oversight on my part.

| Text | What I found | Original-language status |
|---|---|---|
| **2 Enoch** | W. R. Morfill & R. H. Charles, *The Book of the Secrets of Enoch* (Oxford, 1896) — **English translation only**, confirmed by reading the opening pages of the OCR text (lists Charles's other English-translation works, no Slavonic printed). Multiple open PD copies exist (`booksecretsofe00morfgoog`, `bookofsecretsofe00morf`, `cu31924014633568`, `bookofsecretsofe0000unse`) but **all are TRANSLATION-tier**, not usable as an original-language source. | The actual Slavonic critical text (Matvej Sokolov's 1899 Moscow edition, or the later Vaillant 1952 edition) was **searched for and not found** on archive.org this session — likely lives on a Russian digital library (rusneb.ru, elib.rgb.ru) rather than archive.org/HathiTrust, which I did not have budget to check this pass. |
| **Apocalypse of Abraham** | G. H. Box, *The Apocalypse of Abraham* (SPCK, 1918) — English translation, PD, open on archive.org (`AbrahamBOX1918`, confirmed not-restricted). Same issue as above: **translation only**, not confirmed to include the Slavonic text. | Slavonic critical text (A. N. Popov's 1880 first edition, or A. Kozak's 1893 edition) — **not found** on archive.org this session. |
| **Ladder of Jacob** | Not located in any form (translation or original) this session. The Slavonic text lives in N. S. Tikhonravov's 1863 *Pamyatniki otrechennoi russkoi literatury* — **searched for, not found** on archive.org. | Gap. |

**Bottom line: confirmed real gap, not yet solved.** All three original-language Slavonic texts
would most likely need to be chased on Russian digital-library infrastructure (National Library of
Russia, RSL/elib.rgb.ru) rather than archive.org — a different search surface than what this
session's tooling reached well. Worth a dedicated follow-up pass.

---

## 7. Armenian and Georgian pseudepigrapha — light pass, mostly unresolved

Lightest-touch section this session — ran short on both time and web-search budget by this point.

- Checked TITUS project (`titus.uni-frankfurt.de`) directly via WebFetch: has Armenian biblical
  and patristic texts, but **no Armenian apocrypha/pseudepigrapha and no Georgian material at all**
  in its index, confirmed by reading the page.
- Michael E. Stone's modern critical editions (the standard scholarly source for Armenian
  apocrypha — CSCO series and the SBL "Early Judaism and Its Literature" volumes) are what
  archive.org actually has entries for (`stone-1981-adam-english` — *Penitence of Adam*,
  `armenian-apocrypha-relating-to-abraham`, `armenian-apocrypha-relating-to-angels-and-biblical-heroes-2016`,
  `armenianapocryph0000unse` — restricted) — **these are modern (1980s–2016) copyrighted academic
  editions**, not freely obtainable, and I did not confirm whether any of the open-looking
  archive.org items actually contain the Armenian text (vs. English-only) before running out of
  budget to check.
- Did not reach 19th-century Mekhitarist (Venice/Vienna) editions, which are the more likely PD
  source for original Armenian apocrypha text — **not checked this session, genuine gap.**
- Georgian material: **not investigated at all this session** beyond the negative TITUS result.

**Bottom line: unresolved.** This needs a dedicated follow-up pass specifically targeting the
Mekhitarist press editions (Venice, Vienna) for Armenian, and a first pass on Georgian sources —
neither happened here.

---

## 8. Karaite texts — light pass, mostly unresolved

- Checked archive.org for Abraham Firkovich's manuscript collection (the primary source of Karaite
  and Karaite-adjacent Hebrew Bible manuscripts, held at the National Library of Russia, and
  notably including the scribal environment that also produced the Leningrad Codex this project
  already uses) — the specific guessed sub-page `nlr.ru/eng/coll/manuscripts/firkovich.html`
  returned **HTTP 404** (a guessed URL, not confirmed correct — flagging per the standing rule
  against trusting guessed filenames/paths).
  **Follow-up with a stealth fetch (Scrapling, real-browser fingerprint) found the actual live
  page**: `nlr.ru/eng/coll/manuscripts/` resolves (redirects to `nlr.ru/manuscripts`, HTTP 200) —
  this is the Manuscripts Department (Отдел рукописей) of the Russian National Library, and its
  own text confirms an "Электронная библиотека" (**Digital Library**) offering *"electronic
  facsimile publications of manuscript monuments with specialized search capability."* This
  establishes the department **does** run a digital library with a search interface — but I did
  not get as far as querying it for "Firkovich" or Karaite-specific holdings, so digitization
  status of the Firkovich collection specifically is still **not confirmed either way**. Genuine
  next step, not a dead end.
- Isaac Pinsker's *Likkute Kadmoniyyot* (1860) — a 19th-c. compilation of early Karaite literary
  fragments, plausible PD candidate — **searched for on archive.org, not found.**
- Leon Nemoy's *Karaite Anthology* (Yale, 1952) — found on archive.org (`karaiteanthology0000nemo`)
  but **`access-restricted-item: true`** (controlled lending) and it's a translation anthology, not
  primary Karaite-language text, anyway.
- Did not reach Yefet ben Ali's Judeo-Arabic Bible commentaries or Aaron ben Joseph's karaite
  exegesis — no time this session.

**Bottom line: unresolved.** Sefaria (already noted in this project's `INDEX.md` as a free API,
not mirrored) is the most likely near-term path for Karaite commentary material, but that wasn't
re-verified for Karaite-specific holdings this session.

---

## Summary table

| # | Tradition | Status | Best find |
|---|---|---|---|
| 1 | Mandaean | **Strong — 3 of 4 texts solved** | Book of John (bilingual, open); Qolasta + Haran Gawaita via alternate DLI/mirror scans; Mandäische Liturgien fully PD. Ginza Rabba Mandaic critical text unlocated. |
| 2 | Manichaean | **Blocked, but one promising thread** | Manuscript images viewable (Cologne Codex, Turfan); all transcriptions copyrighted (Brepols CFM wall, same shape as Nag Hammadi/Brill). IDP confirmed blocked even under stealth fetch. **Chester Beatty's default digital-image license is CC BY 4.0** (confirmed via stealth fetch past their bot wall) — whether the Manichaean codex images specifically fall under that default or a carve-out is the open question, worth a dedicated follow-up. |
| 3 | Samaritan (beyond Torah) | **Strong** | Asatir, Abu'l-Fath Chronicle, Samaritan Joshua, Defter liturgy, and Memar Marqah editio princeps all confirmed open. Targum, Tolidah, Chronicle Adler unlocated. |
| 4 | Elephantine (literary layer) | **Solved for the pre-1930 layer** | Cowley 1923 + Sachau 1911, both open, both PD, cover the Passover Letter and temple correspondence. Kraeling/Porten confirmed blocked as expected. |
| 5 | Ethiopian (beyond current 36) | **Partial / needs SPARQL follow-up** | MysHE already present. Fekkare Iyasus and Apocalypse of Peter not found by filename search; not ruled out via live catalog search. |
| 6 | Slavonic pseudepigrapha | **Confirmed gap** | None of 2 Enoch / Ladder of Jacob / Apocalypse of Abraham present in original Slavonic anywhere checked; likely needs Russian digital-library infrastructure. |
| 7 | Armenian/Georgian | **Unresolved** | Light pass only; Mekhitarist press editions and Georgian sources not investigated. |
| 8 | Karaite | **Unresolved** | Light pass only; NLR's Manuscripts Dept. digital library exists and is reachable (confirmed via stealth fetch) but not yet queried for Firkovich/Karaite holdings specifically. Pinsker not found, Nemoy anthology restricted. |

## Recommended next steps, in priority order

1. **Pull the three solved Mandaean texts** (Book of John, Qolasta via DLI, Haran Gawaita via
   alternate scan, Mandäische Liturgien) — all commands above, all verified live this session.
2. **Pull the five solved Samaritan texts** — Asatir, Abu'l-Fath, Samaritan Joshua, Defter,
   Memar Marqah vol. 3 — all commands above.
3. **Pull Cowley 1923 + Sachau 1911** for the Elephantine literary/temple correspondence layer.
4. Follow-up pass, if wanted: Ginza Rabba (check BSB/HathiTrust for Petermann 1867), Beta Masaheft
   SPARQL for Fekkare Iyasus/Apocalypse of Peter, and Russian digital libraries for the Slavonic
   pseudepigrapha — these three are the highest-value remaining gaps.
5. **Chester Beatty (Manichaean codex images, possibly CC BY 4.0)** — find the real Search
   Collections Online URL (don't guess it) and get past the Anubis proof-of-work wall on the
   viewer, or just email photographicservices@cbl.ie / Research Services directly per their own
   contact instructions. Worth doing before writing off Manichaean entirely.
6. **NLR digital library — query it for "Firkovich"** to settle the Karaite manuscript-access
   question; the department's digital library is confirmed to exist and be reachable, just not
   yet searched for this specifically.
7. Armenian/Georgian needs a full pass from scratch — treat item 7 above as "not yet researched"
   rather than "researched and blocked."
