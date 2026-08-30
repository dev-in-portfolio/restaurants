# Puerta — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Puerta (Puerta CLT)
- **Slug:** `puerta`
- **Audit Grade / Disposition / Score:** A / YES / 98
- **Audit Batch:** 17
- **Verification Date:** August 25, 2026

## Verification Sources

- [Puerta Official Website](https://puertaclt.com)
- [Unpretentious Palate Elizabeth Restaurant Feature](https://unpretentiouspalate.com)
- [Resy Charlotte Verified Profile](https://resy.com)

## Original Audit Weakness

Puerta relies on external reservation widgets (Resy) and basic single-page navigation. Tucked away on 7th St in Elizabeth with its hidden back-door entrance, it lacks an owned digital showcase capturing its 100+ bottle artisanal agave cellar, heirloom nixtamalized masa craft, Oaxacan mole reductions, and Elizabeth back-door access directives.

## Creative Brief

### Verified Visual / Content Anchors

1. **Historic Elizabeth Location:** 1961 E 7th St, Charlotte NC 28204 (decorative entry door located at back of property).
2. **Contemporary Mexican & Agave Specialties:** 100+ Curated Mezcal/Tequila Bottles, Smoked Mezcalitas, Puerta Agave Old Fashioneds, Birria de Res on Heirloom Nixtamalized Corn Tortillas, Fresh Ceviche Mixto, Carne Asada con Mole Negro, and House Churros con Cajeta.
3. **Contact & Operating Hours:** Phone (704) 412-7767; Mon–Thu 12:00 PM – 10:00 PM | Fri 12:00 PM – 12:00 AM (Kitchen 11PM) | Sat 11:00 AM – 12:00 AM (Kitchen 11PM) | Sun 11:00 AM – 10:00 PM.

### Core Design Moves

1. **Sculptural Mesoamerican Serif Typography:** Refined architectural serif (*Marcellus*) paired with clean body sans (*Plus Jakarta Sans*) and Oaxacan mezcal cellar log mono (*Space Mono*).
2. **Smoked Agave Terracotta & Pina Gold Palette:** Rich Mexican agave palette anchored in deep smoked terracotta (`#29150B`), charred charcoal (`#170B04`), agave piña gold (`#D97706`), mole crimson (`#991B1B`), heirloom corn cream (`#FEF3C7`), and clean pure white.
3. **"The 100+ Agave Cellar & Heirloom Masa Matrix":** Matrix-style dual column layout (`agave-cellar-and-mezcal-craft.html` & `menu.html`) showcasing 100+ bottle agave spirits and craft mezcal cocktails alongside nixtamalized heirloom tacos and wood-fired Latin hearth plates.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Plot Twist` — Midwood Garage Lounge with Prata and Midnight Plum/Electric Magenta.
2. `Platform Coffee + Kitchen` — Industrial Railway Roastery with Space Grotesk and Iron/Copper Amber.
3. `Pho Quynh` — Vietnamese Saigon Heritage with Newsreader and Saigon Cinnamon/Broth Amber.

### Divergent Choices for Puerta

- **Hero Composition:** Modern Mexican Agave Vault & Elizabeth Back-Door Speakeasy Sanctuary split-hero layout: left side features an Agave Vault Seal badge (`"100+ AGAVE CELLAR & CONTEMPORARY MEXICAN HEARTH • ELIZABETH CHARLOTTE"`), sculptural serif typography (*Marcellus*), smoked terracotta & piña gold palette, and right side features a framed hero image of heirloom street tacos and wood-fired dishes.
- **Section Rhythm:** Replaced standard card grids with **Puerta Vault Cards** (`puerta-vault-card`) and Elizabeth agave parlor highlights.
- **HTML Vocabulary:** Completely unique class names (`puerta-header`, `puerta-brand`, `agave-hero-stage`, `puerta-seal-badge`, `puerta-vault-card`, `puerta-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 1961 E 7th St in Charlotte NC 28204 (Back-door entrance) | `visit.html`, `index.html`, `concept.html` | [Puerta Official Website](https://puertaclt.com) |
| Operating hours: Mon-Thu 12-10PM, Fri 12PM-12AM, Sat 11AM-12AM, Sun 11AM-10PM | `visit.html`, `index.html` | [Puerta Official Website](https://puertaclt.com) |
| Direct phone: (704) 412-7767 | `visit.html`, `index.html` | [Puerta Official Website](https://puertaclt.com) |
| 100+ curated mezcal and tequila agave spirits library | `menu.html`, `agave-cellar-and-mezcal-craft.html` | [Unpretentious Palate Feature](https://unpretentiouspalate.com) |
| Heirloom nixtamalized tacos, birria, ceviche mixto, mole negro & churros | `menu.html`, `hearth-cooking-and-masa-craft.html` | [Puerta Menu](https://puertaclt.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Puerta 100-Bottle Mezcal Sommelier Flight Builder:** Custom agave tasting flights paired with artisanal sal de gusano and fresh orange slices.
- **Puerta VIP Agave Locker & Tequila Society Pass:** Exclusive reservations and private bottle storage.
- **Puerta Private Back-Room Fiesta & Taco Banquet Calculator:** Large group event dining packages with custom cocktail pairings.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or online payment processing engine.
- No submission forms of any kind (no contact, order, or feedback forms).
- No automated SMS or email marketing tools.
- No live table seating reservation integration.

### Available for Production Scope

- Custom zero-commission direct ordering app.
- Interactive agave flavor wheel & smoke intensity guide.
- Digital Elizabeth dining gift card engine.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs puerta` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
