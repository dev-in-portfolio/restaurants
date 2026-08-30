# Tap & Vine — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Tap & Vine
- **Slug:** `tap-and-vine`
- **Audit Grade / Disposition / Score:** A / YES / 100
- **Audit Batch:** 21
- **Verification Date:** August 26, 2026

## Verification Sources

- [Official Tap & Vine Web Portal](https://tapandvinenc.com/)
- [Toast POS Order Listing for Tap & Vine Stonecrest](https://toasttab.com/)
- [Charlotte Magazine Wine & Dining Guide](https://charlottemagazine.com)
- [Stonecrest at Piper Glen Directory](https://shopstonecrest.com)

## Original Audit Weakness

Tap & Vine is South Charlotte’s quintessential wine bar and scratch tapas lounge, located at 7828 Rea Road in Stonecrest at Piper Glen (with a sister location at Quail Corners on Park Road). Famous for its vibrant communal atmosphere, curated cellar featuring 60+ wines by the glass and bottle, and upscale Mediterranean-American small plates (lamb lollipops, filet medallions, arancini, artisan flatbreads), Tap & Vine is an essential evening destination for Ballantyne and Piper Glen residents. Third-party aggregator scrapers frequently miscategorize it as an ordinary tavern or sports bar, ignoring its elevated sommelier cellar program, scratch small-plate culinary craftsmanship, and stylish late-night lounge atmosphere.

## Creative Brief

### Verified Visual / Content Anchors

1. **Stonecrest at Piper Glen Location:** 7828 Rea Rd, Charlotte, NC 28277 (with Quail Corners sister location at 8426 Park Rd).
2. **Weekly Operating Hours:** Mon–Thu 11:30 AM – 10:00 PM, Fri–Sat 11:30 AM – 12:00 AM (Midnight), Sun 11:30 AM – 9:00 PM.
3. **Scratch Mediterranean-American Tapas:** Grilled rosemary lamb lollipops with fingerling potatoes, crispy arborio arancini with marinara, tender filet mignon medallions, and roasted beet & burrata salad.
4. **Artisan Oven-Baked Flatbreads:** Crisp hand-stretched flatbreads topped with prosciutto, goat cheese, baby arugula, wild mushrooms, and white truffle oil.
5. **Curated Cellar & Craft Libations:** Expansive wine list spanning Napa Valley Cabernets, Old World Bordeaux and Chianti, craft draft beer rotations, and signature seasonal cocktails.

### Core Design Moves

1. **Cellar Cabernet & Velvet Champagne Palette:** Rich cellar obsidian (`#120f12`), tasting room slate (`#211a20`), cabernet reserve (`#8c263e`), champagne gold (`#d4af37`), and crisp linen white (`#f9f7f5`).
2. **Upscale Lounge & Enoteca Typography:** Sophisticated editorial serif (*Cinzel*) paired with clean geometric sans (*Plus Jakarta Sans*) and monospaced vintage cellar labels (*Space Mono*).
3. **Verified Culinary Photography:** A glass of red wine reflecting glowing lounge lights at a polished bar; grilled lamb chops with roasted garlic, rosemary, and fingerling potatoes; and an oven-crisped flatbread with melted cheese and fresh wild arugula.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Tabla Indian Restaurant` — Ballantyne Indian restaurant with Masala Obsidian, Terracotta Slate, Royal Saffron, and Tandoori Paprika.
2. `Taipei Express` — Historic Eastover Chinese/Taiwanese wok kitchen with Imperial Wok Lacquer, Porcelain Slate, Fiery Wok Crimson, and Imperial Gold.
3. `SWIRL Dessert Bar` — South End dessert bar with Berry Midnight, Parlor Slate, Frosted Strawberry, and Buttercream Champagne.
4. `Sweet Lew's BBQ` — Belmont smokehouse with Pit Charcoal, Weathered Timber, Smoldering Ember, and Barbecue Honey.

### Divergent Choices for Tap & Vine

- **Hero Composition:** Upscale wine lounge split-hero with Stonecrest kicker (`"STONECREST AT PIPER GLEN • 7828 REA ROAD • SCRATCH TAPAS & CURATED CELLAR"`), cabernet reserve and champagne gold accents, featuring a glowing red wine pour, anchored by a floating hero badge (`Tap & Vine | 7828 Rea Rd • Wine Bar & Scratch Tapas Lounge`).
- **Section Rhythm:** Three-card standards grid without emojis highlighting "Curated Global Cellar", "Scratch Tapas Craft", and "Oven-Fired Flatbreads", followed by dual alternating highlight banners.
- **HTML Vocabulary:** Bespoke classes (`tapvine-header`, `tapvine-brand`, `tapvine-hero-stage`, `tapvine-hero-badge`, `tapvine-standards-section`, `tapvine-standard-card`, `tapvine-highlight-banner`, `tapvine-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 7828 Rea Rd, Charlotte, NC 28277 (Stonecrest) | `visit.html`, `index.html`, `concept.html` | [Official Web Portal](https://tapandvinenc.com/) |
| Hours: Mon-Thu 11:30am-10pm, Fri-Sat 11:30am-12am, Sun 11:30am-9pm | `visit.html`, `index.html` | [Toast POS Listing](https://toasttab.com/) |
| Serves Lamb Lollipops, Arancini, Flatbreads, Filet Medallions, Wine | `scratch-tapas-and-artisan-flatbreads.html`, `menu.html` | [Official Menu](https://tapandvinenc.com/) |
| Features curated 60+ wines by glass and bottle, craft cocktails | `curated-wine-cellar-and-cocktail-craft.html`, `index.html` | [Charlotte Magazine Feature](https://charlottemagazine.com) |
| Operates in South Charlotte (Stonecrest & Quail Corners) | `concept.html`, `visit.html` | [Stonecrest Directory](https://shopstonecrest.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Sommelier Wine Tasting Flight Reservations:** Private tasting table booking engine with food pairing pre-selection.
- **South Charlotte Corporate Cocktail & Tapas Buyout Engine:** Interactive event space calculator for corporate receptions and milestone parties.
- **Quarterly Wine Club Subscription:** Curated bottle pickup club with tasting notes and members-only pairing discounts.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or payment processing engine.
- No submission forms of any kind (no booking, contact, or inquiry forms).
- No live delivery tracking.

### Available for Production Scope

- Interactive wine and tapas pairing recommender widget.
- Live cellar inventory counter for allocated vintage reserve bottles.
- VIP patio seating waitlist.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs tap-and-vine` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
