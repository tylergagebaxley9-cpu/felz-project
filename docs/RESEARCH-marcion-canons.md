# Marcion's Canon and the Rejected Canons — Primary Sources

Researched 2026-08-08. Builds directly on `docs/RESEARCH-canon-formation.md` (already-done canon-formation
pass) and `docs/RESEARCH-pre1820-patristics-apocrypha.md` §2.10, §3.7 (already-located pre-1820 editions of
Tertullian, Epiphanius, Irenaeus). Does not repeat the archive.org discovery work from those passes — it
**uses** the editions they already found and verified live, pulls the actual `_djvu.txt` text, and reads it.

**The governing fact of this whole document, stated once and implied everywhere after:** Marcion wrote
nothing that survives independently. Every single claim below about what Marcion said, taught, or put in
his canon is a claim made by a hostile opponent trying to refute him. Tertullian, Irenaeus, and Epiphanius
are not neutral cataloguers — they are prosecutors, and their quotations of Marcion are evidence offered
*against* him. Where this matters most (§1, §3) it is flagged inline; treat it as true throughout.

---

## 0. What's actually quoted below, and from where

| Source | Composed | Edition used | Edition date | Format |
|---|---|---|---|---|
| Tertullian, *Adversus Marcionem* (5 books) | c. 207–208 CE | Rigault-line *Tertulliani Opera* | **1689** | PRINTED, Latin, OCR |
| Irenaeus, *Adversus Haereses* | c. 180 CE | Latin-only pre-Grabe edition | **1639**, Paris | PRINTED, Latin, OCR |
| Epiphanius, *Panarion* (incl. *Anacephalaeosis*) | c. 375–378 CE | Petavius edition | **1682** (reprint of Petavius's **1622** *editio princeps*) | PRINTED, Greek+Latin, OCR |
| Muratorian Fragment | c. 170–200 CE | Muratori's *editio princeps* | **1738/1740** | PRINTED, Latin, OCR |
| Harnack, *Marcion: das Evangelium vom fremden Gott* | 1921 CE | 1st edition | **1921** | Modern reconstruction, German, PD |

All five are pre-1820 (or, for Harnack, PD by age) and were pulled as `_djvu.txt` OCR text layers from
archive.org this session — real filenames confirmed via `/metadata/<id>` before download, per project rule.
**OCR quality note, applying PROVENANCE.md's own documented caveat:** the Latin comes through legibly with
mechanical long-s (ſ→f) and occasional letter-swap noise (e.g. "ARVERSVS" for "ADVERSUS") that is easy to
read past. The **Greek in the Epiphanius scan is not reliably OCR'd** — same problem this project already
documented for Erasmus 1516 and other Greek scans. Where a Greek passage matters (Epiphanius's actual
scholia list, Panarion 42) that limitation is called out explicitly rather than papered over — see §1.4.

```bash
# archive.org identifiers used (all confirmed via /metadata/<id> first)
bim_early-english-books-1641-1700_tertulliani-opera-_tertullian_1689   # Tertullian 1689, 5.4MB djvu.txt
sanctiirenaeilug0000vari                                                # Irenaeus 1639, 3.5MB djvu.txt
bim_eighteenth-century_tou-en-hagiois-patros-he_irenaeus-saint-bishop-_1702  # Irenaeus/Grabe 1702 (Greek+Latin, not deep-read this pass)
bub_gb_1Wfnrs5Tw4MC / bub_gb_ZHNpwbPa85MC                               # Epiphanius/Petavius 1682, 2 vols
antiquitatesit03mura                                                     # Muratori 1738/40, editio princeps
marciondasevange00harn                                                   # Harnack 1921, PD, not restricted
neuestudienzumar0000harn                                                 # Harnack, Neue Studien zu Marcion, 1923, PD
```

---

## 1. Marcion's canon: what was in it, and how we know

### 1.1 The two-part structure — from Tertullian's own summary

Tertullian opens *Adversus Marcionem* Book I with an *argumentum* (an editor's summary, likely by a later
hand but printed with the text since Rigault) stating Marcion's system in one sentence:

> *"Marcion Ponticus ob varia crimina Ecclesia pulsus... cepitque docere duo esse initia, duos Deos
> dissimiles omnino: bonum unum & mitem: saevum alterum & ferocem. A bono novum testamentum, ab illo
> immani vetus promulgatum, qui etiam mundum creavit."*
> — "Marcion of Pontus, expelled from the church for various offenses... began to teach that there were
> two origins, two Gods entirely unlike each other: one good and mild, the other savage and fierce. From
> the good [God comes] the New Testament, from that monstrous one the Old was promulgated — [the one] who
> also made the world."

Tertullian's own working description of Marcion's canon, from Book IV's opening (*Adv. Marc.* IV.2):

> *"Constituimus in primis, Evangelicum Instrumentum Apostolos autores habere... Denique, nobis fidem ex
> Apostolis Ioannes & Matthaeus insinuant; ex Apostolicis, Lucas & Marcus instaurant... Contra Marcion,
> Evangelio scilicet suo, nullum adscribit auctorem... Nam ex iis commentatoribus quos habemus, Lucam
> videtur Marcion elegisse, quem caederet."*
> — "We lay down, to begin with, that the Gospel record has the Apostles as its authors... In sum, faith is
> secured for us by John and Matthew from among the Apostles, and renewed by Luke and Mark from among the
> apostolic men... Marcion, by contrast, assigns no author at all to his Gospel... for from what we can
> establish, Marcion appears to have **chosen Luke — precisely in order to cut it.**"

That verb — *caederet*, "to cut/mutilate" — is the whole hostile framing in one word, and it is Tertullian's
word, not a neutral description (see §2 on why this framing itself is contested).

**The Apostolikon, per Tertullian's Book V and cross-checked against modern indices:** ten Pauline letters,
in this order — Galatians, 1–2 Corinthians, Romans, 1–2 Thessalonians, "Laodiceans" (see below), Colossians,
Philippians, Philemon. **No Pastorals** (1–2 Timothy, Titus), no Hebrews, no Catholic epistles, no Acts.

**The "Laodiceans" detail, confirmed directly from the 1689 text (Adv. Marc. V, on the letter to the
Ephesians):**
> *"...epistola, quam nos ad Ephesios praescriptam habemus, haeretici vero ad Laodicenos."*
> — "...the letter which we have inscribed 'to the Ephesians,' the heretics, however, [call] 'to the
> Laodiceans.'"

Marcion did not add a spurious "Laodiceans" letter — he retitled the letter the church calls Ephesians. This
matters because a *different*, later, genuinely forged "Epistle to the Laodiceans" also circulated (named
separately and condemned in the Muratorian Fragment, §4) — the two are not the same document, and conflating
them is a common error worth flagging.

### 1.2 Marcion's explicit exclusion of the Pastorals — Tertullian's own irritation, quoted directly

This is the primary-source anchor for "no Pastorals," found at the end of Adv. Marc. Book V (discussing
Philemon, the one addressed "to a single man" that Marcion *did* keep):

> *"Miror tamen, quum ad vnum hominem litteras factas receperit, quid ad Timotheum duas, & vnam ad Titum,
> de Ecclesiastico statu compositas recusauerit. Affectauit, opinor, etiam numerum epistolarum
> interpolare."*
> — "I am surprised, however, that although he accepted a letter written to a single man [Philemon], he
> rejected the two to Timothy and the one to Titus, composed on the subject of church order. I suppose he
> was bent on tampering even with the *number* of the epistles."

Tertullian's own theory for *why* Marcion left them out is speculative ("I suppose") — he doesn't actually
know Marcion's reasoning here, he's guessing. Modern scholarship generally reads it the other way: the
Pastorals' heavy emphasis on institutional church order (bishops, elders, "guard the deposit") reads as a
direct rebuttal of Marcionite/gnostic teaching and may not have existed yet, or not been associated with
Paul yet, when Marcion assembled his Apostolikon c. 144 CE — see §6.

### 1.3 The dualism's stated proof-text — Marcion's own argument, via Tertullian

Rare moment where Tertullian preserves something closer to Marcion's actual argument rather than just his
conclusion (Adv. Marc. I, on the "good tree / bad tree" saying):

> *"...& obtusis sensibus ipsa enormitate curiositatis, inveniens creatorem pronuntiantem, 'Ego sum qui
> condo mala'; quanto ipsum praesumpserat mali auctorem... alium Deum praesumpsit esse debere, in ordine
> bonae arboris, bonos fructus [ferentem]."*
> — "...finding the Creator declaring, 'I am he who makes evils' [Isaiah 45:7, LXX], and thereby all the
> more presuming him to be the author of evil... he presumed there must be another God, one who, like a
> good tree, bears good fruit."

This is Marcion's actual exegetical move as Tertullian reports it: take Isaiah 45:7 ("I make peace and
create evil," LXX/MT) as the Creator's own self-description, set it against Jesus's saying that a good tree
cannot bear bad fruit (Matt. 7:17–18), and conclude by strict logic that the two cannot be the same being.
**This is still Tertullian's report of the argument, not a Marcionite document** — but it is closer to
Marcion's own reasoning than the summary paragraphs, because it reconstructs a specific inference rather
than just asserting a conclusion.

### 1.4 Epiphanius, *Panarion* 42 — located, partially readable

Petavius's 1682 edition (reprint of his 1622 *editio princeps*) does contain Heresy 42, headed in the
apparatus **"AD HÆR. XLII. MARCIONISTARUM"** (Petavius's own critical notes, keyed to numbered *scholia* —
"Scholion IX," "Scholion XV," "Scholion XVIII," "Scholion XXI," etc. — each one a specific reading Epiphanius
quotes from Marcion's Gospel text and then refutes). This numbered-scholia structure is exactly the
famous apparatus scholars use to reconstruct Marcion's Gospel verse by verse.

**What was recoverable this session, and what wasn't:** Petavius's Latin *commentary on* the scholia is
legible (e.g., his note on Scholion 15 identifies it as concerning Luke 7:28, "he who is least in the
kingdom of heaven..."). **The scholia's own Greek text — Epiphanius's actual quotations of Marcion's Gospel
— sits in a dual Greek/Latin column layout whose Greek OCR is not usable**, consistent with this project's
already-documented finding about Greek OCR quality on these older scans (PROVENANCE.md). This is a genuine
gap for this pass, not a fabricated summary: **I did not manage to isolate readable primary text of the
scholia list itself from the 1682 scan.** The much shorter *Anacephalaeosis* (summary/recap portion of the
Panarion, same composition date) came through cleanly instead, and is quoted in full at §3 below.

**Practical path if the scholia text specifically is wanted later:** the modern critical edition is Karl
Holl's *Epiphanius* (GCS, 1915–33, vol. 2 covers Haer. 42) — post-1820, not pursued this pass — or Frank
Williams's English translation (Brill, 1987/2009, copyrighted). Dieter T. Roth's 2015 reconstruction (§2)
works directly from Holl's text.

### 1.5 Modern reconstructions and their copyright status

| Reconstruction | Author, year | Status |
|---|---|---|
| *Marcion: das Evangelium vom fremden Gott* | Adolf Harnack, **1921** | **PD** — confirmed not-restricted on archive.org (`marciondasevange00harn`), and 1921 is safely pre-1923/PD-by-age in the US regardless of URAA. Contains **Beilage III** ("Das Apostolikon") and **Beilage IV** ("Das Evangelium Marcions") — his actual verse-by-verse reconstruction with Greek/Latin fragments, in German. |
| *Neue Studien zu Marcion* | Harnack, **1923** | **PD**, confirmed not-restricted (`neuestudienzumar0000harn`) — addendum/corrections to the 1921 work. |
| *Marcion: The Gospel of the Alien God* (English translation of the above) | trans. J.E. Steely & L.D. Bierma, 1990 | **Restricted** (controlled lending) on archive.org — the *translation* is still in copyright even though the German original isn't. |
| *The Text of Marcion's Gospel* | Dieter T. Roth, **2015** | Brill. Searched archive.org (title search) — **not found**, consistent with active copyright. Standard current critical reconstruction, works from Holl's Epiphanius + Tertullian + Adamantius. |
| *The First New Testament: Marcion's Scriptural Canon* | Jason BeDuhn, **2013** | Polebridge Press. Searched archive.org — **not found**, consistent with active copyright. Argues (see §2) that Marcion's text is often *not* a deliberate edit but an independently-transmitted early form. |
| *Marcion and the Dating of the Synoptic Gospels* | Markus Vinzent, 2014 | Peeters. Not searched for separately — same publisher-copyright pattern expected. |
| *Das älteste Evangelium und die Entstehung der kanonischen Evangelien* | Matthias Klinghardt, 2015, 2 vols | Francke. Searched archive.org — **not found**, consistent with active copyright. |
| *Marcion and the Making of a Heretical Mind* | Judith Lieu, 2015 | Cambridge UP. Searched archive.org — **not found**, consistent with active copyright. |

**Bottom line for reconstruction access:** Harnack (1921/1923) is the only fully open, freely-downloadable
reconstruction — and it is still the base text everyone since has argued with, including the four
2013–2015 works that supersede it scholarly-speaking. If a reconstructed running text of Marcion's Gospel is
wanted in this corpus, Harnack's Beilage IV (German, PD) is the actual obtainable option; the modern
English-language critical editions are all closed.

---

## 2. Did Marcion cut Luke, or did canonical Luke expand Marcion? — presenting both sides, unresolved

This is a live, unresolved scholarly dispute. It is presented here without a verdict, per the task's
instruction — what follows is who holds which position and on what evidence, not a ruling.

### 2.1 The traditional view: Marcion abridged an already-existing Luke

**This is what Tertullian and Irenaeus themselves claim** (§1.1, §3 below), and it remains the majority
position among current text-critics, including in the newest specialist monograph on the subject:

- **Dieter T. Roth** (*The Text of Marcion's Gospel*, 2015) — after building the most textually rigorous
  reconstruction to date (using multiple attestation across Tertullian, Epiphanius, and the later
  Adamantius dialogue rather than trusting any one witness alone), concludes Marcion's text is best
  explained as a **redaction of a Luke substantially like the canonical form**, not an independent earlier
  layer.
- **Judith Lieu** (2015) similarly reads Marcion's editorial fingerprints — theologically motivated
  omissions clustering exactly where canonical Luke has material Marcion's system couldn't tolerate
  (infancy narrative, OT citations affirming the Creator, etc.) — as evidence of *deliberate* excision
  rather than independent transmission.
- **The ancient testimony itself** is unanimous on this side: Tertullian, Irenaeus, and Epiphanius all
  describe Marcion as *cutting* a Gospel that was already "Luke's" and already known to the wider church.

**The strongest evidential point for this side:** the omissions in Marcion's Gospel are not random — they
cluster with suspicious precision around material that is doctrinally inconvenient for Marcion's two-god
system (birth narratives implying the Creator's involvement, Jesus citing the Law and Prophets approvingly,
resurrection-of-the-flesh language). A text that happens to be missing exactly the passages one side of a
theological argument would want missing is easier to explain as motivated editing than as coincidence of
independent transmission.

### 2.2 The revisionist view: Marcion's Gospel reflects an earlier, shorter stage that canonical Luke expanded

- **Matthias Klinghardt** (2015, 2 vols) argues at length that Marcion's *Evangelion* is not a mutilation of
  canonical Luke at all but an **earlier gospel text**, closer to a hypothetical common source, which was
  later expanded — through the addition of infancy narratives, extra OT citations, and other material — into
  what became canonical Luke. On this view Marcion didn't *cut* anything; the orthodox editors *added*.
- **Markus Vinzent** (2014) goes further, arguing Marcion's Gospel may be the **earliest written gospel
  text of any kind**, predating and partly generating the Synoptic tradition rather than deriving from it —
  a direct challenge to Marcan priority as usually understood.
- **Jason BeDuhn** (2013) takes a more moderate middle position within this camp: he argues Marcion's text
  should be evaluated **passage by passage** rather than assumed uniformly edited — some variants look like
  Marcion's own doctrinal trimming, but many others look like ordinary manuscript variation of a kind found
  between any two ancient witnesses, meaning Marcion's text may preserve **genuinely older readings** in
  places where it's simply *different* from canonical Luke, not *shorter because censored*.
- Earlier groundwork for this whole line: **John Knox** (*Marcion and the New Testament*, 1942) already
  argued Marcion's role in *prompting* canon formation was likely bigger than his role as a mere heretical
  editor — a reaction that Klinghardt and Vinzent have since pushed much further.

**The strongest evidential point for this side:** Marcion's Gospel, even on the hostile witnesses' own
testimony, sometimes preserves material that actively works *against* Marcion's own theology — passages
affirming Jewish scripture or the Creator that a deliberate Marcionite editor would have had every reason to
cut and apparently didn't. If Marcion were freely rewriting the text to fit his system, the argument goes,
it's odd that inconvenient material survived at all; it's less odd if he was working from — and largely
preserving — a source that simply didn't yet contain the later-added material.

### 2.3 Where this stands, honestly

Neither side has produced a knockout argument, and this is openly framed as unresolved in the current
literature — the field's leading recent monograph (Roth, 2015) restates and refines the traditional
position but does so aware of Klinghardt's and Vinzent's challenge, not as though it didn't exist. **Do not
present either side as settled.** What can be said cleanly: (1) all three ancient hostile witnesses believed
Marcion cut an existing text, and said so explicitly; (2) the internal pattern of what's missing is
consistent with either deliberate theological pruning of an existing text *or* a text that genuinely
predates the added material — the pattern alone doesn't disambiguate; (3) the dispute turns substantially on
how one dates and stratifies canonical Luke's own composition history (multi-source, redacted over decades)
independent of Marcion, which is itself contested ground.

---

## 3. What Marcion rejected, and his stated reasoning — via Epiphanius's Anacephalaeosis

From Petavius's 1682 edition, the *Anacephalaeosis* (a summary companion to the Panarion, same composition
date c. 375–378 CE), Heresy IX in Book I's summary of the first 46 heresies — Greek and Latin in facing
columns, Latin fully legible:

> *"Marcio oriundus ex Ponto, Episcopo patre natus est. A quo ob virginis stuprum ejectus ex Ecclesia, Romam
> confugit. Ubi cum ab iis, qui tum Ecclesiae praeerant, poenitentiam frustra postulasset, Catholicam fidem
> oppugnare instituit. Quamobrem tria esse Principia dixit, Bonum, Iustum, & Malum. Novum Testamentum a
> Vetere, eiusdemque authoris, alienum esse docuit. Carnis resurrectionem negat. Baptismum duntaxat, sed non
> semel, ter tamen, iisdem indulget. Pro mortuis illorum Catechumenis Baptismum alii suscipiunt. Mulieribus
> conferre Baptismum sine ullo discrimine permittit."*
>
> — "Marcion, a native of Pontus, was born the son of a bishop. Expelled from the church by him [his father]
> on account of the seduction of a virgin, he fled to Rome. There, when he had vainly sought penance from
> those then presiding over the Church, he set himself to attack the Catholic faith. For this reason he said
> there were three Principles: Good, Just, and Evil. He taught that the New Testament is alien to the Old,
> and to its author. He denies the resurrection of the flesh. He permits baptism [to be given] not once but
> three times to the same people. Some [Marcionites] receive baptism on behalf of the dead, for their
> catechumens. He permits women to confer baptism without any distinction [i.e., on the same terms as men]."

**Flagging what's in this passage carefully, because several claims here are hostile-tradition specific and
not corroborated elsewhere in the same form:**

- **"Ejected... for the seduction of a virgin"** — this specific charge (also echoed by later writers) is
  widely treated by modern scholars as **hostile legend, not history** — a stock slander pattern applied to
  multiple heresiarchs in this literature, not a documented biographical fact. It is reported here exactly
  as Epiphanius states it, not endorsed.
- **"Three Principles: Good, Just, and Evil"** — this is a **more elaborate scheme than Tertullian's simple
  two-god dualism** (§1.1) and reflects the fact that Marcion's later followers split into different
  theological camps (some, following Apelles, moved toward a single-principle system; others elaborated a
  third principle for matter/evil distinct from the Just Creator). Epiphanius is describing the
  *tradition as it had developed by his own late-4th-century vantage*, which is not necessarily identical to
  Marcion's own original 2nd-century position as Tertullian (writing 150+ years earlier and against
  Marcionites directly) reports it. **Two hostile witnesses, writing two centuries apart, do not fully
  agree on the number of Marcion's principles** — worth stating plainly rather than harmonizing.
- **"Father was a bishop"** — repeated by both Epiphanius here and, per secondary literature, identified with
  a "Philologus of Sinope," but this identification and the whole father-was-a-bishop detail rests entirely
  on this same hostile-biography tradition; it is not independently attested.

**What is corroborated across witnesses, and can be stated with more confidence:** the OT/NT authorial split
itself (two testaments, two authors/gods) is consistent across Tertullian (§1.1, §1.3), Irenaeus (§4 below),
and Epiphanius here — that core claim is not in dispute between the hostile sources even where biographical
details and the exact number of "principles" diverge.

---

## 4. Irenaeus, *Against Heresies* — the four-gospel argument and Marcion by name

Found directly in the pre-Grabe **1639** Latin edition (*Sancti Irenaei Lugdunensis... adversus Valentini,
[et] similium gnosticorum haereses, libri quinque*, Paris). Book/chapter numbering below follows the
modern standard (III.11 etc.) even though this print's own internal chapter markers differ slightly —
content matched by search, not by trusting this edition's own numbering.

### 4.1 Marcion named directly, right before the four-gospel argument (AH III.11.7)

> *"Marcion autem id quod est secundum Lucam circumcidens, ex his quae adhuc servantur penes eum, blasphemus
> in solum existentem Deum ostenditur."*
> — "Marcion, mutilating [literally: circumcising] the Gospel that is according to Luke, is shown, from
> those parts of it which he still retains, to be a blasphemer of the one true God."

Same sentence-group also states the parallel charge against the Ebionites, worth having alongside for §5:

> *"Ebionaei etenim eo Evangelio, quod est secundum Matthaeum solo utentes, ex illo ipso convincuntur, non
> recte praesumentes de Domino."*
> — "The Ebionites, using only the Gospel according to Matthew, are refuted out of that very [Gospel], not
> rightly presuming concerning the Lord."

### 4.2 The four winds / four cherubim argument, in full (AH III.11.8)

> *"Neque autem plura numero quàm hæc sunt, neque rursus pauciora capit esse Evangelia. Quoniam enim quatuor
> regiones mundi sunt in quo sumus, & quatuor principales spiritus, & disseminata est Ecclesia super omnem
> terram, columna autem & firmamentum Ecclesiae est Evangelii, & spiritus vitae; consequens est quatuor
> habere eam columnas, undique stantes incorruptibilitatem, & vivificantes homines. Ex quibus manifestum
> est, quoniam qui est omnium artifex Verbum, qui sedit super Cherubim, & continet omnia, declaratus
> hominibus, dedit nobis quadriforme Evangelium, quod in vno spiritu continetur."*
> — "There can neither be more Gospels in number than these, nor fewer. For since there are four regions of
> the world in which we are, and four principal winds, and the Church is scattered over all the earth, and
> the pillar and foundation of the Church is the Gospel and the spirit of life, it is fitting that she
> should have four pillars, breathing incorruptibility from every side and revivifying men. From which it is
> clear that the Word, the artificer of all things, who sits upon the Cherubim and holds all things
> together, once made manifest to men, gave us the Gospel in a fourfold form, but held together by a single
> spirit."

Irenaeus goes on for another long paragraph matching each of the four "living creatures" of Ezekiel/Revelation
(lion, calf, human face, eagle) to each evangelist by literary character — Mark opens with the prophetic
voice "in the wilderness" (eagle/prophetic-Spirit imagery), Luke opens with Zechariah's priestly sacrifice
(calf/sacrificial imagery), Matthew traces the human genealogy (the human face), John opens with the eternal,
"principal and glorious" generation from the Father (the lion) — the full matching is present in the same
edition, not reproduced in full here for length.

**This argument is offered as a direct rebuttal to exactly the situation Marcion created** — a single-gospel
canon — and to the Valentinians' and Marcosians' habit of favoring one gospel over the others (see §4.3). It
is one of the earliest explicit arguments *for* a fixed four-gospel canon as such, roughly contemporary with
the Muratorian Fragment (§ below) and about 190 years before Athanasius's 27-book list closes the question
(already documented in RESEARCH-canon-formation.md §4).

### 4.3 The same passage names the Valentinians' rival "Gospel of Truth" (AH III.11.9)

Immediately following the four-gospel argument, in the same breath:

> *"Hi verò qui sunt à Valentino, iterum existentes extra omnem timorem, suas conscriptiones proferentes,
> plura habere gloriantur, quàm sint ipsa Evangelia. Siquidem in tantum processerunt audaciae, vti quod ab
> his non olim conscriptum est, veritatis Evangelium citulent, in nihilo conveniens Apostolorum Evangeliis,
> vt nec Evangelium quidem sit apud eos sine blasphemia."*
> — "But those who are of Valentinus, being, again, altogether fearless, put forward their own compositions,
> and boast that they have more Gospels than there really are. Indeed, they have arrived at such a pitch of
> audacity that they entitle their comparatively recent writing 'the Gospel of Truth,' though it agrees in
> nothing with the Gospels of the Apostles, so that with them there is not even a Gospel free of blasphemy."

This is Irenaeus's testimony to the (real, Nag Hammadi-attested — this project already holds gnostic Coptic
material, see EXCLUDED-BOOKS.md) Valentinian *Gospel of Truth* — confirming Irenaeus knew of it by name and
rejected it on the same "doesn't match the apostolic Gospels" ground applied elsewhere in this document's
canon-formation pass.

### 4.4 The Polycarp anecdote (AH III.3.4) — a separate, famous Marcion encounter story

Also located in the same 1639 edition, with a Greek fragment (via Eusebius's quotation, HE IV.14) printed
alongside the Latin:

> *"...ipse autem Polycarpus Marcioni aliquando occurrenti sibi, & dicenti, Cognosce nos, respondit:
> Cognosco te primogenitum Satanae."*
> — "...Polycarp himself, on one occasion when Marcion encountered him and said, 'Recognize us,' replied: 'I
> recognize you — the firstborn of Satan.'"

This is presented by Irenaeus as testimony to Polycarp's direct personal encounter with Marcion, offered as
proof of unbroken apostolic-succession memory rejecting Marcion from within a single generation (Polycarp
being, per Irenaeus, a direct disciple of John). **Flag as anecdote, not independently verifiable** — it
comes from the same author making the four-gospel argument two paragraphs later, in service of the same
overall case against Marcion; Irenaeus is not a disinterested reporter of this encounter either.

---

## 5. Other rejected canons

### 5.1 The Muratorian Fragment's direct relationship to Marcion

Composition c. 170–200 CE; the pre-1820 edition (Muratori's own **1738/1740** *editio princeps*) was already
located and verified in the canon-formation pass (`docs/RESEARCH-canon-formation.md` §2). Re-checked this
session for the Marcion-specific lines, confirmed at line ~63352 of the `antiquitatesit03mura` djvu.txt:

> *"Fertur etiam ad Laudecenses, alii ad Alexandrinos Pauli nomine ficta ad haeresem Marcionis; & alia
> plura, quae in Catholicam Ecclesiam recipi non potest."*
> — "There is current also [an epistle] to the Laodiceans, [and] another to the Alexandrians, forged under
> Paul's name to further the heresy of Marcion, and several others, which cannot be received into the
> Catholic Church."

**Note the terminology collision flagged already in §1.1:** this "to the Laodiceans" is a *different*,
independently-forged letter circulating under Paul's name to promote Marcionism — not the same document as
Marcion's own retitled Ephesians. Both existed; they are not the same text.

And immediately after, tying Marcion together with Valentinus, Basilides, and the Montanists in a single
condemnation:

> *"Arsinoi autem, seu Valentini, vel Miltiadis nihil in totum recipimus, qui etiam novum Psalmorum Librum
> Marcioni conscripserunt una cum Basilide Asianum Cataphrygum constitutorem."*
> — "But of Arsinous, or Valentinus, or Miltiades, we accept nothing at all — who also composed a new Book
> of Psalms for Marcion, together with Basilides, [and] the Asian founder of the Cataphrygians [i.e., the
> Montanists]."

The Fragment's own grammar here is garbled even in the original (a known feature of this text — it survives
in a single, poorly-copied 8th-c. manuscript translated from a lost Greek original, per the canon-formation
pass), but the substance is clear: the earliest surviving Christian canon list explicitly positions itself
**against** Marcion, Valentinus, Basilides, and the Montanists together, by name, in the same short passage —
direct primary confirmation that early canon-listing and anti-Marcionite/anti-heretical polemic were, from
the very first surviving list, the same activity.

### 5.2 Valentinus and the Valentinians

Covered directly above at §4.3 (Irenaeus naming the "Gospel of Truth"). This project already holds Coptic
gnostic primary material relevant to the Valentinian tradition broadly (`nag-hammadi/corpora/`,
EXCLUDED-BOOKS.md) — the *Gospel of Truth* itself (NHC I,3 and XII,2) is a Nag Hammadi tractate; whether it
is specifically on disk in this corpus wasn't re-checked this session (the existing manifest lists Gospel of
Thomas, Pistis Sophia, Acts of Pilate, and two shorter texts as the 5 tractates currently held — Gospel of
Truth not among them per EXCLUDED-BOOKS.md's "HELD PARTIAL" table). The Muratorian Fragment (§5.1) also
independently rejects Valentinus by name.

### 5.3 The Ebionites — Matthew only, Paul rejected

Directly confirmed in the same Irenaeus passage as the four-gospel argument (§4.2 above): *"Ebionaei etenim
eo Evangelio, quod est secundum Matthaeum solo utentes... "* — Irenaeus's own testimony that the Ebionites
used Matthew's Gospel exclusively. Irenaeus does not, in this specific passage, separately detail their
rejection of Paul, but this is well-attested elsewhere in the patristic record (Irenaeus AH I.26.2, and more
fully in Epiphanius Panarion 30 — already located in this corpus's prior pass, Petavius 1682, per
`docs/RESEARCH-pre1820-patristics-apocrypha.md` §3.6) — the Ebionites are consistently reported as rejecting
Paul as an apostate from the Law, the mirror-image reaction to Marcion: where Marcion kept only Paul and cut
almost everything Jewish, the Ebionites kept only the most Jewish Gospel and cut Paul entirely.

### 5.4 The Montanists ("New Prophecy") — a canon-shaping act of a different kind

Not primarily about *which books* but about *ongoing revelation* — the Montanists (from Phrygia, hence
"Cataphrygians" in the hostile sources, active from c. 156/172 CE) claimed continuing prophetic utterances
through Montanus and the prophetesses Priscilla and Maximilla stood on a level with apostolic scripture.
This forced the opposite question from Marcion's: not "which old books count" but "does revelation stay
open." The Muratorian Fragment rejects them by name (§5.1, "Miltiadis" — Miltiades wrote against the
Montanists; the Fragment's phrasing bundles them with Marcion/Valentinus/Basilides as equally unreceivable).
Eusebius's *Historia Ecclesiastica* Book V (already on disk per `docs/RESEARCH-canon-formation.md` §1,
`apostolic-fathers/First1KGreek/data/tlg2018/tlg002/`) devotes substantial space to Montanism and is the
fuller primary-source route if a dedicated pass on Montanism specifically is wanted later — not deep-read
in this session, flagged as available-but-unexplored rather than covered.

### 5.5 Tatian's Diatessaron as a canon-shaping act

Already fully researched in a prior pass — see `docs/RESEARCH-pre1820-patristics-apocrypha.md` §3.8 and the
dedicated `docs/RESEARCH-syriac-diatessaron.md`. Not repeated in full here; the relevant point for *this*
document is structural: Tatian's harmony (c. 172–185 CE) is a **canon-shaping act of the opposite kind from
Marcion's** — instead of cutting down to one gospel by rejecting three, Tatian fused all four into one
continuous narrative, implicitly asserting the same four-and-only-four boundary Irenaeus argues for
explicitly in §4.2, while still collapsing them into a single reading experience. Both Marcion and Tatian,
in their very different ways, produced a *single* gospel text for their communities to actually read — the
orthodox four-separate-gospels solution that ultimately won out was itself one live option among several in
this same mid-to-late 2nd century window, not a default. As previously established, no pre-1820 witness to
Tatian's actual wording survives (Dura fragment excavated 1933; Ephrem's Syriac commentary only identified
1963) — this remains a genuinely unrecoverable primary text regardless of edition date.

