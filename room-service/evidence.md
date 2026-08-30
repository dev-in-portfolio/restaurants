# Room Service — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Room Service
- **Slug:** `room-service`
- **Audit Grade / Disposition / Score:** A / YES / 98
- **Audit Batch:** 18
- **Verification Date:** August 26, 2026

## Verification Sources

- [Room Service CLT Official Portal](https://roomserviceclt.com)
- [Camp North End Directory](https://camp.nc)
- [Axios Charlotte Camp North End Guide](https://axios.com)

## Original Audit Weakness

Room Service relies on basic social media announcements and generic venue directories. Despite its evocative "boutique hotel lounge" design narrative and high foot-traffic Camp North End destination status, it lacks a dedicated interactive digital experience showcasing its bespoke seasonal cocktail menu, sandwich craft, guest room aesthetics, and Camp North End parking & event directives.

## Creative Brief

### Verified Visual / Content Anchors

1. **Camp North End Keswick District:** 701 Keswick Ave, Suite 105, Charlotte NC 28206.
2. **Hotel Lounge & Cocktail Offerings:** Bespoke Craft Cocktails (The Bellhop Old Fashioned, Midnight Check-In Gin Fizz, Penthouse Espresso Martini, Velvet Keycard Spritz, Smoked Mezcal Paloma), Gourmet Artisanal Sandwiches (House Pastrami Reuben on Marbled Rye, Whipped Truffled Feta with Warm Herb Pita, Smoked Turkey Panini, Warm Marcona Almonds & Pickles), and Camp North End patio lounge seating.
3. **Contact & Operating Hours:** Official Web: roomserviceclt.com; Monday: Closed | Tuesday: 4:00 PM – 9:00 PM | Wed–Thu: 11:00 AM – 10:00 PM | Fri–Sat: 11:00 AM – 11:00 PM | Sunday: 12:00 PM – 8:00 PM.

### Core Design Moves

1. **Luxurious Retro Mid-Century Display Serif Typography:** Mid-century boutique hotel display serif (*DM Serif Display*) paired with clean body sans (*Plus Jakarta Sans*) and hotel guest folio mono (*Space Mono*).
2. **Deep Velvet Brass & Champagne Gold Palette:** Upscale boutique hotel lounge palette anchored in deep velvet brass dark (`#181512`), champagne gold (`#E2BA70`), olive moss (`#4A5D4E`), keycard wine (`#9E2A2B`), silk linen beige (`#FDFBF7`), and pure white.
3. **"The Bespoke Cocktail Folio & Gourmet Sandwich Matrix":** Matrix-style dual column layout (`cocktails-and-hotel-bar-craft.html` & `menu.html`) showcasing handcrafted signature libations, curated natural wines, pressed artisan sandwiches, and savory shareable plates.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Ricko’s Churro Bar` — Modern Mexican Churreria with Outfit and Cinnamon Terracotta/Dulce Gold.
2. `Riceblossom` — Imperial Chengdu Fire & Szechuan Wok Chamber with Cinzel and Lacquer Red/Szechuan Gold.
3. `Rhino Market & Deli` — Modern Urban Bodega & Craft Deli with Space Grotesk and Slate/Hunter Green/Mustard Gold.
4. `Ramen Bar Kazoku` — Tokyo Izakaya & Midnight Ramen Sanctuary with Sora and Sumi Ink/Torii Vermilion.

### Divergent Choices for Room Service

- **Hero Composition:** Mid-Century Retro Hotel Lounge & Cocktail Parlor split-hero layout: left side features a Room Service Hotel Keycard Seal badge (`"BOUTIQUE HOTEL LOUNGE • MID-CENTURY COCKTAIL PARLOR • CAMP NORTH END"`), luxurious hotel display serif (*DM Serif Display*), champagne gold & velvet brass palette, and right side features a framed hero image of an artisanal crystal-glass cocktail with citrus twist on a dark marble lounge bar.
- **Section Rhythm:** Replaced standard card grids with **Room Service Vault Cards** (`roomservice-vault-card`) and Camp North End Keswick district cocktail parlor highlights.
- **HTML Vocabulary:** Completely unique class names (`roomservice-header`, `roomservice-brand`, `lounge-hero-stage`, `roomservice-seal-badge`, `roomservice-vault-card`, `roomservice-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 701 Keswick Ave, Suite 105 in Camp North End Charlotte NC | `visit.html`, `index.html`, `concept.html` | [Room Service CLT Official Portal](https://roomserviceclt.com) |
| Operating hours: Tue 4-9, Wed-Thu 11-10, Fri-Sat 11-11, Sun 12-8, Mon Closed | `visit.html`, `index.html` | [Room Service CLT Official Portal](https://roomserviceclt.com) |
| Official web contact: roomserviceclt.com | `visit.html`, `index.html` | [Room Service CLT Official Portal](https://roomserviceclt.com) |
| Inspired by boutique hotel bars, serving craft cocktails, sandwiches & bites | `menu.html`, `cocktails-and-hotel-bar-craft.html` | [Axios Charlotte Camp North End Guide](https://axios.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Room Service Penthouse Cocktail & VIP Table Booking:** Digital reservations and bottle service concierge.
- **Room Service Private Event & Cocktail Social Estimator:** Private buy-out calculator for Camp North End celebrations.
- **Room Service Keycard Club Loyalty Pass:** Digital VIP keycard rewards engine for cocktail regulars.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or online payment processing engine.
- No submission forms of any kind (no contact, order, or feedback forms).
- No automated SMS or email marketing tools.
- No third-party delivery dispatch integration.

### Available for Production Scope

- Custom zero-commission direct mobile pickup app.
- Interactive cocktail masterclass ticketing engine.
- Digital hotel keycard gift voucher system.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs room-service` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
