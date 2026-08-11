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

## Automatic continuation mode — NEW BUILDS ONLY

Normal continuation now works only on untouched `lead` prospects.

Do not automatically redo, repair, refresh, or redesign any restaurant that already has:

- a committed canonical `<slug>/index.html` route;
- an `incomplete`, `qa`, `premium`, `promoted`, or `promoted_secondary` override;
- `portalSection: "later"`;
- a Showcase active/HOLD exclusion.

If the next alphabetical queue candidate already has a committed demo folder, skip it unchanged and continue to the next untouched lead.

Existing builds—including Adamary’s, All Purpose Bar, and the demos built after All Purpose Bar—remain frozen until the user explicitly requests a separate repair/redesign pass.

## Selection order

1. A-grade YES
2. B-grade YES
3. B-grade CONDITIONAL

Within a tier, sort alphabetically ignoring leading `The`, `A`, and `An`. Before selecting, run `node scripts/sync-showcase-exclusions.mjs` so a newly added Showcase demo cannot be rebuilt accidentally.

## Premium demo sales rule

Premium demos sell the **core website**. They do not automatically include the separately sellable DSC add-on packs.

`ADD_ON_BOUNDARY.md` and `BUILD_QUALITY_GATE.md` are mandatory reading.

The former rule requiring two useful custom interactions is retired. The former fixed six-page quota is also retired when verified material does not support six distinct substantive pages.

The current target is **at least five substantive pages, with a sixth only when current evidence supports a genuinely different page job**.

## Build-quality correction

A build is not allowed to self-certify QA in `evidence.md`.

Before `qa` or `premium`, run:

```bash
node scripts/validate-demo.mjs <restaurant-slug>
```

The generated `<slug>/qa-report.json` must pass.

The validator checks objective defects such as CSS balance, JavaScript parse errors, broken local links/assets, broken fragment links, duplicate IDs, missing alt text, placeholder residue, prohibited automatic-demo forms, missing core pages, exact duplicate HTML pages, required evidence sections, and cross-demo design similarity.

`evidence.md` must contain:

- `## Creative Brief`
- `## Claim Ledger`
- `## Add-On Preservation`
- `## Cross-Demo Diversity`

The claim ledger maps meaningful restaurant-specific claims to source URLs. General cuisine knowledge may not be presented as an unsupported fact about how the restaurant operates.

## Cross-demo diversity gate

The All Purpose Bar run showed that a successful demo can become an implicit template for subsequent restaurants. Future builds must now compare against up to the 10 most recent completed demos.

`node scripts/validate-demo.mjs <slug>` invokes:

```bash
node scripts/check-design-diversity.mjs <slug>
```

The diversity script compares HTML class vocabulary, CSS class vocabulary, DOM structure, section composition, and font-family overlap. It writes `<slug>/design-diversity.json`.

A new build that is too structurally similar to a recent demo fails QA. Changing only colors, copy, cuisine nouns, icons, or photos is not sufficient.

## Premium design gate

Premium must be visible in the **core design**, not in add-on functionality.

A site that is essentially a reusable hero/cards/grid template fails even if it has enough pages and clean code. `BUILD_QUALITY_GATE.md` contains the anti-template, swap, and cross-demo diversity tests.

## Completion standard

A restaurant may be marked `premium` only after:

- it is an untouched eligible lead at selection time;
- at least five substantive evidence-supported pages exist;
- `node scripts/validate-demo.mjs <slug>` passes;
- `design-diversity.json` passes against recent demos;
- factual provenance is documented in the Claim Ledger;
- the anti-template design gate passes;
- desktop/mobile browser QA passes;
- console and responsive checks were actually performed, not merely claimed;
- accessibility baseline passes;
- an **Add-On Preservation review** confirms separately sellable DSC enhancements were not accidentally bundled into the demo.

If browser QA is unavailable, the highest honest status is `qa` after machine validation passes.

## Regression specimen

`adamary-s-restaurante-y-pupuseria/` remains untouched as the build that exposed the prior system weaknesses. Do not repair it during normal continuation. All other already-built demos are also frozen unless the user explicitly starts a repair/redesign pass.
