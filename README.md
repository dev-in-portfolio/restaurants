# Charlotte-Area Restaurant Website Demo Factory

This repository is a sales portfolio of custom, unofficial restaurant website redesign concepts.

The goal is for Devin to walk into an independent restaurant and say:

> “I already redesigned your website. Here is what it could look like.”

These are presentation demos—not live restaurant websites, ordering systems, reservation systems, or a consumer directory.

## Automatic workflow for connected threads

When this repository is connected and the user sends only a restaurant list, immediately:

1. Verify each restaurant is open and identify the correct location.
2. Research Google Business information, the official website, official social accounts, current menus, ordering/reservation services and recent reliable local coverage.
3. Identify the restaurant’s actual digital weaknesses and strongest sales opportunity.
4. Build the demos completely.
5. Validate the files and interactions.
6. Commit and push every completed demo.
7. Ensure the changes are on the default branch before reporting completion.

Do not ask the user to repeat the project, choose a template, approve a plan, request a commit, request a push or remember to merge.

Publishing is automatic unless GitHub permissions technically prevent it. If permissions block completion, report the exact blocker.

## Non-negotiable definition of a bespoke premium demo

A demo may be labeled **BESPOKE** or **PREMIUM** only when all of the following are true:

- The restaurant’s real default page is `<restaurant-slug>/index.html`.
- The page is individually authored for that restaurant.
- The page has a restaurant-specific layout and section order.
- The page has a distinct visual identity appropriate to that business.
- The page includes at least one meaningful restaurant-specific interaction, such as a menu finder, event planner, catering estimator, meal switcher, heat ladder, pairing tool, curb-service guide or group-order builder.
- The customer journey is based on that restaurant’s actual needs.
- The copy is based on verified facts or clearly labeled proposed functionality.
- The form is visibly a demo and never submits data.
- The page works responsively on mobile and desktop.
- The page has been structurally and JavaScript validated.

A shared stylesheet may provide resets, accessibility utilities, typography loading and non-submitting demo-form behavior. It must not supply the restaurant’s page architecture or make every demo use the same hero/cards/grid/form skeleton.

## What is not premium

Never call any of the following premium:

- A shared renderer populated with different restaurant data.
- The same page skeleton with only colors, names and copy changed.
- A sidecar `premium.html` while the default `index.html` remains generic.
- A page made mostly from interchangeable gradient cards.
- A generic hero, three feature cards, four menu cards and contact form repeated across businesses.
- An unfinished local page, unpushed branch or unmerged pull request.
- A page that has not been validated.

Do not claim that a demo is finished merely because a folder or restaurant card exists.

## Visual assets

Use assets only when they are legally usable and appropriate for a sales presentation:

- Owner-provided or owner-approved restaurant photography and logos are preferred.
- Official restaurant assets may be referenced only when their use is appropriate and clearly part of an unofficial redesign presentation.
- When approved photography is unavailable, create a distinct custom illustration system rather than pretending a generic stock or gradient block is a restaurant photograph.
- Never imply that an illustration is an actual interior, dish or storefront photograph.

Production versions should replace concept illustrations with owner-approved photography and final brand assets.

## Accuracy rules

Verify these details whenever practical:

- Exact business name and active status
- Address and ZIP code
- Phone number
- Current hours
- Website and official social accounts
- Menu items described as signatures
- Founding year and ownership history
- Ordering, delivery and reservation methods
- Catering, events and multiple locations

Never invent owner names, founding dates, family histories, awards, sourcing claims, scratch-made claims, prices, live availability, current specials, reservation policies or delivery policies.

When a fact cannot be verified, use explicit confirmation language instead of guessing.

## Disclosure rules

Every demo must say that it is an unofficial presentation concept and is not affiliated with or operated by the restaurant.

Forms must:

- Never send information
- Never create a reservation or order
- Never claim the restaurant received a request
- Confirm that the interaction was only a demonstration

## Validation checklist

Before completion, confirm:

- Every requested restaurant has a real `index.html`.
- Every portfolio card links to that `index.html`.
- Names and locations are correct.
- Each bespoke demo has a distinct architecture and interaction.
- Required CSS and JavaScript files resolve correctly.
- Inline JavaScript parses successfully.
- Forms cannot transmit data.
- Disclosures are present.
- Mobile layouts are included.
- Browser rendering has been checked when the environment permits it.
- If browser rendering is blocked by the environment, report that honestly instead of claiming screenshot validation.
- All changes are committed and present on the default branch.

## Repository intent in one sentence

**Research real independent restaurants, build accurate and genuinely restaurant-specific sales demos, validate them honestly, and publish them automatically for Devin to use in person.**
