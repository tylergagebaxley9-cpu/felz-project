> [!danger] 🛑 UNVERIFIED — AGENT OUTPUT, NOT HELD TO THE STANDARD OF `enoch-6.md`
> Produced by a dispatched agent on 2026-08-16 and **not yet audited to this project's standard.**
> Do not cite from this file as settled work, and do not fold it into STUDY-BOOK.md, until the audit below is closed.
>
> **What was checked and passed:**
> - ✅ No Charles-1917 signature English anywhere — the no-English rule appears to have held
> - ✅ Reconstruction is marked; multi-sense `( | )` notation is used; ABSENT is recorded
>
> **🛑 What FAILED the check:**
> - **Ge'ez forms appear here that occur in NO chapter of the 108-chapter corpus.** Across the four agent files there are **69** such forms. Some are plausibly legitimate lexical citations (a dictionary/lemma form differs from the inflected text form), but **this repo has no Ge'ez lexicon, so lemma-citation cannot be mechanically distinguished from fabrication.**
> - By contrast `enoch-6.md`, written only from text that was on screen, scores **0** out-of-corpus forms. That is the standard this file has not met.
>
> **Why this matters here specifically:** the recorded failure mode of this project is *citing from memory while the source said otherwise* (Round 8, three errors, same fault). An out-of-corpus form is exactly that fault's signature.
>
> **To close the audit:** check each out-of-corpus form against a real Ge'ez lexicon (Dillmann's *Lexicon Linguae Aethiopicae*, 1865, is public domain and not yet in the corpus). Until then this file is evidence of work, not a result.

# 1 Enoch 1 — The Oracle of Enoch, and the Verse Jude Quotes

**Translated from the Ge'ez, against the Greek, Qumran Aramaic and Latin witnesses. No English translation consulted.**

Built with `tools/enoch.py`, which drops the Charles-1917 `translation` field bundled in the Ge'ez JSON at parse time, with no flag to re-enable it. See PROVENANCE.md.

---

## 🛑 Provenance chain — read before the text

**1 Enoch has no complete original-language text.** The chain is:

```
Aramaic (lost, ~7% survives at Qumran)
   └─> Greek (lost, ~44% survives)
          └─> Ge'ez  ← the only complete witness, from late manuscripts
```

Measured coverage of the 108 chapters: **Ethiopic 71 · Greek 48 · Qumran Aramaic 8 · Latin 3.**

⭐ **Chapter 1 is the best-attested chapter in the book.** All four traditions are present, and it is the *only* chapter where Aramaic, Greek, Ge'ez **and** Latin all speak at the same verse (1:9). Per-verse coverage in this chapter:

| Verse | Ge'ez | Greek | Aramaic | Latin |
|---|---|---|---|---|
| 1:1 | ✅ | ✅ Gizeh | ✅ 4Q201 | — |
| 1:2 | ✅ | ✅ Gizeh | ✅ 4Q201 (×3) | — |
| 1:3 | ✅ | ✅ Gizeh | ✅ 4Q201 | — |
| 1:4 | ✅ | ✅ Gizeh | ✅ 4Q201 | — |
| 1:5 | ✅ | ✅ Gizeh | ✅ 4Q201 | — |
| 1:6 | ✅ | ✅ Gizeh | ✅ 4Q201 (scrap) | — |
| 1:7 | ✅ | ✅ Gizeh | **ABSENT** | — |
| 1:8 | ✅ | ✅ Gizeh | **ABSENT** | — |
| 1:9 | ✅ | ✅ **Gizeh + Jude** | ✅ 4Q204 (×3) | ✅ **Cyprian + Vigilius** |

⚠️ These semantic ranges are **not validator-gated** — `ranges/*.json` and `verify_ranges.py` are Hebrew-only. Same limitation logged for `translations/enoch-6.md` and `translations/revelation-3.md`. Stated, not papered over.

### Witnesses cited here

| Siglum | Language | What it is |
|---|---|---|
| `p` | Ethiopic | John Rylands Library Ethiopic 23 (Knibb 1978) |
| `Bertalotto` | Ethiopic | orthographic correction of `p` — **see the caution at 1:7** |
| *(base)* | Ethiopic | the running Ge'ez text of the `ethiopian-bible` JSON — a **different** text-form from `p`, and it disagrees with `p` in this chapter |
| `Gizeh` | Greek | Cairo Papyrus 10759 · Codex Panopolitanus (Akhmim) |
| `Jude` | Greek | Jude 14–15 — **a quotation inside another book, not a copy of Enoch.** See the caveat below. |
| `4Q201` | Aramaic | 4QEnoch<sup>a</sup> ar |
| `4Q204` | Aramaic | 4QEnoch<sup>c</sup> ar |
| `Cyprian` | Latin | 1 En 1:9 *apud* Cyprian, *Ad Novatianum* 16.5 |
| `Vigilius` | Latin | 1 En 1:9 *apud* Pseudo-Vigilius |

🛑 **Flagged as modern conjecture by the tool and NOT cited here as evidence:** `Black` (supplies `[ᾧ]` at 1:2 and `[γῆς]` at 1:5), `Gizeh*` (at 1:6), `Swete Charles Black Dindorf` (at 1:8). Where the apparatus prints one of these it is an *editor's* text, not a manuscript's. Note especially that at 1:8 the **conjecture is listed first** (`option="0"`) and the actual Gizeh reading second — reading the apparatus top-down would silently invert manuscript and emendation.

> [!warning] `Jude` is a witness by editorial decision, not by nature
> The apparatus lists Jude 14–15 alongside Gizeh as a Greek "manuscript" of 1 Enoch. That is a defensible convention, but it embeds an assumption: that Jude was *copying a Greek Enoch* rather than translating Aramaic himself, or quoting from memory, or adapting. Every Jude/Gizeh divergence below is therefore ambiguous between "two Greek text-forms" and "Jude did something to the text." Nothing in the apparatus can settle which.
>
> ⚠️ **And "Jude" is edition-dependent.** The Jude text in this apparatus reads `ἐλέγξαι πάντας τοὺς ἀσεβεῖς` at v15. Checked against `greek-nt/SBLGNT/data/sblgntapp/text/Jude.txt` in this repo:
> ```
> Jude 1:15  πάντας τοὺς ἀσεβεῖς  WH Treg NIV ] + αὐτῶν RP; πᾶσαν ψυχὴν NA28
> ```
> **NA28 reads `πᾶσαν ψυχήν` — "every soul."** That lands in exactly the syntactic slot where Gizeh, the Ge'ez and the Latin all have **"all flesh."** So the single largest Jude-versus-Enoch difference identified below (§2, point 4) **exists in the WH/Treg text of Jude and dissolves in NA28.** This is stated up front because the apparatus gives no hint of it.

---

## ⭐⭐⭐ FINDING 1 — Chapter 1 is a rewriting of Deuteronomy 33:2, and only the Aramaic shows it

This is the chapter's equivalent of the Jared/Hermon puns in chapter 6: a link that exists at **root level** in the Aramaic and is destroyed by translation, in the Greek and the Ge'ez alike.

Deut 33:2, from this repo's WLC (`hebrew-ot/morphhb/wlc/Deut.xml`):

> וַיֹּאמַר יְהוָה **מִסִּינַי** בָּא וְזָרַח מִשֵּׂעִיר לָמוֹ **הוֹפִיעַ** מֵהַר פָּארָן וְאָתָה **מֵרִבְבֹת קֹדֶשׁ**

Three of its load-bearing elements reappear in 1 Enoch 1:4 and 1:9:

