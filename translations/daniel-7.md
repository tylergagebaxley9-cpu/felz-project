# Daniel 7:9-14

## Language note — this passage is Aramaic, not Hebrew

Daniel 2:4b-7:28 is written in Imperial Aramaic, not Hebrew. This project
verified from disk that **Daniel is 61.3% Aramaic** by word count. Daniel
7:9-14 falls inside that Aramaic block. `./tools/analyze.py` confirms this
directly — every parse code for this passage begins with **A** (Aramaic),
not **H** (Hebrew): `AVqrmsa`, `ANcmpa`, `AR/Sp3ms`, and so on. Root
identification below uses Strong's numbers only for pointing at the
consonantal root, exactly as `OUR-TRANSLATION.md` does for Hebrew.

## What this is built from, and what it is not

Same discipline as `OUR-TRANSLATION.md`:

**Used** — the Aramaic consonantal text (`hebrew-ot/morphhb`), morphological
parse codes, Strong's numbers for root identification, and the Dead Sea
Scrolls readings for this passage (`./tools/allwitness.py Dan 7 <verse>`).

**Not used** — no published English translation, ancient or modern, no
gloss file, no interlinear English column. The semantic ranges below come
from how each root behaves across its own Biblical Aramaic occurrences, not
from a dictionary gloss.

---

## Word by word

### Verse 9

**חָזֵה הֲוֵית** `חזה` `AVqrmsa` + `הוית` `AVqp1cs` — qal participle + qal
perfect 1cs of **הוה** ("to be")
> This periphrastic pairing (participle + "was/were") recurs through the
> whole vision (7:2, 4, 6, 7, 9, 11×2, 13, 21) and marks durative, ongoing
> watching, not a single glance. Root **חזה**: to see, look at, watch, gaze —
> the same root that gives Aramaic (and Hebrew) its word for a "vision."
> **"I kept watching / I was watching"**

**עַד דִּי** — preposition + relative particle. **"until"**

**כָרְסָוָן** `כרסון` `ANcmpa` — noun, common, masculine **plural** absolute
> Root **כרסא/כרסה**, "throne, seat of authority." This form is plural:
> **"thrones"** — not "a throne." See the note below on the plural-vs-singular
> throne language in this verse.

**רְמִיו** `רמיו` `AVQp3mp` — verb, passive (Peil) perfect 3mp
> Root **רמה/רמא**: literally "to throw, cast, hurl." Used of furniture being
> set down, the extended sense is "to place, set in position" — but the base
> image is a throwing-down, not a gentle placement. The form is passive: the
> thrones were cast/set in place, and **no agent is named** — the clause does
> not say who set them there.
> Range: *to throw · to cast · to set/place (down).*
> **"were set down" / "were cast in place"**

**וְעַתִּיק יוֹמִין** `ו/עתיק` `AC/Aamsc` + `יומין` `ANcmpa` —
conjunction + adjective, masculine singular **construct**, governing a
plural noun
> Root **עתק**: to move forward, advance, proceed onward — in the adjective,
> "advanced, aged, far along (in time)." **יוֹמִין** is the ordinary plural of
> **יוֹם**, "day": "days," here indefinite/general plural, not "the Days."
> The construct binds them: literally **"advanced-of days"** / **"aged of
> days"** — i.e. one who is far advanced in years, extremely old. This is
> the idiom conventionally carried into English as "Ancient of Days"; the
> elements themselves say **advanced-in-years, of days** — venerable
> extreme age, not a proper name.
> Range of עַתִּיק: *advanced (in years) · aged · ancient · venerable.*
> **"and one advanced in days" / "and the Aged of Days"**

**יְתִב** `יתב` `AVqp3ms` — qal perfect 3ms, root **יתב**
> To sit, dwell, take one's seat. Perfect here marks entry into session —
> the act of sitting down/taking his seat, not an ongoing state.
> **"took his seat" / "sat down"**

**לְבוּשֵׁהּ כִּתְלַג חִוָּר** — "his garment/clothing" (לְבוּשׁ, from **לבש**
"to clothe") + "like snow" (כְּ + תְלַג) + "white" (חִוָּר). **"his clothing
was white as snow"**

