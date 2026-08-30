# Portal Architecture — Canonical Two-Source Net-New Queue

## Current state

The portal combines two authoritative prospect sources, then subtracts every restaurant that already has a demo in `dev-in-portfolio/restaurant-showcase` (both active and HOLD):

1. **Rada-Depth Audit (Immutable 407 A/B rows):**
   - 407 total rows
   - 300 Showcase exclusions
   - 107 net-new active prospects (13 A YES / 36 B YES / 58 B CONDITIONAL)

2. **Charlotte Prospect Sweep 2026-08-28 (Authoritative 94 rows):**
   - 94 total rows
   - 25 Showcase exclusions
   - 0 Existing audit duplicate (The Public House)
   - 69 net-new active prospects (26 A+ / 27 A / 16 B)

**Combined active queue: 176 net-new prospects**

## Canonical data

- `queue/audit-ab-master.json` preserves the original 407 audited A/B rows.
- `queue/charlotte-prospect-sweep-2026-08-28.json` preserves the authoritative 94 supplemental sweep rows with supplied grades (A+, A, B).
- `scripts/sync-showcase-exclusions.mjs` reconciles both sources against Showcase active and hold files.
- Active queue data: `queue/a-yes-1.js`, `queue/a-yes-2.js`, `queue/b-yes.js`, `queue/b-conditional.js`, and `queue/sweep-2026-08-28.js`.
- `queue/showcase-exclusions.json` records every removed overlap and how it matched.
- `queue/meta.js` supplies the portal's expected live count (176).

## Hard rule

If a restaurant exists in Showcase active **or Showcase HOLD**, it is excluded from automatic Gemini new-demo selection. A redo requires explicit user intent.

## Integrity checks

The portal reads `queue/meta.js` and verifies that the number of loaded rows equals the combined net-new count (176). It also warns on duplicate canonical names or overrides for names outside the active queue.

## Source data truthfulness

Sweep records are rendered with their authentic source and grade (A+, A, B) without fabricating numeric scores or audit batches.
