# Pre-1820 Greek Editions — NT & Septuagint Research

Researched 2026-08-08. Scope: printed editions of the Greek New Testament and Greek Old
Testament (Septuagint), verified against `INDEX.md` so nothing already on disk is
re-recommended (SBLGNT, Nestle 1904, UGNT, Byzantine Majority, Rahlfs LXX, Swete LXX
are already local and are NOT repeated below).

**The user's rule, restated:** edition date, not witness date, is what's being graded.
"Anything printed after 1820, assume it's inaccurate." Per a mid-task correction from the
user, this manifest does **NOT** filter anything out — every edition found, pre- or
post-1820, is listed below with a tier label. The user decides what to keep; the date is
the input to that decision, not a pre-applied filter.

**Every row below carries two distinct dates. Do not conflate them:**
- **Witness date** — the age of the manuscript(s) the printed text actually rests on.
- **Edition date** — the year the print run in question came off the press.

The single most important fact in this whole document is that for most of these
editions those two numbers are wildly far apart, and not in the direction people assume.
An old **edition** is not the same thing as an old **witness**.

---

## 0. The one fact that reframes everything else here

**Erasmus's 1516 *Novum Instrumentum* — the ancestor of every Textus Receptus edition
below (Stephanus, Beza, Elzevir, and by extension the KJV) — was set from a handful of
12th–13th century Byzantine minuscules he had on hand in Basel** (chiefly Minuscules 1,
2, 2814, 817, 2815 — none earlier than ~1100 CE), rushed to print in about six months to
beat the Complutensian Polyglot to market, and for Revelation he had only **one damaged
12th-century manuscript missing its last six verses, which he back-translated from the
Latin Vulgate into Greek himself** — those Erasmus-invented Greek readings are still in
the Textus Receptus today. So: the printed edition is "only" 510 years old, but the
witnesses under it are medieval, not ancient — centuries younger than Vaticanus,
Sinaiticus, or the papyri the modern eclectic text draws on. An old edition date does not
imply an old witness date. This cuts directly against the intuitive reading of the
user's rule and is worth having explicit going in.

