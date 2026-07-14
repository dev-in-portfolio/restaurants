# Charlotte-Area Restaurant Website Demo Portal

This repository is Devin's sales portfolio and working lead portal for Charlotte-area restaurant website rebuilds.

The goal is simple:

> Walk into an independent restaurant and say: "I already redesigned your website. Here is what it could look like."

These are **unofficial sales demos and prospecting assets**. They are not live restaurant websites, owner-approved production sites, ordering systems, reservation systems, or a consumer directory.

## Current repository state

The repo now contains three different kinds of things:

1. **The main portal** — `index.html`
   - Alphabetized restaurant tile wall.
   - A-Z quick navigation.
   - Honest status labels.
   - Queued leads from all three lead-list messages.

2. **Queued restaurant leads**
   - Restaurants with weak, outdated, broken, duplicated, confusing, missing, or underdeveloped web presences.
   - These tiles are labeled **LEAD • NOT BUILT YET**.
   - Lead tiles do **not** link to built demos until a restaurant-specific rebuild exists.

3. **Built restaurant demos**
   - Restaurant folders such as `boudreauxs/`.
   - These must be individually researched, authored, tested, published, and labeled honestly.

The portal is not just a design gallery anymore. It is the working board for the restaurant prospect list and the rebuild queue.

## Current premium reference build

**Boudreaux’s Kitchen & Tavern** is the current premium reference build.

Its rebuild is intentionally not a generic cream-background restaurant template. It is based on the restaurant’s actual NoDa identity: black corrugated storefront energy, cast-white signage, the long alligator mark, awning language, NoDa mill texture, tavern grit, string-light atmosphere, and lo-fi mural attitude.

Use Boudreaux’s as the bar for what “restaurant-specific identity” means.

Do **not** copy Boudreaux’s structure, colors, gator motif, dark-metal look, layout rhythm, or page system into another restaurant. The lesson is the level of specificity, not the visual style.

## Main SOP — publish so Devin can see it

The normal workflow is:

1. Research the restaurant.
2. Build the restaurant-specific demo.
3. Validate the site.
4. Commit the work.
5. Merge or publish to `main`.
6. Confirm the portal links to the correct route.

Do **not** leave completed work stranded on an unmerged branch when Devin needs to view it through the normal local portal.

Branches and PRs may be used while working, but the deliverable is not useful until it is visible from `main` through:

```text
http://localhost:8080/
```

A hard reset does not delete untracked local folders. If an old local route such as `boudreauxs-restaurant/` survives locally, the repo should either redirect it or the stale local folder should be cleaned up.

## Portal tile rules

Every restaurant tile must have one honest status.

### LEAD • NOT BUILT YET

Use for queued prospects only.

A lead tile means:

- The restaurant is on the prospect list.
- A specific website opportunity has been identified.
- No completed demo is available yet.
- The tile should not link to a nonexistent finished site.

### 1-PAGE • INCOMPLETE

Use only when a single authored page exists.

A one-page prototype is not a full demo, not complete, not premium, and not owner-ready.

### FULL 5-PAGE • QA PENDING

Use only when at least five separate, substantive pages exist and are published, but premium visual QA has not passed.

### PREMIUM • IDENTITY REBUILD

Use only when all five-page requirements and premium QA requirements have passed.

This label is reserved for genuinely restaurant-specific work that survives browser-rendered desktop/mobile review.

## Alphabetical portal rules

The portal must remain easy to navigate as the lead list grows.

Required behavior:

- Restaurant tiles render alphabetically.
- Sorting ignores leading **The**, **A**, and **An**.
- The portal generates A-Z quick navigation from the currently loaded restaurant list.
- Letter headings appear inside the grid.
- Duplicate names across lead sources must collapse into a single tile when possible.
- Premium or built demo tiles should win over queued lead tiles for the same restaurant.

Do not manually scatter tiles in batch order once they are on the portal.

## Lead-list source rules

The current lead inventory comes from three uploaded lead-list messages:

- Message 1 of 3 — Blocks 1-11
- Message 2 of 3 — Blocks 12-22
- Message 3 of 3 — Blocks 23-33

Each lead was collected because the restaurant has a visible website opportunity: broken pages, outdated information, duplicated domains, generic templates, raw filenames, placeholder text, stale events, weak SEO, missing standalone sites, confusing ordering paths, conflicting hours, or similar sales-relevant problems.

When adding more leads:

- Keep the lead tile clearly labeled as not built.
- Preserve the restaurant name and area.
- Avoid duplicates.
- Do not invent a demo folder before a real rebuild exists.
- Do not mark a lead as full or premium because it has a card.

## The primary deliverable

Every selected restaurant rebuild should become a complete five-page website demo.

