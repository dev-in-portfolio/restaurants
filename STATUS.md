# Restaurant Demo Status

## Active Queue Architecture

The canonical demo queue combines two authoritative sources minus all existing demos in `dev-in-portfolio/restaurant-showcase` (both active and HOLD):

1. **Original Rada-Depth Audit (407 A/B rows):**
   - **223 active net-new prospects**
   - **129 A-grade YES**
   - **36 B-grade YES**
   - **58 B-grade CONDITIONAL**
   - **184 audited A/B prospects removed because a Showcase demo already exists** (178 active Showcase, 6 Showcase HOLD)

2. **Charlotte Restaurant Prospect Sweep (2026-08-28) (94 rows):**
   - **89 active net-new prospects admitted**
   - **46 A+ prospects**
   - **27 A prospects**
   - **16 B prospects**
   - **5 records reconciled/excluded** (4 active Showcase demos: Mert’s Heart & Soul, Homestyle Kitchn LLC, Exotica Indian Kitchen & Bar, Deluxe Fun Dining; 1 existing audit record & premium build: The Public House)

**Combined Active Queue Total: 312 net-new prospects**

Showcase inventory checked: **203 active + 31 hold = 234 existing demos**

Exact removals and reconciliations are recorded in `queue/showcase-exclusions.json`.
Immutable sources: `queue/audit-ab-master.json` and `queue/charlotte-prospect-sweep-2026-08-28.json`.

## Build-status rule

`portal-overrides.js` tracks build status only for restaurants still present in the active queue. Existing Showcase demos are not reintroduced through overrides.

## Selection order

1. A-grade YES (Audit) / A+ (Sweep)
2. A (Sweep)
3. B-grade YES (Audit)
4. B-grade CONDITIONAL (Audit) / B (Sweep)

Within a tier, sort alphabetically ignoring leading `The`, `A`, and `An`. Before selecting, run `node scripts/sync-showcase-exclusions.mjs` so a newly added Showcase demo cannot be rebuilt accidentally.

## Completion standard

A restaurant may be marked `premium` only after the current README standard, anti-template gate, factual evidence, desktop/mobile browser QA, machine validation, and accessibility baseline all pass. If browser QA is unavailable, the highest honest status is `qa`.
