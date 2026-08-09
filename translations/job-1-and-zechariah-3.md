# Job 1:6–12 and Zechariah 3:1–2

Same method as `OUR-TRANSLATION.md`, `translations/genesis-6.md`, and
`translations/psalm-82.md`: translated from the consonantal Hebrew
(`hebrew-ot/morphhb`), using morphological parse codes and Strong's-number root
identification only, plus the witnesses on disk. No published English
translation, ancient or modern, and no gloss file, was consulted. Where the
grammar is genuinely ambiguous, every reading it permits is given.

Regenerate the underlying data with:
```
./tools/analyze.py Job 1 6 --range 12
./tools/analyze.py Zech 3 1 --range 2
./tools/allwitness.py Job 1 6   (and 7–12)
./tools/allwitness.py Zech 3 1   (and 2)
```

---

## Why these two passages are grouped: the central grammatical fact

Both passages share a word that has become, in later usage, a proper name:
**שָׂטָן**. Before translating either verse, the grammar of that word has to
be established, because it governs how every occurrence of it below is
rendered.

**הַשָּׂטָן** in Job 1:6 parses as `HTd/Ncmsa` — **particle d (the definite
article) + noun, common, masculine singular absolute.** The article is not
folded into the word as a fixed prefix of a proper name; the tool's own parse
breaks it out as a separate morpheme, exactly as it does for any other
common noun made definite (compare הָאָדָם, "the man," `HTd/Ncmsa`, in Gen 6:1–4).
Every one of the eight occurrences of the word across Job 1:6–12 and Zech
3:1–2 parses the same way: `[conjunction] + Td (article) + Ncmsa`. This holds
in Job 1:6, 1:7 (×2), 1:8, 1:9, 1:12 (×2), and in Zech 3:1 (וְ/הַ/שָּׂטָ֛ן) and
3:2 (הַ/שָּׂטָ֗ן, then הַ/שָּׂטָ֔ן again).

**The grammatical rule:** Biblical Hebrew proper names do not take the
definite article. יְהוָה, אִיּוֹב ("Job"), יְהוֹשֻׁעַ ("Joshua," Zech 3:1) —
every proper name in these very verses appears bare, with no article, because
that is how Hebrew proper names behave. A common noun made definite by the
article, by contrast, is not naming an individual by name; it is picking out
*a particular instance of a class*, the way "the accountant" or "the
messenger" picks out a role-holder, not a personal name. **הַשָּׂטָן** with
the article is grammatically in the second category: "the satan" in the sense
of "the accuser," "the adversary" — a title or role-description, definite
because the narrative has a specific role-holder in view, not because שָׂטָן
functions here as anyone's name.

**What follows from this, stated plainly and no further:** the grammar
establishes that in these two passages the word is a common noun with the
article, not a personal name. Whether that role, applied consistently across
Job and Zechariah, is *the same figure* both times, and what later theological
weight the title carries, is a question the article's presence does not by
itself answer — see the closing section.

### שָׂטָן as a common noun elsewhere — the range, checked

Strong's 7854 (שָׂטָן) occurs of human beings, without the article, doing
exactly what the common-noun sense predicts: functioning as an adversary or
accuser, a role a person can occupy.

- **1 Samuel 29:4** — `./tools/analyze.py 1Sam 29 4`. The Philistine commanders
  worry David will "become a שָׂטָן to us" (יִהְיֶה־לָּנוּ לְשָׂטָן, `HR/Ncmsa`
  — preposition + noun, common, masc singular **absolute, no article**) in
  battle — David himself, a human military rival, named with the bare common
  noun.
- **1 Kings 11:14** — YHWH raises up שָׂטָן (`HNcmsa`, absolute, no article) for
  Solomon: Hadad the Edomite, a human political adversary.
- **1 Kings 11:23** — likewise שָׂטָן (`HNcmsa`, no article) for Rezon son of
  Eliada, another human adversary YHWH raises against Solomon.
- **1 Kings 11:25** — Rezon again: וַיְהִי שָׂטָן לְיִשְׂרָאֵל, "and he was a
  שָׂטָן to Israel" (`HNcmsa`, no article) — the same word, same anarthrous
  form, of the same human figure, "all the days of Solomon."

Across these four occurrences the word's range is consistent: **an
adversary, an opponent, one who obstructs or accuses** — usable of any party
in that role, human or otherwise, definite or not. Nothing in the word itself
restricts it to a supernatural being; it is grammatically an ordinary common
noun for an oppositional role.

