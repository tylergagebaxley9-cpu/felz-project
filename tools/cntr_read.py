#!/usr/bin/env python3
"""
cntr_read.py — pull a verse range out of a CNTR (Center for New Testament
Restoration) manuscript-encoding-specification (MES) transcription and
render readable Greek.

Source: papyri/cntr-transcriptions/{class 1,class 2}/*.txt
Each line is "BBCCCVVV <MES text>" where BB=book (40=Matt...66=Rev),
CCC=chapter (3 digits), VVV=verse (3 digits). A line of just "-" means
the verse is not present in that witness at all (whole verse absent,
not just damaged).

MES editorial marks (see papyri/cntr-transcriptions/README.md):
  \\ page break   |  column break   /  line break   &  lacuna remnant
  %  damaged char ^  missing char   ~  word supplied  +  supplied by vid
  =  nomina sacra $  numeric abbrev
  x{...} = original uncorrected reading, a{...}/b{...} = later correctors'
           readings (we print the FIRST alternative after x{}, i.e. the
           correction actually adopted textually, and note correction).
  [...]  questionable text

This script strips the apparatus noise for a plain reading and can also
dump the raw line for inspection with --raw.

Usage:
    ./cntr_read.py P66 43 1 14 18        # John 1:14-18 in P66
    ./cntr_read.py 01 41 16 1 20         # Mark 16:1-20 in Sinaiticus (GA 01)
    ./cntr_read.py 03 45 8 1 1 --raw     # Vaticanus Rom 8:1, raw MES

GA sigla present on disk (papyri/cntr-transcriptions/class 1/):
    01 Sinaiticus (IV)   02 Alexandrinus (V)   03 Vaticanus (IV)
    04 Ephraemi Rescriptus (V)   05 Bezae (V)   032 Washingtonianus (V)
    + P1-P141 papyri (II-VIII c.)
Book numbers: 40 Matt 41 Mark 42 Luke 43 John 44 Acts 45 Rom 46 1Cor
    47 2Cor 48 Gal 49 Eph 50 Phil 51 Col 52 1Thess 53 2Thess 54 1Tim
    55 2Tim 56 Titus 57 Phlm 58 Heb 59 Jas 60 1Pet 61 2Pet 62 1Jo
    63 2Jo 64 3Jo 65 Jude 66 Rev
"""
import sys, os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = f'{ROOT}/papyri/cntr-transcriptions'

BOOKS = {
    'Matt':40,'Mark':41,'Luke':42,'John':43,'Acts':44,'Rom':45,'1Cor':46,
    '2Cor':47,'Gal':48,'Eph':49,'Phil':50,'Col':51,'1Thess':52,'2Thess':53,
    '1Tim':54,'2Tim':55,'Titus':56,'Phlm':57,'Heb':58,'Jas':59,'1Pet':60,
    '2Pet':61,'1Jo':62,'2Jo':63,'3Jo':64,'Jude':65,'Rev':66,
}


def find_file(siglum):
    for cls in ('class 1', 'class 2'):
        for ext in ('', '.txt'):
            p = f'{BASE}/{cls}/{siglum}{ext}'
            if os.path.exists(p):
                return p
    # try case-insensitive / with P prefix variants
    for cls in ('class 1', 'class 2'):
        for p in glob.glob(f'{BASE}/{cls}/*.txt'):
            if os.path.basename(p).lower() == f'{siglum.lower()}.txt':
                return p
    return None


def clean_mes(raw):
    """Strip MES apparatus down to a single running Greek reading.

    Policy: keep the CORRECTED / edited reading where scribal correction
    marks exist (x{orig}{corr} -> corr); drop page/col/line marks; drop
    supplied-text markers but keep the supplied letters themselves (they
    are the editor's best reconstruction of damaged papyrus, not an
    insertion); keep nomina-sacra letters as-is (=θς stays θς) since
    expanding them is an editorial choice this script won't silently make.
    """
    s = raw
    # x{original}{correction} or x{original} a{correction} -> take the LAST
    # braced alternative (latest hand = the corrected/adopted reading)
    def pick_last_brace(m):
        alts = re.findall(r'\{([^{}]*)\}', m.group(0))
        return alts[-1] if alts else ''
    s = re.sub(r'(?:[xab]\{[^{}]*\}){1,}', pick_last_brace, s)
    # strip remaining structural / damage marks but keep letters
    s = re.sub(r'[\\|/&*%^~+$\[\]]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def read_verses(siglum, book_no, chapter, v_start, v_end=None):
    v_end = v_end or v_start
    path = find_file(siglum)
    if not path:
        return None, f'no CNTR file found for siglum {siglum}'
    out = []
    with open(path, encoding='utf8') as f:
        for line in f:
            line = line.rstrip('\n')
            if len(line) < 8 or not line[:8].isdigit():
                continue
            ref, rest = line[:8], line[9:]
            b, c, v = int(ref[:2]), int(ref[2:5]), int(ref[5:8])
            if b == book_no and c == chapter and v_start <= v <= v_end:
                out.append((v, rest.strip()))
    out.sort()
    return out, None


def main():
    args = sys.argv[1:]
    raw = '--raw' in args
    args = [a for a in args if a != '--raw']
    if len(args) not in (4, 5):
        print(__doc__)
        sys.exit(1)
    # cntr_read.py SIGLUM BOOK CH V1 [V2]
    siglum = args[0]
    book_no = int(args[1])
    chapter = int(args[2])
    v_start = int(args[3])
    v_end = int(args[4]) if len(args) == 5 else v_start

    verses, err = read_verses(siglum, book_no, chapter, v_start, v_end)
    if err:
        print(err)
        sys.exit(1)
    if not verses:
        print(f'{siglum} {book_no}.{chapter}.{v_start}-{v_end}: no lines found '
              f'(outside this witness\'s surviving text, or wrong ref)')
        sys.exit(0)
    for v, text in verses:
        if text.strip() == '-':
            print(f'  v{v}: [VERSE ABSENT — not in this witness]')
            continue
        shown = text if raw else clean_mes(text)
        print(f'  v{v}: {shown}')


if __name__ == '__main__':
    main()
