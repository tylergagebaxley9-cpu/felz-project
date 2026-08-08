# Canon Formation — Primary Sources: What Was Excluded, When, By Whom, On What Grounds

Researched 2026-08-08. Scope: the actual primary documents that shaped which books are "in" the Bible and which
are not — not summaries of them. Every URL below was checked live this session (curl HEAD/GET or WebFetch); status
is reported honestly, including where a page blocks plain `curl` but opens fine in a browser/WebFetch (bot-wall,
not dead), and where I could not verify a claim and say so instead of guessing.

**Rule applied, per PROVENANCE.md:** WITNESS date (when the events/text originated) is separate from EDITION date
(when the copy you can read was printed/transcribed). Pre-1820 printed editions are flagged PRINTED and preferred
where they exist and are free; modern scholarly transcriptions/translations are flagged TRANSLATION or EDITED.

---

## 0. The single most important correction up front

**Nicaea (325) did not decide the biblical canon.** No canon list survives from Nicaea, no ancient source claims
Nicaea debated one, and the canons of Nicaea I (which do survive, in Greek, and are widely available) never
mention the subject. This claim is extremely common online and is simply false — it most likely descends from a
garbled retelling of a much later legend (the *Synodicon Vetus*, 9th c., and some medieval Western sources) that
was never taken seriously by scholarship. **The real canon-shaping events are the ones below: Eusebius's tally
(c. 324), Athanasius's letter (367), a run of regional councils (Laodicea c.363, Rome 382, Hippo 393, Carthage
397/419), and Trent (1546) on the Catholic side; the Reformers' own prefaces and confessions on the Protestant
side; and, for the Apocrypha's final removal from ordinary Protestant Bibles, the 1826 BFBS resolution below.**

A second correction, established directly from primary-source checking in this pass: the "Council of Jamnia"
(Yavneh) as a canon-fixing council in c. 90 CE is a modern scholarly construct (proposed by H. Graetz in 1871,
popularized by the term "Jamnia" from 1871–1960s) that is **not attested in any ancient source** and is now
**rejected by most specialists** (see Jack P. Lewis, "What Do We Mean by Jabneh?", *Journal of Bible and Religion*
32.2, 1964 — the article that broke the consensus; Sundberg and others followed). What Yavneh-era rabbis actually
debated, per the Mishnah, was narrower: whether *Qohelet* and *Song of Songs* "defile the hands" (i.e. count as
sacred scripture) — not a yes/no vote on a fixed list of books. See §9 below; this is stated honestly as a
non-event, not papered over.

---

## 1. Already on disk — do not re-download

Two of the primary items on your list are **already in the local corpus**, in the original Greek, and I located
the exact chapter/verse spans. `INDEX.md` undersold this — go pull it up locally, no network needed.

| Document | Location | Format |
|---|---|---|
| **Eusebius, *Historia Ecclesiastica* III.25** (homologoumena/antilegomena/notha list) | `apostolic-fathers/First1KGreek/data/tlg2018/tlg002/tlg2018.tlg002.1st1K-grc1.xml`, lines 4689–4737 | Greek, CC BY-SA 4.0, ed. Kirsopp Lake/Oulton (Loeb-derived, U. Leipzig digitization) |
| **Origen's canon list, quoted by Eusebius, HE VI.25** (his 22-book OT tally + NT list) | same file, starting line 10532 | Greek, same license |
| Eusebius, full *Historia Ecclesiastica* (all 10 books) | same directory | Greek + English (`...1st1K-eng1.xml`) |
| **Athanasius of Alexandria** — *De Incarnatione*, *Contra Arianos* I–III, *De decretis Nicaenae synodi* | `apostolic-fathers/First1KGreek/data/tlg2035/` | Greek — **but the 39th Festal Letter itself is NOT among these works** (see §4) |
| **Gregory of Nazianzus** — several orations + *Carmina moralia* | `apostolic-fathers/First1KGreek/data/tlg2022/` | Greek — **but this is not his canon poem** (Carm. 1.1.12 is in *Carmina Dogmatica*, a different, unincluded work — see §5) |

