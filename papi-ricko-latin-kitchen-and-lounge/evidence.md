# Papi Ricko Latin Kitchen & Lounge — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Papi Ricko Latin Kitchen & Lounge
- **Slug:** `papi-ricko-latin-kitchen-and-lounge`
- **Audit Grade / Disposition / Score:** A / YES / 99
- **Audit Batch:** 15
- **Verification Date:** August 25, 2026

## Verification Sources

- [Axios Charlotte — Papi Ricko Plaza Midwood Feature](https://axios.com)
- [Charlotte’s Got A Lot Latin Dining Guide](https://charlottesgotalot.com)
- [Toast App Papi Ricko Online Ordering](https://toast.app)

## Original Audit Weakness

Papi Ricko relies on basic social media announcements and third-party delivery listings. Located on high-traffic Central Ave next to Moo & Brew and across from Thirsty Beaver, it lacks an owned digital showcase highlighting its chef-driven Latin street fare, birria craft, VIP table reservations, and weekend nightlife experience.

## Creative Brief

### Verified Visual / Content Anchors

1. **Plaza Midwood Charlotte Location:** 1226 Central Ave, Suite A, Charlotte NC 28204 (Plaza Midwood).
2. **Latin Fusion Specialties:** Slow-Braised Beef Birria Tacos with rich dipping consomé, Surf & Turf Tacos, Al Pastor Craft Burger, Mexican Street Corn (Elote), House-Smoked Wings, Passionfruit & Hibiscus Margaritas, and Mezcal craft cocktails.
3. **Contact & Operating Hours:** Phone (980) 636-7687; VIP Table Service (980) 339-1279; Wed–Thu 4pm–11pm | Fri 11am–2am | Sat 11am–2am | Sun 12pm–8pm | Mon–Tue Closed.

### Core Design Moves

1. **High-Energy Contemporary Display Typography:** Stylish geometric sans (*Outfit*) paired with clean body sans (*Plus Jakarta Sans*) and cantina ticket mono (*Space Mono*).
2. **Midnight Agave & Electric Cantina Magenta Palette:** High-energy nightlife palette anchored in midnight agave navy (`#0F172A`), electric cantina magenta pink (`#EC4899`), glowing marigold amber (`#F59E0B`), and neon turquoise mint (`#06B6D4`).
3. **"The Latin Street Tacos & Tropical Cocktail Matrix":** Matrix-style dual column layout (`birria-and-taco-craft.html` & `menu.html`) showcasing slow-braised birria tacos and craft burgers alongside tropical agave cocktails and Latin brunch plates.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Papi Queso` — Gourmet Grilled Cheese Melt Factory with Space Grotesk fonts and Toasted Sourdough/Cheddar Gold.
2. `Panda’s Den` — Master Wok-Fired Imperial Chinese Kitchen with Cinzel fonts and Vermilion/Amber.
3. `Olivelli Deli` — Modern Italian Salumeria with Syne fonts and Olive Green/Calabrian Chili.

### Divergent Choices for Papi Ricko Latin Kitchen & Lounge

- **Hero Composition:** Electric Latin Neon Cantina & Plaza Midwood Lounge Vault split-hero layout: left side features an Electric Latin Cantina Stamp badge (`"LATIN STREET KITCHEN & COCKTAIL LOUNGE • PLAZA MIDWOOD CHARLOTTE"`), contemporary high-energy typography (*Outfit*), midnight agave & electric magenta palette, and right side features a bold framed hero image of golden crispy birria tacos with rich consomé dipping broth.
- **Section Rhythm:** Replaced standard card grids with **Ricko Vault Cards** (`ricko-vault-card`) and Plaza Midwood nightlife & patio highlights.
- **HTML Vocabulary:** Completely unique class names (`ricko-header`, `ricko-brand`, `cantina-hero-stage`, `ricko-seal-badge`, `ricko-vault-card`, `ricko-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 1226 Central Ave #A in Plaza Midwood, Charlotte NC 28204 | `visit.html`, `index.html`, `concept.html` | [Axios Charlotte Feature](https://axios.com) |
| Operating hours: Wed-Thu 4pm-11pm, Fri-Sat 11am-2am, Sun 12pm-8pm | `visit.html`, `index.html` | [Toast App Papi Ricko](https://toast.app) |
| Phone number: (980) 636-7687 / VIP (980) 339-1279 | `visit.html`, `index.html` | [Toast App Papi Ricko](https://toast.app) |
| Founded by Chef Ricky Ortiz (Tacos Rick-O food truck founder) | `concept.html`, `index.html` | [Axios Charlotte Feature](https://axios.com) |
| Signature Birria tacos with consomé, Al Pastor burger, & cocktails | `menu.html`, `birria-and-taco-craft.html` | [Charlotte’s Got A Lot Guide](https://charlottesgotalot.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Papi Ricko VIP Bottle & Lounge Table Reservation Engine:** Interactive table selection and bottle service booking system for weekend DJ nights.
- **Papi Ricko Taco Truck ("Tacos Rick-O") Live Event Tracker & Catering Engine:** Private fiesta and corporate food truck booking calculator.
- **Papi Ricko Latin Beats & Weekend Brunch Ticketed Event Pass:** Integrated ticketing for drag brunches, Latin Urban nights, and holiday celebrations.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or online payment processing engine.
- No submission forms of any kind (no contact, order, or feedback forms).
- No automated SMS or email marketing tools.
- No live table seating reservation integration.

### Available for Production Scope

- Custom zero-commission direct mobile taco order app.
- Interactive VIP lounge table and bottle selection map.
- Live DJ event schedule and ticket booking portal.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs papi-ricko-latin-kitchen-and-lounge` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
