"""Guide and home page content for Antigua Shore Excursion."""
from antigua_config import (
    ANTIGUAN_EXPERIENCE_ALT,
    ANTIGUAN_EXPERIENCE_IMG,
    BEACHES_ALT,
    BEACHES_IMG,
    BEST_ALT,
    BEST_IMG,
    CLASSIC_BEACH_ALT,
    CLASSIC_BEACH_IMG,
    HISTORY_CULTURE_ALT,
    HISTORY_CULTURE_IMG,
    INTRO_ALT,
    INTRO_IMG,
    KAYAK_SNORKEL_ALT,
    KAYAK_SNORKEL_IMG,
    NELSONS_DOCKYARD_ALT,
    NELSONS_DOCKYARD_IMG,
    PANORAMIC_ALT,
    PANORAMIC_IMG,
    PORT_ARRIVAL_ALT,
    PORT_ARRIVAL_IMG,
    PORT_ALT,
    PORT_IMG,
    SHIRLEY_HEIGHTS_ALT,
    SHIRLEY_HEIGHTS_IMG,
)
from antigua_helpers import (
    card_grid,
    comparison_section,
    internal_links,
    snapshot_default,
)


def content_home() -> str:
    featured = card_grid([
        (HISTORY_CULTURE_IMG, HISTORY_CULTURE_ALT, "History &amp; Culture Tour", "Nelson's Dockyard, Shirley Heights and Dow's Hill in a small-group format.", "antigua-exclusive-history-and-culture-tour.html", "History Tour"),
        (CLASSIC_BEACH_IMG, CLASSIC_BEACH_ALT, "Classic Beach Day", "White sand, turquoise water and a stress-free beach escape.", "classic-beach-day.html", "Beach Day"),
        (KAYAK_SNORKEL_IMG, KAYAK_SNORKEL_ALT, "Kayak &amp; Snorkel", "Mangroves, Cades Reef and beach on one adventure combo.", "antigua-kayak-snorkel-and-beach.html", "Kayak Tour"),
        (ANTIGUAN_EXPERIENCE_IMG, ANTIGUAN_EXPERIENCE_ALT, "The Antiguan Experience", "Countryside drive, pineapple farm and beach finale.", "the-antiguan-experience.html", "Culture Tour"),
    ])
    best_cards = card_grid([
        (HISTORY_CULTURE_IMG, HISTORY_CULTURE_ALT, "History &amp; Culture", "Nelson's Dockyard and Shirley Heights — Antigua's UNESCO heritage.", "antigua-exclusive-history-and-culture-tour.html", "History"),
        (CLASSIC_BEACH_IMG, CLASSIC_BEACH_ALT, "Classic Beach Day", "Antigua's signature white-sand beach day from St John's.", "classic-beach-day.html", "Beach"),
        (KAYAK_SNORKEL_IMG, KAYAK_SNORKEL_ALT, "Kayak &amp; Snorkel", "Cades Bay mangroves and Cades Reef snorkelling.", "antigua-kayak-snorkel-and-beach.html", "Adventure"),
        (PANORAMIC_IMG, PANORAMIC_ALT, "Panoramic &amp; Beach", "Island viewpoints plus a relaxed beach break.", "panoramic-antigua-and-beach-break.html", "Scenic"),
    ])
    snap = snapshot_default()
    return f"""<section class="pt-8 pb-8 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="text-center mb-10">
    <div class="section-label mx-auto">Best Excursions</div>
    <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-4">Best Antigua Shore Excursions</h2>
    <p class="text-gray-600 text-sm max-w-2xl mx-auto">Ranked for cruise schedules — beach days, Nelson's Dockyard history, kayak snorkel adventures and scenic island drives across Antigua and Barbuda from St John's.</p>
  </div>
  {best_cards}
  <p class="text-center mt-8"><a href="best-antigua-shore-excursions.html" class="text-ocean-600 font-semibold text-sm">See full comparison →</a></p>
</div></section>
<section class="pt-4 pb-8 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div>
    <div class="inline-flex items-center gap-2 text-ocean-600 text-xs font-semibold tracking-widest uppercase mb-3"><div class="w-8 h-px bg-ocean-400"></div>St John's Cruise Port</div>
    <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-5">Why Cruise Passengers<br/><span class="text-ocean-600">Choose Antigua</span></h2>
    <p class="text-gray-600 leading-relaxed mb-5">Antigua offers <strong>365 beaches</strong>, UNESCO-listed Nelson's Dockyard, Shirley Heights panoramas and world-class snorkelling — all reachable on a typical <strong>6–10 hour</strong> port call from St John's. Eastern Caribbean dollars (XCD) are official; <strong>USD</strong> is widely accepted at tourist businesses.</p>
    <a href="antigua-port-guide.html" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm shadow-lg">Port Guide</a>
  </div>
  <div class="info-image rounded-3xl aspect-[4/3] shadow-2xl overflow-hidden">
    <img src="{INTRO_IMG}" alt="{INTRO_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="py-16 bg-amber-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="text-center mb-12"><h2 class="text-3xl font-display font-bold text-gray-900">Featured Excursions</h2>
  <p class="text-gray-600 text-sm mt-3 max-w-xl mx-auto">Most-booked shore excursions for Antigua cruise passengers from St John's.</p></div>
  {featured}
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl font-display font-bold text-gray-900 text-center mb-10">Top Things To Do In Antigua</h2>
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 text-sm">
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Nelson's Dockyard</h3><p class="text-gray-600">UNESCO World Heritage Georgian naval dockyard in English Harbour — Antigua's premier history site.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Shirley Heights</h3><p class="text-gray-600">Historic lookout with sweeping views over English Harbour and Falmouth Bay.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Beach Days</h3><p class="text-gray-600">White sand and calm turquoise water at Dickenson Bay, Hawksbill and south-coast coves.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Kayak &amp; Snorkel</h3><p class="text-gray-600">Mangrove lagoons and Cades Reef — Antigua's signature active shore excursion.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">St John's Waterfront</h3><p class="text-gray-600">Heritage Quay, Redcliffe Quay and colourful harbour streets within walking distance of the pier.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Island Culture</h3><p class="text-gray-600">Pineapple farms, fishing villages and scenic drives through Antigua's countryside.</p></div>
  </div>
</div></section>
<section class="py-16 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{NELSONS_DOCKYARD_IMG}" alt="{NELSONS_DOCKYARD_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
  <div>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Nelson's Dockyard &amp; Shirley Heights</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Nelson's Dockyard in English Harbour is a restored 18th-century naval base and UNESCO World Heritage site — about <strong>12 miles / 30–45 minutes</strong> south of St John's cruise port. Shirley Heights overlooks the harbour from Dow Hill with panoramic Caribbean views.</p>
    <p class="text-gray-600 leading-relaxed mb-5">The <a href="antigua-exclusive-history-and-culture-tour.html" class="text-ocean-600 font-medium">Exclusive History and Culture Tour</a> covers both in a small-group format. Read our <a href="nelsons-dockyard-from-antigua-cruise-port.html" class="text-ocean-600 font-medium">Nelson's Dockyard guide</a> and <a href="shirley-heights-antigua-guide.html" class="text-ocean-600 font-medium">Shirley Heights guide</a> for distances and tips.</p>
    <a href="antigua-exclusive-history-and-culture-tour.html" class="text-ocean-600 font-semibold text-sm">History &amp; Culture tour →</a>
  </div>
</div></div></section>
<section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Kayak &amp; Snorkel Adventures</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Antigua's south-west coast offers mangrove lagoon kayaking and snorkelling at <strong>Cades Reef</strong> — a barrier reef system with clear water and abundant marine life. Tours depart from St John's with transport to Cades Bay, about <strong>45–60 minutes</strong> from the cruise port.</p>
    <p class="text-gray-600 leading-relaxed mb-5">Compare the full <a href="antigua-kayak-snorkel-and-beach.html" class="text-ocean-600 font-medium">Kayak, Snorkel and Beach</a> combo with the compact <a href="antigua-half-day-kayak-and-snorkel.html" class="text-ocean-600 font-medium">Half Day Kayak and Snorkel</a> tour.</p>
    <a href="antigua-kayak-snorkel-and-beach.html" class="text-ocean-600 font-semibold text-sm">Kayak &amp; snorkel tours →</a>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{KAYAK_SNORKEL_IMG}" alt="{KAYAK_SNORKEL_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="py-16 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{BEACHES_IMG}" alt="{BEACHES_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
  <div>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Best Beaches For Cruise Passengers</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Dickenson Bay and Hawksbill beaches sit within <strong>15–20 minutes</strong> of St John's — ideal for short independent visits or organised beach days. South-coast coves reached on excursions offer quieter white sand with calm swimming.</p>
    <p class="text-gray-600 leading-relaxed mb-5">The <a href="classic-beach-day.html" class="text-ocean-600 font-medium">Classic Beach Day</a> excursion handles transport, loungers and lunch. See our <a href="best-beaches-in-antigua-for-cruise-passengers.html" class="text-ocean-600 font-medium">beach guide</a> for distances from the cruise port.</p>
    <a href="classic-beach-day.html" class="text-ocean-600 font-semibold text-sm">Classic Beach Day →</a>
  </div>
</div></div></section>
{comparison_section()}
{home_faq_section()}
<section class="py-16 cta-gradient"><div class="max-w-3xl mx-auto px-4 text-center">
  <h2 class="text-3xl font-display font-bold text-white mb-4">Plan Your Antigua Port Day</h2>
  <p class="text-white/85 text-sm mb-6">Compare excursions, read the St John's port guide and build your Antigua itinerary before you dock in Antigua and Barbuda.</p>
  <div class="flex flex-col sm:flex-row gap-4 justify-center">
    <a href="best-antigua-shore-excursions.html" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Compare Excursions</a>
    <a href="antigua-port-guide.html" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Port Guide</a>
  </div>
</div></section>"""


