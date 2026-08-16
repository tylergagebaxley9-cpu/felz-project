# 1 Enoch 6 — The Descent of the Watchers

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

⭐ **Chapter 6 sits inside the 7%.** The Aramaic survives here — in chapters 1–8 and nowhere else in the book — which is why this chapter was chosen first. Four traditions can be compared. For 100 of the 108 chapters, no such check exists.

⚠️ Unlike the Hebrew work, these semantic ranges are **not validator-gated** — `ranges/*.json` and `verify_ranges.py` are Hebrew-only. Same limitation logged for `translations/revelation-3.md`. Stated, not papered over.

### Witnesses cited here

| Siglum | Language | What it is |
|---|---|---|
| `p` | Ethiopic | John Rylands Library Ethiopic 23 (Knibb 1978) |
| `Bertalotto` | Ethiopic | orthographic correction of `p` |
| `Gizeh` | Greek | Codex Panopolitanus (Akhmim) |
| `Syncellus` | Greek | George Syncellus, *Chronographia* |
| `4Q201`, `4Q202`, `4Q204` | Aramaic | Qumran Cave 4 Enoch scrolls |

Brackets `[ ]` in the Aramaic are **editorial reconstruction, not surviving ink.** Where a line reads `…רבו]את קדישו[הי …`, only the unbracketed letters are on the parchment.

---

## ⭐⭐⭐ TWO WORDPLAYS THAT EXIST ONLY IN THE ARAMAIC

This is the finding of the chapter, and it is invisible in every translation ever made from the Ge'ez or the Greek — including Charles.

### 1. Jared / *yarad* — "they descended in the days of Descent"

4Q201 at 6:6 reads `ביומי ירד` — *b-yomey Yared*, "in the days of Jared."

**ירד (y-r-d) is the Semitic verb "to descend."** The verse says the two hundred **descended** in the days of the man whose name *is* "he descended." The name is the event.

- **Ge'ez** `ወወረዱ … ኤርሞን` — translates the verb, transliterates the name. Pun gone.
- **Greek** (Syncellus) `οἱ καταβάντες ἐν ταῖς ἡμέραις Ἰάρεδ` — same loss.
- Only the Aramaic carries both halves in one root.

### 2. Hermon / *ḥerem* — "they put themselves under the ban on the Mountain of the Ban"

4Q201 at 6:5 reads `כחדה ואחרׄמ֯[ו]` and at 6:6 `די ימ֯ו ואח֯ר֯[מו …ב]ה֯` — the verb is **ח־ר־ם (ḥ-r-m)**, "to devote to destruction, to place under the ban, to curse."

**חרמון (Ḥermon) is that root.** The oath they swear and the mountain they swear it on are the *same word*. The text is stating an etymology outright — and the Ge'ez says so ("they called it Mount Hermon **because** they had sworn and bound themselves with curses on it") while making the "because" unintelligible, since ኤርሞን and አውገዙ share nothing.

- **Ge'ez** `ወአውገዙ … ለደብረ፡ ኤርሞን` — accurate sense, no link.
- **Greek** `ἀνεθεμάτισαν … Ἑρμώμ` — accurate sense, no link.
- **Aramaic** `אחרמו … חרמון` — the sentence explains itself.

🛑 Both puns are **structurally unrecoverable** from the Ge'ez or Greek. They are not stylistic flourishes; 6:6 is an *etymological verse* whose entire logic depends on them. A reader of any translation is told there is a reason for the name and is never shown it.

---

## ⭐⭐ THE NAME LIST IS FOUR DIFFERENT LISTS (6:7)

No two witnesses agree. This is the least stable verse in the chapter.

### The leader's name

| Witness | Form |
|---|---|
| Aramaic 4Q201 | **שמיחזה** — *Shemiḥazah* |
| Greek Gizeh | Σεμιαζά |
| Greek Syncellus | Σεμιαζάς |
| Ge'ez (base text) | ስማዝያ — *Səmazəya* |
| Ge'ez ms `p` | ሰሞያዛ — *Semoyaza* |

⭐ The Aramaic **שמיחזה** is transparent Semitic: `שם` (name) + `חזה` (to see / behold) — "my name has seen" or "he sees the Name." Every downstream form is a phonetic shell of it.

### ⭐⭐⭐ The other names are weather and sky — and only the Aramaic shows it

The Aramaic leaders, read as Semitic compounds, are a coherent set:

