# John 1:1–18 — the Prologue

Translated from the Greek directly. No English translation was consulted or
adapted.

## What this is built from, and what it is not

**Used — grammatical analysis and manuscripts, not anyone's English:**

- `greek-nt/morphgnt/64-Jn-morphgnt.txt` — the SBLGNT text (EDITED, Holmes
  2010 — a modern eclectic reconstruction, no single manuscript reads exactly
  this way) with per-word morphological tagging. Reference format in that
  file is `BBCCVV` where John = **book `04`** in MorphGNT's internal
  Gospel-order numbering (Matt 01, Mark 02, Luke 03, John 04) — confirmed by
  inspection; this is a *different* numbering than CNTR's canonical-order
  book codes used below.
- `greek-nt/Nestle1904/xml/` (EDITED, 1904) for cross-checking word division
  and osisIds.
- **The actual manuscripts**, queried live with `tools/cntr_read.py` against
  John 1:18: P66 (c. 200 CE), P75 (c. 175–225 CE), Sinaiticus (01, c. 330–360
  CE), Vaticanus (03, c. 300–325 CE), Ephraemi Rescriptus (04, 5th c. CE),
  Alexandrinus (02, c. 400–440 CE), and Bezae (05, c. 400 CE, which turns out
  to have no reading here — see below).
- My own knowledge of Koine Greek for lexical range.

**Not used**: KJV, any modern English version, any interlinear's English
column, or any gloss file. The semantic ranges below are stated from how each
root and construction behaves in Greek, not copied from a dictionary.

**A note on the base text**: SBLGNT is an *edited* eclectic text (see
`PROVENANCE.md`) — its editor's own critical apparatus is baked into the
running text as raised marks (⸂ ⸃ pointing to a variant unit, ⸀ marking a
word the editor chose among alternatives). Those marks appear at vv. 15, 16,
and 18 below. I did not chase down every one of them — only v. 18 is in scope
for this assignment, and I checked it against the primary manuscripts myself
rather than trusting the SBLGNT apparatus secondhand (see §18).

---

## Verse by verse

### v. 1 — Ἐν ἀρχῇ ἦν ὁ λόγος, καὶ ὁ λόγος ἦν πρὸς τὸν θεόν, καὶ θεὸς ἦν ὁ λόγος.

**Ἐν ἀρχῇ** · preposition ἐν (dat.) + **ἀρχή**, noun, dat. sing. fem., anarthrous
> Root sense of ἀρχή: a starting point, first cause, or origin — and, from the
> same root, *rule, sovereignty, dominion* (the sense surviving in English
> "archon," "monarchy," "anarchy" = no-rule). Range: *beginning · origin ·
> first principle · rule · authority.* Here, in a prepositional phrase, it is
> the "beginning" sense — the phrase echoes the identical anarthrous ἐν ἀρχῇ
> that opens the Septuagint's Genesis 1:1. Neither phrase carries the Greek
> article; prepositional phrases of this kind function as definite in Greek
> without needing one, the same way "in beginning" reads as "in the
> beginning" as a fixed idiom. **"In [the] beginning."**

**ἦν** · verb, εἰμί, imperfect active indicative, 3rd sing.
> "was" — but specifically the *imperfect*: durative, backgrounded past
> existence, with no notion of coming-to-be. This matters because the same
> passage later uses **ἐγένετο** (aorist of γίνομαι, "came to be / happened")
> for everything that is made (vv. 3, 6, 10, 14, 17). The Prologue keeps the
> two verbs strictly apart: ἦν for the Word and for God, ἐγένετο for
> everything contingent. That is a fact about which verb-form appears where,
> not a claim about what it proves theologically.

