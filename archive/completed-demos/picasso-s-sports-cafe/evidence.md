# Picasso’s Sports Café — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Picasso’s Sports Café
- **Slug:** `picasso-s-sports-cafe`
- **Audit Grade / Disposition / Score:** A / YES / 100
- **Audit Batch:** 16
- **Verification Date:** August 25, 2026

## Verification Sources

- [Picasso’s Sports Pub & Café Official Website](https://picassosportscafe.com)
- [Uptown Charlotte Merchant Directory](https://uptowncharlotte.com)
- [Charlotte Area Chamber of Commerce Business Guide](https://charlotteareachamber.com)

## Original Audit Weakness

Picasso’s Sports Café relies on generic template sports bar web layouts and fragmented third-party delivery pages. Operating dual busy Charlotte hubs on WT Harris Blvd and Trade St, it lacks an owned digital showcase capturing its award-winning wing sauce bar, game day watch parties, pizza griddling, and watch party reservation directives.

## Creative Brief

### Verified Visual / Content Anchors

1. **Dual Charlotte Locations:** 
   - University City: 230 E W.T. Harris Blvd, Suite A10, Charlotte NC 28262. Phone: (704) 595-9553.
   - Uptown Charlotte: 123 W Trade St, Charlotte NC 28202. Phone: (704) 332-2227.
2. **Sports Bar Specialties:** Jumbo Flash-Fried Chicken Wings tossed in 10+ scratch sauces (Mild, Hot, Mango Habanero, Garlic Parmesan, Caribbean Jerk), Hand-Tossed Stone-Baked Specialty Pizzas (Meat Lovers, Buffalo Chicken, Philly Cheesesteak), Half-Pound Steakhouse Burgers, Loaded Stadium Nachos, and Draft Craft Beers.
3. **Contact & Operating Hours:** Open 7 days a week, 11:30 AM – 12:00 AM Midnight.

### Core Design Moves

1. **Heavyweight Athletic Display Typography:** Bold condensed athletic display sans (*Barlow Condensed*) paired with clean body sans (*Plus Jakarta Sans*) and stadium scoreboard ticket mono (*Space Mono*).
2. **Stadium Jet Black & Electric Sports Gold Palette:** High-energy sports pub palette anchored in stadium jet black (`#0B0F17`), charcoal slate (`#1E293B`), electric sports gold (`#EAB308`), and fiery buffalo wing red (`#DC2626`).
3. **"The Game Day Jumbo Wings & Hand-Tossed Pizza Matrix":** Matrix-style dual column layout (`jumbo-wings-and-sauce-craft.html` & `menu.html`) showcasing award-winning jumbo wings and scratch sauces alongside stone-baked pizzas and half-pound pub burgers.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Pho Huong Que` — Vietnamese Saigon Heritage with Newsreader fonts and Forest Emerald/Amber.
2. `Passage to India Indian Cuisine` — Royal Mughlai Palace with Cormorant Garamond and Peacock Indigo/Saffron.
3. `Parkway House Family Restaurant` — Greek-American Heritage Diner with Fraunces and Diner Blue/Buttermilk Gold.

### Divergent Choices for Picasso’s Sports Café

- **Hero Composition:** High-Energy Game Day Sports Stadium & Wing Vault split-hero layout: left side features an Athletic Stadium Patch badge (`"GAME DAY SPORTS BAR & JUMBO WINGS • CHARLOTTE NC"`), bold athletic display sans typography (*Barlow Condensed*), jet black & electric gold palette, and right side features a bold framed hero image of crispy jumbo buffalo wings with celery, carrots, and house bleu cheese.
- **Section Rhythm:** Replaced standard card grids with **Picasso Vault Cards** (`picasso-vault-card`) and Charlotte game day stadium watch party highlights.
- **HTML Vocabulary:** Completely unique class names (`picasso-header`, `picasso-brand`, `stadium-hero-stage`, `picasso-seal-badge`, `picasso-vault-card`, `picasso-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 230 E W.T. Harris Blvd #A10 (University) & 123 W Trade St (Uptown) | `visit.html`, `index.html`, `concept.html` | [Picasso’s Sports Pub Website](https://picassosportscafe.com) |
| Operating hours: Open 7 days a week, 11:30 AM - 12:00 AM Midnight | `visit.html`, `index.html` | [Picasso’s Sports Pub Website](https://picassosportscafe.com) |
| Phone numbers: (704) 595-9553 (University) / (704) 332-2227 (Uptown) | `visit.html`, `index.html` | [Uptown Charlotte Guide](https://uptowncharlotte.com) |
| Award-winning jumbo chicken wings tossed in 10+ scratch sauces | `menu.html`, `jumbo-wings-and-sauce-craft.html` | [Picasso’s Sports Pub Website](https://picassosportscafe.com) |
| Hand-tossed stone-baked specialty pizzas & half-pound burgers | `menu.html`, `stone-baked-pizza-and-burgers-craft.html` | [Picasso’s Sports Pub Website](https://picassosportscafe.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Picasso’s Game Day Big Game Wing Platter Pre-Order Engine:** Large wing tray and party platter calculator for Super Bowl, March Madness, and Panthers watch parties.
- **Picasso’s VIP Booth & Watch Party Table Reservation Engine:** Reserved seating app for fantasy drafts and televised sporting events.
- **Picasso’s Mug Club & Game Day Loyalty Rewards:** Digital loyalty pass engine for beer enthusiasts and sports regulars.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or online payment processing engine.
- No submission forms of any kind (no contact, order, or feedback forms).
- No automated SMS or email marketing tools.
- No live table seating reservation integration.

### Available for Production Scope

- Custom zero-commission direct wing ordering app.
- Interactive game day party catering builder.
- Digital sports pub gift card engine.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs picasso-s-sports-cafe` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
