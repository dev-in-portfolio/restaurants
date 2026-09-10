// Build-status patches for the canonical audited queue only.
// Do not add restaurants that are not already present in queue/*.js.
// Allowed statuses: lead, incomplete, qa, premium, promoted, promoted_secondary.
// Minimal completed-build patch example:
// { name: "Restaurant Name", status: "premium", href: "restaurant-slug/index.html" }
// Use portalSection: "later" only when fresh verification shows the audited lead needs a recheck.
window.portalOverrides = [
  { name: "Midwood Country Club", status: "qa", href: "midwood-country-club/index.html" },
  { name: "República Restaurant & Lounge", status: "promoted", href: "republica-restaurant-and-lounge/index.html", note: "Promoted to Showcase as Republica" },
  { name: "Indigo Tea & Coffee Co.", status: "premium", href: "indigo-tea-and-coffee-co/index.html" },
  { name: "Nefelie’s", status: "premium", href: "nefelie-s/index.html" },
  { name: "The Local", status: "premium", href: "the-local/index.html" },
  { name: "Mortimer’s Café & Pub", status: "premium", href: "mortimer-s-cafe-and-pub/index.html" },
  { name: "Santa Fe Mexican Restaurant — Central Ave", status: "premium", href: "santa-fe-mexican-restaurant-central-ave/index.html" },
  { name: "Landmark Restaurant Diner", status: "premium", href: "landmark-restaurant-diner/index.html" },
  { name: "Van Loi Chinese Barbecue", status: "premium", href: "van-loi-chinese-barbecue/index.html" },
  { name: "Pho An Hoa", status: "premium", href: "pho-an-hoa/index.html" },
  { name: "Sweet Crunch Waffles", status: "premium", href: "sweet-crunch-waffles/index.html" },
  { name: "Kuya Omakase 2.0", status: "premium", href: "kuya-omakase-2-0/index.html" },
  { name: "Seoul Good CLT", status: "premium", href: "seoul-good-clt/index.html" },
  { name: "Pasta Crush", status: "premium", href: "pasta-crush/index.html" },
  { name: "La Cocina Mexicana", status: "premium", href: "la-cocina-mexicana/index.html" },
  { name: "Phil’s Deli To Go", status: "premium", href: "phil-s-deli-to-go/index.html" },
  { name: "Sub One Hoagie House", status: "premium", href: "sub-one-hoagie-house/index.html" },
  { name: "Poppin Sushi & Poke", status: "premium", href: "poppin-sushi-and-poke/index.html" },
  { name: "Impeckable Chicken", status: "premium", href: "impeckable-chicken/index.html" },
  { name: "Hip Hop Smoothies", status: "premium", href: "hip-hop-smoothies/index.html" },
  { name: "Jamile’s Cuisine International", status: "premium", href: "jamile-s-cuisine-international/index.html" },
  { name: "Nile Grocery & Cafe", status: "premium", href: "nile-grocery-and-cafe/index.html" },
  { name: "Maroon Market", portalSection: "later", note: "Typographical artifact for parent food hall Monarch Market housing individual vendor stalls (Kuya Omakase, Seoul Good, Pasta Crush); no standalone stall." },
  { name: "Sweet Boutique Bakery", portalSection: "later", note: "Residential custom cake studio at 9814 Zackery Ave; no public retail walk-in storefront." },
  { name: "Mily & Lalo Peruvian Restaurant", portalSection: "later", note: "Located in Columbus GA outside Charlotte market; hold for regional queue." },
  { name: "Angela’s Pizzeria & Restaurant", portalSection: "later", note: "Third-party delivery platforms report temporarily closed; needs recheck." },
  { name: "Shawarma2Go", status: "closed", note: "Closed; ghost kitchen concept at 231 N Caldwell St ceased operations in July 2025." },
  { name: "The Royal Tot", status: "closed", note: "Closed; rooftop tiki lounge at 933 Louise Ave ceased operations." },
  { name: "Lorem Ipsum Listening Bar", status: "closed", note: "Permanently closed in July 2026" },
  { name: "Provided Coffee", status: "closed", note: "Charlotte locations closed in June 2026; consolidated to Concord NC flagship" }
];
