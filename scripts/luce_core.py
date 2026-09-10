import os

os.makedirs("luce-ristorante", exist_ok=True)

nav_links = [
    ("Home", "index.html"),
    ("Full Menu", "menu.html"),
    ("Handmade Pastas", "handmade-pastas-and-tuscan-classics.html"),
    ("Wine Cellar", "wine-cellar-and-aperitivo-cocktails.html"),
    ("Private Events", "private-dining-and-plaza-events.html"),
    ("Visit & Parking", "visit.html")
]

def render_nav(active_page):
    links_html = ""
    for label, url in nav_links:
        active_cls = ' active' if url == active_page else ''
        links_html += f'<li><a href="{url}" class="luce-nav-link{active_cls}">{label}</a></li>\n'
    return f"""
  <div class="luce-announcement">
    <span>Conte Restaurant Group &bull; Truist Center Plaza &bull; 2-Hour Evening Parking Validation After 5:00 PM</span>
    <a href="visit.html">Find Plaza &rarr;</a>
  </div>
  <header class="luce-navbar">
    <div class="luce-nav-container">
      <a href="index.html" class="luce-brand">
        <span class="luce-brand-name">Luce Ristorante e Bar</span>
        <span class="luce-brand-tagline">Truist Center Plaza &bull; Uptown Charlotte</span>
      </a>
      <button class="luce-mobile-toggle" aria-label="Toggle navigation menu">&#9776;</button>
      <ul class="luce-nav-links">
        {links_html}
        <li><a href="tel:7043449222" class="luce-nav-link luce-nav-cta">Reservations (704) 344-9222</a></li>
      </ul>
    </div>
  </header>
"""

def render_footer():
    return """
  <footer class="luce-footer">
    <div class="luce-container">
      <div class="luce-footer-grid">
        <div>
          <h4 class="luce-footer-title">Luce Ristorante e Bar</h4>
          <p style="color: #d6d3d1; font-size: 0.95rem; margin-bottom: 16px;">
            An exquisite Tuscan culinary landmark in Uptown Charlotte by the Conte Restaurant Group. Fresh handmade pastas, prime meats, Mediterranean seafood, and an award-winning Italian cellar.
          </p>
          <span class="luce-badge luce-badge-gold">Fine Dining Tuscan Tradition</span>
        </div>
        <div>
          <h4 class="luce-footer-title">Showcase Navigation</h4>
          <ul class="luce-footer-links">
            <li><a href="index.html" class="luce-footer-link">Home & Overview</a></li>
            <li><a href="menu.html" class="luce-footer-link">Full Italian Dinner Menu</a></li>
            <li><a href="handmade-pastas-and-tuscan-classics.html" class="luce-footer-link">Handmade Pastas & Ragùs</a></li>
            <li><a href="wine-cellar-and-aperitivo-cocktails.html" class="luce-footer-link">Italian Cellar & Aperitivi</a></li>
            <li><a href="private-dining-and-plaza-events.html" class="luce-footer-link">Plaza Patio & Private Events</a></li>
            <li><a href="visit.html" class="luce-footer-link">Truist Center Plaza & Parking</a></li>
          </ul>
        </div>
        <div>
          <h4 class="luce-footer-title">Plaza Location & Hours</h4>
          <div class="luce-footer-contact-item">
            <strong>Address</strong>
            214 N Tryon St, Suite J<br>
            Truist Center Plaza<br>
            Charlotte, NC 28202
          </div>
          <div class="luce-footer-contact-item">
            <strong>Hours of Service</strong>
            Mon &ndash; Thu: 11:30 AM &ndash; 2:30 PM, 5:00 PM &ndash; 10:00 PM<br>
            Fri: 11:30 AM &ndash; 2:30 PM, 5:00 PM &ndash; 10:30 PM<br>
            Sat: 5:00 PM &ndash; 10:30 PM<br>
            Sun: Closed
          </div>
        </div>
        <div>
          <h4 class="luce-footer-title">Reservations & Parking</h4>
          <div class="luce-footer-contact-item">
            <strong>Direct Phone Line</strong>
            <a href="tel:7043449222" style="color: #fed7aa; text-decoration: none; font-weight: 700;">(704) 344-9222</a>
          </div>
          <div class="luce-footer-contact-item">
            <strong>Parking Validation</strong>
            <span>2 hours validated parking in the Truist Center parking deck (entrance on 5th Street) after 5:00 PM.</span>
          </div>
        </div>
      </div>
      <div class="luce-footer-bottom">
        <p>&copy; 2026 Luce Ristorante e Bar &bull; Conte Restaurant Group. Uptown Charlotte. Showcase demo created with zero emojis.</p>
      </div>
    </div>
  </footer>
"""

def wrap_page(title, active_page, content):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Luce Ristorante e Bar Uptown Charlotte</title>
  <meta name="description" content="Luce Ristorante e Bar at 214 N Tryon St Suite J in Truist Center Plaza, Uptown Charlotte. Fine dining Tuscan cuisine, handmade pastas, ossobuco, Italian wine cellar, and patio dining.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
  {render_nav(active_page)}
  <main>
    {content}
  </main>
  {render_footer()}
  <script src="site.js"></script>
</body>
</html>
"""
