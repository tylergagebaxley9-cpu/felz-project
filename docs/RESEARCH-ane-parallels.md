# Research: Ancient Near Eastern Background Texts

Scope: original-language (or original-language + diplomatic transliteration) texts from outside the biblical corpus that bear on reading the Hebrew Bible against its Northwest Semitic and Mesopotamian environment — Ugaritic, Akkadian, Sumerian, Egyptian, Hittite, and Old Aramaic. Triggered by a specific finding already on disk: **Deut 32:8 reads בני אלוהים ("sons of God") in the Qumran Hebrew (4QDeut^j) and ἀγγέλων θεοῦ ("angels of God") in the LXX, but בני ישראל ("sons of Israel") in the Leningrad Codex MT** — see `PROVENANCE.md`. That older reading is a fragment of a Northwest Semitic mythology in which Elyon apportions the nations among divine sons and YHWH receives Jacob as his own share. It is unintelligible without Ugaritic.

**Every URL below was checked live this pass** (curl HEAD / GitHub API / archive.org metadata API / direct fetch), on 2026-08-08, and re-verified in a second independent pass the same day (GitHub API + archive.org `/metadata/<id>` for every archive.org identifier used below, plus a link-by-link crawl of `hethport.net` past its redirect stub). The second pass **corrected §5**: the Hittite state-treaty texts were wrongly marked unavailable in the first pass because the check stopped at `hethport.net`'s bare-root redirect stub instead of following it — see the correction note in §5. Two dates are given for everything: **date of composition** (the thing itself) and **date of edition** (this particular scan/transcription/database). A 1902 transliteration of a 4th-millennium-old cuneiform text is old paper around an old text — read the composition date, not the edition date, exactly as `PROVENANCE.md` already insists for the biblical material.

**Scholarly-status labels**, per instruction, attached to every proposed parallel:
- **WIDELY ACCEPTED** — mainstream critical consensus, cited across confessional lines
- **DEBATED** — real scholars on both sides, genuine open question
- **FRINGE** — held by a minority, usually outside professional Assyriology/Egyptology/biblical studies, or an overreading of a real but much thinner parallel

Nothing here was bulk-downloaded. Commands are given at the end for the specific items worth pulling.

---

## 1. UGARITIC — El, Elyon, the divine council, the 70 sons

This is the section that actually explains Deut 32:8. Read the closing section below for the payoff.

