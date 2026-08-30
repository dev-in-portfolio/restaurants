# Prohibition — Concept Evidence & Brief

## Prospect Summary

- **Canonical Restaurant:** Prohibition (Prohibition Charlotte)
- **Slug:** `prohibition`
- **Audit Grade / Disposition / Score:** A / YES / 96
- **Audit Batch:** 16
- **Verification Date:** August 25, 2026

## Verification Sources

- [Prohibition Official Website](https://prohibitionclt.com)
- [Uptown Charlotte Center City Directory](https://uptowncharlotte.com)
- [Charlotte's Got A Lot Nightlife Guide](https://charlottesgotalot.com)

## Original Audit Weakness

Prohibition relies on generic third-party event forms and unbranded nightlife aggregator listings. Located in prime Uptown on 5th & Tryon, it lacks an owned digital showcase capturing its 1920s speakeasy mixology heritage, 2nd-floor Tryon balcony terrace, VIP table tier breakdown, and Uptown nightlife directives.

## Creative Brief

### Verified Visual / Content Anchors

1. **Uptown Charlotte Location:** 200 N Tryon St, Charlotte NC 28202 (Corner of 5th & Tryon).
2. **1920s Speakeasy Cocktails & Spirits:** The 1920s Smoked Bourbon Old Fashioned, The Bootlegger's Mule, Carolina Moonshine Sour, French 75, The Gatsby Gin Rickey, VIP Bottle Service, and Second-Floor Tryon Overlook Balcony.
3. **Contact & Operating Hours:** Phone (704) 358-4244 / (704) 890-8669; Thu–Fri 5:00 PM – 2:00 AM | Sat 4:00 PM – 2:00 AM | Sun–Wed Closed (Available for Private Buyouts).

### Core Design Moves

1. **Roaring Twenties Art Deco Serif Typography:** Refined classical Art Deco display serif (*Cinzel*) paired with clean body sans (*Plus Jakarta Sans*) and Uptown Tryon speakeasy ticket mono (*Space Mono*).
2. **Speakeasy Noir & Antique Brass Gold Palette:** Atmospheric nightlife palette anchored in deep speakeasy noir (`#0B0B0C`), reclaimed barnwood slate (`#1C1917`), antique brass gold (`#D97706`), bourbon ember (`#EA580C`), vintage ivory linen (`#FEF3C7`), and clean pure white.
3. **"The 1920s Speakeasy Libation & VIP Matrix":** Matrix-style dual column layout (`speakeasy-cocktails-and-whiskey-craft.html` & `menu.html`) showcasing classic Prohibition-era craft cocktails and small-batch moonshines alongside VIP bottle service and rooftop terrace amenities.

## Cross-Demo Diversity

### Inspected Recent Demos

1. `Pho Real` — Modern Vietnamese Noodle Bar with Outfit and Emerald Jade/Imperial Gold.
2. `Puerta` — Mexican Agave Vault with Marcellus and Smoked Terracotta/Agave Gold.
3. `Plot Twist` — Midwood Garage Lounge with Prata and Midnight Plum/Electric Magenta.
4. `Platform Coffee + Kitchen` — Industrial Railway Roastery with Space Grotesk and Iron/Copper Amber.

### Divergent Choices for Prohibition

- **Hero Composition:** 1920s Vintage Speakeasy & Uptown Tryon Balcony Terrace split-hero layout: left side features a 1920s Speakeasy Seal badge (`"EST. 1920S VINTAGE SPEAKEASY & CRAFT SPIRITS LOUNGE • UPTOWN TRYON CHARLOTTE"`), classical Art Deco display typography (*Cinzel*), speakeasy noir & antique brass gold palette, and right side features a framed hero image of smoked craft bourbon cocktails.
- **Section Rhythm:** Replaced standard card grids with **Prohibition Vault Cards** (`prohibition-vault-card`) and Uptown Center City nightlife highlights.
- **HTML Vocabulary:** Completely unique class names (`prohibition-header`, `prohibition-brand`, `speakeasy-hero-stage`, `prohibition-seal-badge`, `prohibition-vault-card`, `prohibition-footer`) ensuring 100% design diversity compliance.

## Claim Ledger

| Claim | Page(s) | Supporting Source URL |
| --- | --- | --- |
| Located at 200 N Tryon St in Charlotte NC 28202 (5th & Tryon) | `visit.html`, `index.html`, `concept.html` | [Prohibition Official Website](https://prohibitionclt.com) |
| Operating hours: Thu-Fri 5PM-2AM, Sat 4PM-2AM, Sun-Wed Closed/Buyouts | `visit.html`, `index.html` | [Prohibition Official Website](https://prohibitionclt.com) |
| Direct phone: (704) 358-4244 / (704) 890-8669 | `visit.html`, `index.html` | [Uptown Charlotte Directory](https://uptowncharlotte.com) |
| 1920s-inspired vintage decor, reclaimed barnwood & 2nd-floor patio | `index.html`, `concept.html` | [Uptown Charlotte Directory](https://uptowncharlotte.com) |
| Smoked old fashioneds, bootlegger mules, moonshine sours & VIP bottle service | `menu.html`, `speakeasy-cocktails-and-whiskey-craft.html` | [Prohibition CLT Menu](https://prohibitionclt.com) |

## Add-On Preservation

### Relevant DSC Add-On Opportunities

- **Prohibition VIP Table & Bottle Service Reservation Engine:** Live table map selection and minimum spend calculators for weekend nightlife.
- **Prohibition Private Speakeasy Buyout & Corporate Gala Calculator:** Automated quotes for full venue buyouts in Uptown.
- **Prohibition Bootlegger Cocktail Club Passport:** Exclusive cocktail flight passes and secret password event invitations.

### Intentionally Not Implemented (Preserved for Upsell)

- No native digital checkout or online payment processing engine.
- No submission forms of any kind (no contact, order, or feedback forms).
- No automated SMS or email marketing tools.
- No live table seating reservation integration.

### Available for Production Scope

- Custom zero-commission VIP booking portal.
- Interactive Prohibition cocktail flavor quiz.
- Digital Uptown nightlife gift card engine.

## QA

- **Machine Validator:** `node scripts/validate-demo.mjs prohibition` executed. `qa-report.json` and `design-diversity.json` generated and verified passing.
- **Browser Verification:** Tested responsive layouts at desktop (1440px) and mobile (375px) viewports, validated keyboard focus rings, zero console errors, no horizontal overflow, and clean DOM structure.
