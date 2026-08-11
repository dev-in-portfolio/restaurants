# DSC Premium Demo Add-On Boundary

This file is mandatory reading before building any restaurant demo in `dev-in-portfolio/restaurants`.

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

For example:

- If the audit says catering is weak, build an excellent static catering/private-events page with clear verified information and a normal CTA. Do **not** build a party planner, quote calculator, package configurator, lead workflow, or advanced inquiry funnel.
- If ordering/reservations are fragmented, make the core site clearly route guests to the verified existing services. Do **not** build a new ordering/reservation system or advanced decision flow.
- If the menu is hard to use, create a clean, readable, responsive menu page. Do **not** automatically add menu search, dietary filtering, pairing logic, guided recommendations, or a concierge.
- If the restaurant has multiple locations, present verified locations clearly. Do **not** automatically build the enhanced multi-location experience sold separately.
- If the restaurant needs better guest engagement, use strong calls to action and clear content. Do **not** add loyalty, rewards, newsletter/SMS capture, customer accounts, automated campaigns, or similar engagement machinery.

## What the baseline premium demo MAY include

These are normal core-demo elements when appropriate:

- bespoke restaurant-specific art direction;
- premium typography, spacing, layout, responsive composition, and motion polish;
- six substantive linked pages required by the repository README;
- accurate verified restaurant copy and story content;
- a clean readable menu organized into normal sections;
- standard navigation, mobile navigation, accordions, disclosure panels, simple galleries, and other ordinary presentation UI;
- verified address, hours, phone, service notes, and location cards;
- clear buttons linking to the restaurant's existing verified ordering or reservation provider;
- a static catering/private-events overview when that page is appropriate;
- a static drinks, brunch, bakery, taproom, coffee, neighborhood, or other restaurant-specific experience page;
- normal accessibility behavior, keyboard support, focus states, responsive design, and reduced-motion handling;
- standard SEO/page metadata needed for a competent static concept, without turning the demo into a separately scoped Local Discovery implementation;
- concept-safe CTAs that do not pretend a real transaction or submission occurred.

The baseline may **visually preview the value** of an area that could later be upgraded. It should not contain the full pack implementation.

## What the automatic demo MUST reserve for the sales upsell

Unless the user explicitly orders otherwise, do not build:

- custom calculators, planners, builders, configurators, recommendation engines, quizzes, or guided decision tools;
- mezcal/beer/wine/coffee flight builders or similar signature interactive experiences;
- digital menu concierge behavior;
- menu search, advanced filtering, dietary recommendation logic, pairing engines, or personalized menu results;
- custom ordering flows, reservation logic, waitlist systems, booking engines, or payment functionality;
- advanced catering/private-event package builders, quote calculators, event planners, lead workflows, or booking tools;
- loyalty/rewards systems, customer accounts, points, memberships, or wallets;
- newsletter/SMS capture systems, marketing automation, drip campaigns, CRM-style capture, or automated follow-up;
- review/reputation feeds, review-request automation, reputation dashboards, or other Trust & Reputation pack machinery;
- advanced photo-story galleries or editorial photo experiences intended to represent the Photo Story add-on;
- advanced local-discovery/SEO systems intended to represent the Local Discovery add-on;
- advanced menu collection experiences intended to represent the Menu Collections add-on;
- enhanced multi-location selectors, location-aware experiences, cross-location comparison, or other Multi-Location Growth functionality;
- any other feature whose primary value is a separately sellable DSC enhancement rather than the core website presentation.

## Simple interaction ceiling

A demo does **not** need two custom interactions to qualify as premium.

Ordinary website interactions are allowed and encouraged when useful: mobile navigation, accordions, tabs used for ordinary content presentation, a simple image gallery, subtle animation, and straightforward links/buttons.

Do not invent a custom interactive feature merely to prove that the site is premium.

If an interaction starts to feel like a feature the restaurant could reasonably pay extra for, **stop and preserve it as an upsell**.

## Conversion-page rule

The required revenue/conversion page still exists, but it should normally demonstrate **presentation and opportunity**, not deliver a full add-on.

Examples:

- Catering page: packages/categories or service overview + contact/official CTA, not a custom catering planner.
- Private dining page: room/event overview + verified capacity/details when available + contact/official CTA, not an event configurator.
- Reservations page: service explanation + link to verified provider, not a custom booking system.
- Ordering page: clear path to the verified provider, not a custom ordering engine.
- Groups/events page: persuasive static page + safe CTA, not an automated lead funnel.

## Evidence requirement

Every new `evidence.md` must contain an **Add-On Preservation** section that records:

1. which DSC add-on opportunities are relevant to this restaurant;
2. which of those opportunities were intentionally **not** implemented in the demo;
3. any baseline element that merely previews an area that could later receive a paid add-on;
4. confirmation that no separately sellable add-on was accidentally bundled into the demo.

This gives the salesperson a ready-made upsell map after the prospect reacts to the core concept.

## QA requirement

Before a demo can be marked `premium`, QA must explicitly check both:

- **Core quality:** the six-page concept is polished, accurate, responsive, accessible, and presentation-ready.
- **Add-on preservation:** the demo has not accidentally implemented separately sellable DSC add-on functionality.

A beautiful demo that gives away the add-on catalog is **not** complete under this repository's sales strategy.
