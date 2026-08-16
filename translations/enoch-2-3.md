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

> [!warning] ⚠️ ADDITIONAL DEFECT IN THIS FILE
> It references **Dindorf, Swete and Black** — all three are **modern editors' conjectures, not manuscripts** (see ENOCH-SURVEY.md). Verify every place they appear and demote them, or the file presents an editor's guess as manuscript evidence.

# 1 Enoch 2–3 — The Order of Nature

**Translated from the Ge'ez, against the Greek, Qumran Aramaic and Latin witnesses. No English translation consulted.**

Built with `tools/enoch.py`, which drops the Charles-1917 `translation` field bundled in the Ge'ez JSON at parse time, with no flag to re-enable it. See PROVENANCE.md. Companion to `translations/enoch-6.md`.

---

## 🛑 Provenance chain — read before the text

**1 Enoch has no complete original-language text.** The chain is:

```
Aramaic (lost, ~7% survives at Qumran)
   └─> Greek (lost, ~44% survives)
          └─> Ge'ez  ← the only complete witness, from late manuscripts
```

⭐ **Chapters 2–3 sit inside the 7%.** Both Qumran scrolls (4Q201, 4Q204) attest every verse here, and the Greek attests every verse (in one case down to a five-word scrap). This is one of only eight chapters in 108 where four-way comparison is possible.

⚠️ These semantic ranges are **not validator-gated** — `ranges/*.json` and `verify_ranges.py` are Hebrew-only. Same limitation logged for `enoch-6.md` and `revelation-3.md`. Stated, not papered over.

### Witnesses cited here

| Siglum | Language | What it is |
|---|---|---|
| *(base)* | Ge'ez | the ethiopian-bible chapter JSON, words field only |
| `p` | Ethiopic | John Rylands Library Ethiopic 23 (Knibb 1978) |
| `Bertalotto` | Ethiopic | orthographic correction of `p` |
| `Gizeh` | Greek | Codex Panopolitanus (Akhmim) |
| `4Q201`, `4Q204` | Aramaic | Qumran Cave 4 Enoch scrolls |
| Latin | — | **ABSENT for all four verses.** The version exists; it does not attest here. |

🛑 The apparatus also carries `Black`, `Swete`, `Charles`, `Dindorf` at 2:2. These are **modern editors' conjectures, not manuscripts**, and `enoch.py` flags them as such. They are recorded below and never counted as evidence.

### 🛑 On the Aramaic brackets — and a defect in the source encoding

Brackets `[ ]` mark **editorial reconstruction, not surviving ink.** Beyond that, transcription dots (Hebrew combining marks `ׄ` / `֯`) mark letters whose ink is present but **uncertain**. Every Aramaic claim below is graded on three levels:

- ✅ **ink** — letter present, no dot, no bracket
- ⚠️ **dotted** — ink present but the editor is not sure of the letter
- 🛑 **recon** — inside brackets; nothing on the parchment

⚠️ **Additional caution: the bracket encoding in the OCP XML is unbalanced.** Six of the eleven Aramaic readings in these two chapters have a `]` with no matching `[`, or an unterminated `[`:

| Reading | `[` | `]` |
|---|---|---|
| 2:1 `4Q201` `וׄלׄא֯ …בס]ר֯כׄן` | 0 | 1 |
| 2:1 `4Q204` `במׄסורתׄ …נהו]ריהוׄ[ן]` | 1 | 2 |
| 2:2 `4Q201` `…]לאחר]נהׄ …` | 3 | 5 |
| 2:2 `4Q204` `…לכ]ו֯ן֯ … ל֯••[` | 1 | 2 |
| 2:3 `4Q204` `…]די כו[ל …` | 1 | 1 (crossed) |
| 3:1 `4Q201` `… מתק֯י֯מ֯י֯ן֯[… [עד ד]…` | 3 | 2 |

Where a word sits next to an unmatched bracket, **its ink status cannot be computed** and is marked ❓ below. This affects two words that would otherwise be headline findings (`סרכן` at 2:1, `נהוריהון` at 2:1). Both are reported as indeterminate rather than claimed.

---

## ⭐⭐⭐ FINDING 1 — The seasons march under BANNERS in the Aramaic

4Q201 at 2:3 reads:

> `[לכן] חזו **לדגלי** [… ע]ל֯יה ו**בדגלי** ש֯תׄוׄא`

**דגל** (*degel*) is a **standard / banner**, and by extension the **division or company that marches under one** — the word of the tribal encampment in Numbers 2. The verse does not say "look at summer and winter." It says **look at the banners of [summer] … and at the banners of winter.** The seasons are troops in formation.

**Ink status — this is the strongest-attested distinctive word in either chapter:**

| Occurrence | As it survives | Status |
|---|---|---|
| 2:3 first | `לדגלי` | ✅ **full ink, every letter, no dots** |
| 2:3 second | `ובדגלי` | ✅ **full ink, every letter, no dots** |
| 4:1 (outside this translation) | `לדׄגׄלי` | ⚠️ ד and ג dotted |

⭐ **Corroboration from outside these chapters:** 4Q201 opens 4:1 with the identical formula `ח֯ז֯וׄ לכן **לדׄגׄלי**`. So `חזו (לכן) לדגלי X` is the **refrain of the whole section**, not a one-off image.

