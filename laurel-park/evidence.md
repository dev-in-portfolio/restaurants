# Laurel Park — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Laurel Park
- **Slug:** `laurel-park`
- **Audit Grade / Disposition / Score:** A / YES / 100
- **Audit Batch:** 11
- **Verification Date:** August 25, 2026

## Verification Sources

- [Laurel Park Official Website](https://laurelparkclt.com)
- [SouthPark Community Merchant Directory](https://southparkclt.org)
- [QC Exclusive Charlotte Dining Review](https://qcexclusive.com)

## Original Audit Weakness

Laurel Park relies on basic OpenTable booking widgets and fragmented third-party event directory pages. Located in high-profile SouthPark on Congress St, it lacks an owned digital showcase capturing its scratch pasta extrusion craft, wood-fired hearth grilling, 2,000 sq ft covered garden veranda, private dining suites, and SouthPark valet directives.

## Creative Brief

### Verified Visual / Content Anchors

1. **SouthPark Charlotte Location:** 4201 Congress St, Unit 190, Charlotte NC 28209 (across from SouthPark Mall).
2. **New American & Mediterranean Specialties:** House-Extruded Truffle Pappardelle with Wild Mushrooms, Wood-Grilled Prime Dry-Aged Ribeye, Pan-Seared Chilean Sea Bass with Meyer Lemon Beurre Blanc, 2,000-sq-ft Covered Botanical Veranda, and Sommelier Wine Library.
3. **Contact & Operating Hours:** Phone (980) 265-4201; Lunch Mon–Fri 11:30 AM – 2:30 PM | Dinner Daily 5:00 PM – 10:00 PM | Weekend Brunch Sat–Sun 10:30 AM – 3:00 PM | Bar Bites Daily 2:30 PM – 5:00 PM.

### Core Design Moves

1. **Refined Botanical Display Serif Typography:** High-elegance editorial serif (*Cormorant Garamond*) paired with clean body sans (*Plus Jakarta Sans*) and SouthPark estate ticket mono (*Space Mono*).
2. **Mediterranean Laurel Emerald & Sandstone Ochre Palette:** Upscale SouthPark garden palette anchored in deep laurel emerald (`#064E3B`), midnight jade (`#022C22`), warm sandstone ochre (`#D97706`), fresh mint (`#10B981`), and crisp sandstone linen (`#F0FDF4`).
3. **"The Wood-Fired Hearth & Handmade Pasta Matrix":** Matrix-style dual column layout (`hearth-grill-and-handmade-pasta-craft.html` & `menu.html`) showcasing house-extruded pastas and wood-grilled steaks alongside pan-seared seafood and botanical veranda cocktails.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Littl Madeleine` — Korean-French Haute Pâtisserie with Italiana and Rose Blush/Plum Velvet.
2. `Pertinacious Coffee` — Modern Specialty Roastery with Epilogue and Espresso Dark/Tangerine Blossom.
3. `Persuasian Restaurant` — Dilworth Asian Fusion Lounge with Playfair Display and Burgundy Velvet/Gold Leaf.

### Divergent Choices for Laurel Park

- **Hero Composition:** SouthPark Mediterranean Veranda & Botanical Hearth split-hero layout: left side features a SouthPark Botanical Estate Seal badge (`"CONTEMPORARY NEW AMERICAN & BOTANICAL VERANDA • SOUTHPARK CHARLOTTE"`), sleek botanical serif typography (*Cormorant Garamond*), deep laurel emerald & sandstone ochre palette, and right side features a framed hero image of artisanal botanical cocktails on the garden veranda.
- **Section Rhythm:** Replaced standard card grids with **Laurel Vault Cards** (`laurel-vault-card`) and SouthPark fine dining highlights.
- **HTML Vocabulary:** Completely unique class names (`laurel-header`, `laurel-brand`, `veranda-hero-stage`, `laurel-seal-badge`, `laurel-vault-card`, `laurel-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 4201 Congress St Unit 190 in SouthPark Charlotte NC | `visit.html`, `index.html`, `concept.html` | [Laurel Park Official Website](https://laurelparkclt.com) |
| Operating hours: Lunch Mon-Fri, Dinner Daily 5-10PM, Weekend Brunch | `visit.html`, `index.html` | [Laurel Park Official Website](https://laurelparkclt.com) |
| Direct phone: (980) 265-4201 | `visit.html`, `index.html` | [SouthPark CLT Directory](https://southparkclt.org) |
| New American & Mediterranean cuisine, handmade pasta & wood-grilled steaks | `menu.html`, `hearth-grill-and-handmade-pasta-craft.html` | [QC Exclusive Dining Guide](https://qcexclusive.com) |
| 2,000 sq ft covered garden veranda & botanical cocktail program | `menu.html`, `botanical-veranda-and-wine-craft.html` | [Laurel Park Official Website](https://laurelparkclt.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Laurel Park VIP SouthPark Table & Veranda Reservation Engine:** Table selection and covered outdoor garden dining booking app.
- **Laurel Park Sommelier Wine Cellar Locker Membership:** Private wine locker reserve and cellar allocation subscription.
- **Laurel Park Private Dining Suite Event Booking Calculator:** Interactive event menu builder for SouthPark business dinners and rehearsal banquets.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or online payment processing engine.
- No submission forms of any kind (no contact, order, or feedback forms).
- No automated SMS or email marketing tools.
- No live table seating reservation integration.

### Available for Production Scope

- Custom zero-commission direct private dining planner.
- Interactive wine and chef tasting menu pairing app.
- Digital SouthPark gift card engine.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs laurel-park` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