| Deut 33:2 | 1 Enoch, Aramaic | 1 Enoch, Greek | 1 Enoch, Ge'ez |
|---|---|---|---|
| **מִסִּינַי** (from Sinai) | *(1:4 not preserved at this word)* | `ἐπὶ τὸ Σεινὰ ὄρος` | `ዲበ፡ ሲና፡ ደብር` |
| **הוֹפִיעַ** (root **י־פ־ע**, shone forth) | **`ויופע`** (1:4) — root **י־פ־ע** ✅ **full ink** | `φανήσεται` | `ወያስተርኢ` |
| **מֵרִבְבֹת קֹדֶשׁ** (from myriads of holiness) | **`רבו]את קדישו[הי`** (1:9) — ⚠️ partly reconstructed | `μυριάσιν … ἁγίοις` / `ἁγίαις μυριάσιν` | `በትእልፊት፡ ቅዱሳን` |

⭐ **`ויופע` is the finding, and it is full surviving ink** — no bracket, no supralinear dot. The Aramaic of 1:4 uses the *same verbal root* as Deut 33:2, in the same theophany, on the same mountain. Greek `φανήσεται` and Ge'ez `ወያስተርኢ` are correct renderings of the *sense* ("he will appear") and carry **none** of the quotation. A reader of the Greek or the Ge'ez cannot tell that Deuteronomy is being cited; a reader of the Aramaic cannot miss it.

⚠️ **`רבו]את`** — of the five letters of *rîbbuʾāt*, "myriads," only **את** is on the parchment; `רבו` is editorial. The word is near-certain from the context and from `קדישו` following, but the claim must be marked. The suffix `[הי` ("his") is likewise reconstructed.

### The Ge'ez numeral is verifiable internally

`ትእልፊት` *təʾələfitə* (1:9) is not guesswork. Across this book it renders the Daniel 7:10 pair:

- 1 En 40:1 and 71:8: `አእላፈ፡ አእላፋት፡ ወትእልፊተ፡ አእላፋት`
- Dan 7:10 (WLC, `hebrew-ot/morphhb/wlc/Dan.xml`): `אֶלֶף אַלְפִין … וְרִבּוֹ רִבְבָן`

So `ትእልፊት` = `רבו` = `μυριάς`, **ten thousand**. That is measured from the corpus, not asserted from a lexicon.

🛑 **The Latin cannot carry it.** Latin has no single word for a myriad. Cyprian writes `cum multis milibus` — "with many *thousands*" — and Vigilius simply `in millibus`. The number drops by an order of magnitude in transmission because the target language lacks the unit, not because the text changed. This is a translation loss with no textual cause.

---

## ⭐⭐⭐ FINDING 2 — Jude against Gizeh at 1:9, clause by clause

The two Greek witnesses to this one verse differ in **eight** places. Neither is a copy of the other.

| # | Gizeh | Jude (WH/Treg text of the apparatus) | Ge'ez | Latin | Aramaic |
|---|---|---|---|---|---|
| 1 | `ὅτι ἔρχεται` — *because he comes* (present) | `ἰδοὺ ἦλθεν κύριος` — *behold, the Lord came* (aorist) | `ወናሁ፡ መጽአ` — *and behold, he came* (perfect) | `Ecce venit` (Cyprian) / `Ecce veniet` (Vigilius, **future**) | — |
| 2 | *subject unnamed* | **`κύριος`** | *subject unnamed* | *subject unnamed* | — |
| 3 | `σὺν ταῖς μυριάσιν αὐτοῦ **καὶ** τοῖς ἁγίοις αὐτοῦ` — **two** groups | `ἐν **ἁγίαις** μυριάσιν αὐτοῦ` — adjective + noun | `በትእልፊት፡ ቅዱሳን` — **construct**, one group | `multis milibus **nuntiorum** suorum` (Cyprian) — *messengers* | `רבו]את קדישו[הי` — **construct** ⚠️ partly reconstructed |
| 4 | `ἀπολέσει πάντας τοὺς ἀσεβεῖς` **and** `ἐλέγξει **πᾶσαν σάρκα**` | `ἐλέγξαι πάντας τοὺς ἀσεβεῖς` — one clause, **no "destroy," no "all flesh"** ⚠️ *but NA28 reads `πᾶσαν ψυχήν` here* | **both**: `ወያህጕሎሙ፡ ለረሲዓን` + `ወይትዋቀሥ፡ ኵሎ፡ ዘሥጋ` | **both**: `perdere omnes impios` + `arguere omnem carnem` | `ב]שרא` = *flesh* ⚠️ `ב` reconstructed |
| 5 | `ἀπολέσει … ἐλέγξει` — **future indicatives** | `ἐλέγξαι` — **infinitive**, parallel to `ποιῆσαι` | finite verbs | infinitives (`perdere`, `arguere`) | — |
| 6 | `περὶ πάντων ἔργων **τῆς** ἀσεβείας` | `περὶ πάντων **τῶν** ἔργων ἀσεβείας` | `በእንተ፡ ኵሉ፡ ዘገብሩ፡ ወረሰዩ` — *all that they did and wrought* | `de omnibus factis/operibus` | `על עו֗בד֗[י` = *concerning the works of* |
| 7 | `σκληρῶν ὧν ἐλάλησαν **λόγων**` **plus** `καὶ περὶ πάντων ὧν **κατελάλησαν**` — **two** speech-clauses | `περὶ πάντων τῶν σκληρῶν ὧν ἐλάλησαν` — **one** | ⭐ **no speech-clause at all** | `de omnibus verbis impiis quae **de deo** locuti sunt` (Cyprian only) | `ר֯[ב]רׄבן [וקש]יׄן` = *gr[ea]t [and har]sh things* |
| 8 | `κατ᾽ αὐτοῦ ἁμαρτωλοὶ ἀσεβεῖς` | `κατ᾽ αὐτοῦ ἁμαρτωλοὶ ἀσεβεῖς` — **identical** | `ላዕሌሁ፡ ኃጥኣን፡ ወረሲዓን` — with **"and"** inserted | ⭐ **absent from both Latin fathers** | — |

### What the table shows

**⭐ `κύριος` is Jude's alone.** Verified by NFD-normalised search across every Greek reading in the chapter: `κυρι-` occurs **once**, in Jude. Gizeh, the Ge'ez, and *both* Latin fathers leave the subject of the theophany unnamed. Jude supplies the divine name that the Enoch tradition, in every other witness, withholds.

**⭐⭐ The tense spread is what a Semitic prophetic perfect produces.** Deut 33:2 has `בָּא` and `אָתָה` — suffix conjugation, past form, future sense. Downstream we get, from the same underlying form: Ge'ez perfect `መጽአ`, Jude aorist `ἦλθεν`, Gizeh present `ἔρχεται`, Vigilius future `veniet`, Cyprian `venit` — which in Latin is **orthographically ambiguous between present and perfect** and cannot be assigned. Four tenses and one undecidable, from one Semitic form. No witness is "wrong"; the category does not survive translation.

**⭐⭐ On the "myriads" clause, Jude looks *closer* to the Semitic than Gizeh does.** A construct chain `רבואת קדישוהי` ("myriads of his holy ones") has two normal Greek renderings: a genitive noun, or an attributive adjective. Jude's `ἐν ἁγίαις μυριάσιν αὐτοῦ` is the adjectival rendering. Gizeh's `σὺν ταῖς μυριάσιν αὐτοῦ **καὶ** τοῖς ἁγίοις αὐτοῦ` splits the chain into **two coordinated groups** — which is what happens when a construct chain is misparsed, not what happens when a different text is copied. The Ge'ez `በትእልፊት፡ ቅዱሳን` and the Aramaic both keep one group. **Three witnesses to one group, Gizeh alone to two.**
> ⚠️ The Aramaic here is `רבו]את קדישו[הי` — the head noun is 3/5 reconstructed. Stated as reconstruction, not as ink.

**⭐⭐⭐ The Ge'ez has lost the speech-offence entirely.** Row 7 is the most consequential Ethiopic loss in the chapter. Gizeh, Jude, Cyprian and 4Q204 all preserve a charge about *what the wicked said*. The Ge'ez has only `ዘገብሩ፡ ወረሰዩ` — "what they **did** and **wrought**." Two verbs of action, none of speech. The only complete text of 1 Enoch has dropped half the indictment.

