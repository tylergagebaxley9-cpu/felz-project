# Three questions: the gender of God, the delay, and the watching

**OURS — REPORT.** Not a translation of a passage. Every Hebrew form below was regenerated from
`hebrew-ot/morphhb/wlc` via `tools/analyze.py`, which emits no English gloss. Counts come from
direct parse of the WLC morphology. No English translation was consulted.

> ⚠️ **Limit, stated up front:** of the roots cited here, only ה־י־ה, א־מ־ר, ב־ן, א־ל־ה־ים, י־ה־ו־ה
> and seven others have validator-gated sense ranges in `ranges/`. The rest (ילד, חיל, פתה, עזב,
> נכון…) are cited by **form and distribution**, which is fact, not by a derived sense range.
> Where I give a meaning for an underived root, it is inferred from its own occurrences listed here
> and nowhere else. See `verify_ranges.py`.

---

## 1. Why is YHWH a "he"?

### The grammar is a grammar, and the text says so

Hebrew has two genders and no neuter. Every noun is one or the other; there is no third option
for a table, a stone, or a god. `אלהים` in Gen 1:27 parses `HNcmpa` — noun common **masculine
plural** absolute — and takes a **3ms** verb (`ויברא`, `HVqw3ms`). That is agreement, not anatomy.

The test case is `רוח`. Parsed across the whole WLC:

```
H7307 as a noun:  271 tokens
  gender "b" (common / either):  271
  gender "m":  0
  gender "f":  0
```

**271 of 271.** The morphology dataset itself refuses to assign it a gender, because its agreement
in the text swings both ways. Hebrew gender is a class marker that sometimes carries sex and
sometimes carries nothing.

### The text explicitly forbids fixing him to a sex

Deut 4:15–16, regenerated:

```
כי לא ראיתם כל תמונה   ...   פן תשחתון ועשיתם לכם פסל תבנית כל סמל
                              תבנית זכר או נקבה
```

`תבנית` (`HNcfsc`, construct) governs `זכר` (`HAamsa`) `או` `נקבה` (`HNcfsa`). The prohibition is
not "don't carve an animal." It names **male or female** as the two forms you must not make him
into. The stated ground is `לא ראיתם כל תמונה` — you saw no form at all.

### And the text repeatedly puts him in the female role

| ref | Hebrew | parse |
|---|---|---|
| Deut 32:18 | `צור ילדך תשי` | `ילד` = **HVqp3ms** — the ordinary verb for bearing a child |
| Deut 32:18 | `אל מחללך` | `חיל` H2342, **polel participle** — the verb of writhing / labour pains |
| Isa 42:14 | `כיולדה אפעה` | `ילד` **HVqrfsa** — "like a *woman giving birth* I groan" — God's own speech, 1cs |
| Isa 66:13 | `כאיש אשר אמו תנחמנו כן אנכי אנחמכם` | `תנחמנו` **HVpi3fs** — the comforter in the simile is a **mother**; God takes her position |
| Num 11:12 | `האנכי הריתי … אם אנכי ילדתיהו` | Moses, **1cs**, throws conception and birth back — he is refusing a role he assumes is not his |
| Gen 1:27 | `בצלם אלהים ברא אתו זכר ונקבה ברא אתם` | the image is filled by **`זכר ונקבה`**, both |

`ילד` in Deut 32:18 and `ילד` in Isa 42:14 are **the same root**, one said of God as subject,
one said by God of himself.

### So

The "he" is (a) a grammatical requirement of a language with no neuter, (b) the pronoun of the
culture that wrote it, and (c) something the text itself works against — once by explicit
prohibition (Deut 4:16), repeatedly by using birth-language of him, and once by putting the image
in a male-and-female pair rather than in a male alone.

Nothing here shows the writers thought he *was* female either. It shows they thought the category
did not apply and kept saying so with the only pronouns they had.

---

## 2. Why hasn't he undone the slavery by now?

### The text does not deny the delay. It puts a number on it.

**Gen 15:13** — God speaking to Abram, in advance:

```
ידע תדע כי גר יהיה זרעך בארץ לא להם ועבדום וענו אתם ארבע מאות שנה
```

`ידע תדע` is infinitive absolute + imperfect: *knowing you shall know*. The affliction is
**announced four hundred years before it is stopped**, by the one announcing it.

**Exod 12:40** — `שלשים שנה וארבע מאות שנה`. Four hundred and thirty.

**Exod 2:23–25** — what happened during it:

```
ויאנחו בני ישראל מן העבדה ויזעקו
ו/ישמע אלהים את נאקתם ויזכר אלהים את בריתו
ו/ירא אלהים את בני ישראל ו/ידע אלהים
```

Note the last three words. **`וידע אלהים` — "and God knew." The verse ends there.** No object.
No verb of action. `ראה` / `שמע` / `ידע` — saw, heard, knew — and the chapter stops.

**Exod 3:7** is the same three verbs in the first person, intensified: `ראה ראיתי` (inf. abs. +
perfect), `שמעתי`, `ידעתי`.

