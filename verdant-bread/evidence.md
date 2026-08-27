# Verdant Bread — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Verdant Bread
- **Slug:** `verdant-bread`
- **Audit Grade / Disposition / Score:** A / YES / 96
- **Audit Batch:** 25
- **Verification Date:** August 27, 2026

## Verification Sources

- [Official Verdant Bread Portal](https://verdantbread.co)
- [Uptown Farmers Market Vendor Directory](https://uptownfarmersmarket.com)
- [Charlotte Magazine Bakery Features](https://charlottemagazine.com)
- [Axios Charlotte Local Bread Guide](https://charlotte.axios.com)

## Original Audit Weakness

Verdant Bread is Charlotte’s leading craft sourdough bakery, situated at 4410-C Monroe Road tucked behind the Common Market Oakwold. Built around wild sourdough fermentation, stone-milled heirloom grains from North Carolina mills, and European viennoiserie, Verdant Bread provides country boules, ciabatta, focaccia, English muffins, and laminated pastries to local residents and top Charlotte chef kitchens. However, its existing web portal was built primarily as a basic Squarespace store without interactive bread subscription schedules, pickup hub logistics (Charlotte, Davidson, Concord), or detailed grain provenance storytelling.

## Creative Brief

### Verified Visual / Content Anchors

1. **Physical Address:** 4410-C Monroe Rd, Charlotte, NC 28205 (Oakwold / East Charlotte, behind Common Market Oakwold).
2. **Contact Phone:** (704) 910-1845.
3. **Weekly Operating Schedule:** Tuesday – Friday 9:30 AM – 3:00 PM (Bakery pickup window); Saturday at Uptown Farmers Market (8:00 AM – 12:30 PM); Sunday – Monday closed for long cold-fermentation and grain milling.
4. **100% Wild Sourdough Craft:** Naturally leavened Carolina Country Sourdough boules, batards, whole grain loaves, and English muffins with no commercial baker's yeast.
5. **Viennoiserie & Regional Subscriptions:** Three-day laminated all-butter croissants, pain au chocolat, sourdough focaccia, and weekly Bread Club pickup subscriptions.

### Core Design Moves

1. **Artisan Baker's Flour & Hearth Crust Palette:** Deep millstone charcoal (`#161513`), toasted crust brown (`#8c522f`), warm Carolina golden wheat (`#d4924b`), flour-dusted oat cream (`#faf6ee`), and fresh verdant meadow green (`#36543b`).
2. **Artisanal Baker Typography:** Warm heritage serif (*Playfair Display*) paired with clean editorial sans (*Plus Jakarta Sans*) and grain mill technical monospace (*DM Mono*).
3. **Verified Culinary Photography:** Sourdough boules with leaf scoring and spiral proofing ridges on natural butcher block wood; thick slices of country sourdough showing open custard-like alveoli crumb; and a silver bakery presentation tray filled with golden hand-laminated all-butter croissants and pain au chocolat.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Zio Casual Italian` — Historic Myers Park neighborhood trattoria with Espresso, Rustic Terracotta, and Tuscan Olive.
2. `Tropical Goodies` — West Charlotte Caribbean & Soul Food with Allspice Charcoal, Turmeric Amber, and Scotch Bonnet Orange.
3. `YUME Ramen Sushi & Bar` — South End Japanese craft ramen & sushi lounge with Sumi Ink, Charred Binchotan, and Hinoki Cedar.
4. `Tryon House Restaurant — Woodlawn` — Classic American family diner with Ironstone, Heritage Forest Green, and Griddle Amber.

### Divergent Choices for Verdant Bread

- **Hero Composition:** Dedicated artisanal sourdough bakery split-hero with East Charlotte corridor kicker (`"MONROE ROAD • 4410-C MONROE RD • OAKWOLD CHARLOTTE • 100% NATURALLY LEAVENED SOURDOUGH"`), millstone charcoal and golden wheat accents, featuring the stone-hearth sourdough boules, anchored by a floating hero badge (`Verdant Bread | 4410-C Monroe Rd • Oakwold Sourdough Bakery`).
- **Section Rhythm:** Three-card standards grid without emojis highlighting "100% Wild Fermentation", "Stone-Milled Carolina Grains", and "Weekly Bread Club Subscriptions", followed by dual alternating highlight banners.
- **HTML Vocabulary:** Bespoke classes (`verdant-header`, `verdant-brand`, `verdant-hero-stage`, `verdant-hero-badge`, `verdant-standards-section`, `verdant-standard-card`, `verdant-highlight-banner`, `verdant-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 4410-C Monroe Rd in Oakwold | `visit.html`, `index.html`, `concept.html` | [Official Portal](https://verdantbread.co) |
| Hours: Tue-Fri 9:30am-3pm, Sat Farmers Market | `visit.html`, `index.html` | [Official Portal](https://verdantbread.co) |
| Phone: (704) 910-1845 | `visit.html`, `index.html` | [Official Portal](https://verdantbread.co) |
| 100% naturally leavened country sourdough, croissants, focaccia | `naturally-leavened-sourdough-craft.html`, `menu.html` | [Official Portal Menu](https://verdantbread.co) |
| Bread subscriptions with regional pickups in Charlotte, Davidson, Concord | `laminated-pastries-and-bread-subscriptions.html`, `index.html` | [Official Portal Subscriptions](https://verdantbread.co) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Verdant Sourdough Bread Club Portal:** Automated weekly subscription billing with custom grain selection and recurring pickup reminders.
- **Home Baker Starter & Milling Kits:** 50-year sourdough mother culture dehydrated packets and locally milled heritage flour bags for home enthusiasts.
- **Wholesale Chef Ordering Dashboard:** B2B portal for Charlotte restaurants and hotels to schedule recurring daily deliveries of burger buns, sandwich loaves, and baguettes.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or payment processing engine.
- No submission forms of any kind (no booking, contact, or pre-order forms).
- No direct shipping or food delivery dispatch.

### Available for Production Scope

- Interactive sourdough slicing and storage temperature guide.
- Live batch tracker showing daily bread bake times.
- Monroe Road and Common Market Oakwold parking directives.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs verdant-bread` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
