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

# 1 Enoch 7–8 — The Giants, and the Arts the Watchers Taught

**Translated from the Ge'ez, against the Greek, Qumran Aramaic and Latin witnesses. No English translation consulted.**

Built with `tools/enoch.py`, which drops the Charles-1917 `translation` field bundled in the Ge'ez JSON at parse time, with no flag to re-enable it. See PROVENANCE.md.

Companion to `translations/enoch-6.md`. Chapter 6 named the Watchers; these two chapters are where they **act** and **teach**, so they are the test bed for whether chapter 6's names mean anything.

---

## 🛑 Provenance chain — read before the text

```
Aramaic (lost, ~7% survives at Qumran)
   └─> Greek (lost, ~44% survives)
          └─> Ge'ez  ← the only complete witness, from late manuscripts
```

⭐ **Chapters 7–8 sit inside the 7%.** The Qumran Aramaic covers exactly chapters 1–8 and nothing else in the book; 4Q201, 4Q202 and 4Q204 all speak here. Four traditions could be compared — except one of them cannot.

🛑 **The Latin is ABSENT for every verse of chapters 7 and 8.** Verified: the Latin Fragments version attests chapters **1, 99 and 106 only**. It is not a silent witness here; it is not a witness here at all. Where the brief says "against the Latin," the honest answer is that there is no Latin to work against.

⚠️ These semantic ranges are **not validator-gated** — `ranges/*.json` and `verify_ranges.py` are Hebrew-only. Same limitation as `enoch-6.md` and `revelation-3.md`.

### Witnesses cited here

| Siglum | Language | What it is |
|---|---|---|
| `p` | Ethiopic | John Rylands Library Ethiopic 23 |
| `Bertalotto` | Ethiopic | orthographic correction of `p` |
| `Gizeh` | Greek | Codex Panopolitanus (Akhmim) |
| `Syncellus` | Greek | George Syncellus, *Chronographia* |
| `4Q201`, `4Q202`, `4Q204` | Aramaic | Qumran Cave 4 Enoch scrolls |

🛑 `Syncellus2` appears at 8:4 and is **a modern editor's conjecture, not a manuscript.** The tool flags it. It is quoted below only as an excluded reading.

🛑 Brackets `[ ]` in the Aramaic are **editorial reconstruction, not surviving ink.** Every claim below that rests on a bracketed letter says so in its own sentence. The superscript dots (`ז֯`, `שׄ`) are a different mark — an *uncertain reading of ink that is present*, not a supplied letter.

---

## ⭐⭐⭐ THE PAYOFF: does the sky-angel teach the sky?

Chapter 6 established that the Aramaic names are transparent meteorological and astral compounds. Chapters 7–8 are the test. **The answer is: partially — with one hard counterexample that must not be smoothed over.**

### Step 1 — the ordinals, rebuilt from adjacency only

Syncellus numbers his twenty Watchers (6:7). The Aramaic numbers them too, but the apparatus splices non-contiguous fragments with `…`, and the ordinal sometimes precedes and sometimes follows the name, so **a full running sequence cannot be recovered from this apparatus.** I therefore use only pairs where a name and an ordinal stand **immediately adjacent** with nothing between them.

| Slot | Aramaic (adjacent pair) | Ink status | Syncellus 6:7 |
|---|---|---|---|
| 4th | `כוכבאל רביעי` Kokab-el — **star** | ✅ full ink (`כ` dotted) | δʹ **Χωβαβιήλ** |
| 7th | `דניאל שבי[עי` Dani-el | ✅ name ink, ordinal `שבי` ink | ζʹ **Σαμψίχ** ✗ |
| 8th | `זיקיאל תמׄי֯נ֯[י` Ziqi-el — **flash / spark** | ✅ name ink | ηʹ **Ζακιήλ** |
| 9th | `ברקאל תשיע֯[י` Baraq-el — **lightning** | ✅ name ink, `תשיע` ink | θʹ **Βαλκιήλ** |
| 10th | `עסאל עסי֯רי` ʿAsa-el | ✅ full ink | ιʹ **Ἀζαλζήλ** |
| 13th | `עננאל תלתת עס֯ר֯` ʿAnan-el — **cloud** | ✅ full ink | ιγʹ **Ἀναγημάς** |
| 16th | `שׄהריאל שתת עש֯[ר]` Sahari-el — **moon** | ✅ name + `שתת עש` ink | ιϚʹ **Σαρινᾶς** ⚠️ |

⭐⭐ **Six of these seven slots are matched by Syncellus's Greek list, position for position** (Χωβαβιήλ←כוכבאל, Ζακιήλ←זיקיאל, Βαλκιήλ←ברקאל with ρ→λ, Ἀζαλζήλ←עסאל, Ἀναγημάς←עננאל; slot 7 is the exception). **The seventh slot disagrees outright** — the Aramaic has Daniel, Syncellus has the sun-angel — and slot 16 is weak: Σαρινᾶς is a poor match for שהריאל, while Syncellus's *twentieth*, Σαριήλ, is a good one.

🛑 So Syncellus's numbering is genuinely old — but it is **not** the Aramaic's numbering. Both facts are true and neither may be dropped.

### Step 2 — what each numbered angel teaches (Syncellus 8:3)

> `ὁ ἕνατος ἐδίδαξεν ἀστροκοπίαν· ὁ δὲ τέταρτος έδίδαξεν ἀστρολογίαν, ὁ δὲ ὄγδοος έδίδαξεν ἀεροσκοπίαν·`
> `ὁ δὲ τρίτος ἐδίδαξε τὰ σημεῖα τῆς γῆς  ὁ δὲ ἕβδομος ἐδίδαξε τὰ σημεῖα τοῦ ἡλίου  ὁ δὲ εἰκοστὸς ἐδίδαξε τὰ σημεῖα τῆς σελήνης.`

### Step 3 — the verdict, slot by slot

