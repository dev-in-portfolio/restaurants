# Portal Status Audit — 2026-07-15

## Scope

Audit of the live `main` portal status claims, the Boudreaux’s page structure, recent restaurant-build commits, shared portal syntax, and the repository completion rules.

## Findings

### 1. The portal was claiming completion under a five-page standard

The portal rendered legacy `status:"full"` entries as `FULL 5-PAGE • QA PENDING` and rendered Boudreaux’s `status:"premium"` as `PREMIUM • IDENTITY REBUILD`.

That conflicts with the current six-page requirement.

### 2. Boudreaux’s is five pages, not six

The Boudreaux’s navigation links to:

1. `index.html`
2. `menu.html`
3. `story.html`
4. `gatherings.html`
5. `visit.html`

It is therefore an existing five-page identity build and is incomplete under the six-page standard.

### 3. Models were actively publishing five-page builds as full

Recent commit messages repeatedly described restaurants as five-page builds and upgraded their portal records from lead to full. This was consistent with the previous README but is no longer consistent with the six-page requirement.

### 4. The shared portal source had a JavaScript syntax error

The inline concepts array contained adjacent object records without a comma between the `ACE No. 3` and `The Royal Tot` entries. That can prevent the portal script from parsing and stop the restaurant wall from rendering.

### 5. The shared portal source contains mixed encoding damage

Several entries contain replacement characters, broken punctuation, and damaged emoji. This appears to have accumulated through concurrent whole-file edits using inconsistent text encoding.

### 6. One giant inline array was creating avoidable merge collisions

Many models were editing the same `index.html` array. This increased the risk of missing commas, overwritten entries, encoding damage, and simultaneous-push conflicts.

## Corrections

- Preserved the previous portal source as `portal-concepts-source.html`.
- Replaced the fragile root portal with a clean shell and separate `portal.js` renderer.
- Added line-by-line legacy record recovery so one malformed record cannot break every tile.
- Added deduplication across legacy entries and both lead sources.
- Added `portal-overrides.js` as the only shared restaurant-status override file.
- Forced every legacy `full` or `premium` record to display as `INCOMPLETE • 6-PAGE STANDARD NOT MET`.
- Kept queued leads labeled `LEAD • NOT BUILT YET`.
- Added future statuses for `6/6 PAGES • QA PENDING` and `PREMIUM • 6-PAGE IDENTITY REBUILD`, but no restaurant currently receives either status.
- Updated the README to require six separate substantive pages.

## Current result

At the time of this reset:

- No restaurant is marked complete.
- No restaurant is marked premium.
- Boudreaux’s is marked incomplete.
- Existing builds remain viewable.
- Lead tiles remain queued.
- Future models must add a verified override only after the six-page standard is met.
