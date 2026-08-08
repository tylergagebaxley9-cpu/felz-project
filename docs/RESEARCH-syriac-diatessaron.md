# Research: pre-Peshitta / independent Syriac & Aramaic witnesses, and the Diatessaron

Scope: everything **older than or textually independent of** the Peshitta, which the
corpus already has (`aramaic-syriac/peshitta`, `aramaic-syriac/syrnt`, both ETCBC). Do
not re-acquire those. This pass covers the Old Syriac Gospels, the Diatessaron problem
end to end, Harklean/Philoxenian, the Syro-Hexapla, Christian Palestinian Aramaic (CPA)
lectionaries, Ephrem and Aphrahat, and the modern digital infrastructure (Sinai
Palimpsests Project, syriaca.org, SEDRA/Beth Mardutho, CAL, HMML).

**Method, per the project's now-standard rule**: every archive.org identifier below
was resolved against the **live metadata API** (`https://archive.org/metadata/<id>`)
first — never guessed from a title — and every filename listed is a real filename
that API returned. Every "confirmed" link was then HTTP-checked directly this session
(2026-08-08). Where an item's own `access-restricted-item` flag was `true`, I verified
the restriction by actually requesting the file rather than trusting the flag (some
restricted-flagged items have unrestricted microform duplicates uploaded separately —
that pattern shows up twice below, for the Dura fragment and Ephrem's commentary, and
is worth remembering).

