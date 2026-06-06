#!/usr/bin/env python3
"""Generate Antigua Shore Excursion static site files."""
from pathlib import Path

from antigua_config import (
    ACCENT,
    ALL_IMAGES,
    ANTIGUAN_EXPERIENCE_ALT,
    ANTIGUAN_EXPERIENCE_IMG,
    BEACHES_ALT,
    BEACHES_IMG,
    BEST_ALT,
    BEST_IMG,
    CLASSIC_BEACH_ALT,
    CLASSIC_BEACH_IMG,
    DATE,
    DOMAIN,
    HALF_DAY_KAYAK_ALT,
    HALF_DAY_KAYAK_IMG,
    HISTORY_CULTURE_ALT,
    HISTORY_CULTURE_IMG,
    HERO_GRADIENT,
    HOME_HERO,
    HOME_HERO_ALT,
    KAYAK_SNORKEL_ALT,
    KAYAK_SNORKEL_IMG,
    NELSONS_DOCKYARD_ALT,
    NELSONS_DOCKYARD_IMG,
    ONE_DAY_ALT,
    ONE_DAY_IMG,
    PANORAMIC_ALT,
    PANORAMIC_IMG,
    PLACEHOLDER_PNG,
    PORT_ALT,
    PORT_IMG,
    PORT_ARRIVAL_ALT,
    PORT_ARRIVAL_IMG,
    ROOT,
    SHIRLEY_HEIGHTS_ALT,
    SHIRLEY_HEIGHTS_IMG,
    SITE,
    SITEMAP_PAGES,
)
from antigua_guides import all_guide_content, home_faq_data
from antigua_helpers import hero_inner, hero_wave, home_schema, page_shell, tourist_trip_schema
from antigua_tours import all_tour_content


def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    print(f"  wrote {path}")


def hero_home() -> str:
    return f"""  <section class="site-hero">
    <div class="absolute inset-0 hero-bg" style="background-image: {HERO_GRADIENT}, url('{HOME_HERO}');" role="img" aria-label="{HOME_HERO_ALT}"></div>
    <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-3xl">
        <div class="site-hero__eyebrow inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm border border-white/30 rounded-full px-4 py-1.5 mb-3">
          <span class="w-2 h-2 rounded-full bg-pr-400 animate-pulse"></span>
          <span class="text-white/90 text-xs font-semibold tracking-widest uppercase">St John's · Antigua and Barbuda</span>
        </div>
        <h1 class="site-hero__title text-4xl sm:text-5xl lg:text-[3.25rem] font-display font-bold text-white leading-tight mb-3">
          Antigua Shore<br/><span class="{ACCENT}">Excursions</span><br/>from the Cruise Port
        </h1>
        <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed mb-5 max-w-2xl">
          Beach days, Nelson's Dockyard, Shirley Heights, kayak snorkel adventures and island culture — the shore excursions cruise passengers book most from St John's, Antigua.
        </p>
        <div class="site-hero__actions flex flex-col sm:flex-row gap-3">
          <a href="best-antigua-shore-excursions.html" class="btn-primary inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">Compare Excursions</a>
          <a href="classic-beach-day.html" class="btn-outline inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm">Classic Beach Day</a>
        </div>
        <div class="site-hero__tags flex flex-wrap gap-2 mt-5 pt-4 border-t border-white/20">
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Nelson's Dockyard</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Shirley Heights</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Beach Days</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Cruise Passengers</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">XCD &amp; USD</span>
        </div>
      </div>
    </div>
    {hero_wave()}
  </section>"""