**וּשְׂעַר רֵאשֵׁהּ כַּעֲמַר נְקֵא** — "and the hair (שְׂעַר) of his head
(רֵאשֵׁהּ)" + "like wool (עֲמַר), pure/clean (נְקֵא, root **נקא/נקה**)."
**"and the hair of his head was like pure wool"**

**כָּרְסְיֵהּ** `כרסי/ה` `ANcmsc/Sp3ms` — noun, masculine **singular**
construct + 3ms suffix
> Same root as כָרְסָוָן above (**כרסא**, "throne"), but here **singular**,
> with a 3ms possessive suffix: **"his throne."** The verse opened with
> **plural thrones being set down**, and now narrows to **one throne**,
> described in detail, belonging to the figure who just sat down.
> **"his throne"**

**שְׁבִיבִין דִּי־נוּר** — "flames (שְׁבִיבִין, root **שביב**) of fire (נוּר)."
**"flames of fire"**

**גַּלְגִּלּוֹהִי נוּר דָּלִק** — "its wheels (גַּלְגִּלּוֹהִי, root **גלגל**,
"wheel") [were] burning (דָּלִק, qal participle, root **דלק**, "to burn,
blaze") fire." **"its wheels were burning fire"**

### On the plural thrones (כָרְסָוָן) and the one throne (כָּרְסְיֵהּ)

The grammar is plain and worth stating exactly: v.9 opens with **plural**
thrones (כָרְסָוָן, "thrones") being set down with no stated occupants named
for the extra seats, and the verse's remaining description — the white
clothing, the wool-like hair, the fiery wheeled seat — is then given for
**one** throne (כָּרְסְיֵהּ, "his throne," singular, bound to "the Aged of
Days" by the suffix). The text itself never says who sits in the other
thrones, or how many there are beyond "more than one."

**Literary parallel, clearly labelled as such:** `translations/psalm-82.md`
translates a scene of *אֱלֹהִים* standing "in the assembly of El, in the
midst of the gods (אֱלֹהִים)" — a plural divine council convened around a
presiding figure. Daniel 7:9's plural thrones with one described occupant
is **structurally reminiscent** of that council-scene pattern found
elsewhere in the Hebrew Bible. This is a **literary/thematic parallel
between two separate texts, not textual evidence about Daniel 7 itself** —
nothing in Daniel 7:9's own witnesses (Masoretic; no DSS reading survives
for this verse, see below) says who occupies the other thrones, whether they
are occupied by other divine beings, angels, a heavenly court, or are
simply narrative furniture. The verse does not resolve this by itself.

### Verse 10

**נְהַר דִּי־נוּר נָגֵד וְנָפֵק מִן־קֳדָמוֹהִי** — "A river of fire was
flowing (נָגֵד, root **נגד**, "to flow, draw out") and going forth (נָפֵק,
root **נפק**, "to go out, come forth") from before him."

**אֶלֶף אַלְפִין יְשַׁמְּשׁוּנֵּהּ** — "a thousand thousands were serving/
ministering to him" (יְשַׁמְּשׁוּנֵּהּ, piel imperfect 3mp + 3ms suffix, root
**שמש**, "to serve, minister, attend upon" — an intensive stem, personal
attendance).

**וְרִבּוֹ רִבְבָן קָדָמוֹהִי יְקוּמוּן** — "and ten thousand ten-thousands
were standing before him" (root **קום**, "to stand, arise").

**דִּינָא יְתִב** — "the court/judgment (דִּינָא, determined) sat" — same
verb יְתִב as the Aged of Days "sat" in v.9: the court convenes.

**וְסִפְרִין פְּתִיחוּ** — "and books (סִפְרִין) were opened (פְּתִיחוּ,
passive perfect 3mp, root **פתח**)."

### Verse 11 — DSS witness

`./tools/allwitness.py Dan 7 11` returns a scroll reading: **4Q113** carries
seven tracked word-slots for this verse, of which only two have surviving
ink — the consonants **רנ** and, in the next slot, **א**. Positionally (the
third and fourth of seven slots) this falls where the Masoretic text has
**קַרְנָא** ("the horn") in the clause "because of the sound of the great
words that the horn was speaking" — consistent with, but far short of
proof of, the MT wording at that point. Everything else in the verse is a
lacuna in this scroll (blank slots, no ink recorded). Reported here exactly
as the tool returns it; no restoration is assumed beyond what the tool
prints.

