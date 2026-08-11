# Premium Core Build Quality Gate

This file is mandatory reading for every automatic restaurant demo build in `dev-in-portfolio/restaurants`.

It exists to prevent two opposite failures:

1. **feature overbuild** — a demo gives away separately sellable DSC add-ons;
2. **creative underbuild** — a demo technically checks boxes but looks like a generic restaurant template.

The target is:

> **High-end core website. Low add-on leakage. Verified facts. Proof-based QA.**

If this file conflicts with older fixed-page-count or self-reported QA wording elsewhere in the repository, **this file controls the build-quality decision**.

## 1. Page architecture is evidence-led, not quota-led

Do not invent content to satisfy a page count.

A premium-core automatic demo must contain **at least five substantive linked HTML pages**. Six is preferred only when current verified material genuinely supports a sixth distinct page.

Core coverage normally includes:

- `index.html` — homepage;
- `menu.html` — readable verified menu presentation;
- `visit.html` or `contact.html` — practical verified information and current CTA path;
- one identity/story/concept page supported by actual restaurant-specific evidence;
- one restaurant-specific editorial or conversion page supported by an actually verified service, program, product category, or customer need.

A sixth page should exist only when it has a genuinely different job and enough verified material to justify it.

### Never create filler pages

Do not create a page merely because the old six-page pattern expects one.

If owner/founder/history material cannot be verified, do **not** manufacture an `Our Story` narrative. Use a better-supported concept/editorial page or omit that page slot.

If catering/private dining/events are not verified, do **not** create invented packages or a fictional conversion page.

General cuisine or cultural information may be used editorially when appropriate, but it must be framed as **general context**, not as an unsupported claim about how this restaurant operates.

## 2. Restaurant-specific factual claims require provenance

`evidence.md` must contain a `## Claim Ledger` section.

For every meaningful restaurant-specific claim used in the demo beyond basic identity/contact information, record:

- the claim;
- the page where it appears;
- the source URL that supports it.

Examples that require direct restaurant-specific support include:

- founded in / founded to / family-owned / chef-led claims;
- “made from scratch,” “house-made,” “hand-patted,” “imported,” “local,” “organic,” “daily,” or similar preparation/sourcing claims;
- named catering packages, package quantities, guest counts, capacities, minimums, delivery zones, or event details;
- named awards, press, signature-item claims, “most popular,” “chef recommended,” or other ranking claims;
- service claims such as breakfast all day, late night, private dining, catering, reservations, parking, accessibility, live music, or recurring events;
- exact operational promises beyond what the current source directly supports.

General food knowledge is **not** a source for restaurant-specific operating claims.

If a claim cannot be sourced, remove or rewrite it before QA.

## 3. No invented conversion inventory

A conversion page may present a **verified** service beautifully, but it may not invent the inventory of that service.

For example, a catering page may say that catering is available when an official source supports that fact and may route the visitor to the current contact/order path.

It may **not** invent:

- package names;
- tray sizes;
- number of servings;
- guest-count ranges;
- package contents;
- event capacities;
- minimum spends;
- lead times;
- delivery boundaries;
- booking rules.

Those details are either verified facts or future client-approved production content.

## 4. Automatic demos do not include forms

For automatic prospect demos, **do not include inquiry, catering, reservation, newsletter, contact, or lead-capture forms**, even when they are non-submitting demo forms.

Use a clear CTA to a verified existing phone number, email address, ordering provider, reservation provider, or other current public path.

A form is part of a commercial workflow and should remain available for the appropriate DSC add-on or production scope unless the user explicitly asks to demonstrate one.

## 5. Premium must be visible in the core design

Premium is not a file count and not a feature count.

Before coding, add a `## Creative Brief` section to `evidence.md` containing:

### Verified visual/content anchors

List at least three restaurant-specific anchors derived from current evidence. Examples include the actual service model, physical setting, menu emphasis, neighborhood context, real visual cues from the current public presence, verified history, or verified product focus.

### Three core design moves

State three concrete visual/compositional choices that make this site specific to this restaurant **without using paid add-on functionality**.

Examples:

- unusual editorial composition;
- custom typographic treatment;
- a restaurant-specific grid or rhythm;
- an original decorative motif;
- menu composition that reflects the restaurant's actual service model;
- deliberate use of negative space, scale, layering, framing, or image treatment;
- a navigation or page-flow concept tied to how guests actually use this restaurant.

These are design moves, not app features.

## 6. Anti-template gate

A build fails the premium-core gate if most of the site could be reused unchanged for another restaurant by swapping the name, cuisine, palette, and photos.

Do not let the entire site reduce to:

> dark-overlay hero → centered headline → pill buttons → three generic cards → alternating two-column sections → generic footer

That pattern may appear in part, but it cannot be the entire design language.

At least two substantive pages must use meaningfully different composition families rather than repeating the same card/grid shell.

Avoid defaulting to common AI restaurant shorthand such as a Playfair-style serif plus earth-tone palette merely because the cuisine is traditional or Latin. Typography and color must come from the chosen art direction, not a generic cuisine stereotype.

### Swap test

Before QA, ask:

> If I replaced the restaurant name, food nouns, colors, and images, would this still look like the same site for another restaurant?

If yes, the build is not premium yet. Redesign the core presentation before moving to QA.

## 7. Machine validation is mandatory

Before a build may receive `qa` or `premium`, run:

```bash
node scripts/validate-demo.mjs <restaurant-slug>
```

This validator checks objective failures including:

- minimum substantive page count;
- required core files;
- CSS brace/syntax-balance failures;
- JavaScript parse errors;
- broken local links and assets;
- broken fragment/deep links;
- duplicate IDs;
- missing image alt attributes;
- placeholder/test residue;
- automatic-demo forms;
- missing home-return links;
- missing required evidence sections.

It writes `<slug>/qa-report.json`.

A non-zero exit code means the build is **not `qa` and not `premium`**. Fix the errors and rerun until it passes.

Do not replace validator output with a sentence in `evidence.md` claiming that everything passed.

## 8. Browser QA must be described literally

Machine validation does not replace browser QA.

If browser rendering is available, inspect the actual rendered site and record exactly what was checked.

At minimum, inspect:

- homepage at desktop and mobile widths;
- menu at desktop and mobile widths;
- the most restaurant-specific page at desktop and mobile widths;
- navigation on every page;
- console output;
- responsive overflow/clipping;
- keyboard navigation and focus behavior.

Do not write “zero console errors,” “tested to 360px,” or similar claims unless those checks were actually performed.

If browser rendering is unavailable, say so plainly. The highest honest status remains `qa` only after the machine validator passes.

## 9. Status rules after this correction

- `lead` — eligible, no current qualifying build;
- `incomplete` — build exists but fails structure, facts, design, or validation;
- `qa` — machine validator passes and implementation is ready for/has partial browser QA;
- `premium` — machine validator passes, factual provenance is sound, add-ons remain preserved, the anti-template gate passes, and full desktop/mobile browser QA passes;
- `promoted` / `promoted_secondary` — only with explicit Showcase approval.

A folder with five or six files is not evidence of quality. A polished `evidence.md` is not evidence of QA. **The rendered result and machine checks control.**

## 10. Known regression specimen

`adamary-s-restaurante-y-pupuseria/` is intentionally left untouched as the build that exposed these system weaknesses.

Do not silently repair it as part of build-system work. Use it as a regression specimen: the validator should expose objective defects in that build, and future automatic demos should avoid its unsupported-content and generic-template failure modes.
