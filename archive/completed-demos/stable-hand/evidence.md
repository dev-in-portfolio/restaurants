# Stable Hand — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Stable Hand
- **Slug:** `stable-hand`
- **Audit Grade / Disposition / Score:** A / YES / 100
- **Audit Batch:** 20
- **Verification Date:** August 26, 2026

## Verification Sources

- [Official Stable Hand Website](https://stablehandclt.com)
- [Axios Charlotte South End Coffee & Wine Profile](https://axios.com)
- [Charlotte's got a lot Cafe Feature](https://charlottesgotalot.com)
- [Joe Coffee Stable Hand Partner Page](https://joe.coffee)

## Original Audit Weakness

Stable Hand is a beloved neighborhood cafe, specialty coffee bar (partnered with HEX Coffee Roasters), all-day scratch breakfast and lunch kitchen, and natural wine bar located at 125 Remount Road (Suite B) in Charlotte's vibrant South End. While highly celebrated for its creative seasonal beverages (such as miso butterscotch and rosemary lattes), scratch breakfast sandwiches on toasted brioche, savory grain porridge bowls, and biodynamic natural wines, generic directory listings often reduce it to a simple coffee counter, missing its extensive from-scratch kitchen menu, evening wine hours, and community-centric South End space.

## Creative Brief

### Verified Visual / Content Anchors

1. **South End Remount Road Location:** Situated at 125 Remount Rd, Suite B, Charlotte, NC 28203.
2. **Weekly Operational Schedule:** Monday 7:00 AM – 5:00 PM; Tuesday – Saturday 7:00 AM – 7:00 PM; Sunday 8:00 AM – 5:00 PM.
3. **HEX Coffee Roasters Partnership:** Pour-overs, espresso, and seasonal house syrups including rosemary, miso butterscotch, and iced matcha tonics.
4. **All-Day Scratch Daytime Kitchen:** Breakfast sandwiches on toasted brioche with pasture-raised eggs and thick bacon, avocado sourdough toast with poached eggs, savory rice porridge bowls, Greek yogurt bowls with house-made lemon curd, crispy sumac potato wedges, and Whisk + Wood pastries.
5. **Natural & Biodynamic Wine Program:** Curated low-intervention orange wines, pet-nats, and chilled reds available by the glass, flight, and retail bottle.

### Core Design Moves

1. **Warm Botanical Oat & Terracotta Clay Palette:** Rich espresso obsidian (`#141312`), warm oat parchment (`#f8f6f0`), earthy sage green (`#5a755d`), warm terracotta clay (`#c96c44`), and toasted honey gold (`#df9b3e`).
2. **Contemporary Editorial Typography:** Clean modern serif (*Cinzel*) paired with functional geometric sans (*Plus Jakarta Sans*) and monospaced roast & harvest tags (*Space Mono*).
3. **Authentic Cafe & Brunch Photography:** Gorgeous rosetta latte art in a matte ceramic cup, scratch toasted brioche breakfast sandwich with dripping farm egg, and thick-cut avocado sourdough toast with poached eggs.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Spaghett` — Intimate Italian craft pasta house with Cinzel and Heritage Charcoal/Antique Brick/Saffron Gold/Florentine Terracotta.
2. `Somewhere CLT` — 25+ Lounge with Cinzel and Night Obsidian/Plum/Neon Magenta/Electric Violet.
3. `Southern Pecan Gulf Coast Kitchen` — Lowcountry coastal kitchen with Cinzel and Cypress Obsidian/Roasted Pecan/Buttered Gold/Marshland Sage.
4. `South End Hideaway` — Social club & lounge with Cinzel and Nightlife Obsidian/Velvet Slate/Neon Cyan/Burnished Gold.

### Divergent Choices for Stable Hand

- **Hero Composition:** South End daytime cafe split-hero with Remount Road kicker (`"SOUTH END • 125 REMOUNT ROAD • SPECIALTY COFFEE, SCRATCH KITCHEN & NATURAL WINE"`), botanical sage and terracotta accents, featuring rosetta latte art on blond wood, anchored by a floating hero badge (`Stable Hand CLT | 125 Remount Rd • HEX Coffee & All-Day Cafe`).
- **Section Rhythm:** Three-card standards grid without emojis highlighting "HEX Coffee & Seasonal Syrups", "All-Day Scratch Kitchen", and "Natural & Biodynamic Wines", followed by dual alternating highlight banners.
- **HTML Vocabulary:** Bespoke classes (`stablehand-header`, `stablehand-brand`, `stablehand-hero-stage`, `stablehand-hero-badge`, `stablehand-standards-section`, `stablehand-standard-card`, `stablehand-highlight-banner`, `stablehand-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 125 Remount Rd, Suite B, Charlotte, NC 28203 | `visit.html`, `index.html`, `concept.html` | [Official Website](https://stablehandclt.com) |
| Operating hours: Mon 7am-5pm, Tue-Sat 7am-7pm, Sun 8am-5pm | `visit.html`, `index.html` | [Official Website Hours](https://stablehandclt.com) |
| Serves HEX Coffee espresso, pour-overs, and seasonal house syrups | `specialty-coffee-and-hex-roasters-craft.html`, `menu.html` | [Axios South End](https://axios.com) |
| Scratch kitchen features breakfast sandwiches, avocado toast, and grain bowls | `scratch-kitchen-and-natural-wine-cellar.html`, `menu.html` | [Charlotte's got a lot](https://charlottesgotalot.com) |
| Natural, biodynamic wine bottles and glasses available | `scratch-kitchen-and-natural-wine-cellar.html`, `menu.html` | [Official Website](https://stablehandclt.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Mobile Coffee Pre-Order & Contactless Pickup App:** Custom white-label express order queue for morning rush commuters.
- **Natural Wine Subscription & Bottle Club:** Monthly 2-pack and 4-pack natural wine subscription with sommelier tasting cards.
- **Home Espresso & Pour-Over Masterclasses:** Online workshop booking engine for barista-guided brewing classes.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or payment processing engine.
- No submission forms of any kind (no booking, contact, or inquiry forms).
- No live table booking or delivery integration.

### Available for Production Scope

- Custom zero-commission mobile order-ahead platform.
- Integrated bottle shop retail checkout with local pickup.
- Private evening cafe event reservations.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs stable-hand` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
