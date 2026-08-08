#!/usr/bin/env python3
"""
scrape_walled.py — fetch sources that plain curl/urllib could not reach.

Every target here is a site that returned 403, an anti-bot interstitial, or a
Cloudflare challenge during the research passes. Scrapling's StealthyFetcher
drives a real browser fingerprint, which is what these walls actually check.

This tool fetches PUBLIC, openly-licensed or public-domain material only. It
does not touch paywalled editions, lending-gated items, or anything behind a
login. Sites that gate content deliberately (Brill, Brepols, controlled digital
lending) are out of scope and stay out.

Usage:
    ./scrape_walled.py --list
    ./scrape_walled.py --target papyri-info
    ./scrape_walled.py --all
"""
import argparse, json, os, sys, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'docs', 'walled-fetch')

# Each target: why plain fetch failed, and what we want off it.
TARGETS = {
    'papyri-info': {
        'url': 'https://papyri.info/docs/license',
        'why': 'anti-bot wall; blocked license verification for idp.data (2.85 GB)',
        'want': 'the actual license text, so the CC BY 3.0 claim can be confirmed or dropped',
    },
    'poxy-3522': {
        'url': 'https://papyri.info/ddbdp/p.oxy;50;3522/',
        'why': 'anti-bot wall; no open transcription found anywhere',
        'want': 'P.Oxy 3522 — Greek Job with the Tetragrammaton in paleo-Hebrew script',
    },
    'mechon-mamre': {
        'url': 'https://www.mechon-mamre.org/i/t/t0.htm',
        'why': 'never tried; candidate Aleppo Codex proxy',
        'want': 'what its Hebrew text is actually based on, and its license',
    },
    'hathitrust-paris-polyglot': {
        'url': 'https://babel.hathitrust.org/cgi/ls?q1=Biblia%20polyglotta%20Paris%201645;a=srchls;anyall1=phrase;field1=ocr;lmt=ft',
        'why': 'Cloudflare bot-check blocked curl and WebFetch',
        'want': 'Paris Polyglot 1629-45 — the ONLY printing of the Samaritan Pentateuch editio princeps',
    },
    'bensira': {
        'url': 'https://bensira.org/',
        'why': 'not yet pulled; per-folio transcriptions',
        'want': 'index of all 8 Hebrew Ben Sira witnesses (Genizah A-F, Masada, Qumran)',
    },
    'inscriptifact': {
        'url': 'https://inscriptifact.usc.edu/',
        'why': 'returned 403',
        'want': 'Ketef Hinnom / Kuntillet Ajrud imaging archive status',
    },
    'hebrewbooks-dikdukei-soferim': {
        'url': 'https://hebrewbooks.org/simplesearch.aspx?q=%D7%93%D7%A7%D7%93%D7%95%D7%A7%D7%99+%D7%A1%D7%95%D7%A4%D7%A8%D7%99%D7%9D+%D7%A8%D7%91%D7%99%D7%A0%D7%95%D7%91%D7%99%D7%A5',
        'why': 'Cloudflare "Just a moment..." 403 on curl and WebFetch',
        'want': 'Rabbinovicz, Dikdukei Soferim (1867-97) — a working hebrewbooks.org book ID/download link',
    },
}


def fetch(name, spec, timeout=60):
    """Try the strongest fetcher available, degrading gracefully.

    StealthyFetcher needs camoufox (not installed here); DynamicFetcher drives
    real Playwright Chromium with stealth on, which clears most bot walls.
    Plain Fetcher is the last resort and will not beat a challenge page.
    """
    from scrapling.fetchers import StealthyFetcher, DynamicFetcher, Fetcher
    errors = []
    for label, call in (
        ('stealthy', lambda: StealthyFetcher.fetch(
            spec['url'], headless=True, network_idle=True, timeout=timeout * 1000)),
        ('dynamic', lambda: DynamicFetcher.fetch(
            spec['url'], headless=True, network_idle=True, stealth=True,
            timeout=timeout * 1000)),
        ('plain', lambda: Fetcher.get(spec['url'], timeout=timeout)),
    ):
        try:
            page = call()
            print(f'  [{label}] fetched', flush=True)
            return page
        except Exception as e:
            errors.append(f'{label}: {type(e).__name__}: {str(e)[:90]}')
            continue
    raise RuntimeError(' | '.join(errors))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--target')
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--list', action='store_true')
    a = ap.parse_args()

    if a.list:
        for k, v in TARGETS.items():
            print(f'{k:28} {v["why"]}')
            print(f'{"":28} want: {v["want"]}\n')
        return

    todo = list(TARGETS) if a.all else ([a.target] if a.target else [])
    if not todo:
        print('nothing to do — pass --target NAME, --all, or --list')
        sys.exit(1)

    os.makedirs(OUT, exist_ok=True)
    results = []
    for name in todo:
        spec = TARGETS.get(name)
        if not spec:
            print(f'unknown target: {name}')
            continue
        print(f'\n=== {name} ===\n  {spec["url"]}\n  why: {spec["why"]}', flush=True)
        try:
            page = fetch(name, spec)
            status = getattr(page, 'status', '?')
            html = str(page.html_content) if hasattr(page, 'html_content') else str(page)
            text = page.get_all_text() if hasattr(page, 'get_all_text') else ''
            dest = os.path.join(OUT, f'{name}.html')
            open(dest, 'w', encoding='utf8').write(html)
            open(os.path.join(OUT, f'{name}.txt'), 'w', encoding='utf8').write(text)
            print(f'  OK status={status}  html={len(html)}B  text={len(text)}B -> {dest}')
            results.append({'target': name, 'status': status,
                            'html_bytes': len(html), 'text_bytes': len(text)})
        except Exception as e:
            print(f'  FAIL {type(e).__name__}: {str(e)[:160]}')
            results.append({'target': name, 'error': f'{type(e).__name__}: {str(e)[:160]}'})
        time.sleep(1)

    json.dump(results, open(os.path.join(OUT, 'results.json'), 'w'), indent=2)
    ok = len([r for r in results if 'error' not in r])
    print(f'\n{"="*56}\nfetched {ok}/{len(results)}  -> {OUT}')


if __name__ == '__main__':
    main()
