# Queen City Bites & Crafts — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Queen City Bites & Crafts (QCBC)
- **Slug:** `queen-city-bites-and-crafts`
- **Audit Grade / Disposition / Score:** A / YES / 98
- **Audit Batch:** 17
- **Verification Date:** August 25, 2026

## Verification Sources

- [QCBC Official Website](https://qcbc-clt.com)
- [QCBC Untappd Tap List](https://untappd.com/v/queen-city-bites-and-crafts/8133591)
- [Uptown Charlotte Brevard Court Directory](https://uptowncharlotte.com)

## Original Audit Weakness

QCBC relies on generic third-party Toast and ChowNow ordering portals and fragmented social listings. Located in the historic cobblestone arcade of Brevard Court directly across from Romare Bearden Park and Truist Field, it lacks an owned digital showcase capturing its 20-tap local craft rotation, European-style alleyway patio dining, artisan bratwurst and poutine craft, and Uptown event pre-game directives.

## Creative Brief

### Verified Visual / Content Anchors

1. **Historic Brevard Court Location:** 135 Brevard Court, Charlotte NC 28202 (between Church & Tryon across from Romare Bearden Park).
2. **Craft Beer & Gastropub Offerings:** 20+ Rotating Craft Beer Taps, Beer-Braised Bratwurst, Certified Angus Smash Burgers, Quebec-Style Gravy Poutine, Loaded Hand-Cut Fries, Gourmet Craft Hot Dogs, and Uptown Gameday Patios.
3. **Contact & Operating Hours:** Phone (704) 526-0159; Sun–Mon 11:00 AM – 10:00 PM | Tue–Thu 11:00 AM – 11:00 PM | Fri–Sat 11:00 AM – 12:00 AM.

### Core Design Moves

1. **Warm European Editorial Serif Typography:** Rich characterful serif (*Fraunces*) paired with clean body sans (*Plus Jakarta Sans*) and Brevard Court cellar ticket mono (*Space Mono*).
2. **Brick Tavern Crimson & Honey Pilsner Gold Palette:** Historic alleyway tavern palette anchored in deep brick tavern crimson (`#7F1D1D`), cobblestone charcoal (`#1C1917`), honey pilsner gold (`#F59E0B`), fresh parsley green (`#16A34A`), warm pretzel linen (`#FEF3C7`), and clean pure white.
3. **"The 20-Tap Craft Rotation & Artisan Brats Matrix":** Matrix-style dual column layout (`craft-taps-brats-and-poutine-craft.html` & `menu.html`) showcasing 20 rotating draft lines, beer-braised sausages, smash burgers, and rich poutines alongside Romare Bearden gameday patio seating.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Queen Park Social` — LoSo Entertainment Club with Syne and Warehouse Charcoal/Electric Cyan/Coral.
2. `Punta Cana` — Tropical Dominican Grill with DM Serif Display and Caribbean Sapphire/Sunburst Mango.
3. `Prohibition` — 1920s Speakeasy with Cinzel and Noir/Antique Brass Gold.
4. `Pho Real` — Modern Vietnamese Noodle Bar with Outfit and Emerald Jade/Imperial Gold.

### Divergent Choices for QCBC

- **Hero Composition:** Historic Brevard Court Brick Alley & European Arcade Taproom split-hero layout: left side features a Brevard Court Historic Seal badge (`"EST. HISTORIC BREVARD COURT • 20 CRAFT TAPS & ARTISAN BRATS • UPTOWN CHARLOTTE"`), warm editorial display typography (*Fraunces*), brick crimson & honey gold palette, and right side features a framed hero image of artisanal burgers and gourmet bratwursts.
- **Section Rhythm:** Replaced standard card grids with **QCBC Vault Cards** (`qcbc-vault-card`) and Brevard Court cobblestone walkway highlights.
- **HTML Vocabulary:** Completely unique class names (`qcbc-header`, `qcbc-brand`, `brevard-hero-stage`, `qcbc-seal-badge`, `qcbc-vault-card`, `qcbc-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 135 Brevard Court in Charlotte NC 28202 (Uptown) | `visit.html`, `index.html`, `concept.html` | [QCBC Official Website](https://qcbc-clt.com) |
| Operating hours: Sun-Mon 11AM-10PM, Tue-Thu 11AM-11PM, Fri-Sat 11AM-12AM | `visit.html`, `index.html` | [QCBC Official Website](https://qcbc-clt.com) |
| Direct phone: (704) 526-0159 | `visit.html`, `index.html` | [QCBC Official Website](https://qcbc-clt.com) |
| 20 rotating craft beer taps, local NC brews & Untappd live board | `index.html`, `craft-taps-brats-and-poutine-craft.html` | [Untappd QCBC Tap List](https://untappd.com/v/queen-city-bites-and-crafts/8133591) |
| Beer-braised brats, smash burgers, Quebec poutine & loaded fries | `menu.html`, `smash-burgers-and-patio-craft.html` | [QCBC Menu](https://qcbc-clt.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **QCBC Live Untappd Tap Wall & Digital Keg Flow Integration:** Real-time remaining keg level tracker.
- **QCBC Romare Bearden Gameday & Knights Stadium Express Pickup:** Fast-lane stadium takeout ordering.
- **QCBC Brevard Court Craft Beer Passport:** Rewards club for sampling all rotating 20 taps.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or online payment processing engine.
- No submission forms of any kind (no contact, order, or feedback forms).
- No automated SMS or email marketing tools.
- No live table seating reservation integration.

### Available for Production Scope

- Custom zero-commission stadium takeout app.
- Interactive beer style & food pairing engine.
- Digital Brevard Court gift card engine.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs queen-city-bites-and-crafts` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
