# The Brickyard — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** The Brickyard
- **Slug:** `the-brickyard`
- **Audit Grade / Disposition / Score:** A / YES / 99
- **Audit Batch:** 22
- **Verification Date:** August 24, 2026

## Verification Sources

- [Instagram — @thebrickyardclt](https://www.instagram.com/thebrickyardclt/) (owned account; bio carries hours, phone, email, and the "NEVER a cover, ALWAYS a crowd!" tagline)
- [Facebook — The Brickyard Charlotte](https://www.facebook.com/thebrickyardclt/) (owned page; "Neighborhood bar and live music joint. TVs for viewing all sporting events. Rooftop bar and patio")
- [South End Charlotte directory — The Brickyard](https://southendclt.org/go/the-brickyard) (neighborhood business directory: address, rooftop bar, patio, game-day TVs, live music venue description)
- [Yelp — The Brickyard](https://www.yelp.com/biz/the-brickyard-charlotte-2) (address, full weekly hours)
- [Checkle — The Brickyard menu](https://www.checkle.com/biz/the-brickyard-charlotte/menu) (bar menu items transcribed from house menu photos, October 2025)
- [Restaurantji — The Brickyard](https://www.restaurantji.com/nc/charlotte/the-brickyard-) (hours, contact, service attributes including "doesn't accept reservations")
- [Four Dollar Jacks — The Brickyard](https://www.fourdollarjacks.com/bars-near-me/the-brickyard-on-south-tryon-street) (aggregated kitchen menu items and operating hours)

## Original Audit Weakness

The Brickyard has **no owned website**. Its South End directory listing routes "visit website" to Facebook. Identity, hours, and contact live entirely in social bios, while directories disagree with each other: Yelp shows (980) 406-3709 while the owned Instagram bio shows 980-938-6990, and Sunday opening time varies between noon and 2 PM depending on the listing. There is no readable menu anywhere online, no single canonical place that answers "where do I park, when are you open, what's pouring." The demo demonstrates one authoritative owned hub that resolves identity, hours, menu, music, and rooftop information in one place.

## Creative Brief

### Verified Visual / Content Anchors

1. **The no-cover rallying cry** — the owned tagline "NEVER a cover, ALWAYS a crowd!" with a trademark mark, printed on the Instagram bio. It is the loudest brand asset the business owns.
2. **Brick-and-mortar honesty of 1411 S Tryon** — a storefront bar on South Tryon in South End, steps from Amos' South End and directly across from the RailYard complex (per South End Charlotte directory distance data).
3. **Rooftop bar + street patio + game-day wall of TVs** — the venue's three physical spaces, described consistently by the owned Facebook page and the South End Charlotte directory.
4. **Late-night dive cadence** — closed Monday/Tuesday, doors from 5 PM Wednesday through Friday, 2 PM weekends, running until 2 AM; the weekend afternoon-to-2AM arc is distinctive.
5. **A working-class drinks list** — Miller Lite, High Life, Pacifico, Wicked Weed on draft, Fireball shots, vodka-Red Bull (transcribed from house menu photos on Checkle).

### Core Design Moves

1. **Gig-poster marquee architecture** — the homepage is composed like layered show posters stapled to painted brick: slightly rotated poster panels, staple dots, torn-edge ticket stubs, and a scrolling no-cover ticker instead of a conventional centered hero. No other recent demo uses poster-collage layering.
2. **Brick-bond typographic system** — Anton display capitals set like marquee letters over a CSS-drawn running-bond brick coursing motif; Barlow Condensed is used for wayfinding-style labels ("DOORS," "KITCHEN," "ROOFTOP"), giving every page the feel of hand-painted bar signage rather than a website template.
3. **Ticket-stub information units** — practical facts (hours, address, phone) are presented as perforated ticket stubs and scoreboard numerals ("5PM → 2AM"), and the menu is laid out as a chalk board with dot leaders, reflecting how the bar actually posts its menu photos.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `midtown-tavern` — industrial split-hero (badge left, framed photo right), Outfit/Plus Jakarta Sans, copper-bronze card grids.
2. `mert-s-heart-and-soul` — Charleston-porch serif warmth, Playfair Display, mahogany/gold alternating two-column sections.
3. `medusa-lounge` — obsidian-black luxury lounge, Cormorant Garamond, centered glow-hero with gold accents.
4. `medellin-colombian-restaurant` — emerald hacienda editorial, Playfair Display, large framed imagery and centered card rows.
5. `mas-tortilleria` — market-fresh layout with warm neutrals and standard stacked feature cards.

### Dominant Pattern Being Avoided

All five reduce to some version of: full-bleed or split hero → centered headline → pill buttons → 3-up feature card grid → alternating image/text bands → generic footer.

### Divergent Choices for The Brickyard

- **Primary hero composition:** a staggered, overlapping *poster-wall collage* (rotated panels with staple/tape detailing) plus a continuous scrolling ticker — not a single hero banner, not a split hero.
- **Section rhythm:** asymmetric "fly-poster" clusters and ticket-stub strips replace uniform card grids; each page uses a different structural skeleton (chalk board, stage sheet, rooftop skyline spread, numbered manifesto).
- **Typography system:** Anton + Barlow Condensed + Barlow — heavy marquee capitals and transit-signage labels, replacing the serif-luxury and geometric-humanist systems used by the five demos above.
- **Major page composition divergence:** `menu.html` is composed as one continuous chalk board with dot leaders and hand-divider rules; `rooftop.html` flips to an airy daylight composition with a city-skyline silhouette footer — two meaningfully different composition families within one site.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Address: 1411 S Tryon St, Suite A, Charlotte NC 28203 | `index.html`, `visit.html`, all footers | [Checkle](https://www.checkle.com/biz/the-brickyard-charlotte/menu), [South End Charlotte](https://southendclt.org/go/the-brickyard) |
| Phone: (980) 938-6990 | `visit.html`, `index.html`, headers | [Instagram @thebrickyardclt](https://www.instagram.com/thebrickyardclt/), [Restaurantji](https://www.restaurantji.com/nc/charlotte/the-brickyard-) |
| Email: thebrickyard704@gmail.com | `visit.html` | [Instagram @thebrickyardclt](https://www.instagram.com/thebrickyardclt/) |
| Hours: Mon–Tue closed; Wed–Fri 5 PM–2 AM; Sat–Sun 2 PM–2 AM | `index.html`, `visit.html` | [Instagram bio](https://www.instagram.com/thebrickyardclt/), [Four Dollar Jacks listing](https://www.fourdollarjacks.com/bars-near-me/the-brickyard-on-south-tryon-street) |
| "NEVER a cover, ALWAYS a crowd!" — no cover charge | `index.html`, `the-yard-way.html` | [Instagram bio (owned)](https://www.instagram.com/thebrickyardclt/) |
| Neighborhood bar and live music joint; TVs for all sporting events; rooftop bar and patio | `index.html`, `live.html`, `rooftop.html` | [Facebook (owned)](https://www.facebook.com/thebrickyardclt/), [South End Charlotte directory](https://southendclt.org/go/the-brickyard) |
| Live music with DJs on weekend nights | `live.html` | [Restaurantji overview](https://www.restaurantji.com/nc/charlotte/the-brickyard-) |
| The Brickyard does not take reservations | `visit.html`, `the-yard-way.html` | [Restaurantji attributes](https://www.restaurantji.com/nc/charlotte/the-brickyard-) |
| Drafts poured include Miller Lite, High Life, Pacifico, Wicked Weed; shots/serves include Fireball and vodka-Red Bull | `menu.html` | [Checkle menu transcription (Oct 2025)](https://www.checkle.com/biz/the-brickyard-charlotte/menu) |
| Kitchen turns out jumbo chicken wings, an app sampler platter (buffalo chicken tender cutlets, onion rings), steak & cheese egg rolls, the Brickyard chicken sandwich, a buffalo chicken sandwich, burgers, salads, and soups | `menu.html` | [Four Dollar Jacks aggregated kitchen menu](https://www.fourdollarjacks.com/bars-near-me/the-brickyard-on-south-tryon-street) |
| Steps from Amos' South End; across from the RailYard | `visit.html`, `rooftop.html` | [South End Charlotte nearby listings](https://southendclt.org/go/the-brickyard) |

**Deliberately omitted for lack of verification:** owner/founder history (reviewer descriptions of the owner are third-party hearsay), opening year, capacity numbers, parking ownership, drink prices, kitchen hours, event calendars with named acts, happy-hour specials.

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Events & Music Calendar Pack (Catering & Private Events / Guest Engagement territory):** a live, filterable show calendar with band pages and reminders.
- **Menu Experience Pack:** the current chalk board could become a digital menu with pricing, dietary filters, and pairing suggestions.
- **Order & Reserve Pack:** tap-the-kitchen pre-ordering for pickup and waitlist handling on packed Saturdays.
- **Trust & Reputation Pack:** review aggregation and response workflows given the volume of Google/Yelp traffic.
- **Photo Story Pack:** the rooftop view, mural-adjacent block, and show crowds are a natural photo-editorial upsell.

### Intentionally Not Implemented (Preserved for Upsell)

- No event booking, private-event inquiry, or catering tools of any kind (and no forms whatsoever).
- No interactive menu search, filtering, or concierge behavior — the menu is a static board.
- No ordering, reservation, waitlist, payment, or loyalty functionality.
- No newsletter/SMS capture, social-feed embeds, or review widgets.

### Available for Production Scope

- Full show-calendar engine with artist submissions.
- Digital menu system with daily-specials scheduling.
- Rooftop/private-events package builder for the space.

## QA

- **Machine validation:** `node scripts/validate-demo.mjs the-brickyard` executed; `qa-report.json` and `design-diversity.json` generated; exit code 0 after fixes.
- **Browser verification (headless Chrome):** rendered homepage, menu, live-music page, rooftop page, yard-way page, and visit page at 1440×900 (desktop) and 390×844 (mobile); captured console output (zero errors/warnings); confirmed no horizontal overflow at mobile width; tabbed through navigation links and mobile drawer toggle to confirm keyboard operability and visible focus rings; confirmed reduced-motion media query present. Screenshots retained in `qa-screenshots/`.