def home_faq_section() -> str:
    return """<section class="py-16 bg-white"><div class="max-w-3xl mx-auto px-4">
  <h2 class="text-3xl font-display font-bold text-gray-900 text-center mb-8">Antigua Shore Excursions FAQ</h2>
  <div class="space-y-4">
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Where is the Antigua cruise port?</summary>
      <p class="mt-4 text-sm text-gray-500">Ships dock at St John's on Antigua's north-west coast — Heritage Quay and Redcliffe Quay terminals are in the capital's harbour. Downtown St John's is walkable from the pier.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">How far is Nelson's Dockyard from the cruise port?</summary>
      <p class="mt-4 text-sm text-gray-500">Nelson's Dockyard in English Harbour is approximately 12 miles (19 km) south of St John's — expect 30–45 minutes by tour bus or taxi on winding coastal roads.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">How far are beaches from St John's cruise port?</summary>
      <p class="mt-4 text-sm text-gray-500">Dickenson Bay and Hawksbill beaches are 3–5 miles north-west — about 10–20 minutes by taxi. South-coast beaches on excursions are 30–60 minutes depending on the route.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">How long do cruise ships stay in Antigua?</summary>
      <p class="mt-4 text-sm text-gray-500">Most St John's port calls are 6 to 10 hours. History tours and beach days need 4–5 hours; kayak snorkel combos fit comfortably within a full day ashore.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">What currency is used in Antigua?</summary>
      <p class="mt-4 text-sm text-gray-500">Eastern Caribbean dollars (XCD) are official, pegged to USD. US dollars are widely accepted — carry small bills for taxis and tips.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Can I explore Antigua without an excursion?</summary>
      <p class="mt-4 text-sm text-gray-500">Yes — St John's waterfront, Heritage Quay shops and nearby beaches are reachable by taxi or on foot. Nelson's Dockyard and Cades Reef need organised transport. See our <a href="can-you-explore-antigua-without-an-excursion.html" class="text-ocean-600">without excursion guide</a>.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Is Antigua safe for cruise passengers?</summary>
      <p class="mt-4 text-sm text-gray-500">St John's is heavily visited by cruise guests. Organised excursions to beaches, Nelson's Dockyard and snorkel sites are standard and well managed. See our <a href="is-antigua-safe-for-cruise-passengers.html" class="text-ocean-600">safety guide</a>.</p></details>
  </div>
</div></section>"""


