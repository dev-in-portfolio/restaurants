import os

os.makedirs("hasaki-grill-and-sushi", exist_ok=True)

nav_links = [
    ("Home", "index.html"),
    ("Full Menu", "menu.html"),
    ("Hibachi & Bentos", "teppan-hibachi-and-bento-boxes.html"),
    ("Specialty Sushi", "specialty-sushi-rolls-and-sashimi.html"),
    ("Corporate Catering", "corporate-catering-and-sushi-platters.html"),
    ("Visit & Location", "visit.html")
]

def render_nav(active_page):
    links_html = ""
    for label, url in nav_links:
        active_cls = ' active' if url == active_page else ''
        links_html += f'<li><a href="{url}" class="hasaki-nav-link{active_cls}">{label}</a></li>\n'
    return f"""
  <div class="hasaki-announcement">
    <span>Ally Center 1st Floor &bull; Sizzling Teppan Hibachi & Craft Sushi &bull; Open Mon-Sat!</span>
    <a href="visit.html">Find 440 S Church St &rarr;</a>
  </div>
  <header class="hasaki-navbar">
    <div class="hasaki-nav-container">
      <a href="index.html" class="hasaki-brand">
        <span class="hasaki-brand-name">Hasaki<span>Grill</span></span>
        <span class="hasaki-brand-tagline">Ally Center &bull; Uptown Charlotte</span>
      </a>
      <button class="hasaki-mobile-toggle" aria-label="Toggle navigation menu">&#9776;</button>
      <ul class="hasaki-nav-links">
        {links_html}
        <li><a href="tel:9808199580" class="hasaki-nav-link hasaki-nav-cta">Call (980) 819-9580</a></li>
      </ul>
    </div>
  </header>
"""

def render_footer():
    return """
  <footer class="hasaki-footer">
    <div class="hasaki-container">
      <div class="hasaki-footer-grid">
        <div>
          <h4 class="hasaki-footer-title">Hasaki Grill &amp; Sushi</h4>
          <p style="color: #d4d4d8; font-size: 0.95rem; margin-bottom: 16px;">
            Authentic Japanese teppanyaki hibachi, chef signature sushi rolls, and executive lunch bento boxes located inside the Ally Center on South Church Street.
          </p>
          <span class="hasaki-badge hasaki-badge-wasabi">Fast-Casual Hibachi &amp; Sushi</span>
        </div>
        <div>
          <h4 class="hasaki-footer-title">Showcase Navigation</h4>
          <ul class="hasaki-footer-links">
            <li><a href="index.html" class="hasaki-footer-link">Home & Overview</a></li>
            <li><a href="menu.html" class="hasaki-footer-link">Full Japanese Menu</a></li>
            <li><a href="teppan-hibachi-and-bento-boxes.html" class="hasaki-footer-link">Teppan Hibachi & Bento Boxes</a></li>
            <li><a href="specialty-sushi-rolls-and-sashimi.html" class="hasaki-footer-link">Specialty Sushi Rolls & Poke</a></li>
            <li><a href="corporate-catering-and-sushi-platters.html" class="hasaki-footer-link">Corporate Sushi Platters</a></li>
            <li><a href="visit.html" class="hasaki-footer-link">Ally Center Location & Parking</a></li>
          </ul>
        </div>
        <div>
          <h4 class="hasaki-footer-title">Location & Hours</h4>
          <div class="hasaki-footer-contact-item">
            <strong>Address</strong>
            440 S Church St, Suite 104<br>
            Ally Center (1st Floor)<br>
            Charlotte, NC 28202
          </div>
          <div class="hasaki-footer-contact-item">
            <strong>Operating Hours</strong>
            Monday &ndash; Thursday: 11:00 AM &ndash; 9:00 PM<br>
            Friday &ndash; Saturday: 11:00 AM &ndash; 10:00 PM<br>
            Sunday: Closed
          </div>
        </div>
        <div>
          <h4 class="hasaki-footer-title">Direct Orders & Pickup</h4>
          <div class="hasaki-footer-contact-item">
            <strong>Direct Phone Line</strong>
            <a href="tel:9808199580" style="color: #fecdd3; text-decoration: none; font-weight: 700;">(980) 819-9580</a>
          </div>
          <div class="hasaki-footer-contact-item">
            <strong>Online Ordering & Pickup</strong>
            <span>Order through hasakigrill.com for fast lobby counter pickup or Uptown tower delivery.</span>
          </div>
        </div>
      </div>
      <div class="hasaki-footer-bottom">
        <p>&copy; 2026 Hasaki Grill &amp; Sushi. Ally Center Uptown Charlotte. Showcase demo created with zero emojis.</p>
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
  <title>{title} | Hasaki Grill & Sushi Uptown Charlotte</title>
  <meta name="description" content="Hasaki Grill & Sushi at 440 S Church St Suite 104 in Ally Center, Uptown Charlotte. Sizzling hibachi steak and chicken, bento boxes, craft sushi rolls, poke, and corporate catering.">
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
