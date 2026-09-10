#!/usr/bin/env python3
"""QA checks for Antigua Shore Excursion Phase 15B static build."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "scripts" / "protected_routes.json"

QUARANTINE_NAMES = (
    "antigua-kayak-snorkel.png",
    "half-day-kayak-snorkel.png",
    "cades-reef.png",
    "classic-beach-day.png",
    "best-antigua-excursions.png",
    "one-day-antigua.png",
    "panoramic-antigua.png",
)

BANNED_SUBSTRINGS = (
    "cdn.tailwindcss.com",
    "shoreexcursionsgroup",
    "info@wowatour.com",
    "partials/",
    "data-content=",
    "Most-booked",
    "Most-booked",
    "Return To Ship On Time",
    "Return to Ship on Time",
)

SEG_CODE_RE = re.compile(r"\bCAA[A-Z]{2,}[A-Z0-9]*\b")
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.I | re.S)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.I | re.S)


def fail(msg: str, errors: list[str]) -> None:
    errors.append(msg)
    print(f"FAIL: {msg}")


def main() -> int:
    errors: list[str] = []
    print("QA Antigua Phase 15B…")

    if not MANIFEST.exists():
        fail(f"missing {MANIFEST.relative_to(ROOT)}", errors)
        return 1

    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    routes = data.get("routes") or []
    if not routes:
        fail("protected_routes.json has no routes", errors)

    html_files: list[Path] = []
    for route in routes:
        rel = route.get("file")
        if not rel:
            fail(f"route missing file: {route}", errors)
            continue
        path = ROOT / rel
        if not path.exists():
            fail(f"protected route file missing: {rel}", errors)
        else:
            html_files.append(path)
            print(f"  ok file {rel}")

    titles: dict[str, str] = {}
    h1s: dict[str, str] = {}
    contact_ok = False

    for path in html_files:
        text = path.read_text(encoding="utf-8", errors="replace")
        rel = str(path.relative_to(ROOT))

        for name in QUARANTINE_NAMES:
            if name in text:
                fail(f"quarantine image ref in {rel}: {name}", errors)

        if "/images/quarantine/" in text or "images/quarantine/" in text:
            fail(f"quarantine path ref in {rel}", errors)

        for banned in BANNED_SUBSTRINGS:
            if banned.lower() in text.lower():
                fail(f"banned string in {rel}: {banned}", errors)

        if SEG_CODE_RE.search(text):
            fail(f"possible SEG product code in {rel}", errors)

        if "js/site.js" in text or 'fetch(' in text and "partials" in text:
            fail(f"legacy partial loader pattern in {rel}", errors)

        if 'id="page-content"' in text and "data-content=" in text:
            fail(f"JS-shell pattern in {rel}", errors)

        # Must have inlined main content (not empty main)
        if '<main id="main-content"' in text:
            m = re.search(
                r'<main id="main-content"[^>]*>(.*?)</main>', text, re.I | re.S
            )
            if m and len(re.sub(r"\s+", "", m.group(1))) < 80:
                fail(f"thin/empty main content in {rel}", errors)

        mt = TITLE_RE.search(text)
        if mt:
            title = re.sub(r"\s+", " ", mt.group(1)).strip()
            if title in titles:
                fail(f"duplicate title in {rel} and {titles[title]}: {title}", errors)
            else:
                titles[title] = rel
        else:
            fail(f"missing title in {rel}", errors)

        mh = H1_RE.search(text)
        if mh:
            h1 = re.sub(r"<[^>]+>", " ", mh.group(1))
            h1 = re.sub(r"\s+", " ", h1).strip()
            if h1 in h1s:
                fail(f"duplicate H1 in {rel} and {h1s[h1]}: {h1}", errors)
            else:
                h1s[h1] = rel
        else:
            fail(f"missing H1 in {rel}", errors)

        if "canonical" not in text.lower():
            fail(f"missing canonical in {rel}", errors)

        if rel == "contact/index.html":
            if "hello@antiguashoreexcursion.com" in text:
                contact_ok = True

    if not contact_ok:
        fail("contact page missing hello@antiguashoreexcursion.com", errors)

    # Worker + wrangler presence
    if not (ROOT / "worker.js").exists():
        fail("missing worker.js", errors)
    wr = (ROOT / "wrangler.jsonc").read_text(encoding="utf-8")
    if "not_found_handling" not in wr:
        fail("wrangler missing not_found_handling", errors)
    if "run_worker_first" not in wr:
        fail("wrangler missing run_worker_first", errors)

    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    if ".html</loc>" in sitemap:
        fail("sitemap still lists .html URLs", errors)
    if "www.antiguashoreexcursion.com" in sitemap:
        fail("sitemap lists www host", errors)

    if errors:
        print(f"{len(errors)} error(s)")
        return 1
    print("QA passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