HERO_DEFS = {
    "hero-home.html": hero_home(),
    "hero-excursions.html": hero_inner(
        "St John's · Antigua", f"Best Antigua<br/><span class=\"{ACCENT}\">Shore Excursions</span>",
        "Compare beach days, Nelson's Dockyard history, kayak snorkel adventures and scenic island tours for your ship schedule.",
        BEST_IMG, BEST_ALT, breadcrumb="Best Excursions",
    ),
    "hero-port-guide.html": hero_inner(
        "Cruise Passenger Guide", f"Antigua<br/><span class=\"{ACCENT}\">Cruise Port Guide</span>",
        "St John's terminal, Heritage Quay, distances to beaches and Nelson's Dockyard, taxis, currency and return-to-ship timing.",
        PORT_IMG, PORT_ALT, breadcrumb="Port Guide",
        cta=("best-antigua-shore-excursions.html", "View Shore Excursions →"),
        tags=["🚢 Cruise Port", "🏖️ Beaches", "💵 XCD & USD", "⚓ Nelson's Dockyard"],
    ),
    "hero-one-day.html": hero_inner(
        "Port Day Timeline", f"One Day in<br/><span class=\"{ACCENT}\">Antigua</span>",
        "Hour-by-hour plan from gangway to departure — history, beach or kayak snorkel with return-to-ship buffer.",
        ONE_DAY_IMG, ONE_DAY_ALT, breadcrumb="One Day in Antigua",
    ),
    "hero-beaches.html": hero_inner(
        "365 Beaches", f"Best Beaches for<br/><span class=\"{ACCENT}\">Cruise Passengers</span>",
        "Dickenson Bay, Hawksbill and excursion beaches — white sand, turquoise water and cruise-friendly beach days from St John's.",
        BEACHES_IMG, BEACHES_ALT, breadcrumb="Best Beaches",
    ),
    "hero-safety.html": hero_inner(
        "Cruise Passenger Safety", f"Is Antigua<br/><span class=\"{ACCENT}\">Safe</span>?",
        "Practical safety advice for cruise guests — St John's waterfront, organised excursions, water activities and travel tips in Antigua and Barbuda.",
        PORT_IMG, PORT_ALT, breadcrumb="Safety Guide",
    ),
    "hero-without-excursion.html": hero_inner(
        "Independent Exploring", f"Explore Antigua<br/><span class=\"{ACCENT}\">Without an Excursion</span>",
        "Heritage Quay shopping, St John's waterfront walks and taxi tips for nearby beaches without a tour booking.",
        PORT_IMG, PORT_ALT, breadcrumb="Without Excursion",
    ),
    "hero-nelsons-dockyard.html": hero_inner(
        "UNESCO Heritage", f"Nelson's Dockyard<br/><span class=\"{ACCENT}\">from Cruise Port</span>",
        "English Harbour's restored Georgian naval dockyard — distances from St John's, entry fees and shore excursion options.",
        NELSONS_DOCKYARD_IMG, NELSONS_DOCKYARD_ALT, breadcrumb="Nelson's Dockyard",
    ),
    "hero-shirley-heights.html": hero_inner(
        "Panoramic Views", f"Shirley Heights<br/><span class=\"{ACCENT}\">Antigua Guide</span>",
        "Historic military lookout over English Harbour — the best panoramic views on an Antigua cruise port day.",
        SHIRLEY_HEIGHTS_IMG, SHIRLEY_HEIGHTS_ALT, breadcrumb="Shirley Heights",
    ),
    "hero-the-antiguan-experience.html": hero_inner(
        "Island Culture", f"The Antiguan<br/><span class=\"{ACCENT}\">Experience</span>",
        "Scenic drive, private home visit, pineapple farm and white-sand beach — Antigua culture and relaxation combined.",
        ANTIGUAN_EXPERIENCE_IMG, ANTIGUAN_EXPERIENCE_ALT, breadcrumb="Antiguan Experience",
    ),
    "hero-classic-beach-day.html": hero_inner(
        "Beach · Caribbean", f"Classic<br/><span class=\"{ACCENT}\">Beach Day</span>",
        "Stress-free white sand, calm turquoise water, lunch and loungers timed for your St John's cruise schedule.",
        CLASSIC_BEACH_IMG, CLASSIC_BEACH_ALT, breadcrumb="Classic Beach Day",
    ),
    "hero-antigua-kayak-snorkel-and-beach.html": hero_inner(
        "Adventure Combo", f"Kayak, Snorkel<br/><span class=\"{ACCENT}\">&amp; Beach</span>",
        "Mangrove kayaking in Cades Bay, snorkelling Cades Reef and beach relaxation on Antigua's south-west coast.",
        KAYAK_SNORKEL_IMG, KAYAK_SNORKEL_ALT, breadcrumb="Kayak &amp; Snorkel",
    ),
    "hero-antigua-exclusive-history-and-culture-tour.html": hero_inner(
        "Small Group", f"History &amp;<br/><span class=\"{ACCENT}\">Culture Tour</span>",
        "Exclusive visit to Nelson's Dockyard, Dow's Hill and Shirley Heights — maximum 12 guests for personalised heritage touring.",
        HISTORY_CULTURE_IMG, HISTORY_CULTURE_ALT, breadcrumb="History &amp; Culture",
    ),
    "hero-panoramic-antigua-and-beach-break.html": hero_inner(
        "Scenic Drive", f"Panoramic Antigua<br/><span class=\"{ACCENT}\">&amp; Beach</span>",
        "Five hours of island viewpoints, coastal scenery and a relaxed beach break with refreshments included.",
        PANORAMIC_IMG, PANORAMIC_ALT, breadcrumb="Panoramic &amp; Beach",
    ),
    "hero-antigua-half-day-kayak-and-snorkel.html": hero_inner(
        "Half Day Adventure", f"Half Day Kayak<br/><span class=\"{ACCENT}\">&amp; Snorkel</span>",
        "Mangrove lagoon paddle, secluded beach and Cades Reef snorkelling — compact format for cruise schedules.",
        HALF_DAY_KAYAK_IMG, HALF_DAY_KAYAK_ALT, breadcrumb="Half Day Kayak",
    ),
}

