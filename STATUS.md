# Restaurant Demo Status

## Active canonical queue

The repository has been reset to the final reconciled A/B prospect set from the completed 645-record Rada-depth audit.

- **407 active audited prospects**
- **284 A-grade YES**
- **46 B-grade YES**
- **77 B-grade CONDITIONAL**
- HOLD, NO, closed/out-of-scope records, and merged aliases are excluded from automatic build selection.

Queue source files:

- `queue/a-yes-1.js`
- `queue/a-yes-2.js`
- `queue/b-yes.js`
- `queue/b-conditional.js`

## Build-status reset

`portal-overrides.js` was intentionally reset. Therefore every canonical prospect currently begins as `lead` unless a new six-page build is completed after this reset and receives a fresh override.

Existing restaurant folders are **legacy working material**, not completion evidence. Some are one-page prototypes, some were built under an older five-page standard, and some belong to restaurants no longer in the canonical active queue.

Do not automatically build a restaurant merely because its folder exists.

## Current completion standard

A restaurant may be marked `premium` only after the current README standard is met:

- six substantive linked pages;
- restaurant-specific premium art direction;
- two useful accessible interactions, including one conversion interaction;
- current factual verification and `evidence.md`;
- desktop and mobile browser QA;
- accessibility baseline passed;
- no live real-world form/payment/reservation claims;
- a fresh minimal patch in `portal-overrides.js`.

If browser QA is not available, the highest honest status is `qa`.

## Selection order

1. A-grade YES
2. B-grade YES
3. B-grade CONDITIONAL

Within a tier, sort alphabetically ignoring leading `The`, `A`, and `An`.

See `README.md` for the full one-shot build specification.
