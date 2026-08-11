# Portal Architecture — Audited Net-New Queue

## Current state

The portal starts from the completed audit's A/B prospect universe, then subtracts every restaurant that already has a demo in `dev-in-portfolio/restaurant-showcase`. Showcase HOLD demos are excluded too: HOLD means not currently presented there, not "needs another demo here."

Current reconciliation checkpoint:

- Audit A/B universe: **407**
- Showcase inventory checked: **114 active + 31 hold = 145 demos**
- Audit A/B restaurants with an existing Showcase demo: **95**
- Net-new Gemini queue: **312**
- Remaining tiers: **218 A YES / 36 B YES / 58 B CONDITIONAL**

The generated queue can change as Showcase changes. `queue/meta.js` after `node scripts/sync-showcase-exclusions.mjs` is authoritative.

## Canonical data

- `queue/audit-ab-master.json` preserves the original 407 audited A/B rows.
- `scripts/sync-showcase-exclusions.mjs` compares that immutable source against both Showcase data files.
- The generated active queue lives in the four `queue/*.js` bucket files.
- `queue/showcase-exclusions.json` records every removed overlap and how it matched.
- `queue/meta.js` supplies the portal's expected live count.

## Showcase hard rule

If a restaurant exists in Showcase active **or Showcase HOLD**, it is excluded from automatic Gemini new-demo selection. A redo requires explicit user intent.

## Integrity checks

The portal does not hardcode 407 as its rendered queue size. It reads `queue/meta.js` and verifies that the number of loaded rows equals the latest generated net-new count. It also warns on duplicate canonical names or overrides for names outside the net-new queue.

## Legacy folders and sources

Old restaurant folders and the retired legacy lead/concept files remain historical/reference material only. They cannot make a restaurant eligible. Build selection comes only from the generated net-new queue.

## Premium demo sales boundary

Premium status no longer means "include as many features as possible."

The demo's job is to sell the **premium core website** while preserving Dark Star Consulting's separately sellable add-on packs. `ADD_ON_BOUNDARY.md` contains the detailed boundary and is mandatory for build agents.

The old completion requirement for **two useful interactions including one conversion interaction is retired**. That rule encouraged agents to build separately monetizable functionality, such as custom planners, builders, concierge tools, and other signature interactions, directly into prospect demos.

Ordinary website interactions remain appropriate: navigation, accordions, standard tabs, simple galleries, subtle motion, and straightforward links to verified existing ordering/reservation services.

Custom feature functionality that maps to a sellable DSC add-on must be preserved for the proposal unless the user explicitly requests that add-on in the demo.

## Completion rule

The current six-page premium standard in `README.md` requires:

- restaurant-specific bespoke design;
- six substantive pages;
- strong core information architecture and presentation;
- verified current evidence;
- responsive desktop/mobile browser QA;
- accessibility checks;
- truthful demo-safe behavior;
- **Add-On Preservation review**;
- `evidence.md` documentation of relevant add-ons intentionally preserved as upsell opportunities.

A demo that looks excellent but gives away separately sellable DSC add-ons does **not** qualify as complete under the current sales strategy.
