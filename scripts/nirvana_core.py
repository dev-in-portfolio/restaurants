import os

os.makedirs("nirvana-ii", exist_ok=True)

nav_links = [
    ("Home", "index.html"),
    ("Full Menu", "menu.html"),
    ("Biryanis & Thalis", "signature-biryanis-and-thali-combos.html"),
    ("Curries & Tandoor", "tandoori-curries-and-vegetarian-classics.html"),
    ("Corporate Catering", "corporate-catering-and-lunch-boxes.html"),
    ("Visit & Location", "visit.html")
]

def render_nav(active_page):
    links_html = ""
    for label, url in nav_links:
        active_cls = ' active' if url == active_page else ''
        links_html += f'<li><a href="{url}" class="nirvana-nav-link{active_cls}">{label}</a></li>\n'
    return f"""
  <div class="nirvana-announcement">
    <span>Uptown Charlotte Indian Fusion Haven &bull; Open Mon-Fri 11:30am-3:30pm &bull; Fast-Casual Dum Biryanis & Thalis!</span>
    <a href="visit.html">Find 401 S Tryon St &rarr;</a>
  </div>
  <header class="nirvana-navbar">
    <div class="nirvana-nav-container">
      <a href="index.html" class="nirvana-brand">
        <span class="nirvana-brand-title">Nirvana II</span>
        <span class="nirvana-brand-tagline">Indian Fusion &bull; Uptown Charlotte</span>
      </a>
      <button class="nirvana-mobile-toggle" aria-label="Toggle navigation menu">&#9776;</button>
      <ul class="nirvana-nav-links">
        {links_html}
        <li><a href="tel:9802907002" class="nirvana-nav-link nirvana-nav-cta">Call (980) 290-7002</a></li>
      </ul>
    </div>
  </header>
"""

def render_footer():
    return """
  <footer class="nirvana-footer">
    <div class="nirvana-container">
      <div class="nirvana-footer-grid">
        <div>
          <h4 class="nirvana-footer-title">Nirvana II</h4>
          <p style="color: #d4d4d8; font-size: 0.95rem; margin-bottom: 16px;">
            Authentic North and South Indian culinary mastery in the heart of Uptown Charlotte. Fragrant dum biryanis, slow-simmered curries, tandoori specialties, and executive lunch thalis.
          </p>
          <span class="nirvana-badge nirvana-badge-teal">Fast-Casual Corporate Lunch</span>
        </div>
        <div>
          <h4 class="nirvana-footer-title">Showcase Navigation</h4>
          <ul class="nirvana-footer-links">
            <li><a href="index.html" class="nirvana-footer-link">Home & Overview</a></li>
            <li><a href="menu.html" class="nirvana-footer-link">Full Indian Menu</a></li>
            <li><a href="signature-biryanis-and-thali-combos.html" class="nirvana-footer-link">Dum Biryanis & Thali Boxes</a></li>
            <li><a href="tandoori-curries-and-vegetarian-classics.html" class="nirvana-footer-link">Curries & Tandoori Classics</a></li>
            <li><a href="corporate-catering-and-lunch-boxes.html" class="nirvana-footer-link">Corporate Catering Trays</a></li>
            <li><a href="visit.html" class="nirvana-footer-link">Location & Pickup Details</a></li>
          </ul>
        </div>
        <div>
          <h4 class="nirvana-footer-title">Location & Hours</h4>
          <div class="nirvana-footer-contact-item">
            <strong>Address</strong>
            401 S Tryon St<br>
            Uptown Charlotte, NC 28202
          </div>
          <div class="nirvana-footer-contact-item">
            <strong>Operating Hours</strong>
            Monday &ndash; Friday: 11:30 AM &ndash; 3:30 PM<br>
            Saturday &ndash; Sunday: Closed
          </div>
        </div>
        <div>
          <h4 class="nirvana-footer-title">Direct Orders & Pickup</h4>
          <div class="nirvana-footer-contact-item">
            <strong>Direct Phone Line</strong>
            <a href="tel:9802907002" style="color: #fde68a; text-decoration: none; font-weight: 700;">(980) 290-7002</a>
          </div>
          <div class="nirvana-footer-contact-item">
            <strong>Online Takeout & Delivery</strong>
            <span>Available on major ordering platforms or call ahead for direct lobby express pickup.</span>
          </div>
        </div>
      </div>
      <div class="nirvana-footer-bottom">
        <p>&copy; 2026 Nirvana II / Nirvana Indian Fusion. Proudly serving Uptown Charlotte. Showcase demo created with zero emojis.</p>
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
  <title>{title} | Nirvana II Indian Fusion Uptown Charlotte</title>
  <meta name="description" content="Nirvana II at 401 S Tryon St, Uptown Charlotte. Authentic dum biryanis, butter chicken, thali lunch combos, samosas, and corporate catering.">
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
