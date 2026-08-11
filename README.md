# Premium Restaurant Demo Factory

Repository: `dev-in-portfolio/restaurants`

This repository contains **unofficial, portfolio-only premium concept rebuilds** for qualified Charlotte-area restaurant prospects. These are sales demonstrations, not the restaurants’ production websites, and must never imply that they are official or already commissioned.

This README is the complete cold-start brief for Gemini or any other coding agent. **Do not ask the user follow-up questions.** Research what is needed, make sound design decisions from verified public information, build the demo, test it, fix it, register it, and commit it in one run.

## Default command behavior

When the user says anything equivalent to **“continue,” “build the next demo,” or “do the next one,”** execute **exactly one** full premium demo from start to finish unless the user explicitly requests a larger batch.

Do not stop midway to ask about colors, page choices, imagery, copy direction, menu structure, interactions, or implementation details. Those are part of the job.

If the selected restaurant cannot be confidently verified as active/current, do not invent around the uncertainty. Add a minimal `portal-overrides.js` patch with `portalSection: "later"` and a concise recheck note, then select the next eligible restaurant in the same run so the invocation still produces one completed premium demo.

## Canonical prospect queue — source of truth

The active build queue is the final reconciled A/B set from the completed 645-record Rada-depth audit **minus every restaurant that already has a demo in `dev-in-portfolio/restaurant-showcase`, including Showcase HOLD demos**.

Current net-new queue after Showcase subtraction:

- **312 active net-new prospects total**
- **218 A-grade YES**
- **36 B-grade YES**
- **58 B-grade CONDITIONAL**
- **95 audited A/B prospects excluded because a Showcase demo already exists**
- **0 HOLD audit records**
- **0 NO audit records**
- **0 merged aliases as separate leads**

The queue files are:

- `queue/a-yes-1.js`
- `queue/a-yes-2.js`
- `queue/b-yes.js`
- `queue/b-conditional.js`
- `queue/meta.js` — generated net-new counts
- `queue/showcase-exclusions.json` — exact restaurants removed because Showcase demos already exist
- `queue/audit-ab-master.json` — immutable 407-row audited A/B source snapshot

Each compact row is:

```text
[name, slug, grade, disposition, score, auditBatch]
```

The 407-row audit master is preserved in `queue/audit-ab-master.json`. The four active queue files are generated net-new build data after Showcase subtraction. **Do not manually re-add Showcase restaurants.** Build status belongs in `portal-overrides.js`.

The old files `portal-leads-message2-original.js`, `portal-leads-message3.js`, and `portal-concepts-source.html` are legacy historical artifacts only. They are no longer loaded by the portal and are **not** valid prospect sources. Never re-add a restaurant from those files unless it is present in the canonical queue above.

Existing restaurant folders are also **not** proof that a restaurant is currently eligible or complete. They may be old prototypes, prior five-page builds, or historical work. The canonical queue decides eligibility; the current six-page QA standard decides completion.

## Showcase exclusion is mandatory

A restaurant that already has a demo in `dev-in-portfolio/restaurant-showcase` is **not a new-demo candidate**, even if that Showcase record is currently in HOLD. Do not spend a Gemini run rebuilding it unless the user explicitly orders a redo.

Before selecting the next restaurant, run:

```bash
node scripts/sync-showcase-exclusions.mjs
```

The sync reads both `restaurant-showcase/data/restaurants.json` and `restaurant-showcase/data/hold-restaurants.json`, rebuilds the net-new queue from the immutable 407-row audit source, and writes `queue/showcase-exclusions.json`. If Showcase changed, include the resulting queue housekeeping in the same commit.

Never bypass this rule because an old folder exists here, because a Showcase demo is on HOLD, or because the audit grade is A. **Existing Showcase demo = hard exclusion from automatic new-demo rotation.**

## Build-selection order

Select the next `lead` with no verified premium override in this order:

1. A-grade `YES`
2. B-grade `YES`
3. B-grade `CONDITIONAL`

Within each tier, sort alphabetically while ignoring leading `The`, `A`, and `An`.

Skip records with an override that is already `qa`, `premium`, `promoted`, or `promoted_secondary`. Skip `portalSection: "later"` records until explicitly re-verified.

Do not lower an audited grade, promote a B to A, or change the final disposition from the queue. Fresh research may cause a recheck/later decision, but it does not rewrite the historical audit.

## Required research before writing code

Research the selected restaurant using **current public sources**, prioritizing the restaurant’s current owned/official sources. Verify enough to build accurately without another prompt:

- current operating identity and whether it is open;
- canonical domain and any competing/legacy domains;
- current address/location structure and public hours;
- current menu categories and service model;
- ordering and reservation paths;
- founder, chef, family, neighborhood, or origin story when verifiable;
- events, private dining, catering, bar/taproom/bakery/service features where relevant;
- the website/customer-journey weakness that makes the concept worth demonstrating;
- visual cues that genuinely fit this restaurant rather than a generic cuisine stereotype.

Do not assume the old demo folder, old portal card, or old website data is current.

If a fact is uncertain, **omit it instead of asking the user**. If exact menu prices, team names, awards, policies, parking details, or hours cannot be verified, do not fabricate them.

## Mandatory evidence file

Every new premium demo folder must contain `evidence.md` before the build is considered complete.

`evidence.md` must record:

1. restaurant name and queue grade/disposition/score;
2. date of verification;
3. current sources used;
4. verified operating facts used in the demo;
5. the specific website/customer-journey problem the demo addresses;
6. the chosen art direction and why it fits this restaurant;
7. any facts deliberately omitted because they could not be verified;
8. final desktop/mobile/accessibility QA results.

This file exists so later agents do not need another conversation to understand why the demo looks and works the way it does.

## Required deliverable — six substantive pages

A premium demo lives in its canonical `<slug>/` folder and contains **at least six separate linked HTML pages** with genuinely different jobs:

1. `index.html` — premium, conversion-aware home page.
2. `menu.html` — useful, searchable/readable menu exploration; never just a screenshot wall.
3. `story.html` or `about.html` — verified restaurant identity, story, team, or concept.
4. **Restaurant-specific experience page** — examples: drinks, brunch, bakery, taproom, chef’s table, listening room, neighborhood, wine program, coffee program, game-day guide, etc.
5. **Revenue/conversion page** — examples: private dining, catering, groups, events, reservations guidance, ordering guidance, cakes/custom orders, wholesale, or venue booking.
6. `visit.html` or `contact.html` — verified practical information and a clear next action.

A long homepage with anchors does not count as six pages. Tabs, modals, repeated templates, or duplicate layouts do not count as separate substantive pages.

## Premium means premium

The result should look like a restaurant paid a serious studio to rethink its owned digital experience.

### The design must be restaurant-specific

Create a bespoke visual system from the verified concept:

- art direction;
- typography hierarchy;
- color system;
- spacing/rhythm;
- component language;
- imagery treatment;
- motion behavior;
- menu presentation;
- conversion journey.

Do not clone another restaurant folder and swap the name, colors, and copy. Existing builds may be inspected for QA techniques, but **not used as a shell**.

Do not use lazy cuisine stereotypes when the actual restaurant gives you better material. A neighborhood dive bar, chef-driven tasting room, bakery, brewery, family diner, cocktail lounge, ramen shop, coffee roaster, and Dominican restaurant should not emerge from the same visual composition.

### The documented weakness must visibly improve

The concept must solve the reason this restaurant qualified. Examples include:

- one authoritative hours/location system instead of conflicting data;
- a real owned website instead of Facebook/Toast/directories doing all the work;
- clean canonical structure instead of multiple live domains;
- readable menu architecture instead of PDFs/images/vendor fragments;
- active event programming instead of stale event pages;
- real owner/chef/story content instead of template copy;
- private dining/catering/group conversion instead of an unfinished form;
- clean mobile visit planning instead of scattered third-party data.

Do not merely make the homepage prettier.

## Interaction requirement

Every premium demo must include **at least two useful accessible interactions**, with at least one tied to conversion or decision-making.

Good examples:

- menu filtering/search;
- dietary/allergen guidance;
- location selector;
- beer/wine/coffee flight builder;
- group/private-dining planner;
- party-size or event guidance;
- event picker;
- bakery/custom-order planner;
- ordering-path guide;
- dish or pairing explorer.

Hover effects, scroll animation, carousels, decorative counters, anchor scrolling, and fake success messages do **not** satisfy the interaction requirement by themselves.

## Demo safety and factual integrity

- Do not invent menu items, prices, people, awards, dates, locations, opening hours, policies, testimonials, or availability.
- Do not scrape or reuse protected restaurant photography, logos, illustrations, or distinctive brand assets without permission.
- Use original CSS/graphic treatment, appropriately licensed generic imagery, or abstract visual systems when restaurant-owned media cannot be used.
- Do not create a real payment, reservation, order, email, analytics, or form-submission integration.
- Any form in a demo must be clearly non-submitting/demo-safe and must never claim the restaurant received the request.
- Keep API keys, secrets, scraped private data, and customer information out of the repo.
- Every page should make the unofficial concept nature reasonably clear without ruining the presentation.

