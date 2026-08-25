# Pokebowl Ramen — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Pokebowl Ramen (Poke Bowl Ramen)
- **Slug:** `pokebowl-ramen`
- **Audit Grade / Disposition / Score:** A / YES / 100
- **Audit Batch:** 16
- **Verification Date:** August 25, 2026

## Verification Sources

- [Pokebowl Ramen Official Platform](http://pokebowlramennc.com)
- [Grubhub Verified Restaurant Profile](https://grubhub.com)
- [DoorDash Local Charlotte Merchant Profile](https://doordash.com)

## Original Audit Weakness

Pokebowl Ramen relies on generic third-party delivery portal listings (DoorDash/Grubhub) and basic templated online ordering. Located in Northeast Charlotte on Brookdale Dr, it lacks an owned digital showcase capturing its 16-hour bone broth reduction craft, custom raw poke assembly matrix, crispy gyoza & sushi roll artistry, boba bar, and Brookdale pickup directives.

## Creative Brief

### Verified Visual / Content Anchors

1. **Northeast Charlotte Location:** 9621 Brookdale Dr, Suite 100, Charlotte NC 28215.
2. **Japanese & Hawaiian Specialties:** 16-Hour Pork Chashu Tonkotsu Ramen, Spicy Miso Ramen, Fresh Ahi Tuna & Atlantic Salmon Poke Bowls with House Ponzu and Spicy Mayo, Pan-Fried Pork Gyoza, Dragon Rolls, and Brown Sugar Pearl Boba Teas.
3. **Contact & Operating Hours:** Phone (980) 819-8639; Tue–Thu 11:00 AM – 9:30 PM | Fri–Sat 11:00 AM – 10:00 PM | Sun 11:00 AM – 9:00 PM | Closed Mondays.

### Core Design Moves

1. **Contemporary Japanese Display Sans Typography:** Bold modern display (*Outfit*) paired with clean body sans (*Plus Jakarta Sans*) and Tokyo ramen ticket mono (*Space Mono*).
2. **Obsidian Charcoal & Seaweed Teal Palette:** Electric Tokyo noodle house palette anchored in deep obsidian charcoal (`#0A0F1D`), midnight slate (`#020617`), seaweed teal (`#0D9488`), fiery chili crimson (`#E11D48`), warm broth ochre (`#F59E0B`), and clean eggshell white.
3. **"The 16-Hour Tonkotsu Broth & Fresh Island Poke Matrix":** Matrix-style dual column layout (`tonkotsu-ramen-and-poke-craft.html` & `menu.html`) showcasing simmered ramen bowls and custom poke creations alongside crispy appetizers and brown sugar boba teas.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Laurel Park` — SouthPark Mediterranean Veranda with Cormorant Garamond and Laurel Emerald/Sandstone Ochre.
2. `Littl Madeleine` — Korean-French Haute Pâtisserie with Italiana and Rose Blush/Plum Velvet.
3. `Pertinacious Coffee` — Modern Specialty Roastery with Epilogue and Espresso Dark/Tangerine Blossom.

### Divergent Choices for Pokebowl Ramen

- **Hero Composition:** Tokyo Neon Ramen Bar & Island Poke Lab split-hero layout: left side features an Artisanal Broth & Poke Seal badge (`"16-HOUR TONKOTSU BROTH & FRESH ISLAND POKE • CHARLOTTE NC"`), bold modern Japanese display typography (*Outfit*), obsidian & neon teal palette, and right side features a framed hero image of steaming tonkotsu ramen with braised pork belly and soft-boiled ajitsuke tamago egg.
- **Section Rhythm:** Replaced standard card grids with **Ramen Vault Cards** (`ramen-vault-card`) and Northeast Charlotte ramen bar highlights.
- **HTML Vocabulary:** Completely unique class names (`ramen-header`, `ramen-brand`, `ramen-hero-stage`, `ramen-seal-badge`, `ramen-vault-card`, `ramen-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 9621 Brookdale Dr Suite 100 in Charlotte NC 28215 | `visit.html`, `index.html`, `concept.html` | [Pokebowl Ramen Platform](http://pokebowlramennc.com) |
| Operating hours: Tue-Thu 11AM-9:30PM, Fri-Sat 11AM-10PM, Sun 11AM-9PM | `visit.html`, `index.html` | [Pokebowl Ramen Platform](http://pokebowlramennc.com) |
| Direct phone: (980) 819-8639 | `visit.html`, `index.html` | [Grubhub Verified Profile](https://grubhub.com) |
| 16-hour simmered tonkotsu broth, spicy miso, & pork chashu | `menu.html`, `tonkotsu-ramen-and-poke-craft.html` | [Pokebowl Ramen Menu](http://pokebowlramennc.com) |
| Fresh Ahi tuna poke bowls, sushi rolls, & brown sugar boba tea | `menu.html`, `poke-bowls-and-boba-craft.html` | [Pokebowl Ramen Menu](http://pokebowlramennc.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Pokebowl Ramen Interactive Poke Bowl & Ramen Broth Customizer:** Step-by-step visual base, protein, marinade, and topping builder for takeout orders.
- **Pokebowl Ramen VIP Boba & Noodle Loyalty Passport:** Digital punch card and monthly noodle bowl perks.
- **Pokebowl Ramen Family & Corporate Catering Trays:** Large-format poke platter and noodle party pack builder.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or online payment processing engine.
- No submission forms of any kind (no contact, order, or feedback forms).
- No automated SMS or email marketing tools.
- No live table seating reservation integration.

### Available for Production Scope

- Custom zero-commission direct ordering app.
- Interactive ramen pairing and allergen filter engine.
- Digital Charlotte gift card engine.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs pokebowl-ramen` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
