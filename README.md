# Charlotte-Area Restaurant Website Rebuild Portal

Repository: **https://github.com/dev-in-portfolio/restaurants**

This repo is Devin's restaurant lead portal and portfolio of unofficial restaurant-specific website rebuilds.

## Current truth

No restaurant is currently marked complete or premium.

The project now requires **six separate substantive pages**. Existing five-page builds—including Boudreaux's—remain useful work, but they are incomplete under the current standard until a sixth page is added and the full site passes verification.

The portal therefore uses these statuses:

- **LEAD • NOT BUILT YET** — queued prospect with no usable rebuild.
- **INCOMPLETE • 6-PAGE STANDARD NOT MET** — an existing build that has not been verified as six separate substantive pages.
- **6/6 PAGES • QA PENDING** — six pages exist, but premium browser QA is not finished.
- **PREMIUM • 6-PAGE IDENTITY REBUILD** — six pages, restaurant-specific interactions, and desktop/mobile browser QA all pass.

Do not use `full`, `complete`, `finished`, or `premium` merely because a folder, homepage, card, or five-page site exists.

## First response and automatic continuation

Do not ask Devin which letter to begin with.

Fetch the latest `main`, inspect the current portal records and automatically select the next eligible restaurant that needs an upgrade.

Prioritize existing incomplete builds before unbuilt leads. Within each category, select alphabetically while ignoring leading **The**, **A** and **An**.

Begin the selected restaurant immediately.

After completing, validating, committing and publishing it to `main`, automatically select the next eligible restaurant and continue. Do not wait for Devin to say `continue`.

Skip restaurants that are already promoted, meaningful upgrades, premium, QA pending, placed in At a Later Time, inactive, duplicated, awaiting verification or already being handled by another model.

## Selection priority

Choose restaurants in this order:

1. Existing `incomplete` builds that do not meet the six-page standard.
2. Eligible `lead` restaurants that do not yet have a usable rebuild.

Do not automatically select restaurants classified as:

- `promoted`
- `promoted_secondary`
- `premium`
- `qa`
- `later` or `portalSection: "later"`
- closed
- inactive
- duplicate legacy records
- awaiting business-status verification

Before starting, verify that another active model or recent commit is not already working on that restaurant. If it is, skip it and select the next eligible restaurant.

## Hard exclusion: At a Later Time

Any restaurant assigned to the **At a Later Time** section is not eligible for automatic work.

A restaurant must be excluded whenever its canonical portal record contains `portalSection: "later"` or an equivalent field used by the portal to place it in the later section. This placement exclusion overrides the restaurant's technical build status.

Therefore, a restaurant in **At a Later Time** must be ignored even when its technical status is `incomplete`, `lead`, `qa`, `premium`, or any other status.

### Automatic workflow behavior

Before constructing the next-work queue, the model must:

1. Resolve restaurants through their canonical records and alias mappings.
2. Remove every restaurant assigned to **At a Later Time**.
3. Remove promoted, meaningful-upgrade, premium and QA-pending restaurants.
4. Remove closed, inactive, duplicate and business-verification-pending restaurants.
5. Remove restaurants already being handled by another active model.
6. Prioritize the remaining `incomplete` builds.
7. If no eligible incomplete builds remain, select the next eligible `lead`.
8. Sort eligible restaurants alphabetically while ignoring leading **The**, **A** and **An**.
9. Begin the next eligible restaurant automatically.

### Prohibited actions

The autonomous workflow must never automatically:

- rebuild an At a Later Time restaurant;
- upgrade it;
- perform QA on it;
- promote it;
- copy it into staging;
- change its status;
- remove its later placement;
- return it to the normal alphabetical work queue;
- select it as the next restaurant needing work.

Later-section restaurants must be skipped silently while the workflow continues to the next eligible restaurant.

### Canonical-name handling

The exclusion must use the canonical restaurant record and existing aliases.

A later-section restaurant must not bypass the exclusion because of accented versus unaccented characters, apostrophe differences, punctuation differences, capitalization differences, corrupted legacy text, alternate names, renamed records, or duplicate legacy cards.

## Six-page deliverable

Every completed restaurant rebuild must have at least six separate, substantive HTML pages:

1. **Home** — `<restaurant-slug>/index.html`
2. **Menu**
3. **Story / About**
4. **Restaurant-specific experience page** — brunch, taproom, bakery, neighborhood guide, drinks, locations, entertainment, or another real need
5. **Conversion page** — catering, reservations, private dining, events, ordering, group dining, parties, or another real conversion path
6. **Visit / Contact**

Six homepage sections, anchor links, tabs, modal panels, or repeated copies of one layout do not count as six pages.

Each page must have its own purpose, composition, useful content, responsive state, and working navigation.

## Research and accuracy

Use current official sources and recent reliable coverage. Verify the restaurant's identity, location, menu structure, hours, ordering/reservation paths, social accounts, story, visual character, and actual website weaknesses.

Do not invent prices, menu items, owners, history, awards, policies, hours, integrations, availability, or contact details.

Public restaurant contact information may be used when verified. Secrets, tokens, private credentials, and private customer data must never be committed.

## No template sludge

Each restaurant must have its own visual identity, information architecture, page rhythm, interactions, and conversion journey.

Do not reuse one shared restaurant shell with different names and colors. Shared resets, accessibility helpers, navigation utilities, and safe demo-form behavior are allowed; repeated restaurant layouts are not.

Boudreaux's demonstrates restaurant-specific visual thinking, but it is currently a five-page incomplete build—not a complete or premium status reference.

## Required interactions

Include at least two useful restaurant-specific interactions, including one conversion-oriented interaction.

Examples: menu search/filter, meal-time selector, catering estimator, party planner, location selector, order guide, tasting builder, pairing finder, reservation guide, event controls, dietary filter, or group-order builder.

Decorative animation, hover effects, anchor scrolling, and fake form success messages do not count by themselves.

Forms must not submit or claim a request was received unless a real approved integration exists.

## Browser QA

Before a card can reach **6/6 PAGES • QA PENDING**, confirm all six pages exist and are linked.

Before a card can reach **PREMIUM • 6-PAGE IDENTITY REBUILD**, browser-render and inspect every page at desktop and mobile sizes. Check navigation, touch targets, keyboard access, contrast, clipping, overflow, assets, links, interactions, and page-to-page quality.

Code inspection alone does not prove premium quality.

## Portal files

The portal is intentionally separated to reduce collisions:

- `index.html` — clean portal shell
- `portal.js` — loading, deduplication, status enforcement, sorting and rendering
- `portal-concepts-source.html` — preserved legacy portal data source; do not edit
- `portal-overrides.js` — add or replace restaurant records here
- `portal-leads-message2-original.js` and `portal-leads-message3.js` — queued lead sources

The portal automatically treats all legacy `full` and `premium` entries as **incomplete** until a current override explicitly proves a six-page status.

When updating `portal-overrides.js`, re-fetch the latest file first and preserve every unrelated entry.

## Play nice

Multiple models may work in this repo simultaneously. New commits, comments, files, folders, branches, QA output, and portal entries are normal.

- Fetch the latest `main` before starting.
- Re-fetch shared files immediately before editing them.
- Preserve unrelated work.
- Work mainly inside the assigned restaurant folder.
- Integrate compatible concurrent changes.
- Never hard reset, force-push, move `main` backward, delete unfamiliar work, or revert a commit merely because another model made it.

When another model pushes first: **okay, nice.** Take a breath, fetch the latest `main`, keep their valid work, reapply or merge yours, validate the combined result, and retry.

Escalate only when two changes are genuinely incompatible and cannot both be preserved.

## Publishing and continuation

For each restaurant:

1. Fetch latest `main`.
2. Research and build six substantive pages.
3. Add at least two useful interactions.
4. Validate code, routes, links, assets and forms.
5. Browser-test all six pages on desktop and mobile.
6. Fetch latest `main` again.
7. Integrate concurrent work.
8. Update `portal-overrides.js` with the honest status.
9. Commit, push and merge to `main`.
10. Confirm the folder, portal route and status are present on `main`.
11. Automatically select the next eligible restaurant and begin work immediately.

Do not leave completed work on an unmerged branch.

## Completion rule

A restaurant is not complete until six separate substantive pages exist, required interactions work, desktop/mobile QA passes, the portal status is accurate, and everything is published on `main`.
