#!/usr/bin/env python3
"""Build Antigua Shore Excursion World 2.0 static HTML (Phase 15B)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from antigua_config import APEX, PROTECTED_ROUTES, ROOT as SITE_ROOT  # noqa: E402
from antigua_pages import (  # noqa: E402
    about,
    antiguan_experience,
    beaches,
    best_excursions,
    classic_beach_day,
    contact,
    diy,
    half_day_kayak,
    history_culture,
    home,
    kayak_snorkel,
    methodology,
    nelsons,
    not_found,
    one_day,
    panoramic,
    port_guide,
    privacy,
    safety,
    shirley,
    terms,
)
from antigua_shell import page_shell  # noqa: E402


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(f"  wrote {path.relative_to(SITE_ROOT)}")


def render(builder, *, robots: str | None = None, include_trust: bool = True) -> str:
    hero, main, faqs, meta = builder()
    return page_shell(
        meta["title"],
        meta["description"],
        meta["canonical_path"],
        meta["page_id"],
        hero,
        main,
        meta.get("og_image"),
        faq_entities=faqs,
        robots=robots,
        include_trust=include_trust,
    )


PAGES: list[tuple[str, object, dict]] = [
    ("index.html", home, {}),
    ("best-antigua-shore-excursions/index.html", best_excursions, {}),
    ("antigua-port-guide/index.html", port_guide, {}),
    ("one-day-in-antigua-from-a-cruise-ship/index.html", one_day, {}),
    ("best-beaches-in-antigua-for-cruise-passengers/index.html", beaches, {}),
    ("can-you-explore-antigua-without-an-excursion/index.html", diy, {}),
    ("classic-beach-day/index.html", classic_beach_day, {}),
    ("antigua-exclusive-history-and-culture-tour/index.html", history_culture, {}),
    ("antigua-kayak-snorkel-and-beach/index.html", kayak_snorkel, {}),
    ("nelsons-dockyard-from-antigua-cruise-port/index.html", nelsons, {}),
    ("shirley-heights-antigua-guide/index.html", shirley, {}),
    ("the-antiguan-experience/index.html", antiguan_experience, {}),
    ("antigua-half-day-kayak-and-snorkel/index.html", half_day_kayak, {}),
    ("panoramic-antigua-and-beach-break/index.html", panoramic, {}),
    ("is-antigua-safe-for-cruise-passengers/index.html", safety, {}),
    ("contact/index.html", contact, {}),
    ("about/index.html", about, {}),
    ("privacy/index.html", privacy, {}),
    ("terms/index.html", terms, {}),
    ("methodology/index.html", methodology, {}),
]


def build_pages() -> None:
    for rel, builder, opts in PAGES:
        write(SITE_ROOT / rel, render(builder, **opts))
    write(
        SITE_ROOT / "404.html",
        render(not_found, robots="noindex, follow", include_trust=False),
    )


def build_sitemap() -> None:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for route in PROTECTED_ROUTES:
        if route.get("sitemap") is False:
            continue
        path = route["path"]
        loc = f"{APEX}/" if path == "/" else f"{APEX}{path}"
        kind = route.get("kind", "")
        if path == "/":
            pri, freq = "1.0", "weekly"
        elif kind in {"hub", "guide", "attraction", "decision"}:
            pri, freq = "0.9", "monthly"
        else:
            pri, freq = "0.5", "yearly"
        lines.extend(
            [
                "  <url>",
                f"    <loc>{loc}</loc>",
                f"    <changefreq>{freq}</changefreq>",
                f"    <priority>{pri}</priority>",
                "  </url>",
            ]
        )
    lines.append("</urlset>")
    lines.append("")
    write(SITE_ROOT / "sitemap.xml", "\n".join(lines))


def build_robots() -> None:
    write(
        SITE_ROOT / "robots.txt",
        f"""User-agent: *
Allow: /

Sitemap: {APEX}/sitemap.xml
""",
    )


def build_protected_manifest() -> None:
    manifest = {
        "domain": APEX,
        "phase": "15B",
        "canonical_policy": "trailing-slash-extensionless-on-apex",
        "routes": PROTECTED_ROUTES,
    }
    write(
        SITE_ROOT / "scripts" / "protected_routes.json",
        json.dumps(manifest, indent=2) + "\n",
    )


def main() -> None:
    print("Building Antigua Shore Excursion World 2.0 (Phase 15B)…")
    build_pages()
    build_sitemap()
    build_robots()
    build_protected_manifest()
    print("Build complete.")


if __name__ == "__main__":
    main()
