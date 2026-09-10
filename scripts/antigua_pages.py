"""Antigua Shore Excursion — Phase 15B page content modules.

Each public page function returns:
  (hero_html, main_html, faq_list_or_None, meta)

meta keys: title, description, canonical_path, page_id, og_image
faq_list: list[tuple[str, str]] | None
"""
from __future__ import annotations

from antigua_config import (
    ACCENT,
    BEACHES,
    BEACHES_ALT,
    CLASSIC_BEACH_HERO,
    CLASSIC_BEACH_HERO_ALT,
    CRUISE_PORT,
    CRUISE_PORT_ALT,
    EMAIL,
    EXPERIENCE,
    EXPERIENCE_ALT,
    EXCURSIONS_HERO,
    EXCURSIONS_HERO_ALT,
    HERO_HOME,
    HERO_HOME_ALT,
    HISTORY,
    HISTORY_ALT,
    INTRO,
    INTRO_ALT,
    NELSONS,
    NELSONS_ALT,
    ONE_DAY_HERO,
    ONE_DAY_HERO_ALT,
    PORT_ARRIVAL,
    PORT_ARRIVAL_ALT,
    SHIRLEY,
    SHIRLEY_ALT,
    SITE,
)
from typing import Any, Optional

from antigua_shell import (
    cruise_snapshot,
    faq_section,
    hero_band,
    related_links,
)

Meta = dict  # title/description/canonical_path/page_id/og_image
FaqList = list
PageTuple = tuple


def _cta(primary_href: str, primary_label: str, secondary_href: str = "", secondary_label: str = "") -> str:
    parts = [
        f'<a href="{primary_href}" class="btn-primary inline-flex items-center justify-center gap-2 '
        f'text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">{primary_label}</a>'
    ]
    if secondary_href:
        parts.append(
            f'<a href="{secondary_href}" class="btn-outline inline-flex items-center justify-center gap-2 '
            f'text-white font-semibold px-7 py-3 rounded-full text-sm">{secondary_label}</a>'
        )
    return "".join(parts)


def _section(inner: str, *, bg: str = "bg-white", pad: str = "pt-8 pb-12") -> str:
    return f'<section class="{pad} {bg}"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">{inner}</div></section>\n'


def _prose(inner: str, *, bg: str = "bg-white", narrow: bool = True) -> str:
    wrap = "max-w-3xl" if narrow else "max-w-7xl"
    return (
        f'<section class="py-14 {bg}"><div class="{wrap} mx-auto px-4 sm:px-6 lg:px-8">'
        f"{inner}</div></section>\n"
    )


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------