---

## 6. What the orthodox added in response

### 6.1 The Pastorals

Section §1.2 above gives Tertullian's own primary-source irritation at Marcion's exclusion of 1–2 Timothy
and Titus. **The causal claim that the Pastorals were written or promoted specifically *in response to*
Marcion is a modern scholarly inference, not something any ancient source states outright** — worth being
precise about that distinction. What the primary sources do establish directly: (1) the Pastorals' content
is heavily focused on institutional church order, guarding "the deposit" of correct teaching, and warning
against false "knowledge" (*gnosis*, 1 Tim. 6:20) — thematically exactly the kind of material a
Marcionite/gnostic challenge would provoke; (2) Marcion's Apostolikon demonstrably did not include them,
whether because he rejected them or because they did not yet exist/circulate under Paul's name for him to
include — both are live possibilities, not adjudicated by the primary sources checked this session; (3)
Tertullian's own guess ("I suppose he was bent on tampering with the number of epistles," §1.2) treats their
exclusion as *Marcion's* omission of an already-known text, i.e. Tertullian himself assumes the Pastorals
predate Marcion — but Tertullian writing in 207 CE, sixty years after Marcion's canon, is not a contemporary
witness to that question either.

### 6.2 The anti-Marcionite prologues

**Not independently re-verified this session — reporting secondary-source findings with the primary text
itself flagged as unconfirmed, per the "state clearly and stop" rule rather than guessing at a quote.**