def home_faq_data() -> list[tuple[str, str]]:
    return [
        ("Where is the Antigua cruise port?", "St John's harbour — Heritage Quay and Redcliffe Quay terminals."),
        ("How far is Nelson's Dockyard from the cruise port?", "Approximately 12 miles, 30–45 minutes by road."),
        ("How far are beaches from St John's cruise port?", "Nearest beaches 10–20 minutes; excursion beaches 30–60 minutes."),
        ("How long do cruise ships stay in Antigua?", "Most port calls are 6 to 10 hours."),
        ("What currency is used in Antigua?", "Eastern Caribbean dollars official; USD widely accepted."),
        ("Can I explore Antigua without an excursion?", "Yes in St John's; farther sites need transport."),
        ("Is Antigua safe for cruise passengers?", "Heavily touristed; organised tours recommended for off-port sites."),
    ]


def content_best_excursions() -> str:
    snap = snapshot_default(best_for="Comparing all excursion types", popular="See comparison table below")
    rankings = """<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Excursions by Traveler Type</h2>
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 text-sm">
    <div class="bg-sand-50 rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Families</h3><p class="text-gray-600 mb-3">Classic Beach Day, Panoramic Antigua and History &amp; Culture tours suit mixed ages.</p><a href="classic-beach-day.html" class="text-ocean-600 font-semibold">Beach Day →</a></div>
    <div class="bg-sand-50 rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Couples</h3><p class="text-gray-600 mb-3">Panoramic &amp; Beach Break, Antiguan Experience and History &amp; Culture small-group tours.</p><a href="panoramic-antigua-and-beach-break.html" class="text-ocean-600 font-semibold">Panoramic Tour →</a></div>
    <div class="bg-sand-50 rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">First Timers</h3><p class="text-gray-600 mb-3">The Antiguan Experience and Exclusive History &amp; Culture cover island highlights.</p><a href="the-antiguan-experience.html" class="text-ocean-600 font-semibold">Antiguan Experience →</a></div>
    <div class="bg-ocean-50 rounded-3xl p-6 border border-ocean-100"><h3 class="font-display font-bold text-lg mb-2">Adventure</h3><p class="text-gray-600 mb-3">Kayak Snorkel &amp; Beach and Half Day Kayak &amp; Snorkel at Cades Reef.</p><a href="antigua-kayak-snorkel-and-beach.html" class="text-ocean-600 font-semibold">Kayak &amp; Snorkel →</a></div>
    <div class="bg-ocean-50 rounded-3xl p-6 border border-ocean-100"><h3 class="font-display font-bold text-lg mb-2">Beach Lovers</h3><p class="text-gray-600 mb-3">Classic Beach Day and Panoramic Antigua with beach break.</p><a href="classic-beach-day.html" class="text-ocean-600 font-semibold">Classic Beach →</a></div>
    <div class="bg-ocean-50 rounded-3xl p-6 border border-ocean-100"><h3 class="font-display font-bold text-lg mb-2">History &amp; Culture</h3><p class="text-gray-600 mb-3">Exclusive History &amp; Culture — Nelson's Dockyard and Shirley Heights.</p><a href="antigua-exclusive-history-and-culture-tour.html" class="text-ocean-600 font-semibold">History Tour →</a></div>
  </div>
</div></section>"""
    cards = card_grid([
        (HISTORY_CULTURE_IMG, HISTORY_CULTURE_ALT, "History &amp; Culture", "Nelson's Dockyard and Shirley Heights small-group tour.", "antigua-exclusive-history-and-culture-tour.html", "History"),
        (CLASSIC_BEACH_IMG, CLASSIC_BEACH_ALT, "Classic Beach Day", "White sand beach escape with lunch included.", "classic-beach-day.html", "Beach"),
        (KAYAK_SNORKEL_IMG, KAYAK_SNORKEL_ALT, "Kayak &amp; Snorkel", "Mangroves, Cades Reef and beach combo.", "antigua-kayak-snorkel-and-beach.html", "Adventure"),
        (ANTIGUAN_EXPERIENCE_IMG, ANTIGUAN_EXPERIENCE_ALT, "Antiguan Experience", "Culture, pineapple farm and beach.", "the-antiguan-experience.html", "Culture"),
    ])
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Best Antigua Shore Excursions</h2>
  <p class="text-gray-600 leading-relaxed text-sm">Operators meet at the <strong>St John's cruise terminal</strong> in Antigua and Barbuda and plan returns with buffer before all aboard on your Caribbean cruise.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
{comparison_section()}
{rankings}
<section class="py-16 bg-white"><div class="max-w-7xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Excursion Guides</h2>
  {cards}
  <div class="mt-12 max-w-3xl mx-auto">{internal_links()}</div>
