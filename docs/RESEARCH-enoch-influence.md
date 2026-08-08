# 1 Enoch's footprint in the New Testament and early Christianity

Compiled 2026-08-08. Every quotation below was pulled live from files on this
disk at the paths given — nothing is quoted from memory. Method: distinguish
**(a) direct quotation** (the NT author is demonstrably reproducing Enochic
wording), **(b) clear allusion** (specific enough content/vocabulary overlap
that dependence is the best explanation), and **(c) shared apocalyptic
milieu** (same imagery pool, no demonstrable literary dependence). Category
(c) is not inflated into (a) or (b) anywhere below.

Already established and not re-derived here: **Jude 14–15 quotes 1 Enoch 1:9
as prophecy** (Ἐπροφήτευσεν), confirmed phrase-by-phrase against the Ge'ez.
This document maps everything else.

---

## 0. Sources on disk and how they were read

- **1 Enoch, complete Ge'ez text + English**: `ethiopic/ethiopian-bible/public/data/chapters/1En/<ch>.json`. English translation is **R.H. Charles, 1917** (public domain) per `ethiopic/ethiopian-bible/README.md`; Ge'ez itself from Beta Masaheft (Hamburg), CC BY-SA. **TRANSLATION** provenance — the Ge'ez is a 4th–6th century CE translation out of Greek (per `PROVENANCE.md`), not the Aramaic original.
- **Jubilees**: same reader, `.../Jub/<ch>.json`. English = R.H. Charles, 1902.
- **Qumran Aramaic Enoch**: `dead-sea-scrolls/etcbc-dss/tf/2.0/` (Text-Fabric plain-text format), Martin Abegg's transcription. **ORIGINAL** — actual 2nd/1st-century BCE ink (see §2 for how this was extracted; the shipped `tools/dssread.py` cannot reach these because it keys on `book`/`chapter`/`verse` tags that only exist for canonical MT books — the Enoch scrolls carry none, so a custom extraction via `scroll` → `oslots` → `full` was built for this task, described below).
- **Greek NT**: `greek-nt/Nestle1904/xml/*.xml`, OSIS `osisId="Book.Ch.Vs!word"`. **EDITED**, 1904.
- **Barnabas** (Greek): `apostolic-fathers/First1KGreek/data/tlg1216/tlg001/tlg1216.tlg001.opp-grc1.xml`
- **Eusebius, HE**: `apostolic-fathers/First1KGreek/data/tlg2018/tlg002/tlg2018.tlg002.1st1K-grc1.xml`, searched with NFD-normalize + combining-mark strip as instructed (accented Greek does not grep directly).
- **Genesis 6**: `tools/allwitness.py Gen 6 <verse>` (MT + LXX; no DSS witness exists for Gen 6:1–4 in this corpus's Text-Fabric build — checked and confirmed absent, see §1).
- **Tertullian, Augustine, Jerome**: searched exhaustively (`grep -ril` across the whole corpus). **Not on disk.** The only hits are incidental name-mentions inside 17th–19th-century polyglot front matter (Walton, Tischendorf apparatus), not their actual texts. Per this corpus's Data Integrity rule, their positions are reported below from established secondary scholarship *and flagged as such*, not quoted as primary text, because they cannot be verified against a file on this disk.

---

## 1. The Watchers, Genesis 6:1–4, and the two 2nd-Temple angel-passages

### Genesis 6:1–4, every witness on disk

```
./tools/allwitness.py Gen 6 1 / 2 / 4
```

**MT (Leningrad, 1008 CE):**
> 6:1 וַֽיְהִי֙ כִּֽי־הֵחֵ֣ל הָֽאָדָ֔ם לָרֹ֖ב עַל־פְּנֵ֣י הָֽאֲדָמָ֑ה וּבָנ֖וֹת יֻלְּד֥וּ לָהֶֽם׃
> 6:2 וַיִּרְא֤וּ בְנֵי־הָֽאֱלֹהִים֙ אֶת־בְּנ֣וֹת הָֽאָדָ֔ם כִּ֥י טֹבֹ֖ת הֵ֑נָּה וַיִּקְח֤וּ לָהֶם֙ נָשִׁ֔ים מִכֹּ֖ל אֲשֶׁ֥ר בָּחָֽרוּ׃
> 6:4 הַנְּפִלִ֞ים הָי֣וּ בָאָ֮רֶץ֮ בַּיָּמִ֣ים הָהֵם֒ ... הֵ֧מָּה הַגִּבֹּרִ֛ים אֲשֶׁ֥ר מֵעוֹלָ֖ם אַנְשֵׁ֥י הַשֵּֽׁם׃

"בְנֵי הָאֱלֹהִים" — **sons of God** — plainly. The Nephilim are called "the גִּבֹּרִים [gibborim, mighty ones], men of renown."

**LXX (Rahlfs, translated c. 250–100 BCE):**
> 6:2 οἱ **υἱοὶ τοῦ θεοῦ** τὰς θυγατέρας τῶν ἀνθρώπων ... ἔλαβον ἑαυτοῖς γυναῖκας
> 6:4 οἱ δὲ **γίγαντες** ἦσαν ἐπὶ τῆς γῆς ... οἱ γίγαντες οἱ ἀπ᾿ αἰῶνος, οἱ ἄνθρωποι οἱ ὀνομαστοί

LXX renders בְנֵי הָאֱלֹהִים literally, "sons of God" (υἱοὶ τοῦ θεοῦ), and translates נְּפִלִים as γίγαντες, **giants** — the same word later used for Enoch's giant offspring of the Watchers. **MT and LXX agree** here (this is not a Deut 32:8-style variant); both preserve the "sons of God" reading undisturbed.

No Dead Sea Scroll witness for Gen 6:1–4 exists in this corpus's DSS build — checked directly; `allwitness.py` reports nothing for it and a manual scan of the DSS `book`/`chapter`/`verse` features for Genesis found no coverage of chapter 6. This is a real gap in what survived/was digitized, not evidence either way.

### 1 Enoch's expansion (Book of Watchers, chs. 6–16)

Genesis gives four verses and no explanation of *why* this happened or what became of it. 1 Enoch supplies a full narrative — named ringleaders, an oath, teaching of forbidden arts, monstrous offspring, and God's judicial response:

> **1 En 6:1–2** (`.../1En/6.json`) — "And it came to pass when the children of men had multiplied that in those days were born unto them beautiful and comely daughters. And the angels, the children of the heaven, saw and lusted after them..."
>
> **1 En 6:6** — "they were in all two hundred; who descended in the days of Jared on the summit of Mount Hermon"
>
> **1 En 7:2** — "they bare great giants, whose height was three thousand ells"
>
> **1 En 10:4, 11–13** — "And again the Lord said to Raphael: 'Bind Azâzêl hand and foot, and cast him into the darkness... And the Lord said unto Michael: Go, bind Semjâzâ and his associates... bind them fast for **seventy generations** in the valleys of the earth, till the day of their judgement... In those days they shall be led off to **the abyss of fire**: and to the torment and the prison in which they shall be confined for ever.'"

This is the Watchers story in full: named leader (Semjâzâ/Shemihazah), an angel bound "hand and foot" and cast into darkness pending final judgment, a *fixed but enormous term* of imprisonment ("seventy generations"), and an "abyss."

### 2 Peter 2:4 and Jude 6 — direct dependence on this specific narrative (allusion, arguably closer)

**2 Peter 2:4** (`greek-nt/Nestle1904/xml/22-2peter.xml`):
> εἰ γὰρ ὁ Θεὸς ἀγγέλων ἁμαρτησάντων οὐκ ἐφείσατο ἀλλὰ **σειροῖς ζόφου ταρταρώσας** παρέδωκεν εἰς κρίσιν τηρουμένους
> *"For if God did not spare the angels who sinned, but cast them into Tartarus (ταρταρώσας — a hapax legomenon in the whole Greek Bible, borrowed from the pagan underworld term Τάρταρος) with chains/pits of gloom, committing them to be kept for judgment..."*

**Jude 6:**
> ἀγγέλους τε τοὺς μὴ τηρήσαντας τὴν ἑαυτῶν ἀρχὴν ἀλλὰ ἀπολιπόντας τὸ ἴδιον οἰκητήριον εἰς κρίσιν μεγάλης ἡμέρας **δεσμοῖς ἀϊδίοις ὑπὸ ζόφον τετήρηκεν**
> *"And the angels who did not keep their own domain, but abandoned their proper dwelling, He has kept in eternal bonds under gloom for the judgment of the great day"*

Neither verse is a *quotation* of 1 Enoch — no shared vocabulary chain the way Jude 14–15 has. But the plot points are the specific, non-biblical elaborations found only in 1 Enoch 6–16, not in Genesis: angels who "did not keep" their proper place/dwelling (ἀρχή, οἰκητήριον — matches 1 En's angels leaving heaven for earth), bound (δεσμοῖς / cf. Enoch's "bind... hand and foot"), in darkness (ζόφος / cf. "cast him into the darkness"), **reserved for a future day of judgment** rather than punished immediately (τηρουμένους, τετήρηκεν / cf. "confined... till the day of their judgement"). This is category **(b) clear allusion to the Enochic elaboration of Genesis 6**, not a Genesis-only reading — Genesis never says the "sons of God" were imprisoned pending judgment; that detail is 1 Enoch's.

### 1 Peter 3:19–20 — same episode, different angle

> **1 Pet 3:19–20**: ἐν ᾧ καὶ τοῖς ἐν φυλακῇ πνεύμασιν πορευθεὶς ἐκήρυξεν, ἀπειθήσασίν ποτε ὅτε ἀπεξεδέχετο ἡ τοῦ Θεοῦ μακροθυμία ἐν ἡμέραις Νῶε
> *"...he went and made proclamation to the spirits now in prison, who once were disobedient, when the patience of God kept waiting in the days of Noah..."*

"Spirits in prison" (πνεύμασιν... ἐν φυλακῇ) tied explicitly to "the days of Noah" is the Watchers episode's aftermath as 1 Enoch tells it: **1 En 15:8–12** describes the giants' offspring becoming disembodied "**evil spirits**... upon the earth" after the Flood destroys their bodies, and **1 En 10:11–13** describes the Watchers themselves confined ("bind them fast... in the prison"). 1 Peter does not name Enoch and the theology (Christ preaching to them) is not in Enoch at all — this is **(b) allusion to the narrative frame**, with 1 Peter doing independent theological work on top of it.

### Matthew 22:30 — a quiet counter-echo, not a citation

> ἐν γὰρ τῇ ἀναστάσει οὔτε γαμοῦσιν οὔτε γαμίζονται, ἀλλ᾿ ὡς ἄγγελοι ἐν τῷ οὐρανῷ εἰσιν
> *"for in the resurrection they neither marry nor are given in marriage, but are like angels in heaven"*

This is Jesus refuting the Sadducees on resurrection, not discussing the Watchers. But the *premise it assumes* — that angels do not, by nature, marry/procreate — is precisely what makes the Watchers' sin transgressive in 1 Enoch 15:3–7 ("Wherefore have ye left the high, holy, and eternal heaven, and lain with women... though ye were holy, spiritual, living the eternal life, you have defiled yourselves with the blood of women"). Category **(c) shared premise**, not dependence — the "angels don't marry" idea could stand on its own without Enoch. Flagged because it is frequently over-claimed as a "quote"; it is not.

### 1 Corinthians 11:10 — "because of the angels," genuinely contested

> διὰ τοῦτο ὀφείλει ἡ γυνὴ ἐξουσίαν ἔχειν ἐπὶ τῆς κεφαλῆς **διὰ τοὺς ἀγγέλους**

Paul gives no explanation of which angels or why. Since antiquity (this reading is associated with **Tertullian**, *On the Veiling of Virgins* — not verifiable on this disk, see §0) some have connected this to 1 En 6–8's angels desiring women "because they were beautiful," reading Paul's veil requirement as a prophylactic against a repeat of Genesis 6/1 Enoch 6. This is **genuinely disputed** among modern scholars (proponents include some readings following Fitzmyer; many commentators reject it as speculative given Paul gives zero explanatory apparatus). Category **(c) at best** — the text does not license more.

### 2 Corinthians 11:14 — "angel of light," not Enochic

> αὐτὸς γὰρ ὁ Σατανᾶς μετασχηματίζεται εἰς ἄγγελον φωτός

This has no correspondence in the Watchers material (which is about lust and forbidden knowledge, not disguise/deception). Included per the task list but the honest finding is: **no Enochic connection found**. This is ordinary early-Jewish Satan-tradition, not Enoch-specific.

---

## 2. Qumran Aramaic Enoch — extracting it, and what it shows for Jude 14–15

**The extraction problem.** `tools/dssread.py` looks up passages by matching `book`/`chapter`/`verse` word-features. Checked directly: those three features are populated only for canonical MT books (confirmed — zero of the 11,181 Enoch words carry any `book` tag). The Enoch scrolls (4Q201–4Q212) are tagged only at the **fragment/line** level with a `scroll` feature (e.g. `4Q201`), not per-word, and are connected to their words only through `oslots.tf`, an edge feature. A custom script was built for this task:
1. Load `scroll` restricted to the `line` node range (`1552973–1605867`) → all lines belonging to `4Q201`…`4Q212`. **869 lines found across the twelve manuscripts** (per-scroll: 4Q201=93, 4Q202=55, 4Q203=81, 4Q204=126, 4Q205=31, 4Q206=86, 4Q207=6, 4Q208=124, 4Q209=171, 4Q210=25, 4Q211=16, 4Q212=55).
2. Resolve each target line's slot-range via `oslots.tf` (values like `1044-1045` are the node's **slot range**, not a node-range-with-shared-value — confirmed by checking for the tab character, which only appears on genuine node-range lines; oslots continuation lines have no tab).
3. Stream `oslots.tf` again for the `word` node range, and containment-match each word's slot range against the sorted line ranges. **11,181 words matched.**
4. Pull `full.tf` (Unicode transcription) per matched word, grouped by line, in node order.