**⭐ And the Aramaic preserves an adjective nobody else has.** `ר֯[ב]רׄבן` — *rabrabin*, "great / haughty / insolent (things)" — is **4 of 5 letters in ink**. No Greek, Ge'ez or Latin witness has any counterpart to it. Greek has only `σκληρῶν`.

> 🛑 **The circularity that must be flagged.** The apparatus reconstructs `[וקש]יׄן` — the word that would match `σκληρῶν` — from **two surviving letters**, `ין`. The reconstruction is almost certainly *driven by* the Greek. It therefore **cannot be turned around and cited as Aramaic confirmation of the Greek.** The honest statement is: the Aramaic ink supports an adjective the Greek lacks (`רברבן`), and the adjective the Greek has is supplied by editors.

**⭐ The Latin fathers both stop short of the closing subject.** `ἁμαρτωλοὶ ἀσεβεῖς` — the "sinners, ungodly ones" who are the grammatical subject of the whole final clause — is present in Gizeh and Jude *identically*, in the Ge'ez with a conjunction added, and in **neither** Latin quotation. Cyprian instead ends `quae de deo locuti sunt` — "which they spoke **about God**," naming God where every Greek witness has only `κατ᾽ αὐτοῦ`, "against him."

---

## ⭐⭐ FINDING 3 — Where the Ethiopic manuscript beats the Ethiopic base text

The `ethiopian-bible` running text and ms `p` are **not the same text-form**, and in this chapter `p` twice preserves the reading the older versions support:

| Verse | Base text | ms `p` / `Bertalotto` | Greek | Aramaic | Verdict |
|---|---|---|---|---|---|
| 1:1 | `ኵሉ` (non-accusative) | **`ኵሎ`** (accusative) | `πάντας` (accusative) | — | ⭐ `p` is grammatically right and matches the Greek |
| 1:5 | `አጽናፈ፡ **ዓለም**` — ends of the **world / age** | **`አጽናፈ፡ ምድር`** — ends of the **earth** | `τῶν περάτων τῆς **γῆς**` | **`ארעה`** = *the earth*, ✅ **full ink** | ⭐⭐ `p` agrees with **both** older versions against the base text |

⭐ The 1:5 case is the stronger one: `ארעה` is undamaged, unbracketed Aramaic. Three witnesses read "earth"; the base Ge'ez alone reads "world/age."

---

## What the brackets and dots actually mean

The Aramaic in this file carries **three tiers of certainty**, and they are not interchangeable:

| Notation | Meaning |
|---|---|
| plain letter | **ink on the parchment** |
| letter with supralinear dot (`א֯`, `אׄ`) | **uncertain reading** — something is there; which letter is disputed |
| `[ בְּסוֹגְרַיִם ]` | **editorial reconstruction — nothing is there** |

The complete ink/reconstruction ledger for every Aramaic scrap in chapter 1, parsed programmatically from the XML rather than read off the page:

| Verse | ms | Surviving ink | Reconstructed |
|---|---|---|---|
| 1:1 | 4Q201 | `חנך לבח֯` | `ירין` |
| 1:2a | 4Q201 | `מתלוה` · `מר` | `י וא` |
| 1:2b | 4Q201 | `ומ֯ןׄ מ֯ל֯י֯` · `וקדׄישין כלה` | **`עירין`** (= "Watchers" — 🛑 **entirely editorial**) · `ון` |
| 1:2c | 4Q201 | `ן דׄרה להן לד֯` · `ח֯יק אׄנה אׄמ` | `להד` · `ר ר` · `לל` |
| 1:3 | 4Q201 | `ינ֯פק קדיש` · `בה מן` | `ה ר` |
| 1:4 | 4Q201 | `בׄה **ויופע** ב` · `גבור` | `ר` · `תקף` · `תה` |
| 1:5 | 4Q201 | **`אר֯עׄה֯ ו`** · `ל קצו` | `קצות` · **`יזועון כ`** (the verb — 🛑 **entirely editorial**) · `ת` |
| 1:6 | 4Q201 | `רמן וי` | — |
| 1:9a | 4Q204 | `את קדישו` | `רבו` · `הי` |
| 1:9b | 4Q204 | `שרא על עו֗בד֗` | `ב` · `י` |
| 1:9c | 4Q204 | `ר֯` · `רׄבן` · `יׄן` | `ב` · **`וקש`** |

🛑 **Two claims that people build arguments on are 100% reconstruction here:**
1. **`[עירין]` — "Watchers" — at 1:2.** Not one letter of it survives in 4Q201. Anyone citing the Aramaic of 1:2 for the Watchers is citing an editor.
2. **`[יזועון]` — "they shall quake" — at 1:5.** Also entirely supplied. The Aramaic therefore **cannot arbitrate** the large Ge'ez/Greek disagreement at 1:5 (see the verse note).

---

## THE TEXT

> Where the witnesses genuinely differ, all readings are given and none is preferred.
> `( | )` marks a word whose Ge'ez carries more than one sense.

### 1:1

**ቃለ፡ በረከት፡ ዘሄኖክ፡ በከመ፡ ባረከ፡ ኅሩያነ፡ ወጻድቃነ፡ እለ፡ ሀለዉ፡ ይኩኑ፡ በዕለተ፡ ምንዳቤ፡ ለአሰስሎ፡ ኵሉ፡ እኩያን፡ ወረሲዓን።**

*qalä bäräkätə zähenokə bäkämä baräkä ḫəruyanä wäṣadəqanä ʾəlä häläwu yəkunu bäʿəlätä mənədabe läʾäsäsəlo kwəlu ʾəkuyanə wäräsiʿanə*

**The (word | speech | voice) of blessing of Ḥenok, wherewith he blessed the (chosen | elect) and the righteous who are to be in the day of (tribulation | distress | constraint), for the (removing | wiping away | sweeping off | extirpation) of all the (evil | wicked) and the (ungodly | impious).**

- `ቃለ` *qalä* — **voice / word / utterance**. Ge'ez does not separate the sound from the saying.
- `ለአሰስሎ` — infinitive of a verb of **sweeping away, wiping out, removing**. Greek `ἐξᾶραι` is the same act.
- ⭐ Ge'ez has **two** nouns joined by `ወ` — `እኩያን፡ ወረሲዓን`, "the evil **and** the ungodly." Greek has **one**, and it is a different word: `τοὺς ἐχθρούς`, **the enemies**. Neither is preferred here; they are simply different objects.

**Witnesses:**
- Ge'ez `p`/`Bertalotto`: `ዘሄኖከ` (final vowel) · `ዘከመ` for `በከመ` · ⭐ **`ኵሎ` for `ኵሉ`** — the accusative, agreeing with Greek `πάντας`.
- Greek `Gizeh`: `Λόγος εὐλογίας Ἑνώχ, καθὼς εὐλόγησεν ἐκλεκτοὺς δικαίους οἵτινες ἔσονται εἰς ἡμέραν ἀνάγκης ἐξᾶραι πάντας τοὺς ἐχθρούς, **καὶ σωθήσονται δίκαιοι**.`
  - ⭐⭐ **The final clause — "and the righteous shall be saved" — has no counterpart in the Ge'ez.** A whole promise, present in the Greek and absent from the only complete text.
  - Greek `ἐκλεκτοὺς δικαίους` is **asyndetic** (one phrase, "elect righteous ones"); Ge'ez inserts `ወ` and makes it two groups. This is a **pattern** in this chapter — see 1:3 and 1:9 — and it changes how many parties the text is talking about.