A restaurant is not complete when it has only one long landing page, one `index.html`, a restaurant card, a folder, or five sections on the same page.

The five pages must be **five separate, substantive HTML documents** connected by working navigation.

The standard structure is:

1. **Home** — `<restaurant-slug>/index.html`
2. **Menu** — `<restaurant-slug>/menu.html`
3. **About / Story** — usually `<restaurant-slug>/about.html` or `<restaurant-slug>/story.html`
4. **Restaurant-specific conversion page** — for example `catering.html`, `events.html`, `reservations.html`, `order.html`, `private-dining.html`, `locations.html`, `taproom.html`, `brunch.html`, `gatherings.html`, or another page chosen from the business’s actual needs
5. **Visit / Contact** — usually `<restaurant-slug>/contact.html` or `<restaurant-slug>/visit.html`

The exact page names may change when the restaurant’s needs justify it, but the site must always contain **at least five real pages**. Five anchor links or five homepage sections do not count.

Each page must have a real purpose, substantial content, responsive design, correct navigation, and enough differentiation that it does not feel like filler created only to reach five files.

## Automatic workflow for connected threads

When this repository is connected and Devin sends only a restaurant list, immediately:

1. Verify each restaurant is open and identify the correct location.
2. Research Google Business information, the official website, official social accounts, current menus, ordering/reservation services and recent reliable local coverage.
3. Identify the restaurant’s actual digital weaknesses, strongest sales opportunity and best five-page information architecture.
4. Build the restaurant-specific five-page demo.
5. Connect all pages with working desktop and mobile navigation.
6. Validate every page, link, interaction and disclosure.
7. Complete the premium-evidence review before using premium language.
8. Add or update the portfolio card only after the pages and status support it.
9. Commit and push the completed work.
10. Ensure the changes are visible on `main` before reporting completion.

Do not ask Devin to repeat the project, choose a template, approve a plan, request a commit, request a push or remember to merge.

Publishing is automatic unless GitHub permissions technically prevent it. If permissions block completion, report the exact blocker.

## Completion vocabulary — use these terms exactly

To prevent ambiguous status reports:

- **Queued lead** means a restaurant appears in the portal as a prospect but no demo has been built.
- **Single-page prototype** means one authored page. It is incomplete and must never be called a full demo, premium demo, finished site or completed restaurant.
- **Partial five-page demo** means two to four substantive pages exist. It is incomplete.
- **Full five-page demo** means at least five separate substantive pages exist, are linked together, validated and published on `main`.
- **Premium five-page demo** means a full five-page demo that also passes every anti-faux-premium quality gate and browser-rendered visual QA requirement below.
- **Production-ready website** means owner-approved branding, photography, menus, policies and real integrations are connected. A premium five-page sales demo is not automatically production-ready.

Never use the word **built**, **done**, **finished**, **complete**, **full**, **premium** or **bespoke** without making clear whether the result is a queued lead, single-page prototype, full five-page demo, premium five-page demo or production-ready website.

When reporting completion, state the exact count and status:

```text
Restaurant Name — 5/5 pages built and published to main; full five-page demo; premium QA pending
```

Only after every premium gate passes may the report say:

```text
Restaurant Name — 5/5 pages built, published to main and visually QA-tested; premium five-page demo
```

If fewer than five pages exist, report the actual count and say it is incomplete:

```text
Restaurant Name — 1/5 pages built; incomplete single-page prototype
```

## Non-negotiable definition of a full five-page demo

A restaurant may be labeled **FULL** or **COMPLETE** only when all of the following are true:

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
- The customer journey is based on that restaurant’s actual needs.
- The copy is based on verified facts or clearly labeled proposed functionality.
- Forms are visibly demonstrations and never submit data.
- All five pages work responsively on mobile and desktop.
- All HTML, CSS, JavaScript, links and navigation have been validated.
- All files are committed and present on `main`.

A shared stylesheet may provide resets, accessibility utilities, typography loading, consistent site navigation and non-submitting demo-form behavior. It must not supply the restaurant’s page architecture, visual identity or make every demo use the same hero/cards/grid/form skeleton.

## Anti-faux-premium rule — hard stop

**A site is not premium merely because it is dark, animated, colorful, custom-coded, labeled bespoke, or split into five files.**

The word **PREMIUM** is reserved for work that visibly and functionally exceeds an ordinary template. A full five-page demo that fails any requirement in this section must be called:

```text
Full five-page demo — premium QA pending
```

It must not be called premium, bespoke premium, polished, finished premium, owner-ready or presentation-ready.

### 1. No dressed-up shared shell

A premium site must not be the same underlying composition repeated with new colors, restaurant names and copy.

The following are prohibited:

- Reusing the same hero proportions, card grid, section order, conversion block and footer composition across restaurants.
- Reusing the same five page layouts with only wording and colors changed.
- Repeating a generic pattern such as hero → three cards → menu cards → form on most pages.
- Using a data object or shared renderer to generate restaurant pages.
- Calling inline restaurant-specific CSS “bespoke” when the actual DOM structure remains substantially identical.
- Hiding template reuse behind renamed classes.

Shared navigation, accessibility helpers, resets and form-safety code are allowed. The restaurant’s **information architecture, page compositions, visual rhythm and conversion journey must be individually designed**.

### 2. Five real pages, not one design copied five times

Each of the five pages must have its own page-level purpose and composition.

Premium fails when:

- The menu, about, conversion and contact pages are shortened copies of the homepage.
- Interior pages use identical hero and card structures with only headings changed.
- Pages exist mostly to satisfy the file count.
- Content is thin, generic or interchangeable with another restaurant.
- Navigation links exist but the pages do not provide substantial new value.

### 3. Restaurant-specific content depth

The site must demonstrate meaningful research, not restaurant-themed filler.

Across the five pages, premium work must include verified or clearly qualified details such as:

- Correct business identity and location information.
- Real cuisine, service model and customer use cases.
- Verified menu categories or clearly labeled representative menu direction.
- The restaurant’s genuine story, atmosphere or neighborhood role.
- Its actual conversion needs: ordering, catering, events, private dining, reservations, taproom visits, multiple locations or another relevant path.
- Specific weaknesses in the existing digital experience that the redesign resolves.

Generic phrases such as “fresh ingredients,” “unforgettable experience,” “something for everyone,” “where flavor meets community” or interchangeable hospitality copy do not establish premium quality.

### 4. Meaningful interactions, not decorative buttons

A premium five-page demo must include **at least two functional restaurant-specific interactions across the site**, including at least one conversion-oriented interaction.

Examples include:

- Searchable or filterable menu.
- Catering estimator.
- Group-order builder.
- Reservation or private-event planner.
- Location selector with location-specific content.
- Beer, wine or pairing finder.
- Meal-time, heat-level or dietary menu selector.
- Event calendar controls.
- Curb-service or pickup decision guide.

Anchor scrolling, hover effects, carousels, decorative tabs that reveal minimal copy, fake success messages and generic contact forms do not count by themselves.

### 5. Premium visual evidence

A premium site must have a deliberate visual-asset strategy across all five pages.

Preferred evidence:

- Owner-provided or owner-approved photography and logos.
- Legally usable official brand assets appropriate for an unofficial sales presentation.
- Purpose-built original illustrations, diagrams, menu graphics or identity elements when approved photography is unavailable.

Premium fails when the visual system is mostly:

- Generic gradients.
- Radial-gradient “food plates.”
- Large translucent words used as fake imagery.
- Recolored circles, rectangles or interchangeable abstract blocks.
- Emoji used as primary restaurant art.
- The same illustration treatment repeated across unrelated restaurants.
- Stock imagery that does not depict the restaurant and is presented as though it does.

Custom illustrations may be used, but they must be **purpose-built, varied, restaurant-specific and clearly illustrations**. They cannot serve as a low-effort substitute for a complete visual design.

### 6. Premium polish across the whole site

Premium quality must remain consistent beyond the homepage.

All five pages must show:

- Intentional typography and spacing.
- Clear hierarchy and readable content.
- Consistent but non-repetitive art direction.
- Designed desktop and mobile states.
- Useful empty, disabled and demonstration states where applicable.
- Consistent navigation and calls to action.
- No raw filenames, placeholder text, broken assets, horizontal overflow, clipped content or accidental browser defaults.
- No page that looks unfinished compared with the homepage.

### 7. Browser-rendered visual QA is mandatory for the premium label

Code inspection alone cannot establish premium quality.

Before using **PREMIUM** or **BESPOKE PREMIUM**, every page must be browser-rendered and checked at minimum in:

- A desktop viewport.
- A mobile viewport.

The review must check:

- Layout integrity.
- Navigation behavior.
- Legibility and contrast.
- Overflow and clipping.
- Asset loading.
- Interaction behavior.
- Page-to-page visual consistency.
- Whether the result actually looks premium rather than merely containing premium-sounding code.

If browser rendering or screenshots are blocked by the environment, report:

```text
5/5 pages built and code-validated; browser visual QA blocked; not yet eligible for PREMIUM label
```

**Never infer visual polish from HTML and CSS alone. Never label a site premium when browser-rendered QA was not completed.**

### 8. Honest asset and integration status

A premium sales demo may use demonstration forms and proposed integrations, but it must distinguish them clearly.

Do not claim:

- Real ordering when the button is a demo.
- Real reservations when no reservation provider is connected.
- Live menu availability when it is static.
- Current event data when it is representative.
- Owner-approved photography or branding when approval has not occurred.
- Production readiness when key assets or integrations are pending.

Missing owner assets do not automatically block a premium sales demo, but the replacement visual system must still pass the premium visual-evidence standard above.

## Premium evidence report

Before marking any restaurant premium, record and report this evidence:

- `Pages: 5/5 substantive pages`
- `Navigation: desktop passed / mobile passed`
- `Distinct page compositions: 5/5`
- `Restaurant-specific interactions: [exact count and names]`
- `Visual assets: owner-approved / legally usable official / original illustration system`
- `Desktop browser QA: passed`
- `Mobile browser QA: passed`
- `Broken links/assets: 0`
- `Forms: demonstration-only and non-submitting`
- `Default branch: main confirmed`
- `Final status: PREMIUM` or `premium QA pending`

A vague statement such as “custom,” “high-end,” “fully authored,” “restaurant-specific,” or “premium-styled” is not evidence.

## What does not count as a full or premium demo

Never call any of the following full, complete, premium or finished:

- One long scrolling page, regardless of how polished it looks.
- Five sections or five anchor links on one page.
- One `index.html` plus empty, duplicate or placeholder pages.
- A shared renderer populated with different restaurant data.
- The same page skeleton with only colors, names and copy changed.
- A sidecar `premium.html` while the default site remains generic.
- A page made mostly from interchangeable gradient cards.
- A generic hero, feature cards, menu cards and contact form repeated across businesses.
- Five files generated from the same structure with headings changed.
- A restaurant folder or portfolio card without all five pages.
- An unfinished local site, unpushed branch or unmerged pull request.
- A site that has not been validated.
- A site that has not passed browser-rendered desktop and mobile QA.
- A site whose interior pages are visibly weaker or thinner than its homepage.
- A site that uses labels, commit messages or README wording as a substitute for evidence.

Do not claim that a restaurant is finished merely because its homepage, folder or portfolio card exists.

## Five-page quality rules

Every page must add meaningful value.

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

- Exact business name and active status.
- Address and ZIP code.
- Phone number.
- Current hours.
- Website and official social accounts.
- Menu items described as signatures.
- Founding year and ownership history.
- Ordering, delivery and reservation methods.
- Catering, events and multiple locations.

Never invent owner names, founding dates, family histories, awards, sourcing claims, scratch-made claims, prices, live availability, current specials, reservation policies or delivery policies.

When a fact cannot be verified, use explicit confirmation language instead of guessing.

## Disclosure rules

Every page of every demo must say that it is an unofficial presentation concept and is not affiliated with or operated by the restaurant.

Forms must:

- Never send information.
- Never create a reservation or order.
- Never claim the restaurant received a request.
- Confirm that the interaction was only a demonstration.

## Full-demo validation checklist

Before reporting a restaurant as a full five-page demo, confirm:

- The restaurant folder contains at least five substantive HTML pages.
- `index.html`, a menu page, an about/story page, a restaurant-specific conversion page and a visit/contact page exist.
- All five pages open successfully.
- Every page links to the other core pages through working navigation.
- Desktop and mobile navigation work.
- Every portfolio card links to the restaurant’s `index.html`.
- Names and locations are correct.
- The site has a distinct architecture and restaurant-specific customer journey.
- Required CSS and JavaScript files resolve correctly.
- Inline JavaScript parses successfully.
- Internal links do not point to missing pages or IDs.
- Forms cannot transmit data.
- Disclosures are present on all five pages.
- Mobile layouts are included on all five pages.
- All changes are committed and present on `main`.

A restaurant that fails any required five-page check must be reported as incomplete.

## Premium validation checklist

Before applying a premium label, also confirm:

- Every anti-faux-premium rule has been reviewed explicitly.
- The five page compositions are meaningfully distinct.
- The site does not substantially duplicate another restaurant’s DOM structure or visual system.
- At least two meaningful restaurant-specific interactions work.
- The asset strategy passes the premium visual-evidence standard.
- Every page has comparable visual polish and content depth.
- Desktop browser-rendered QA passed for all five pages.
- Mobile browser-rendered QA passed for all five pages.
- Broken links and broken assets equal zero.
- The premium evidence report has been completed.

A full five-page demo that fails any premium check remains a **full five-page demo — premium QA pending**.

## Repository intent in one sentence

**Find real restaurant website opportunities, keep every lead visible in the portal, build accurate five-page restaurant-specific sales demos, prove premium quality through evidence and browser-rendered QA, label every status honestly, and publish completed work to `main` so Devin can use it in person.**