**Correction to INDEX.md:** the line "[First1KGreek] Contains ... plus Josephus and Philo" is **half wrong**.
Philo is there (`tlg0018`, confirmed). **Josephus is not** — no `tlg0526` (Josephus's TLG number) directory exists,
and no groupname search for "Josephus" returns a hit anywhere in the corpus's 500+ authors. Worth fixing in
INDEX.md; Josephus's free Greek text lives at Perseus instead (§9).

I also confirmed **Cyril of Alexandria** (not Cyril of *Jerusalem* — different person, wrong Cyril) is in this
corpus. Cyril of Jerusalem, whose Catechetical Lecture 4 gives a canon list, is not there — sourced externally
below.

---

## 2. Muratorian Fragment (c. 170–200 CE composition; Milan, Bibl. Ambrosiana Cod. J 101 sup., 8th-c. MS)

The earliest surviving Christian canon list — a mutilated Latin fragment (missing beginning and probably
translated from a lost Greek original), first published by Lodovico Muratori in 1740.

| Edition | Date | URL | Status | Notes |
|---|---|---|---|---|
| **Muratori's own editio princeps** — *Antiquitates Italicae Medii Aevi*, vol. 3 | **1738/1740** | `https://archive.org/download/antiquitatesit03mura/antiquitatesit03mura_djvu.txt` | **200, verified live, content confirmed** | PRINTED, pre-1820. Titled by Muratori "*Fragmentum acephalum Caji ... de Canone sacrarum Scripturarum*" — he misattributed it to Caius the Roman presbyter (c. 196 CE); that attribution is now rejected, the fragment is anonymous. Opens "*quibus tamen interfuit, et ita posuit*" (matches the standard opening) — grep-verified at line ~63268 of the OCR text. This is the actual first printing anyone can point to. |
| Latin + English, modern typeset | scholarly (Gwatkin 1937 reprint of the Latin) | `http://www.bible-researcher.com/muratorian.html` | 200 via WebFetch/browser UA; **406 to plain `curl`** — bot-wall, not dead. Use `curl -A "Mozilla/5.0 ..."` or a browser. | Latin from Henry Gwatkin, *Selections from Early Writers* (1937), with facing English. Convenient modern reading copy. |
| English only | — | `https://www.earlychristianwritings.com/text/muratorian2.html` | 200 | No Latin on this page — English translation only. Site is © Peter Kirby, no open license stated. |

**What it actually says, vs. what's claimed:** the fragment lists 4 Gospels (only Luke/John's entries survive —
the start naming Matthew/Mark is lost to the manuscript's damage), Acts, 13 Pauline epistles (no Hebrews), Jude,
2 John (ambiguous whether 2 or 3 John), Wisdom of Solomon (explicitly, as NT-adjacent — unusual), Revelation of
John, and **Revelation of Peter "which some of us will not have read in church."** It explicitly **rejects**
Shepherd of Hermas *for canonical reading in church* — not because it's bad, but on a stated ground: Hermas was
written "very recently, in our own times" by Hermas, brother of Pope Pius I (c. 140–155 CE), so it fails the
apostolic-authorship test — "it ought indeed to be read, but not publicly in church, among the prophets... or the
apostles." It also names and rejects Marcionite forgeries under Paul's name, and writings of the Valentinians,
Montanists ("Cataphrygians"), and Basilides by name, "which cannot be received into the Catholic Church."

---

## 3. Eusebius, *Historia Ecclesiastica* III.25 — on disk, see §1

The homologoumena ("acknowledged"), antilegomena ("disputed, but known to most"), and notha ("spurious")
categories. **Exact books Eusebius sorts, from the Greek text on disk (translated from what I pulled):**

- **Acknowledged (homologoumena):** 4 Gospels, Acts, Paul's epistles, 1 John, 1 Peter; Revelation "if it seems
  right" (he flags his own uncertainty about it twice in this chapter).
- **Disputed but known to most (antilegomena):** James, Jude, 2 Peter, 2–3 John.
- **Spurious (notha) — "yet known to most church writers":** Acts of Paul, Shepherd (of Hermas), Apocalypse of
  Peter, Epistle of Barnabas, the *Didache* ("Teachings of the Apostles"), and — he adds — some also put the
  **Gospel of the Hebrews** here, which Hebrew-Christian converts particularly favor. He puts Revelation here too
  as an alternative, for those who reject it.
- **Explicitly rejected as heretical forgeries, not even "spurious" — "must be thrust aside as absurd and
  impious":** gospels circulated under the names of **Peter, Thomas, and Matthias**, and Acts "of Andrew and John
  and the other apostles." His stated ground: nobody in the whole chain of orthodox writers ever cites them, their
  style doesn't match apostolic Greek, and their doctrinal content is far from orthodoxy — i.e. an authorship
  test plus a doctrinal test, stated explicitly, not asserted.

---

## 4. Athanasius, 39th Festal Letter (367 CE)

**Transmission is genuinely split by language — this matters for what "the Greek text" means:**

- The canon-list section (roughly §§15–19, where the 27 NT books are named) **does survive as continuous Greek**,
  preserved via Byzantine canon-collections/catenae rather than as an independent manuscript of the letter — this
  is why Migne could print it (PG 26, col. 1436).
- The rest of the pastoral letter (the parts about the church calendar, Easter dating, exhortation) survives
  complete only in **Coptic** (fragmentary — Lefort published the known Coptic fragments in 1955; Coquin added
  more in 1984; a further fragment was published in 2010, per the *Harvard Theological Review* article "A New
  Fragment of Athanasius's Thirty-Ninth Festal Letter") and in **Syriac** (via a summary index, not the full text).

| Text | URL | Status | Notes |
|---|---|---|---|
| Greek (canon-list portion), with note on transmission | `https://earlychurchtexts.com/main/athanasius/festal_letter_39.shtml` | **200, verified, Greek confirmed live** | Greek from Migne PG 26. Confirms the "read but not canonized" category explicitly. |
| English (NPNF) | NPNF 2nd series, vol. 4 — widely mirrored (ccel.org, newadvent.org) | — | Standard translation. |

**What it actually says:** Athanasius lists exactly the 27 NT books in the modern order — the **first surviving
list that matches the modern NT canon exactly**, no more, no less. He then draws a third category the user
specifically asked about — books **read but not canonized**:

> "...ἔστι καὶ ἕτερα βιβλία τούτων ἔξωθεν, οὐ κανονιζόμενα μέν, τετυπωμένα δὲ παρὰ τῶν Πατέρων ἀναγινώσκεσθαι..."
> ("there are other books besides these, not canonized, but appointed by the Fathers to be read")

He names, for this middle category: **Wisdom of Solomon, Wisdom of Sirach, Esther, Judith, Tobit, the
"Teaching of the Apostles" (Didache), and the Shepherd** (of Hermas) — useful for catechesis, not for doctrine.
Everything else (he names specific apocryphal gospels/acts elsewhere in the letter) is "an invention of heretics."

---

## 5. Origen (via Eusebius HE VI.25) — on disk, see §1; Cyril of Jerusalem; Council of Laodicea; Gregory of
Nazianzus; Amphilochius of Iconium

All four of the external items are hosted, Greek + English, on the same well-organized site
(`bible-researcher.com`, ed. Michael Marlowe) — **note: this domain returns HTTP 406 to plain `curl`'s default
user-agent (bot-block), but resolves fine with a browser UA or WebFetch.** Confirmed 200 with
`curl -A "Mozilla/5.0 ..."`.

| Source | Date | URL | Greek/original? | Key content |
|---|---|---|---|---|
| **Cyril of Jerusalem**, Catechetical Lecture 4.33–36 | c. 350 CE | `http://www.bible-researcher.com/cyril.html` | Yes, Greek per Migne, facing English | 22 OT books; NT = 4 Gospels + Acts + 7 Catholic epistles + 14 Pauline. **Excludes Revelation** — the page's own note ties this to a broader Eastern reaction against Revelation after Montanist over-use of it. |
| **Council of Laodicea**, canon 60 | c. 363 CE | `http://www.bible-researcher.com/laodicea.html` | Yes, Greek per B.F. Westcott's *General Survey* (1881) | 22 OT books incl. Baruch/Epistle of Jeremiah bundled with Jeremiah; NT = **26 books, omitting Revelation**. **Authenticity flagged as doubtful by the page itself** — canon 60 (the actual list) is absent from several Greek MSS of the Laodicea canons and from the Latin version entirely; canon 59 (books-only rule, no list) is the part that's solidly attested. Treat the list as probably a later addition to a genuine 4th-c. council, not certainly conciliar. |
| **Gregory of Nazianzus**, *Carmina Dogmatica* I.1.12, "On the genuine books of Scripture" | c. 380 CE | `http://www.bible-researcher.com/gregory.html` | Yes, Greek, Migne PG 37.471–474 | 22 OT books; NT = 4 Gospels + Acts + 14 Pauline + 7 Catholic epistles. **Explicitly excludes Revelation** ("in case its counterfeit corrupt the many," per the poem's own closing lines). *Not* in the local First1KGreek corpus (that only has his orations + a different, moral-sentence poem). |
| **Amphilochius of Iconium**, *Iambics to Seleucus* | c. 380 CE | `http://www.bible-researcher.com/amphilocius.html` | Yes, Greek, Migne PG 37 (printed among Gregory Nazianzus's works there) | Explicitly hedges rather than flatly excluding: Esther "some approve of the addition"; Hebrews — some call it "spurious," he defends it; Catholic epistles — some accept only 3 (James, 1 Peter, 1 John), others all 7; Revelation — "some approve, but the more part say it is spurious." This is the most openly split/undecided of all the 4th-c. lists — genuinely useful as a snapshot of live disagreement, not consensus. |

Master index of 23 canon-list primary sources (170–730 CE) on the same site, useful for anything not covered
above: `http://www.bible-researcher.com/canon8.html` (200, verified).

---

## 6. Councils: Rome 382, Hippo 393, Carthage 397/419, Trullo 692, Florence 1442, Trent 1546

### Rome 382 and Carthage III (397) — Latin text found and verbatim-confirmed

| Council | URL | Status | Text confirmed |
|---|---|---|---|
| **Council of Rome, 382** (the "Damasine list" — traditionally under Pope Damasus I; **its attribution to an actual 382 synod is debated by scholars**, since this list is transmitted as part of the *Decretum Gelasianum* tradition, §10, and the 382-synod framing may be a later retrojection) | `http://patristica.net/denzinger/enchiridion-symbolorum.html` (Denzinger §§179–180) | 200, Latin, verified | "*Genesis liber unus; Exodus lib. 1;... Item Sapientia lib. 1, Ecclesiasticus lib. 1... Tobiae lib. 1; Esdrae libri 2; Hester lib. 1; Judit lib. 1; Machabeorum libri 2*" — full enumerated OT list including deuterocanon, confirmed verbatim. |
| **Third Council of Carthage, 397**, canon on scripture | `http://www.bible-researcher.com/carthage.html` (Latin) + Denzinger §186 (`http://patristica.net/denzinger/enchiridion-symbolorum.html`) | 200 both, Latin confirmed | Opens "*Item placuit ut praeter Scripturas canonicas nihil in ecclesia legatur sub nomine divinarum Scripturarum*" ("it was agreed that nothing be read in church under the name of the divine Scriptures except the canonical Scriptures"). Lists Tobit, Judith, Wisdom, Sirach, 1–2 Maccabees alongside the protocanonical books. **One manuscript reading adds** "for the confirmation of this canon let the church across the sea [Rome] be consulted" — the page itself flags this as likely a later (c. 419) editorial addition, not the original 397 wording — an honest textual-variant note worth keeping, since it's sometimes cited to claim Rome ratified Carthage's list when the manuscript evidence for that clause is contested. |

### Hippo 393 — the honest answer

**No independent text of Hippo's canon decision survives.** The Council of Hippo's acts are lost outright; what
survives is the **Breviarium Hipponense**, a summary drawn up at Carthage in 397 (the same council listed above)
that recaps Hippo's 393 canons in digest form — meaning the Carthage 397 text above **is** the closest surviving
access to Hippo's ruling, not a separate document. (English translations of the Breviarium and the Carthage
397/419 acts, by Roger Pearse, are at `https://www.roger-pearse.com/weblog/tag/council-of-hippo/` — confirmed 200,
Latin (Munier's edition) with facing NPNF-based English, but that particular canon-37b/38/39 page I checked
covers *different* canons (Donatist baptism, ordination) — the scripture canon and this page happen not to
overlap; use it for the wider Hippo/Carthage acts, not as the scripture-list source.)

### Trullo (Quinisext Council), 692 — canon 2

| Text | URL | Status | Notes |
|---|---|---|---|
| English | `https://www.clerus.org/clerus/dati/2001-03/31-13/Ctrullo.html` | 200, verified, English | Canon 2 does not itself list books — it **ratifies by name** the earlier canon-authorities: the 85 Apostolic Canons, and by name **Dionysius, Peter, and Athanasius of Alexandria; Gregory the Wonder-worker; Basil; Gregory of Nyssa; Gregory the Theologian [Nazianzus]; Amphilochius of Iconium**; plus the councils of Laodicea, Carthage, etc. — effectively a "canon of canons," folding all the 4th-c. lists above into binding Eastern church law at one stroke in 692. |
| Greek | **not located and verified in this pass** | GAP | Multiple English mirrors found (NPNF, EWTN, clerus.org); no independently-confirmed free Greek text of Trullo's canons located this session. Worth a follow-up against Rhalles-Potles *Syntagma* or documentacatholicaomnia.eu. |

### Florence, *Cantate Domino* (Bull of Union with the Copts), 4 Feb 1442

**Correcting a real, checkable claim:** this bull is sometimes cited as the first council to give a complete
enumerated 46/27-book list (predating Trent by over a century). **I checked three independent full-text sources
this session — Wikipedia's article, catholicism.org's posted text, and a direct EWTN link — and searched each for
"Genesis," "Tobit," "Judith," "Maccabees," "Baruch." None of the three contains an enumerated book list; all three
give only the general formula "one and the same God is the author of the Old and New Testament."** I could not
locate a resolving free page with the fuller enumerated version in this pass (tried papalencyclicals.net,
Denzinger via patristica.net — that Denzinger mirror stops at the 5th century). **This is a genuine open gap, not
a confirmed fact either way** — flagging per the "state clearly and stop rather than guessing" rule rather than
repeating the "Florence had the full list" claim uncritically. If it matters, the next step is a Denzinger scan
(DS 1334–1336) or Mansi vol. 31.

### Trent, Session IV, 8 April 1546 — "*Sacrosancta*" (De Canonicis Scripturis)

| Edition | Date | URL | Status |
|---|---|---|---|
| **Pre-1820 Latin print** — *Concilium Tridentinum, hoc est, Canones & decreta...* | **1567** | `https://archive.org/download/bub_gb_QFEokxgibOMC/bub_gb_QFEokxgibOMC_djvu.txt` | **200, verified live.** PRINTED, pre-1820. OCR quality on this scan is poor (period ligatures/long-s garble grep matches) — I could not isolate the Session IV canon list by text search in the OCR layer; usable as a page-image PDF (43 MB) reference, not reliably searchable. Flagging honestly rather than claiming a passage I didn't actually confirm in this copy. |
| English (Waterworth translation, from the standard Latin) | modern | `https://history.hanover.edu/texts/trent/ct04.html` | 200, verified, content confirmed | Opens "The sacred and holy, ecumenical, and general Synod of Trent..." Lists Tobit, Judith, Baruch, Wisdom, Ecclesiasticus (Sirach), 1–2 Maccabees as canonical alongside the protocanon, "with equal reverence," and closes with an anathema on anyone who does not receive all of them as sacred and canonical — this is the actual anathema clause, the strongest and latest formal conciliar statement in either direction. |

**What actually changed at Trent, stated precisely:** Trent did not "add" the deuterocanonical books — they were
already read as scripture in the Latin liturgical tradition going back through Carthage/Rome above. What Trent
did, that no prior council had done with this force, was **make acceptance of that list a matter of anathema**
— i.e. it converted a long-standing liturgical practice into a formally closed, binding dogma, explicitly *because*
the Reformers were at that moment rejecting the same books (see §7). The date and the causal link to the
Reformation are the real story, not "Trent invented the Apocrypha."

---

## 7. Reformation-side: Luther's prefaces, Westminster Confession (1647), Thirty-Nine Articles (1571)

### Luther — and a real misattribution corrected

**The famous "epistle of straw" line is NOT in Luther's preface to James specifically — it's in his general
*Preface to the New Testament* (1522), where he ranks the books.** I checked the actual preface to James/Jude
(`Das Newe Testament Deutzsch/Jak`) directly and the phrase does not occur there; it is in
`Das Newe Testament Deutzsch` (the general NT preface), confirmed by searching German Wikisource's full-text
index and pulling the exact sentence.

| Text | Date | URL | Status | Content |
|---|---|---|---|---|
| *Vorrede auff das Newe Testament* (general NT preface) — original German, 1522 Septembertestament spelling | 1522 | `https://de.wikisource.org/wiki/Das_Newe_Testament_Deutzsch` | **200, verified, exact quote confirmed** | "*Darumb ist sanct Jacobs Epistel eyn rechte stroern Epistel gegen sie [John's Gospel/1 John, Paul's Romans/Galatians/Ephesians, 1 Peter], denn sie doch keyn Euangelisch art an yhr hat*" — "St James's epistle is a real strawy epistle compared to them, since it has no Gospel character to it." This is the actual sentence, in context: a **relative ranking**, not an isolated insult — he's grading it against what he considers the New Testament's core. Also in this preface: Hebrews, James, Jude, and Revelation are listed **unnumbered**, separated from the 23 numbered books, in his own table of contents — a structural demotion, not a removal. |
| *Vorrhede auff die Episteln S. Jacobi vnnd Judas* — the actual preface to James/Jude | 1522 | `https://de.wikisource.org/wiki/Das_Newe_Testament_Deutzsch/Jak` | 200, verified | Confirmed: does raise doctrinal objections ("I do not hold it to be of apostolic authorship," and the justification-by-works vs. Paul tension), but **does not contain "stroherne Epistel."** |
| English translation (both prefaces) | modern | e.g. Project Wittenberg mirrors | — | Widely available; Luther never removed James/Jude/Hebrews/Revelation from his Bible — they're printed in every edition, just unnumbered and last. He removed nothing; he re-ranked. |

### Westminster Confession of Faith, 1647, Chapter 1

| Text | URL | Status |
|---|---|---|
| Full Ch. 1, "Of the Holy Scripture" | `https://opc.org/wcf.html` | 200, verified, exact text confirmed |

§2 enumerates all 66 Protestant canonical books by name. §3 states: "The books commonly called Apocrypha, not
being of divine inspiration, are no part of the canon of the Scripture, and therefore are of no authority in the
church of God, nor to be any otherwise approved, or made use of, than other human writings." — the flattest,
most absolute Protestant confessional rejection in this entire manifest; no "read for example of life" carve-out
at all (contrast Article VI below).

### Thirty-Nine Articles of Religion, 1571, Article VI

| Text | URL | Status |
|---|---|---|
| Article VI, full text | `https://en.wikisource.org/wiki/Thirty-Nine_Articles_of_Religion` | 200, verified, exact text confirmed |

Quoting Jerome: the Church "doth read [the Apocrypha] for example of life and instruction of manners; but yet
doth it not apply them to establish any doctrine." Names, verbatim: 3 Esdras, 4 Esdras, Tobit, Judith, rest of
Esther, Wisdom, Sirach, Baruch, Song of the Three Children, Susanna, Bel and the Dragon, Prayer of Manasses,
1–2 Maccabees. **This is the middle position** — softer than Westminster's flat rejection, still short of Trent's
canonization — and it is the position that the Church of England (and the early BFBS, until 1826) actually
printed and distributed for two and a half centuries.

---

## 8. The 1826 British and Foreign Bible Society Apocrypha Controversy — the actual resolutions

**This is the moment the Apocrypha physically left the ordinary Protestant Bible**, and you asked specifically for
primary text, not description. Found: the actual pamphlets, containing the actual "Resolved—" language, on
archive.org. **Always query `/metadata/<id>` for real filenames first** — both of these were found that way, not
guessed.

| Document | Date | Archive.org ID | Status |
|---|---|---|---|
| *Statement by the Committee of the Edinburgh Bible Society relative to the Circulation of the Apocrypha by the British and Foreign Bible Society* | **1825** (1st ed.) | `StatementOfTheBibleSocietyConcerningTheApocrypha` (file `StatementOfTheBibleSocietyConcerningTheApocrypha-1825_djvu.txt`) | **200, verified live, content pulled and read** |
| Same title, **2nd edition, expanded**, includes the final 1826/1827 material | **1826** | `statementbycommi0001vari` | **200, verified live, content pulled and read (1.8 MB djvu.txt)** |
| Robert Haldane, *Review of the Conduct of the Directors of the British and Foreign Bible Society relative to the Apocrypha* | 1828 | `reviewofconducto00haldrich` | 200, verified live (not deep-read this pass — the anti-Apocrypha faction's own polemic, for context) |
| *Vindication of the Proceedings of the [Edinburgh] Bible Society Concerning the Apocrypha* | — | `VindicationsaboutBfbsOfTheProceedingsOfTheBibleSocietyConcerning` | 200, verified live (not deep-read this pass) |

### The actual chain of resolutions, quoted from the pamphlets

**August 1822** (first restriction, funding-only, did not stop the practice):
> "Resolved — That when grants shall be made by any of the Bible Societies in connexion with this Institution,
> which are accustomed to circulate the Apocrypha... the Committee... request of those Societies, that they will
> appropriate all future grants which they may receive from the British and Foreign Bible Society, exclusively to
> the printing of the books of the Old and New Testament, as generally received in this country; such Societies
> remaining at full liberty to apply their own funds in whatever way... to the printing and circulation of the
> Apocrypha, it may seem good to them."

This did nothing in practice — Continental societies kept binding the Apocrypha in using their own funds, and by
1824 the BFBS itself briefly re-authorized Rev. Leander Van Ess to intersperse it, then rescinded that.

**20 December 1824** (tightened — no interspersing, but still allows separately-funded printing):
> "That no pecuniary grants be made by the Committee of the British and Foreign Bible Society for the purpose of
> aiding the printing and publishing of any edition of the Bible in which the Apocrypha shall be interspersed
> with the Canonical books of Holy Scripture; and that all grants of money to Foreign Societies, which are
> accustomed to publish Bibles containing the Apocrypha, be made under the express stipulation... that such
> grants shall be exclusively applied to printing and publishing the Canonical books of Scripture only."

The Edinburgh Bible Society's committee judged this still inadequate (it let Continental societies keep
publishing combined Bibles from other funds) and published the 1825 pamphlet above protesting it, escalating the
dispute publicly. Robert Haldane and Rev. Dr. Andrew Thomson led the Edinburgh opposition; their pressure and that
of other large Auxiliaries is what forced the final vote.

**8 May 1826 — the definitive resolution, at the BFBS's 22nd Anniversary General Meeting, London, Lord Teignmouth
presiding — unanimously adopted, no more loopholes:**

> "1st. That the fundamental law of the Society, which limits its operations to the circulation of the Holy
> Scriptures, be fully and distinctly recognised as **excluding the circulation of the Apocrypha**.
>
> 2d. That, in conformity to the preceding resolution, **no pecuniary aid can be granted to any Society
> circulating the Apocrypha**, nor, except for the purpose of being applied in conformity to the said resolution,
> to any individual whatever.
>
> 3d. That in all cases in which grants... of the Holy Scriptures... shall be made to any Society, the books be
> issued bound, and on the express condition that they shall be distributed **without alteration or addition**."

**1827 — a fourth resolution closing the last loophole** (pure-Scripture grants indirectly subsidizing Apocrypha
printing elsewhere), plus a circular letter (dated **19 March 1827**, from BFBS House, London) sent to every
Foreign Bible Society explaining the new rule and quoting the May 1826 resolutions verbatim to them — this
circular letter's text is also captured in full in the pamphlet.

**This is the actual event, dated precisely: 8 May 1826.** Everything before it (1822, 1824) was partial and
leaky; everything after (1827) closed remaining gaps. The stated ground throughout, in the Society's own words,
was not doctrinal condemnation of the Apocrypha's *content* — it was a **constitutional/fundamental-rule
argument**: the BFBS's founding charter committed it to circulating "the Holy Scriptures... without note or
comment," and the Edinburgh faction argued (and won) that binding the Apocrypha in without distinguishing it from
canonical text violated that founding promise to subscribers, regardless of what anyone thought of Tobit or
Wisdom on the merits. The controversy also **split Scottish Bible-society structure** — the Edinburgh Bible
Society pursued open opposition/near-secession from the parent London society over this, per the pamphlets
(confirmed: "pursued this secession from the parent Society as a measure...").

---

## 9. Jewish canon

| Source | Date | URL | Status | Notes |
|---|---|---|---|---|
| **Josephus**, *Against Apion* I.37–43 (the "22 books" count) | c. 95–100 CE composition | `https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0216` | 200, verified. Page toggles between Whiston's English (CC BY-SA 3.0) and **B. Niese's 1892 Greek critical edition** — confirmed the Greek toggle exists. Book 1 of *Against Apion* survives complete in Greek (only *Against Apion* Book 2, §§51–113, is lost from the sole Greek MS and has to be supplied from the Latin translation + Eusebius's quotations) — §§37–43 is safely inside the intact Greek portion. Exact deep-link to §37 not independently confirmed working this session (Perseus's old query syntax kept 302-redirecting to an "invalid query" page); use the TOC from the doc-level URL above to navigate to Book 1. | Josephus's actual count: **22 books**, not 24 or 39 — he groups them as 5 (Torah) + 13 (Prophets, including most of what Christians call "Writings") + 4 (hymns/wisdom). He explicitly states the ground: unlike Greek historians who keep writing more books with no accepted authority, the Jewish canon is closed because "from the death of Moses... to the reign of Artaxerxes... the prophets... wrote down what was done in their times"; **after Artaxerxes** (i.e. after prophecy ceased, on his theory) later works were written but "not esteemed of like authority" because "there hath not been an exact succession of prophets." This authorship/prophetic-succession argument is a distinct, independent line from the later Christian apostolic-authorship test in §3/§4 above — worth not conflating them. |
| **Mishnah Yadayim 3:5** (the Song of Songs / Qohelet "defiles the hands" dispute) | compiled c. 200 CE, debate itself set at Yavneh, late 1st c. | `https://www.sefaria.org/api/texts/Mishnah_Yadayim.3.5` (API) / `https://www.sefaria.org/Mishnah_Yadayim.3.5` (reader) | 200, verified, full Hebrew + English pulled | R. Akiva's famous line, confirmed verbatim: "the whole world is not as worthy as the day on which the Song of Songs was given to Israel; for all the writings are holy, but the Song of Songs is the holy of holies. If they had a dispute, they had a dispute only about Qohelet." **This is a dispute about status, already assumed scriptural by most parties, not a vote to admit or expel either book** — that nuance matters, because it's routinely overstated as "the rabbis almost banned Song of Songs," which the text itself doesn't support. |
| **Bava Batra 14b–15a** (the traditional authorship list — who wrote each biblical book) | Talmudic discussion, redacted c. 500 CE, attributed material earlier | `https://www.sefaria.org/api/texts/Bava_Batra.15a` | 200, verified, pulled | Confirmed content: Moses wrote the Torah + Job; Joshua wrote his book + 8 verses of Deuteronomy; Samuel wrote Judges, Samuel, Ruth; David + 10 elders wrote Psalms; Jeremiah wrote Kings + Lamentations; Hezekiah's men wrote Isaiah, Proverbs, Song of Songs, Ecclesiastes; the Men of the Great Assembly wrote Ezekiel, the Twelve, Daniel, Esther; Ezra wrote his own book + Chronicles' genealogy down to his own time, completed by Nehemiah. This is a **traditional attribution list, not a canon-admission list** — it assumes all these books are already canonical and asks only who physically wrote/redacted them; do not present it as a Jamnia-style vote. |
| License note (both Sefaria items) | — | — | — | Sefaria's William Davidson Talmud English translation is **CC BY-NC** — noncommercial only, matches the existing DSS ⚠️ CC BY-NC flag pattern already used elsewhere in this corpus (see PROVENANCE.md). The Hebrew/Aramaic text itself (Mishnah, Talmud) is ancient and public domain; only Sefaria's specific presentation/pointing/translation carries the license. |
| "Council of Jamnia" | — | — | — | **No primary document exists because the event, as usually described (a council that closed the Hebrew canon c. 90 CE), did not happen.** See §0. What's real: a rabbinic academy did operate at Yavneh after 70 CE, and the Mishnah passage above records an actual internal dispute about two books' status among several already-accepted works — that's the entire kernel of truth. |

---

## 10. Decretum Gelasianum — rejected/apocryphal books list

Traditionally attributed to Pope Gelasius I (492–496 CE) but modern scholarship (von Dobschütz's 1912 critical
edition, the standard one) dates the text's final form to the early 6th century, drawing on an earlier core that
may go back to Damasus (hence its overlap with the "Rome 382" list in §6 — the two are historically entangled,
not independent confirmations of each other).

| Text | URL | Status |
|---|---|---|
| Latin, full text incl. rejected-books section | `https://www.tertullian.org/decretum.htm` | **200, verified, content confirmed.** Rejected-books section headed "*Item notitia librorum apocryphorum*" ("Likewise, a list of the apocryphal books"). Edition: von Dobschütz, *TU* 38.4 (1912). |
| English translation | `https://www.tertullian.org/decretum_eng.htm` | 200, verified |

**Ground stated for rejection** (per the document's own five-part structure): the list is explicitly split into
accepted-canonical (matching the standard OT+NT list, including the deuterocanon), accepted-patristic
(named church writers whose works may be read), and a final class of **named apocrypha to be avoided** — includes
Acts of Andrew, Acts of Thecla and Paul, Gospel of Thomas, Gospel of Matthias, Gospel/Preaching of Peter,
"Itinerary" under Peter's name, and others by name — the stated ground is authorship (falsely attributed to
apostles by heretics) rather than doctrinal content per book, matching the same test Eusebius applies in §3.

---

## Manifest — exact verification commands run this session

```bash
# archive.org — ALWAYS check /metadata/<id> for real filenames, never guess
curl -s "https://archive.org/metadata/statementbycommi0001vari"
curl -s "https://archive.org/metadata/StatementOfTheBibleSocietyConcerningTheApocrypha"
curl -s "https://archive.org/metadata/antiquitatesit03mura"
curl -s "https://archive.org/metadata/bub_gb_QFEokxgibOMC"

# archive.org search (no WebSearch tool needed — advancedsearch.php is a plain fetch)
curl -s "https://archive.org/advancedsearch.php?q=title%3A%28apocrypha%29+AND+title%3A%28controversy+OR+bible+society%29&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=year&rows=50&output=json"

# pull and grep the actual resolution text
curl -sL "https://archive.org/download/statementbycommi0001vari/statementbycommi0001vari_djvu.txt" -o /tmp/bfbs_large.txt
grep -n "1826" /tmp/bfbs_large.txt

# bible-researcher.com blocks plain curl (406) — use a browser UA
curl -sL -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36" \
  "http://www.bible-researcher.com/muratorian.html"

# Sefaria API — Hebrew/Aramaic + English, structured JSON
curl -s "https://www.sefaria.org/api/texts/Mishnah_Yadayim.3.5?context=0&lang=he"
curl -s "https://www.sefaria.org/api/texts/Bava_Batra.15a?context=0&lang=en"

# German Wikisource — search API to find the real page title (guessed titles 404)
curl -s "https://de.wikisource.org/w/api.php?action=query&list=search&srsearch=stroern%20Epistel&format=json"

# On-disk primary sources — no network needed
grep -n 'subtype="chapter" n="25"' apostolic-fathers/First1KGreek/data/tlg2018/tlg002/tlg2018.tlg002.1st1K-grc1.xml
```

---

## Open gaps (honestly flagged, not papered over)

1. **Council of Florence's *Cantate Domino*** — could not confirm or rule out an enumerated book list in the free
   text; three sources checked all lack it. Needs Denzinger DS 1334–1336 or Mansi vol. 31 directly.
2. **Trullo canon 2, Greek text** — English confirmed on multiple mirrors; no free Greek text independently
   verified this session. Try Rhalles-Potles *Syntagma* or documentacatholicaomnia.eu.
3. **Trent Session IV, 1567 Latin print** — confirmed to exist and resolve (archive.org, pre-1820), but OCR
   quality on that scan defeated text-search for the specific canon passage; usable as page images, not as
   searchable text. The modern English (Hanover) is solid; a cleaner pre-1820 Latin search (a different scan, or
   the PDF page images directly) would close this.
4. **Hippo 393's canon in isolation** — genuinely doesn't exist as a separate document; the Carthage 397
   Breviarium digest is the closest thing, and that's already delivered above, not a gap so much as a fact worth
   knowing.
5. **Rome 382's status as an actual synod** — the list exists (§6) but scholars are divided on whether an actual
   council under Damasus issued it in 382, or whether that date/framing is a later attachment to a text whose
   real origin is the 6th-century Gelasian tradition (§10). Both possibilities are noted; I did not adjudicate
   between them, since that's a live scholarly dispute, not a fact-check I can settle from primary text alone.

None of the above needed `tools/scrape_walled.py` — nothing hit an actual anti-bot JS-challenge wall this session
(bible-researcher.com's 406 was a simple user-agent check, cleared with `-A`). If a future pass hits Trullo's
Greek or Florence's full text behind an actual Cloudflare/JS wall, that's the tool to reach for.

---

## Timeline — who excluded/demoted what, when, on what stated ground

| Date | Actor | What happened | Stated ground |
|---|---|---|---|
| c. 90 CE (Yavneh) | Rabbinic academy (Mishnah Yadayim 3:5) | **Not a canon vote.** Internal dispute over whether Song of Songs / Qohelet "defile the hands" — both already treated as scripture by most. "Council of Jamnia" as a canon-closing event is a modern historiographic myth (§0, §9) — UNVERIFIED as an actual event, and the weight of scholarship (Lewis 1964 onward) says it did not happen as popularly described. |
| c. 95–100 CE | Josephus, *Against Apion* I.37–43 | States (does not decide) a 22-book Jewish canon, closed at Artaxerxes on the ground that prophetic succession ended then. | Cessation-of-prophecy / authorship argument |
| c. 170–200 CE | Muratorian Fragment (anonymous, Rome) | First Christian list: excludes Shepherd of Hermas from public church reading (not condemned, just too recent/non-apostolic); names and rejects Marcionite, Valentinian, Montanist, Basilidian writings. | Date of composition (apostolic era vs. "our own times") + heretical origin |
| c. 240 CE | Origen (via Eusebius HE VI.25 — **on disk**) | Reports a 22-book Jewish OT count matching Josephus; separately affirms only 4 gospels as "undisputed under heaven." | Reports consensus rather than ruling |
| c. 313–325 CE | Eusebius, *Historia Ecclesiastica* III.25 (**on disk**) | Sorts NT books into homologoumena / antilegomena / notha; flatly rejects Gospels of Peter, Thomas, Matthias and other Acts as heretical forgeries. | Absence from the orthodox citation chain + un-apostolic style/doctrine |
| c. 350 CE | Cyril of Jerusalem, Catech. 4.33–36 | 22 OT + NT list **excluding Revelation** for catechumens. | Catechetical caution; reflects wider Eastern wariness of Revelation |
| c. 363 CE | Council of Laodicea, canon 59–60 | Canon 59 (solid): only canonical books to be read in church. Canon 60 (list itself, disputed as a later addition): 22 OT + 26 NT, **excluding Revelation**. | Liturgical discipline |
| 367 CE | Athanasius, 39th Festal Letter | **First list matching the modern 27-book NT exactly.** Separately names Wisdom, Sirach, Esther, Judith, Tobit, Didache, Shepherd as "read but not canonized." | Apostolic authorship for the 27; catechetical usefulness for the middle tier |
| c. 380 CE | Gregory of Nazianzus, *Carm.* 1.1.12 | 22 OT + NT excluding Revelation ("in case its counterfeit corrupt the many"). | Guards against forged Apocalypses circulating under John's name |
| c. 380 CE | Amphilochius, *Iambics to Seleucus* | Reports live disagreement rather than ruling: Esther, Hebrews, scope of Catholic epistles, and Revelation all noted as contested among his contemporaries. | Honest survey, not consensus |
| 382 CE | "Council of Rome" list (Denzinger 179–180) | Full enumerated OT+NT incl. deuterocanon. **Attribution to an actual 382 synod is scholarly-disputed** — may be retrojected from the 6th-c. Gelasian tradition. | UNVERIFIED which came first, the synod or the list |
| 393 CE | Council of Hippo | Acts lost outright; ruling only survives secondhand via Carthage 397's digest. | — |
| 397 CE | Third Council of Carthage | Reaffirms canon incl. deuterocanon; "nothing read in church except canonical scripture." | Liturgical discipline, same as Laodicea 59 |
| c. 492–520s CE | *Decretum Gelasianum* | Names specific rejected books (Acts of Andrew, Gospel of Thomas, Gospel of Matthias, etc.) under "*notitia librorum apocryphorum*." | False apostolic attribution by heretics |
| 692 CE | Council in Trullo (Quinisext), canon 2 | Ratifies, as one binding package, Laodicea + Carthage + the named Fathers' lists (Athanasius, Gregory Naz., Amphilochius, etc.) | Consolidation, not new exclusion |
| 1522 CE | Luther, prefaces to the German NT | Re-ranks (does not remove) Hebrews/James/Jude/Revelation to an unnumbered tail; calls James "a strawy epistle" **in the general NT preface, not the James preface itself** (corrected misattribution, §7). | Theological weight (justification by faith) vs. apostolic authorship doubt |
| 1546 CE | Council of Trent, Session IV | First time acceptance of the full deuterocanonical list is made a matter of **anathema** — converts existing liturgical practice into closed dogma. | Direct response to Reformation rejection |
| 1571 CE | Thirty-Nine Articles, Art. VI | Middle position: Apocrypha read "for example of life," not for doctrine. Names 14 books explicitly. | Jerome's authority, cited by name |
| 1647 CE | Westminster Confession, ch. 1 | Flattest Protestant rejection: Apocrypha "no part of the canon... of no authority... than other human writings." No devotional carve-out. | Not of divine inspiration |
| **8 May 1826 CE** | **British and Foreign Bible Society, 22nd Anniversary Meeting, London** | **The Apocrypha is excluded from BFBS funding/circulation absolutely — the event that actually removed it from the ordinary printed Protestant Bible market**, closing loopholes left by the partial 1822 and 1824 resolutions; a 4th resolution and circular letter in 1827 closed the remaining funding loophole. | Constitutional argument: the Society's founding rule committed it to "the Holy Scriptures... without note or comment"; forced by the Edinburgh Bible Society's public campaign (Haldane, Andrew Thomson) after the weaker 1822/1824 measures failed to actually stop Continental societies binding the Apocrypha in. |

**Net pattern across 1,700+ years:** every actor above who names a specific ground gives one of three tests —
(1) **apostolic/prophetic authorship** (Josephus's prophetic-succession cutoff; Eusebius's citation-chain test;
Gelasianum's false-attribution test), (2) **liturgical discipline** (Laodicea 59, Carthage 397 — what may be
*read aloud in church*, a narrower question than "is it inspired"), or (3) **institutional/constitutional
argument** (BFBS 1826 — not "is Tobit inspired" but "did we promise subscribers Scripture-only funding"). Doctrinal
content of the disputed books themselves is almost never the stated reason in any primary text checked here —
worth noting since it cuts against the popular assumption that these books were excluded because of what they
said.
