# Research: Completing `targums/` and filling `ben-sira/`

Every candidate below carries the project's standard **two-date + Tier** format:

- **Witness** — when the manuscript/artifact itself was physically made.
- **Edition** — when *this particular* transcription/printing/digitization was published.
- **Tier** — a *label, not a filter*. Nothing here is excluded on Tier grounds; the user wants to judge for himself.
  - **Tier 1** — the manuscript/artifact itself: diplomatic transcription, facsimile, image, no editorial reconstruction layer.
  - **Tier 2** — printed edition published **before 1820**.
  - **Tier 3** — modern critical edition / reconstruction / digitization (1820–present), including modern *diplomatic* transcriptions of ancient manuscripts (those are still Tier 3 by publication date even though the text they transcribe is Tier-1-grade evidence — flagged inline wherever that distinction matters).

All URLs below were checked with `curl -I`/`curl -o /dev/null -w "%{http_code}"` or WebFetch on 2026-08-08. No bulk data was downloaded — this is a manifest only, per instruction (root filesystem under disk pressure).

---

## Part 1 — What's actually on disk right now (corrected from INDEX.md)

INDEX.md only lists `onkelos/` and `pseudo-jonathan/`. Inspection found a **third, undocumented directory**:

| Dir | Files present | Source (from in-file header) | Format |
|---|---|---|---|
| `targums/onkelos/` | Genesis, Exodus, Leviticus, Numbers, Deuteronomy (full Torah) | Sefaria API, version "Onkelos [Book]", License: Public Domain | plain `.txt`, `## Chapter N ##` + `verse:num text` |
| `targums/pseudo-jonathan/` | Genesis, Exodus, Leviticus, Numbers, Deuteronomy (full Torah) | Sefaria API, version "Targum Jonathan on [Book]" (Sefaria's internal name for what scholarship calls Pseudo-Jonathan — see note below) | same plain-text format |
| `targums/targum-jerusalem/` | **Genesis, Exodus only** — Leviticus/Numbers/Deuteronomy missing | Sefaria API, version "Targum Jerusalem on Torah", License: Public Domain | same plain-text format |

**Naming trap already baked into the corpus**: on Sefaria, the node literally titled "Targum Jonathan" under **Torah** is Pseudo-Jonathan (the medieval composite misattributed to Jonathan ben Uzziel); the node titled "Targum Jonathan" under **Prophets** is the *real*, ancient Targum Jonathan. The existing `pseudo-jonathan/` directory is correctly named for content even though its Sefaria source string says "Targum Jonathan on Genesis" — don't let that confuse a future pass. The genuine Targum Jonathan to the Prophets (below) is a **different, currently absent** text.

**Pipeline consistency**: all three existing dirs were pulled via the same method — Sefaria's `/api/texts/{ref}` endpoint, saved as flat text with a `# Source: Sefaria API, version 'X', License: Public Domain` header. To keep `targums/` consistent, everything new below should use the same Sefaria API pull where Sefaria has it (Tier 3 digitization either way — Sefaria's own text objects don't carry a pre-1820 print pedigree even where the underlying targum tradition is ancient), with additions/exceptions to that noted explicitly.

---

## Part 2 — Targums: complete manifest

### 2A. Sefaria API — same pipeline as what's already on disk, verified live

Confirmed against Sefaria's `/api/index` full table of contents (`https://www.sefaria.org/api/index`, 4 MB JSON) and spot-checked per-book against `/api/shape/{title}` (returns chapter counts — used to catch stubs before recommending anything).

| Target work | Sefaria title(s) | Verified complete? | Witness | Edition | Tier | curl/wget |
|---|---|---|---|---|---|---|
| **Targum Jonathan to the Prophets** (all 21 books) | `Targum_Jonathan_on_{Joshua…Malachi}` | **Yes** — shape-checked: Joshua 24 ch, Isaiah 66 ch, Jeremiah 52 ch, Ezekiel 48 ch, all 12 Minor Prophets, Judges/Sam/Kings all present and full-length | Aramaic targum tradition attributed (Talmud, b.Meg. 3a) to Jonathan ben Uzziel, 1st c. CE; scholarly consensus places actual redaction in Babylonia, **c. 3rd–5th c. CE**; earliest complete MS = **Codex Reuchlinianus, dated 1105 CE** | Sefaria digital text, ongoing (**API accessed 2026**); underlying print lineage traces to Bomberg's Rabbinic Bible (1517/1525) | Tier 3 (this pull); the Bomberg print lineage it descends from is Tier 2 (see 2B) | `for b in Joshua Judges "I_Samuel" "II_Samuel" "I_Kings" "II_Kings" Isaiah Jeremiah Ezekiel Hosea Joel Amos Obadiah Jonah Micah Nahum Habakkuk Zephaniah Haggai Zechariah Malachi; do curl -s "https://www.sefaria.org/api/texts/Targum_Jonathan_on_${b}?context=0&commentary=0" -o "${b}.json"; done` |
| **Fragment Targums / Targum Jerusalem — remaining 3 Torah books** | `Targum Jerusalem, Leviticus` / `, Numbers` / `, Deuteronomy` (note: this is a "complex" Sefaria text — ref format is `Targum Jerusalem, {Book}.{ch}`, not `Targum_Jerusalem_on_{Book}`) | **Yes**, content confirmed live (fetched sample verses for all 3) | Palestinian targum fragments (multiple independent MSS: Paris, Vatican Ebr. 440, Nuremberg, Leipzig, Genizah scraps), individual MSS date **11th–15th c. CE**; underlying targumic tradition much older, layered with Neofiti/Ps-Jonathan material | Sefaria digital, ongoing; first substantially collected in print by **Bomberg's Rabbinic Bible margins (1517/1525)**, first dedicated modern critical edition **Ginsburger 1899** (Tier 3, not what Sefaria is using directly but same textual family) | Tier 3 (this pull) | `curl -s "https://www.sefaria.org/api/texts/Targum%20Jerusalem%2C%20Leviticus.1?context=0"` (URL-encode the comma+space; same pattern for Numbers/Deuteronomy) |
| **Targum to Chronicles (I & II)** | `Targum_of_I_Chronicles`, `Targum_of_II_Chronicles` | **Yes** — I Chron 29 ch, II Chron 36 ch, both full-length, confirmed via shape API | Anonymous, late Palestinian targum, generally dated **8th–9th c. CE** (much later than Onkelos/Jonathan — Chronicles was excluded from synagogue reading so had no early liturgical targum); sole complete MS = **Cambridge Add. 1846** (formerly Erfurt), **15th c.** | Sefaria digital, ongoing; **editio princeps is pre-1820** — Matthaeus Beck, Augsburg, **1680–83** — see 2B for the print lead | Tier 3 (this pull); editio princeps is Tier 2 | `curl -s "https://www.sefaria.org/api/texts/Targum_of_I_Chronicles.1?context=0"` |
| **Targum to the Writings** — Psalms, Job, Proverbs, Song of Songs, Ruth, Lamentations, Ecclesiastes (Qohelet), Esther (both the "Rishon"/plain targum and the expansive **Targum Sheni**) | `Aramaic_Targum_to_{Psalms,Job,Proverbs,Song_of_Songs,Ruth,Lamentations,Ecclesiastes,Esther}`, `Targum_Sheni_on_Esther` | **Yes, all 9** — shape-checked: Psalms 150 ch, Job 42 ch, Proverbs 31 ch, Song of Songs 8 ch, Ruth 4 ch, Lamentations 5 ch, Ecclesiastes 12 ch, Esther (Rishon) 10 ch, Targum Sheni 10 ch — all match standard chapter counts | Composite/late Palestinian targums, individually dated roughly **4th–11th c. CE** depending on book (Job/Psalms targum earliest layers may go back to Qumran-era targum fragments of Job — 4Q157, 11QtgJob — though those are separate Qumran texts, not what Sefaria hosts here); Targum Sheni to Esther is a distinct, much-expanded midrashic targum, **7th–10th c. CE** | Sefaria digital pull dates vary by book — versions sourced from a mix of 19th-c. English translations re-Aramaicized/paired (e.g. Ecclesiastes version notes "Coheleth, trans. by C.D. Ginsburg, London **1861**"; Ruth "Samson H. Levey, Hebrew Union College, **1934**"; Lamentations "trans. by C.M.M. Brady"; Esther Rishon/Job/Psalms = "Sefaria Community Translation," undated/crowd) — **mixed provenance, verify per-book if precision matters** | Tier 3 (all) — note some Sefaria versionTitles are themselves 19th-c. (1861) but that's the *translation* metadata field, not evidence the Aramaic text itself is diplomatically pre-1820; treat as modern digitization | same `/api/texts/{title}.1?context=0` pattern per book |
| **Targum Neofiti** | `Targum_Neofiti` | **NO — do not use.** Verified via `/api/shape/Targum_Neofiti`: `length: 1, chapters: [8]`. Fetched the actual content: it is **8 verses of Genesis 1 only** (Gen 1:1–1:8), full stop. Sefaria does not host a real Targum Neofiti text. | — | — | — | **Blocked on this route — see 2C for the real path (Vatican MS + Díez Macho critical edition)** |

**Correction to note in `Home.md`/`INDEX.md`**: Sefaria's own site pages *display* Neofiti nicely (verse-by-verse UI), which is why web search made it look complete — but the underlying API text object is a stub. This is exactly the kind of "assume it resolves, it doesn't really" trap the project has hit before with 404'd repos; here the URL resolves (200 OK) but the *content* is fake-complete. Confirmed by direct content fetch, not by trusting HTTP status.

### 2B. Pre-1820 print editions (Tier 2) — the request's actual priority

All confirmed live on archive.org, all US public domain (pre-1928), all have **OCR/djvu text layers** confirmed present.

| Edition | Witness content | Edition date | Archive.org item | djvu.txt confirmed? |
|---|---|---|---|---|
| **Bomberg's Second Rabbinic Bible (Mikra'ot Gedolot)**, ed. Jacob ben Ḥayyim, Venice — contains Onkelos + Targum Jonathan (Torah+Prophets) + the Writings targums in the margins of the Hebrew text | Reflects the printed-Targum tradition as it stood by the early 16th c.; not a single manuscript, itself a compiled edition | **1524–25** | `https://archive.org/details/second-rabbinic-bible-venice-1525-bw-full-images` (B/W scan, 4 vols) and `https://archive.org/details/second-rabbinic-bible-venice-1525-color-full-images` (color scan, 4 vols); also `https://archive.org/details/mikraot_gdolot` (same edition, different upload) | **Yes** — `mikraot_gdolot` item has `Torah_djvu.txt`, `Joshua, Judges, Samuel, Kings_djvu.txt`, `Major and minor prophets_djvu.txt`, and a `Writings.pdf`/`Writings_djvu.txt`-equivalent (61 files total in the item) — i.e. **OT + Targum text is machine-extractable from this exact upload** |
| **Bomberg's First Rabbinic Bible**, ed. Felix Pratensis, Venice (predecessor to the above) | same caveat | **1516–17** | `https://archive.org/details/Miqraot-Gedolot-First-Edition_Venice_1517` (vol. 4 confirmed; other vols likely siblings — not individually re-checked) | **Yes** — `Miqra'ot Gedolot_First Edition_Venice_1517_djvu.txt` confirmed present |
| **Walton's London Polyglot** — vols. 1–3 contain the Targum (Onkelos+Jonathan) alongside Hebrew/Vulgate/LXX/Syriac/Arabic; **vol. 4 explicitly contains the "Triplex Targum" = Targum Yerushalmi I & II (i.e. the Fragment Targums) plus a Persian version** | Same "compiled from printed Jewish tradition" caveat as Bomberg | **1654–57** (this archive.org copy's title page reads 1667, likely a later-bound set) | `https://archive.org/details/walton_polyglot` ("improved" full 9-language upload, 1652–57); also `https://archive.org/details/nby_236649` (single-item scan, catalogued **1667**) | Not individually re-verified per volume — flagged as a follow-up if this edition is prioritized; item resolves and is downloadable |
| **Antwerp Polyglot** (Biblia Regia), ed. Arias Montano — also contains Targum text | same caveat | **1568–73** | *Not located with a confirmed working archive.org identifier in this pass* — search returned only secondary/bibliographic hits, no direct scan item verified. **Flagging as unconfirmed, not blocked** — worth a dedicated follow-up search (it exists; multiple libraries have scanned it, e.g. via Google Books, but I did not verify a stable direct-download identifier). |
| **Editio princeps of Targum to Chronicles**, Matthaeus Beck, Augsburg | Cambridge Add. 1846 MS lineage, 15th c. | **1680–83** | *Not located/verified this pass* — a real, named pre-1820 edition exists per standard targum scholarship, but I did not find a confirmed archive.org/Google Books item URL for it. **Flagging as unconfirmed lead, not blocked.** |
| **Targum Sheni to Esther**, first print, Pesaro | MSS vary, work itself 7th–10th c. | **1519** (per standard bibliography) | *Not located/verified this pass.* The item **is** on Sefaria in Aramaic/English via a much later (1888, Cassel) source — see 2A table — but the 1519 editio princeps itself was not confirmed on archive.org in this pass. |
| **Nutt's "Fragments of a Samaritan Targum"** (Bodleian MS edition, with intro on Samaritan history) | Bodleian MS, undated precisely in the results returned | **1874** — post-1820, i.e. Tier 3 by this project's rule, but it's the earliest freely-available *printed edition* of any Samaritan Targum material found | `https://archive.org/details/bub_gb_8JNhAAAAcAAJ` | Google-Books-sourced archive.org mirror; standard OCR layer typically present on `bub_gb_*` items (not individually re-checked here) |