The Complutensian Polyglot (1514/1522) rested on Vatican manuscripts Cardinal Cisneros
borrowed from Pope Leo X — somewhat better and independently sourced, but still medieval
minuscules, not the great uncials. **No pre-19th-century printed Greek NT used
Vaticanus, Sinaiticus, or Alexandrinus as its base text for the running text** — those
codices weren't fully collated/published until Woide (1786, Alexandrinus only, NT),
Bianchini/Birch's partial Vaticanus readings, and Tischendorf's own 1840s–60s
manuscript-hunting (Sinaiticus wasn't even discovered until 1844/1859). This is exactly
why Mill, Wettstein, Griesbach, Matthaei, Alter, and Birch matter so much despite being
"only" apparatus built on the same medieval base text: they're where the manuscript
tradition starts getting systematically compared and the base text starts being
corrected against something other than what Erasmus had in Basel.

For the Septuagint side the picture flips: the **Sixtine LXX (1587) is the first
edition based on Codex Vaticanus** (~300–325 CE) — a genuinely ancient witness, unlike
the NT case above. Grabe's LXX (1707–20) does the same for Codex Alexandrinus
(~400–440 CE). So on the OT/LXX side, "old edition" and "old, good witness" actually do
align — worth knowing that the two halves of this project have opposite risk profiles.

---

## 1. Greek New Testament

### 1.1 Complutensian Polyglot — the first printed Greek NT

| | |
|---|---|
| Witness date | Medieval Vatican minuscules lent to Cisneros by Leo X; exact MSS never conclusively identified, believed 11th–15th c. |
| Edition date | Printed 1514 (colophon), publication held until papal approval, 1522 |
| Editor | Cardinal Francisco Jiménez de Cisneros, with Antonio de Nebrija, Diego López de Zúñiga et al., Alcalá de Henares |
| Tier | **1 — highest value** |

Six folio volumes: vols 1–4 = Hebrew/Aramaic/Greek/Latin OT (contains the **Complutensian
LXX**, see §2.1), vol 5 = Greek/Latin NT, vol 6 = Hebrew-Aramaic dictionary and grammar.

| Archive.org item | Content | Size | OCR (`_djvu.txt`) | Verified |
|---|---|---|---|---|
| [`complutensianpolyglot`](https://archive.org/details/complutensianpolyglot) | All 6 vols, HD scan, per-volume PDFs | 8.1 GB total; single vol PDFs range ~60–500 MB (e.g. `Volume 6/31Imgenes197a296.pdf` = 62 MB) | Yes | HTTP 200 confirmed on a vol-6 PDF |
| [`GRCNA28_DBS_HS`](https://archive.org/details/GRCNA28_DBS_HS) | Vol 5 only (Greek NT + Latin) | 8.2 GB item; single PDF `Greek-(1517)-Complutensian-Polyglot-Bible-(Latin-Hebrew).pdf` = 513 MB | Yes | HTTP 200 confirmed |
| [`complutensian_polyglot_bible`](https://archive.org/details/complutensian_polyglot_bible) | Full set, LoC/World Digital Library source, multiple resolution options incl. a 1.15 GB "smallest legible" text PDF and a 5.1 GB full-res PDF | 139.5 GB total collection (many redundant resolution tiers — **do not download the whole item**) | Yes | 200 (metadata only checked) |
| [`polyglotcomplutensis`](https://archive.org/details/polyglotcomplutensis) | Full set, alt. scan | 14.9 GB | Yes | not HEAD-checked (redundant with above) |
| [`ComplutensianPolyglotBibleOldTestamentNewTestament`](https://archive.org/details/ComplutensianPolyglotBibleOldTestamentNewTestament) | Full set, alt. scan | 14.3 GB | Yes | not HEAD-checked (redundant) |

OCR of 1514 Greek type is poor as expected — hand-corrected transcription doesn't exist
freely for this edition. **Recommendation: use `GRCNA28_DBS_HS`'s single PDF (513 MB)
for the NT, and pull individual volume PDFs from `complutensianpolyglot` for the LXX
volumes rather than downloading any full item.**

### 1.2 Erasmus, *Novum Instrumentum omne* / *Novum Testamentum* — all 5 editions found

| Ed. | Witness date | Edition date | Archive.org ID | Size (single PDF) | OCR | Verified |
|---|---|---|---|---|---|---|
| 1st | ~12th–13th c. Basel minuscules (Min. 1, 2, 2814, 817, 2815); Rev. 22:16–21 back-translated by Erasmus from the Vulgate | 1516, Basel (Froben) | [`nouuminstrument00eras`](https://archive.org/details/nouuminstrument00eras) | 82.3 MB | Yes | **200 confirmed** |
| 1st (2nd copy) | same | 1516 | [`novum-instrumentum-omne-diligenter-ab-erasmo-roterodamo-greek-latin-1516`](https://archive.org/details/novum-instrumentum-omne-diligenter-ab-erasmo-roterodamo-greek-latin-1516) | 697 MB total | Yes | not HEAD-checked (redundant) |
| 2nd | same base + light revision | 1519, Basel | [`novvm-testamentvm-omne-mvlto-quam-antehac-diligentius-ab-erasmo-roterodamo-1519`](https://archive.org/details/novvm-testamentvm-omne-mvlto-quam-antehac-diligentius-ab-erasmo-roterodamo-1519) | 913 MB total | Yes | not HEAD-checked |
| 3rd | same base; Comma Johanneum added under pressure | 1522, Basel | [`roterodamvs-erasmus-novum-testamentum-1522`](https://archive.org/details/roterodamvs-erasmus-novum-testamentum-1522) | 61.2 MB | Yes | **200 confirmed** |
| 4th | same base + Complutensian collation in margin | 1527, Basel | [`NovumTestamentumIuxtaGraecorumLectionemExEmendatioribusExemplaribusVet`](https://archive.org/details/NovumTestamentumIuxtaGraecorumLectionemExEmendatioribusExemplaribusVet) | 262 MB (text vol) | Yes | not HEAD-checked |
| 5th | same base, final revision | 1535, Basel | [`ARes162051`](https://archive.org/details/ARes162051) (text) + [`ARes162052`](https://archive.org/details/ARes162052) (Erasmus's own annotations, separate vol) | 82.1 MB / 126.3 MB | Yes | **both 200 confirmed** |

Tier 1 for all five — this is the direct textual ancestor of Stephanus/Beza/Elzevir/KJV
and the single most historically important item in this list precisely because of §0
above.

### 1.3 Stephanus (Robert Estienne)

| | |
|---|---|
| Witness date | Erasmus's medieval base + Complutensian collation + 15 additional MSS collated by Estienne's son Henri, incl. Codex Bezae and Codex Regius (both still only medieval/9th–6th c. at best) |
| Edition dates | 1546, 1549, 1550 ("Editio Regia"), 1551 (Geneva — introduced verse numbers) |

I could **not** locate a scan of the original 1546, 1549, or 1551 print run as a
standalone archive.org item — only the 1550 "Editio Regia" is represented, and even that
is not a straightforward period scan; see caveat below.

| Archive.org item | What it actually is | Size | OCR | Verified |
|---|---|---|---|---|
| [`1550-stephanus-textus-receptus`](https://archive.org/details/1550-stephanus-textus-receptus) | Scanned print claiming to be the 1550 text directly | 863 MB total, single PDF 51.7 MB | Yes | **200 confirmed** |
| [`1550TheGreekNewTestamentStephanus`](https://archive.org/details/1550TheGreekNewTestamentStephanus) | Same text, alt. upload | 279 MB | Yes | not HEAD-checked |
| [`textusreceptusstephanus1550`](https://archive.org/details/textusreceptusstephanus1550) | 1550 text **with 7,456 added textual notes** — a modern collation aid layered on the old text | 301 MB | Yes | not HEAD-checked |
| [`1550-scrivener-1860`](https://archive.org/details/1550-scrivener-1860) | **Not the original** — this is F.H.A. Scrivener's **1860** hand-set typographic reprint of the 1550 text (Cambridge). A 19th-c. edition reproducing a 16th-c. text. | 570 MB | Yes | not HEAD-checked |

**Caveat, stated plainly:** none of these are confirmed period (1546–1551) print scans
with clear provenance — they read as modern reprint houses' re-typesettings of the 1550
text uploaded to archive.org without strong metadata on what print run was
photographed. Treat the *text* as authentically Stephanus 1550 (it is the most
well-attested TR base text there is), but do not treat any of these PDFs as a facsimile
of a physical 1550 book the way the Erasmus/Complutensian items above are. If a true
period facsimile matters, check e-rara.ch, MDZ (digitale-sammlungen.de), or the Bodleian
next — I did not find one in the time available. Tier 2 pending that check.

**Machine-readable text:** [`byztxt/greektext-textus-receptus`](https://github.com/byztxt/greektext-textus-receptus)
(GitHub, public domain, "copy freely") and [`byztxt/greektext-scrivener`](https://github.com/byztxt/greektext-scrivener)
carry Unicode Greek text with morphology/Strong's tags for this tradition — this is the
"modern transcription of a pre-1820 edition" case the brief asked about. License: public
domain per repo README.

### 1.4 Beza, Théodore — multiple editions, 1565–1604

| Witness date | Edition date | Archive.org ID | Size | OCR | Verified |
|---|---|---|---|---|---|
| Same medieval base + Beza's own collation of Codex Bezae (D, ~5th c. — Beza owned it) and Codex Claromontanus | 1565, Geneva | [`jesu-christi-iesv-christi-d.-n.-novum-testamentum-sive-novum-foedus-cuius-graeco-theodori-bezae-1565`](https://archive.org/details/jesu-christi-iesv-christi-d.-n.-novum-testamentum-sive-novum-foedus-cuius-graeco-theodori-bezae-1565) | 1.45 GB | Yes | not HEAD-checked |
| same | 1565 (2nd copy) | [`novum-testamentum-sive-foedus-jesu-christi-d.-n.-graece-et-latine-theodoro-beza-interprete-1565`](https://archive.org/details/novum-testamentum-sive-foedus-jesu-christi-d.-n.-graece-et-latine-theodoro-beza-interprete-1565) | 624 MB | Yes | not HEAD-checked |
| same | 1598 (5th/final ed., the one the KJV translators used most) | [`jesu-christi-domini-nostri-novum-testamentum-sive-novum-foedus-cujus-graeco-theodori-bezae-1598`](https://archive.org/details/jesu-christi-domini-nostri-novum-testamentum-sive-novum-foedus-cujus-graeco-theodori-bezae-1598) | 1.56 GB | Yes | not HEAD-checked |

Note: Beza's Codex Bezae is the one witness in this whole NT section old enough to
matter on its own (5th c.) — but Beza's *printed text* mostly did not follow D where it
diverged from the Erasmian tradition; he cited it in his notes more than he adopted its
readings. Tier 1 for historical value, Tier 2 for actually shifting the base text.

### 1.5 Elzevir, 1624 and 1633 — the Textus Receptus proper

| Witness date | Edition date | Archive.org ID | Size | OCR | Verified |
|---|---|---|---|---|---|
| Beza's 1565/1598 base, essentially unchanged | 1633, Leiden (2nd ed. — preface coined "Textum ... nunc ab omnibus receptum," the origin of the name "Textus Receptus") | [`ned-kbn-all-00002699-001`](https://archive.org/details/ned-kbn-all-00002699-001) | 901 MB total, single PDF 191 MB | Yes | **200 confirmed** |

I could not locate a distinct 1624 (1st ed.) scan on archive.org — the 1633 is the
famous one (the "Textus Receptus" name comes specifically from its preface) and is
confirmed above. If the 1624 specifically matters, check e-rara.ch next.

**Machine-readable text:** [`byztxt/greektext-elzevir`](https://github.com/byztxt/greektext-elzevir)
— Elzevir TR text with morphology + Strong's numbers, public domain, maintained by Dr.
Maurice Robinson / Dr. Ulrik Sandborg-Petersen. This directly answers the brief's
question about a modern transcription of a pre-1820 edition: it exists, and it's public
domain.

Tier 1.

### 1.6 Walton's London Polyglot (1657) — NT volume

| | |
|---|---|
| Witness date | Same TR-family medieval base for the Greek column, alongside Hebrew, Samaritan, Aramaic, Syriac, Arabic, Ethiopic, Persian, Latin, Greek LXX columns |
| Edition date | 1657 (vol containing Gospels–Revelation was the last of 6 folios issued, all 1654–57) |
| Editor | Brian Walton, London |
| Tier | 2 — valuable as the first NT printed alongside that many independent-language witnesses side by side, but the Greek text itself doesn't advance beyond Stephanus/Beza |

| Archive.org item | Size | OCR | Verified |
|---|---|---|---|
| [`Walton-Polyglot`](https://archive.org/details/Walton-Polyglot) ("Merge Copy," Persian-text-focused upload) | 578 MB | Yes | not HEAD-checked |
| [`WaltPoly1PrologVariantReadings`](https://archive.org/details/WaltPoly1PrologVariantReadings) — the real find: a **multi-volume merged item**, each volume as its own file set. The Greek NT (John–Revelation) volume is `WaltPoly10_John-Rev.pdf` | 16.2 GB total item; single-volume PDF `WaltPoly10_John-Rev.pdf` = 109 MB | Yes | **200 confirmed** |

**Recommendation: pull `WaltPoly10_John-Rev.pdf` (109 MB) alone, not the full 16.2 GB item.**

### 1.7 John Mill, *Novum Testamentum Graecum* (Oxford, 1707) — landmark 30,000-variant apparatus

| Witness date | Edition date |
|---|---|
| Same medieval TR base text (Mill did not change the running text — his innovation was the apparatus) + collations from ~100 additional MSS and versions | 1707, Oxford |

**I could not confirm a scan of Mill's actual first edition (Oxford, 1707) on
archive.org.** What I found instead are later reprints/derivatives that carry Mill's
name but are not his original apparatus:

| Archive.org item | What it is | Edition date | Size | Verified |
|---|---|---|---|---|
| [`novumtestamentu00baskgoog`](https://archive.org/details/novumtestamentu00baskgoog) | Baskerville's edition "juxta exemplar Millianum" — follows Mill's base *text*, not his apparatus | 1763, Cambridge | 180 MB | not HEAD-checked |
| [`novumtestamentum00mill`](https://archive.org/details/novumtestamentum00mill) | Titled under Mill's name; American reprint | 1813 | 829 MB | not HEAD-checked |
| [`hekainediatheken00mill`](https://archive.org/details/hekainediatheken00mill) | Explicitly "Mill's translation edited by Caleb Alexander," 2nd ed. (1st ed. 1800), Massachusetts Bible Society — **not Mill's critical apparatus, just his base text in an American devotional reprint** | 1814 | 738 MB | not HEAD-checked |

**Honest bottom line: the 30,000-variant Mill apparatus itself does not appear to be
freely scanned and hosted anywhere I could verify in the time available.** HathiTrust
has a catalog record (https://catalog.hathitrust.org/Record/012314445) but catalog
access ≠ confirmed full-view/downloadable status, and I did not verify page-level access
— do not assume it's open without checking HathiTrust's own reader. Next places to check:
Bodleian digital collections (Mill was Oxford's own edition), Google Books directly, or
PRDL (prdl.org, lists 10 free Mill titles per their author page but I did not verify each
link resolves). Tier 1 by importance, Tier 3 by confirmed availability — flagging
honestly rather than guessing a URL.

### 1.8 Wettstein, *Novum Testamentum Graecum* (Amsterdam, 1751–52, 2 vols)

| Witness date | Edition date |
|---|---|
| Medieval TR base text; apparatus introduces the manuscript sigla (uncial letters, minuscule numbers) still used in NA28/UBS5 today | 1751–52, Amsterdam |

| Archive.org item | Size | OCR | Verified |
|---|---|---|---|
| [`hekainediatheken00clem`](https://archive.org/details/hekainediatheken00clem) | 1.84 GB total, single PDF 112 MB | Yes | **200 confirmed** |

Tier 1 — this is the edition that gave the field its manuscript-naming convention;
extremely high value despite the base text being unchanged.

### 1.9 Bengel, *Novum Testamentum Graecum* (Tübingen, 1734)

| Witness date | Edition date |
|---|---|
| Medieval TR base; Bengel introduced the first systematic genealogical grouping of MSS into families (the ancestor of the modern stemma method) | 1734, Tübingen |

| Archive.org item | Size | OCR | Verified |
|---|---|---|---|
| [`bub_gb_ardIAAAAcAAJ`](https://archive.org/details/bub_gb_ardIAAAAcAAJ) | 1.20 GB (Google Books scan mirrored to IA; no single top-level PDF found in the file list — access via the IA reader or Google Books directly) | Yes | metadata 200, no direct PDF filename found |
| [`dioalbertibengel00beng`](https://archive.org/details/dioalbertibengel00beng), *Apparatus criticus ad Novum Testamentum* | Bengel's separately-published critical apparatus, 1763 reissue | 1.20 GB | Yes | not HEAD-checked |

Tier 1.

### 1.10 Griesbach, *Novum Testamentum Graece* (1775–1807)

Griesbach's is the first edition to seriously depart from the TR toward what would
become the modern eclectic text, grouping witnesses into "recensions" (Alexandrian,
Western, Byzantine) — a direct ancestor of the SBLGNT/NA lineage already on this user's
disk, but itself pre-1820.

| Witness date | Edition date | Archive.org ID | Size | OCR | Verified |
|---|---|---|---|---|---|
| Broadened beyond TR base — first edition to weigh Codex Alexandrinus / Vaticanus readings pulled from Woide's & other collations, though the physical uncials themselves are still not the base text | 1st ed., 1775–77, Halle — **not located on archive.org**, see gap below | — | — | — | not found |
| same, expanded | 2nd ed., vol 1 (Gospels) 1796, Halle | [`bim_eighteenth-century_novum-testamentum-graece_1796_1`](https://archive.org/details/bim_eighteenth-century_novum-testamentum-graece_1796_1) | 2.58 GB, single PDF 442 MB | Yes | **200 confirmed** |
| same | 2nd ed., vol 2 (Acts–Rev) 1806 | [`bim_eighteenth-century_novum-testamentum-graece_1806_2`](https://archive.org/details/bim_eighteenth-century_novum-testamentum-graece_1806_2) | 2.72 GB | Yes | not HEAD-checked |
| same | reprint/derivative, 1809 | [`hekainediatheken00grie`](https://archive.org/details/hekainediatheken00grie) | 1.27 GB | Yes | not HEAD-checked |
| same | reprint/derivative, 1818 | [`novumtestamentum01grie`](https://archive.org/details/novumtestamentum01grie) (vol 1) + [`novumtestamentum02grie`](https://archive.org/details/novumtestamentum02grie) (vol 2) | 986 MB + 985 MB | Yes | not HEAD-checked |
| same, later reprint edited by Schott | 1836 — **post-1820, included per instruction** | [`hekainediatheken00grie_0`](https://archive.org/details/hekainediatheken00grie_0) | 1.06 GB | Yes | not HEAD-checked |

I searched specifically for the true 1775–77 first Halle edition and did not find it on
archive.org; the 1796–1806 second edition (Griesbach's own most-cited edition, the one
Bible societies and later scholars actually used) is confirmed present and downloadable.
Tier 1.

### 1.11 Matthaei, *Novum Testamentum Graece* (Riga/Moscow, 1782–88)

Matthaei collated Moscow-held Byzantine manuscripts unavailable to Western European
editors — genuinely new witness data, independent of the Erasmus/Complutensian lineage
in its sourcing even though textually still Byzantine.

| Witness date | Edition date | Archive.org ID | Size | OCR | Verified |
|---|---|---|---|---|---|
| Byzantine/Moscow-held minuscules, ages not independently re-verified here | 1803 reissue "ad codices Mosquenses" (the 1782–88 original's re-collation) | [`novumtestamentu01mattgoog`](https://archive.org/details/novumtestamentu01mattgoog) | 143 MB, single PDF 21.8 MB | Yes | **200 confirmed** |
| same | 1803 (2nd copy) | [`bub_gb_CGUUAAAAQAAJ`](https://archive.org/details/bub_gb_CGUUAAAAQAAJ) | 869 MB | Yes | not HEAD-checked |

I did not find the original 1782–88 print run itself as distinct from this 1803
re-collation — flagging honestly. Tier 1 for the underlying witness value, Tier 2 for
edition-date precision (what's confirmed downloadable is the 1803 revision, not the
1782–88 original).

### 1.12 Alter, *Novum Testamentum Graece* (Vienna, 1786–87)

Franz Karl Alter used only the Greek manuscripts held in Vienna's Imperial Library —
another independent, narrowly-sourced witness pool.

**I could not confirm a working archive.org (or other free) full-scan link for this
edition in the time available.** Google Books lists at least volume 1 (1787) as
digitized per secondary sources, but I did not get a resolvable direct URL. Tier 3
pending further search — do not treat as obtained. Next step: search Google Books
directly (books.google.com) for "Alter Novum Testamentum Graecum Vindobonensem 1786,"
or check ÖNB (Austrian National Library) digital collections, since this is a
Vienna-published, Vienna-sourced edition.

### 1.13 Birch, *Quatuor Evangelia Graece* (Copenhagen, 1788) + *Variae Lectiones* (1798–1801)

Birch collated the Vatican-held manuscripts (including readings from Codex Vaticanus
itself, decades before Sixtine's full LXX use of it was echoed on the NT side) — a
genuinely valuable independent collation.

**Same finding as Alter: no confirmed free full-scan link located in the time
available.** WorldCat and an auction-house catalog entry confirm the physical edition's
existence and title (*Quatuor Evangelia Graece cum variantibus a textu lectionibus Codd.
MSS. Bibliothecae Vaticanae*, Havniae 1788) but neither is a digitized-text source. Tier
3 pending further search — check Det Kongelige Bibliotek (Danish Royal Library, Birch's
home institution) digital collections next.

### 1.14 Woide, facsimile of Codex Alexandrinus NT (London, 1786)

| Witness date | Edition date |
|---|---|
| **Codex Alexandrinus, ~400–440 CE** — the oldest witness anywhere in this NT section by a margin of 700+ years | 1786, London (typographic quasi-facsimile — cast type imitating the uncial hand, not a photographic facsimile; photographic facsimile technology didn't exist yet) |

**The true 1786 original was not located as a free scan.** What IS confirmed and
downloadable is Bishop Cowper's 1860 reprint of Woide's text:

| Archive.org item | What it is | Size | OCR | Verified |
|---|---|---|---|---|
| [`hkaindiathknovum00woid`](https://archive.org/details/hkaindiathknovum00woid) | Cowper's 1860 reprint of Woide's 1786 text | 978 MB, single PDF 47.5 MB | Yes | **200 confirmed** |
| [`codexalexandrinu00woid`](https://archive.org/details/codexalexandrinu00woid) | same, alt. scan | 1.02 GB | Yes | not HEAD-checked |
| [`codex-alexandrinus`](https://archive.org/details/codex-alexandrinus) | **A different, later thing** — E. Maunde Thompson's 1879–1883/1909 full photographic facsimile for the British Museum. Higher image fidelity to the actual manuscript than Woide, but a 19th/20th-c. edition, and post-1820. Included per instruction. | 5.93 GB | Yes | not HEAD-checked |

Tier 1 for witness importance (oldest source in this section), Tier 2 for edition
precision (the 1786 original itself isn't confirmed obtained — what's confirmed is an
1860 reprint of its text, plus the later 1883 photographic facsimile as a post-1820
alternative).

### 1.15 Kipling, Codex Bezae facsimile (Cambridge, 1793)

| Witness date | Edition date |
|---|---|
| Codex Bezae, ~5th c. (the same MS Beza himself used, §1.4) | 1793, Cambridge, 2 folio volumes |

**Not located as a free scan.** WorldCat confirms the physical edition's existence and
full title (*Codex Theodori Bezae Cantabrigiensis... Thomas Kipling*). What I did find
instead is a completely different, later, unrelated work with a similar-sounding title —
[`bezaecodexcanta00cambgoog`](https://archive.org/details/bezaecodexcanta00cambgoog),
F.H.A. Scrivener's *Bezae Codex Cantabrigiensis* — a critical **transcription** (not
facsimile) published in **1864**, post-1820. That item is a legitimate, valuable,
freely-downloadable resource in its own right (full transcription with critical notes)
but it is not Kipling 1793 and should not be substituted for it without flagging the
substitution, which this note now does. Tier 3 for Kipling specifically (not obtained);
noting the Scrivener 1864 alternative as Tier 2/post-1820 if the user wants a Bezae
transcription regardless of date.

| Archive.org item | What it is | Size | OCR | Verified |
|---|---|---|---|---|
| [`bezaecodexcanta00cambgoog`](https://archive.org/details/bezaecodexcanta00cambgoog) | Scrivener 1864 transcription (NOT Kipling 1793) | not checked | djvu.txt exists per earlier `_djvu.txt` full-text hit | not HEAD-checked |

### 1.16 Post-1820 NT critical editions encountered during this search (included per instruction)

None of these were part of the original pre-1820 assignment, but they turned up during
research and the user wants everything listed, dated, and left for him to judge.

| Edition | Witness date basis | Edition date | Archive.org ID | Size | Verified |
|---|---|---|---|---|---|
| Tregelles, *The Greek New Testament* | First edition to systematically prioritize the oldest uncials (Vaticanus, Alexandrinus, etc.) over the Byzantine mass — a real break from the TR tradition | 1857–1879 (issued in parts) | [`greeknewtestamen01treg`](https://archive.org/details/greeknewtestamen01treg) | 385 MB | **200 confirmed** |
| Tischendorf, *Novum Testamentum Graece*, editio octava critica maior (8th ed.) | Incorporates Tischendorf's own discovery/collation of Codex Sinaiticus (1844/1859) — the fullest pre-20th-c. apparatus | Vol 1 (Gospels) 1869; Vol 2 (Acts–Rev) 1872 | [`tischendorf-ntg-vol.-1-gospels-8th-ed.-critica-maior-1869`](https://archive.org/details/tischendorf-ntg-vol.-1-gospels-8th-ed.-critica-maior-1869) / [`tischendorf-ntg-vol.-2-acts-to-apoc.-8th-ed.-critica-maior-1872`](https://archive.org/details/tischendorf-ntg-vol.-2-acts-to-apoc.-8th-ed.-critica-maior-1872) | 1.54 GB / 1.45 GB | **200 confirmed (vol 1)** |
| Scrivener, *Bezae Codex Cantabrigiensis* (transcription) | Codex Bezae, 5th c. | 1864 | [`bezaecodexcanta00cambgoog`](https://archive.org/details/bezaecodexcanta00cambgoog) | n/a | not HEAD-checked |
| "Mill's translation," ed. Caleb Alexander, Massachusetts Bible Society | Mill's base text only, not his apparatus | 2nd ed. 1814 (1st ed. 1800) — technically pre-1820 by a hair; listed here because it's NOT actually Mill's critical work despite the name, see §1.7 | [`hekainediatheken00mill`](https://archive.org/details/hekainediatheken00mill) | 738 MB | not HEAD-checked |

---

## 2. Septuagint (Greek Old Testament)

### 2.1 Complutensian LXX (1514–17)

Bundled inside the Complutensian Polyglot's OT volumes — see §1.1 above for identifiers
and sizes; the LXX text runs in the Greek column of vols 1–4 (`complutensianpolyglot`
item, "Volume 1" through "Volume 4" folders). No standalone LXX-only Complutensian scan
was found — pull individual volume PDFs from that item rather than the NT-focused
`GRCNA28_DBS_HS`. Tier 1.

### 2.2 Aldine LXX (Venice, 1518)

| | |
|---|---|
| Witness date | First complete Greek Bible ever printed; text drawn largely from the Complutensian OT + various Venetian MSS, editor Andreas Asolanus (Aldus's son-in-law; Aldus himself died 1515, before publication) |
| Edition date | 1518, Venice, Aldine Press |

**Not located as a free full scan.** The only digitized Aldine-1518 material I could
confirm is a **single leaf**, not the book: Loyola Marymount University Digital
Collections, "Aldine Greek Bible, 1518"
(https://digitalcollections.lmu.edu/Documents/Detail/aldine-greek-bible-1518/12256,
CC BY 4.0) — one leaf from a broken/dispersed copy, not usable as corpus text. Tier 3,
not obtained. Next step: check Google Books directly, HathiTrust, or e-rara.ch — I did
not get a resolvable hit on any of those in the time available and am not going to guess
a URL.

### 2.3 Sixtine LXX (Rome, 1587) — Codex Vaticanus-based

| | |
|---|---|
| Witness date | **Codex Vaticanus, ~300–325 CE** — this is the edition that made Vaticanus the standard LXX base text for the next 300+ years |
| Edition date | 1587, Rome, commissioned by Pope Sixtus V, directed by Antonio Carafa |
| Tier | **1 — highest value on the LXX side** |

| Archive.org item | Size | OCR | Verified |
|---|---|---|---|
| [`LATSEPT_DBS_HS`](https://archive.org/details/LATSEPT_DBS_HS) | 2.97 GB total, single PDF 138 MB | Yes | **200 confirmed** |

**Caveat on this one:** the archive.org title field mislabels it "Latin (1587)
Septuigant" — the description text confirms it's the Sixtine/Roman Septuagint (a Greek
text edition, per the description and the "_DBS_HS" upload series which mirrors the
Complutensian NT item above the same way), but I did not open the PDF itself to confirm
page-by-page that the running text is Greek rather than an accompanying Latin
crib. Recommend a quick visual spot-check of the first few pages before treating this as
settled — flagging rather than asserting.

### 2.4 Grabe LXX (Oxford, 1707–20) — Codex Alexandrinus-based

| | |
|---|---|
| Witness date | **Codex Alexandrinus, ~400–440 CE** |
| Edition date | Tomus I published 1707; the full 4-tomus set completed by others after Grabe's 1711 death, finishing 1720 |
| Tier | 1 |

| Archive.org item | Vol / printing | Size | OCR | Verified |
|---|---|---|---|---|
| [`bim_eighteenth-century_septuaginta-interpretum-_grabe-joannes-ernestus_1707_1`](https://archive.org/details/bim_eighteenth-century_septuaginta-interpretum-_grabe-joannes-ernestus_1707_1) | Tomus I, 1707 | 3.03 GB, single PDF 498 MB | Yes | **200 confirmed** |
| [`31383040993688`](https://archive.org/details/31383040993688) | Tomus I–ultimus, 1707 (alt. catalog copy) | 2.55 GB | Yes | not HEAD-checked |
| `bim_eighteenth-century_septuaginta-interpretum-_grabe-joannes-ernestus_1719_2` | Tomus, 1719 | not sized | Yes | not HEAD-checked |
| `bim_eighteenth-century_septuaginta-interpretum-_grabe-joannes-ernestus_1719_4` | Tomus, 1719 | not sized | Yes | not HEAD-checked |
| `bim_eighteenth-century_septuaginta-interpretum-_grabe-joannes-ernestus_1720_3` | Tomus, 1720 | not sized | Yes | not HEAD-checked |
| Several `bub_gb_*` Google Books mirrors dated 1730–1732 | Later reissue/printing (possibly the Francis Lee-continued reissue) — not independently confirmed which specific reprint | ~1–2 GB each | Yes | not HEAD-checked |

Only Tomus I was HEAD-verified; the 1719/1720 volume identifiers were confirmed to
exist via search but not individually HEAD-checked for this report — do that before
relying on them.

### 2.5 Montfaucon, *Hexaplorum Origenis quae supersunt* (Paris, 1713)

Explicitly flagged in the brief as worth checking since Field's Hexapla (1875) is
post-1820 — **confirmed present and pre-1820**.

| | |
|---|---|
| Witness date | Reconstructs Origen's 3rd-c. Hexapla from patristic citations and marginalia — not a single manuscript witness but a compilation project |
| Edition date | 1713, Paris |
| Editor | Bernard de Montfaucon |
| Tier | 1 |

| Archive.org item | Size | OCR | Verified |
|---|---|---|---|
| [`A208086`](https://archive.org/details/A208086) | 4.42 GB total, single PDF 138 MB | Yes | **200 confirmed** |
| `bub_gb_cGDnzs0uq2YC`, `bub_gb_F7Ktk8CpF7MC`, `bub_gb_CDJdzwgNdnwC`, `bub_gb_W3OuvnBdplIC` | alt. Google Books mirrors, same 1713 edition | not sized | Yes | not HEAD-checked |

### 2.6 Holmes & Parsons, *Vetus Testamentum Graecum cum variis lectionibus* (Oxford, 1798–1827)

The largest LXX apparatus ever assembled — explicitly called out in the brief as very
high value. **Volumes 1 and 2 are pre-1820; volumes 3, 4&5 are post-1820 and are
included per instruction, same set, same importance.**

| Vol | Witness date basis | Edition date | Archive.org ID | Size | OCR | Verified |
|---|---|---|---|---|---|---|
| 1 (Pentateuch) | Collation of ~300 MSS and versions | **1798** | [`1798-oxford-septuagint-edited-by-holmes-and-parsons-volume-1`](https://archive.org/details/1798-oxford-septuagint-edited-by-holmes-and-parsons-volume-1) | 3.46 GB, single PDF 145 MB | Yes | **200 confirmed** |
| 2 | same | **1818** | [`1818-oxford-septuagint-edited-by-holmes-and-parsons-volume-2`](https://archive.org/details/1818-oxford-septuagint-edited-by-holmes-and-parsons-volume-2) | 4.21 GB, single PDF 156 MB | Yes | **200 confirmed** |
| 3 | same | 1823 — post-1820 | [`1823-oxford-septuagint-edited-by-holmes-and-parsons-volume-3`](https://archive.org/details/1823-oxford-septuagint-edited-by-holmes-and-parsons-volume-3) | 2.02 GB | Yes | not HEAD-checked |
| 4 & 5 (combined) | same | 1827 — post-1820 | [`1827-oxford-septuagint-edited-by-holmes-and-parsons-volume-4-5`](https://archive.org/details/1827-oxford-septuagint-edited-by-holmes-and-parsons-volume-4-5) | 4.10 GB | Yes | not HEAD-checked |
| Full set, alt. scan | all vols | 1798–1823 | [`VetusTestamentumGraecumCumVariisLecVol101Genesis`](https://archive.org/details/VetusTestamentumGraecumCumVariisLecVol101Genesis) | 13.7 GB, 564 files (this is a heavily split multi-part scan — do not bulk-pull) | Yes | metadata 200 only |

Tier 1, all five volumes — the brief is right that this is the single highest-value LXX
apparatus item on the list, and per the user's standing instruction it's listed complete
including the post-1820 volumes.

### 2.7 Field's Hexapla (Oxford, 1875) — post-1820, included per instruction

| | |
|---|---|
| Witness date | Same Hexapla-reconstruction project as Montfaucon 1713 above, redone with a century and a half more patristic/MS evidence |
| Edition date | 1875, Oxford (Clarendon) |
| Editor | Frederick Field |
| Tier | **3 — flagged explicitly by the brief as post-1820; the modern standard reference for Hexaplaric fragments, but outside the pre-1820 scope this project is otherwise built on** |

| Archive.org item | Vol | Size | OCR | Verified |
|---|---|---|---|---|
| [`origenis-hexaplorum-t.-1-1875`](https://archive.org/details/origenis-hexaplorum-t.-1-1875) | T.1: Prolegomena, Genesis–Esther | 797 MB, single PDF 115 MB | Yes | **200 confirmed** |
| [`origenis-hexaplorum-t.-2-1875`](https://archive.org/details/origenis-hexaplorum-t.-2-1875) | T.2: Job–Malachi + Auctarium/indices | 1.11 GB | Yes | not HEAD-checked |
| [`origenishexaplor02origuoft`](https://archive.org/details/origenishexaplor02origuoft) | alt. scan (very large — appears to bundle extra material) | 19.8 GB | Yes | not HEAD-checked |

---

## 3. Not located — honest gaps

| Item | Status | Suggested next step |
|---|---|---|
| Mill's actual 1707 critical apparatus (not just "juxta exemplar Millianum" reprints of his base text) | Not confirmed free/downloadable | HathiTrust record exists (catalog.hathitrust.org/Record/012314445) but full-view access not verified; try Bodleian, Google Books directly, or PRDL (prdl.org) |
| Aldine LXX (Venice 1518), full book | Only a single detached leaf confirmed (LMU Digital Collections) | Google Books, HathiTrust, e-rara.ch |
| Alter, *Novum Testamentum Graecum* (Vienna 1786–87) | Not located | Google Books directly; Austrian National Library (ÖNB) digital collections |
| Birch, *Quatuor Evangelia Graece* (Copenhagen 1788) + *Variae Lectiones* (1798–1801) | Not located | Det Kongelige Bibliotek (Danish Royal Library) digital collections |
| Kipling's actual 1793 Codex Bezae facsimile | Not located (found a different, later 1864 Scrivener transcription instead — not a substitute, flagged in §1.15) | Cambridge University Library digital collections; CUL holds Codex Bezae itself and may hold Kipling's edition too |
| Stephanus 1546 / 1549 / 1551 as standalone period scans | Not located; only 1550-labeled reprints of uncertain provenance found | e-rara.ch, MDZ (digitale-sammlungen.de), Bodleian |
| Elzevir 1624 (1st ed.) specifically, distinct from the confirmed 1633 (2nd ed.) | Not located | e-rara.ch |

None of these are asserted as unobtainable — they're unconfirmed in the time spent on
this pass. Do not treat absence from this manifest's confirmed rows as proof of
non-existence.

---

## 4. Manifest — exact commands (nothing bulk-downloaded; run these individually as needed)

All commands pull a **single file**, not a full archive.org item, to stay within disk
budget. Swap `-O` target names as desired.

```bash
# --- Greek NT ---

# Erasmus 1516 (1st ed.) — 82 MB
curl -L -o erasmus-1516.pdf \
  "https://archive.org/download/nouuminstrument00eras/nouuminstrument00eras.pdf"

# Erasmus 1522 (3rd ed.) — 61 MB
curl -L -o erasmus-1522.pdf \
  "https://archive.org/download/roterodamvs-erasmus-novum-testamentum-1522/ROTERODAMVS%2C%20Erasmus%20-%20Novum%20Testamentum%20%5B1522%5D.pdf"

# Erasmus 1535 (5th/final ed.) — 82 MB text + 126 MB annotations
curl -L -o erasmus-1535-text.pdf \
  "https://archive.org/download/ARes162051/ARes162051.pdf"
curl -L -o erasmus-1535-annotations.pdf \
  "https://archive.org/download/ARes162052/ARes162052.pdf"

# Stephanus 1550 (provenance caveat — see §1.3) — 52 MB
curl -L -o stephanus-1550.pdf \
  "https://archive.org/download/1550-stephanus-textus-receptus/1550%20Stephanus%20Textus%20Receptus.pdf"

# Elzevir 1633 (Textus Receptus proper) — 191 MB
curl -L -o elzevir-1633.pdf \
  "https://archive.org/download/ned-kbn-all-00002699-001/ned-kbn-all-00002699-001.pdf"

# Walton's Polyglot, Greek NT vol (John–Rev) only — 109 MB, NOT the 16 GB full item
curl -L -o walton-polyglot-nt.pdf \
  "https://archive.org/download/WaltPoly1PrologVariantReadings/WaltPoly10_John-Rev.pdf"

# Wettstein 1751-52 — 112 MB
curl -L -o wettstein-1751.pdf \
  "https://archive.org/download/hekainediatheken00clem/hekainediatheken00clem.pdf"

# Griesbach 1796 2nd ed. vol 1 (Gospels) — 442 MB
curl -L -o griesbach-1796-v1.pdf \
  "https://archive.org/download/bim_eighteenth-century_novum-testamentum-graece_1796_1/bim_eighteenth-century_novum-testamentum-graece_1796_1.pdf"

# Matthaei 1803 — 22 MB
curl -L -o matthaei-1803.pdf \
  "https://archive.org/download/novumtestamentu01mattgoog/novumtestamentu01mattgoog.pdf"

# Woide/Cowper reprint of Codex Alexandrinus NT — 47 MB
curl -L -o woide-alexandrinus-nt.pdf \
  "https://archive.org/download/hkaindiathknovum00woid/hkaindiathknovum00woid.pdf"

# Complutensian Polyglot, Greek NT vol only — 513 MB
curl -L -o complutensian-nt.pdf \
  "https://archive.org/download/GRCNA28_DBS_HS/Greek-%281517%29-Complutensian-Polyglot-Bible-%28Latin-Hebrew%29.pdf"

# Machine-readable TR text (Elzevir + Scrivener), public domain, tiny (git clone)
git clone --depth 1 https://github.com/byztxt/greektext-elzevir.git
git clone --depth 1 https://github.com/byztxt/greektext-textus-receptus.git
git clone --depth 1 https://github.com/byztxt/greektext-scrivener.git

# --- post-1820, included per instruction ---

# Tregelles — 20 MB
curl -L -o tregelles-1857.pdf \
  "https://archive.org/download/greeknewtestamen01treg/greeknewtestamen01treg.pdf"

# Tischendorf 8th ed. vol 1 (Gospels, 1869) — 81 MB
curl -L -o tischendorf-8th-v1.pdf \
  "https://archive.org/download/tischendorf-ntg-vol.-1-gospels-8th-ed.-critica-maior-1869/Tischendorf_NTG%2C%20vol.%201%20-%20Gospels%20%5B8th%20ed.%2C%20critica%20maior%5D%20%281869%29.pdf"

# --- Septuagint ---

# Sixtine LXX 1587 (Vaticanus-based) — 138 MB — VERIFY it's Greek not Latin before relying on it, see §2.3
curl -L -o sixtine-lxx-1587.pdf \
  "https://archive.org/download/LATSEPT_DBS_HS/Latin-%281587%29-Septuigant-Vetus-Testamentum-Iuxta-Septuaginta.pdf"

# Grabe LXX 1707 Tomus I (Alexandrinus-based) — 498 MB
curl -L -o grabe-lxx-1707-t1.pdf \
  "https://archive.org/download/bim_eighteenth-century_septuaginta-interpretum-_grabe-joannes-ernestus_1707_1/bim_eighteenth-century_septuaginta-interpretum-_grabe-joannes-ernestus_1707_1.pdf"

# Montfaucon Hexaplorum 1713 — 138 MB
curl -L -o montfaucon-hexapla-1713.pdf \
  "https://archive.org/download/A208086/A208086.pdf"

# Holmes & Parsons vol 1, 1798 — 145 MB
curl -L -o holmes-parsons-1798-v1.pdf \
  "https://archive.org/download/1798-oxford-septuagint-edited-by-holmes-and-parsons-volume-1/1798%20-%20Oxford%20Septuagint%20edited%20by%20Holmes%20and%20Parsons%20-%20Volume%201.pdf"

# Holmes & Parsons vol 2, 1818 — 156 MB
curl -L -o holmes-parsons-1818-v2.pdf \
  "https://archive.org/download/1818-oxford-septuagint-edited-by-holmes-and-parsons-volume-2/1818%20-%20Oxford%20Septuagint%20edited%20by%20Holmes%20and%20Parsons%20-%20Volume%202.pdf"

# Field's Hexapla 1875 (post-1820, Tier 3, included per instruction) — 115 MB
curl -L -o field-hexapla-1875-t1.pdf \
  "https://archive.org/download/origenis-hexaplorum-t.-1-1875/HEBR%20-%20Field%20-%20Hexaplorum%20quae%20supersunt%2C%20t.1%2C%202012.pdf"
```

**Total if every single-file command above is pulled once: roughly 4.4 GB.** (Not the
sum of every "total_size" figure in the tables — those are full archive.org *item*
sizes including every redundant format: DjVu, ABBYY OCR archive, JP2 zips, EPUB, etc.
The individual PDF files listed in the manifest above are the only files the commands
actually pull.)

---

## 5. Summary

| Category | Confirmed obtainable (HTTP-verified or metadata-confirmed) | Not located this pass |
|---|---|---|
| Greek NT pre-1820 editions | Complutensian, Erasmus (all 5), Beza (1565, 1598), Elzevir 1633, Walton NT vol, Mill (base text only, not apparatus), Wettstein, Bengel, Griesbach (2nd ed.+), Matthaei (1803 revision), Woide (1860 reprint of 1786 text) | Mill's actual apparatus, Stephanus 1546/49/51 originals, Elzevir 1624, Alter, Birch, Kipling |
| Greek NT post-1820 (included per instruction) | Tregelles, Tischendorf 8th ed., Scrivener 1864 Bezae transcription | — |
| Septuagint pre-1820 editions | Complutensian LXX (bundled), Sixtine 1587 (caveat: language not visually spot-checked), Grabe 1707 Tomus I confirmed + later vols found not fully checked, Montfaucon 1713, Holmes & Parsons vols 1–2 | Aldine 1518 (only a single leaf found) |
| Septuagint post-1820 (included per instruction) | Holmes & Parsons vols 3, 4&5, Field's Hexapla 1875 | — |

**Top 3 highest-value items, by the brief's own stated criteria:**

1. **Wettstein 1751–52** — gave the field the manuscript sigla still in use in NA28/UBS5 today, fully verified and downloadable at 112 MB for the single PDF.
2. **Holmes & Parsons 1798–1827** — the largest LXX apparatus ever assembled; both pre-1820 volumes (1798, 1818) HTTP-verified, ~150 MB each as single PDFs.
3. **Sixtine LXX 1587** — the first printed edition based on Codex Vaticanus (a genuinely 4th-century witness, unlike almost everything on the NT side of this list), verified and downloadable at 138 MB, with the one open caveat that its language content wasn't visually spot-checked.

Close behind: the **Erasmus 1516–1535 run** (all five editions confirmed, ~450 MB total)
for the reason laid out in §0 — it's the item that most directly falsifies the assumption
that "pre-1820 edition" implies "old witness," which is the single most important thing
this research surfaced.
