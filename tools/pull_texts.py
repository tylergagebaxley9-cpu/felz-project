#!/usr/bin/env python3
"""
pull_texts.py — download every verified archive.org text layer into
early-editions/scans/, skipping copyrighted items.

Reads docs/PULLABLE.tsv (identifier, file, bytes) produced by the metadata
sweep. Resumes: a file already on disk at the expected size is skipped.
Failures are reported at the end and never silently swallowed.
"""
import csv, os, sys, urllib.parse, urllib.request, time, hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'early-editions', 'scans')

# Deutsche Bibelgesellschaft uploads — NA28 / copyrighted LXX. Not ours to take.
BLOCKED = {'GRCNA28_DBS_HS', 'LATSEPT_DBS_HS'}

def main():
    rows = list(csv.DictReader(open(os.path.join(ROOT, 'docs', 'PULLABLE.tsv')),
                               delimiter='\t'))
    rows = [r for r in rows if r['identifier'] not in BLOCKED]
    os.makedirs(OUT, exist_ok=True)

    total = len(rows)
    done = skipped = failed = 0
    bytes_got = 0
    errors = []

    for n, r in enumerate(rows, 1):
        ident, fname, size = r['identifier'], r['file'], int(r['bytes'])
        # Filenames must stay under the 255-byte ext4 limit. Archive.org
        # filenames run to 200+ chars, so truncate and disambiguate with a
        # short hash of the full original name (kept in the sidecar index).
        safe = f"{ident}__{fname}".replace('/', '_')
        if len(safe.encode()) > 200:
            h = hashlib.sha1(f"{ident}/{fname}".encode()).hexdigest()[:8]
            stem = safe[:170].rstrip('. ')
            safe = f"{stem}~{h}_djvu.txt"
        dest = os.path.join(OUT, safe)

        if os.path.exists(dest) and abs(os.path.getsize(dest) - size) < 64:
            skipped += 1
            continue

        url = (f"https://archive.org/download/{urllib.parse.quote(ident)}/"
               f"{urllib.parse.quote(fname)}")
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'bible-sources/1.0'})
            with urllib.request.urlopen(req, timeout=180) as resp, open(dest, 'wb') as fh:
                while True:
                    chunk = resp.read(262144)
                    if not chunk:
                        break
                    fh.write(chunk)
            got = os.path.getsize(dest)
            bytes_got += got
            done += 1
            print(f"[{n}/{total}] OK   {got/1048576:7.2f} MB  {safe[:70]}", flush=True)
        except Exception as e:
            failed += 1
            errors.append((ident, fname, str(e)[:80]))
            if os.path.exists(dest):
                os.remove(dest)
            print(f"[{n}/{total}] FAIL              {safe[:70]}  {e}", flush=True)
        time.sleep(0.2)   # be polite to archive.org

    print("\n" + "=" * 62)
    print(f"downloaded : {done}")
    print(f"skipped    : {skipped} (already present)")
    print(f"failed     : {failed}")
    print(f"new bytes  : {bytes_got/1048576:.1f} MB")
    if errors:
        print("\nFAILURES:")
        for i, f, e in errors:
            print(f"  {i} :: {f} :: {e}")
        sys.exit(1)
    print("all files retrieved")


if __name__ == '__main__':
    main()