### 1 Chronicles 21:1 — the one place the usage differs

`./tools/analyze.py 1Chr 21 1`:

> וַיַּעֲמֹד **שָׂטָן** עַל־יִשְׂרָאֵל וַיָּסֶת אֶת־דָּוִיד לִמְנוֹת אֶת־יִשְׂרָאֵל

**שָׂטָן** here parses `HNcmsa` — noun, common, masculine singular **absolute**.
No article, no preposition-with-assimilated-article, nothing that could hide
a definite form. This is the one place among all the occurrences checked
where שָׂטָן stands as the grammatical **subject** of a verb (וַיַּעֲמֹד, "and
[he/it] stood up") with no article, functioning almost like a name in
narrative position even though its form is that of an ordinary indefinite
common noun. Every other occurrence checked in this document is either
anarthrous-and-clearly-a-role-word-for-a-named-human (1 Sam 29:4; 1 Kgs 11:14,
23, 25) or has the article (Job, Zechariah). 1 Chronicles 21:1 is unique in the
set: an unarticulated שָׂטָן that is nonetheless the subject inciting an
action, not predicated of an already-named human rival.

**The parallel at 2 Samuel 24:1** — `./tools/analyze.py 2Sam 24 1`:

> וַיֹּסֶף אַף־יְהוָה לַחֲרוֹת בְּיִשְׂרָאֵל וַיָּסֶת אֶת־דָּוִד בָּהֶם לֵאמֹר לֵךְ מְנֵה אֶת־יִשְׂרָאֵל וְאֶת־יְהוּדָה

The subject of the same verb of incitement (וַיָּסֶת, hiphil of סות, "and he
incited") in the Samuel telling of this event is **אַף־יְהוָה**, "the anger of
YHWH" (`HNp` יְהוָה in construct with אַף, "anger, nose"), not שָׂטָן. Both
accounts describe the identical event — David incited to take the census —
with the identical verb of incitement (וַיָּסֶת), but Samuel's grammatical
subject is YHWH's own anger, while Chronicles' grammatical subject is an
anarthrous שָׂטָן.

**What this establishes, precisely, and no further:** this is a real,
checkable grammatical fact — the same narrated action has two different
grammatical subjects in its two tellings, and 1 Chronicles 21:1 is the one
occurrence of שָׂטָן in this survey without the article, standing in a
subject position elsewhere occupied by "YHWH's anger." What that substitution
*means* — a later theological development separating out an accusing agent
distinct from YHWH, a stylistic variation, or something else — is not
something the grammar of either verse can settle by itself. It is reported
here as a difference in the text, not as evidence for a particular account of
why the difference exists.

---

# Job 1:6–12

## Word by word

**וַיְהִי** · `ו/יהי` · `HC/Vqw3ms` — conjunction + verb, qal, wayyiqtol 3ms
> Root **היה**, "to be, become, happen." Narrative-opening formula, as in Gen
> 6:1. **"And it came to pass"**

**הַיּוֹם** · `ה/יום` · `HTd/Ncmsa` — article + noun, masc singular absolute
> **יום**, "day," definite. **"the day"** — i.e. "on a/the day"

**וַיָּבֹאוּ** · `ו/יבאו` · `HC/Vqw3mp` — conjunction + verb, qal, wayyiqtol 3mp
> Root **בוא**, "to come, enter, go." **"and [they] came"**

**בְּנֵי הָאֱלֹהִים** · `בני` `HNcmpc` + `ה/אלהים` `HTd/Ncmpa` — construct plural
+ article + noun, masc plural absolute
> **בְּנֵי**: construct of **בן**, "son"; construct state broadens the sense
> to "members of, belonging to the class of" (as established at Deut 32:8 and
> Gen 6:2). **הָאֱלֹהִים**: **אלהים**, plural in form, taking singular
> agreement of the God of Israel or plural agreement of divine beings
> generally; carries the article here, exactly as at Gen 6:2/6:4. This is the
> **same construction** documented there: `translations/genesis-6.md` and
> `HIGHLIGHTS.md` lay out that this exact phrase, בְּנֵי הָאֱלֹהִים/בְּנֵי
> אֱלֹהִים, also stands (without the article) behind the older, non-Masoretic
> reading of Deut 32:8 (4Q37, LXX) and (with the article, as here) in Gen
> 6:2/6:4, uncontested in the Hebrew witnesses at those verses. **The parallel
> is real and worth stating: it is the identical construct phrase.** What it
> does *not* establish on its own is that Job 1:6 depicts the same beings, the
> same event, or the same theology as Gen 6 — only that Biblical Hebrew uses
> this same idiom, "sons of God/the God[s]," elsewhere for a group distinct
> from ordinary humans presenting themselves in a formal setting. Job's own
> use of a nearly identical phrase recurs at Job 2:1 and 38:7 (בְּנֵי אֱלֹהִים,
> at the founding of the world) — internal to the book, not cited further here
> since it falls outside the assigned range, but worth flagging as the phrase
> is not a one-off within Job itself.
> **"the sons of God"**

**לְהִתְיַצֵּב** · `ל/התיצב` · `HR/Vtc` — preposition לְ + verb, **hithpael**,
infinitive construct
> Root **יצב** (Strong's 3320), the same root family as Deut 32:8's יַצֵּב
> (hiphil, "he fixed/set in place" — established there under the closely
> related root נצב, the two being variant spellings of one weak-initial-נ
> root). The **hithpael** stem here is reflexive/reciprocal: not "to be set in
> place by another" but "to station *oneself*, to take *one's own* stand, to
> present oneself." This exact hithpael form of the root is the standard
> Biblical Hebrew idiom for **formally presenting oneself before a superior or
> in an assembly** — e.g. הִתְיַצֵּב לִפְנֵי פַרְעֹה, "present yourself before
> Pharaoh" (Exod 8:16, 9:13); הִתְיַצְּבוּ בְּאֹהֶל מוֹעֵד, "present
> yourselves at the tent of meeting" (Deut 31:14); הִתְיַצְּבוּ ... לִפְנֵי
> יְהוָה (1 Sam 10:19, Josh 24:1). Range: *to station oneself · to take one's
> stand · to present oneself (before someone in authority).*
> **"to present themselves"**

**עַל** · `על` · `HR` — preposition
> **על** has a wide range (*upon · over · against · concerning · beside · in
> the presence of*). With a verb of standing/presenting oneself before a
> superior, עַל regularly marks **attendance in a royal or divine presence**,
> not hostility — compare 1 Kgs 22:19 (`./tools/analyze.py 1Kgs 22 19`):
> "יְהוָה יֹשֵׁב עַל־כִּסְאוֹ וְכָל־צְבָא הַשָּׁמַיִם עֹמֵד **עָלָיו**
> מִימִינוֹ וּמִשְּׂמֹאלוֹ" — YHWH seated on his throne, "all the host of
> heaven standing **at his side/about him**, at his right and at his left."
> The construction [standing verb] + עַל + [enthroned figure] is that same
> council-attendance idiom there; Job 1:6 uses the reflexive-presenting verb
> plus the identical preposition for the same kind of scene. **"before" / "in
> attendance on"** (not "against")

**יְהוָה** · `יהוה` · `HNp` — the divine name. Left untransliterated, as
elsewhere in this project. **"YHWH"**

**וַיָּבוֹא גַם הַשָּׂטָן בְּתוֹכָם** · `ו/יבוא` `HC/Vqw3ms` (root בוא, as
above) + `גם` `HD` adverb + `ה/שטן` `HTd/Ncmsa` (established above: article +
common noun) + `ב/תוכ/ם` `HR/Ncmsc/Sp3mp` (preposition + construct noun
**תָּוֶךְ**, "midst," + 3mp suffix)
> **גַּם**: "also, even" — marking the satan's arrival as an addition to the
> scene just described. **בְּתוֹכָם**: "in their midst," i.e. among the sons
> of God who have just presented themselves. **"and the satan also came among
> them"**

## The verse

> **And it came to pass on the day that the sons of God came to present
> themselves before YHWH, that the satan also came among them.**

---

## Job 1:7

**וַיֹּאמֶר יְהוָה אֶל־הַשָּׂטָן** — "and YHWH said to the satan" (all forms as
established above)

**מֵאַיִן** · `מ/אין` · `HR/Ti` — preposition + interrogative particle
> **אַיִן**, "where" (interrogative). With מִן: "from where." **"from where"**

**תָּבֹא** · `תבא` · `HVqi2ms` — qal imperfect 2ms, root **בוא** (as above).
**"do you come"**

**וַיַּעַן הַשָּׂטָן אֶת־יְהוָה וַיֹּאמַר** — "and the satan answered YHWH and
said" · **וַיַּעַן**, root **ענה** (Strong's 6030), "to answer, respond."

**מִשּׁוּט** · `מ/שוט` · `HR/Vqc` — preposition מִן + verb, qal, infinitive
construct
> Root **שוט** (Strong's 7751). Its Biblical Hebrew occurrences (2 Sam 24:2,
> 8; Job 1:7, 2:2; 2 Chr 16:9; Jer 5:1, 49:3; Amos 8:12; Zech 4:10; Dan 12:4)
> consistently describe covering ground back and forth — the idiom at Zech
> 4:10 and 2 Chr 16:9, "the eyes of YHWH range/rove throughout all the
> earth" (עֵינֵי יְהוָה מְשׁוֹטְטִים בְּכָל־הָאָרֶץ), and at 2 Sam 24:2/8 of
> the census-takers "roving through" the tribes of Israel to count them. The
> range across these occurrences: *to rove · to roam · to range about · to go
> to and fro (covering territory).* Not aimless wandering so much as
> **surveying movement across a territory** — the same sense that fits the
> census-taking and the divine "eyes ranging the earth" idioms. **"from
> roving"**

**בָּאָרֶץ** · `ב/ארץ` · `HRd/Ncbsa` — preposition (with assimilated article)
+ noun. **"through the earth"**

**וּמֵהִתְהַלֵּךְ בָּהּ** · `ו/מ/התהלך` `HC/R/Vtc` (conjunction + preposition +
verb, **hithpael**, infinitive construct) + `ב/ה` `HR/Sp3fs`
> Root **הלך** (Strong's 1980), "to walk, go." Qal is the plain "walk"; the
> **hithpael** here is the iterative/reflexive stem, already documented in
> this corpus at Psalm 82:5 (יִתְהַלָּכוּ, "they walk about, go back and
> forth") and used elsewhere of Enoch (Gen 5:22, 24, הִתְהַלֶּךְ) and of the
> sound of God "walking about" in the garden (Gen 3:8, מִתְהַלֵּךְ) — a
> repeated, unhurried traversing, not a single directed trip. Range: *to walk
> about · to go back and forth · to traverse repeatedly.* **"and from walking
> about in it"**

> **And YHWH said to the satan, "From where do you come?" And the satan
> answered YHWH and said, "From roving through the earth, and from walking
> about in it."**

---

## Job 1:8

**הֲשַׂמְתָּ לִבְּךָ עַל־עַבְדִּי אִיּוֹב** · `ה/שמת` `HTi/Vqp2ms` (interrogative
particle + qal perfect 2ms, root **שים**, "to set, place") + `לב/ך`
(construct noun + 2ms suffix, "your heart") + `על` (preposition) + `עבד/י`
(construct noun + 1cs suffix, "my servant") + `איוב` (proper noun, "Job")
> Idiom: "to set one's heart upon" = to take note of, consider, fix attention
> on. **"Have you set your heart/attention on my servant Job"**

**כִּי אֵין כָּמֹהוּ בָאָרֶץ** — "for there is none like him in the earth" (כִּי,
conjunction "for"; אֵין, negative existential particle; כָּמֹהוּ, preposition
כְּ "like" + 3ms suffix; בָאָרֶץ, "in the earth")

**אִישׁ תָּם וְיָשָׁר יְרֵא אֱלֹהִים וְסָר מֵרָע** · `איש` `HNcmsa` + `תם`
`HAamsa` + `ו/ישר` `HC/Aamsa` + `ירא` `HAamsc` + `אלהים` `HNcmpa` + `ו/סר`
`HC/Vqrmsa` (qal participle, root **סור**, "to turn aside") + `מ/רע` `HR/Aamsa`
> **תָּם**: adjective, root תמם, "complete, whole, blameless." **יָשָׁר**:
> adjective, root ישר, "straight, upright." **יְרֵא אֱלֹהִים**: adjective
> construct + noun, "fearing God" — the same plural-form אֱלֹהִים discussed
> throughout this project, here taking the ordinary singular-referent sense
> ("God," not "gods"), consistent with its use for the deity elsewhere in
> Job's narrative frame. **וְסָר מֵרָע**: qal participle "turning aside" + מִן
> "from" + adjective רַע, "evil" — "and turning away from evil."
> **"a man blameless and upright, fearing God and turning away from evil"**

> **And YHWH said to the satan, "Have you set your attention on my servant
> Job? For there is none like him in the earth — a man blameless and upright,
> fearing God and turning away from evil."**

---

## Job 1:9

**וַיַּעַן הַשָּׂטָן אֶת־יְהוָה וַיֹּאמַר** — "and the satan answered YHWH and
said" (as v.7)

**הַחִנָּם** · `ה/חנם` · `HTi/D` — interrogative particle + adverb
> Root **חנן** family; the adverb **חִנָּם** (Strong's 2600) ranges across its
> occurrences (Gen 29:15; Exod 21:2, 11; 1 Sam 19:5; Job 1:9, 2:3, 9:17; Ps
> 35:7, 19, 69:5, 109:3; Prov 1:11, 17, 23:29, 24:28, 26:2; Ezek 6:10) between
> two related senses that both trace to the same root idea of something given
> or done **without payment or grounds**: (1) *for nothing, without payment,
> gratis* — Exod 21:2's freed slave who "goes out חִנָּם," without paying for
> his freedom; (2) *without cause, groundlessly, for no reason* — 1 Sam 19:5,
> David killed Goliath "without cause" against him; Prov 24:28, testifying
> against a neighbor חִנָּם, "without cause." Both senses are live for a
> single word depending on context; the interrogative here questions whether
> Job's fear of God is "for nothing" in the sense of *ungrounded, unearned by
> any incentive* — closer to sense (2), but the "unpaid/uncompensated" nuance
> of sense (1) is not absent, since the question that follows in vv.10–11
> turns on exactly what Job has been given in return. **"for nothing / without
> cause"**

**יָרֵא אִיּוֹב אֱלֹהִים** · `ירא` `HVqp3ms` (qal perfect 3ms, root **ירא**, "to
fear") + `איוב` + `אלהים` — **"does Job fear God"**

> **And the satan answered YHWH and said, "Is it for nothing that Job fears
> God?"**

---

## Job 1:10

**הֲלֹא אַתָּה שַׂכְתָּ בַעֲדוֹ וּבְעַד בֵּיתוֹ וּבְעַד כָּל־אֲשֶׁר־לוֹ מִסָּבִיב**
> **הֲלֹא**: interrogative + negative, "is it not." **אַתָּה**: "you." **שַׂכְתָּ**:
> qal perfect 2ms, root **שוך**, "to hedge, fence about, wall in." **בַעֲדוֹ**:
> preposition בְּעַד ("around, on behalf of") + 3ms suffix. **וּבְעַד בֵּיתוֹ**:
> "and around his house." **וּבְעַד כָּל־אֲשֶׁר־לוֹ מִסָּבִיב**: "and around all
> that is his, on every side." **"Have you not hedged him about, and his house,
> and all that he has, on every side?"**

**מַעֲשֵׂה יָדָיו בֵּרַכְתָּ וּמִקְנֵהוּ פָּרַץ בָּאָרֶץ**
> **מַעֲשֵׂה יָדָיו**: construct "the work of his hands." **בֵּרַכְתָּ**: piel
> perfect 2ms, root **ברך**, "to bless." **מִקְנֵהוּ**: "his livestock." **פָּרַץ**:
> qal perfect 3ms, root **פרץ**, "to break out, burst forth, spread out." **"You
> have blessed the work of his hands, and his livestock has spread out in the
> land."**

> **"Have you not hedged him about, and his house, and all that he has, on
> every side? You have blessed the work of his hands, and his livestock has
> spread out in the land."**

---

## Job 1:11

**וְאוּלָם שְׁלַח־נָא יָדְךָ וְגַע בְּכָל־אֲשֶׁר־לוֹ**
> **וְאוּלָם**: adversative adverb, "but, however." **שְׁלַח**: qal imperative
> 2ms, root **שלח**, "send, put forth." **נָא**: particle of entreaty. **יָדְךָ**:
> "your hand." **וְגַע**: qal imperative 2ms, root **נגע**, "touch." **בְּכָל־
> אֲשֶׁר־לוֹ**: "against all that is his." **"But put forth your hand now and
> touch all that is his"**

**אִם־לֹא עַל־פָּנֶיךָ יְבָרֲכֶךָּ**
> **אִם־לֹא**: oath-formula construction, "surely" (an idiom of asseveration —
> literally "if not," used in oaths to assert the opposite strongly).
> **עַל־פָּנֶיךָ**: "to your face." **יְבָרֲכֶךָּ**: piel imperfect 3ms + 2ms
> suffix, root **ברך**, "bless." The verb ברך in contexts like this one also
> carries an attested euphemistic range ("curse," the reverse sense, used to
> avoid writing the more direct word of cursing God) — noted here as a live
> possibility the root itself carries elsewhere, without asserting which sense
> is meant in this instance. **"surely he will bless [/curse] you to your
> face"**

> **"But put forth your hand now and touch all that is his — surely he will
> bless you to your face."**

---

## Job 1:12

**וַיֹּאמֶר יְהוָה אֶל־הַשָּׂטָן הִנֵּה כָל־אֲשֶׁר־לוֹ בְּיָדֶךָ**
> **הִנֵּה**: presentative particle, "behold." **כָל־אֲשֶׁר־לוֹ**: "all that is
> his." **בְּיָדֶךָ**: "in your hand." **"And YHWH said to the satan, 'Behold,
> all that is his is in your hand—'"**

**רַק אֵלָיו אַל־תִּשְׁלַח יָדֶךָ**
> **רַק**: restrictive particle, "only." **אֵלָיו**: "against him [himself]."
> **אַל־תִּשְׁלַח יָדֶךָ**: negative particle + qal jussive 2ms, root **שלח**
> (as v.11), "do not put forth your hand." **"—only against him do not put
> forth your hand.'"**

**וַיֵּצֵא הַשָּׂטָן מֵעִם פְּנֵי יְהוָה**
> **וַיֵּצֵא**: qal wayyiqtol 3ms, root **יצא**, "to go out." **מֵעִם**:
> compound preposition, "from with." **פְּנֵי יְהוָה**: construct "the face
> of," + YHWH. **"And the satan went out from the presence of YHWH."**

> **And YHWH said to the satan, "Behold, all that he has is in your hand;
> only against him himself do not put forth your hand." And the satan went
> out from the presence of YHWH.**

## The verses together — Job 1:6–12

> And it came to pass on the day that the sons of God came to present
> themselves before YHWH, that the satan also came among them. And YHWH said
> to the satan, "From where do you come?" And the satan answered YHWH and
> said, "From roving through the earth, and from walking about in it." And
> YHWH said to the satan, "Have you set your attention on my servant Job? For
> there is none like him in the earth — a man blameless and upright, fearing
> God and turning away from evil." And the satan answered YHWH and said, "Is
> it for nothing that Job fears God? Have you not hedged him about, and his
> house, and all that he has, on every side? You have blessed the work of his
> hands, and his livestock has spread out in the land. But put forth your
> hand now and touch all that is his — surely he will bless you to your
> face." And YHWH said to the satan, "Behold, all that he has is in your
> hand; only against him himself do not put forth your hand." And the satan
> went out from the presence of YHWH.

## Witnesses

`./tools/allwitness.py Job 1 6` (through `12`): no Dead Sea Scroll fragment
for Job 1 is present in this corpus — the Masoretic Leningrad Codex is the
only Hebrew witness on disk for these verses. An Aramaic **Targum** is present
for every verse (c. 2nd–9th c. CE, a translation, not a manuscript variant of
the Hebrew). It renders הַשָּׂטָן with the Aramaic cognate **סִטְנָא**/
**סִיטְנָא** throughout, itself carrying the Aramaic definite-state ending
(-א, "the-"), consistently — i.e. the Targum's translators also treated the
word as a definite common noun/title, not a bare name they transliterated. No
LXX/Septuagint text for Job is loaded in this project's witness tool, so no
Greek comparison is offered here.

---

# Zechariah 3:1–2

## Word by word

**וַיַּרְאֵנִי** · `ו/ירא/ני` · `HC/Vhw3ms/Sp1cs` — conjunction + verb,
**hiphil**, wayyiqtol 3ms + 1cs suffix
> Root **ראה**, "to see." Hiphil causative: "to cause to see, to show."
> **"And he showed me"**

**אֶת־יְהוֹשֻׁעַ הַכֹּהֵן הַגָּדוֹל** · `יהושע` `HNp` + `ה/כהן` `HTd/Ncmsa` +
`ה/גדול` `HTd/Aamsa`
> **יְהוֹשֻׁעַ**: proper noun, "Joshua" — no article, as proper names do not
> take one. **הַכֹּהֵן הַגָּדוֹל**: "the high priest" (article + noun, article +
> adjective — a title, definite, but a common-noun title, not a name).
> **"Joshua the high priest"**

**עֹמֵד לִפְנֵי מַלְאַךְ יְהוָה** · `עמד` `HVqrmsa` (qal participle, root
**עמד**, "to stand") + `ל/פני` `HR/Ncbpc` (preposition + construct "face(s)
of" = "before") + `מלאך` `HNcmsc` (construct, "messenger of") + `יהוה`
> **"standing before the messenger of YHWH"**

**וְהַשָּׂטָן עֹמֵד עַל־יְמִינוֹ** · `ו/ה/שטן` `HC/Td/Ncmsa` — conjunction +
article + noun, common, masc singular absolute
> As established above: the article is a separate, identifiable morpheme in
> the parse, exactly as at every occurrence in Job 1. **עֹמֵד**: qal
> participle, "standing" — the identical verb and form used two words earlier
> of Joshua standing before the messenger. **עַל־יְמִינוֹ**: preposition עַל +
> construct noun יָמִין ("right hand") + 3ms suffix — "at his right hand."
> This is the same [standing-verb] + עַל construction discussed at Job 1:6,
> and it matches, almost word for word, the scene at 1 Kgs 22:19 of the
> heavenly host positioned at the enthroned one's right and left
> (מִימִינוֹ וּמִשְּׂמֹאלוֹ). The position — flanking, at the right hand —
> describes a formal, attending stance in this scene, not by itself an act of
> attack; the hostile action is named separately, by the next word.
> **"and the satan standing at his right hand"**

**לְשִׂטְנוֹ** · `ל/שטנ/ו` · `HR/Vqc/Sp3ms` — preposition לְ + verb, **qal**,
**infinitive construct**, root שׂטן + 3ms suffix
> **This is the verb from the same root as הַשָּׂטָן itself** — Strong's 7853,
> the verbal cognate of the noun 7854. Parsed as an actual finite verb-form
> (infinitive construct), not a noun: literally "to satan/oppose him," i.e.
> "in order to accuse/oppose him." **What this shows about the word's basic
> force:** שׂטן is not merely a label that happens to be attached to a
> character; the same three consonants function as an ordinary Hebrew **verb**
> meaning "to accuse, oppose, be adversarial toward" — confirmed by this
> infinitive form functioning exactly as verbal infinitives do elsewhere
> (purpose/result: "[he is standing at his right hand] in order to
> accuse/oppose him"). The noun הַשָּׂטָן and the verb לְשִׂטְנוֹ share one
> root doing one basic thing: **the noun names the doer of the action the verb
> names.** This is a further, independent confirmation — from the verb, not
> just the noun's article — that שָׂטָן denotes a *function* (one who
> opposes/accuses) rather than operating as a proper name. **"to accuse
> him" / "to oppose him"**

> **And he showed me Joshua the high priest standing before the messenger of
> YHWH, and the satan standing at his right hand, to accuse him.**

---

## Zechariah 3:2

**וַיֹּאמֶר יְהוָה אֶל־הַשָּׂטָן** — "and YHWH said to the satan" (all forms as
established)

**יִגְעַר יְהוָה בְּךָ הַשָּׂטָן**
> **יִגְעַר**: qal jussive 3ms, root **גער**, "to rebuke." **בְּךָ**: "in/at
> you." **הַשָּׂטָן**: vocative, direct address, article + common noun as
> throughout — "O satan," in the sense of "O accuser." **"YHWH rebuke you, O
> satan"**

**וְיִגְעַר יְהוָה בְּךָ הַבֹּחֵר בִּירוּשָׁלָ͏ִם**
> Repetition of the rebuke formula. **הַבֹּחֵר**: article + qal participle,
> root **בחר**, "to choose" — "the one who chooses," a divine self-description
> ("YHWH... the chooser of Jerusalem"). **"and YHWH, who has chosen
> Jerusalem, rebuke you"**

**הֲלוֹא זֶה אוּד מֻצָּל מֵאֵשׁ**
> **הֲלוֹא**: interrogative + negative, "is not." **זֶה**: demonstrative,
> "this." **אוּד**: noun, "firebrand, burning stick." **מֻצָּל**: **hophal**
> passive participle, root **נצל**, "to snatch away, deliver" — passive:
> "snatched, plucked." **מֵאֵשׁ**: "from fire." **"Is this not a firebrand
> plucked from the fire?"**

> **And YHWH said to the satan, "YHWH rebuke you, O satan! YHWH, who has
> chosen Jerusalem, rebuke you! Is this not a firebrand plucked from the
> fire?"**

## The verses together — Zechariah 3:1–2

> And he showed me Joshua the high priest standing before the messenger of
> YHWH, and the satan standing at his right hand, to accuse him. And YHWH
> said to the satan, "YHWH rebuke you, O satan! YHWH, who has chosen
> Jerusalem, rebuke you! Is this not a firebrand plucked from the fire?"

## Witnesses

`./tools/allwitness.py Zech 3 1`: only the Masoretic Leningrad Codex is on
disk for verse 1 — no DSS or Targum text loaded for this verse in this
project's data.

`./tools/allwitness.py Zech 3 2`: **a Dead Sea Scroll fragment is present —
4Q80** (the Minor Prophets scroll, c. 250 BCE – 68 CE):

> `ו יומר יהוה אל ה שטן יגער יהוה ב׳ך ה שטן ו יגער יהוה ב׳ך ה בחר ב ירושלם ה
> לוא זה אוד מצל מ אש`

Stripped of the scroll's spacing/orthography, this reads **הַשָּׂטָן** — with
the article — in both occurrences, matching the Masoretic Leningrad Codex
exactly, word for word, no variant. Unlike Deut 32:8 (where the older scroll
and the Masoretic text disagree), the article on הַשָּׂטָן at Zech 3:2 is
attested identically in a Hebrew manuscript roughly a thousand years older
than Leningrad. This is not a contested reading; the definite article here is
solid across the witnesses on disk.

---

## Summary: what the grammar establishes, and what it does not

- **הַשָּׂטָן carries the definite article in every occurrence across Job
  1:6–12 and Zech 3:1–2** (eight occurrences total, confirmed by
  `analyze.py`'s morphological breakdown, and confirmed unchanged in the one
  place a Dead Sea Scroll survives to check it, Zech 3:2/4Q80). Hebrew proper
  names do not take the article. This is a hard grammatical fact: in these
  passages, the word is functioning as **a title or role-description** ("the
  accuser," "the adversary"), not as a personal name.
- **שָׂטָן as a bare common noun, without the article, is independently
  attested of human beings** — David (1 Sam 29:4), Hadad (1 Kgs 11:14), Rezon
  (1 Kgs 11:23, 25) — confirming the word's ordinary range is "adversary,
  opponent, one who obstructs or accuses," usable of any party in that role.
- **The verbal form לְשִׂטְנוֹ at Zech 3:1** — the qal infinitive construct of
  the same root, "to accuse/oppose him" — independently confirms that the
  root's basic force is an action (accusing, opposing), and the noun is an
  agent-title built on that action.
- **1 Chronicles 21:1 is the one occurrence checked where שָׂטָן appears
  without the article while still functioning as the grammatical subject of
  an act of incitement** — a position elsewhere in the parallel account (2 Sam
  24:1) occupied by "the anger of YHWH" (אַף־יְהוָה). This is a genuine,
  checkable difference in how the same narrated event is told in its two
  versions. The grammar shows the difference exists and precisely where; it
  does not by itself explain why the wording differs between the two books.
- **בְּנֵי הָאֱלֹהִים at Job 1:6 is the same construct phrase** already
  documented in this corpus at Gen 6:2/6:4 (with the article) and, in its
  older non-Masoretic form, at Deut 32:8 (without the article, 4Q37/LXX). The
  shared idiom is real; it does not by itself establish that Job, Genesis, and
  the older Deuteronomy text all describe identical beings or events — only
  that Biblical Hebrew uses this construction elsewhere for a group other than
  ordinary humans "presenting themselves" in a formal setting.
- **What the grammar cannot settle:** whether "the satan" of Job and
  "the satan" of Zechariah are meant as the same figure, what later
  theological development did with this title, and how the anarthrous
  1 Chronicles 21:1 relates historically to the article's presence everywhere
  else surveyed here. These are real questions; they are questions for
  theology, literary history, and further textual comparison beyond the
  Masoretic/DSS/Targum data on disk — not questions Biblical Hebrew grammar,
  by itself, resolves. Reported as open, not adjudicated.

---

*Analytical data: `hebrew-ot/morphhb` (CC BY), `dead-sea-scrolls/etcbc-dss`
(CC BY-NC), `targums/*`. Regenerate the underlying readings with
`./tools/allwitness.py Job 1 <verse>` (6 through 12), `./tools/allwitness.py
Zech 3 <verse>` (1, 2), and `./tools/analyze.py Job 1 6 --range 12` /
`./tools/analyze.py Zech 3 1 --range 2`. The 1 Sam 29:4, 1 Kgs 11:14/23/25,
1 Chr 21:1, 2 Sam 24:1, and 1 Kgs 22:19 comparisons were checked directly with
`./tools/analyze.py` against the references named. The English is this
project's own.*
