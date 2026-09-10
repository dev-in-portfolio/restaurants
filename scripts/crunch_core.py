import os

os.makedirs("crunch-bistro", exist_ok=True)

nav_links = [
    ("Home", "index.html"),
    ("Full Menu", "menu.html"),
    ("Salads & Grain Bowls", "signature-chopped-salads-and-warm-bowls.html"),
    ("Flatbreads & Wraps", "artisan-lavash-flatbreads-and-wraps.html"),
    ("Acai & Catering", "superfruit-acai-and-corporate-catering.html"),
    ("Visit & Location", "visit.html")
]

def render_nav(active_page):
    links_html = ""
    for label, url in nav_links:
        active_cls = ' active' if url == active_page else ''
        links_html += f'<li><a href="{url}" class="crunch-nav-link{active_cls}">{label}</a></li>\n'
    return f"""
  <div class="crunch-announcement">
    <span>Uptown Charlotte's Fresh Health & Wellness Kitchen &bull; Open Mon-Fri 10am-3:30pm &bull; Chopped Salads & Grain Bowls!</span>
    <a href="visit.html">Find 401 N Tryon St &rarr;</a>
  </div>
  <header class="crunch-navbar">
    <div class="crunch-nav-container">
      <a href="index.html" class="crunch-brand">
        <span class="crunch-brand-name">Crunch<span>Bistro</span></span>
        <span class="crunch-brand-tagline">401 N Tryon St &bull; Uptown Charlotte</span>
      </a>
      <button class="crunch-mobile-toggle" aria-label="Toggle navigation menu">&#9776;</button>
      <ul class="crunch-nav-links">
        {links_html}
        <li><a href="tel:9804985774" class="crunch-nav-link crunch-nav-cta">Call (980) 498-5774</a></li>
      </ul>
    </div>
  </header>
"""

def render_footer():
    return """
  <footer class="crunch-footer">
    <div class="crunch-container">
      <div class="crunch-footer-grid">
        <div>
          <h4 class="crunch-footer-title">Crunch Bistro</h4>
          <p style="color: #cbd5e1; font-size: 0.95rem; margin-bottom: 16px;">
            Clean, nutritious, chef-crafted fast-casual dining in Uptown Charlotte. Custom chopped salads, warm tricolor quinoa grain bowls, crispy lavash flatbreads, and organic superfruit açaí bowls.
          </p>
          <span class="crunch-badge crunch-badge-lime">Corporate Wellness Partner</span>
        </div>
        <div>
          <h4 class="crunch-footer-title">Showcase Navigation</h4>
          <ul class="crunch-footer-links">
            <li><a href="index.html" class="crunch-footer-link">Home & Overview</a></li>
            <li><a href="menu.html" class="crunch-footer-link">Full Wellness Menu</a></li>
            <li><a href="signature-chopped-salads-and-warm-bowls.html" class="crunch-footer-link">Chopped Salads & Grain Bowls</a></li>
            <li><a href="artisan-lavash-flatbreads-and-wraps.html" class="crunch-footer-link">Lavash Flatbreads & Wraps</a></li>
            <li><a href="superfruit-acai-and-corporate-catering.html" class="crunch-footer-link">Açaí Bowls & Office Catering</a></li>
            <li><a href="visit.html" class="crunch-footer-link">401 N Tryon Location</a></li>
          </ul>
        </div>
        <div>
          <h4 class="crunch-footer-title">Location & Hours</h4>
          <div class="crunch-footer-contact-item">
            <strong>Address</strong>
            401 N Tryon St<br>
            Uptown Charlotte, NC 28202
          </div>
          <div class="crunch-footer-contact-item">
            <strong>Operating Hours</strong>
            Monday &ndash; Friday: 10:00 AM &ndash; 3:30 PM<br>
            Saturday &ndash; Sunday: Closed
          </div>
        </div>
        <div>
          <h4 class="crunch-footer-title">Direct Orders & Catering</h4>
          <div class="crunch-footer-contact-item">
            <strong>Call-Ahead Line</strong>
            <a href="tel:9804985774" style="color: #a7f3d0; text-decoration: none; font-weight: 700;">(980) 498-5774</a>
          </div>
          <div class="crunch-footer-contact-item">
            <strong>Online Takeout & Delivery</strong>
            <span>Order through crunchbistro.com or Toast for quick lobby pickup and Uptown office delivery.</span>
          </div>
        </div>
      </div>
      <div class="crunch-footer-bottom">
        <p>&copy; 2026 Crunch Bistro. Clean eating for Uptown Charlotte. Showcase demo created with zero emojis.</p>
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
  <title>{title} | Crunch Bistro Uptown Charlotte</title>
  <meta name="description" content="Crunch Bistro at 401 N Tryon St, Uptown Charlotte. Signature chopped salads, warm quinoa grain bowls, lavash flatbreads, organic acai, and corporate wellness catering.">
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
