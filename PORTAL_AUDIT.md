# Portal Architecture — Audited Queue Reset

## Current state

The portal no longer builds its active lead wall from the old mixed legacy sources.

The active source of truth is now the final reconciled A/B prospect set from the completed 645-record Rada-depth audit:

- **407 canonical active prospects**
- **284 A-grade YES**
- **46 B-grade YES**
- **77 B-grade CONDITIONAL**

HOLD, NO, closed, inactive, out-of-scope and merged alias records are excluded from the active build rotation.

## Canonical data

The queue is intentionally split into four compact files:

- `queue/a-yes-1.js`
- `queue/a-yes-2.js`
- `queue/b-yes.js`
- `queue/b-conditional.js`

Each row is:

```text
[name, slug, grade, disposition, score, auditBatch]
```

These files are audit data. Build completion does not modify them.

## Status overlays

`portal-overrides.js` contains only build-status patches for names already in the canonical queue.

The renderer applies overrides on top of the audit record, preserving the final grade, disposition, score, slug and audit-batch provenance.

This means a build agent can safely add a small patch such as:

```js
{ name: "Restaurant Name", status: "premium", href: "restaurant-slug/index.html" }
```

without rewriting the 407-record queue.

Overrides for names not found in the audited queue are ignored and surfaced as portal warnings.

## Legacy sources

These files are retained only as historical artifacts and are no longer loaded by `index.html`:

- `portal-leads-message2-original.js`
- `portal-leads-message3.js`
- `portal-concepts-source.html`

They must not be used to select new builds.

The previous portal mixed legacy concepts, old lead sources and status overrides. That architecture allowed stale, closed, merged and out-of-scope records to reappear. The new portal intentionally prevents that by starting only from the 407 canonical audited records.

## Existing restaurant folders

Existing folders are not automatically active cards and do not establish completion status.

A folder may contain:

- a historical prototype;
- an older five-page build;
- an incomplete build;
- work for a restaurant no longer in the active queue;
- or useful reference material for a current audited lead.

Only a canonical queue entry plus a current override determines portal state.

## Completion rule

The current standard is the six-page premium standard in `README.md`.

No build should receive `premium` unless it has:

- six substantive pages;
- two useful interactions including one conversion interaction;
- current factual evidence recorded in `evidence.md`;
- responsive desktop/mobile browser QA;
- accessibility baseline verification;
- no deceptive real-world form/order/reservation behavior.

If browser QA cannot be completed, use `qa`, not `premium`.

## Integrity checks in `portal.js`

The renderer now checks that:

- exactly **407** queue rows loaded;
- canonical queue names do not duplicate;
- override records refer only to names in the audited queue.

Any violation is displayed as a portal warning rather than silently expanding the active lead set.