</div></section>"""


def content_port_guide() -> str:
    snap = snapshot_default(activity_level="Low in town; moderate on tours", popular="Taxis, tour pickups, waterfront walking")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
  <p class="text-gray-600 leading-relaxed text-sm">Ships dock at <strong>St John's</strong>, the capital of Antigua and Barbuda — a compact Caribbean harbour city with Heritage Quay and Redcliffe Quay cruise terminals on a typical <strong>6–10 hour</strong> call.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-7xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-8">St John's Antigua Cruise Port Location</h2>
  <div class="info-image rounded-3xl aspect-[21/9] shadow-xl overflow-hidden mb-8 max-w-5xl mx-auto">
    <img src="{PORT_ARRIVAL_IMG}" alt="{PORT_ARRIVAL_ALT}" width="1200" height="514" loading="lazy" decoding="async" />
  </div>
  <div class="grid lg:grid-cols-3 gap-6 text-sm">
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Where Is the Port?</h3><p class="text-gray-600">St John's harbour on Antigua's north-west coast. Heritage Quay and Redcliffe Quay serve major cruise lines with duty-free shopping and waterfront dining steps from the gangway.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Walking St John's</h3><p class="text-gray-600">Heritage Quay, Redcliffe Quay, the public market and St John's Cathedral are walkable from the pier. Allow 1–2 hours for a self-guided harbour stroll.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Tour Pickups</h3><p class="text-gray-600">Shore excursion operators meet at the cruise terminal or designated pickup zones. Taxis queue near the port exit — agree fares before departing.</p></div>
  </div>
</div></section>
<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Practical Port Day Info</h2>
  <div class="grid sm:grid-cols-3 gap-6 text-sm">
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Distance to Nelson's Dockyard</strong><p class="mt-2 text-gray-600">~12 miles / <strong>30–45 min</strong> south to English Harbour.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Distance to Dickenson Bay</strong><p class="mt-2 text-gray-600">~3 miles / <strong>10–15 min</strong> north-west — nearest popular beach.</p></div>
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Currency</strong><p class="mt-2 text-gray-600">Eastern Caribbean dollars (XCD). <strong>USD</strong> accepted — carry small bills for taxis and tips.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Taxis</strong><p class="mt-2 text-gray-600">Licensed taxis at the port — negotiate round-trip fares. Fixed-route buses are cheaper but slower.</p></div>
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Return Timing</strong><p class="mt-2 text-gray-600">Allow <strong>60–90 minutes</strong> before all aboard. Shore excursions build buffer; independent guests track ship time carefully.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Weather</strong><p class="mt-2 text-gray-600">Tropical year-round, 77–88°F typical. Rainy season July–November; morning tours avoid afternoon showers.</p></div>
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Safety</strong><p class="mt-2 text-gray-600">St John's waterfront is heavily touristed. See our <a href="is-antigua-safe-for-cruise-passengers.html" class="text-ocean-600 font-medium">safety guide</a>.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Cades Reef</strong><p class="mt-2 text-gray-600">~45–60 min south-west — kayak and snorkel excursion destination.</p></div>
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Few Hours Only?</strong><p class="mt-2 text-gray-600">Walk St John's waterfront or taxi to Dickenson Bay for a quick beach visit.</p></div>
  </div>
  <p class="text-center mt-8"><a href="one-day-in-antigua-from-a-cruise-ship.html" class="text-ocean-600 font-semibold text-sm">One-day itinerary →</a> · <a href="best-antigua-shore-excursions.html" class="text-ocean-600 font-semibold text-sm">Compare excursions →</a></p>
  <div class="mt-10 max-w-3xl mx-auto">{internal_links()}</div>
</div></section>"""


