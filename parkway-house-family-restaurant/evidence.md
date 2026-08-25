# Parkway House Family Restaurant — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Parkway House Family Restaurant
- **Slug:** `parkway-house-family-restaurant`
- **Audit Grade / Disposition / Score:** A / YES / 96
- **Audit Batch:** 15
- **Verification Date:** August 25, 2026

## Verification Sources

- [Parkway House Family Restaurant Official Website](https://parkwayhousenc.com)
- [SinglePlatform Parkway House Menu Guide](https://singleplatform.com)
- [Grubhub Charlotte Dining Guide](https://grubhub.com)

## Original Audit Weakness

Parkway House Family Restaurant relies on basic third-party aggregator listings and outdated web formats. Located at 5821 E W.T. Harris Blvd, it lacks an owned digital showcase capturing its all-day breakfast heritage, scratch diner griddling, Greek-American specialties, and family dining directives.

## Creative Brief

### Verified Visual / Content Anchors

1. **East Charlotte NC Location:** 5821 E W.T. Harris Blvd, Charlotte NC 28215 (East Town Shopping Center).
2. **Greek-American Diner Specialties:** Golden Buttermilk Pancakes, Country Fried Steak & Eggs, Gyro Pan Handle Skillet with spiced gyro meat, sweet onions, tomatoes, and imported feta, Triple-Decker Club Sandwiches, USDA Ribeye Steak Platters, and fresh baked pies.
3. **Contact & Operating Hours:** Phone (704) 563-1323; Mon–Fri 6:00 AM – 9:30 PM | Sat–Sun 7:00 AM – 9:30 PM.

### Core Design Moves

1. **Warm Vintage Serif Display Typography:** Stately vintage serif (*Fraunces*) paired with clean body sans (*Plus Jakarta Sans*) and diner order guest check mono (*Space Mono*).
2. **Diner Royal Blue & Buttermilk Gold Palette:** Classic American diner palette anchored in rich diner royal blue (`#1E3A8A`), deep oxford navy (`#172554`), buttermilk pancake gold (`#F59E0B`), and warm diner butter cream (`#FFFBEB`).
3. **"The All-Day Breakfast & Greek Diner Classics Matrix":** Matrix-style dual column layout (`all-day-breakfast-craft.html` & `menu.html`) showcasing buttermilk griddled pancakes and skillet breakfasts alongside Greek gyro platters and club sandwiches.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Papi Ricko Latin Kitchen & Lounge` — Electric Latin Cantina with Outfit fonts and Midnight Agave/Electric Magenta.
2. `Papi Queso` — Gourmet Grilled Cheese Melt Factory with Space Grotesk fonts and Toasted Sourdough/Cheddar Gold.
3. `Panda’s Den` — Master Wok-Fired Imperial Chinese Kitchen with Cinzel fonts and Vermilion/Amber.

### Divergent Choices for Parkway House Family Restaurant

- **Hero Composition:** Classic Greek-American Heritage Diner & All-Day Breakfast Vault split-hero layout: left side features a Heritage Diner Stamp badge (`"FAMILY DINER & ALL-DAY BREAKFAST • CHARLOTTE NC"`), warm vintage serif typography (*Fraunces*), diner royal blue & buttermilk gold palette, and right side features a bold framed hero image of golden griddled breakfast platters and country fried steak.
- **Section Rhythm:** Replaced standard card grids with **Parkway Vault Cards** (`parkway-vault-card`) and East Charlotte diner community highlights.
- **HTML Vocabulary:** Completely unique class names (`parkway-header`, `parkway-brand`, `diner-hero-stage`, `parkway-seal-badge`, `parkway-vault-card`, `parkway-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 5821 E W.T. Harris Blvd in Charlotte NC 28215 | `visit.html`, `index.html`, `concept.html` | [Parkway House Official Website](https://parkwayhousenc.com) |
| Operating hours: Mon-Fri 6am-9:30pm, Sat-Sun 7am-9:30pm | `visit.html`, `index.html` | [Parkway House Official Website](https://parkwayhousenc.com) |
| Phone number: (704) 563-1323 | `visit.html`, `index.html` | [Parkway House Official Website](https://parkwayhousenc.com) |
| All-day scratch breakfast (buttermilk pancakes, country fried steak, gyro skillet) | `menu.html`, `all-day-breakfast-craft.html` | [SinglePlatform Menu Guide](https://singleplatform.com) |
| Classic Greek-American lunch/dinner entrees & triple decker clubs | `menu.html`, `greek-and-american-classics-craft.html` | [Parkway House Official Website](https://parkwayhousenc.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Parkway House Express Morning Call-Ahead & Curbside Pickup Queue:** Fast breakfast ordering engine for morning commuters.
- **Parkway House Family Feast & Pancake Breakfast Catering Engine:** Large breakfast pan and buffet platter calculator for church and corporate events.
- **Parkway House Senior & VIP Diner Club:** Loyalty points and weekly special breakfast discounts engine.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or online payment processing engine.
- No submission forms of any kind (no contact, order, or feedback forms).
- No automated SMS or email marketing tools.
- No live table seating reservation integration.

### Available for Production Scope

- Custom zero-commission direct breakfast order app.
- Interactive catering breakfast banquet builder.
- Digital diner gift card engine.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs parkway-house-family-restaurant` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
