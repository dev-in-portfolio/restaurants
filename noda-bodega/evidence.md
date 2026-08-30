# NoDa Bodega — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** NoDa Bodega
- **Slug:** `noda-bodega`
- **Audit Grade / Disposition / Score:** A / YES / 99
- **Audit Batch:** 14
- **Verification Date:** August 24, 2026

## Verification Sources

- [NoDa Bodega Official Portal](http://nodabodega.com)
- [HappyCow — NoDa Bodega Charlotte](https://happycow.net)
- [Wanderlog — NoDa Bodega Profile](https://wanderlog.com)

## Original Audit Weakness

NoDa Bodega relies on basic single-page web host templates and Facebook updates. Located at 1200 E 36th St in the historic arts district, it lacks an owned digital showcase capturing its legendary sandwich creations, breakfast burrito drops, craft beer bodega retail, and NoDa patio dining directives.

## Creative Brief

### Verified Visual / Content Anchors

1. **Historic NoDa Arts District Location:** 1200 E 36th St, Charlotte NC 28205 (E 36th St & North Davidson St in NoDa Charlotte).
2. **Artisan Deli & Bodega Specialties:** The Bodega Italian Sub, Kimchi Roast Beef, Pastrami Reuben on Rye, Hot Turkey Cuban, Vegan Tempeh Banh Mi, Friday & Saturday Breakfast Burritos, Scratch Deli Salads, & Craft Beer Coolers.
3. **Contact & Operating Hours:** Phone (704) 375-8704; Tue–Thu 10:00 AM – 4:00 PM | Fri–Sat 8:00 AM – 4:00 PM | Sun–Mon Closed.

### Core Design Moves

1. **Punchy Bohemian Arts Display Typography:** Bold playful urban display font (*Bungee*) paired with clean body sans (*Plus Jakarta Sans*) and bodega deli ticket mono (*Space Mono*).
2. **Forest Olive & Mustard Relish Palette:** Bohemian neighborhood deli palette anchored in deep forest olive (`#14532D`), mustard relish yellow (`#CA8A04`), cherry pepper red (`#DC2626`), and warm kraft paper parchment (`#FEF9C3`).
3. **"The Colossal Sandwich & Bodega Provisions Matrix":** Matrix-style dual column layout (`artisan-sandwiches-craft.html` & `menu.html`) showcasing massive hot & cold deli subs alongside weekend breakfast burritos and scratch bodega sides.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `No Proof` — Modern Luxe Speakeasy with Prata fonts and Obsidian Onyx/Botanical Emerald.
2. `Ninety’s Dessert Bar` — Radical 90s Pop Retro Memphis with Righteous fonts and Memphis Teal/Neon Pink.
3. `Niki’s Food Shop` — Vintage Charlotte Southern Diner with Alfa Slab One fonts and Hickory Brown/Biscuit Gold.

### Divergent Choices for NoDa Bodega

- **Hero Composition:** NoDa Arts District Bohemian Bodega & Handcrafted Deli Vault split-hero layout: left side features a Bohemian Deli Stamp badge (`"ARTISAN NEIGHBORHOOD SANDWICH DELI & BODEGA • NODA CHARLOTTE"`), rustic organic display typography (*Bungee*), deep forest olive & mustard yellow palette, and right side features a bold framed hero image of stacked artisan deli sandwiches.
- **Section Rhythm:** Replaced standard card grids with **NoDa Bodega Vault Cards** (`bodega-vault-card`) and Charlotte NoDa neighborhood highlights.
- **HTML Vocabulary:** Completely unique class names (`bodega-header`, `bodega-brand`, `arts-hero-stage`, `bodega-seal-badge`, `bodega-vault-card`, `bodega-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 1200 E 36th St in Charlotte NC 28205 | `visit.html`, `index.html`, `concept.html` | [NoDa Bodega Official Portal](http://nodabodega.com) |
| Operating hours: Tue-Thu 10am-4pm, Fri-Sat 8am-4pm, Sun-Mon Closed | `visit.html`, `index.html` | [HappyCow Profile](https://happycow.net) |
| Phone number: (704) 375-8704 | `visit.html`, `index.html` | [NoDa Bodega Official Portal](http://nodabodega.com) |
| Colossal artisan sandwiches (The Bodega Italian, Pastrami Reuben, Hot Turkey Cuban) | `menu.html`, `artisan-sandwiches-craft.html` | [Wanderlog Profile](https://wanderlog.com) |
| Weekend breakfast burritos (Fri & Sat mornings from 8am) | `menu.html`, `weekend-breakfast-burrito-craft.html` | [NoDa Bodega Official Portal](http://nodabodega.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **NoDa Bodega Daily Sandwich Special SMS Drop:** Live broadcast of today's rotating hot specials and soup of the day.
- **NoDa Bodega Office Party Platter & Box Lunch Engine:** Corporate catering calculator for large sandwich trays and box lunches.
- **NoDa Express Order-Ahead Mobile Line:** Zero-commission lunch order ahead app.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or online payment processing engine.
- No submission forms of any kind (no contact, order, or feedback forms).
- No automated SMS or email marketing tools.
- No live table seating reservation integration.

### Available for Production Scope

- Custom zero-commission direct mobile sandwich order app.
- Interactive custom sandwich builder and dietary filter.
- Office box lunch catering portal.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs noda-bodega` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
