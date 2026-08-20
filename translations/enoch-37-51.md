# 1 Enoch 37–51 — The Book of Parables, first half

**Translated from the Ge'ez. No English translation was consulted at any point.**

Built with `tools/enoch.py` (which drops the Charles-1917 `translation` field bundled in the Ge'ez JSON at parse time), `tools/geezroot.py`, and direct grep of `lexicon/dillmann-1865_djvu.txt`. **Every sense range below is taken from Dillmann's Latin.** See PROVENANCE.md and ATTRIBUTION.md.

---

# 🛑🛑 THIS BLOCK HAS NO CONTROL

**Chapters 37–71 are the Book of Parables. Per `translations/ENOCH-SURVEY.md`, this section has ZERO Qumran Aramaic attestation and almost no Greek.**

For **every verse in 37–51**, `tools/enoch.py` reports:

```
Qumran Aramaic     ABSENT — version exists, does not attest this verse
Latin Fragments    ABSENT — version exists, does not attest this verse
Greek              ABSENT — version exists, does not attest this verse
```

The only witnesses that ever appear are **Ethiopic** — the base text plus the manuscript `p` (John Rylands Ethiopic 23) and `Bertalotto`'s orthographic correction of `p`. That is one late Ethiopic manuscript tradition and nothing else.

The transmission chain for this block, with the surviving links marked:

```
Aramaic original   LOST   — no scroll, no fragment, nothing
      ↓
Greek translation  LOST   — nothing for 37–51
      ↓
Ge'ez translation  SURVIVES  ← the entire evidence base
```

**A Ge'ez word here is a translation of a translation, and neither of the two upstream texts exists to check it against.** Where the Ge'ez is corrupt, we cannot know it. Where the Ge'ez translator guessed, we inherit the guess with no way to see the seam.

## 🛑🛑 …AND IT IS THE MOST DOCTRINALLY WEIGHTED PART OF THE BOOK

These two facts belong side by side, and are almost never printed that way:

| | |
|---|---|
| **Attestation** | the *worst* in 1 Enoch — one language, one late manuscript family |
| **Doctrinal weight** | the *heaviest* in 1 Enoch — `ወልደ፡ሰብእ` "son of man", `ኅሩይ` "chosen one", `እግዚአ፡መናፍስት` "lord of spirits", the throne of glory, the pre-existent name |

The three phrases that have carried the most theological freight out of 1 Enoch into later reading are **exactly** the phrases with the least evidence behind them. Nothing in this block can be corroborated, and nothing in this block is minor.

⚠️ As with `translations/enoch-6.md`: these semantic ranges are **not validator-gated** — `ranges/*.json` and `verify_ranges.py` are Hebrew-only. Stated, not papered over.

⚠️ **Conjectures are not manuscripts.** No reading below is attributed to Charles, Dillman, Dindorf, Goar, Swete, Lods, Black, Bonner, Kenyon, F-R, Gizeh\*, Syncellus2, TertullianB or Ε. Where `enoch.py` would have printed one it is suppressed; none arose in this block, because the apparatus here carries only `p` and `Bertalotto`.

---

# ⭐⭐ THE THREE TITLES — measured, then read from Dillmann's Latin

`tools/geezroot.py` gives the distribution; Dillmann gives the range. Neither gives English.

## 1. `እግዚአ፡መናፍስት` — the compound formula

```
./tools/geezroot.py --lemma መናፍስት   →  112 occurrences, 111 as bare መናፍስት
./tools/geezroot.py --lemma እግዚአ     →  149 occurrences
```

Of the 112 `መናፍስት`, **110 fall inside chapters 37–71.** The only two outside are 16:1 and 108:7. The formula is not a feature of 1 Enoch; it is a feature of *this section*, and it is dense here — 51 of the 112 land in my fifteen chapters alone.

### 🛑 FINDING 1 — Dillmann files BOTH halves of the formula in non-divine classes

This is the first of my two lexicon findings, and it is not a nuance.

**`መንፈስ` (pl. `መንፈሳት` *and* `መናፍስት`)** — Dillmann's entry runs:

> `መንፈስ፡ subst., m. et f., Pl. መንፈሳት፡ et መናፍስት, spiritus, τὸ πνεῦμα,`
> **1)** *halitus, spiritus* — cited at **Hen. 14, 2** and **108, 9**
> **2)** *ventus* — cited at **Hen. 70, 3**
> **3)** *anima, vis vitalis, vita*
> **4)** *animus, spiritus hominis, quatenus eo continentur affectus et commotiones, voluntas, intellectus*
> **5a)** *spiritus divinus*
> **5b)** *natura incorporalis, angeli, daemones, genii* — **`አግዚአ፡መናፍስት Hen. 38, 2 ...`** and *`መንፈሳት፡ Hen. 39, 12`*, and *`genii naturae rerum praepositi Hen. 60, 16 seq.`*
> **5c)** *spiritus vel animae mortuorum* — cited at **Hen. 22, 3. 5. 103, 3**
> **5d)** *spectrum*

🛑 Dillmann places the plural of the title's second half under **5b — angels, demons, *genii*** — the class of *incorporeal natures*, explicitly including **daemones**, and explicitly including **`genii naturae rerum praepositi`**, "tutelary spirits set over the natures of things." He is *not* placing it under 5a (*divinus*) or 5c (*of the dead*).

⭐ And the identical noun means **wind** (2) and **breath** (1) inside 1 Enoch itself, on Dillmann's own citations — Hen. 70:3 for *ventus*, Hen. 14:2 for *halitus*. The word does not become a technical term by being pluralised.

**`እግዚእ`** — Dillmann's entry runs:

> `dominus`
> **a)** *herus servorum* — master of slaves, owner (Gen. 24; Matth. 10, 24; Tit. 2, 9)
> **b)** *dominator* … *eo, cujus quis dominus est* — with `አግዚአ፡ዙሉ፡ብሔር` "lord of the whole land" (Judith 2, 5), `አግዚአ፡አጋአዝት` (Dan. 2, 47), `አግዚአ፡ለሰንበት` "lord of the sabbath" (Marc. 2, 28), **and `አግዚአ፡መናፍስት Hen. 38, 2 seq.`**
> **c)** *in specie de Deo et Christo*
> **d)** *honoris causa in compellandis aliis* — courtesy address
> **e)** `አጋእዝት` = *κυριότητες*, "one of the nine orders of angels" — **cited at `Hen. 61, 10`**

🛑 **Dillmann files `እግዚአ፡መናፍስት` under (b), the plain "master-of-X" construction — alongside "master of the house", "lord of the sabbath", "owner of the ox" — and NOT under (c), the divine class.** He had (c) available on the same page and did not use it here.

⭐ Note (e): the *plural* of the same noun, `አጋእዝት`, is a **rank of angels** in Ge'ez, and Dillmann's citation for that is **Hen. 61:10 — inside the Parables**. So this section uses the word `እግዚእ` for created beings too.

**Therefore the formula's honest range is:**

> **`እግዚአ፡መናፍስት` = (Master | Owner | Lord | Ruler) of the (spirits | breaths | winds | lives | incorporeal natures | angels | daemons | tutelary genii)**

Nothing in the Ge'ez, and nothing in Dillmann, narrows that to one reading. **Every occurrence below prints the range.** After the first few chapters I abbreviate it as `[LoS-range]` to keep the text readable, but the range is never revoked and never resolved.

## 2. `ኅሩይ` — the chosen/elect one

```
./tools/geezroot.py --lemma ኅሩይ  →  15 occurrences
   8:1 · 40:5 · 45:3 · 49:2 · 49:4 · 51:3 · 51:5 · 52:6 · 52:9
   53:6 · 61:5 · 61:8 · 61:10 · 62:1 · 93:8
```

### ⭐⭐ FINDING 2 — Dillmann gives `ኅሩይ` a fourth sense that has never been printed in this title: *arbiter, conciliator, mediator*

Dillmann's entry, in full sense-structure:

> `ኅሩይ part., fem. ኅሪት`
> **1)** *electus, selectus* — chosen, picked out. Cited at **Hen. 1, 1. 8. 5, 7. 8. 38, 2. 40, 5**; "de sanctis et justis" (Matth. 24, 22); "de angelis" (1 Tim. 5, 21); "**de Messia** Asc. Jes. 8, 7; **Hen. 40, 5**"
> **2)** *praestans* (ἐκλεκτός) — outstanding, choice, of the best quality (Gen. 41, 5. 7)
> **3)** *acceptus, gratus, approbatus* (δεκτός) — accepted, pleasing, approved (Jes. 49, 8; Luc. 4, 19; 2 Cor. 6, 2)
> **4)** ***arbiter** (a litigantibus electus), **conciliator**, **mediator*** — Job 9, 33; Gal. 3, 19. 20; 1 Tim. 2

🛑 **Sense 4 is a live, documented sense of the exact participle, and it means *the arbitrator the disputing parties have chosen* — an umpire, a go-between.** Dillmann's citations for it are Job 9:33 (the umpire who could lay a hand on both parties) and Galatians 3:19–20 / 1 Timothy 2 (μεσίτης, *mediator*).

⭐ The figure this title names in 37–51 is the one who **sits to judge** (45:3, 51:3) and before whom the disputing parties are brought. Sense 1 and sense 4 are the *same word in the same form*, and both fit the passages. One of them has been printed for centuries; the other has not been printed at all.

⚠️ Both readings stay on the page below. `ኅሩይ` is rendered **(chosen | selected | choice | excellent | accepted | approved | arbiter | mediator)** at first occurrence, and thereafter `(chosen | choice | approved | arbiter)` for brevity — never resolved.

⭐ Note `ኅሩይ` at **8:1**, in the Watchers material where the Greek and Aramaic *do* survive: there it qualifies `እብን፡ክቡር፡ወኅሩይ`, stones — sense 2, *praestans*, "choice." Same word, same form, plainly non-personal. That is the one place in 1 Enoch where the word can be seen doing ordinary work.

## 3. `ወልደ፡ሰብእ` — the son-of-man phrase

Measured across the whole Parables section, **the Ge'ez does not use one fixed phrase**:

| verse | Ge'ez |
|---|---|
| 46:2, 46:3, 46:4, 48:2 | `ወልደ፡ሰብእ` |
| 60:10, 69:10 | `ወልደ፡ሰብእ` |
| 62:5, 69:29, 71:14 | **`ወልደ፡ብእሲ`** |

Inside 37–51 **all four occurrences are `ወልደ፡ሰብእ`**; the switch to `ወልደ፡ብእሲ` begins at 62:5, outside this block. The two nouns are not synonyms in Dillmann:

- **`ሰብእ`** — *homo* collectively, **humankind**; the plural sense is built in. (Cf. `enoch-6.md` 6:1, where `ውሉደ፡ሰብእ` is humanity, not males.)
- **`ብእሲ`** — Dillmann: **1)** *vir* — **a)** *opp. feminae: mas, masculus* (male as against female); **b)** *opp. pueris et senibus: vir fortis* (a man in his strength, as against boys and old men); **c)** *opp. uxori: maritus* (husband); **2)** *homo, ἄνθρωπος*.

⭐ So `ወልደ፡ሰብእ` is unambiguously **"child of humankind"**, while `ወልደ፡ብእሲ` carries *male / husband / grown man* as its first sense and "human being" only as its second. **The Ge'ez Parables alternate between them and nothing survives upstream to tell us whether the alternation is in the source or is the Ge'ez translator's variation.** That is stated and left open.

Rendered below as **(son | child) of (humankind | the human | a human being)**.

---

# THE TEXT

> `( | )` marks a word whose Ge'ez carries more than one sense in Dillmann. **No sense is preferred.**
> Every verse is followed by its witness line. In this block that line is always the same, and it always says so.

---

## Chapter 37 — the superscription

### 37:1

**ራእይ፡ ዘርእየ፡ ካልአ፡ ራእየ፡ ጥበብ፡ ዘርእየ፡ ሄኖክ፡ ወልደ፡ ያሬድ፡ ወልደ፡ መላልኤል፡ ወልደ፡ ቃይናን፡ ወልደ፡ ሄኖስ፡ ወልደ፡ ሴት፡ ወልደ፡ አዳም።**

*raʾəyə zärəʾəyä kaləʾä raʾəyä ṭəbäbə zärəʾəyä henokə wälədä yaredə wälədä mälaləʾelə wälədä qayənanə wälədä henosə wälədä setə wälədä ʾädamə*