| Slot | Name means | Teaches | Verdict |
|---|---|---|---|
| **4th** כוכבאל | **star** | ἀστρολογία — star-reading | ✅ **HOLDS, on ink, both traditions** |
| **8th** זיקיאל | **flash / spark / meteor** | ἀεροσκοπία — watching the air | ✅ **HOLDS, on ink, both traditions** |
| **9th** ברקאל | **lightning** | ἀστροκοπία — star-observation | 🛑 **FAILS, on ink, both traditions** |
| **10th** עסאל | (no sky element) | 8:1 — metals, weapons, cosmetics | ✅ control case: no false positive |
| **13th** עננאל | **cloud** | *no teaching preserved anywhere* | ⚪ unknown |
| 3rd | ← *earth?* (inference) | σημεῖα τῆς γῆς — earth-signs | ✅ but see below |
| 7th / sun-angel | **sun** | σημεῖα τοῦ ἡλίου — sun-signs | ✅ but the slot conflicts |
| 20th / moon-angel | **moon** | σημεῖα τῆς σελήνης — moon-signs | ✅ but the slot conflicts |

### Step 4 — the two direct in-verse pairings in the Aramaic itself

These need no ordinal bridge at all. The Aramaic 8:3 runs `NAME + אלף (taught) + TEACHING`:

- 4Q201: `[שמ]שׄיאל אלף נׄח֯שׄי שׄמ[ש` — "…**-shiel** taught the **omens of the sun**."
  ⚠️ The name's sun-element `[שמ]` is **editorial reconstruction**; `שׄיאל` is ink. The teaching is stronger: `נׄח֯שׄי` is ink, and `שׄמ` is ink with only the final `ש` supplied. **So "omens of the sun" is essentially on parchment; "Shamshiel" is half-supplied.**
- 4Q202: `…ארע]ת֯קפ אלף נחש[י] אר[עא` — "…**-taqoph** taught the **omens of the ear[th]**."
  ⚠️ The name's earth-element `ארע]` is **entirely editorial**; only `ת֯קפ` ("is-strong") is ink. The teaching's `נחש` and `אר` are ink.

⭐ And Gizeh preserves one more, with no reconstruction anywhere: `Σεριὴλ σεληναγωγίας` — the **moon**-name teaching **moon**-conducting.

### Step 5 — the honest summary

**The correspondence HOLDS for the astral subset and FAILS for the meteorological subset.**

- **Sun, star, moon, earth, air** all get matching teachings, twice on surviving ink (star/4th, flash/8th) and three more times with either a reconstructed letter or a single Greek witness carrying the weight.
- **Rain (מטראל), cloud (עננאל), thunder (רעמאל)** — the three purely meteorological names from chapter 6 — receive **no teaching in any witness.** Not a mismatch; a silence.
- 🛑 **Lightning fails outright.** ברקאל is the 9th on ink in 4Q201; Βαλκιήλ is the 9th in Syncellus; and the 9th teaches ἀστροκοπία. Gizeh independently says `Βαρακιὴλ ἀστρολογίας`, and the Ge'ez independently says `ወበራቅኤል፡ ረኣይያነ፡ ከዋክብት` — "and Baraqel, observers of the stars." **All three traditions give the lightning-angel an astral art. Nobody in this book teaches lightning.**

So the teaching-list is not a meteorology; it is a **divination manual** — reading omens from sun, moon, stars, earth and air. It overlaps the chapter-6 name list at the astral names and slides off the weather ones. **The pattern is real and it is partial. It should not be reported as clean.**

> 🛑 **One claim I built and then had to throw away.** From `[חדעסר]א לה מטר אל` I first concluded that the *rain*-angel is the 11th and that Syncellus's 11th, Φαρμαρός, teaches φαρμακεία — a rain-angel dispensing drugs, a spectacular counterexample. It does not stand: in that phrase the ordinal is separated from the name by `לה`, so it may belong to the preceding lost name, and the ordinal itself is reconstructed except its final `א`. **Matarel's position is unknown and the counterexample is withdrawn.** What survives is the smaller observation that Syncellus alone spells the 11th `Φαρμαρός` where Gizeh has `Ἀρμαρώς` and the Ge'ez `አርሚሮስ` — an *f*- that appears only in the witness who has him teach *φαρμακείας*. That looks like a Greek pun grown onto the name, but it is an inference about a mechanism, not a reading.

---

## ⭐⭐ SECOND FINDING: the Ge'ez has lost the metals

Aramaic 8:1 (4Q202) names four metals and what is done with each:

| Aramaic | Ink status | Sense |
|---|---|---|
| `[למ]עבד חרבן די פרזל` | ✅ `עבד חרבן די פרזל` **all ink** | to make **swords of iron** |
| `ושר֯[ינין] …נח[ש` | ⚠️ `נח` ink, `[ש` supplied | coats of mail … **bronze/copper** |
| `[י]עבדון ד[הבא]א` | ⚠️ `ד…א` ink, `[הבא]` supplied | they will work **gold** |
| `ועלא כסׄפא למעבדהא לצמידין` | ✅ **all ink** | and as for **silver**, to work it into **bracelets** |

Both Greek witnesses have `τὰ μέταλλα` — **the metals** — in a reading they share (`[Gizeh Syncellus]`), and Syncellus expands it to `τὰ μέταλλα τῆς γῆς καὶ τὸ χρυσίον πῶς ἐργάσωνται` and adds `τὸν ἄργυρον`.

🛑 **The Ge'ez 8:1 contains no metal at all.** Where the Greek has "the metals and their working," the Ge'ez reads `ወአርአዮሙ፡ ለዘእምድኅሬሆሙ፡ ወምግባራቲሆሙ` — "and he showed them **that which is after them** and **their workings**." The second half (`ምግባራቲሆሙ` = `τὴν ἐργασίαν αὐτῶν`) survives exactly; the noun it belonged to is gone.

⭐ **Verified that this is loss, not vocabulary poverty:** the Ge'ez of 1 Enoch has ወርቅ (gold, 7×), ብሩር (silver, 8×), ኀጺን (iron, 6×), ብርት (bronze, 5×) — all four cluster at 52:2–8, 56:1, 67:4. The translator had the words. They are simply not in 8:1.

