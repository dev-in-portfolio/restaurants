# DSC Premium Demo Add-On Boundary

This file is mandatory reading before building any restaurant demo in `dev-in-portfolio/restaurants`.

Also read `BUILD_QUALITY_GATE.md` in full. The two files work together:

- `ADD_ON_BOUNDARY.md` protects separately sellable DSC scope;
- `BUILD_QUALITY_GATE.md` protects visual quality, factual provenance, flexible page architecture, and proof-based QA.

If older repository wording still describes a fixed six-page quota or allows self-certified QA, `BUILD_QUALITY_GATE.md` controls the build-quality decision.

## Purpose

The demo is a **sales demonstration for the core website**, not a free implementation of every feature Dark Star Consulting can sell after the restaurant says yes.

A demo must look premium because of **art direction, layout, typography, responsive execution, factual clarity, and overall UX quality**. It must not become premium by giving away separately sellable DSC add-on functionality.

The working rule is:

> **Premium core demo, preserved upsell surface.**
>
> Show the restaurant how much better the core site can feel. Leave the separately sellable enhancement packs available for the sales conversation and production scope.

## Current DSC add-on catalog — reserved from automatic demos

The following current add-ons are separate products and must **not be fully implemented in an automatic prospect demo unless the user explicitly orders that specific add-on to be demonstrated**:

### P1

- Brand Finish Pack
- Menu Experience Pack
- Photo Story Pack
- Local Discovery Pack
- Trust & Reputation Pack

### P2

- Order & Reserve Pack
- Catering & Private Events Pack
- Guest Engagement Pack
- Menu Collections Pack

### P3

- Signature Interactive Experience
- Digital Menu Concierge
- Multi-Location Growth Pack

## Critical interpretation rule

The restaurant audit may describe missed opportunities or recommend features that overlap the packs above. **Those audit recommendations are not an instruction to build every recommended feature into the sales demo.**

Use the audit to identify the business problem and sales angle. Demonstrate that the core site can solve the underlying presentation/trust/customer-journey problem, while preserving separately sellable enhancements for the proposal.

Examples:

- If the audit says catering is weak, present verified catering availability and a strong static CTA. Do **not** invent catering packages, tray sizes, guest counts, capacities, planners, quote tools, forms, or lead workflows.
- If ordering/reservations are fragmented, make the core site clearly route guests to verified existing services. Do **not** build a new ordering/reservation system or advanced decision flow.
- If the menu is hard to use, create a clean, readable, responsive menu page. Do **not** automatically add menu search, dietary filtering, pairing logic, guided recommendations, or a concierge.
- If the restaurant has multiple locations, present verified locations clearly. Do **not** automatically build the enhanced multi-location experience sold separately.
- If the restaurant needs better guest engagement, use strong calls to action and clear content. Do **not** add loyalty, rewards, newsletter/SMS capture, customer accounts, forms, automated campaigns, or similar engagement machinery.

## Commercial-scope rule

Judge the add-on boundary by **what business capability is being delivered**, not by whether the code is technically simple.

A feature does not become core merely because it is easy to code.

Examples:

- a non-submitting catering inquiry form is still the beginning of a catering/lead workflow;
- a simple preference quiz is still guided menu functionality;
- a lightweight loyalty card is still guest engagement;
- a simple location switcher may still be part of Multi-Location Growth if it creates the paid multi-location experience.

For automatic demos, preserve the sellable capability even when a simplified implementation would be easy.

## What the baseline premium demo MAY include

These are normal core-demo elements when appropriate and factually supported:

- bespoke restaurant-specific art direction;
- premium typography, spacing, composition, responsive behavior, and motion polish;
- **five or more substantive linked pages, with a sixth page only when verified material supports a genuinely different job**;
- accurate verified restaurant copy and story content;
- general cultural/editorial context when clearly framed as general rather than as an unsupported restaurant-specific claim;
- a clean readable menu organized into normal sections;
- standard navigation, mobile navigation, accordions, disclosure panels, simple galleries, and other ordinary presentation UI;
- verified address, hours, phone, service notes, and location information;
- clear buttons linking to the restaurant's existing verified ordering or reservation provider;
- a static catering/private-events overview **only when that service is verified**;
- a static drinks, brunch, bakery, taproom, coffee, neighborhood, or other restaurant-specific editorial page when current evidence supports it;
- normal accessibility behavior, keyboard support, focus states, responsive design, and reduced-motion handling;
- standard page metadata needed for a competent static concept, without turning the demo into a separately scoped Local Discovery implementation;
- concept-safe CTAs that route to verified current public paths.

The baseline may **visually preview the value** of an area that could later be upgraded. It should not contain the full pack implementation.

## What the automatic demo MUST reserve for the sales upsell

Unless the user explicitly orders otherwise, do not build:

- custom calculators, planners, builders, configurators, recommendation engines, quizzes, or guided decision tools;
- mezcal/beer/wine/coffee flight builders or similar signature interactive experiences;
- digital menu concierge behavior;
- menu search, advanced filtering, dietary recommendation logic, pairing engines, or personalized menu results;
- custom ordering flows, reservation logic, waitlist systems, booking engines, or payment functionality;
- advanced catering/private-event package builders, quote calculators, event planners, lead workflows, or booking tools;
- **automatic-demo forms of any kind**, including non-submitting catering, inquiry, contact, newsletter, reservation, or lead-capture forms;
- loyalty/rewards systems, customer accounts, points, memberships, or wallets;
- newsletter/SMS capture systems, marketing automation, drip campaigns, CRM-style capture, or automated follow-up;
- review/reputation feeds, review-request automation, reputation dashboards, or other Trust & Reputation pack machinery;
- advanced photo-story galleries or editorial photo experiences intended to represent the Photo Story add-on;
- advanced local-discovery/SEO systems intended to represent the Local Discovery add-on;
- advanced menu collection experiences intended to represent the Menu Collections add-on;
- enhanced multi-location selectors, location-aware experiences, cross-location comparison, or other Multi-Location Growth functionality;
- any other feature whose primary value is a separately sellable DSC enhancement rather than the core website presentation.

## No invented service inventory

If a restaurant publicly verifies catering, private dining, events, wholesale, custom cakes, or another revenue service, the demo may present that service.

It may not invent the service's commercial details.

Do not fabricate:

- package names;
- tray sizes;
- serving counts;
- guest capacities;
- minimum orders;
- lead times;
- delivery zones;
- package contents;
- booking rules;
- event availability.

Use only current verified details. Otherwise keep the page high-level and route to the current public contact path.

## Simple interaction ceiling

A demo does **not** need custom interactions to qualify as premium.

Ordinary website interactions are allowed when useful: mobile navigation, accordions, tabs used for ordinary content presentation, a simple image gallery, subtle animation, and straightforward links/buttons.

Do not invent a custom interactive feature merely to prove that the site is premium.

If an interaction starts to feel like a feature the restaurant could reasonably pay extra for, **stop and preserve it as an upsell**.

## Evidence requirement

Every new `evidence.md` must contain:

- `## Creative Brief` — verified restaurant-specific anchors and three core design moves;
- `## Claim Ledger` — meaningful restaurant-specific claims mapped to source URLs;
- `## Add-On Preservation` — relevant DSC add-on opportunities, what was intentionally not implemented, and what remains sellable.

The claim ledger prevents general cuisine knowledge from being rewritten as unsupported facts about the restaurant.

## QA requirement

Before a demo can receive `qa` or `premium`, run:

```bash
node scripts/validate-demo.mjs <restaurant-slug>
```

The generated `qa-report.json` is the objective implementation gate. A failing validator means the build is not `qa` and not `premium`.

Browser QA is still required for `premium` as defined in `BUILD_QUALITY_GATE.md`.

A polished `evidence.md` does not override failed machine checks, unsupported facts, generic-template design, or missing browser verification.
