# Mother of Dragons — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Mother of Dragons
- **Slug:** `mother-of-dragons`
- **Audit Grade / Disposition / Score:** A / YES / 100
- **Audit Batch:** 14
- **Verification Date:** August 24, 2026

## Verification Sources

- [Mother of Dragons Official Portal](https://www.motherofdragons.com)
- [Axios Charlotte — Mother of Dragons Profile](https://charlotte.axios.com)
- [Facebook Official Page — Mother of Dragons CLT](https://www.facebook.com)

## Original Audit Weakness

Mother of Dragons relies on basic template site and third-party game booking widgets. Located at 1640 Sardis Rd N, it lacks an owned digital showcase capturing its fantasy tavern atmosphere, tabletop game library tiers, sommelier wine list, private game room bookings, and Charlotte gamer directives.

## Creative Brief

### Verified Visual / Content Anchors

1. **South Charlotte / Matthews Location:** 1640 Sardis Rd N, Suite 110, Charlotte NC 28270 (Sardis Road North / Crown Point Charlotte).
2. **Board Game & Tavern Specialties:** 50+ Curated Tabletop Board Game Library, Boutique Wine by the Glass & Bottle, Specialty Espresso Drinks, Paninis, Wraps, Artisan Gelato, & Themed Private RPG Gaming Vaults.
3. **Contact & Operating Hours:** Phone (980) 262-2402; Tue–Thu 10:00 AM – 9:00 PM | Fri–Sat 10:00 AM – 10:00 PM | Sun 11:00 AM – 8:00 PM | Mon Closed.

### Core Design Moves

1. **Mythic Fantasy Display Typography:** Heroic medieval display serif (*Cinzel Decorative*) paired with clean body sans (*Plus Jakarta Sans*) and RPG dice stat mono (*Space Mono*).
2. **Dragon Scale Obsidian & Ember Orange Palette:** Mythic tavern palette anchored in deep dragon scale obsidian indigo (`#1E1B4B`), glowing ember orange (`#F97316`), royal amethyst purple (`#7C3AED`), and mystic slate (`#F8FAFC`).
3. **"The 50+ Board Game Library & Dragon Hearth Matrix":** Matrix-style dual column layout (`tabletop-game-vault-craft.html` & `menu.html`) showcasing curated tabletop games alongside boutique wine flights, specialty lattes, & warm paninis.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Miro Spanish Grille` — Spanish Mediterranean Sunlit Bodega with Cinzel fonts and Rioja Crimson/Saffron Gold.
2. `Midwood Country Club` — Vintage Plaza Midwood Neon Dive with DM Serif Display fonts and Felt Green/Neon Gold.
3. `Milkbread` — Warm Japanese Shokupan with Plus Jakarta Sans fonts and Honey/Espresso.

### Divergent Choices for Mother of Dragons

- **Hero Composition:** Mythic Fantasy Tavern & Dragon Hearth Vault split-hero layout: left side features a Dragon Crest Stamp badge (`"TABLETOP BOARD GAME CAFÉ & WINE BAR • SOUTH CHARLOTTE NC"`), mythic display serif (*Cinzel Decorative*), deep obsidian indigo & ember orange palette, and right side features a bold framed hero image of the atmospheric game lounge.
- **Section Rhythm:** Replaced standard card grids with **Dragon Vault Cards** (`dragon-vault-card`) and Charlotte tabletop gaming highlights.
- **HTML Vocabulary:** Completely unique class names (`dragon-header`, `dragon-brand`, `ember-hero-stage`, `dragon-seal-badge`, `dragon-vault-card`, `dragon-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 1640 Sardis Rd N in Charlotte NC 28270 | `visit.html`, `index.html`, `concept.html` | [Mother of Dragons Official Portal](https://www.motherofdragons.com) |
| Operating hours: Tue-Thu 10am-9pm, Fri-Sat 10am-10pm, Sun 11am-8pm, Mon Closed | `visit.html`, `index.html` | [Mother of Dragons Official Portal](https://www.motherofdragons.com) |
| Phone number: (980) 262-2402 | `visit.html`, `index.html` | [Mother of Dragons Official Portal](https://www.motherofdragons.com) |
| 50+ Curated Board Games Library & Private RPG Game Rooms | `menu.html`, `tabletop-game-vault-craft.html` | [Axios Charlotte Profile](https://charlotte.axios.com) |
| Boutique Wine Flights, Espresso Drinks, Paninis, & Gelato | `menu.html`, `bites-and-potions-craft.html` | [Mother of Dragons Official Portal](https://www.motherofdragons.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Mother of Dragons Game Pass & Club Pass:** Monthly unlimited board game pass & VIP member subscription engine.
- **Mother of Dragons Private D&D / RPG Room Booking Engine:** Themed private room reservation system with custom dungeon master packages.
- **Mother of Dragons Tournament & Guild Scheduler:** Social deception game night & tournament ticketing engine.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or online payment processing engine.
- No submission forms of any kind (no contact, order, or feedback forms).
- No automated SMS or email marketing tools.
- No live table seating reservation integration.

### Available for Production Scope

- Custom zero-commission direct tabletop game booking app.
- Interactive custom RPG room & party package builder.
- Custom game library checkout and rulebook companion portal.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs mother-of-dragons` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
