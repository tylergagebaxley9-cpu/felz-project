# Revelation 3:2–12

*Greek. The end of the letter to Sardis and the whole of the letter to
Philadelphia — two letters, not one, and the seam falls inside this range.*

Translated from the Greek directly. No English translation was consulted or
adapted.

---

## What this is built from, and what it is not

**Used — grammatical analysis and manuscripts, not anyone's English:**

- `greek-nt/morphgnt/87-Re-morphgnt.txt` — the SBLGNT text (**EDITED**, Holmes
  2010: a modern eclectic reconstruction; **no single manuscript reads exactly
  this way**) with per-word morphological tagging. Reference format `BBCCVV`,
  Revelation = book `27` in MorphGNT's internal numbering.
- `greek-nt/SBLGNT/data/sblgntapp/text/Rev.txt` — the editor's own apparatus,
  used only to see *where* he knew there was a decision, never as the authority
  on what the manuscripts say.
- **The actual manuscripts**, read from disk with `tools/cntr_read.py` against
  Rev 3:2–12:
  - **01 Sinaiticus** (c. 330–360 CE) — extant, complete for this passage
  - **02 Alexandrinus** (c. 400–440 CE) — extant, complete
  - **04 Ephraemi Rescriptus** (5th c. CE) — extant, complete
  - **P115** — **enters at v. 10 and not before.** Partial in v. 10 (begins
    mid-verse at πειράσαι), complete in v. 11, breaks off inside v. 12 after
    ἐξέλθῃ ἔτι.
- The printed **RP** (Robinson–Pierpont Byzantine) and **KJTR** (the Textus
  Receptus underlying the KJV), from
  `papyri/cntr-transcriptions/critical texts/` — read to locate where the
  *printed* traditions diverge, never as authorities on the manuscripts.
- My own knowledge of Koine Greek for lexical range.

**Extant but silent here — stated so the absence is not read as agreement:**

- **03 Vaticanus** contains **no Revelation at all** (0 lines for book 66 in the
  transcription; the codex breaks off in Hebrews).
- **05 Bezae** likewise contains **no Revelation**.
- **P47**, the great Revelation papyrus (3rd c.), begins at **Rev 9:10** and
  runs to 17:2 — it does not reach this passage.
- **0169** begins at **Rev 3:19**.

So for **vv. 2–9** the oldest ink available anywhere on this disk is
**Sinaiticus, c. 330–360 CE** — roughly 250 years after composition, and there
is nothing older to check it against.

> [!note] The witness base changes mid-passage
> At **v. 10 the floor drops by roughly a century**: P115 begins exactly there.
> It is conventionally dated to the **3rd century**, which would make it the
> oldest ink on this disk for vv. 10–12 — but **that date is not carried in the
> CNTR files themselves**. It is external knowledge, stated as such, and not
> verifiable from anything in this repo. What *is* verifiable here is that P115
> exists for these three verses and for none of the seven before them.
>
> So "the manuscripts" in this file means **three** witnesses in vv. 2–9 and
> **four** in vv. 10–12. The arithmetic of agreement is not the same on both
> sides of that line.

**Not used**: KJV, any modern English version, any interlinear's English column,
`tools/gloss.py`, or any lexicon's gloss list. The semantic ranges below are
stated from how each root behaves in Greek.

> [!warning] Where the printed text is not the manuscripts
> The SBLGNT running text carries raised editorial marks (⸀ for a chosen word,
> ⸂ ⸃ around a chosen phrase). In this range they fall at vv. 2, 3, 4, 5, 7 and
> 9. **Three of them turn out to hide manuscript disagreement the apparatus does
> not report** — see §Variants. The apparatus lists what the *printed editions*
> (WH, Treg, NA28, RP) do; it is not a list of what the *manuscripts* do.

---

# The passage whole

Given first so the argument is visible, then defended word by word. Where a word
carries more than one live meaning the alternatives are stacked in
`(a | b | c)` and **none is preferred**.

**3:2** — Become one who is (staying awake | on watch | roused from sleep), and
make firm (set fast | prop up | steady) the remaining things, which were about
to die; for I have not found your works (deeds | workings) (filled up | made
complete | fulfilled) in the sight of my God.

**3:3** — Keep remembering, then, how you have received and heard, and (keep |
guard | observe) it, and change your mind (turn your thinking around). If, then,
you do not stay awake, I will come as a thief, and you will certainly not know
what sort of hour I will come upon you.

**3:4** — But you have a few names (a few persons) in Sardis which did not stain
(defile | soil) their garments, and they will walk with me in white (bright |
shining) things, because they are worthy (of matching weight).

**3:5** — The one (conquering | prevailing | winning the case) will in this way
be wrapped about in white garments, and I will certainly not wipe away (blot
out | smear off) his name out of the scroll (book) of life, and I will
(acknowledge | say the same thing about | agree over) his name in the sight of
my Father and in the sight of his (messengers | angels).

**3:6** — The one having an ear, let him hear what the (Spirit | Breath | Wind)
is saying to the (assemblies | called-out gatherings | congregations).

**3:7** — And to the (messenger | angel) of the assembly in Philadelphia write:
These things says the (holy one | set-apart one), the (true | real | genuine)
one, the one having the key of David, the one opening and no one will shut, and
shutting and no one opens —

**3:8** — I know your works. Look — I have given, in your sight, a door standing
opened, which no one is able to shut — because you have small (little | slight)
power (ability | capacity), and you kept my word, and you did not deny (disown |
refuse) my name.

**3:9** — Look, I give (some) out of the synagogue (gathering-together) of the
Adversary — of those saying themselves to be (Judeans | Jews) **and they are
not**, but they are lying — look, I will make them so that they will come and
bow down (prostrate themselves) in the sight of your feet, and they will know
that I loved you.

**3:10** — Because (that | since) you kept (guarded | observed) the word of my
(remaining-under | endurance | patient waiting), I also will keep (guard) you
**out of** the hour of the (testing | trial | temptation) which is about to come
upon the whole (inhabited world | settled earth | empire), to (test | try |
tempt) those dwelling upon the (earth | land).

