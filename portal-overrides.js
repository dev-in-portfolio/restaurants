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
  { name: "Babaloo Coffee Club", status: "premium", href: "babaloo-coffee-club/index.html" },
  { name: "Backyard Brew", status: "premium", href: "backyard-brew/index.html" },
  { name: "Bar à Vins", status: "premium", href: "bar-a-vins/index.html" },
  { name: "Blue Orchid Sushi & Asian Bistro", status: "premium", href: "blue-orchid-sushi-and-asian-bistro/index.html" },
  { name: "Bonzai Thai Cuisine", status: "premium", href: "bonzai-thai-cuisine/index.html" },
  { name: "Brawley’s Beverage", status: "premium", href: "brawley-s-beverage/index.html" },
  { name: "Buona Vita Pub & Pizzeria", status: "premium", href: "buona-vita-pub-and-pizzeria/index.html" },
  { name: "Café Audire", status: "premium", href: "cafe-audire/index.html" },
  { name: "Caffeto Specialty Coffee", status: "premium", href: "caffeto-specialty-coffee/index.html" },
  { name: "Caribbean Hut", status: "premium", href: "caribbean-hut/index.html" },
  { name: "Carmella’s Pizza Grill", status: "premium", href: "carmella-s-pizza-grill/index.html" },
  { name: "Chaat ’N’ Dosa", status: "premium", href: "chaat-n-dosa/index.html" },
  { name: "Cheat’s Cheesesteaks", status: "premium", href: "cheat-s-cheesesteaks/index.html" },
  { name: "Chez Marie Pâtisserie", status: "premium", href: "chez-marie-patisserie/index.html" },
  { name: "CHNO Coffee Co.", status: "premium", href: "chno-coffee-co/index.html" },
  { name: "Choi’s Korea & Wing", status: "premium", href: "choi-s-korea-and-wing/index.html" },
  { name: "Chop Chop Red Pot", status: "premium", href: "chop-chop-red-pot/index.html" },
  { name: "Cilantro Noodle + Kitchen", status: "premium", href: "cilantro-noodle-plus-kitchen/index.html" },
  { name: "Circle G Restaurant", status: "premium", href: "circle-g-restaurant/index.html" },
  { name: "Clark’s Snack Bar", status: "premium", href: "clark-s-snack-bar/index.html" },
  { name: "Club West Brewing", status: "premium", href: "club-west-brewing/index.html" },
  { name: "Coffey Creek Café", status: "premium", href: "coffey-creek-cafe/index.html" },
  { name: "Comal Taco Co.", status: "premium", href: "comal-taco-co/index.html" },
  { name: "DeepCuts HiFi", status: "premium", href: "deepcuts-hifi/index.html" }
];