PAGE_META = [
    dict(file="index.html", title=f"{SITE} | Beach, History &amp; Kayak Tours from St John's Antigua",
         description="Plan Antigua shore excursions for cruise passengers — beach days, Nelson's Dockyard, Shirley Heights, kayak snorkel adventures and island culture from St John's cruise port.",
         keywords="Antigua shore excursions, St John's cruise excursions, Nelson's Dockyard cruise tour, Antigua beach day, kayak snorkel Antigua",
         path="", data_page="home", hero="partials/hero-home.html", content="home.html", schema=home_schema(home_faq_data())),
    dict(file="best-antigua-shore-excursions.html", title="Best Antigua Shore Excursions | Compare St John's Cruise Tours",
         description="Compare the best Antigua shore excursions — beach days, Nelson's Dockyard history, kayak snorkel combos and scenic island drives with cruise timing from St John's.",
         keywords="best Antigua shore excursions, St John's cruise port tours, compare Antigua excursions, Antigua and Barbuda shore trips",
         path="best-antigua-shore-excursions.html", data_page="excursions", hero="partials/hero-excursions.html",
         content="best-antigua-shore-excursions.html", preload=BEST_IMG,
         schema={"@context": "https://schema.org", "@type": "WebPage", "name": "Best Antigua Shore Excursions", "url": f"{DOMAIN}/best-antigua-shore-excursions.html"}),
    dict(file="antigua-port-guide.html", title="Antigua Cruise Port Guide | St John's for Cruise Passengers",
         description="Antigua cruise port guide — St John's terminal, Heritage Quay, distances to beaches and Nelson's Dockyard, taxis, currency and shore excursion planning.",
         keywords="Antigua cruise port guide, St John's port day, cruise passenger guide Antigua, Nelson's Dockyard from cruise ship",
         path="antigua-port-guide.html", data_page="port", hero="partials/hero-port-guide.html",
         content="antigua-port-guide.html", preload=PORT_IMG,
         schema={"@context": "https://schema.org", "@type": "Article", "headline": "Antigua Cruise Port Guide", "url": f"{DOMAIN}/antigua-port-guide.html"}),
    dict(file="one-day-in-antigua-from-a-cruise-ship.html", title="One Day in Antigua from a Cruise Ship | Port Itinerary",
         description="How to spend one day in Antigua on a cruise stop — Nelson's Dockyard, beach time or kayak snorkel with return-to-ship buffer for St John's port calls.",
         keywords="one day in Antigua cruise, St John's port day itinerary, cruise stop Antigua planning",
         path="one-day-in-antigua-from-a-cruise-ship.html", data_page="port", hero="partials/hero-one-day.html",
         content="one-day-in-antigua-from-a-cruise-ship.html", preload=ONE_DAY_IMG,
         schema={"@context": "https://schema.org", "@type": "Article", "headline": "One Day in Antigua from a Cruise Ship", "url": f"{DOMAIN}/one-day-in-antigua-from-a-cruise-ship.html"}),
    dict(file="best-beaches-in-antigua-for-cruise-passengers.html", title="Best Beaches in Antigua for Cruise Passengers | St John's Guide",
         description="Best beaches in Antigua for cruise passengers — Dickenson Bay, Hawksbill, distances from St John's port and beach day excursion options.",
         keywords="best beaches Antigua cruise, Dickenson Bay cruise, St John's beach day cruise passengers",
         path="best-beaches-in-antigua-for-cruise-passengers.html", data_page="beaches", hero="partials/hero-beaches.html",
         content="best-beaches-in-antigua-for-cruise-passengers.html", preload=BEACHES_IMG,
         schema={"@context": "https://schema.org", "@type": "Article", "headline": "Best Beaches in Antigua for Cruise Passengers", "url": f"{DOMAIN}/best-beaches-in-antigua-for-cruise-passengers.html"}),
    dict(file="nelsons-dockyard-from-antigua-cruise-port.html", title="Nelson's Dockyard from Antigua Cruise Port | English Harbour Guide",
         description="Nelson's Dockyard guide for St John's cruise passengers — English Harbour UNESCO site, distances from port, entry fees and history shore excursion tips.",
         keywords="Nelson's Dockyard Antigua cruise, English Harbour shore excursion, Nelson's Dockyard from St John's",
         path="nelsons-dockyard-from-antigua-cruise-port.html", data_page="history", hero="partials/hero-nelsons-dockyard.html",
         content="nelsons-dockyard-from-antigua-cruise-port.html", preload=NELSONS_DOCKYARD_IMG,
         schema={"@context": "https://schema.org", "@type": "Article", "headline": "Nelson's Dockyard from Antigua Cruise Port", "url": f"{DOMAIN}/nelsons-dockyard-from-antigua-cruise-port.html"}),
    dict(file="shirley-heights-antigua-guide.html", title="Shirley Heights Antigua Guide | Lookout for Cruise Passengers",
         description="Shirley Heights guide for Antigua cruise passengers — panoramic English Harbour views, distances from St John's and tours including the historic lookout.",
         keywords="Shirley Heights Antigua cruise, English Harbour viewpoint, Shirley Heights shore excursion",
         path="shirley-heights-antigua-guide.html", data_page="history", hero="partials/hero-shirley-heights.html",
         content="shirley-heights-antigua-guide.html", preload=SHIRLEY_HEIGHTS_IMG,
         schema={"@context": "https://schema.org", "@type": "Article", "headline": "Shirley Heights Antigua Guide", "url": f"{DOMAIN}/shirley-heights-antigua-guide.html"}),
    dict(file="is-antigua-safe-for-cruise-passengers.html", title="Is Antigua Safe for Cruise Passengers? | Port Safety Guide",
         description="Is Antigua safe for cruise passengers? Practical safety tips for St John's waterfront, organised excursions to beaches and Nelson's Dockyard in Antigua and Barbuda.",
         keywords="is Antigua safe cruise, Antigua safety cruise passengers, safe Antigua shore excursions",
         path="is-antigua-safe-for-cruise-passengers.html", data_page="port", hero="partials/hero-safety.html",
         content="is-antigua-safe-for-cruise-passengers.html", preload=PORT_IMG,
         schema={"@context": "https://schema.org", "@type": "Article", "headline": "Is Antigua Safe for Cruise Passengers?", "url": f"{DOMAIN}/is-antigua-safe-for-cruise-passengers.html"}),
    dict(file="can-you-explore-antigua-without-an-excursion.html", title="Can You Explore Antigua Without an Excursion? | Cruise Guide",
         description="Explore Antigua without a booked excursion — St John's waterfront, Heritage Quay shopping and tips for reaching beaches independently from the cruise terminal.",
         keywords="Antigua without excursion, explore St John's cruise ship, self guided Antigua port day",
         path="can-you-explore-antigua-without-an-excursion.html", data_page="port", hero="partials/hero-without-excursion.html",
         content="can-you-explore-antigua-without-an-excursion.html", preload=PORT_IMG,
         schema={"@context": "https://schema.org", "@type": "Article", "headline": "Can You Explore Antigua Without an Excursion?", "url": f"{DOMAIN}/can-you-explore-antigua-without-an-excursion.html"}),
    dict(file="the-antiguan-experience.html", title="The Antiguan Experience | St John's Cruise Shore Excursion",
         description="The Antiguan Experience shore excursion for cruise passengers — scenic drive, pineapple farm, private home visit and white-sand beach with lunch from St John's port.",
         keywords="Antiguan Experience tour, Antigua culture cruise excursion, pineapple farm Antigua shore trip",
         path="the-antiguan-experience.html", data_page="tours", hero="partials/hero-the-antiguan-experience.html",
         content="the-antiguan-experience.html", preload=ANTIGUAN_EXPERIENCE_IMG,
         schema=tourist_trip_schema("The Antiguan Experience", "Culture, pineapple farm and beach shore excursion from St John's Antigua cruise port.")),
    dict(file="classic-beach-day.html", title="Classic Beach Day | Antigua Cruise Shore Excursion",
         description="Classic Beach Day shore excursion for Antigua cruise passengers — white sand, turquoise water, loungers and lunch with cruise-timed returns from St John's.",
         keywords="Classic Beach Day Antigua, Antigua beach excursion cruise, white sand beach St John's",
         path="classic-beach-day.html", data_page="beaches", hero="partials/hero-classic-beach-day.html",
         content="classic-beach-day.html", preload=CLASSIC_BEACH_IMG,
         schema=tourist_trip_schema("Classic Beach Day", "White sand beach day shore excursion from St John's Antigua cruise port.")),
    dict(file="antigua-kayak-snorkel-and-beach.html", title="Antigua Kayak Snorkel and Beach | St John's Cruise Excursion",
         description="Antigua Kayak Snorkel and Beach tour for cruise passengers — Cades Bay mangroves, Cades Reef snorkelling and beach time with lunch from St John's port.",
         keywords="Antigua kayak snorkel cruise, Cades Reef excursion, mangrove kayak Antigua shore trip",
         path="antigua-kayak-snorkel-and-beach.html", data_page="kayak", hero="partials/hero-antigua-kayak-snorkel-and-beach.html",
         content="antigua-kayak-snorkel-and-beach.html", preload=KAYAK_SNORKEL_IMG,
         schema=tourist_trip_schema("Antigua Kayak Snorkel and Beach", "Kayak, snorkel and beach combo from St John's Antigua cruise port.")),
    dict(file="antigua-exclusive-history-and-culture-tour.html", title="Antigua Exclusive History and Culture Tour | Cruise Excursion",
         description="Exclusive History and Culture tour for Antigua cruise passengers — Nelson's Dockyard, Dow's Hill and Shirley Heights small-group tour from St John's.",
         keywords="Antigua history tour cruise, Nelson's Dockyard shore excursion, Shirley Heights culture tour",
         path="antigua-exclusive-history-and-culture-tour.html", data_page="history", hero="partials/hero-antigua-exclusive-history-and-culture-tour.html",
         content="antigua-exclusive-history-and-culture-tour.html", preload=HISTORY_CULTURE_IMG,
         schema=tourist_trip_schema("Antigua Exclusive History and Culture Tour", "Nelson's Dockyard and Shirley Heights small-group shore excursion from St John's.")),
    dict(file="panoramic-antigua-and-beach-break.html", title="Panoramic Antigua and Beach Break | St John's Cruise Tour",
         description="Panoramic Antigua and Beach Break for cruise passengers — scenic island drive, viewpoints and beach relaxation with beverages from St John's port.",
         keywords="panoramic Antigua tour cruise, scenic Antigua shore excursion, beach break St John's",
         path="panoramic-antigua-and-beach-break.html", data_page="tours", hero="partials/hero-panoramic-antigua-and-beach-break.html",
         content="panoramic-antigua-and-beach-break.html", preload=PANORAMIC_IMG,
         schema=tourist_trip_schema("Panoramic Antigua and Beach Break", "Scenic drive and beach break shore excursion from St John's Antigua.")),
    dict(file="antigua-half-day-kayak-and-snorkel.html", title="Antigua Half Day Kayak and Snorkel | Cruise Shore Excursion",
         description="Half Day Kayak and Snorkel for Antigua cruise passengers — mangrove lagoon paddle, Cades Reef snorkelling and snacks from St John's cruise port.",
         keywords="half day kayak Antigua cruise, Cades Reef snorkel excursion, mangrove kayak St John's",
         path="antigua-half-day-kayak-and-snorkel.html", data_page="kayak", hero="partials/hero-antigua-half-day-kayak-and-snorkel.html",
         content="antigua-half-day-kayak-and-snorkel.html", preload=HALF_DAY_KAYAK_IMG,
         schema=tourist_trip_schema("Antigua Half Day Kayak and Snorkel", "Mangrove kayak and Cades Reef snorkel from St John's Antigua cruise port.")),
]


