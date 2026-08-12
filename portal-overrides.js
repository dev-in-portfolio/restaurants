// Build-status patches for the canonical audited queue only.
// Do not add restaurants that are not already present in queue/*.js.
// Allowed statuses: lead, incomplete, qa, premium, promoted, promoted_secondary.
// Minimal completed-build patch example:
// { name: "Restaurant Name", status: "premium", href: "restaurant-slug/index.html" }
// Use portalSection: "later" only when fresh verification shows the audited lead needs a recheck.
window.portalOverrides = [
  { name: "1900 Mexican Grill", status: "premium", href: "1900-mexican-grill/index.html" },
  { name: "Adamary’s Restaurante y Pupuseria", status: "qa", href: "adamary-s-restaurante-y-pupuseria/index.html" },
  { name: "All Purpose Bar", status: "premium", href: "all-purpose-bar/index.html" },
  { name: "Angela’s Pizzeria & Restaurant", portalSection: "later", note: "Third-party delivery platforms report temporarily closed; needs recheck." },
  { name: "Anita’s Mexican Grill", status: "premium", href: "anita-s-mexican-grill/index.html" },
  { name: "ANJU Korean Dining & Bar", status: "premium", href: "anju-korean-dining-and-bar/index.html" },
  { name: "Ann Marie’s Gourmet Burgers & Fries", status: "premium", href: "ann-marie-s-gourmet-burgers-and-fries/index.html" },
  { name: "Aqua e Vino", status: "premium", href: "aqua-e-vino/index.html" },
  { name: "Aria Tuscan Grill", status: "premium", href: "aria-tuscan-grill/index.html" },
  { name: "Aroy Thai", status: "premium", href: "aroy-thai/index.html" },
  { name: "Assorted Table Wine & Shop", status: "premium", href: "assorted-table-wine-and-shop/index.html" },
  { name: "Astoria Café", status: "premium", href: "astoria-cafe/index.html" },
  { name: "Azucar Cuban Restaurant", status: "premium", href: "azucar-cuban-restaurant/index.html" },
  { name: "Azul Tequileria & Cocina", status: "premium", href: "azul-tequileria-and-cocina/index.html" },
  { name: "DeepCuts HiFi", status: "premium", href: "deepcuts-hifi/index.html" }
];
