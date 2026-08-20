# 1 Enoch 17–24 — The Journey: fire, the cornerstone, the seven angels, the prison of the stars, and the mountain of the dead

**Translated from the Ge'ez, against the Greek. No English translation consulted.**

Built with `tools/enoch.py`, which drops the Charles-1917 `translation` field bundled in the Ge'ez
JSON at parse time with no flag to re-enable it, and `tools/dillmann.py` (new this session) for the
Latin of Dillmann's *Lexicon Linguae Aethiopicae* (1865). See `PROVENANCE.md`, `ATTRIBUTION.md`.

---

## Provenance chain

```
Aramaic  — ABSENT for this entire block. The Qumran material stops at ch 8.
   └─> Greek  — Gizeh throughout; Gizeh2 joins at ch 21. This is the control.
          └─> Ge'ez  — p and Bertalotto, the only complete witness
```

This block is **better attested than 37–51 and worse than 6–8**. There is no Aramaic, so no access
to the original language; but there *is* a continuous Greek, so unlike the Parables every Ge'ez
sentence here can be checked against something older.

### 🛑 What the lexicon could not supply

Two load-bearing words returned no usable Dillmann entry. Per rule 1 they are **not rendered as
English** and are printed as Ge'ez with the gap marked:

- **`ዐውሎ`** (17:2) — `dillmann.py` finds it only in citations (`ዐውሎሁ፡ለነፋስ`, Sir. 43:17, where it
  stands beside `ነፋስ` "wind"), never in its own entry. A stem search reaches `ዐውል` but that hit is
  ⚠️ **from the French Tigre glossary bound into the same archive.org scan, not from Dillmann** —
  see the note below. **[SENSE NOT DERIVED]**
- **`ሱርርተ`** (21:2) — no entry, no usable stem. **[SENSE NOT DERIVED]**

> [!danger] 🛑 FOURTH INSTANCE — the post-1820 layer entering through tooling
> `lexicon/dillmann-1865_djvu.txt` is **not only Dillmann**. A **French**-glossed Tigre/Amharic
> word-list is bound into the same volume, and it scores like a lexicon entry. A lookup for `ዐውል`
> returns `'aul, priz` — French, not Latin, not Dillmann, and not 1865 Ge'ez lexicography.
> `dillmann.py` now flags these ⚠️ **NOT DILLMANN** and refuses to rank them as entries.
> Previous three instances: an apparatus of editions read as manuscripts (`revelation-3`),
> Strong's-1890 for root ID (`PROVENANCE`), Charles's conjectures printed as parchment (`enoch-6`).

---

# ⭐⭐⭐ FINDING 1 — 20:1: the Ge'ez calls them **Watchers**; the Greek calls them **Powers**

| | text |
|---|---|
| **Ge'ez** 20:1 | `ወዝንቱ፡ ውእቱ፡ አስማቲሆሙ፡ ለእለ፡ ይተግሁ፡ ቅዱሳን፡ መላእክት።` |
| **Gizeh** 20:1 | `Ἄγγελοι τῶν δυνάμεων.` |

`ይተግሁ` is from the root Dillmann files as **`vigil, pervigil, epitheton angelorum`** — wakeful,
ever-watchful, **an epithet of angels**. It is the Ge'ez side of `ትጉሃን` ∥ `ἐγρήγοροι`, the one
technical term this repo has already shown survives the whole chain intact (see `enoch-9-16.md`,
Finding 7). So the Ge'ez heading reads: *these are the names of **those who keep watch**, the holy
angels.*

The Greek heading is `ἄγγελοι τῶν δυνάμεων` — **angels of the powers/hosts**. That is a different
category entirely: a rank in a heavenly army, not a description of staying awake.

🛑 The chapter that gives the seven archangels their names is headed by **two different
descriptions of what they are**, and every English Enoch has to pick one silently.

---

# ⭐⭐⭐ FINDING 2 — 20:2: Uriel has two completely different jobs, and Dillmann cites this verse