All twelve Enoch manuscripts from Cave 4 are physically present in this corpus's Text-Fabric build. Content-matching the surviving Aramaic against Charles's English (the only available bridge, since these fragments carry no chapter/verse tags in the dataset) shows 4Q201 covers roughly 1 En 1:1 through the Watchers narrative into ch. 10 (its line at node `1559620` reads "ל רפאל אמר אזל נא רפאל ו אסר ל עסאל ידין ו רגלין" — "to Raphael he said: Go now, Raphael, and bind Asael hand and foot," matching **1 En 10:4** almost word for word), and 4Q204 covers material including **1 En 1:9 and the Watchers-leaders list overlapping 89–90**-region content Barnabas cites (§4 below).

### The 1:9/Jude 14–15 line, read honestly (bracket-by-bracket)

4Q204, line at Text-Fabric node `1559782` (raw transcription, brackets = editorial reconstruction of a lacuna, per standard DSS sigla):

```
[ כדי יאתה עם רבו ]את קדישו[ ׳הי ל מעבד דין על כול׳ה ו יובד כול רשיעין ]
```

Stripping every bracketed (reconstructed) span leaves **only what is actually inked on the parchment**:

```
את קדישו
```

— a fragment of "…[myria]ts of his hol[y ones]" (Aramaic קדישוהי, "his holy ones" — cognate to the word behind Jude's ἁγίαις, "holy," and the Ge'ez ቅዱሳን qedusan in 1 En 1:9). The next line (node `1559783`):