**A (vision | sight | thing-seen) that he saw — a second (vision | sight) of (wisdom | prudence | understanding | knowledge | skill | craft), which Henok saw: son of Yared, son of Malalʾel, son of Qaynan, son of Henos, son of Set, son of ʾAdam.**

- `ራእይ` *raʾəyə* and `ራእየ` *raʾəyä* — the same noun twice, the second in construct. Both from `ርእየ` "to see"; the noun is the *act* or *object* of seeing, not narrowed to a prophetic technical term.
- `ጥበብ` *ṭəbäbə* — Dillmann: **1)** *sapientia, prudentia, intelligentia, scientia, disciplina*; sub-senses **a)** *philosophia*, **b)** *medicina*, **c)** *astronomia*; **2)** *peritia, ars, scientia* — practical skill, craft. The word is not confined to the moral-religious sense.
- ⭐ `ወልደ፡ያሬድ` — Yared is the same name that carries the buried `ירד` "descend" pun in the Aramaic of 6:6 (see `enoch-6.md`). Here it is only a name; **there is no Aramaic for this chapter to check it against.**

**Witness:** Ethiopic only — `[Bertalotto p]` reads `ካልእ` for `ካልአ` and `ወልድ፡መላልኤል` for `ወልደ፡መላልኤል` (construct-state orthography, no sense difference).
🛑 **GE'EZ ALONE** — Greek, Latin and Qumran Aramaic all absent.

### 37:2

**ወዝ፡ ርእሱ፡ ለነገረ፡ ጥበብ፡ ዘአንሣእኩ፡ እትናገር፡ ወእብል፡ ለእለ፡ የኀድሩ፡ ዲበ፡ የብስ፡ ስምዑ፡ ቀደምት፡ ወርእዩ፡ ደኃርያን፡ ነገረ፡ ቅዱሰ፡ እለ፡ እነግር፡ ቅድመ፡ እግዚአ፡ መናፍስት።**

*wäzə rəʾəsu länägärä ṭəbäbə zäʾänəśaʾəku ʾətənagärə wäʾəbələ läʾəlä yäḫädəru dibä yäbəsə səməʿu qädämətə wärəʾəyu däḫarəyanə nägärä qədusä ʾəlä ʾənägərə qədəmä ʾəgəziʾä mänafəsətə*

**And this is the (head | beginning | chief part | sum) of the (word | speech | matter | affair) of (wisdom | understanding | skill), which I took up to speak and to say to those who (dwell | lodge | abide) upon the dry land: Hear, you former ones, and see, you later ones — the (holy | sacred | consecrated) word which I speak before the (Master | Owner | Lord | Ruler) of the (spirits | breaths | winds | lives | incorporeal natures | angels | daemons | tutelary genii).**

- `ርእሱ` *rəʾəsu* — literally "his/its head." Ge'ez `ርእስ` covers *head, top, beginning, chief thing, self*. "The head of the word" can be the *opening* of the discourse or its *substance*. Both stand.
- `ነገር` *nägär* — *word, speech, matter, thing, affair* — the same breadth as Hebrew דבר; not narrowed to "utterance."
- `የብስ` *yäbəsə* — the **dry land**, as against the sea. Not "the earth" as a globe.
- `ቀደምት` / `ደኃርያን` — "the former/earlier ones" and "the later/last ones." Whether these are earlier and later *people* or earlier and later *generations* is not marked in the Ge'ez.
- ⚠️ Note the pairing: the former ones are told to **hear**, the later ones to **see**. The verbs are not interchangeable in the Ge'ez and are kept distinct.

**Witness:** Ethiopic only — `p` `የኃድሩ` vs `Bertalotto` `የኀድሩ` (ኀ/ኃ, orthographic); `[Bertalotto p]` reads `ሰምዑ` for `ስምዑ` and `ቅዱስ` for `ቅዱሰ` (the latter shifts the word from accusative to nominative — a real, if small, syntactic variant).
🛑 **GE'EZ ALONE.**

### 37:3

**እሉ፡ ቀዳሚ፡ ይኄይስ፡ ብሂል፡ ወደኃርያንሂ፡ ኢንከልእ፡ ርእሳ፡ ለጥበብ።**

*ʾəlu qädami yəḫeyəsə bəhilə wädäḫarəyanəhi ʾinəkäləʾə rəʾəsa läṭəbäbə*

**These — to the first ones it is (better | preferable | more excellent) to say; and to the later ones also we do not (withhold | refuse | prohibit | keep back) the (head | beginning | chief part) of the (wisdom | understanding).**

- `ይኄይስ` *yəḫeyəsə* — comparative "is better / is preferable." The sentence is elliptical in the Ge'ez and the syntax is genuinely hard: `እሉ፡ቀዳሚ፡ይኄይስ፡ብሂል` could be "to these former ones it is better to speak" or "these first — it is better to say." **The Ge'ez does not disambiguate and nothing upstream survives to arbitrate.** Left as it stands.
- `ኢንከልእ` *ʾinəkäləʾə* — first person **plural**, "we do not withhold," in a discourse otherwise in the first person singular (`እትናገር`, `እብል`, `እነግር` in 37:2). ⚠️ The person shift is in the text; it is not smoothed here.
- `ርእሳ፡ለጥበብ` — again "the head of wisdom," picking up `ርእሱ፡ለነገረ፡ጥበብ` in 37:2.

**Witness:** Ethiopic only — `[Bertalotto p]` `ይሄይስ` for `ይኄይስ` (ሄ/ኄ, orthographic).
🛑 **GE'EZ ALONE.**

### 37:4

**ወእስከ፡ ይእዜ፡ ኢተውህበኒ፡ እምቅድመ፡ እግዚአ፡ መናፍስት፡ ዘነሣእኩ፡ ጥበበ፡ በከመ፡ ኀለይኩ፡ በከመ፡ ፈቀደ፡ እግዚአ፡ መናፍስት፡ ዘተውህበኒ፡ እምኔሁ፡ ክፍለ፡ ሕይወት፡ ዘለዓለም።**

*wäʾəsəkä yəʾəze ʾitäwəhəbäni ʾəməqədəmä ʾəgəziʾä mänafəsətə zänäśaʾəku ṭəbäbä bäkämä ḫäläyəku bäkämä fäqädä ʾəgəziʾä mänafəsətə zätäwəhəbäni ʾəmənehu kəfəlä ḥəyəwätə zäläʿalämə*

**And until now there was not given to me, from before the (Master | Owner | Lord) of the (spirits | breaths | winds | lives | angels | daemons | genii), such (wisdom | understanding) as I have taken, according as I (thought | considered | reckoned | devised) — according as the (Master | Owner | Lord) of the (spirits | breaths | winds | …) (willed | desired | decreed): that there be given to me from him a (portion | share | division) of (life | living) (of eternity | everlasting | of the age).**

- `ኀለይኩ` *ḫäläyəku* — *to think, consider, reckon, plan, devise*. Not "understand"; the verb is deliberative.
- `ፈቀደ` *fäqädä* — *to will, wish, desire, decree, require*. Volition and decree are one word.
- `ዘለዓለም` *zäläʿalämə* — `ዓለም` is *saeculum / aion* as much as *aeternitas*: **"of the age"** and **"everlasting"** are the same phrase. Kept doubled.
- ⚠️ `ኢተውህበኒ ... ዘነሣእኩ` — "it was not given to me ... which I took." The negative and the relative pull against each other; the sense is most likely "no such wisdom had been given me before as the wisdom I now received," but the Ge'ez as written is awkward and is reported awkward.

**Witness:** Ethiopic only — `[Bertalotto p]` omits the opening `ወ`, reading `እስከ` for `ወእስከ`; `p` `ሀለይኩ` vs `Bertalotto` `ኀለይኩ` (ሀ/ኀ).
🛑 **GE'EZ ALONE.**

### 37:5

**ወኮኑ፡ ብየ፡ ሠለስቱ፡ ምሳሌያት፡ ወአንሰ፡ እብሎሙ፡ ለእለ፡ የኀድሩ፡ ዲበ፡ የብስ።**

*wäkonu bəyä śäläsətu məsaleyatə wäʾänəsä ʾəbəlomu läʾəlä yäḫädəru dibä yäbəsə*

**And there were with me three (parables | likenesses | comparisons | proverbs | riddles | enigmas | aphorisms), and I for my part speak them to those who (dwell | lodge | abide) upon the dry land.**

- ⭐ `ምሳሌ` *məsale* — Dillmann heads the entry ***assimilatio, comparatio***, then: **1)** *parabola, similitudo, proverbium, **aenigma**, sententiose dictum, dicterium* — παραβολή, παροιμία. **He cites this very verse: `Hen. 37, 5 seq.`** and `Hen. 68, 1`.
  🛑 **"Parable" is one item in a list that also contains *riddle* and *proverb*.** The section's own name for itself is not fixed to the narrative-parable sense. The three ምሳሌያት of 38–44, 45–57 and 58–69 could as fairly be called three *riddles* or three *likenesses*.
  ⚠️ Dillmann separately notes that the plural spelling `ምሳለያት` at Asc. Jes. 4:21 *errori librarii debetur* — is owed to a scribal error. Our base text here reads `ምሳሌያት` (with ሌ, not ለ), so it is not that form; noted only so the distinction is on record.

**Witness:** Ethiopic only — and this is the **largest variant in the chapter**: `[Bertalotto p]` reads `ወኮኑ፡ብየ፡፫ምሳሌ፡ወአነ፡አንሣእኩ፡እንዘ፡እብሎሙ` — the numeral `፫` with the **singular** `ምሳሌ`, and an extra verb `አንሣእኩ፡እንዘ` ("I took up, while [I] speak them") absent from the base text. `p` `የሐድሩ` vs `Bertalotto` `የኀድሩ`. The verse ends `የብስ።ድ` in the manuscripts — a stray `ድ`.
🛑 **GE'EZ ALONE** — and with the base text and `p` disagreeing on a whole verb, there is no third witness to break the tie.

---

## Chapter 38 — the first parable: the congregation of the righteous

### 38:1

**ምሳሌ፡ ቀዳሚ፡ ሶበ፡ ያስተርኢ፡ ማኅበረ፡ ጻድቃን፡ ወይትኴነኑ፡ ኃጥኣን፡ በኀጢአቶሙ፡ ወእምገጸ፡ የብስ፡ ይትሀወኩ።**

*məsale qädami sobä yasətärəʾi maḫəbärä ṣadəqanə wäyətəkwenänu ḫaṭəʾanə bäḫäṭiʾätomu wäʾəməgäṣä yäbəsə yətəhäwäku*

**The first (parable | likeness | comparison | proverb | riddle): when the (congregation | assembly | company | society) of the (righteous | just) appears, and the (sinners | offenders) are (judged | condemned | brought to trial) for their (sin | offence | error), and from the face of the dry land they are (troubled | agitated | driven in confusion | thrown into tumult).**

- `ማኅበር` *maḫəbär* — Dillmann: *congregatio, coetus, societas*. A gathering; not an institution.
- `ይትኴነኑ` *yətəkwenänu* — passive of `ኰነነ`, which covers both **to judge** and **to condemn**. Ge'ez does not separate the trial from the verdict here.
- `ይትሀወኩ` *yətəhäwäku* — *to be agitated, disturbed, thrown into confusion, driven*. Whether they are *driven off* the land or *thrown into turmoil* on it is not decided by the Ge'ez.

**Witness:** Ethiopic only — `[Bertalotto p]` `በኃጢአቶሙ` (ኃ for ኀ) and `ይትሐወኩ` (ሐ for ሀ); orthographic. The manuscripts end the verse with a continuing `፡` rather than the base text's `።`.
🛑 **GE'EZ ALONE.**

### 38:2

**ወሶበ፡ ያስተርኢ፡ ጻድቅ፡ በገጾሙ፡ ለጻድቃን፡ እለ፡ ኅሩያን፡ ተግባሮሙ፡ ስቁል፡ በእግዚአ፡ መናፍስት፡ ወያስተርኢ፡ ብርሃን፡ ለጻድቃን፡ ወለኅሩያን፡ እለ፡ የኀድሩ፡ ዲበ፡ የብስ፡ አይቴ፡ ማኅደረ፡ ኃጥኣን፡ ወአይቴ፡ ምዕራፎሙ፡ ለእለ፡ ክሕድዎ፡ ለእግዚአ፡ መናፍስት፡ እምኀየሶሙ፡ ሶበ፡ ኢተወልዱ።**

