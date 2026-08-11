# Restaurant Demo Status

## Active net-new queue

The completed 645-record Rada-depth audit produced **407 A/B prospects** before Showcase reconciliation. Existing demos in `dev-in-portfolio/restaurant-showcase` are now a hard exclusion, including Showcase HOLD entries.

- **312 active net-new prospects**
- **218 A-grade YES**
- **36 B-grade YES**
- **58 B-grade CONDITIONAL**
- **95 audited A/B prospects removed because a Showcase demo already exists** (89 active Showcase, 6 Showcase HOLD)
- Showcase inventory checked: **114 active + 31 hold = 145 existing demos**

Exact removals are recorded in `queue/showcase-exclusions.json`. The immutable pre-subtraction audit source is `queue/audit-ab-master.json`.

## Build-status rule

`portal-overrides.js` tracks build status only for restaurants still present in the net-new queue. Existing Showcase demos are not reintroduced through overrides.

## Selection order

1. A-grade YES
2. B-grade YES
3. B-grade CONDITIONAL

Within a tier, sort alphabetically ignoring leading `The`, `A`, and `An`. Before selecting, run `node scripts/sync-showcase-exclusions.mjs` so a newly added Showcase demo cannot be rebuilt accidentally.

## Completion standard

A restaurant may be marked `premium` only after the current README six-page standard, useful-interaction requirement, factual evidence, desktop/mobile browser QA, and accessibility baseline all pass. If browser QA is unavailable, the highest honest status is `qa`.
