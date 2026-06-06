"""Antigua Shore Excursion site configuration."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://antiguashoreexcursion.com"
SITE = "Antigua Shore Excursion"
DATE = "2026-06-06"
FONTS = (
    "https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700"
    "&family=Source+Sans+3:wght@400;500;600;700&display=swap"
)
HERO_GRADIENT = (
    "linear-gradient(135deg, rgba(37, 99, 235, 0.75) 0%, "
    "rgba(249, 115, 22, 0.65) 50%, rgba(30, 58, 138, 0.55) 100%)"
)
ACCENT = "text-pr-300"

HOME_HERO = "images/hero-antigua.png"
HOME_HERO_ALT = (
    "Turquoise Caribbean water and white sand beach in Antigua for cruise "
    "passengers planning shore excursions from St John's cruise port"
)
PORT_IMG = "images/antigua-cruise-port.png"
PORT_ALT = (
    "St John's Antigua cruise port with colourful harbour and cruise ships "
    "docked for shore excursion passengers in Antigua and Barbuda"
)
PORT_ARRIVAL_IMG = "images/antigua-port-arrival.png"
PORT_ARRIVAL_ALT = (
    "Cruise ship at St John's harbour Antigua with Heritage Quay and "
    "Redcliffe Quay waterfront for cruise passenger port day planning"
)
BEST_IMG = "images/best-antigua-excursions.png"
BEST_ALT = (
    "Nelson's Dockyard and Shirley Heights representing the best Antigua "
    "shore excursions for cruise passengers from St John's port"
)
ONE_DAY_IMG = "images/one-day-antigua.png"
ONE_DAY_ALT = (
    "English Harbour and St John's Antigua coastline for planning a one-day "
    "cruise ship shore excursion itinerary in Antigua and Barbuda"
)
INTRO_IMG = "images/antigua-intro.png"
INTRO_ALT = (
    "Antigua coastline with turquoise Caribbean water and tropical scenery "
    "near St John's cruise port for beach and culture shore excursions"
)

ANTIGUAN_EXPERIENCE_IMG = "images/the-antiguan-experience.png"
ANTIGUAN_EXPERIENCE_ALT = (
    "Antigua countryside and cultural setting on The Antiguan Experience "
    "shore excursion with pineapple farm visit from St John's cruise port"
)
CLASSIC_BEACH_IMG = "images/classic-beach-day.png"
CLASSIC_BEACH_ALT = (
    "White sand beach with calm turquoise water on Classic Beach Day "
    "Antigua shore excursion for cruise passengers from St John's port"
)
KAYAK_SNORKEL_IMG = "images/antigua-kayak-snorkel.png"
KAYAK_SNORKEL_ALT = (
    "Kayaks in Antigua mangrove lagoon and snorkelers over reef on "
    "Antigua Kayak Snorkel and Beach shore excursion from St John's"
)
HISTORY_CULTURE_IMG = "images/history-culture-tour.png"
HISTORY_CULTURE_ALT = (
    "Nelson's Dockyard English Harbour Antigua on Exclusive History and "
    "Culture Tour shore excursion for St John's cruise passengers"
)
PANORAMIC_IMG = "images/panoramic-antigua.png"
PANORAMIC_ALT = (
    "Panoramic Antigua coastline viewpoint from Shirley Heights scenic "
    "shore excursion with beach break for cruise passengers St John's"
)
HALF_DAY_KAYAK_IMG = "images/half-day-kayak-snorkel.png"
HALF_DAY_KAYAK_ALT = (
    "Half day kayak through mangrove lagoon and snorkel at Cades Reef "
    "Antigua shore excursion for cruise passengers from St John's port"
)

NELSONS_DOCKYARD_IMG = "images/nelsons-dockyard.png"
NELSONS_DOCKYARD_ALT = (
    "Nelson's Dockyard UNESCO World Heritage site English Harbour Antigua "
    "visited on history shore excursions from St John's cruise port"
)
SHIRLEY_HEIGHTS_IMG = "images/shirley-heights.png"
SHIRLEY_HEIGHTS_ALT = (
    "Shirley Heights military lookout overlooking English Harbour Antigua "
    "for cruise passengers on Nelson's Dockyard and scenic island tours"
)
BEACHES_IMG = "images/antigua-beaches.png"
BEACHES_ALT = (
    "Hawksbill Bay white sand beach near St John's Antigua for cruise "
    "passenger beach day shore excursions in Antigua and Barbuda"
)
CADES_REEF_IMG = "images/cades-reef.png"
CADES_REEF_ALT = (
    "Snorkeling over coral reef in clear Caribbean water at Cades Reef "
    "Antigua on kayak and snorkel shore excursions from St John's port"
)

ALL_IMAGES = [
    HOME_HERO, PORT_IMG, PORT_ARRIVAL_IMG, BEST_IMG, ONE_DAY_IMG, INTRO_IMG,
    ANTIGUAN_EXPERIENCE_IMG, CLASSIC_BEACH_IMG, KAYAK_SNORKEL_IMG,
    HISTORY_CULTURE_IMG, PANORAMIC_IMG, HALF_DAY_KAYAK_IMG,
    NELSONS_DOCKYARD_IMG, SHIRLEY_HEIGHTS_IMG, BEACHES_IMG, CADES_REEF_IMG,
]

SITEMAP_PAGES = [
    ("", "1.0", "weekly"),
    ("best-antigua-shore-excursions.html", "0.9", "monthly"),
    ("antigua-port-guide.html", "0.8", "monthly"),
    ("one-day-in-antigua-from-a-cruise-ship.html", "0.8", "monthly"),
    ("best-beaches-in-antigua-for-cruise-passengers.html", "0.8", "monthly"),
    ("nelsons-dockyard-from-antigua-cruise-port.html", "0.8", "monthly"),
    ("shirley-heights-antigua-guide.html", "0.8", "monthly"),
    ("is-antigua-safe-for-cruise-passengers.html", "0.8", "monthly"),
    ("can-you-explore-antigua-without-an-excursion.html", "0.8", "monthly"),
    ("the-antiguan-experience.html", "0.9", "monthly"),
    ("classic-beach-day.html", "0.9", "monthly"),
    ("antigua-kayak-snorkel-and-beach.html", "0.9", "monthly"),
    ("antigua-exclusive-history-and-culture-tour.html", "0.9", "monthly"),
    ("panoramic-antigua-and-beach-break.html", "0.9", "monthly"),
    ("antigua-half-day-kayak-and-snorkel.html", "0.9", "monthly"),
]

SHIP_ICON = (
    '<svg fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">'
    '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" '
    'd="M3 17h18M5 17l2-8h10l2 8M9 9l1-4h4l1 4"/></svg>'
)

PLACEHOLDER_PNG = (
    b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01"
    b"\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89"
    b"\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n"
    b"\xdb\x00\x00\x00\x00IEND\xaeB`\x82"
)

TOUR_PAGES = [
    "the-antiguan-experience",
    "classic-beach-day",
    "antigua-kayak-snorkel-and-beach",
    "antigua-exclusive-history-and-culture-tour",
    "panoramic-antigua-and-beach-break",
    "antigua-half-day-kayak-and-snorkel",
]

GUIDE_PAGES = [
    "antigua-port-guide",
    "one-day-in-antigua-from-a-cruise-ship",
    "best-antigua-shore-excursions",
    "best-beaches-in-antigua-for-cruise-passengers",
    "nelsons-dockyard-from-antigua-cruise-port",
    "shirley-heights-antigua-guide",
    "is-antigua-safe-for-cruise-passengers",
    "can-you-explore-antigua-without-an-excursion",
]