*wäsobä yasətärəʾi ṣadəqə bägäṣomu läṣadəqanə ʾəlä ḫəruyanə tägəbaromu səqulə bäʾəgəziʾä mänafəsətə wäyasətärəʾi bərəhanə läṣadəqanə wäläḫəruyanə ʾəlä yäḫädəru dibä yäbəsə ʾäyəte maḫədärä ḫaṭəʾanə wäʾäyəte məʿərafomu läʾəlä kəḥədəwo läʾəgəziʾä mänafəsətə ʾəməḫäyäsomu sobä ʾitäwälədu*

**And when the (righteous one | just one | Righteous One) appears before the face of the (righteous | just), those who are (chosen | selected | choice | excellent | accepted | approved | arbiters | mediators) — whose work is (hung | suspended | made to depend | fastened | clinging | weighed) upon the (Master | Owner | Lord) of the (spirits | breaths | winds | lives | angels | daemons | genii) — and light appears to the (righteous | just) and to the (chosen | choice | approved) who (dwell | abide) upon the dry land: where then is the (dwelling | lodging | habitation) of the (sinners | offenders), and where their (resting-place | station | halting-place) — those who (denied | disowned | renounced | were faithless to) the (Master | Owner | Lord) of the (spirits | …)? It had been better for them had they not been born.**