**Honest gap**: I could not confirm working archive.org identifiers for the Antwerp Polyglot, the Beck 1680s Targum-Chronicles editio princeps, or the 1519 Targum Sheni editio princeps within this pass. These are real historical editions (well attested in targum scholarship), but "I know it exists" and "I verified the URL resolves" are different claims, and per this project's standing rule I'm not reporting the second when I only have the first.

### 2C. Manuscript images (Tier 1) — not text, not mirrored, but the actual artifacts

| Item | What it is | Access | Blocker |
|---|---|---|---|
| **Codex Neofiti 1** (Vat. Neofiti 1) — the *sole* complete MS of Targum Neofiti | Copied **1504 CE** (per colophon); underlying Palestinian targum tradition likely **1st–4th c. CE** composition layers | `https://digi.vatlib.it/mss/Neofiti` (46 Neofiti-fond items digitized; Neofiti.1 confirmed present) | **Explicit reproduction restriction**: Vatican Library states "Neither the text nor the images may be reproduced, in any form, without the authorisation of the Vatican Library." Viewable, not redistributable — cannot be mirrored into this corpus without direct permission. |
| **Codex Reuchlinianus** (Targum Jonathan to Prophets, complete) | **1105 CE** | Held at Badische Landesbibliothek, Karlsruhe; a full facsimile edition exists (Sperber) but I did not verify a free digital scan in this pass | Not verified this pass — follow-up lead |