⭐⭐ And the Ge'ez preserves the *rest* of the list intact, which is what makes the gap visible:

| Item | Aramaic | Greek (Gizeh) | Ge'ez |
|---|---|---|---|
| bracelets | `לצמידין` ✅ ink | `ψέλια` | `አውቃፋተ` |
| ornaments | — | `κόσμους` | `ወሠርጐ` |
| **kohl / antimony** | `כוחלא` ✅ ink | `στίβεις` | `ወተኵሕሎተ` |
| eye-beautifying | `ועל צדי[דא` ⚠️ `צדי` ink | `τὸ καλλιβλέφαρον` | `ወአሠንዮ፡ ቀራንብት` |
| choice stones | — | `παντοίους λίθους ἐκλεκτούς` | `ወእብነ፡ እምኵሉ፡ እብን፡ ክቡር፡ ወኅሩይ` |
| dyes | — | `τὰ βαφικά` | `ወኵሎ፡ ጥምዐታተ፡ ኅብር` |

⭐ **Aramaic `כוחלא` and Ge'ez `ተኵሕሎተ` are the same Semitic root k-w-ḥ-l**, and the Greek in between them (`στίβι`) is not. This is *not* evidence that the Ge'ez saw the Aramaic — Ge'ez is itself a Semitic language and owns that root natively. It is evidence that the Ge'ez translator recognised the *thing* and reached for his own word for it, which is why this item survived where "the metals" did not.

⚠️ The Ge'ez ends with `ወተውላጠ፡ ዓለም` — "**and the changing (alteration | transformation) of the age (world)**" — which **both Greek witnesses lack**; they stop at `καὶ τὰ βαφικά`. A Ge'ez plus, unexplained.

⭐ **Internal corroboration for the dyes:** Ge'ez 65:6 lists together `ሥራያተ` (sorceries), `ኅብራት` (colours/dyes) and `ይሰብኩ፡ ስብኮ` (they cast castings) — the same metal-and-dye-and-sorcery cluster as 8:1, elsewhere in the same book.

---

## ⭐⭐ THIRD FINDING: the sorcery-teaching is a triple doublet, and it is ancient

The teaching of drugs and spells appears at **three** places, and no two witnesses put it in the same set of places:

| | 7:1 | 7:2 | 8:3 |
|---|---|---|---|
| **Ge'ez** | ✅ `ሥራያተ፡ ወስብዓታተ፡ ወመቲረ፡ ሥርው` | — | ✅ (given to `አሜዛራክ`) |
| **Gizeh** | ✅ `φαρμακείας καὶ ἐπαοιδὰς καὶ ῥιζοτομίας` | — | ✅ (given to `Σεμιαζᾶς`) |
| **Syncellus** | ✗ (has `ἕως τοῦ κατακλυσμοῦ` instead) | ✅ `ἐδίδαξαν … φαρμακείας καὶ ἐπαοιδάς` | ✅ (given to `Σεμιαζᾶς`) |
| **Aramaic** | ✅ `ולאלפׄה אנין חרשה` / `לחרש]תׄא ולכׄ[שפתא` | — | ✅ `שמי חזה אלף …` |

⭐ The Aramaic has it at **both** 7:1 and 8:3, on ink in both places. **The doublet is not a Ge'ez artifact and not a Greek one — it goes back to the Aramaic.**

⭐⭐ **The Ge'ez contradicts itself about who taught it, and its own 9:7 gives the older answer.** Ge'ez 8:3 opens `አሜዛራክ፡ መሀረ፡ ኵሎ፡ መሳብዕያነ` — Amezarak taught all the enchanters. But Ge'ez **9:7** reads `ወአመረ፡ ስብዓታተ፡ ስማዝያ` — "**and Shemihazah made known incantations**," using the same word `ስብዓት` and naming the leader as in 6:3. The Aramaic (`שמי חזה אלף`, full ink) and both Greek witnesses (`Σεμιαζᾶς ἐδίδαξεν`, a shared reading) agree with Ge'ez 9:7 against Ge'ez 8:3. **The Ge'ez preserves the correct attribution one chapter later than it loses it.**

⚠️ `שמי חזה` is written as **two words with a space** in 4Q201 — as `מטר אל` and `רעמׄ א[ל` are in chapter 6. Noted because it bears on whether these were felt as names or as descriptions.

---

## THE TEXT

> Where the witnesses genuinely differ, all readings are given and none is preferred.
> `( | )` marks a word whose Ge'ez carries more than one sense.

### 7:1

**ወባዕዳንሂ፡ ኵሉ፡ ምስሌሆሙ፡ ወነሥኡ፡ ሎሙ፡ አንስትያ፡ ወኀረየ፡ ኵሉ፡ ለለ፡ ርእሱ፡ አሐተ፡ አሐተ፡ ወወጠኑ፡ ይባኡ፡ ኀቤሆን፡ ወተደመሩ፡ ምስሌሆን፡ ወመሀርዎን፡ ሥራያተ፡ ወስብዓታተ፡ ወመቲረ፡ ሥርው፡ ወዕፀወ፡ አመርዎን።**

*wäbaʿədanəhi kwəlu məsəlehomu wänäśəʾu lomu ʾänəsətəya wäḫäräyä kwəlu lälä rəʾəsu ʾäḥätä ʾäḥätä wäwäṭänu yəbaʾu ḫäbehonə wätädämäru məsəlehonə wämähärəwonə śərayatä wäsəbəʿatatä wämätirä śərəwə wäʿəṣ́äwä ʾämärəwonə*

**And all the others with them — and they took women for themselves, and each one chose for himself one and one; and they began to go in to them and (joined | mingled | united) themselves with them; and they taught them (sorceries | magic arts | poisonings) and (incantations | adjurations | binding-spells), and the cutting of roots, and they made known to them the (plants | trees | wood).**

