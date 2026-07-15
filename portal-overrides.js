// Shared portal overrides.
// Add or replace one restaurant entry here after re-fetching the latest main branch.
// Allowed statuses: lead, incomplete, qa, premium.
// qa requires six separate substantive pages. premium also requires completed desktop/mobile browser QA.
window.portalOverrides = [
  {
    name: "Boudreaux’s Kitchen & Tavern",
    area: "NoDa",
    cuisine: "Louisiana Cajun Kitchen",
    description: "Soulful Cajun and Creole cuisine in the heart of NoDa. Built with industrial metal, neon strings, and a local crowd. Features a Bloody Mary bar customizer and group planner.",
    emoji: "🐊",
    href: "boudreauxs/index.html",
    gradient: "linear-gradient(135deg,#0d1010,#a5432d 52%,#f2b643)",
    status: "premium"
  },
  {
    name: "131 MAIN Restaurant",
    area: "Charlotte and Matthews",
    cuisine: "Modern American Grill",
    description: "Warm, upscale grill dining with locations at SouthPark and Blakeney. Prepared on a hickory wood-fire grill. Features an interactive cornbread customizer, location menu switcher, and reserve wine pairing assistant.",
    emoji: "🥩",
    href: "131-main-restaurant/index.html",
    gradient: "linear-gradient(135deg,#eab308,#2d1f18 52%,#121214)",
    status: "premium"
  }
];