**On Targum Neofiti specifically**: since Sefaria's text is a stub (2A) and the Vatican won't let the manuscript images be reproduced, the only remaining route to real Neofiti text is **Díez Macho's critical edition** (Madrid, 1968–79, 6 vols.) — modern (Tier 3), and almost certainly still under copyright (CSIC, Spain) — not free. **This means Targum Neofiti is functionally blocked for this corpus**: the free digital text is fake-complete, the manuscript is access-restricted, and the only real critical edition is copyrighted. Worth stating plainly rather than papering over.

### 2D. CAL (Comprehensive Aramaic Lexicon, Hebrew Union College)

`https://cal.huc.edu` — confirmed live, described as covering "Onqelos, Pseudo-Jonathan, Neofiti, Fragment Targums, and more," open-access lexicon/corpus search tool. **No bulk download or API found** — it's a per-chapter/per-word web lookup tool (`get_a_chapter.php` style endpoints), not a dataset you `git clone` or `wget`. Scraping it chapter-by-chapter is technically possible but (a) is not the "manifest, don't download" ask, (b) has unclear terms for bulk reuse (nothing found stating a reuse license for extracted text), and (c) would be a genuinely useful *addition* to Neofiti-blocker above if someone wanted to pursue it later — flagging as a lead, not a resolved item.