🛑 **Nothing downstream carries it.**
- **Greek 2:3** — `ἴδετε τὴν θερείαν καὶ τὸν χειμῶνα` — plain "the summer and the winter."
- **Ge'ez 2:3** — `ወርእይዎ፡ ለሐጋይ፡ ወለክረምት` — plain, and with **no word at all** in the `דגלי` slot.
- **Ge'ez 4:1** — `ጠየቁ፡ **መዋዕለ**፡ ሐጋይ` — "observe the **days** of summer." The Ge'ez did not merely drop `דגלי`; at 4:1 it **substituted a time-word for a military one.** A banner became a calendar.

⚠️ The Greek is **ABSENT at 4:1**, so the intermediate step cannot be seen. Whether the Greek or the Ge'ez performed the substitution is undetermined.

---

## ⭐⭐⭐ FINDING 2 — One root carries the argument of chapters 2–5, and each version breaks it at a different place

The section's whole logic is: *nature does not change; you changed.* Each witness runs that on a keyword — and the keyword survives to the accusation in only two of the three.

### Aramaic — root שנה, "to change"

| Ref | Reading | Ink status |
|---|---|---|
| 2:2 `4Q201` | `[ל]אשניה` — "to change" | ✅ אשניה ink; ל 🛑 recon |
| 5:2 `4Q201` | `שׄנה` — "changes" | ⚠️ ש dotted |
| 5:4 `4Q201` | `ואנׄתׄן֯ **שניתן** עבדׄכן֯` — "and you, **you have changed** your work" | ✅ שניתן full ink |

⭐ The Aramaic carries שנה **all the way into the accusation.** 5:4 is the punchline and it is on clean parchment.

### Greek — root ἀλλοιόω, "to alter"

`ἠλλοίωσαν` (2:1) · `ἀλλοιοῦνται` (2:2) · `οὐκ ἀλλοιοῦται` (5:2) · `οὐκ ἀλλοιοῦσιν` (5:3) — and then at 5:4, **`ἀλλὰ ἀπέστητε`**, "but you **revolted / stood away**." 🛑 **The Greek chain breaks at the last link.** Four occurrences build the figure and the fifth abandons it.

### Ge'ez — root ዐደወ, "to cross over / transgress"

This is the surprise. `ዐደወ` occurs **exactly twice in all 18,490 word-tokens of Ge'ez Enoch** — verified by root scan:

| Ref | Reading | Who |
|---|---|---|
| 2:1 | `ወኢይትዐደዉ፡ እምትእዛዞሙ` — "and they **do not transgress** their command" | the luminaries |
| 5:4 | `አላ፡ **ተዐደውክሙ**` — "but **you transgressed**" | humankind |

⭐⭐ **The root exists in this book only as this one negated/affirmed pair.** The Ge'ez keeps the inclusio that the Greek dropped — and the Greek's own words at those two points are *different* verbs (`παραβαίνουσιν` at 2:1, `ἀπέστητε` at 5:4). **On this figure the Ge'ez is the better witness**, which is the reverse of the usual direction of travel in this book. It is the same lesson `enoch-6.md` drew about Syncellus: the later text is not automatically the poorer one.

⚠️ 1 Enoch 5 is **outside the chapters translated here**. It is cited as corroboration only; its full apparatus has not been worked through.

---

## ⭐⭐ FINDING 3 — "Order" is a different word in every witness, and the Ge'ez chose "command" on purpose

2:1 is the vocabulary crux of the whole "order of nature" section.

| Witness | Words in the order-slot | Root(s) |
|---|---|---|
| **Aramaic 4Q204** | `במׄסורתׄ` — "in the (ordinance \| bond \| handing-over)" | **מסר** |
| **Aramaic 4Q201** | `…בס]ר֯כׄן` — "in [their] (order \| rule \| array)" | **סרך** ❓ |
| **Greek Gizeh** | `**τεταγμένος** ἕκαστος ἐν τῷ **τεταγμένῳ** καιρῷ … οὐ παραβαίνουσιν τὴν ἰδίαν **τάξιν**` | **τάσσω ×3** |
| **Ge'ez** | `**ሥሩዕ**፡ ኵሉ፡ በበ፡ ዘመኑ … ወኢይትዐደዉ፡ እም**ትእዛዞሙ**` | **śrʿ** then **ʾzz** |

Three observations, each independently checkable:

**(a) The Greek triple is probably the Greek translator's own figure.** The two Aramaic scrolls use **two different roots** (`מסר`, `סרך`) at this verse. Nothing in the surviving Aramaic supports a single-root triple. ⚠️ Both Aramaic words are fragmentary and one is indeterminate; this is an inference from absence and is offered as such.

**(b) The Ge'ez had the word and did not use it.** `ሥርዐት` (*śərʿat*, "order / ordinance / rule") occurs **26 times** in Ge'ez Enoch, densest in the Astronomical Book (74–82, 89, 93, 99, 106, 108). At 2:1, where the Greek says `τάξιν`, the Ge'ez could have written `ሥርዐቶሙ` and instead wrote `ትእዛዞሙ` — **"their command."** This is a lexical choice, not lexical poverty.

