# Charlotte-Area Restaurant Website Rebuild Portal

Repository: **https://github.com/dev-in-portfolio/restaurants**

This repo is Devin’s restaurant lead portal and portfolio of unofficial restaurant-specific website rebuilds.

## Current truth

No restaurant is currently marked complete or premium.

The project now requires **six separate substantive pages**. Existing five-page builds—including Boudreaux’s—remain useful work, but they are incomplete under the current standard until a sixth page is added and the full site passes verification.

The portal therefore uses these statuses:

- **LEAD • NOT BUILT YET** — queued prospect with no usable rebuild.
- **INCOMPLETE • 6-PAGE STANDARD NOT MET** — an existing build that has not been verified as six separate substantive pages.
- **6/6 PAGES • QA PENDING** — six pages exist, but premium browser QA is not finished.
- **PREMIUM • 6-PAGE IDENTITY REBUILD** — six pages, restaurant-specific interactions, and desktop/mobile browser QA all pass.

Do not use `full`, `complete`, `finished`, or `premium` merely because a folder, homepage, card, or five-page site exists.

## First response for a model

Read the latest `README.md` and latest `main`, then ask exactly:

> **Which letter should I start building?**

After Devin gives a letter, choose the first eligible queued restaurant under that letter, ignoring leading **The**, **A**, and **An** for alphabetization.

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

Use current official sources and recent reliable coverage. Verify the restaurant’s identity, location, menu structure, hours, ordering/reservation paths, social accounts, story, visual character, and actual website weaknesses.

Do not invent prices, menu items, owners, history, awards, policies, hours, integrations, availability, or contact details.

Public restaurant contact information may be used when verified. Secrets, tokens, private credentials, and private customer data must never be committed.

## No template sludge

Each restaurant must have its own visual identity, information architecture, page rhythm, interactions, and conversion journey.

Do not reuse one shared restaurant shell with different names and colors. Shared resets, accessibility helpers, navigation utilities, and safe demo-form behavior are allowed; repeated restaurant layouts are not.

Boudreaux’s demonstrates restaurant-specific visual thinking, but it is currently a five-page incomplete build—not a complete or premium status reference.

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
11. Automatically begin the next eligible queued restaurant under the assigned letter.

Do not leave completed work on an unmerged branch. Do not wait for Devin to say **continue**.

## Completion rule

A restaurant is not complete until six separate substantive pages exist, required interactions work, desktop/mobile QA passes, the portal status is accurate, and everything is published on `main`.