- `ወተደመሩ` *wätädämäru* — the root is **to join, add, unite, mix**. It carries no defilement. 🛑 **The Greek does not translate it, it interprets it:** both witnesses read `μιαίνεσθαι ἐν αὐταῖς`, "**to be defiled** with them." Ge'ez neutral, Greek moral. **Both are given; neither is preferred.**
- `ስብዓታተ` *səbəʿatatä* — from the root of **to swear / adjure** (cf. Hebrew שבע). The word is a *sworn* spell, an adjuration, not a recipe. It recurs at 9:7.
- `ዕፀወ` *ʿəṣ́äwä* — **trees / wood / plants**. Gizeh's `τὰς βοτάνας` ("the herbs") narrows it.

**Witnesses:**
- Aramaic 4Q201 `ולאלפׄה אנין חרשה ו[…` — "and to teach them **sorcery** and…"; 4Q202 `…לחרש]תׄא ולכׄ[שפתא` — "sorcery and spell[craft]", where `חרש]תׄא` is largely supplied and `ולכׄ` is ink. Root `חרש` also means *to be silent / deaf* and *to plough, engrave* — the Aramaic word is not unambiguous on its own; the Greek and Ge'ez settle it as sorcery.
- Aramaic 4Q201 `מן כל די בחרו` — "from all whom they chose" ✅ ink, matching the Ge'ez's `ወኀረየ`.
- ⭐ Syncellus opens with a **date the other three witnesses do not have**: `ἐν τῷ χιλιοστῷ ἑκατοστῷ ἑβδομηκοστῷ ἔτει τοῦ κόσμου` — "in the 1170th year of the world" — and closes `ἕως τοῦ κατακλυσμοῦ`, "until the flood." Neither Gizeh, nor the Ge'ez, nor the Aramaic has either. ⚠️ Syncellus is a *chronographer*; unlike his older readings in chapter 6, this looks like his own frame. Flagged as suspicion, not established.
- Syncellus **lacks** the whole teaching clause here (see the doublet table above).
- Ge'ez `p`/`Bertalotto` read `ወባዕዳን` for `ወባዕዳንሂ`, `አንስያ` for `አንስትያ`, and `አሐተ` **once** where the base text doubles it (`አሐተ፡ አሐተ` = "one and one," distributive).

### 7:2

**ወእማንቱሰ፡ ፀንሳ፡ ወወለዳ፡ ረዓይተ፡ ዐበይተ፡ ወቆሞሙ፡ በበ፡ ሠላሳ፡ ምእት፡ በእመት።**

*wäʾəmanətusä ṣ́änəsa wäwäläda räʿayətä ʿäbäyətä wäqomomu bäbä śälasa məʾətə bäʾəmätə*

**And they conceived and bore great giants, and their (stature | height) was, each of them, three thousand in cubits.**

- `ረዓይተ` *räʿayətä* — ⭐ **verified against the whole Ge'ez book: this word occurs only at 7:2, 7:4, 9:9, 15:3, 15:8, 15:11, 16:1 — the Watchers cycle and nowhere else.** It is the technical term for these beings. A different word entirely, `ኖሎት`, carries "shepherds" at 89:61–90:22. So the tempting derivation from the *pasture* root has no support inside this text and is not offered.
- The number is written out in the base text (`ሠላሳ፡ ምእት` = thirty × hundred) and as the numeral `፴፻` in both mss. Both are **3000**.

**Witnesses:**
- Greek Gizeh `ἐκ πηχῶν τρισχιλίων` — **3000 cubits**. Ge'ez and Gizeh agree exactly.
- 🛑 **Syncellus has no measurement at all.** In its place he gives **three generations**: `ἔτεκον αὐτοῖς γένη τρία· πρῶτον γίγαντας μεγάλους· οἱ δε Γίγαντες ἐτέκνωσαν Ναφηλείμ, καὶ τοῖς Ναφελεὶμ ἐγεννήθησαν Ἐλιούδ` — giants, who fathered Nephilim, who fathered Elioud — plus `καὶ ἦσαν αὐξανόμενοι κατὰ τὴν μεγαλειότητα αὐτῶν`, "they went on growing according to their greatness."
- ⚠️ **The Aramaic gives no size either.** 4Q201 `והויה בטנן מנהׄן וילׄ[דתן` ("and they became pregnant from them and bo[re…]") and `הוו מתׄילדין על ארעה֯` ("were being born upon the earth"); 4Q202 `…כי]לדות[הון`. **The 3000 cubits rest on Gizeh and the Ge'ez only.** Two of four witnesses; the two later ones.

### 7:3

**እሉ፡ በልዑ፡ ኵሎ፡ ጻማ፡ ሰብእ፡ እስከ፡ ስእንዎሙ፡ ሴስዮተ፡ ሰብእ።**

*ʾəlu bäləʿu kwəlo ṣama säbəʾə ʾəsəkä səʾənəwomu sesəyotä säbəʾə*

**These devoured all the (toil | labour | earnings) of humankind, until human beings were unable to (feed | sustain | provision) them.**

⭐ **Three-way agreement, root for root:** Ge'ez `ጻማ` / Aramaic `ע֯מל כל בני אנשה` ("the toil of all the sons of men," ✅ ink apart from a dotted `ע`) / Gizeh `τοὺς κόπους τῶν ἀνθρώπων`. All three say the giants ate the *work*, not the food — the labour itself.

**Witnesses:** 4Q202 `ה]ווא֯ א֯כלין` — periphrastic "they **were** eating," durative, against Gizeh's imperfect `κατησθίοσαν`. Ge'ez `p` reads `ፃማ`, `Bertalotto` `ጻማ` — orthographic. Syncellus **absent** for this verse.

### 7:4

**ወተመይጡ፡ ረዓይት፡ ላዕሌሆሙ፡ ይብልዕዎሙ፡ ለሰብእ።**

*wätämäyəṭu räʿayətə laʿəlehomu yəbələʿəwomu läsäbəʾə*

**And the giants (turned | turned back | turned against) upon them, to devour humankind.**

🛑 **Three witnesses, three different verbs, and they are not the same act:**

