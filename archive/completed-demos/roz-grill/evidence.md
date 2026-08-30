# Roz Grill — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Roz Grill
- **Slug:** `roz-grill`
- **Audit Grade / Disposition / Score:** A / YES / 100
- **Audit Batch:** 18
- **Verification Date:** August 26, 2026

## Verification Sources

- [Shop Arboretum Merchant Directory](https://shoparboretum.com)
- [Toast Online Ordering Roz Grill](https://toasttab.com)
- [Uber Eats Roz Grill Menu](https://ubereats.com)
- [DoorDash Roz Grill Profile](https://doordash.com)

## Original Audit Weakness

Roz Grill operates in the prominent Arboretum Shopping Center in South Charlotte with a devoted local following for halal Mediterranean cuisine, scratch pita, and charcoal skewers. However, their digital footprint consisted largely of third-party delivery aggregation profiles and a basic ordering portal. It lacked an owned, brand-forward web experience that showcases their Mediterranean hospitality, halal sourcing integrity, house-made mezze dips (hummus, muhammara, whipped feta), and fresh-squeezed juice bar.

## Creative Brief

### Verified Visual / Content Anchors

1. **Arboretum Shopping Center Location:** 8200 Providence Road, Charlotte NC 28277. Prominently located in the Arboretum retail hub at the intersection of Providence Road and Pineville-Matthews Road (NC-51).
2. **Mediterranean, Greek & Middle Eastern Menu:** Char-grilled halal kebabs (lamb, chicken, beef kofta, shrimp), Gyro platters, Roz Bites (spinach and cheese croquettes), house dips (hummus with extra virgin olive oil, creamy tzatziki, muhammara, whipped feta), falafel platters, fresh-pressed juice bar, knafeh, and honey-glazed baklava.
3. **Contact & Hours:** Phone (704) 910-1936; Open Daily: 11:00 AM – 9:00 PM. Dine-in, takeout, and catering service.

### Core Design Moves

1. **Olive Grove & Terracotta Sun Palette:** Mediterranean warmth grounded in deep olive noir (`#0f1712`), rich cypress card (`#16231b`), warm terracotta clay (`#c25e3a`), olive oil gold (`#d97706`), fresh sage tint (`#10b981`), and warm ivory linen (`#fcfbf8`).
2. **Warm Mediterranean Typography:** Elegant serif headers (*Cinzel* or *Lora* paired with *Plus Jakarta Sans*) with editorial rhythm, accompanied by clean metadata styling.
3. **Authentic Mediterranean Photography:** High-resolution spread featuring warm toasted flatbread, silky swirled hummus, whipped labneh, golden falafel, and pistachio-stuffed baklava with zero text and zero logos.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `República Restaurant & Lounge` — Dominican Gastronomy & Latin Lounge with Plus Jakarta Sans and Deep Night Navy/Amber Gold/Coral.
2. `Red@28th` — Multicultural Literary Lounge & Hookah Bar with Lora and Burgundy/Tobacco Amber.
3. `QC Social Lounge` — Uptown Nightclub & VIP Bottle Service with Space Grotesk and Obsidian/Neon Orchid/Gold.
4. `Red Sea Restaurant & Bar` — Horn of Africa Habesha Dining with Marcellus and Terracotta Ochre/Turmeric Gold.

### Divergent Choices for Roz Grill

- **Hero Composition:** Split-hero design with an Arboretum South Charlotte Kicker (`"THE ARBORETUM • 8200 PROVIDENCE ROAD • CHARLOTTE NC"`), warm terracotta CTA buttons, and a framed hero feast spread anchored by a floating hero badge (`Arboretum South Charlotte | 8200 Providence Rd • Daily 11 AM - 9 PM`).
- **Section Rhythm:** Three-card standards grid without emojis highlighting "100% Halal Charcoal Grill", "Scratch Mezze & Fresh Pita", and "Fresh Juice Bar & Pastry", followed by two rich alternating highlight banners.
- **HTML Vocabulary:** Bespoke classes (`roz-header`, `roz-brand`, `roz-hero-stage`, `roz-hero-badge`, `roz-standards-section`, `roz-standard-card`, `roz-highlight-banner`, `roz-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 8200 Providence Road in Charlotte NC 28277 (The Arboretum) | `visit.html`, `index.html`, `concept.html` | [Shop Arboretum Directory](https://shoparboretum.com) |
| Operating hours: Daily 11:00 AM - 9:00 PM | `visit.html`, `index.html` | [Shop Arboretum Directory](https://shoparboretum.com) |
| Direct phone: (704) 910-1936 | `visit.html`, `index.html` | [Toast Tab Roz Grill](https://toasttab.com) |
| Specializes in Mediterranean, Greek, and Middle Eastern cuisine | `concept.html`, `index.html` | [Shop Arboretum Directory](https://shoparboretum.com) |
| Serves halal kebabs, gyro platters, falafel, hummus, and whipped feta | `menu.html`, `mediterranean-grill-and-kebabs-craft.html` | [Uber Eats Roz Grill](https://ubereats.com) |
| In-house fresh juice bar and handmade baklava & knafeh | `menu.html`, `scratch-mezze-juices-and-sweets-craft.html` | [Shop Arboretum Directory](https://shoparboretum.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Roz Family & Corporate Catering Estimator:** Interactive Mediterranean party platter calculator for kebabs, basmati rice, and dips.
- **Arboretum Curbside Pickup Express:** Live vehicle notification tool for quick pickup outside the Arboretum storefront.
- **Roz Fresh Juice Subscription:** Weekly wellness club pass for cold-pressed pomegranate, orange, and mint juices.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or online payment processing engine.
- No submission forms of any kind (no contact, reservation, or catering forms).
- No automated SMS or delivery driver tracking integrations.
- No table reservation booking system.

### Available for Production Scope

- Custom zero-commission direct online ordering app.
- Interactive catering event menu builder.
- Customer loyalty points program.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs roz-grill` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
