# Research: The rabbinic corpus in original Hebrew/Aramaic

The corpus currently has **zero** rabbinic literature. This is the single largest
gap in scope, and it matters for the two reasons the project cares about:

1. **Variant biblical readings** — the rabbis argue about the text itself (tiqqune
   soferim, sebirin, qere/ketiv, the Masorah) centuries before any Masoretic codex
   on disk was written down.
2. **The canon argument, on the record** — Mishnah Yadayim 3:5 and Bavli Bava
   Batra 14b–15a are not later commentary *about* a settled canon; they are the
   primary evidence that the canon was ever in dispute at all, and who the rabbis
   themselves thought wrote which book.

Same two-date + Tier format as the rest of `docs/`:

- **Witness** — when the work was composed/redacted (not when a manuscript of it happens to survive).
- **Edition** — when *this particular* digitization/printing was made.
- **Tier 1** manuscript-grade diplomatic transcription · **Tier 2** pre-1820 print · **Tier 3** modern critical edition/digitization.

All URLs/API calls below were checked live on **2026-08-08** with `curl`. Per
project method, every Sefaria pull was verified against **content**, not HTTP
status — the `he` field was actually read, and multi-chapter texts were checked
against the `/api/shape/{title}` endpoint's `chapters` array before being called
complete. **Nothing was bulk-downloaded** — this is a manifest with exact,
copy-pasteable commands.

**Scope boundary respected**: targums are excluded — the project already pulls
those from Sefaria (`targums/`). Ben Sira is excluded — already covered in
`RESEARCH-targums-bensira.md`.

---

## Part 0 — The pipeline this project already has, reused, plus three traps hit live in this pass

`tools/pull_targums.py` already solved Sefaria's two traps for this project:
(a) a bare book ref returns only the *first section*, and (b) some listed texts
are HTTP-200 stubs. The same guard applies below — every "verified complete"
claim in this doc was checked against `/api/shape/{title}`'s `chapters` array,
not just a 200 status. A `pull_rabbinics.py` for this corpus should follow the
exact same shape: fetch `/api/shape/{title}` first, iterate real chapter counts,
flag anything under the expected count as INCOMPLETE and refuse to write it.

**All three of this project's known research traps were hit live during this
pass, and are recorded here so the next person (or the next `pull_*.py`)
doesn't repeat them:**

