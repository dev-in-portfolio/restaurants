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
  { name: "Anita’s Mexican Grill", status: "premium", href: "anita-s-mexican-grill/index.html" }
];
