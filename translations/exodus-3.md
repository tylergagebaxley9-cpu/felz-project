# Exodus 3:13–15

The revelation of the divine name. Translated from the Hebrew consonantal text
and cross-checked against the Septuagint and the Samaritan Pentateuch — both
read directly from the corpus, not from any published English translation.
Method as stated in `translations/OUR-TRANSLATION.md`: grammatical analysis is
used; nobody else's English is.

**On the witnesses**: the Dead Sea Scrolls corpus on disk does not carry this
passage — checked two ways, `./tools/allwitness.py Exod 3 14` and
`./tools/dssread.py Exod 3 14`, both return nothing (`dssread.py` explicitly:
"no scroll on disk carries Exod 3:14"). This is a real absence, not a
lookup failure: no fragment covering Exodus 3 survives in this corpus. The
Samaritan Pentateuch *is* on disk (`samaritan/sp/`) and covers this passage,
but `allwitness.py`'s built-in reader has the same class of bug documented in
`docs/RESEARCH-divine-name.md` for DSS scroll membership: its `book`/`chapter`/
`verse` features are recorded only on book/chapter/verse-type nodes, not on
word nodes, so the naive per-word lookup silently returns nothing. Below, the
Samaritan reading was recovered directly by walking `oslots.tf` (word node →
underlying sign range → containing verse node), the same containment-lookup
method `dssmap.py` uses for DSS scrolls.

---

## Word by word — verse 13

**וַיֹּאמֶר** · `ו/יאמר` · `HC/Vqw3ms` — conjunction + verb, qal, wayyiqtol 3ms
> Root **אמר** (ʾ-m-r), "to say." The wayyiqtol is the standard Hebrew narrative
> past — "and he said," advancing the story.

**מֹשֶׁה אֶל־הָאֱלֹהִים** — "Moses, to the God" / "to God"
> **הָאֱלֹהִים**: the noun אֱלֹהִים (see below) with the definite article. Definite
> here — "the God," i.e. the specific deity just speaking with Moses, not "a
> god" generically.

**הִנֵּה אָנֹכִי בָא** · `הנה`/`אנכי`/`בא` · `HTm`/`HPp1cs`/`HVqrmsa`
> **הִנֵּה**: presentative particle. *Behold · look · here is.* Draws attention to
> what follows.
> **אָנֹכִי**: independent 1cs pronoun, "I" — emphatic, since the verb form
> already carries the person; its presence foregrounds the subject.
> **בָא**: qal active participle of **בוא** (b-w-ʾ), "to come, go, enter." The
> participle expresses an ongoing or imminent action: **"I am coming"** /
> "I am about to go."

