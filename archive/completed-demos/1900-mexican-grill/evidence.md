# Evidence Packet — 1900 Mexican Grill

## Prospect Metadata
- **Canonical Name:** 1900 Mexican Grill
- **Slug:** `1900-mexican-grill`
- **Audit Tier:** A-grade YES
- **Audit Score:** 84
- **Audit Batch:** 1
- **Verification Date:** August 11, 2026

## Official Sources Verified
1. **Official Website:** `https://1900mexicangrill.com`
2. **Third-Party Online Ordering & Reservations:**
   - Toast / Order.online (Midtown & South Park stores)
   - Yelp Reservations (Midtown & South Park)
3. **Local Business Listings & Directories:**
   - Charlotte's Got A Lot Official Listing
   - Postmates / DoorDash verified menu listings
   - News coverage regarding Mezcal program in NC

## Verified Operating Facts
- **Midtown Elizabeth Location:** 1523 Elizabeth Ave, Charlotte, NC 28204 | Phone: (704) 334-4677
- **South Park Location:** 5110 Park Rd #1e, Charlotte, NC 28209 | Phone: (704) 523-1554
- **Hours of Operation (Both Locations):**
  - Monday – Thursday: 11:00 AM – 10:00 PM
  - Friday – Saturday: 11:00 AM – 11:00 PM
  - Sunday: 12:00 PM – 9:00 PM
- **Culinary Concept:** Inspired by Mexico City taquerias & traditional street food plazas. Features scratch kitchen mole poblano, chiles rellenos, birria de res, tableside guacamole fresco, taqueria-style tacos, and 25+ craft margaritas.
- **Spirits & Cantina Specialty:** Features North Carolina's largest collection of Mezcal (80+ artisanal wild and cultivated agave expressions) and custom Private Reserve Tequilas selected from agave barrels in Mexico.

## Documented Website Weakness Solved
The live public site (`1900mexicangrill.com`) suffered from several key digital customer journey flaws:
1. **Legacy 2019 Template:** Outdated visual structure with generic Gofuu template remnants, Copyright 2019, and unstyled raw buttons.
2. **Hidden Menu Content:** Food menu was relegated to an unstyled external PDF download (`Menu_2024.pdf`), frustrating mobile users.
3. **Unpromoted Specialty Bar Program:** Despite boasting NC's largest Mezcal collection, the live site had no interactive way to explore agave varieties, flight pairings, or artisanal salts.
4. **Weak Group & Catering Conversion:** Catering was mentioned only in plain text with no estimator, menu breakdown, or inquiry pathway.
5. **Confusing Dual-Location Access:** Users struggled to quickly toggle between Elizabeth Ave and South Park locations for hours, maps, and reservation paths.

## Bespoke Art Direction & Visual Identity
- **Design Philosophy:** Mexico City Warmth meets Sophisticated Artisanal Cantina.
- **Color Palette:**
  - *Terracotta Red* (`#C83E2B` / `#A62B1E`): Warm Earthy Mexican clay & salsa tones.
  - *Agave Teal* (`#2A7B76` / `#1D5451`): Lush agave plant tones & depth.
  - *Warm Sandstone* (`#F7F4EF` / `#FFFDF9`): Soft parchment background tones replacing harsh white.
  - *Charcoal / Obsidian* (`#1A1817`): Cantina night atmosphere.
  - *Sunlit Gold* (`#D9A036`): Agave nectar and mezcal pour highlights.
- **Typography:**
  - Headings: `Playfair Display` (serif) & `Outfit` — refined, heritage feel.
  - Body: `Inter` — clean, highly readable navigation & menu details.
- **Visual Features:** Modern glassmorphic cards, agave flight interactive platter, dietary badge tags, responsive mobile tab navigation.

## Standard Six-Page Deliverable Structure
1. `index.html` — Hero, Mexico City concept overview, dual location comparison, signature dishes, and direct booking/catering callouts.
2. `menu.html` — Fully searchable & filterable menu (Tacos, Specialties, Fajitas, Guac, Desserts) with dietary tags (GF, Veg, House Favorite).
3. `story.html` — Verified story of 1900's origins in 2009, Mexico City inspiration, scratch kitchen commitment, and barrel selection tradition.
4. `cantina.html` (Experience Page) — Mezcal & Tequila Reserve showcase, agave education guide, and **Interactive Mezcal & Salt Flight Builder** (Interaction 1).
5. `catering.html` (Conversion Page) — Social & Corporate Catering guide, Fiesta packages, and **Interactive Catering & Taco Bar Party Estimator** (Interaction 2).
6. `visit.html` — Dual location guide (Midtown vs South Park), live interactive location switcher, parking/neighborhood info, phone links, and Yelp reservation guidance.

## Intentionally Omitted / Demo Safety
- Specific founding family member names beyond public press references were kept tasteful and authentic.
- Live payment gateways or online order checkout processing are intentionally simulated with safe non-submitting demo modal windows to prevent accidental customer submission.
- Standard repo unofficial concept disclaimer included via `scripts/shared/darkstar-footer.js`.

## QA & Verification Checklist
- [x] 6 substantive linked HTML pages created.
- [x] Mobile hamburger menu & responsive navigation verified across screen sizes.
- [x] Search & dietary filtering on `menu.html` verified.
- [x] Interactive Mezcal Flight Builder on `cantina.html` verified.
- [x] Interactive Catering Calculator on `catering.html` verified.
- [x] Multi-location switcher on `visit.html` verified.
- [x] `comparison-button.js` and `darkstar-footer.js` integrated across all 6 pages.
- [x] Zero console errors, zero dead links, zero missing image assets.
- [x] Keyboard focus states & reduced-motion CSS media query support verified.