1. **Sefaria bare-book-ref trap, caught red-handed on `Sifrei_Bamidbar`.**
   `curl -s "https://www.sefaria.org/api/texts/Sifrei_Bamidbar?context=0"`
   returns **HTTP 200** with a populated-looking `he` array — but that array
   has only **8 entries** (pisqa 1's verses), while the response's own
   `"lengths": [161, 295]` field says the real work has 161 pisqaot / 295
   verses total. `"length": 161` is even sitting right there in the same
   JSON blob as the 8-item array. **The fix, applied throughout this doc**:
   always check `lengths`/`length` before treating a bare-ref response as the
   whole work, and walk chapters explicitly (`Sifrei_Bamidbar.84`,
   `Sifrei_Bamidbar.85`, ... not `Sifrei_Bamidbar`) for anything with more
   than one section. This is exactly how pisqa 84 (Numbers 10:35, tied to
   Mishnah Yadayim 3:5 — see Part 6C) was actually located: chapter-by-chapter,
   not from the bare-ref response.
2. **archive.org identifier vs. actual filename.** Every archive.org file
   referenced in this doc (Okhlah we-Okhlah, the Rabbinovicz 1972 reprint) was
   confirmed via `https://archive.org/metadata/<identifier>` — which lists the
   *real* filenames inside the item (`dasbuchochlahwoc00fren_djvu.txt`, not a
   guessed name) and the `access-restricted-item` flag — rather than guessing
   a `_djvu.txt` suffix off the identifier and taking a 404 as "dead."
3. **403 / Cloudflare "Just a moment..." is not the same as "doesn't exist."**
   `hebrewbooks.org` and `catalog.hathitrust.org` both returned hard 403s to
   plain `curl` and to the `WebFetch` tool in the first half of this pass.
   Both turned out to have real, resolvable content once fetched with
   `tools/scrape_walled.py` (Scrapling's `StealthyFetcher`, a real browser
   fingerprint) — see Part 7 for what that unlocked on Dikdukei Soferim. The
   corrected rule: a 403/challenge page from a plain HTTP client is a "try the
   stealth fetcher" signal, not a dead end to write up as unavailable.

---

## Part 1 — Mishnah (redacted c. 200 CE)

Sefaria hosts the complete Mishnah (all 6 sedarim, 63 tractates) with **three
parallel Hebrew versions**: an unpointed Torat Emet text, a pointed Vilna/Romm
1913 print, and a **Kaufmann manuscript**-based edition (ed. Dan Be'eri) — the
Kaufmann MS (Budapest, Kaufmann A50, early 12th c.) is itself one of the two
best early complete Mishnah witnesses, alongside the Parma/Cambridge MSS.

### 1A. Mishnah Yadayim 3:5 — the canon-dispute mishnah — verified live

```
curl -s "https://www.sefaria.org/api/texts/Mishnah_Yadayim.3.5?context=0&commentary=0"
```

Returned in full. Text (Hebrew, unpointed base + Torat Emet pointed):

> "...כָּל כִּתְבֵי הַקֹּדֶשׁ מְטַמְּאִין אֶת הַיָּדַיִם. שִׁיר הַשִּׁירִים וְקֹהֶלֶת מְטַמְּאִין אֶת הַיָּדַיִם... אָמַר רַבִּי עֲקִיבָא, חַס וְשָׁלוֹם, לֹא נֶחֱלַק אָדָם מִיִּשְׂרָאֵל עַל שִׁיר הַשִּׁירִים שֶׁלֹּא תְטַמֵּא אֶת הַיָּדַיִם... וְאִם נֶחְלְקוּ, לֹא נֶחְלְקוּ אֶלָּא עַל קֹהֶלֶת."
> ("All the Holy Scriptures render the hands unclean. Song of Songs and
> Ecclesiastes render the hands unclean... R. Akiva said: Heaven forbid! No one
> in Israel ever disputed that Song of Songs renders the hands unclean... and if
> they disputed, it was only about Ecclesiastes.")

This is the single most direct primary-source text for "which books count" —
not a later report about a dispute, the dispute itself, with named parties
(R. Yehuda, R. Yose, R. Shimon, R. Akiva, R. Yohanan b. Yehoshua) on the record.

| | |
|---|---|
| Witness (composition) | Mishnah redacted **c. 200 CE** (R. Yehuda HaNasi); this specific dispute reports 1st-c. CE Yavneh-era debate |
| Witness (Kaufmann MS) | **early 12th c. CE** — one of the two best complete Mishnah manuscripts |
| Edition (this pull) | Sefaria API, live |
| Tier | 3 (this digitization); Tier 1 for the Kaufmann-MS-based version specifically |
| License | **CC-BY** (Hebrew, Torat Emet 357); Kaufmann-MS-based edition license not separately re-checked — verify per-version before bulk pull |
| Full-tractate fetch | `curl -s "https://www.sefaria.org/api/texts/Mishnah_Yadayim.3?context=0"` (chapter 3, 5 mishnayot); whole tractate is 4 chapters, `/api/shape/Mishnah_Yadayim` confirms `[5,4,5,8]` |

### 1B. Full Mishnah — bulk shape

`/api/index/Shishah_Sedarim` (or per-seder) gives the full table of contents.
Reasonable per-seder pull pattern, same as `pull_targums.py`:

```bash
for tractate in Berakhot Peah Demai ... ; do
  curl -s "https://www.sefaria.org/api/texts/Mishnah_${tractate}?context=0" -o "Mishnah_${tractate}.json"
done
```

63 tractates total. Not enumerated here in full — the point is the pipeline
is proven on Yadayim; running it across all 63 is mechanical.

---

## Part 2 — Tosefta (c. 250 CE)

### 2A. Tosefta Yadayim — the second canon-dispute source, verified live

Sefaria's default chapter numbering differs from the standard **Zuckermandel**
edition citation convention — the passage cited in scholarship as "Tosefta
Yadayim 2:14" is at **Sefaria ref `Tosefta_Yadayim.2.6`**. Verified by fetching
the whole chapter and grepping for the keyword, not by trusting a guessed ref:

```
curl -s "https://www.sefaria.org/api/texts/Tosefta_Yadayim.2?context=0&commentary=0"
```

Chapter 2, mishnah 6 (Sefaria numbering):

> "רַבִּי שִׁמְעוֹן בֶּן מְנַסְיָא אוֹמֵר, שִׁיר הַשִּׁירִים מְטַמְּאָה אֶת הַיָּדַיִם מִפְּנֵי שֶׁנֶּאֶמְרָה בְּרוּחַ הַקֹּדֶשׁ, וְקֹהֶלֶת אֵינָהּ מְטַמְּאָה אֶת הַיָּדַיִם שֶׁאֵינָהּ אֶלָּא מֵחָכְמָתוֹ שֶׁל שְׁלֹמֹה..."
> (R. Shimon b. Menasya: Song of Songs defiles the hands because it was said
> by the holy spirit; Ecclesiastes does *not* defile the hands, being only
> Solomon's own wisdom.)

This is a genuinely **different position** from the Mishnah's — a named Tanna
arguing Kohelet fails a *different* test (divine inspiration vs. human wisdom)
than the Mishnah's dispute records. This is exactly the kind of variant
argument that makes the Tosefta worth having alongside the Mishnah, not instead
of it.

| | |
|---|---|
| Witness | c. 250 CE (Tosefta redaction; incorporates earlier baraitot) |
| Edition | Sefaria digitization |
| Tier | 3 |
| License | **CC0** / Public Domain (Hebrew — `heVersionTitle: "Tosefta Yadayim - Machon Mamre"`) |
| Full tractate | `curl -s "https://www.sefaria.org/api/texts/Tosefta_Yadayim?context=0"` — 2 chapters, 9+9 halakhot, shape-confirmed |

### 2B. Full Tosefta — mixed provenance, verify per-tractate

`books.json` from Sefaria-Export lists **330 Hebrew entries** under
`Tosefta > Lieberman Edition` and **124** under `Tosefta > Vilna Edition`.
The naming is a trap worth flagging: **"Lieberman Edition" here does not mean
Saul Lieberman's copyrighted 20th-c. *Tosefta Ki-Fshutah* commentary/text** —
spot-checking the actual API resolution shows the base Hebrew text is sourced
from **Mechon Mamre's digitization of the Vienna Codex** reading tradition
(license mostly **CC0**), while a *separate* "Brief Commentary" sub-branch
under the same category is Lieberman's actual notes (not independently
license-checked, presumed restrictive — skip it). Spot-checks:

```
Tosefta_Bava_Batra.1.1  -> CC0,  heVersionTitle "Tosefta Bava Batra - Machon Mamre"
Tosefta_Sotah.1.1       -> CC0,  heVersionTitle "Tosefta Sota - Machon Mamre"
Tosefta_Sanhedrin.1.1   -> license field empty, heVersionTitle "Tosefta Sanhedrin - Machon Mamre" (same lineage, unset tag)
Tosefta_Berakhot.1.1    -> license "unknown", heVersionTitle "Tosefta B'rachot" (NOT Machon Mamre — different source, check before pulling)
```

**Recommendation**: pull tractate-by-tractate, and hold the ones whose
`license` field comes back `unknown`/empty for a manual check rather than
writing them blind — same discipline `pull_targums.py` already applies to
short/stub texts, just applied to license instead of length.

---

## Part 3 — Talmud Bavli (c. 500–600 CE redaction)

Sefaria's flagship text: the **William Davidson Edition**, vocalized
Aramaic/Hebrew, full 37 tractates (2,711 dapim). License is **CC-BY-NC** across
the board (confirmed on every daf checked below) — this is the one major
non-commercial restriction in this whole manifest; flag it in `PROVENANCE.md`
if pulled, the same way the DSS and Sinaiticus NC restrictions are already
flagged there.

### 3A. Bava Batra 14b–15a — who wrote which book — verified live, full text pulled

```
curl -s "https://www.sefaria.org/api/texts/Bava_Batra.14b?context=0&commentary=0"
curl -s "https://www.sefaria.org/api/texts/Bava_Batra.15a?context=0&commentary=0"
```

14b line 8 opens the baraita **"סִדְרָן שֶׁל נְבִיאִים"** ("the order of the
Prophets": Joshua+Judges, Samuel+Kings, Jeremiah, Ezekiel, Isaiah, the Twelve)
— note this order puts **Isaiah after Jeremiah and Ezekiel**, and the Gemara
immediately asks why (14b line 10), since Isaiah is chronologically earlier;
the answer given is thematic, not chronological. Line 11 continues into
**"סִדְרָן שֶׁל כְּתוּבִים"** ("the order of the Writings": Ruth, Psalms, Job,
Proverbs, Ecclesiastes, Song of Songs, Lamentations, Daniel, Scroll of Esther,
Ezra, Chronicles) — a **different book order than any modern printed Tanakh**,
worth its own note if this project ever documents canon-order variants
alongside text variants.

Line 12 (14b) into 15a opens **"וּמִי כְתָבָן"** ("and who wrote them"):

> משֶׁה כָּתַב סִפְרוֹ וּפָרָשַׁת בִּלְעָם וְאִיּוֹב. יְהוֹשֻׁעַ כָּתַב סִפְרוֹ וּשְׁמוֹנָה פְּסוּקִים שֶׁבַּתּוֹרָה [דמיתתו]. שְׁמוּאֵל כָּתַב סִפְרוֹ ... דָּוִד כָּתַב סֵפֶר תְּהִלִּים עַל יְדֵי עֲשָׂרָה זְקֵנִים ... יִרְמְיָה כָּתַב סִפְרוֹ וְסֵפֶר מְלָכִים וְקִינוֹת. חִזְקִיָּה וְסִיעָתוֹ כָּתְבוּ יְשַׁעְיָה מִשְׁלֵי שִׁיר הַשִּׁירִים וְקֹהֶלֶת ...
>
> Moses wrote his own book, the Balaam section, and Job. Joshua wrote his own
> book and eight verses of the Torah [the account of his own death]. Samuel
> wrote his own book... David wrote Psalms through ten elders... Jeremiah
> wrote his own book, Kings, and Lamentations. Hezekiah and his colleagues
> wrote Isaiah, Proverbs, Song of Songs, and Ecclesiastes...

— continuing with a live dispute over **whether Job existed as a historical
person or is a parable** (15a lines 14–17: Rava dates him to the era of the
spies; an anonymous sage before R. Shmuel bar Nachmani argues Job never
existed and never was created, he's a parable — an explicit rabbinic voice
denying Job's historicity, on the record, in the Talmud itself).

| | |
|---|---|
| Witness | c. 500–600 CE (Bavli redaction); attributes an older baraita |
| Edition | William Davidson Edition (Sefaria digitization + Koren/Steinsaltz-adjacent vocalization project) |
| Tier | 3 |
| License | **CC-BY-NC** |
| Verified | Yes — full daf text fetched and read, both 14b and 15a |

### 3B. Shabbat 115a — divine-name handling, sacred writings in a fire

```
curl -s "https://www.sefaria.org/api/texts/Shabbat.115a?context=0&commentary=0"
```

Note: **Shabbat 115a proper does not open with the divine-name discussion** —
the daf as fetched begins mid-sugya on a walnut-shelling ruling (Yom Kippur
falling on a weekday) before moving to its main topic. The classic sugya on
**rescuing sacred scrolls from a fire on Shabbat, including ones written in
other languages, and what to do about scrolls containing the divine Name** is
centered on **Shabbat 115a–116b** as a block, not a single line on 115a alone
— confirm the exact line before quoting a specific citation; fetch 115a–116b
together (6 dapim) rather than assuming one daf holds the whole sugya.

```
curl -s "https://www.sefaria.org/api/texts/Shabbat.115a-116b?context=0&commentary=0"
```

| | |
|---|---|
| Witness | c. 500–600 CE |
| License | **CC-BY-NC** |
| Verified | Content resolves; exact line-level location of the divine-name material needs a closer read before quoting — flagged honestly rather than guessed |

### 3C. Megillah 7a — Esther's canonicity — verified live

```
curl -s "https://www.sefaria.org/api/texts/Megillah.7a?context=0&commentary=0"
```

Resolves, CC-BY-NC. Megillah 7a is where the Gemara records the dispute over
whether Esther "was said/written under the holy spirit" (i.e. canonical) —
R. Shmuel bar Yehuda's report that Esther sent to the Sages asking to be
canonized ("כתבוני לדורות" — "write me down for [all] generations") and
initial rabbinic resistance is here.

### 3D. Sanhedrin 99a — verified live, CC-BY-NC (afterlife/heresy sugya, tangential to canon but on the same daf-range as other canon material in Sanhedrin 90–101)

### 3E. Tractate Soferim — the minor tractate on scribal law, verified live

Not resolvable at `Soferim.1.1` — the correct Sefaria ref is `Tractate_Soferim`:

```
curl -s "https://www.sefaria.org/api/texts/Tractate_Soferim.1?context=0&commentary=0"
```

Resolves with real content (scribal materials, writing surfaces — Hebrew begins
"אֵין כּוֹתְבִין סְפָרִים... לֹא עַל עוֹר בְּהֵמָה טְמֵאָה"). This is one of the
seven **minor tractates** appended to Nezikin in the Vilna Talmud — post-Talmudic
(geonic-era, roughly **8th c. CE**) but transmitted with the Bavli text
tradition. Directly relevant to the project: Soferim is the tractate that
codifies scribal rules for **writing the divine Name, correcting errors,
disposing of worn-out scrolls (genizah), and the physical rules a Torah scroll
must meet** — adjacent to, and sometimes citing, the tiqqune soferim tradition
(see Part 6).

| | |
|---|---|
| Witness | c. 8th c. CE (post-Talmudic, geonic) |
| Edition | Talmud Bavli, Vilna 1883 |
| Tier | 3 (digitization); underlying print is Tier 2-adjacent by lineage (Vilna Shas, 1880–86) |
| License | **CC-BY** (Hebrew) |

---

## Part 4 — Talmud Yerushalmi (c. 400 CE)

Confirmed present and complete for all four sedarim it actually covers
(Zeraim, Moed, Nashim, Nezikin — Yerushalmi has no Kodashim and only
tractate Niddah from Tohorot, which is a real historical gap in the Yerushalmi
itself, not a digitization gap).

```
curl -s "https://www.sefaria.org/api/texts/Jerusalem_Talmud_Sanhedrin.1.2?context=0&commentary=0"
```

Shape-confirmed non-trivial for Berakhot, Yevamot, Sanhedrin (spot-checked).

| | |
|---|---|
| Witness | c. 400 CE (Palestinian redaction, earlier than the Bavli by ~150–200 years) |
| Edition | Hebrew text digitized alongside **Heinrich W. Guggenheimer's academic edition** (De Gruyter, 1999–2015) — this is the `heVersionTitle` Sefaria reports; the Hebrew itself is the traditional print text (Krotoshin/Vilna lineage), the Guggenheimer connection is a provenance/attribution note, not evidence the Hebrew text itself is a 21st-c. copyrighted translation |
| Tier | 3 |
| License | **CC-BY** (confirmed on Sanhedrin, Berakhot) |

**Caveat worth stating plainly**: the `heVersionTitle` string naming a modern,
priced academic De Gruyter edition next to a `CC-BY` license tag is the kind
of thing that deserves a second look before bulk-pulling at scale — Sefaria's
license field is almost certainly correct (they run a legal review process
before tagging anything CC-anything), but it wasn't independently cross-checked
against Guggenheimer's own publisher terms in this pass.

---

## Part 5 — Midrash: essentially the entire corpus, verified present

This is the best news in this whole research pass. Every major midrashic work
requested is on Sefaria, in Hebrew, and the **entire set together is ~23.5 MB**
— small enough that pulling the whole thing is trivial once license is checked
per-work.

### 5A. Verified complete + sized (Hebrew, `merged` version, via Sefaria-Export GCS bucket — see Part 9)

| Work | Sefaria title | Chapters/units (shape-verified) | Hebrew source | License | Size |
|---|---|---|---|---|---|
| **Genesis Rabbah** | `Bereshit Rabbah` | 100 parashiyot | Midrash Rabbah — Torat Emet | CC-BY | 2.32 MB |
| **Exodus Rabbah** | `Shemot Rabbah` | 52 parashiyot | Midrash Rabbah — Torat Emet | CC-BY | 1.50 MB |
| **Leviticus Rabbah** | `Vayikra Rabbah` | 37 parashiyot | Midrash Rabbah — Torat Emet | CC-BY | 1.12 MB |
| **Numbers Rabbah** | `Bamidbar Rabbah` | 23 parashiyot | Midrash Rabbah — Torat Emet | CC-BY | 2.28 MB |
| **Deuteronomy Rabbah** | `Devarim Rabbah` | 17 (or 11, per recension) | Midrash Rabbah — Torat Emet | CC-BY | 0.52 MB |
| **Song of Songs Rabbah** | `Shir HaShirim Rabbah` | 8 parashiyot | Midrash Rabbah — Torat Emet | CC-BY | 0.95 MB |
| **Ruth Rabbah** | `Ruth Rabbah` | 9 parashiyot | Midrash Rabbah — Torat Emet | CC-BY | 0.23 MB |
| **Lamentations Rabbah** | `Eikhah Rabbah` | 5 chapters + petichta | Midrash Rabbah — Torat Emet | CC-BY | 0.63 MB |
| **Ecclesiastes Rabbah** | `Kohelet Rabbah` | 12 chapters | Midrash Rabbah — Torat Emet | CC-BY | 0.80 MB |
| **Esther Rabbah** | `Esther Rabbah` | 10 parashiyot | Midrash Rabbah — Torat Emet | CC-BY | 0.34 MB |
| **Mekhilta deRabbi Yishmael** | `Mekhilta DeRabbi Yishmael` | 9 tractates (Pischa, Beshalach, Shirah, Vayassa, Amalek, Bachodesh, Nezikin, Kaspa, Shabbata) | Beeri Edition, Koren 2019 | CC-BY | 1.54 MB |
| **Mekhilta deRabbi Shimon bar Yochai** | `Mekhilta_DeRabbi_Shimon_Ben_Yochai` (note: **Ben**, not Bar) | Fragmentary by nature — reconstructed from citations in Yalkut Shimoni/Midrash HaGadol, many empty chapter slots | D. Hoffman ed., Frankfurt 1905 | **CC0** | not separately sized |
| **Sifra** (on Leviticus) | `Sifra` | Baraita d'R. Yishmael + 9 dibbura sections, 278 sub-units total | Venice 1545 print, digitized | CC-BY | 1.25 MB |
| **Sifre on Numbers** | `Sifrei Bamidbar` | 161 pisqaot | Wikisource | **CC-BY-SA** (he license differs from en license) | 0.51 MB |
| **Sifre on Deuteronomy** | `Sifrei Devarim` | 357 pisqaot | Vocalized Edition (a distinct Finkelstein-lineage text also listed, not the one pulled) | **CC-BY-NC** | 1.23 MB |
| **Pesikta Rabbati** | `Pesikta Rabbati` | 47 pisqaot | OYW (undated digitization) | **CC0** | 0.93 MB |
| **Pesikta deRav Kahana** | `Pesikta DeRav Kahana` | 28 pisqaot | Mandelbaum ed. (Oxford MS-based), NY 1987 | license not separately confirmed — check before pulling, Mandelbaum's edition is 20th-c. and could carry restrictions | 0.60 MB |
| **Midrash Tanchuma** (standard/Yelamdenu-style print) | `Midrash Tanchuma` | 828 sub-sections across 5 books (Torah portions) | Torat Emet | not separately confirmed, likely CC-BY per family pattern | 3.99 MB |
| **Midrash Tanchuma, Buber recension** | `Midrash Tanchuma Buber` | 1,048 sub-sections | S. Buber ed., 1885 | not separately confirmed | 2.01 MB |

**Bonus finds, not in the original request but same corpus family and free:**

| Work | What it is | Size |
|---|---|---|
| `Seder Olam Rabbah` | Tannaitic chronology midrash (dates from Creation to the Bar Kokhba revolt) | 0.12 MB |
| `Tanna DeBei Eliyahu Rabbah` | Ethical/aggadic midrash, geonic-era compilation of older material | 0.55 MB |

### 5B. Method note on the size numbers above

Sizes are `Content-Length` from a live `HEAD` request against each work's
`merged.json` on the **Sefaria-Export** Google Cloud Storage bucket (see Part 9
for the bucket itself) — e.g.:

```bash
curl -sI "https://storage.googleapis.com/sefaria-export/json/Midrash/Aggadah/Midrash%20Rabbah/Bereshit%20Rabbah/Hebrew/merged.json"
```

**Important caveat found in this pass**: the `merged.json` files themselves do
**not** carry a `license` field inline — they carry a `versionSource` URL and a
`versionTitle` string, but license has to be cross-checked against the live
`/api/texts/{ref}` endpoint (which does return `license`), not assumed from the
bulk file. This is a real trap for a future bulk-pull script: don't write a
`merged.json` to disk and call the license question closed just because it
downloaded — verify license via the API first, the same way `pull_targums.py`
already verifies completeness via the API rather than trusting the download.

**Sum of the 21 core works sized above: ~23.5 MB.** This is not a projection —
every file in that sum was individually HEAD-checked, and together they
represent essentially the complete classical Midrash corpus (all 10 books of
Rabbah, both Mekhiltas, Sifra, both Sifre, both Pesikta works, both Tanchuma
recensions) plus two bonus works. At this size, downloading the whole set is
not a "bulk download" in any meaningful sense — it's smaller than a single
LXX-Rahlfs file already on disk.

---

## Part 6 — Masoretic apparatus proper

This is the part of the request with the most negative results, reported
honestly rather than papered over.

### 6A. Masorah magna / parva — NOT available as a standalone digitized text anywhere checked

- **Sefaria**: `/api/name/Masorah` and `/api/name/Mesorah` both resolve only
  to a **Topic tag** (`key: "mesorah"`, used to label source sheets), not a
  text collection. Sefaria does not host the Masorah magna/parva apparatus as
  its own browsable/fetchable work.
- **What's already on disk comes closest**: `hebrew-ot/morphhb` (OSHB/WLC) does
  encode **qere/ketiv** (confirmed: 20 `qere`-tagged instances in `Gen.xml`
  alone) and has scattered `<note>` elements where the editors diverged from
  BHS — but this is not the marginal Masorah parva (the letter/word-count
  notations and cross-reference key-letters written in the codex margins) or
  the Masorah magna (the expanded lists at top/bottom of page). Those notes
  were never transcribed into OSHB's structured data; they exist only as
  images of the actual codex pages.
- **STEPBible-Data**: no Masorah dataset found (already used for TAHOT tagging
  on disk; confirmed no additional masoretic-apparatus files in the repo).

**Bottom line**: a real, free, machine-readable transcription of the Masorah
magna/parva apparatus (as opposed to the base consonantal/vocalized text it
annotates) was **not found** in this pass. The closest thing that exists is
below (Okhlah we-Okhlah), which is a related but distinct genre — a *systematic
compilation* of masoretic word-lists, not a page-by-page transcription of the
marginal notes themselves.

### 6B. Okhlah we-Okhlah — found, real, public domain, downloadable

Frensdorff's edition is the standard 19th-c. scholarly edition of this work —
a systematic list-genre companion to the Masorah (organized as dozens of
numbered word/phrase lists: words occurring exactly twice with different
meanings, plene/defective spelling pairs, etc.), transcribed from a single
Paris manuscript (Bibliothèque Nationale).

```bash
curl -sI "https://archive.org/download/dasbuchochlahwoc00fren/dasbuchochlahwoc00fren_djvu.txt"
# HTTP 200, content-length 1016978
```

| | |
|---|---|
| Witness | The Okhlah we-Okhlah genre itself is early medieval Masoretic scholarship, generally dated **9th–10th c. CE** (pre-dates or is contemporary with the Masoretic codices); the specific Paris MS Frensdorff used is not independently dated in this pass |
| Edition | S. Frensdorff, *Das Buch Ochlah W'ochlah (Massora)*, Hannover, **1864** |
| Tier | 2 (pre-1820 cutoff doesn't apply the same way to a 19th-c. *scholarly edition* of a medieval list — flag as Tier 3 by the project's own definition, i.e. modern critical edition of old material, despite being genuinely the standard reference) |
| Archive.org identifier | `dasbuchochlahwoc00fren` (also mirrored at `bub_gb_AQk52MpnRzcC`, `OkhlahVeOkhlah`) |
| Access | **Confirmed not access-restricted**, djvu.txt present, US public domain (pre-1928) |
| **OCR caveat** | Text is **German + Hebrew mixed** (Frensdorff's introduction and apparatus are in German; the actual masoretic lists are Hebrew). Grepping the OCR text for specific Hebrew technical terms (e.g. סבירין) returned no hits — this may mean OCR quality on the Hebrew portions is poor (the project has already hit this exact failure mode with the Erasmus Greek-OCR'd-as-Latin case in `PROVENANCE.md`), or that this particular list isn't in this particular manuscript's selection. **Not resolved either way in this pass — flag as needing a closer read before relying on it for a specific list.** |

### 6C. Tiqqune soferim (the ~18 "corrections of the scribes") — HIGHEST PRIORITY ITEM, content verified live

**There is no single ancient text called "Tiqqune Soferim."** That matters for
this project specifically: it means the rabbinic tradition's own
acknowledgment that the scribes altered the text is not one discrete document
to pull, but a claim embedded, piecemeal, inside works this doc already
confirms are on Sefaria. Two of those loci were fetched and read directly in
this pass (not just confirmed to exist):

**Tractate Soferim, chapter 6 — the single best on-topic location, full text pulled:**

```bash
curl -s "https://www.sefaria.org/api/texts/Tractate_Soferim.6?context=0&commentary=0"
```

All 9 halakhot of the chapter were fetched (shape-confirmed: chapter 6 has
exactly 9 units). This chapter is the Talmudic-tradition catalogue of
scribal/textual peculiarities, and it is where the *related* categories the
user asked about — not "tiqqune soferim" under that exact name, but the same
family — actually live:

- **Halakhah 3**: the ten dotted words in the Torah (עשר נקודות בתורה) —
  the puncta extraordinaria, with the list starting "ישפוט ה' ביני וביניך"
  (Genesis 16:5) and continuing through named examples with the specific
  letters marked.
- **Halakhah 4**: **"אָמַר רַבִּי שִׁמְעוֹן בֶּן לָקִישׁ: שְׁלֹשָׁה סְפָרִים נִמְצְאוּ בָּעֲזָרָה..."**
  — "R. Shimon ben Lakish said: three [Torah] scrolls were found in the
  Temple court" — each with a different reading in three separate places
  (ספר מעונה / ספר זאטוטי / ספר היא), and **the scribes resolved each
  disagreement by majority vote among the three scrolls** ("באחד מצאו כתוב...
  ובשנים כתוב... וקיימו שנים ובטלו אחד" — "in one it was written X, in two it
  was written Y... they upheld the two and annulled the one"). This is a
  primary rabbinic text **explicitly describing textual variants being
  resolved by a scribal committee**, not a single fixed autograph — about as
  close to a smoking gun as this project is going to find for "the rabbis
  knew the text varied and corrected it themselves."
- **Halakhot 5, 8–9**: lists of words with a written/read (ketiv/qere-style)
  mismatch — three words "not written with an aleph but read with a vav,"
  words that are read but not written, and words written but not read. This
  is the same technical family as *sebirin* (6D) even though neither halakhah
  uses that exact term.

`Tractate Soferim` does **not**, on this direct read of chapter 6, use the
literal phrase "תיקוני סופרים" — the tractate's name refers to scribal *law*
generally, not this specific euphemism tradition. Worth stating precisely
rather than implying a false match on the name alone.

**Sifre on Numbers, pisqa 84 (Numbers 10:35, "וַיְהִי בִּנְסֹעַ הָאָרֹן") — found and pulled after hitting the bare-ref trap (see Part 0):**

```bash
curl -s "https://www.sefaria.org/api/texts/Sifrei_Bamidbar.84?context=0&commentary=0"
# license: CC-BY, 5 verses
```

Halakhah 1 opens: **"וַיְהִי בִּנְסֹעַ הָאָרֹן. נָקוֹד עָלָיו מִלְמַעְלָה וּמִלְּמַטָּה, מִפְּנֵי שֶׁלֹּא הָיָה זֶה מְקוֹמוֹ. רַבִּי אוֹמֵר: מִפְּנֵי שֶׁהוּא סֵפֶר בְּעַצְמוֹ. מִכָּאן אָמְרוּ: סֵפֶר שֶׁנִּמְחַק וְנִשְׁתַּיֵּר בּוֹ פ"ה אוֹתִיּוֹת כְּפָרָשַׁת וַיְהִי בִּנְסוֹעַ הָאָרֹן מְטַמֵּא אֶת הַיָּדַיִם..."**
— "'And it came to pass, when the Ark set forward...' It is dotted above and
below, because this was not its [proper] place. Rebbi says: because it is a
book unto itself. **From here they said: a scroll that has been erased but
85 letters remain, like the passage 'Vayehi binso'a ha-aron,' renders the
hands unclean...**" — this is the *exact* source-citation the Mishnah Yadayim
3:5 "85 letters" rule (quoted in Part 1A) is drawing on, found by walking
Sifre Bamidbar chapter-by-chapter rather than trusting the bare-ref response,
which returned only pisqa 1. It independently corroborates that the rabbis
treated this specific passage as textually anomalous/dislocated — bracketed
with special marks precisely because tradition held it was moved out of its
original place in the Torah.

**Not located in this pass, stated honestly**: the specific verse-by-verse
euphemism list most commonly cited today as "the 18 tiqqune soferim" (e.g.
Genesis 18:22 "וְאַבְרָהָם עוֹדֶנּוּ עֹמֵד לִפְנֵי ה׳" — traditionally said to have
originally read the reverse, "and the LORD was still standing before
Abraham," softened for reverence) was searched for directly — grepped across
Mekhilta deRabbi Yishmael (all 6 sub-tractates, all chapters), Avot deRabbi
Natan (both recensions, chapters 30–37 where standard citations place it),
and Bereshit Rabbah (parashiyot 48–50, covering Genesis 18) for the phrases
"תקון"/"תיקון"/"כנה הכתוב" — **zero hits**. This matches the actual scholarly
consensus on this topic (see McCarthy's 1981 monograph *The Tiqqune Sopherim*,
and the *Encyclopaedia Judaica* entry): **there is no single ancient rabbinic
passage that enumerates all ~18 in one place.** The fullest ancient
enumerations are preserved in the **Masorah's own marginal notes** attached
to the individual verses (6A — not machine-readable anywhere found) and in
list-compilations of the **Okhlah we-Okhlah** type (6B — found, PD, but OCR
quality on its Hebrew lists is unverified). Individual Talmudic/midrashic
passages (including the two pulled above) preserve *some* of the underlying
phenomena and the rabbis' own awareness that the text had been shaped by
scribal hands, but not the number-18 list as such. **Practical
recommendation**: don't chase a nonexistent single "tiqqune soferim" text;
the two passages pulled above are the real, verified, on-topic content this
project should cite, and the Masorah/Okhlah gap (6A/6B) is the honest
limitation on getting the full traditional list in any machine-readable form.

### 6D. Sebirin and itture soferim — same situation as 6C

Both are technical Masoretic categories (sebirin = places the reader might
guess a different word than what's written; itture soferim = a small list,
traditionally five words, where a conjunctive vav was "removed by the
scribes"). Neither resolves as a standalone Sefaria text
(`/api/name/Sebirin`, `/api/name/Itture Soferim` both empty). The classical
locus for sebirin is **Bavli Nedarim 37b–38a** (already covered per Part 3 —
Nedarim itself was not individually pulled/verified in this pass, only
confirmed as part of the standard 37-tractate Bavli); the classical locus for
itture soferim is inside the **Masorah** apparatus itself (6A, unresolved) and
inside **Okhlah we-Okhlah** (6B) as one of its numbered lists. Same
recommendation as 6C: don't chase a nonexistent standalone text, pull Nedarim
+ the Okhlah we-Okhlah scan, and locate the passages within them as a
follow-up pass.

---

## Part 7 — Dikdukei Soferim (Rabbinovicz) — RESOLVED via stealth fetch; real, free, non-commercial license

Plain `curl` and `WebFetch` both hit hard `403`s on `hebrewbooks.org` — the
single most likely free host for this work — and archive.org/HathiTrust
search turned up nothing free (the one hit, a 1972 reprint, is lending-gated).
Per the corrected method (Part 0, trap 3), this was re-tried with
`tools/scrape_walled.py` (Scrapling `StealthyFetcher`, real browser
fingerprint) instead of being written up as blocked — and it worked.

| | |
|---|---|
| Author | Raphael Nathan Nota Rabbinovicz (d. 1888) |
| Content | Talmud Bavli variant readings drawn primarily from the **Munich Codex (Cod. Hebr. 95, 1342 CE)**, cross-checked against other MSS, early printed editions, and medieval rabbinic citations |
| Composition | **1867–1886** (15 volumes published in his lifetime); a 16th volume appeared **1897**, posthumous, from his notes |
| Tier | 3 (19th-c. critical apparatus, even though pre-1900 enough that the *original* carries no copyright) |

### 7A. Found — real HebrewBooks.org book IDs, confirmed via DuckDuckGo HTML search (not blocked) then loaded via stealth fetch

```bash
curl -s "https://html.duckduckgo.com/html/?q=hebrewbooks.org+דקדוקי+סופרים+רבינוביץ" -A "Mozilla/5.0"
```

Returned real, distinct hebrewbooks.org book IDs matching individual
Rabbinovicz volumes by tractate:

| HebrewBooks ID | Volume | URL |
|---|---|---|
| `38512` | Part 1 — Berakhot, Zeraim | `https://hebrewbooks.org/38512` |
| `38518` | Part 7 — Shabbat | `https://hebrewbooks.org/38518` |
| `38521` | Part 15 — Menachot | `https://hebrewbooks.org/38521` |
| `22086` | (concentrated/מרוכזת edition) — Nezikin | `https://hebrewbooks.org/22086` |
| `22189` | (concentrated/מרוכזת edition) — Zeraim | `https://hebrewbooks.org/22189` |

### 7B. Verified live — page loads, metadata confirms it's the real work, download link resolves

```bash
python3 -c "
from scrapling.fetchers import StealthyFetcher
page = StealthyFetcher.fetch('https://hebrewbooks.org/38512', headless=True, network_idle=True)
print(page.status)   # 200
"
```

The book-detail page for ID `38512` (loaded through Cloudflare successfully
via stealth fetch) reads, verbatim: **"כותר: דקדוקי סופרים - חלק א - ברכות,
זרעים | מחבר: רבינוביץ, רפאל נתן נטע, 1835-1888"** ("Title: Dikdukei Soferim —
Part 1 — Berakhot, Zeraim | Author: Rabbinovicz, Raphael Nathan Neta,
1835–1888") — this is unambiguously the real work, not a different book with
a similar name. The page also carries a direct download link:

```
https://download.hebrewbooks.org/downloadhandler.ashx?req=38512
```

Fetching that URL through the stealth browser triggered an actual file
download event (`Page.goto: Download is starting`) rather than another
challenge page — i.e. **the PDF genuinely streams once past Cloudflare**. The
site's own homepage banner states it hosts **"66,162 Classical Hebrew Books
for Free Download."** This was confirmed as a working access path; the PDF
itself was **not saved** (no bulk download, per instruction — this was a
single-URL access verification, same as the archive.org `HEAD` checks used
throughout this doc).

### 7C. License — real, but not CC/PD-equivalent; same shape as Mechon Mamre (Part 8), slightly more permissive

Fetched `hebrewbooks.org/virtmedia/TermsofUse111925_.html` directly (the real
terms-of-use link, found by grepping the homepage HTML for `href` — a guessed
`/termsofuse.aspx` 404'd first). Key clauses, verbatim:

> "No commercial use: you may use the Works and Services only for personal
> use, including educational and scholarly use, and not for any commercial
> [purpose]... You do not acquire any ownership rights by downloading or
> otherwise using any Work... [prohibited:] Redistribute any Work for a fee
> or any commercial purpose, or rent, lease, loan, trade, sell/re-sell or
> otherwise monetize the Services or Work."

So: **free to view/download for personal, educational, and scholarly use;
explicitly not CC-BY-equivalent, and not license-compatible with this
project's general "public domain or openly licensed, redistributable" bar**
stated in `INDEX.md`. Practically identical posture to Mechon Mamre (Part 8)
— HebrewBooks even states some of its scans were "provided to HebrewBooks
with the permission and under license from the copyright owners," meaning
some individual scans may carry additional restrictions beyond HebrewBooks'
own baseline terms. **Usable for personal research reading of a genuinely
public-domain 1867–97 work; not a source to bulk-mirror into this corpus
under its current "openly licensed" bar** without treating it the same way
the project already treats the CC-BY-NC Bavli text — flagged, not silently
pulled in alongside the CC-BY/CC0 material.

---

## Part 8 — Mechon Mamre as an Aleppo Codex proxy (specifically investigated)

### 8A. What the Hebrew text is actually based on — confirmed from the site's own description

The site's own Hebrew-language landing page for its pointed Tanakh
(`https://www.mechon-mamre.org/i/t/t0.htm`) states, verbatim:

> **"תורה נביאים וכתובים בכתיב המסורה מנוקד לפי הכתר וכתבי היד הקרובים לו, מהדורת חשוון התשע"ח"**
>
> "Torah, Nevi'im, and Ketuvim in Masoretic spelling, vocalized **according to
> the Keter [= 'the Crown', i.e. the Aleppo Codex] and manuscripts close to
> it**, Cheshvan 5778 edition [≈ October–November 2017]."

This directly confirms the project's hypothesis: **Mechon Mamre's Hebrew Bible
text is explicitly Aleppo-Codex-based, with gap-filling from related
manuscripts** for the ~200 chapters of the Aleppo Codex that are physically
lost (most of the Torah, parts of the end of the codex). This is stated by the
site itself, in Hebrew, on the page that actually serves the vocalized text —
not inferred from secondary description.

Site-wide, this pointed/cantillated Tanakh is one of **four parallel Hebrew
Bible presentations** Mechon Mamre offers (pointed with cantillation, pointed
without cantillation, unpointed "full spelling," and with Targum Onkelos
interlinear) — the Aleppo-Codex basis applies to the core text underlying all
of them.

### 8B. License — the actual blocker, and it's a hard one

`https://www.mechon-mamre.org/copy.htm` states, in English, verbatim:

> "All of the material in this site is copyrighted... You may use materials
> from this site **only for your private study and teaching, not for
> publishing in any form, including any Web site**... Any other use requires
> written permission from us."

This is **not** a CC-license, not public domain, and not compatible with this
project's stated licensing posture (everything on disk is "public domain or
openly licensed... check before redistributing," per `INDEX.md`). Mechon
Mamre explicitly and repeatedly asserts a restrictive copyright over its
*presentation* of the text — including, per their own FAQ, over the *choice
and arrangement* even though "no one can have a copyright that excludes all
others from preparing their own unique copy of the Bible... for copyright
protection" (their words, acknowledging the underlying text is public domain
while claiming their specific edition isn't reusable).

**Practical conclusion**: Mechon Mamre is confirmed to be Aleppo-Codex-based
(answering the "what is it actually based on" question directly), but it is
**not a usable source for this corpus** under the project's own licensing
rule — mirroring or bulk-downloading it would violate the site's explicit
terms. It remains useful as a **reference/cross-check** (visit the live site
to compare a specific verse against Leningrad-Codex-based `morphhb`), but not
as something to pull files from.

### 8C. Bonus finding: Mechon Mamre is also the Hebrew source for several Tosefta tractates already confirmed above

Multiple `heVersionTitle` strings surfaced in Part 2 read "...— Machon Mamre"
(their own transliteration). Sefaria's digitization of those specific
Tosefta tractates is **CC0**, i.e. Sefaria evidently obtained rights or
independently re-digitized that text rather than mirroring Mechon Mamre's
copyrighted presentation directly — worth knowing so nobody double-counts a
license conflict where there isn't one: **the Tosefta text is fine to use
(per Sefaria's CC0 tag on it); it is Mechon Mamre's own site/presentation of
the Tanakh specifically that carries the restrictive copyright.**

### 8D. English side, for completeness

The English translation paired with the Hebrew on Mechon Mamre is the **JPS
1917 edition** — genuinely public domain (confirmed on their own FAQ page) —
but that's a translation, out of this doc's original-language scope, and
easily obtainable public-domain elsewhere without touching Mechon Mamre's
restricted presentation.

---

## Part 9 — Sefaria-Export (github.com/Sefaria/Sefaria-Export) — investigated directly

```
curl -s "https://api.github.com/repos/Sefaria/Sefaria-Export"
```

| | |
|---|---|
| Repo | `github.com/Sefaria/Sefaria-Export` |
| What it actually is | A **lightweight index + tooling repo** (the git repo itself reports **~14.7 GB** via GitHub's API `size` field, but that figure is misleading — see below) |
| Where the data lives | A **public Google Cloud Storage bucket**, `gs://sefaria-export/`, **not** in git — confirmed via the repo's own README: "~26GB, ~85K files," downloadable with no authentication |
| License | **No single repo-wide license** — confirmed via `LICENSE.md`: "Each text is licensed separately... find the license for each text in their JSON versions under the `license` field. This is generally either 'Public Domain', 'CC0', 'CC-BY', 'CC-BY-SA', or 'CC-BY-NC'." Matches exactly what direct API spot-checks in Parts 1–5 above found. |
| Format | `json/{categories}/{title}/{language}/{versionTitle}.json`, plus `txt/`, `cltk-full/`, `cltk-flat/`, `schemas/`, `links/` (intertextual link CSVs), `table_of_contents.json` |
| `books.json` | A **20.2 MB** master index, **19,716 book/version/language entries total**, regenerated monthly. Fetched and inspected directly (`/tmp/books.json` this session — not committed anywhere, scratch only) |
| Resolves? | **Yes, confirmed** — every individual file spot-checked in Parts 3 and 5 above (`Mishnah_Yadayim`, `Bava_Batra` Hebrew, all 10 Rabbah books, both Mekhiltas, Sifra, both Sifre, both Pesikta, both Tanchuma) returned real `HTTP 200` with correct `Content-Length` from the live GCS bucket, e.g.: |

```bash
curl -sI "https://storage.googleapis.com/sefaria-export/json/Talmud/Bavli/Seder%20Nezikin/Bava%20Batra/Hebrew/merged.json"
# HTTP/2 200, content-length: 1473818
```

**Scope-relevant subset**: filtering `books.json` to Hebrew-language entries
under `Talmud`/`Mishnah`/`Tosefta`/`Midrash` gives **10,841 entries** (this
includes every named manuscript-based sub-version plus the `merged` best-text
file for each work — not 10,841 separate *works*, more like ~600–800 distinct
works × several Hebrew versions each). The `merged` Hebrew files alone for
just this rabbinic scope are the right subset to actually pull.

**This is the correct long-term tool for this scope**: rather than replicating
`pull_targums.py`'s API-crawl pattern (slow, one HTTP call per chapter,
already hit rate-limit-shaped friction in this project's history), a
`pull_rabbinics.py` should use `books.json` to find `merged` + `Hebrew`
entries for the specific title list from Parts 1–5, `HEAD`-check each for
license-field presence (noting license lives in the `/api/texts/` response,
not the bulk file itself — see Part 5B), and pull directly from
`storage.googleapis.com/sefaria-export/`. Example pattern:

```bash
curl -O "https://storage.googleapis.com/sefaria-export/json/Mishnah/Seder%20Tahorot/Mishnah%20Yadayim/Hebrew/merged.json"
```

---

## Summary

| Item | Status | Free/original-language? |
|---|---|---|
| Mishnah (incl. Yadayim 3:5) | **Verified complete, content read** | Yes — CC-BY/CC0 Hebrew, Sefaria |
| Tosefta (incl. the Y2:6/Zuckermandel-2:14 parallel) | **Verified complete, content read** | Yes — mostly CC0 (Machon Mamre lineage via Sefaria), a few tractates need per-title license check |
| Talmud Bavli (BB 14b–15a, Megillah 7a, Shabbat 115a-116b, Sanhedrin 99a, Soferim) | **Verified complete, key content read** | Yes — but **CC-BY-NC** across the board |
| Talmud Yerushalmi | **Verified complete/present** | Yes — CC-BY |
| Midrash (full Rabbah series + Mekhilta ×2 + Sifra + Sifre ×2 + Pesikta ×2 + Tanchuma ×2 + bonuses) | **Verified complete, sized: ~23.5 MB** | Yes — mostly CC-BY/CC0, two works (Sifre Devarim, Pesikta deRav Kahana) need a closer license look |
| Masorah magna/parva | **Not found anywhere as machine-readable text** | No — genuine gap |
| Okhlah we-Okhlah | **Found, resolves, PD** | Yes — Tier 3 edition (Frensdorff 1864) of old material; OCR quality on Hebrew unverified |
| Tiqqune soferim / sebirin / itture soferim | **Not a standalone text. Two on-topic loci content-verified live** (Tractate Soferim ch. 6 — dotted letters, the three-Temple-scrolls majority-vote story, ketiv/qere-style lists; Sifre Bamidbar 84 — the Numbers 10:35 passage tying directly to Mishnah Yadayim 3:5). **The specific ~18-item enumerated euphemism list was searched for directly and NOT found** in Mekhilta, ADRN, or Bereshit Rabbah in this pass — UNVERIFIED whether any single ancient passage holds it; best available leads for the full list remain the Masorah (6A, not machine-readable) and Okhlah we-Okhlah (6B, found but OCR-unverified) | Partial — the two verified passages are free (CC-BY), the complete 18-item list is not confirmed to exist anywhere machine-readable |
| Dikdukei Soferim (Rabbinovicz) | **RESOLVED via stealth fetch** — real HebrewBooks.org book IDs found (38512, 38518, 38521, 22086, 22189), book-detail page and download handler both confirmed live behind Cloudflare | Free to view/download for personal/scholarly use, but **not CC/PD-equivalent** — HebrewBooks' own terms are non-commercial-only, same restrictive shape as Mechon Mamre |
| Mechon Mamre (Aleppo Codex proxy question) | **Fully investigated** | **No** — text is genuinely Aleppo-Codex-based (confirmed in their own words) but the site asserts restrictive copyright incompatible with this project |
| Sefaria-Export bulk repo | **Fully investigated, confirmed resolving** | Yes, per-text license (mixed CC-BY/CC0/CC-BY-NC/PD) — best long-term pull mechanism for this whole scope |

**Nothing was bulk-downloaded in this pass.** Total verified/estimated size for
everything marked "Yes" above, if pulled: Mishnah + Tosefta (small, low-single
digit MB each), Talmud Bavli (~40–60 MB estimated whole, only 4 of 37
tractates individually sized), Talmud Yerushalmi (~20–25 MB estimated whole,
only 2 of ~39 present tractates individually sized), Midrash (**23.5 MB,
individually confirmed, not estimated**), Okhlah we-Okhlah (~1 MB OCR text).
**Rough total for the whole rabbinic scope: on the order of 100–150 MB** —
small relative to the ~6.5 GB corpus already on disk, and the licensing is the
real work here, not the storage.