def nav_html() -> str:
    return f"""<nav class="fixed top-0 left-0 right-0 z-50 bg-white/90 border-b border-pr-100 shadow-sm">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-12">
      <a href="index.html" class="flex items-center gap-2">
        <div class="w-7 h-7 rounded-full btn-ocean flex items-center justify-center">
          <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z"/>
          </svg>
        </div>
        <span class="font-display font-semibold text-ocean-800 text-base leading-tight">Antigua Shore<br/><span class="text-[10px] font-body font-normal text-pr-600 tracking-widest uppercase">Excursion</span></span>
      </a>
      <div class="hidden lg:flex items-center gap-5 text-sm font-medium">
        <a href="index.html" data-nav="home" class="text-gray-600 hover:text-ocean-600 transition-colors">Home</a>
        <a href="best-antigua-shore-excursions.html" data-nav="excursions" class="text-gray-600 hover:text-ocean-600 transition-colors">Excursions</a>
        <a href="nelsons-dockyard-from-antigua-cruise-port.html" data-nav="history" class="text-gray-600 hover:text-ocean-600 transition-colors">History</a>
        <a href="best-beaches-in-antigua-for-cruise-passengers.html" data-nav="beaches" class="text-gray-600 hover:text-ocean-600 transition-colors">Beaches</a>
        <a href="antigua-kayak-snorkel-and-beach.html" data-nav="kayak" class="text-gray-600 hover:text-ocean-600 transition-colors">Kayak</a>
        <a href="antigua-port-guide.html" data-nav="port" class="text-gray-600 hover:text-ocean-600 transition-colors">Port Guide</a>
      </div>
      <a href="best-antigua-shore-excursions.html" class="hidden md:inline-flex items-center gap-2 btn-ocean text-white text-sm font-semibold px-4 py-2 rounded-full shadow-md">
        Compare Tours
      </a>
      <button type="button" class="lg:hidden p-2 rounded-lg text-gray-600 hover:bg-sand-50" aria-label="Open menu">
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
    </div>
  </div>
</nav>
"""