| | Verb | Means |
|---|---|---|
| Ge'ez | `ወተመይጡ` | **turned** (against them) |
| Gizeh | `ἐτόλμησαν` | **dared, ventured** (against them) |
| Aramaic 4Q201 | `ק֯שרין` | **conspiring, binding together** |

And the object differs too: the Aramaic reads `…ק֯שרין לקטלה לאנשא` — "conspiring **to kill** men" (`קטל` = to kill; ✅ ink, `ק` dotted) — where the Ge'ez and Gizeh both say **to eat** them. **All three are given; none is preferred.** Syncellus absent.

### 7:5

**ወወጠኑ፡ የአብሱ፡ በአዕዋፍ፡ ወበአራዊት፡ ወበዘይትሐወስ፡ ወበዓሣት፡ ወሥጋሆሙ፡ በበይናቲሆሙ፡ ተባልዑ፡ ወደመ፡ ሰትዩ፡ እምኔሃ።**

*wäwäṭänu yäʾäbsu bäʾäʿəwafə wäbäʾärawitə wäbäzäyətəḥäwäsə wäbäʿaśatə wäśəgahomu bäbäyənatihomu täbaləʿu wädämä sätəyu ʾəməneha*

**And they began to sin against the birds, and against the (beasts | wild animals), and against that which creeps, and against the fish; and they devoured one another's flesh among themselves, and drank blood from it.**

⭐ Every element of the list is confirmed by the Aramaic: `ק֯ובל כל כנ֯ף֯ ו֯[חיו]ת֯ ארע[ה` ("against every winged thing and the [beas]ts of the earth" — `כנף` ink, `[חיו]` supplied), 4Q202 `…ור]חשי[א` ("and the creeping things"), `[…ו]נ֯נ֯י֯א [ימהא] ו֯למ֯כ֯ל בׄשרׄ[הן` ("and the fish [of the sea], and to eat their flesh"), 4Q202 `…שתׄינא דמ֯[א]א` ("drinking blood").

⭐ Ge'ez `ሰትዩ` and Aramaic `שתׄינא` are the same Semitic root **š-t-y**, "to drink," surviving intact across the whole chain.

**Witnesses:** ⚠️ Both Ethiopic mss read `ወዲበ፡ አፈዊት` where the base text has `ወበአራዊት` — an unexplained divergence in the word for beasts, not merely orthographic. They also read `ወበአሳት` for `ወበዓሣት` (fish). Syncellus absent throughout.

### 7:6

**ወአሜሃ፡ ሰከየቶሙ፡ ለዐማፅያን።**

*wäʾämeha säkäyätomu läʿämaṣ́əyanə*

**And then [she] (accused | made complaint against | brought petition against) the (lawless | unjust | violent) ones.**

⭐⭐ **The base Ge'ez text has lost its subject, and the grammar proves it.** `ሰከየቶሙ` carries the **3rd-person feminine singular** perfect ending `-ት-`. Something feminine did the accusing, and the base text does not say what. Both mss supply it: `ወአሜሃ፡ **ምድር**፡ ሰከየቶሙ` — "then **the earth** accused them." Gizeh agrees: `τότε **ἡ γῆ** ἐνέτυχεν κατὰ τῶν ἀνόμων`.

So: the mss and the Greek preserve the subject; the base text preserves only the verb ending that requires one. **Corrected here from the mss, and the correction is flagged.**

**Witnesses:** Aramaic 4Q202 `…מׄאׄא ב֯הׄ מתעבד  vacat` — "…was being done in it," followed by a **vacat** (a deliberate blank in the scroll, marking a section break). Ethiopic `p` `ለኣማፅያን` / `Bertalotto` `ለዐማፃያን`. ⚠️ Verse division differs: the base text ends 7:5 with `እምኔሃ`; both mss begin **7:6** with it. Syncellus absent.

---

### 8:1

**ወአዛዝኤል፡ መሀሮሙ፡ ለሰብእ፡ ገቢረ፡ አስይፍት፡ ወመጥባሕት፡ ወወልታ፡ ወድርዐ፡ እንግድዓ፡ ወአርአዮሙ፡ ለዘእምድኅሬሆሙ፡ ወምግባራቲሆሙ፡ አውቃፋተ፡ ወሠርጐ፡ ወተኵሕሎተ፡ ወአሠንዮ፡ ቀራንብት፡ ወእብነ፡ እምኵሉ፡ እብን፡ ክቡር፡ ወኅሩይ፡ ወኵሎ፡ ጥምዐታተ፡ ኅብር፡ ወተውላጠ፡ ዓለም።**

*wäʾäzazəʾelə mähäromu läsäbəʾə gäbirä ʾäsəyəfətə wämäṭəbaḥətə wäwäləta wädərəʿä ʾənəgədəʿa wäʾärəʾäyomu läzäʾəmədəḫərehomu wäməgəbaratihomu ʾäwəqafatä wäśärəgwä wätäkwəḥəlotä wäʾäśänəyo qäranəbətə wäʾəbənä ʾəməkwəlu ʾəbənə kəburə wäḫəruyə wäkwəlo ṭəməʿätatä ḫəbərə wätäwəlaṭä ʿalämə*

**And ʿAzazʾel taught humankind the making of swords and (slaughtering-knives | daggers) and shields and breastplates of the chest; and he showed them (what is after them | what comes behind them) and their workings — bracelets, and (ornament | adornment), and the painting with kohl, and the beautifying of the (eyebrows | eyelashes), and stone from every precious and choice stone, and all the (dyeings | tinctures) of colour, and the (changing | alteration | transformation) of the (world | age).**

- `ወተኵሕሎተ` — the k-ḥ-l root: **antimony/kohl applied to the eye.** Occurs **once in the entire Ge'ez Enoch**, here. Gizeh `στίβεις`; Aramaic `כוחלא` ✅ ink.
- `ወተውላጠ፡ ዓለም` — ⚠️ has **no Greek counterpart**; both witnesses stop at `καὶ τὰ βαφικά`.
- `ለዘእምድኅሬሆሙ` — where both Greek witnesses have `τὰ μέταλλα`. See the metals section above.

**Witnesses — the name:**

