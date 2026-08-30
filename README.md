# Premium Restaurant Demo Factory

Repository: `dev-in-portfolio/restaurants`

This repository contains **unofficial, portfolio-only premium concept rebuilds** for qualified Charlotte-area restaurant prospects. These are sales demonstrations, not production websites, and must never imply that they are official or already commissioned.

This README is the operating contract for Gemini or any other coding agent.

## Mandatory read order

Before selecting or building anything, read these files in full:

1. `README.md`
2. `ADD_ON_BOUNDARY.md`
3. `BUILD_QUALITY_GATE.md`
4. `STATUS.md`
5. `PORTAL_AUDIT.md`

`ADD_ON_BOUNDARY.md` protects separately sellable DSC scope.

`BUILD_QUALITY_GATE.md` controls page architecture, factual provenance, anti-template design quality, machine validation, and browser QA.

If older historical material conflicts with those files, the current README + boundary + quality gate control.

## Governing sales rule

> **Premium core demo, preserved upsell surface.**

The demo should make the restaurant want the core website because the **design itself is excellent**.

Premium comes from:

- restaurant-specific art direction;
- typography;
- composition;
- information hierarchy;
- responsive execution;
- storytelling supported by evidence;
- menu presentation;
- polish;
- usability;
- mobile quality.

Premium does **not** come from giving away separately sellable DSC add-ons.

## Default command behavior

When the user says anything equivalent to **“continue,” “build the next demo,” or “do the next one,”** complete exactly **one** eligible premium-core demo end-to-end unless the user explicitly requests a batch.

Do not stop to ask about colors, page choices, imagery, layout, or ordinary implementation decisions.

Do not stop after research or planning.

If the selected restaurant cannot be confidently verified as active/current, add a minimal `portalSection: "later"` override with a concise recheck note and continue to the next eligible restaurant so the run still produces one completed demo.

## Start current

Work from current `main`.

Before selection:

```bash
node scripts/sync-showcase-exclusions.mjs
```

Use the generated queue after that sync. Do not rely on remembered counts.

## Canonical prospect queue

The active build queue is assembled dynamically from the authoritative prospect sources, then excludes restaurants already represented in `dev-in-portfolio/restaurant-showcase` (including active and HOLD inventory).

Do **not** hard-code, copy forward, or rely on queue totals in this README. The inventory changes as prospects are added, reconciled, built, promoted, held, archived, or explicitly removed.

Authoritative prospect sources:

1. **Original Rada-Depth Audit** — canonical audited A/B prospect source.
2. **Charlotte Restaurant Prospect Sweep (2026-08-28)** — canonical supplemental sweep source.

After running:

```bash
node scripts/sync-showcase-exclusions.mjs
```

treat the generated queue state as current. `queue/meta.js` and the generated exclusion data are the runtime authority for what is presently eligible; this README intentionally does not publish inventory figures.

Canonical data:

- `queue/a-yes-1.js`
- `queue/a-yes-2.js`
- `queue/b-yes.js`
- `queue/b-conditional.js`
- `queue/sweep-2026-08-28.js` — generated active supplemental sweep prospects
- `queue/meta.js` — generated current queue metadata
- `queue/showcase-exclusions.json` — exact restaurants removed because Showcase demos already exist or duplicate an existing audit record
- `queue/audit-ab-master.json` — immutable audited A/B source snapshot
- `queue/charlotte-prospect-sweep-2026-08-28.json` — authoritative supplemental sweep source snapshot

Do not select from old restaurant folders, retired lead scripts, or `portal-concepts-source.html`.

Existing Showcase demo = hard exclusion from automatic new-demo rotation unless the user explicitly requests a redo.

## Selection order

Choose the next eligible `lead` in this order:

1. A-grade YES (Audit) / A+ (Sweep)
2. A (Sweep)
3. B-grade YES (Audit)
4. B-grade CONDITIONAL (Audit) / B (Sweep)

Within the highest available tier, sort alphabetically while ignoring leading `The`, `A`, and `An`.

Skip:

- Showcase exclusions;
- HOLD;
- NO;
- merged aliases;
- closed/inactive/out-of-scope businesses;
- legitimate `qa`, `premium`, `promoted`, or `promoted_secondary` overrides;
- `portalSection: "later"` records.

Do not rewrite historical audit grade, disposition, score, or canonical identity to make a restaurant eligible.

## Research before code

Use current public sources, prioritizing owned/official sources.

Verify enough to build accurately:

- current operating identity;
- canonical domain and competing/legacy domains;
- address/location structure;
- public hours;
- current phone/contact information;
- menu categories and service model;
- current ordering/reservation paths;
- founder/chef/family/history only when directly verifiable;
- catering/private dining/events only when directly verifiable;
- the website/customer-journey weakness that makes the demo worth showing;
- real restaurant-specific visual/content anchors;
- likely DSC add-on opportunities that should remain sellable.

If a fact is uncertain, omit it.

General cuisine knowledge may be used as clearly framed editorial context. It may **not** be rewritten as a restaurant-specific claim without a source.

## Evidence file