**3:11** — I am coming (quickly | soon | suddenly). Keep gripping (hold fast to)
what you have, so that no one takes your (wreath | garland | victor's crown).

**3:12** — The one (conquering | prevailing) — I will make him a pillar
(column) in the (sanctuary | inner shrine) of my God, and he will certainly not
go outside any longer; and I will write upon him the name of my God, and the
name of the city of my God — the new Jerusalem, the one coming down out of the
(sky | heaven) from my God — and my new name.

---

# Verse by verse

### v. 2 — γίνου γρηγορῶν, καὶ στήρισον τὰ λοιπὰ ἃ ἔμελλον ἀποθανεῖν, οὐ γὰρ εὕρηκά σου τὰ ἔργα πεπληρωμένα ἐνώπιον τοῦ θεοῦ μου

**γίνου** · verb, γίνομαι, present middle imperative, 2nd sing.
> Range: *come to be · become · be born · happen · prove to be · come to pass.*
> Not εἰμί. The imperative is **present** (durative: keep on becoming), and the
> command is not "be watchful" but "**become** one who is watching" — the verb
> of coming-into-a-state, addressed to someone not currently in it.

**γρηγορῶν** · verb, γρηγορέω, present active participle, nom. sing. masc.
> A back-formation from ἐγρήγορα, the perfect of ἐγείρω ("rouse, raise"). Its
> root sense is therefore *to be in the state of having been woken*. Range:
> *stay awake · keep watch · be alert · be roused.* Together with γίνου this is
> a **periphrastic** construction — "become watching" — which stresses ongoing
> state, not a single act. The metaphor is literally sleep.

**στήρισον** · verb, στηρίζω, aorist active imperative, 2nd sing.
> Range: *fix firmly · set fast · prop · support · make stable · buttress.*
> Physical before it is figurative — the word used of planting something so it
> will not fall over. Aorist: a decisive act, contrasted with the durative
> γίνου γρηγορῶν beside it.

**τὰ λοιπὰ** · article + adjective λοιπός, acc. pl. **neuter**
> *the remaining · the rest · what is left over.* Neuter, so grammatically "the
> remaining things" — **not** "the remaining people," which would be masculine
> τοὺς λοιπούς. Whether the neuter is meant impersonally (the surviving works,
> the remnant of what is there) or is a neuter-for-persons idiom is not settled
> by the grammar. Both readings are available; the Greek does not choose.

**ἃ ἔμελλον ἀποθανεῖν** · relative pron. + μέλλω imperfect act. indic. 3rd
**pl.** + ἀποθνῄσκω aorist act. infinitive
> μέλλω range: *be about to · be on the point of · intend · be destined to.*
> ἀποθνῄσκω: *die · be dying.* Literally "**which were about to die**" — a past
> tense looking forward from a past vantage point. Note the plural verb with the
> neuter plural subject: classical Greek would take a singular (ἔμελλεν), and
> Revelation's Greek does not. This is a real, repeated feature of this book's
> style, not a copyist's error.
>
> ⚠️ **Variant**: SBLGNT marks this whole unit ⸂…⸃. The Byzantine tradition (RP)
> reads **ἔμελλες ἀποβάλλειν** — 2nd singular, "which **you** were about to
> **throw away**." That is a different sentence: the things are not dying of
> themselves, the addressee is discarding them. All three manuscripts on disk
> (01, 02, 04) read **ἔμελλον ἀποθανεῖν**.

**οὐ γὰρ εὕρηκά** · negative + γάρ + εὑρίσκω perfect active indicative 1st sing.
> Perfect: *I have found and the finding stands.* Range of εὑρίσκω: *find ·
> discover · come upon · obtain.*

**σου τὰ ἔργα** · pronoun gen. + article + ἔργον acc. pl. neut.
> ἔργον range: *work · deed · act · task · labour · thing accomplished.*
>
> ⚠️ **Variant** (⸀ in SBLGNT): the article **τὰ** is present in Treg/NA28/RP and
> **absent** in WH. From disk: **Sinaiticus has τὰ; Alexandrinus and Ephraemi
> both read σου ἔργα without it.** Without the article the sense drifts toward
> "any works of yours" rather than "your works" as a known quantity. Small, and
> real.

**πεπληρωμένα** · πληρόω, perfect passive participle, acc. pl. neut.
> Range: *fill up · make full · complete · bring to fullness · fulfil · carry
> out fully.* The image underneath is a vessel or a measure being filled to its
> capacity. The perfect passive means the works stand in a completed state — and
> the sentence says they do **not**. Whether "unfinished" here is quantitative
> (not enough of them) or qualitative (not carried through) the participle does
> not say.

**ἐνώπιον τοῦ θεοῦ μου** · preposition + θεός gen. sing.
> ἐνώπιον is built from ἐν + ὤψ ("eye/face") — *in the face of · in the sight
> of · before.* "In the presence of" flattens the ocular metaphor that is
> actually in the word. Note **μου** — "my God," spoken by the one dictating
> the letter.

---

### v. 3 — μνημόνευε οὖν πῶς εἴληφας καὶ ἤκουσας καὶ τήρει, καὶ μετανόησον

**μνημόνευε** · μνημονεύω, present active imperative, 2nd sing.
> Range: *remember · be mindful of · hold in memory · make mention of · call to
> mind.* Present imperative — a standing instruction, not a single recollection.

**εἴληφας** · λαμβάνω, perfect active indicative, 2nd sing.
> Range: *take · receive · get · grasp · seize · accept.* Perfect: you took, and
> you still hold it. Paired with **ἤκουσας** (aorist, ἀκούω, *hear · listen ·
> heed · understand*) — the tense pairing is deliberate: the receiving abides,
> the hearing was an event.

**τήρει** · τηρέω, present active imperative, 2nd sing.
> Range: *keep · guard · watch over · preserve · observe (a command).* The word
> for keeping a prisoner as much as for keeping a rule.

**μετανόησον** · μετανοέω, aorist active imperative, 2nd sing.
> μετά ("after, change of") + νοέω ("perceive, think, apprehend with the
> mind"). Range: *change one's mind · think differently afterwards · reconsider
> · turn one's perception around.* The Greek word is cognitive, not emotional —
> there is no sorrow, penalty or penance in the root. Rendering it "repent"
> imports a devotional register through Latin *paenitentia* that the Greek
> compound does not carry on its own. Both are offered above.

### …ἐὰν οὖν μὴ γρηγορήσῃς, ἥξω ὡς κλέπτης

**γρηγορήσῃς** · aorist active subjunctive, 2nd sing., after ἐάν μή — the
ordinary conditional construction.

> 🛑 **A variant the SBLGNT apparatus does not report.** Sinaiticus does not read
> γρηγορήσῃς here at all. It reads **ἐὰν οὖν μὴ μετανοήσῃς** — "if, then, you do
> not **change your mind**." 02 and 04 read γρηγορήσῃς. So the oldest complete
> witness on disk makes the condition *repentance*, and the other two make it
> *wakefulness*. The apparatus lists neither. Found only by reading the
> manuscripts.
>
> Sinaiticus's reading is the easier one to explain as secondary — μετανόησον
> stands three words earlier and a scribe's eye can carry it forward — but
> "easier to explain" is an argument, not evidence, and it is recorded here as
> an argument.

**ἥξω** · ἥκω, future active indicative, 1st sing.
> Range: *have come · be present · arrive · come.* ἥκω is unusual: its present
> already means "I am here, having arrived," so the future is *I will be
> arrived*. Distinct from ἔρχομαι, which is motion.

**κλέπτης** · noun, nom. sing. masc. — *thief · stealer.* From κλέπτω, to
steal — the comparison is to the unannounced arrival, not to the taking.

**οὐ μὴ … γνῷς** · double negative + γινώσκω aorist active subjunctive, 2nd sing.
> οὐ μή + aorist subjunctive is the **emphatic** future denial in Greek — "you
> will absolutely not know," stronger than a plain future negative. γινώσκω
> range: *know · come to know · recognise · perceive · learn.*

**ποίαν ὥραν** · interrogative ποῖος + ὥρα, acc. sing. fem.
> ποῖος asks *of what kind*, not *which one of a list* (that is τίς). So: "what
> **sort of** hour" — the quality of the moment, not its number on a clock. ὥρα
> range: *hour · season · time · the right moment · a period of the day.*

> ⚠️ **Variants**: RP adds **ἐπί σε** after the first ἥξω ("I will come **upon
> you** as a thief") — and **Sinaiticus has it**, so the Byzantine reading is
> not late invention here. Treg reads γνώσῃ (future indicative) for γνῷς
> (subjunctive); **Sinaiticus again supports it** — 01 reads *ου μη γνωση οιαν
> ωραν*, with οἵαν ("of what kind") for ποίαν as well.

---

### v. 4 — ἀλλὰ ἔχεις ὀλίγα ὀνόματα ἐν Σάρδεσιν ἃ οὐκ ἐμόλυναν τὰ ἱμάτια αὐτῶν

**ὀλίγα ὀνόματα** · adjective + ὄνομα, acc. pl. neut.
> ὄνομα is *name*, plainly. Used here of **persons counted by name** — a way of
> counting individuals that is ordinary in Greek administrative and census
> language, so "a few names" and "a few persons" are the same statement. Both
> are given above because the metaphor is live in the passage: names are what
> vv. 5 and 8 go on to be about.

**ἐμόλυναν** · μολύνω, aorist active indicative, 3rd pl.
> Range: *stain · soil · smear · defile · make dirty.* Physical first — the
> word for getting mud on something. Whether the defilement in view is ritual,
> moral or something else is not in the verb.

**ἱμάτια** · ἱμάτιον, acc. pl. neut. — the **outer** garment, the cloak thrown
over the χιτών. Range: *garment · cloak · outer robe · (plural) clothes.*

**περιπατήσουσιν** · περιπατέω, future active indicative, 3rd pl.
> περί ("around") + πατέω ("tread"). Range: *walk about · go around · (of
> conduct) live, conduct oneself.* Both senses are alive; a future with μετʼ
> ἐμοῦ ("with me") pulls toward the literal.

**ἐν λευκοῖς** · adjective, dat. pl. neut., with no noun
> λευκός range: *white · bright · shining · radiant.* Greek λευκός covers
> brightness as much as colour — it is used of sunlight and of polished metal.
> The noun is left out; the Greek is literally "in white [things]."

**ἄξιοι** · adjective, nom. pl. masc.
> From ἄγω in the sense of *weighing* — the root idea is **counterbalancing**,
> a thing that draws the scale down as much as what it is set against. Range:
> *worthy · deserving · of equal weight · comparable · fit.* Note the shift
> from neuter (ὀνόματα … ἃ) to **masculine** ἄξιοι: the sentence starts counting
> names and ends describing men.

> ⚠️ **Variants**: RP reads ὀλίγα ἔχεις (word order). 04 reads ἑαυτῶν
> ("their own") for αὐτῶν. **02 reads περιπατη σου**, splitting περιπατήσουσιν
> into two words — a scribal slip, not a variant reading, and recorded as such.

---

### v. 5 — ὁ νικῶν οὕτως περιβαλεῖται ἐν ἱματίοις λευκοῖς

**ὁ νικῶν** · νικάω, present active participle, nom. sing. masc., articular
> Range: *conquer · be victorious · prevail · overcome · win (a contest, a
> battle, **a lawsuit**).* The forensic sense is standard Greek and is worth
> keeping visible, because vv. 5 and 9 are both about testimony given before a
> court-like assembly (before the Father, before the messengers). Present
> participle: *the one who is conquering*, ongoing, not *the one who conquered*.

**οὕτως** · adverb — *thus · in this way · so.*
> ⚠️ **Variant**: RP reads **οὗτος**, the demonstrative pronoun — "**this one**
> will be wrapped," not "**thus** he will be wrapped." In uncial script with no
> accents, ΟΥΤΩΣ and ΟΥΤΟΣ differ by a single letter. All three manuscripts on
> disk read οὕτως.

**περιβαλεῖται** · περιβάλλω, future **middle** indicative, 3rd sing.
> περί + βάλλω, *throw around*. Middle voice: *he will throw [it] around
> himself* — he clothes himself, rather than being clothed by another. Range:
> *put around · clothe · wrap · surround (also of a siege wall).*
> ⚠️ 04 reads **περιβάλλεται**, present rather than future; 02 reads
> περιβαλεῖτε (itacism for -ται). The future is what 01 supports.

**οὐ μὴ ἐξαλείψω** · emphatic denial + ἐξαλείφω, future active indicative
> ἐκ + ἀλείφω ("smear, anoint"). Root image: **smearing a written surface until
> the writing is gone** — wiping a wax tablet, washing ink off papyrus. Range:
> *wipe out · blot out · erase · obliterate · annul.* The metaphor is
> specifically documentary, which matters given what follows.

**ἐκ τῆς βίβλου τῆς ζωῆς** · βίβλος, gen. sing. fem.
> βίβλος is the papyrus plant, then the writing material, then the written
> roll. Range: *scroll · book · written record · register.* "Register" is worth
> holding in view: the sentence is about a **name being kept on or struck off a
> list**, which is what civic citizen-rolls were for.

**ὁμολογήσω** · ὁμολογέω, future active indicative, 1st sing.
> ὁμοῦ ("same") + λέγω ("say") — literally *to say the same thing as*. Range:
> *agree · concede · admit · acknowledge publicly · declare openly · confess.*
> The core is **concurrence**, not disclosure of a secret: to ὁμολογέω a name
> is to say the same about it as someone else does — here, before the Father
> and the messengers.

**ἐνώπιον τοῦ πατρός μου καὶ ἐνώπιον τῶν ἀγγέλων αὐτοῦ**
> ⚠️ **Sinaiticus reads ἔμπροσθεν** for the first ἐνώπιον — *in front of, before*
> (spatial position) rather than *in the face of* (line of sight). 02 and 04
> read ἐνώπιον twice, as printed.

**ἀγγέλων** · ἄγγελος, gen. pl. masc.
> Range: *messenger · envoy · one sent with a message · (in Jewish and Christian
> Greek) angel.* The word is ordinary Greek for a human courier and carries no
> supernatural marking in itself. The same word is used in v. 7 for whoever the
> letter is addressed to.

---

### v. 6 — ὁ ἔχων οὖς ἀκουσάτω τί τὸ πνεῦμα λέγει ταῖς ἐκκλησίαις

**οὖς** · noun, acc. sing. neut. — *ear.* **Singular**, not "ears."

**ἀκουσάτω** · ἀκούω, aorist active imperative, **3rd** sing.
> A third-person imperative, which English has no direct form for: not "listen!"
> addressed to the hearer but "let him hear" / "he is to hear," a command issued
> about a third party.

**τὸ πνεῦμα** · noun, nom. sing. neut.
> From πνέω, *to blow · to breathe*. Range: *wind · breath · breathing · life-
> breath · spirit.* Greek does not separate these into different words, and the
> capital letter that marks it as a title in English does not exist in the
> manuscripts, which are written in unaccented majuscule throughout. **All three
> witnesses write it as a nomen sacrum** (contracted, overlined — `=πνα` in the
> transcription convention), which shows the scribes read it as the divine
> referent. That is evidence about 4th–5th century reading, not about the
> author's Greek.

**ταῖς ἐκκλησίαις** · ἐκκλησία, dat. pl. fem.
> ἐκ ("out") + καλέω ("call") — the **called-out** body. In ordinary Greek civic
> usage, the assembly of citizens summoned to deliberate and vote. Range:
> *assembly · called-out gathering · congregation · (later) church.* Rendering
> it "church" imports a building and an institution that the word does not
> contain; "assembly" keeps the civic sense that a Greek reader had.

---

### v. 7 — Καὶ τῷ ἀγγέλῳ τῆς ἐν Φιλαδελφείᾳ ἐκκλησίας γράψον

**Τάδε λέγει** · ὅδε, acc. pl. neut. + λέγω, present active indicative
> ὅδε is the *near* demonstrative — "these things here, which follow." τάδε
> λέγει is the standing formula that opens each of the seven letters, and it is
> also the formula the Septuagint uses to render Hebrew כֹּה אָמַר יְהוָה, "thus
> said YHWH," at the head of a prophetic oracle. The formula is doing
> attribution work.

**ὁ ἅγιος** · adjective, nom. sing. masc., articular
> Range: *set apart · dedicated · consecrated · holy.* The core is separation
> from common use, not moral purity — which is a later specialization.

**ὁ ἀληθινός** · adjective, nom. sing. masc.
> Distinct from ἀληθής. **ἀληθής** = *truthful, not lying* (of statements and
> speakers). **ἀληθινός** = *real, genuine, the actual thing as opposed to a
> copy or a counterfeit* (of things). Range: *true · real · genuine · authentic
> · true-to-type.* The choice of -ινος here means *the real one*, not *the one
> who tells the truth* — and it is the same distinction that makes v. 9's
> ψεύδονται land.

> 🛑 **Word order, unreported in the apparatus.** SBLGNT prints **ὁ ἅγιος, ὁ
> ἀληθινός**. But **Sinaiticus and Alexandrinus both read ὁ ἀληθινός ὁ ἅγιος —
> reversed.** Only Ephraemi (04) has the printed order. Two of the three oldest
> witnesses on disk agree against the printed text, and the SBLGNT apparatus
> does not record it. Nothing hangs on the order; it is logged because the
> printed text presents itself as settled here and it is not.

**τὴν κλεῖν Δαυίδ** · κλείς, acc. sing. fem.
> *key · bolt · bar* — the thing that works a door, and by extension the
> authority over it. The phrase is a direct pull from Isaiah 22:22 (the key of
> the house of David laid on Eliakim's shoulder: he opens and none shuts, he
> shuts and none opens). The allusion is verbal and structural, not just
> thematic.
> ⚠️ **Variant**: RP reads **τοῦ Δαυίδ** with the article, and **Sinaiticus has
> it** (`κλιν του δαδ`). 02 and 04 read the anarthrous Δαυίδ. All three write
> Δαυίδ as a nomen sacrum (`=δαδ`).

**ὁ ἀνοίγων … καὶ κλείων** · ἀνοίγω / κλείω, present active participles
> ἀνοίγω: *open · unlock · unbar.* κλείω: *shut · close · lock · bar.*

**οὐδεὶς κλείσει … οὐδεὶς ἀνοίγει** — future, then **present**.
> The asymmetry is in the printed text: "no one **will shut** … no one
> **opens**." Whether that is deliberate or a transmission artefact is exactly
> what the variants make unclear:
>
> ⚠️ **Three-way disagreement, all in one clause.**
> - **SBLGNT/WH/Treg/NA28**: …καὶ οὐδεὶς κλείσει, καὶ κλείων καὶ οὐδεὶς ἀνοίγει.
> - **RP**: …καὶ οὐδεὶς κλείσει **αὐτήν, εἰ μὴ ὁ ἀνοίγων** — "and no one will
>   shut **it, except the one who opens**," and ends **ἀνοίξει** (future).
> - **Sinaiticus** on disk: `και ανυγων και ουδισ κλισει και κλειων και ουδισ
>   **ανυξει**` — the printed clause structure but the **future ἀνοίξει**, i.e.
>   the RP verb form inside the WH sentence.
> - **04**: `ο ανυγων και ουδεισ κλισει και κλιει και **ουδε εις** ανοιγει` —
>   present ἀνοίγει, and οὐδεὶς written as two words, **οὐδὲ εἷς**, "not even
>   one" (an emphatic spelling this scribe uses again in v. 8).
>
> No two of the three manuscripts agree with each other completely in this
> clause. The printed text is a reconstruction here in the full sense.

---

### v. 8 — Οἶδά σου τὰ ἔργα — ἰδοὺ δέδωκα ἐνώπιόν σου θύραν ἠνεῳγμένην

**Οἶδά** · οἶδα, perfect active indicative, 1st sing., **present in meaning**
> οἶδα is the perfect of an obsolete verb meaning *to see* — literally *I have
> seen*, therefore *I know*. Range: *know · be aware of · understand ·
> recognise.* It is knowledge from having perceived, as against γινώσκω's
> knowledge from coming-to-learn.
> ⚠️ 01 reads οἶδα **τὰ ἔργα σου** (different word order); 02 and 04 read οἶδά
> σου τὰ ἔργα as printed.

**ἰδοὺ** · particle (frozen aorist middle imperative of εἶδον)
> *look · see · behold · here now.* Functionally an attention-marker; it does
> not inflect for the person addressed.

**δέδωκα** · δίδωμι, perfect active indicative, 1st sing.
> *I have given, and the giving stands.* Range of δίδωμι: *give · grant · hand
> over · put · place · appoint.*

**θύραν ἠνεῳγμένην** · θύρα acc. sing. fem. + ἀνοίγω perfect passive participle
> θύρα: *door · doorway · gate · entrance.* The **perfect passive** participle
> is the whole force of the image: not "an open door" as a description, but a
> door **that has been opened and stands opened** — a completed act by someone,
> with a state persisting.
> ⚠️ The augment/reduplication of this perfect is unstable across the
> witnesses — 01 **ἠνεῳγμένην**, 02 and 04 **ἀνεῳγμένην**. This is a spelling
> difference in a notoriously irregular verb, not a difference of meaning, and
> is logged only so it is not later mistaken for one.

**οὐδεὶς δύναται κλεῖσαι** · οὐδείς + δύναμαι pres. mid. indic. + κλείω aor. inf.
> δύναμαι: *be able · be capable · have power to.*
> ⚠️ 02 and 04 add **αὐτήν** ("to shut **it**"); **Sinaiticus omits it**, as the
> printed text does. 04 again writes **οὐδὲ εἷς**, "not even one."

**μικρὰν ἔχεις δύναμιν** · μικρός acc. sing. fem. + ἔχω + δύναμις acc. sing. fem.
> μικρός: *small · little · slight · insignificant.* δύναμις, from δύναμαι
> immediately above (the two words are set beside each other on purpose):
> *power · ability · capacity · strength · capability to act · (of armies)
> force · (of events) a mighty work.* The clause is introduced by **ὅτι**,
> which can be *because* or *that*. As *because*, the small power is the ground
> of the open door. The Greek permits it and the syntax does not force it.

**ἐτήρησάς μου τὸν λόγον** · τηρέω aorist, 2nd sing.
> Same verb as v. 3's τήρει. λόγος range: *word · utterance · statement ·
> account · message · reason · matter.* ⚠️ 04 reads **τηρήσας** (participle,
> dropping the augment) — a slip that makes the clause ungrammatical as it
> stands.

**οὐκ ἠρνήσω** · ἀρνέομαι, aorist **middle** indicative, 2nd sing.
> Range: *deny · disown · refuse · decline · say no to · renounce.* Middle-only
> verb (no active form exists). The object is **τὸ ὄνομά μου**, "my name" —
> so what was not disowned is the name, tying back to v. 5's name kept on the
> register and forward to v. 9.

---

### v. 9 — ἰδοὺ διδῶ ἐκ τῆς συναγωγῆς τοῦ Σατανᾶ

**διδῶ** · δίδωμι — MorphGNT tags this **present active subjunctive, 1st sing.**
> 🛑 **This form is a genuine problem and it should be stated as one.** A bare
> subjunctive with no ἵνα, ἐάν or ὅταν governing it, in a main clause introduced
> by ἰδού, is not normal Greek. Three things are true at once and the passage
> does not choose between them:
> 1. It may be an **itacistic spelling** of a contracted present indicative —
>    Revelation's Greek does this elsewhere — in which case it simply means
>    "I give."
> 2. It may be a real **hortatory/deliberative subjunctive**, "let me give."
> 3. It may be what the Byzantine tradition thought it was: **RP reads δίδωμι**,
>    the plain present indicative, smoothing the form away.
>
> ⚠️ **And the manuscripts split three ways.** 02 and 04 read **διδῶ** as
> printed. **Sinaiticus reads δέδωκα** — the *perfect*, "I **have given**" —
> which is the identical verb form standing in v. 8 (δέδωκα). The SBLGNT
> apparatus records only διδῶ vs δίδωμι and does not mention Sinaiticus's
> perfect at all.
>
> Which way the change ran is arguable in both directions: a scribe may have
> harmonised v. 9 to v. 8, or may have found δέδωκα awkward and reached for a
> present. Recorded, not decided.

**ἐκ τῆς συναγωγῆς** · preposition ἐκ + συναγωγή, gen. sing. fem.
> **The sentence has no direct object.** δίδωμι governs ἐκ + genitive with
> nothing to give — a **partitive** construction: "I give [some] **out of** the
> gathering." What is being given is left unstated in the Greek; every English
> rendering that supplies "some of them" is supplying a word that is not there.
> The bracketed "(some)" above marks the gap rather than filling it silently.
>
> συναγωγή: σύν ("together") + ἄγω ("bring, lead") — a **bringing-together**.
> Range: *a gathering · an assembly · the act of collecting · the assembled
> body · (as a building) the meeting-house.* Ordinary Greek uses it of any
> collection, including of crops and of money. It is the same kind of word as
> ἐκκλησία in v. 6, formed from a different verb.

**τοῦ Σατανᾶ** · noun, gen. sing. masc.
> Not a Greek word. A **transliteration** of Hebrew שָׂטָן *śāṭān*, which is a
> common noun meaning *adversary · opponent · accuser · one who obstructs* — and
> which is used in the Hebrew Bible of ordinary human opponents as well as of
> the figure in Job 1 and Zechariah 3 (see `translations/job-1-and-zechariah-3.md`).
> By the time it is transliterated into Greek with an article it is functioning
> as a title. Both are given above.

**τῶν λεγόντων ἑαυτοὺς Ἰουδαίους εἶναι**
> λέγω present participle gen. pl. + ἑαυτοῦ acc. pl. (reflexive) + Ἰουδαῖος
> acc. pl. + εἰμί present infinitive. An accusative-and-infinitive construction:
> "those saying **themselves** to be Ἰουδαίους." The reflexive is emphatic: the
> claim is self-made.
>
> **Ἰουδαῖος** range: the adjective is formed from Ἰούδα / יְהוּדָה — Judah. It
> covers *of the tribe of Judah · of the territory of Judea · a Judean by
> descent or residence · an adherent of the ancestral customs of Judea.* Greek
> writers of this period use it across that whole span and the language does not
> mark which is meant. The two English options — "Judean" (place and people) and
> "Jew" (people and practice) — divide a range the Greek keeps whole, so both
> are printed and **neither is preferred**.

**καὶ οὐκ εἰσίν** · negative + εἰμί, present indicative, 3rd pl.
> "**and they are not.**" Three words, and the hinge of the sentence. It negates
> the **claim to the title**, and nothing else is said about who they are or
> what they should be called instead.
>
> Corroborating what `HIGHLIGHTS.md` already records for Rev 2:9 and 3:9:
> **there is no idol vocabulary anywhere in this verse** — no εἴδωλον,
> εἰδωλολατρία, or any cognate, though Revelation uses that vocabulary five
> times elsewhere. And here **the manuscripts do not disagree**: 01, 02 and 04
> all read καὶ οὐκ εἰσίν, identically. The text is stable; what drifted is
> paraphrase downstream of it.

**ἀλλὰ ψεύδονται** · ψεύδομαι, present middle indicative, 3rd pl.
> *lie · speak falsely · deceive · be false.* Middle-only. The present tense is
> durative: an ongoing false claim, not one utterance.

**ποιήσω αὐτοὺς ἵνα ἥξουσιν καὶ προσκυνήσουσιν**
> ποιέω future active indicative + ἵνα + **two future indicatives**.
> 🛑 **ἵνα normally requires the subjunctive.** ἵνα + future indicative is a
> solecism by classical standards and a recognised, repeated feature of
> Revelation's Greek. **RP corrects it** to ἥξωσιν / προσκυνήσωσιν
> (subjunctives). All three manuscripts on disk read the **future indicatives**,
> uncorrected — so the harder, ungrammatical reading is the attested one.
>
> ποιέω range: *make · do · cause · bring about · appoint.* With ἵνα here it is
> causative: *I will make them so that…*
>
> ἥκω again (as in v. 3, of the thief) — *arrive · be present.*
>
> **προσκυνήσουσιν** · προσκυνέω: πρός ("toward") + κυνέω ("kiss"). The literal
> act is **kissing toward** — the Persian and Greek gesture of homage, which
> involved prostration. Range: *do obeisance · prostrate oneself · bow down ·
> pay homage · worship.* Greek uses it for homage to a human king as readily as
> to a god; the word itself does not distinguish the two.

**ἐνώπιον τῶν ποδῶν σου** — literally *in the sight of your feet*, the same
ocular preposition as vv. 2 and 5. The mixed metaphor (eyes of feet) is in the
Greek and is not smoothed here.

**καὶ γνῶσιν ὅτι ἐγὼ ἠγάπησά σε**
> γινώσκω, aorist active **subjunctive, 3rd plural** — "**and they may know**,"
> still governed by the ἵνα.
>
> 🛑 **The largest disagreement in this range, and the apparatus does not carry
> it.** **Sinaiticus reads καὶ γνώσῃ — second person singular, future: "and
> *you* will know that I loved you."** 02 and 04 read γνῶσιν, third plural.
>
> This is not a spelling difference. On 02/04 the verse ends with **the
> claimants** learning something. On Sinaiticus it ends with **the addressee**
> learning it — the whole clause turns from them to you. The SBLGNT apparatus
> at 3:9 lists διδῶ, ἥξουσιν/προσκυνήσουσιν, and ἐγώ, and says nothing about
> this. Found by reading 01 directly.
>
> Note that Sinaiticus is internally consistent: it began the verse with
> δέδωκα (v. 8's verb) and ends it with γνώσῃ (v. 3's 2nd-singular γνώσῃ). Its
> reading of the verse hangs together. That makes it a coherent alternative
> text, not an accumulation of slips — which is a reason to record it, not a
> reason to prefer it.

**ἐγὼ** · pronoun, nom. — grammatically unnecessary (the verb already marks 1st
sing.), therefore **emphatic**: *I* loved you. ⚠️ RP omits it; all three
manuscripts on disk have it.

**ἠγάπησά** · ἀγαπάω, aorist active indicative, 1st sing.
> Range: *love · show love to · hold in high regard · prefer · be content with
> · welcome.* The aorist states it as a completed fact, without duration —
> "I loved you," not "I have been loving you." Nothing in the verb form itself
> carries the "unconditional / divine love" distinction from φιλέω that is often
> asserted for it; that distinction is a claim about usage, and this verse is
> not evidence for or against it.

---

### v. 10 — ὅτι ἐτήρησας τὸν λόγον τῆς ὑπομονῆς μου

**ὅτι** · conjunction.
> Range: *because · that · since* — and in some constructions simply the marker
> that opens quoted speech. Here it is either **causal** ("because you kept") or
> **declarative** ("[I know] that you kept"), continuing v. 8's Οἶδα. The Greek
> does not settle it and the translation above leaves both standing.
>
> ⚠️ **02 Alexandrinus does not read ὅτι at all. It reads καί** — "**and** you
> kept the word." That turns the clause from a *reason* into one more item in
> the list of commendations begun in v. 8. **Not in the apparatus**, which is
> silent at v. 10 entirely. 01, 04, RP and KJTR all read ὅτι.

**ἐτήρησας** · τηρέω, aorist active indicative, 2nd sing.
> Range: *watch over · guard · keep under observation · preserve · hold to ·
> observe (a command).* The root sense is **custodial watching**, not obedience;
> obedience is what it comes to mean once the object is a command. Aorist:
> stated as accomplished fact, not as a habit.
>
> 🛑 **04 Ephraemi does not read this word.** It reads **ΕΠΗΡΑϹ / ἐπῆρας** —
> itself a well-formed Greek verb: ἐπαίρω, aorist active 2nd sing., "**you
> lifted up · you raised · you exalted**." Two accounts are possible and this
> file does not choose:
> 1. A **copying slip** for ἐτήρησας — the two words share their opening and
>    closing letters and differ in the middle, the classic shape of one.
> 2. A **real variant**: "you lifted up the word of my endurance."
>
> **Not in the apparatus.** Note that 04 nonetheless reads τηρήσω later in the
> same verse, so whatever happened here happened to this word alone — the scribe
> did not carry it through.

**τὸν λόγον τῆς ὑπομονῆς μου** · λόγος acc. sing. + ὑπομονή gen. sing. + μου.
> **ὑπομονή** · ὑπό ("under") + μένω ("remain, stay"). The literal sense is
> **remaining under** — staying put beneath a weight rather than getting out
> from under it. Range: *endurance · steadfastness · patient waiting ·
> perseverance.* English "patience" is too passive and "perseverance" too
> active; the word is about **not moving**.
>
> **The genitive is unresolved and it matters.** τῆς ὑπομονῆς μου can be:
> - *the word **about** my endurance* (objective)
> - *the word **that comes from** my endurance* (subjective / source)
> - *my **enduring** word* (attributive — the Semitic-style genitive Revelation
>   uses freely)
>
> Greek marks none of these. Every English version picks one silently.

**κἀγώ σε τηρήσω ἐκ τῆς ὥρας τοῦ πειρασμοῦ**
> **κἀγώ** — crasis of καὶ ἐγώ, "**I too / I also**." Emphatic, and the
> reciprocity is deliberate: *you* kept, *I too* will keep. **The same verb
> τηρέω stands on both sides**, and the translation above holds it to one
> English word for that reason.
>
> 🛑 **Sinaiticus has no verb here at all.** 01 reads **κἀγώ σε ἐκ τῆς ὥρας** —
> τηρήσω simply absent, leaving the sentence without a predicate. Almost
> certainly mechanical (the eye skipping from σε onward), but it is what the
> parchment says and **the apparatus does not record it**. 02, 04, RP and KJTR
> all have τηρήσω; P115 begins later in the verse and cannot testify.
>
> ⚠️ **τηρήσω ἐκ — the preposition is ἐκ, not ἀπό.** ἐκ is *out of · from
> within*; ἀπό is *away from · off*. A great deal of modern argument about the
> timing of deliverance is built on which of the two stands here, in both
> directions. What is on the page: **ἐκ, unanimously — all four witnesses and
> both printed traditions.** What ἐκ *implies* about being kept outside the hour
> versus preserved through it, **the preposition does not say**; τηρέω + ἐκ is
> too rare to establish an idiom and this file will not manufacture one.
> Rendered "out of" above because that is what ἐκ is.
>
> **ὥρα** — *hour · a twelfth of daylight · a season · the right moment · a
> short definite span.* Not necessarily sixty minutes.

**τοῦ πειρασμοῦ … πειράσαι** · πειρασμός gen. sing. + πειράζω, aorist infinitive.
> **The verse puns and English cannot keep it.** Both are the same root πειρα-
> ("attempt, try") and both carry the whole range: *test · trial · proving ·
> attempt · enticement to wrong.* Greek has **one** word where English splits
> into "test" (neutral, establishing quality) and "tempt" (hostile, inducing
> failure). Nothing in either form chooses. The options are stacked above
> precisely because a reader who takes "temptation" for the noun and "test" for
> the verb — or the reverse — has invented a distinction the Greek does not draw.

**τῆς μελλούσης ἔρχεσθαι ἐπὶ τῆς οἰκουμένης ὅλης**
> μέλλω present participle gen. sing. fem. + ἔρχομαι present infinitive: *which
> is about to · on the point of · destined to come.* The participle is feminine
> and agrees with **ὥρας**, not with πειρασμοῦ — it is the *hour* that is about
> to come.
>
> **οἰκουμένη** — a present passive participle of οἰκέω ("dwell") used as a
> noun: literally **the being-inhabited [land]**. Range: *the inhabited world ·
> the settled earth · the civilised world · (in ordinary Greek and Roman usage)
> the empire.* It is not a word for the planet. ὅλης — "whole, entire."

**τοὺς κατοικοῦντας ἐπὶ τῆς γῆς** · κατοικέω, present participle acc. pl.
> κατά + οἰκέω — *settle down · dwell permanently · inhabit.* The κατα- prefix
> is the difference between residing and merely staying. **γῆ**: *earth · land ·
> ground · soil · a country.* Whether this is the globe or a territory is not
> decidable from the noun.
>
> ⚠️ P115, entering mid-verse at πειράσαι, carries a **dittography** here —
> τούς written twice, the first struck, visible in the transcription as
> `τουσ {} τουσ`. A copying slip with no bearing on sense, recorded because it
> is the first thing this witness does on arriving in the passage.

---

### v. 11 — ἔρχομαι ταχύ· κράτει ὃ ἔχεις

> 🛑 **This is where the KJV's "Behold" comes from, and it is in no manuscript
> on this disk.**
> **KJTR reads Ἰδού, ἔρχομαι ταχύ.** SBLGNT, RP, and **all four manuscripts —
> 01, 02, 04 and P115 — read simply ἔρχομαι ταχύ, with no ἰδού.** Four
> witnesses against, none for. This is not even a case where the Byzantine and
> Alexandrian traditions split: **RP agrees with the majuscules against the
> Textus Receptus.** The apparatus does not list it, because the apparatus
> collates WH / Treg / NA28 / RP — and all four of *those* omit it, so from the
> apparatus's point of view there is nothing to report. The reading has to be
> found by opening the TR itself.
>
> Compare Rev 22:7 and 22:12, where ἰδού **is** in the text. A scribe
> harmonising v. 11 to those is the obvious explanation. It is still an
> explanation, not a demonstration.

**ἔρχομαι** · ἔρχομαι, present **middle** indicative, 1st sing.
> Present tense, not future. Greek uses the present both for an action already
> under way and for one imminent and certain; "I am coming" holds both where
> "I will come" narrows it. Nothing in the form dates the arrival.

**ταχύ** · adverb, from ταχύς.
> Range: *quickly · swiftly · without delay · soon · suddenly.* **Two different
> claims live in this one word** and Greek does not separate them: *speed of
> travel once begun* (quickly) versus *shortness of the interval before it
> begins* (soon). Both are printed above for that reason.

**κράτει** · κρατέω, present active **imperative**, 2nd sing.
> From κράτος (*strength, might, dominion*). Range: *take hold of · grip · seize
> · hold fast · master · rule over.* The physical sense is the base one — a hand
> closing on something. **Present imperative: continuous** — *keep gripping*,
> not *grip once*. All four manuscripts read it (01 spells it κρατι, an itacism).

**ὃ ἔχεις** · relative pronoun acc. sing. **neuter** + ἔχω present 2nd sing.
> "**what** you have." Neuter — so the antecedent is not the wreath (masc.), not
> the word (masc.), not the door (fem.). It is left unstated.

**ἵνα μηδεὶς λάβῃ τὸν στέφανόν σου** · ἵνα + λαμβάνω, aorist subjunctive 3rd sing.
> Regular Greek here — ἵνα with the subjunctive, unlike v. 9's ἵνα + future
> indicative. λαμβάνω: *take · receive · seize · get hold of.* The verb does not
> specify theft; it specifies **transfer of possession**.
>
> **στέφανος** · from στέφω, "encircle, wreathe." This is the **woven wreath** —
> the athlete's victory garland, the banqueter's crown of leaves, the civic
> honour-crown. It is **not** the royal diadem.
>
> ⚠️ **Revelation itself proves it keeps the two apart.** διάδημα, the actual
> royal band, occurs **3 times** in the book (12:3, 13:1, 19:12); στέφανος
> occurs **8 times**; the author never confuses them. Counted directly in
> `87-Re-morphgnt.txt`. So English "crown" imports a monarchy the word does not
> carry, which is why "wreath / garland" leads the options above.
>
> **All four manuscripts and both printed editions agree on this verse
> word-for-word** apart from Sinaiticus's itacisms (κρατι, εχισ, μηδισ) and its
> overline abbreviation of τόν. **It is the most stable verse in the range** —
> and the one verse where the KJV adds a word.

---

### v. 12 — ὁ νικῶν ποιήσω αὐτὸν στῦλον ἐν τῷ ναῷ τοῦ θεοῦ μου

**ὁ νικῶν** · νικάω, present active participle, **nominative** sing. masc.
> 🛑 **A hanging nominative.** The participle is nominative — grammatically the
> subject — but the sentence's verb is ποιήσω, *first* person ("I will make"),
> and the one conquering is picked up again as **αὐτόν, accusative**. The
> opening phrase has no syntactic connection to what follows; it is announced,
> then resumed by a pronoun. This is a *nominativus pendens*, and in Revelation
> it is a habit rather than an error — compare ἵνα + future indicative at v. 9.
> **All four witnesses read it this way. Nobody corrected it.** The em-dash above
> marks the break; smoothing it to "to the one who conquers I will grant" is a
> repair, not a rendering.
>
> νικάω range: *conquer · prevail · be victorious · win a lawsuit · overcome.*
> Same verb as v. 5.

**ποιήσω αὐτὸν στῦλον** · ποιέω future 1st sing. + αὐτός acc. + στῦλος acc.
> A double accusative: *make X [into] Y.*
>
> 🛑 **Sinaiticus reads ποιήσω αὐτῷ — dative, not accusative.** Not an itacism;
> -ῳ and -ον are confusable neither by sound nor by sight. On 01 the sense shifts
> from "**I will make him** a pillar" to "**I will make for him** a pillar" — the
> person is no longer the pillar, the pillar is a thing given to him. 02, 04,
> P115, RP and KJTR all read αὐτόν. **Not in the apparatus.**
>
> **στῦλος** — *pillar · column · supporting post.* Architectural and
> load-bearing; the word is about **holding a structure up**, not about ornament
> or permanence in the abstract.

**ἐν τῷ ναῷ τοῦ θεοῦ μου**
> ⚠️ **01 omits ἐν**, reading a bare dative τῷ ναῷ. The sense is unaffected — a
> locative dative does the same work — but it is one more place where Sinaiticus
> stands alone and the apparatus is silent.
>
> **ναός** · **the inner sanctuary**, the dwelling-chamber itself — not the
> temple complex. Greek distinguishes it from **ἱερόν**, the whole precinct with
> its courts and colonnades.
>
> ⚠️ **Revelation uses ναός 16 times and ἱερόν 0 times** — counted in
> `87-Re-morphgnt.txt`; the count is exactly zero. The book never once speaks of
> the temple *grounds*. English "temple" flattens a distinction the author keeps
> without exception across the whole book, which is why "sanctuary / inner
> shrine" leads above.

**καὶ ἔξω οὐ μὴ ἐξέλθῃ ἔτι** · ἔξω + οὐ μή + ἐξέρχομαι aorist subj. + ἔτι.
> **οὐ μή + aorist subjunctive** is the strongest negation Greek has — an
> emphatic denial that the thing will *ever* occur. "Certainly not" above is the
> weakest possible English for it.
>
> The construction is redundant on purpose: **ἔξω** ("outside") +
> **ἐξ**-έρχομαι ("go **out**") — *outside he will not go out*. The doubling is
> in the Greek and is kept.
>
> ⚠️ **01 omits ἔτι** ("any longer · still · yet"). With ἔτι the promise is that
> the going-out stops; without it, that it never happens at all. 02, 04, P115,
> RP and KJTR have it. **Not in the apparatus.** P115 breaks off immediately
> after this word — ἐξέλθῃ ἔτι is the last thing it says before the leaf ends.

**καὶ γράψω ἐπ' αὐτὸν τὸ ὄνομα τοῦ θεοῦ μου**
> γράφω future 1st sing. — the ordinary word for writing, with no cultic or
> branding sense of its own. ἐπί + accusative: *upon · onto.*
>
> ⚠️ **04 Ephraemi omits ἐπ' αὐτόν**, reading simply καὶ γράψω τὸ ὄνομα — "and I
> will write the name," with no statement of what it is written *on*. 01, 02, RP
> and KJTR have it; P115 has already broken off. **Not in the apparatus.**

**τῆς καινῆς Ἰερουσαλήμ** · καινός gen. sing. fem. + indeclinable place-name.
> **καινός, not νέος.** Greek has both words for "new" and they are not
> synonyms: **νέος** is new **in time** (recent, young); **καινός** is new **in
> kind** (fresh, unprecedented, of a different sort). καινός stands here and
> again at the verse's last word. English has one word and the distinction does
> not survive.
>
> ⚠️ **Orthography, not variant**: 01 and 04 spell it **κενῆς**, an αι/ε
> itacism — but **κενός is itself a real Greek word meaning *empty***, so the
> spelling collapses two distinct words into one written form. Context settles
> it. The collapse is still worth seeing, because it is exactly the mechanism by
> which real variants are born. 04 does the same at the end of the verse,
> writing τὸ κενόν for τὸ καινόν.
>
> ⚠️ **The nomen sacrum for Jerusalem is contracted differently by different
> scribes**: 01 writes **ΙΗΛΜ**; 02 and 04 write **ΙΛΗΜ**. Same word, two
> conventions. Neither is a textual variant; together they are evidence that the
> abbreviation system was not uniform.

**ἡ καταβαίνουσα ἐκ τοῦ οὐρανοῦ**
> καταβαίνω present active participle, **nominative** sing. fem., with the
> article ἡ.
>
> 🛑 **The second solecism in the verse — and this is the one the apparatus does
> carry.** The participle is **nominative**, but the noun it describes —
> Ἰερουσαλήμ, governed by τῆς καινῆς — is **genitive**. The agreement simply
> fails. Same grammatical habit as ὁ νικῶν at the verse's opening: Revelation
> repeatedly lets a nominative float free of its case-frame.
>
> **RP repairs it**, reading **ἣ καταβαίνει** — relative pronoun with a finite
> verb, "which comes down," which is grammatical.
> `SBLGNT/data/sblgntapp/text/Rev.txt` at Rev 3:12 records exactly this and
> nothing else: *καταβαίνουσα WH Treg NA28 ] καταβαίνει RP*. **It is the only
> entry the apparatus has for all three verses.**
>
> ⚠️ **KJTR sides with the majuscules here**, keeping ἡ καταβαίνουσα. So the
> Textus Receptus preserves the harder reading in v. 12 while adding a word in
> v. 11 — a useful corrective to treating any printed tradition as uniformly
> "smoothed" or uniformly "expanded."
>
> **οὐρανός** — *sky · the heavens · the region above.* Singular here. The word
> covers the physical sky and the divine dwelling without distinguishing them;
> Greek readers had no separate term for either. ⚠️ 02 and 04 write it as a
> nomen sacrum (ΟΥΝΟΥ); **01 writes it out in full** — a small sign that the
> class of words treated as sacred was still fluid.

**καὶ τὸ ὄνομά μου τὸ καινόν**
> The article repeated after the noun (τὸ ὄνομά μου **τὸ** καινόν) — attributive
> position, which makes καινόν emphatic rather than incidental: *my name, the
> new one.* All witnesses agree apart from 04's κενόν spelling, above.

---

# Variants — the whole range, in one place

| Verse | SBLGNT prints | 01 Sinaiticus | 02 Alexandrinus | 04 Ephraemi | In apparatus? |
|---|---|---|---|---|---|
| 2 | ἔμελλον ἀποθανεῖν | = | = | = | yes (RP: ἔμελλες ἀποβάλλειν) |
| 2 | σου **τὰ** ἔργα | τὰ | **omits** | **omits** | yes |
| 3 | ἐὰν μὴ **γρηγορήσῃς** | **μετανοήσῃς** | γρηγορήσῃς | γρηγορήσῃς | 🛑 **no** |
| 3 | ἥξω (no ἐπί σε) | **+ ἐπί σε** | = | = | yes (RP) |
| 3 | γνῷς / ποίαν | **γνώσῃ / οἵαν** | γνῷς | γνῷς | partly (Treg γνώσῃ) |
| 4 | ἔχεις ὀλίγα | = | = | ἑαυτῶν for αὐτῶν | yes (RP order) |
| 5 | οὕτως | = | = | = | yes (RP: οὗτος) |
| 5 | περιβαλεῖται | = | (itacism) | **περιβάλλεται** | 🛑 no |
| 5 | **ἐνώπιον** τοῦ πατρός | **ἔμπροσθεν** | ἐνώπιον | ἐνώπιον | 🛑 **no** |
| 7 | ὁ **ἅγιος**, ὁ **ἀληθινός** | **reversed** | **reversed** | as printed | 🛑 **no** |
| 7 | κλεῖν Δαυίδ | **τοῦ Δαυίδ** | Δαυίδ | Δαυίδ | yes (RP) |
| 7 | οὐδεὶς **ἀνοίγει** | **ἀνοίξει** (fut.) | ἀνοίγει | ἀνοίγει | yes (RP) |
| 8 | οἶδά **σου τὰ** ἔργα | **τὰ ἔργα σου** | as printed | as printed | 🛑 no |
| 8 | κλεῖσαι (no αὐτήν) | no αὐτήν | **+ αὐτήν** | **+ αὐτήν** | 🛑 no |
| 9 | **διδῶ** | **δέδωκα** | διδῶ | διδῶ | partly (RP δίδωμι) |
| 9 | ἥξουσιν / προσκυνήσουσιν (fut.) | = | = | = | yes (RP subj.) |
| 9 | **γνῶσιν** (3 pl.) | **γνώσῃ** (2 sg.) | γνῶσιν | γνῶσιν | 🛑 **no** |
| 9 | ἐγώ | = | = | = | yes (RP omits) |
| 10 | **ὅτι** ἐτήρησας | ὅτι | **καί** | ὅτι | 🛑 **no** |
| 10 | **ἐτήρησας** | = | = | **ἐπῆρας** (ἐπαίρω) | 🛑 **no** |
| 10 | σε **τηρήσω** ἐκ | **omits τηρήσω** | τηρήσω | τηρήσω | 🛑 **no** |
| 10 | **ἐκ** τῆς ὥρας | = | = | = | no — all agree |
| 11 | ἔρχομαι ταχύ (no ἰδού) | = | = | = | 🛑 **no** (KJTR **+ Ἰδού**) |
| 11 | κράτει ὃ ἔχεις … στέφανον | = | = | = | no — all agree |
| 12 | ποιήσω **αὐτόν** | **αὐτῷ** (dat.) | αὐτόν | αὐτόν | 🛑 **no** |
| 12 | **ἐν** τῷ ναῷ | **omits ἐν** | ἐν | ἐν | 🛑 no |
| 12 | ἐξέλθῃ **ἔτι** | **omits ἔτι** | ἔτι | ἔτι | 🛑 no |
| 12 | γράψω **ἐπ' αὐτόν** | ἐπ' αὐτόν | ἐπ' αὐτόν | **omits** | 🛑 **no** |
| 12 | ἡ **καταβαίνουσα** | = | = | = | ✅ **yes** (RP ἣ καταβαίνει) |

**P115** (vv. 10–12 only) agrees with 02/04 against 01 at every point where it is
legible: it has τηρήσω-side text intact from πειράσαι on, ἔρχομαι ταχύ with no
ἰδού, αὐτόν accusative, ἐν τῷ ναῷ, and ἔτι — then breaks off. Its only
peculiarities are mechanical: a struck dittograph τοὺς τοὺς in v. 10 and ναοῦ
corrected to ναῷ in v. 12.

**Sixteen disagreements among the manuscripts are not in the printed apparatus at
all**, and across the three added verses **the apparatus has exactly one entry**
(καταβαίνουσα at v. 12) for eleven observable differences. Four of the new ones
change the sense: v. 10's opening conjunction (because vs and), v. 10's first
verb (kept vs lifted up), v. 10's missing τηρήσω in 01, and v. 12's αὐτῷ vs
αὐτόν (a pillar *given to* him vs him *being* the pillar).

> [!important] The v. 11 case is the sharpest one in the file
> At v. 11 **four manuscripts and RP all agree**, and **KJTR alone adds Ἰδού** —
> which is the KJV's "Behold." An apparatus that collates only printed critical
> editions will never show this, because WH, Treg, NA28 and RP *all* omit the
> word: there is no disagreement *among editions* to record. The addition is
> visible only by opening the Textus Receptus and the manuscripts side by side.
> **A word can be in the most-read English Bible in the world and have no
> support in any witness on this disk, and no apparatus will tell you.**

> [!important] What this means about the printed text
> This is not a claim that SBLGNT is careless — its apparatus is explicitly a
> *selective* one, recording where the major printed editions differ from each
> other, not where the manuscripts do. It is a claim about how it must be used:
> **an apparatus of editions is not an apparatus of manuscripts**, and reading
> only the former leaves you believing a passage is settled where the parchment
> shows it is not. The same lesson as `HIGHLIGHTS.md`'s Erasmus entry, arriving
> from the other direction.

---

# What this passage cannot tell us

- **In vv. 2–9 there is no witness older than the 4th century.** P47 begins at
  9:10; P115 at 3:10. Whatever happened to that text in its first 250 years is
  not recoverable from anything on this disk. **In vv. 10–12 P115 lowers the
  floor by roughly a century — but only there**, and its date is not on disk
  either (see the note at the top).
- **Where 01, 02 and 04 disagree in vv. 2–9, there is no fourth vote.** With
  Vaticanus and Bezae both lacking Revelation entirely, that range has the
  thinnest witness base of any passage translated in this project so far.
  Two-against-one is the *most* that can ever be assembled there, and
  two-against-one among three manuscripts is a weak argument, not a strong one.
  Compare Isaiah 53:11, where independent convergence across traditions made a
  real case. **vv. 10–12 are marginally better off** — P115 gives a genuine
  third vote against Sinaiticus's several singular readings — but it is
  fragmentary and stops inside v. 12.
- **ἐκ at v. 10 does not decide the question that is asked of it.** The
  preposition is stable across every witness; what it *implies* about being kept
  outside a trial versus preserved through one is an argument about idiom, and
  the idiom is not established by this verse or by the frequency of τηρέω + ἐκ in
  the corpus. Both readings survive the grammar, and this file does not choose.
- **The two solecisms in v. 12 are not evidence of a bad copyist.** They are
  uncorrected in all four witnesses, which means they are what the text *is*.
  Whether they reflect a Semitic-language substrate, deliberate style, or
  imperfect Greek is a question about the author, and nothing in the manuscripts
  answers it.
- **The grammar of v. 9 does not identify anyone.** It says a claim is made and
  denied. Who is making it, on what grounds, and what the denial rests on are
  not in the Greek, and this file does not supply them.
- **Root-level derivation has not been done for Greek.** `corpus.py`,
  `rootqueue.py` and the `ranges/` files cover the **Hebrew** OT only
  (8,640 roots, 306,785 words). The semantic ranges above are stated from
  knowledge of Greek and defended from the forms, but they are **not** backed by
  the same mechanical, verse-cited, validator-gated apparatus that the Hebrew
  roots are. That is a real difference in evidentiary standard between this file
  and `ranges/*.json`, and it is stated rather than papered over.

---

## Provenance of this file

**OURS** — our own translation and analysis. Sources: SBLGNT (**EDITED**, 2010),
MorphGNT tagging (**ANALYSIS**), CNTR transcriptions of GA 01, 02, 04 and P115
(**ORIGINAL** — diplomatic transcriptions of manuscripts, not photographs; we
hold **no manuscript images**), and the CNTR files for the printed **RP** and
**KJTR** (**EDITED** — printed editions, used only to locate divergence). No
English translation, interlinear, or gloss file was consulted. Regenerate the
manuscript readings with:

```
./tools/cntr_read.py 01 66 3 2 12
./tools/cntr_read.py 02 66 3 2 12
./tools/cntr_read.py 04 66 3 2 12
./tools/cntr_read.py P115 66 3 10 12          # enters at v.10, breaks off in v.12
grep -E '^66003(01[012])' 'papyri/cntr-transcriptions/critical texts/RP.txt'
grep -E '^66003(01[012])' 'papyri/cntr-transcriptions/critical texts/KJTR.txt'
awk '$1>=270302 && $1<=270312' greek-nt/morphgnt/87-Re-morphgnt.txt
sed -n '/^Revelation 3:2$/,/^Revelation 3:14$/p' \
    greek-nt/SBLGNT/data/sblgntapp/text/Rev.txt
```

> [!warning] The apparatus command in this file was wrong until 2026-08-21
> The earlier version read `awk '/^3:2 /,/^3:10 /' … Rev.txt` and **it did not
> do what it claimed**. In `sblgntapp`, only the **first entry of a chapter**
> carries a `C:V` prefix (`3:2 ἔμελλον…`); every later entry in that chapter is
> keyed by **bare verse number** (`3 ἥξω…`, `9 διδῶ…`, `12 καταβαίνουσα…`). So
> the closing pattern `/^3:10 /` never matched anything, the awk range ran from
> line 107 to end-of-file, and the command silently returned **864 lines — the
> rest of the book** — instead of the eight verses it named. It never errored.
>
> The lesson is the file's own: **a reproduction command that cannot fail is not
> a reproduction command.** The replacement above anchors on the
> `Revelation C:V` header lines and returns 28 lines. Re-check it by counting.

**Counts cited in this file, and how to re-check them:**

```
grep -c ' διάδημα$' greek-nt/morphgnt/87-Re-morphgnt.txt   # 3
grep -c ' στέφανος$' greek-nt/morphgnt/87-Re-morphgnt.txt  # 8
grep -c ' ναός$'     greek-nt/morphgnt/87-Re-morphgnt.txt  # 16
grep -c ' ἱερόν$'    greek-nt/morphgnt/87-Re-morphgnt.txt  # 0
```

**Extended 2026-08-21** from 3:2–9 to 3:2–12. The three added verses complete the
letter to Philadelphia; the earlier range ended mid-letter.
