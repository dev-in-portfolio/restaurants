# Pho Quynh — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Pho Quynh (Phở Quỳnh)
- **Slug:** `pho-quynh`
- **Audit Grade / Disposition / Score:** A / YES / 99
- **Audit Batch:** 16
- **Verification Date:** August 25, 2026

## Verification Sources

- [PlaceJoys Central Avenue Dining Directory](https://placejoys.com)
- [Secret Charlotte East Charlotte Food Guide](https://secretcharlotte.co)
- [Menufy Verified Restaurant Profile](https://menufy.com)

## Original Audit Weakness

Pho Quynh relies on generic third-party online menus (Menufy/PlaceJoys) and unbranded directory listings. Located on high-density Central Avenue, it lacks an owned digital showcase capturing its 24-hour beef bone broth reduction craft, fresh herb garden sourcing, vermicelli bowl matrix, family story, and Central Ave carryout directives.

## Creative Brief

### Verified Visual / Content Anchors

1. **Central Avenue East Charlotte Location:** 4900 Central Ave, Charlotte NC 28205.
2. **Vietnamese Culinary Specialties:** 24-Hour Simmered Oxtail & Brisket Phở Đặc Biệt, Phở Tái Nạm, Bún Thịt Nướng Chả Giò (Grilled Lemongrass Pork Vermicelli), Crispy Bánh Xèo Vietnamese Crepes, Crispy Pork Spring Rolls, and Iced Cà Phê Sữa Đá.
3. **Contact & Operating Hours:** Phone (980) 201-9124; Mon–Sat 10:00 AM – 10:00 PM | Sun 11:00 AM – 9:00 PM.

### Core Design Moves

1. **Warm Vietnamese Editorial Serif Typography:** Refined heritage serif (*Newsreader*) paired with clean body sans (*Plus Jakarta Sans*) and Saigon kitchen ticket mono (*Space Mono*).
2. **Saigon Cinnamon & Star Anise Amber Palette:** Heritage Vietnamese broth palette anchored in deep Saigon cinnamon earth (`#451A03`), warm star anise amber (`#D97706`), fresh Thai basil mint (`#059669`), lantern gold (`#F59E0B`), rice noodle cream (`#FFFBEB`), and pure white.
3. **"The 24-Hour Bone Broth & Central Ave Bún Matrix":** Matrix-style dual column layout (`bone-broth-pho-and-bun-craft.html` & `menu.html`) showcasing 24-hour bone broths and vermicelli noodle bowls alongside crispy street bites and Vietnamese iced coffees.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Poppy’s Bagels & More` — NYC Kettle Bakery & Jewish Deli with Fraunces and Brooklyn Navy/Deli Mustard.
2. `Pokebowl Ramen` — Tokyo Neon Ramen Bar with Outfit and Obsidian/Seaweed Teal.
3. `Laurel Park` — SouthPark Mediterranean Veranda with Cormorant Garamond and Laurel Emerald/Sandstone Ochre.

### Divergent Choices for Pho Quynh

- **Hero Composition:** Central Avenue Vietnamese Saigon Heritage & 24-Hour Pho Vault split-hero layout: left side features a Central Ave Pho Vault Seal badge (`"24-HOUR BONE BROTH & SAIGON STREET CRAFT • CENTRAL AVE CHARLOTTE"`), warm Vietnamese serif typography (*Newsreader*), Saigon cinnamon & broth amber palette, and right side features a framed hero image of steaming pho broth with rare beef eye round and fresh Thai basil.
- **Section Rhythm:** Replaced standard card grids with **Quynh Vault Cards** (`quynh-vault-card`) and Central Avenue Vietnamese kitchen highlights.
- **HTML Vocabulary:** Completely unique class names (`quynh-header`, `quynh-brand`, `saigon-hero-stage`, `quynh-seal-badge`, `quynh-vault-card`, `quynh-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 4900 Central Ave in Charlotte NC 28205 | `visit.html`, `index.html`, `concept.html` | [PlaceJoys Central Ave Guide](https://placejoys.com) |
| Operating hours: Mon-Sat 10AM-10PM / Sun 11AM-9PM | `visit.html`, `index.html` | [ShowMeLocal Profile](https://showmelocal.com) |
| Direct phone: (980) 201-9124 | `visit.html`, `index.html` | [ShowMeLocal Profile](https://showmelocal.com) |
| 24-hour simmered bone broth, Phở Đặc Biệt, & Phở Tái Nạm | `menu.html`, `bone-broth-pho-and-bun-craft.html` | [Menufy Pho Quynh Menu](https://menufy.com) |
| Bún Thịt Nướng, crispy egg rolls, bánh xèo & Cà Phê Sữa Đá | `menu.html`, `street-bites-and-vietnamese-coffee-craft.html` | [Menufy Pho Quynh Menu](https://menufy.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Pho Quynh Interactive Pho Customizer & Broth Selector:** Step-by-step visual bowl builder with customized meat cuts, noodle styles, and chili oil heat levels.
- **Pho Quynh Family & Party Noodle Banquet Engine:** Large-format vermicelli platters and spring roll party tray builder.
- **Pho Quynh VIP Noodle Pass Loyalty Club:** Digital punch card and monthly noodle bowl rewards.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or online payment processing engine.
- No submission forms of any kind (no contact, order, or feedback forms).
- No automated SMS or email marketing tools.
- No live table seating reservation integration.

### Available for Production Scope

- Custom zero-commission direct ordering app.
- Interactive broth heat & allergen guide.
- Digital Central Ave gift card engine.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs pho-quynh` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
