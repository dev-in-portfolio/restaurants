# Taipei South — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Taipei South
- **Slug:** `taipei-south`
- **Audit Grade / Disposition / Score:** A / YES / 98
- **Audit Batch:** 21
- **Verification Date:** August 26, 2026

## Verification Sources

- [Official Taipei South Web Portal](https://taipeisouth.com/)
- [Charlotte's got a lot Official Culinary Directory](https://charlottesgotalot.com)
- [DoorDash Live Menu for South Charlotte Johnston Rd](https://doordash.com)
- [Mecklenburg County Public Health Records](https://mecknc.gov)

## Original Audit Weakness

Taipei South is South Charlotte’s revered Taiwanese and regional Chinese sit-down culinary institution, located at 10106 Johnston Road in the McMullen Creek corridor. Renowned across Mecklenburg County for its authentic Taiwanese Beef Noodle Soup (Niu Rou Mian) featuring tender slow-braised beef shank in five-spice aromatic broth, handmade pork and napa cabbage dumplings, Three Cup Chicken (San Bei Ji), and crispy master-wok classics like General Tso's Chicken and Szechuan Beef, Taipei South provides a genuine full-service dining room experience with a full bar. Third-party scrapers frequently conflate it with quick-service takeout counters, failing to present its expansive sit-down dining hall, authentic Taiwanese braising traditions, lunch specials, and multi-course banquet capabilities.

## Creative Brief

### Verified Visual / Content Anchors

1. **South Charlotte Johnston Road Location:** 10106 Johnston Rd, Charlotte, NC 28210 (McMullen Creek Market corridor).
2. **Weekly Operating Schedule:** Mon–Fri 11:30 AM – 3:00 PM (Lunch) & 5:00 PM – 9:30 PM (Dinner); Sat–Sun 12:00 PM – 3:00 PM (Lunch) & 5:00 PM – 9:30 PM (Dinner).
3. **Taiwanese Beef Noodle Soup (Niu Rou Mian):** Chewy wheat noodles in a deeply aromatic bone broth infused with star anise, ginger, rock sugar, and soy, topped with thick chunks of slow-braised beef shank, baby greens, and fresh scallions.
4. **Crispy Master-Wok Classics:** Glistening wok-fried General Tso's Chicken tossed with roasted whole red chilies and sweet-tangy garlic sauce, served with steamed broccoli and fluffy white jasmine rice.
5. **Handmade Dumplings & Small Plates:** Plump steamed pork and napa cabbage jiaozi served with aged Zhenjiang black vinegar and chili oil; crispy scallion pancakes; and Sichuan Dan Dan noodles.

### Core Design Moves

1. **Imperial Jade & Taiwanese Lacquer Palette:** Taiwanese lacquer obsidian (`#121014`), night market slate (`#211d24`), imperial banquet surface (`#2b2530`), jade celadon (`#3d7a64`), Taiwanese imperial gold (`#d4a237`), and steamed rice white (`#f9f8f6`).
2. **Traditional Taiwanese Banquet Typography:** Stately classical display serif (*Cinzel*) paired with clean legible modern body (*Plus Jakarta Sans*) and monospaced kitchen indexes (*Space Mono*).
3. **Verified Culinary Photography:** A steaming bowl of authentic Taiwanese Beef Noodle Soup with braised shank and green scallions; a platter of freshly steamed handmade pork and cabbage dumplings with dipping sauce and chopsticks; and a glistening bowl of crispy General Tso's chicken with whole chili peppers and broccoli.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Thai House` — Charlotte Thai institution with Teakwood Obsidian, Bamboo Slate, Golden Saffron, and Lemongrass Green.
2. `Tavern on the Tracks` — South End sports pub with Industrial Iron, Ballast Charcoal, Wing Amber, and Gold Rush.
3. `Taqueria Los Altos` — East Charlotte Jalisco taqueria with Jalisco Obsidian, Clay Terracotta, Chile Red, and Maize Gold.
4. `Tap & Vine` — South Charlotte wine bar with Cellar Obsidian, Tasting Slate, Cabernet Reserve, and Champagne Gold.

### Divergent Choices for Taipei South

- **Hero Composition:** Taiwanese banquet split-hero with Johnston Road kicker (`"SOUTH CHARLOTTE • 10106 JOHNSTON RD • AUTHENTIC TAIWANESE & REGIONAL CHINESE CUISINE"`), jade celadon and imperial gold accents, featuring a steaming bowl of Taiwanese Beef Noodle Soup, anchored by a floating hero badge (`Taipei South | 10106 Johnston Rd • South Charlotte Taiwanese & Chinese Landmark`).
- **Section Rhythm:** Three-card standards grid without emojis highlighting "Slow-Braised Niu Rou Mian", "Handmade Jiaozi Dumplings", and "Master Wok Heat", followed by dual alternating highlight banners.
- **HTML Vocabulary:** Bespoke classes (`taipeisouth-header`, `taipeisouth-brand`, `taipeisouth-hero-stage`, `taipeisouth-hero-badge`, `taipeisouth-standards-section`, `taipeisouth-standard-card`, `taipeisouth-highlight-banner`, `taipeisouth-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 10106 Johnston Rd, Charlotte, NC 28210 | `visit.html`, `index.html`, `concept.html` | [Official Web Portal](https://taipeisouth.com/) |
| Hours: Mon-Fri 11:30-3 & 5-9:30, Sat-Sun 12-3 & 5-9:30 | `visit.html`, `index.html` | [Charlotte's got a lot](https://charlottesgotalot.com) |
| Serves Taiwanese Beef Noodle Soup, Dumplings, General Tso's | `taiwanese-beef-noodle-soup-and-braised-broths.html`, `menu.html` | [DoorDash Live Menu](https://doordash.com) |
| Authentic Taiwanese & regional Chinese sit-down dining room | `concept.html`, `index.html` | [Mecklenburg Health Records](https://mecknc.gov) |
| Full service bar, lunch specials, and family banquet service | `visit.html`, `menu.html` | [Official Portal](https://taipeisouth.com/) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Banquet Table & Lunar New Year Reservation System:** Digital booking calendar for large family round tables with lazy susans.
- **Handmade Frozen Dumpling Bulk Orders:** Online ordering cart for bags of 50 frozen handmade pork/cabbage dumplings for home cooking.
- **Express Corporate Lunch Bento Box Configurator:** Multi-item lunch combination builder for Ballantyne and South Charlotte offices.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or payment processing engine.
- No submission forms of any kind (no booking, contact, or inquiry forms).
- No live delivery tracking.

### Available for Production Scope

- Interactive spice and Sichuan peppercorn heat level selector.
- Real-time dining room waitlist indicator.
- Express takeout curbside pickup bay notifications.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs taipei-south` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