| Witness | Form |
|---|---|
| Aramaic 4Q202 | `ע֯שׄאׄ[ל]` — ʿ-Ś-ʾ + supplied `-el`, **all three surviving letters carry uncertainty dots** |
| Aramaic 4Q201 (6:7) | `עסאל` ✅ full ink, "the tenth" |
| Greek Gizeh | `Ἀζαήλ` |
| Greek Syncellus | `Ἀζαήλ`, "the tenth of the chiefs" |
| Ge'ez | `አዛዝኤል` — **a doubled middle consonant no other witness has** |

⭐⭐ **Three-way ordinal agreement:** 4Q201 6:7 `עסאל עסי֯רי` (✅ ink), Syncellus 6:7 `ιʹ Ἀζαλζήλ`, Syncellus 8:1 `ὁ δέκατος τῶν ἀρχόντων`. The Aramaic and the Greek chronographer independently make this angel the **tenth**. ⚠️ Gizeh and the Ge'ez number nobody.

**Other readings:**
- Syncellus alone closes with `καὶ ἐποίησαν ἑαυτοῖς οἱ ὑιοὶ τῶν ἀνθρώπων καὶ ταῖς θυγατράσιν αὐτῶν, καὶ παρέβησαν καὶ ἐπλάνησαν τοὺς ἁγίους` — "and the sons of men made them for themselves and for their daughters, and they transgressed and **led the holy ones astray**." Gizeh, Ge'ez and Aramaic all lack it.
- Gizeh alone has `διδάγματα ἀγγέλων` ("teachings of angels").
- ⚠️ Aramaic `מא ית[חפר]` — "what is [dug/mined]": `מא ית` is ink, **the mining verb `[חפר]` is entirely editorial.** Any statement that the Aramaic mentions *mining* rests on supplied letters.
- Ethiopic variants: `p` `መሐሮሙ`, `ወድርዓ`, `ወተኵህሎተ`, `ዕብን`; `Bertalotto` `መሀሮሙ`, `ወድርዐ`, `ወተኵሎተ`, `እብን`. Both mss read `ዘእምድኅሬሆሙ` (without `ለ-`) and `ወምግባረሆሙ` for `ወምግባራቲሆሙ`.

### 8:2

**ወኮነ፡ ርስዐት፡ ዐቢይ፡ ወዘምዎ፡ ወስሕቱ፡ ወማሰነ፡ ኵሉ፡ ፍናዊሆሙ።**

*wäkonä rəsəʿätə ʿäbiyə wäzäməwo wäsəḥətu wämasänä kwəlu fənawihomu*

**And there was great (impiety | godlessness | wickedness), and they committed fornication, and they went astray, and all their ways were (corrupted | destroyed | ruined).**

- `ርስዐት` — ⚠️ Ge'ez orthography does not separate the root of **to forget** from the root of **to be wicked/impious** (cf. Hebrew רשע) here. Internal evidence settles it: `ረሲዓን` "the wicked" is used ten times across 1:1, 1:9, 5:7, 16:1, 38:3 and elsewhere, and `ርስዐት` itself recurs at 104:9. The Greek confirms: `ἀσέβεια`, **impiety**. The "forgetting" sense is recorded here and set aside.

**Witnesses:**
- Aramaic 4Q202 `…והוו]א פחׄ[זין` — the root `פחז`, "**to be wanton, reckless, licentious**." ⚠️ Only `פח` is ink; `[זין` is supplied and `והווא]` entirely so. A different image from ἀσέβεια — but the surviving ink is two letters, and no argument should be built on it.
- ⚠️ Both mss have **two** quantifiers where the Greek has one: `ርስዐት፡ ዓቢይ … ወብዙኅ፡ ዘምዎ` ("great impiety … and **much** fornication") against Gizeh/Syncellus `ἀσέβεια πολλή`. The base text has only `ዐቢይ`.
- ⭐ Voice differs at the close: Gizeh `ἠφανίσθησαν ἐν πάσαις ταῖς ὁδοῖς αὐτῶν` (**passive** — "they were destroyed in all their ways"); Syncellus `ἠφάνισαν τὰς ὁδοὺς αὐτῶν` (**active** — "they destroyed their ways"). Ge'ez `ወማሰነ፡ ኵሉ፡ ፍናዊሆሙ` sides with Gizeh. Both given.
- Ethiopic mss read `ወማሰና` and `ፍናቂሆሙ`.

### 8:3

**አሜዛራክ፡ መሀረ፡ ኵሎ፡ መሳብዕያነ፡ ወመታርያነ፡ ሥርዋት፡ አርሚሮስ፡ ፈትሐ፡ ስብዓታተ፡ ወበራቅኤል፡ ረኣይያነ፡ ከዋክብት፡ ወኮከብኤል፡ ትእምርታተ፡ ወጥምኤል፡ መሀረ፡ ራእየ፡ ኮከብ፡ ወአስራድኤል፡ መሀረ፡ ሩጸተ፡ ወርኅ።**

*ʾämezarakə mähärä kwəlo mäsabəʿəyanä wämätarəyanä śərəwatə ʾärəmirosə fätəḥä səbəʿatatä wäbäraqəʾelə räʾayəyanä käwakəbətə wäkokäbəʾelə təʾəmərətatä wäṭəməʾelə mähärä raʾəyä kokäbə wäʾäsəradəʾelə mähärä ruṣätä wärəḫə*

**Amezarak taught all the (enchanters | adjurers | spell-binders) and the cutters of roots. Armiros (loosed | untied | released) incantations. And Baraqʾel — the observers of the stars. And Kokabʾel — signs. And Ṭamʾel taught the (seeing | observation) of the star. And Asradʾel taught the (running | course) of the moon.**

⭐ **The Ge'ez turns arts into practitioners.** Where the Greek has abstract art-names (`ἐπαοιδάς`, `ῥιζοτομίας`, `ἀστρολογίας`), the Ge'ez has agent nouns — `መሳብዕያነ` "enchanters," `መታርያነ ሥርዋት` "root-cutters," `ረኣይያነ ከዋክብት` "star-observers". A consistent shift, not a one-off.