Three short Latin prologues to the Gospels of Mark, Luke, and John (no prologue to Matthew survives),
preserved in roughly 40 Vulgate manuscripts, originally composed in Greek (only Luke's prologue survives in
Greek). First identified and named as a group by **Donatien De Bruyne** (1928) and championed by **Adolf
Harnack** (the same scholar as §1.5) as possibly the earliest surviving gospel introductions — a claim "no
longer widely accepted" per current scholarship. **F. F. Bruce** argued for a 2nd-century date and saw
anti-Marcionite polemical intent specifically in Luke's prologue; the current consensus is that the dating
is uncertain, and that **only the prologue to John actually names Marcion** — the "anti-Marcionite" label for
the whole group of three is, on the current view, something of a misnomer inherited from De Bruyne/Harnack's
original framing rather than a description all three prologues independently earn. **I was not able to
locate and verify a live copy of the actual Latin text (particularly the John prologue's Marcion-naming
passage) this session** — two direct URL attempts 404'd — so no direct quotation is given here; this section
should be treated as a well-sourced pointer for a follow-up pass, not as verified primary text.

---

## Honest gaps from this pass

1. **Epiphanius Panarion 42's actual scholia (Marcion's Gospel readings quoted verse-by-verse)** — the
   volume and section are confirmed located (Petavius 1682, `bub_gb_1Wfnrs5Tw4MC`), but the Greek OCR
   defeated extraction of the scholia text itself this session. Petavius's Latin commentary *on* the scholia
   came through; the scholia's Greek content (the actual primary-source payload) did not. Next step: either
   a manual page-image read of the PDF around the Haer. 42 section, or accept the modern Holl (1915–33)/
   Williams (1987/2009) editions as the practical route, both post-1820/copyrighted.
