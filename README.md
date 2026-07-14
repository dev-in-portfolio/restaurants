# Charlotte-Area Restaurant Website Demo Factory

This repository is a sales portfolio of custom, unofficial restaurant website redesign demos.

The goal is for Devin to walk into an independent restaurant and say:

> “I already redesigned your website. Here is what it could look like.”

These are presentation demos—not live restaurant websites, ordering systems, reservation systems, or a consumer directory.

## The primary deliverable

**Every restaurant receives a complete five-page website demo.**

A restaurant is not complete when it has only one long landing page, one `index.html`, a restaurant card, a folder, or five sections on the same page.

The five pages must be **five separate, substantive HTML documents** connected by working navigation.

The standard structure is:

1. **Home** — `<restaurant-slug>/index.html`
2. **Menu** — `<restaurant-slug>/menu.html`
3. **About / Story** — `<restaurant-slug>/about.html`
4. **Restaurant-specific conversion page** — for example `catering.html`, `events.html`, `reservations.html`, `order.html`, `private-dining.html`, `locations.html`, `taproom.html`, or another page chosen from the business’s actual needs
5. **Visit / Contact** — `<restaurant-slug>/contact.html`

The exact page names may change when the restaurant’s needs justify it, but the site must always contain **at least five real pages**. Five anchor links or five homepage sections do not count.

Each page must have a real purpose, substantial content, responsive design, correct navigation, and enough differentiation that it does not feel like filler created only to reach five files.

## Automatic workflow for connected threads

When this repository is connected and the user sends only a restaurant list, immediately:

1. Verify each restaurant is open and identify the correct location.
2. Research Google Business information, the official website, official social accounts, current menus, ordering/reservation services and recent reliable local coverage.
3. Identify the restaurant’s actual digital weaknesses, strongest sales opportunity and best five-page information architecture.
4. Build all five pages for every restaurant.
5. Connect all pages with working desktop and mobile navigation.
6. Validate every page, link, interaction and disclosure.
7. Add or update the portfolio card only after all five pages exist.
8. Commit and push every completed five-page demo.
9. Ensure the changes are on the default branch before reporting completion.

Do not ask the user to repeat the project, choose a template, approve a plan, request a commit, request a push or remember to merge.

Publishing is automatic unless GitHub permissions technically prevent it. If permissions block completion, report the exact blocker.

## Completion vocabulary — use these terms exactly

To prevent ambiguous status reports:

- **Single-page prototype** means one authored page. It is incomplete and must never be called a full demo, premium demo, finished site or completed restaurant.
- **Partial five-page demo** means two to four substantive pages exist. It is incomplete.
- **Full five-page demo** means at least five separate substantive pages exist, are linked together, validated and published on the default branch.
- **Production-ready website** means owner-approved branding, photography, menus, policies and real integrations are connected. A full five-page sales demo is not automatically production-ready.

Never use the word **built**, **done**, **finished**, **complete**, **full**, **premium** or **bespoke** without making clear whether the result is a single-page prototype, a full five-page demo or a production-ready website.

When reporting completion, state the exact count:

> `Restaurant Name — 5/5 pages built and published`

If fewer than five pages exist, report the actual count and say it is incomplete:

> `Restaurant Name — 1/5 pages built; incomplete`

## Non-negotiable definition of a full bespoke premium demo

A restaurant may be labeled **FULL**, **BESPOKE**, **PREMIUM** or **COMPLETE** only when all of the following are true:

- At least five separate substantive HTML pages exist for that restaurant.
- The restaurant’s default page is `<restaurant-slug>/index.html`.
- A dedicated menu page exists.
- A dedicated story/about page exists.
- A dedicated restaurant-specific conversion page exists.
- A dedicated visit/contact page exists.
- Every page is reachable through working site navigation.
- Navigation works on desktop and mobile.
- The pages are individually authored for that restaurant.
- The site has a restaurant-specific information architecture and page order.
- The site has a distinct visual identity appropriate to that business.
- The site includes at least one meaningful restaurant-specific interaction, such as a menu finder, event planner, catering estimator, meal switcher, heat ladder, pairing tool, curb-service guide or group-order builder.
- The customer journey is based on that restaurant’s actual needs.
- The copy is based on verified facts or clearly labeled proposed functionality.
- Forms are visibly demonstrations and never submit data.
- All five pages work responsively on mobile and desktop.
- All HTML, CSS, JavaScript, links and navigation have been validated.
- All files are committed and present on the default branch.