def footer_html() -> str:
    return f"""  <footer class="bg-gray-900 text-gray-400 py-14">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
        <div class="sm:col-span-2 lg:col-span-1">
          <a href="index.html" class="font-display font-semibold text-white text-lg">{SITE}</a>
          <p class="mt-3 text-sm leading-relaxed">Planning guide for cruise visitors to St John's, Antigua and Barbuda. Not affiliated with any cruise line.</p>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Excursions</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="the-antiguan-experience.html" class="hover:text-white transition-colors">The Antiguan Experience</a></li>
            <li><a href="classic-beach-day.html" class="hover:text-white transition-colors">Classic Beach Day</a></li>
            <li><a href="antigua-kayak-snorkel-and-beach.html" class="hover:text-white transition-colors">Kayak, Snorkel &amp; Beach</a></li>
            <li><a href="antigua-exclusive-history-and-culture-tour.html" class="hover:text-white transition-colors">History &amp; Culture Tour</a></li>
            <li><a href="panoramic-antigua-and-beach-break.html" class="hover:text-white transition-colors">Panoramic &amp; Beach Break</a></li>
            <li><a href="antigua-half-day-kayak-and-snorkel.html" class="hover:text-white transition-colors">Half Day Kayak &amp; Snorkel</a></li>
          </ul>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Guides</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="best-antigua-shore-excursions.html" class="hover:text-white transition-colors">Best Excursions</a></li>
            <li><a href="antigua-port-guide.html" class="hover:text-white transition-colors">Port Guide</a></li>
            <li><a href="one-day-in-antigua-from-a-cruise-ship.html" class="hover:text-white transition-colors">One Day in Antigua</a></li>
            <li><a href="nelsons-dockyard-from-antigua-cruise-port.html" class="hover:text-white transition-colors">Nelson's Dockyard</a></li>
            <li><a href="shirley-heights-antigua-guide.html" class="hover:text-white transition-colors">Shirley Heights</a></li>
            <li><a href="best-beaches-in-antigua-for-cruise-passengers.html" class="hover:text-white transition-colors">Best Beaches</a></li>
            <li><a href="is-antigua-safe-for-cruise-passengers.html" class="hover:text-white transition-colors">Safety Guide</a></li>
            <li><a href="can-you-explore-antigua-without-an-excursion.html" class="hover:text-white transition-colors">Without an Excursion</a></li>
          </ul>
        </div>
      </div>
      <div class="border-t border-gray-800 pt-8 text-xs text-center sm:text-left">
        <p>&copy; 2026 {SITE}. Verify times and prices with operators before booking.</p>
      </div>
    </div>
  </footer>
"""