```
[ ו יוכח ל כול ב ]שר א על עו(# בד #)[ י רשע׳הון כול׳הון די עבדו ו מללו ל ארשעה ]
```

Surviving ink only: `שר א על עו` — "…[fle]sh, concerning the de[ed(s)]…" — matching the position of Jude's "to convict all flesh... of all their works."

**This has to be stated precisely.** The famous close match between 4Q204 and Jude/1 Enoch 1:9 ("when he comes with myriads of his holy ones to execute judgment on all and destroy all the wicked... and convict all flesh...") is, in this transcription, **mostly Milik's editorial restoration of a damaged line**, not surviving ink — restorations of exactly this kind are, in the published critical edition (Milik 1976), explicitly guided by the Ethiopic version and by Jude's own Greek quotation. Using the reconstructed text as "independent Aramaic confirmation of Jude's wording" would be circular. What genuinely is independent, physical, 1st-century-BCE-to-1st-century-CE evidence is smaller: the surviving letters **קדישו** ("holy [ones]") and **שר א ... עו** ("flesh... de[ed]") sit in the expected positions and are compatible with — but do not by themselves prove — the fuller reconstructed reading.

**Manuscript dating.** Per Milik's paleographic dating (the standard reference for these fragments), **4Q201 (4QEnᵃ)** is the oldest Enoch manuscript at Qumran, assigned to roughly **200–150 BCE** — one of the oldest Aramaic literary hands from the site at all. **4Q204 (4QEnᶜ)**, the manuscript carrying the (partly reconstructed) 1:9 material, is later, Herodian-era, roughly **late 1st c. BCE – early 1st c. CE**. Notably, 4Q201 itself appears (in this extraction) to skip directly from mountains melting (matching 1 En 1:6) to seasonal/astronomical material (matching ch. 2) at the line boundary `1559560`→`1559561` — i.e., **the oldest copy has a physical gap exactly where 1:7–9 would be**; the passage's only Aramaic witness in this corpus is the younger, more heavily restored 4Q204. Whether that gap in 4Q201 is because the leaf broke there or because that copy phrased things differently cannot be determined from what survives.

