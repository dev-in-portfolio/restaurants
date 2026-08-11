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

Premium status does not mean "include as many features as possible."

The demo's job is to sell the **premium core website** while preserving Dark Star Consulting's separately sellable add-on packs. `ADD_ON_BOUNDARY.md` contains the commercial boundary.

The old completion requirement for two custom interactions is retired. Ordinary website interactions remain appropriate, while custom functionality that maps to a sellable DSC add-on remains reserved for the proposal unless explicitly requested.

## Build-system quality correction

`BUILD_QUALITY_GATE.md` now controls premium-core build quality.

The fixed six-page quota is retired when verified material does not support six genuinely distinct pages. Automatic demos require **at least five substantive evidence-supported pages**, with a sixth only when current material justifies it.

The new system also requires:

- a `Creative Brief` with verified restaurant-specific anchors and three core design moves;
- a `Claim Ledger` mapping meaningful restaurant-specific claims to source URLs;
- an anti-template swap test so a generic hero/cards/grid shell cannot qualify merely by changing colors and copy;
- no automatic-demo forms;
- no invented catering/event/package inventory;
- machine validation before `qa` or `premium`.

Run:

```bash
node scripts/validate-demo.mjs <restaurant-slug>
```

The validator writes `<slug>/qa-report.json` and fails on objective defects such as broken CSS balance, JavaScript parse errors, broken local links/assets, missing fragment targets, duplicate IDs, missing alt text, placeholders, prohibited forms, missing core pages, or missing evidence sections.

A sentence in `evidence.md` claiming that QA passed does not override a failed validator.

## Completion rule

`premium` now requires:

- at least five substantive evidence-supported pages;
- restaurant-specific bespoke core design that passes the anti-template gate;
- successful machine validation;
- factual provenance through the Claim Ledger;
- responsive desktop/mobile browser QA actually performed;
- console, keyboard, focus, overflow/clipping, and accessibility checks actually performed;
- truthful demo-safe behavior;
- Add-On Preservation review.

If browser rendering is unavailable, the highest honest status is `qa` after machine validation passes.

## Regression specimen

`adamary-s-restaurante-y-pupuseria/` is intentionally left unchanged as the build that exposed the prior system weaknesses. It is not to be silently repaired during build-system housekeeping. It should be useful for verifying that the new validator and quality rules catch the kinds of defects and unsupported-content patterns that previously slipped through.
