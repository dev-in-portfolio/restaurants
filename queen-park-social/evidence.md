# Queen Park Social — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Queen Park Social
- **Slug:** `queen-park-social`
- **Audit Grade / Disposition / Score:** A / YES / 100
- **Audit Batch:** 17
- **Verification Date:** August 25, 2026

## Verification Sources

- [Queen Park Social Official Website](http://www.queenparksocial.com/)
- [Charlotte's Got A Lot Entertainment Guide](https://charlottesgotalot.com)
- [ChalkySticks Venue Directory](https://chalkysticks.com)

## Original Audit Weakness

Queen Park Social relies on generic third-party event forms and fragmented social links. Located in the hyper-competitive LoSo brewery district on Yancey Rd, it lacks an owned digital showcase capturing its 8 boutique bowling lanes, retro gaming floor, corporate team-building packages, and signature gastropub shareables.

## Creative Brief

### Verified Visual / Content Anchors

1. **LoSo Charlotte Location:** 4125 Yancey Rd, Charlotte NC 28217.
2. **Entertainment & Gastropub Offerings:** 8 Boutique Bowling Lanes, Shuffleboard, Skee-Ball & Retro Arcade Games, Smash Sliders, Loaded Waffle Fries, House Wings, Brisket Tacos, Warm Pretzel Bites with Craft Beer Cheese, Frozen Slushies, and Local Charlotte Craft Beer Drafts.
3. **Contact & Operating Hours:** Phone (980) 819-5626; Mon–Thu 4:00 PM – 12:00 AM | Fri 4:00 PM – 1:00 AM | Sat 11:00 AM – 1:00 AM | Sun 11:00 AM – 10:00 PM (21+ after 8:00 PM).

### Core Design Moves

1. **High-Energy Industrial Sans Typography:** Modern mid-century industrial sans (*Syne*) paired with clean body sans (*Plus Jakarta Sans*) and LoSo bowling score sheet mono (*Space Mono*).
2. **LoSo Warehouse Charcoal & Electric Cyan/Coral Palette:** Vibrant entertainment palette anchored in deep warehouse charcoal (`#18181B`), bowling pine amber (`#D97706`), electric retro cyan (`#06B6D4`), neon flamingo coral (`#F43F5E`), maple lane cream (`#FEF3C7`), and clean pure white.
3. **"The 8-Lane Bowling & Gastropub Shareables Matrix":** Matrix-style dual column layout (`boutique-bowling-and-arcade-craft.html` & `menu.html`) showcasing boutique bowling, arcade amenities, and corporate buyout packages alongside shareable appetizers, sliders, and craft taps.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Punta Cana` — Tropical Dominican Grill with DM Serif Display and Caribbean Sapphire/Sunburst Mango.
2. `Prohibition` — 1920s Speakeasy with Cinzel and Noir/Antique Brass Gold.
3. `Pho Real` — Modern Vietnamese Noodle Bar with Outfit and Emerald Jade/Imperial Gold.
4. `Puerta` — Mexican Agave Vault with Marcellus and Smoked Terracotta/Agave Gold.

### Divergent Choices for Queen Park Social

- **Hero Composition:** LoSo Industrial Social Club & Mid-Century Bowling Hall split-hero layout: left side features a LoSo Bowling Seal badge (`"8 BOUTIQUE BOWLING LANES • RETRO GAMING & CRAFT BEER HALL • LOSO CHARLOTTE"`), high-energy industrial typography (*Syne*), warehouse charcoal & electric cyan palette, and right side features a framed hero image of smash burgers and loaded fries.
- **Section Rhythm:** Replaced standard card grids with **Queen Park Vault Cards** (`queenpark-vault-card`) and LoSo Lower South End entertainment highlights.
- **HTML Vocabulary:** Completely unique class names (`queenpark-header`, `queenpark-brand`, `loso-hero-stage`, `queenpark-seal-badge`, `queenpark-vault-card`, `queenpark-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 4125 Yancey Rd in Charlotte NC 28217 (LoSo) | `visit.html`, `index.html`, `concept.html` | [Queen Park Social Official Website](http://www.queenparksocial.com/) |
| Operating hours: Mon-Thu 4PM-12AM, Fri 4PM-1AM, Sat 11AM-1AM, Sun 11AM-10PM (21+ after 8PM) | `visit.html`, `index.html` | [Queen Park Social Official Website](http://www.queenparksocial.com/) |
| Direct phone: (980) 819-5626 | `visit.html`, `index.html` | [Queen Park Social Official Website](http://www.queenparksocial.com/) |
| 8 bowling lanes, arcade games, pool tables & shuffleboard | `index.html`, `boutique-bowling-and-arcade-craft.html` | [Charlotte's Got A Lot Guide](https://charlottesgotalot.com) |
| Smash sliders, loaded waffle fries, brisket tacos & local craft beer drafts | `menu.html`, `gastropub-shareables-and-bar-craft.html` | [Queen Park Social Menu](http://www.queenparksocial.com/) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Queen Park Social Corporate Team-Building & Lane Booking Calculator:** Interactive lane and buffet party quote generator.
- **Queen Park Bowling League & Retro Arcade Season Pass:** Digital signups and tournament leaderboard.
- **Queen Park Express Food & Drink Mobile Ordering:** Tabletop QR ordering for bowling lanes and gaming lounge.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or online payment processing engine.
- No submission forms of any kind (no contact, order, or feedback forms).
- No automated SMS or email marketing tools.
- No live table seating reservation integration.

### Available for Production Scope

- Custom zero-commission bowling lane reservation app.
- Interactive tournament scoring board.
- Digital LoSo nightlife gift card engine.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs queen-park-social` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
