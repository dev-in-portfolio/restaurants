# Charlotte-Area Restaurant Website Demo Factory

This repository is a sales portfolio of custom, unofficial restaurant website redesign concepts.

The goal is for Devin to walk into an independent restaurant and say:

> “I already redesigned your website. Here is what it could look like.”

These are presentation demos—not live restaurant websites, public ordering systems, or a consumer directory.

---

# Instructions for Connected ChatGPT / Codex Threads

## Primary rule

When this repository is connected and the user sends only a restaurant list, immediately research, build, validate, commit, push, and merge the demos.

Example input:

```text
Restaurant One — Charlotte
Restaurant Two — Matthews
Restaurant Three — Pineville
```

Do not require the user to:

- Re-explain the project
- Choose a template
- Supply restaurant links
- Approve a plan
- Ask for a commit
- Ask for a push
- Ask for a pull request
- Ask for a merge
- Remind the assistant to publish the work

This README is the authoritative operating workflow.

---

# Mandatory End-to-End Workflow

For every restaurant batch:

1. Verify each restaurant is currently operating.
2. Research its current website, Google Business information, official social pages, menu, ordering links, reservation systems, and obvious website weaknesses.
3. Build a restaurant-specific demo using the existing shared system.
4. Add the restaurant to `concept-sites.js`.
5. Create its folder and `index.html` loader page.
6. Add its card to the root `index.html` portfolio.
7. Validate every folder path, card link, concept key, disclosure, and demo form.
8. Commit all completed changes.
9. Push the commit to GitHub.
10. Ensure the completed work is merged into the repository’s default branch.
11. Confirm the default branch contains the new demos before reporting completion.

## Publishing is automatic

**A batch is not complete merely because files were created locally or placed on a feature branch.**

The assistant must automatically finish the Git workflow without waiting for the user to remember or request it.

Preferred behavior:

- When direct default-branch writes are permitted, commit the changes directly to the default branch.
- When branch protection requires a pull request, create a branch, commit, push, open the pull request, merge it into the default branch, and confirm the merge.
- Do not leave the work only in an unpushed local checkout.
- Do not stop after opening a draft pull request.
- Do not report “done” while the new demos exist only on an unmerged branch.
- Do not ask for separate approval to commit, push, or merge unless GitHub permissions or branch protection technically prevent completion.

If permissions prevent the final push or merge, complete everything possible and report the exact blocker. Otherwise, publishing and merging are mandatory and automatic.

Do not modify or remove existing demos unless the user explicitly asks.

---

# Research and Accuracy Rules

Research every restaurant before writing factual copy.

Use sources in this order whenever available:

1. Google Maps / Google Business Profile
2. Official restaurant website
3. Official restaurant social accounts
4. Official ordering or reservation platforms
5. Reliable recent local reporting

Verify whenever practical:

- Current operating status
- Exact business name
- Address and ZIP code
- Phone number
- Hours
- Official website
- Menu and recognizable dishes
- Ordering and reservation methods
- Catering and private-event services
- Founding year
- Ownership or family history
- Multiple locations

Never invent restaurant facts such as:

- Founding years
- Owner names
- Family histories
- Awards
- Michelin recognition
- Sourcing claims
- Imported ingredients
- Scratch-made claims
- Exact recipes
- Landmark status
- Delivery policies
- Reservation policies
- Live wait times
- Current specials
- Current prices

When a fact cannot be confirmed, use conservative wording such as:

```text
Current phone to be confirmed with the restaurant
Current hours to be confirmed before launch
Exact current location to be confirmed
Owner-approved menu details would replace these demo examples
```

Creative headlines, taglines, design direction, proposed integrations, and clearly labeled representative menu sections are allowed.

---

# Demo Architecture

Shared files:

- `concept-sites.css` — responsive shared visual system
- `concept-sites.js` — restaurant data and shared renderer
- `index.html` — main redesign portfolio

Each restaurant gets a lowercase kebab-case folder:

```text
restaurant-name/index.html
```

Example loader:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Unofficial website redesign concept for RESTAURANT in CITY, North Carolina.">
  <title>RESTAURANT | Website Redesign Concept</title>
  <link rel="stylesheet" href="../concept-sites.css">
</head>
<body data-concept="uniqueConceptKey">
  <noscript>This restaurant website concept requires JavaScript to display.</noscript>
  <script src="../concept-sites.js"></script>
</body>
</html>
```

The `data-concept` value must exactly match the restaurant object key in `concept-sites.js`.

Each concept must include restaurant-specific:

- Name and location
- Cuisine and experience positioning
- Color palette and hero treatment
- Headline and introductory copy
- Three highlight statistics
- Three website-opportunity cards
- Four representative menu or experience spotlights
- Brand story
- Tags
- Address, phone, email, and hours when verified
- Primary call to action
- Appropriate inquiry type

A demo must not feel like the same generic website with only the name and colors changed.

---

# Demo Disclosure Rules

Every demo must visibly include:

```text
Unofficial website redesign concept • Presentation demo
```

The footer must clarify that the demo is not affiliated with or operated by the restaurant.

Forms must:

- Be demonstrations only
- Never send information
- Never imply the restaurant received an order, reservation, or message
- Confirm clearly:

```text
Demo complete — no information was submitted.
```

Never create fake live wait times, table availability, inventory, order confirmations, or restaurant responses.

---

# Main Portfolio Rules

Add one card for every new demo to the root `index.html` concepts array.

Each card must include:

- Restaurant name
- Accurate area
- Cuisine or experience type
- Concise sales angle
- Emoji
- Correct folder link
- Distinct gradient
- `DEMO` badge

Do not use fabricated ratings or prices.

---

# Completion Checklist

Before reporting completion, confirm:

- [ ] Every requested restaurant has a folder and `index.html`.
- [ ] Every `data-concept` key exists in `concept-sites.js`.
- [ ] Every concept key is unique.
- [ ] Every portfolio card links to the correct folder.
- [ ] Restaurant names are spelled correctly.
- [ ] Operating status was checked.
- [ ] Core facts are verified or explicitly marked for confirmation.
- [ ] No unsupported history, awards, ownership, sourcing, or menu claims were added.
- [ ] Demo forms do not send data.
- [ ] Every page retains the unofficial-demo disclosure.
- [ ] Mobile structure remains intact.
- [ ] Changes were committed.
- [ ] Changes were pushed to GitHub.
- [ ] Changes are present on the default branch.
- [ ] Any required pull request was merged.

Only after all applicable boxes are complete should the assistant report that the batch is done.

---

# Future Thread Experience

The user should be able to connect the repository and send only:

```text
Build these demos next:

Restaurant A — Charlotte
Restaurant B — Matthews
Restaurant C — Pineville
```

The assistant should perform the complete research, build, validation, commit, push, and merge workflow automatically.

Only ask a question when two distinct active businesses share the same name and the correct one cannot be resolved through research.

---

# Repository Intent in One Sentence

**Research real independent restaurants, build accurate restaurant-specific redesign demos, publish and merge every completed batch to GitHub automatically, and keep the portfolio ready for Devin’s in-person website sales pitches.**
