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
  { name: "Night Swim Coffee", status: "premium", href: "night-swim-coffee/index.html" },
  { name: "Niki’s Food Shop", status: "premium", href: "niki-s-food-shop/index.html" },
  { name: "Ninety’s Dessert Bar", status: "premium", href: "ninety-s-dessert-bar/index.html" },
  { name: "No Proof", status: "premium", href: "no-proof/index.html" },
  { name: "NoDa Bodega", status: "premium", href: "noda-bodega/index.html" },
  { name: "Nora Mac’s Traditional Irish Pub", status: "premium", href: "nora-mac-s-traditional-irish-pub/index.html" },
  { name: "Oaklore Bar & Bottle Shop", status: "premium", href: "oaklore-bar-and-bottle-shop/index.html" },
  { name: "Oh My Ganache, The Cheesecake Bar", status: "premium", href: "oh-my-ganache-the-cheesecake-bar/index.html" },
  { name: "Oh My Soul", status: "premium", href: "oh-my-soul/index.html" },
  { name: "Olivelli Deli", status: "premium", href: "olivelli-deli/index.html" },
  { name: "Panda’s Den", status: "premium", href: "panda-s-den/index.html" },
  { name: "Papi Queso", status: "premium", href: "papi-queso/index.html" },
  { name: "Papi Ricko Latin Kitchen & Lounge", status: "premium", href: "papi-ricko-latin-kitchen-and-lounge/index.html" },
  { name: "Parkway House Family Restaurant", status: "premium", href: "parkway-house-family-restaurant/index.html" },
  { name: "Passage to India Indian Cuisine", status: "premium", href: "passage-to-india-indian-cuisine/index.html" },
  { name: "Pho Huong Que", status: "premium", href: "pho-huong-que/index.html" },
  { name: "Picasso’s Sports Café", status: "premium", href: "picasso-s-sports-cafe/index.html" },
  { name: "Persuasian Restaurant", status: "premium", href: "persuasian-restaurant/index.html" },
  { name: "Pertinacious Coffee", status: "premium", href: "pertinacious-coffee/index.html" },
  { name: "Littl Madeleine", status: "premium", href: "littl-madeleine/index.html" },
  { name: "Laurel Park", status: "premium", href: "laurel-park/index.html" },
  { name: "Pokebowl Ramen", status: "premium", href: "pokebowl-ramen/index.html" },
  { name: "Poppy’s Bagels & More", status: "premium", href: "poppy-s-bagels-and-more/index.html" },
  { name: "Pho Quynh", status: "premium", href: "pho-quynh/index.html" },
  { name: "Platform Coffee + Kitchen", status: "premium", href: "platform-coffee-plus-kitchen/index.html" },
  { name: "Mily & Lalo Peruvian Restaurant", portalSection: "later", note: "Located in Columbus GA outside Charlotte market; hold for regional queue." },
  { name: "Angela’s Pizzeria & Restaurant", portalSection: "later", note: "Third-party delivery platforms report temporarily closed; needs recheck." },
  { name: "Lorem Ipsum Listening Bar", status: "closed", note: "Permanently closed in July 2026" }
];