def home() -> PageTuple:
    hero = hero_band(
        eyebrow="Antigua · St John's cruise port",
        title_html=(
            f'Antigua Shore<br/><span class="{ACCENT}">Excursions</span><br/>'
            "for Cruise Passengers"
        ),
        lead=(
            "A practical guide to what fits a St John's call: near-port beaches, "
            "south-coast history at Nelson's Dockyard, kayak and reef days, "
            "or a walkable DIY plan around Heritage Quay and Redcliffe Quay."
        ),
        image=HERO_HOME,
        aria_label=HERO_HOME_ALT,
        actions=_cta(
            "/best-antigua-shore-excursions/",
            "Compare day styles",
            "/antigua-port-guide/",
            "Read the port guide",
        ),
        tags=["Dickenson Bay", "Nelson's Dockyard", "Shirley Heights", "DIY St John's"],
    )

    snap = cruise_snapshot(
        [
            ("Typical time ashore", "Often around 6–10 hours — confirm your ship"),
            ("Near-port strengths", "St John's waterfront; Dickenson Bay ~10–15 min"),
            ("South-coast history", "Nelson's Dockyard / English Harbour ~30–45 min"),
            ("Planning focus", "One coherent theme beats over-stacking"),
            ("Return window", "Build a conservative buffer before all aboard"),
            ("This site", "Editorial planning — no booking checkout here"),
        ],
        label="Antigua cruise passenger snapshot",
    )

    main = f"""
{_section(f'''
<div class="grid lg:grid-cols-2 gap-12 lg:gap-20 items-center">
  <div>
    <div class="section-label">Antigua cruise port</div>
    <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 leading-snug mb-5">
      What Antigua is<br/><span class="text-ocean-600">actually good for</span>
    </h2>
    <p class="text-gray-600 leading-relaxed mb-5">
      Cruise ships call at <strong>St John's</strong>, with terminals around
      <strong>Heritage Quay</strong> and <strong>Redcliffe Quay</strong>.
      Near-port time suits waterfront walking, shopping and a short taxi to Dickenson Bay
      (roughly 10–15 minutes north-west). Nelson's Dockyard and Shirley Heights sit toward
      English Harbour — often around 30–45 minutes south by road — so history days need an
      earlier departure and a protected return window.
    </p>
    <p class="text-gray-600 leading-relaxed mb-8">
      Eastern Caribbean dollars are official; USD is widely accepted at tourist businesses.
      Use this site to choose a style for the day, then confirm live ship times and any
      operator details independently — we do not publish fees, product codes or booking checkouts.
    </p>
    <a href="/best-antigua-shore-excursions/" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm shadow-lg">
      Explore decision groups
    </a>
  </div>
  <div class="info-image rounded-3xl aspect-[4/3] shadow-2xl overflow-hidden">
    <img src="{INTRO}" alt="{INTRO_ALT}" width="800" height="600" loading="eager" decoding="async" />
  </div>
</div>
''')}
{_section(f'''
<div class="text-center mb-12">
  <div class="section-label justify-center">Decision spine</div>
  <h2 class="text-3xl font-display font-bold text-gray-900">Five useful starting points</h2>
  <p class="mt-4 text-gray-500 max-w-2xl mx-auto">Pick the page that matches your question — not a ranking of “bestsellers”.</p>
</div>
<div class="grid sm:grid-cols-2 lg:grid-cols-5 gap-6">
  <a href="/best-beaches-in-antigua-for-cruise-passengers/" class="card-hover bg-white rounded-2xl overflow-hidden border border-gray-100 shadow-sm group block flex flex-col">
    <div class="card-media h-36"><img src="{BEACHES}" alt="{BEACHES_ALT}" width="600" height="288" loading="lazy" decoding="async" /></div>
    <div class="p-5 flex flex-col flex-1">
      <h3 class="text-lg font-display font-semibold text-gray-900 group-hover:text-ocean-600 transition-colors">Beach</h3>
      <p class="text-sm text-gray-500 mt-2 leading-relaxed flex-1">Near-port swimming and quieter cove days when water time is the priority.</p>
      <span class="inline-flex mt-4 text-ocean-600 text-sm font-semibold">Beach guide →</span>
    </div>
  </a>
  <a href="/antigua-exclusive-history-and-culture-tour/" class="card-hover bg-white rounded-2xl overflow-hidden border border-gray-100 shadow-sm group block flex flex-col">
    <div class="card-media h-36"><img src="{HISTORY}" alt="{HISTORY_ALT}" width="600" height="288" loading="lazy" decoding="async" /></div>
    <div class="p-5 flex flex-col flex-1">
      <h3 class="text-lg font-display font-semibold text-gray-900 group-hover:text-ocean-600 transition-colors">History &amp; culture</h3>
      <p class="text-sm text-gray-500 mt-2 leading-relaxed flex-1">Nelson's Dockyard and Shirley Heights — south-coast heritage with honest transfer time.</p>
      <span class="inline-flex mt-4 text-ocean-600 text-sm font-semibold">History guide →</span>
    </div>
  </a>
  <a href="/antigua-kayak-snorkel-and-beach/" class="card-hover bg-white rounded-2xl overflow-hidden border border-gray-100 shadow-sm group block flex flex-col">
    <div class="card-media h-36 bg-ocean-800 flex items-center justify-center text-white/80 text-sm px-4 text-center">Kayak &amp; reef day</div>
    <div class="p-5 flex flex-col flex-1">
      <h3 class="text-lg font-display font-semibold text-gray-900 group-hover:text-ocean-600 transition-colors">Kayak / adventure</h3>
      <p class="text-sm text-gray-500 mt-2 leading-relaxed flex-1">Mangrove paddling and reef snorkelling styles — active days that still need a buffer.</p>
      <span class="inline-flex mt-4 text-ocean-600 text-sm font-semibold">Kayak guide →</span>
    </div>
  </a>
  <a href="/can-you-explore-antigua-without-an-excursion/" class="card-hover bg-white rounded-2xl overflow-hidden border border-gray-100 shadow-sm group block flex flex-col">
    <div class="card-media h-36"><img src="{CRUISE_PORT}" alt="{CRUISE_PORT_ALT}" width="600" height="288" loading="lazy" decoding="async" /></div>
    <div class="p-5 flex flex-col flex-1">
      <h3 class="text-lg font-display font-semibold text-gray-900 group-hover:text-ocean-600 transition-colors">DIY / St John's</h3>
      <p class="text-sm text-gray-500 mt-2 leading-relaxed flex-1">Walk the quays, taxi to a nearby beach, and know when organised transport helps.</p>
      <span class="inline-flex mt-4 text-ocean-600 text-sm font-semibold">DIY guide →</span>
    </div>
  </a>
  <a href="/one-day-in-antigua-from-a-cruise-ship/" class="card-hover bg-white rounded-2xl overflow-hidden border border-gray-100 shadow-sm group block flex flex-col sm:col-span-2 lg:col-span-1">
    <div class="card-media h-36"><img src="{ONE_DAY_HERO}" alt="{ONE_DAY_HERO_ALT}" width="600" height="288" loading="lazy" decoding="async" /></div>
    <div class="p-5 flex flex-col flex-1">
      <h3 class="text-lg font-display font-semibold text-gray-900 group-hover:text-ocean-600 transition-colors">One-day planning</h3>
      <p class="text-sm text-gray-500 mt-2 leading-relaxed flex-1">Realistic port-day shapes matched to call length — without optimistic stacking.</p>
      <span class="inline-flex mt-4 text-ocean-600 text-sm font-semibold">One-day guide →</span>
    </div>
  </a>
</div>
''', bg="bg-pr-50", pad="py-16")}
{_section(snap + related_links([
    ("/antigua-port-guide/", "Port guide"),
    ("/one-day-in-antigua-from-a-cruise-ship/", "One day ashore"),
    ("/best-antigua-shore-excursions/", "Excursion styles"),
    ("/contact/", "Contact"),
]), pad="pb-16 pt-4")}
{faq_section([
    (
        "Where do cruise ships call in Antigua?",
        "Most calls are at St John's harbour, with terminals associated with Heritage Quay and "
        "Redcliffe Quay. Confirm your ship's berth notes for your sailing.",
    ),
    (
        "How long do ships usually stay?",
        "Typical Antigua calls often run around 6–10 hours ashore. Always confirm gangway and "
        "all-aboard times on your sailing — schedules vary.",
    ),
    (
        "How far is Nelson's Dockyard from the port?",
        "English Harbour / Nelson's Dockyard is roughly 30–45 minutes south by road from St John's, "
        "depending on traffic and stops. Treat that as approximate planning guidance.",
    ),
    (
        "Can I explore without a booked excursion?",
        "Yes for St John's waterfront and nearby beaches by taxi. Farther sites such as Nelson's "
        "Dockyard and south-west reef areas usually need organised transport and careful timing.",
    ),
], heading="Antigua shore day FAQ")}
"""

    faqs: FaqList = [
        (
            "Where do cruise ships call in Antigua?",
            "Most calls are at St John's harbour, with terminals associated with Heritage Quay and "
            "Redcliffe Quay. Confirm your ship's berth notes for your sailing.",
        ),
        (
            "How long do ships usually stay?",
            "Typical Antigua calls often run around 6–10 hours ashore. Always confirm gangway and "
            "all-aboard times on your sailing — schedules vary.",
        ),
        (
            "How far is Nelson's Dockyard from the port?",
            "English Harbour / Nelson's Dockyard is roughly 30–45 minutes south by road from St John's, "
            "depending on traffic and stops. Treat that as approximate planning guidance.",
        ),
        (
            "Can I explore without a booked excursion?",
            "Yes for St John's waterfront and nearby beaches by taxi. Farther sites such as Nelson's "
            "Dockyard and south-west reef areas usually need organised transport and careful timing.",
        ),
    ]

    meta: Meta = {
        "title": "Antigua Shore Excursion | Cruise Passenger Planning Guide",
        "description": (
            "Plan Antigua shore excursions from St John's — beaches, Nelson's Dockyard, "
            "kayak days, DIY waterfront options and realistic one-day cruise planning."
        ),
        "canonical_path": "/",
        "page_id": "home",
        "og_image": HERO_HOME,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# BEST EXCURSIONS (hub)
# ---------------------------------------------------------------------------


def best_excursions() -> PageTuple:
    hero = hero_band(
        eyebrow="Decision hub",
        title_html=f'Compare Antigua<br/><span class="{ACCENT}">shore day styles</span>',
        lead=(
            "Beach, history and culture, kayak and adventure, scenic island drives, "
            "and independent St John's time — grouped by how they fit a cruise call, "
            "not by invented popularity rankings."
        ),
        image=EXCURSIONS_HERO,
        aria_label=EXCURSIONS_HERO_ALT,
        breadcrumb="Excursions",
        actions=_cta(
            "/antigua-port-guide/",
            "Port logistics first",
            "/one-day-in-antigua-from-a-cruise-ship/",
            "One-day scenarios",
        ),
    )

    snap = cruise_snapshot(
        [
            ("How to use this page", "Choose a style, then open the matching guide"),
            ("Near-port", "St John's quays; Dickenson Bay ~10–15 min"),
            ("South coast", "Nelson's Dockyard & Shirley Heights ~30–45 min"),
            ("Active days", "Kayak / snorkel styles — confirm duration live"),
            ("Commerce", "No prices, product codes or checkout on this site"),
        ]
    )

    main = f"""
{_prose('''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Antigua shore days split cleanly once you decide how far you are willing to travel from St John's.
  Stay close for waterfront time and nearby beaches; commit the day if you want English Harbour history
  or a south-west kayak and reef itinerary. Mixing every highlight on a short call usually produces
  rushed photography and a tense return window.
</p>
''' + snap)}
{_section('''
<div class="mb-10">
  <div class="section-label">Beach</div>
  <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-3">Near-port water time</h2>
  <p class="text-gray-600 leading-relaxed max-w-3xl mb-6">
    Beach days suit shorter calls, mixed groups and anyone who wants swimming ahead of inland roads.
    Dickenson Bay is the nearest widely known option north-west of the harbour; quieter coves appear
    on organised beach-style days. Read the beach guide before stacking shopping stops.
  </p>
  <p class="space-x-4">
    <a href="/best-beaches-in-antigua-for-cruise-passengers/" class="text-ocean-600 font-semibold">Beach guide →</a>
    <a href="/classic-beach-day/" class="text-ocean-600 font-semibold">Classic beach day (editorial) →</a>
  </p>
</div>
<div class="mb-10">
  <div class="section-label">History &amp; culture</div>
  <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-3">English Harbour without pretending it is next door</h2>
  <p class="text-gray-600 leading-relaxed max-w-3xl mb-6">
    Nelson's Dockyard and Shirley Heights sit in Antigua's south-coast heritage corridor.
    Road time from St John's is often around 30–45 minutes each way — confirm live — so treat this
    as a committed theme, not a quick add-on after a long beach lunch.
  </p>
  <p class="space-x-4">
    <a href="/antigua-exclusive-history-and-culture-tour/" class="text-ocean-600 font-semibold">History &amp; culture →</a>
    <a href="/nelsons-dockyard-from-antigua-cruise-port/" class="text-ocean-600 font-semibold">Nelson's Dockyard →</a>
    <a href="/shirley-heights-antigua-guide/" class="text-ocean-600 font-semibold">Shirley Heights →</a>
  </p>
</div>
<div class="mb-10">
  <div class="section-label">Kayak / adventure</div>
  <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-3">Mangroves, reef time and beach finishes</h2>
  <p class="text-gray-600 leading-relaxed max-w-3xl mb-6">
    Kayak and snorkel days usually involve transfers toward the south-west coast and water segments
    that need fitness, sun protection and honest timing. Compare the fuller kayak-and-beach framing
    with the shorter half-day style — both remain editorial guides on this site.
  </p>
  <p class="space-x-4">
    <a href="/antigua-kayak-snorkel-and-beach/" class="text-ocean-600 font-semibold">Kayak, snorkel &amp; beach →</a>
    <a href="/antigua-half-day-kayak-and-snorkel/" class="text-ocean-600 font-semibold">Half-day kayak →</a>
  </p>
</div>
<div class="mb-10">
  <div class="section-label">Scenic / island overview</div>
  <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-3">Viewpoints plus a beach break</h2>
  <p class="text-gray-600 leading-relaxed max-w-3xl mb-6">
    Panoramic island drives trade depth at one site for several lookouts and a swim stop.
    Useful when your group wants photographs and lighter activity — less useful if everyone
    wants a long unsupervised beach afternoon.
  </p>
  <p class="space-x-4">
    <a href="/panoramic-antigua-and-beach-break/" class="text-ocean-600 font-semibold">Panoramic &amp; beach →</a>
    <a href="/the-antiguan-experience/" class="text-ocean-600 font-semibold">Island experience →</a>
  </p>
</div>
<div class="mb-4">
  <div class="section-label">Independent / DIY</div>
  <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-3">When you skip a package</h2>
  <p class="text-gray-600 leading-relaxed max-w-3xl mb-6">
    St John's is unusually walkable for a Caribbean cruise capital. Heritage Quay, Redcliffe Quay
    and a short taxi beach hop can fill a few hours well. Farther heritage and reef sites still
    need transport plans and a conservative return buffer.
  </p>
  <p><a href="/can-you-explore-antigua-without-an-excursion/" class="text-ocean-600 font-semibold">Explore without an excursion →</a></p>
</div>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
<p class="text-gray-600 leading-relaxed mb-4">
  These pages are planning guides. Booking is not offered on this website yet — if you arrange
  anything independently, confirm inclusions, pickup logistics and timing with the operator and
  your cruise line before you travel.
</p>
''' + related_links([
    ("/one-day-in-antigua-from-a-cruise-ship/", "One day scenarios"),
    ("/antigua-port-guide/", "Port guide"),
    ("/is-antigua-safe-for-cruise-passengers/", "Safety notes"),
    ("/contact/", "Contact"),
]), bg="bg-white")}
{faq_section([
    (
        "How should I choose between beach and history?",
        "Choose beach for shorter calls and lower transfer risk. Choose Nelson's Dockyard / Shirley Heights "
        "when you accept south-coast road time and still leave a conservative return window.",
    ),
    (
        "Do you sell tours here?",
        "No. This is an independent planning guide. Use /contact/ for editorial questions only.",
    ),
    (
        "Is there one best Antigua excursion?",
        "No single product fits every ship schedule. Match beach, heritage, kayak or DIY to your call length "
        "and group energy, then stop adding stops.",
    ),
], heading="Comparing Antigua day styles")}
"""

    faqs: FaqList = [
        (
            "How should I choose between beach and history?",
            "Choose beach for shorter calls and lower transfer risk. Choose Nelson's Dockyard / Shirley Heights "
            "when you accept south-coast road time and still leave a conservative return window.",
        ),
        (
            "Do you sell tours here?",
            "No. This is an independent planning guide. Use /contact/ for editorial questions only.",
        ),
        (
            "Is there one best Antigua excursion?",
            "No single product fits every ship schedule. Match beach, heritage, kayak or DIY to your call length "
            "and group energy, then stop adding stops.",
        ),
    ]

    meta: Meta = {
        "title": "Best Antigua Shore Excursions | Compare Cruise Day Styles",
        "description": (
            "Compare Antigua cruise excursion styles from St John's — beach, history and culture, "
            "kayak adventures, scenic drives and independent DIY options."
        ),
        "canonical_path": "/best-antigua-shore-excursions/",
        "page_id": "excursions",
        "og_image": EXCURSIONS_HERO,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# PORT GUIDE
# ---------------------------------------------------------------------------


def port_guide() -> PageTuple:
    hero = hero_band(
        eyebrow="Port logistics",
        title_html=f'Antigua<br/><span class="{ACCENT}">cruise port guide</span>',
        lead=(
            "What cruise passengers should know about St John's harbour, "
            "Heritage Quay and Redcliffe Quay, near-port choices and how far "
            "popular sights really sit from the pier."
        ),
        image=CRUISE_PORT,
        aria_label=CRUISE_PORT_ALT,
        breadcrumb="Port guide",
        actions=_cta(
            "/best-antigua-shore-excursions/",
            "Compare day styles",
            "/one-day-in-antigua-from-a-cruise-ship/",
            "One day ashore",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Port area", "St John's — Heritage Quay & Redcliffe Quay"),
            ("Typical call", "Often ~6–10 hours — confirm your ship"),
            ("Near-port", "Waterfront walk; Dickenson Bay ~10–15 min"),
            ("South coast", "Nelson's Dockyard ~30–45 min by road"),
            ("Currency", "XCD official; USD widely accepted at tourist businesses"),
            ("Return planning", "Leave buffer; traffic and queues vary"),
        ]
    )

    main = f"""
{_prose('''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Antigua's main cruise gateway is <strong>St John's</strong> on the north-west coast.
  Passengers usually organise the day around the harbour terminals at
  <strong>Heritage Quay</strong> and <strong>Redcliffe Quay</strong>, then choose between
  staying local or committing road time toward English Harbour or the south-west coast.
  Exact berth and gangway instructions belong to your cruise line for that sailing.
</p>
''' + snap)}
{_section(f'''
<div class="info-image rounded-3xl aspect-[21/9] shadow-xl overflow-hidden mb-10 max-w-5xl mx-auto">
  <img src="{PORT_ARRIVAL}" alt="{PORT_ARRIVAL_ALT}" width="1200" height="514" loading="lazy" decoding="async" />
</div>
<div class="grid lg:grid-cols-3 gap-6 text-sm">
  <div class="bg-sand-50 rounded-2xl p-6 border border-pr-100">
    <h2 class="font-display font-bold text-lg text-gray-900 mb-2">Where is the port?</h2>
    <p class="text-gray-600 leading-relaxed">
      St John's harbour serves major cruise lines with waterfront shopping and dining close to the
      terminal flow. Downtown streets and the cathedral area are walkable for a short self-guided loop.
    </p>
  </div>
  <div class="bg-sand-50 rounded-2xl p-6 border border-pr-100">
    <h2 class="font-display font-bold text-lg text-gray-900 mb-2">Moving on from the pier</h2>
    <p class="text-gray-600 leading-relaxed">
      Organised tour pickups, licensed taxis and a compact walking plan are the common next steps.
      Agree taxi quotes clearly, confirm currency, and keep a note of any return pickup arrangement.
    </p>
  </div>
  <div class="bg-sand-50 rounded-2xl p-6 border border-pr-100">
    <h2 class="font-display font-bold text-lg text-gray-900 mb-2">Currency &amp; basics</h2>
    <p class="text-gray-600 leading-relaxed">
      Eastern Caribbean dollars (XCD) are official. USD is widely accepted at tourist businesses —
      small notes help for short taxi hops and tips. We do not invent fixed taxi rates here.
    </p>
  </div>
</div>
''', bg="bg-white", pad="py-12")}
{_prose('''
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Distances that shape the day</h2>
<ul class="space-y-3 text-gray-600 leading-relaxed mb-8">
  <li><strong class="text-gray-800">Dickenson Bay:</strong> roughly 10–15 minutes north-west of the harbour — a practical near-port beach hop.</li>
  <li><strong class="text-gray-800">Nelson's Dockyard / English Harbour:</strong> roughly 30–45 minutes south — plan as a committed heritage theme.</li>
  <li><strong class="text-gray-800">South-west kayak / reef areas:</strong> often a longer transfer than Dickenson Bay; confirm live with any operator.</li>
</ul>
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">What fits different call lengths</h2>
<ul class="space-y-3 text-gray-600 leading-relaxed mb-8">
  <li><strong class="text-gray-800">Shorter windows:</strong> Heritage Quay / Redcliffe Quay walking, or a single nearby beach taxi — not Dockyard plus reef plus shopping.</li>
  <li><strong class="text-gray-800">Typical mid-length calls:</strong> one main theme with a light secondary stop nearby.</li>
  <li><strong class="text-gray-800">Longer calls:</strong> south-coast history or an active kayak day becomes more realistic if you depart early and protect the return.</li>
</ul>
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Planning the return window</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  Build a conservative buffer before all aboard. Queues, weather and road slowdowns are normal Caribbean variables.
  This site talks about cruise-aware timing — not unsupported “back on ship guarantees.”
</p>
''' + related_links([
    ("/one-day-in-antigua-from-a-cruise-ship/", "One day in Antigua"),
    ("/best-antigua-shore-excursions/", "Excursion styles"),
    ("/can-you-explore-antigua-without-an-excursion/", "Without an excursion"),
    ("/is-antigua-safe-for-cruise-passengers/", "Safety notes"),
]), bg="bg-sand-50")}
{faq_section([
    (
        "Is Antigua a tender port?",
        "Do not assume. Confirm your sailing's berth or tender notes with the cruise line. "
        "Local conditions and ship assignments can differ.",
    ),
    (
        "What is realistic near the port?",
        "Waterfront walking around Heritage Quay and Redcliffe Quay, plus a short taxi to Dickenson Bay, "
        "are the practical near-port themes. Nelson's Dockyard is a longer-distance commitment.",
    ),
    (
        "How much buffer should I leave?",
        "Leave more than you think you need — especially after south-coast drives. Confirm all-aboard "
        "time on the day and treat published schedules as live documents.",
    ),
], heading="St John's port FAQ")}
"""

    faqs: FaqList = [
        (
            "Is Antigua a tender port?",
            "Do not assume. Confirm your sailing's berth or tender notes with the cruise line. "
            "Local conditions and ship assignments can differ.",
        ),
        (
            "What is realistic near the port?",
            "Waterfront walking around Heritage Quay and Redcliffe Quay, plus a short taxi to Dickenson Bay, "
            "are the practical near-port themes. Nelson's Dockyard is a longer-distance commitment.",
        ),
        (
            "How much buffer should I leave?",
            "Leave more than you think you need — especially after south-coast drives. Confirm all-aboard "
            "time on the day and treat published schedules as live documents.",
        ),
    ]

    meta: Meta = {
        "title": "Antigua Port Guide | St John's Cruise Logistics & Shore Days",
        "description": (
            "Practical Antigua cruise port guide for St John's — Heritage Quay and Redcliffe Quay, "
            "distances to beaches and Nelson's Dockyard, and return-window planning."
        ),
        "canonical_path": "/antigua-port-guide/",
        "page_id": "port",
        "og_image": CRUISE_PORT,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# ONE DAY
# ---------------------------------------------------------------------------


def one_day() -> PageTuple:
    hero = hero_band(
        eyebrow="Port-day planning",
        title_html=f'One day in Antigua<br/><span class="{ACCENT}">from a cruise ship</span>',
        lead=(
            "Choose a style for the hours you actually have — beach, history, kayak, "
            "DIY St John's, or a scenic overview — instead of inventing one perfect itinerary."
        ),
        image=ONE_DAY_HERO,
        aria_label=ONE_DAY_HERO_ALT,
        breadcrumb="One day",
        actions=_cta(
            "/best-antigua-shore-excursions/",
            "Compare styles",
            "/antigua-port-guide/",
            "Port guide",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Anti-stacking rule", "One theme + optional light nearby stop"),
            ("Easy day", "Quays walk or Dickenson Bay taxi"),
            ("Heritage day", "Nelson's Dockyard / Shirley Heights"),
            ("Active day", "Kayak & snorkel styles"),
            ("Typical call", "Often ~6–10 hours — confirm live"),
        ]
    )

    main = f"""
{_prose('''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  An Antigua cruise day is long enough to do something memorable and short enough to ruin itself
  with optimistic stacking. Start with your all-aboard time, then pick one of the styles below.
</p>
''' + snap)}
{_section('''
<div class="grid md:grid-cols-2 gap-6">
  <article class="rounded-2xl border border-ocean-100 bg-white p-6">
    <h2 class="text-xl font-display font-bold text-gray-900 mb-3">Easy beach or quay day</h2>
    <p class="text-sm text-gray-600 leading-relaxed">
      Swim near port or stay on foot around Heritage Quay and Redcliffe Quay. Use the
      <a href="/best-beaches-in-antigua-for-cruise-passengers/" class="text-ocean-600 font-medium">beach guide</a>
      and
      <a href="/can-you-explore-antigua-without-an-excursion/" class="text-ocean-600 font-medium">DIY guide</a>
      — keep shopping light and protect the return window.
    </p>
  </article>
  <article class="rounded-2xl border border-ocean-100 bg-white p-6">
    <h2 class="text-xl font-display font-bold text-gray-900 mb-3">History day</h2>
    <p class="text-sm text-gray-600 leading-relaxed">
      Commit to English Harbour:
      <a href="/nelsons-dockyard-from-antigua-cruise-port/" class="text-ocean-600 font-medium">Nelson's Dockyard</a>
      and
      <a href="/shirley-heights-antigua-guide/" class="text-ocean-600 font-medium">Shirley Heights</a>.
      Skip a long unsupervised beach hop on the same call unless your ship stays unusually late.
    </p>
  </article>
  <article class="rounded-2xl border border-ocean-100 bg-white p-6">
    <h2 class="text-xl font-display font-bold text-gray-900 mb-3">Kayak / reef day</h2>
    <p class="text-sm text-gray-600 leading-relaxed">
      Choose an active water day only if fitness and call length support transfers plus paddling or snorkelling.
      Start with
      <a href="/antigua-kayak-snorkel-and-beach/" class="text-ocean-600 font-medium">kayak, snorkel &amp; beach</a>
      or the shorter
      <a href="/antigua-half-day-kayak-and-snorkel/" class="text-ocean-600 font-medium">half-day framing</a>.
    </p>
  </article>
  <article class="rounded-2xl border border-ocean-100 bg-white p-6">
    <h2 class="text-xl font-display font-bold text-gray-900 mb-3">Scenic overview day</h2>
    <p class="text-sm text-gray-600 leading-relaxed">
      Viewpoints and a beach break suit groups who want variety without deep time at one site.
      See
      <a href="/panoramic-antigua-and-beach-break/" class="text-ocean-600 font-medium">panoramic Antigua</a>
      and
      <a href="/the-antiguan-experience/" class="text-ocean-600 font-medium">the Antiguan experience</a>
      — both editorial only here.
    </p>
  </article>
</div>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">What not to do</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  Do not treat Antigua as a checklist. Nelson's Dockyard, Shirley Heights, a long beach lunch and a
  kayak-and-reef combo rarely fit a single cruise call from St John's without stress.
  Pick one coherent theme, then stop adding stops.
</p>
''' + related_links([
    ("/best-antigua-shore-excursions/", "Excursion hub"),
    ("/antigua-port-guide/", "Port guide"),
    ("/classic-beach-day/", "Classic beach day"),
    ("/contact/", "Contact"),
]))}
{faq_section([
    (
        "Is there one best day in Antigua?",
        "No. Match beach, heritage, kayak, DIY or a scenic overview to your call length "
        "and fitness — then stop adding stops.",
    ),
    (
        "Can I see Nelson's Dockyard and do a long beach day?",
        "Usually a poor trade on a typical call. South-coast road time plus a full beach afternoon "
        "leaves little margin for queues and delays.",
    ),
], heading="One-day planning FAQ")}
"""

    faqs: FaqList = [
        (
            "Is there one best day in Antigua?",
            "No. Match beach, heritage, kayak, DIY or a scenic overview to your call length "
            "and fitness — then stop adding stops.",
        ),
        (
            "Can I see Nelson's Dockyard and do a long beach day?",
            "Usually a poor trade on a typical call. South-coast road time plus a full beach afternoon "
            "leaves little margin for queues and delays.",
        ),
    ]

    meta: Meta = {
        "title": "One Day in Antigua from a Cruise Ship | Realistic Port Plans",
        "description": (
            "Plan one day in Antigua from a cruise ship — beach, history, kayak, DIY St John's "
            "and scenic scenarios without over-stacking."
        ),
        "canonical_path": "/one-day-in-antigua-from-a-cruise-ship/",
        "page_id": "one-day",
        "og_image": ONE_DAY_HERO,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# BEACHES
# ---------------------------------------------------------------------------


def beaches() -> PageTuple:
    hero = hero_band(
        eyebrow="Beach planning",
        title_html=f'Best beaches in Antigua<br/><span class="{ACCENT}">for cruise passengers</span>',
        lead=(
            "Which Antigua beaches fit a St John's call — near-port options such as Dickenson Bay, "
            "and when quieter cove days need organised transport."
        ),
        image=BEACHES,
        aria_label=BEACHES_ALT,
        breadcrumb="Beaches",
        actions=_cta(
            "/classic-beach-day/",
            "Classic beach day guide",
            "/can-you-explore-antigua-without-an-excursion/",
            "DIY beach hop",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Nearest popular beach", "Dickenson Bay ~10–15 min north-west"),
            ("West-coast option", "Hawksbill / Five Islands area — short taxi"),
            ("Quieter coves", "Often reached on organised beach-style days"),
            ("DIY tip", "Agree round-trip taxi timing before you settle in"),
            ("Return window", "Still plan a buffer — popular beaches get busy"),
        ]
    )

    main = f"""
{_section(f'''
<div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <div class="section-label">Cruise-useful beaches</div>
    <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-4">Stay close when the clock is tight</h2>
    <p class="text-gray-600 leading-relaxed mb-4">
      Antigua is famous for its coastline, but cruise passengers only need the beaches that fit
      the hours after docking at St John's. Dickenson Bay sits roughly 10–15 minutes north-west —
      a practical taxi hop when swimming is the priority. West-coast coves around Hawksbill / Five Islands
      are also in the short-transfer orbit for many passengers.
    </p>
    <p class="text-gray-600 leading-relaxed mb-4">
      Quieter south-coast beaches can look idyllic in photographs and still be a poor fit if the transfer
      eats your swimming time. Organised beach-style days sometimes include loungers and a timed return;
      independent taxis put the clockkeeping on you.
    </p>
    <ul class="space-y-2 text-sm text-gray-600">
      <li class="flex gap-2"><span class="text-ocean-600">✔</span> Dickenson Bay for near-port swimming</li>
      <li class="flex gap-2"><span class="text-ocean-600">✔</span> Agree taxi return time before you unpack</li>
      <li class="flex gap-2"><span class="text-ocean-600">✔</span> Keep shopping as a light add-on, not a third major stop</li>
    </ul>
  </div>
  <div class="info-image rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{BEACHES}" alt="{BEACHES_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
</div>
''')}
{_section(snap, pad="pb-8 pt-0")}
{_prose('''
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Decision questions</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  <strong>Do you want maximum water time?</strong> Stay near St John's.
  <strong>Do you want a quieter cove with transport handled?</strong> Read the
  <a href="/classic-beach-day/" class="text-ocean-600 font-medium">classic beach day</a> editorial page —
  booking is not offered on this site yet.
  <strong>Do you also want Nelson's Dockyard?</strong> That is usually a different day shape.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  Facilities, chair rentals and access rules change. Confirm live locally or with your provider;
  we do not invent fees or opening hours.
</p>
''' + related_links([
    ("/classic-beach-day/", "Classic beach day"),
    ("/panoramic-antigua-and-beach-break/", "Panoramic & beach"),
    ("/antigua-port-guide/", "Port guide"),
    ("/one-day-in-antigua-from-a-cruise-ship/", "One day"),
]), bg="bg-sand-50")}
{faq_section([
    (
        "How far is Dickenson Bay from the cruise port?",
        "Roughly 10–15 minutes north-west of St John's by road, depending on traffic. "
        "Treat the minutes as approximate planning guidance.",
    ),
    (
        "Can I beach-hop independently?",
        "Yes for nearby north-west beaches if you use a licensed taxi, agree the fare and return timing, "
        "and protect your all-aboard window. Farther coves need more careful scheduling.",
    ),
], heading="Antigua beach FAQ")}
"""

    faqs: FaqList = [
        (
            "How far is Dickenson Bay from the cruise port?",
            "Roughly 10–15 minutes north-west of St John's by road, depending on traffic. "
            "Treat the minutes as approximate planning guidance.",
        ),
        (
            "Can I beach-hop independently?",
            "Yes for nearby north-west beaches if you use a licensed taxi, agree the fare and return timing, "
            "and protect your all-aboard window. Farther coves need more careful scheduling.",
        ),
    ]

    meta: Meta = {
        "title": "Best Beaches in Antigua for Cruise Passengers | St John's Guide",
        "description": (
            "Cruise passenger beach guide for Antigua — Dickenson Bay timing from St John's, "
            "west-coast options and when organised beach days make more sense."
        ),
        "canonical_path": "/best-beaches-in-antigua-for-cruise-passengers/",
        "page_id": "beaches",
        "og_image": BEACHES,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# DIY — high preservation, not hard sell
# ---------------------------------------------------------------------------


def diy() -> PageTuple:
    hero = hero_band(
        eyebrow="Independent exploring",
        title_html=f'Can you explore Antigua<br/><span class="{ACCENT}">without an excursion?</span>',
        lead=(
            "Yes — especially around St John's. Here is what works on foot or by taxi, "
            "what usually needs organised transport, and how to keep a cruise return window realistic."
        ),
        image=PORT_ARRIVAL,
        aria_label=PORT_ARRIVAL_ALT,
        breadcrumb="Without an excursion",
        actions=_cta(
            "/antigua-port-guide/",
            "Port logistics",
            "/best-beaches-in-antigua-for-cruise-passengers/",
            "Nearby beaches",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Best DIY fit", "Heritage Quay, Redcliffe Quay, short harbour walk"),
            ("Easy taxi add-on", "Dickenson Bay ~10–15 min each way"),
            ("Harder DIY", "Nelson's Dockyard, Shirley Heights, reef days"),
            ("Clock rule", "Agree return pickup before you settle in"),
            ("When a tour helps", "South-coast timing, guides, multi-stop pacing"),
        ]
    )

    main = f"""
{_prose('''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Plenty of cruise passengers enjoy Antigua without booking a shore package. St John's is compact:
  once you clear the terminal flow, <strong>Heritage Quay</strong> and <strong>Redcliffe Quay</strong>
  put shops, waterfront restaurants and harbour views within walking distance. That alone can fill
  a short call. The question is not “is DIY possible?” — it is “what does DIY realistically cover
  before all aboard?”
</p>
''' + snap)}
{_section('''
<div class="grid md:grid-cols-2 gap-6">
  <article class="rounded-2xl border border-ocean-100 bg-white p-6">
    <div class="section-label">Few hours only</div>
    <h2 class="text-xl font-display font-bold text-gray-900 mb-3">Stay in the harbour orbit</h2>
    <p class="text-sm text-gray-600 leading-relaxed mb-3">
      Walk the quays, browse duty-free areas, photograph the harbour and take a calm lunch near the water.
      Add St John's Cathedral or the public market only if energy and heat allow — shade and hydration matter.
    </p>
    <p class="text-sm text-gray-600 leading-relaxed">
      Keep valuables close in crowded market stretches. DIY does not mean careless; it means simple logistics.
    </p>
  </article>
  <article class="rounded-2xl border border-ocean-100 bg-white p-6">
    <div class="section-label">Half-day beach hop</div>
    <h2 class="text-xl font-display font-bold text-gray-900 mb-3">Taxi to Dickenson Bay</h2>
    <p class="text-sm text-gray-600 leading-relaxed mb-3">
      Dickenson Bay is roughly 10–15 minutes north-west of the cruise harbour — one of the most practical
      independent beach moves from St John's. Use a licensed taxi, agree the fare and, crucially,
      the return pickup time before you settle on loungers.
    </p>
    <p class="text-sm text-gray-600 leading-relaxed">
      Build margin for traffic and terminal queues. A beautiful swim is not worth a sprint back to the gangway.
    </p>
  </article>
  <article class="rounded-2xl border border-ocean-100 bg-white p-6">
    <div class="section-label">Public transport</div>
    <h2 class="text-xl font-display font-bold text-gray-900 mb-3">Buses exist — clocks still win</h2>
    <p class="text-sm text-gray-600 leading-relaxed mb-3">
      Local buses can be inexpensive for independent travellers with flexibility, including routes that
      head toward the south coast. They are slower and less predictable than a pre-arranged taxi or tour
      transfer — fine for experienced DIY travellers, risky if your ship’s window is tight.
    </p>
    <p class="text-sm text-gray-600 leading-relaxed">
      Confirm current routes and the walk between the terminal area and any bus station on the day;
      do not rely on a memory of last year’s timetable.
    </p>
  </article>
  <article class="rounded-2xl border border-ocean-100 bg-white p-6">
    <div class="section-label">When organised help helps</div>
    <h2 class="text-xl font-display font-bold text-gray-900 mb-3">Dockyard, heights and reef days</h2>
    <p class="text-sm text-gray-600 leading-relaxed mb-3">
      <a href="/nelsons-dockyard-from-antigua-cruise-port/" class="text-ocean-600 font-medium">Nelson's Dockyard</a>
      and
      <a href="/shirley-heights-antigua-guide/" class="text-ocean-600 font-medium">Shirley Heights</a>
      sit roughly 30–45 minutes south. Kayak and reef itineraries add water segments and equipment logistics.
      Organised transport is not mandatory — but it removes several failure points on a cruise clock.
    </p>
    <p class="text-sm text-gray-600 leading-relaxed">
      If you go privately, keep the wish list short and reverse-plan from all aboard.
    </p>
  </article>
</div>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">A simple DIY checklist</h2>
<ul class="space-y-3 text-gray-600 leading-relaxed mb-6">
  <li>Note gangway and all-aboard times from the ship — treat them as live documents.</li>
  <li>Decide: quay walk only, nearby beach taxi, or a longer private hire — not all three plus shopping.</li>
  <li>Carry small notes of USD or XCD for taxis; agree the price before departure.</li>
  <li>Save a meeting point for your return pickup; do not assume the driver will wait indefinitely.</li>
  <li>Leave a conservative buffer — planning guidance, not a guarantee against every delay.</li>
</ul>
<p class="text-gray-600 leading-relaxed mb-4">
  This page stays focused on independent exploration because that is a real passenger question.
  Organised day styles remain available as editorial comparisons on the
  <a href="/best-antigua-shore-excursions/" class="text-ocean-600 font-medium">excursions hub</a>
  if your group later prefers a guided format — booking is not offered on this website yet.
</p>
''' + related_links([
    ("/antigua-port-guide/", "Port guide"),
    ("/best-beaches-in-antigua-for-cruise-passengers/", "Beach guide"),
    ("/one-day-in-antigua-from-a-cruise-ship/", "One day"),
    ("/is-antigua-safe-for-cruise-passengers/", "Safety notes"),
]))}
{faq_section([
    (
        "Can I explore Antigua without a shore excursion?",
        "Yes for St John's waterfront and nearby beaches by taxi. Farther heritage and reef sites "
        "need more transport planning and a careful return window.",
    ),
    (
        "Is Dickenson Bay realistic independently?",
        "Often yes on a typical call: roughly 10–15 minutes each way, plus swim time and a buffer. "
        "Agree the taxi return before you settle in.",
    ),
    (
        "Should I rent a car for one cruise day?",
        "Some passengers do; others find taxi or organised transport simpler for a single call. "
        "Factor parking, unfamiliar roads and the all-aboard clock — we do not sell rentals here.",
    ),
], heading="Exploring Antigua independently")}
"""

    faqs: FaqList = [
        (
            "Can I explore Antigua without a shore excursion?",
            "Yes for St John's waterfront and nearby beaches by taxi. Farther heritage and reef sites "
            "need more transport planning and a careful return window.",
        ),
        (
            "Is Dickenson Bay realistic independently?",
            "Often yes on a typical call: roughly 10–15 minutes each way, plus swim time and a buffer. "
            "Agree the taxi return before you settle in.",
        ),
        (
            "Should I rent a car for one cruise day?",
            "Some passengers do; others find taxi or organised transport simpler for a single call. "
            "Factor parking, unfamiliar roads and the all-aboard clock — we do not sell rentals here.",
        ),
    ]

    meta: Meta = {
        "title": "Can You Explore Antigua Without an Excursion? | DIY Cruise Guide",
        "description": (
            "Practical DIY guide for Antigua cruise passengers — St John's walking, Dickenson Bay taxis, "
            "when organised transport helps, and how to protect your return window."
        ),
        "canonical_path": "/can-you-explore-antigua-without-an-excursion/",
        "page_id": "diy",
        "og_image": PORT_ARRIVAL,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# CLASSIC BEACH DAY — editorial only
# ---------------------------------------------------------------------------


def classic_beach_day() -> PageTuple:
    hero = hero_band(
        eyebrow="Editorial beach day",
        title_html=f'Classic beach day<br/><span class="{ACCENT}">in Antigua</span>',
        lead=(
            "How a simple Antigua beach-focused shore day fits a St John's cruise call — "
            "pacing, who it suits, and what to confirm independently. Not a bookable product page."
        ),
        image=CLASSIC_BEACH_HERO,
        aria_label=CLASSIC_BEACH_HERO_ALT,
        breadcrumb="Classic beach day",
        actions=_cta(
            "/best-beaches-in-antigua-for-cruise-passengers/",
            "Beach planning guide",
            "/one-day-in-antigua-from-a-cruise-ship/",
            "One-day scenarios",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Role", "Relaxed swimming and shade-focused day"),
            ("Best for", "Shorter calls; mixed energy levels"),
            ("Transfer", "Usually shorter than English Harbour"),
            ("Pairing", "Light quay time — not Dockyard + reef"),
            ("This page", "Editorial only — no booking on this site"),
        ]
    )

    main = f"""
{_section(f'''
<div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <div class="section-label">Why passengers ask</div>
    <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-4">Sun and sea without a marathon inland drive</h2>
    <p class="text-gray-600 leading-relaxed mb-4">
      A classic Antigua beach day is the answer when the ship’s clock is finite and the group’s
      priority is swimming, shade and a calm lunch rather than stacking heritage stops.
      Near-port beaches such as Dickenson Bay keep transfer risk lower; quieter cove-style days
      may involve a longer coach or taxi ride — still usually less ambitious than English Harbour
      plus a second major theme.
    </p>
    <p class="text-gray-600 leading-relaxed mb-4">
      Booking is not offered on this website yet. If you arrange a beach day independently,
      confirm the beach location, what is included, and how the return to St John's is timed —
      with the operator and against your live all-aboard time.
    </p>
  </div>
  <div class="info-image rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{CLASSIC_BEACH_HERO}" alt="{CLASSIC_BEACH_HERO_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
</div>
''')}
{_section(snap, pad="pb-8 pt-0")}
{_prose('''
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Planning notes</h2>
<ul class="space-y-3 text-gray-600 leading-relaxed mb-6">
  <li>Ask where you will actually spend the beach hours — names and facilities change by season.</li>
  <li>Clarify whether lunch, chairs or shade are included or paid locally.</li>
  <li>Keep shopping as a light finish near the quays, not a third destination.</li>
  <li>Protect a conservative return buffer; we do not claim ship-return guarantees.</li>
</ul>
<p class="text-gray-600 leading-relaxed mb-4">
  Prefer viewpoints plus a swim? See
  <a href="/panoramic-antigua-and-beach-break/" class="text-ocean-600 font-medium">panoramic Antigua and beach break</a>.
  Prefer walking St John's instead? Use the
  <a href="/can-you-explore-antigua-without-an-excursion/" class="text-ocean-600 font-medium">DIY guide</a>.
</p>
''' + related_links([
    ("/best-beaches-in-antigua-for-cruise-passengers/", "Beach guide"),
    ("/best-antigua-shore-excursions/", "Compare styles"),
    ("/antigua-port-guide/", "Port guide"),
    ("/contact/", "Contact"),
]), bg="bg-sand-50")}
{faq_section([
    (
        "Is a classic beach day good for cruise passengers?",
        "Yes when swimming and relaxed pacing matter more than covering the whole island. "
        "Confirm location and timing live with any provider you choose.",
    ),
    (
        "Can I book this here?",
        "Not in this phase. This is an editorial planning page only.",
    ),
], heading="Classic beach day FAQ")}
"""

    faqs: FaqList = [
        (
            "Is a classic beach day good for cruise passengers?",
            "Yes when swimming and relaxed pacing matter more than covering the whole island. "
            "Confirm location and timing live with any provider you choose.",
        ),
        (
            "Can I book this here?",
            "Not in this phase. This is an editorial planning page only.",
        ),
    ]

    meta: Meta = {
        "title": "Classic Beach Day Antigua | Cruise Passenger Editorial Guide",
        "description": (
            "Editorial guide to a classic Antigua beach day from St John's — who it suits, "
            "pacing tips and what to confirm independently. Not a booking page."
        ),
        "canonical_path": "/classic-beach-day/",
        "page_id": "classic-beach",
        "og_image": CLASSIC_BEACH_HERO,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# HISTORY & CULTURE — editorial
# ---------------------------------------------------------------------------


def history_culture() -> PageTuple:
    hero = hero_band(
        eyebrow="Editorial heritage day",
        title_html=f'Antigua history &amp; culture<br/><span class="{ACCENT}">from St John\'s</span>',
        lead=(
            "How a south-coast heritage day — Nelson's Dockyard, lookouts such as Shirley Heights, "
            "and related interpretation stops — fits a cruise call. Editorial planning only."
        ),
        image=HISTORY,
        aria_label=HISTORY_ALT,
        breadcrumb="History & culture",
        actions=_cta(
            "/nelsons-dockyard-from-antigua-cruise-port/",
            "Nelson's Dockyard guide",
            "/shirley-heights-antigua-guide/",
            "Shirley Heights guide",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Theme", "English Harbour heritage corridor"),
            ("Transfer", "Often ~30–45 min south from St John's"),
            ("Core stops", "Nelson's Dockyard; Shirley Heights lookout"),
            ("Activity", "Mostly walking and viewing — confirm mobility needs"),
            ("This page", "Editorial only — no booking on this site"),
        ]
    )

    main = f"""
{_section(f'''
<div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <div class="section-label">South-coast commitment</div>
    <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-4">Antigua's strongest history day from a cruise ship</h2>
    <p class="text-gray-600 leading-relaxed mb-4">
      A history-and-culture shore day from St John's usually points south to
      <strong>Nelson's Dockyard</strong> in English Harbour — a restored Georgian naval yard and
      UNESCO-listed landscape — with a lookout stop at <strong>Shirley Heights</strong> for harbour
      and Caribbean views. Dow's Hill interpretation stops sometimes appear on the same corridor.
    </p>
    <p class="text-gray-600 leading-relaxed mb-4">
      Road time is often around 30–45 minutes each way. That is approximate planning guidance, not a
      promise. Short calls should think carefully before adding a long beach lunch on top.
    </p>
    <p class="text-gray-600 leading-relaxed">
      Booking is not offered on this website yet. Confirm any operator’s itinerary, park entry
      arrangements and return timing independently.
    </p>
  </div>
  <div class="info-image rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{HISTORY}" alt="{HISTORY_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
</div>
''')}
{_section(snap, pad="pb-8 pt-0")}
{_prose('''
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Who it suits</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  Passengers who want maritime history, photography and guided context more than a full swim day.
  Families and mixed ages often manage the walks if heat and uneven surfaces are considered —
  check mobility needs before you commit.
</p>
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4 mt-10">Read next</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  Deeper site notes:
  <a href="/nelsons-dockyard-from-antigua-cruise-port/" class="text-ocean-600 font-medium">Nelson's Dockyard from the cruise port</a>
  and
  <a href="/shirley-heights-antigua-guide/" class="text-ocean-600 font-medium">Shirley Heights guide</a>.
  For a lighter scenic-plus-beach shape, see
  <a href="/panoramic-antigua-and-beach-break/" class="text-ocean-600 font-medium">panoramic Antigua</a>.
</p>
''' + related_links([
    ("/best-antigua-shore-excursions/", "Compare styles"),
    ("/one-day-in-antigua-from-a-cruise-ship/", "One day"),
    ("/antigua-port-guide/", "Port guide"),
    ("/contact/", "Contact"),
]), bg="bg-sand-50")}
{faq_section([
    (
        "Is Nelson's Dockyard realistic on a cruise call?",
        "Often yes on a typical 6–10 hour Antigua call if you treat it as the main theme and "
        "protect a return buffer. Confirm live road timing.",
    ),
    (
        "Can I book a history tour here?",
        "Not in this phase. This page is editorial planning only.",
    ),
], heading="History & culture FAQ")}
"""

    faqs: FaqList = [
        (
            "Is Nelson's Dockyard realistic on a cruise call?",
            "Often yes on a typical 6–10 hour Antigua call if you treat it as the main theme and "
            "protect a return buffer. Confirm live road timing.",
        ),
        (
            "Can I book a history tour here?",
            "Not in this phase. This page is editorial planning only.",
        ),
    ]

    meta: Meta = {
        "title": "Antigua History and Culture Tour | Cruise Editorial Guide",
        "description": (
            "Editorial guide to Antigua history and culture shore days from St John's — "
            "Nelson's Dockyard, Shirley Heights and cruise-aware pacing. Not a booking page."
        ),
        "canonical_path": "/antigua-exclusive-history-and-culture-tour/",
        "page_id": "history",
        "og_image": HISTORY,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# KAYAK SNORKEL — CSS-only hero
# ---------------------------------------------------------------------------


def kayak_snorkel() -> PageTuple:
    hero = hero_band(
        eyebrow="Editorial adventure day",
        title_html=f'Antigua kayak, snorkel<br/><span class="{ACCENT}">&amp; beach</span>',
        lead=(
            "How an active Antigua shore day — mangrove kayaking, reef snorkelling and a beach finish — "
            "fits a St John's cruise call. Editorial only; confirm operators independently."
        ),
        image=None,
        aria_label="Antigua coastline gradient representing kayak and snorkel shore days from St John's",
        css_only=True,
        breadcrumb="Kayak & snorkel",
        actions=_cta(
            "/antigua-half-day-kayak-and-snorkel/",
            "Shorter half-day framing",
            "/best-antigua-shore-excursions/",
            "Compare styles",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Theme", "Kayak + snorkel + beach combo"),
            ("Fitness", "Moderate — paddling and swimming"),
            ("Transfer", "Usually longer than Dickenson Bay"),
            ("Clock", "Needs early start and protected buffer"),
            ("This page", "Editorial only — no booking on this site"),
        ]
    )

    main = f"""
{_prose('''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Antigua’s kayak-and-snorkel shore days typically move passengers from St John's toward the
  south-west coast for sheltered paddling (often mangrove or lagoon settings) and reef snorkelling
  associated with areas such as Cades Reef, then finish with beach time. Exact put-ins and reef
  segments vary by operator and conditions — treat marketing maps as orientation, not a promise.
</p>
''' + snap)}
{_prose('''
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Cruise-passenger framing</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  This style suits active travellers who want water time with structure. It is a poorer fit for
  passengers who dislike heat, want a long unsupervised beach afternoon, or have a short call.
  Transfers plus kit briefings plus two water segments consume the day quickly.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  Booking is not offered on this website yet. If you arrange anything independently, confirm duration,
  what is included, fitness expectations and how the return to St John's is timed — against your
  live all-aboard time, not against a brochure average.
</p>
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4 mt-10">Half-day vs fuller combo</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  Prefer a tighter, time-focused framing? Read
  <a href="/antigua-half-day-kayak-and-snorkel/" class="text-ocean-600 font-medium">Antigua half-day kayak and snorkel</a>
  — a distinct page, not a redirect. Use both guides to decide which shape matches your ship’s window.
</p>
''' + related_links([
    ("/antigua-half-day-kayak-and-snorkel/", "Half-day kayak"),
    ("/best-beaches-in-antigua-for-cruise-passengers/", "Beach guide"),
    ("/one-day-in-antigua-from-a-cruise-ship/", "One day"),
    ("/contact/", "Contact"),
]), bg="bg-sand-50")}
{faq_section([
    (
        "Is kayak and snorkel realistic from a cruise ship?",
        "Often on a typical Antigua call if you start early, accept transfer time and protect a return buffer. "
        "Confirm live duration with any operator.",
    ),
    (
        "Can I book this here?",
        "Not in this phase. This is an editorial planning page only.",
    ),
], heading="Kayak & snorkel FAQ")}
"""

    faqs: FaqList = [
        (
            "Is kayak and snorkel realistic from a cruise ship?",
            "Often on a typical Antigua call if you start early, accept transfer time and protect a return buffer. "
            "Confirm live duration with any operator.",
        ),
        (
            "Can I book this here?",
            "Not in this phase. This is an editorial planning page only.",
        ),
    ]

    meta: Meta = {
        "title": "Antigua Kayak, Snorkel and Beach | Cruise Editorial Guide",
        "description": (
            "Editorial guide to Antigua kayak, snorkel and beach shore days from St John's — "
            "fitness, timing and what to confirm independently. Not a booking page."
        ),
        "canonical_path": "/antigua-kayak-snorkel-and-beach/",
        "page_id": "kayak",
        "og_image": INTRO,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# NELSON'S DOCKYARD
# ---------------------------------------------------------------------------


def nelsons() -> PageTuple:
    hero = hero_band(
        eyebrow="Heritage site guide",
        title_html=f'Nelson\'s Dockyard<br/><span class="{ACCENT}">from Antigua cruise port</span>',
        lead=(
            "Practical cruise-passenger notes on visiting Nelson's Dockyard from St John's — "
            "distance, day shape and how it pairs with Shirley Heights."
        ),
        image=NELSONS,
        aria_label=NELSONS_ALT,
        breadcrumb="Nelson's Dockyard",
        actions=_cta(
            "/antigua-exclusive-history-and-culture-tour/",
            "History day framing",
            "/shirley-heights-antigua-guide/",
            "Shirley Heights",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Location", "English Harbour, south coast"),
            ("Transfer from St John's", "Often ~30–45 minutes by road"),
            ("Character", "UNESCO-listed Georgian naval dockyard"),
            ("Pairing", "Shirley Heights lookout on many heritage days"),
            ("Fees / hours", "Confirm live locally — not published here"),
        ]
    )

    main = f"""
{_section(f'''
<div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <div class="section-label">Why it matters</div>
    <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-4">Antigua's headline heritage stop</h2>
    <p class="text-gray-600 leading-relaxed mb-4">
      Nelson's Dockyard is a restored Georgian naval facility in English Harbour and the centrepiece
      of a wider national park landscape recognised by UNESCO. For cruise passengers, it is the
      clearest “history day” destination from St John's — provided you accept the southbound road time.
    </p>
    <p class="text-gray-600 leading-relaxed mb-4">
      Expect roughly 30–45 minutes each way depending on traffic and stops. That is approximate
      planning guidance. Entry arrangements, museum hours and trail access change — confirm live
      rather than relying on outdated blog figures.
    </p>
    <ul class="space-y-2 text-sm text-gray-600">
      <li class="flex gap-2"><span class="text-ocean-600">✔</span> Strong fit as a primary theme on mid-to-longer calls</li>
      <li class="flex gap-2"><span class="text-ocean-600">✔</span> Pairs naturally with Shirley Heights</li>
      <li class="flex gap-2"><span class="text-ocean-600">✔</span> Weak fit if you also insist on a full kayak-and-reef combo</li>
    </ul>
  </div>
  <div class="info-image rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{NELSONS}" alt="{NELSONS_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
</div>
''')}
{_section(snap, pad="pb-8 pt-0")}
{_prose('''
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Independent vs organised</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  Some passengers reach English Harbour by private taxi or local bus. Organised heritage days handle
  pacing across Dockyard and lookout stops. Neither approach deletes the road miles — see the
  <a href="/can-you-explore-antigua-without-an-excursion/" class="text-ocean-600 font-medium">DIY guide</a>
  for independent trade-offs.
</p>
''' + related_links([
    ("/shirley-heights-antigua-guide/", "Shirley Heights"),
    ("/antigua-exclusive-history-and-culture-tour/", "History & culture"),
    ("/antigua-port-guide/", "Port guide"),
    ("/one-day-in-antigua-from-a-cruise-ship/", "One day"),
]), bg="bg-sand-50")}
{faq_section([
    (
        "How far is Nelson's Dockyard from St John's cruise port?",
        "Roughly 30–45 minutes south by road, depending on traffic and stops. "
        "Treat the minutes as approximate.",
    ),
    (
        "Can I combine Dockyard with a long beach afternoon?",
        "Usually stressful on a typical call. Choose heritage or a full beach day as the primary theme.",
    ),
], heading="Nelson's Dockyard FAQ")}
"""

    faqs: FaqList = [
        (
            "How far is Nelson's Dockyard from St John's cruise port?",
            "Roughly 30–45 minutes south by road, depending on traffic and stops. "
            "Treat the minutes as approximate.",
        ),
        (
            "Can I combine Dockyard with a long beach afternoon?",
            "Usually stressful on a typical call. Choose heritage or a full beach day as the primary theme.",
        ),
    ]

    meta: Meta = {
        "title": "Nelson's Dockyard from Antigua Cruise Port | St John's Guide",
        "description": (
            "Cruise passenger guide to Nelson's Dockyard from St John's — approximate transfer time, "
            "pairing with Shirley Heights and realistic port-day planning."
        ),
        "canonical_path": "/nelsons-dockyard-from-antigua-cruise-port/",
        "page_id": "nelsons",
        "og_image": NELSONS,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# SHIRLEY HEIGHTS
# ---------------------------------------------------------------------------


def shirley() -> PageTuple:
    hero = hero_band(
        eyebrow="Lookout guide",
        title_html=f'Shirley Heights<br/><span class="{ACCENT}">Antigua guide</span>',
        lead=(
            "What cruise passengers should know about Shirley Heights — the historic lookout "
            "above English Harbour — and how it fits a St John's port day."
        ),
        image=SHIRLEY,
        aria_label=SHIRLEY_ALT,
        breadcrumb="Shirley Heights",
        actions=_cta(
            "/nelsons-dockyard-from-antigua-cruise-port/",
            "Nelson's Dockyard",
            "/panoramic-antigua-and-beach-break/",
            "Panoramic day framing",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Role", "Historic lookout above English Harbour"),
            ("Transfer", "Same south-coast corridor as Nelson's Dockyard"),
            ("Visit style", "Short walk to viewpoints — confirm mobility"),
            ("Cruise note", "Famous Sunday gatherings are not a typical ship-day feature"),
            ("Pairing", "Often combined with Dockyard on heritage days"),
        ]
    )

    main = f"""
{_section(f'''
<div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <div class="section-label">The view passengers want</div>
    <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-4">Harbour panorama with a military past</h2>
    <p class="text-gray-600 leading-relaxed mb-4">
      Shirley Heights sits on high ground above English Harbour and Falmouth Harbour — a historic
      military lookout that today is visited for sweeping Caribbean views and photography.
      From St John's it shares the same approximate 30–45 minute southbound transfer as Nelson's Dockyard.
    </p>
    <p class="text-gray-600 leading-relaxed mb-4">
      Cruise guests should not plan around evening parties marketed for hotel visitors; daytime
      lookout stops on heritage or panoramic shore days are the realistic ship-day version.
      Access details and any park fees change — confirm live.
    </p>
  </div>
  <div class="info-image rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{SHIRLEY}" alt="{SHIRLEY_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
</div>
''')}
{_section(snap, pad="pb-8 pt-0")}
{_prose('''
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">How to use it in a cruise plan</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  Treat Shirley Heights as part of a south-coast heritage or scenic theme, not as a quick add-on
  after Dickenson Bay and a kayak day. Editorial framings:
  <a href="/antigua-exclusive-history-and-culture-tour/" class="text-ocean-600 font-medium">history and culture</a>
  and
  <a href="/panoramic-antigua-and-beach-break/" class="text-ocean-600 font-medium">panoramic Antigua and beach break</a>.
</p>
''' + related_links([
    ("/nelsons-dockyard-from-antigua-cruise-port/", "Nelson's Dockyard"),
    ("/antigua-exclusive-history-and-culture-tour/", "History & culture"),
    ("/one-day-in-antigua-from-a-cruise-ship/", "One day"),
    ("/antigua-port-guide/", "Port guide"),
]), bg="bg-sand-50")}
{faq_section([
    (
        "Is Shirley Heights worth it on a cruise day?",
        "Yes if you already committed to the south coast for Nelson's Dockyard or a scenic drive. "
        "It is a weak standalone rush from the pier on a short call.",
    ),
    (
        "How far is it from St John's?",
        "Roughly the same south-coast transfer as Nelson's Dockyard — often around 30–45 minutes by road.",
    ),
], heading="Shirley Heights FAQ")}
"""

    faqs: FaqList = [
        (
            "Is Shirley Heights worth it on a cruise day?",
            "Yes if you already committed to the south coast for Nelson's Dockyard or a scenic drive. "
            "It is a weak standalone rush from the pier on a short call.",
        ),
        (
            "How far is it from St John's?",
            "Roughly the same south-coast transfer as Nelson's Dockyard — often around 30–45 minutes by road.",
        ),
    ]

    meta: Meta = {
        "title": "Shirley Heights Antigua Guide | Cruise Passenger Lookout Notes",
        "description": (
            "Cruise passenger guide to Shirley Heights in Antigua — views above English Harbour, "
            "transfer context from St John's and realistic port-day pairing."
        ),
        "canonical_path": "/shirley-heights-antigua-guide/",
        "page_id": "shirley",
        "og_image": SHIRLEY,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# ANTIGUAN EXPERIENCE — editorial
# ---------------------------------------------------------------------------


def antiguan_experience() -> PageTuple:
    hero = hero_band(
        eyebrow="Editorial island day",
        title_html=f'The Antiguan<br/><span class="{ACCENT}">Experience</span>',
        lead=(
            "A culture-and-countryside shore day framing from St John's — scenic drives, "
            "local stops and a beach finish — explained for cruise timing. Not a booking page."
        ),
        image=EXPERIENCE,
        aria_label=EXPERIENCE_ALT,
        breadcrumb="Antiguan Experience",
        actions=_cta(
            "/best-antigua-shore-excursions/",
            "Compare styles",
            "/best-beaches-in-antigua-for-cruise-passengers/",
            "Beach guide",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Theme", "Countryside / culture + beach finish"),
            ("Best for", "First-time visitors wanting variety"),
            ("Pace", "Several stops — keep expectations flexible"),
            ("Contrast", "Less Dockyard-deep than a pure history day"),
            ("This page", "Editorial only — no booking on this site"),
        ]
    )

    main = f"""
{_section(f'''
<div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <div class="section-label">Island overview style</div>
    <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-4">Beyond the pier without a single-site deep dive</h2>
    <p class="text-gray-600 leading-relaxed mb-4">
      “The Antiguan Experience” style of shore day typically mixes a scenic drive through countryside
      and coastal villages with local cultural or agricultural stops — pineapple heritage is a common
      talking point on Antigua — and finishes with beach time. Exact stops vary by operator and season.
    </p>
    <p class="text-gray-600 leading-relaxed mb-4">
      It suits passengers who want a sampler rather than a long unsupervised beach or a Dockyard-focused
      history day. Because the route is multi-stop, protect the return window and avoid adding Nelson's
      Dockyard as a last-minute extra.
    </p>
    <p class="text-gray-600 leading-relaxed">
      Booking is not offered on this website yet. Confirm inclusions and timing independently if you
      arrange anything with a provider.
    </p>
  </div>
  <div class="info-image rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{EXPERIENCE}" alt="{EXPERIENCE_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
</div>
''')}
{_section(snap, pad="pb-8 pt-0")}
{_prose('''
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">How it compares</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  Want deeper English Harbour history? Use the
  <a href="/antigua-exclusive-history-and-culture-tour/" class="text-ocean-600 font-medium">history and culture</a>
  guide. Want viewpoints plus a swim with lighter cultural content? See
  <a href="/panoramic-antigua-and-beach-break/" class="text-ocean-600 font-medium">panoramic Antigua</a>.
  Prefer DIY St John's? Start with the
  <a href="/can-you-explore-antigua-without-an-excursion/" class="text-ocean-600 font-medium">without an excursion</a>
  page.
</p>
''' + related_links([
    ("/one-day-in-antigua-from-a-cruise-ship/", "One day"),
    ("/classic-beach-day/", "Classic beach day"),
    ("/antigua-port-guide/", "Port guide"),
    ("/contact/", "Contact"),
]), bg="bg-sand-50")}
{faq_section([
    (
        "Who is the Antiguan Experience style for?",
        "First-time visitors and mixed groups who want countryside context plus a beach finish, "
        "without committing the whole day to one heritage site.",
    ),
    (
        "Can I book it on this site?",
        "Not in this phase. Editorial planning only.",
    ),
], heading="Antiguan Experience FAQ")}
"""

    faqs: FaqList = [
        (
            "Who is the Antiguan Experience style for?",
            "First-time visitors and mixed groups who want countryside context plus a beach finish, "
            "without committing the whole day to one heritage site.",
        ),
        (
            "Can I book it on this site?",
            "Not in this phase. Editorial planning only.",
        ),
    ]

    meta: Meta = {
        "title": "The Antiguan Experience | Cruise Editorial Island Day Guide",
        "description": (
            "Editorial guide to The Antiguan Experience shore day style from St John's — "
            "countryside, culture stops and beach finish for cruise passengers. Not a booking page."
        ),
        "canonical_path": "/the-antiguan-experience/",
        "page_id": "experience",
        "og_image": EXPERIENCE,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# HALF-DAY KAYAK — CSS-only; distinct from full kayak page
# ---------------------------------------------------------------------------


def half_day_kayak() -> PageTuple:
    hero = hero_band(
        eyebrow="Editorial · time-focused",
        title_html=f'Antigua half-day<br/><span class="{ACCENT}">kayak &amp; snorkel</span>',
        lead=(
            "A shorter, timing-first framing for Antigua kayak and reef time from a cruise call — "
            "distinct from the fuller kayak, snorkel and beach guide. Editorial only."
        ),
        image=None,
        aria_label="Antigua coastal gradient for half-day kayak and snorkel planning from St John's",
        css_only=True,
        breadcrumb="Half-day kayak",
        actions=_cta(
            "/antigua-kayak-snorkel-and-beach/",
            "Fuller kayak & beach guide",
            "/one-day-in-antigua-from-a-cruise-ship/",
            "One-day scenarios",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Framing", "Tighter / time-focused active water day"),
            ("Contrast", "Less beach-lounge emphasis than fuller combo pages"),
            ("Fitness", "Still moderate — paddling and swimming"),
            ("Ship clock", "Ask operators for real duration vs brochure labels"),
            ("This page", "Standalone editorial URL — not a redirect"),
        ]
    )

    main = f"""
{_prose('''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Half-day kayak-and-snorkel framings exist because not every cruise passenger wants a long beach
  finale after paddling and reef time. The useful question is not the marketing label “half day” —
  it is whether the operator’s real door-to-pier duration still leaves a conservative buffer for
  your sailing.
</p>
''' + snap)}
{_prose('''
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">How this differs from the primary kayak page</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  The
  <a href="/antigua-kayak-snorkel-and-beach/" class="text-ocean-600 font-semibold">Antigua kayak, snorkel and beach</a>
  guide emphasises the fuller combo shape: transfer, paddling, reef time and a more deliberate beach finish.
  This page stays tighter: prioritise water segments, clarify total hours, and decide whether a long lounge
  stop is worth the clock risk on your call.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  Both URLs remain live and distinct. Neither sells a tour here. Booking is not offered on this website yet —
  confirm operators independently, including fitness expectations and return timing.
</p>
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4 mt-10">Questions to ask any provider</h2>
<ul class="space-y-3 text-gray-600 leading-relaxed mb-6">
  <li>What is the typical total time from St John's pickup to drop-off?</li>
  <li>How much is kayaking vs boat/snorkel vs beach?</li>
  <li>What happens in choppy water or poor visibility?</li>
  <li>How do you handle cruise all-aboard windows?</li>
</ul>
''' + related_links([
    ("/antigua-kayak-snorkel-and-beach/", "Primary kayak guide"),
    ("/best-antigua-shore-excursions/", "Compare styles"),
    ("/antigua-port-guide/", "Port guide"),
    ("/contact/", "Contact"),
]), bg="bg-sand-50")}
{faq_section([
    (
        "Is half-day kayak the same as the full kayak page?",
        "No. This page focuses on shorter, time-sensitive framing. The primary kayak page covers "
        "the fuller kayak, snorkel and beach combo shape.",
    ),
    (
        "Can I book a half-day kayak here?",
        "Not in this phase. Editorial planning only — confirm operators independently.",
    ),
], heading="Half-day kayak FAQ")}
"""

    faqs: FaqList = [
        (
            "Is half-day kayak the same as the full kayak page?",
            "No. This page focuses on shorter, time-sensitive framing. The primary kayak page covers "
            "the fuller kayak, snorkel and beach combo shape.",
        ),
        (
            "Can I book a half-day kayak here?",
            "Not in this phase. Editorial planning only — confirm operators independently.",
        ),
    ]

    meta: Meta = {
        "title": "Antigua Half Day Kayak and Snorkel | Time-Focused Cruise Guide",
        "description": (
            "Editorial half-day kayak and snorkel guide for Antigua cruise passengers — "
            "tighter timing questions and how it differs from the fuller kayak-and-beach page."
        ),
        "canonical_path": "/antigua-half-day-kayak-and-snorkel/",
        "page_id": "half-day-kayak",
        "og_image": INTRO,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# PANORAMIC — use SHIRLEY image
# ---------------------------------------------------------------------------


def panoramic() -> PageTuple:
    hero = hero_band(
        eyebrow="Editorial scenic day",
        title_html=f'Panoramic Antigua<br/><span class="{ACCENT}">&amp; beach break</span>',
        lead=(
            "Viewpoints, coastal drives and a swim stop — a lighter scenic framing for St John's "
            "cruise passengers. Editorial planning only."
        ),
        image=SHIRLEY,
        aria_label=SHIRLEY_ALT,
        breadcrumb="Panoramic & beach",
        actions=_cta(
            "/shirley-heights-antigua-guide/",
            "Shirley Heights notes",
            "/classic-beach-day/",
            "Beach-focused alternative",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Theme", "Lookouts + beach break"),
            ("Best for", "Photography and lighter activity"),
            ("Trade-off", "Breadth over deep time at one site"),
            ("Often includes", "South-coast viewpoints when timing allows"),
            ("This page", "Editorial only — no booking on this site"),
        ]
    )

    main = f"""
{_section(f'''
<div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <div class="section-label">Scenic overview</div>
    <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-4">Island views without pretending you can see everything</h2>
    <p class="text-gray-600 leading-relaxed mb-4">
      A panoramic Antigua day typically strings together coastal roads and hilltop lookouts —
      Shirley Heights is a frequent highlight when included — then finishes with a beach break.
      It is built for passengers who want photographs and variety more than a long unsupervised swim
      morning or a museum-deep Dockyard visit.
    </p>
    <p class="text-gray-600 leading-relaxed mb-4">
      Because the route is scenic and multi-stop, exact viewpoints change with traffic and ship timing.
      Booking is not offered on this website yet; confirm any operator’s stop list independently.
    </p>
  </div>
  <div class="info-image rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{SHIRLEY}" alt="{SHIRLEY_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
</div>
''')}
{_section(snap, pad="pb-8 pt-0")}
{_prose('''
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Compare nearby styles</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  Want more heritage depth?
  <a href="/antigua-exclusive-history-and-culture-tour/" class="text-ocean-600 font-medium">History and culture</a>.
  Want swimming first?
  <a href="/classic-beach-day/" class="text-ocean-600 font-medium">Classic beach day</a>.
  Want countryside culture plus beach?
  <a href="/the-antiguan-experience/" class="text-ocean-600 font-medium">The Antiguan Experience</a>.
</p>
''' + related_links([
    ("/shirley-heights-antigua-guide/", "Shirley Heights"),
    ("/best-antigua-shore-excursions/", "Compare styles"),
    ("/one-day-in-antigua-from-a-cruise-ship/", "One day"),
    ("/contact/", "Contact"),
]), bg="bg-sand-50")}
{faq_section([
    (
        "Is panoramic Antigua good for first-timers?",
        "Often yes when the group wants views and a swim without committing to one deep heritage site. "
        "Confirm the stop list live.",
    ),
    (
        "Can I book this here?",
        "Not in this phase. Editorial planning only.",
    ),
], heading="Panoramic day FAQ")}
"""

    faqs: FaqList = [
        (
            "Is panoramic Antigua good for first-timers?",
            "Often yes when the group wants views and a swim without committing to one deep heritage site. "
            "Confirm the stop list live.",
        ),
        (
            "Can I book this here?",
            "Not in this phase. Editorial planning only.",
        ),
    ]

    meta: Meta = {
        "title": "Panoramic Antigua and Beach Break | Cruise Editorial Guide",
        "description": (
            "Editorial guide to panoramic Antigua and beach-break shore days from St John's — "
            "viewpoints, pacing and how it compares with beach-only or history days."
        ),
        "canonical_path": "/panoramic-antigua-and-beach-break/",
        "page_id": "panoramic",
        "og_image": SHIRLEY,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# SAFETY — careful, no guarantees
# ---------------------------------------------------------------------------


def safety() -> PageTuple:
    hero = hero_band(
        eyebrow="Practical awareness",
        title_html=f'Is Antigua safe<br/><span class="{ACCENT}">for cruise passengers?</span>',
        lead=(
            "Sensible, non-alarmist notes for St John's port days — crowded waterfronts, taxis, "
            "water activities and return timing. Not a guarantee and not a security certification."
        ),
        image=CRUISE_PORT,
        aria_label=CRUISE_PORT_ALT,
        breadcrumb="Safety",
        actions=_cta(
            "/antigua-port-guide/",
            "Port guide",
            "/can-you-explore-antigua-without-an-excursion/",
            "DIY planning",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Context", "Busy cruise harbour on port days"),
            ("Near pier", "Heritage Quay & Redcliffe Quay are heavily visited"),
            ("Transport", "Prefer licensed taxis; agree fares clearly"),
            ("Water time", "Follow guide instructions; respect conditions"),
            ("This page", "General awareness — not a safety guarantee"),
        ]
    )

    main = f"""
{_prose('''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Antigua is a well-visited Eastern Caribbean cruise stop. Many passengers move comfortably around
  St John's waterfront and on organised day trips. Comfort is not the same as a promise: petty theft
  can occur in crowded tourist areas anywhere, road conditions vary, and water sports carry inherent risk.
  Use normal travel judgement rather than treating any destination as risk-free.
</p>
''' + snap)}
{_section('''
<div class="grid md:grid-cols-2 gap-6">
  <article class="rounded-2xl border border-ocean-100 bg-white p-6">
    <h2 class="text-xl font-display font-bold text-gray-900 mb-3">St John's waterfront</h2>
    <p class="text-sm text-gray-600 leading-relaxed">
      Heritage Quay and Redcliffe Quay are busy when ships are in. Keep bags closed, phones secure,
      and be aware in market crowds. Walking near the harbour in daylight with shipmates is a common DIY plan —
      see the
      <a href="/can-you-explore-antigua-without-an-excursion/" class="text-ocean-600 font-medium">independent exploring guide</a>.
    </p>
  </article>
  <article class="rounded-2xl border border-ocean-100 bg-white p-6">
    <h2 class="text-xl font-display font-bold text-gray-900 mb-3">Taxis and transfers</h2>
    <p class="text-sm text-gray-600 leading-relaxed">
      Use licensed taxis from recognised port areas where possible. Agree the fare and return arrangement
      before departure. We do not invent official rate tables here — quotes change.
    </p>
  </article>
  <article class="rounded-2xl border border-ocean-100 bg-white p-6">
    <h2 class="text-xl font-display font-bold text-gray-900 mb-3">Organised days</h2>
    <p class="text-sm text-gray-600 leading-relaxed">
      Beach, heritage and kayak days still require sun protection, hydration and attention to briefings.
      Choose providers carefully and confirm how they handle timing — this site does not guarantee
      operator performance or ship returns.
    </p>
  </article>
  <article class="rounded-2xl border border-ocean-100 bg-white p-6">
    <h2 class="text-xl font-display font-bold text-gray-900 mb-3">Water activities</h2>
    <p class="text-sm text-gray-600 leading-relaxed">
      Snorkelling and kayaking depend on weather, swell and personal fitness. Follow guide instructions,
      use appropriate flotation if offered, and be honest about swimming ability. Reef-safe sunscreen habits
      help the environment; they do not remove ocean risk.
    </p>
  </article>
</div>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">What this page is not</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  It is not a crime-rate dashboard, medical advice, or an insurance policy. Conditions change.
  For official travel advice, consult your government’s guidance and your cruise line’s port notes.
  For planning logistics, start with the
  <a href="/antigua-port-guide/" class="text-ocean-600 font-medium">port guide</a>.
</p>
''' + related_links([
    ("/antigua-port-guide/", "Port guide"),
    ("/one-day-in-antigua-from-a-cruise-ship/", "One day"),
    ("/best-antigua-shore-excursions/", "Excursion styles"),
    ("/contact/", "Contact"),
]))}
{faq_section([
    (
        "Is Antigua safe for cruise passengers?",
        "Many passengers visit St John's and popular tour routes without incident when they use "
        "common-sense precautions. No destination is risk-free; stay aware and plan your return window.",
    ),
    (
        "Should I only take ship-sold tours?",
        "Ship tours and independent plans both have trade-offs. Decide based on timing confidence, "
        "group needs and provider reputation — we do not sell either here.",
    ),
], heading="Safety FAQ")}
"""

    faqs: FaqList = [
        (
            "Is Antigua safe for cruise passengers?",
            "Many passengers visit St John's and popular tour routes without incident when they use "
            "common-sense precautions. No destination is risk-free; stay aware and plan your return window.",
        ),
        (
            "Should I only take ship-sold tours?",
            "Ship tours and independent plans both have trade-offs. Decide based on timing confidence, "
            "group needs and provider reputation — we do not sell either here.",
        ),
    ]

    meta: Meta = {
        "title": "Is Antigua Safe for Cruise Passengers? | Practical Port Notes",
        "description": (
            "Practical safety awareness for Antigua cruise passengers in St John's — waterfront, "
            "taxis, water activities and return timing. General guidance, not a guarantee."
        ),
        "canonical_path": "/is-antigua-safe-for-cruise-passengers/",
        "page_id": "safety",
        "og_image": CRUISE_PORT,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# TRUST PAGES
# ---------------------------------------------------------------------------


def contact() -> PageTuple:
    hero = hero_band(
        eyebrow="Trust",
        title_html=f'Contact<br/><span class="{ACCENT}">{SITE}</span>',
        lead="Editorial questions about this Antigua cruise planning guide.",
        image=HERO_HOME,
        aria_label=HERO_HOME_ALT,
        breadcrumb="Contact",
    )
    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Email <a href="mailto:{EMAIL}" class="text-ocean-600 font-semibold">{EMAIL}</a>
  for questions about this independent guide. We do not process bookings, payments or shore-excursion
  checkouts on this website in the current phase.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  Please include your ship’s scheduled Antigua / St John's date if you are asking about planning logic —
  we still will not invent fees or guarantee operator inventory.
</p>
<p class="text-sm text-gray-500">Do not send payment card details by email.</p>
''')}
"""
    meta: Meta = {
        "title": f"Contact | {SITE}",
        "description": f"Contact {SITE} at {EMAIL} for editorial questions about this Antigua cruise planning guide.",
        "canonical_path": "/contact/",
        "page_id": "contact",
        "og_image": HERO_HOME,
    }
    return hero, main, None, meta


def about() -> PageTuple:
    hero = hero_band(
        eyebrow="Trust",
        title_html=f'About<br/><span class="{ACCENT}">{SITE}</span>',
        lead="Independent cruise-passenger planning for Antigua, from St John's.",
        image=INTRO,
        aria_label=INTRO_ALT,
        breadcrumb="About",
    )
    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  {SITE} helps cruise passengers decide what is genuinely practical from a St John's call —
  near-port beaches and waterfront walking, south-coast heritage at Nelson's Dockyard and Shirley Heights,
  kayak and reef days, and independent DIY options — without pretending every highlight fits every ship schedule.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  We are not a cruise line, not a pier operator, and not a booking marketplace in this phase.
</p>
<p class="text-gray-600 leading-relaxed">
  Read our <a href="/methodology/" class="text-ocean-600 font-medium">methodology</a>
  and <a href="/contact/" class="text-ocean-600 font-medium">contact</a> pages for how we work.
</p>
''')}
"""
    meta: Meta = {
        "title": f"About | {SITE}",
        "description": f"About {SITE} — an independent cruise passenger planning guide for Antigua from St John's.",
        "canonical_path": "/about/",
        "page_id": "about",
        "og_image": INTRO,
    }
    return hero, main, None, meta


def privacy() -> PageTuple:
    hero = hero_band(
        eyebrow="Legal",
        title_html=f'Privacy<br/><span class="{ACCENT}">policy</span>',
        lead="How this editorial website handles information.",
        image=HERO_HOME,
        aria_label=HERO_HOME_ALT,
        breadcrumb="Privacy",
    )
    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed mb-4">
  {SITE} is an editorial planning website. If you email us at
  <a href="mailto:{EMAIL}" class="text-ocean-600 font-medium">{EMAIL}</a>,
  we use your message only to respond. We do not sell personal information.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  Standard server and security logs may record technical data such as IP address, user agent and requested URLs.
  Analytics, if enabled by the hosting platform, may collect aggregated traffic statistics.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  This site does not operate a booking checkout in the current phase and does not ask for payment card details.
</p>
<p class="text-sm text-gray-500">Questions: <a href="mailto:{EMAIL}" class="text-ocean-600">{EMAIL}</a>.</p>
''')}
"""
    meta: Meta = {
        "title": f"Privacy Policy | {SITE}",
        "description": f"Privacy policy for {SITE} — how this Antigua cruise planning website handles information.",
        "canonical_path": "/privacy/",
        "page_id": "privacy",
        "og_image": HERO_HOME,
    }
    return hero, main, None, meta


def terms() -> PageTuple:
    hero = hero_band(
        eyebrow="Legal",
        title_html=f'Terms of<br/><span class="{ACCENT}">use</span>',
        lead="Editorial information only — not a booking contract.",
        image=HERO_HOME,
        aria_label=HERO_HOME_ALT,
        breadcrumb="Terms",
    )
    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed mb-4">
  Content on {SITE} is general planning information for cruise passengers. It is not a ticket,
  voucher, insurance policy or contract with any tour operator. Attraction access, road times and
  ship schedules change — confirm live details before you travel.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  We are not affiliated with cruise lines calling at St John's, Antigua. Mentions of beaches, harbours,
  lookouts or reef areas do not imply partnership.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  To the fullest extent permitted by law, we disclaim liability for decisions made solely on the basis
  of this website. Nothing here creates a consumer booking relationship.
</p>
<p class="text-sm text-gray-500">Contact: <a href="mailto:{EMAIL}" class="text-ocean-600">{EMAIL}</a>.</p>
''')}
"""
    meta: Meta = {
        "title": f"Terms of Use | {SITE}",
        "description": f"Terms of use for {SITE} — editorial cruise planning information, not a booking marketplace.",
        "canonical_path": "/terms/",
        "page_id": "terms",
        "og_image": HERO_HOME,
    }
    return hero, main, None, meta


def methodology() -> PageTuple:
    hero = hero_band(
        eyebrow="Trust",
        title_html=f'Methodology<br/><span class="{ACCENT}">&amp; sourcing</span>',
        lead="How we organise Antigua cruise-day guidance without inventing commercial claims.",
        image=INTRO,
        aria_label=INTRO_ALT,
        breadcrumb="Methodology",
    )
    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed mb-4">
  {SITE} prioritises cruise-passenger decisions: call length, transfer burden, and whether a stop
  sits in St John's local orbit or requires a longer south-coast or south-west commitment.
</p>
<ul class="space-y-3 text-gray-600 leading-relaxed mb-6">
  <li>Preserve equity URLs that already attract search interest, including independent DIY intent.</li>
  <li>Separate near-port options from longer transfers such as Nelson's Dockyard.</li>
  <li>Avoid unsupported guarantees, star ratings, inventing fees/hours, and public product codes.</li>
  <li>Keep commercial-shaped pages editorial until a later approved commerce phase.</li>
  <li>Use only live Antigua-location image assets; prefer CSS-only heroes where safe photos are unavailable.</li>
</ul>
<p class="text-gray-600 leading-relaxed">
  Softened wording (“often”, “roughly”, “confirm live”) marks uncertainty on minutes and berth details.
  See <a href="/about/" class="text-ocean-600 font-medium">about</a> and
  <a href="/contact/" class="text-ocean-600 font-medium">contact</a>.
</p>
''')}
"""
    meta: Meta = {
        "title": f"Methodology | {SITE}",
        "description": f"How {SITE} researches and organises Antigua cruise shore excursion planning guides.",
        "canonical_path": "/methodology/",
        "page_id": "methodology",
        "og_image": INTRO,
    }
    return hero, main, None, meta


def not_found() -> PageTuple:
    hero = ""
    main = f"""
<section class="pt-28 pb-24 bg-white">
  <div class="max-w-xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
    <p class="section-label justify-center">404</p>
    <h1 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-4">Page not found</h1>
    <p class="text-gray-600 leading-relaxed mb-8">
      That URL is not part of the {SITE} guide. Try the excursions hub or port guide.
    </p>
    <div class="flex flex-col sm:flex-row gap-3 justify-center">
      <a href="/" class="btn-ocean inline-flex items-center justify-center text-white font-semibold px-7 py-3 rounded-full text-sm">Home</a>
      <a href="/best-antigua-shore-excursions/" class="inline-flex items-center justify-center font-semibold px-7 py-3 rounded-full text-sm border border-ocean-200 text-ocean-700">Excursions</a>
      <a href="/antigua-port-guide/" class="inline-flex items-center justify-center font-semibold px-7 py-3 rounded-full text-sm border border-ocean-200 text-ocean-700">Port guide</a>
    </div>
  </div>
</section>
"""
    meta: Meta = {
        "title": f"Page not found | {SITE}",
        "description": f"The requested page was not found on {SITE}.",
        "canonical_path": "/404.html",
        "page_id": "not-found",
        "og_image": HERO_HOME,
    }
    return hero, main, None, meta