2. **Anti-Marcionite prologues' primary Latin text** — not independently located this session (§6.2). Two
   guessed URLs 404'd; not pursued further given search-budget constraints. Genuine gap, not a confirmed
   dead end — a properly-sourced follow-up (De Bruyne 1928's own publication, or a Vulgate critical edition
   like Wordsworth-White) would close it.
3. **Grabe 1702 Irenaeus (Greek+Latin)** — confirmed present and located in the prior pass, not deep-read
   this session; all Irenaeus quotations above come from the Latin-only 1639 edition instead. If Greek text
   of III.11.8 specifically is wanted (some of it survives in Greek via other citation chains), Grabe 1702
   is the next thing to check.
4. **Marcion's *Antitheses* itself** — mentioned by name and structure in Tertullian (Adv. Marc. IV,
   quoted at the top of §1.1's Book IV citation — "Antitheses cognominatum... quo duos deos dividens") but
   no attempt was made this session to extract a reconstructed list of its actual contrasts; Tertullian
   engages with it thematically rather than quoting it as a numbered list in the sections read.

## Verification commands run this session

```bash
curl -s "https://archive.org/metadata/bim_early-english-books-1641-1700_tertulliani-opera-_tertullian_1689"
curl -sL -o tertullian1689.txt "https://archive.org/download/bim_early-english-books-1641-1700_tertulliani-opera-_tertullian_1689/bim_early-english-books-1641-1700_tertulliani-opera-_tertullian_1689_djvu.txt"
grep -n -i "marcion" tertullian1689.txt

curl -sL -o irenaeus1639.txt "https://archive.org/download/sanctiirenaeilug0000vari/sanctiirenaeilug0000vari_djvu.txt"
grep -n -i "quatuor.*regiones\|marcion" irenaeus1639.txt

curl -sL -o epiph1.txt "https://archive.org/download/bub_gb_1Wfnrs5Tw4MC/bub_gb_1Wfnrs5Tw4MC_djvu.txt"
grep -n -i "marcion" epiph1.txt

curl -sL -o muratori1738.txt "https://archive.org/download/antiquitatesit03mura/antiquitatesit03mura_djvu.txt"
grep -n -i "marcion" muratori1738.txt

# PD status check for modern reconstructions
curl -s "https://archive.org/advancedsearch.php?q=title%3A%28Marcion%29+AND+creator%3A%28Harnack%29&fl%5B%5D=identifier&fl%5B%5D=year&rows=20&output=json"
```

Files pulled this session are in the scratchpad, not committed to the corpus — this document is the durable
output; the raw `_djvu.txt` pulls were working copies for grepping quotes, not archival copies.
