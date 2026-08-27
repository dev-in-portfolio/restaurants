# Suffolk Punch Brewing — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Suffolk Punch Brewing
- **Slug:** `suffolk-punch-brewing`
- **Audit Grade / Disposition / Score:** A / YES / 100
- **Audit Batch:** 20
- **Verification Date:** August 26, 2026

## Verification Sources

- [Official Suffolk Punch Brewing Portal](https://suffolkpunchbrewing.com/)
- [South End Charlotte Brewery Guide](https://charlottesgotalot.com)
- [Unpretentious Palate Restaurant Directory](https://unpretentiouspalate.com)

## Original Audit Weakness

Suffolk Punch Brewing is an anchor institution in Charlotte's South End, located at 2911 Griffith Street directly along the Charlotte Rail Trail next to the Lynx New Bern Light Rail Station. Beyond operating as a craft brewery producing renowned beers like Pulp Prescription Hazy IPA and Blue Daisy Pilsner, it is an all-day culinary destination featuring an executive chef-driven scratch kitchen, a full morning espresso coffee bar, wood-fired artisan Tuscan flatbreads, double smash burgers, and a massive dog-friendly outdoor pavilion. Generic third-party scraper listings frequently misclassify it as an industrial tasting-room warehouse with food trucks, completely obscuring its dedicated restaurant kitchen, high-craft brunch, and full-service coffee program.

## Creative Brief

### Verified Visual / Content Anchors

1. **South End Rail Trail Anchor:** 2911 Griffith Street, Charlotte, NC 28203.
2. **Weekly Operating Hours:** Monday – Thursday: 11:00 AM – 10:00 PM; Friday: 11:00 AM – 12:00 AM (Midnight); Saturday: 10:00 AM – 12:00 AM (Midnight); Sunday: 10:00 AM – 9:00 PM.
3. **Core Craft Beer Program:** House-brewed flagships including Pulp Prescription Hazy IPA, Blue Daisy Bohemian Pilsner, Daydream Bavarian Hefeweizen, and Hyde Park Amber Ale, poured across expansive tap towers and customizable tasting flights.
4. **Chef-Driven Scratch Kitchen:** Signature SPB Double Smash Burger with garlic parmesan frites, Tuscan-style hand-stretched flatbread pizzas, Mojo Pork Tostones, Ahi Tuna Wonton Nachos, and weekend brunch staples like Carolina BBQ Shrimp & Grits.
5. **Outdoor Beer Garden & Rail Trail Access:** A covered outdoor pavilion and sunlit beer garden seamlessly connected to the pedestrian Rail Trail, welcoming neighbors, cyclists, and leashed dogs.

### Core Design Moves

1. **South End Brewery Copper & Hops Palette:** Deep malt obsidian (`#121312`), weathered brewery brick (`#24201c`), aged brewery copper (`#c87a38`), fresh hop sage (`#4f7a55`), and clean frothy foam (`#fbf8f2`).
2. **Industrial Brewhouse Typography:** Robust display serif (*Cinzel*) paired with contemporary geometric sans (*Plus Jakarta Sans*) and monospaced brewery taplist tags (*Space Mono*).
3. **Verified Culinary & Taproom Photography:** Metal tasting flights of craft beers on a polished bar, double smash burger with crisp golden fries in a gastropub bowl, and artisan hand-stretched Tuscan pizza with blistered crust and fresh basil.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Substrate` — Optimist Park blue-collar enoteca with Cinzel and Vinyl Obsidian/Cellar Slate/Rusted Terracotta/Vermouth Amber.
2. `Stable Hand` — South End specialty coffee & all-day cafe with Cinzel and Espresso Obsidian/Oat Parchment/Sage Green/Terracotta Clay.
3. `Spaghett` — Fourth Ward historic house Italian prix fixe with Cinzel and Heritage Charcoal/Antique Brick/Saffron Gold/Florentine Terracotta.
4. `Somewhere CLT` — 25+ Nightlife Lounge with Cinzel and Night Obsidian/Plum/Neon Magenta/Electric Violet.

### Divergent Choices for Suffolk Punch Brewing

- **Hero Composition:** South End Rail Trail brewhouse split-hero with Griffith Street kicker (`"SOUTH END • 2911 GRIFFITH STREET • CRAFT BREWERY, SCRATCH KITCHEN & BEER GARDEN"`), aged copper and hop sage accents, featuring an eight-pour taproom tasting flight, anchored by a floating hero badge (`Suffolk Punch Brewing | 2911 Griffith St • Brewhouse & Rail Trail Beer Garden`).
- **Section Rhythm:** Three-card standards grid without emojis highlighting "House-Brewed Flagships & Flights", "Chef-Driven Scratch Kitchen", and "Rail Trail Beer Garden & Coffee", followed by dual alternating highlight banners.
- **HTML Vocabulary:** Bespoke classes (`spb-header`, `spb-brand`, `spb-hero-stage`, `spb-hero-badge`, `spb-standards-section`, `spb-standard-card`, `spb-highlight-banner`, `spb-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 2911 Griffith Street, Charlotte, NC 28203 | `visit.html`, `index.html`, `concept.html` | [Official Website](https://suffolkpunchbrewing.com/) |
| Operating hours: Mon-Thu 11am-10pm, Fri 11am-12am, Sat 10am-12am, Sun 10am-9pm | `visit.html`, `index.html` | [Suffolk Punch Brewing Hours](https://suffolkpunchbrewing.com/) |
| Brews Pulp Prescription Hazy IPA, Blue Daisy Pilsner, and seasonal craft beers | `house-brewed-beers-and-taproom-craft.html`, `menu.html` | [Official Taplist](https://suffolkpunchbrewing.com/) |
| Serves SPB Double Burger, Tuscan pizzas, tostones, and weekend brunch | `chef-driven-scratch-kitchen-and-brunch.html`, `menu.html` | [Official Menu](https://suffolkpunchbrewing.com/) |
| Features covered beer garden pavilion directly on the Charlotte Rail Trail | `concept.html`, `visit.html` | [South End Charlotte Guide](https://charlottesgotalot.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Suffolk Punch Mug Club & Growler Society:** Annual membership portal for draft discounts, exclusive can releases, and VIP brewery tours.
- **Private Event & Beer Garden Pavilion Booking:** Online inquiry portal for corporate gatherings, rehearsal dinners, and Rail Trail patio celebrations.
- **Real-Time Taproom Draft Level & Can Inventory Tracker:** Digital live display of keg yields and four-pack cooler availability.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or payment processing engine.
- No submission forms of any kind (no booking, contact, or inquiry forms).
- No live table booking or delivery integration.

### Available for Production Scope

- Interactive draft keg inventory board.
- Integrated private event reservation system.
- Direct-to-table QR ordering integration.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs suffolk-punch-brewing` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
