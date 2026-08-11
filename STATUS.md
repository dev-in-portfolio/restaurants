# Restaurant Demo Status

## Active net-new queue

The completed 645-record Rada-depth audit produced **407 A/B prospects** before Showcase reconciliation. Existing demos in `dev-in-portfolio/restaurant-showcase` are a hard exclusion, including Showcase HOLD entries.

Current reconciliation checkpoint:

- **312 active net-new prospects**
- **218 A-grade YES**
- **36 B-grade YES**
- **58 B-grade CONDITIONAL**
- **95 audited A/B prospects removed because a Showcase demo already exists** (89 active Showcase, 6 Showcase HOLD)
- Showcase inventory checked: **114 active + 31 hold = 145 existing demos**

Exact removals are recorded in `queue/showcase-exclusions.json`. The immutable pre-subtraction audit source is `queue/audit-ab-master.json`. Run `node scripts/sync-showcase-exclusions.mjs` before selection because the generated counts may change as Showcase changes.

## Build-status rule

`portal-overrides.js` tracks build status only for restaurants still present in the net-new queue. Existing Showcase demos are not reintroduced through overrides.

## Selection order

1. A-grade YES
2. B-grade YES
3. B-grade CONDITIONAL

Within a tier, sort alphabetically ignoring leading `The`, `A`, and `An`. Before selecting, run `node scripts/sync-showcase-exclusions.mjs` so a newly added Showcase demo cannot be rebuilt accidentally.

## Premium demo sales rule

Premium demos sell the **core website**. They do not automatically include the separately sellable DSC add-on packs.

`ADD_ON_BOUNDARY.md` is mandatory reading. The current reserved add-on catalog includes:

- Brand Finish Pack
- Menu Experience Pack
- Photo Story Pack
- Local Discovery Pack
- Trust & Reputation Pack
- Order & Reserve Pack
- Catering & Private Events Pack
- Guest Engagement Pack
- Menu Collections Pack
- Signature Interactive Experience
- Digital Menu Concierge
- Multi-Location Growth Pack

A demo should look premium through bespoke design, responsive execution, strong information architecture, verified content, and polish. Do **not** invent custom planners, builders, configurators, concierge tools, loyalty systems, advanced ordering/reservation flows, catering/event systems, or other sellable enhancements just to make the demo feel premium.

The former rule requiring two useful interactions including one conversion interaction is retired.

## Completion standard

A restaurant may be marked `premium` only after:

- the current README six-page standard passes;
- factual evidence is documented;
- desktop/mobile browser QA passes;
- accessibility baseline passes;
- ordinary interactions that actually exist are tested;
- an **Add-On Preservation review** confirms separately sellable DSC enhancements were not accidentally bundled into the demo;
- `evidence.md` records relevant upsell opportunities intentionally preserved for the proposal.

If browser QA is unavailable, the highest honest status is `qa`.