**אֶל־בְּנֵי יִשְׂרָאֵל** — "to the sons of Israel" (בְּנֵי as construct, "sons of /
members of," per Deut 32:8 above)

**וְאָמַרְתִּי לָהֶם** · `ו/אמרתי`/`ל/הם` · `HC/Vqq1cs`
> **אָמַרְתִּי**: qal perfect 1cs with vav-consecutive — in this sequence, future
> in force: **"and I will say to them."**

**אֱלֹהֵי אֲבוֹתֵיכֶם שְׁלָחַנִי אֲלֵיכֶם** — "the God of your fathers has sent me to you"
> **אֱלֹהֵי**: construct of אֱלֹהִים (below), "God of."
> **אֲבוֹתֵיכֶם**: אָב, "father," plural + 2mp suffix. **"your fathers."**
> **שְׁלָחַנִי**: root **שלח** (š-l-ḥ), "to send." Qal perfect 3ms + 1cs suffix:
> "he has sent me." Range: *to send · to send out · to dispatch.*

**וְאָמְרוּ לִי מַה־שְּׁמוֹ** — "and they will say to me, 'What is his name?'"
> **מַה**: interrogative particle, *what.*
> **שְּׁמוֹ**: **שֵׁם** (name, see v.15 below) + 3ms suffix, "his name."

**מָה אֹמַר אֲלֵהֶם** — "what shall I say to them?"
> **אֹמַר**: qal imperfect 1cs of אמר. Standalone imperfect, deliberative
> question — "what am I to say."

### Verse 13, whole

> **And Moses said to the God, "Look, I am going to the sons of Israel, and I
> will say to them, 'The God of your fathers has sent me to you,' and they
> will say to me, 'What is his name?' — what shall I say to them?"**

---

## Word by word — verse 14 (the crux)

**וַיֹּאמֶר אֱלֹהִים אֶל־מֹשֶׁה** — "And God said to Moses"

**אֱלֹהִים** · `אלהים` · `HNcmpa` — noun, common, masculine plural absolute
> **אֱלוֹהַּ / אֱלֹהִים**. Plural in form. Takes plural agreement when it means
> "gods" generally, singular agreement when it refers to the God of Israel.
> Here the verb is 3ms (וַיֹּאמֶר, "he said," not "they said") — singular
> agreement, so the form is functioning as a singular referent: **"God."**
> Range: *God · gods · divine beings · a god* — disambiguated to singular by
> verb agreement in this verse, exactly as with Deut 32:8's אֱלֹהִים discussion.

**אֶהְיֶה** · `אהיה` · `HVqi1cs` — verb, qal, imperfect, 1st common singular
> Root **היה** (h-y-h). This is Biblical Hebrew's verb of being, but not a
> simple copula — ordinary present-tense predication in Hebrew is normally a
> **verbless** nominal clause ("the man [is] good," no verb needed). היה is
> used specifically where *existence, coming-into-being, becoming, or an event
> occurring/continuing* is in view. Range: *to be · to exist · to become · to
> happen, come to pass · to be present · to continue being.* The fact that a
> finite verb is used here at all — rather than a bare pronoun-clause — is
> itself meaningful: it points toward a dynamic sense (being/becoming/being-
> present) rather than a static predicate-nominative "I am [a specific thing]."
>
> **Imperfect (yiqtol) aspect**: Biblical Hebrew's imperfect encodes
> *imperfective* aspect — action viewed as incomplete, ongoing, or not yet
> concluded — not a fixed English tense. Depending on context it can render as
> simple future ("I will be"), habitual/durative present ("I am, continually"),
> or modal senses (potential/volitional — "I can be," "I would be"). Standing
> alone, outside a narrative wayyiqtol chain, its most common defaults are
> future or gnomic-present; both are grammatically live here.
>
> **What the form does *not* support**: אֶהְיֶה is **qal**, not hiphil. A
> causative reading ("I cause to be," "I bring into being") is not available
> from this verb's own morphology — that would require a different stem than
> the text has. Any causative sense belongs only to a separate question about
> the *name* יהוה's own derivation (see below), not to a reading of this verb.

**אֲשֶׁר** · `אשר` · `HTr` — relative particle
> Indeclinable; one of the widest-range function words in the language.
> Range: *who · which · that · what · because · in that · where · when* —
> it marks a relation between clauses without specifying whether the linked
> content is a person, a quality, an action, a reason, or a place. Here it
> links two identical verb clauses; it does not by itself tell you whether the
> connection is definitional ("I am [the one] who I am"), causal ("I am
> because I am" — אֲשֶׁר can mean "because" elsewhere, e.g. Gen 30:18, Deut
> 3:24, though a causal sense sits awkwardly against two identical flanking
> clauses), or open/indefinite (see idem per idem, below).

**אֶהְיֶה** (repeated) — same form, same analysis as above.

### The idem per idem pattern

Hebrew has a recognized construction: a verb, repeated, with אֲשֶׁר (or a
similar particle) between the two occurrences — "X *ʾăšer* X." It recurs
elsewhere in the Torah and Former Prophets with a consistent function of
**deliberate non-specification** — "whatever/whoever/wherever it may be,"
refusing to name a determinate content:

- Exod 33:19 — וְחַנֹּתִי אֶת־אֲשֶׁר אָחֹן וְרִחַמְתִּי אֶת־אֲשֶׁר אֲרַחֵם, "I will show
  favor to whom I show favor, and I will have compassion on whom I have
  compassion" — same book, same speaker (YHWH to Moses).
- 1 Sam 23:13 — וַיִּתְהַלְּכוּ בַּאֲשֶׁר יִתְהַלָּכוּ, roughly "they went about
  wherever they could go."
- 2 Kgs 8:1 — גּוּרִי בַּאֲשֶׁר תָּגוּרִי, "sojourn wherever you can sojourn."

Applied here, this pattern licenses a further reading distinct from both the
ontological and the plain-future ones: **"I am/will be whatever I am/will
be"** — a self-determining formula that declines to hand over a content that
could be pinned down, invoked, or controlled. This is a grammatical fact about
how Hebrew uses this repetition pattern elsewhere, not an imported gloss.

### Every reading the grammar permits, together

Given the imperfect's aspectual range, היה's own semantic range, and the idem
per idem pattern, **אֶהְיֶה אֲשֶׁר אֶהְיֶה** is genuinely renderable as any of:

1. **"I am who I am"** — gnomic/durative present, a stated ongoing identity.
2. **"I will be who I will be"** — straightforward future, the imperfect's
   most common bare sense.
3. **"I am who I will be" / "I will be who I am"** — mixed readings; nothing
   requires the two identical verb forms to carry identical temporal force
   just because they're the same word.
4. **"I will become what I will become"** — leaning on היה's "become/happen"
   sense rather than static "be": an unfolding, not-yet-fixed identity, which
   fits a God about to act in a history that has not happened yet.
5. **"I am/will be whatever I am/will be"** — the idem per idem reading:
   deliberate non-specification, a refusal to be captured by a name in the
   way other ancient Near Eastern deity-names could be invoked.

**Not available**: a causative sense ("I cause being" / "I am the one who
brings things into being") for אֶהְיֶה itself — the verb is qal, not hiphil.

**כֹּה תֹאמַר לִבְנֵי יִשְׂרָאֵל אֶהְיֶה שְׁלָחַנִי אֲלֵיכֶם**
> **כֹּה**: adverb, *thus, so, in this way* — introduces direct-speech
> instructions, "thus you shall say."
> The clause repeats **אֶהְיֶה** alone, now functioning as what Moses is to
> report as the name/self-designation itself: **"I-am / I-will-be has sent me
> to you."** Whatever reading is chosen for the double form above should be
> chosen consistently here — the text uses the identical single word.

### Verse 14, whole

> **And God said to Moses, "I am who I am" / "I will be who I will be" /
> "I am/will be whatever I am/will be" [see above — the grammar supports all
> of these]. And he said, "Thus you shall say to the sons of Israel: 'I-am /
> I-will-be has sent me to you.'"**

### אֶהְיֶה and יהוה — what the text supports, and what is inference

The consonants of אֶהְיֶה are h-y-h (as spelled, אהיה: א is the 1cs imperfect
preformative, not a root letter). The divine name's consonants are י-ה-ו-ה.
היה (h-y-h) and הוה (h-w-h) are attested **biforms of the same verb** across
Biblical Hebrew and Aramaic — not homonyms, but the same root with a
y/w alternation the language shows elsewhere too. If יהוה is built on a
3rd-person prefix-conjugation of הוה, it would parse as roughly "he is /
he becomes / he causes to be," depending again on stem — the four consonants
alone don't disclose which stem (qal or hiphil) is meant, if any verbal
derivation is meant at all, since יהוה also simply functions in the text as a
proper name that need not be synchronically analyzed by its speakers as a
live verb form.

**What the text supports**: real consonantal/root kinship between אֶהְיֶה
(1cs, "I am/will be") and the shape of יהוה (which — if verbal — would be
3ms, "he is/will be"); direct narrative proximity (v.14 gives the אהיה
saying, v.15 gives the name יהוה, in the same conversation, unbroken).

**What is inference, not statement**: the text never uses an explicit
etymology formula for יהוה the way it does elsewhere for other names (e.g.
Gen 2:23's "she shall be called *woman* [אִשָּׁה] because she was taken out of
*man* [אִישׁ]"). Verse 14 does not say "and that is why my name is YHWH."
The reader is left to connect אֶהְיֶה and יהוה by the consonantal resemblance
and the narrative sequence; the text does not make the connection explicit
for us.

---

## Word by word — verse 15

**וַיֹּאמֶר עוֹד אֱלֹהִים אֶל־מֹשֶׁה** — "And God said further/again to Moses"
> **עוֹד**: adverb. Range: *again · still · yet · further · continuing.*
> Marks this as an additional statement, not a correction of v.14.

**כֹּה־תֹאמַר אֶל־בְּנֵי יִשְׂרָאֵל** — "Thus you shall say to the sons of Israel"

**יְהוָה** — the divine name, four consonants.
> Left untransliterated, per this project's standing practice (see
> `docs/RESEARCH-divine-name.md`, `translations/OUR-TRANSLATION.md` on Deut
> 32:9): the Masoretic vowel points on this word are borrowed from אֲדֹנָי as
> a qere perpetuum reading-instruction, not a record of the word's own sound.
> **"YHWH."**

**אֱלֹהֵי אֲבֹתֵיכֶם אֱלֹהֵי אַבְרָהָם אֱלֹהֵי יִצְחָק וֵאלֹהֵי יַעֲקֹב**
> "the God of your fathers, the God of Abraham, the God of Isaac, and the God
> of Jacob" — אֱלֹהֵי construct, repeated four times, naming the referent by
> covenant lineage rather than defining the name just given.

**שְׁלָחַנִי אֲלֵיכֶם** — "has sent me to you" (as v.13)

**זֶה־שְּׁמִי לְעֹלָם** · `זה`/`שמ/י`/`ל/עלם`
> **זֶה**: near demonstrative pronoun, "this."
> **שְׁמִי**: **שֵׁם**, "name" + 1cs suffix — "my name." שֵׁם is a designation, a
> label by which one is called or addressed.
> **לְעֹלָם**: preposition לְ + **עוֹלָם**. Range: *a long or indefinite duration
> · an age · the future so far as it can be reckoned · forever, everlasting.*
> עוֹלָם does not always denote strict metaphysical eternity in Biblical
> Hebrew — it is frequently bounded by context (e.g. a servant "forever" =
> for his lifetime). Here, with no bounding context supplied, the range runs
> from "for a very long/indefinite time" to "forever" — the text does not
> itself disambiguate which end of that range is meant.
> **"This is my name for the age" / "...forever" / "...for the indefinite
> future"** — the honest range, not a single pick.

**וְזֶה זִכְרִי לְדֹר דֹּר** · `ו/זה`/`זכר/י`/`ל/דר`/`דר`
> **זִכְרִי**: **זֵכֶר**, from root **זכר** (z-k-r), "to remember, mention,
> invoke, call to mind" + 1cs suffix. זֵכֶר is **not** the same word as שֵׁם:
> where שֵׁם is the label itself, זֵכֶר is the act or content of
> remembering/invoking/mentioning that label — closer to "what I am called
> and invoked as" than to "my designation." Range: *remembrance · memorial ·
> mention · invocation.*
> **לְדֹר דֹּר**: "to generation, generation" — two occurrences of **דּוֹר**
> ("generation, age, cycle of life") juxtaposed without a conjunction in the
> Masoretic text. This asyndetic doubling is a known Hebrew idiom for
> distributive repetition: "generation after generation," "every generation."

### The parallel — what it does

Two lines, same referent (יהוה), two different nouns:

> line 1: **this is my [שֵׁם / label] for the age / forever**
> line 2: **and this is my [זֵכֶר / what-I-am-invoked-as] for generation after
> generation**

Because שֵׁם and זֵכֶר are not synonyms, the parallel is not pure restatement.
It moves from the naming act itself (line 1: this is what I am *called*) to
the ongoing communal practice of invoking that name (line 2: this is how I am
*remembered and mentioned*, generation to generation). The doubling reinforces
durability across both lines while shifting the verb-idea from "being named"
to "being remembered/invoked" — permanence of the label, and permanence of
its use.

### Verse 15, whole

> **And God said further to Moses, "Thus you shall say to the sons of Israel:
> 'YHWH, the God of your fathers, the God of Abraham, the God of Isaac, and
> the God of Jacob, has sent me to you.' This is my name for the age (/
> forever / for the indefinite future), and this is what I am remembered and
> invoked as, generation after generation."**

---

## The Samaritan Pentateuch (MS Chester Beatty 751, 12th–13th c. CE — text tradition much older)

Recovered directly from `samaritan/sp/tf/` by mapping word nodes to verse
nodes through `oslots.tf` (the built-in `allwitness.py` reader returns nothing
for this passage due to the node-level bug noted above).

**v.13**: identical to the Masoretic consonants, apart from one purely
orthographic spelling (אבתיכם defective, vs. Masoretic אֲבוֹתֵיכֶם plene — same
word, no textual difference).

**v.14**: **consonantally identical to the Masoretic text** —
`אהיה אשר אהיה` reads the same in both traditions. No variant here; the
Samaritan Pentateuch gives no reason to prefer a different wording of the
crux phrase itself.

**v.15**: identical through `שלחני אליכם זה שמי לעולם`. One real difference at
the close: Masoretic **לְדֹר דֹּר** (asyndetic, "generation, generation") vs.
Samaritan **לדר ודר** (with a conjunction, "generation *and* generation"). A
small, genuine textual variant — same idiom, same sense ("every generation"),
differently conjoined.

---

## The Septuagint (Greek, translation c. 250–100 BCE)

**v.14**: `καὶ εἶπεν ὁ θεὸς πρὸς Μωυσῆν ἐγώ εἰμι ὁ ὤν καὶ εἶπεν οὕτως ἐρεῖς τοῖς
υἱοῖς Ισραηλ ὁ ὢν ἀπέσταλκέν με πρὸς ὑμᾶς`

> "And God said to Moses, 'ἐγώ εἰμι ὁ ὤν [I am the One Who Is / I am He Who
> Exists].' And he said, 'Thus you shall say to the sons of Israel: ὁ ὢν
> [The Being One / He Who Is] has sent me to you.'"