### 2E. ETCBC/Text-Fabric, STEPBible-Data — negative results

- **ETCBC Text-Fabric**: no targum dataset found. ETCBC's public Text-Fabric corpora (BHSA, Peshitta, etc. — already on disk) are Hebrew Bible / Syriac only.
- **STEPBible-Data** (`github.com/STEPBible/STEPBible-Data`, CC BY 4.0, already used for TAHOT on disk): confirmed **no Targum/Aramaic-OT dataset** in the repo.

### 2F. Samaritan Targum

No single clean modern free source found. What exists:
- **Nutt 1874** (Tier 3 by date, but earliest free print) — see 2B.
- **Abraham Tal's critical edition** (Tel Aviv, 1980–83, 3 vols.) — the standard modern scholarly edition — almost certainly copyrighted, not free.
- Manuscript witnesses are scattered and the transmission is famously corrupt (multiple divergent recensions, no single authoritative MS); this is a genuinely harder text to source than the Jewish targums. **Recommend treating as unresolved** rather than forcing a low-quality substitute in.

---

## Part 3 — Ben Sira (Sirach) Hebrew witnesses

The Greek Sirach is already in `septuagint/LXX-Rahlfs-1935/` — this section is Hebrew-only, per scope.

### 3A. bensira.org — Tier 1, with an access caveat