## Technical baseline

Prefer a static, dependency-light site unless the restaurant-specific interaction genuinely needs more.

Every new folder should normally contain:

```text
<slug>/
  index.html
  menu.html
  story.html or about.html
  <experience-page>.html
  <conversion-page>.html
  visit.html or contact.html
  site.css
  site.js
  evidence.md
```

Use semantic HTML, responsive CSS, progressive enhancement, and plain JavaScript unless there is a real reason not to.

Required accessibility baseline:

- keyboard-operable controls;
- visible focus states;
- meaningful labels;
- usable alt text where imagery is meaningful;
- sufficient contrast;
- logical heading order;
- sensible touch targets;
- `prefers-reduced-motion` support;
- no interaction that requires hover alone.

## One-run QA loop

Do not finish the invocation with known defects. **Fix them during the same run.**

Before setting `premium`:

1. confirm six substantive pages exist;
2. verify every page is linked through navigation and can return to the home page;
3. confirm no lorem ipsum, Wix instructions, raw shortcodes, fake `555` numbers, `email@example.com`, placeholder headings, or template residue remains;
4. verify every restaurant fact used in the pages;
5. test all local links and assets;
6. test both required interactions;
7. confirm demo forms cannot submit real requests or falsely report success;
8. render every page at desktop and mobile widths;
9. fix horizontal overflow, clipping, broken images, dead links, console errors, unreadable text, bad touch targets, and layout collapse;
10. keyboard-test interactive controls and visible focus;
11. verify reduced-motion behavior;
12. document the result in `evidence.md`.

Code inspection is not browser QA. If browser rendering is available, use it. If the environment truly cannot browser-render, status may reach `qa` but **not `premium`**.

## Portal/status workflow

The portal renders only the canonical audited queue plus `portal-overrides.js`.

Base queue records always begin as `lead`. After the demo is created, add a **minimal patch** to `portal-overrides.js`; do not duplicate the entire queue record.

Examples:

```js
{ name: "Restaurant Name", status: "qa", href: "restaurant-slug/index.html" }
```

```js
{ name: "Restaurant Name", status: "premium", href: "restaurant-slug/index.html" }
```

The renderer preserves the audited grade/disposition/score from the queue and applies the override only as build status/presentation metadata.

Allowed statuses:

- `lead` — audited and eligible; no current verified six-page build.
- `incomplete` — a folder/build exists but the current six-page standard is not met.
- `qa` — six substantive pages exist and implementation QA is complete enough for browser QA, but premium browser verification is not finished.
- `premium` — six pages, required interactions, desktop/mobile browser QA, accessibility baseline, and evidence all pass.
- `promoted` / `promoted_secondary` — only when explicitly approved for showcase placement.
- `portalSection: "later"` — fresh verification shows the prospect should temporarily leave automatic build rotation.

Never mark a record premium because a folder already exists or because an old build was previously called premium under a different standard.

## Existing folders

Old restaurant folders are legacy working material. For a selected canonical prospect:

- inspect its existing folder if one exists;
- retain any accurate material worth keeping;
- **rebuild or replace whatever is necessary** to satisfy this README;
- do not preserve a weak five-page structure merely because it already exists;
- do not let an old folder determine the new art direction.

Folders for restaurants outside the current net-new queue are historical only and must not be selected automatically. Showcase restaurants remain excluded even if a similarly named folder exists here.

## Collaboration and commits

- Re-fetch latest `main` before touching shared files.
- Work primarily inside the selected restaurant folder.
- Re-fetch `portal-overrides.js` immediately before updating it.
- Preserve unrelated concurrent work.
- Do not hard-reset, force-push, or revert someone else’s changes.
- Commit the complete demo and its status patch with a focused message.
- Verify the selected restaurant route and portal card exist on `main` after the commit.

## Definition of done

A run is complete only when **one canonical eligible restaurant** has:

- current facts researched without user follow-up;
- `evidence.md` written;
- a bespoke six-page premium demo;
- at least two useful interactions, including one conversion interaction;
- accurate, safe, non-deceptive content;
- responsive and accessible behavior;
- desktop/mobile QA performed and defects fixed in the same run;
- a correct portal override (`qa` or `premium`, never an inflated claim);
- a committed, published `main` result.

If any of those are missing, the build is not done.
