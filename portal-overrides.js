// Build-status patches for the canonical audited queue only.
// Do not add restaurants that are not already present in queue/*.js.
// Allowed statuses: lead, incomplete, qa, premium, promoted, promoted_secondary.
// Minimal completed-build patch example:
// { name: "Restaurant Name", status: "premium", href: "restaurant-slug/index.html" }
// Use portalSection: "later" only when fresh verification shows the audited lead needs a recheck.
window.portalOverrides = [
  { name: "1900 Mexican Grill", status: "premium", href: "1900-mexican-grill/index.html" },
  { name: "Adamary’s Restaurante y Pupuseria", status: "qa", href: "adamary-s-restaurante-y-pupuseria/index.html" }
];