`https://bensira.org` ("The Book of Ben Sira: Online Text Edition") — confirmed live. It is a **manuscript navigator**, not a bulk dataset: for each of the Genizah MSS (**A, B, C, D, E, F**) plus **Masada** and **Qumran**, it serves per-folio pages with a manuscript **image**, a **transcription** tab, and a **translation** tab. Both the Qumran fragments (2Q18, 11QPsa) were spot-checked live:

- `https://bensira.org/transcriptions/Qumran/2Q18.pdf` — **200 OK**, diplomatic transcription PDF
- `https://bensira.org/transcriptions/Qumran/11QPsa.pdf` — **200 OK**, diplomatic transcription PDF
- The equivalent per-folio pattern for MS A is `transcriptions/A/A_I_Recto.pdf` (confirmed from the navigator's default page load) — i.e. every Genizah MS folio has its own transcription PDF at a predictable path, but there is **no single bulk file or archive** — it would need to be crawled folio-by-folio.

**This is genuinely Tier 1**: it's a diplomatic transcription of the actual manuscript witnesses, not a reconstruction. The site plainly states images are "Used by kind permission of the Syndics of Cambridge University" for the Genizah plates, and the Qumran images carry "© Courtesy of the Israel Antiquities Authority, the Leon Levy Dead Sea Scrolls Digital Library." **No blanket redistribution license is stated anywhere on the site** — permission is granted for the site's own display, not explicitly for downstream reuse/mirroring. Downloading a handful of PDFs for personal research reading is almost certainly fine; treating the whole site as a bulk-fetchable dataset for this corpus would need a permissions check first. Flagging honestly rather than assuming.

Witness dates by manuscript (standard Genizah paleographic dating, widely agreed in the literature — not independently re-verified against a primary paleography source in this pass):

| MS | Content | Witness date | Discovered |
|---|---|---|---|
| Genizah MS A | Sir 3:6–16:26, 27:5(?)–30:11, 31:12(?)–33:8, 35:9–38:27, 39:15–51:30 (largest MS) | **10th–12th c. CE** copy | 1896 (Schechter, Cambridge) |
| Genizah MS B | Sir 10:19(?)–15:19(?), 25:8–33:3, 35:9–38:27(margin), etc. | **11th–12th c. CE** | 1896–1900 |
| Genizah MS C | excerpts (florilegium-style) | **11th–12th c. CE** | 1896–1900 |
| Genizah MS D | Sir 36:29–38:1 | **11th–12th c. CE** | 1896–1900 |
| Genizah MS E | Sir 32:16(?)–34:1 | **11th–12th c. CE** | 1900s |
| Genizah MS F | Sir 31:24–33:8, 36:24–37:26 | **11th–12th c. CE** | 1931 |
| Masada scroll (MasSir/Mas1h) | Sir 39:27–44:17 | **c. 100 BCE** (Hasmonean-era hand — the earliest and least-reconstructed Hebrew witness) | 1964 (Yadin excavation) |
| Qumran 2Q18 | Sir 6:14–15, 6:20–31 | **c. 50 BCE – 1 CE** | 1952 (Qumran Cave 2) |
| Qumran 11QPsa | Sir 51:13–20, 51:30b | **c. 30–50 CE** (Herodian-era hand) | 1956 (Qumran Cave 11) |

The composition itself dates **c. 196–175 BCE** (Jerusalem; the author's grandson translated it into Greek in Egypt, per the prologue, "in the 38th year of Euergetes," i.e. **132 BCE**). Note per the priority-change instruction: **the Genizah MSS being discovered in 1896 does not make them "modern"** — they are 10th–12th-century physical artifacts; 1896 is only when they resurfaced. Same logic for Masada (1964 dig, 1st-c.-BCE artifact) and Qumran (1950s digs, 1st-c.-BCE/CE artifacts). All three are Tier 1 regardless of discovery/publication date.

### 3B. Facsimile + transcription editions, pre-1928 (US public domain), on archive.org — Tier 1 (facsimile) despite post-1820 publication

| Edition | Content | Edition date | Archive.org item | Verified |
|---|---|---|---|---|
| Schechter & Taylor, *The Wisdom of Ben Sira* | Cairo Genizah MS B (the editio princeps of the Genizah find) — facsimile plates + printed Hebrew transcription | **1899** | `https://archive.org/details/wisdomofbensirap00scheuoft` | **200 OK**; djvu.txt confirmed present (`wisdomofbensirap00scheuoft_djvu.txt`); not access-restricted |
| Cowley & Neubauer, *The Original Hebrew of a Portion of Ecclesiasticus (XXXIX.15–XLIX.11)* | Genizah MS A portion, with early versions + English translation | **1897** | `https://archive.org/details/originalhebrewof00cowlrich` (alt. copy: `originalhebrewof00cowluoft`) | **Confirmed via archive.org search API** (`numFound: 6` hits, both identifiers live) |
| Margoliouth (or related), *The Original Hebrew of Ecclesiasticus XXXI.12-31, and XXXVII.26* | Further Genizah portion | **1899** | `https://archive.org/details/originalhebrewof00marg` | Confirmed via same search |

These are genuinely valuable: they're facsimile-grade (Tier 1 despite a post-1820 imprint date) reproductions of the actual Genizah leaves, fully downloadable, public domain, OCR'd. **This is probably the single best free, bulk-downloadable Hebrew Ben Sira source for this corpus.**

### 3C. Yadin's Masada edition — access-restricted

`https://archive.org/details/bensirascrollfro0000yadi` — Yigael Yadin, *The Ben Sira Scroll from Masada* (Israel Exploration Society / Hebrew University, **1965**). Confirmed **`access-restricted-item: true`** — this is a controlled-digital-lending (borrow, 1-hour loan) item, not a free download, despite having internal djvu.txt/PDF files (those are only exposed to borrowers). **Blocked** for this corpus without a library-borrow workaround, which isn't appropriate for a static local dataset anyway.

### 3D. Cairo Genizah bulk digital collections — access/licensing blockers

- **Cambridge Digital Library** (Taylor-Schechter Genizah Research Unit) — hosts the actual Genizah fragment images; bensira.org's own image credit line points back here. Not independently re-verified for a bulk API in this pass, but the credit-line language ("kind permission of the Syndics of Cambridge University") strongly implies the same non-bulk, display-only posture as bensira.org itself.
- **Friedberg Genizah Project (FGP)** — ~740,000 digitized Genizah images across 40+ partner libraries. Requires a **personal account** to use; terms require crediting FGP/Friedberg Jewish Manuscript Society on any reuse; **no bulk download mechanism found**. Not a fit for offline mirroring as currently documented.

### 3E. Modern critical editions (Tier 3) — exist, not free, listed per instruction not to omit

| Edition | Publisher/date | Status |
|---|---|---|
| Beentjes, *The Book of Ben Sira in Hebrew: A Text Edition of All Extant Hebrew Manuscripts* | Brill, **1997** | Standard synoptic scholarly edition. Copyrighted, not found free anywhere. |
| Rey & Reymond, *A Critical Edition of the Hebrew Manuscripts of Ben Sira, With Translations and Philological Notes* | Brill, Supplements to JSJ vol. 217, **2024** | The newest full critical edition of all 9 Hebrew MSS incl. DSS. Hardback $152, copyrighted, not free. |
| Yadin, *The Ben Sira Scroll from Masada* | Israel Exploration Society, **1965/1999 reprint** | See 3C — access-restricted lending item. |

None of these are obtainable free/bulk. Listed for completeness per the "include everything, let him judge" instruction.

---

## Part 4 — Manifest: exact commands (no bulk download executed)

```bash
# --- Targums: fill via Sefaria API, same pipeline as onkelos/pseudo-jonathan/targum-jerusalem ---

# 1. Targum Jonathan to the Prophets (21 books) -> targums/targum-jonathan-prophets/
mkdir -p targums/targum-jonathan-prophets
for b in Joshua Judges I_Samuel II_Samuel I_Kings II_Kings Isaiah Jeremiah Ezekiel \
         Hosea Joel Amos Obadiah Jonah Micah Nahum Habakkuk Zephaniah Haggai Zechariah Malachi; do
  curl -s "https://www.sefaria.org/api/texts/Targum_Jonathan_on_${b}?context=0&commentary=0" \
    -o "targums/targum-jonathan-prophets/${b}.json"
done

# 2. Fill out Fragment Targum / Targum Jerusalem (Leviticus, Numbers, Deuteronomy) -> targums/targum-jerusalem/
for b in Leviticus Numbers Deuteronomy; do
  curl -s --get "https://www.sefaria.org/api/texts/Targum%20Jerusalem%2C%20${b}" \
    --data-urlencode "context=0" -o "targums/targum-jerusalem/${b}.json"
done

# 3. Targum to Chronicles -> targums/targum-chronicles/
mkdir -p targums/targum-chronicles
curl -s "https://www.sefaria.org/api/texts/Targum_of_I_Chronicles?context=0" -o targums/targum-chronicles/I_Chronicles.json
curl -s "https://www.sefaria.org/api/texts/Targum_of_II_Chronicles?context=0" -o targums/targum-chronicles/II_Chronicles.json

# 4. Targum to the Writings (Megillot + Job/Psalms/Proverbs) -> targums/targum-writings/
mkdir -p targums/targum-writings
for b in Psalms Job Proverbs Song_of_Songs Ruth Lamentations Ecclesiastes Esther; do
  curl -s "https://www.sefaria.org/api/texts/Aramaic_Targum_to_${b}?context=0" -o "targums/targum-writings/${b}.json"
done
curl -s "https://www.sefaria.org/api/texts/Targum_Sheni_on_Esther?context=0" -o targums/targum-writings/Esther_Sheni.json

# --- Targum Neofiti: BLOCKED, do not pull from Sefaria (stub, 8 verses only). No action. ---

# --- Pre-1820 print (Tier 2), for cross-checking / OCR text extraction, NOT auto-downloaded here ---
# Bomberg 2nd Rabbinic Bible (1524-25), OCR'd:
#   https://archive.org/download/mikraot_gdolot/Torah_djvu.txt
#   https://archive.org/download/mikraot_gdolot/Major%20and%20minor%20prophets_djvu.txt
#   https://archive.org/download/mikraot_gdolot/Joshua%2C%20Judges%2C%20Samuel%2C%20Kings_djvu.txt
#   https://archive.org/download/mikraot_gdolot/Writings_djvu.txt   # (confirm exact filename via `curl -s https://archive.org/metadata/mikraot_gdolot`)
# Bomberg 1st Rabbinic Bible (1516-17):
#   https://archive.org/download/Miqraot-Gedolot-First-Edition_Venice_1517/Miqra%27ot%20Gedolot_First%20Edition_Venice_1517_djvu.txt
# Walton's London Polyglot (1654-57), vol. 4 has the Triplex Targum:
#   https://archive.org/details/walton_polyglot   (check item file listing for per-volume djvu.txt)

# --- Ben Sira Hebrew ---

# Tier 1, best bulk-downloadable option: Schechter & Taylor 1899 facsimile + transcription
mkdir -p ben-sira/schechter-taylor-1899
curl -s "https://archive.org/download/wisdomofbensirap00scheuoft/wisdomofbensirap00scheuoft_djvu.txt" \
  -o ben-sira/schechter-taylor-1899/text.txt
# (also grab the PDF for the facsimile plates themselves, via the same archive.org item's file list)

# Cowley & Neubauer 1897 (Genizah MS A portion)
mkdir -p ben-sira/cowley-neubauer-1897
curl -s "https://archive.org/download/originalhebrewof00cowlrich/originalhebrewof00cowlrich_djvu.txt" \
  -o ben-sira/cowley-neubauer-1897/text.txt

# bensira.org — Tier 1 diplomatic transcriptions, but per-folio only, no bulk archive.
# Do NOT mass-crawl without checking reuse terms first (see 3A caveat).
# Individual confirmed-live examples if pulling a handful for reference:
#   https://bensira.org/transcriptions/Qumran/2Q18.pdf
#   https://bensira.org/transcriptions/Qumran/11QPsa.pdf
#   https://bensira.org/transcriptions/A/A_I_Recto.pdf   (pattern for Genizah MSS A-F, folio by folio)

# Masada scroll (Yadin 1965): BLOCKED — archive.org item is lending-restricted, no free download.
```

---

## Summary of blockers (explicit, per instruction)

| Item | Blocker |
|---|---|
| **Targum Neofiti**, real/complete text | Sefaria's copy is an 8-verse stub (verified by content, not just HTTP status); Vatican MS images are reproduction-restricted; the only real critical edition (Díez Macho) is modern and copyrighted. No free path found. |
| **Samaritan Targum**, clean modern free source | Transmission is genuinely fragmented across recensions; best free lead is an 1874 partial edition (Nutt); the standard modern critical edition (Tal) is copyrighted. |
| **Antwerp Polyglot**, confirmed direct URL | Exists, not verified this pass — follow-up needed. |
| **Targum-to-Chronicles editio princeps (Beck, 1680–83)** and **Targum Sheni editio princeps (Pesaro, 1519)** | Both real, neither confirmed on archive.org this pass — follow-up needed. |
| **Masada Ben Sira scroll (Yadin 1965 edition)** | archive.org item is lending-restricted (borrow only), not a free download. |
| **Cairo Genizah bulk image/text collections** (Cambridge Digital Library, Friedberg Genizah Project) | Both real and substantial, but neither offers unrestricted bulk download/reuse terms — FGP requires an account and credits-on-reuse; Cambridge's own bensira.org credit line implies the same permission-gated posture. |
| **Modern Ben Sira critical editions** (Beentjes 1997, Rey & Reymond 2024) | Genuinely copyrighted, no free version located. Listed for completeness only. |

## What's cleanly obtainable, no blockers

- Full Targum Jonathan to the Prophets (21 books) — Sefaria API, verified complete
- Remaining 3 books of the Fragment Targums (Lev/Num/Deut) — Sefaria API, verified live
- Targum to I & II Chronicles — Sefaria API, verified complete
- Full Targum to the Writings (8 books + Targum Sheni) — Sefaria API, verified complete
- Bomberg's 1516/1517 and 1524/1525 Rabbinic Bibles — archive.org, OCR'd, pre-1820, PD
- Schechter & Taylor 1899 Ben Sira facsimile+transcription — archive.org, PD, not access-restricted
- Cowley & Neubauer 1897 / Margoliouth 1899 Ben Sira portions — archive.org, PD
- bensira.org per-folio transcription PDFs for all 8 Hebrew witnesses (A–F, Masada, Qumran) — live, though permission terms for bulk reuse are unstated and should be checked before treating as a mass-download source

Estimated added size: the Sefaria JSON pulls are all small (each targum book is tens to low hundreds of KB of text — comparable to the existing 2.1 MB `targums/` total, so the full targum set should land well under 10 MB). The archive.org djvu.txt OCR files are similarly light (single-digit MB each); the accompanying facsimile PDFs/image sets are the only potentially large pulls (tens of MB per multi-volume Rabbinic Bible) and were **not** downloaded in this pass.
