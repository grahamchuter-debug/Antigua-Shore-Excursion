"""Antigua Shore Excursion — World 2.0 Phase 15B site configuration."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DOMAIN = "antiguashoreexcursion.com"
APEX = f"https://{DOMAIN}"
SITE = "Antigua Shore Excursion"
EMAIL = "hello@antiguashoreexcursion.com"
DATE = "2026-09-10"
ACCENT = "text-pr-400"

FONTS = (
    "https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700"
    "&family=Source+Sans+3:wght@400;500;600;700&display=swap"
)

HERO_GRADIENT = (
    "linear-gradient(140deg, rgba(15, 23, 42, 0.78) 0%, "
    "rgba(30, 64, 175, 0.62) 42%, rgba(249, 115, 22, 0.38) 72%, "
    "rgba(0, 0, 0, 0.22) 100%)"
)

# Active Antigua-location assets only (see images/ATTRIBUTION.md).
# Wrong-island / duplicate files live under images/quarantine/ and must not be referenced.
HERO_HOME = "/images/hero-antigua.png"
HERO_HOME_ALT = (
    "Dickenson Bay beach in Antigua with turquoise Caribbean water "
    "for cruise passengers planning shore time from St John's"
)

CRUISE_PORT = "/images/antigua-cruise-port.png"
CRUISE_PORT_ALT = (
    "St John's Antigua cruise harbour with ships and colourful waterfront "
    "near Heritage Quay and Redcliffe Quay"
)

PORT_ARRIVAL = "/images/antigua-port-arrival.png"
PORT_ARRIVAL_ALT = (
    "Cruise ship at St John's harbour Antigua for port-day arrival planning"
)

INTRO = "/images/antigua-intro.png"
INTRO_ALT = (
    "Antigua coastline with turquoise water and green hills "
    "near typical shore-excursion routes from St John's"
)

BEACHES = "/images/antigua-beaches.png"
BEACHES_ALT = (
    "Sea Grapes Beach at Hawksbill Bay Antigua — a west-coast beach "
    "option often considered by cruise passengers"
)

NELSONS = "/images/nelsons-dockyard.png"
NELSONS_ALT = (
    "Nelson's Dockyard at English Harbour Antigua, a UNESCO-listed "
    "historic harbour visited on many south-coast day trips from St John's"
)

HISTORY = "/images/history-culture-tour.png"
HISTORY_ALT = (
    "English Harbour and Nelson's Dockyard waterfront in Antigua "
    "for history-focused cruise shore planning"
)

SHIRLEY = "/images/shirley-heights.png"
SHIRLEY_ALT = (
    "Shirley Heights lookout above English Harbour Antigua "
    "with panoramic harbour and Caribbean views"
)

EXPERIENCE = "/images/the-antiguan-experience.png"
EXPERIENCE_ALT = (
    "Antigua countryside scenery representing island sightseeing "
    "and culture-and-beach style shore days from St John's"
)

# Honest stand-ins / CSS-only where no safe dedicated photo exists
EXCURSIONS_HERO = NELSONS
EXCURSIONS_HERO_ALT = NELSONS_ALT
ONE_DAY_HERO = SHIRLEY
ONE_DAY_HERO_ALT = SHIRLEY_ALT
CLASSIC_BEACH_HERO = HERO_HOME
CLASSIC_BEACH_HERO_ALT = HERO_HOME_ALT
# Kayak / reef pages: no active wrong-island imagery — CSS-only heroes
KAYAK_HERO = None
HALF_DAY_KAYAK_HERO = None

PROTECTED_ROUTES: list[dict] = [
    {"path": "/", "file": "index.html", "kind": "home"},
    {
        "path": "/best-antigua-shore-excursions/",
        "file": "best-antigua-shore-excursions/index.html",
        "kind": "hub",
    },
    {
        "path": "/antigua-port-guide/",
        "file": "antigua-port-guide/index.html",
        "kind": "guide",
    },
    {
        "path": "/one-day-in-antigua-from-a-cruise-ship/",
        "file": "one-day-in-antigua-from-a-cruise-ship/index.html",
        "kind": "guide",
    },
    {
        "path": "/best-beaches-in-antigua-for-cruise-passengers/",
        "file": "best-beaches-in-antigua-for-cruise-passengers/index.html",
        "kind": "guide",
    },
    {
        "path": "/can-you-explore-antigua-without-an-excursion/",
        "file": "can-you-explore-antigua-without-an-excursion/index.html",
        "kind": "decision",
    },
    {
        "path": "/classic-beach-day/",
        "file": "classic-beach-day/index.html",
        "kind": "attraction",
    },
    {
        "path": "/antigua-exclusive-history-and-culture-tour/",
        "file": "antigua-exclusive-history-and-culture-tour/index.html",
        "kind": "attraction",
    },
    {
        "path": "/antigua-kayak-snorkel-and-beach/",
        "file": "antigua-kayak-snorkel-and-beach/index.html",
        "kind": "attraction",
    },
    {
        "path": "/nelsons-dockyard-from-antigua-cruise-port/",
        "file": "nelsons-dockyard-from-antigua-cruise-port/index.html",
        "kind": "attraction",
    },
    {
        "path": "/shirley-heights-antigua-guide/",
        "file": "shirley-heights-antigua-guide/index.html",
        "kind": "attraction",
    },
    {
        "path": "/the-antiguan-experience/",
        "file": "the-antiguan-experience/index.html",
        "kind": "attraction",
    },
    {
        "path": "/antigua-half-day-kayak-and-snorkel/",
        "file": "antigua-half-day-kayak-and-snorkel/index.html",
        "kind": "attraction",
    },
    {
        "path": "/panoramic-antigua-and-beach-break/",
        "file": "panoramic-antigua-and-beach-break/index.html",
        "kind": "attraction",
    },
    {
        "path": "/is-antigua-safe-for-cruise-passengers/",
        "file": "is-antigua-safe-for-cruise-passengers/index.html",
        "kind": "guide",
    },
    {"path": "/contact/", "file": "contact/index.html", "kind": "trust"},
    {"path": "/about/", "file": "about/index.html", "kind": "trust"},
    {"path": "/privacy/", "file": "privacy/index.html", "kind": "trust"},
    {"path": "/terms/", "file": "terms/index.html", "kind": "trust"},
    {"path": "/methodology/", "file": "methodology/index.html", "kind": "trust"},
    {"path": "/404.html", "file": "404.html", "kind": "error", "sitemap": False},
]
