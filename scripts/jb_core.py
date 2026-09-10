import os

os.makedirs("johnny-burrito", exist_ok=True)

nav_links = [
    ("Home", "index.html"),
    ("Full Menu", "menu.html"),
    ("Burritos & Bowls", "famous-burritos-and-bowls.html"),
    ("Tamale Tradition", "tuesday-friday-tamale-tradition.html"),
    ("Salsas & Catering", "salsa-bar-and-concourse-catering.html"),
    ("Visit & Concourse", "visit.html")
]

def render_nav(active_page):
    links_html = ""
    for label, url in nav_links:
        active_cls = ' active' if url == active_page else ''
        links_html += f'<li><a href="{url}" class="jb-nav-link{active_cls}">{label}</a></li>\n'
    return f"""
  <div class="jb-announcement">
    <span>Uptown Charlotte Concourse Legend Since 1998 &bull; Open Mon-Fri 11am-3pm &bull; Tamales Every Tuesday & Friday!</span>
    <a href="visit.html">Find Down Escalators &rarr;</a>
  </div>
  <header class="jb-navbar">
    <div class="jb-nav-container">
      <a href="index.html" class="jb-brand">
        <span class="jb-brand-name">Johnny Burrito</span>
        <span class="jb-brand-tagline">Two Wells Fargo Concourse &bull; Charlotte NC</span>
      </a>
      <button class="jb-mobile-toggle" aria-label="Toggle navigation menu">&#9776;</button>
      <ul class="jb-nav-links">
        {links_html}
        <li><a href="tel:7043714448" class="jb-nav-link jb-nav-cta">Call (704) 371-4448</a></li>
      </ul>
    </div>
  </header>
"""

def render_footer():
    return """
  <footer class="jb-footer">
    <div class="jb-container">
      <div class="jb-footer-grid">
        <div>
          <h4 class="jb-footer-title">Johnny Burrito</h4>
          <p style="color: #cbd5e1; font-size: 0.95rem; margin-bottom: 16px;">
            Charlotte's subterranean burrito institution since 1998. Fast-casual California burritos, crispy nacho salads, scratch salsas, and famous Tuesday & Friday homemade tamales.
          </p>
          <span class="jb-badge jb-badge-lime">Cash-Eesh Discount Accepted</span>
        </div>
        <div>
          <h4 class="jb-footer-title">Showcase Navigation</h4>
          <ul class="jb-footer-links">
            <li><a href="index.html" class="jb-footer-link">Home & Overview</a></li>
            <li><a href="menu.html" class="jb-footer-link">Concourse Walk-The-Line Menu</a></li>
            <li><a href="famous-burritos-and-bowls.html" class="jb-footer-link">Burritos & Nacho Bowls</a></li>
            <li><a href="tuesday-friday-tamale-tradition.html" class="jb-footer-link">Tuesday & Friday Tamales</a></li>
            <li><a href="salsa-bar-and-concourse-catering.html" class="jb-footer-link">Salsa Bar & Corporate Catering</a></li>
            <li><a href="visit.html" class="jb-footer-link">Two Wells Fargo Escalator Guide</a></li>
          </ul>
        </div>
        <div>
          <h4 class="jb-footer-title">Concourse Location & Hours</h4>
          <div class="jb-footer-contact-item">
            <strong>Address</strong>
            301 S Tryon St, Concourse Level<br>
            (Under Two Wells Fargo Atrium)<br>
            Charlotte, NC 28202
          </div>
          <div class="jb-footer-contact-item">
            <strong>Hours of Operation</strong>
            Monday &ndash; Friday: 11:00 AM &ndash; 3:00 PM<br>
            Saturday &ndash; Sunday: Closed
          </div>
        </div>
        <div>
          <h4 class="jb-footer-title">Direct Orders</h4>
          <div class="jb-footer-contact-item">
            <strong>Phone Call Ahead</strong>
            <a href="tel:7043714448" style="color: #fed7aa; text-decoration: none; font-weight: 700;">(704) 371-4448</a>
          </div>
          <div class="jb-footer-contact-item">
            <strong>Fax Orders</strong>
            <span>(704) 371-4449</span><br>
            <small style="color: #94a3b8;">(No fax orders accepted 10:45 AM &ndash; 1:30 PM)</small>
          </div>
          <div class="jb-footer-contact-item">
            <strong>Payment Perks</strong>
            <span>Ask for the Cash-Eesh direct cash discount at checkout!</span>
          </div>
        </div>
      </div>
      <div class="jb-footer-bottom">
        <p>&copy; 2026 Johnny Burrito. Proudly serving Uptown Charlotte since 1998. Showcase demo created with zero emojis.</p>
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
  <title>{title} | Johnny Burrito Uptown Charlotte</title>
  <meta name="description" content="Johnny Burrito in Two Wells Fargo Concourse, Uptown Charlotte. Famous customizable burritos, Tuesday/Friday tamales, scratch salsa bar, and fast-casual lunch since 1998.">
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