def trust_strip_html() -> str:
    return """<section class="trust-strip" aria-label="Antigua shore excursion highlights">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <ul class="trust-strip__list">
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Nelson's Dockyard</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Beach Days</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Kayak &amp; Snorkel</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Cruise-Friendly Returns</li>
    </ul>
  </div>
</section>
"""


def main() -> None:
    print("Building Antigua Shore Excursion site…")

    write("partials/nav.html", nav_html())
    write("partials/footer.html", footer_html())
    write("partials/trust-strip.html", trust_strip_html())

    for name, html in HERO_DEFS.items():
        write(f"partials/{name}", html)

    for name, html in all_guide_content().items():
        write(f"content/{name}", html)

    for name, html in all_tour_content().items():
        write(f"content/{name}", html)

    for p in PAGE_META:
        write(
            p["file"],
            page_shell(
                title=p["title"],
                description=p["description"],
                keywords=p["keywords"],
                canonical_path=p["path"],
                data_page=p["data_page"],
                hero=p["hero"],
                content=p["content"],
                preload=p.get("preload", HOME_HERO),
                schema=p.get("schema"),
            ),
        )

    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")

    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, priority, freq in SITEMAP_PAGES:
        url = f"{DOMAIN}/{loc}" if loc else f"{DOMAIN}/"
        lines += [
            "  <url>",
            f"    <loc>{url}</loc>",
            f"    <lastmod>{DATE}</lastmod>",
            f"    <changefreq>{freq}</changefreq>",
            f"    <priority>{priority}</priority>",
            "  </url>",
        ]
    lines.append("</urlset>")
    write("sitemap.xml", "\n".join(lines) + "\n")

    write("package.json", """{
  "name": "antigua-shore-excursion",
  "private": true,
  "scripts": {
    "build": "python3 scripts/build-antigua-site.py",
    "images": "python3 scripts/fetch-antigua-images.py",
    "deploy": "wrangler deploy",
    "preview": "python3 -m http.server 8907"
  },
  "devDependencies": {
    "wrangler": "^4.94.0"
  }
}
""")

    write("wrangler.jsonc", """{
  "$schema": "node_modules/wrangler/config-schema.json",
  "name": "antigua-shore-excursion",
  "compatibility_date": "2026-06-06",
  "observability": { "enabled": true },
  "assets": { "directory": "." },
  "routes": [
    {
      "pattern": "antiguashoreexcursion.com",
      "custom_domain": true
    }
  ]
}
""")

    write("deploy.sh", f"""#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

if [[ ! -f node_modules/.bin/wrangler ]]; then
  npm install
fi

echo "Deploying {SITE} to Cloudflare..."
npx wrangler deploy

echo "Done. Check {DOMAIN}/ shortly."
""")

    (ROOT / "deploy.sh").chmod(0o755)

    images_dir = ROOT / "images"
    images_dir.mkdir(exist_ok=True)
    for img in ALL_IMAGES:
        p = ROOT / img
        if p.exists() and p.stat().st_size > 5000:
            continue
        p.write_bytes(PLACEHOLDER_PNG)

    write("images/ATTRIBUTION.md", """# Image attribution

Hero and content images are sourced from [Wikimedia Commons](https://commons.wikimedia.org) under Creative Commons licences where applicable.

Run `npm run images` to download location-accurate photos. Replace any image with your own assets — keep filenames consistent with `scripts/antigua_config.py`.
""")

    write("README.md", """# Antigua Shore Excursion

Cruise-passenger planning guide for St John's, Antigua and Barbuda shore excursions.

## Development

```bash
npm install
npm run build
npm run images
npm run preview
```

Open http://localhost:8907 (requires local server for partial loading).

## Deploy to Cloudflare Pages

```bash
npm run build && npm run images && ./deploy.sh
```

Domain: https://antiguashoreexcursion.com
""")

    print("Done.")


if __name__ == "__main__":
    main()