**ὁ λόγος** · article + noun, nom. sing. masc., λόγος
> From λέγω, "to say, speak, reckon, count, tell." The noun's range is wide:
> *word · speech · utterance · statement · account · narrative · argument ·
> reason · rationale · ratio · discourse · matter, subject-under-discussion.*
> In Greek philosophical usage (Heraclitus, the Stoics) λόγος also names the
> rational ordering-principle running through the cosmos. Rendering it
> **"Word"** — capitalized, as a proper name — is a translation choice with a
> history (it goes back through Latin *Verbum*). It selects the
> speech/utterance pole of the range and treats the word as a title; it
> downplays the "reason/account/ordering-principle" pole that a Greek reader
> steeped in either the LXX (where λόγος κυρίου, "the word/utterance of the
> LORD," is the mechanism of creation and prophecy, Ps 33:6, Gen 1) or in
> Greek philosophy would also have heard. Nothing here decides that dispute;
> both audiences are real and the Greek word covers both. I keep **"Word"**
> capitalized below because it is functioning as a name-like subject across
> the passage, while flagging that this typographic distinction (a capital
> letter marking personhood) does not exist in the Greek at all — the
> manuscripts are written in unaccented majuscule, with no upper/lower-case
> distinction to signal it.

**πρὸς τὸν θεόν** · preposition πρός (+ acc.) + article + θεός, acc. sing. masc.
> πρός + accusative with a stative verb like ἦν denotes proximity/relation
> more vividly than a flat "with" — its range covers *toward · to · in the
> direction of · face to face with · in company with · in relation to.*
> **"with God"** is the compact rendering, but it flattens the "facing/toward"
> component the preposition carries.

**καὶ θεὸς ἦν ὁ λόγος** — the contested clause.
> Word order: **θεὸς** (predicate noun, **no article**) — **ἦν** (copula) —
> **ὁ λόγος** (subject, **with article**). The predicate stands first,
> anarthrous, before the verb; the subject follows, articular.
>
> This is one of the most argued clauses in the New Testament, and the syntax
> genuinely underdetermines the answer. Three things are true at once:
>
> 1. **Colwell's Rule** (E. C. Colwell, 1933) observed that in NT Greek,
>    a *definite* predicate noun that *precedes* the verb usually lacks the
>    article — anarthrous placement before the verb was, empirically, how
>    Greek often marked a predicate noun that was nonetheless definite. On
>    this observation, θεός here *could* be definite ("the Word was God" /
>    "the Word was the God") without needing the article, purely because of
>    where it sits in the clause.
> 2. **The standard objection to using Colwell's Rule this way**: the rule as
>    Colwell stated it is one-directional. It says definite anarthrous
>    predicates are usually pre-verbal; it does **not** say pre-verbal
>    anarthrous predicates are usually definite. The converse doesn't follow
>    from the original statistical observation, and later study of Colwell's
>    own data (notably Harner, 1973, and subsequent work) found a large
>    proportion of pre-verbal anarthrous predicates in the NT are best read as
>    **qualitative** — describing the *nature or category* the subject
>    belongs to, rather than either its precise identity (definite) or its
>    membership in an indefinite class ("a god" among others).
> 3. Greek has no true indefinite article, so an anarthrous noun is not
>    automatically "a ___" the way it would default to in English — anarthrous
>    nouns in Greek can be definite, qualitative, or genuinely indefinite
>    depending on context, and word order/emphasis is doing real work here
>    that a bare parse code cannot settle.
>
> **What the syntax permits, without picking a winner:**
> - **Qualitative**: "what God was, the Word was" / "the Word was divine" —
>   the Word fully shares the nature/category denoted by θεός, without the
>   clause asserting the Word simply *is* ὁ θεός (the specific referent named
>   in the clause just before, v. 1b). This is the reading most modern
>   grammarians who reject a simple Colwell-definite argument tend to favor,
>   on the grounds that flatly equating ὁ λόγος with ὁ θεός here would erase
>   the distinction the same verse just drew between them ("the Word was
>   *with* God").
> - **Definite**: "the Word was God" — full identity with the God just named,
>   with the anarthrous, pre-verbal position explained by Colwell's pattern
>   rather than by indefiniteness.
> - **Indefinite**: "the Word was a god" — grammatically available in that bare
>   Greek nouns are not inherently definite, though this is a minority
>   position among grammarians and requires treating θεός as marking
>   membership in a class of beings called θεοί rather than the qualitative or
>   definite readings above.
>
> The grammar alone does not adjudicate among these. This project reports the
> range the syntax permits rather than declaring one correct.

**The verse (SBLGNT running text, my rendering):**

> **In the beginning was the Word, and the Word was with God, and [what God
> was, the Word was / the Word was God / the Word was a god] — the Word was θεός.**

I am leaving the third clause both glossed and untranslated-into-one-English-
choice above deliberately; see the box for why. If a single running English
sentence is wanted for readability, the least loaded compact form the Greek
supports is: **"...and God was what the Word was"** (foregrounding the
qualitative reading, on the grounds it best preserves the anarthrous/articular
contrast that vanishes in English word order either way) — but this is a
translator's choice, flagged as such, not a grammatical necessity.

---

### v. 2 — οὗτος ἦν ἐν ἀρχῇ πρὸς τὸν θεόν.

**οὗτος** · demonstrative pronoun, nom. sing. masc.
> "This one / he." Resumes ὁ λόγος from v. 1 as subject.

**ἦν ... πρὸς τὸν θεόν** — as v. 1: imperfect "was," πρός + acc. "with/toward
God."

> **This one was in the beginning with God.**

---

### v. 3 — πάντα δι' αὐτοῦ ἐγένετο, καὶ χωρὶς αὐτοῦ ἐγένετο οὐδὲ ἕν. ὃ γέγονεν

**πάντα** · adjective, nom. plur. neut., πᾶς — "all things, everything."

**δι' αὐτοῦ** · preposition διά (+ gen.) — "through him." διά + genitive marks
means/agency/channel: *through, by means of, by the agency of.*

**ἐγένετο** · verb, γίνομαι, aorist middle indicative, 3rd sing.
> "came into being / came to be / happened." The aorist marks a discrete
> event of coming-to-be — the verb that, across this passage, is reserved for
> what is contingent/made, as against ἦν for the Word's own durative
> existence (see v. 1 note).

**χωρὶς αὐτοῦ** · preposition χωρίς (+ gen.) — "apart from him, without him,
separately from him."

**οὐδὲ ἕν** · "not even one [thing]" — emphatic negation, οὐδέ ("not even") +
εἷς/ἕν ("one," neuter).

**ὃ γέγονεν** · relative pronoun ὅ (neut. nom./acc. sing.) + γίνομαι, perfect
active indicative
> "that which has come to be / what has come into being." γέγονεν is
> *perfect* tense (not the aorist ἐγένετο used earlier in the same verse) —
> a state resulting from a past event, "stands having come to be."
>
> **A genuine punctuation ambiguity, not resolvable from the Greek alone**:
> the earliest manuscripts carry no punctuation at all — sentence division is
> entirely an editorial layer added by modern editors (SBLGNT punctuates as
> printed above, ending v. 3 with a full stop *after* ὃ γέγονεν, so that it
> reads as the start of v. 4: *"That which has come into being — in him was
> life..."*). The older, equally grammatical construal (attested in patristic
> quotation and reflected in some manuscript punctuation traditions) attaches
> ὃ γέγονεν to the end of v. 3 instead: *"...not one thing came into being
> apart from him that has come into being."* Both readings are complete,
> grammatical Greek sentences; nothing in the syntax itself decides which
> clause ὃ γέγονεν belongs to.

> **v.3, reading A (with SBLGNT's own punctuation, carrying into v.4):**
> All things came into being through him, and apart from him not one thing
> came into being.
>
> **v.3, reading B (ὃ γέγονεν closing v.3):**
> All things came into being through him, and apart from him not one thing
> that has come into being came into being.

---

### v. 4 — ἐν αὐτῷ ζωὴ ἦν, καὶ ἡ ζωὴ ἦν τὸ φῶς τῶν ἀνθρώπων·

*(Following reading A above — see v.3 note for the alternative division.)*

**ζωὴ** · noun, nom. sing. fem., ζωή — "life," broadly: biological life,
existence, one's manner of living. Anarthrous here as subject-complement of
an existential ἦν ("there was life in him").

**ἦν τὸ φῶς τῶν ἀνθρώπων** — note the contrast with v. 1c: here **both** the
subject (ἡ ζωή) **and** the predicate (τὸ φῶς) carry the article. This is a
straightforward, reversible identity statement, not the anarthrous-predicate
puzzle of v. 1c — worth flagging precisely because it shows the Prologue
*does* use fully-articular equations elsewhere, which throws the anarthrous
θεός of v. 1c into relief as a distinct construction, not an accident of
style.

**φῶς** · noun, "light" — physical light, without further qualification here.

**τῶν ἀνθρώπων** · article + ἄνθρωπος, gen. plur. masc. — "of humans /
mankind." ἄνθρωπος is the gender-generic word for a human being, distinct
from ἀνήρ ("a male," which appears later at v. 13).

> **In him was life, and the life was the light of humankind.**

---

### v. 5 — καὶ τὸ φῶς ἐν τῇ σκοτίᾳ φαίνει, καὶ ἡ σκοτία αὐτὸ οὐ κατέλαβεν.

**φαίνει** · verb, φαίνω, present active indicative — "shines, gives light,
shows itself, appears." Present tense: an ongoing, still-current shining, not
a past event.

**σκοτία** · noun, "darkness" — the state/realm of being without light.

**κατέλαβεν** — the contested verb.
> κατά ("down, against, thoroughly") + λαμβάνω ("take, grasp, seize, receive").
> The compound's range genuinely splits into two families of sense that pull
> in opposite directions for this clause:
> - **to seize / overpower / overcome** — a hostile or forceful "getting hold
>   of," used elsewhere of darkness/danger overtaking someone, of a storm
>   catching a ship, of arresting or seizing a person or a place.
> - **to grasp / comprehend / take in [mentally]** — the same compound is
>   used for mental apprehension, "getting hold of" an idea, understanding.
>
> Both are attested, live senses of καταλαμβάνω in Koine Greek, and the
> negated aorist here — "the darkness did **not** κατέλαβεν it" — is
> genuinely ambiguous between them:
> - **"the darkness did not overcome/overpower it"** (the light kept shining
>   against opposition; a claim about a contest)
> - **"the darkness did not grasp/comprehend it"** (the darkness had no
>   purchase on it, could not take it in/understand it; a claim about
>   incomprehension)
>
> Nothing in the grammar picks between these; both are legitimate translations
> of κατέλαβεν and are given here without resolving which the author intended.

> **And the light shines in the darkness, and the darkness did not
> overcome it / did not grasp it.**

---

### v. 6 — Ἐγένετο ἄνθρωπος ἀπεσταλμένος παρὰ θεοῦ, ὄνομα αὐτῷ Ἰωάννης·

**Ἐγένετο** · aorist of γίνομαι again — "there came to be / there arose." Note
this is applied to a human being's historical appearance, the same verb used
of creation in v. 3 — the Prologue does not reserve ἐγένετο only for
cosmic-scale events.

**ἀπεσταλμένος** · participle, perfect passive, ἀποστέλλω
> "having been sent / sent out, commissioned, dispatched [as an envoy]." Root
> of ἀπόστολος, "apostle" ("one sent out"). Perfect tense: a sending with
> ongoing effect — he stands sent, not merely was sent once and done.

**παρὰ θεοῦ** · "from God" — παρά + genitive, "from the side of, from the
presence of."

**ὄνομα αὐτῷ Ἰωάννης** · literally "name to-him John" — idiomatic naming
formula, "his name [was] John."

> **There came to be a man sent from God; his name was John.**

---

### v. 7 — οὗτος ἦλθεν εἰς μαρτυρίαν, ἵνα μαρτυρήσῃ περὶ τοῦ φωτός, ἵνα πάντες πιστεύσωσιν δι' αὐτοῦ.

**μαρτυρίαν / μαρτυρήσῃ** · μαρτυρία (noun) / μαρτυρέω (verb) — "testimony,
witness" / "to testify, bear witness, give evidence." Originally a legal/
juridical term (a witness's deposition), extended to any solemn attestation.

**πιστεύσωσιν** · verb, πιστεύω, aorist active subjunctive, 3rd plur.
> Range: *to believe, to trust, to have faith in, to put confidence in, to
> rely on.* The word covers both a cognitive "hold to be true" and a
> relational "place trust in" — Greek does not split these into two verbs the
> way some later theological vocabularies do; both senses live inside
> πιστεύω and both are live possibilities wherever it recurs (again at v. 12).

**δι' αὐτοῦ** · "through him." Note: the nearest grammatical antecedent for
αὐτοῦ is τοῦ φωτός ("the light") in the immediately preceding clause, not
Ἰωάννης — the natural reading is "believe through [testimony about] the
light," though the referent is not marked with total formal clarity by the
pronoun alone.

> **This one came for testimony, so that he might testify about the light, so
> that all might believe/trust through it.**

---

### v. 8 — οὐκ ἦν ἐκεῖνος τὸ φῶς, ἀλλ' ἵνα μαρτυρήσῃ περὶ τοῦ φωτός.

**ἐκεῖνος** · demonstrative pronoun, "that one" — distancing/distinguishing
demonstrative, marking John off from the subject of v. 9.

**ἀλλ' ἵνα μαρτυρήσῃ** — an ellipsis in the Greek: literally "but in order
that he might testify..." with no verb supplied for what he *did* — a verb
like "he came" must be mentally carried over from v. 7's ἦλθεν. This is a
gap in the Greek's surface grammar, not an invented meaning; I flag it as
elliptical rather than silently filling it.

> **He was not the light, but [came] so that he might testify about the light.**

---

### v. 9 — ἦν τὸ φῶς τὸ ἀληθινὸν ὃ φωτίζει πάντα ἄνθρωπον ἐρχόμενον εἰς τὸν κόσμον.

**ἀληθινόν** · adjective, "true, real, genuine, authentic" — ἀληθινός in Greek
usage regularly contrasts the real/archetypal thing with a copy, type, or
mere semblance of it (distinct from ἀληθής, "true" in the sense of factually
accurate); range: *true · real · genuine · the substance as against the
shadow/type.*

**φωτίζει** · verb, φωτίζω, present active indicative — "gives light to,
illuminates, enlightens" (denominative from φῶς).

**ἐρχόμενον** — the contested word.
> Participle, present middle/passive, formed as ἐρχόμενος/-η/-ον from
> ἔρχομαι, "to come, go." MorphGNT's own tagging parses this token as
> **accusative singular masculine** — agreeing with **πάντα ἄνθρωπον**
> ("every human, [who is] coming into the world"), immediately preceding it
> in word order.
>
> But that tagging is an editorial *decision*, not a fact given for free by
> the letters on the page: the inflected form ἐρχόμενον is **identical** in
> spelling for the masculine accusative singular *and* the neuter
> nominative/accusative singular of this participle class. τὸ φῶς ("the
> light") earlier in the same sentence is neuter — grammatically the
> identical surface form ἐρχόμενον could in principle belong with it instead,
> especially read against the earlier ἦν τὸ φῶς at the start of the verse
> (yielding a periphrastic-style "the light... was coming into the world").
> Word order favors attaching it to the immediately adjacent ἄνθρωπον; the
> homographic form does not forbid attaching it to τὸ φῶς. Both are
> grammatically live:
> - **attached to "man"**: "...enlightens every man who is coming into the
>   world" (the coming belongs to every human being who is born)
> - **attached to "the light"**: "...enlightens every man — [it, the light,]
>   coming into the world" (the coming belongs to the light itself)

> **The true light, which enlightens every human coming into the world, was
> [shining] / The true light was [there], enlightening every human — coming
> into the world.**

---

### v. 10 — Ἐν τῷ κόσμῳ ἦν, καὶ ὁ κόσμος δι' αὐτοῦ ἐγένετο, καὶ ὁ κόσμος αὐτὸν οὐκ ἔγνω.

**κόσμος** · noun, "world" — root sense *order, arrangement, adornment*
(the same root gives "cosmetic"); extended to "the ordered universe/world."
Range: *order · adornment · the world/universe as an ordered whole ·
(sometimes) humanity as a collective.*

**ἔγνω** · verb, γινώσκω, aorist active indicative — "knew, recognized, came
to know [by experience/acquaintance]" — distinct from the stative "know as a
settled fact" sense that Greek carries in a different verb (οἶδα, not used
here); γινώσκω's range leans toward knowledge gained through encounter or
relationship.

> **He was in the world, and the world came into being through him, and the
> world did not know/recognize him.**

---

### v. 11 — εἰς τὰ ἴδια ἦλθεν, καὶ οἱ ἴδιοι αὐτὸν οὐ παρέλαβον.

**τὰ ἴδια / οἱ ἴδιοι** · adjective ἴδιος, "one's own" — neuter plural "his own
[things/property/home]," masculine plural "his own [people]." The same
adjective, once of place/possession and once of persons.

**παρέλαβον** · verb, παραλαμβάνω, aorist active indicative
> παρά ("alongside, to one's side") + λαμβάνω ("take"). Distinct from the
> simple λαμβάνω used in the very next verse (v. 12, ἔλαβον) — the παρα-
> prefix adds the sense of taking someone *to one's own side*, receiving them
> in, welcoming them as one's own — a stronger claim than bare "receiving"
> would be. Range: *to receive, take to oneself, accept, welcome in.*

> **He came to his own [home/domain], and his own [people] did not receive/
> welcome him in.**

---

### v. 12 — ὅσοι δὲ ἔλαβον αὐτόν, ἔδωκεν αὐτοῖς ἐξουσίαν τέκνα θεοῦ γενέσθαι, τοῖς πιστεύουσιν εἰς τὸ ὄνομα αὐτοῦ,

**ἔλαβον** · λαμβάνω, aorist active — plain "took, received," without the
"to one's own side" nuance of παρέλαβον in v. 11 (see there).

**ἐξουσίαν** · noun, ἐξουσία — range: *authority · right · power · permission
· license · jurisdiction.* From ἔξεστι, "it is permitted/possible."

**τέκνα** · noun, τέκνον, "children" — from τίκτω, "to bear, give birth to."
τέκνον emphasizes the fact of having been born (offspring), gender-neutral,
distinct from υἱός ("son," which can carry legal-heir connotations and
appears in the v. 18 variant discussed below).

**γενέσθαι** · infinitive, aorist middle, γίνομαι — "to become, to come to
be" — the same verb-family as ἐγένετο throughout, here as an infinitive
completing ἐξουσίαν ("authority/right to become...").

> **But as many as received him, to them he gave the right to become children
> of God — to those trusting in his name —**

---

### v. 13 — οἳ οὐκ ἐξ αἱμάτων οὐδὲ ἐκ θελήματος σαρκὸς οὐδὲ ἐκ θελήματος ἀνδρὸς ἀλλ' ἐκ θεοῦ ἐγεννήθησαν.

**αἱμάτων** · noun, αἷμα, genitive **plural** — "of bloods." Worth flagging as
a real morphological oddity: αἷμα ("blood") is ordinarily used in the
singular in Greek; a genitive *plural* here (αἱμάτων, not the expected
singular αἵματος) is a marked, unusual form. What it is doing — evoking the
mingling of parental bloods in conception, or reflecting a Hebraic idiom
carried into Greek — is an interpretive question the plural form itself does
not settle; I flag the form as genuinely irregular rather than assert one
explanation for it.

**θελήματος** · noun, θέλημα, "will, desire, wish, intent" — from θέλω, "to
will, wish."

**σαρκός** · noun, σάρξ, "flesh" — range: *flesh/body · human nature ·
physical descent/lineage · corporeal existence.* The same word (σάρξ)
recurs in v. 14 for the Word "becoming flesh" — a deliberate verbal echo
worth noting: the word used for ordinary human generation here is the exact
word used of the Word's own becoming two verses later.

**ἀνδρός** · noun, ἀνήρ, "a man" — specifically *male*, as distinct from the
gender-generic ἄνθρωπος used elsewhere in this passage (vv. 4, 9).

**ἐγεννήθησαν** · verb, γεννάω, aorist passive indicative — "were begotten,
were born, were brought forth." This is the actual "beget" verb (root
γενν-) — and it stands right here in the text, letting us see directly
that it is a *different* root from the μονογεν- of μονογενής in v. 14 and
v. 18 (μόνος + γένος, "kind/class," not μόνος + this verb γεννάω). See v. 14.

> **who were begotten not from bloods, nor from the will of the flesh, nor
> from the will of a man/husband, but from God.**

---

### v. 14 — Καὶ ὁ λόγος σὰρξ ἐγένετο καὶ ἐσκήνωσεν ἐν ἡμῖν, καὶ ἐθεασάμεθα τὴν δόξαν αὐτοῦ, δόξαν ὡς μονογενοῦς παρὰ πατρός, πλήρης χάριτος καὶ ἀληθείας·

**σὰρξ ἐγένετο** · "became flesh" — ἐγένετο again, the same aorist "came to
be" used of creation (v. 3), the world (v. 10), John (v. 6). Whatever is
being claimed here is being described with the identical verb used
throughout the passage for things coming into existence/happening — a fact
about the Greek's vocabulary choice, not a further interpretive claim.

**ἐσκήνωσεν** · verb, σκηνόω, aorist active indicative
> From σκηνή, "tent" (the same noun used in the LXX for the wilderness
> Tabernacle, ἡ σκηνὴ τοῦ μαρτυρίου, "the tent of testimony/witness"). The
> verb's concrete, literal sense is "pitched a tent, encamped, took up
> residence in a tent." Range: *to pitch tent · to encamp · to dwell,
> [with the tent-image retained].* Rendering it simply "dwelt" loses the
> physical tent-image the Greek root carries.

**ἐθεασάμεθα** · verb, θεάομαι, aorist middle indicative, 1st plur.
> "we gazed at, beheld, viewed" — root of English "theater." A stronger,
> more deliberate word than a generic "see" (contrast ὁράω/ἑώρακεν in v. 18):
> it denotes attentive, often wondering contemplation, viewing as a spectacle.

**δόξαν** · noun, δόξα, "glory" — from δοκέω, "to seem, to think, to have an
opinion." δόξα's older Greek sense is "opinion, reputation, what one is
thought to be"; the sense "visible splendor/glory [of God]" is a semantic
shift under the influence of the Septuagint, where δόξα regularly renders
Hebrew כָּבוֹד ("weight, honor, glory"). Flagging this because the "radiance/
glory" sense is not the word's native Greek starting point — it is a
loanword-shift carried in through biblical Greek usage, which I note rather
than pretend is simply "what δόξα means" in Greek generally.

**μονογενοῦς** — the flagged word.
> Genitive singular of μονογενής, an adjective built from **μόνος** ("only,
> alone, sole") + **γένος** ("kind, class, race, offspring-group" — from the
> same root as γίνομαι/γεννάω but itself a noun meaning *kind/type*, not the
> verb "to beget"). The compound's transparent sense is **"only [one] of its
> kind" / "one-of-a-kind" / "unique."**
>
> This is *not* built from μόνος + γεννάω ("to beget/father"); that would
> require a different compound. The traditional English rendering
> **"only-begotten"** imports a begetting/generation sense that the word's
> actual components do not contain — it reads μονογενής as if its second half
> were the verb "to beget" rather than the noun "kind." (Contrast v. 13's
> ἐγεννήθησαν, the real "beget" verb, standing two verses earlier in the same
> passage — a useful control case for seeing the two roots are not the same.)
> The accurate range of μονογενής is: *only one of its kind · unique · one
> and only · sole [example of a category].* Whether that uniqueness is being
> asserted about a relationship of sonship/begetting is a question the
> word's *components* do not answer by themselves — that has to come from
> context, not etymology.

**πλήρης χάριτος καὶ ἀληθείας** · adjective πλήρης ("full") + genitives χάρις
("grace, favor, kindness, a freely-given benefit; also charm, gracefulness")
and ἀλήθεια ("truth" — from ἀ- privative + the root of λανθάνω/λήθη,
"to escape notice / forgetting," so literally "un-concealment, that which is
not hidden").

> **And the Word became flesh and pitched its tent among us, and we gazed at
> its glory — glory as of a one-of-a-kind [child/one] from a father — full of
> grace/favor and truth/unconcealment.**

---

### v. 15 — (Ἰωάννης μαρτυρεῖ περὶ αὐτοῦ καὶ κέκραγεν λέγων· Οὗτος ἦν ὃν εἶπον· Ὁ ὀπίσω μου ἐρχόμενος ἔμπροσθέν μου γέγονεν, ὅτι πρῶτός μου ἦν·)

*(SBLGNT marks ⸂ ⸃ around ὃν εἶπον, flagging a variant-unit in its own
apparatus — a different manuscript tradition has a different word order or
addition here. I have not independently checked that variant on disk; it is
outside this assignment's scope, which is v. 18.)*

**κέκραγεν** · verb, κράζω, perfect active indicative — "has cried out /
cries out [and still does]" — an onomatopoeic, emphatic verb for loud, raw
crying-out (associated with a raven's or crow's cry), stronger than ordinary
"say."

**ὀπίσω / ἔμπροσθεν** · adverbs — "after, behind" / "before, in front of,
ahead of."

**γέγονεν ... ἦν** — the same ἦν/ἐγένετο (here γέγονεν, perfect) contrast
tracked since v. 1: "has come to be ahead of me" (γέγονεν, a change of
rank/position) "because he was (ἦν, unqualified prior existence) before/
first of me." The wordplay trades on the same two verb-families used
throughout.

**πρῶτος** · adjective, "first" — genuinely ambiguous between *first in time*
and *first in rank/preeminence*; both senses are live in πρῶτος and the
grammar alone does not choose.

> **(John testifies about him and has cried out, saying: "This was he of
> whom I said: 'The one coming after me has come to be ahead of me, because
> he was first/before me.'")**

---

### v. 16 — ὅτι ἐκ τοῦ πληρώματος αὐτοῦ ἡμεῖς πάντες ἐλάβομεν, καὶ χάριν ἀντὶ χάριτος·

*(SBLGNT marks ⸀ before ὅτι, meaning the editors chose this conjunction among
attested alternatives at this point — again, outside this assignment's
scope to adjudicate.)*

**πληρώματος** · noun, πλήρωμα, "fullness, that which fills, sum total" —
from πληρόω, "to fill"; cognate with πλήρης ("full") in v. 14 — a deliberate
verbal echo, "full of grace" (v.14) → "of his fullness" (v.16).

**χάριν ἀντὶ χάριτος** — worth flagging: **ἀντί** + genitive is not a vague
"upon" or "added to." Its core sense is *exchange, substitution,
correspondence* — "this in place of / instead of / corresponding to that."
Range: *instead of · in place of · in exchange for · corresponding to.*
"Grace upon grace" (a common gloss elsewhere) softens what ἀντί actually
denotes; "grace in place of grace" or "grace corresponding to grace" sit
closer to the word's actual range, though which nuance (replacement?
correspondence? accumulation?) is intended is not settled by the preposition
alone.

> **For from his fullness we all received, and grace in place of/
> corresponding to grace.**

---

### v. 17 — ὅτι ὁ νόμος διὰ Μωϋσέως ἐδόθη, ἡ χάρις καὶ ἡ ἀλήθεια διὰ Ἰησοῦ Χριστοῦ ἐγένετο.

**νόμος** · noun, "law, custom" — from νέμω, "to distribute, apportion, deal
out, allot; to pasture [flocks]." The root sense is *apportionment/allotted
custom*, extended to "law" as codified, agreed custom.

**ἐδόθη** · verb, δίδωμι, aorist passive indicative — "was given," a discrete
act of giving.

Worth noting: the law "**was given**" (ἐδόθη, passive of "give") but grace
and truth "**came to be**" (ἐγένετο) — the same verb-family used throughout
this passage for creation, the world, John's appearance, and the Word's
becoming flesh. The sentence pairs two different verbs on either side of its
μέν/δέ-less contrast, and that choice of verb is a checkable fact about the
Greek, not an inserted theological reading.

> **For the law was given through Moses; grace and truth came to be through
> Jesus Christ.**

---

### v. 18 — θεὸν οὐδεὶς ἑώρακεν πώποτε· μονογενὴς θεός (or: ὁ μονογενὴς υἱός) ὁ ὢν εἰς τὸν κόλπον τοῦ πατρὸς ἐκεῖνος ἐξηγήσατο.

**θεὸν οὐδεὶς ἑώρακεν πώποτε** — object θεόν is fronted before the subject
οὐδείς for emphasis ("**God** — no one has ever seen").

**ἑώρακεν** · verb, ὁράω, perfect active indicative — "has seen [and the
seeing stands as an abiding fact]," reinforced by **πώποτε**, "ever, at any
time" (with the negative: "never yet, at no time").

**κόλπον** · noun, κόλπος — range: *bosom, chest, breast · the fold of a
garment [where something is carried close] · a bay/inlet of the sea.* Here
the intimacy sense: the place of closest nearness — reclining at someone's
bosom at a meal, an infant held at the breast.

**ἐξηγήσατο** · verb, ἐξηγέομαι, aorist middle indicative
> ἐκ- ("out") + ἡγέομαι ("to lead, guide") — literally "led out [in words],"
> extended to *explain, interpret, narrate, expound, set forth, make known.*
> Root of English "exegesis." Note: the verb here has **no stated direct
> object** in the Greek — "he has explained/unfolded/declared [him]" supplies
> "him" from context (most naturally θεόν, back at the start of the verse),
> but strictly the object is elided/implied, not written.

#### THE VARIANT — μονογενὴς θεός vs (ὁ) μονογενὴς υἱός

I queried the manuscripts directly with `tools/cntr_read.py` rather than
relying on any edition's apparatus note. Results, verified on disk just now:

| Witness | Date | Reading at v. 18 |
|---|---|---|
| P66 | c. 200 CE | `μονογενης =θσ` — **μονογενὴς θεός** |
| P75 | c. 175–225 CE | `ο μονογενης =θσ` — **ὁ μονογενὴς θεός** |
| Sinaiticus (01) | c. 330–360 CE | `μονογενης =θσ` — **μονογενὴς θεός** |
| Vaticanus (03) | c. 300–325 CE | `μονογενης =θσ` — **μονογενὴς θεός** |
| Ephraemi Rescriptus (04) | 5th c. CE | `μονογενης =θσ` — **μονογενὴς θεός** |
| **Alexandrinus (02)** | c. 400–440 CE | `ο μονογενης υιος` — **ὁ μονογενὴς υἱός** (the outlier among these) |
| Bezae (05) | c. 400 CE | **no reading recoverable** — Bezae's Greek transcription of John stops mid-verse partway through v. 16 (see the running text pulled above); the leaf covering roughly John 1:17–3:16 is a well-documented physical lacuna in this codex, so Bezae is simply silent here, not a third reading |

`=θσ` is the manuscripts' *nomen sacrum* abbreviation for θεός (an overlined
contraction scribes used for sacred names — θεός, κύριος, Ἰησοῦς, Χριστός,
πνεῦμα — throughout the NT tradition, not something specific to this verse).

**What I actually found**: five of the six witnesses on disk that preserve
this verse — including both papyri (the two earliest witnesses to this verse
at all, P66 and P75, both around 200 CE) and two of the three great
4th/5th-century uncial codices (Sinaiticus and Vaticanus), plus Ephraemi —
read **μονογενὴς θεός**, "an only/one-of-a-kind God" or "a unique god."
Only **Alexandrinus** reads **ὁ μονογενὴς υἱός**, "the only/one-of-a-kind
Son" — the reading that also became the Byzantine majority text and, later,
the Textus Receptus/KJV tradition.

θεός is, on this evidence, both the *earlier*-attested reading (papyri
~150–200 years older than Alexandrinus) and the *harder* reading — "only
God" is the more startling, less expected phrase, where "only Son" is the
far more common Johannine phrase elsewhere (John 3:16, 3:18; 1 John 4:9)
that a copyist's habit would tend to produce by assimilation. Both of those
facts (older attestation, harder reading) are standard reasons textual
critics weight a variant as likely original — but they are reasons, not a
proof, and this project does not declare a winner where honest disagreement
exists; Alexandrinus's reading is a real, early (5th-century) manuscript
reading, not a late fabrication, even though it is outnumbered here.

**Translating both readings, in full:**

> **Reading θεός** (P66, P75, Sinaiticus, Vaticanus, Ephraemi):
> No one has ever seen God; a/the only [one]-of-its-kind God, the one being
> at/in the Father's bosom — that one has explained/unfolded [him].
>
> **Reading υἱός** (Alexandrinus; also Byzantine majority / TR):
> No one has ever seen God; the only [one]-of-its-kind Son, the one being
> at/in the Father's bosom — that one has explained/unfolded [him].

Note also: within the θεός witnesses themselves the article is not uniform —
P66, Sinaiticus, Vaticanus, and Ephraemi all read **anarthrous**
`μονογενης =θσ` (no article), while **P75** reads `ο μονογενης =θσ`, *with*
the article. Alexandrinus's υἱός reading also carries the article
(`ο μονογενης υιος`). So the article's presence/absence does not track
cleanly with the θεός/υἱός split — it is its own, separate point of
manuscript variation, and I report it rather than smooth it into a single
pattern. Only the anarthrous majority (P66/01/03/04) echoes the anarthrous
θεός construction of v. 1c structurally; P75's articular ὁ μονογενὴς θεός
does not.

---

## Summary — where the Greek itself does not settle the question

- **v. 1, λόγος**: wide semantic range (word/speech/account/reason/discourse/
  cosmic-ordering-principle); "Word" is a chosen convention, not a forced
  translation.
- **v. 1c, θεὸς ἦν ὁ λόγος**: anarthrous pre-verbal predicate. Colwell's Rule
  and its qualitative/definite/indefinite readings are all grammatically
  available; the syntax does not decide among them.
- **v. 3/4 boundary, ὃ γέγονεν**: genuine, unpunctuated-in-the-earliest-
  manuscripts ambiguity about which sentence it closes/opens.
- **v. 5, κατέλαβεν**: "overcame/overpowered" vs. "grasped/comprehended" are
  both live senses of the compound; the negated aorist does not disambiguate.
- **v. 9, ἐρχόμενον**: the inflected form is homographic between agreement
  with "man" (accusative masc.) and "the light" (neuter); word order favors
  the former, the surface form does not forbid the latter.
- **v. 14, μονογενής**: built from μόνος + γένος ("kind"), not μόνος + γεννάω
  ("beget") — "only-begotten" imports a sense the compound's own parts do
  not contain.
- **v. 18, μονογενὴς θεός vs. μονογενὴς υἱός**: checked live against six
  manuscripts. Five of six on disk (P66, P75, Sinaiticus, Vaticanus,
  Ephraemi) read θεός; Alexandrinus alone (among these) reads υἱός. Bezae
  has no reading here due to a physical lacuna. Both readings are translated
  above in full; the older/harder-reading arguments favor θεός without this
  project declaring the matter closed.

---

*Analytical data: `greek-nt/morphgnt/64-Jn-morphgnt.txt` (CC BY-SA, SBLGNT
text under the SBLGNT EULA), `greek-nt/Nestle1904/xml/`. Manuscript readings
for v. 18 pulled live with `tools/cntr_read.py {P66,P75,01,02,03,04,05} 43 1
18 18`. Regenerate with the same commands. The English is this project's own.*
