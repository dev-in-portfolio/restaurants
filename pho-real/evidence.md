# Pho Real — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Pho Real (Pho Real Charlotte)
- **Slug:** `pho-real`
- **Audit Grade / Disposition / Score:** A / YES / 100
- **Audit Batch:** 16
- **Verification Date:** August 25, 2026

## Verification Sources

- [Pho Real Official Website](https://phorealcharlotte.com)
- [HappyCow Verified Charlotte Listing](https://happycow.net)
- [ChowNow Charlotte Ordering Profile](https://chownow.com)

## Original Audit Weakness

Pho Real relies on generic third-party ChowNow and Grubhub ordering pages and unbranded social listings. Located in University Executive Park off McCullough Dr, it lacks an owned digital showcase capturing its 24-hour slow-simmered bone broth craft, full Vietnamese bar program, University City campus pickup directives, and corporate party catering trays.

## Creative Brief

### Verified Visual / Content Anchors

1. **University City Location:** 440 E McCullough Dr, Suite 206, Charlotte NC 28262.
2. **Vietnamese Culinary & Bar Specialties:** 24-Hour Beef Bone Broth Pho, "Pho Real Deal" Sampler Platter (Stuffed Wings, Cha Gio Egg Rolls & Fried Quail), Grilled Lemongrass Pork Vermicelli (Bun Thit Nuong), Shaking Beef (Bo Luc Lac), Banh Mi, and Iced Vietnamese Milk Coffee.
3. **Contact & Operating Hours:** Phone (704) 717-2500; Open Daily Monday – Sunday 11:00 AM – 9:00 PM.

### Core Design Moves

1. **Contemporary Asian Display Typography:** Geometric display sans (*Outfit*) paired with clean body sans (*Plus Jakarta Sans*) and University Executive Park kitchen ticket mono (*Space Mono*).
2. **Emerald Jade & Imperial Gold Palette:** Vibrant modern Vietnamese palette anchored in deep emerald jade (`#064E3B`), night lotus forest (`#022C22`), jasmine mint lime (`#10B981`), imperial broth gold (`#F59E0B`), rice silk cream (`#ECFDF5`), and crisp linen white.
3. **"The 24-Hour Bone Broth & Street Feast Matrix":** Matrix-style dual column layout (`bone-broth-pho-and-sampler-craft.html` & `menu.html`) showcasing slow-simmered bone broth pho and house specialties alongside the Pho Real Deal sampler and craft beverages.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Puerta` — Mexican Agave Vault with Marcellus and Smoked Terracotta/Agave Gold.
2. `Plot Twist` — Midwood Garage Lounge with Prata and Midnight Plum/Electric Magenta.
3. `Platform Coffee + Kitchen` — Industrial Railway Roastery with Space Grotesk and Iron/Copper Amber.
4. `Pho Quynh` — Saigon Heritage with Newsreader and Saigon Cinnamon/Broth Amber.

### Divergent Choices for Pho Real

- **Hero Composition:** Modern University City Noodle Bar & Asian Street Dining split-hero layout: left side features a University City Broth Seal badge (`"24-HOUR BONE BROTH PHO & CONTEMPORARY VIETNAMESE BAR • UNIVERSITY CITY CHARLOTTE"`), contemporary geometric typography (*Outfit*), deep emerald jade & imperial gold palette, and right side features a framed hero image of steaming pho with fresh basil and lime wedges.
- **Section Rhythm:** Replaced standard card grids with **Pho Real Vault Cards** (`phoreal-vault-card`) and University Executive Park dining highlights.
- **HTML Vocabulary:** Completely unique class names (`phoreal-header`, `phoreal-brand`, `jade-hero-stage`, `phoreal-seal-badge`, `phoreal-vault-card`, `phoreal-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 440 E McCullough Dr Suite 206 in Charlotte NC 28262 | `visit.html`, `index.html`, `concept.html` | [Pho Real Official Website](https://phorealcharlotte.com) |
| Operating hours: Open Daily 11:00 AM – 9:00 PM | `visit.html`, `index.html` | [Pho Real Official Website](https://phorealcharlotte.com) |
| Direct phone: (704) 717-2500 | `visit.html`, `index.html` | [Pho Real Official Website](https://phorealcharlotte.com) |
| 24-hour slow-simmered beef bone broth pho & vegetarian pho options | `menu.html`, `bone-broth-pho-and-sampler-craft.html` | [HappyCow Listing](https://happycow.net) |
| "Pho Real Deal" sampler platter (stuffed wings, cha gio, fried quail) | `menu.html`, `street-bites-and-bar-craft.html` | [ChowNow Profile](https://chownow.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Pho Real University Campus & Corporate Catering Platter Calculator:** Automated group pricing for vermicelli bowls and egg roll platters for UNC Charlotte departments.
- **Pho Real VIP Noodle Club & Broth Pass:** Monthly loyalty subscriptions for frequent diners.
- **Pho Real Custom Boba & Vietnamese Iced Coffee Mobile Express Pickup:** Quick grab-and-go drink ordering.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or online payment processing engine.
- No submission forms of any kind (no contact, order, or feedback forms).
- No automated SMS or email marketing tools.
- No live table seating reservation integration.

### Available for Production Scope

- Custom zero-commission direct ordering app.
- Interactive broth spice selector & protein builder.
- Digital University City gift card engine.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs pho-real` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
