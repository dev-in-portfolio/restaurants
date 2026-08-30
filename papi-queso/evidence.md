# Papi Queso — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Papi Queso
- **Slug:** `papi-queso`
- **Audit Grade / Disposition / Score:** A / YES / 95
- **Audit Batch:** 15
- **Verification Date:** August 24, 2026

## Verification Sources

- [Papi Queso Official Website](https://papiquesoclt.com)
- [Optimist Hall Charlotte Directory](https://optimisthall.com)
- [Charlotte’s Got A Lot Dining Guide](https://charlottesgotalot.com)

## Original Audit Weakness

Papi Queso relies on basic food hall aggregator listings and standard online ordering links. Located inside bustling Optimist Hall at 1115 N Brevard St, it lacks an owned digital showcase highlighting its artisanal cheese blends, slow-smoked BBQ integration, scratch tomato soup pairing, and food hall pick-up directives.

## Creative Brief

### Verified Visual / Content Anchors

1. **Optimist Hall Charlotte Location:** 1115 N Brevard St, Suite 2, Charlotte NC 28206 (Inside Optimist Hall Food Hall).
2. **Gourmet Grilled Cheese Specialties:** The Legendary "Pig Mac" (hickory-smoked pulled pork, creamy macaroni & cheese, caramelized pickled red onions on golden butter-toasted sourdough), "Lil Cheesy" three-cheese artisan melt, "Texas Cheese Steak", velvet tomato soup dippers, and truffle parmesan tots.
3. **Contact & Operating Hours:** Phone (704) 999-1764; Mon–Thu 11:00 AM – 9:00 PM | Fri–Sat 11:00 AM – 10:00 PM | Sun 11:00 AM – 9:00 PM.

### Core Design Moves

1. **Ultra-Bold Neo-Grotesque Display Typography:** Punchy, modern display sans (*Space Grotesk*) paired with clean body sans (*Plus Jakarta Sans*) and cheese melt station ticket mono (*Space Mono*).
2. **Melted Cheddar Gold & Tomato Velvet Scarlet Palette:** Rich comfort food palette anchored in molten cheddar gold (`#F59E0B`), roasted tomato soup scarlet (`#DC2626`), toasted sourdough crust dark brown (`#451A03`), and rich butter cream (`#FEF3C7`).
3. **"The Gourmet Melt & Velvet Tomato Soup Matrix":** Matrix-style dual column layout (`gourmet-melt-craft.html` & `menu.html`) showcasing artisan sourdough melts alongside velvet soup dippers and loaded tater tots.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Panda’s Den` — Master Wok-Fired Imperial Chinese Kitchen with Cinzel fonts and Vermilion/Amber.
2. `Olivelli Deli` — Modern Italian Salumeria with Syne fonts and Olive Green/Calabrian Chili.
3. `Oh My Soul` — Afro-Bohemian Botanical Sanctuary with Outfit fonts and Jungle Forest Green/Marigold.

### Divergent Choices for Papi Queso

- **Hero Composition:** Modern Artisan Melt Factory & Optimist Hall Cheese Vault split-hero layout: left side features a Melt Master Stamp badge (`"GOURMET GRILLED CHEESE MELTS • OPTIMIST HALL CHARLOTTE"`), ultra-bold neo-grotesque typography (*Space Grotesk*), molten cheddar gold & tomato scarlet palette, and right side features a bold framed hero image of cheese pull sourdough melts and crispy tots.
- **Section Rhythm:** Replaced standard card grids with **Papi Vault Cards** (`papi-vault-card`) and Optimist Hall food hall highlights.
- **HTML Vocabulary:** Completely unique class names (`papi-header`, `papi-brand`, `melt-hero-stage`, `papi-seal-badge`, `papi-vault-card`, `papi-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 1115 N Brevard St #2 in Optimist Hall, Charlotte NC 28206 | `visit.html`, `index.html`, `concept.html` | [Papi Queso Official Website](https://papiquesoclt.com) |
| Operating hours: Mon-Thu 11am-9pm, Fri-Sat 11am-10pm, Sun 11am-9pm | `visit.html`, `index.html` | [Optimist Hall Directory](https://optimisthall.com) |
| Phone number: (704) 999-1764 | `visit.html`, `index.html` | [Papi Queso Official Website](https://papiquesoclt.com) |
| Signature Pig Mac with pulled pork and mac & cheese on sourdough | `menu.html`, `gourmet-melt-craft.html` | [Papi Queso Official Website](https://papiquesoclt.com) |
| Velvet tomato soup dippers and loaded tater tots | `menu.html`, `tomato-soup-and-sides-craft.html` | [Charlotte’s Got A Lot Guide](https://charlottesgotalot.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Papi Queso Food Hall Fast-Track Mobile Pickup Queue:** Express order-ahead pickup engine for high-volume lunch rushes.
- **Papi Queso Melt Box & Tailgate Platter Catering Engine:** Group catering melt box and tote platter calculator for corporate and game-day events.
- **Papi Queso VIP Melt Club & Cheese Fanatics Rewards:** Customer loyalty points and secret menu access engine.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or online payment processing engine.
- No submission forms of any kind (no contact, order, or feedback forms).
- No automated SMS or email marketing tools.
- No live table seating reservation integration.

### Available for Production Scope

- Custom zero-commission direct mobile melt order app.
- Interactive custom melt and dipping sauce builder.
- Food hall real-time pickup status board.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs papi-queso` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