**Bottom line for Jude 14–15**: this remains a genuine and important data point — a Qumran Aramaic Enoch manuscript, independently dated by handwriting to a century-plus before Jude was likely written, was clearly at the right place in the text to carry 1:9's content, and what letters do survive are consistent with it. But "the Aramaic exactly matches Jude, word for word, in ink" **overstates what this transcription actually shows.**

---

## 3. "Son of Man" — the Similitudes, and the dating controversy

1 Enoch's Book of Parables/Similitudes (chs. 37–71) repeatedly names a pre-existent, heavenly, enthroned judge-figure "**that Son of Man**" (Ge'ez ወልደ ሰብእ, *wälədä säbəʾə* — confirmed word-by-word from `.../1En/46.json`'s `words[]` array):

> **1 En 46:2–3** — "concerning that Son of Man, who he was, and whence he was... This is the Son of Man who hath righteousness, With whom dwelleth righteousness... because the Lord of Spirits hath chosen him"
>
> **1 En 48:2–3, 6** — "at that hour that Son of Man was named In the presence of the Lord of Spirits... Yea, before the sun and the signs were created, Before the stars of the heaven were made, His name was named... for this reason hath he been chosen and hidden before Him, Before the creation of the world"
>
> **1 En 62:5, 7, 9** — "they shall see... that Son of Man Sitting on the throne of his glory... For from the beginning the Son of Man was hidden... all the kings and the mighty... shall fall down before him... and worship and set their hope upon that Son of Man"
>
> **1 En 69:27, 29** — "the sum of judgement was given unto the Son of Man, and he caused the sinners to pass away and be destroyed... For that Son of Man has appeared, and has seated himself on the throne of his glory"