| Aramaic | Element | Means |
|---|---|---|
| **כוכבאל** Kokab-el | כוכב | **star** of God |
| **ברקאל** Baraq-el | ברק | **lightning** of God |
| **מטראל** Maṭar-el | מטר | **rain** of God |
| **עננאל** Anan-el | ענן | **cloud** of God |
| **שמשיאל** Shamshi-el | שמש | **sun** of God |
| **שהריאל** Sahari-el | שהר | **moon** of God |
| **רעמאל** Raam-el | רעם | **thunder** of God |

🛑 In Gizeh these have become `Κιμβρά, Σαμμανή, Ἀρεαρώς, Χωχαριήλ, Ἀνανθνά, Ῥακειήλ` — meaningless. The Ge'ez likewise: `አኪቢኤል, ጣሚኤል, ዘቄቤ, አራዝያል`.

⭐ **The names are a list of things the sky does**, which is precisely what these angels go on to teach humans in chapters 7–8. The Aramaic list is thematically load-bearing; the translations preserve only noise. This is a case where the *earliest* witness is also the only *intelligible* one.

### ⭐⭐ The Aramaic and Syncellus NUMBER the leaders; Gizeh and Ge'ez do not

4Q201/4Q204 run explicit ordinals — `תנין` (2nd), `תליתי` (3rd), `רביעי` (4th), `חמישי` (5th), `שביעי` (7th), `תמיני` (8th), `תשיעי` (9th), `עסירי` (10th), `חדעסרא` (11th), `תריעסר` (12th), `תלתת עסר` (13th), `ארבעת עסר` (14th), `חמשת עסר` (15th), `שתת עסר` (16th), `שבעת עסר` (17th), `תשעת עסר` (19th), `עסרין` (20th).

Syncellus does the same in Greek letter-numerals: `αʹ Σεμιαζάς … κʹ Σαριήλ`.

**Gizeh and the Ge'ez give a bare list.** So on this verse **Syncellus preserves an older form of the text than Gizeh does** — a conclusion available only because the Aramaic survives to arbitrate. That is worth remembering generally: the fuller manuscript is not automatically the better one.

---

## THE TEXT

> Where the witnesses genuinely differ, all readings are given and none is preferred.
> `( | )` marks a word whose Ge'ez carries more than one sense.

### 6:1

**ወኮነ፡ እምዘ፡ በዝኁ፡ ውሉደ፡ ሰብእ፡ በእማንቱ፡ መዋዕል፡ ተወልዳ፡ ሎሙ፡ አዋልድ፡ ሠናያት፡ ወላሕያት።**

*wäkonä ʾəməzä bäzəḫu wəludä säbəʾə bäʾəmanətu mäwaʿələ täwäləda lomu ʾäwalədə śänayatə wälaḥəyatə*

**And it came to pass, when the children of ʾadam (humankind | men) had become many, in those days daughters were born to them — (good | beautiful | fair) and (comely | lovely | graceful).**

- `ሰብእ` *säbəʾə* — humanity collectively, not males specifically. The Greek `τῶν ἀνθρώπων` is the same ambiguity; both can mean *human beings* or *men*.
- `ሠናያት` *śänayatə* — the root spans **good / beautiful / pleasing**. Moral and aesthetic are not separated.

**Witnesses:**
- Ge'ez `p` ወላህያት / `Bertalotto` ወላሕያት — orthographic only.
- Aramaic 4Q202 `] שפירן ו֯[…` — *shappirin*, "beautiful" (fem. pl.). One adjective visible; the second is lost.
- Greek Gizeh `ὡραῖαι καὶ **καλαί**` — **two** adjectives, agreeing with the Ge'ez.
- Greek Syncellus `ὡραῖαι.` — **one only.**
- Gizeh/Syncellus also differ at the opening: `οὗ ἂν` vs `ὅτε`.

### 6:2

**ወርእዩ፡ ኪያሆን፡ መላእክት፡ ውሉደ፡ ሰማያት፡ ወፈተውዎን፡ ወይቤሉ፡ በበይናቲሆሙ፡ ንዑ፡ ንኅረይ፡ ለነ፡ አንስተ፡ እምውሉደ፡ ሰብእ፡ ወንለድ፡ ለነ፡ ውሉደ።**

*wärəʾəyu kiyahonə mälaʾəkətə wəludä sämayatə wäfätäwəwonə wäyəbelu bäbäyənatihomu nəʿu nəḫəräyə länä ʾänəsətä ʾəməwəludä säbəʾə wänəlädə länä wəludä*