The book that is supposed to be the rescue story spends its opening on the fact that he was
**watching and not moving**, and it does not apologise for it or explain it.

### The complaint you are making is inside the canon, in the same words

| ref | Hebrew | what the parse shows |
|---|---|---|
| Hab 1:2 | `עד אנה יהוה שועתי ולא תשמע אזעק אליך חמס ולא תושיע` | `תשמע` **2ms**, `תושיע` **hiphil 2ms** — "you do not hear," "you do not save," said *to his face* |
| Ps 44:24 | `עורה למה תישן אדני` | `עורה` **imperative 2ms** — *wake up* — and `תישן` **HVqi2ms**, "why do you **sleep**" |
| Ps 44:25 | `למה פניך תסתיר תשכח ענינו ולחצנו` | `תשכח` 2ms — "you **forget** our affliction and our oppression" |
| Ps 22:2 | `אלי אלי למה עזבתני` | `עזב` **HVqp2ms + 1cs** — completed action: *you abandoned me* |
| Job 42:7 | `לא דברתם אלי נכונה כעבדי איוב` | God's anger `חרה אפי` is at the **friends who defended him**; Job, who accused him for 35 chapters, is the one who spoke `נכונה` |

### ⭐ Jer 20:7 — the verb Jeremiah chose

```
פתיתני יהוה ואפת חזקתני ותוכל
```

`פתיתני` = H6601, **piel perfect 2ms + 1cs suffix**. Every piel of this root in the Hebrew Bible —
**all 17 tokens**, regenerated:

| ref | form | who does it |
|---|---|---|
| Exod 22:15 | `יפתה` | a man **seducing** an unbetrothed girl — the seduction statute |
| Judg 14:15 · 16:5 | `פתי` (impv. 2fs) | Delilah, twice, commissioned to work on Samson |
| 1 Kgs 22:20 ∥ 2 Chr 18:19 | `יפתה` | **YHWH asks: "who will entice Ahab?"** |
| 1 Kgs 22:21 ∥ 2 Chr 18:20 | `אפתנו` | the spirit: "**I** will entice him" |
| 1 Kgs 22:22 ∥ 2 Chr 18:21 | `תפתה` | **YHWH authorises it**: "you will entice, and also prevail" |
| Ezek 14:9 | `פתיתי` (1cs) | **"I, YHWH, have enticed that prophet"** |
| 2 Sam 3:25 · Prov 1:10 · 16:29 · 24:28 · Ps 78:36 | — | deceiving, enticing to violence, flattering |
| **Jer 20:7** | `פתיתני` (2ms→1cs) | **Jeremiah, of God** |

So the range of this verb is *seduction* and *divinely-authorised deception* — and **7 of the 17
have God as the agent or the one commissioning it**. Jeremiah did not reach for a soft word and
neither did the editors who kept it.

---

## 3. "Just watching"

Two answers exist in the corpus and they do not agree.

**Ps 82** — regenerated in full, vv. 1–8:

```
v1  אלהים נצב בעדת אל בקרב אלהים ישפט
v2  עד מתי תשפטו עול ופני רשעים תשאו סלה
v3  שפטו דל ויתום עני ורש הצדיקו
v4  פלטו דל ואביון מיד רשעים הצילו
v5  לא ידעו ולא יבינו בחשכה יתהלכו ימוטו כל מוסדי ארץ
v6  אני אמרתי אלהים אתם ובני עליון כלכם
v7  אכן כאדם תמותון וכאחד השרים תפלו
v8  קומה אלהים שפטה הארץ כי אתה תנחל בכל הגוים
```

The charge in v2–4 is **exactly your charge**: judging crookedly, favouring the wicked, and failing
to `פלט` and `נצל` — extract and rescue — the `דל`, the `יתום`, the `עני`, the `אביון`. And in v7
the verdict goes **against the divine beings**: `כאדם תמותון` — *you will die like a human*. The
psalm holds gods liable for not intervening, and the last line demands that someone finally get up
(`קומה`).

**Job 38** — the other answer. God finally speaks and gives **no reason**:
`מי זה מחשיך עצה במלין בלי דעת` (38:2), `איפה היית ביסדי ארץ` (38:4). Questions, not an
explanation. Then in 42:7 he tells the friends *they* are the ones who spoke wrongly.

So: the corpus contains the accusation, in the first person, from prophets and psalmists and Job;
it records God as **seeing, hearing, and knowing** through 400 years of slavery before acting; it
preserves a psalm sentencing divine beings to death for precisely this failure; and where it might
have supplied a defence it supplies questions instead, then sides with the man who accused.

What it does not contain anywhere is a text saying the question is out of bounds.

---

*Regenerate: `./tools/analyze.py <Book> <ch> <v>`. Piel counts: parse `hebrew-ot/morphhb/wlc/*.xml`
for `lemma` 6601 with `Vp` in `morph`. `רוח` gender: same, lemma 7307, `morph` starting `HN`.*