| Item | Composed | Edition | Format | License | Size | Resolves? |
|---|---|---|---|---|---|---|
| **Copenhagen Ugaritic Corpus** (`DT-UCPH/cuc`) — Text-Fabric dataset of *Die keilalphabetischen Texte aus Ugarit* (KTU), 278 tablets | c. 1400–1200 BCE | ongoing, GitHub, latest commit `0408967` (2026-07-31) | Text-Fabric (tablet/column/line/sign-level, `g_cons` = consonantal Latin transliteration) + some plain `.txt`/`.tsv` files under `reviewed/` | **CC BY-NC 4.0** (confirmed in README, DOI 10.5281/zenodo.10695308) | ~12 KB repo metadata; corpus itself is small (text, not images) | **Yes** — `git clone`, GitHub API confirmed |
| KTU (2nd ed., Dietrich/Loretz/Sanmartín 1995) — the standard critical print edition cited by KTU-numbers | c. 1400–1200 BCE | 1995, Ugarit-Verlag | scan | **Access-restricted** (archive.org `cuneiformalphabe0008unse` is in the "printdisabled" controlled-lending collection, not freely downloadable) | 666 pp. | **No** — restricted |
| EUPT — *Edition des ugaritischen poetischen Textkorpus* (Göttingen, DFG-funded), digital critical edition w/ vocalization + morphosyntax | c. 1400–1200 BCE | ongoing, alpha, live 2026 | web edition, XML backend mentioned | **Not stated** — no license or terms page found this pass | N/A | **Yes**, resolves (https://eupt.uni-goettingen.de), but license unconfirmed — flag before reuse |
| Ras Shamra Tablet Inventory (RSTI), U. Chicago OCHRE | archaeological metadata, not text | ongoing | web tables/maps | **CC BY-NC-ND** | N/A | **Yes** (https://ochre.lib.uchicago.edu/RSTI/) — but this is a tablet **inventory/catalog**, not transliterated text; useful for provenance, not reading |
| "Ugaritic Data Bank" (Cunchillos/Vita/Zamora, Madrid CSIC, Laboratorio de Hermeneumática) | c. 1400–1200 BCE | 1999–2000s | proprietary DB, was print-published as *The Texts of the Ugaritic Data Bank* (Gorgias Press) | print edition is **commercial** | — | **No** — `labherm.filol.csic.es` (the host domain from the 1999–2000 b-hebrew mailing list era) is **dead** (connection failure, confirmed this pass) |

**The DT-UCPH/cuc repo is the one to actually use.** It is from the same lab (Text-Fabric group centered on DT-UCPH / CACCHT) that produced `samaritan/sp`, already in this corpus, so the tooling and conventions will feel familiar. Per its README, the 278 tablets available include **KTU 1.1–1.7** (the Baal Cycle — this covers **KTU 1.2**, the divine-council/Yam scene, and **KTU 1.4**, the "seventy sons of Athirat" feast), **1.14–1.19** (Kirta and Aqhat), plus the 2.x letters and 3.x legal texts. It is work in progress — not every tablet has been through the `reviewed/` pass yet, but the raw Text-Fabric data covers the range needed here.

**Deuterocanonical value note:** the Aramaic Sefire treaty (§7 below — not freely obtainable in transliteration this pass) independently invokes the divine pair **"ʾl wʿlyn"** ("El and Elyon") as treaty witnesses (Sefire I A, line 11) — a rare non-biblical, non-Ugaritic attestation that Elyon functioned as a distinct or paired divine name alongside El, strengthening (not proving) the case that Deut 32:8's אלוהים ⁄ עליון pairing draws on a real, attested West Semitic theologoumenon rather than an isolated poetic flourish.

---

## 2. MESOPOTAMIAN LITERATURE — Enuma Elish, Atrahasis, Gilgamesh XI

The clean modern digital critical editions of these three texts (eBL/Munich, ORACC literary projects) turned out to be **behind an authenticated API** or otherwise not confirmed freely bulk-reusable this pass. What *is* solidly free are the original early-20th-century philological editions — autographed cuneiform + transliteration + translation, public domain, still philologically serious (the transliterations are dated but genuine, produced by the scholars who first worked out these texts).

| Item | Composed | Edition | Format | License | Size | Resolves? |
|---|---|---|---|---|---|---|
| **L.W. King, *The Seven Tablets of Creation*** (Enūma Eliš) — vol. 1 (discussion/translation) + vol. 2 (cuneiform text/transliteration) | Old Babylonian core, Standard Babylonian recension by ~1100 BCE | **1902** | PDF + OCR `_djvu.txt` | **Public domain** | vol. 2 (text): archive.org `seventabletsofcr02kinguoft` | **Yes** — confirmed not access-restricted |
| Luckenbill, *The Ashur Version of the Seven Tablets of Creation* — supplementary fragment | same | **1921** | PDF + `_djvu.txt` | Public domain | archive.org `ashurversionofse00luck` | **Yes** |
| **SEAL** (Sources of Early Akkadian Literature, Streck/Wasserman, Leipzig + Hebrew University) — includes **Atrahasis**: 5 Old Babylonian + 9 Middle Babylonian/Assyrian witnesses; **Gilgamesh**: 13 OB + 15 MB/MA witnesses | 3rd–2nd millennium BCE compositions | ongoing digital ed. | web database, browsable, transliteration + apparatus per witness | **CC BY-NC-ND** | N/A (browse-only) | **Yes** — freely browsable, no login required |
| **R. Campbell Thompson, *The Epic of Gilgamish: Text, Transliteration and Notes*** — includes **Tablet XI** (the flood narrative, Uta-napishti) | Old Babylonian core, Standard Babylonian (Nineveh) recension ~7th c. BCE copies | **1930**, Oxford | PDF + OCR `_djvu.txt` | **Public domain** | archive.org `epicgilgamish0000rcam` | **Yes** |
| Alt. 1928 Thompson item | same | 1928 | PDF + `_djvu.txt` | Public domain | archive.org `thompson-1928-gilgamesh` | **Yes** |
| eBL (electronic Babylonian Library), Munich/BAdW — has near-complete modern critical editions of Enūma Eliš, Atrahasis via its Fragmentarium | as above | ongoing, 2018– | web app (React SPA) + REST API (`ebl-api`, MIT-licensed **code**) | **Text/data license not confirmed** — API requires an Auth0 `read:texts` scope for text content; underlying scholarly-text license is not stated in the public README | N/A | Site resolves; **bulk/API text access is gated**, not a clean open download this pass |
| ORACC `cams/gkab` (Geography of Knowledge in Assyria & Babylonia) | Assyrian/Babylonian scholarly library texts, incl. some Gilgamesh material | 2007–2014 | ORACC HTML/JSON | **CC BY-SA 3.0** | small | **Yes**, confirmed live and license-tagged — but this project is omen/scholarly-text focused, not a full Enuma Elish/Atrahasis edition |

**Recommendation:** pull King 1902 vol. 2 (Enūma Eliš) and Thompson 1930 (Gilgamesh, incl. Tablet XI) as PDFs — both small, both PD, both contain actual transliterated cuneiform. For Atrahasis, there is no PD edition (it wasn't properly reconstructed until Lambert & Millard 1965/1969, which is copyrighted, Eisenbrauns/Clarendon) — SEAL is the best free option, browse-only under CC BY-NC-ND.

---

## 3. SUMERIAN — ETCSL: Eridu Genesis (Flood Story) and the Sumerian King List

| Item | Composed | Edition | Format | License | Size | Resolves? |
|---|---|---|---|---|---|---|
| **ETCSL** (Electronic Text Corpus of Sumerian Literature), Oxford Faculty of Oriental Studies | Old Babylonian-period copies of Sumerian compositions, orig. composition often Ur III or earlier | project ran 1998–2006, site still live | HTML, per-text transliteration (`c.` prefix) and translation (`t.` prefix) via CGI query | Copyright retained by project authors (Black, Cunningham, Robson, Ebeling, Taylor, Zólyomi et al.); **no CC/open-license tag found** — citation requested, terms otherwise unstated | small (text) | **Yes** — confirmed live, both transliteration and translation pulled and verified this pass |
| — **The Flood Story ("Eridu Genesis")**, transliteration | Old Babylonian copy of an older Sumerian composition | text no. **c.1.7.4** | HTML | as above | small | **Yes** — `https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=c.1.7.4` fetched, confirmed Sumerian transliteration content (opens "approx. 36 lines missing... nam-lu2-ulu3-ju10 ha-lam-ma-bi-a...") |
| — **The Sumerian King List**, transliteration | composed/redacted early 2nd millennium BCE, describing antediluvian and post-flood dynasties | text no. **c.2.1.1** | HTML | as above | ~252 KB page | **Yes** — fetched, confirmed content ("Sumerian king list" title string present) |
| Same texts, English translation only (not original-language) | — | `t.1.7.4`, `t.2.1.1` | HTML | as above | small | **Yes**, for reference — not in scope as "original language" but useful for orientation |
| ORACC mirror `oracc.museum.upenn.edu/etcsl/` | same | mirror | — | — | — | Root page resolves (200); the numbered text-URLs tried this pass (`/etcsl/1.7.4/`, `/etcsl/2.1.1/`) **404'd** — use the Oxford CGI URLs above instead |

Note the file naming convention: **`c.` = composite transliteration text, `t.` = translation.** Both are served by the same CGI endpoint with a `text=` query parameter, e.g. `?text=c.1.7.4`.

---

## 4. EGYPTIAN — Great Hymn to the Aten, Instruction of Amenemope, Book of the Dead ch. 125

All three located as **public-domain, pre-1930 hieroglyphic-text-plus-transliteration editions** on archive.org — genuinely old philology, freely downloadable, not restricted.

| Item | Composed | Edition | Format | License | Size | Resolves? |
|---|---|---|---|---|---|---|
| **N. de G. Davies, *The Rock Tombs of El Amarna*, Part VI: Tombs of Parennefer, Tutu, and Ay** — contains the hieroglyphic **Great Hymn to the Aten**, inscribed in the tomb of Ay | reign of Akhenaten, ~1350 BCE | **1908** (Egypt Exploration Fund) | PDF + OCR `_djvu.txt`, hieroglyphic plates | **Public domain** | archive.org `archaeologicalsu0000fllg_n2o3` | **Yes** — confirmed not access-restricted |
| **E.A.W. Budge, *The Teaching of Amen-em-apt, Son of Kanekht*** — Egyptian hieroglyphic text (from Papyrus BM 10474) + English translation of the **Instruction of Amenemope** | composition variously dated late 2nd millennium – early 1st millennium BCE | **1924**, British Museum/Hodder & Stoughton | PDF + `_djvu.txt` | **Public domain** | archive.org `teachingofamenem0000eawa` | **Yes** — confirmed not access-restricted |
| **E.A.W. Budge, *The Book of the Dead: Papyrus of Ani*** — hieroglyphic text + transliteration + translation, includes **chapter 125** (the "negative confession" / weighing of the heart) | New Kingdom papyrus, ~1250 BCE | **1913/1895** (Medici Society facsimile ed. cited most; earlier 1895 ed. also PD) | PDF + `_djvu.txt` | **Public domain** | archive.org `bwb_S0-EHD-900_1` (1913) and `papyrus-of-ani-e.-a.-wallis-budge` (1895) | **Yes** — both confirmed not access-restricted |
| Thesaurus Linguae Aegyptiae (TLA, BBAW/Leipzig) — modern digital corpus, would have all three in hieroglyphic + transliteration + lemmatized form | as above | ongoing | React SPA + API | Not confirmed this pass — homepage is a JS shell, subpages tried (`/about`, `/legal`, `/data-license`) all 404'd server-side | — | Site root resolves (200); **could not confirm license or reach specific texts this pass** — flag for a dedicated follow-up with their documented API rather than URL-guessing |

---

## 5. HITTITE / AKKADIAN TREATIES — the structural template argument for Deuteronomy

This is a live, two-sided scholarly argument, not a settled parallel — see §9.

> **Correction (this verification pass, 2026-08-08):** the previous pass's verdict on the 2nd-millennium Hittite side was **wrong** — the exact "guessed filename / declared dead too fast" failure mode `PROVENANCE.md`'s method notes warn about. `hethport.net` bare-root does return a nearly empty 311-byte stub, but that stub is a `<meta refresh>` redirect to `hethport.net/HPM/index.php`, which is a fully live, actively maintained site (Hethitologie-Portal Mainz / Akademie der Wissenschaften Mainz). Checked live this pass: the CTH catalog (`../CTH/`) and tablet concordance (`hetkonk_abfrage.php?c=<CTHnum>`) both work and return real scholarly content (manuscript inventory numbers, findspots, join history, full bibliography). More importantly, the concordance pages for **CTH 51** (Šuppiluliuma I–Šattiwaza) and **CTH 62** (Muršili II–Duppi-Teššub) each link out to a live sub-project, `txhet_svh` ("Staatsverträge der Hethiter," ed. G. Wilhelm / Wilhelm–Fuscagni), which serves a **full manuscript-by-manuscript transliteration** of the actual treaty text — verified by fetching `txhet_svh/exemplar.php?xst=CTH 51.I&expl=A&lg=DE&ed=G. Wilhelm` and confirming genuine Akkadian cuneiform transliteration in the middle of the page (§-numbered, e.g. `D UTU-ši Šuppiluliuma LUGAL GAL LUGAL KUR URU Ḫatti ... na-ra-am D U`, with manuscript witness sigla `A1 Vs. 11` etc.) — this is the historical-prologue section of the actual Šuppiluliuma–Šattiwaza treaty, not a summary.

| Item | Composed | Edition | Format | License | Size | Resolves? |
|---|---|---|---|---|---|---|
| **SAAo/SAA02** (State Archives of Assyria online, vol. 2: *Neo-Assyrian Treaties and Loyalty Oaths*, ed. Parpola & Watanabe) — includes **Esarhaddon's Succession Treaty** (the "Vassal Treaties of Esarhaddon," VTE), **Esarhaddon's Treaty with Baal of Tyre**, and others | 672 BCE (VTE) and other 8th–7th c. BCE Neo-Assyrian treaties | ORACC ed., 2014– | ORACC HTML/JSON, transliteration + translation + lemmatization | **CC BY-SA 3.0** (confirmed) | small | **Yes** — confirmed live, confirmed license, confirmed table of contents lists "Esarhaddon's Succession Treaty," "Esarhaddon's Treaty with Baal, King of Tyre," "Vassal Treaty..." |
| **Hethitologie-Portal Mainz (HPM), `txhet_svh` project** — digital edition of Hittite state treaties, ed. G. Wilhelm (CTH 51) / Wilhelm–Fuscagni (CTH 62), incl. **Šuppiluliuma I–Šattiwaza of Mittani** (CTH 51, 9 manuscript witnesses A–C) and **Muršili II–Duppi-Teššub of Amurru** (CTH 62, 6 witnesses) — the core texts Mendenhall's original 1954 argument was built on | 14th–13th c. BCE | edition pages dated 2016– (introductio pages carry per-text dates, e.g. "INTR 2016-01-10"), actively maintained | PHP-served HTML, manuscript-by-manuscript transliteration (`exemplar.php`) with tabs for images/partitura/exemplar/translation | Site footer carries a **CC BY-SA 4.0** badge (confirmed present on the CTH concordance pages, `creativecommons.org/licenses/by-sa/4.0`); not independently re-stated on the `txhet_svh` edition subpages themselves — treat as very likely covered by the same site-wide license but flag that specific point as unconfirmed | edition page for CTH 51 exemplar A ≈ 290 KB HTML (incl. nav/CSS chrome; the transliteration itself is a fraction of that) | **Yes** — confirmed live, confirmed real transliteration content fetched and read mid-page, for CTH 51 and CTH 62. Access path: CTH catalog → `hetkonk_abfrage.php?c=<n>` concordance → its `hethiter.net/:CTH <n>` citation link → `rd.php` redirect → `txhet_svh/intro.php` → `exemplar.php?xst=...&expl=<A/B/C...>` |
| **Ḫattušili III–Ramesses II** (the Egyptian-Hittite peace treaty, CTH 91) | 13th c. BCE (c. 1259 BCE) | — | — | — | — | **Cataloged but not yet a `txhet_svh` edition.** The CTH 91 concordance page is live (3 fragments, full bibliography incl. Beckman, Kitchen-Lawrence 2012, Devecchi 2015) but — unlike CTH 51/62 — carries **no** outbound `hethiter.net` edition link, so no free transliteration was found for this specific treaty this pass. The Egyptian hieroglyphic side (Karnak/Ramesseum) is separately covered by Egyptological sources not checked in this pass. |
| KTU (2nd ed.) print edition and superseded standard print apparatus, KAI (Donner & Röllig, *Kanaanäische und Aramäische Inschriften*) — publishes some treaty/inscription texts | various | 1962–64, Harrassowitz | print | **Copyrighted**, no free digital edition located | — | — |
| TITUS's Hittite corpus page | — | — | — | — | — | The main text corpus page tried this pass (`hitthome.htm`, `didact/idg/anatol/hettext.htm`) both returned "the requested page is not (yet) available" — effectively dead/stub, not usable as a source. Not needed anyway now that HPM's own `txhet_svh` is confirmed live. |

**Corrected bottom line for this section:** the Neo-Assyrian side (VTE) is solidly available, free, and license-clean via ORACC SAA02. The 2nd-millennium Hittite side — which matters for the dating argument (see §9) — **is** freely available in real transliteration for two of the three treaties Mendenhall's argument rests on (Šuppiluliuma–Šattiwaza, Muršili–Duppi-Teššub), via HPM's `txhet_svh` project; only the third (Ḫattušili–Ramesses) is catalog-only there. This reverses the previous pass's "not confirmed / appears down" verdict — the earlier check evidently stopped at the bare `hethport.net` root's near-empty redirect stub without following it.

---

## 6. CODE OF HAMMURABI

| Item | Composed | Edition | Format | License | Size | Resolves? |
|---|---|---|---|---|---|---|
| **R.F. Harper, *The Code of Hammurabi, King of Babylon, about 2250 B.C.*** — autographed cuneiform text, transliteration, translation, glossary, sign list | c. 1750 BCE (Hammurabi's reign) | **1904**, University of Chicago Press | PDF + OCR `_djvu.txt` | **Public domain** | archive.org `codeofhammurabik00harpuoft` | **Yes** — confirmed not access-restricted |
| Martha Roth, *Law Collections from Mesopotamia and Asia Minor* — the modern critical standard | same | 1995/1997, SBL | — | **Copyrighted** | — | Not free — noted for completeness, matches the project's existing NA28/BHS-style exclusion pattern |

Harper 1904 is old (translation conventions and some readings are dated by 120 years of subsequent scholarship) but it is a real transliteration of the actual Louvre stele text (Susa, Sb 8), not a paraphrase, and it is unambiguously public domain.

---

## 7. ARAMAIC — Sefire treaties and the Deir ʿAlla plaster inscription (Balaam)

**Neither is freely available in transliteration this pass.** Documented honestly rather than papered over:

| Item | Composed | Edition | Status |
|---|---|---|---|
| **Sefire treaty inscriptions** (KAI 222–224; three stelae, Bar-Gaʾyah of KTK and Matiʿʾel of Arpad) | c. 754–740 BCE | standard edition: J.A. Fitzmyer, *The Aramaic Inscriptions of Sefire* (rev. ed. 1995, Biblical Institute Press) | **Copyrighted**, no free digital transliteration located |
| **Deir ʿAlla plaster inscription** ("Balaam son of Beʿor," combination I & II) | c. 800–700 BCE (paleography); found 1967, Jordan | standard edition: J. Hoftijzer & G. van der Kooij, *Aramaic Texts from Deir ʿAlla* (1976, Brill) | **Copyrighted**, no free digital transliteration located |
| **CAL** (Comprehensive Aramaic Lexicon, Hebrew Union College, dir. Stephen Kaufman) — does include Old Aramaic material covering this period and dialect group | — | ongoing digital lexicon/corpus | Site is live and browsable (`cal.huc.edu`), but its own homepage explicitly states: *"Please do not try to scrape our site. We are always happy to provide legitimate academic users with relevant dumps of our data"* (contact: skaufman@huc.edu). Per that notice, **this pass did not scrape it** — individual lookups are fine via their search interface; a bulk pull requires directly contacting the maintainer, which is outside the scope of an automated fetch. |

Both texts matter for the same dossier as Deut 32:8: Sefire I A independently pairs **"ʾl wʿlyn"** (El and Elyon) as treaty-witness deities (see §1), and the Deir ʿAlla text names "Balaam son of Beʿor, a seer of the gods" (blʿm brbʿr ʾš ḥzh ʾlhn) receiving a night vision from "the gods" ('lhn) — an extra-biblical, non-Israelite attestation of the same seer named in Numbers 22–24, using the same plural-god vocabulary (ʾlhn) that Deut 32:8's בני אלהים draws on. Worth pursuing a dedicated follow-up pass on both, ideally via WSRP/InscriptiFact (usc.edu) for images and a direct CAL data-dump request for text.

---

## 8. Suggested fetch commands (small items only)

```bash
# Ugaritic — Copenhagen Ugaritic Corpus (Text-Fabric), CC BY-NC 4.0, 278 KTU tablets incl. Baal Cycle
git clone --depth 1 https://github.com/DT-UCPH/cuc.git

# Enuma Elish — King 1902, vol. 2 (cuneiform text + transliteration), PD
wget https://archive.org/download/seventabletsofcr02kinguoft/seventabletsofcr02kinguoft.pdf
wget https://archive.org/download/seventabletsofcr02kinguoft/seventabletsofcr02kinguoft_djvu.txt

# Gilgamesh (incl. Tablet XI, the flood) — Thompson 1930, PD
wget https://archive.org/download/epicgilgamish0000rcam/epicgilgamish0000rcam.pdf
wget https://archive.org/download/epicgilgamish0000rcam/epicgilgamish0000rcam_djvu.txt

# Great Hymn to the Aten — Davies, Rock Tombs of El Amarna VI (1908), PD
wget https://archive.org/download/archaeologicalsu0000fllg_n2o3/archaeologicalsu0000fllg_n2o3.pdf

# Instruction of Amenemope — Budge 1924, PD
wget https://archive.org/download/teachingofamenem0000eawa/teachingofamenem0000eawa.pdf

# Book of the Dead, Papyrus of Ani (incl. ch. 125) — Budge 1913, PD
wget https://archive.org/download/bwb_S0-EHD-900_1/bwb_S0-EHD-900_1.pdf

# Code of Hammurabi — Harper 1904, autographed text + transliteration, PD
wget https://archive.org/download/codeofhammurabik00harpuoft/codeofhammurabik00harpuoft.pdf
wget https://archive.org/download/codeofhammurabik00harpuoft/codeofhammurabik00harpuoft_djvu.txt

# Sumerian — ETCSL, fetch individual transliterations by text number (c.=transliteration, t.=translation)
curl -sk "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=c.1.7.4" -o eridu-genesis-translit.html   # Flood Story
curl -sk "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=c.2.1.1" -o sumerian-king-list-translit.html

# Neo-Assyrian treaties (VTE etc.) — ORACC SAA02, CC BY-SA 3.0, browse/scrape per ORACC's normal terms
# (browse at https://oracc.museum.upenn.edu/saao/saa02/corpus ; bulk JSON at build-oracc.museum.upenn.edu per project)

# Hittite state treaties — HPM txhet_svh digital edition, CC BY-SA 4.0 (site-wide badge; not restated per-page)
# Suppiluliuma I - Sattiwaza of Mittani (CTH 51), manuscripts A/B/C:
curl -sk -G "https://hethport.net/txhet_svh/exemplar.php" --data-urlencode "xst=CTH 51.I" --data-urlencode "expl=A" --data-urlencode "lg=DE" --data-urlencode "ed=G. Wilhelm" -o cth51-suppiluliuma-sattiwaza-exemplarA.html
curl -sk -G "https://hethport.net/txhet_svh/exemplar.php" --data-urlencode "xst=CTH 51.I" --data-urlencode "expl=B" --data-urlencode "lg=DE" --data-urlencode "ed=G. Wilhelm" -o cth51-suppiluliuma-sattiwaza-exemplarB.html
curl -sk -G "https://hethport.net/txhet_svh/exemplar.php" --data-urlencode "xst=CTH 51.I" --data-urlencode "expl=C" --data-urlencode "lg=DE" --data-urlencode "ed=G. Wilhelm" -o cth51-suppiluliuma-sattiwaza-exemplarC.html
# Mursili II - Duppi-Tessub of Amurru (CTH 62) — start at the intro page and read exemplar links from there:
curl -sk -G "https://hethport.net/txhet_svh/intro.php" --data-urlencode "xst=CTH 62" --data-urlencode "lg=DE" --data-urlencode "ed=G. Wilhelm – F. Fuscagni" -o cth62-mursili-duppitessub-intro.html
```

Nothing above exceeds a few hundred MB; most are single-digit-to-double-digit MB PDFs. No polyglot-scale downloads in this batch.

---

## 9. Scholarly status of each proposed parallel

| Parallel | Status | Who holds what |
|---|---|---|
| **Deut 32:8's בני אלוהים (DSS/LXX) vs. בני ישראל (MT), read against Ugaritic El/Elyon and the divine council** | **WIDELY ACCEPTED** as the correct original reading and as depending on real West Semitic divine-council theology | Now the majority critical position (reflected in NRSV, NJPS, ESV footnote, NIV footnote); championed by Mark S. Smith, Michael Heiser, P. Kyle McCarter, and the DSS editors themselves (Skehan first flagged 4QDeut^j). A minority of harmonizing/confessional commentators still defend MT's בני ישראל as original or as a legitimate theological correction rather than a scribal alteration — that is a live but minority position, not a fringe one. |
| **Instruction of Amenemope ↔ Proverbs 22:17–24:22** | **WIDELY ACCEPTED** genuine literary relationship | Near-consensus since Adolf Erman identified the parallel in 1924, strengthened by close structural correspondence (Prov 22:20's "thirty sayings" matching Amenemope's 30 chapters). Direction of dependence (Egypt→Israel) is the majority view; a minority (mostly older, e.g. some pre-1980s conservative scholars) argued for a common source or reverse direction — that debate is largely settled toward Egyptian priority now. |
| **Deir ʿAlla "Balaam son of Beʿor" ↔ Numbers 22–24's Balaam** | **WIDELY ACCEPTED** as the same tradition-figure | Near-unanimous since the 1967 discovery; one of the least disputed extrabiblical confirmations of a named biblical figure's independent circulation. Debate is confined to literary-critical questions (how the biblical and Transjordanian traditions relate), not to the identification itself. |
| **Atrahasis / Gilgamesh XI ↔ Genesis 6–9 flood narrative** | **WIDELY ACCEPTED** that there is a genetic literary/traditional relationship | Consensus since George Smith's 1872 announcement that *some* relationship exists (shared ANE flood-tradition stream); genuinely debated is the *mode* — direct textual borrowing vs. common oral/written tradition-stream vs. mediated transmission (e.g., via Northwest Semitic intermediaries). A minority (some evangelical scholars) argue for independent historical memory rather than literary dependence; that is a debated, not fringe, position within the guild, though a minority one. |
| **Enuma Elish ↔ Genesis 1** (Tiamat/tehom, "Chaoskampf") | **DEBATED** | Once near-consensus following Gunkel (*Schöpfung und Chaos*, 1895) and the "Babel-Bibel" debates; now genuinely contested. The philological link Tiamat↔tehom is now widely regarded as weaker than once claimed (tehom is not a loanword from Tiamat; both derive independently from a common Semitic root). Structural/thematic parallels (primordial waters, divine speech/ordering) are still cited by many (e.g., in the Chaoskampf tradition broadly), but direct dependence of Genesis 1 specifically on Enuma Elish specifically is a minority position today; more scholars favor a shared ANE cosmological idiom mediated through Canaanite tradition rather than direct Babylonian borrowing. |
| **Great Hymn to the Aten ↔ Psalm 104** | **DEBATED** | Proposed since J.H. Breasted (early 20th c.); still widely cited as at minimum a plausible influence or shared genre. The ~600–700 year gap between Akhenaten (c. 1350 BCE) and Psalm 104's probable composition, plus Akhenaten's cult being actively suppressed after his death, makes *direct* transmission hard to establish — many now favor mediation through a broader Levantine solar-hymn tradition (attested at Ugarit and elsewhere) rather than a direct Egypt→Israel line. |
| **Hittite/Neo-Assyrian suzerainty treaty form ↔ Deuteronomy's covenant structure** (preamble, historical prologue, stipulations, deposit/reading clause, witnesses, blessings/curses) | **WIDELY ACCEPTED** that Deuteronomy is *shaped by* ANE treaty form in general; **DEBATED, with dating consequences,** which treaty tradition specifically | Mendenhall (1954) and later Kline argued the match is closest to **2nd-millennium Hittite** treaties, which — if right — supports an early (Mosaic-era, 2nd millennium) compositional core for Deuteronomy; this is still actively defended (K.A. Kitchen, Kenneth Kitchen's *On the Reliability of the Old Testament*). Levinson, Otto, and Steymans instead argue Deuteronomy (esp. chs. 13 and 28's curse sequence) shows specific, close verbal dependence on the **7th-century Neo-Assyrian VTE (Esarhaddon)** — which, if right, supports a late/Josianic-era compositional layer. Both camps are serious, current, peer-reviewed positions; this is not settled. Both sides of the primary-text comparison are now confirmed freely readable (§5): VTE via ORACC SAA02, and Šuppiluliuma–Šattiwaza / Muršili–Duppi-Teššub via HPM's `txhet_svh`. |
| **Code of Hammurabi ↔ the Covenant Code (Exod 21–23)** | **General ANE legal-genre relationship: WIDELY ACCEPTED.** **Specific direct literary dependence: DEBATED**, with one influential recent thesis pushing further than consensus | The general observation (shared casuistic law form, shared case topics like the goring ox, negligence liability) has been standard comparative-law scholarship since Hammurabi's 1901–02 discovery. David P. Wright's 2009 monograph (*Inventing God's Law*) argued for close, structured, sequential literary dependence of the Covenant Code specifically on Hammurabi's text — a stronger and more specific claim than the field's prior consensus, and it remains contested (reviewed both favorably and skeptically); treat Wright's specific thesis as a debated minority position, distinct from the well-established general parallel. |
| **Sumerian King List's antediluvian long-reigning kings ↔ Genesis 5's long-lived patriarchs; both structured around a flood** | **DEBATED** | The formal parallel (long pre-flood lifespans, a structured list, a flood as hinge point) is widely noted and considered non-coincidental at the level of shared ANE tradition; direct literary dependence of Genesis 5 on the Sumerian King List specifically is not demonstrable and not the mainstream claim — most treat both as independent developments within a common ANE "great antiquity of origins" convention rather than one copying the other. |
| **Book of the Dead ch. 125 (negative confession) ↔ biblical ethical/legal enumerations** (Decalogue, Ezek 18, Job 31) | **FRINGE as a "parallel," legitimate as a comparative-religion observation** | This is regularly mentioned in introductory textbooks as an analogy (a structured list of denied wrongdoings before divine judgment), but no serious scholar argues literary dependence — the genre similarity (an oath-of-innocence / negative-confession form) is attested independently across the ANE (cf. also Job 31 taken alone). Treat as background texture, not a parallel in the same evidentiary class as Amenemope/Proverbs or Deut 32:8/Ugaritic. |

---

## 10. What the Ugaritic material actually says about El, Elyon, and the divine council (for Deut 32:8)

Drawing on the KTU 1.1–1.7 range confirmed present in `DT-UCPH/cuc` (§1):

- **El** is the aged, presiding high god of the Ugaritic pantheon — "Bull El" (*ṯr il*), "father of years" (*ab šnm*), "creator of creatures" (*bny bnwt*). He does not fight the way Baal does; he **presides**. In KTU 1.2 (the Baal–Yam cycle), when Yam's messengers arrive, the scene plays out in El's divine council/assembly — El is the one addressed, the one whose authority the other gods operate under, even as Baal is the active combatant.
- **The divine council itself** is a real, named institution in these texts — *puḫru ʿilīma* / *puḫru moʿdi* ("assembly of El," "assembled council") — a court of subordinate gods around El, structurally identical in shape to what Deut 32:8's older reading assumes: a high god presiding over a body of lesser divine beings who are assigned to their own domains.
- **The "seventy sons of Athirat"** (*šbʿm bn aṯrt*), named explicitly in KTU 1.4 (the tablet describing a feast Baal holds for them), are El's sons by his consort Athirat — the full membership of that council, given as a fixed, formulaic number: **seventy**. This is the direct structural analogue to the "sons of God"/"sons of Elyon" of Deut 32:8, and its number (70) is very likely the same number underlying the "seventy nations" tradition in Genesis 10's Table of Nations and later rabbinic literature about seventy guardian angels/princes set over the seventy nations of the earth.
- **What the Ugaritic texts do *not* give you is an exact Vorlage.** No surviving Ugaritic tablet says, in so many words, "Elyon divided the nations among the seventy sons and gave [X] to [Y] as his portion" — that specific narrative move is the Hebrew poem's own composition. What Ugarit supplies is the **theological grammar** that makes the line legible at all: a high god (El, called *ʿly* / functionally paralleled by the separate-but-related epithet "Elyon" attested independently in the Aramaic Sefire treaty, §1 and §7) who is father and president of a council of divine sons, a fixed traditional headcount for that council (70), and a live, unremarkable Northwest Semitic assumption that such sons administer or are allotted spheres of the cosmos. Deut 32:8–9 (in its DSS/LXX form) takes that grammar and does something pointed with it: Elyon assigns the nations to the *benei elohim*, and YHWH is not the president of the council receiving the whole world by default — YHWH is *one of the allotted sons*, whose portion, singled out, is Jacob. The MT's later בני ישראל reading erases the polytheistic scaffolding by making Israel itself the numerical basis for the division rather than the divine sons — which is exactly the kind of theologically motivated scribal smoothing PROVENANCE.md's disagreement-reading rubric predicts for an "ORIGINAL vs. TRANSLATION/ORIGINAL" case once a second witness (here, DSS) turns up independently agreeing with the LXX.