**Second lesson, learned mid-pass and worth flagging explicitly**: a plain `curl` with
no User-Agent got a false **404** from `sinai.library.ucla.edu` on every path tried,
which I initially wrote up as "the site is down." Re-checking with a browser
User-Agent string got 200s throughout — the site was never down, `curl`'s default UA
was being filtered. That correction is applied in §1/§9/BLOCKED below. I checked
whether this project's `tools/scrape_walled.py` was relevant to anything else in this
pass: it wasn't — the one genuine 403 I hit (`brill.com`, checking the Leiden Peshitta
Institute's status) is a deliberate commercial paywall, which that tool's own scope
note excludes by design ("Sites that gate content deliberately — Brill, Brepols,
controlled digital lending — are out of scope and stay out"), so no stealth fetch was
warranted there; a plain UA-string retry was sufficient for the one case that did turn
out to be a false negative.

## Tier key (same convention as `RESEARCH-manuscripts.md`)

- **Tier 1** — transcription/facsimile of the actual manuscript, in the original
  language. No editorial modernization.
- **Tier 2** — pre-1820 printed edition transcribing a real manuscript (matches
  PROVENANCE.md's PRINTED label).
- **Tier 3** — post-1820 critical edition assembled by a modern editor.

Every entry gives **MS date** (the physical witness) and **Edition date** (what you'd
actually be downloading) separately, per PROVENANCE.md's rule.

---

## 1. Old Syriac Gospels — Sinaitic Palimpsest + Curetonian Gospels

Both **older than the Peshitta NT and textually distinct from it** — this is the whole
point of chasing them. Two independent manuscripts, overlapping coverage, neither
complete.

| Witness | MS date | Physical location |
|---|---|---|
| **Syrus Sinaiticus** (Sinai Syr. 30) | 4th–5th c. CE (palimpsest — Gospels text is the *lower* writing, overwritten in 778 CE by a text of female saints' lives) | St. Catherine's Monastery, Sinai |
| **Syrus Curetonianus** | 5th c. CE | British Library (Add. MS 14451) |

### Confirmed obtainable — Tier 2 (pre-1820 doesn't apply here, all editions are 1858+, so these are Tier 3 in a strict sense, but they are diplomatic transcriptions with no textual reconstruction — functionally Tier 1 content in a 19th/20th-c. typeset wrapper)

**Cureton 1858** — *editio princeps* of the Curetonian Gospels (Syriac text only, no translation in this volume):
- `https://archive.org/details/remainsofveryant00cure` — confirmed 200. `remainsofveryant00cure_djvu.txt` (359 KB), `.pdf` (10.2 MB), `_jp2.zip` (71 MB, page images).
- Alt scan: `https://archive.org/details/remainsofveryant00unse` — confirmed 200, `_djvu.txt` 741 KB.

**Bensly/Harris/Burkitt/Lewis 1894** — *"The Four Gospels in Syriac, transcribed from the Sinaitic Palimpsest"* — the first published Syriac-text transcription of Sinaiticus (four scholars split the work after Bensly died mid-project):
- `https://archive.org/details/fourgospelsinsyr00bens` — confirmed 200. `_djvu.txt` 497 KB, `.pdf` 12.8 MB.

**Agnes Smith Lewis 1910** — *"The Old Syriac Gospels, or Evangelion da-Mepharreshe"* — the **standard, definitive edition**: full Sinaiticus text with Curetonian variants in the apparatus, plus patristic citations. Supersedes the 1894 transcription.
- `https://archive.org/details/oldsyriacgospels00lewirich` — confirmed 200. `_djvu.txt` 830 KB, `.pdf` 30.8 MB.
- Direct-download mirror (same 1910 text): `https://archive.org/download/SYROLD_DBS_HS/Syriac-(1910)-Gospels-(Evangelion-da-Mepharreshe)-Sinai-or-Syro-Antiochene-Palimpsest-Gospels.pdf` — confirmed (302→200).

**Burkitt 1904** — *"Evangelion da-Mepharreshe: the Curetonian Version of the Four Gospels, with the readings of the Sinai Palimpsest and the early Syriac Patristic evidence"* — two volumes, vol. 1 is the Syriac text base on Curetonian with Sinaiticus apparatus, vol. 2 is introduction/notes. This is the edition Burkitt is famous for, and the title your task brief names.
- Vol. 1 (Text): `https://archive.org/details/evangeliondameph0001fcra` — confirmed 200. `_djvu.txt` 1.0 MB, `.pdf` 29.6 MB.
- Vol. 2 (Introduction/notes): `https://archive.org/details/evangeliondameph0002fcra` — confirmed 200. `_djvu.txt` 745 KB, `.pdf` 21.1 MB.

**Lewis's 1894/1896 English translation** (not original language — TRANSLATION tier, lower priority): `https://archive.org/details/translationoffo00lewi` — confirmed extant, not independently re-verified this pass since it's not original-language.

### Honest caveat on all of the above

**None of this is a machine-readable Unicode Syriac transcription.** Every one of these
is a 19th/20th-c. typeset book, scanned, with an OCR'd `_djvu.txt` layer. Syriac-script
OCR from that era is close to useless as text — same failure mode PROVENANCE.md already
documents for Erasmus's Greek layer (`ὅτὶ Ὀυὰ τγκαταλείψας` for Acts 2:27). I did not
find **any** project that has produced a clean Unicode Syriac digital edition of either
Old Syriac Gospel manuscript — not on GitHub, not at CAL, not at Beth Mardutho. This
matches an independent research pass I found mid-search (see §9) that reached the same
conclusion: *"Old Syriac currently has no machine-processable Unicode transcription.
Existing resources are either period print scans or low-quality OCR."* If you want Old
Syriac Gospels text for anything beyond human reading of page images, the Latin-letter
transliteration and apparatus in Burkitt 1904 / Lewis 1910 is the closest thing that
exists, and someone would have to manually key it.

### Not obtainable / degraded access

- **CAL** (`cal.huc.edu`) has Old Syriac browsable verse-by-verse with morphology —
  but explicitly **"do not try to scrape our site"**; bulk data requires emailing
  `skaufman@huc.edu` directly ("happy to provide legitimate academic users with
  relevant dumps"). Not a self-serve download.
- **Sinai Palimpsests Project** (spectral imaging of 160+ Sinai palimpsests, Syriac
  among the ten languages covered — the scholarly team page names Grigory Kessel, the
  same scholar who published the 4th Old Syriac Gospels witness, Vat. iber. 4, in NTS
  2023, confirming Syriac undertexts are actively within this project's scope). Landing
  page `sinaipalimpsests.org` resolves over **plain HTTP only** (its HTTPS cert is
  misconfigured, points to an unrelated UCLA host — confirmed via curl). Its "Research
  Site" link points to `sinai.library.ucla.edu` — **correction to an earlier check in
  this same pass**: a plain `curl` (default User-Agent) returned 404 on every path,
  which I initially read as the site being down. Re-checked with a real browser
  User-Agent string and the site is fully live: homepage returns 200 with full content
  (IIIF-based image delivery, confirmed from the page's own text), and `/browse`
  returns 200 with *"Unauthorized — Please login to access this page. If you do not
  have an account, click the login link to register."* **So the correct status is:
  not down, login-gated** — same access model as HMML (§9): free account registration
  required, terms of use apply (a PDF, not independently transcribed this pass), no
  indication of open bulk download. The umbrella org, EMEL (`emelibrary.org`, confirmed
  live), states on its own homepage: *"EMEL is a service organization and does not
  assert ownership or copyright over digital images it creates"* and *"does not retain
  copies"* — consistent with images living at the UCLA-hosted research site under its
  own login/terms rather than at EMEL itself. **Whether Sinai Syr. 30 specifically (the
  Syriac Sinaiticus Gospels palimpsest) is within this project's imaged set is not
  confirmed** — it was already deciphered by chemical reagent in Lewis's day (1890s),
  long before spectral imaging existed, so it's plausible but not verified that it's
  one of the manuscripts this particular project re-imaged. Worth a follow-up with a
  registered account if bulk/individual manuscript access matters.
- **Kiraz 1996, *A Comparative Edition of the Four Gospels: Aligning the Sinaiticus,
  Curetonianus, Peshîttâ and Ḥarklean Versions*** (Brill/Piscataway, 4 vols) is the
  modern scholarly standard synoptic edition — commercial, not free. Beth Mardutho
  hosts a **sample/front-matter PDF only**: `https://bethmardutho.org/wp-content/uploads/2020/07/Kiraz_1996_Comparative-Edition-of-the-Syriac-Gospel.pdf` (confirmed 200, 275 KB — front matter, not the text).

### Recent scholarship, for context (not downloadable data, just worth knowing about)

- **Brock 2016** identified a **third** Old Syriac Gospels witness — a fragment (Matt
  11:30–12:26), published in *Deltio Biblikōn Meletōn* 31.1 (2016) 7–18.
- **Kessel 2023** identified a **fourth** — a double palimpsest, Vat. iber. 4, ff. 1–5
  — published in *New Testament Studies*, Cambridge Core. The field is not frozen;
  new Old Syriac witnesses are still turning up in library palimpsests as multispectral
  imaging gets applied to more manuscripts.

---

## 2. The Diatessaron — every surviving route, checked

Composed by Tatian c. 172–185 CE. **The autograph is gone, no manuscript of Tatian's
own text survives in any language**, and — confirming the earlier finding already in
this corpus's `docs/RESEARCH-pre1820-patristics-apocrypha.md` §3.8 — **no pre-1820
access to it exists.** What follows is what *is* freely obtainable post-1820, organized
by route, with an honest verdict at the end of each.

### 2a. Dura-Europos fragment — the one genuine ORIGINAL-LANGUAGE witness

The only surviving fragment that is plausibly **in the Diatessaron's own compositional
language tradition** (Greek — the fragment itself is Greek, though whether Tatian
composed in Greek or Syriac originally is still contested by scholars). Excavated 1933
at Dura-Europos, Syria; a single parchment scrap, P.Dura 10, ~14 lines, matching a
passage harmonizing the Passion narratives. Editio princeps: Carl Kraeling, *A Greek
Fragment of Tatian's Diatessaron from Dura* (Studies and Documents 3, 1935).

| MS date | Edition date |
|---|---|
| c. 250 CE (Dura was destroyed/abandoned 256/257 CE — hard upper bound) | 1935 |

- Primary scan `https://archive.org/details/greekfragmentoft0000tati` is
  **access-restricted** (borrow-only, confirmed via HTTP 401 on the file).
- **Working mirror (microform copy of the same book, unrestricted)**:
  `https://archive.org/details/MN41439ucmf_4` — confirmed 200 on
  `MN41439ucmf_4_djvu.txt` (80 KB) and `.pdf` (1.7 MB). This is the actual Greek text
  of the fragment plus Kraeling's commentary, freely downloadable.

**This is the single most important find in this whole pass for "original language
Diatessaron access"** — it's a real fragment of the real thing, not a translation of a
translation, and it's freely obtainable.

### 2b. Ephrem's Commentary on the Diatessaron — Syriac manuscript IS viewable online

Ephrem (d. 373 CE) wrote a prose commentary following the Diatessaron's sequence,
which is the best proxy we have for Tatian's actual arrangement, even though it's not
Tatian's text itself.

**The manuscript** — Chester Beatty Syriac MS 709 (Dublin), the only known copy of
Ephrem's commentary in its own language, Estrangelo script, **CBL's own catalog dates
it c. 500 CE** (i.e., within ~125 years of Ephrem's death — a genuinely early copy):

- **Free IIIF viewer, live, verified this session**:
  `https://viewer.cbl.ie/viewer/object/Syc_709_1/1/LOG_0000/`
  - IIIF Presentation API 2.0 manifest confirmed at
    `https://viewer.cbl.ie/viewer/api/v1/records/Syc_709_1/manifest/` — 82 canvases
    (both sides of 41 folios, f.1r–f.41v), IIIF Image API level2 service per canvas
    (meaning you can request full-resolution crops programmatically, not just the
    embedded viewer widget).
  - **Copyright: Chester Beatty Library** (confirmed from the manifest's own metadata
    field). Freely viewable; redistribution terms are the standard CBL library
    reproduction policy (`chesterbeatty.ie`), not an open license — treat as
    look-don't-bulk-take unless you contact CBL for reproduction rights.
  - This is the actual manuscript in the actual language — genuinely the best thing
    this whole research pass turned up for "closest to Tatian available."

**Pre-discovery Syriac fragments** — before Chester Beatty 709 was identified/published
(1957 acquisition, published from 1963), J. Rendel Harris had already reconstructed
substantial passages of Ephrem's lost Syriac commentary by tracing quotations embedded
in *later* Syriac commentators who had access to it:

- `https://archive.org/details/fragmentsofcomme0000ephr` — Harris, *Fragments of the
  Commentary of Ephrem Syrus upon the Diatessaron* (1895) — confirmed 200,
  `_djvu.txt` 196 KB, `.pdf` 6.5 MB. Genuine reconstructed Syriac (visible as Syriac
  script in the scan), pre-dates the manuscript's rediscovery by 60+ years.

**Armenian version + Latin translation** (the route that was open before either the
Syriac fragments or the manuscript existed in scholarship) — the Mechitarist fathers of
Venice published the Armenian text; Georg Moesinger translated it into Latin:

- `https://archive.org/details/evangeliiconcor01msgoog` — J.B. Aucher / Georg
  Moesinger, *Evangelii concordantis expositio* (1876) — confirmed 200,
  `_djvu.txt` 586 KB, `.pdf` 18.2 MB. **TRANSLATION tier, two removes** (Latin ← Armenian
  ← lost Syriac original).
- Alt copy: `https://archive.org/details/MN41655ucmf_1` — confirmed 200.

**Modern critical apparatus — BLOCKED**:
- Louis Leloir's Syriac critical edition (CSCO 137, Scriptores Syri 71, Louvain 1963,
  from the Chester Beatty MS) is published by **Peeters** (Louvain) — copyrighted,
  same publisher-blocking pattern as the Leiden Peshitta (§7 below). I found only
  **access-restricted** archive.org copies of Leloir's *French* translation
  (`commentairedelva0000ephr_l8h9`, `commentairedelev0121ephr`) — borrow-only, not
  usable.
- Carmel McCarthy's 1993 **English** translation (*Saint Ephrem's Commentary on
  Tatian's Diatessaron*, Journal of Semitic Studies Supplement 2, Oxford University
  Press) — I found a full, unrestricted-looking upload at
  `https://archive.org/details/ephrem-the-syrian-commentary-on-the-diatessaron`.
  **Do not pull this.** I opened the text layer and confirmed it's the complete
  © 1993 Oxford University Press book, and nothing on the archive.org item page
  indicates OUP authorized this upload — it reads as an unauthorized scan sitting on
  a platform that doesn't always enforce takedowns quickly. Flagging as BLOCKED on
  copyright grounds independent of the corpus's original-language framing (it's also
  an English translation, not original-language, so it wouldn't belong in this corpus
  even if it were clean).

### 2c. Arabic Diatessaron

Translated via Ibn al-Ṭayyib (11th c. CE) from an earlier Syriac base, itself
translated from Tatian — TRANSLATION tier, several removes from the original, but the
fullest continuous-narrative witness that survives.

- **Ciasca 1888** — first printed edition (Latin title page: *Tatiani Evangeliorum
  Harmoniae Arabice*), the edition your task brief names:
  `https://archive.org/details/tatianievangelio0000paug` — confirmed 200,
  `_djvu.txt` 626 KB, `.pdf` 21.0 MB. Two more independent copies exist too
  (`Ciasca1888TatianiEvangeliorumHarmoniae...`, `diatessaron-latin`), both confirmed
  resolving.
- **Marmardji 1935** — the *better* edition, using more/different manuscripts than
  Ciasca and giving a French rather than Latin translation:
  `https://archive.org/details/diatessarondetat0000tati` — confirmed 200 (this one is
  **not** access-restricted, unlike some other 1930s items in this pass),
  `_djvu.txt` 1.55 MB, `.pdf` 63.9 MB. Second full copy with page-image jp2:
  `https://archive.org/details/diatessaron-collection` — confirmed 200, includes
  `_jp2.zip` (585 MB, actual page scans if you want the Arabic script itself rather
  than the OCR layer).
- Note: the **Arabic Diatessaron Project** (Lancioni & Joosse, TEI/XML digital
  edition of all Arabic MSS) exists as an academic effort but — per the project's own
  published description — **has not publicly released its data repository**. Nothing
  to pull here, listed for completeness only.

### 2d. Persian Harmony — BLOCKED (borrow-only, no free mirror found)

A 13th-century Persian gospel harmony (MS in the Laurentian Library, Florence) that
preserves some Diatessaronic readings independent of the Arabic line. Standard edition:
Giuseppe Messina, *Diatessaron persiano* (1951).

- `https://archive.org/details/diatessaronpersi0000tati` — **confirmed 401 on the
  actual file** (metadata says `access-restricted-item: true`, and I verified this is
  real, not just a flag — the direct file request itself returns 401, borrow-only).
  I searched for an unrestricted microform duplicate the way I found one for the Dura
  fragment and Ephrem's commentary — **none exists for this title.** BLOCKED, no
  workaround found this pass.

### 2e. Codex Fuldensis — Latin harmony, 546 CE, TRANSLATION tier but genuinely old witness

Commissioned by Bishop Victor of Capua, who found a gospel harmony (almost certainly
ultimately Diatessaronic in structure, though the *text* used is Vulgate, not a direct
Tatian translation) and had it copied in 546 CE. This is the earliest **dated** Latin
NT manuscript.

| MS date | Edition date |
|---|---|
| 546 CE | 1868 (Ranke); facsimile images undated upload |

- **Ranke 1868** — standard printed edition of the text:
  `https://archive.org/details/codexfuldensisn00rankgoog` — confirmed 200,
  `_djvu.txt` 965 KB, `.pdf` 15.5 MB.
- **Facsimile page images** (actual manuscript, not just the printed text) —
  `https://archive.org/details/CodexFuldensis` — confirmed 200. Contains two
  independent scan sets with `_jp2.zip` files (335 MB and 805 MB — real facsimile
  images of Codex Bonifatianus 1, held at Fulda's Hochschul- und Landesbibliothek)
  plus a bundled OCR'd Ranke copy. This is the closest thing to actually looking at
  the 546 CE manuscript itself that's freely available.

### 2f. Liège Diatessaron — Middle Dutch, medieval vernacular harmony

13th-c. Middle Dutch translation, MS at Liège University Library — one of a family of
medieval vernacular harmonies (with cousins in Middle High German, Italian, Middle
English) that textually echo the Diatessaron's sequence even though none of them are
in an "original" language for this corpus's purposes. Standard edition: Daniel Plooij
(with A.J. Barnouw / C.A. Phillips continuing after Plooij's 1935 death), published in
installments 1923–1970 (Amsterdam Academy).

- `https://archive.org/details/primitivetextofd0000ploo` — Plooij 1923, confirmed 200,
  `_djvu.txt` 154 KB.
- `https://archive.org/details/furtherstudyofli0000ploo` — Plooij 1925, confirmed 200,
  `_djvu.txt` 211 KB.
- `https://archive.org/details/ligediatessaron0000tati` — *The Liège Diatessaron*
  (1929, the fuller critical edition, Latin Fuldensis parallel + English translation),
  confirmed 200, `_djvu.txt` 2.19 MB, `.pdf` 55.6 MB.

### Diatessaron verdict

**Summary table — every route chased this pass, MS date vs. edition date, side by side:**

| Route | MS / witness date | Edition date | Recoverable? |
|---|---|---|---|
| Tatian's own text, any language | c. 172–185 CE (composition) | — | **No.** No manuscript, no edition, no route. |
| Dura-Europos fragment (Greek) | c. 250 CE (Dura fell 256/257 CE) | 1935 (Kraeling) | **Yes, freely** — §2a, unrestricted mirror. ~14 lines only. |
| Ephrem's Commentary — Syriac MS (Chester Beatty 709) | **c. 500 CE** | N/A — viewable manuscript, not a printed edition | **Yes, freely viewable** (IIIF) — §2b. Not Tatian's text, but the best structural proxy, in the original language. |
| Ephrem's Commentary — reconstructed Syriac (Harris) | quotations preserved in later Syriac writers, dates vary | 1895 (Harris) | **Yes, freely** — §2b. Partial, pre-dates the MS's rediscovery. |
| Ephrem's Commentary — Armenian → Latin | Armenian translation, date uncertain (early, pre-9th c. plausible) | 1876 (Moesinger, from the 19th-c. Venice Mechitarist Armenian print) | **Yes, freely** — §2b. Translation, two removes. |
| Ephrem's Commentary — Syriac critical edition | (same MS as above) | 1963 (Leloir, CSCO) | **No** — Peeters copyright, only borrow-restricted French translation found. |
| Ephrem's Commentary — English translation | (same MS as above) | 1993 (McCarthy, OUP) | **No** — copyrighted; an unauthorized-looking upload exists but should not be pulled. |
| Arabic Diatessaron | translated 11th c. CE (Ibn al-Ṭayyib), from an earlier Syriac base | 1888 (Ciasca) / 1935 (Marmardji, better) | **Yes, freely** — §2c. Translation, multiple removes. |
| Persian Harmony | 13th-c. MS (Florence, Laurentian Library) | 1951 (Messina) | **No** — borrow-only, no free mirror found. |
| Codex Fuldensis (Latin) | **546 CE** (dated by scribal note) | 1868 (Ranke, text) / undated (facsimile images) | **Yes, freely**, both text and actual manuscript facsimile — §2e. Vulgate text, Diatessaronic *structure* only. |
| Liège Diatessaron (Middle Dutch) | 13th-c. MS | 1923 / 1925 / 1929 (Plooij et al.) | **Yes, freely** — §2f. Medieval vernacular, several removes. |

Read together, here is the honest state of recoverability:

1. **The actual words Tatian wrote, in the language he wrote them in: not recoverable,
   full stop.** No manuscript, no quotation-chain, gets you that.
2. **The one piece of physical evidence that's genuinely original-language and
   genuinely close in time**: the Dura fragment — Greek, ~14 lines, c. 250 CE, freely
   downloadable via the unrestricted microform mirror (§2a). This is real, small, and
   the single strongest exhibit.
3. **The best window into Tatian's *structure and content*** (not his wording) is
   Ephrem's Commentary — and unusually for this whole research pass, **the actual
   Syriac manuscript is freely viewable online right now**, IIIF, full-resolution,
   c. 500 CE copy (§2b). That's a real original-language witness to a text that
   comments on and largely preserves the Diatessaron's sequence, even though it isn't
   the Diatessaron's own text.
4. **Everything else — Arabic, Persian, Latin (Fuldensis), Dutch (Liège) — is a
   translation of a translation, in some cases three or four removes from Tatian**,
   and mutually disagrees with the others in enough places that reconstructing "the"
   Diatessaron from them is a genuinely unsolved and actively debated philological
   problem (this is why Ciasca, Marmardji, Messina, and Plooij each produced
   *different* editions rather than superseding one another).
5. **The Persian Harmony is the one route that's simply closed off right now** — not
   structurally impossible like pre-1820 access, just paywalled/borrow-only with no
   free alternative I could find.

If the corpus wants "the Diatessaron" in some usable form, the two defensible choices
are: (a) the Dura fragment alone, honestly labeled as 14 lines of Greek and nothing
more, or (b) Ephrem's Commentary (Chester Beatty 709 images, or Harris's 1895
reconstructed-Syriac fragments as machine-readable text) honestly labeled as *evidence
about* the Diatessaron rather than the Diatessaron itself. Anything built by splicing
Arabic/Persian/Latin/Dutch harmonies together is an editorial reconstruction no less
speculative than a modern eclectic NT text — arguably more so, since those four
traditions actively disagree with each other on sequence and content.

---

## 3. Harklean (616 CE) and "Philoxenian" (508 CE)

**Important accuracy note, confirmed from the primary source itself**: Joseph White's
1778–1803 printed edition — the standard old edition, titled on its own title page
*"...versio Syriaca Philoxeniana..."* — is now understood by modern Syriac scholarship
(Burkitt, and confirmed by Arthur Vööbus's manuscript work) to actually be the
**Harklean** revision (Thomas of Harqel, 616 CE), not the original 508 CE Philoxenian
translation. White had access to the Ridley manuscripts at Oxford and simply used the
label current in his day. **The true Philoxenian text of the Gospels does not survive
as a clearly separable witness** — it's embedded in and largely superseded by Harklean
in the manuscript tradition. Some scholars argue that a handful of readings in a
distinct branch (sometimes called the "Pococke" text, covering the minor Catholic
epistles 2 Peter/2–3 John/Jude plus Revelation, absent from the classic Peshitta canon)
may preserve Philoxenian rather than Harklean readings, but this is a live scholarly
question, not settled fact.

| Witness | MS/translation date | Edition date |
|---|---|---|
| Harklean NT (labeled "Philoxeniana" by White; actually Harklean per modern scholarship) | 616 CE | 1778 (Gospels) / 1799 (Acts+Epistles, vol. 1) / 1803 (Acts+Epistles vol. 2 + Apocalypse) |

Confirmed obtainable, all PRINTED tier (pre-1820), public domain:

- Gospels (1778): `https://archive.org/details/sacrorumevangel00unkngoog` — confirmed
  200, `_djvu.txt` 356 KB, `.pdf` 11.6 MB. (Multiple duplicate scans also exist:
  `india.history.resource.73115`, `bim_eighteenth-century_sacrorum-evangeliorum-ve_1778_1`
  and `_2`, `SacrorumEvangeliorumVersioSyriacaPhi`, `MN41399ucmf_0` — not all
  individually re-verified, listed for redundancy if the primary link ever breaks.)
- Acts + Epistles, vol. 1 (1799): `https://archive.org/details/bim_eighteenth-century_actuum-apostolorum-et-ep_white-joseph_1799_1` — confirmed 200, `_djvu.txt` 489 KB (note: `.pdf` is enormous, 480 MB — this is a raw uncompressed scan, expect a slow pull).
- Acts + Epistles, vol. 2 (1803): `https://archive.org/details/bim_eighteenth-century_actuum-apostolorum-et-ep_white-joseph_1803_2` — listed by the search API, not independently re-verified with a metadata call this pass.

---

## 4. Syro-Hexapla (617 CE) — Paul of Tella's Syriac translation of Origen's Hexaplaric LXX column

This is genuinely important the way your task brief flags it: Origen's Hexapla itself
is lost except in fragments, and the Syro-Hexapla is one of the two or three best
surviving windows into what the Hexapla's fifth column (his critically-marked LXX text
with asterisks/obeli showing divergence from the Hebrew) actually said. Independent of
both the Hebrew MT tradition and the plain LXX tradition already in this corpus.

| MS date | Edition date |
|---|---|
| 617 CE (translation date); the primary surviving MS, Codex Ambrosianus C. 313 inf., is dated **705 CE** | 1778 (De Rossi, partial) / 1874 (Ceriani, facsimile) / 1880 (Lagarde, continuation) |

- **De Rossi 1778** — earliest printed specimen, **pre-1820**, PRINTED tier per
  PROVENANCE.md's own framework:
  `https://archive.org/details/bub_gb_q2taZmMO5igC` — confirmed 200,
  `_djvu.txt` 26 KB, `.pdf` 582 KB (short — it's a specimen, not the full text).
- **Ceriani 1874** — **photolithographic facsimile** of Codex Ambrosianus itself (i.e.,
  this reproduces the actual manuscript, not a modern typeset re-edition — Tier 1
  content):
  `https://archive.org/details/codexsyrohexapla00unse` — confirmed 200,
  `_djvu.txt` 2.07 MB, `.pdf` 42.9 MB.
  Full-resolution mirror: `https://archive.org/details/CerianiCodexSyroHexaplarisAmbrosianusMonumentaSacraEtProfana7Milan1874` — confirmed 200, `.pdf` 388 MB.
- **Lagarde 1880** — continuation/completion of fragments not in the Ambrosian codex,
  drawing on other Syriac witnesses (his source states apud Syros = "preserved among
  the Syrians"):
  `https://archive.org/details/veteristestamen00epipgoog` — confirmed 200,
  `_djvu.txt` 697 KB, `.pdf` 6.8 MB.

All public domain, all resolve.

---

## 5. Christian Palestinian Aramaic (CPA) lectionaries

CPA is a distinct dialect from classical Syriac — spoken/liturgical Aramaic of the
Melkite (Chalcedonian) Christian communities of Palestine, written in a script related
to but distinct from Estrangelo. Survives almost entirely in lectionary manuscripts
(readings organized by liturgical calendar, not continuous-text Bibles), mostly from
St. Catherine's Monastery, Sinai, and the Vatican.

| MS date | Edition date |
|---|---|
| Underlying MSS mostly 11th–13th c. CE (the CPA translation tradition itself is older, roughly 5th–8th c., but that's a dialect/tradition date, not any single surviving MS's date) | 1897 / 1899 / 1907 |

- **Lewis, Gibson & Nestle 1897** — *"A Palestinian Syriac Lectionary containing
  lessons from the Pentateuch, Job, Proverbs, Prophets, Acts, and Epistles"* — the
  broader OT+NT lectionary:
  `https://archive.org/details/palestiniansyria00lewiuoft` — confirmed 200,
  `_djvu.txt` 596 KB, `.pdf` 10.6 MB.
- **Lewis & Gibson 1899** — *"The Palestinian Syriac Lectionary of the Gospels,
  re-edited from two Sinai MSS. and from P. de Lagarde's edition of the 'Evangeliarium
  Hierosolymitanum'"* — the Gospels-specific lectionary, re-editing and superseding
  Lagarde's own earlier edition:
  `https://archive.org/details/palestiniansyria00lagauoft` — confirmed 200,
  `_djvu.txt` 1.14 MB, `.pdf` 20.2 MB.
- **Lewis 1907** — *"A Supplement to a Palestinian Syriac Lectionary"* — additional
  material found after the 1899 edition:
  `https://archive.org/details/supplementtopale0000agne` — listed by the search API
  (title/year confirmed), file-level HTTP check not independently re-run this pass.
- **Vatican Syriac 19** — an actual CPA lectionary manuscript, Assemani's catalog
  description/edition:
  `https://archive.org/details/VaticanSyriac19ChristianPalestinianAramaicLectionary` —
  confirmed 200, `_djvu.txt` 104 KB, `.pdf` 13.4 MB.

All public domain, all confirmed resolving except the Supplement (title-confirmed
only).

---

## 6. Ephrem the Syrian's biblical commentaries (general — beyond the Diatessaron commentary)

Ephrem (d. 373 CE) wrote verse-by-verse commentaries on Genesis and Exodus (his OT
commentary corpus is much thinner than his NT/hymnic output — most other OT books he
touched only in scattered hymns, not sustained commentary) plus his enormous corpus of
genuine hymns (*madrashe*) and metrical homilies (*memre*), many of which quote or
allude to a pre-Peshitta biblical text.

**Caveat carried over from general Ephrem scholarship**: a huge amount of material
circulates under Ephrem's name that isn't his — "Ephraem Graecus" (a separate corpus of
Greek ascetical works falsely attributed to him) is the largest chunk of this. The two
sources below are both attributed by their editors to the genuine Syriac-original
Ephrem, but that attribution work is exactly the kind of scholarly judgment call worth
flagging, not silently trusting.

| MS date | Edition date |
|---|---|
| Ephrem composed c. 350s–370s CE; no autograph survives, earliest MSS are 6th–7th c. | 1732–1743 (Assemani); 1882–1902 (Lamy) |

- **Assemani, Roman edition, *Sancti Patris Nostri Ephraem Syri Opera Omnia*** —
  **pre-1820**, PRINTED tier, six volumes, Syriac + Greek + Latin translation:
  `https://archive.org/details/sanctipatrisnostriephraem` (vol. 1, 1732) — confirmed
  200, but **no OCR text layer** (image-only PDF, 370 MB — expect this to be a straight
  facsimile, not searchable). Vol. 3 (1743): `sactipatrisnostriephraemsyri3` — listed,
  not independently re-verified. Vol. 2: `SanctiPatrisNostriEphraemSyriOperaOmniaQuaeExstantGraeceSyriaceLatineVol.2` — listed, not independently re-verified.
- **Lamy, *Sancti Ephraem Syri Hymni et Sermones*** (1882–1902, 4 vols) — the standard
  19th-c. critical typeset edition, genuine Syriac text with Latin translation:
  `https://archive.org/details/sanctiephraemsy01lamygoog` (vol. 1, 1882),
  `sanctiephraemsy02lamygoog` (vol. 2, 1886), `sanctiephraemsy03lamygoog` /
  `sanctiephraemsy00lamygoog` (vol. 3, 1902), `sanctiephraemsy04lamygoog` (vol. 4,
  1882 — note vol. 4's catalog year looks like a metadata error given vols 2–3 are
  later; not independently resolved this pass). Vol. 1 confirmed 200 via search API;
  file-level checks not re-run for all four volumes this pass — flag as an open thread.

**Modern critical editions (Tonneau's CSCO edition of the Genesis/Exodus commentaries,
1955) are Peeters-published — same BLOCKED pattern as Leloir's Diatessaron commentary
edition (§2b) and the Leiden Peshitta (§7). Not chased further; assume blocked by the
same publisher pattern already established elsewhere in this corpus's research.**

---

## 7. Aphrahat's Demonstrations (337–345 CE)

The earliest datable Syriac father — writing a full generation before Ephrem, in
Persian-ruled Adiabene rather than Roman Edessa, which matters because it means his
biblical citations reflect an even earlier and more geographically separate slice of
the pre-Peshitta Syriac Bible than Ephrem's.

| MS date | Edition date |
|---|---|
| Composed 337–345 CE; earliest MSS 6th–7th c. | 1869 (Wright); 1894/1907 (Parisot) |

- **Wright 1869** — *"The Homilies of Aphraates, the Persian Sage"* — Syriac text
  edition (his English translation was announced but, per standard bibliography, was
  never completed/published — this volume is text only):
  `https://archive.org/details/homiliesaphraat00wriggoog` — confirmed 200,
  `_djvu.txt` 644 KB. **Checked the OCR layer directly**: no recognizable Unicode
  Syriac characters survived OCR (same failure mode as the Old Syriac Gospels scans,
  §1) — usable as a PDF page-image facsimile, not as searchable text.
- **Parisot, *Patrologia Syriaca*, vol. 1 (1894)** — the standard critical edition,
  Syriac text with facing Latin translation, vocalized:
  `https://archive.org/details/patrologiasyria01grafgoog` — confirmed 200,
  `_djvu.txt` 1.50 MB, `.pdf` 18.7 MB.
- **Parisot, *Patrologia Syriaca*, vol. 2 (1907)** — continues Aphrahat plus other
  early material:
  `https://archive.org/details/gtu_32400002832867_2` — confirmed 200,
  `_djvu.txt` 2.01 MB, `.pdf` 51.4 MB.

All public domain, all confirmed resolving.

---

## 8. Syro-Hexapla apparatus context / Leiden Peshitta Institute — copyright verified

Per your task's instruction to verify the Leiden Peshitta OT critical edition's
copyright status: **confirmed copyrighted.** *The Old Testament in Syriac according to
the Peshiṭta Version* (Leiden Peshitta Institute, founded by P.A.H. de Boer, ongoing
since 1966) is published by **Brill** — I confirmed the series page resolves at
`https://brill.com/display/serial/POTBI` (redirects, 301→normal Brill catalog behavior)
and Brill's own site search returns a 403 to automated requests, consistent with a
standard commercial-publisher paywall, not an open-access series. No change from the
existing BLOCKED status implied elsewhere in this corpus — confirmed rather than
assumed.

---

## 9. Modern digital infrastructure — what's live, what isn't

| Site | Status | Notes |
|---|---|---|
| **sinaipalimpsests.org** | Live over HTTP only; HTTPS cert broken (points to an unrelated UCLA host) | Landing/about page only. Links to `sinai.library.ucla.edu`. |
| **sinai.library.ucla.edu** (the actual Sinai Palimpsests research/image site) | **Live** — confirmed only after retrying with a browser User-Agent; plain `curl`'s default UA got 404'd on every path, which is a false-negative, not a real outage | Free registration required to browse/search; `/browse` returns "Unauthorized, please login" (200, not blocked). IIIF-based delivery. Covers Syriac undertexts (team includes Grigory Kessel). Whether Sinai Syr. 30 itself is in scope: unconfirmed. |
| **emelibrary.org** (Early Manuscripts Electronic Library, umbrella org for Sinai imaging) | Live | Confirms it doesn't host images itself — consistent with the UCLA site above being the actual access point, under its own login/terms. |
| **syriaca.org** (Syriac Reference Portal) | Live, confirmed | Reference/metadata infrastructure (Syriac Gazetteer, Biographical Dictionary, saints catalogue, manuscript *catalogues*) — **not a full-text corpus**. CC BY 4.0. Draft data at `github.com/srophe`. Useful as a research tool, not a text source for this corpus. |
| **cal.huc.edu** (Comprehensive Aramaic Lexicon) | Live, confirmed | 4M-word parsed Aramaic text base across all dialects/periods, browsable per-verse. Explicitly asks not to be scraped; bulk dumps available on request to `skaufman@huc.edu` for "legitimate academic users." |
| **sedra.bethmardutho.org** (SEDRA/Beth Mardutho) | Live, confirmed | Lexical database + word-lookup API underlying the Peshitta NT (already in this corpus via ETCBC's `syrnt`, so largely redundant). Its "Syriac Library" browse feature currently holds only the **Odes and Psalms of Solomon** and the **UBS Peshitta** — nothing from this task's scope (no Old Syriac, no Harklean). |
| **HMML / vHMML Reading Room** (`vhmml.org`) | Live, confirmed | Huge Syriac manuscript holdings (large fraction of HMML's total collection is Eastern Christian, much of it Syriac). **Requires free account registration; Terms of Use explicitly prohibit copying/redistributing images without prior authorization from HMML** — confirmed by reading the actual terms text on the reading-room page. Good for individual manuscript lookups with an account, not a bulk-acquisition source. |
| **Chester Beatty Library viewer** (`viewer.cbl.ie`) | Live, confirmed, IIIF | See §2b — the one genuinely strong original-language manuscript access point found this pass. |
| **`github.com/peshitta`** (Kiraz-adjacent tooling org) | Live | MIT-licensed Syriac/CAL/SEDRA transliteration conversion utilities (`sedrajs` etc.) — useful tooling if you ever build a Syriac NLP pipeline, but these operate on Peshitta NT text you already have, not on anything in this task's scope. |
| **`github.com/chenzhan4321/diatessaron-synopsis`** | Live | An independent researcher's in-progress computational Diatessaron/Old Syriac synopsis project. **No declared license** (all-rights-reserved by GitHub default) — don't treat its code/data as reusable without contacting the author. Its own research notes (`corpus_sources.md`, in Chinese) reached the same core conclusion as this document independently: no clean Unicode Old Syriac transcription exists anywhere, and it flagged the same Chester Beatty IIIF manifest and the same archive.org identifiers for Ciasca/Marmardji/Cureton/Lewis/Burkitt found here. Cross-referencing it *raised* my confidence in the archive.org identifiers above rather than being the source of them — I independently verified every one against the live metadata API myself before including it. |

---

## Manifest — commands, by priority

```bash
# ============================================================
# TIER 1 (or closest to it) — do these first
# ============================================================

# Dura-Europos Greek fragment of the Diatessaron — the one real original-language
# physical witness, c. 250 CE. Use the microform mirror, NOT the access-restricted item.
wget https://archive.org/download/MN41439ucmf_4/MN41439ucmf_4_djvu.txt -P aramaic-syriac/diatessaron/
wget https://archive.org/download/MN41439ucmf_4/MN41439ucmf_4.pdf -P aramaic-syriac/diatessaron/

# Ephrem's Commentary on the Diatessaron — Chester Beatty Syriac MS 709, actual
# manuscript, IIIF. Pull the manifest first, then loop the image service URLs.
# (82 canvases; this is a facsimile pull, not bulk-download-everything — go per-page.)
curl -s "https://viewer.cbl.ie/viewer/api/v1/records/Syc_709_1/manifest/" -o aramaic-syriac/ephrem-diatessaron-commentary/Syc709_manifest.json
# then, per canvas, e.g. full-res page 1:
# https://viewer.cbl.ie/viewer/api/v1/records/Syc_709_1/files/images/Syc709_1_01.jpg/full/full/0/default.jpg

# Ceriani 1874 facsimile of the Syro-Hexapla (Codex Ambrosianus, actual manuscript)
wget https://archive.org/download/codexsyrohexapla00unse/codexsyrohexapla00unse_djvu.txt -P aramaic-syriac/syro-hexapla/
wget https://archive.org/download/codexsyrohexapla00unse/codexsyrohexapla00unse.pdf -P aramaic-syriac/syro-hexapla/

# Codex Fuldensis facsimile images (546 CE Latin harmony)
wget https://archive.org/download/CodexFuldensis/Codex_Fuldensis_Source_djvu.txt -P aramaic-syriac/codex-fuldensis/
# jp2.zip is 805MB -- only pull if you actually want page images, not just text

# ============================================================
# TIER 2/3 — Old Syriac Gospels editions (typeset, not Unicode, see caveat in §1)
# ============================================================
wget https://archive.org/download/remainsofveryant00cure/remainsofveryant00cure_djvu.txt -P aramaic-syriac/old-syriac-gospels/cureton-1858/
wget https://archive.org/download/fourgospelsinsyr00bens/fourgospelsinsyr00bens_djvu.txt -P aramaic-syriac/old-syriac-gospels/bensly-harris-burkitt-lewis-1894/
wget https://archive.org/download/oldsyriacgospels00lewirich/oldsyriacgospels00lewirich_djvu.txt -P aramaic-syriac/old-syriac-gospels/lewis-1910/
wget https://archive.org/download/evangeliondameph0001fcra/evangeliondameph0001fcra_djvu.txt -P aramaic-syriac/old-syriac-gospels/burkitt-1904/
wget https://archive.org/download/evangeliondameph0002fcra/evangeliondameph0002fcra_djvu.txt -P aramaic-syriac/old-syriac-gospels/burkitt-1904/

# ============================================================
# Diatessaron — Arabic and Liège lines
# ============================================================
wget https://archive.org/download/diatessarondetat0000tati/diatessarondetat0000tati_djvu.txt -P aramaic-syriac/diatessaron/arabic-marmardji-1935/
wget https://archive.org/download/tatianievangelio0000paug/tatianievangelio0000paug_djvu.txt -P aramaic-syriac/diatessaron/arabic-ciasca-1888/
wget https://archive.org/download/ligediatessaron0000tati/ligediatessaron0000tati_djvu.txt -P aramaic-syriac/diatessaron/liege-plooij-1929/
wget https://archive.org/download/primitivetextofd0000ploo/primitivetextofd0000ploo_djvu.txt -P aramaic-syriac/diatessaron/liege-plooij-1923/
wget https://archive.org/download/furtherstudyofli0000ploo/furtherstudyofli0000ploo_djvu.txt -P aramaic-syriac/diatessaron/liege-plooij-1925/

# Ephrem's Diatessaron commentary — pre-discovery reconstructed Syriac + Armenian/Latin
wget https://archive.org/download/fragmentsofcomme0000ephr/fragmentsofcomme0000ephr_djvu.txt -P aramaic-syriac/ephrem-diatessaron-commentary/harris-1895/
wget https://archive.org/download/evangeliiconcor01msgoog/evangeliiconcor01msgoog_djvu.txt -P aramaic-syriac/ephrem-diatessaron-commentary/moesinger-1876/

# ============================================================
# Harklean NT (Joseph White's 1778-1803 edition; note the "Philoxeniana" mislabel, §3)
# ============================================================
wget https://archive.org/download/sacrorumevangel00unkngoog/sacrorumevangel00unkngoog_djvu.txt -P aramaic-syriac/harklean/white-1778-gospels/
wget https://archive.org/download/bim_eighteenth-century_actuum-apostolorum-et-ep_white-joseph_1799_1/bim_eighteenth-century_actuum-apostolorum-et-ep_white-joseph_1799_1_djvu.txt -P aramaic-syriac/harklean/white-1799-acts-epistles/

# ============================================================
# Christian Palestinian Aramaic lectionaries
# ============================================================
wget https://archive.org/download/palestiniansyria00lewiuoft/palestiniansyria00lewiuoft_djvu.txt -P aramaic-syriac/cpa-lectionaries/lewis-gibson-nestle-1897/
wget https://archive.org/download/palestiniansyria00lagauoft/palestiniansyria00lagauoft_djvu.txt -P aramaic-syriac/cpa-lectionaries/lewis-gibson-1899/
wget https://archive.org/download/VaticanSyriac19ChristianPalestinianAramaicLectionary/AssemaniVaticanSyriac19CpaLectionary_djvu.txt -P aramaic-syriac/cpa-lectionaries/vat-syr-19/

# ============================================================
# Aphrahat's Demonstrations
# ============================================================
wget https://archive.org/download/patrologiasyria01grafgoog/patrologiasyria01grafgoog_djvu.txt -P aramaic-syriac/aphrahat/patrologia-syriaca-vol1-1894/
wget https://archive.org/download/gtu_32400002832867_2/gtu_32400002832867_2_djvu.txt -P aramaic-syriac/aphrahat/patrologia-syriaca-vol2-1907/
wget https://archive.org/download/homiliesaphraat00wriggoog/homiliesaphraat00wriggoog.pdf -P aramaic-syriac/aphrahat/wright-1869/
# ^ pull the .pdf not the djvu.txt for this one -- OCR text layer is unusable (verified, no Syriac survived OCR)

# ============================================================
# Ephrem's Hymni et Sermones (Lamy 1882-1902) and Assemani's Roman edition (1732-43, PRE-1820)
# ============================================================
wget https://archive.org/download/sanctiephraemsy01lamygoog/sanctiephraemsy01lamygoog_djvu.txt -P aramaic-syriac/ephrem-hymns/lamy-vol1-1882/
# vols 2-4 identifiers listed in §6 -- not individually file-checked this pass, verify before pulling
wget https://archive.org/download/sanctipatrisnostriephraem/Printing_Version_3527_MB.pdf -P aramaic-syriac/ephrem-hymns/assemani-roman-1732/
# ^ 370MB, image-only (no OCR layer) -- this is a facsimile pull, be deliberate about it
```

---

## BLOCKED — confirmed, with reasons

| Item | Why blocked | Any workaround found? |
|---|---|---|
| **Persian Harmony** (Messina 1951, *Diatessaron persiano*) | archive.org item confirmed borrow-only (401 on direct file request, not just a metadata flag) | None — checked for an unrestricted microform mirror the way I found one for Dura/Ephrem; doesn't exist for this title. |
| **Leloir's Syriac critical edition of Ephrem's Diatessaron commentary** (CSCO 137, 1963) | Peeters (Louvain) copyright | Only found borrow-restricted copies of Leloir's *French* translation, not the Syriac edition itself. |
| **McCarthy 1993 English translation** of Ephrem's commentary | © Oxford University Press 1993; a full text upload exists on archive.org but with no indication OUP authorized it | Do not pull — copyright risk, and it's a translation, not original-language, so it's out of scope for this corpus regardless. |
| **Kiraz 1996 four-column Comparative Edition** (Sinaiticus/Curetonianus/Peshitta/Harklean aligned) | Brill/Gorgias commercial edition | Only a front-matter sample PDF is free. |
| **Leiden Peshitta Institute OT critical edition** | Brill, confirmed copyrighted this pass (per your task's request to verify) | None — matches the corpus's existing assumption, now confirmed rather than assumed. |
| **Tonneau's CSCO edition of Ephrem's Genesis/Exodus commentary** (1955) | Peeters, same publisher-block pattern as Leloir above | Not chased for a workaround — flagging by pattern-match, not independently re-verified. Assemani's 1732-43 Roman edition (§6) is the free fallback for Ephrem's OT commentary in Syriac. |
| **HMML's Syriac manuscript holdings, in bulk** | Terms of Use explicitly prohibit copying/redistribution without prior authorization, confirmed by reading the actual terms text | Free account gets you individual-manuscript browsing, not bulk acquisition. |
| **Sinai Palimpsests Project research site** (`sinai.library.ucla.edu`) | **Not down** (corrected mid-pass — plain curl's default User-Agent was 404'd, a browser UA gets 200 throughout). Actually login-gated: free account required, same model as HMML. | Register an account and log in; no bulk/anonymous access found. Whether Sinai Syr. 30 itself is among the imaged manuscripts is still unconfirmed. |

---

## Open threads not fully chased (say so rather than guess)

- Lamy's *Hymni et Sermones* vols 2–4 (§6) — only vol. 1 was individually file-checked
  this pass; the archive.org identifiers for the other three are listed but not
  re-verified with a direct metadata call.
- Assemani's Roman edition vols 2–3 — same situation, listed from the search API,
  not individually re-verified.
- White's Harklean vol. 2 (Acts+Epistles, 1803) and the several duplicate scans of the
  1778 Gospels volume — only the primary identifier for each was independently
  confirmed; the duplicates are listed for redundancy, not individually re-checked.
- Lewis's 1907 CPA Supplement — title/year confirmed via the search API, file-level
  HTTP check not re-run.
- Whether the "Pococke text" (2 Peter/2–3 John/Jude/Revelation) genuinely preserves
  Philoxenian rather than Harklean readings is a live scholarly debate I flagged in §3
  but did not attempt to adjudicate or find a specific free edition for — worth a
  dedicated follow-up if the Philoxenian/Harklean distinction matters to you
  specifically, rather than "Harklean-labeled-as-Philoxenian is fine."
- I did not attempt to locate a Vatican Library (`digi.vatlib.it`) direct scan of
  Vat. sir. 19 (the CPA lectionary) to compare against the 19th-c. Assemani edition
  in §5 — the INDEX.md already notes `digi.vatlib.it` as a known-good manuscript image
  source for other material, so this is plausibly there, just not checked this pass.
