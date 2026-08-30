# Niki's Food Shop — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Niki’s Food Shop
- **Slug:** `niki-s-food-shop`
- **Audit Grade / Disposition / Score:** A / YES / 99
- **Audit Batch:** 14
- **Verification Date:** August 24, 2026

## Verification Sources

- [Charlotte's Got A Lot — Niki's Food Shop Profile](https://charlottesgotalot.com)
- [Restaurantji — Niki's Food Shop Charlotte](https://restaurantji.com)
- [Giftly Local Profile — Niki's Food Shop](https://giftly.com)

## Original Audit Weakness

Niki’s Food Shop has no official standalone website, relying entirely on third-party aggregators and tourist directories. Located at 2200 Beatties Ford Rd, it lacks an owned digital showcase capturing its legendary Historic West End cafeteria heritage, daily rotating meat-and-three steam table specials, breakfast biscuits, and cash-preferred diner directives.

## Creative Brief

### Verified Visual / Content Anchors

1. **Historic West End Charlotte Location:** 2200 Beatties Ford Rd, Charlotte NC 28216 (Beatties Ford Corridor / Historic West End Charlotte).
2. **Southern Diner & Meat-and-Three Specialties:** Golden Southern Fried Chicken, Country Style Steak in Rich Onion Gravy, Smothered Pork Chops, Four-Cheese Baked Mac & Cheese, Collard Greens, Sweet Potato Souffle, Warm Cornbread, & Early Morning Sausage Egg & Cheese Biscuits.
3. **Contact & Operating Hours:** Phone (704) 398-2638; Mon–Fri 6:00 AM – 5:00 PM | Sat 6:00 AM – 3:00 PM | Sun Closed (Cash-Preferred with On-Site ATM).

### Core Design Moves

1. **Heavy Nostalgic Diner Typography:** Bold Southern diner slab serif (*Alfa Slab One*) paired with clean body sans (*Plus Jakarta Sans*) and cafeteria steam table mono (*Space Mono*).
2. **Hickory Brown & Biscuit Gold Palette:** Nostalgic Southern diner palette anchored in hickory brown (`#451A03`), golden cornbread amber (`#D97706`), warm buttermilk cream (`#FEF3C7`), and collard green (`#14532D`).
3. **"The Meat-and-Three Steam Table Matrix":** Matrix-style dual column layout (`meat-and-three-craft.html` & `menu.html`) showcasing classic Southern meats alongside scratch Southern sides and scratch breakfast biscuits.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Night Swim Coffee` — Modern Nordic Minimalist Roastery with Epilogue fonts and Ocean Navy/Wave Cyan.
2. `Nalan Indian Cuisine` — Royal Indian Spice Palace with Marcellus fonts and Royal Terracotta/Turmeric Amber.
3. `Must Be Nice` — Glamorous South End Neon Velvet Nightclub with Syne fonts and Velvet Plum/Neon Magenta.

### Divergent Choices for Niki’s Food Shop

- **Hero Composition:** Vintage Charlotte Southern Diner & Steam-Table Cafeteria Vault split-hero layout: left side features a Southern Meat-and-Three Stamp badge (`"HISTORIC WEST END MEAT-AND-THREE INSTITUTION • CHARLOTTE NC"`), bold nostalgic slab serif typography (*Alfa Slab One*), hickory brown & biscuit gold palette, and right side features a bold framed hero image of classic country breakfast and biscuits.
- **Section Rhythm:** Replaced standard card grids with **Niki's Vault Cards** (`nikis-vault-card`) and Charlotte Historic West End dining highlights.
- **HTML Vocabulary:** Completely unique class names (`nikis-header`, `nikis-brand`, `diner-hero-stage`, `nikis-seal-badge`, `nikis-vault-card`, `nikis-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 2200 Beatties Ford Rd in Charlotte NC 28216 | `visit.html`, `index.html`, `concept.html` | [Charlotte's Got A Lot Profile](https://charlottesgotalot.com) |
| Operating hours: Mon-Fri 6am-5pm, Sat 6am-3pm, Sun Closed | `visit.html`, `index.html` | [Restaurantji Profile](https://restaurantji.com) |
| Phone number: (704) 398-2638 | `visit.html`, `index.html` | [Charlotte's Got A Lot Profile](https://charlottesgotalot.com) |
| Southern Meat-and-Three specials (Fried Chicken, Country Style Steak, Pork Chops) | `menu.html`, `meat-and-three-craft.html` | [Charlotte's Got A Lot Profile](https://charlottesgotalot.com) |
| Early morning country breakfast biscuits and scratch sides | `menu.html`, `breakfast-and-biscuits-craft.html` | [Giftly Local Profile](https://giftly.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Niki's Daily Steam Table SMS Board:** Live automated SMS broadcast of today's rotating meats and vegetables.
- **Niki's Sunday Church & Catering Banquet Engine:** Large-pan Southern catering ordering engine for family gatherings and church functions.
- **Niki's Express Breakfast Biscuit Order Ahead:** Zero-commission morning pickup queue.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or online payment processing engine.
- No submission forms of any kind (no contact, order, or feedback forms).
- No automated SMS or email marketing tools.
- No live table seating reservation integration.

### Available for Production Scope

- Custom zero-commission direct mobile pickup app.
- Interactive daily rotating meat-and-three board.
- Catering party tray quantity calculator.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs niki-s-food-shop` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
