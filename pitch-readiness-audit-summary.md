# Temporary Promoted-Site Pitch Readiness Audit

Audited the 66 canonical records with `status: "promoted"` and no `portalSection: "later"`.

## Result

- Pitchable as-is under the static audit: **16**
- Needs review before pitching: **41**
- Not ready: **9**

## Pitchable as-is

1. Bahn Thai
2. Bao & Broth
3. Bart's Mart
4. Beef 'N Bottle
5. Boudreaux’s Kitchen & Tavern
6. Brooks' Sandwich House
7. Cafe South
8. Carolina Scoops
9. Caswell Station
10. Cornerstone Pub & Grill
11. Curry Gate
12. Dish
13. E.L.K. Tavern
14. Enderly Coffee Co.
15. Euro Grill & Cafe
16. Gus' Family Restaurant

## Not ready

1. Comet Grill
2. House of Pizza
3. Kristophers Sports Bar
4. Mad Greek Café
5. Moosehead Grill
6. New Zealand Café
7. Sir Edmond Halley's
8. The Diamond Restaurant
9. The Thirsty Beaver Saloon

These nine contain repeated placeholder/disclaimer copy across substantive pages, multiple short pages, and near-duplicate page content.

## Review-first group

The remaining 41 passed the hard-failure checks but should be reviewed before a client presentation. Most were flagged for one short page, missing semantic `<main>` elements, or both.

## Static audit checks

- Six or more direct HTML pages
- `index.html` present
- No known placeholder-copy phrases
- No broken local `href` or `src` references
- Sufficient visible page content
- Distinct page titles
- No repeated near-duplicate pages
- Basic navigation and semantic structure

This was a static repository audit, not a substitute for final browser-based desktop/mobile visual inspection.
