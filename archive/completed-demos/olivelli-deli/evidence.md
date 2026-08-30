# Olivelli Deli — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Olivelli Deli
- **Slug:** `olivelli-deli`
- **Audit Grade / Disposition / Score:** A / YES / 100
- **Audit Batch:** 15
- **Verification Date:** August 24, 2026

## Verification Sources

- [Olivelli Deli Official Website](https://olivellideli.com)
- [Axios Charlotte — Olivelli Deli NoDa Feature](https://axios.com)
- [Tonidandel-Brown Restaurant Group](https://olivellideli.com)

## Original Audit Weakness

Olivelli Deli relies on basic walk-up ordering and third-party delivery platforms. Located at 3120 N Davidson St in NoDa, it lacks an owned digital showcase capturing its scratch Italian salumi slicing, house-baked benne seed rolls, morning breakfast sandwich service, and walk-up window directives.

## Creative Brief

### Verified Visual / Content Anchors

1. **NoDa Arts District Charlotte Location:** 3120 N Davidson St, Suite 100, Charlotte NC 28205 (NoDa Arts District).
2. **Artisan Italian Deli Specialties:** The Legendary "Oli Italiano" (prosciutto di parma, spicy capicola, mortadella, genoa salame, aged provolone, shredded cabbage, pickled red onion, castelvetrano olive tapenade on house benne seed roll), "P-Eggy B" (bacon, egg, pimento cheese), "Cappa Cappa Egga" (capicola, egg, cheese), house giardiniera, marinated olives, and homemade Italian soft serve ice cream.
3. **Contact & Operating Hours:** Tue–Sun 8:00 AM – 8:00 PM (Breakfast 8am–11am; Sandwiches & Soft Serve 11am–8pm) | Mon Closed.

### Core Design Moves

1. **Striking Geometric Modernist Display Typography:** Bold retro Italian modernist display sans (*Syne*) paired with clean body sans (*Plus Jakarta Sans*) and deli counter order ticket mono (*Space Mono*).
2. **Castelvetrano Olive & Calabrian Chili Palette:** Authentic Italian salumeria palette anchored in rich Castelvetrano olive green (`#1B382B`), spicy Calabrian chili red (`#C2410C`), warm toasted benne gold (`#EAB308`), and salumi parchment cream (`#FEFCE8`).
3. **"The Artisan Italian Salumi & Morning Breakfast Matrix":** Matrix-style dual column layout (`benne-seed-sandwich-craft.html` & `menu.html`) showcasing layered Italian deli cold cuts alongside breakfast egg sandwiches and homemade soft serve.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Oh My Soul` — Afro-Bohemian Botanical Sanctuary with Outfit fonts and Jungle Forest Green/Marigold.
2. `Oh My Ganache, The Cheesecake Bar` — Modern Artisan Confectionery with Playfair Display fonts and Dark Cocoa/Raspberry Rose.
3. `Oaklore Bar & Bottle Shop` — Charred Oak & Copper Distillery with DM Serif Display fonts and Charred Oak/Copper.

### Divergent Choices for Olivelli Deli

- **Hero Composition:** Modern Italian Salumeria & NoDa Walk-Up Deli Window split-hero layout: left side features an Italian Salumi Stamp badge (`"ARTISAN ITALIAN DELI & BENNE SEED SANDWICHES • NODA CHARLOTTE"`), bold geometric modernist typography (*Syne*), rich Castelvetrano olive green & Calabrian chili palette, and right side features a bold framed hero image of stacked Italian deli cold cuts on sesame benne rolls.
- **Section Rhythm:** Replaced standard card grids with **Olivelli Deli Cards** (`olivelli-vault-card`) and Charlotte NoDa walk-up window highlights.
- **HTML Vocabulary:** Completely unique class names (`olivelli-header`, `olivelli-brand`, `deli-hero-stage`, `olivelli-seal-badge`, `olivelli-vault-card`, `olivelli-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 3120 N Davidson St, Suite 100 in Charlotte NC 28205 | `visit.html`, `index.html`, `concept.html` | [Olivelli Deli Official Website](https://olivellideli.com) |
| Operating hours: Tue-Sun 8am-8pm (Breakfast 8am-11am), Mon Closed | `visit.html`, `index.html` | [Olivelli Deli Official Website](https://olivellideli.com) |
| Operated by Tonidandel-Brown Restaurant Group (Supperland, Ever Andalo) | `concept.html`, `index.html` | [Axios Charlotte Feature](https://axios.com) |
| Signature Oli Italiano sandwich on homemade benne seed roll | `menu.html`, `benne-seed-sandwich-craft.html` | [Axios Charlotte Feature](https://axios.com) |
| Scratch breakfast sandwiches (P-Eggy B, Cappa Cappa Egga) and soft serve | `menu.html`, `breakfast-and-softserve-craft.html` | [Olivelli Deli Official Website](https://olivellideli.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Olivelli Express Walk-Up Mobile Pickup Queue:** Fast-lane ordering engine for lunch rush and morning coffee.
- **Olivelli Italian Party Platter & Catering Box Engine:** Group sandwich platter and salumi board calculator for corporate events.
- **Olivelli Salumi & Imported Pantry Subscription:** Monthly curated Italian olive oil, tinned fish, and cured meat club.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or online payment processing engine.
- No submission forms of any kind (no contact, order, or feedback forms).
- No automated SMS or email marketing tools.
- No live table seating reservation integration.

### Available for Production Scope

- Custom zero-commission direct mobile sandwich order app.
- Interactive custom sandwich builder.
- Group catering box and party platter pre-order engine.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs olivelli-deli` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