**חָזֵה הֲוֵית בֵּאדַיִן מִן־קָל מִלַּיָּא רַבְרְבָתָא דִּי קַרְנָא
מְמַלֱּלָה חָזֵה הֲוֵית עַד דִּי קְטִילַת חֵיוְתָא וְהוּבַד גִּשְׁמַהּ
וִיהִיבַת לִיקֵדַת אֶשָּׁא**
> "I kept watching then, because of the sound of the great words that the
> horn was speaking; I kept watching until the beast was killed, and its
> body was destroyed, and it was given over to the burning of fire."

### Verse 12

**וּשְׁאָר חֵיוָתָא הֶעְדִּיו שָׁלְטָנְהוֹן** — "and the rest of the beasts
(שְׁאָר, "remainder") — their dominion (שָׁלְטָן, root **שלט**, "to have
power/authority over") was removed" (הֶעְדִּיו, hiphil perfect 3mp, root
**עדה/עדי**, "to pass on, pass away, remove" — causative "they removed" used
impersonally, "it was taken away").

**וְאַרְכָה בְחַיִּין יְהִיבַת לְהוֹן עַד זְמַן וְעִדָּן** — "but a
lengthening (אַרְכָה, root **ארך**, "to be long") in life was given
(יְהִיבַת, passive perfect 3fs, root **יהב**) to them for a season and a
time" (זְמַן... וְעִדָּן — the same word עִדָּן that returns famously at
Dan 7:25, "a time, times, and half a time").

### Verse 13 — the crux: כְּבַר אֱנָשׁ

**חָזֵה הֲוֵית בְּחֶזְוֵי לֵילְיָא** — "I kept watching in the visions of
the night" (חֶזְוֵי construct plural of the same root חזה as v.9; לֵילְיָא,
determined, "the night").

**וַאֲרוּ עִם־עֲנָנֵי שְׁמַיָּא** — "and behold (וַאֲרוּ, presentative
particle), with the clouds of heaven" (עֲנָנֵי construct plural "clouds of";
שְׁמַיָּא determined "the heavens/sky").