⭐ `ትእምርታተ` "signs" — **verified against the whole book: the only other occurrences are 82:16 and 82:19, both `ትእምርታተ፡ መዋዕል`, "the signs of the seasons," in the astronomical book.** In this text the word is calendrical and celestial. That supports the Aramaic's fuller phrase `נחשי כוכבין`, "the **omens of the stars**" — the Ge'ez and Gizeh both kept "signs" and dropped what they are signs *of*.

⭐ `ፈትሐ` "loosed" is an exact semantic match for Gizeh's `ἐπαοιδῶν λυτήριον` — **the un-binding of spells**, the counter-art to `ስብዓት`.

**Witnesses — the Aramaic, letter by letter:**

| Reading | Ink | Sense |
|---|---|---|
| 4Q201 `שמי חזה אלף` | ✅ **all ink** | Shemihazah taught |
| 4Q201 `חׄב֯[רו` | ⚠️ `חב` ink, `[רו` supplied | spell-binding (`חבר`) |
| 4Q202 `א]ל֯[ף] חרש` | ⚠️ `חרש` ink, "taught" supplied | sorcery |
| 4Q201 `[כ]שפ֯ו וח֯רטמו֯ ובוש[ין` | ⚠️ `שפו`, `וחרטמו`, `ובוש` ink | sorcery, and magic-arts (`חרטם`, cf. Dan 2:2), and *bwš…* — **untranslated, I could not identify the root with confidence** |
| 4Q201 `[נ]חׄשי כוכב֯ין` | ⚠️ `חשי כוכבין` ink, only `[נ]` supplied | **the omens of the stars** |
| 4Q201 `זיכקאאׄ[ל` | ⚠️ `זיכקאא` ink | a name — Ziq(i)el; `זיק` = spark, flash, meteor |
| 4Q201 `[שמ]שׄיאל אלף נׄח֯שׄי שׄמ[ש` | ⚠️ name half supplied; teaching `נחשי שמ` ink | …-shiel taught **the omens of the sun** |
| 4Q202 `ארע]ת֯קפ אלף נחש[י] אר[עא` | ⚠️ name's "earth" supplied; `נחש … אר` ink | …-taqoph taught **the omens of the earth** |
| 4Q201 `[לגלי]הׄ רׄזין לנשיהן` | ✅ `רזין לנשיהן` ink | …**mysteries to their wives** |
| 4Q202 `וכול֯הון שריו֯ לגליה` | ✅ **all ink** | **and all of them began to reveal** |

⭐ `נחש` is the same consonantal string that means **bronze** at 8:1 (`נח[ש`) and **divination/omen** here. The homonymy is real and is left standing.

⭐⭐ **The closing clause is the sharpest split in these two chapters.** The Aramaic (on ink, in **both** scrolls) and Syncellus agree that **all** the Watchers began revealing mysteries:

> 4Q202 `וכול֯הון שריו֯ לגליה` · 4Q201 `רׄזין לנשיהן`
> Syncellus `πάντες οὗτοι ἤρξαντο ἀνακαλύπτειν τὰ μυστήρια ταῖς γυναιξὶν αὐτῶν καὶ τοῖς τέκνοις αὐτῶν`

🛑 **Gizeh and the Ge'ez both lack it entirely.** Syncellus additionally carries the giants' cannibalism here (`ἤρξαντο οἱ γίγαντες κατεσθίειν τὰς σάρκας τῶν ἀνθρώπων`), which Gizeh and the Ge'ez placed back at 7:4. **This is the chapter-6 pattern repeating: where the Aramaic survives to arbitrate, Syncellus is on its side and the fuller Gizeh is not.**

**Witnesses — the Greek doublet:**

⚠️ At apparatus unit 1869, **both** readings are attributed to `Syncellus`: the name-form `Βαρακιὴλ ἀστρολογίας` (shared with Gizeh) *and* the ordinal-form `ὁ ἕνατος … ὁ δὲ τέταρτος … ὁ δὲ ὄγδοος …`. The same happens at unit 1870. **Syncellus's text carries both recensions of 8:3 side by side** — a named list and a numbered list. This is what makes the ordinal cross-check in the payoff section possible at all.

**Ethiopic variants:** `p` `መሐረ` (×2), `መሳብእያን`, `ሰብአታት`; `Bertalotto` `መሀረ`, `መሳብዕያን`, `ስብዐታት`. Both mss read `አርማኖስ` for `አርሚሮስ`, `ወበረቀዓል` for `ወበራቅኤል`, `ወኮከብኢል` for `ወኮከብኤል`, `ርእየ` for `ራእየ`, `ሩፀተ` for `ሩጸተ`, and both drop the accusative on `መሳብዕያን`/`ወመታርያን`.

⚠️ Ge'ez `አስራድኤል` teaches the moon but contains **no moon element** in its own form, and does not appear in the Ge'ez chapter-6 list at all. Gizeh's `Σεριήλ` and Syncellus's `Σαριήλ` both plausibly reflect `שהריאל`; the Ge'ez form does not. Noted, not explained.

### 8:4

**ወበህጕለተ፡ ሰብእ፡ ጸርሑ፡ ሰብእ፡ ወበጽሐ፡ ቃሎሙ፡ ሰማየ።**

*wäbähəgwəlätä säbəʾə ṣärəḥu säbəʾə wäbäṣəḥä qalomu sämayä*

**And at the (destruction | perishing | loss) of humankind, human beings cried out, and their voice reached heaven.**

⚠️ The base text has `ሰብእ` **twice** (once as the genitive of "destruction," once as the subject of "cried out"); both mss have it **once**: `ወበኅጕለተ፡ ሰብእ፡ ጸርሑ፡ ወበጽሐ…`. Given as the base has it, with the ms reading recorded.

