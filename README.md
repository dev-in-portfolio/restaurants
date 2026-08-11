# Premium Restaurant Demo Factory

Repository: `dev-in-portfolio/restaurants`

This repository contains **unofficial, portfolio-only concept rebuilds** for qualified Charlotte-area restaurant prospects. A concept demonstrates what a better owned web experience could be; it is not the restaurant's production website and must never imply that it is.

This document is a cold-start instruction set. Treat it as the complete brief: inspect the repository and current prospect record, make the next eligible demo, validate it, and publish the result. Do not ask follow-up questions unless a required fact cannot be verified from official sources.

## Non-negotiable outcome

Build a genuinely restaurant-specific, premium six-page experience that a restaurant owner could recognize as made for their business—not a recolored template or a generic food site. Ship it only when it is accurate, polished, accessible, and registered in the portal with an honest status.

## Scope and safety

- Use only current, public, verifiable business information from official restaurant sources and reputable current coverage.
- Do not invent menu items, prices, people, awards, dates, hours, locations, policies, integrations, availability, or customer testimonials.
- Do not copy protected restaurant photography, logos, or distinctive brand assets without permission. Use original/appropriately licensed visual treatment, CSS art, abstract imagery, or clearly generic imagery.
- Do not add real payment, order, reservation, email, analytics, or form-submission integrations unless they already exist in the repository and have been approved. A demo form must clearly behave as a demo and must not claim a message or booking was received.
- Keep secrets, API keys, customer data, and scraped private data out of the repository.
- Do not modify, delete, or overwrite an existing restaurant build merely because it is incomplete. Existing folders, shared assets, scripts, templates, and archived lead sources are retained unless a task explicitly says otherwise.

## The canonical queue

The active queue must contain only reconciled records from the final restaurant audit. A record is eligible only when all of the following are true:

1. It has final disposition `YES` or `CONDITIONAL`.
2. Its final grade is `A` or `B`.
3. It is an active, in-scope business—not `HOLD`, `NO`, closed, inactive, out of scope, or awaiting operating-status verification.
4. It is the canonical identity after aliases, duplicate rows, and rebrands are merged.

Never infer eligibility from an old portal card, a folder name, or a preliminary research note. The final reconciled audit is the source of truth. In particular, do not re-add merged aliases, closed names, or businesses that require a recheck.

When changing the queue, preserve the legacy source files as archives if useful, but ensure the rendered portal reads only the canonical audited queue. Do not expose archived or excluded records as active lead cards.

Every active queue record must contain:

- canonical restaurant name and stable slug;
- area/location label;
- final grade and final disposition;
- concise, evidence-based issue summary;
- a demo direction tied to the actual restaurant and its documented weakness;
- status `lead` until a verified build is registered.

## Selecting the next build

Work autonomously. First fetch the latest `main`, inspect the active audited queue, existing folders, and overrides, then select the next eligible restaurant.

Priority order:

1. an active A-grade `YES` lead without a verified six-page build;
2. an active B-grade `YES` lead without a verified six-page build;
3. an active A-grade `CONDITIONAL` lead;
4. an active B-grade `CONDITIONAL` lead.

Within a tier, work alphabetically ignoring `The`, `A`, and `An`. Skip any restaurant already in active work, an archival/later section, or with an accurate `qa`, `premium`, `promoted`, or `promoted_secondary` status. Do not change an excluded record just to make it eligible.

If a current official source conflicts materially with the audit, verify before building. If the restaurant is closed, has changed identity, or cannot be confidently verified as active, mark the queue record for recheck rather than producing a speculative demo.

## Research packet before implementation

Before writing pages, collect a compact, source-backed packet in the restaurant folder or its audit note:

- canonical identity, current location(s), service model, and current public hours;
- current menu categories and at least enough verified content for a credible menu structure;
- real story, cuisine, neighborhood context, and differentiators;
- the exact documented website weakness this concept improves;
- 2–3 visual/art-direction cues that fit the business;
- the correct conversion path (for example private dining, catering, booking guidance, ordering guidance, events, or visit planning).

If any detail is unknown, omit it or use clearly generic demo copy. Accuracy beats density.

## Required deliverable: six substantive pages

Each completed concept lives in its own `<restaurant-slug>/` directory and includes at least these six separate, linked HTML pages:

1. `index.html` — conversion-aware home page.
2. `menu.html` — useful menu exploration, not a screenshot wall.
3. `story.html` or `about.html` — real restaurant story and identity.
4. A restaurant-specific experience page — for example drinks, brunch, bakery, location guide, taproom, chef's table, or neighborhood guide.
5. A conversion page — for example private dining, catering, groups, reservations, events, or ordering guidance.
6. `visit.html` or `contact.html` — location, verified practical information, accessibility/parking/transit guidance where applicable, and clear next action.

Anchors, tabs, modals, duplicated layouts, and homepage sections do not count as separate pages. Every page needs a distinct job, meaningful content, responsive layout, and working navigation.

## Premium quality bar

The demo must feel deliberately art-directed for this restaurant:

- establish a distinctive visual system: typography, color, rhythm, imagery treatment, components, and motion appropriate to the concept;
- use a page hierarchy and content flow that is specific to the restaurant's business model;
- make the restaurant's documented problem visibly better (for example one clear source of truth for hours/locations, a readable menu, an integrated event path, or a proper owned-web home);
- provide at least two meaningful, accessible interactions, including one conversion-oriented interaction;
- ensure interactions change useful state or help a guest decide—decorative animation, hover states, anchor scrolling, and fake submissions do not count;
- use semantic HTML, keyboard-operable controls, visible focus states, adequate contrast, meaningful labels/alt text, and reduced-motion support.

Permitted interaction examples include menu filtering/search, dietary guidance, group-planning estimator, location selector, event picker, order guide, flight builder, or reservation/party-size guidance. Build the interaction around verified restaurant needs; do not add a random feature solely to meet a quota.

## Reuse versus repetition

Shared primitives are encouraged: resets, accessible navigation helpers, form safeguards, QA utilities, and small generic UI components. A reused restaurant shell is not.

Do not clone a prior restaurant folder and only swap names, colors, and text. New work must have its own layout composition, visual hierarchy, interaction model, content architecture, and conversion journey. Existing folders are references for quality—not templates to duplicate.

## Portal data and statuses

The portal is data-driven. Keep the renderer and shared scripts stable; change only the canonical queue/override data needed for the restaurant you are completing. Re-fetch shared files immediately before changing them.

Use statuses honestly:

- `lead` — audited, eligible prospect; no verified six-page concept.
- `incomplete` — a build exists but does not meet the six-page standard.
- `qa` — all six substantive pages exist and are linked; browser QA is still pending.
- `premium` — six substantive pages, required interactions, and desktop/mobile browser QA all pass.
- `promoted` / `promoted_secondary` — reserved for explicitly approved showcase work.
- `portalSection: "later"` — excluded from automatic selection regardless of status.

Never label a card `qa`, `premium`, `promoted`, or complete because a folder exists, because it has five pages, or because the homepage looks good.

## QA gate

Before committing:

1. Confirm the six required pages exist and navigation works in both directions.
2. Verify all facts, links, labels, and conversion paths against the research packet.
3. Test every interaction and make sure demo forms cannot send or falsely confirm a real request.
4. Browser-render each page at desktop and mobile widths.
5. Check no horizontal overflow, clipping, broken assets, console errors, dead links, unreadable contrast, inaccessible controls, or touch-target failures.
6. Check keyboard navigation, focus visibility, and reduced-motion behavior.
7. Update the portal record only to the status actually earned.

Code review alone is not browser QA.

## Collaboration and publishing

Multiple agents may work here. Preserve unrelated work.

1. Fetch latest `main` before starting and again immediately before editing a shared portal file.
2. Work primarily within the selected restaurant folder.
3. Do not hard-reset, force-push, revert another contributor's work, or delete unfamiliar files.
4. If a compatible change arrives first, integrate it, re-run validation, and continue.
5. Commit focused changes, push to `main`, and verify that the portal entry and restaurant route are present on `main`.
6. Once one restaurant is fully published, select the next eligible record and continue without waiting for a follow-up prompt.

## Definition of done

A restaurant concept is done only when it has an evidence-based, restaurant-specific six-page demo; two useful interactions including a conversion interaction; passing desktop and mobile browser QA; an accurate portal status; and a published `main` commit.