**And the (angels | messengers), the children of the heavens, saw them and (desired | lusted after | took pleasure in) them, and said to one another: "Come, let us choose for ourselves women from among the children of humankind, and let us beget for ourselves children."**

- `መላእክት` *mälaʾəkətə* — **messenger** is the base sense; "angel" is a role, not a separate word. Same relation as Hebrew מלאך / Greek ἄγγελος.
- `ወፈተውዎን` — desire, ranging from **wish/want** to **lust**. The Ge'ez does not itself mark it as sinful.

**Witnesses:**
- ⭐ **Syncellus alone reads `οἱ ἐγρήγοροι`** — "the **Watchers**," the Wakeful Ones. **Gizeh has no such word**, nor does the Ge'ez here. The English title of these beings rests on this one witness at this verse.
- Syncellus `ἀπὸ τῶν **θυγατέρων** τῶν ἀνθρώπων **τῆς γῆς**` — "from the **daughters** of the men **of the earth**"; Gizeh has only `ἀπὸ τῶν ἀνθρώπων`.
- Gizeh alone adds `καὶ γεννήσομεν ἑαυτοῖς τέκνα` — the begetting clause, which the Ge'ez also has (`ወንለድ፡ ለነ፡ ውሉደ`) and Syncellus lacks.
- Aramaic 4Q202 `] ואתמ֯[ללו …` — *and they [spoke]*, a verb of **speaking**, where Ge'ez and Greek open with **seeing**.

### 6:3

**ወይቤሎሙ፡ ስማዝያ፡ ዘውእቱ፡ መልአኮሙ፡ እፈርህ፡ አንሰ፡ ዮጊ፡ ኢትፈቅዱ፡ ይትገበር፡ ዝንቱ፡ ግብር፡ ወእከውን፡ አነ፡ ባሕቲትየ፡ ፈዳይሃ፡ ለዛቲ፡ ኀጢአት፡ ዐባይ።**

**And Shemiḥazah, who was their (chief | leader | angel), said to them: "I fear that perhaps you will not consent that this deed be done, and I alone shall be the one who (pays | repays | discharges the debt for) this great sin."**

- `ፈዳይሃ` — one who **pays / repays**. The Greek makes it explicit: `ὀφειλέτης`, **debtor**. Sin as debt, not as stain.

**Witnesses:** Aramaic **ABSENT**. Latin **ABSENT**. Gizeh `ὃς ἦν ἄρχων αὐτῶν` (relative clause) vs Syncellus `ὁ ἄρχων αὐτῶν` (apposition) — same sense. Ge'ez `p` reads `ለዛቱ … አበይ` for `ለዛቲ … ዐባይ`.

### 6:4

**ወአውሥእዎ፡ ሎቱ፡ ኵሎሙ፡ ወይቤሉ፡ መሐላ፡ ንምሐል፡ ኵልነ፡ ወንትዋገዝ፡ በበይናቲነ፡ ከመ፡ ኢንሚጣ፡ ለዛቲ፡ ምክር፡ ወንግበራ፡ ለዛቲ፡ ምክር፡ ግብረ።**

**And they all answered him and said: "Let us all swear an oath, and let us (bind | curse) one another, that we shall not turn back from this (counsel | plan | decision) — but shall do this counsel as a deed."**

- `ምክር` *məkərə* — **counsel / plan / decision**, and also the *body* that takes it. Same range as Hebrew עצה.
- `ወንትዋገዝ` — reciprocal: to place one another under a curse or ban. **This is the ḥerem verb** in the Aramaic (`ואחרמו`), and the hinge of the Hermon etymology.

**Witnesses:**
- Aramaic is rich here: 4Q201 `] ואמרו לׄה כלהן` (*and they all said to him*), `] נתוב כלנה` (*let us all return/turn back*), `מן מלכהׄ ד֯[ן` (*from th[is] counsel*); 4Q202 `מ]לכא֯ ד֯[ן`, `]נעב֯דׄ` (*let us do*).
- ⭐ Gizeh and Syncellus both add `μέχρις οὗ ἂν τελέσωμεν αὐτὴν` — "**until we have accomplished it**" — a clause **the Ge'ez does not have.** Both Greek witnesses against the Ethiopic.
- Gizeh closes `καὶ ποιήσωμεν τὸ πρᾶγμα τοῦτο`; Syncellus stops.

### 6:5

**አሜሃ፡ መሐሉ፡ ኵሎሙ፡ ኅቡረ፡ ወአውገዙ፡ ኵሎሙ፡ በበይናቲሆሙ፡ ቦቱ።**

**Then they all swore together, and they all placed one another under the ban by it.**