**(c) What the choice does.** `ትእዛዝ` renders `πρόσταγμα` elsewhere in this book (18:15 = Ge'ez `ትእዛዘ`), and 18:15 is the stars who **did** transgress. So in Ge'ez, 2:1 and 18:15 become a matched pair — luminaries that keep the command against stars that broke it. The Ge'ez trades a figure of **intrinsic arrangement** (τάξις: also a battle-line, also a rank — the same military register as `דגל` and `סרך`) for a figure of **imposed decree**. The martial metaphor visible in the Aramaic dies here.

⚠️ **Reconstruction warning.** `סרך` is the Qumran technical term for a communal *Rule*. That would be a striking word to find in Enoch — and it **cannot be claimed**. Letter by letter, `בס]ר֯כׄן` is: `ב` ❓ `ס` ❓ (both adjacent to an unmatched `]`), `ר` ⚠️ dotted, `כ` ⚠️ dotted, `ן` ✅ ink. **Only ן is certain.** The word is not evidence for anything on its own. By contrast `במׄסורתׄ` in 4Q204 is `ב` ✅ `מ` ⚠️ `ס` ✅ `ו` ✅ `ר` ✅ `ת` ⚠️ — substantially on the parchment.

---

## ⭐⭐ FINDING 4 — At 3:1 the Ge'ez turns an imperative into a memoir

Every witness opens 3:1 with a **double command to look**:

- **Greek Gizeh** — `καταμάθετε καὶ **ἴδετε** πάντα τὰ δένδρα` — "learn thoroughly and **see** all the trees" (both 2nd person plural imperative)
- **Aramaic 4Q201** — `ח֯ז֯ו֯ ד֯כ֯ל֯ א֯י֯לׄ[ניה]` — `חזו`, "**see!**" (2nd person plural imperative) ⚠️ all three letters dotted
- **Ge'ez** — `ጠየቁ፡ **ወርኢኩ**፡ ከመ፡ ኵሉ፡ ዕፀው` — "observe, **and I saw**, how all the trees…"

`ወርኢኩ` *wä-rəʾiku* is a **first person singular perfect**. The plural imperative would be `ወርእዩ` *wä-rəʾəyu*.

⭐ **Both Ethiopic witnesses (`p` and `Bertalotto`) carry the first-person form**, so the reading is older than either manuscript.

⚠️ **Measured, and offered as observation not emendation:** `ወርኢኩ` "and I saw" occurs **91 times** in Ge'ez Enoch — it is the book's single most common narrative formula, the refrain of the Watchers and Astronomical visions. `ወርእዩ` "and see!" occurs **4 times**. A rare imperative standing beside a 91× formula is the classic setting for assimilation. But the Ge'ez says what it says, and the alternative — that its Vorlage genuinely read "I saw" — is not excluded. **Both are stated; neither is preferred, and the text is not corrected.**

The rest of the section keeps the imperative intact in Ge'ez (`ጠየቁ` at 2:1, 3:1, 4:1, 5:1 — exactly four times in the book, exactly the four openings of this section; `ወርእይዋ` 2:2, `ወርእይዎ` 2:3). So the slip, if it is one, is local to a single word.

---

## ⭐ FINDING 5 — Three fewer things happen in the Ge'ez sky

| Detail | Aramaic | Greek | Ge'ez |
|---|---|---|---|
| "for yourselves" (ethical dative) | `לכון` ✅ ink (2:2 `4Q204`); `לכן` 🛑 recon (2:3); `לכן` (4:1) | `ὑμῖν φαίνεται` (2:2 only) | **absent throughout** |
| the earth's works are **perishable** | *(lacuna)* | `ὥς εἰσιν **φθαρτά**` (2:2) | **absent** |
| rain **pours** | `ש֯פ֯כ֯י֯ן֯` ⚠️ all 5 dotted (2:3) | *(lacuna)* | `የዐርፉ` — "**rest / settle** upon it" |

- ⭐ **`לכון`, "for yourselves,"** is the Aramaic's signature. It is on clean ink at 2:2 in 4Q204 and recurs at 4:1. The Greek preserves one trace of it (`ὑμῖν` at 2:2); the Ge'ez base text has none, ending 2:2 with a bare `ዘያስተርኢ`, "which appears."
- ⭐ **`φθαρτά`, "perishable,"** is in Gizeh and in nothing else. It also sits oddly beside the very next clause, `ὡς οὐκ ἀλλοιοῦνται` ("how they do not change"). No manuscript variant is offered; the tension is in the Greek itself. **Recorded, not resolved.**
- ⚠️ **Rain: `שפכין` vs `የዐርፉ`.** "Pouring out" against "resting upon" is a real difference in image — active against static. But every one of the five letters of `שפכין` is dotted, and the noun beside it, `[מט]ר֯ה֯` "rain", is 🛑 reconstructed in its first two letters and ⚠️ dotted in the other two. **This divergence rests on uncertain ink and a largely editorial noun. It is flagged, not argued.**

---

## ⚠️ FINDING 6 — "Fourteen trees" has no support outside the Ge'ez, and 4Q204 may read "four"

Ge'ez 3:1: `ዘእንበለ፡ **ዐሠርቱ፡ ወአርባዕቱ**፡ ዕፀው` — "except **fourteen** trees" (base text writes it out; both Ethiopic mss use the numeral `፲ወ፬`).

The Greek at 3:1 survives as five words with lacunae on both sides — **the number is not in it.**

4Q204 at 3:1 reads `…**ארבעת֯** ב֯רׄא די…` at the corresponding point:

| Letter | א | ר | ב | ע | ת |
|---|---|---|---|---|---|
| status | ✅ | ✅ | ✅ | ✅ | ⚠️ |

`ארבעת` is **"four"** in the construct/counting form. The teen-element that would make it *fourteen* is **not in the surviving text.** For comparison, the same scroll family writes "fourteenth" at 6:7 as `[אר]בעת אעאס֯ר` (4Q201) and `ארבעת עשר]י` (4Q202) — i.e. `ארבעת` **+ עסר/עשר**. Here `ארבעת` is followed by `ב֯רׄא` (⚠️ ב and ר dotted, ✅ א), which I **cannot identify**; it is not a teen-marker.

🛑 **I could not determine whether the Aramaic read four or fourteen.** The fragment breaks, `ב֯רׄא` is unread, and `עסר` could stand in the lacuna. What can be said: **the number fourteen is attested by the Ge'ez alone**, and the one other witness at that point has `ארבע` in clear ink with no teen-element beside it. Nothing is harmonised.

⭐ The **duration** at the end of the same verse is the opposite case — there the Aramaic settles a Ge'ez ambiguity. See 3:1 below.

---

## THE TEXT

> Where the witnesses genuinely differ, all readings are given and none is preferred.
> `( | )` marks a word whose Ge'ez carries more than one sense.

### 2:1

**ጠየቁ፡ ኵሎ፡ ዘውስተ፡ ሰማይ፡ ግብረ፡ እፎ፡ ኢይመይጡ፡ ፍናዊሆሙ፡ ብርሃናት፡ ዘውስተ፡ ሰማይ፡ ከመ፡ ኵሉ፡ ይሠርቅ፡ ወየዐርብ፡ ሥሩዕ፡ ኵሉ፡ በበ፡ ዘመኑ፡ ወኢይትዐደዉ፡ እምትእዛዞሙ።**

*ṭäyäqu kwəlo zäwəsətä sämayə gəbərä ʾəfo ʾiyəmäyəṭu fənawihomu bərəhanatə zäwəsətä sämayə kämä kwəlu yəśärəqə wäyäʿärəbə śəruʿə kwəlu bäbä zämänu wäʾiyətəʿädäwu ʾəmətəʾəzazomu*

**(Examine | Observe | Scrutinise) every (work | deed | making) that is in heaven — how they do not (turn | change | alter) their (paths | ways | roads), the (lights | luminaries) that are in heaven; how each one (rises | shines forth | breaks out) and (sets | goes down), (ordered | arranged | appointed | drawn up), each one in its own (time | season | age); and they do not (transgress | cross over | overstep) their (command | ordinance | precept).**

- `ጠየቁ` *ṭäyäqu* — imperative plural, root *ṭyq*: **examine, inquire into, scrutinise**. Occurs 4× in the book, at 2:1, 3:1, 4:1, 5:1 — the four openings of this section and nowhere else.
- `ግብረ` *gəbərä* — **work / deed / act**, root *gbr*. The same root returns as `ወኢገበርክሙ` "you did not **do**" at 5:4, so the Ge'ez keeps a link the Greek (`ἔργα` … `ἐποιήσατε`) does not.
- `ፍናዊሆሙ` — plural of `ፍኖት` **way / road / path**. Greek `ὁδούς` matches exactly.
- `ሥሩዕ` *śəruʿə* — passive participle of `ሠርዐ` "to **order, arrange, set in place, ordain**." This exact form is a **hapax in Ge'ez Enoch** (1 of 18,490 tokens); the verb appears once more at 5:2, and the noun `ሥርዐት` 24 more times.
- `በበ፡ ዘመኑ` — `በበ` is a **distributive** ("each in its own"); `ዘመን` = **time / season / epoch / age**.
- `ትእዛዝ` *təʾzaz* — **command / ordinance / precept / mandate**, root *ʾzz* "to command." Not an order-word. See Finding 3.

**Witnesses:**
- **Ge'ez `p` / `Bertalotto`** agree with the base against three details: both read `በዘመኑ` — **without the distributive `በበ`**. Greek `ἕκαστος ἐν τῷ τεταγμένῳ καιρῷ` supports a distributive; the base Ge'ez preserves it and both manuscripts have lost it.
- Orthographic only: `ወየዐርብ`/`ወየዓርብ`, `ወኢይትዐደዉ`/`ወኢይትዓደዉ`. `p` reads `እምትዛዞሙ` — haplography of the `እ` in `ትእዛዝ`.
- **Greek Gizeh** (sole Greek witness): `Κατανοήσατε πάντα τὰ ἔργα ἐν τῷ οὐρανῷ, πῶς **οὐκ ἠλλοίωσαν** τὰς ὁδοὺς αὐτῶν…` ⭐ `ἠλλοίωσαν` is **aorist** — "they did not alter" — against the Ge'ez imperfect `ኢይመይጡ` ("they do not alter"). A completed past against an ongoing present.
- ⭐ **Greek alone adds `καὶ ταῖς ἑορταῖς αὐτῶν φαίνονται`** — "and **at their feasts** they appear." No Ge'ez equivalent; the Aramaic is broken at that point. A **cultic/calendrical** clause present only in Greek.
- **Aramaic 4Q204** `ל[כ]ו[ן]  ש֯[מיא לעובד …` — "for [yo]u … the he[avens, to the work of …]". ⚠️ `לכון`: ל ✅ כ 🛑 ו ✅ ן 🛑. `ש֯[מיא` — **only the ש has ink, and it is dotted**; "the heavens" is otherwise editorial. `לעובד` is 🛑 **wholly reconstructed**. This reading proves very little on its own.
- **Aramaic 4Q201** `וׄלׄא֯ …בס]ר֯כׄן` — "and not … in [their] order/rule". ⚠️❓ see Finding 3; only `ן` is certain ink.
- **Aramaic 4Q204** `במׄסורתׄ …נהו]ריהוׄ[ן] כולה[ו]ן דׄי …` — "in the (ordinance | bond | handing-over) of … [the ligh]ts of them, all of them, which…". `במסורת` substantially ✅ ink. ❓ `נהו` sits past an unmatched `]`, so the **stem of "their lights" may be editorial**; what is certainly on parchment is `ריהו` + `כולהון`.
- **Latin: ABSENT.**

### 2:2

**ወርእይዋ፡ ለምድር፡ ወለብዉ፡ በእንተ፡ ምግባር፡ ዘይትገበር፡ ላዕሌሃ፡ እምቀዳሚ፡ እስከ፡ ተፍጻሜቱ፡ ከመ፡ ኢይትመየጡ፡ ኵሉ፡ ግብሩ፡ ለአምላክ፡ ዘያስተርኢ።**

*wärəʾəyəwa lämədərə wäläbəwu bäʾənətä məgəbarə zäyətəgäbärə laʿəleha ʾəməqädami ʾəsəkä täfəṣametu kämä ʾiyətəmäyäṭu kwəlu gəbəru läʾäməlakə zäyasətärəʾi*

**And see it — the earth — and (understand | perceive | take to heart | consider) concerning the (work | deed | practice) that is done upon it, from the (first | beginning) until its (completion | end | fulfilment | consummation): how it is not (turned | changed | altered), all the work of God, which (appears | is manifest | is visible).**

- `ወለብዉ` *wäläbəwu* — root *lbb*, "heart": **understand / perceive / be intelligent / take to heart**. Not a neutral "look."
- `ተፍጻሜት` *täfṣamet* — **completion / end / fulfilment / consummation**, root *fṣm*. The Greek `τελείωσις` carries the same double edge (a stop and a perfecting).
- `ዘያስተርኢ` — `አስተርአየ`, causative-reflexive of "to see": **appear / show itself / be made manifest**.

**Witnesses:**
- ⭐ **Ge'ez base vs manuscripts, a real difference:** base `**በእንተ**፡ ምግባር` = "**concerning** the work"; `p`/`Bertalotto` `**እም**ግብር` = "**from / out of** the work." Greek `**περὶ** τῶν ἔργων` supports the base text.
- Base `ኢይትመየጡ` (**plural**) vs mss `ኢይትመየጥ` (**singular**). Greek `ἀλλοιοῦνται` is plural.
- ⭐ Base ends `ዘያስተርኢ።` — a statement. Both mss end `**እንዘ**፡ ያስተርኢ**፧**` — "while it appears**?**", **punctuated as a question** (`፧`). Greek is flatly declarative: `ὑμῖν φαίνεται`. **All three readings given; none preferred.**
- Base `ወርእይዋ` / `Bertalotto` `ርአይዋ` / `p` `ርእይዋ`.
- **Greek Gizeh** `ἴδετε τὴν γῆν καὶ διανοήθητε περὶ τῶν ἔργων τῶν ἐν αὐτῇ **γεινομενων** ἀπ᾽ ἀρχῆς μέχρι τελειώσεως **ὥς εἰσιν φθαρτά**, ὡς οὐκ ἀλλοιοῦνται, οὐδὲν τῶν ἐπὶ γῆς, ἀλλὰ πάντα ἔργα θεοῦ **ὑμῖν** φαίνεται.`
  - 🛑 The apparatus offers `γενομένων` [Black] and `γινομένων` [Swete Charles Dindorf] for the manuscript's `γεινομενων`. **All three are modern editors' spellings of the same participle; only `γεινομενων` is in a manuscript.** They are not variant readings and are not counted as witnesses.
  - `φθαρτά` and `ὑμῖν` are Greek-only. See Finding 5.
- **Aramaic 4Q201** `חׄ[זו] **לארעה** ו**א[תבו]נ֯נׄו** **בעבדה**[…` — "S[ee] **the earth** and **c[onsi]der** **its work**". ✅ `לארעה` and `בעבדה` are **fully on ink**. ⭐ Note `ל` as the object marker — exactly what the Ge'ez does with `ለምድር`, and what the Greek does not (`τὴν γῆν`, bare accusative). A Semitic construction that jumps the Greek and lands in the Ge'ez.
- **Aramaic 4Q204** `לכון חזוא … ואתבוננא ל[א]ר֯עאׄ **בעעו֯בדׄ**[ה …` — ✅ `לכון`, `חזוא`, `ואתבוננא` **all fully on ink**. ⚠️ `בעעובד` is written with a **doubled ע, both letters on ink** — an apparent **dittography visible in the scroll itself**. Recorded as it stands; not silently corrected.
  - ⭐ 4Q201 `חזו` / `אתבוננו` vs 4Q204 `חזוא` / `אתבוננא` — **the two Aramaic scrolls differ in orthography from each other.** Textual variation exists *within* the Aramaic, not only downstream of it.
- **Aramaic 4Q201** `…]לאחר]נהׄ ד**מ[נ]ד[עם]** …[ל]**אשניה** וכל **מתח[ז]א**` — "…to the last, that no[thi]ng … **changes**, and everything **is seen**." ✅ `אשניה` (root שנה, Finding 2) and `מתחזא` largely on ink.
- **Aramaic 4Q204** `…לכ]ו֯ן֯ **מתחזאׄ** ל֯••[` — "…to yo]u **it is visible**". ✅ `מתחז` ink. The `••` are illegible traces. This matches Greek `ὑμῖν φαίνεται` word for word — and the Ge'ez has lost the "to you."
- **Latin: ABSENT.**

### 2:3

**ወርእይዎ፡ ለሐጋይ፡ ወለክረምት፡ ከመ፡ ኵላ፡ ምድር፡ መልአት፡ ማየ፡ ወደመና፡ ወጠል፡ ወዝናም፡ የዐርፉ፡ ላዕሌሃ።**

*wärəʾəyəwo läḥägayə wäläkərämətə kämä kwəla mədərə mäləʾätə mayä wädämäna wäṭälə wäzənamə yäʿärəfu laʿəleha*

**And see it — the (dry season | summer) and the (rainy season | winter): how the whole earth is filled with water, and (cloud | clouds) and dew and rain (rest | settle | alight | come to rest) upon it.**

- ⭐⭐ `ሐጋይ` / `ክረምት` are **not a temperature pair.** In Ge'ez `ሐጋይ` is the **dry season** and `ክረምት` the **rainy season** — the Ethiopian year is divided by water, not by heat. The Greek pair `θερεία` / `χειμών` is summer/winter. Because this verse is *about water filling the earth*, the Ge'ez pair reads as the *cause* of the sentence, while the Greek pair reads as mere calendar. The translation cannot carry both; both senses are printed.
- `የዐርፉ` *yäʿärəfu* — root *ʿrf*, **to rest / repose / settle / come to rest**. Base text plural; both mss singular `የዐርፍ`.

**Witnesses:**
- Ge'ez base `ኵላ፡ ምድር` (feminine agreement) vs mss `ኵሉ፡ ምድር` (masculine). Base `ወለክረምት` vs mss `ወላክረምት`. Base `የዐርፉ` (pl.) vs `Bertalotto` `የዐርፍ` / `p` `የአርፍ` (sg.).
- **Greek Gizeh** — `ἴδετε τὴν θερείαν καὶ τὸν χειμῶνα ...` ⚠️ **The Greek breaks off here.** The ellipsis is in the source, marking a lacuna. Six words survive; everything about water, cloud, dew and rain is lost in Greek.
- **Aramaic 4Q201** `[לכן] **חזו לדגלי** [… ע]ל֯יה ו**בדגלי** ש֯תׄוׄא דׄ[כל] **ארעא** [וע]**ננה** [מט]ר֯ה֯ ש֯פ֯כ֯י֯ן֯` — see Finding 1. Ink grading: `חזו` ✅, `לדגלי` ✅, `ובדגלי` ✅, `ארעא` ✅, `ננה` ✅ but `[וע]` 🛑 (so "**cloud**" depends on a reconstructed ע), `שתוא` "winter" ⚠️ (ש,ת,ו dotted; only א clean), `[מט]ר֯ה֯` "rain" 🛑⚠️ (mostly editorial), `ש֯פ֯כ֯י֯ן֯` "pouring" ⚠️ (all five dotted). 🛑 `[לכן]` is **entirely reconstructed here** — the "for yourselves" of this verse is editorial, though the same word is ✅ ink at 2:2 in the other scroll.
- **Aramaic 4Q204** `…]די כו[ל …` — "…which all…". Two words; nothing determinable.
- **Latin: ABSENT.**

### 3:1

*(Chapter 3 is a single verse in the Ge'ez.)*

**ጠየቁ፡ ወርኢኩ፡ ከመ፡ ኵሉ፡ ዕፀው፡ እፎ፡ ያስተርእዩ፡ ከመ፡ ይቡስ፡ ወኵሉ፡ አቍጽሊሆሙ፡ ንጉፋት፡ ዘእንበለ፡ ዐሠርቱ፡ ወአርባዕቱ፡ ዕፀው፡ ዘኢይትነገፉ፡ እለ፡ ይጸንሑ፡ እምብሉይ፡ እስከ፡ ይመጽእ፡ ሐዲስ፡ እምክልኤቱ፡ ወሠለስቱ፡ ክረምት።**

*ṭäyäqu wärəʾiku kämä kwəlu ʿəṣ́äwə ʾəfo yasətärəʾəyu kämä yəbusə wäkwəlu ʾäqwəṣəlihomu nəgufatə zäʾənəbälä ʿäśärətu wäʾärəbaʿətu ʿəṣ́äwə zäʾiyətənägäfu ʾəlä yəṣänəḥu ʾəməbəluyə ʾəsəkä yəmäṣəʾə ḥädisə ʾəməkələʾetu wäśäläsətu kərämətə*

**(Examine | Observe | Scrutinise) — and I saw — how all the trees (appear | show themselves | are made visible) as though (dry | withered | parched), and all their leaves are (shed | shaken off | stripped away); except fourteen trees which are not (shed | stripped | shaken off), which (wait | remain | endure | persist) from the old until the new comes, over two and three (rainy seasons | winters | years).**

- ⚠️ `ወርኢኩ` — "**and I saw**", 1st person singular. See Finding 4. The parallel witnesses have a plural imperative; the Ge'ez is not corrected here.
- `ይቡስ` *yəbusə* — **dry / withered / parched**, root *ybs*. ⭐ The Aramaic has the **same Semitic root**: `מיבישין` (*myabbishin*), ✅ **fully on ink**. One of the few points in this book where a root survives intact from Aramaic to Ge'ez across the lost Greek.
- `ንጉፋት` … `ዘኢይትነገፉ` — ⭐ a **root-figure the Ge'ez does keep**: `ነገፈ` "to shake off, shed, strip." The root occurs **exactly twice in all of Ge'ez Enoch, both in this verse** — once affirmed of the many trees, once negated of the fourteen. The verse is built on it.
- `ይጸንሑ` — **wait / remain / endure / persist**. Aramaic has `מתק֯י֯מ֯י֯ן֯` (root **קום**, "to stand / be established / endure") — ⚠️ מת ✅ ink, קימין dotted. "Standing firm" against "waiting" is a shift of image, though not of sense.
- ⭐⭐ `ክረምት` here is the crux. In 2:3 it was the **rainy season**, paired against `ሐጋይ`. Here it counts a duration — "two and three `ክረምት`" — and could be **rainy seasons, winters, or years**. **The Aramaic settles it:** 4Q204 reads `דתרתין ודתלת **שניׄןׄ**` — **`שנין`, "years"** (`שנ` ✅ ink, `ין` ⚠️ dotted), and 4Q201 reconstructs `[שנין יעברן]` 🛑 at the same point. So the Ge'ez ambiguity is a **rainy-season-for-year** substitution — natural where there is one rainy season a year. All three senses are printed above; the Aramaic evidence for "years" is noted, not silently adopted.
- ⭐ `ይቡስ` again at 5:4 as `**ይቡሳነ፡ ልብ**` — "**dry of heart**" — where Greek has `σκληροκάρδιοι`, "**hard**-hearted", and where the same Greek verse uses `σκληρούς` for `ድሩካተ` "hard (words)". So the Ge'ez chose a *different* word for the hearts than for the words, and the word it chose is **the word for the withered trees of 3:1**. ⚠️ The Aramaic adjective at 5:4 is inside a lacuna (`[…לבב]ן`), so **whether the Ge'ez preserves this link or created it cannot be determined.**

**Witnesses:**
- ⭐ **Ge'ez manuscripts disagree with each other on a conjunction:** `p` reads `**እለ**፡ ይጸንሑ` ("**which** wait"); `Bertalotto` reads `**አላ**፡ ይጸንሑ` ("**but** they wait"). The base text has `እለ`. **Both given.**
- Numerals: base writes them out (`ዐሠርቱ፡ ወአርባዕቱ`, `እምክልኤቱ፡ ወሠለስቱ`); both mss use Ethiopic numerals (`፲ወ፬`, `እም፪ኤ፡ ወእም፫`).
- ⭐⭐ **A preposition doubled in exactly matching places.** The Ethiopic mss read `**እም**፪ኤ፡ **ወእም**፫፡ ክረምት` — repeating `እም` ("from") before *both* numbers, where the base text has it once (`እምክልኤቱ፡ ወሠለስቱ`). 4Q204 reads `**ד**תרתין ו**ד**תלת` — repeating the proclitic `ד` before both, ✅ **fully on ink**; 4Q201 reads `[עד ד]תרתין ותלת` with only one, and that one 🛑 reconstructed. **The two Aramaic scrolls split exactly as the two Ge'ez forms split.** ⚠️ Whether this is transmission or coincidence of a common idiom cannot be determined from two data points, and no conclusion is drawn.
- **Greek Gizeh** `. . . καταμάθετε καὶ ἴδετε πάντα τὰ δένδρα . . .` — ⚠️ **five words between two lacunae.** The ellipses are in the source. The Greek attests only the opening command; it says nothing about dryness, leaves, the number fourteen, or the duration.
- **Aramaic 4Q201** `ח֯ז֯ו֯ ד֯כ֯ל֯ א֯י֯לׄ[ניה] כ֯ל֯הׄן֯ **מיבישין** [… ]מ֯ן֯ …[ע]ל֯יהן **מתק֯י֯מ֯י֯ן֯**[… [עד ד]תרתין֯ ותלת [שנין יעברן]` — ⚠️ almost every letter of the opening (`חזו דכל אילניה כלהן`) is **dotted**; `[ניה]` and `[עד ד]` and `[שנין יעברן]` are 🛑 reconstructed. `מיבישין` ✅ is the one clean word.
- **Aramaic 4Q204** `מן עלי]ה֯ון …**ארבעת֯** ב֯רׄא די [… ]**דתרתין ודתלת שניׄןׄ**` — see Finding 6 for `ארבעת`, above for `שנין`.
- **Latin: ABSENT.**

---

## Verification pass — what was checked, and what it changed

Every load-bearing claim was re-checked against the XML and the Ge'ez word-tokens rather than against my reading of them. The Ge'ez `translation` field was never opened.

| Claim | Result |
|---|---|
| `דגלי` on clean ink twice at 2:3 | ✅ confirmed letter-by-letter; also at 4:1 (dotted) |
| Ge'ez 4:1 renders that slot as `መዋዕለ` "days" | ✅ confirmed |
| Greek 2:1 has three τάσσω-root words | ✅ `τεταγμένος`, `τεταγμένῳ`, `τάξιν` — after NFD normalisation |
| Ge'ez root `ዐደወ` occurs only at 2:1 and 5:4 | ✅ confirmed, 2 tokens in 18,490 |
| Greek breaks its ἀλλοιόω chain at 5:4 | ✅ `ἀπέστητε`, not ἀλλοιόω |
| Aramaic keeps שנה through to 5:4 | ✅ `שניתן` on clean ink |
| `ሥርዐት` "does not occur in Enoch" | 🛑 **FALSE — retracted.** 26 tokens. See method note below |
| `ሥሩዕ` is a hapax form | ✅ 1 of 18,490 tokens; but the **root is not** hapax |
| `ነገፈ` root confined to 3:1 | ✅ 2 tokens, both in 3:1 |
| Ge'ez 3:1 reads a 1cs perfect where Greek/Aramaic read an imperative | ✅ confirmed in base and in both Ethiopic mss |
| `ወርኢኩ` is the book's dominant formula | ✅ 91 occurrences vs 4 for `ወርእዩ` |
| Aramaic read "fourteen" at 3:1 | 🛑 **UNDETERMINED** — `ארבעת` is ink, no teen-element survives, `ב֯רׄא` unidentified |
| `סרך` in the Aramaic of 2:1 | ⚠️ **not claimable** — only `ן` is certain ink, and the word abuts an unmatched bracket |
| Latin attests 2:1–3:1 | ✅ **ABSENT** at all four verses |

> [!warning] Method lesson — the accent-blind search failed again, in Ethiopic this time
> I first searched the Ge'ez tokens for the stem `ሥርዓ` (with `ዓ`, ʿalef-form) and got **zero hits**, and nearly wrote that Ge'ez Enoch has no word for "order." The actual form uses `ዐ` (ʿayn-form): `ሥርዐተ`, `ሥርዐቶሙ`, `ሥርዐታት` — **26 tokens**, concentrated in the Astronomical Book.
>
> This is the *same failure mode* `enoch-6.md` logged for unaccented Greek against accented text, transposed into Ethiopic: two visually near-identical characters, a silent zero, and a conclusion that would have read as a finding. It changed the argument's polarity — from "the Ge'ez lacked the word" to "**the Ge'ez had the word and chose not to use it**," which is a much stronger and quite different claim.
>
> 🛑 **Rule, restated because restating it did not prevent the recurrence:** normalise before comparing, and treat any null result as *suspect* until the matcher is proven against a known-present string. A search that cannot match is indistinguishable from a claim that is false — in every script, not just Greek.

> [!warning] Method lesson — bracket encoding cannot be trusted to be balanced
> My first pass computed ink-vs-reconstruction by tracking bracket depth through each Aramaic reading. It reported `ב` and `ס` of `בס]רכן` as **ink**, because the closing `]` had no opener and the depth counter never went positive. Six of the eleven Aramaic readings here have unbalanced brackets.
>
> A depth counter on unbalanced input does not fail — it returns a confident wrong answer, and the wrong answer was in the *permissive* direction, promoting editorial reconstruction to surviving evidence. That is precisely the error Rule 2 exists to prevent. Affected words are marked ❓ and no claim rests on them.

## What these chapters show about the book

1. **The Aramaic thinks in military formation.** `דגלי` (banners/divisions, ×2 clean ink at 2:3, again at 4:1) and probably `סרך` (rule/array) put the luminaries and seasons in *ranks*. The Greek half-keeps it — `τάξις` is also a battle-line — and the Ge'ez converts it to **days** and **commands**. What survives in translation is obedience; what is lost is the parade.
2. **Each version breaks the section's keyword-chain at a different link**, and the Ge'ez is the one that keeps it to the end (`ዐደወ`, 2:1 ↔ 5:4). ⭐ **The latest witness is not uniformly the worst.** Same conclusion `enoch-6.md` reached about Syncellus, by a completely different route.
3. **Small things are gone from the Ge'ez**: "for yourselves" (`לכון`/`ὑμῖν`), "perishable" (`φθαρτά`), "at their feasts" (`ταῖς ἑορταῖς`), the distributive `በበ` in both manuscripts.
4. **A number stands on one witness.** "Fourteen trees" is Ge'ez-only; the Greek is lacunose and the Aramaic has `ארבע` in clear ink with nothing beside it. This is what most of 1 Enoch looks like — except that here we can *see* that it stands on one witness.
5. 🛑 **And for 100 of the 108 chapters, none of this checking is possible.** Chapters 2–3 are among the eight good cases. Read the book's textual condition off these chapters, then apply it as a warning to the rest.
