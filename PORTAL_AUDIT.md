# Portal Architecture — Audited Net-New Queue

## Current state

The portal starts from the completed audit's A/B prospect universe, then subtracts every restaurant that already has a demo in `dev-in-portfolio/restaurant-showcase`. Showcase HOLD demos are excluded too: HOLD means not currently presented there, not "needs another demo here."

Current reconciliation:

- Audit A/B universe: **407**
- Showcase inventory checked: **114 active + 31 hold = 145 demos**
- Audit A/B restaurants with an existing Showcase demo: **95**
- Net-new Gemini queue: **312**
- Remaining tiers: **218 A YES / 36 B YES / 58 B CONDITIONAL**

## Canonical data

- `queue/audit-ab-master.json` preserves the original 407 audited A/B rows.
- `scripts/sync-showcase-exclusions.mjs` compares that immutable source against both Showcase data files.
- The generated active queue lives in the four `queue/*.js` bucket files.
- `queue/showcase-exclusions.json` records every removed overlap and how it matched.
- `queue/meta.js` supplies the portal's expected live count.

## Hard rule

If a restaurant exists in Showcase active **or Showcase HOLD**, it is excluded from automatic Gemini new-demo selection. A redo requires explicit user intent.

## Integrity checks

The portal no longer hardcodes 407 as its rendered queue size. It reads `queue/meta.js` and verifies that the number of loaded rows equals the latest generated net-new count. It also warns on duplicate canonical names or overrides for names outside the net-new queue.

## Legacy folders and sources

Old restaurant folders and the retired legacy lead/concept files remain historical/reference material only. They cannot make a restaurant eligible. Build selection comes only from the generated net-new queue.

## Completion rule

The current six-page premium standard in `README.md` remains unchanged: restaurant-specific design, six substantive pages, two useful interactions including one conversion interaction, current evidence, responsive/browser QA, accessibility checks, and truthful demo-safe behavior.
