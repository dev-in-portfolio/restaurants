# The Diamond Restaurant — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** The Diamond Restaurant
- **Slug:** `the-diamond-restaurant`
- **Audit Grade / Disposition / Score:** A / YES / 98
- **Audit Batch:** 22
- **Verification Date:** August 24, 2026
- **Note:** an old stub folder exists at the non-canonical slug `diamond-restaurant/` (historical, form-based, retired). This build is the fresh canonical `the-diamond-restaurant/` and reuses nothing from the stub.

## Verification Sources

- [thediamondrestaurant.com](http://thediamondrestaurant.com/) (owned site — JS-rendered shell; its About text is mirrored verbatim by the sources below)
- [CharlotteEAST Facebook post quoting the owned About text](https://www.facebook.com/clteast/photos/1669444450082977) ("Originally the Diamond Soda Grill… conceived in 1945 by founders Flonnie and W.A. James…")
- [Historic Charlotte — "Roadside Wonders" PDF](https://www.historiccharlotte.org/downloads/Roadside%20Wonders%20Presentation%20FINAL.pdf) (1945 opening, original Diamond Soda Grill name, Flonnie and W.A. James, red neon sign visible from Independence Boulevard)
- [Checkle — Diamond Restaurant menu transcription](https://www.checkle.com/biz/diamond-restaurant-charlotte/menu) (October 2025: full priced menu including Fried Balogna $9.99, Chips & Dip $8.99, Big Block Burger $14.99, Diamond Dog $10.99, Winky Dinky Dog $9.99, Gyro Platter $21.99, banana pudding $6.99; late-night menu note "9–11 pm")
- [Postcard/Google listing](https://www.postcard.inc/places/diamond-restaurant-charlotte-uPkh69KbjHY) (updated Aug 24, 2026: phone, $10–20, accepts reservations, features, 4.2 Google/1,595 reviews, 3.5 Yelp/477, Infatuation + Eater quotes)
- [The Infatuation — Charlotte review](https://www.theinfatuation.com/charlotte/reviews/the-diamond-commonwealth-ave) ("all the way" / "Southern style" ordering culture, Big Block Burger, Winky-Dinky Dog, pimento dip, banana pudding, 80 years)
- [Eater Carolinas](https://carolinas.eater.com/maps/best-classic-charlotte-restaurants) ("11 Oldest Charlotte Restaurants" and "11 Best NC Diners" features; patio, Greek-leaning menu items, sides)
- [USA Restaurants directory](https://usarestaurants.info/explore/united-states/north-carolina/mecklenburg-county/charlotte/diamond-restaurant-704-375-8959.htm) (12 PM–9 PM daily listing — treated as one conflicting data point, see ledger)
- Customer reviews (Google/Yelp via Postcard aggregation): late-night closes of 3–4 AM on weekends, dog-friendly patio, jukebox, small parking lot with street parking, $5 Saturday mimosas, breakfast as a recent addition

## Original Audit Weakness

An 80-year-old institution with a neon sign famous enough to be in a historic-roads presentation has a website that renders as an empty JavaScript shell for much of its audience, while its actual information lives in third-party transcriptions. Hours are the clearest casualty: one directory says noon-to-9 daily while dozens of recent reviews describe 3–4 AM weekend closes and a 9 PM late-night menu. The demo demonstrates a site that carries the diner's own history, its real menu with prices, and honest hours guidance in plain HTML.

## Creative Brief

### Verified Visual / Content Anchors

1. **The red neon script** — the name written in bright red cursive on the brick building ("just asking to be photographed," per Eater), visible from Independence Boulevard since the 1940s (Historic Charlotte).
2. **The 1945 story** — Flonnie and W.A. James opening the Diamond Soda Grill; Mrs. James, a Marshville native, as "the beating heart of the Diamond"; son Ralph's quote about daily regulars.
3. **The counter and the booths** — spinny counter seats, lived-in booths, a corner jukebox, and a front patio looking onto Commonwealth (Eater, reviews).
4. **The order culture** — "all the way" or "Southern style" (chili, mustard, onions, slaw) on burgers and the fried bologna sandwich (Infatuation); the Winky Dinky Dog loaded with pimento cheese and chili.
5. **Eight decades of menu layers** — Southern diner plates, Greek-leaning dishes from a later era, a full bar, and banana pudding with 'Nilla wafers.

### Core Design Moves

1. **Neon-tube typography system** — the wordmark and key headlines use a neon-script face (Yellowtail) with tube-style glow outlines over porcelain, paired with Bevan slab display for menu-board voice and Libre Franklin for body — a script-plus-slab diner system no recent demo uses.
2. **Tube-outline panels** — section cards are drawn as rounded neon tubes (border-image-free CSS outlines with soft glow shadows) on a light porcelain ground, inverting the dark-background neon cliché; the site reads as daylight diner with neon accents.
3. **Diamond-cut section markers** — a repeating ◆ diamond motif (the name, literally) marks menu groups, list rows, and the footer rule, tying the identity into structure rather than decoration.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `the-craic` — plum dictionary hero, Young Serif, vertical rail, tap ledger.
2. `the-corner-pub` — green/cream scoreboard panels, Oswald + Zilla Slab.
3. `the-changebaker-place` — cream gazette, Fraunces, film reels.
4. `the-brickyard` — dark poster collage, Anton, ticket stubs.
5. `midtown-tavern` — copper split hero, Outfit, card grids.

### Dominant Pattern Being Avoided

Dark neon-on-black cliché, hero-banner-plus-cards, scoreboard panels, gazette columns, dictionary entries.

### Divergent Choices for The Diamond Restaurant

- **Primary hero composition:** a light porcelain "daylight diner" hero with the neon script wordmark glowing against white, flanked by a ticket-style since-1945 stamp — the inverse of dark neon treatments and of every recent demo's hero.
- **Section rhythm:** tube-outline panels in staggered counter/booth rhythm and diamond-marked menu groups replace card grids, ledgers, reels, and boards.
- **Typography system:** Yellowtail + Bevan + Libre Franklin — script display is absent from all five recent demos.
- **Major page composition divergence:** `menu.html` is a true priced menu board (verified prices) organized by the counter's own categories; `since-1945.html` is a decade-by-decade timeline strip — two more distinct families.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| 1901 Commonwealth Ave, Plaza Midwood, Charlotte NC 28205 | `index.html`, `visit.html`, `plaza-midwood.html` | [Postcard/Google listing](https://www.postcard.inc/places/diamond-restaurant-charlotte-uPkh69KbjHY), [Checkle](https://www.checkle.com/biz/diamond-restaurant-charlotte/menu) |
| Phone (704) 375-8959 | `visit.html`, headers | [Postcard](https://www.postcard.inc/places/diamond-restaurant-charlotte-uPkh69KbjHY), [Checkle](https://www.checkle.com/biz/diamond-restaurant-charlotte/menu) |
| Opened 1945 as Diamond Soda Grill by Flonnie and W.A. James; Mrs. James a Marshville, NC native; son Ralph quoted | `since-1945.html` | [CharlotteEAST quoting owned About](https://www.facebook.com/clteast/photos/1669444450082977), [Historic Charlotte PDF](https://www.historiccharlotte.org/downloads/Roadside%20Wonders%20Presentation%20FINAL.pdf) |
| Red neon sign visible from Independence Boulevard; snug brick diner | `since-1945.html`, `index.html` | [Historic Charlotte PDF](https://www.historiccharlotte.org/downloads/Roadside%20Wonders%20Presentation%20FINAL.pdf) |
| Named to Eater's "11 Oldest Charlotte Restaurants" and "11 Best NC Diners" | `since-1945.html` | [Eater Carolinas](https://carolinas.eater.com/maps/best-classic-charlotte-restaurants) |
| Menu items and prices (Fried Balogna $9.99, Chips & Dip $8.99, Pimento Dip $10.99, Diamond Fingers $14.99, Wings (10) $18.99, Big Block $14.99, Small Block $11.99, Full Blown Hemi $18.99, Diamond Dog $10.99, Winky Dinky Dog $9.99, Gyros Pita $13.99, Gyro Platter $21.99, Beef Tips $22.95, Vegetable Plates $14.99/$18.99, Banana Pudding $6.99, Peach Cobbler $7.99, etc.) | `menu.html` | [Checkle transcription, Oct 2025](https://www.checkle.com/biz/diamond-restaurant-charlotte/menu) |
| "All the way" / "Southern style" ordering; Winky Dinky Dog with pimento cheese and chili; banana pudding with 'Nilla wafers | `menu.html`, `since-1945.html` | [The Infatuation](https://www.theinfatuation.com/charlotte/reviews/the-diamond-commonwealth-ave) |
| Full bar; beer and wine lists including NC craft (Hop Drop, Triple C, Birdsong) and $6.99 mimosa | `menu.html` | [Checkle transcription](https://www.checkle.com/biz/diamond-restaurant-charlotte/menu) |
| Late-night menu from 9 PM; weekend closes reported at 3–4 AM by recent reviewers | `late-night.html`, `visit.html` | [Checkle note](https://www.checkle.com/biz/diamond-restaurant-charlotte/menu), [Postcard review aggregation](https://www.postcard.inc/places/diamond-restaurant-charlotte-uPkh69KbjHY) |
| Hours conflict: one directory lists 12 PM–9 PM daily | `visit.html` (honest-hours framing) | [USA Restaurants](https://usarestaurants.info/explore/united-states/north-carolina/mecklenburg-county/charlotte/diamond-restaurant-704-375-8959.htm) |
| Accepts reservations; $10–20; popular lunch/dinner; cozy; family friendly; good for groups | `visit.html` | [Postcard features](https://www.postcard.inc/places/diamond-restaurant-charlotte-uPkh69KbjHY) |
| Front patio on Commonwealth; dog-friendly patio; counter stools; jukebox (3 plays/$1 per reviewer) | `index.html`, `late-night.html`, `visit.html` | [Eater](https://carolinas.eater.com/maps/best-classic-charlotte-restaurants), [Postcard reviews](https://www.postcard.inc/places/diamond-restaurant-charlotte-uPkh69KbjHY) |
| 4.2 on Google (~1,595 reviews); 3.5 on Yelp (~477) | `index.html` | [Postcard](https://www.postcard.inc/places/diamond-restaurant-charlotte-uPkh69KbjHY) |
| Small parking lot plus nearby street parking; $5 Saturday mimosas reported | `visit.html` | [Postcard reviews](https://www.postcard.inc/places/diamond-restaurant-charlotte-uPkh69KbjHY) |

**Deliberately omitted for lack of verification:** current exact weekly hours (conflicting sources — the demo says so and routes to the phone line), current owner/management names, breakfast hours, the Midwood Challenge terms, happy-hour details.

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Menu Experience Pack / Digital Menu Concierge:** the priced menu could become a live menu with daily pie/cake/special rotation and dietary filters.
- **Order & Reserve Pack:** the reservation flag and delivery ordering could be unified into one flow.
- **Local Discovery Pack:** the hours conflict across directories is a live cleanup project.
- **Photo Story Pack:** the neon sign, counter, and patio are a natural editorial shoot.
- **Guest Engagement Pack:** late-night and weekend crowds are an SMS/social audience.

### Intentionally Not Implemented (Preserved for Upsell)

- No forms (the retired stub's demo form was deliberately not reproduced).
- No reservation/booking logic — the demo routes to phone and existing ordering paths.
- No menu search/filtering; the board is static HTML.
- No specials engine, loyalty, newsletter, or review automation.

### Available for Production Scope

- Live daily-specials and pie-of-the-day scheduling.
- Hours-of-operations management synced across directories.
- Late-night event programming pages.

## QA

- **Machine validation:** `node scripts/validate-demo.mjs the-diamond-restaurant` executed; `qa-report.json` and `design-diversity.json` generated; exit code 0.
- **Browser verification (headless Chrome):** all six pages rendered at 1440×900 and 390×844; console captured (zero errors/warnings); horizontal overflow 0px on every page; mobile drawer toggle verified with `aria-expanded`; keyboard tab-through confirmed visible focus states; full-page screenshots reviewed; screenshots retained in `qa-screenshots/`.