**Witnesses:** Aramaic 4Q201 `] כלהן` / `כחדה ואחרׄמ֯[ו` — *all of them* / *together, and they placed-under-the-ban*. Gizeh `τότε ὄμοσαν πάντες … ἐν αὐτῷ`; Syncellus omits both `τότε` and the closing `ἐν αὐτῷ`, and inverts to `πάντες ὥμοσαν`.

### 6:6

**ወኮኑ፡ ኵሎሙ፡ ክልኤተ፡ ምእተ፡ ወወረዱ፡ ውስተ፡ አርዲስ፡ ዘውእቱ፡ ድማኁ፡ ለደብረ፡ ኤርሞን፡ ወጸውዕዎ፡ ለደብረ፡ ኤርሞን፡ እስመ፡ መሐሉ፡ ቦቱ፡ ወአውገዙ፡ በበይናቲሆሙ።**

**And they were, all of them, two hundred; and they came down onto Ardis, which is the summit of Mount Ḥermon. And they called it Mount Ḥermon, because they had sworn upon it and placed one another under the ban.**

🛑 **This is the verse the wordplays live in.** See the section above — the "because" is only a reason in Aramaic.

**Witnesses:**
- ⭐⭐ **Gizeh is ABSENT for this entire verse.** The Greek survives **only through Syncellus**, who alone carries `ἐν ταῖς ἡμέραις **Ἰάρεδ**` — the days of Jared. Without Syncellus, the Greek tradition would not preserve the name at all.
- Aramaic 4Q201 `] ביומי ירד ע֯ל` and `] די ימ֯ו ואח֯ר֯[מו …ב]ה֯`.
- ⚠️ The Ge'ez base text as printed **lacks "in the days of Jared"**, which both the Aramaic and Syncellus have. Ge'ez has `ውስተ፡ አርዲስ` — "onto **Ardis**" — a place-name where the others have a date. `አርዲስ` and `Ἰάρεδ`/`ירד` are plausibly the same consonants read differently. **Both readings are given; neither is preferred.**
- Mountain name: Ge'ez ኤርሞን / ms `p` አርሞን; Syncellus `Ἑρμονιεὶμ` at first mention, `Ἑρμώμ` at second — the Greek itself is unstable.
- The number is written out in the base text (`ክልኤተ፡ ምእተ`) but as a numeral `፪፻` in ms `p`.

### 6:7

**ወዝንቱ፡ ውእቱ፡ አስማቲሆሙ፡ ለመላእክቲሆሙ፡ …**

**And these are the names of their (chiefs | leaders):** Shemiḥazah, who was their chief — then nineteen more.

🛑 **Four witnesses, four different lists.** See the section above. The Aramaic names are meteorological compounds (star, lightning, rain, cloud, sun, moon, thunder); the Greek and Ge'ez have reduced them to phonetic noise. The Aramaic and Syncellus number them; Gizeh and Ge'ez do not.

**No reconstruction is offered here.** Printing a single harmonised list of twenty names would be inventing a text that no manuscript contains.

### 6:8

**እሉ፡ እሙንቱ፡ ሐበይቶሙ፡ ለክልኤቱ፡ ምእት፡ መላእክት።**

**These are their (chiefs | captains) — of the two hundred (angels | messengers).**

**Witnesses:** ⭐ Here the traditions converge. Aramaic 4Q201 `] אלין אנון רבנין ורב[נ]יא עס֯[ר]תא` — "these are the chiefs, and the chiefs **of tens**"; Greek Gizeh `οὗτοι εἰσιν ἀρχαὶ αὐτῶν οἱ (ἐπὶ) δέκα` — "these are their chiefs, those **over ten**". Both carry a decimal command structure. **The Ge'ez has lost the "of tens"** and reads only "chiefs of the two hundred angels."

---

## What this chapter shows about the book

1. **Where the Aramaic survives, it is not merely older — it is more intelligible.** Two puns and seven meaningful names are recoverable only there.
2. **Syncellus is not a lesser witness.** He alone preserves *the Watchers* (6:2), *the days of Jared* (6:6), and the numbered list (6:7). Gizeh is longer; Syncellus is at points earlier.
3. **The Ge'ez loses small things consistently** — "until we have accomplished it" (6:4), "of tens" (6:8), the Jared date (6:6) — while remaining the only complete text.
4. 🛑 **And for 100 of 108 chapters, none of this checking is possible.** Chapter 6 is the good case. The book's own textual condition should be read off this chapter and then applied as a warning to the rest.