Every new qualifying build must contain `evidence.md`.

At minimum it must include:

### Prospect Summary

- canonical restaurant;
- grade/disposition/score;
- audit batch;
- verification date.

### Verification Sources

Current source URLs actually used.

### Original Audit Weakness

The specific customer-journey/web problem being demonstrated.

### Creative Brief

Required by `BUILD_QUALITY_GATE.md`:

- at least three verified restaurant-specific visual/content anchors;
- three concrete **core design moves** that create restaurant-specific visual authorship without using paid add-on functionality.

### Claim Ledger

For meaningful restaurant-specific claims used in the pages, record:

- claim;
- page;
- source URL.

Claims such as house-made, imported, founded to, family-owned, hand-patted, most popular, chef recommended, catering packages, guest capacities, parking/accessibility, recurring events, and preparation methods require direct support.

### Add-On Preservation

Record:

- relevant DSC add-on opportunities;
- what was intentionally not implemented;
- what remains available for the proposal/production phase.

### QA

Record actual QA performed. Do not claim checks that were not performed.

## Page architecture — evidence-led, not quota-led

The old fixed six-page quota is retired when the evidence does not support six genuinely different pages.

An automatic premium-core demo requires **at least five substantive linked HTML pages**.

Six is preferred only when current verified material genuinely supports a sixth distinct page.

Normal core coverage includes:

1. `index.html` — premium homepage;
2. `menu.html` — clear verified menu presentation;
3. `visit.html` or `contact.html` — verified practical information and current CTA path;
4. one identity/story/concept page supported by restaurant-specific evidence;
5. one restaurant-specific editorial or conversion page supported by an actually verified service, program, product focus, or customer need.

A sixth page is welcome when it has a real independent job and enough evidence.

Do **not** manufacture:

- a founder/history story because a story page sounds premium;
- catering/private-event inventory because a conversion page is expected;
- a generic cuisine-education page written as if it documents the restaurant's actual process;
- filler pages merely to hit a number.

If verified story material is thin, use a better-supported concept/editorial page or omit that page slot.

## Premium core design requirement

The result should look like a serious studio rethought the restaurant's owned web presence.

Premium must be visible **before** considering functionality.

Create restaurant-specific:

- art direction;
- typography hierarchy;
- color logic;
- spacing/rhythm;
- composition;
- imagery treatment;
- menu presentation;
- page hierarchy;
- motion behavior where useful.

Do not clone another restaurant folder and swap copy/colors.

Do not default to cuisine stereotypes.

Do not let the entire site become:

> dark-overlay hero → centered headline → pill buttons → three cards → alternating two-column sections → generic footer

That pattern may appear in part but cannot be the whole visual language.

At least two substantive pages must use meaningfully different composition families.

Before QA, perform the `BUILD_QUALITY_GATE.md` swap test:

> If the restaurant name, food nouns, colors, and images were replaced, would this still look like the same site for another restaurant?

If yes, redesign before QA.

## Solve the audit weakness at core level

Use the audit to understand **why the restaurant is a prospect**.

Do not use the audit's Recommended Website Solution or Missed Opportunities columns as a feature checklist.

Examples:

- conflicting hours → show one clear verified hours/location system;
- social/ordering-platform dependency → show the value of a real owned website;
- multiple domains → demonstrate one clean canonical information architecture;
- unreadable menu → build a strong readable menu while preserving Menu Experience/Concierge upsells;
- weak catering/private dining → present only verified service information and a strong current CTA while preserving advanced catering/event functionality;
- fragmented ordering/reservations → route clearly to verified existing providers while preserving Order & Reserve enhancements.

## Add-on ceiling

`ADD_ON_BOUNDARY.md` is authoritative.

Do not automatically build separately sellable DSC functionality such as:

- planners, builders, calculators, configurators, quizzes, recommendation engines;
- Signature Interactive Experiences;
- Digital Menu Concierge;
- advanced menu search/filter/dietary/pairing systems;
- custom ordering/reservation/waitlist/payment systems;
- advanced catering/private-event tools;
- loyalty/rewards/accounts;
- newsletter/SMS/CRM/marketing automation;
- reputation automation;
- advanced Photo Story, Local Discovery, Menu Collections, or Multi-Location Growth implementations.

### No automatic-demo forms

Automatic prospect demos do not include inquiry, catering, reservation, newsletter, contact, or lead-capture forms, even when they are non-submitting demo forms.

Use verified current phone/email/order/reservation links instead.

Judge the boundary by **commercial capability**, not technical complexity.

If something feels like a feature DSC could charge extra for, preserve it as an upsell.

## No invented conversion inventory

A verified service can be presented beautifully.

Do not invent its commercial details.

Never fabricate:

- package names;
- tray sizes;
- serving counts;
- guest capacities;
- minimum orders;
- package contents;
- event availability;
- lead times;
- delivery zones;
- booking rules.

## Allowed baseline interactions

Ordinary core UI is fine:

- mobile navigation;
- accordions;
- ordinary content tabs;
- simple galleries;
- subtle motion;
- anchor navigation;
- normal links/buttons to verified current services.

