# Persuasian Restaurant — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Persuasian Restaurant (Persuasian Asian Fusion & Wine Bar)
- **Slug:** `persuasian-restaurant`
- **Audit Grade / Disposition / Score:** A / YES / 100
- **Audit Batch:** 15
- **Verification Date:** August 25, 2026

## Verification Sources

- [Persuasian Asian Fusion & Wine Bar Official Website](https://persuasianrestaurant.com)
- [SinglePlatform Persuasian Dilworth Menu Guide](https://singleplatform.com)
- [Grubhub Charlotte Asian Dining Guide](https://grubhub.com)

## Original Audit Weakness

Persuasian Restaurant relies on basic third-party aggregator ordering portals and outdated web layouts. Located in historic Dilworth on Park Rd, it lacks an owned digital showcase capturing its scratch Asian wok craft, curated boutique wine list, intimate lounge atmosphere, and dining room directives.

## Creative Brief

### Verified Visual / Content Anchors

1. **Dilworth Charlotte Location:** 2214 Park Road, Charlotte NC 28203 (Dilworth neighborhood).
2. **Asian Fusion & Wine Specialties:** Szechuan Pork Dumplings in Chili Oil, Hong Kong Chilean Sea Bass, Crispy Sesame Chicken, Traditional Chicken/Shrimp Pad Thai, Crispy Crab Rangoon, and Sommelier-Curated Boutique Wine Pairings.
3. **Contact & Operating Hours:** Phone (704) 333-1837; Tue–Sun 4:00 PM – 9:30 PM | Closed Mondays.

### Core Design Moves

1. **Elegant Luxury Display Serif Typography:** High-fashion serif (*Playfair Display*) paired with clean body sans (*Plus Jakarta Sans*) and sommelier cellar ticket mono (*Space Mono*).
2. **Burgundy Wine Velvet & Gold Leaf Palette:** Intimate wine lounge palette anchored in deep burgundy wine velvet (`#4A0E17`), dark plum mahogany (`#2D080E`), warm gold leaf (`#F59E0B`), rich crimson (`#9F1239`), and silk cream (`#FFFBEB`).
3. **"The Asian Wok Craft & Curated Wine Cellar Matrix":** Matrix-style dual column layout (`asian-fusion-and-wok-craft.html` & `menu.html`) showcasing scratch Asian wok entrees and handcrafted dumplings alongside boutique international wines and craft cocktails.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Picasso’s Sports Café` — Athletic Sports Bar with Barlow Condensed and Jet Black/Sports Gold.
2. `Pho Huong Que` — Vietnamese Saigon Heritage with Newsreader and Forest Emerald/Amber.
3. `Passage to India Indian Cuisine` — Royal Mughlai Palace with Cormorant Garamond and Peacock Indigo/Saffron.

### Divergent Choices for Persuasian Restaurant

- **Hero Composition:** Dilworth Asian Fusion Lounge & Wine Cellar split-hero layout: left side features an Asian Wine Cellar Seal badge (`"ASIAN FUSION & CURATED WINE BAR • DILWORTH CHARLOTTE"`), sleek luxury serif typography (*Playfair Display*), burgundy wine velvet & gold leaf palette, and right side features a bold framed hero image of artisanal cocktails and curated boutique wines.
- **Section Rhythm:** Replaced standard card grids with **Persuasian Vault Cards** (`persuasian-vault-card`) and Dilworth Asian dining & wine cellar highlights.
- **HTML Vocabulary:** Completely unique class names (`persuasian-header`, `persuasian-brand`, `cellar-hero-stage`, `persuasian-seal-badge`, `persuasian-vault-card`, `persuasian-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 2214 Park Road in Charlotte NC 28203 (Dilworth) | `visit.html`, `index.html`, `concept.html` | [Persuasian Official Website](https://persuasianrestaurant.com) |
| Operating hours: Tue-Sun 4:00 PM - 9:30 PM (Closed Mondays) | `visit.html`, `index.html` | [Persuasian Official Website](https://persuasianrestaurant.com) |
| Phone number: (704) 333-1837 | `visit.html`, `index.html` | [Persuasian Official Website](https://persuasianrestaurant.com) |
| Asian fusion specialties (Szechuan dumplings, Chilean sea bass, Pad Thai) | `menu.html`, `asian-fusion-and-wok-craft.html` | [SinglePlatform Menu Guide](https://singleplatform.com) |
| Curated boutique wine pairings and craft cocktail lounge | `menu.html`, `wine-pairings-and-lounge-craft.html` | [Persuasian Official Website](https://persuasianrestaurant.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Persuasian Dilworth Date Night & Table Reservation Engine:** Interactive table selection and intimate dining room booking app.
- **Persuasian Sommelier Wine Club & Cellar Pairing Pass:** Monthly hand-picked Asian-paired wine club subscription engine.
- **Persuasian Private Dining & Banquet Catering Engine:** Custom group dining menus for Dilworth corporate and private celebrations.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or online payment processing engine.
- No submission forms of any kind (no contact, order, or feedback forms).
- No automated SMS or email marketing tools.
- No live table seating reservation integration.

### Available for Production Scope

- Custom zero-commission direct Asian takeout app.
- Interactive wine and wok pairing guide.
- Digital gift card engine.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs persuasian-restaurant` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