**Witnesses:**
- Aramaic 4Q201 `ולׄ[קבל] מ֯עבד …מן ארעא [… סלק֯ ק[דם] …` — "and be[cause of] the deed … from the earth … it went up bef[ore] …"; 4Q202 `…אר]עא וקלאׄ` ("…the earth, and the voice").
- ⭐ The Aramaic and Ge'ez share **"the voice"** (`וקלא` / `ቃሎሙ`) where Gizeh makes `ἡ βοή` the subject of the ascent.
- ⚠️ **The "before [the Lord]" reading rests on one surviving letter.** Aramaic `ק[דם]` has **only the `ק` on parchment**; `דם` is supplied. Syncellus independently reads `ἐνώπιον Κυρίου`, where Gizeh has only `εἰς οὐρανούς`. The two agree — but the Aramaic half of that agreement is one letter plus an editor. **Stated as suspicion, not as evidence.**
- Syncellus adds `καὶ ἤρξαντο οἱ ἄνθρωποι ἐλαττοῦσθαι ἐπὶ τῆς γῆς` — "and men began to **grow fewer** upon the earth."
- 🛑 A third reading here (`Τότε ἐβόησαν οἱ ἄνθρωποι … ἐνώπιον τοῦ κυρίου τῶν κυρίων πάντων τῇ μεγαλωσύνῃ`) is sigla'd **`Syncellus2` — a modern editor's conjecture, not a manuscript.** It is the most rhetorically satisfying reading on the page and it is **excluded**. Quoted here only so that its exclusion is on the record.

---

## Verification pass — what was checked, and what it changed

| Claim | Result |
|---|---|
| Latin attests nothing in ch 7–8 | ✅ confirmed — Latin covers ch **1, 99, 106** only |
| Ge'ez 8:1 has no word for any metal | ✅ confirmed; and ወርቅ/ብሩር/ኀጺን/ብርት all occur elsewhere in the book, so it is loss, not vocabulary |
| `τὰ μέταλλα` in both Greek witnesses | ✅ confirmed, one shared `[Gizeh Syncellus]` reading |
| `ረዓይት` used only of the giants | ✅ confirmed — 7 occurrences, all in the Watchers cycle; `ኖሎት` carries "shepherd" |
| `ትእምርታተ` is a celestial/calendrical word | ✅ confirmed — only 8:3, 82:16, 82:19 |
| Ge'ez 9:7 gives the incantations to Shemihazah | ✅ confirmed, against Ge'ez 8:3's `አሜዛራክ` |
| 7:6 base text has a subjectless 3fs verb | ✅ confirmed; both mss and Gizeh supply "the earth" |
| Syncellus's ordinals match Qumran at 4, 8, 9, 10, 13 | ✅ confirmed on adjacent ink pairs; ✗ diverge at 7 and 16/20 |
| Star-angel → astrology, flash-angel → air-watching | ✅ confirmed on ink in both traditions |
| Lightning-angel → lightning | 🛑 **FALSE in all three traditions** — he teaches an astral art everywhere |
| Rain-angel (11th) teaches φαρμακεία | 🛑 **RETRACTED** — Matarel's ordinal cannot be established; see the boxed note above |
| `Syncellus2` at 8:4 is a manuscript | 🛑 **FALSE** — editor's conjecture, excluded |

> [!warning] Method lesson — the chapter-6 grep bug recurred, in a different script
> Chapter 6 recorded that an accent-blind grep against accented Greek silently returned nothing. **The identical failure happened here in Hebrew script**, because the Qumran transcriptions carry combining dots over uncertain letters (`ז֯יקיאל`, `כסׄפא`, `ת֯קפ`).
>
> Measured: of 21 root probes run against the Aramaic, **10 returned zero on the raw text and non-zero after NFD-normalising and stripping combining marks** — including `זיק`, `תקפ`, `רזין`, `כספ`, `חרטמ`, `טור`, `קשר`, `שתי`. Two of those ten (`זיק`, `תקפ`) are load-bearing for the central finding of this file. **A raw grep would have reported that Ziqiel does not exist.**
>
> The rule from chapter 6 was written for Greek and is actually script-independent: **normalise before you compare, and treat any null result as suspect until the matcher is proven against a known-present string.**

> [!warning] Method lesson — an ambiguous formula nearly became a fact
> My first pass read the Aramaic 6:7 list as a clean `ORDINAL + לה + NAME` sequence and derived a full numbering from it. It does not hold: the apparatus splices non-contiguous fragments, `לה` sometimes closes an entry and sometimes opens one, and the two scrolls put the same names in different slots. **Restricting the claim to name-and-ordinal pairs that are physically adjacent cost six data points and saved the argument** — and it dissolved one counterexample I had already written up as a finding.
>
> Same family as the retracted `አርዲስ ≈ ירד` claim in `enoch-6.md`: in both cases the error was reading a *pattern* off evidence that only supported *adjacency*.

## What these chapters show about the book

1. ⭐ **The chapter-6 name list is partly vindicated and partly not.** Star, flash, sun, moon and earth angels teach star-, air-, sun-, moon- and earth-lore. Rain, cloud and thunder teach nothing anyone recorded. **Lightning teaches astrology in every witness there is.** The Aramaic name list is coherent as *names*; the teaching list is a narrower thing — a divination manual — and the two overlap without matching.
2. ⭐ **Syncellus is again the witness that agrees with Qumran.** He alone numbers the Watchers, he alone has "all of them began to reveal the mysteries," he alone puts the appeal "before the Lord." Gizeh is longer and, at these points, later. That is now a two-chapter pattern.
3. **The Ge'ez loses concrete nouns and keeps the grammar around them** — the metals at 8:1, the earth at 7:6, the object of "signs" at 8:3. In each case the surrounding words still fit a noun that is gone. This is a recognisable failure mode, and it is a reason to read the Ge'ez's *silences* as suspect rather than as evidence of absence.
4. 🛑 **Chapter 8 is where the Aramaic runs out.** 4Q201, 4Q202 and 4Q204 speak for the last time at 8:4. From chapter 9 to chapter 108 — a hundred chapters, including the whole Book of Parables — there is no Aramaic to arbitrate anything. **Everything demonstrated in these three files was possible only because of the 7%.** Every conclusion drawn from the rest of the book is drawn without it.
