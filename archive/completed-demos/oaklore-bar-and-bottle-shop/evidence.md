# Oaklore Bar & Bottle Shop — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Oaklore Bar & Bottle Shop
- **Slug:** `oaklore-bar-and-bottle-shop`
- **Audit Grade / Disposition / Score:** A / YES / 97
- **Audit Batch:** 14
- **Verification Date:** August 24, 2026

## Verification Sources

- [Oaklore Distilling Co. Official Website](https://oakloredistilling.com)
- [Axios Charlotte — Oaklore Distilling Feature](https://axios.com)
- [Bourbon Obsessed — Oaklore Distilling Profile](https://bourbonobsessed.com)

## Original Audit Weakness

Oaklore relies on basic Shopify commerce pages and third-party event calendars. Located at 11136 Monroe Rd, it lacks an owned digital showcase capturing its grain-to-glass North Carolina distillation process, custom barrel-aged cocktail craft, fire-pit patio lounge ambiance, and distillery tasting room directives.

## Creative Brief

### Verified Visual / Content Anchors

1. **Charlotte / Matthews NC Location:** 11136 Monroe Rd, Matthews NC 28105 (Monroe Rd / Charlotte Metro).
2. **Grain-to-Glass Craft Specialties:** Small-Batch Four Grain Bourbon, NC Straight Rye Whiskey, Barrel-Aged Smoked Old Fashioned, Botanical Vodka & Gin, Custom Spirit Tasting Flights, & Fire-Pit Patio Hospitality.
3. **Contact & Operating Hours:** Phone (704) 617-0500; Mon–Thu 11:00 AM – 9:00 PM | Fri–Sat 11:00 AM – 11:00 PM | Sun 12:00 PM – 6:00 PM.

### Core Design Moves

1. **Warm Sculptural Display Serif Typography:** Warm industrial display serif (*DM Serif Display*) paired with clean body sans (*Plus Jakarta Sans*) and cooperage barrel proof mono (*Space Mono*).
2. **Charred Oak & Burnished Copper Palette:** Artisanal distillery palette anchored in charred white oak timber (`#1C1008`), burnished copper amber (`#C25E2E`), honeyed bourbon gold (`#F59E0B`), and toasted grain cream (`#FEF3C7`).
3. **"The Distilled Spirits & Barrel-Aged Cocktail Matrix":** Matrix-style dual column layout (`grain-to-glass-distillation-craft.html` & `menu.html`) showcasing award-winning North Carolina whiskeys alongside house barrel-aged cocktails and tasting room flights.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Nora Mac’s Traditional Irish Pub` — Dublin Celtic Public House with Cinzel fonts and Stout Onyx/Shamrock Emerald.
2. `NoDa Bodega` — Bohemian Arts Deli with Bungee fonts and Forest Olive/Mustard Relish.
3. `No Proof` — Modern Luxe Speakeasy with Prata fonts and Obsidian Onyx/Botanical Emerald.

### Divergent Choices for Oaklore

- **Hero Composition:** Master Copper Pot Still & Charred White Oak Distillery Vault split-hero layout: left side features a Copper Pot Still Stamp badge (`"GRAIN-TO-GLASS CRAFT DISTILLERY & BOTTLE VAULT • MATTHEWS CHARLOTTE"`), warm industrial display typography (*DM Serif Display*), deep charred oak & burnished copper palette, and right side features a bold framed hero image of golden small-batch bourbon and artisanal tasting lounge ambiance.
- **Section Rhythm:** Replaced standard card grids with **Oaklore Vault Cards** (`oaklore-vault-card`) and Charlotte / Matthews distillery highlights.
- **HTML Vocabulary:** Completely unique class names (`oaklore-header`, `oaklore-brand`, `distillery-hero-stage`, `oaklore-seal-badge`, `oaklore-vault-card`, `oaklore-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 11136 Monroe Rd in Matthews NC 28105 | `visit.html`, `index.html`, `concept.html` | [Oaklore Distilling Co. Official Website](https://oakloredistilling.com) |
| Operating hours: Mon-Thu 11am-9pm, Fri-Sat 11am-11pm, Sun 12pm-6pm | `visit.html`, `index.html` | [Oaklore Distilling Co. Official Website](https://oakloredistilling.com) |
| Phone number: (704) 617-0500 | `visit.html`, `index.html` | [Oaklore Distilling Co. Official Website](https://oakloredistilling.com) |
| Grain-to-glass spirits (Four Grain Bourbon, NC Straight Rye Whiskey) | `menu.html`, `grain-to-glass-distillation-craft.html` | [Bourbon Obsessed Profile](https://bourbonobsessed.com) |
| Tasting room, bottle shop, and fire-pit patio hospitality | `concept.html`, `barrel-aged-cocktails-craft.html` | [Axios Charlotte Feature](https://axios.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Oaklore Single Barrel Selection & Private Cask Engine:** Custom barrel allocation and private bottling club portal.
- **Oaklore VIP Distillery Tour & Master Distiller Class Engine:** Interactive spirits tasting and masterclass booking portal.
- **Oaklore Express Bottle Reserve & Pickup Line:** Mobile bottle shop reservation system.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or online payment processing engine.
- No submission forms of any kind (no contact, order, or feedback forms).
- No automated SMS or email marketing tools.
- No live table seating reservation integration.

### Available for Production Scope

- Custom zero-commission direct bottle reservation app.
- Interactive distillery barrel aging tracker.
- Private fire-pit lounge buyout booking engine.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs oaklore-bar-and-bottle-shop` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