A shared stylesheet may provide resets, accessibility utilities, typography loading and non-submitting demo-form behavior. It must not supply the restaurant’s page architecture or make every demo use the same hero/cards/grid/form skeleton.

## What does not count as a full demo

Never call any of the following full, complete, premium or finished:

- One long scrolling page, regardless of how polished it looks.
- Five sections or five anchor links on one page.
- One `index.html` plus empty, duplicate or placeholder pages.
- A shared renderer populated with different restaurant data.
- The same page skeleton with only colors, names and copy changed.
- A sidecar `premium.html` while the default site remains generic.
- A page made mostly from interchangeable gradient cards.
- A generic hero, feature cards, menu cards and contact form repeated across businesses.
- A restaurant folder or portfolio card without all five pages.
- An unfinished local site, unpushed branch or unmerged pull request.
- A site that has not been validated.

Do not claim that a restaurant is finished merely because its homepage, folder or portfolio card exists.

## Five-page quality rules

Every page must add meaningful value:

### Home

- Establish the restaurant’s identity and strongest reason to visit.
- Provide clear paths to menu, ordering/reservations, the restaurant story and visit information.
- Do not duplicate the full content of every interior page.

### Menu

- Use a readable HTML menu architecture rather than relying only on an embedded PDF or image.
- Organize dishes around the restaurant’s actual customer decisions.
- Clearly label representative content when current prices or full menu data cannot be verified.

### About / Story

- Use only verified history, ownership and brand facts.
- Do not invent family stories, founding dates, awards or sourcing claims.
- Explain what makes this restaurant locally distinct.

### Restaurant-specific conversion page

- Choose the highest-value need for that business: catering, events, reservations, private dining, ordering, locations, taproom calendar, group dining or another verified need.
- Include a restaurant-specific interaction or decision tool where useful.
- Never fake a completed order, reservation or inquiry.

### Visit / Contact

- Prioritize current address, phone, hours, directions, parking and accessibility where verified.
- Clearly distinguish multiple locations.
- Any form must be a non-submitting demonstration.

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

Every page of every demo must say that it is an unofficial presentation concept and is not affiliated with or operated by the restaurant.

Forms must:

- Never send information
- Never create a reservation or order
- Never claim the restaurant received a request
- Confirm that the interaction was only a demonstration

## Validation checklist

Before reporting a restaurant complete, confirm:

- The restaurant folder contains at least five substantive HTML pages.
- `index.html`, a menu page, an about/story page, a restaurant-specific conversion page and a visit/contact page exist.
- All five pages open successfully.
- Every page links to the other core pages through working navigation.
- Desktop and mobile navigation work.
- Every portfolio card links to the restaurant’s `index.html`.
- Names and locations are correct.
- The site has a distinct architecture and restaurant-specific interaction.
- Required CSS and JavaScript files resolve correctly.
- Inline JavaScript parses successfully.
- Internal links do not point to missing pages or IDs.
- Forms cannot transmit data.
- Disclosures are present on all five pages.
- Mobile layouts are included on all five pages.
- Browser rendering has been checked when the environment permits it.
- If browser rendering is blocked by the environment, report that honestly instead of claiming screenshot validation.
- All changes are committed and present on the default branch.

A restaurant that fails any required five-page check must be reported as incomplete.

## Portfolio-card rule

Do not mark a portfolio card **BESPOKE**, **PREMIUM**, **FULL** or **COMPLETE** until all five pages have passed validation and are published on the default branch.

Single-page prototypes may appear only when clearly labeled **1-PAGE PROTOTYPE — INCOMPLETE**.

## Repository intent in one sentence

**Research real independent restaurants, build accurate five-page restaurant-specific sales demos, validate every page honestly, and publish them automatically for Devin to use in person.**