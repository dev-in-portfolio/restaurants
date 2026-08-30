# Miro Spanish Grille — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Miro Spanish Grille
- **Slug:** `miro-spanish-grille`
- **Audit Grade / Disposition / Score:** A / YES / 89
- **Audit Batch:** 13
- **Verification Date:** August 24, 2026

## Verification Sources

- [Miro Spanish Grille Official Portal](https://www.mirospanishgrille.com)
- [Charlotte's Got A Lot Directory — Miro Spanish Grille](https://www.charlottesgotalot.com)
- [SouthPark CLT Directory — Miro Expansion Profile](https://southparkclt.org)

## Original Audit Weakness

Miro Spanish Grille relies on legacy website templates and basic OpenTable links. Located at 12239 N Community House Rd in Ballantyne, it lacks an owned digital showcase capturing its authentic Spanish culinary artistry, wood-grilled meats, Bomba rice saffron paella craft, and Ballantyne directives.

## Creative Brief

### Verified Visual / Content Anchors

1. **Ballantyne Charlotte Location:** 12239 N Community House Rd, Suite 102, Charlotte NC 28277 (Ballantyne Charlotte off Ballantyne Commons Pkwy).
2. **Spanish Culinary Specialties:** Authentic Saffron Seafood Paella Valenciana (Bomba rice, saffron, lobster, shrimp, mussels, clams, calamari, chorizo), Grilled Lamb Chops, Gambas al Ajillo, Patatas Bravas, Jamón Ibérico, Spanish Rioja & Ribera del Duero Wine Cellar.
3. **Contact & Operating Hours:** Phone (704) 540-7374; Mon–Thu 5:00 PM – 8:45 PM | Fri–Sat 5:00 PM – 9:45 PM | Sun Closed.

### Core Design Moves

1. **Classical Iberian Display Typography:** Classical display serif (*Cinzel*) paired with clean body sans (*Plus Jakarta Sans*) and Spanish bodega cellar mono (*Space Mono*).
2. **Rioja Crimson & Saffron Gold Palette:** Spanish Mediterranean palette anchored in deep Rioja Garnacha crimson (`#881337`), saffron gold (`#EAB308`), Mediterranean azure (`#0284C7`), and warm toasted Andalusian parchment (`#FFFBEB`).
3. **"The Saffron Paella & Tapas Bodega Matrix":** Matrix-style dual column layout (`saffron-paella-craft.html` & `menu.html`) showcasing saffron seafood paella alongside authentic Spanish hot & cold tapas and Rioja fine wines.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Midwood Country Club` — Vintage Plaza Midwood Neon Dive with DM Serif Display fonts and Felt Green/Neon Gold.
2. `Milkbread` — Warm Japanese Shokupan with Plus Jakarta Sans fonts and Honey/Espresso.
3. `Midtown Tavern` — Industrial Brick & Craft Copper with Outfit fonts and Copper Bronze/Barley Amber.

### Divergent Choices for Miro Spanish Grille

- **Hero Composition:** Spanish Mediterranean Sunlit Bodega & Saffron Paella Hearth split-hero layout: left side features a Spanish Tapas Stamp badge (`"AUTHENTIC SPANISH TAPAS & SAFFRON PAELLA • BALLANTYNE CHARLOTTE"`), classical Iberian display serif (*Cinzel*), deep Rioja crimson & saffron gold palette, and right side features a bold framed hero image of golden seafood paella.
- **Section Rhythm:** Replaced standard card grids with **Miro Vault Cards** (`miro-vault-card`) and Ballantyne fine dining highlights.
- **HTML Vocabulary:** Completely unique class names (`miro-header`, `miro-brand`, `rioja-hero-stage`, `iberian-seal-badge`, `miro-vault-card`, `miro-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 12239 N Community House Rd in Charlotte NC 28277 | `visit.html`, `index.html`, `concept.html` | [Miro Spanish Grille Official Portal](https://www.mirospanishgrille.com) |
| Operating hours: Mon-Thu 5pm-8:45pm, Fri-Sat 5pm-9:45pm, Sun Closed | `visit.html`, `index.html` | [Charlotte's Got A Lot Directory](https://www.charlottesgotalot.com) |
| Phone number: (704) 540-7374 | `visit.html`, `index.html` | [Miro Spanish Grille Official Portal](https://www.mirospanishgrille.com) |
| Signature Saffron Seafood Paella Valenciana & Grilled Lamb Chops | `menu.html`, `saffron-paella-craft.html` | [Miro Spanish Grille Official Portal](https://www.mirospanishgrille.com) |
| Authentic Tapas, Gambas al Ajillo, Patatas Bravas, & Rioja Wine Cellar | `menu.html`, `iberian-tapas-craft.html` | [Miro Spanish Grille Official Portal](https://www.mirospanishgrille.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Miro Direct Table Reservation Engine:** Owned reservation management portal with SMS confirmations.
- **Miro Spanish Wine Club & Tasting Pass:** Exclusive VIP cellar tasting subscription pass.
- **Miro Private Dining & Corporate Paella Banquet Engine:** Custom private dining and corporate event booking engine.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or online payment processing engine.
- No submission forms of any kind (no contact, order, or feedback forms).
- No automated SMS or email marketing tools.
- No live table seating reservation integration.

### Available for Production Scope

- Custom zero-commission direct mobile table reservation app.
- Interactive custom paella banquet & corporate event calculator.
- Custom sommelier wine pairing and bottle cellar management portal.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs miro-spanish-grille` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