A premium demo does not need custom interactive features.

## Demo safety and factual integrity

- No invented menu items, prices, people, awards, dates, locations, hours, policies, testimonials, events, or availability.
- No unsupported restaurant-specific preparation/sourcing claims.
- Do not reuse protected restaurant photography/logos/illustrations without permission.
- Use original visual treatment, appropriately licensed/generic imagery, or abstract systems when needed.
- Do not create real payments, orders, reservations, email delivery, analytics, or data collection.
- Keep secrets and private data out of the repo.
- Keep the unofficial concept nature reasonably clear without ruining the presentation.

## Technical baseline

Prefer a dependency-light static site.

Typical folder:

```text
<slug>/
  index.html
  menu.html
  <identity-or-concept-page>.html
  <restaurant-specific-page>.html
  visit.html or contact.html
  [optional sixth substantive page].html
  site.css
  site.js
  evidence.md
  qa-report.json
```

Use semantic HTML, responsive CSS, progressive enhancement, and plain JavaScript unless there is a real need for something else.

Accessibility baseline:

- keyboard-operable controls;
- visible focus states;
- meaningful labels;
- alt text for meaningful imagery;
- sufficient contrast;
- logical heading order;
- sensible touch targets;
- `prefers-reduced-motion` support;
- no hover-only interaction.

## Machine QA is mandatory

Before `qa` or `premium`, run:

```bash
node scripts/validate-demo.mjs <restaurant-slug>
```

The validator writes `<slug>/qa-report.json`.

A non-zero exit code means the build is **not `qa` and not `premium`**.

Fix the failures and rerun.

The validator checks objective defects including:

- minimum page/core-file structure;
- CSS brace balance;
- JavaScript parse errors;
- broken local links/assets;
- broken fragment/deep links;
- duplicate IDs;
- missing image alt attributes;
- placeholder/test residue;
- prohibited automatic-demo forms;
- missing home-return links;
- missing required evidence sections.

`evidence.md` may not override failed machine validation.

## Browser QA

Machine QA does not replace browser QA.

If browser rendering is available, inspect the rendered result.

At minimum:

- homepage desktop + mobile;
- menu desktop + mobile;
- most restaurant-specific page desktop + mobile;
- navigation on every page;
- console output;
- overflow/clipping;
- keyboard/focus behavior.

Do not write “zero console errors,” “tested at 360px,” or similar statements unless those checks actually happened.

If browser rendering is unavailable, say so plainly. The highest honest status is `qa` after the machine validator passes.

## Portal/status workflow

The portal renders the canonical audited net-new queue plus `portal-overrides.js`.

Use minimal build-status patches only.

Examples:

```js
{ name: "Restaurant Name", status: "qa", href: "restaurant-slug/index.html" }
```

```js
{ name: "Restaurant Name", status: "premium", href: "restaurant-slug/index.html" }
```

Allowed statuses:

- `lead` — eligible, no current qualifying build;
- `incomplete` — build exists but fails current structure/facts/design/validation;
- `qa` — machine validator passes and implementation is ready for/has partial browser QA;
- `premium` — machine validator passes, provenance is sound, anti-template design gate passes, add-ons remain preserved, and full desktop/mobile browser QA passes;
- `promoted` / `promoted_secondary` — only when explicitly approved for Showcase;
- `portalSection: "later"` — fresh verification shows the prospect needs recheck before automatic selection.

Never mark premium because a folder merely exists or because an old build used that label under an older standard.

## Existing folders

For a selected eligible prospect with an old folder:

- inspect it;
- retain accurate material worth keeping;
- rebuild or replace what is necessary to meet the current README, `ADD_ON_BOUNDARY.md`, and `BUILD_QUALITY_GATE.md`;
- do not let the old folder dictate art direction;
- remove old add-on functionality if it would now give away sellable scope.

Folders outside the current net-new queue are historical only and are never selected automatically.

## Collaboration and commits

- Re-fetch latest `main` before shared-file edits.
- Work primarily inside the selected restaurant folder.
- Re-fetch `portal-overrides.js` immediately before editing it.
- Preserve unrelated concurrent work.
- Do not hard-reset, force-push, mass-delete, or revert unrelated work.
- Commit focused changes.
- Verify final local HEAD matches `origin/main` after push.

## Definition of done

One automatic run is complete only when one eligible restaurant has:

- current facts researched;
- required `evidence.md` sections;
- at least five substantive evidence-supported pages;
- premium restaurant-specific core design that passes the anti-template swap test;
- separately sellable add-ons preserved;
- no invented conversion inventory;
- no automatic-demo forms;
- `node scripts/validate-demo.mjs <slug>` passing;
- responsive/accessibility implementation;
- truthful browser QA status;
- correct portal override;
- committed/pushed final result.

If any required gate is missing, the build is not done.

## Regression specimen

`adamary-s-restaurante-y-pupuseria/` is intentionally left unchanged as the build that exposed the previous system weaknesses. Do not silently repair it during build-system housekeeping. Use it as a regression specimen for the new validator and quality rules.
