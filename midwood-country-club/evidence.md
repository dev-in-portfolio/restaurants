# Midwood Country Club — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Midwood Country Club
- **Slug:** `midwood-country-club`
- **Audit Grade / Disposition / Score:** A / YES / 99
- **Audit Batch:** 13
- **Verification Date:** August 24, 2026

## Verification Sources

- [ChalkySticks Venue Directory — Midwood Country Club](https://www.chalkysticks.com)
- [Creative Loafing Charlotte — Best Dive Bars](https://clclt.com)
- [Beer for Driving NC Bar Directory](https://www.beerfordriving.com)

## Original Audit Weakness

Midwood Country Club has no official dedicated website, relying solely on third-party dive bar lists and social check-ins. Located at 2840 Commonwealth Ave in Plaza Midwood, it lacks an owned digital showcase capturing its legendary neighborhood dive bar culture, pool & dart tournaments, outdoor patio, and Plaza Midwood directives.

## Creative Brief

### Verified Visual / Content Anchors

1. **Plaza Midwood Location:** 2840 Commonwealth Ave, Charlotte NC 28205 (Plaza Midwood off Commonwealth Ave & Gordon St).
2. **Dive Bar & Patio Amenities:** Cold Domestic & Craft Draft Beers, Shot & Beer Combos, Regulation Pool Tables, Steel-Tip Darts, Dog-Friendly Covered Patio, Jukebox, & Late-Night Hangouts.
3. **Contact & Operating Hours:** Phone (704) 777-7622; Mon–Fri 2:00 PM – 2:00 AM | Sat–Sun 12:00 PM – 2:00 AM.

### Core Design Moves

1. **Gritty Retro Display Typography:** Bold vintage display serif (*DM Serif Display*) paired with clean body sans (*Inter*) and dive bar tab mono (*Space Mono*).
2. **Felt Green & Neon Gold Palette:** Classic dive bar pool room palette anchored in deep pool felt green (`#064E3B`), glowing neon gold (`#FACC15`), moody charcoal night (`#111827`), and vintage cream (`#FEF3C7`).
3. **"The Dive Bar Tap Wall & Pool Hall Matrix":** Matrix-style dual column layout (`dive-bar-culture-craft.html` & `menu.html`) showcasing ice-cold draft beers alongside regulation pool tables, darts, & covered patio socializing.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Milkbread` — Warm Japanese Shokupan with Plus Jakarta Sans fonts and Honey/Espresso.
2. `Midtown Tavern` — Industrial Brick & Craft Copper with Outfit fonts and Copper Bronze/Barley Amber.
3. `Mert’s Heart & Soul` — Lowcountry Charleston Porch with Playfair Display fonts and Mahogany Amber/Cornbread Gold.

### Divergent Choices for Midwood Country Club

- **Hero Composition:** Vintage Plaza Midwood Neon Dive & Green Felt Pool Hall Vault split-hero layout: left side features a Dive Bar Stamp badge (`"UNPRETENTIOUS DIVE BAR & COVERED PATIO • PLAZA MIDWOOD CHARLOTTE"`), gritty bold retro display serif (*DM Serif Display*), deep pool felt green & neon gold palette, and right side features a bold framed hero image of the historic bar interior.
- **Section Rhythm:** Replaced standard card grids with **Country Club Vault Cards** (`countryclub-vault-card`) and Plaza Midwood neighborhood highlights.
- **HTML Vocabulary:** Completely unique class names (`countryclub-header`, `countryclub-brand`, `felt-hero-stage`, `dive-seal-badge`, `countryclub-vault-card`, `countryclub-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 2840 Commonwealth Ave in Charlotte NC 28205 | `visit.html`, `index.html`, `concept.html` | [ChalkySticks Venue Directory](https://www.chalkysticks.com) |
| Operating hours: Mon-Fri 2pm-2am, Sat-Sun 12pm-2am | `visit.html`, `index.html` | [ChalkySticks Venue Directory](https://www.chalkysticks.com) |
| Phone number: (704) 777-7622 | `visit.html`, `index.html` | [Beer for Driving Directory](https://www.beerfordriving.com) |
| Regulation Pool Tables, Steel-Tip Darts, & Covered Patio | `menu.html`, `dive-bar-culture-craft.html` | [Creative Loafing Charlotte](https://clclt.com) |
| Cold Domestic & Craft Draft Beers, Jukebox, & Dive Bar Vibe | `menu.html`, `patio-and-pours-craft.html` | [Creative Loafing Charlotte](https://clclt.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Midwood Bar Tab & Rewards Pass:** Exclusive digital rewards pass for Plaza Midwood regulars.
- **Midwood Pool & Dart League Registration Portal:** Interactive tournament scheduler & league signup system.
- **Midwood Private Patio Event Booking Engine:** Covered outdoor patio party reservation engine.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or online payment processing engine.
- No submission forms of any kind (no contact, order, or feedback forms).
- No automated SMS or email marketing tools.
- No live table seating reservation integration.

### Available for Production Scope

- Custom zero-commission direct mobile bar order & tab app.
- Interactive tournament scoring & bracket leaderboard display.
- Custom corporate party & patio booking portal.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs midwood-country-club` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