**What the Greek chose that the Hebrew does not force**:

1. **Tense/aspect**: ἐγώ εἰμι is a present-tense copula — a flat "I am,"
   collapsing the Hebrew imperfect's open range (future, habitual-present,
   modal) down to one option. The Hebrew verb form itself does not require
   present tense; Greek's grammar forced a choice the translator had to make.
2. **The relative clause becomes a substantive title**: ὁ ὤν is the articular
   present participle of εἰμί — grammatically a noun-phrase, "the one who
   is / the existing one," not a verb clause. Hebrew's אֲשֶׁר אֶהְיֶה is a
   full relative *clause* ("who/that I am/will be"); Greek turns the second
   half into a substantized epithet. This is a real structural shift, not
   just a translation of words — the Hebrew never nominalizes the phrase into
   a title the way ὁ ὤν does.
3. **The title stands in for the name a verse early**: in v.14b, where the
   Hebrew has Moses report אֶהְיֶה alone as the sender's self-designation, the
   Greek reports ὁ ὢν — the same substantized title, now functioning as a
   name-like referent in the messenger formula, one verse before the actual
   name יהוה/κύριος appears in v.15. The Hebrew keeps the "I-am" saying and
   the name יהוה as two separate disclosures across two verses; the Greek's
   ὁ ὢν already reads like a name by the end of v.14.