| | Uriel is over… |
|---|---|
| **Ge'ez** | `እስመ፡ ዘረዓም፡ ወዘረዓድ` — of **thunder** and of **trembling** |
| **Gizeh + Gizeh2** | `ὁ ἐπὶ τοῦ κόσμου καὶ τοῦ ταρτάρου` — over **the world** and **Tartarus** |

⭐ **Dillmann's entry for `ረዓም` cites 1 Enoch 20:2 itself**: `subst. 1) tonitru **Hen. 20, 2**.
2) vox tonans, strepitus, fremitus`. So the Ge'ez word here is *thunder* on the lexicographer's own
authority, using this very verse as his proof text.

`ረዓድ` appears in Dillmann only in the pairing `ፍርሀት፡ወረዓድ` = *timor et tremor* (Luc. 1:12,
`φόβος … ἐπέπεσεν`) — **fear and trembling**. So: thunder and the shaking that follows it.

Neither Ge'ez word has anything to do with `κόσμος` or `τάρταρος`. This is not a translation
drifting; it is two different sentences. Note also that **Gizeh2 joins Gizeh here** — both Greek
witnesses agree against the Ge'ez, which makes the Greek reading the better-attested one and the
Ge'ez the odd man out.

---

# ⭐⭐ FINDING 3 — 18:1/18:2: the cornerstone sits on the seam, and the versification moved

**Gizeh 18:1** ends: `… καὶ τὸν θεμέλιον τῆς γῆς, **καὶ τὸν λίθον ἴδον τῆς γωνίας τῆς γῆς**.`
**Ge'ez 18:1** ends at `ወመሠረታቲሃ፡ ለምድር` (and the foundations of the earth) — **and stops**.
**Ge'ez 18:2** then opens: `ወርኢኩ፡ እብነ፡ ማእዘንተ፡ ምድር፡ …`

So the cornerstone clause is in **both**; the two traditions simply put the verse break on opposite
sides of it. `ማእዘንት` is confirmed by Dillmann's citation of 1 Petr. 2:7, `ውስተ፡ ርእሰ፡ ማእዘንት` =
`εἰς κεφαλὴν γωνίας` — head of the corner. Same word, same stone.

🛑 Worth stating because it is the *opposite* of a variant: an apparatus that aligns by verse number
would report a Greek plus at 18:1 and a Ge'ez plus at 18:2, and there is no plus at all.
**Unit-alignment can manufacture a disagreement out of punctuation.**

---

# ⭐⭐ FINDING 4 — 22:2: the Greek has the whole scene the Ge'ez lacks

**Ge'ez 22:2** — four fine places, hollow, deep, wide and very smooth. That is all.

**Gizeh 22:2** — `καὶ τέσσαρες τόποι ἐν αὐτῷ κοῖλοι, βάθος ἔχοντες καὶ λίαν λεῖοι, **τρεῖς αὐτῶν
σκοτινοὶ καὶ εἷς φωτινός, καὶ πηγὴ ὕδατος ἀνὰ μέσον αὐτοῦ.** καὶ εἶπον **Πῶς λεῖα τὰ κοιλώματα
ταῦτα καὶ ὁλοβαθῆ καὶ σκοτινὰ τῇ ὁράσει;**`

The Greek carries two things the Ge'ez has nothing for:

1. **`τρεῖς αὐτῶν σκοτινοὶ καὶ εἷς φωτινός, καὶ πηγὴ ὕδατος`** — three of the four are **dark** and
   one is **bright**, and there is a **spring of water** in the middle. This is the structural
   detail of the chamber of the dead: the compartments are not equivalent, and one has light and
   water. **The Ge'ez has no light, no water, and no asymmetry.**
2. **Enoch's own question** — "how smooth are these hollows, and utterly deep, and dark to look at?"
   The Ge'ez narrates; the Greek has Enoch speak.

The chapter that divides the dead into separate compartments reads very differently depending on
whether one of them is lit.

---

# ⭐ FINDING 5 — 17:2: a dark place or a storm?

| | |
|---|---|
| **Ge'ez** | `ወወሰዱኒ፡ ውስተ፡ መካን፡ ዘዐውሎ` |
| **Gizeh** | `καὶ ἀπήγαγόν με εἰς **γνοφώδη** τόπον` — a **gloomy / murky** place |

`ዐውሎ` is **[SENSE NOT DERIVED]** — Dillmann gives it no entry this tool can reach, and every
citation puts it beside `ነፋስ` (wind), which points at storm rather than darkness. `γνοφώδης` is
unambiguously about gloom. Recorded as an open divergence, **not resolved**, because resolving it
would mean choosing the Greek to define a Ge'ez word — which is how a version gets read back into
the text it was made from.

Same verse, second half: `ደብር፡ ዘከተማ፡ ርእሱ፡ ይበጽሕ፡ ውስተ፡ ሰማይ`. Dillmann, **LIKELY ENTRY**, on
`ከተማ`: *extremum, summum, extremitas, summitas* — with `ከተማ፡ምድር` = extremity of the earth
(Prov. 17:24). So: a mountain **whose summit — its head — reaches into heaven**. Gizeh agrees
exactly: `ὄρος οὗ ἡ κεφαλὴ ἀφικνεῖτο εἰς τὸν οὐρανόν`. ⚠️ `ከተማ` also carries a euphemistic sense in
Dillmann (`ከተማ፡ነፍስት`, Gen. 17:11) — a second, unrelated use of "extremity". Not in play here, noted
so the range is complete rather than tidy.

---

# ⭐ FINDING 6 — 19:1: the spirits are "many-formed" in both, and the Ge'ez says how

| | |
|---|---|
| **Ge'ez** | `ወብዙኀ፡ ራእየ፡ ከዊኖሙ` — having become **many of appearance** |
| **Gizeh** | `τὰ πνεύματα αὐτῶν **πολύμορφα** γενόμενα` — having become **many-formed** |

A rare clean agreement in this block, and worth logging as such: `ራእይ` (appearance/vision) against
`μορφή` (form) is as close as two languages get. The chapter's claim — that the spirits of the dead
giants take many shapes and mislead people into sacrificing to them **as to gods**
(`ከመ፡ ይሡዑ፡ ለአጋንንት፡ ከመ፡ አማልክት` ∥ `ἐπιθύειν τοῖς δαιμονίοις`) — is stable across the chain.

---

# THE TEXT

## Chapter 17 — carried to the place of fire

### 17:1
**ወነሥኡኒ፡ ውስተ፡ አሐዱ፡ መካን፡ ኅበ፡ ሀለዉ፡ ህየ፡ ከመ፡ እሳት፡ ዘይነድድ፡ ወሶበ፡ ይፈቅዱ፡ ያስተርእዩ፡ ከመ፡ ሰብእ።**

*wänäśəʾuni wəsətä ʾäḥädu mäkanə ḫəbä häläwu həyä kämä ʾəsatə zäyənädədə wäsobä yəfäqədu
yasətärəʾəyu kämä säbəʾə*

**And they (took | received | carried) me into one place, where those who are there are like
burning fire — and when they wish, they appear like men.**

- **Witness — Gizeh:** `καὶ παραλαβόντες με εἴς τινα τόπον ἀπήγαγον, ἐν ᾧ οἱ ὄντες ἐκεῖ γίνονται ὡς
  πῦρ φλέγον καὶ ὅταν θέλωσιν, φαίνονται ὡσεὶ ἄνθρωποι.` Agrees throughout. The Greek uses **two**
  verbs of conveying (`παραλαβόντες` … `ἀπήγαγον`) where the Ge'ez has one.
- Ethiopic: `p Bertalotto` write the numeral `፩` for `አሐዱ` and `ኀበ` for `ኅበ` — orthographic.
- Qumran Aramaic — **ABSENT**. Latin — **ABSENT**.

### 17:2
**ወወሰዱኒ፡ ውስተ፡ መካን፡ ዘዐውሎ፡ ወውስተ፡ ደብር፡ ዘከተማ፡ ርእሱ፡ ይበጽሕ፡ ውስተ፡ ሰማይ።**

*wäwäsäduni wəsətä mäkanə zäʿäwəlo wäwəsətä däbərə zäkätäma rəʾəsu yəbäṣəḥə wəsətä sämayə*

**And they led me to a place of `ዐውሎ` [SENSE NOT DERIVED — see Finding 5], and to a mountain the
(summit | extremity | topmost part) of which — its head — reaches into heaven.**

- **Witness — Gizeh:** `εἰς γνοφώδη τόπον` — see Finding 5. Second half agrees exactly.
- Ethiopic: `p` `ዘዓውሎ` / `Bertalotto` `ዘዐውሎ`; both read `እስከ፡ ሰማይ` ("as far as heaven") where the
  base has `ውስተ፡ ሰማይ` ("into heaven"). ⚠️ A real difference in how far the mountain gets.
- Qumran Aramaic — **ABSENT**. Latin — **ABSENT**.

## Chapter 18 — the storehouses and the cornerstone

### 18:1
**ወርኢኩ፡ መዛግብተ፡ ኵሉ፡ ነፋሳት፡ ወርኢኩ፡ ከመ፡ ቦሙ፡ አሰርገወ፡ ኵሎ፡ ፍጥረተ፡ ወመሠረታቲሃ፡ ለምድር።**

*wärəʾiku mäzagəbətä kwəlu näfasatə wärəʾiku kämä bomu ʾäsärəgäwä kwəlo fəṭərätä wämäśärätatiha
lämədərə*

**And I saw the (treasuries | storehouses) of all the winds, and I saw that with them he (adorned |
arrayed | furnished) all creation, and the foundations of the earth.**

- **Witness — Gizeh:** `ἴδον τοὺς θησαυροὺς τῶν ἀνέμων πάντων, ἴδον ὅτι ἐν αὐτοῖς ἐκόσμησεν πάσας
  τὰς κτίσεις καὶ τὸν θεμέλιον τῆς γῆς, **καὶ τὸν λίθον ἴδον τῆς γωνίας τῆς γῆς**.` — `ἐκόσμησεν`
  (adorned/ordered) matches `አሰርገወ` closely. The final clause: **Finding 3**.
- ⚠️ Greek `τὸν θεμέλιον` **singular** against Ge'ez `ወመሠረታቲሃ` **plural** — one foundation or many.
- Qumran Aramaic — **ABSENT**. Latin — **ABSENT**.

### 18:2
**ወርኢኩ፡ እብነ፡ ማእዘንተ፡ ምድር፡ ወርኢኩ፡ አርባዕተ፡ ነፋሳተ፡ እለ፡ ይጸውርዋ፡ ለምድር፡ ወለጽንዐ፡ ሰማይ።**

*wärəʾiku ʾəbənä maʾəzänətä mədərə wärəʾiku ʾärəbaʿətä näfasatä ʾəlä yəṣäwərəwa lämədərə
wäläṣənəʿä sämayə*

**And I saw the stone of the corner of the earth, and I saw the four winds which bear up the earth
and the (firmament | strength | firmness) of heaven.**

- `ማእዘንት` — Dillmann via 1 Petr. 2:7, `ውስተ፡ ርእሰ፡ ማእዘንት` = `εἰς κεφαλὴν γωνίας`. Corner, angle.
- **Witness — Gizeh:** `ἴδον τοὺς τέσσαρας ἀνέμους τὴν γῆν βαστάζοντας,` — the Greek has the four
  winds bearing the earth and **stops there**. It lacks `ወለጽንዐ፡ ሰማይ` — *and the firmament of
  heaven*. The Ge'ez winds carry one more thing than the Greek winds do.
- Ethiopic: `p` `ዕብነ` / `Bertalotto` `እብነ`; `p` `ወለጽንዓ` / `Bertalotto` `ወለጽንዐ`; numeral `፬`.
- Qumran Aramaic — **ABSENT**. Latin — **ABSENT**.

## Chapter 19 — Uriel explains the spirits

### 19:1
**ወይቤለኒ፡ ኡርኤል፡ በዝየ፡ ተደሚሮሙ፡ መላእክት፡ ምስለ፡ አንስት፡ ይቀውሙ፡ መናፍስቲሆሙ፡ ወብዙኀ፡ ራእየ፡ ከዊኖሙ፡ አርኰስዎሙ፡ ለሰብእ፡
ወያስሕትዎሙ፡ ለሰብእ፡ ከመ፡ ይሡዑ፡ ለአጋንንት፡ ከመ፡ አማልክት፡ እስመ፡ በዕለት፡ ዐባይ፡ ኵነኔ፡ በዘይትኴነኑ፡ እስከ፡ ይትፌጸሙ።**

**And Uriel said to me: here shall stand the angels who mingled themselves with the women; and their
spirits, having become many of appearance, (defile | pollute) mankind and (lead astray | cause to
err) mankind, so that they sacrifice to the demons as to gods — until the great day of judgment, in
which they shall be judged until they are (finished | consummated | brought to an end).**

- **Witness — Gizeh:** `Καὶ εἶπέν μοι Οὐριὴλ Ἐνθάδε οἱ μιγέντες ἄγγελοι ταῖς γυναιξὶν στήσονται, καὶ
  τὰ πνεύματα αὐτῶν πολύμορφα γενόμενα λυμαίνεται τοὺς ἀνθρώπους καὶ πλανήσει αὐτοὺς ἐπιθύειν τοῖς
  δαιμονίοις μέχρι τῆς μεγάλης κρίσεως, ἐν ᾗ κριθήσονται εἰς ἀποτελείωσιν.` Close throughout —
  **Finding 6**.
- ⚠️ Greek `λυμαίνεται` (ravage, ruin, outrage) is harsher than a defilement word; the two verbs
  sit in different registers. Both printed, neither preferred.
- Ethiopic: `p` `ወብዙኃ` / `Bertalotto` `ወብዙኀ`; `p` `ዓባይ` / `Bertalotto` `ዐባይ`. ⚠️ `p Bertalotto`
  **repeat** `እስመ፡ በዕለት፡ ዓባይ` — a dittography in the Ethiopic tradition.
- Qumran Aramaic — **ABSENT**. Latin — **ABSENT**.

### 19:2
**ወአንስቲያሆሙኒ፡ አስሒቶን፡ መላእክተ፡ ከመ፡ ሰላማውያት፡ ይከውና።**

**And their women also, having led the angels astray, shall become as (peaceable ones | those at
peace) [`ሰላማውያት` — sense open].**

- 🛑 A one-line verse with no Greek. The women's fate is stated in the Ge'ez alone.

## Chapter 20 — the names of the seven

### 20:1
**ወዝንቱ፡ ውእቱ፡ አስማቲሆሙ፡ ለእለ፡ ይተግሁ፡ ቅዱሳን፡ መላእክት።**

**And these are the names of those who keep watch — the holy angels.**

- **Witness — Gizeh:** `Ἄγγελοι τῶν δυνάμεων.` — **Finding 1.** Not the same heading.

### 20:2
**ኡርኤል፡ አሐዱ፡ እመላእክት፡ ቅዱሳን፡ እስመ፡ ዘረዓም፡ ወዘረዓድ።**

**Uriel, one of the holy angels — for [he is] of the thunder and of the trembling.**

- `ረዓም` — Dillmann: *tonitru*, **citing this verse**. `ረዓድ` — *tremor*, in the pair
  `ፍርሀት፡ወረዓድ` = *timor et tremor*. **Finding 2.**
- **Witness — Gizeh + Gizeh2:** `Οὐριήλ, ὁ εἷς τῶν ἁγίων ἀγγέλων ὁ ἐπὶ τοῦ κόσμου καὶ τοῦ
  ταρτάρου.` Both Greek witnesses against the Ge'ez.
- Ethiopic: `p Bertalotto` `፩፡ እምነ፡ መላእክት` and `ዘርአም፡ ወዘረአድ` — orthographic.

### 20:3
**ሩፋኤል፡ አሐዱ፡ እመላእክት፡ ቅዱሳን፡ ዘመናፍስተ፡ ሰብእ።**

**Raphael, one of the holy angels — who is over the spirits of men.**

- ⭐ Cross-reference: `enoch-9-16.md` Finding 6 records that **the Ge'ez omits Raphael from the four
  at 9:1 while naming him at 10:4**. He is here at 20:3 as well. The Ge'ez knows Raphael perfectly
  well and left him out of exactly one list.

## Chapter 21 — the prison of the stars

### 21:2
**ወርኢኩ፡ በህየ፡ ግብረ፡ ግሩመ፡ ኢ፡ ሰማየ፡ ልዑለ፡ ወኢ፡ ምድረ፡ ሱርርተ፡ አላ፡ መካነ፡ በድው፡ ዘድልው፡ ወግሩም።**

**And I saw there a (terrible | dreadful) work: neither heaven above, nor earth `ሱርርተ` [SENSE NOT
DERIVED], but a place — desert, (prepared | fitted) and terrible.**

- **Witness — Gizeh + Gizeh2:** `ἐθεασάμην ἔργον φοβερόν· ἑώρακα οὔτε οὐρανὸν ἐπάνω, οὔτε γῆν
  τεθεμελιωμένην, ἀλλὰ τόπον ἀκατασκεύαστον καὶ φοβερόν.`
- 🛑 **The Greek is the exact opposite of the Ge'ez on one word.** Greek `ἀκατασκεύαστον` =
  **un**prepared, unformed — the same word the LXX uses of the earth in Gen 1:2 (`ἀόρατος καὶ
  ἀκατασκεύαστος`). Ge'ez `ዘድልው` is a *positive* participle: prepared, fitted, ready. One tradition
  says the place was never made; the other says it was made ready. **Recorded, not resolved.**
- ⚠️ Gizeh and Gizeh2 differ from each other twice here (`κἀκεῖ` / `καὶ ἐκεῖ`; `τεθέαμαι` inserted
  by Gizeh) — the two Greek hands are not one text.

### 21:3
**ወህየ፡ ርኢኩ፡ ሰብዓተ፡ ከዋክብተ፡ ሰማይ፡ እሱራን፡ በላዕሌሁ፡ ኅቡረ፡ ከመ፡ አድባር፡ ዐበይት፡ ወከመ፡ እሳት፡ እንዘ፡ ይነድዱ።**

**And there I saw seven of the stars of heaven, bound upon it together, like great mountains and
like fire, burning.**

- 🛑 `enoch.py` returns **no witness block at all** for this verse — not even an ABSENT line.
  Reported, not filled. The seven bound stars stand on the Ge'ez alone here.

## Chapter 22 — the mountain of the dead

### 22:1
**ወእምህየ፡ ሖርኩ፡ ካልአ፡ መካነ፡ ወአርአየኒ፡ በምዕራብ፡ ደብረ፡ ዐቢየ፡ ወነዋኀ፡ ወኰኵሐ፡ ጽኑዐ።**

**And from there I went to another place, and he showed me in the west a great and high mountain,
and hard rock.**

- **Witness — Gizeh:** `Κἀκεῖθεν ἐφώδευσα εἰς ἄλλον τόπον, καὶ ἔδειξέν μοι πρὸς δυσμὰς ἄλλο ὄρος
  μέγα καὶ ὑψηλόν, πέτρας στερεάς.` Agrees. Greek adds `ἄλλο` ("another" mountain).
- Ethiopic: `p`/`Bertalotto` split on `ዓቢይ`/`ዐቢይ`, `ወነዋህ`/`ወነዋኅ`, `ፅኑዕ`/`ጽኑዕ` — orthographic,
  but all three read the **absolute** where the base has the **accusative** `ዐቢየ ወነዋኀ ጽኑዐ`.

### 22:2
**ወአርባዕቱ፡ መካናት፡ ሠናያት፡ ወበውስቴቱ፡ ዕሙቅ፡ ወርሒብ፡ ወልሙጽ፡ ጥቀ፡ ከመ፡ ልሙጽ፡ ዘያንኰረኵር፡ ወዕሙቅ፡ ወጽልመት፡ ለነጽሮ።**

**And four fine places, and within it deep and wide and very smooth, like something smooth that
rolls — and deep and dark to look upon.**

- **Witness — Gizeh:** carries **three dark, one bright, a spring of water, and Enoch's question**,
  none of which the Ge'ez has. **Finding 4.**
- Ethiopic: `p Bertalotto` add `ዘቦቱ` and read `ወርኂብ`; numeral `፬`.

## Chapter 23 — the fire that never rests

### 23:1
**ወእምህየ፡ ርኢኩ፡ ካልአ፡ መካነ፡ መንገለ፡ ዐረብ፡ እስከ፡ አጽናፈ፡ ምድር።**

**And from there I saw another place, toward the west, as far as the (ends | extremities) of the
earth.**

### 23:2
**ወርኢኩ፡ እሳተ፡ ዘይነድድ፡ ወይረውጽ፡ እንዘ፡ ኢየዐርፍ፡ ወኢይነትግ፡ እምሩጸቱ፡ መዓልተ፡ ወሌሊተ፡ አላ፡ ከማሁ፡ ክመ።**

**And I saw a fire burning and running, which does not rest and does not (break off | cease) from
its running, day and night — but is just so, continually.**

### 23:3
**ወተስእልኩ፡ እንዘ፡ እብል፡ ዝንቱ፡ ምንት፡ ውእቱ፡ ዘአልቦ፡ ዕረፍት።**

**And I asked, saying: what is this, which has no rest?**

### 23:4
**And there answered me one of the holy angels who was with me, and he said to me: this that you
have seen — that which is toward the fire that burns — [is] all the heaven [text continues].**

- 🛑 Chapter 23 gets **no Greek and no Latin and no Aramaic**. Four verses on the Ge'ez alone.
  This is the beginning of the long stretch where the control drops away.

## Chapter 24 — the seven mountains and the tree

### 24:1
**ወእምህየ፡ ሖርኩ፡ ካልአ፡ መካነ፡ ምድር፡ ወአርአየኒ፡ ደብረ፡ እሳት፡ ዘያንበለብል፡ መዓልተ፡ ወሌሊተ።**

**And from there I went to another place of the earth, and he showed me a mountain of fire, flaming
day and night.**

### 24:2
**ወሖርኩ፡ መንገሌሁ፡ ወርኢኩ፡ ሰብዓተ፡ አድባረ፡ ክቡራነ፡ ወኵሉ፡ አሐዱ፡ እምነ፡ አሐዱ፡ እንዘ፡ ይትዌለጥ፡ ወአእባነ፡ ክቡራነ፡ ወሠናያነ፡
ወኵሉ፡ ክቡር፡ ወስቡሕ፡ ራእዮሙ፡ ወሠናይ፡ ገጾሙ፡ ሠለስቱ፡ መንገለ፡ ጽባሕ፡ ወጽኑዓን፡ አሐዱ፡ ዲበ፡ አሐዱ፡ ወሠለስቱ፡ መንገለ፡ ሰሜን፡ አሐዱ፡
ዲበ፡ አሐዱ፡ ጽኑዓን፡ ወቈላት፡ ዕሙቃት፡ ወጠዋያት፡ አሐቲ፡ ለአሐቲ፡ ኢይትቃረባ።**

**And I went toward it, and I saw seven honoured mountains, and every one differing from every
other; and honoured and beautiful stones, and all of them honoured and glorious in their appearance
and fair of face: three toward the east, firm, one upon another; and three toward the north, one
upon another, firm; and deep and crooked ravines, no one of them coming near another.**

---

## What this block cost, and what it did not settle

- **Six findings**, three of them substantive (20:1, 20:2, 22:2) and one that *removes* an apparent
  variant rather than adding one (18:1/2).
- **Two words left underived** and printed as Ge'ez — `ዐውሎ`, `ሱርርተ` — because the only route to
  them ran through the Greek, and using a version to define its own source is the thing this
  project exists to refuse.
- **21:2 `ዘድልው` vs `ἀκατασκεύαστον`** is a flat contradiction and is left standing as one.
- **Chapters 23–24 have no non-Ge'ez witness.** From here to the end of the Book of Watchers the
  control thins out; from 37 it disappears entirely.

⚠️ Semantic ranges here are **not validator-gated** — `ranges/*.json` and `verify_ranges.py` are
Hebrew-only. Same limitation logged for `revelation-3.md` and every Enoch file.
