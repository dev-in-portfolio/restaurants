# Charlotte-Area Restaurant Website Demo Factory

This repository is a **sales portfolio of custom, unofficial restaurant website redesign concepts**.

The demos are built so Devin can visit independent restaurants and say:

> “I already redesigned your website. Here is what it could look like.”

They are **not live restaurant websites**, public ordering systems, or a consumer restaurant directory. Each demo should look polished and restaurant-specific while remaining visibly labeled as an unofficial presentation concept.

---

# Instructions for ChatGPT / Codex / Connected GitHub Threads

## Primary operating rule

When the user connects this repository and sends only a list such as:

```text
Restaurant One — Charlotte
Restaurant Two — Matthews
Restaurant Three — Pineville
```

**Immediately research and build the new demos.**

Do not require the user to repeat the project explanation, choose a template, approve a plan, provide links, or restate these instructions.

Use this README as the authoritative workflow.

The expected default action is:

1. Verify every restaurant.
2. Research its current online presence and website weaknesses.
3. Build a restaurant-specific demo using the existing shared system.
4. Add the demo to the main portfolio page.
5. Validate all paths and concept keys.
6. Commit the completed changes to the repository’s default branch.
7. Report what was added and any factual details intentionally left for owner confirmation.

Do not modify or remove existing restaurant demos unless the user explicitly requests it.

---

# What Each Demo Is Supposed to Do

Each demo should:

- Feel specifically designed for that restaurant.
- Reflect the restaurant’s real identity, cuisine, atmosphere, neighborhood, and strongest sales opportunities.
- Clearly outperform or improve upon the restaurant’s current online presentation.
- Give Devin a compelling visual tool for an in-person sales pitch.
- Demonstrate possible ordering, reservations, catering, events, or inquiry experiences without pretending those systems are already connected.
- Work well on desktop and mobile.

A demo should **not** feel like the same generic restaurant site with only the name and colors changed.

---

# Mandatory Research Workflow

Research each restaurant before writing copy.

## Source priority

Use the freshest and most reliable sources available:

1. **Google Maps / Google Business Profile**
   - Exact current business name
   - Open, temporarily closed, or permanently closed status
   - Address
   - Phone
   - Current hours
   - Website and social links
   - Recent owner updates
   - Recent reviews and exterior photographs

2. **Official restaurant website**
   - Menu
   - Ordering links
   - Reservations
   - Catering
   - Private events
   - Gift cards
   - Restaurant history
   - Contact information

3. **Official social accounts**
   - Current operating status
   - Recent menu items
   - Events
   - Updated hours
   - Current location

4. **Official ordering and reservation platforms**
   - Toast
   - Clover
   - SpotOn
   - OpenTable
   - DoorDash
   - Uber Eats
   - Grubhub
   - Slice
   - Other restaurant-linked services

5. **Reliable recent local coverage**
   - Axios Charlotte
   - Charlotte Observer
   - Charlotte Magazine
   - WCNC
   - WFAE
   - Local municipal or downtown-development sources

Do not treat an old directory, scraped menu site, or unverified AI-generated summary as authoritative when fresher primary information exists.

## Verification standard

Before presenting a detail as fact, verify it whenever practical.

Especially verify:

- Exact business name
- Whether the restaurant is currently operating
- Address and ZIP code
- Phone number
- Hours
- Founding year
- Ownership or family story
- Menu items described as signatures
- Ordering and reservation methods
- Catering and private-event services
- Multiple locations

When information cannot be confidently verified, use conservative copy such as:

- `Current phone to be confirmed with the restaurant`
- `Current hours to be confirmed before launch`
- `Exact current service location to be confirmed`
- `Owner-approved menu details would replace these demo examples`

Do not invent facts merely to make the demo sound complete.

---

# Accuracy Rules

## Safe creative freedom

It is acceptable to create:

- Headlines
- Taglines
- Design positioning
- Proposed information architecture
- Suggested customer journeys
- Generic descriptions of a cuisine category
- Proposed future integrations
- Clearly labeled representative menu sections

## Never invent these as restaurant facts

Do not invent:

- Founding years
- Owner names
- Family histories
- Awards
- Michelin recognition
- Sourcing claims
- Imported ingredients
- Scratch-made preparation claims
- Ownership transitions
- Exact recipes
- “Landmark” status
- Reservation policies
- Delivery policies
- Live wait times
- Current specials
- Current prices
- Exact hours
- Exact phone numbers or addresses

If a compelling historical or operational fact is used, it must come from a credible source.

---

# Existing Demo Architecture

New demos use the repository’s shared concept system.

## Shared files

- `concept-sites.css` — responsive shared visual system
- `concept-sites.js` — restaurant-specific data and shared page renderer
- `index.html` — main restaurant redesign portfolio

## Each new restaurant folder

Create one folder with a URL-safe slug:

```text
restaurant-name/index.html
```

Use lowercase kebab-case:

```text
beef-n-bottle/
sir-edmond-halleys/
home-style-kitchn/
```

The restaurant page should be a lightweight loader using the shared files:

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

The `data-concept` value must exactly match the new object key in `concept-sites.js`.

---

# Required Concept Data

Add one restaurant-specific object to `concept-sites.js`.

Each concept must include:

```js
conceptKey: {
  name: "Restaurant Name",
  short: "RN",
  location: "Neighborhood • City",
  cuisine: "Cuisine • Experience • Service",
  accent: "#hex",
  accent2: "#hex",
  paper: "#hex",
  heroImage: "CSS gradient or approved image treatment",
  headline: "Restaurant-specific headline.",
  lede: "Restaurant-specific positioning statement.",
  stats: [
    ["Fact or positioning", "Supporting label"],
    ["Fact or positioning", "Supporting label"],
    ["Fact or positioning", "Supporting label"]
  ],
  features: [
    ["01", "Specific improvement", "Why this matters for this restaurant."],
    ["02", "Specific improvement", "Why this matters for this restaurant."],
    ["03", "Specific improvement", "Why this matters for this restaurant."]
  ],
  menu: [
    ["Category", "Item or experience", "Verified or clearly representative description."],
    ["Category", "Item or experience", "Verified or clearly representative description."],
    ["Category", "Item or experience", "Verified or clearly representative description."],
    ["Category", "Item or experience", "Verified or clearly representative description."]
  ],
  storyTitle: "Restaurant-specific story heading.",
  story: "Verified history or conservative brand-positioning copy.",
  tags: ["Tag", "Tag", "Tag", "Tag", "Tag", "Tag"],
  address: "Verified address or confirmation language",
  phone: "Verified phone or confirmation language",
  email: "Verified email when available",
  hours: "Verified hours or confirmation language",
  actionLabel: "Primary CTA",
  actionText: "Proposed production integration",
  formTopic: "Appropriate inquiry type"
}
```

## Restaurant-specific differentiation

At minimum, customize:

- Visual palette
- Hero treatment
- Headline
- Positioning paragraph
- Three opportunity cards
- Four menu/experience spotlights
- Brand story
- Tags
- Primary CTA
- Inquiry type

Examples of genuinely different sales angles:

- Historic steakhouse → atmosphere, reservations, gift cards, wine
- Sports bar → live game schedule, specials, watch parties
- Social-first soul-food kitchen → today’s plates, pickup, catering
- Fine dining → reservations, wine, private events
- Dive bar → live music, story, directions, minimal polish
- Pizza and wine market → pizza style, bottles, retail market, neighborhood identity

---

# Demo Disclosure Requirements

Every new demo must retain the shared disclosure language:

```text
Unofficial website redesign concept • Presentation demo
```

The footer must clarify that the demo is not affiliated with or operated by the restaurant.

Interactive forms must:

- Be demonstrations only.
- Never send data.
- Never imply the restaurant received a reservation, order, or inquiry.
- Display a confirmation such as:

```text
Demo complete — no information was submitted.
```

Never create fake live wait times, inventory, table availability, order confirmations, or restaurant responses.

---

# Main Portfolio Update

Add one new card per restaurant to the `concepts` array in root `index.html`.

Each card requires:

```js
{
  name: "Restaurant Name",
  area: "Charlotte",
  cuisine: "Cuisine • Experience",
  description: "Concise explanation of the redesign opportunity.",
  emoji: "🍽️",
  href: "restaurant-slug/index.html",
  gradient: "linear-gradient(...)"
}
```

Card requirements:

- `href` must match the created folder.
- Description should explain the concept’s sales angle.
- Area should be Charlotte, Matthews, Pineville, Monroe, Ballantyne, or the accurate nearby area.
- Do not use fabricated star ratings or prices.
- Keep the `DEMO` badge.

---

# Visual Quality Standard

New demos should be:

- Responsive
- Legible
- Restaurant-specific
- Visually polished
- Appropriate to the business category
- Free of placeholder lorem ipsum
- Free of raw filenames
- Free of broken links
- Free of fake production claims
- Strong enough to show directly to a restaurant owner

Use the shared system by default, but extend `concept-sites.css` when a new concept genuinely requires a new reusable component.

Do not create a radically different technical architecture for each restaurant unless the user explicitly asks for a fully bespoke build.

---

# Completion Checklist

Before reporting that a batch is complete, confirm:

- [ ] Every requested restaurant has a folder and `index.html`.
- [ ] Every page’s `data-concept` key exists in `concept-sites.js`.
- [ ] Every concept key is unique.
- [ ] Every main-portfolio card links to the correct folder.
- [ ] Every restaurant name is spelled correctly.
- [ ] Current operating status was checked.
- [ ] Core facts are verified or explicitly marked for confirmation.
- [ ] No unsupported founding years, owner stories, awards, or sourcing claims were added.
- [ ] No demo form sends data or falsely confirms a restaurant action.
- [ ] All pages retain the unofficial-demo disclosure.
- [ ] Mobile structure remains intact.
- [ ] Changes are committed to the repository.

If the repository has no automated CI checks, inspect the updated files directly and report that no automated checks are configured.

---

# Expected User Experience in Future Threads

The user should be able to begin a new connected thread and send only:

```text
Build these demos next:

Restaurant A — Charlotte
Restaurant B — Matthews
Restaurant C — Pineville
```

The assistant should then perform the entire workflow without asking the user to re-explain the purpose of the repository.

Only ask a question when two distinct active businesses share the same name and location cannot be resolved through research. Otherwise, make the safest evidence-based choice and proceed.

---

# Repository Intent in One Sentence

**Research real independent restaurants, build accurate restaurant-specific redesign demos, add them to the portfolio, and make them ready for Devin to use during in-person website sales pitches.**