def content_one_day() -> str:
    snap = snapshot_default(best_for="Morning history or culture + afternoon beach")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
  <p class="text-gray-600 text-sm">Sample timeline for a <strong>6–10 hour</strong> St John's port call. Adjust for your ship's actual gangway and all-aboard times.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-3xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Classic Antigua Port Day</h2>
  <ol class="space-y-4 text-sm">
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">08:00</span><div><strong>Depart pier</strong><p class="text-gray-600 mt-1">Meet history tour or Antiguan Experience — morning departures avoid afternoon heat and rain.</p></div></li>
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">09:30</span><div><strong>Main activity</strong><p class="text-gray-600 mt-1">Nelson's Dockyard and Shirley Heights, or countryside drive with pineapple farm visit.</p></div></li>
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">12:30</span><div><strong>Lunch</strong><p class="text-gray-600 mt-1">Included on most tours, or dine at a St John's waterfront restaurant between activities.</p></div></li>
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">14:00</span><div><strong>Beach or harbour</strong><p class="text-gray-600 mt-1">Classic Beach Day loungers if on a beach tour, or return to Heritage Quay for shopping.</p></div></li>
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">16:30</span><div><strong>Return toward ship</strong><p class="text-gray-600 mt-1">Tour transfer or taxi to terminal — allow margin before all aboard.</p></div></li>
  </ol>
  <div class="mt-8 bg-white rounded-2xl p-6 border border-pr-100">
    <h3 class="font-display font-bold text-lg mb-3">Suggested Excursions</h3>
    <ul class="space-y-2 text-sm text-gray-600">
      <li><a href="antigua-exclusive-history-and-culture-tour.html" class="text-ocean-600 font-medium">History &amp; Culture Tour</a> — best for Nelson's Dockyard and Shirley Heights</li>
      <li><a href="the-antiguan-experience.html" class="text-ocean-600 font-medium">The Antiguan Experience</a> — culture and beach for first-timers</li>
      <li><a href="classic-beach-day.html" class="text-ocean-600 font-medium">Classic Beach Day</a> — relaxed sun and swim</li>
    </ul>
  </div>
  <div class="mt-10">{internal_links()}</div>