- ⭐⭐ `ስቁል` *səqulə` — **this is the key word of the verse, and Dillmann cites this exact clause.** `ስቁል` is the participle of `ሰቀለ`, whose senses Dillmann gives as **1)** *suspendere* (to hang), **2)** *suspendio necare, suspendere in … cruce; crucifigere* (to hang to death, to crucify), **3)** *ponderare* (to weigh). The participle he then splits: **1)** *suspensus; in specie crucifixus*, **2)** *suspensus, pendens, pendulus, adhaerens, affixus*, **3)** *ponderatus*.
  Under sense **2** he prints our clause verbatim: `ተግባሮሙ፡ስቁል፡በአግዚአ፡መናፍስት Hen. 38, 2. 40, 5. 46, 8.`
  🛑 So `ተግባሮሙ፡ስቁል` is at minimum **"their work hangs upon / depends on / clings to"** the Lord of Spirits — and the same participle in the same lexicon also means ***weighed*** (in a balance) and ***crucified***. The image of deeds *hanging in the balance* and deeds *depending on* a patron are not distinguished by this word. Both printed.
- `ጻድቅ` singular against `ጻድቃን` plural in the same clause — the Ge'ez sets one *righteous one* against the *righteous ones*. Whether the singular is a title or a generic is not marked.
- `ክሕድዎ` *kəḥədəwo* — *to deny, disown, renounce, be faithless to, apostatise*. Covers both intellectual denial and broken allegiance.
- `ምዕራፍ` *məʿəraf* — a *resting-place, halting-place, station* (from `ዐረፈ`, to rest). Not "reward."

**Witness:** Ethiopic only — `[Bertalotto p]` `ለጸድቃን` (ጸ for ጻ, first instance only) and `እምሐየሶሙ` (ሐ for ኀ); `p` `የኃድሩ` vs `Bertalotto` `የኀድሩ`. All orthographic.
🛑 **GE'EZ ALONE** — and this is one of the three verses in all of 1 Enoch that carries `ተግባሮሙ፡ስቁል`. Nothing outside Ethiopic attests any of the three.

### 38:3

**ወሶበ፡ ይትከሠታ፡ ኅቡኣቲሆሙ፡ ለጻድቃን፡ ይትኴነኑ፡ ኃጥኣን፡ ወይትሀወኩ፡ ረሲዓን፡ እምገጸ፡ ጻድቃን፡ ወኅሩያን።**

*wäsobä yətəkäśäta ḫəbuʾatihomu läṣadəqanə yətəkwenänu ḫaṭəʾanə wäyətəhäwäku räsiʿanə ʾəməgäṣä ṣadəqanə wäḫəruyanə*

**And when the (hidden things | secrets | concealed things) of the (righteous | just) are (revealed | uncovered | disclosed | opened), the (sinners | offenders) are (judged | condemned), and the (wicked | impious | ungodly) are (troubled | agitated | driven) from before the face of the (righteous | just) and the (chosen | choice | approved | arbiters).**

- ⚠️ `ኅቡኣቲሆሙ፡ለጻድቃን` — "the hidden things **of** the righteous." Whether these are secrets *belonging to* the righteous, secrets *concerning* them, or secrets *kept for* them is undetermined; Ge'ez `ለ` + noun after a construct is a resumptive genitive and does not specify. Printed unresolved.
- `ረሲዓን` *räsiʿanə* — *impii*, the wicked/ungodly; a different word from `ኃጥኣን` "sinners" in the same verse. The two are not collapsed here.

**Witness:** Ethiopic only — `[Bertalotto p]` identical to the base text.
🛑 **GE'EZ ALONE.**

### 38:4

**ወእምይእዜ፡ ኢይከውኑ፡ አዚዛነ፡ ወኢ፡ ልዑላነ፡ እለ፡ ይእኅዝዋ፡ ለምድር፡ ወኢይክሉ፡ ርእየ፡ ገጸ፡ ቅዱሳን፡ እስመ፡ ለእግዚአ፡ መናፍስት፡ ተርእየ፡ ብርሃኑ፡ ለገጸ፡ ቅዱሳን፡ ጻድቃን፡ ወኅሩያን።**

*wäʾəməyəʾəze ʾiyəkäwənu ʾäzizanä wäʾi ləʿulanä ʾəlä yəʾəḫəzəwa lämədərə wäʾiyəkəlu rəʾəyä gäṣä qədusanə ʾəsəmä läʾəgəziʾä mänafəsətə tärəʾəyä bərəhanu lägäṣä qədusanə ṣadəqanə wäḫəruyanə*

**And from now they shall not be (mighty | powerful | strong), nor (exalted | high | lofty) — those who (hold | seize | grasp | possess) the earth — and they shall not be able to see the face of the (holy ones | saints | consecrated ones); for the light of the (Master | Owner | Lord) of the (spirits | breaths | winds | angels | daemons | genii) has appeared upon the face of the (holy | consecrated) ones, the (righteous | just) and the (chosen | choice | approved | arbiters).**

- `ይእኅዝዋ፡ለምድር` — `አኀዘ` is *to take hold of, seize, grasp, hold, possess*. It carries both "own" and "grip by force." The verse does not choose.
- ⚠️ `ለእግዚአ፡መናፍስት፡ተርእየ፡ብርሃኑ` — the `ለ` marks a dative/possessive: literally "to/of the Lord of Spirits appeared his light." "His light appeared" and "there appeared, for the Lord of Spirits, light" are both grammatical. Printed as the former, with the alternative recorded here.

**Witness:** Ethiopic only — `p` `አዚዛን` vs `Bertalotto` `ዐዚዛን` (አ/ዐ, orthographic); `[Bertalotto p]` writes `ወኢልዑላነ` as one word against the base text's `ወኢ፡ልዑላነ`.
🛑 **GE'EZ ALONE.**

### 38:5

**ወነገሥት፡ አዚዛን፡ በውእቱ፡ ጊዜ፡ ይትሀጐሉ፡ ወይትወሀቡ፡ ውስተ፡ እደ፡ ጻድቃን፡ ወቅዱሳን።**

*wänägäśətə ʾäzizanə bäwəʾətu gize yətəhägwälu wäyətəwähäbu wəsətä ʾədä ṣadəqanə wäqədusanə*

**And the (mighty | powerful) kings in that time shall be (destroyed | perish | be ruined | be undone), and shall be given into the hand of the (righteous | just) and the (holy | consecrated) ones.**

- `ይትሀጐሉ` *yətəhägwälu* — passive/reflexive of `አህጐለ` "to destroy, ruin, cause to perish." Whether they *perish* or *are destroyed* is not distinguished by the stem here.

**Witness:** Ethiopic only — `p` `አዚዛን` vs `Bertalotto` `ዐዚዛን`; `[Bertalotto p]` `ይትኃጐሉ` for `ይትሀጐሉ`. Orthographic.
🛑 **GE'EZ ALONE.**

### 38:6

**ወእምህየ፡ አልቦ፡ ዘያስተምሕር፡ ሎሙ፡ ኀበ፡ እግዚአ፡ ስብሐት፡ እስመ፡ ተወድአ፡ እንቲኣሆሙ፡ ሕይወት።**

*wäʾəməhəyä ʾäləbo zäyasətäməḥərə lomu ḫäbä ʾəgəziʾä səbəḥätə ʾəsəmä täwädəʾä ʾənətiʾahomu ḥəyəwätə*

**And from then there is none who (intercedes | entreats mercy | begs pardon) for them with the (Master | Owner | Lord) of (glory | praise | honour), for their life is (finished | completed | used up | at an end).**

- ⭐ `ያስተምሕር` *yasətäməḥərə* — causative-reflexive of `ምሕረ` "to have mercy": *to seek mercy for, to intercede, to beg pardon on another's behalf*. The action is petitioning, not forgiving.
- 🛑 **TITLE VARIANT.** The base text reads **`እግዚአ፡ስብሐት`** — "Lord of **glory/praise**" — where `[Bertalotto p]` reads **`እግዚአ፡መናፍስት`**, the standard formula. ⚠️ This is a substantive divergence *in the title itself*, not orthography, and there is **no Greek and no Aramaic to arbitrate it**. Either the base text preserves a variant epithet that `p` levelled to the section's formula, or the base text is corrupt. **Undecidable on the surviving evidence.** Both readings printed; neither preferred.
- `ተወድአ` *täwädəʾä* — *to be finished, completed, exhausted, come to an end*.

**Witness:** Ethiopic only — `[Bertalotto p]` `እልቦ` for `አልቦ`, `እንቲአሆሙ` for `እንቲኣሆሙ` (orthographic), and the substantive `መናፍስት` for `ስብሐት` noted above; `p` `ዘያስተምህር` vs `Bertalotto` `ዘያስተምሕር` (ህ/ሕ).
🛑 **GE'EZ ALONE.**

---

## Chapter 39 — the dwellings of the righteous, and the sleepless ones

> From here on `[LoS]` abbreviates the full range established above: **(Master | Owner | Lord | Ruler) of the (spirits | breaths | winds | lives | incorporeal natures | angels | daemons | tutelary genii)**. The abbreviation is typographic only. **The range is never resolved.**

### 39:1

**ወይከውን፡ በዝንቱ፡ መዋዕል፡ ይወርዱ፡ ደቂቅ፡ ኅሩያን፡ ወቅዱሳን፡ እምልዑላን፡ ሰማያት፡ ወአሐደ፡ ይከውን፡ ዘርዖሙ፡ ምስለ፡ ውሉደ፡ ሰብእ።**

*wäyəkäwənə bäzənətu mäwaʿələ yəwärədu däqiqə ḫəruyanə wäqədusanə ʾəmələʿulanə sämayatə wäʾäḥädä yəkäwənə zärəʿomu məsəlä wəludä säbəʾə*

**And it shall be, in these days, that (children | offspring | little ones), (chosen | choice | approved | arbiters) and (holy | consecrated), shall come down from the (high | lofty | exalted) heavens, and their seed shall become one with the (children | offspring) of (humankind | humanity).**

- ⭐ `ይወርዱ` *yəwärədu* — **the descent verb**, the same root that in the Aramaic of 6:6 puns on the name Yared (`enoch-6.md`). Here the descent of `ደቂቅ፡ኅሩያን፡ወቅዱሳን` mixing seed with humanity restates the Watchers episode of chapters 6–7 in this section's vocabulary. **No Aramaic survives here**, so whether the pun was ever in this passage cannot be known.
- `ደቂቅ` *däqiqə* — *children, sons, offspring, little ones*; the singular `ደቅ` also means *small*.
- ⚠️ Nothing in the Ge'ez marks whether this descent is approved or transgressive. The words `ኅሩያን` and `ቅዱሳን` are the same words used of the redeemed throughout this chapter.

**Witness:** Ethiopic only — `[Bertalotto p]` writes the numeral `፩` for `አሐደ` and `ዘርኦሙ` for `ዘርዖሙ`.
🛑 **GE'EZ ALONE.**

### 39:2

**ወበውእቱ፡ መዋዕል፡ ነሥአ፡ ሄኖክ፡ መጻሕፍተ፡ ቅንአት፡ ወመዓት፡ ወመጻሕፍተ፡ ጕጕአ፡ ወሀውክ፡ ወምሕረት፡ ኢይከውን፡ ላዕሌሆሙ፡ ይቤ፡ እግዚአ፡ መናፍስት።**

*wäbäwəʾətu mäwaʿələ näśʾä henokə mäṣaḥəfətä qənəʾätə wämäʿatə wämäṣaḥəfətä gwəgwəʾa wähäwəkə wäməḥərätə ʾiyəkäwənə laʿəlehomu yəbe ʾəgəziʾä mänafəsətə*

**And in those days Henok took (books | writings | scrolls) of (zeal | jealousy | ardour) and of (wrath | anger | fury), and (books | writings) of (haste | urgency | agitation) and of (confusion | tumult | disturbance) — and mercy shall not be upon them, said the [LoS].**

- `መጻሕፍት` *mäṣaḥəfət* — plural of `መጽሐፍ`, *a writing, book, letter, document*. Not necessarily a codex.
- `ቅንአት` *qənəʾätə* — *zelus*: covers **jealousy** and **zeal/ardour** without distinction, as does its Semitic cognate.
- `ጕጕአ` / `ሀውክ` — *haste, eagerness* and *disturbance, tumult*. Whether these name the books' contents or their effect is not determined.

**Witness:** Ethiopic only — `[Bertalotto p]` drops the initial `ወ`; `p` `ቅንዓት` vs `Bertalotto` `ቅንአት`; `[Bertalotto p]` `ጒጕኣ` for `ጕጕአ`. Orthographic.
🛑 **GE'EZ ALONE.**

### 39:3

**ወበውእቱ፡ ጊዜ፡ መሠጠኒ፡ ደመና፡ ወዐውሎ፡ ነፋስ፡ እምነ፡ ገጻ፡ ለምድር፡ ወአንበረኒ፡ ውስተ፡ ጽንፈ፡ ሰማያት።**

*wäbäwəʾətu gize mäśäṭäni dämäna wäʿäwəlo näfasə ʾəmənä gäṣa lämədərə wäʾänəbäräni wəsətä ṣənəfä sämayatə*

**And at that time a cloud (snatched | seized | tore) me away, and a whirlwind of wind, from the face of the earth, and set me down at the (edge | border | extremity | hem) of the heavens.**

- ⭐ `ነፋስ` *näfasə* — "wind." ⚠️ **Note carefully:** this is a *different* noun from `መንፈስ` (the singular behind `መናፍስት`) — but Dillmann's `መንፈስ` entry gives *ventus*, "wind," as its own **sense 2**, citing Hen. 70:3. So Ge'ez has two words for wind here, and one of them is the word in the title. Printed for the reader to weigh; not used to argue.
- `መሠጠ` *mäśäṭä* — *to snatch, tear away, carry off by force*. Violent.

**Witness:** Ethiopic only — `p` `ወዓውሎ` vs `Bertalotto` `ወዐውሎ`; `[Bertalotto p]` `ነፉስ` for `ነፋስ` and `እምገጻ` for `እምነ፡ገጻ`.
🛑 **GE'EZ ALONE.**

### 39:4

**ወበህየ፡ ርኢኩ፡ ካልአ፡ ራእየ፡ ማኅደሪሆሙ፡ ለጻድቃን፡ ወምስካባቲሆሙ፡ ለቅዱሳን።**

*wäbähəyä rəʾiku kaləʾä raʾəyä maḫədärihomu läṣadəqanə wäməsəkabatihomu läqədusanə*

**And there I saw another (vision | sight): the (dwellings | lodgings | habitations) of the (righteous | just | truthful) and the (resting-places | couches | beds) of the (holy | consecrated) ones.**

- ⭐ `ጻድቅ` *ṣadəq* — the root that Dillmann glosses ***verax, justus fuit*** — "was **truthful**, was **just**." Ge'ez `ጽድቅ` accordingly covers **righteousness AND truth** in one noun; Dillmann's citations pair it repeatedly with `ርትዕ` (Jer. 4:2; Jos. 24:14). **Rendered (righteous | just | truthful) throughout, never narrowed.**
- `ምስካብ` *məsəkab* — *a bed, couch, place of lying down*, from `ሰከበ` "to lie down." Rest, not reward.

**Witness:** Ethiopic only — `[Bertalotto p]` inverts word order to `ራእየ፡ካልአ` and reads `ማኅደረሆሙ` for `ማኅደሪሆሙ`.
🛑 **GE'EZ ALONE.**

### 39:5

**ወበህየ፡ ርእያ፡ አዕይንትየ፡ ማኅደሪሆሙ፡ ምስለ፡ መላእክት፡ ወምስካባቲሆሙ፡ ምስለ፡ ቅዱሳን፡ ወይስእሉ፡ ወያስተበቍዑ፡ ወይጼልዩ፡ በእንተ፡ ውሉደ፡ ሰብእ፡ ወጽድቅ፡ ከመ፡ ማይ፡ ይውሕዝ፡ በቅድሜሆሙ፡ ወምሕረት፡ ከመ፡ ጠል፡ ውስተ፡ ምድር፡ ከመ፡ ዝ፡ ውእቱ፡ ማእከሎሙ፡ ለዓለመ፡ ዓለም።**

*wäbähəyä rəʾəya ʾäʿəyənətəyä maḫədärihomu məsəlä mälaʾəkətə wäməsəkabatihomu məsəlä qədusanə wäyəsəʾəlu wäyasətäbäqwəʿu wäyəṣeləyu bäʾənətä wəludä säbəʾə wäṣədəqə kämä mayə yəwəḥəzə bäqədəmehomu wäməḥərätə kämä ṭälə wəsətä mədərə kämä zə wəʾətu maʾəkälomu läʿalämä ʿalämə*

**And there my eyes saw their (dwellings | habitations) with the (angels | messengers), and their (resting-places | couches) with the (holy | consecrated) ones; and they (ask | petition | request) and they (entreat | supplicate | beg earnestly) and they (pray | intercede) on behalf of the (children | offspring) of (humankind | humanity); and (righteousness | justice | truth) flows like water before them, and mercy like dew upon the earth. Thus it is among them for ever and ever.**

- ⭐ **Three distinct verbs of petition in sequence** — `ይስእሉ` (ask/request), `ያስተበቍዑ` (entreat, supplicate urgently; causative-reflexive), `ይጼልዩ` (pray). The Ge'ez piles them; they are not synonyms and are not collapsed here.
- `መላእክት` *mälaʾəkət* — *angeli* **and** *nuntii, legati* — messengers of any kind. The word does not by itself mean a celestial being.

**Witness:** Ethiopic only — `[Bertalotto p]` drops the initial `ወ`, writes `ከመዝ` as one word, and reads `ለዓለም፡ዓለም` for `ለዓለመ፡ዓለም`.
🛑 **GE'EZ ALONE.**

### 39:6

**ወበውእቱ፡ መዋዕል፡ ርእያ፡ አዕይንትየ፡ መካነ፡ ኅሩያን፡ ዘጽድቅ፡ ወዘሃይማኖት፡ ወጽድቅ፡ ይከውን፡ በመዋዕሊሆሙ፡ ለጻድቃን፡ ወኅሩያን፡ ኍልቊ፡ አልቦሙ፡ ቅድሜሁ፡ ለዓለመ፡ ዓለም።**

*wäbäwəʾətu mäwaʿələ rəʾəya ʾäʿəyənətəyä mäkanä ḫəruyanə zäṣədəqə wäzähayəmanotə wäṣədəqə yəkäwənə bämäwaʿəlihomu läṣadəqanə wäḫəruyanə ḫwələqwə ʾäləbomu qədəmehu läʿalämä ʿalämə*

**And in those days my eyes saw the place of the (chosen | choice | approved | arbiters) of (righteousness | justice | truth) and of (faith | fidelity | faithfulness | trust); and (righteousness | justice | truth) shall be in their days; and the (righteous | just | truthful) and the (chosen | choice | approved), of them there is no number before him, for ever and ever.**

- `ሃይማኖት` *hayəmanot* — Dillmann glosses simply ***fides***, with `መሃይምን` = *fidelis*. Latin *fides* covers **belief, trust, fidelity, trustworthiness** in one word, and the Ge'ez inherits the whole span. Not narrowed to "faith" in the creedal sense.

**Witness:** Ethiopic only — `[Bertalotto p]` `መከነ` for `መካነ`, `ወጻድቃን` for `ለጻድቃን` (⚠️ this changes the syntax: "and the righteous" rather than "for the righteous"), and `ኍልቈ` for `ኍልቊ`.
🛑 **GE'EZ ALONE.**

### 39:7

**ወርኢኩ፡ ማኅደሮሙ፡ መትሕተ፡ አክናፈ፡ እግዚአ፡ መናፍስት፡ ወኵሎሙ፡ ጻድቃን፡ ወኅሩያን፡ በቅድሜሁ፡ ይትለሐዩ፡ ከመ፡ ብርሃነ፡ እሳት፡ ወአፉሆሙ፡ ይመልእ፡ በረከተ፡ ወከናፍሪሆሙ፡ ይሴብሕ፡ ስሞ፡ ለእግዚአ፡ መናፍስት፡ ወጽድቅ፡ ቅድሜሁ፡ ኢየኀልቅ፡ ወርትዕ፡ ቅድሜሁ፡ ኢየኀልቅ።**

*wärəʾiku maḫədäromu mätəḥətä ʾäkənafä ʾəgəziʾä mänafəsətə wäkwəlomu ṣadəqanə wäḫəruyanə bäqədəmehu yətəläḥäyu kämä bərəhanä ʾəsatə wäʾäfuhomu yəmäləʾə bäräkätä wäkänafərihomu yəsebəḥə səmo läʾəgəziʾä mänafəsətə wäṣədəqə qədəmehu ʾiyäḫäləqə wärətəʿə qədəmehu ʾiyäḫäləqə*

**And I saw their (dwelling | habitation) beneath the wings of the [LoS]; and all the (righteous | just | truthful) and the (chosen | choice | approved) before him (shine | are radiant | are bright) like the light of fire; and their mouth is full of blessing, and their lips (glorify | praise | magnify) the name of the [LoS]; and (righteousness | justice | truth) before him does not (fail | come to an end | run out), and (rectitude | uprightness | equity | truth) before him does not (fail | come to an end).**

- ⭐🛑 **`አክናፈ፡እግዚአ፡መናፍስት` — "the WINGS of the Lord of Spirits."** The Ge'ez gives this figure wings, here and again at 40:2 (`በአርባዕቱ፡ክነፊሁ`, "in his four wings"). ⚠️ Whether this is the Ge'ez translator's image, the lost Greek's, or the lost Aramaic's is **unknowable** — this is precisely the kind of thing a comparison would settle, and there is nothing to compare.
- ⭐ `ርትዕ` *rətəʿ* — Dillmann: **1)** *rectitudo, integritas, candor*, also *justitia*; **2a)** *probitas*; **2b)** *rectum, jus fasque, aequitas* — "saepissime conjunctum cum `ጽድቅ` et `ፍትሕ`", i.e. most often paired with exactly the word it is paired with here; **2c)** *verum, veritas* (τὸ ἀληθές).
  🛑 So the closing couplet `ጽድቅ … ርትዕ` pairs two nouns that **both** span *righteousness* and *truth*. The line is not "righteousness and truth"; it is two overlapping words for the same double thing, and any English that splits them is inventing a distinction the Ge'ez does not make.

**Witness:** Ethiopic only — `[Bertalotto p]` `ማኅደሪሆሙ` for `ማኅደሮሙ`, `እክናፈ` for `አክናፈ`, `ይትለሀዩ` for `ይትለሐዩ`, `እሰት` for `እሳት`, `ይሴብሐ፡ስም` for `ይሴብሕ፡ስሞ` (⚠️ drops the possessive suffix: "praise a name" / "the name" rather than "his name"); `p` `ኢየሐልቅ` vs `Bertalotto` `ኢየኀልቅ` twice.
🛑 **GE'EZ ALONE.**

### 39:8

**ወበህየ፡ ፈቀድኩ፡ እኅድር፡ ወፈተወቶ፡ ነፍስየ፡ ለውእቱ፡ ማኅደር፡ በህየ፡ ኮነ፡ ክፍልየ፡ ቅድመ፡ እስመ፡ ከመ፡ ዝ፡ ጸንዐ፡ በእንቲኣየ፡ በቅድመ፡ እግዚአ፡ መናፍስት።**

*wäbähəyä fäqädəku ʾəḫədərə wäfätäwäto näfəsəyä läwəʾətu maḫədärə bähəyä konä kəfələyä qədəmä ʾəsəmä kämä zə ṣänəʿä bäʾənətiʾayä bäqədəmä ʾəgəziʾä mänafəsətə*

**And there I (wished | desired | willed) to dwell, and my (soul | life | self) (desired | longed for | craved) that dwelling. There had my (portion | share | lot) been beforehand, for so it was (established | confirmed | made firm | decreed) concerning me before the [LoS].**

- ⚠️ `ነፍስየ` *näfəsəyä* — `ነፍስ`, the *other* soul-word, distinct from `መንፈስ`. Ge'ez keeps both, and Dillmann's `መንፈስ` entry explicitly notes that at 1 Thess. 5:23 the two render the Greek pair. **In this section the title uses `መንፈስ`, but the narrator's inner self is `ነፍስ`.** The distinction is real in the Ge'ez and is preserved here.
- `ጸንዐ` *ṣänəʿä* — *to be firm, strong, established, confirmed*. Not specifically "decreed"; the fixity is what is stated.

**Witness:** Ethiopic only — `[Bertalotto p]` drops the initial `ወበ`, writes `ከመዝ` as one word, and `በእንቲአየ` for `በእንቲኣየ`; `p` `ፀንዓ` vs `Bertalotto` `ጽንዐ` (⚠️ `Bertalotto`'s `ጽንዐ` is a different vocalisation — a noun "firmness" rather than the verb — a small but real divergence with no third witness to settle it).
🛑 **GE'EZ ALONE.**

### 39:9

**ወበውእቶን፡ መዋዕል፡ ሰባሕኩ፡ ወአልዐልኩ፡ ስሞ፡ ለእግዚአ፡ መናፍስት፡ በረከተ፡ ወስብሐተ፡ ወሀብኩ፡ እስመ፡ ውእቱ፡ አጽንዐኒ፡ በበረከት፡ ወስብሐት፡ በከመ፡ ፈቃዱ፡ ለእግዚአ፡ መናፍስት።**

*wäbäwəʾətonə mäwaʿələ säbaḥəku wäʾäləʿäləku səmo läʾəgəziʾä mänafəsətə bäräkätä wäsəbəḥätä wähabəku ʾəsəmä wəʾətu ʾäṣənəʿäni bäbäräkätə wäsəbəḥätə bäkämä fäqadu läʾəgəziʾä mänafəsətə*

**And in those days I (praised | glorified | magnified) and (lifted up | exalted | raised) the name of the [LoS]; blessing and (glory | praise) I gave, for he (strengthened | established | made me firm) with blessing and (glory | praise), according to the (will | pleasure | desire | decree) of the [LoS].**

**Witness:** Ethiopic only — `[Bertalotto p]` **omits `ወሀብኩ`** ("I gave") entirely, giving `በረከተ፡ወስብሐተ፡እስመ፡ውእቱ…`. ⚠️ **This is an omitted verb, not orthography.** `p` `ወዓልዓልኩ` / `አጽንዓኒ` vs `Bertalotto` `ወአልዐልኩ` / `አጽንዐኒ`.
🛑 **GE'EZ ALONE** — a missing main verb with nothing outside Ethiopic to confirm which reading is original.

### 39:10

**ወጕንዱየ፡ ርእያ፡ አዕይንትየ፡ በውእቱ፡ መካን፡ ወባረክዎ፡ ወሰባሕክዎ፡ እንዘ፡ እብል፡ ቡሩክ፡ ውእቱ፡ ወይትባረክ፡ እምቅድመ፡ ዓለም፡ ወእስከ፡ ለዓለም።**

*wägwənəduyä rəʾəya ʾäʿəyənətəyä bäwəʾətu mäkanə wäbaräkəwo wäsäbaḥəkəwo ʾənəzä ʾəbələ burukə wəʾətu wäyətəbaräkə ʾəməqədəmä ʿalämə wäʾəsəkä läʿalämə*

**And long did my eyes (see | gaze) in that place; and I blessed him and (praised | glorified) him, saying: Blessed is he, and let him be blessed from before the (world | age | eternity) and unto the (age | for ever).**

- `ዓለም` *ʿaläm* — *saeculum, aion, mundus, aeternitas*. **"World," "age," and "eternity" are one word.** `እምቅድመ፡ዓለም` is therefore equally "before the world (existed)" and "from before the age."

**Witness:** Ethiopic only — `[Bertalotto p]` reads `አምቅድም` for `እምቅድመ፡ዓለም` — ⚠️ **the manuscripts lack `ዓለም` here**, giving simply "from before-time." A whole word's difference in a formula about pre-existence, with nothing to check it.
🛑 **GE'EZ ALONE.**

### 39:11

**ወበቅድሜሁ፡ አልቦ፡ ማኅለቅት፡ ውእቱ፡ የአምር፡ ዘእንበለ፡ ይትፈጠር፡ ዓለም፡ ምንት፡ ውእቱ፡ ዓለም፡ ወለትውልደ፡ ትውልድ፡ ዘትከውን።**

*wäbäqədəmehu ʾäləbo maḫəläqətə wəʾətu yäʾämərə zäʾənəbälä yətəfäṭärə ʿalämə mənətə wəʾətu ʿalämə wälätəwələdä təwələdə zätəkäwənə*

**And before him there is no (end | limit | consummation). He knows, before the (world | age) was created, what the (world | age) is, and what shall be for generation upon generation.**

**Witness:** Ethiopic only — `[Bertalotto p]` inserts a phrase-divider `፤` after `አልቦ`, and reads `ዘይከውን` (masc.) for `ዘትከውን` (fem.) — an agreement variant.
🛑 **GE'EZ ALONE.**

### 39:12

**ይባርኩከ፡ እለ፡ ኢይነውሙ፡ ወይቀውሙ፡ በቅድመ፡ ስብሐቲከ፡ ወይባርኩ፡ ወይሴብሑ፡ ወያሌዕሉ፡ እንዘ፡ ይብሉ፡ ቅዱስ፡ ቅዱስ፡ ቅዱስ፡ እግዚአ፡ መናፍስት፡ ወይመልእ፡ ምድረ፡ መናፍስተ።**

*yəbarəkukä ʾəlä ʾiyənäwəmu wäyəqäwəmu bäqədəmä səbəḥätikä wäyəbarəku wäyəsebəḥu wäyaleʿəlu ʾənəzä yəbəlu qədusə qədusə qədusə ʾəgəziʾä mänafəsətə wäyəmäləʾə mədərä mänafəsətä*

**Those who do not sleep bless you, and they stand before your (glory | praise); and they bless and (glorify | praise) and (exalt | lift up), saying: (Holy | Consecrated), (Holy | Consecrated), (Holy | Consecrated) is the [LoS] — and he fills the earth with (spirits | breaths | winds | incorporeal natures | angels | daemons | genii).**

- 🛑 **The Ge'ez says the earth is filled with `መናፍስተ` — accusative plural of the very noun in the title.** Not "glory," not "praise: the object of `ይመልእ` is the same word as the title's second half, in the accusative. **This is what the Ge'ez says, and it is the only witness there is.**
- ⭐⭐ **DILLMANN ON THIS VERSE.** His `መንፈስ` entry declares **two plurals — `መንፈሳት` and `መናፍስት`** — and under sense 5b he cites *`መንፈሳት፡ Hen. 39, 12`*, i.e. **the other plural, at this verse.** The manuscripts here read `መንፈሰሳተ`, which is `መንፈሳተ` with a repeated syllable. So the base text and the manuscripts stand on *different plurals of the same noun in the same clause*: base `መናፍስተ`, mss `መንፈሰሳተ`(→`መንፈሳተ`). No sense difference — but it shows the transmission was not stable even on the section's signature word.
- ⚠️ The manuscripts also read `መናፍስት፡መናፍስት፡ይመልዕ፡ምድረ፡መንፈሰሳተ` — **`መናፍስት` written twice** — and `ወይከውሙ` for `ወይቀውሙ`. Dittography is the obvious guess but it is a guess; there is nothing to check it against.

**Witness:** Ethiopic only, as detailed above.
🛑 **GE'EZ ALONE** — and this is one of the most-quoted lines in the section.

### 39:13

**ወበህየ፡ ርእያ፡ አዕይንትየ፡ ኵሎ፡ እለ፡ ኢይነውሙ፡ ይቀውሙ፡ ቅድሜሁ፡ ወይባርኩ፡ ወይብሉ፡ ቡሩክ፡ አንተ፡ ወቡሩክ፡ ስሙ፡ ለእግዚአ፡ መናፍስት፡ ለዓለመ፡ ዓለም።**

*wäbähəyä rəʾəya ʾäʿəyənətəyä kwəlo ʾəlä ʾiyənäwəmu yəqäwəmu qədəmehu wäyəbarəku wäyəbəlu burukə ʾänətä wäburukə səmu läʾəgəziʾä mänafəsətə läʿalämä ʿalämə*

**And there my eyes saw all those who do not sleep standing before him, blessing and saying: Blessed are you, and blessed is the name of the [LoS], for ever and ever.**

- ⚠️ The address shifts from third person ("blessed is he") to second ("blessed are **you**") mid-sentence. Kept.

**Witness:** Ethiopic only — 🛑 `[Bertalotto p]` reads **`ለእግዚእ`** alone — **"of the Lord," without `መናፍስት`.** ⚠️ The manuscripts drop the section's signature title here. Compare 38:6 (base `እግዚአ፡ስብሐት` vs mss `እግዚአ፡መናፍስት`) and 40:3 below (base `እግዚአ፡መናፍስት` vs mss `እግዚአ፡ስብሐት`). **The title is not textually stable, and it varies in both directions.**
🛑 **GE'EZ ALONE.**

### 39:14

**ወተወለጠ፡ ገጽየ፡ እስመ፡ ስእንኩ፡ ነጽሮ።**

*wätäwäläṭä gäṣəyä ʾəsəmä səʾənəku näṣəro*

**And my face was (changed | altered | transformed), for I was not able to (look | gaze | behold).**

- `ተወለጠ` *täwäläṭä* — *to be changed, altered, transformed, exchanged*. Whether the face fell, blanched or was transfigured is not specified.

**Witness:** Ethiopic only — `[Bertalotto p]` reads `እስከ` ("until") for `እስመ` ("for, because"). ⚠️ **A conjunction swap that inverts the logic**: "my face was changed *because* I could not gaze" vs "*until* I could not gaze." No third witness.
🛑 **GE'EZ ALONE.**

---

## Chapter 40 — the four faces and the four names

### 40:1

**ወርኢኩ፡ እምድኅረዝ፡ አእላፈ፡ አእላፋት፡ ወትእልፊተ፡ አእላፋት፡ ወአልቦሙ፡ ኍልቊ፡ ወሐሳብ፡ ለእለ፡ ይቀውሙ፡ ቅድመ፡ እግዚአ፡ መናፍስት።**

*wärəʾiku ʾəmədəḫərä-zə ʾäʾəlafä ʾäʾəlafatə wätəʾələfitä ʾäʾəlafatə wäʾäləbomu ḫwələqwə wäḥäsabə läʾəlä yəqäwəmu qədəmä ʾəgəziʾä mänafəsətə*

**And after this I saw thousands of thousands and ten-thousands of thousands — and there is to them no (number | count) and no (reckoning | calculation) — of those who stand before the [LoS].**

- `አእላፍ` / `ትእልፊት` — the two Ge'ez large-number words, conventionally *thousand* and *ten thousand / myriad*, but both are also used loosely for "a very great many." The pairing is an intensifier.

**Witness:** Ethiopic only — `[Bertalotto p]` `አዕላፋት` for `አእላፋት`, and reads `ትእልፊት` (not `አእላፋት`) in the second phrase, giving "ten-thousands of ten-thousands"; also drops `ለ` before `እለ`, and 🛑 **adds `ስብሐተ`**: `ቅድመ፡ስብሐተ፡እግዚአ፡መናፍስት`, "before the **glory** of the [LoS]." ⚠️ Substantive addition, unverifiable.
🛑 **GE'EZ ALONE.**

### 40:2

**ወርኢኩ፡ ወበአርባዕቱ፡ ክነፊሁ፡ ለእግዚአ፡ መናፍስት፡ አርባዕተ፡ ገጻት፡ ካልኣተ፡ እምእለ፡ ይቀውሙ፡ ወአስማቲሆሙ፡ አእመርኩ፡ ዘአይድዐኒ፡ መልአክ፡ ዘመጽአ፡ ምስሌየ፡ ወኵሎ፡ ኅቡኣተ፡ አርአየኒ።**

*wärəʾiku wäbäʾärəbaʿətu kənäfihu läʾəgəziʾä mänafəsətə ʾärəbaʿətä gäṣatə kaləʾatä ʾəməʾəlä yəqäwəmu wäʾäsəmatihomu ʾäʾəmäräku zäʾäyədəʿäni mäləʾäkə zämäṣəʾä məsəleyä wäkwəlo ḫəbuʾatä ʾärəʾäyäni*

**And I saw — and in the four wings of the [LoS], four faces, other than those who stand; and I came to know their names, which the (angel | messenger) who came with me (told | declared | announced) to me; and he showed me all (hidden things | secrets).**

- 🛑 **"the four wings of the Lord of Spirits" — the wings again** (cf. 39:7). The four faces are located *in* his wings. ⚠️ Whether `በአርባዕቱ፡ክነፊሁ` means "on his four wings" or "within the four quarters of his wings" is not settled by the Ge'ez, and there is nothing upstream to consult.

**Witness:** Ethiopic only — `[Bertalotto p]` drops the initial `ወ`, uses numerals `፬` twice, reads **`መነፍስት`** for `መናፍስት` (⚠️ yet another spelling of the signature word), inserts a second `ርኢኩ`, reads singular `፬ገጸ፡ካልአ` for plural `አርባዕተ፡ገጻት፡ካልኣተ`, repeats `አስማቲሆሙ`, and `ኀብኣተ` for `ኅቡኣተ`. `p` `ዘአይድዓኒ` vs `Bertalotto` `ዘአይድዐኒ`.
🛑 **GE'EZ ALONE** — and note how heavily the two Ethiopic lines diverge in a verse this short.

### 40:3

**ወሰማዕኩ፡ ቃሎሙ፡ ለእልክቱ፡ ገጽ፡ አርባዕቱ፡ ገጽ፡ እንዘ፡ ይሴብሑ፡ ቅድመ፡ እግዚአ፡ መናፍስት።**

*wäsämaʿəku qalomu läʾələkətu gäṣə ʾärəbaʿətu gäṣə ʾənəzä yəsebəḥu qədəmä ʾəgəziʾä mänafəsətə*

**And I heard the (voice | word | sound) of those faces, the four faces, as they (glorified | praised) before the [LoS].**

**Witness:** Ethiopic only — `[Bertalotto p]` reads `ለእልከቱ፡፬ገጽ` (dropping the doubled `ገጽ`) and 🛑 **`እግዚአ፡ስብሐት`** — "Lord of **glory**" — where the base text has `እግዚአ፡መናፍስት`. ⚠️ **This is the exact inverse of 38:6**, where the base text had `ስብሐት` and the manuscripts `መናፍስት`. **The two Ethiopic traditions swap these two titles in both directions, and nothing survives to arbitrate either case.**
🛑 **GE'EZ ALONE.**

### 40:4

**ወቃል፡ ቀዳማዊ፡ ይባርኮ፡ ለእግዚአ፡ መናፍስት፡ ለዓለመ፡ ዓለም።**

*wäqalə qädamawi yəbarəko läʾəgəziʾä mänafəsətə läʿalämä ʿalämə*

**And the first (voice | word) blesses the [LoS] for ever and ever.**

**Witness:** Ethiopic only — `[Bertalotto p]` drops the initial `ወ`.
🛑 **GE'EZ ALONE.**

### 40:5

**ወቃለ፡ ካልአ፡ ሰማዕኩ፡ እንዘ፡ ይባርኮ፡ ለኅሩይ፡ ወለኅሩያን፡ እለ፡ ስቁላን፡ ለእግዚአ፡ መናፍስት።**

*wäqalä kaləʾä sämaʿəku ʾənəzä yəbarəko läḫəruyə wäläḫəruyanə ʾəlä səqulanə läʾəgəziʾä mänafəsətə*

**And the second (voice | word) I heard, blessing the (Chosen One | Selected One | Choice One | Approved One | **Arbiter** | **Mediator**) and the (chosen | choice | approved) ones who are (hung | suspended | made to depend | fastened | clinging | **weighed**) upon the [LoS].**

- ⭐⭐ **This verse carries BOTH of my two lexicon findings in eight words.**
  1. `ኅሩይ` in the singular, as a title, immediately followed by `ኅሩያን` in the plural, as a class. **Dillmann cites this exact verse twice** — under sense 1 (*electus*) with the note "**de Messia** … Hen. 40, 5", and again in the general list "Hen. 1, 1. 8. 5, 7. 8. 38, 2. **40, 5**". But his sense **4** for the same participle is ***arbiter (a litigantibus electus), conciliator, mediator***. The singular here is the figure who will *judge* in 45:3 and 51:3. **Both senses are in Dillmann and both fit. Neither is preferred.**
  2. `ስቁላን` — the plural of the participle Dillmann cites at this verse: `ተግባሮሙ፡ስቁል፡በአግዚአ፡መናፍስት Hen. 38, 2. **40, 5.** 46, 8`, filed under *suspensus, pendens, adhaerens* — but with *ponderatus*, "**weighed**", standing as sense 3 of the same participle.
- ⚠️ **Preposition variant, and it matters.** The base text reads `ስቁላን፡**ለ**እግዚአ፡መናፍስት` (dative `ለ`, "hung *to/for*"); `[Bertalotto p]` reads `ስቁላን፡**በ**እግዚአ፡መናፍስት` (instrumental/locative `በ`, "hung *upon/by*"). **Dillmann's citation uses `በ`.** "Depending on him" and "belonging to him" are different claims, and the manuscripts do not agree. No Greek, no Aramaic.

**Witness:** Ethiopic only — `[Bertalotto p]` `ወለኀሩያን` (ኀ/ኅ) and the `በ`/`ለ` divergence above.
🛑 **GE'EZ ALONE.**

### 40:6

**ወሣልሰ፡ ቃለ፡ ሰማዕኩ፡ እንዘ፡ ይስእሉ፡ ወይጼልዩ፡ በእንተ፡ እለ፡ የኀድሩ፡ ውስተ፡ የብስ፡ ወያስተበቍዑ፡ በስሙ፡ ለእግዚአ፡ መናፍስት።**

*wäśaləsä qalä sämaʿəku ʾənəzä yəsəʾəlu wäyəṣeləyu bäʾənətä ʾəlä yäḫädəru wəsətä yäbəsə wäyasətäbäqwəʿu bäsəmu läʾəgəziʾä mänafəsətə*

**And the third (voice | word) I heard (asking | petitioning) and praying on behalf of those who (dwell | abide) upon the dry land, and (entreating | supplicating urgently) in the name of the [LoS].**

**Witness:** Ethiopic only — `p` `የኃድሩ` vs `Bertalotto` `የኀድሩ`; `[Bertalotto p]` `ወያስተበቈዑ` for `ወያስተበቍዑ`.
🛑 **GE'EZ ALONE.**

### 40:7

**ወቃለ፡ ራብዐየ፡ ሰማዕኩ፡ እንዘ፡ ይሰድዶሙ፡ ለሰይጣናት፡ ወኢየኀድጎሙ፡ ይባኡ፡ ኀበ፡ እግዚአ፡ መናፍስት፡ ከመ፡ ያስተዋድይዎሙ፡ ለእለ፡ የኀድሩ፡ ዲበ፡ የብስ።**

*wäqalä rabəʿäyä sämaʿəku ʾənəzä yəsädədomu läsäyəṭanatə wäʾiyäḫädəgomu yəbaʾu ḫäbä ʾəgəziʾä mänafəsətə kämä yasətäwadəyəwomu läʾəlä yäḫädəru dibä yäbəsə*

**And the fourth (voice | word) I heard, (driving away | expelling | pursuing | persecuting) the (satans | adversaries | accusers), and not (permitting | leaving | allowing) them to enter before the [LoS] to (accuse | bring charges against | denounce) those who (dwell | abide) upon the dry land.**

- ⭐ `ሰይጣናት` *säyəṭanat* — **plural**. A transliterated Semitic loan whose underlying sense is *adversary, accuser*; the Ge'ez pluralises it into a class, not a person.
- `ያስተዋድይዎሙ` — causative-reflexive of `ወደየ`: *to lay a charge against, accuse, denounce*. The forensic sense is explicit, and it is what the plural `ሰይጣናት` is doing.
- `ይሰድዶሙ` — *to drive out, expel, pursue, persecute*. The verb is the same one used of the sinners being driven off the land in 41:2.

**Witness:** Ethiopic only — `p` `ራብአየ` vs `Bertalotto` `ራብዓየ`; `[Bertalotto p]` `ይባአ` (sing.) for `ይባኡ` (pl.); `p` `የኃድሩ` vs `Bertalotto` `የኀድሩ`.
🛑 **GE'EZ ALONE.**

### 40:8

**ወእምድኅረ፡ ዝ፡ ተስእልክዎ፡ ለመልአከ፡ ሰላም፡ ዘየሐውር፡ ምስሌየ፡ ዘውእቱ፡ አርአየኒ፡ ኵሎ፡ ዘኅቡእ፡ ወእብሎ፡ መኑ፡ ውእቶሙ፡ እሉ፡ አርባዕቱ፡ ገጽ፡ ዘርኢኩ፡ ወእለ፡ ሰማዕኩ፡ ቃሎሙ፡ ወጸሐፍክዎሙ።**

*wäʾəmədəḫərä zə täsəʾələkəwo lämäləʾäkä sälamə zäyäḥäwərə məsəleyä zäwəʾətu ʾärəʾäyäni kwəlo zäḫəbuʾə wäʾəbəlo mänu wəʾətomu ʾəlu ʾärəbaʿətu gäṣə zärəʾiku wäʾəlä sämaʿəku qalomu wäṣäḥäfəkəwomu*

**And after this I asked the (angel | messenger) of peace who walks with me, who himself showed me every hidden thing, and I said to him: Who are these four faces which I saw, and whose (voice | word) I heard and wrote down?**

- `መልአከ፡ሰላም` — "(angel | messenger) of (peace | wholeness | well-being | safety)." `ሰላም` has the full Semitic range.

**Witness:** Ethiopic only — `[Bertalotto p]` writes `ወእምድኅረዝ` as one word, **omits `ወእብሎ`** ("and I said to him"), and uses the numeral `፬`. ⚠️ Another omitted verb.
🛑 **GE'EZ ALONE.**

### 40:9

**ወይቤለኒ፡ ዝ፡ ቃል፡ ቀዳማዊ፡ ውእቱ፡ መሓሪ፡ ወርሑቀ፡ መዓት፡ ቅዱስ፡ ሚካኤል፡ ወካልእ፡ ዘዲበ፡ ኵሉ፡ ሕማም፡ ወዲበ፡ ኵሉ፡ ቍስል፡ ዘውሉደ፡ ሰብእ፡ ውእቱ፡ ሩፋኤል፡ ወሣልስ፡ ዘዲበ፡ ኵሉ፡ ኀይል፡ ውእቱ፡ ቅዱስ፡ ገብርኤል፡ ወራብዕ፡ ዘዲበ፡ ንስሓ፡ ለተስፋ፡ እለ፡ ይወርሱ፡ ሕይወተ፡ ዘለዓለም፡ ውእቱ፡ ፋኑኤል።**

*wäyəbeläni zə qalə qädamawi wəʾətu mäḥari wärəḥuqä mäʿatə qədusə mikaʾelə wäkaləʾə zädibä kwəlu ḥəmamə wädibä kwəlu qwəsələ zäwəludä säbəʾə wəʾətu rufaʾelə wäśaləsə zädibä kwəlu ḫäyələ wəʾətu qədusə gäbərəʾelə wärabəʿə zädibä nəsəḥa lätäsəfa ʾəlä yəwärəsu ḥəyəwätä zäläʿalämə wəʾətu fanuʾelə*

**And he said to me: This first (voice | word) — he is the (merciful | compassionate) one and (slow to | far from) (wrath | anger), the (holy | consecrated) Mikaʾel. And the second, who is over every (sickness | disease | suffering | pain) and over every (wound | sore | affliction) of the (children | offspring) of (humankind | humanity) — he is Rufaʾel. And the third, who is over every (power | strength | force | host) — he is the (holy | consecrated) Gäbrəʾel. And the fourth, who is over (repentance | penitence | turning-back) unto (hope | expectation) of those who (inherit | take possession of) (life | living) (everlasting | of the age) — he is Fanuʾel.**

- `ርሑቀ፡መዓት` — literally "far-off of wrath," an idiom for slowness to anger. The Ge'ez idiom is spatial, not temporal.
- `ኀይል` *ḫäyəl* — *power, strength, force, army, host*. "Over every host" and "over every power" are the same phrase.
- ⚠️ The four names are Ethiopic transliterations of Semitic theophoric compounds. **No Greek or Aramaic survives at this verse to show what the forms behind them were** — contrast 6:7, where four witnesses can be compared and no two agree (see `enoch-6.md`). Here comparison is simply unavailable.

**Witness:** Ethiopic only — `[Bertalotto p]` `ወይቤለኑ` for `ወይቤለኒ` (⚠️ "he said to **us**" for "he said to **me**"), `ዝቀዳማዊ` (omitting `ቃል`, "this first" without "voice"); `p` `ኃይል` vs `Bertalotto` `ኀይል`.
🛑 **GE'EZ ALONE.**

### 40:10

**ወእሉ፡ አርባዕቱ፡ መላእክቲሁ፡ ለእግዚአብሔር፡ ልዑል፡ ወአርባዕተ፡ ቃለ፡ ሰማዕኩ፡ በውእቶን፡ መዋዕል።**

*wäʾəlu ʾärəbaʿətu mälaʾəkətihu läʾəgəziʾabəḥerə ləʿulə wäʾärəbaʿətä qalä sämaʿəku bäwəʾətonə mäwaʿələ*

**And these four are the (angels | messengers) of ʾƎgziʾabəḥer the (Most High | Exalted | Lofty); and four (voices | words) I heard in those days.**

- 🛑 **A THIRD TITLE.** `እግዚአብሔር` — literally `እግዚእ` + `ብሔር`, "(Master | Lord) of the (land | country | region | world)" — appears here, in a chapter that has said `እግዚአ፡መናፍስት` seven times. Dillmann notes at his `እግዚእ` entry that `እግዚአብሔር` is *magis usitatum* — the more usual word — for God. ⚠️ **So within ten verses the Ge'ez uses `እግዚአ፡መናፍስት`, `እግዚአ፡ስብሐት` (mss at 40:3) and `እግዚአብሔር፡ልዑል`.** Whether these translate three different Greek phrases or one is unknowable: **there is no Greek.**

**Witness:** Ethiopic only — `[Bertalotto p]` uses numerals `፬` twice.
🛑 **GE'EZ ALONE.**

---

## Chapter 41 — the deeds weighed, and the storehouses

### 41:1

**ወእምድኅረ፡ ዝ፡ ርኢኩ፡ ኵሎ፡ ኅቡኣቲሆሙ፡ ለሰማያት፡ ወመንግሥት፡ እፎ፡ ትትከፈል፡ ወተግባረ፡ ሰብእ፡ ከመ፡ በመዳልው፡ ይዴለው።**

*wäʾəmədəḫərä zə rəʾiku kwəlo ḫəbuʾatihomu läsämayatə wämänəgəśətə ʾəfo tətəkäfälə wätägəbarä säbəʾə kämä bämädaləwə yədeläwə*

**And after this I saw all the (hidden things | secrets) of the heavens, and how the (kingdom | kingship | rule) is (divided | distributed | apportioned), and the (work | deeds | labour) of (humankind | humanity), how it is (weighed | balanced) as in a (balance | scales).**

- ⭐⭐⭐ **THIS VERSE IS THE INTERNAL CONTROL ON `ስቁል`.** `መዳልው` *mädaləw* is a **balance / scales** (Prov. 16:11; Hez. 5:1; Sir. 42:7 in Dillmann's citations), and `ይዴለው` is the verb *ponderare*, **to weigh** (Jes. 46:6; 4 Esr. 1:35).
  🛑 So the section states outright, in its own words, that **`ተግባረ፡ሰብእ` — the deeds of humankind — are WEIGHED IN A BALANCE.** And in 38:2, 40:5 and 46:8 the section says `ተግባሮሙ፡ስቁል` of the same deeds, using a participle whose Dillmann sense 3 is ***ponderatus*, "weighed."**
  ⭐ **The same noun (`ተግባር`), the same subject (humankind's deeds), one chapter apart — once with an explicit balance, once with a participle that also means "weighed."** That is an argument *from inside the Ge'ez* for keeping "weighed" alive as a reading of `ስቁል`, and it needs no external witness. It is offered as evidence, **not as a resolution**: "hangs upon / depends on" remains equally available and Dillmann files the citation there.

**Witness:** Ethiopic only — `[Bertalotto p]` `ኅበኣቲሆሙ` for `ኅቡኣቲሆሙ` and `ይደለው` for `ይዴለው`.
🛑 **GE'EZ ALONE.**

### 41:2

**ወበህየ፡ ርኢኩ፡ ማኅደሪሆሙ፡ ለቅዱሳን፡ ወማኅደሮሙ፡ ለኅሩያን፡ ወርእያ፡ አዕይንትየ፡ በህየ፡ ኵሎሙ፡ ኃጥኣን፡ እንዘ፡ ይሰደዱ፡ እምህየ፡ እለ፡ ይክሕድዎ፡ ለስመ፡ እግዚአ፡ መናፍስት፡ ወይስሕብዎሙ፡ ወቀዊመ፡ አልቦሙ፡ በመቅሠፍት፡ እንተ፡ ትወፅእ፡ እምእግዚአ፡ መናፍስት።**

*wäbähəyä rəʾiku maḫədärihomu läqədusanə wämaḫədäromu läḫəruyanə wärəʾəya ʾäʿəyənətəyä bähəyä kwəlomu ḫaṭəʾanə ʾənəzä yəsädädu ʾəməhəyä ʾəlä yəkəḥədəwo läsəmä ʾəgəziʾä mänafəsətə wäyəsəḥəbəwomu wäqäwimä ʾäləbomu bämäqəśäfətə ʾənətä təwäḍəʾə ʾəməʾəgəziʾä mänafəsətə*

**And there I saw the (dwellings | habitations) of the (holy | consecrated) and the (dwelling | habitation) of the (chosen | choice | approved | arbiters); and my eyes saw there all the (sinners | offenders) being (driven out | expelled | pursued) from there — those who (deny | disown | renounce) the name of the [LoS] — and they (drag | draw | haul) them away, and there is no standing for them, because of the (chastisement | scourge | punishment | plague) which goes out from the [LoS].**

- `መቅሠፍት` *mäqəśäft* — from `ቀሠፈ` "to scourge, flog": *scourging, chastisement, punishment, plague*. The physical image is a whip.
- ⚠️ `ወይስሕብዎሙ` — the subject of "they drag" is unstated. It could be the sinners being dragged by unnamed agents (passive in effect) or the sinners dragging others. **The Ge'ez does not say. Not smoothed.**

**Witness:** Ethiopic only — `[Bertalotto p]` drops the initial `ወ` and 🛑 **swaps the two nouns**: `ማኅደሪሆሙ፡ለኅሩያን፡ወምስካባቲሆሙ፡ለቅዱሳን` ("the dwellings of the chosen and the couches of the holy") against the base text's "the dwellings of the holy and the dwelling of the chosen." ⚠️ Both the pairing and the second noun differ. `[Bertalotto p]` also `ይከሀድዎ` for `ይክሕድዎ` and `ወቀዊም` for `ወቀዊመ`.
🛑 **GE'EZ ALONE.**

### 41:3

**ወበህየ፡ ርእያ፡ አዕይንትየ፡ ኅቡኣተ፡ መባርቅተ፡ ወነጐድጓድ፡ ወኅቡኣተ፡ ነፋሳተ፡ ወእፎ፡ ይትከፈሉ፡ ከመ፡ ይንፍኁ፡ ዲበ፡ ምድር፡ ወኅቡኣተ፡ ደመና፡ ወጠል፡ ወበህየ፡ ርኢኩ፡ እምኀበ፡ ይወፅእ፡ በውእቱ፡ መካን፡ ወእምህየ፡ ይጸግቡ፡ ጸበለ፡ ምድር።**

*wäbähəyä rəʾəya ʾäʿəyənətəyä ḫəbuʾatä mäbarəqətä wänägwädəgwadə wäḫəbuʾatä näfasatä wäʾəfo yətəkäfälu kämä yənəfəḫu dibä mədərə wäḫəbuʾatä dämäna wäṭälə wäbähəyä rəʾiku ʾəməḫäbä yəwäḍəʾə bäwəʾətu mäkanə wäʾəməhəyä yəṣägəbu ṣäbälä mədərə*

**And there my eyes saw the (hidden things | secrets) of the lightnings and the thunder, and the (hidden things | secrets) of the winds, and how they are (divided | apportioned | distributed) so as to blow upon the earth; and the (hidden things | secrets) of the cloud and the dew; and there I saw from where it goes out in that place, and from there the dust of the earth is (satisfied | sated | filled).**

- ⭐ **Lightning, thunder, winds, cloud, dew** — the *same semantic field* as the Watchers' names in the Aramaic of 6:7 (`ברקאל` lightning, `מטר אל` rain, `עננאל` cloud, `רעמ אל` thunder — see `enoch-6.md`). There the field was visible only because the Aramaic survived. **Here the field is visible in the Ge'ez itself, but there is no Aramaic to show whether any of it is name-play.**
- `ነፋሳተ` *näfasatä* — plural of `ነፋስ`, winds. Again, the *other* wind-word; see 39:3.

**Witness:** Ethiopic only — `p` `ኅብአተ` vs `Bertalotto` `ኅብኣተ` (three times); `[Bertalotto p]` `ወነጐድጓደ` for `ወነጐድጓድ`, omits `ወ` before `እፎ`, `ይንፍሑ` for `ይንፍኁ`, ⚠️ **repeats `ዲበ፡ምድር` twice**, `ደመናት` (pl.) for `ደመና` (sg.), `ይፀግቡ` for `ይጸግቡ`; `p` `ፀበለ` vs `Bertalotto` `ጸበለ`.
🛑 **GE'EZ ALONE.**

### 41:4

**ወበህየ፡ ርኢኩ፡ መዛግብተ፡ ዕፅዋነ፡ ወእምኔሆሙ፡ ይትከፈሉ፡ ነፋሳት፡ ወመዝገበ፡ በረድ፡ ወመዝገበ፡ ጊሜ፡ ወዘደመናት፡ ወደመና፡ ዚኣሁ፡ እምላዕለ፡ ምድር፡ የኀድር፡ እምቅድመ፡ ዓለም።**

*wäbähəyä rəʾiku mäzagəbətä ʿəḍwanä wäʾəmənehomu yətəkäfälu näfasatə wämäzəgäbä bärädə wämäzəgäbä gime wäzädämänatə wädämäna ziʾahu ʾəməlaʿəlä mədərə yäḫädərə ʾəməqədəmä ʿalämə*

**And there I saw the (storehouses | treasuries) shut up, and from them the winds are (divided | apportioned); and the (storehouse | treasury) of hail, and the (storehouse | treasury) of (mist | fog | frost), and that of the clouds; and his cloud (dwells | abides) above the earth from before the (world | age).**

- `መዝገብ` *mäzgäb* — a *storehouse, treasury, granary*. Not a "chamber."
- `ዕፅዋነ` — participle of `ዐፀወ` "to shut, close, bar." The storehouses are **shut**.

**Witness:** Ethiopic only — `[Bertalotto p]` expands `ወዘደመናት` to `ወመዝገበ፡ደመናት` (supplying the noun), and `ዚአሁ` for `ዚኣሁ`; `p` `የኃድር` vs `Bertalotto` `የኀድር`.
🛑 **GE'EZ ALONE.**

### 41:5

**ወርኢኩ፡ መዛግብተ፡ ፀሓይ፡ ወዘወርኅ፡ ወእምአይቴ፡ ይወፅኡ፡ ወአይቴ፡ ይገብኡ፡ ወግብአቶሙ፡ ስቡሕ፡ ወእፎ፡ ይከብር፡ አሐዱ፡ እምካልኡ፡ ወምሕዋሮሙ፡ ብዑል፡ ወኢየኀልፉ፡ ምሕዋረ፡ ወኢይዌስኩ፡ ወኢያሐጽጹ፡ ምሕዋረ፡ ዚኣሆሙ፡ ወሃይማኖቶሙ፡ የዐቅቡ፡ አሐዱ፡ ምስለ፡ ካልኡ፡ በመሐላ፡ ዘነበሩ።**

*wärəʾiku mäzagəbətä ḍäḥayə wäzäwärəḫə wäʾəməʾäyəte yəwäḍəʾu wäʾäyəte yəgäbəʾu wägəbəʾätomu səbuḥə wäʾəfo yəkäbərə ʾäḥädu ʾəməkaləʾu wäməḥəwaromu bəʿulə wäʾiyäḫäləfu məḥəwarä wäʾiyəwesəku wäʾiyaḥäṣəṣu məḥəwarä ziʾahomu wähayəmanotomu yäʿäqəbu ʾäḥädu məsəlä kaləʾu bämäḥäla zänäbäru*

**And I saw the (storehouses | treasuries) of the sun and of the moon, and from where they go out and where they return; and their return is (glorious | praiseworthy); and how one is (honoured | glorified | made weighty) above the other; and their (course | orbit | circuit) is (rich | ample | abundant); and they do not (pass | transgress | overstep) the (course | circuit), and they neither add to nor diminish their (course | circuit); and they keep their (faith | fidelity | trust | trustworthiness), one with the other, by the oath by which they are bound.**

- ⭐ `ሃይማኖቶሙ፡የዐቅቡ` — "they keep their `ሃይማኖት`." Dillmann glosses `ሃይማኖት` as *fides*, which in Latin is **belief, trust, fidelity, trustworthiness, a sworn undertaking** — and here the subjects are **the sun and moon**, bound by an oath. ⚠️ **This is the same noun used of the righteous at 39:6.** Any English that renders one "faith" and the other "fidelity" is making a distinction the Ge'ez does not have.
- `ይከብር` *yəkäbərə* — *to be heavy, weighty, honoured, glorious*. The physical and honorific senses are one root.

**Witness:** Ethiopic only — `[Bertalotto p]` `ፀሐይ` for `ፀሓይ`, `ወወርኅ` for `ወዘወርኅ`, drops `ወ` before `እምአይቴ`, `ውእፎ` for `ወእፎ`, `፩እምከልዑ` for `አሐዱ፡እምካልኡ`, `እምኅዋረ`/`እምሕዋረ` for `ምሕዋረ`, `ዚአሆሙ` for `ዚኣሆሙ`, `፩` for `አሐዱ`; `p` `ወኢየኃልፉ`/`ወኢየሐፅፁ` vs `Bertalotto` `ወኢየኀልፉ`/`ወኢየሐጽጹ` (⚠️ note both manuscripts read `የሐጽጹ`, third person, against the base text's `ያሐጽጹ`, causative).
🛑 **GE'EZ ALONE.**

### 41:6

**ወይወፅእ፡ ቅድመ፡ ፀሓይ፡ ወይገብር፡ ፍኖቶ፡ በትእዛዘ፡ እግዚአ፡ መናፍስት፡ ወይጸንዕ፡ ስሙ፡ ለዓለመ፡ ዓለም።**

*wäyəwäḍəʾə qədəmä ḍäḥayə wäyəgäbərə fənoto bätəʾəzazä ʾəgəziʾä mänafəsətə wäyəṣänəʿə səmu läʿalämä ʿalämə*

**And the sun goes out first and makes its (path | way | course) at the (command | ordinance | decree) of the [LoS]; and his name is (strong | firm | established) for ever and ever.**

**Witness:** Ethiopic only — `[Bertalotto p]` `ፀሐይ` for `ፀሓይ` and `ወይፀንዕ` for `ወይጸንዕ`.
🛑 **GE'EZ ALONE.**

### 41:7

**ወእምድኅረ፡ ዝ፡ ርኢኩ፡ ፍኖተ፡ ዘኅቡእ፡ ወዘክሡት፡ ዘወርኅ፡ ወምሕዋረ፡ ፍኖቱ፡ ይፌጽም፡ በውእቱ፡ መካን፡ በመዓልት፡ ወበሌሊት፡ ወአሐዱ፡ ለካልኡ፡ ይኔጽሮ፡ በቅድመ፡ እግዚአ፡ መናፍስት፡ ወየአኵቱ፡ ወይሴብሑ፡ ወኢየዐርፉ፡ እስመ፡ አኰቴቶሙ፡ ዕረፍቶሙ፡ ውእቱ፡ ሎሙ።**

*wäʾəmədəḫərä zə rəʾiku fənotä zäḫəbuʾə wäzäkəśutə zäwärəḫə wäməḥəwarä fənotu yəfeṣəmə bäwəʾətu mäkanə bämäʿalətə wäbälelitə wäʾäḥädu läkaləʾu yəneṣəro bäqədəmä ʾəgəziʾä mänafəsətə wäyäʾäkwətu wäyəsebəḥu wäʾiyäʿärəfu ʾəsəmä ʾäkwətetomu ʿəräfətomu wəʾətu lomu*

**And after this I saw the (path | way) of the moon, hidden and (open | manifest | revealed), and it completes the (course | circuit) of its (path | way) in that place, by day and by night; and one (looks upon | regards | gazes at) the other before the [LoS]; and they (give thanks | acknowledge | confess) and (glorify | praise) and do not rest — for their (thanksgiving | acknowledgement) is their rest.**

- ⭐ `የአኵቱ` / `አኰቴት` — from `አኰተ`, *to give thanks, acknowledge, confess*. The closing line is a genuine paradox in the Ge'ez as it stands: they never rest, *because* their thanksgiving **is** their rest.

**Witness:** Ethiopic only — `[Bertalotto p]` **omits `ርኢኩ`** ("I saw" — ⚠️ the main verb of the sentence), reads `ፍኖት` (nom.) for `ፍኖተ` (acc.), `፩ለከካሌኡ፡ይኔጽር` for `አሐዱ፡ለካልኡ፡ይኔጽሮ` (dropping the object suffix), `ወኢየአርፉ` for `ወኢየዐርፉ`, and `ዕረፍት` for `ዕረፍቶሙ` (dropping the possessive); `p` `ዘወርኃ`/`ወምኅዋረ` vs `Bertalotto` `ዘወርኀ`/`ወምሕዋረ`.
🛑 **GE'EZ ALONE** — with the sentence's main verb present in one Ethiopic line and absent in the other, and no other language to consult.

### 41:8

**እስመ፡ ፀሓይ፡ ብሩህ፡ ብዙኅ፡ ሙያጤ፡ ቦቱ፡ ለበረከት፡ ወለመርገም፡ ወምርዋጸ፡ ፍኖቱ፡ ለወርኅ፡ ለጻድቃን፡ ብርሃን፡ ወለኃጥኣን፡ ጽልመት፡ በስሙ፡ ለእግዚአ፡ መናፍስት፡ ዘፈጠረ፡ ማእከለ፡ ብርሃን፡ ወማእከለ፡ ጽልመት፡ ወከፈለ፡ መንፈሰ፡ ለሰብእ፡ ወአጽንዐ፡ መንፈሶሙ፡ ለጻድቃን፡ በስመ፡ ጽድቀ፡ ዚኣሁ።**

*ʾəsəmä ḍäḥayə bəruhə bəzuḫə muyaṭe botu läbäräkätə wälämärəgämə wämərəwaḍä fənotu läwärəḫə läṣadəqanə bərəhanə wäläḫaṭəʾanə ṣələmätə bäsəmu läʾəgəziʾä mänafəsətə zäfäṭärä maʾəkälä bərəhanə wämaʾəkälä ṣələmätə wäkäfälä mänəfäsä läsäbəʾə wäʾäṣənəʿä mänəfäsomu läṣadəqanə bäsəmä ṣədəqä ziʾahu*

**For the sun is (bright | shining | clear); many are the (turnings | returns | changes) it has, for blessing and for (curse | cursing); and the (running | swift course) of the (path | way) of the moon is light to the (righteous | just | truthful) and darkness to the (sinners | offenders) — in the name of the [LoS], who created a (division | separation) between light and between darkness, and (divided | apportioned) the **(spirit | breath | wind | life | mind)** to (humankind | humanity), and (strengthened | established) the **(spirit | breath | life | mind)** of the (righteous | just | truthful) in the name of his (righteousness | justice | truth).**

- ⭐⭐⭐ **`ወከፈለ፡መንፈሰ፡ለሰብእ` — "and he apportioned `መንፈስ` to humankind."**
  🛑 **This is the singular of the exact noun in the title, used in the same verse as the title, of what human beings are given.** Two clauses later: `መንፈሶሙ፡ለጻድቃን`, "the `መንፈስ` of the righteous."
  ⭐ So within one verse the Ge'ez calls him `እግዚአ፡መናፍስት` and then says he distributes `መንፈስ` to people. **On the text's own usage, the `መናፍስት` he is master of demonstrably includes human `መንፈስ` — Dillmann's senses 3 (*anima, vis vitalis, vita*) and 4 (*animus, spiritus hominis … voluntas, intellectus*).**
  This does **not** settle the title — Dillmann files the title's occurrence under 5b (*angeli, daemones, genii*), and 39:12 has the earth filled with them. **It shows the range is genuinely live in this very section, in both directions, and that narrowing the title to any one of them is a choice the Ge'ez does not make.**
- `ጽልመት` *ṣələmät* — darkness. Note the construction `ማእከለ … ወማእከለ`, "between … and between," a Semitic calque preserved in the Ge'ez.

**Witness:** Ethiopic only — 🛑 `[Bertalotto p]` reads **`በስሙ፡በእግዚእ`** — "in his name, in the **Lord**" — dropping `መናፍስት` entirely (compare 39:13). ⚠️ Also `ብዙኀ` for `ብዙኅ`, `ምያጤ` for `ሙያጤ`, `ወከፈለ፡መንፈሶሙ፡ለሰብእ` for `ወከፈለ፡መንፈሰ፡ለሰብእ` (⚠️ **"their spirit" for "spirit" — the manuscripts make the apportioned spirit already-possessed**), `ጽድቀ፡ዚአሁ` for `ጽድቀ፡ዚኣሁ`; `p` `ማዕከለ`/`ወአጽንዓ` vs `Bertalotto` `ማእከለ`/`ወአጽንዐ`.
🛑 **GE'EZ ALONE** — and the manuscripts differ from the base text on both the title and the spirit-clause, in the one verse where the two are joined.

### 41:9

**እስመ፡ መልአክ፡ ኢይከልእ፡ ወሥልጣን፡ ኢይክል፡ ከሊአ፡ እስመ፡ መኰንን፡ ለኵሎሙ፡ ይሬኢ፡ ወእሎንተ፡ ኵሎሙ፡ በቅድሜሁ፡ ውእቱ፡ ይኴንን።**

*ʾəsəmä mäləʾäkə ʾiyəkäləʾə wäśələṭanə ʾiyəkələ käliʾä ʾəsəmä mäkwänənə läkwəlomu yəreʾi wäʾəlonətä kwəlomu bäqədəmehu wəʾətu yəkwenənə*

**For the (angel | messenger) does not (hinder | withhold | forbid), and (power | authority | dominion) is not able to (hinder | withhold | forbid); for the (judge | ruler | prince | governor) sees them all, and all these before him — he (judges | condemns | rules).**

- ⭐ `መኰንን` and `ይኴንን` are the **same root** — `ኰነነ`, *to judge, condemn, rule, govern*. Ge'ez does not separate ruling from judging, and the verse plays the noun against the verb. `ይኴንን` is the same form used of the sinners at 38:1 and 38:3.
- `ሥልጣን` *śələṭan* — *power, authority, dominion, magistracy*. Whether an abstract power or an official is meant is not marked.

**Witness:** Ethiopic only — `[Bertalotto p]` `መልእክ` for `መልአክ` and **omits `ወሥልጣን፡ኢይክል`** — reading simply `ኢይከልእ፡ከሊአ`. ⚠️ **A whole clause missing from the manuscripts.**
🛑 **GE'EZ ALONE** — a clause present in one Ethiopic line and absent in the other, with nothing outside Ethiopic in existence.