4. **Ontological commitment**: ὁ ὤν, "Being" as a substantive, sits inside a
   Greek philosophical vocabulary (existence, being-itself) that has no
   equivalent claim built into the Hebrew verb היה, whose core sense —
   documented above — runs through *becoming, happening, being present* at
   least as much as through static existence. The Hebrew leaves open whether
   this is a claim about timeless being, future action, or a refusal to be
   named (the idem per idem reading); the Greek picks the ontological end of
   that range and states it as a philosophical proposition.
5. **v.15**: the Greek renders יהוה as **κύριος** ("Lord") in running prose —
   the LXX's standard practice for the name throughout, and, per this
   project's own research (`docs/RESEARCH-divine-name.md` §4e), the oldest
   attested "replacement" of the Tetragrammaton in the whole transmission
   history, older than Philo, older than any Masoretic vowel-pointing.

---

## Summary

The Hebrew of v.14 gives one verb (אֶהְיֶה, qal imperfect 1cs of היה),
repeated, joined by the widest-range relative particle in the language
(אֲשֶׁר). Biblical Hebrew's imperfect does not fix a tense, and this exact
repeated-verb-with-אֲשֶׁר pattern elsewhere in the Torah (Exod 33:19) marks
deliberate non-specification. That gives, honestly, at least five distinct
readings with real grammatical grounds — "I am who I am," "I will be who I
will be," two mixed-tense readings, and "I am/will be whatever I am/will
be" — with a causative sense explicitly *not* supported by the verb's own
(qal, not hiphil) form. The connection to יהוה rests on a real consonantal
kinship (h-y-h / h-w-h as attested biforms) and narrative proximity, but the
text never states the etymology the way it does for other names elsewhere in
Genesis — that link is the reader's inference, not the text's claim. The
Septuagint's ἐγώ εἰμι ὁ ὤν makes a specific ontological choice — present
tense, a substantized "Being" as title — that the Hebrew's aspectual verb and
open relative particle do not themselves require.

---

*Analytical data: `hebrew-ot/morphhb` (CC BY), `samaritan/sp` (CC BY-NC),
`septuagint/LXX-Rahlfs-1935`. Dead Sea Scrolls checked and confirmed absent
for this passage (`dead-sea-scrolls/etcbc-dss`). Regenerate with
`./tools/analyze.py Exod 3 13 --range 15` and `./tools/allwitness.py Exod 3
14`. The Samaritan reading required a direct oslots walk (see top of file);
the English throughout is this project's own.*