</div></section>"""


def content_beaches_guide() -> str:
    snap = snapshot_default(best_for="Choosing a beach near St John's", popular="Dickenson Bay, Hawksbill, excursion beaches")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <p class="text-gray-600 leading-relaxed mb-6">Antigua claims 365 beaches — one for every day of the year. For cruise passengers docking at St John's, Dickenson Bay and Hawksbill are the closest popular choices within 10–20 minutes. Organised beach excursions reach quieter south-coast coves with white sand and calm turquoise water.</p>
    <ul class="space-y-3 mb-6 text-sm text-gray-600">
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Dickenson Bay</strong> — ~3 miles / 10–15 min. Calm water, beach bars. Taxi from port.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Hawksbill (Four Beaches)</strong> — ~4 miles / 15 min. Multiple coves near Five Islands.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Excursion beaches</strong> — <a href="classic-beach-day.html" class="text-ocean-600">Classic Beach Day</a> includes transport and lunch.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Return timing:</strong> Beach tours include 60–90 min ship buffer.</li>
    </ul>
    <a href="classic-beach-day.html" class="text-ocean-600 font-semibold text-sm">Classic Beach Day excursions →</a>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{BEACHES_IMG}" alt="{BEACHES_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{internal_links([("panoramic-antigua-and-beach-break.html", "Panoramic &amp; Beach")])}</div></section>"""