**כְּבַר אֱנָשׁ** `כ/בר` `AR/Ncmsc` + `אנש` `ANcmsa` — preposition + noun
construct + noun absolute
> This is the phrase itself, and the grammar is not in doubt. **בַּר** is
> the Aramaic word for "son" (construct state here — "son of"). **אֱנָשׁ** is
> the ordinary Aramaic word for "human being, mankind, humanity" — the
> Aramaic cognate of Hebrew אֱנוֹשׁ. Put together, **כְּבַר אֱנָשׁ** is
> literally **"like a son of man,"** and "son of X" is a completely
> standard Aramaic (and Hebrew) idiom for "a member of the category X" —
> "son of man" this way simply means **"a human being."**
>
> The prefixed **כְּ** ("like, as") is a preposition of comparison — it
> marks a **simile**. That is doing real, identifiable grammatical work: the
> text is not saying the figure in the vision *is* labelled "a human being"
> as a name or title; it says the figure appeared **like** one — resembling
> a human being in form, as compared to the four beasts of the preceding
> visions (a lion, a bear, a leopard, and a nondescript fourth beast) which
> this figure is *not* like.
>
> **What this settles:** the phrase, grammatically, means "one with the
> appearance of a human being" — an ordinary Aramaic way of describing a
> human-shaped figure, exactly as "son of man" (without the comparative כְּ)
> is used elsewhere in Aramaic and Hebrew simply to mean "a human" or, in
> address (e.g. throughout Ezekiel's Hebrew), "mortal."
>
> **What this does not settle:** a simile in a visionary description does
> not, by grammar alone, determine what the figure *is* ontologically —
> human, angelic, heavenly, or divine. "Appeared like a human being" is
> compatible with a strictly human figure, with an angelic being described
> in human terms (as celestial beings elsewhere in Daniel and other
> apocalyptic texts are), or with something the text leaves deliberately
> unspecified. The grammar supplies the comparison; it does not supply the
> identity. Verses 13-14 describe what is *given* to this figure
> (everlasting dominion, glory, kingship, universal service) without
> further specifying his nature, and Daniel 7:27 later assigns comparable
> dominion to "the people of the holy ones of the Most High" — which is
> itself a separate interpretive question this file is not resolving.
> **"like a son of man" / "like a human being" / "one in human form"**

**אָתֵה הֲוָה** `אתה` `AVqrmsa` + `הוה` `AVqp3ms` — periphrastic, qal
participle + qal perfect 3ms of **הוה**, matching the durative pattern used
throughout the vision. **"was coming"**

**וְעַד־עַתִּיק יוֹמַיָּא מְטָה** — "and he came/arrived (מְטָה, qal
perfect 3ms, root **מטא/מטה**, "to reach, arrive at") to the Aged of Days."
Here the noun is spelled **יוֹמַיָּא** — plural, **determined** ("the
days") — vs. v.9's indefinite plural **יוֹמִין**. Both instances name the
same figure; the construct sense (see v.9 above) is unchanged.

**וּקְדָמוֹהִי הַקְרְבוּהִי** — "and they brought him near before him" /
"and he was presented before him" (הַקְרְבוּהִי, hiphil perfect 3mp +
3ms suffix, root **קרב**, "to come near, approach" — hiphil causative,
"to bring near, present." The subject "they" is unexpressed/impersonal;
Aramaic regularly uses an unmarked 3mp verb this way where English would
use a passive.)

### Verse 14 — who gives, to whom, and פְּלַח

**וְלֵהּ יְהִיב שָׁלְטָן** `ו/ל/ה` `AC/R/Sp3ms` + `יהיב` `AVQp3ms` —
conjunction + preposition + suffix ("and to him") + passive (Peil) perfect
3ms of **יהב** ("to give")
> The verb is **passive**, and the clause names **no subject**. Literally:
> "and to him, dominion was given" — there is no expressed grammatical
> agent for "gave" anywhere in this clause. **לֵהּ** ("to him") is explicit
> and unambiguous as the *recipient*: by direct narrative continuity from
> v.13, "him" is the figure just described as "one like a son of man," now
> standing before the Aged of Days. **Who gives is not stated by the
> grammar of this verb.** The only candidate in the immediate narrative
> context is the Aged of Days, before whom the figure was just presented in
> v.13 — a reasonable inference from the scene's sequence, and the kind of
> unnamed-agent passive ("it was given," "it was granted") that apocalyptic
> Aramaic and Hebrew use elsewhere to avoid naming God as the grammatical
> subject of a verb. But that identification is drawn from context and
> narrative sequence, not from anything the word יְהִיב itself supplies.
> **"and to him was given"**

**שָׁלְטָן וִיקָר וּמַלְכוּ** — "dominion/authority (שָׁלְטָן, root
**שלט**) and glory/honor (יְקָר, root **יקר**) and kingship/royal rule
(מַלְכוּ, root **מלך**)."

**וְכֹל עַמְמַיָּא אֻמַיָּא וְלִשָּׁנַיָּא** — "and all peoples (עַמְמַיָּא),
nations (אֻמַיָּא), and languages (לִשָּׁנַיָּא)" — a fixed triad that recurs
across Daniel (3:4, 7, 29; 5:19; 6:26).