Compare the Gospels' Greek title ὁ υἱὸς τοῦ ἀνθρώπου (literally "the son of the man" — same construction):

> **Mark 13:26** — καὶ τότε ὄψονται **τὸν Υἱὸν τοῦ ἀνθρώπου** ἐρχόμενον ἐν νεφέλαις μετὰ δυνάμεως πολλῆς καὶ δόξης
> **Matt 25:31** — Ὅταν δὲ ἔλθῃ **ὁ υἱὸς τοῦ ἀνθρώπου** ἐν τῇ δόξῃ αὐτοῦ καὶ πάντες οἱ ἄγγελοι μετ᾿ αὐτοῦ τότε καθίσει ἐπὶ θρόνου δόξης αὐτοῦ

The functional overlap is real and specific: a heavenly figure, seated on a **throne of glory**, attended by angels, exercising **final judgment** — not the ordinary Semitic idiom "son of man" = "a human being" (as in, e.g., Ezekiel's address, or Ps 8:4), but a specific title for a pre-existent judge. No NT author names Enoch as the source, and there is no verbatim quotation — this is category **(b) thematic/titular parallel at most**, strong enough that it has driven a large body of scholarship, but not a demonstrable quotation the way Jude 14–15 is.

### The dating controversy — reported, not resolved, per instructions

This matters entirely because of *when* the Similitudes were written relative to the Gospels, and the honest state of the question is a real, live disagreement:

- **The Similitudes are the one section of 1 Enoch with zero fragments among the Qumran manuscripts.** This was verified directly in this research: of the 869 lines recovered across all twelve Cave 4 Enoch scrolls (4Q201–4Q212, §2 above), content-matched against Charles's English translation, none corresponds to chs. 37–71 — consistent with the standard scholarly finding (Milik 1976) that the five other sections of 1 Enoch (Book of Watchers, Astronomical Book, Book of Dreams, Epistle of Enoch, Apocalypse of Weeks) are all attested in Aramaic at Qumran, but the Similitudes never are.
- **J.T. Milik** (the original editor of the Qumran Enoch fragments, 1976) argued from this absence — plus what he read as Christian theological content in the "Son of Man" material — that the Similitudes were composed **late, possibly 3rd century CE**, i.e. Christian or post-Christian, making any influence run the other way or not at all.
- **This view did not hold.** The majority of subsequent specialists — **J.C. VanderKam, G.W.E. Nickelsburg** (whose 1 Enoch commentary is one of the two scholarly sources this corpus's own README already cites for Enoch material), **J.H. Charlesworth**, and the working consensus that emerged from the 2005 Enoch Seminar meeting at Camaldoli — date the Similitudes to the **late Second Temple period**, commonly narrowed to **the reign of Herod the Great, roughly 40 BCE – 4 BCE, or more broadly 1st c. BCE to 1st c. CE**, i.e. pre-Christian or contemporaneous with earliest Christianity, not derivative of it.
- **Primary evidence for the early dating, verified from this corpus's own 1 Enoch text**: **1 En 56:5–7** (`.../1En/56.json`) — "the angels shall return And hurl themselves to the east upon **the Parthians and Medes**... they shall go up and tread under foot the land of His elect ones... But the city of my righteous shall be a hindrance to their horses." This is read by VanderKam and Nickelsburg as reflecting **the Parthian invasion of Judea in 40 BCE** (when Parthian forces briefly seized Jerusalem and installed Antigonus II) — a specific historical anchor pointing to 1st-century-BCE composition, well before Christianity. The text also contains **no reference to the Temple's destruction in 70 CE**, which most scholars find hard to explain in an apocalyptic Jewish text written after that date.
- **The puzzle is not fully closed even on the early dating**: if the Similitudes existed by the mid-1st century BCE, their total absence at Qumran needs an explanation too — proposals include that the sect's library simply never acquired a copy, or that the Similitudes had a separate transmission/circulation history from the other four Enochic booklets, but none of this is settled.

**This document takes no side.** The honest state is: absence from Qumran is a real, verified fact; what it implies about date is genuinely contested; the current majority position among specialists favors pre-Christian or contemporaneous composition, against Milik's minority post-Christian view.

---

## 4. Jubilees, the 364-day calendar, and the Qumran calendar dispute

**Jub 6** (`.../Jub/6.json`; note: this file's verse field for ch. 6 is a data artifact — the entire chapter's prose is collapsed into verse 1, with verses 2–38 empty strings; content quoted below is real text, just mis-segmented at the source) states the calendar rule explicitly:

> "...command thou the children of Israel that they observe the years according to this reckoning — **three hundred and sixty-four days**, and (these) will constitute a complete year..."

and gives the polemical reason — a warning against following lunar observation:

> "For there will be those who will assuredly **make observations of the moon** — how (it) disturbs the seasons and comes in from year to year **ten days too soon**. For this reason the years will come upon them when they will disturb (the order)... they will confound all the days, the holy with the unclean, and the unclean day with the holy; for they will go wrong as to the months and sabbaths and feasts and jubilees."

This is Jubilees' own explanation of the fight: a solar year of exactly 364 days (52 weeks exactly — deliberately chosen so festivals always fall on the same weekday) versus the standard lunar/lunisolar calendar used by the Jerusalem priesthood, which drifts roughly ten days a year against the sun and needs periodic intercalation. Jubilees frames the 364-day scheme not as one option among several but as written "on the heavenly tablets" — i.e., as revealed, correct time itself; anyone using a different calendar is, on this view, keeping feasts on the wrong day, effectively defiling them. The 364-day calendar is also the scheme underlying 1 Enoch's own Astronomical Book (chs. 72–82, the section attested at Qumran in 4Q208–4Q211, per §2's line counts — 4Q209 alone contributed 171 of the 869 recovered lines, the single largest share, consistent with its being the longest Enoch scroll found). This calendar is the same one associated with the Qumran sect's own liturgical calendar (4QMMT and the various *Mishmarot* texts argue for it against the Jerusalem Temple's practice) — the corpus's Dead Sea Scrolls holding for Enoch is itself physical evidence for who was preserving and presumably using this calendar tradition.

### Eusebius preserves Enoch cited as a live astronomical authority, in a calendar argument, in the 3rd century CE

Searching `apostolic-fathers/First1KGreek/data/tlg2018/tlg002/tlg2018.tlg002.1st1K-grc1.xml` (Eusebius, *Historia Ecclesiastica*) for Ἐνώχ (after NFD-normalizing and stripping combining marks, since the raw file's accents defeat plain grep) finds exactly one occurrence, in **HE VII.32**, inside Eusebius's quotation of **Anatolius of Laodicea**'s treatise on the date of Easter/Passover:

> "...του δε τον πρωτον παρ' Εβραιοις μηνα περι ισημεριαν ειναι παραστατικα **και τα εν τω Ενωχ μαθηματα**"
> *"...and that the first month among the Hebrews falls around the equinox — the teachings in Enoch also attest this."*

Anatolius (a bishop, writing on the Passover computation, quoted here by Eusebius without objection) cites "the things taught in Enoch" as supporting astronomical/calendrical evidence for where the Hebrew new year falls relative to the equinox — i.e., **1 Enoch's Astronomical Book being invoked as a legitimate scientific authority on the calendar question**, by a bishop, in material Eusebius preserves approvingly, in the 3rd century CE. This is not Eusebius's own verdict on Enoch's canonicity (his NT-books discussion in HE III.25, translated in full at `translations/eusebius-HE-3.25.md`, is about the *New Testament* list and does not mention Enoch — a check worth stating plainly since it would be easy to assume it did), but it is a genuine, on-disk primary citation of Enoch as calendrical authority.

---

## 5. Early Christian citation — who quoted it as scripture, who didn't

### Barnabas — quotes it by name, with the formula used for scripture

**Epistle of Barnabas 4:3** (`apostolic-fathers/First1KGreek/data/tlg1216/tlg001/tlg1216.tlg001.opp-grc1.xml`):

> "τὸ τέλειον σκάνδαλον ἤγγικεν, περὶ οὗ **γέγραπται**, ὡς **Ἐνὼχ** λέγει. Εἰς τοῦτο γὰρ ὁ δεσπότης συντέτμηκεν τοὺς καιροὺς καὶ τὰς ἡμέρας, ἵνα ταχύνῃ ὁ ἠγαπημένος αὐτοῦ καὶ ἐπὶ τὴν κληρονομίαν ἥξῃ"
> *"The final stumbling-block has drawn near, concerning which **it is written** [γέγραπται — the standard formula for citing scripture], as **Enoch says**. For to this end the Master has cut short the times and the days, that his beloved might hasten and come to his inheritance."*

The editorial apparatus in this file cites this as corresponding to Enoch 89:61–64 and 90:17 (the Animal Apocalypse's "shepherds" section). Critically, the *very next section*, **Barn 4:4**, introduces a Daniel citation with almost identical grammar: "λέγει δὲ οὕτως καὶ **ὁ προφήτης** [and thus also **the prophet** says]: Δανιήλ..." — Barnabas places Enoch and Daniel back to back, both introduced as authoritative "it is written" sources. This is category **(a) direct quotation, introduced as scripture**, by name.

(A second citation sometimes attributed to Enoch, **Barn 16:6** — "γέγραπται γάρ: Καὶ ἔσται, τῆς ἑβδομάδος συντελουμένης οἰκοδομηθήσεται ναὸς θεοῦ ἐνδόξως..." — was checked directly and **does not name Enoch** in this text; it is an unattributed "it is written" citing an unidentified apocalyptic source. Reporting it as an Enoch quotation, which is common in secondary literature, is not supported by what this file actually says. Only Barn 4:3 explicitly names Enoch.)

### Jude — already established: quotes 1 En 1:9 as prophecy (Ἐπροφήτευσεν), the strongest direct quotation in the entire NT.

### Tertullian, Augustine, Jerome — not verifiable from this corpus

As noted in §0, none of these three authors' texts are on disk here. What is widely reported in secondary scholarship — that **Tertullian** (*De Cultu Feminarum* I.3) defended 1 Enoch's authenticity and inspiration against objectors who doubted a book Noah's flood should have destroyed, while **Augustine** (*City of God* XV.23) and **Jerome** (scattered references, e.g. in his commentary work) treated it as apocryphal/non-canonical — cannot be quoted or checked against a primary source here, and per this corpus's own data-integrity standard is reported only as a well-attested claim from secondary scholarship, not as verified primary evidence.

### Eusebius — see §4; cites Enoch via Anatolius as calendrical authority, does not address its canonical status directly in the material found.

---

## 6. Why it was excluded — what the primary sources on disk actually give reasons for

Being precise about what this corpus can and cannot show:

- **No primary source found on disk gives an explicit argument for excluding 1 Enoch from a canon.** Eusebius's HE III.25 (§0, full translation at `translations/eusebius-HE-3.25.md`) is about the New Testament book list specifically and never mentions Enoch — it cannot be used as evidence either way about Enoch's status.
- What the disk **does** show is the live, unsettled character of the argument in the earliest period: Jude quotes 1 Enoch as fulfilled prophecy (Ἐπροφήτευσεν) sometime in the 1st century CE; Barnabas quotes it with the "it is written" scripture-formula, on equal footing with Daniel, in the early-mid 2nd century; a 3rd-century bishop's astronomical argument (preserved by Eusebius) treats "the teachings in Enoch" as still-usable authority for calendar computation. None of these treat Enoch's status as already settled or already rejected.
- The eventual exclusion from the Western/Eastern canons (while 1 Enoch remained canonical in Ethiopia, per `EXCLUDED-BOOKS.md`) rests, per widely-cited secondary scholarship, substantially on **Augustine's and Jerome's** later judgments — but as stated in §5, their actual texts are not on this disk, so **the specific reasons they gave cannot be verified or quoted here**, only reported as a gap. This is the honest limit of what this corpus can establish, and per its own Data Integrity instruction this stops here rather than reconstructing their arguments from memory dressed as verified fact.

---

## Summary table — category discipline

| NT passage | 1 Enoch material | Category | Basis |
|---|---|---|---|
| Jude 14–15 | 1 En 1:9 | **(a) direct quotation**, "Ἐπροφήτευσεν" | Previously verified phrase-by-phrase against Ge'ez |
| 2 Pet 2:4 / Jude 6 | 1 En 10 (Watchers bound pending judgment) | **(b) clear allusion** | Specific plot details (bound, darkness, reserved for judgment) absent from Genesis, present only in Enoch |
| 1 Pet 3:19–20 | 1 En 10, 15 (spirits in prison, days of Noah) | **(b) allusion to narrative frame** | "Spirits in prison" + Noah is Enoch's frame; theology (Christ preaching) is not |
| Matt 22:30 | 1 En 15:3–7 (angels don't marry) | **(c) shared premise** | Assumed idea, not a citation |
| 1 Cor 11:10 | 1 En 6–8 (angels desire women) | **(c) contested allusion** | Genuinely disputed in scholarship; Paul gives no gloss |
| 2 Cor 11:14 | — | **no connection found** | Different tradition (deceptive disguise, not lust) |
| Mark 13:26, Matt 25:31 etc. ("Son of Man") | 1 En 46, 48, 62, 69 (Similitudes) | **(b) titular/thematic parallel** | No verbatim quotation; strong functional overlap (throne of glory, judgment, angels) |
| Rev 9:1–2; 20:1–3 (abyss, key, chain, bound term) | 1 En 10:4–13; 18:12–16; 21 | **(c) shared apocalyptic imagery pool** | No verbatim dependence demonstrated; same cosmology of a keyed/sealed abyss housing bound rebellious beings |
| Barn 4:3 | 1 En 89–90 region | **(a) direct quotation**, "γέγραπται... ὡς Ἐνὼχ λέγει" | Explicit citation formula + named source |

---

## What would need to be added to go further

- **Tertullian, Augustine, Jerome primary texts** — genuinely absent from this corpus; would need to be pulled to verify the specific exclusion arguments rather than reporting them secondhand.
- **A full line-by-line pass over all 869 recovered Qumran Enoch lines**, chapter-by-chapter, to build a real concordance against Charles's chapter/verse numbers (this task sampled targeted chapters/scrolls, not the full 869).
- **4QMMT and the *Mishmarot* calendar texts**, if present elsewhere in the DSS holding, for the Qumran sect's own explicit calendar polemic alongside Jubilees'.
