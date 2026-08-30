# Rhino Market & Deli — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Rhino Market & Deli
- **Slug:** `rhino-market-and-deli`
- **Audit Grade / Disposition / Score:** A / YES / 96
- **Audit Batch:** 18
- **Verification Date:** August 25, 2026

## Verification Sources

- [Rhino Market & Deli Official Website](https://rhinomarket.com)
- [Uptown Charlotte Dining Directory](https://uptowncharlotte.com)
- [Charlotte's Got A Lot Neighborhood Market Guide](https://charlottesgotalot.com)

## Original Audit Weakness

Rhino Market & Deli relies on generic multi-location locator templates and third-party delivery redirects (Toast/ChowNow/UberEats). Despite being Charlotte's premier independent urban market & deli brand, it lacks an immersive flagship digital showcase highlighting its handcrafted hot deli sandwiches, local grocery ethos, curated craft taplist, and neighborhood roots.

## Creative Brief

### Verified Visual / Content Anchors

1. **Flagship Location & Network:** Flagship at 1500 W Morehead St, Suite E, Charlotte NC 28208 (Wesley Heights / FreeMoreWest) with hubs in Uptown, South End, NoDa, SouthPark, and CLT Airport.
2. **Deli & Bodega Offerings:** The Famous Chicken Torta on Crusty Ciabatta, The Sicilian Italian Grinder, The Legendary Rhino Club, Breakfast Burritos with Hash & Eggs, Local Enderly Coffee Cold Brew, and Curated NC Craft Beers & Natural Wines.
3. **Contact & Flagship Operating Hours:** Deli Phone (704) 375-2036 | Market Phone (704) 348-1428; Market: Mon–Thu 7AM–10PM, Fri–Sat 7AM–11PM, Sun 8AM–7PM | Deli: Mon–Sat 7AM–9PM, Sun 8AM–3PM.

### Core Design Moves

1. **Heavyweight Neo-Grotesque Display Typography:** Architectural urban display sans (*Space Grotesk*) paired with clean body sans (*Plus Jakarta Sans*) and bodega deli ticket mono (*Space Mono*).
2. **Hunter Green & Mustard Deli Gold Palette:** Modern urban market palette anchored in deep bodega slate (`#0F172A`), hunter green (`#166534`), sharp mustard gold (`#EAB308`), craft hop olive (`#4D7C0F`), warm butcher paper kraft (`#FEF3C7`), and clean pure white.
3. **"The Flagship Deli Sandwiches & Craft Bottleshoppe Matrix":** Matrix-style dual column layout (`deli-sandwiches-and-torta-craft.html` & `menu.html`) showcasing hot pressed tortas, cold deli grinders, breakfast burritos, and local bottleshoppe selections.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Ramen Bar Kazoku` — Tokyo Izakaya & Midnight Ramen Sanctuary with Sora and Sumi Ink/Torii Vermilion.
2. `Red Sea Restaurant & Bar` — Horn of Africa Habesha Dining with Marcellus and Terracotta Ochre/Turmeric Gold.
3. `Rai Lay Thai Cuisine` — Southern Thai Coastal Sanctuary with Cormorant Garamond and Andaman Teal/Phuket Gold.
4. `Queen City Bites & Crafts` — Historic Brevard Court Tavern with Fraunces and Brick Crimson/Honey Gold.

### Divergent Choices for Rhino Market

- **Hero Composition:** Modern Urban Bodega & Craft Deli Market split-hero layout: left side features a Rhino Market & Deli Seal badge (`"WESLEY HEIGHTS ORIGINAL • HANDCRAFTED DELI & BOTTLESHOPPE • LOCAL NC GOODS"`), heavyweight architectural sans typography (*Space Grotesk*), hunter green & mustard gold palette, and right side features a framed hero image of stacked artisanal deli sandwiches and tortas.
- **Section Rhythm:** Replaced standard card grids with **Rhino Vault Cards** (`rhino-vault-card`) and Wesley Heights urban bodega highlights.
- **HTML Vocabulary:** Completely unique class names (`rhino-header`, `rhino-brand`, `bodega-hero-stage`, `rhino-seal-badge`, `rhino-vault-card`, `rhino-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Flagship located at 1500 W Morehead St Suite E in Wesley Heights (28208) | `visit.html`, `index.html`, `concept.html` | [Rhino Market Official Website](https://rhinomarket.com) |
| Operating hours: Market 7AM-10/11PM, Deli 7AM-9PM (Sun 8AM-3/7PM) | `visit.html`, `index.html` | [Rhino Market Official Website](https://rhinomarket.com) |
| Flagship Deli phone: (704) 375-2036 / Market: (704) 348-1428 | `visit.html`, `index.html` | [Rhino Market Official Website](https://rhinomarket.com) |
| Multiple Charlotte neighborhood locations (Uptown, South End, NoDa, SouthPark, Airport) | `concept.html`, `visit.html` | [Rhino Market Official Website](https://rhinomarket.com) |
| Chicken Torta, Sicilian, Rhino Club, Breakfast Burrito, Enderly Coffee & Craft Beer | `menu.html`, `deli-sandwiches-and-torta-craft.html` | [Rhino Market Official Menu](https://rhinomarket.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Rhino Flagship Multi-Location Express Pickup Selector:** Live location switchboard for advance hot sandwich pickup.
- **Rhino Office Catering & Party Platter Box Builder:** Custom sandwich box lunch calculator for Uptown and South End offices.
- **Rhino Rare Bottle Release & Natural Wine Club:** Monthly allocation notification subscription for local beer and wine geeks.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or online payment processing engine.
- No submission forms of any kind (no contact, order, or feedback forms).
- No automated SMS or email marketing tools.
- No live table seating reservation integration.

### Available for Production Scope

- Custom zero-commission direct ordering mobile app.
- Interactive multi-location taplist and beer cellar browser.
- Digital Queen City gift card engine.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs rhino-market-and-deli` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