- Aramaic `4Q201`: ink `חנך לבח֯`, reconstructed `[ירין`. So: *Ḥenok, for the ch[osen…* — the preposition `ל` is on the parchment, where Greek and Ge'ez both have a direct object. ⚠️ "chosen" rests on three reconstructed letters.
- Latin **ABSENT** — version exists, does not attest this verse.

### 1:2

**ወአውሥአ፡ ሄኖክ፡ ወይቤ፡ ብእሲ፡ ጻድቅ፡ ዘእምኀበ፡ እግዚአብሔር፡ እንዘ፡ አዕይንቲሁ፡ ክሡታት፡ ወይሬኢ፡ ራእየ፡ ቅዱስ፡ ዘበሰማያት፡ ዘአርአዩኒ፡ መላእክት፡ ወሰማዕኩ፡ ዘእምኀቤሆሙ፡ ኵሎ፡ ወአእመርኩ፡ አነ፡ ዘእሬኢ፡ ወአኮ፡ ለዝ፡ ትውልድ፡ አላ፡ ለዘይመጽኡ፡ ትውልድ፡ ርሑቃን።**

*wäʾäwəśəʾä henokə wäyəbe bəʾəsi ṣadəqə zäʾəməḫäbä ʾəgəziʾäbəḥerə ʾənəzä ʾäʿəyənətihu kəśutatə wäyəreʾi raʾəyä qədusə zäbäsämayatə zäʾärəʾäyuni mälaʾəkətə wäsämaʿəku zäʾəməḫäbehomu kwəlo wäʾäʾəmärəku ʾänä zäʾəreʾi wäʾäko läzə təwələdə ʾäla läzäyəmäṣəʾu təwələdə rəḥuqanə*

**And Ḥenok (answered | responded | took up his answer) and said: A righteous man, one who is from ʾƎgziʾabḥer (the Lord God), while his eyes were opened, and he sees a vision of the Holy One which is in the heavens, which the (angels | messengers) showed me — and I heard from them everything, and I myself knew what I see; and not for this generation, but for a generation that is coming, (far off | distant).**

- `ወአውሥአ` — **to answer, respond**. But see the Greek: it renders `ἀναλαβὼν τὴν παραβολὴν αὐτοῦ`, "taking up his parable." The Ge'ez keeps the verb and **loses the object**.
- ⭐ The Semitic idiom underneath is `נשא משל`, "to lift up an oracle" — the Balaam formula. The Aramaic has it: `מתלוה[י` = **his parables**.
- `ርሑቃን` *rəḥuqanə* — ⭐ **cognate with the Aramaic `רחיק` of the same verse.** Root **r-ḥ-q** survives intact from Aramaic to Ge'ez *through* a Greek (`πόρρω`) that shares nothing with it. A rare case of the chain preserving the root by accident.
- `እግዚአብሔር` — ⭐ the **only** occurrence of this divine title in the chapter. 1:4 and 1:8 use `አምላክ` instead. The Ge'ez varies its word for God where the Greek uses `θεός` throughout.

**Witnesses:**
- Ge'ez `p`: `ራዕየ` / `Bertalotto`: `ራእየ` — orthographic. ⭐ But both read **`ቅዱሰ`** where the base text has **`ቅዱስ`** — an accusative, i.e. *"a holy vision"* rather than *"a vision of the Holy One."* Greek `τοῦ ἁγίου` (genitive) supports the base text. **Both readings given; neither preferred.**
- Ge'ez `p`/`Bertalotto` also lack the relative `ዘ` before `እምኀቤሆሙ`, and split `ለዘ፡ ይመጽኡ`.
- Greek `Gizeh`: `Καὶ ἀναλαβὼν τὴν παραβολὴν αὐτοῦ εἶπεν Ἑνώχ· Ἄνθρωπος δίκαιός ἐστιν, [lacuna] ὅρασις ἐκ τοῦ θεοῦ αὐτῷ ἀνεῳγμένη ἦν· ἔχων τὴν ὅρασιν τοῦ ἁγίου καὶ τοῦ οὐρανοῦ. ἔδειξέν μοι, καὶ ἁγιολόγων ἁγίων ἤκουσα ἐγώ, καὶ ὡς ἤκουσα παρ᾽ αὐτῶν πάντα καὶ ἔγνων ἐγὼ θεωρῶν· καὶ οὐκ εἰς τὴν νῦν γενεὰν διενοούμην, ἀλλὰ ἐπὶ πόρρω οὖσαν ἐγὼ λαλῶ.`
  - 🛑 The lacuna is filled by **conjecture only** — `[ᾧ]` (`Black`). Without it Gizeh is asyndetic. Not cited as evidence.
  - ⭐ **What was opened differs.** Ge'ez: *his eyes* (`አዕይንቲሁ፡ ክሡታት`). Greek: *a vision* (`ὅρασις … ἀνεῳγμένη ἦν`). Same verb, different subject.
  - ⭐ **Where "from God" attaches differs.** Ge'ez binds `ዘእምኀበ፡ እግዚአብሔር` to **the man**; Greek binds `ἐκ τοῦ θεοῦ` to **the vision**.
  - Greek `ἔδειξέν μοι` is **3rd singular with no subject**; Ge'ez `ዘአርአዩኒ፡ መላእክት` names **the angels**, plural.
  - Greek `ἁγιολόγων ἁγίων` — "of holy ones speaking holy things," `ἅγιος` doubled. The Aramaic has two **distinct** classes at this point (see below).
  - ⭐ Ge'ez ends without a verb; Greek `ἐγὼ λαλῶ` and Aramaic `אׄמ[לל` both have **"I speak."** The Ge'ez lost the main verb of the sentence.
- Aramaic `4Q201`, three units:
  - `…]מתלוה[י וא]מר […` — ink `מתלוה` + `מר`: *his parable[s, and he s]aid.*
  - `…]ומ֯ןׄ מ֯ל֯י֯ [עירין] וקדׄישין כלה[ון …` — *and from the words of [Watchers] and Holy Ones, all of th[em].* 🛑 **`[עירין]` is 100% reconstruction.** Ink gives only "and from the words of … and holy ones, all of th[em]."
  - `…להד]ן דׄרה להן לד֯[ר ר]ח֯יק אׄנה אׄמ[לל …` — *for th[is] generation, but for a fa[r] gene[ration] I sp[eak].*
- Latin **ABSENT**.

### 1:3

**በእንተ፡ ኅሩያን፡ እቤ፡ ወአውሣእኩ፡ በእንቲኣሆሙ፡ ምስለ፡ ዘይወፅእ፡ ቅዱስ፡ ወዐቢይ፡ እማኅደሩ።**

*bäʾənətä ḫəruyanə ʾəbe wäʾäwəśaʾəku bäʾənətiʾahomu məsələ zäyəwäṣ́əʾə qədusə wäʿäbiyə ʾəmaḫədäru*

**Concerning the (chosen | elect) I spoke, and I (took up | answered) concerning them — with him who goes forth, the Holy One and the Great One, from his (dwelling | habitation | abode).**

- `ወአውሣእኩ` — the same root as `ወአውሥአ` in 1:2, and again **the object is missing**: Greek supplies `τὴν παραβολήν μου`, "my parable."
- `እማኅደሩ` — from `ማኅደር`, **dwelling / lodging / abode**.

**Witnesses:**
- Ge'ez `p`/`Bertalotto`: `በእንቲአሆሙ` · `ዘይወጽእ` · `p` `ወዓቢይ` / `Bertalotto` `ወዐቢይ` — orthographic.
- Greek `Gizeh`: `Καὶ περὶ τῶν ἐκλεκτῶν νῦν λέγω καὶ περὶ αὐτῶν ἀνέλαβον τὴν παραβολήν μου. καὶ ἐξελεύσεται ὁ ἅγιός **μου** ὁ μέγας ἐκ τῆς κατοικήσεως αὐτοῦ,`
- Aramaic `4Q201`: `…] ינ֯פק קדיש[ה ר]בה מן […` — ink `ינפק קדיש` + `בה מן`. The verb `נפק` ("go out") = Greek `ἐξελεύσεται` = Ge'ez `ይወፅእ`; all three agree.
- ⭐⭐ **Three witnesses, three different titles:**

| Witness | Reading | Structure |
|---|---|---|
| Aramaic | `קדיש[ה ר]בה` | *the Great Holy One* — one title, no possessive |
| Greek | `ὁ ἅγιός **μου** ὁ μέγας` | ***my** Great Holy One* — adds a possessive |
| Ge'ez | `ቅዱስ፡ **ወ**ዐቢይ` | *the Holy One **and** the Great One* — adds a conjunction, splitting one title into two |

  ⚠️ The Aramaic `[ה ר]` is reconstructed; `קדיש` and `בה` are ink. **The `μου` is Greek-only; the `ወ` is Ge'ez-only.** Neither is preferred; both are recorded as additions their own witness alone carries.
- Latin **ABSENT**.

### 1:4

**ወአምላከ፡ ዓለም፡ ወእምህየ፡ ይከይድ፡ ዲበ፡ ሲና፡ ደብር፡ ወያስተርኢ፡ በትዕይንቱ፡ ወያስተርኢ፡ በጽንዐ፡ ኀይሉ፡ እምሰማይ።**

*wäʾäməlakä ʿalämə wäʾəməhəyä yəkäyədə dibä sina däbərə wäyasətärəʾi bätəʿəyənətu wäyasətärəʾi bäṣənəʿä ḫäyəlu ʾəməsämayə*

**And the God of the (world | age | eternity) — and from there he shall (tread | trample | set foot) upon Sinai the mountain, and he shall appear (in | with | by) his (camp | encampment | host), and he shall appear in the (strength | firmness) of his (might | power | army) from heaven.**

- `ትዕይንት` — **camp / encampment / host**, and a **hapax in this book**. Greek `παρεμβολή` covers the same ground: an army's camp, and the army in it.
- `ኀይል` — **power / might**, and also **an armed force**. Both senses are live in a theophany with a host.

**Witnesses:**
- Ge'ez `p`: `በጽንዓ` · `ኃይሉ` / `Bertalotto`: `በጽንዐ` · `ኀይሉ` — orthographic.
- Greek `Gizeh`: `καὶ ὁ θεὸς τοῦ αἰῶνος **ἐπὶ γῆν** πατῆσει ἐπὶ τὸ Σεινὰ ὄρος καὶ φανήσεται **ἐκ** τῆς παρεμβολῆς αὐτοῦ, καὶ φανήσεται ἐν τῇ δυνάμει τῆς ἰσχύος αὐτοῦ **ἀπὸ τοῦ οὐρανοῦ τῶν οὐρανῶν**.`
  - ⭐ Greek `ἐπὶ γῆν` ("upon the earth") stands where Ge'ez has `ወእምህየ` ("and from there"). Different words, not a variant spelling.
  - ⭐ Preposition reversed: Greek `**ἐκ** τῆς παρεμβολῆς` — *out of* his camp; Ge'ez `**በ**ትዕይንቱ` — *in / with* his camp.
  - ⭐ Greek `ἀπὸ τοῦ οὐρανοῦ **τῶν οὐρανῶν**` — *the heaven **of heavens***; Ge'ez `እምሰማይ` — plain **"from heaven."**
- Aramaic `4Q201`: `…ר]בׄה **ויופע** ב[תקף] גבור[תה …` — ink: `בׄה ויופע ב` and `גבור`. ⭐⭐ **`ויופע` is full ink and is the Deut 33:2 verb** — see Finding 1. `[תקף]` ("strength") and the suffix `[תה]` are reconstruction.
- Latin **ABSENT**.

### 1:5

**ወይፈርሁ፡ ኵሉ፡ ወያድለቀልቁ፡ ትጉሃን፡ ወይነሥኦሙ፡ ፍርሀት፡ ወረዓድ፡ ዐቢይ፡ እስከ፡ አጽናፈ፡ ዓለም።**

*wäyəfärəhu kwəlu wäyadəläqäləqu təguhanə wäyənäśəʾomu fərəhätə wäräʿadə ʿäbiyə ʾəsəkä ʾäṣənafä ʿalämə*

**And all shall fear, and the (Watchers | Wakeful Ones) shall (quake | shake | be convulsed), and fear and great trembling shall (seize | take hold of) them, unto the ends of the (world | age) — [ms `p`: **the earth**].**

- `ትጉሃን` *təguhanə* — ⭐ **the Watchers.** This is not an assumption imported from elsewhere: within this book the same root appears as a verb at 20:1, `እለ፡ ይተግሁ፡ ቅዱሳን፡ መላእክት` ("the holy angels **who keep watch / are wakeful**"), and at 100:8 of humans, `እለ፡ ትተግሁ፡ ከመ፡ ትለብውዎ፡ ለእኩይ` ("you who **stay awake** to devise evil"). The noun is the standing term at 10:7, 10:9, 10:15, 12:2, 12:3, 14:1, 14:3, 15:9, 16:1, 16:2, 91:15. **The base sense is wakefulness, not surveillance.**
- `ወያድለቀልቁ` — **to quake, shake, be convulsed**. Confirmed internally at 60:1: `ታድለቀልቅ፡ ሰማየ፡ ሰማያት፡ ድልቅልቀ፡ ዐቢይ` — "the heaven of heavens shook with a great shaking."

**Witnesses:**
- Ge'ez `Bertalotto` `ወይፈርሁ` / `p` `ወይፈርህ` (singular) · both `ወይነሥአሙ`, `ፍርሃት` · `Bertalotto` `ዐቢይ` / `p` `ዓቢይ` · ⭐⭐ **both read `አጽናፈ፡ ምድር` — "ends of the EARTH" — against the base text's `ዓለም`.** See Finding 3.
- Greek `Gizeh`: `καὶ φοβηθήσονται πάντες καὶ **πιστεύσουσιν** οἱ **ἐγρήγοροι**, καὶ **ᾄσουσιν ἀπόκρυφα** ἐν πᾶσιν τοῖς ἄκροις τῆς [lacuna] · καὶ σεισθήσονται πάντα τὰ ἄκρα τῆς γῆς, καὶ λήμψεται αὐτοὺς τρόμος καὶ φόβος μέγας μέχρι τῶν περάτων τῆς γῆς.`
  - 🛑 The lacuna is filled by **conjecture only** — `[γῆς]` (`Black`).
  - ⭐⭐ **The Watchers agree; their verb does not.** `ἐγρήγοροι` = `ትጉሃν` exactly — both mean *the wakeful ones*, and this is the one place in chapter 1 where the Greek and Ge'ez independently name them. But Gizeh says they **believe** (`πιστεύσουσιν`) and the Ge'ez says they **quake**. Gizeh then adds `καὶ ᾄσουσιν ἀπόκρυφα` — *"and they shall sing/chant hidden things"* — which the Ge'ez does not have in any form. **All readings stand; no harmonisation is offered.**
  - ⭐ **Three "ends of the earth" in Greek, two in Aramaic, one in Ge'ez.** Gizeh: `ἐν πᾶσιν τοῖς ἄκροις τῆς [γῆς]` … `πάντα τὰ ἄκρα τῆς γῆς` … `μέχρι τῶν περάτων τῆς γῆς`. Ge'ez keeps only the third (`እስከ` = `μέχρι`) and drops the first two. That compression is also where the Ge'ez's quaking verb ends up attached to the Watchers rather than to the ends of the earth — **an inference about mechanism, marked as such, not a reading.**
  - ⭐ Word order inverted: Ge'ez `ፍርሀት፡ ወረዓድ` (fear then trembling); Greek `τρόμος καὶ φόβος` (trembling then fear).
- Aramaic `4Q201`: `…קצות] אר֯עׄה֯ ו[יזועון כ]ל קצו[ת …` — ink `אר֯עׄה֯ ו` and `ל קצו`. 🛑 **The verb `[יזועון]` is entirely reconstructed**, so the Aramaic **cannot decide** between "quake" and "believe". What it *does* give, in ink, is `ארעה` — **the earth** — which is Finding 3's decisive letter.
- Latin **ABSENT**.

### 1:6

**ወይደነግፁ፡ አድባር፡ ነዋኃን፡ ወይቴሐቱ፡ አውግር፡ ነዊኃን፡ ወይትመሰዉ፡ ከመ፡ መዓረ፡ ግራ፡ እምላህብ።**

*wäyədänägəṣ́u ʾädəbarə näwaḫanə wäyəteḥätu ʾäwəgərə näwiḫanə wäyətəmäsäwu kämä mäʿarä gəra ʾəməlahəbə*

**And the high mountains shall be (terrified | startled | shaken), and the high hills shall be (brought low | humbled), and they shall (melt | dissolve | vanish away) like beeswax before the flame.**

- `መዓረ፡ ግራ` — literally *honey of the comb*, i.e. **beeswax**. Verified twice over: internally at 52:6, `ይከውኑ፡ ከመ፡ መዓረ፡ ግራ፡ ዘቅድመ፡ ገጸ፡ እሳት` — the identical idiom in the identical image; and externally by Greek `κηρός`, wax.
- `ወይደነግፁ` — the root is **alarm / terror**, not simply motion; Greek `σεισθήσονται` is physical shaking. Both senses printed.

**Witnesses:**
- Ge'ez `p`/`Bertalotto` read `ነዋኃት` for the second `ነዊኃን` — gender/number of the adjective for "high."
- Greek `Gizeh`: `καὶ **σεισθήσονται καὶ πεσοῦνται καὶ διαλυθήσονται** ὄρη ὑψηλά, καὶ ταπεινωθήσονται βουνοὶ ὑψηλοὶ **τοῦ διαρυῆναι ὄρη**, καὶ τακήσονται ὡς κηρὸς **ἀπὸ προσώπου πυρὸς** ἐν φλογί.`
  - ⭐ **Three verbs in Greek for the mountains** (shaken, fall, dissolve) where the Ge'ez has **one**.
  - ⭐ Greek `τοῦ διαρυῆναι ὄρη` — "so that the mountains flow away" — has **no Ge'ez counterpart**.
  - ⭐ Greek `ἀπὸ προσώπου πυρὸς ἐν φλογί` — "from the **face** of **fire** in **flame**" (three elements); Ge'ez `እምላህብ` — "from the flame" (one). The Semitic idiom `מפני` ("from the face of") survives in the Greek and is gone from the Ge'ez.
- Greek 🛑 `Gizeh*` `πεινωθησονται` — **flagged as conjecture by the tool and not cited as evidence.** ⚠️ Honest note: `Gizeh*` is **not defined in the apparatus's manuscript list** (which has only `Gizeh` and `Gizeh2`). I could not determine from the data whether the asterisk means "first hand of the papyrus" or an editorial note. **Because I cannot determine it, I do not use it.**
- Aramaic `4Q201`: `…]רמן וי[…` — ink `רמן וי`, a scrap. `רמן` = **high / lofty** (fem. pl.), matching the adjective on the mountains or hills; the following `וי` is the head of a lost verb. Too little to align to a clause.
- Latin **ABSENT**.

### 1:7

**ወትሰጠም፡ ምድር፡ ወኵሉ፡ ዘውስተ፡ ምድር፡ ይትሀጐል፡ ወይከውን፡ ፍትሕ፡ ላዕለ፡ ኵሉ፡ ወላዕለ፡ ጻድቃን፡ ኵሎሙ።**

*wätəsäṭämə mədərə wäkwəlu zäwəsətä mədərə yətəhägwälə wäyəkäwənə fətəḥə laʿəlä kwəlu wälaʿəlä ṣadəqanə kwəlomu*

**And the earth shall be (submerged | swallowed up | sunk) — [ms `Bertalotto`: **split apart / torn open**] — and everything that is in the earth shall (perish | be destroyed), and there shall be (judgement | justice | a verdict) upon all, and upon all the righteous.**

- `ፍትሕ` — **judgement / justice / legal decision**. The forensic sense is primary; this is a courtroom word, and it governs the whole close of the chapter.

**Witnesses:**
- ⭐⭐ **A lexical split inside the Ethiopic:** `p` (and the base text) read `ወትሰጠም` — *be submerged / swallowed up*; `Bertalotto` reads `ወትሠጠጥ` — *be split / torn apart*. Greek `διασχισθήσεται ἡ γῆ σχίσμα ῥαγάδι` — *"the earth shall be split with a splitting, a rent"* — supports **split**.
  > ⚠️ **Caution that must be stated.** `Bertalotto` is described in the apparatus as *"correction of orthographic tendencies in ms p."* `ሰጠመ` and `ሠጠጠ` differ in their final radical (`ም` vs `ጥ`) — that is **not orthography, it is a different word**. Either the siglum's description understates what Bertalotto does, or this entry is doing something the apparatus does not explain. **I could not determine which from the data available.** Both readings are printed; neither is preferred.
- Greek `Gizeh`: `καὶ διασχισθήσεται ἡ γῆ σχίσμα ῥαγάδι, καὶ πάντα ὅσα ἐστὶν ἐπὶ τῆς γῆς ἀπολεῖται, καὶ κρίσις ἔσται κατὰ πάντων.`
  - ⭐ Greek `σχίσμα ῥαγάδι` is a **cognate-accusative-plus-instrumental** doubling — "split with a split, by a rent." That is a Semitic intensifying construction showing through the Greek. The Ge'ez has no doubling.
  - ⭐ **Greek stops at `κατὰ πάντων`.** The Ge'ez continues `ወላዕለ፡ ጻድቃን፡ ኵሎሙ` — "**and upon all the righteous**." A judgement clause aimed at the righteous, present only in the Ethiopic.
  - ⚠️ **Verse-division disagreement:** the base Ge'ez text puts `ወላዕለ፡ ጻድቃን፡ ኵሎሙ` at the **end of 1:7**; the Ethiopic apparatus (`p`/`Bertalotto`) puts the identical words at the **start of 1:8**. Same text, different verse.
- Aramaic **ABSENT** — version exists, does not attest this verse.
- Latin **ABSENT**.

### 1:8

**ለጻድቃንሰ፡ ሰላመ፡ ይገብር፡ ሎሙ፡ ወየዐቅቦሙ፡ ለኅሩያን፡ ወይከውን፡ ሣህል፡ ላዕሌሆሙ፡ ወይከውኑ፡ ኵሎሙ፡ ዘአምላክ፡ ወይሤርሑ፡ ወይትባረኩ፡ ወይበርህ፡ ሎሙ፡ ብርሃነ፡ አምላክ።**

*läṣadəqanəsä sälamä yəgäbərə lomu wäyäʿäqəbomu läḫəruyanə wäyəkäwənə śahələ laʿəlehomu wäyəkäwənu kwəlomu zäʾäməlakə wäyəśerəḥu wäyətəbaräku wäyəbärəhə lomu bərəhanä ʾäməlakə*

**But for the righteous — he will make peace for them, and he will (guard | keep | protect) the (chosen | elect), and (mercy | compassion | grace) shall be upon them, and they shall all be God's, and they shall (prosper | fare well | be favoured) and be blessed, and the light of God shall shine for them.**

- `ወይሤርሑ` — a **hapax in this book**. The Greek parallel is `τὴν εὐδοκίαν δώσει αὐτοῖς`, "he shall give them (good pleasure | favour)," which supports the range *prosper / fare well / be well-pleased*. Given as multiple senses because the Greek is itself a paraphrase and cannot pin the Ge'ez.
- `ሣህል` — **mercy / clemency / forbearance**.

**Witnesses:**
- Ge'ez `p`/`Bertalotto` open with `ወላዕለ፡ ጻድቃን፡ ኵሎሙ` (see the verse-division note at 1:7) · `Bertalotto` `ወየዐቅቦሙ` / `p` `ወየዓቅቦሙ` · both end `ብርሃነ፡ አምላከ` (final vowel).
- Greek `Gizeh`: `καὶ μετὰ τῶν δικαίων τὴν εἰρήνην ποιήσει, καὶ ἐπὶ τοὺς ἐκλεκτοὺς ἔσται συντήρησις **καὶ εἰρήνη**, καὶ ἐπ᾽ αὐτοὺς **γενηται** ἔλεος, καὶ ἔσονται πάντες τοῦ θεοῦ, καὶ τὴν εὐδοκίαν δώσει αὐτοῖς καὶ πάντας εὐλογήσει καὶ πάντων ἀντιλήμψεται καὶ **βοηθήσει ἡμῖν**, καὶ φανήσεται αὐτοῖς φῶς **καὶ ποιήσει ἐπ᾽ αὐτοὺς εἰρήνην**.`
  - 🛑 **`γενήσεται` is a CONJECTURE** (`Swete Charles Black Dindorf`). **The manuscript reads `γενηται`.** Note that the apparatus lists the conjecture as `option="0"` and Gizeh as `option="1"` — the emendation is printed *first*. The manuscript reading is the subjunctive/unaugmented form; the editors regularise it to a future. **The manuscript form is what is printed above.**
  - ⭐ Ge'ez `ወመተ` — no: Ge'ez has a **verb**, `ወየዐቅቦሙ` ("he will guard them"), where Greek has a **noun**, `συντήρησις` ("preservation"). Greek then adds a second `καὶ εἰρήνη` that the Ge'ez lacks.
  - ⭐⭐ **`βοηθήσει ἡμῖν` — "and he shall help US."** A **first person plural** in the middle of a third-person oracle. No other witness has it: the Ge'ez has `ወይሤርሑ፡ ወይትባረኩ` ("they shall prosper and be blessed"), third plural throughout. Flagged, not explained — I cannot determine whether this is a Greek corruption, a liturgical intrusion, or an original feature.
  - ⭐ Ge'ez names **whose** light: `ብርሃነ፡ አምላክ`, "the light **of God**." Greek has bare `φῶς`. Conversely Greek closes `καὶ ποιήσει ἐπ᾽ αὐτοὺς εἰρήνην` ("and he shall make peace upon them"), which the Ge'ez lacks. **Each version has something the other does not, in the same clause.**
- Aramaic **ABSENT**.
- Latin **ABSENT**.

### 1:9 — the verse Jude quotes

**ወናሁ፡ መጽአ፡ በትእልፊት፡ ቅዱሳን፡ ከመ፡ ይግበር፡ ፍትሐ፡ ላዕሌሆሙ፡ ወያህጕሎሙ፡ ለረሲዓን፡ ወይትዋቀሥ፡ ኵሎ፡ ዘሥጋ፡ በእንተ፡ ኵሉ፡ ዘገብሩ፡ ወረሰዩ፡ ላዕሌሁ፡ ኃጥኣን፡ ወረሲዓን።**

*wänahu mäṣəʾä bätəʾələfitə qədusanə kämä yəgəbärə fətəḥä laʿəlehomu wäyahəgwəlomu läräsiʿanə wäyətəwaqäśə kwəlo zäśəga bäʾənətä kwəlu zägäbəru wäräsäyu laʿəlehu ḫaṭəʾanə wäräsiʿanə*

**And behold, he (came | has come) with myriads of holy ones, to (execute judgement | render a verdict) upon them; and he shall destroy the (ungodly | impious), and shall (contend at law with | bring a charge against | convict) all flesh concerning everything that the sinners and the ungodly have done and wrought against him.**

- `ናሁ` — the presentative particle, **behold**. Matches `ἰδού` (Jude) and `Ecce` (both Latin); Gizeh alone has `ὅτι` instead, which makes v9 a *causal clause* attached to v8 rather than a fresh proclamation. **Both structures given.**
- `መጽአ` — **perfect**. See Finding 2 on the tense spread.
- `ትእልፊት` — **myriad (10,000)**; established from 40:1 / 71:8 against Dan 7:10.
- `ወይትዋቀሥ` — a **hapax in this book**. Reciprocal/Gt stem of a root of **legal dispute**: *to litigate with, to bring a suit against, to convict.* Greek `ἐλέγξει`, Latin `arguere` — all three are courtroom vocabulary, continuing `ፍትሕ` from 1:7.
- `ኃጥኣን፡ ወረሲዓን` — ⭐ **"and" again**, where Gizeh and Jude both read the asyndetic `ἁμαρτωλοὶ ἀσεβεῖς`. Third instance of the Ge'ez pattern (cf. 1:1, 1:3).

**Witnesses:** *(the full clause-by-clause comparison is Finding 2 above; only the raw readings are listed here)*

- Ge'ez `p`/`Bertalotto`: `ወያሕጕሎሙ` for `ወያህጕሎሙ` — orthographic (`ሀ`/`ሐ`).
- Greek `Gizeh`: `ὅτι ἔρχεται σὺν ταῖς μυριάσιν αὐτοῦ καὶ τοῖς ἁγίοις αὐτοῦ, ποιῆσαι κρίσιν κατὰ πάντων, καὶ ἀπολέσει πάντας τοὺς ἀσεβεῖς, καὶ ἐλέγξει πᾶσαν σάρκα περὶ πάντων ἔργων τῆς ἀσεβείας αὐτῶν ὧν ἠσέβησαν καὶ σκληρῶν ὧν ἐλάλησαν λόγων, καὶ περὶ πάντων ὧν κατελάλησαν κατ᾽ αὐτοῦ ἁμαρτωλοὶ ἀσεβεῖς.`
- Greek `Jude`: `ἰδοὺ ἦλθεν κύριος ἐν ἁγίαις μυριάσιν αὐτοῦ, ποιῆσαι κρίσιν κατὰ πάντων, καὶ ἐλέγξαι πάντας τοὺς ἀσεβεῖς περὶ πάντων τῶν ἔργων ἀσεβείας αὐτῶν ὧν ἠσέβησαν καὶ περὶ πάντων τῶν σκληρῶν ὧν ἐλάλησαν κατ᾽ αὐτοῦ ἁμαρτωλοὶ ἀσεβεῖς.`
  - ⚠️ **Edition-dependent**: NA28 reads `πᾶσαν ψυχήν` for `πάντας τοὺς ἀσεβεῖς`; RP adds `αὐτῶν`. See the caveat at the top.
  - ⭐ `ἐλέγξαι` (Jude, infinitive) and `ἐλέγξει` (Gizeh, future indicative) differ by **one vowel**. Tempting to call it an aural slip — but in Koine `αι` merged with `ε` while `ει` merged with `ι`, so these were **not** homophones. On the phonology, this looks like a deliberate syntactic difference, not a mishearing. Stated as an argument, not a fact.
- Aramaic `4Q204`, three units — ink and reconstruction separated in the ledger above:
  - `…רבו]את קדישו[הי …` — *[myri]ads of h[is] holy ones.*
  - `… ב]שרא על עו֗בד֗[י  …` — *[all f]lesh, concerning the wor[ks of…* ⚠️ the `ב` that makes `שרא` into **"flesh"** is reconstructed; the identification is near-certain from `על עובדי` following, but it is one supplied letter.
  - `…] ר֯[ב]רׄבן [וקש]יׄן […` — *gr[ea]t [and har]sh things.* ⭐ `רברבן` is 4/5 ink and has **no counterpart in any other witness**; `[וקש]ין` is 3/5 editorial and is the word that matches Greek `σκληρῶν`. 🛑 See the circularity warning in Finding 2.
- Latin `Cyprian`: `Ecce venit cum multis milibus nuntiorum suorum facere iudicium de omnibus et perdere omnes impios et arguere omnem carnem de omnibus factis impiorum quae fecerunt impie et de omnibus verbis impiis quae de deo locuti sunt.`
- Latin `Vigilius`: `Ecce veniet in millibus facere iudicium et perdere omnes impios et arguere omnem carnem de omnibus operibus impietatis operibus eorum.`
  - ⭐ **`nuntiorum suorum`** — Cyprian has *his **messengers*** where Greek, Ge'ez and Aramaic all have *holy ones*. This is a real semantic substitution, not a translation of `ἁγίων`.
  - ⭐ **`de deo`** — Cyprian says the words were spoken **about God**; every Greek witness has only `κατ᾽ αὐτοῦ`, "against him." Cyprian names the referent the Greek leaves as a pronoun.
  - ⭐ Cyprian has `verbis **impiis**` where Greek has `σκληρῶν` (*hard, harsh*) — a moral word for a forceful one.
  - ⭐ Latin `de omnibus` (*concerning* all) for Greek `κατὰ πάντων` (*against* all); Vigilius drops the phrase from the judgement clause entirely, and both Latin fathers end without any equivalent of `ἁμαρτωλοὶ ἀσεβεῖς`.
  - ⭐ Ge'ez `ላዕሌሆሙ` — "upon **them**" — where Gizeh and Jude have `κατὰ πάντων` ("against **all**"). ⭐ **Four witnesses, four different objects of the judgement:** *them* (Ge'ez) / *all* (both Greek) / *concerning all* (Cyprian) / *nothing* (Vigilius).

---

## Verification pass — what was checked, and what it changed

Every load-bearing claim above was re-checked against the XML, the WLC and the SBLGNT in this repo rather than against my reading of them. **Greek and Hebrew searches were NFD-normalised with combining marks stripped before comparison**, and the matcher was first proven against a known-present accented string (`Ἑνώχ`, 2 hits) so that a null result could not be mistaken for a negative finding.

| Claim | Result |
|---|---|
| `κύριος` occurs in Jude only, nowhere else in ch. 1 | ✅ 1 hit, `[Jude]` |
| `ἰδού` occurs in Jude only | ✅ 1 hit, `[Jude]` |
| `ἐγρήγοροι` at 1:5 in Gizeh | ✅ confirmed — and the Ge'ez `ትጉሃን` is the same concept, independently |
| `ἀπολέσει` ("destroy") absent from Jude | ✅ 1 hit, `[Gizeh]` only |
| `σάρκα` ("flesh") absent from Jude | ✅ 1 hit, `[Gizeh]` only |
| …but Jude's text is edition-dependent | ⚠️ **NA28 reads `πᾶσαν ψυχήν` in that slot** — checked in `greek-nt/SBLGNT/data/sblgntapp/`. The finding is weaker than the apparatus implies. |
| `ትጉሃን` = the Watchers, from internal evidence only | ✅ verb at 20:1 and 100:8; noun at 11 further places |
| `ትእልፊት` = myriad | ✅ via 40:1 / 71:8 against Dan 7:10 `רבו רבבן` (WLC) |
| `መዓረ፡ ግራ` = beeswax | ✅ via 52:6 (identical idiom) + Greek `κηρός` |
| `ויופע` (1:4) is the Deut 33:2 root | ✅ **full ink**, no bracket; Deut 33:2 `הוֹפִיעַ` verified in WLC |
| `[עירין]` "Watchers" in Aramaic 1:2 | 🛑 **100% editorial reconstruction** — cannot be cited |
| `[יזועון]` "shall quake" in Aramaic 1:5 | 🛑 **100% editorial reconstruction** — the Aramaic cannot arbitrate 1:5 |
| `[רבו]את` "myriads" in Aramaic 1:9 | ⚠️ 3 of 5 letters reconstructed |
| `[ב]שרא` "flesh" in Aramaic 1:9 | ⚠️ the letter that makes it "flesh" is reconstructed |
| `[וקש]ין` matches Greek `σκληρῶν` | 🛑 **circular** — 3 of 5 letters supplied, probably *from* the Greek |
| `Gizeh*` at 1:6 | ⚠️ **undetermined** — the siglum is not in the apparatus's manuscript list; not used |
| `Bertalotto` at 1:7 is "orthographic" | ⚠️ **false as stated** — `ወትሠጠጥ` vs `ወትሰጠም` is a different root, not a spelling |
| At 1:8 the apparatus prints the conjecture before the manuscript | ⚠️ confirmed — `option="0"` is `Swete Charles Black Dindorf`, `option="1"` is Gizeh |

> [!warning] Method note carried forward from `enoch-6.md`
> The accent-blind-grep failure documented there was pre-empted here: all Greek matching NFD-normalises and strips combining marks, and the matcher was validated against a known-present string *before* any negative result was accepted. **A search that cannot match is indistinguishable from a claim that is false.**

> [!warning] New method note from this chapter
> **Reading an apparatus top-down assumes `option="0"` is the manuscript. At 1:8 it is not.** The conjecture `γενήσεται` is listed first and the papyrus reading `γενηται` second. Any tool or human that takes the first reading as the base text will silently print an emendation as a manuscript. Checked across chapter 1: this inversion occurs **once**, at 1:8 — but once is enough to make position an unsafe proxy for authority.

---

## What this chapter shows about the book

1. **⭐ The Deuteronomy 33:2 quotation is visible only in the Aramaic.** `ויופע` — full ink, no reconstruction — is the same root as `הוֹפִיעַ`. Greek `φανήσεται` and Ge'ez `ወያስተርኢ` are accurate and carry none of it. Chapter 1 is not merely *like* the Sinai theophany; it is quoting it, and two of the three surviving traditions cannot say so.

2. **⭐ Jude supplies the subject that Enoch withholds.** `κύριος` appears once in the entire chapter's Greek, in Jude alone. Gizeh, the Ge'ez, and both Latin fathers leave the one who comes unnamed. The most famous sentence in 1 Enoch acquired its divine subject at the moment it was quoted by someone else.

3. **⭐ On one clause, the quotation is closer to the Semitic than the manuscript is.** Gizeh splits `רבואת קדישוהי` into two coordinated groups; Jude, the Ge'ez and the Aramaic all keep one. The same lesson chapter 6 taught with Syncellus: **the fuller manuscript is not automatically the better one.**

4. **⭐ The Ge'ez has dropped the speech-offence.** Gizeh, Jude, Cyprian and 4Q204 all charge the wicked with what they *said*. The Ge'ez charges them only with what they *did*. The only complete text of the book is missing half the indictment of its most-quoted verse.

5. **The Ge'ez coordinates what its sources juxtapose.** `ኅሩያነ፡ ወጻድቃነ` (1:1), `ቅዱስ፡ ወዐቢይ` (1:3), `ኃጥኣን፡ ወረሲዓን` (1:9) — three times a single Greek or Aramaic phrase becomes two Ge'ez groups joined by `ወ`. This is a consistent translational habit, and it changes how many parties the text appears to be describing.

6. **The Latin loses a number it has no word for.** `μυριάς` becomes `milia`. Nothing textual happened; the target language simply lacks the unit. Any argument from the Latin about the *size* of the host is an argument about Latin vocabulary.

7. 🛑 **Two of the most quotable Aramaic readings in this chapter are entirely editorial.** `[עירין]` ("Watchers," 1:2) and `[יזועון]` ("shall quake," 1:5) have not one surviving letter between them. Chapter 1 is the best-attested chapter in the book, and even here the Aramaic is thin enough that its two most useful words are supplied. **For 100 of 108 chapters there is no Aramaic at all.** Read the strength of this chapter, then apply the weakness of it as a warning to the rest.