**לֵהּ יִפְלְחוּן** `ל/ה` `AR/Sp3ms` + `יפלחון` `AVqi3mp` — "to him they
will **פלח**" (qal imperfect 3mp, root **פלח**)
> Root **פלח**'s actual occurrences in Biblical Aramaic: Dan 3:12, 14, 17,
> 18, 28 — refusing to "serve/worship" (פלח, paired explicitly with **סגד**,
> "bow down, worship") the king's gods or the golden image; Dan 6:17(16),
> 21(20) — Darius describing Daniel's God, "whom you serve (פלח)
> continually"; Ezra 7:24 — "servants (פלחי) of this house of God," temple
> cultic personnel; and Dan 7:27, where "all dominions" are said to **פלח**
> and obey "the people of the holy ones of the Most High."
>
> Every attested Biblical Aramaic occurrence of this root involves either
> explicit cultic worship of a deity (paired with "bow down" in Dan 3),
> devotional service to a god (Dan 6), or cultic/temple service (Ezra 7:24)
> — **except** Dan 7:27, which uses the identical verb for "all dominions"
> submitting to a *people's* rule, in a plainly political register. The
> root itself does not carry a marker distinguishing "render cultic
> worship" from "render total political submission" — in this small
> corpus, the same word covers both, and the object determines nothing
> about which sense is meant beyond what the scene independently indicates.
> Applied to v.14, where "all peoples, nations, and languages" **פלח** the
> figure who has just received שָׁלְטָן ("dominion"), יְקָר ("glory"), and
> מַלְכוּ ("kingship") from an unnamed giver: **the verb by itself
> underdetermines whether this is being described as worship of a divine
> or quasi-divine figure, or as the total political submission owed to a
> universal sovereign, or (given 7:27's parallel) both at once.** Biblical
> Aramaic does not lexically separate these categories the way, say,
> English "worship" and "obey" do.
> Range: *to serve · to minister to · to worship · to render (cultic or
> total) service to.*
> **"they will serve/worship him"**

**שָׁלְטָנֵהּ שָׁלְטָן עָלַם דִּי־לָא יֶעְדֵּה** — "his dominion is a
dominion of eternity/an everlasting dominion (עָלַם, "long duration, an
age, eternity") which will not pass away (יֶעְדֵּה, qal imperfect 3ms, same
root **עדה** as v.12's "was removed" — the other kingdoms' dominion *is*
removed; this one's will *not* pass away — the text uses the identical root
for both, in deliberate contrast)."

**וּמַלְכוּתֵהּ דִּי־לָא תִתְחַבַּל** — "and his kingdom (מַלְכוּתֵהּ) is
one that will not be destroyed/ruined" (תִתְחַבַּל, Hitpe'el imperfect 3fs,
root **חבל**, "to injure, ruin, destroy" — reflexive/passive: "be
destroyed").

---

## The verses, whole (Masoretic Aramaic text)

> **[9]** I kept watching until thrones were set down, and the Aged of Days
> took his seat. His clothing was white as snow, and the hair of his head
> was like pure wool. His throne was flames of fire; its wheels were
> burning fire.
>
> **[10]** A river of fire was flowing and going out from before him. A
> thousand thousands were serving him, and ten thousand ten-thousands were
> standing before him. The court sat, and books were opened.
>
> **[11]** I kept watching then, because of the sound of the great words
> that the horn was speaking. I kept watching until the beast was killed,
> and its body was destroyed, and it was given over to the burning of fire.
>
> **[12]** As for the rest of the beasts, their dominion was removed, but a
> lengthening of life was given to them for a season and a time.
>
> **[13]** I kept watching in the visions of the night, and behold, with
> the clouds of heaven, one like a son of man was coming; and he came to
> the Aged of Days, and he was brought near before him.
>
> **[14]** And to him was given dominion, and glory, and kingship, and all
> peoples, nations, and languages will serve/worship him. His dominion is
> an everlasting dominion which will not pass away, and his kingdom is one
> that will not be destroyed.

---

## Dead Sea Scrolls — what survives at Daniel 7:9-14

`./tools/allwitness.py` was run for every verse in this passage. Daniel's
Cave 4 scrolls on disk in this corpus are **4Q112, 4Q113, 4Q115**. A direct
scan of the underlying Text-Fabric data (matching `book`/`chapter` tags
across all three scrolls' word nodes in Dan 7) gives their actual chapter
coverage:

- **4Q112** — verses 5, 6, 7, 25, 26, 27, 28
- **4Q113** — verses 1, 2, 3, 4, 5, 6, 11, 25, 26, 27, 28
- **4Q115** — verses 15, 16, 17, 18, 19, 20, 21, 22, 23

**Verses 9, 10, 12, 13, and 14 — the entire passage this file translates,
except v.11 — are not extant in any of the three Daniel scrolls in this
corpus.** That includes v.13, the "one like a son of man" verse, and v.14,
the dominion-and-service verse: **no Qumran Aramaic witness for either
survives on this disk.** This was checked directly, not inferred from a
verse-by-verse `allwitness.py` call returning empty — see the raw per-scroll
verse lists above.

**Verse 11** is the one exception, and even there the surviving text is
minimal: `./tools/allwitness.py Dan 7 11` reports (no "⚠ SCROLLS DISAGREE"
flag — only one scroll carries any text here):

> **[4Q113]** רנ א

4Q113 tracks seven word-positions for this verse; five are blank (no ink
recorded), and the surviving two fragments — **רנ** and, in the next
position, **א** — sit, positionally, where the Masoretic text has **קַרְנָא**
("the horn") in "the sound of the great words that the horn was speaking."
That position match is suggestive but not proof of the full Masoretic
wording; it is two consonant-fragments, not a control reading of the
clause.

**Net finding:** this corpus's Qumran evidence for Daniel 7:9-14 amounts to
a two-letter fragment at v.11, positionally consistent with "the horn," and
nothing at all — not agreement, not disagreement, simply absence — for
vv.9, 10, 12, 13, and 14. Any claim that the Dead Sea Scrolls "confirm" or
"preserve" the son-of-man verse or the dominion verse in their present
wording is not supported by what is on this disk. The manuscript record for
this exact stretch of text is silence.

---

## Summary — what the Aramaic supports and does not

- **עַתִּיק יוֹמִין / עַתִּיק יוֹמַיָּא** ("Ancient of Days"): literally "one
  advanced/aged in days" — extreme, venerable old age, expressed as a
  construct chain, not a formal name.
- **כָרְסָוָן ... כָּרְסְיֵהּ** (thrones, plural, v.9a; his throne, singular,
  v.9b): the grammar itself shifts from plural to singular within the
  verse. Who occupies the unnamed extra thrones is not stated. Divine-
  council language elsewhere (Ps 82, `translations/psalm-82.md`) is a
  literary parallel worth naming — not textual evidence bearing on Daniel
  7 itself.
- **כְּבַר אֱנָשׁ** ("like a son of man"): grammatically a simile
  (comparative כְּ) built on the ordinary idiom "son of X" = "member of
  category X." It plainly means "resembling/like a human being." It does
  not, by grammar alone, establish whether the figure so described is
  human, angelic, or divine — that is an interpretive question the simile
  leaves open.
- **וְלֵהּ יְהִיב שָׁלְטָן** (v.14): a passive verb with an unnamed agent.
  The recipient ("to him") is unambiguous from context — the son-of-man
  figure of v.13. The giver is not named by the grammar; the Aged of Days
  is the only contextual candidate, inferred from sequence, not stated.
- **יִפְלְחוּן** (v.14, from **פלח**): its range in Biblical Aramaic covers
  cultic worship, devotional service to a god, and (once, at Dan 7:27,
  the same verb) political submission to a people's rule. The word does
  not itself distinguish these; v.14 underdetermines whether "serve" here
  means worship, political homage, or both.
- **The Similitudes of 1 Enoch** (1 En 37-71) use "that Son of Man" as a
  fixed title for a pre-existent, enthroned, heavenly judge —
  `docs/RESEARCH-enoch-influence.md` §3. Whether/how that tradition relates
  to Daniel 7:13 is a genuinely open scholarly question, further
  complicated by the fact that the Similitudes' own date is contested
  (Milik's minority post-Christian dating vs. the VanderKam/Nickelsburg/
  Charlesworth majority pre-Christian dating). This file does not resolve
  that question or assume a direction of influence in either direction —
  it is flagged here as relevant context, not settled by anything in
  Daniel 7:9-14's own grammar.

---

*Analytical data: `hebrew-ot/morphhb` (CC BY), `dead-sea-scrolls/etcbc-dss`
(CC BY-NC). Regenerate the underlying readings with
`./tools/analyze.py Dan 7 9 --range 14` and `./tools/allwitness.py Dan 7 <verse>`
for verses 9-14. The English is this project's own.*
