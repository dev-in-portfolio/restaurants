// Build-status patches for the canonical audited queue only.
// Do not add restaurants that are not already present in queue/*.js.
// Allowed statuses: lead, incomplete, qa, premium, promoted, promoted_secondary.
// Minimal completed-build patch example:
// { name: "Restaurant Name", status: "premium", href: "restaurant-slug/index.html" }
// Use portalSection: "later" only when fresh verification shows the audited lead needs a recheck.
window.portalOverrides = [
  { name: "The Brickyard", status: "premium", href: "the-brickyard/index.html" },
  { name: "The ChangeBaker Place", status: "premium", href: "the-changebaker-place/index.html" },
  { name: "The Corner Pub", status: "premium", href: "the-corner-pub/index.html" },
  { name: "The Craic", status: "premium", href: "the-craic/index.html" },
  { name: "The Diamond Restaurant", status: "premium", href: "the-diamond-restaurant/index.html" },
  { name: "Milkbread", status: "premium", href: "milkbread/index.html" },
  { name: "Midwood Country Club", status: "premium", href: "midwood-country-club/index.html" },
  { name: "Miro Spanish Grille", status: "premium", href: "miro-spanish-grille/index.html" },
  { name: "Mother of Dragons", status: "premium", href: "mother-of-dragons/index.html" },
  { name: "Must Be Nice", status: "premium", href: "must-be-nice/index.html" },
  { name: "Nalan Indian Cuisine", status: "premium", href: "nalan-indian-cuisine/index.html" },
  { name: "Mily & Lalo Peruvian Restaurant", portalSection: "later", note: "Located in Columbus GA outside Charlotte market; hold for regional queue." },
  { name: "Angela’s Pizzeria & Restaurant", portalSection: "later", note: "Third-party delivery platforms report temporarily closed; needs recheck." },
  { name: "Lorem Ipsum Listening Bar", status: "closed", note: "Permanently closed in July 2026" }
];
