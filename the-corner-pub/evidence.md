# The Corner Pub — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** The Corner Pub
- **Slug:** `the-corner-pub`
- **Audit Grade / Disposition / Score:** A / YES / 99
- **Audit Batch:** 22
- **Verification Date:** August 24, 2026

## Verification Sources

- [corner-pub.popmenu.com — Contact](https://corner-pub.popmenu.com/contact) (the pub's own website platform: canonical address 335 N Graham St, phone, full weekly hours with kitchen-close times)
- [corner-pub.popmenu.com — site navigation](https://corner-pub.popmenu.com/) (owned: online ordering, gift cards via Toast, private events, specials page, VIP club)
- [Uptown Charlotte directory — The Corner Pub](https://uptowncharlotte.com/go/the-corner-pub) (Center City Partners directory: description, categories including cocktails/wine/sports bar, social accounts)
- [Restaurant Guru — Corner Pub](https://restaurantguru.com/The-Corner-Pub-Charlotte) (updated June 2026: hours corroboration, features — outdoor seating, takeaway, delivery, wheelchair accessible, parking, TV, no bookings; dishes customers actually order)
- [Yelp — The Corner Pub](https://www.yelp.com/biz/the-corner-pub-charlotte) (owned business description: Fourth Ward, intersection of 7th St & N Graham St, within blocks of Bank of America Stadium and the ballpark)
- [cornerpubcharlotte.com](http://cornerpubcharlotte.com/) (owned domain; resolves to the same Popmenu site)

## Original Audit Weakness

The pub's information is fragmented and partly contradictory across the web: the Uptown Charlotte directory lists "355 N Graham St, 28206" while the pub's own site says "335 N Graham St, 28202"; the food menu lives inside a JavaScript app that search engines and many visitors never see rendered; kitchen-closing times exist only on one deep contact page. A first-time visitor comparing listings cannot tell where the pub actually sits or when the kitchen closes. The demo demonstrates one authoritative hub with a canonical address, a readable kitchen board, and game-day information in plain HTML.

## Creative Brief

### Verified Visual / Content Anchors

1. **The intersection** — the pub sits literally on the corner of 7th Street & North Graham Street in historic Fourth Ward (owned description), a crossroads identity the brand name leans on.
2. **The skyline + stadium proximity** — "within blocks of both Bank of America Stadium and the [Knights] ballpark" with city-skyline views from the pub (owned description); tailgate and watch-party culture ("come out to tailgate or watch the games").
3. **The regulars' pub** — "an established crowd of regulars," laid-back atmosphere, friendly staff praised by name in reviews; Google rating 4.5 across ~459 reviews.
4. **The kitchen's greatest hits** — cajun garlic and lemon pepper wings, mozzarella sticks, nachos, chili, soft pretzels, pizza, burgers, wraps, cheese fries (repeatedly mentioned across customer reviews and dish aggregations).
5. **Pub green heritage** — a classic Fourth Ward corner pub pouring draft beer and wine with outdoor seating on the corner.

### Core Design Moves

1. **Scoreboard modernism** — a structured panel system of thick-ruled "boards" (game day, kitchen, pints) inspired by athletics scoreboards and pub signage: deep pub green, cream, and brass with Oswald condensed capitals and Zilla Slab body — a slab-and-condensed system no recent demo uses.
2. **The crossroads motif** — a diagonal intersection graphic (two crossing streets with the pub at the corner) recurs as the hero mark, section dividers, and map-card illustration, making the "corner" identity structural rather than decorative.
3. **Stat-numeral information design** — practical facts (hours, kitchen-close times, stadium proximity in blocks) are set as scoreboard numerals in ruled stat panels, replacing generic icon-card grids.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `the-brickyard` — dark soot/brick gig-poster collage, Anton marquee type, rotated ticket stubs, ticker bands.
2. `the-changebaker-place` — cream editorial gazette, Fraunces serif, drop caps, film-reel chapters, pinned bulletin cards.
3. `midtown-tavern` — copper industrial split hero, Outfit, card grids.
4. `mert-s-heart-and-soul` — Playfair porch warmth, alternating bands.
5. `medusa-lounge` — Cormorant obsidian-gold centered luxury.

### Dominant Pattern Being Avoided

Hero banner → centered headline → 3-up cards → alternating bands; dark poster collage; light literary gazette.

### Divergent Choices for The Corner Pub

- **Primary hero composition:** a structured "corner intersection" diagram hero — the crossroads graphic with the pub pinned at 7th & Graham beside oversized condensed stat panels — not a photo hero, poster wall, or editorial masthead.
- **Section rhythm:** ruled scoreboard panels and stat blocks with thick double borders replace cards, posters, reels, and bulletins.
- **Typography system:** Oswald condensed caps + Zilla Slab — athletic/slab heritage, distinct from Anton (poster sans), Fraunces/Playfair/Cormorant (serifs), and Outfit (geometric sans) used by the five demos above.
- **Major page composition divergence:** `menu.html` is a chalk-and-brass "kitchen board" with section rails and stat callouts; `game-day.html` flips to a fixture-card schedule composition — two more families inside one site.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Corner of 7th St & N Graham St, historic Fourth Ward, Uptown Charlotte | `index.html`, `fourth-ward.html`, `visit.html` | [Yelp owned description](https://www.yelp.com/biz/the-corner-pub-charlotte), [Uptown Charlotte directory](https://uptowncharlotte.com/go/the-corner-pub) |
| Address: 335 N Graham St, Charlotte NC 28202 | `visit.html`, footers | [Popmenu contact (owned)](https://corner-pub.popmenu.com/contact) |
| Phone: (704) 376-2720 | `visit.html`, headers | [Popmenu contact (owned)](https://corner-pub.popmenu.com/contact) |
| Hours: Sun 12 PM–12 AM; Mon–Tue 4 PM–12 AM; Wed–Fri 4 PM–2 AM; Sat 12 PM–2 AM | `visit.html`, `index.html` | [Popmenu contact (owned)](https://corner-pub.popmenu.com/contact) |
| Kitchen closes: 10 PM Sun–Thu; 11 PM Fri–Sat | `visit.html`, `menu.html` | [Popmenu contact (owned)](https://corner-pub.popmenu.com/contact) |
| Within blocks of Bank of America Stadium and the Knights' ballpark; skyline views; come tailgate or watch games | `game-day.html`, `index.html` | [Uptown directory details (owned description)](https://uptowncharlotte.com/go/the-corner-pub) |
| Kitchen hits: wings (cajun garlic, lemon pepper), mozzarella sticks, nachos, chili, soft pretzels, pizza, burgers, chicken wraps, cheese fries, fries | `menu.html` | [Restaurant Guru dish aggregation + customer reviews](https://restaurantguru.com/The-Corner-Pub-Charlotte) |
| Draft beer and wine; cocktails and wine categories; "plenty of brews" | `pints.html` | [Restaurant Guru](https://restaurantguru.com/The-Corner-Pub-Charlotte), [Uptown directory categories](https://uptowncharlotte.com/go/the-corner-pub) |
| Features: outdoor seating, takeaway, delivery, TV, parking, wheelchair accessible, credit cards, no bookings | `visit.html` | [Restaurant Guru features](https://restaurantguru.com/The-Corner-Pub-Charlotte) |
| Online ordering, Toast gift cards, private events page, specials page, VIP club exist | `menu.html`, `visit.html` | [Popmenu site navigation (owned)](https://corner-pub.popmenu.com/) |
| Established regulars' crowd, laid-back atmosphere, Google rating 4.5 (~459 reviews) | `fourth-ward.html` | [Uptown directory](https://uptowncharlotte.com/go/the-corner-pub), [Restaurant Guru](https://restaurantguru.com/The-Corner-Pub-Charlotte) |

**Deliberately omitted for lack of verification:** exact prices (except the review-reported $10–20 per person range, cited as such), named tap lists, happy-hour specials details, private-events capacities/pricing, owner/founder names, founding year.

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Menu Experience Pack / Digital Menu Concierge:** the JS-locked menu could become a fast, searchable menu with photos and dietary filters.
- **Order & Reserve Pack:** direct ordering flow improvements and waitlist for game days (their Popmenu ordering and Toast gift cards already exist to build on).
- **Catering & Private Events Pack:** the pub has a private-events page — package builders and inquiry workflows remain sellable.
- **Guest Engagement Pack:** the existing VIP club and specials cadence are natural engagement upsells.
- **Local Discovery Pack:** the 355-vs-335 address conflict across directories is a live local-SEO cleanup opportunity.

### Intentionally Not Implemented (Preserved for Upsell)

- No forms of any kind — private events route to the pub's existing channels.
- No menu search/filter/concierge behavior; the kitchen board is static HTML.
- No custom ordering, reservations, waitlist, payments, loyalty, or newsletter systems.
- No specials engine or event calendar system.

### Available for Production Scope

- Private-events package builder for the pub's event space.
- Game-day specials scheduler synced to the fixtures page.
- Directory cleanup (Local Discovery) resolving the 355/335 address conflict.

## QA

- **Machine validation:** `node scripts/validate-demo.mjs the-corner-pub` executed; `qa-report.json` and `design-diversity.json` generated; exit code 0.
- **Browser verification (headless Chrome):** all six pages rendered at 1440×900 and 390×844; console captured (zero errors/warnings); horizontal overflow 0px on every page; mobile drawer toggle verified with `aria-expanded`; keyboard tab-through confirmed visible focus states; full-page screenshots reviewed for layout integrity; screenshots retained in `qa-screenshots/`.
