import os

os.makedirs("the-sandwich-club", exist_ok=True)

nav_links = [
    ("Home", "index.html"),
    ("Full Menu", "menu.html"),
    ("Clubs & Melts", "triple-decker-clubs-and-gourmet-melts.html"),
    ("Breakfast & Biscuits", "morning-breakfast-and-biscuit-bar.html"),
    ("Corporate Catering", "corporate-lunch-boxes-and-platters.html"),
    ("Visit & Location", "visit.html")
]

def render_nav(active_page):
    links_html = ""
    for label, url in nav_links:
        active_cls = ' active' if url == active_page else ''
        links_html += f'<li><a href="{url}" class="tsc-nav-link{active_cls}">{label}</a></li>\n'
    return f"""
  <div class="tsc-announcement">
    <span>Uptown Charlotte's 30+ Signature Sandwich Landmark &bull; Open Mon-Fri 7am-3pm &bull; Breakfast Biscuits & Boxed Lunches!</span>
    <a href="visit.html">Find 435 S Tryon St &rarr;</a>
  </div>
  <header class="tsc-navbar">
    <div class="tsc-nav-container">
      <a href="index.html" class="tsc-brand">
        <span class="tsc-brand-name">The Sandwich Club</span>
        <span class="tsc-brand-tagline">435 S Tryon St &bull; Uptown Charlotte</span>
      </a>
      <button class="tsc-mobile-toggle" aria-label="Toggle navigation menu">&#9776;</button>
      <ul class="tsc-nav-links">
        {links_html}
        <li><a href="tel:7043441975" class="tsc-nav-link tsc-nav-cta">Call (704) 344-1975</a></li>
      </ul>
    </div>
  </header>
"""

def render_footer():
    return """
  <footer class="tsc-footer">
    <div class="tsc-container">
      <div class="tsc-footer-grid">
        <div>
          <h4 class="tsc-footer-title">The Sandwich Club</h4>
          <p style="color: #d6d3d1; font-size: 0.95rem; margin-bottom: 16px;">
            Charlotte's independent deli institution on S Tryon Street since 1993. Over 30 signature handcrafted sandwiches, triple-decker clubs, croissant melts, and early morning breakfast biscuits.
          </p>
          <span class="tsc-badge tsc-badge-green">Local Uptown Legend</span>
        </div>
        <div>
          <h4 class="tsc-footer-title">Showcase Navigation</h4>
          <ul class="tsc-footer-links">
            <li><a href="index.html" class="tsc-footer-link">Home & Overview</a></li>
            <li><a href="menu.html" class="tsc-footer-link">Full Deli & Breakfast Menu</a></li>
            <li><a href="triple-decker-clubs-and-gourmet-melts.html" class="tsc-footer-link">Triple-Decker Clubs & Melts</a></li>
            <li><a href="morning-breakfast-and-biscuit-bar.html" class="tsc-footer-link">Morning Breakfast Bar</a></li>
            <li><a href="corporate-lunch-boxes-and-platters.html" class="tsc-footer-link">Corporate Boxed Lunches</a></li>
            <li><a href="visit.html" class="tsc-footer-link">Location Across From The Green</a></li>
          </ul>
        </div>
        <div>
          <h4 class="tsc-footer-title">Location & Hours</h4>
          <div class="tsc-footer-contact-item">
            <strong>Address</strong>
            435 S Tryon St<br>
            (Across from The Green & Ratcliffe)<br>
            Charlotte, NC 28202
          </div>
          <div class="tsc-footer-contact-item">
            <strong>Operating Hours</strong>
            Monday &ndash; Friday: 7:00 AM &ndash; 3:00 PM<br>
            Saturday &ndash; Sunday: Closed
          </div>
        </div>
        <div>
          <h4 class="tsc-footer-title">Direct Orders & Catering</h4>
          <div class="tsc-footer-contact-item">
            <strong>Call-Ahead Phone Line</strong>
            <a href="tel:7043441975" style="color: #fed7aa; text-decoration: none; font-weight: 700;">(704) 344-1975</a>
          </div>
          <div class="tsc-footer-contact-item">
            <strong>Online Ordering & Pickup</strong>
            <span>Order through sandwichclub2go.com or call ahead for swift counter pickup.</span>
          </div>
        </div>
      </div>
      <div class="tsc-footer-bottom">
        <p>&copy; 2026 The Sandwich Club. Proudly fueling Uptown Charlotte since 1993. Showcase demo created with zero emojis.</p>
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
  <title>{title} | The Sandwich Club Uptown Charlotte</title>
  <meta name="description" content="The Sandwich Club at 435 S Tryon St, Uptown Charlotte. Over 30 signature sandwiches, triple-decker clubs, Grand Brie croissant melt, scratch breakfast, and corporate catering.">
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