def content_nelsons_dockyard_guide() -> str:
    snap = snapshot_default(best_for="Planning a Nelson's Dockyard visit", popular="History tours, English Harbour, UNESCO site")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <p class="text-gray-600 leading-relaxed mb-6">Nelson's Dockyard is a restored Georgian naval facility in English Harbour and the centrepiece of Nelson's Dockyard National Park — a UNESCO World Heritage site. Named for Admiral Horatio Nelson, who was stationed in Antigua in the 1780s, it is the only surviving Georgian dockyard in the world and Antigua's must-see history attraction.</p>
    <ul class="space-y-3 mb-6 text-sm text-gray-600">
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Distance from St John's:</strong> ~12 miles / 30–45 min by bus or taxi</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Entry:</strong> National park fee covers Dockyard, Shirley Heights and Dow's Hill</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Highlights:</strong> Naval museum, marina, restored buildings, Fort Berkeley trail</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Best tour:</strong> <a href="antigua-exclusive-history-and-culture-tour.html" class="text-ocean-600">Exclusive History &amp; Culture</a></li>
    </ul>
    <a href="antigua-exclusive-history-and-culture-tour.html" class="btn-ocean inline-flex items-center text-white font-semibold px-6 py-3 rounded-full text-sm">History Tour</a>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{NELSONS_DOCKYARD_IMG}" alt="{NELSONS_DOCKYARD_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{internal_links([("shirley-heights-antigua-guide.html", "Shirley Heights")])}</div></section>"""


def content_shirley_heights_guide() -> str:
    snap = snapshot_default(best_for="Shirley Heights lookout and views", popular="History tours, Sunday BBQ, English Harbour panorama")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <p class="text-gray-600 leading-relaxed mb-6">Shirley Heights is a historic military compound on Dow Hill overlooking English Harbour — built in the 1780s to protect the naval dockyard below. Today it offers Antigua's most celebrated panoramic views across Falmouth Harbour, English Harbour and the Caribbean Sea. It is part of Nelson's Dockyard National Park and included on most history shore excursions from St John's.</p>
    <ul class="space-y-3 mb-6 text-sm text-gray-600">
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Distance from St John's:</strong> ~12 miles / 30–45 min (same route as Nelson's Dockyard)</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Lookout:</strong> Short walk from parking to the main viewpoint</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Sunday BBQ:</strong> Famous sunset party with live steel band (not on cruise days)</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Best tour:</strong> <a href="panoramic-antigua-and-beach-break.html" class="text-ocean-600">Panoramic Antigua</a> or <a href="antigua-exclusive-history-and-culture-tour.html" class="text-ocean-600">History &amp; Culture</a></li>
    </ul>
    <a href="antigua-exclusive-history-and-culture-tour.html" class="btn-ocean inline-flex items-center text-white font-semibold px-6 py-3 rounded-full text-sm">History Tour</a>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{SHIRLEY_HEIGHTS_IMG}" alt="{SHIRLEY_HEIGHTS_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{internal_links([("nelsons-dockyard-from-antigua-cruise-port.html", "Nelson's Dockyard")])}</div></section>"""


def content_safety() -> str:
    snap = snapshot_default(best_for="Understanding Antigua safety", activity_level="N/A")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4">
  <p class="text-gray-600 leading-relaxed text-sm mb-6">Antigua is one of the Caribbean's most visited cruise destinations. St John's waterfront and organised shore excursions to beaches, Nelson's Dockyard and snorkel sites are heavily touristed. Cruise passengers generally report safe, welcoming experiences when using licensed taxis and reputable tour operators.</p>
  <div class="space-y-4 text-sm">
    <div class="bg-sand-50 rounded-2xl p-5 border border-pr-100"><h3 class="font-display font-bold mb-2">St John's Waterfront</h3><p class="text-gray-600">Heritage Quay and Redcliffe Quay are busy with cruise guests during port days. Stay aware of belongings in crowded market areas.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-5 border border-ocean-100"><h3 class="font-display font-bold mb-2">Excursions</h3><p class="text-gray-600">Book through reputable operators with return-to-ship guarantees. Kayak and snorkel tours provide safety equipment and trained guides.</p></div>
    <div class="bg-sand-50 rounded-2xl p-5 border border-pr-100"><h3 class="font-display font-bold mb-2">Taxis &amp; Transport</h3><p class="text-gray-600">Use licensed taxis at the port. Agree fares before departing; avoid unlicensed offers outside designated areas.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-5 border border-ocean-100"><h3 class="font-display font-bold mb-2">Water Activities</h3><p class="text-gray-600">Wear reef-safe sunscreen. Snorkel only with guides at Cades Reef. Monitor weather during rainy season (July–November).</p></div>
  </div>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{internal_links()}</div></section>"""


def content_without_excursion() -> str:
    snap = snapshot_default(best_for="Self-guided St John's and short beach visits", activity_level="Low to moderate")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4">
  <p class="text-gray-600 leading-relaxed text-sm mb-6">Yes — you can enjoy Antigua without a booked shore excursion. St John's harbour, Heritage Quay shopping, Redcliffe Quay and nearby beaches are reachable on foot or by taxi. Nelson's Dockyard, Shirley Heights and Cades Reef need organised transport or a rental vehicle.</p>
  <div class="space-y-4 text-sm">
    <div class="bg-sand-50 rounded-2xl p-5 border border-pr-100"><h3 class="font-display font-bold mb-2">Few Hours Only</h3><p class="text-gray-600">Walk Heritage Quay and Redcliffe Quay, browse duty-free shops and grab lunch on the waterfront — all within minutes of the gangway.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-5 border border-ocean-100"><h3 class="font-display font-bold mb-2">Taxi to Dickenson Bay</h3><p class="text-gray-600">Negotiate round-trip from the port — 10–15 min to Antigua's nearest popular beach. Confirm return pickup before all aboard.</p></div>
    <div class="bg-sand-50 rounded-2xl p-5 border border-pr-100"><h3 class="font-display font-bold mb-2">When Book a Tour</h3><p class="text-gray-600">Nelson's Dockyard, kayak snorkel combos and south-coast beaches need organised transport, guides and timing aligned to your ship.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-5 border border-ocean-100"><h3 class="font-display font-bold mb-2">Public Bus</h3><p class="text-gray-600">Bus 17 runs toward Nelson's Dockyard from West Bus Station (~1 km from port) — budget option for independent travellers with time.</p></div>
  </div>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{internal_links()}</div></section>"""


def all_guide_content() -> dict[str, str]:
    return {
        "home.html": content_home(),
        "best-antigua-shore-excursions.html": content_best_excursions(),
        "antigua-port-guide.html": content_port_guide(),
        "one-day-in-antigua-from-a-cruise-ship.html": content_one_day(),
        "best-beaches-in-antigua-for-cruise-passengers.html": content_beaches_guide(),
        "nelsons-dockyard-from-antigua-cruise-port.html": content_nelsons_dockyard_guide(),
        "shirley-heights-antigua-guide.html": content_shirley_heights_guide(),
        "is-antigua-safe-for-cruise-passengers.html": content_safety(),
        "can-you-explore-antigua-without-an-excursion.html": content_without_excursion(),
    }
