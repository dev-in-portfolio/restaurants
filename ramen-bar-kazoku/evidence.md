# Ramen Bar Kazoku — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Ramen Bar Kazoku (Kazoku Ramen)
- **Slug:** `ramen-bar-kazoku`
- **Audit Grade / Disposition / Score:** A / YES / 98
- **Audit Batch:** 17
- **Verification Date:** August 25, 2026

## Verification Sources

- [Ramen Bar Kazoku Official Website](https://kazokuramen.com)
- [Kazoku Ramen Official Menu](https://ramenkazoku.com)
- [South Charlotte Dining Directory](https://charlottesgotalot.com)

## Original Audit Weakness

Ramen Bar Kazoku relies on generic third-party online ordering templates and unbranded social listings. Located in prime South Charlotte on Rea Road, it lacks an owned digital showcase capturing its 18-hour bone marrow broth reduction, artisanal alkaline ramen noodle pairings, family-first hospitality philosophy, and Ballantyne takeout express directives.

## Creative Brief

### Verified Visual / Content Anchors

1. **South Charlotte Location:** 7828 Rea Rd, Suite B, Charlotte NC 28277 (Ballantyne / Piper Glen corridor).
2. **Japanese Ramen & Izakaya Offerings:** 18-Hour Tonkotsu Ramen, Spicy Miso Tonkotsu, Black Garlic Oil (Mayu) Tonkotsu, Tokyo Shoyu Ramen, Tori Paitan Chicken Ramen, Crispy Pork Gyoza, Takoyaki Octopus Balls, Chashu Don Rice Bowls, Japanese Draft Beers, and Craft Sake.
3. **Contact & Operating Hours:** Phone (980) 208-1778; Lunch Daily 11:30 AM – 2:30 PM | Dinner Daily 4:30 PM – 9:00 PM (Mon–Sun).

### Core Design Moves

1. **Modern Japanese Geometric Sans Typography:** Contemporary high-contrast sans (*Sora*) paired with clean body sans (*Plus Jakarta Sans*) and Tokyo ramen ticket mono (*Space Mono*).
2. **Sumi Ink Indigo & Torii Vermilion Palette:** Tokyo nighttime ramen counter palette anchored in deep sumi ink indigo (`#090D16`), torii vermilion crimson (`#E11D48`), rich miso gold (`#F59E0B`), nori slate (`#1E293B`), silk bamboo cream (`#F8FAFC`), and clean pure white.
3. **"The 18-Hour Tonkotsu & Izakaya Tapas Matrix":** Matrix-style dual column layout (`tonkotsu-broth-and-ramen-craft.html` & `menu.html`) showcasing pork bone marrow broth reductions, springy wavy noodles, and izakaya appetizers alongside craft sake and Japanese lagers.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Red Sea Restaurant & Bar` — Horn of Africa Habesha Dining with Marcellus and Terracotta Ochre/Turmeric Gold.
2. `Rai Lay Thai Cuisine` — Southern Thai Coastal Sanctuary with Cormorant Garamond and Andaman Teal/Phuket Gold.
3. `Queen City Bites & Crafts` — Historic Brevard Court Tavern with Fraunces and Brick Crimson/Honey Gold.
4. `Queen Park Social` — LoSo Entertainment Club with Syne and Warehouse Charcoal/Electric Cyan/Coral.

### Divergent Choices for Kazoku

- **Hero Composition:** Tokyo Izakaya & Midnight Ramen Sanctuary split-hero layout: left side features a Kazoku Ramen Seal badge (`"18-HOUR TONKOTSU SIMMER • ARTISAN ALKALINE NOODLES • SOUTH CHARLOTTE"`), contemporary Japanese sans typography (*Sora*), sumi ink indigo & torii vermilion palette, and right side features a framed hero image of steaming authentic Japanese ramen with soft-boiled ajitsuke tamago egg and chashu pork.
- **Section Rhythm:** Replaced standard card grids with **Kazoku Vault Cards** (`kazoku-vault-card`) and Rea Road Japanese noodle bar highlights.
- **HTML Vocabulary:** Completely unique class names (`kazoku-header`, `kazoku-brand`, `tokyo-hero-stage`, `kazoku-seal-badge`, `kazoku-vault-card`, `kazoku-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 7828 Rea Rd Suite B in Charlotte NC 28277 (Ballantyne) | `visit.html`, `index.html`, `concept.html` | [Kazoku Official Website](https://kazokuramen.com) |
| Operating hours: Lunch 11:30AM-2:30PM, Dinner 4:30PM-9:00PM Daily | `visit.html`, `index.html` | [Kazoku Official Website](https://kazokuramen.com) |
| Direct phone: (980) 208-1778 | `visit.html`, `index.html` | [Kazoku Official Website](https://kazokuramen.com) |
| "Kazoku" translates to "Family" in Japanese | `index.html`, `concept.html` | [Kazoku Official Website](https://kazokuramen.com) |
| 18-hour tonkotsu broth, spicy miso, black garlic ramen & gyoza | `menu.html`, `tonkotsu-broth-and-ramen-craft.html` | [Kazoku Official Menu](https://ramenkazoku.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Kazoku Noodle Texture & Broth Richness Customizer:** Interactive noodle firmness and oil level builder.
- **Kazoku Ballantyne Express Takeout Separator:** Specialized broth-and-noodle dual container packing selector.
- **Kazoku VIP Ramen Loyalty & Slurp Club:** Rewards passport for tracking seasonal chef ramen bowls.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or online payment processing engine.
- No submission forms of any kind (no contact, order, or feedback forms).
- No automated SMS or email marketing tools.
- No live table seating reservation integration.

### Available for Production Scope

- Custom zero-commission takeout ordering app.
- Interactive sake pairing guide.
- Digital South Charlotte gift card engine.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs ramen-bar-kazoku` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
