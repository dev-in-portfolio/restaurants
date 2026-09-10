# -*- coding: utf-8 -*-

def nav_html(active_file):
    links = [
        ("index.html", "Home"),
        ("menu.html", "Full Menu"),
        ("scandinavian-pub-fare-and-meatballs.html", "Nordic Comfort"),
        ("brevard-court-patio-and-taproom.html", "Brevard Patio"),
        ("feast-platters-and-gameday-packages.html", "Feast Platters"),
        ("visit.html", "Visit &amp; Hours")
    ]
    html = '<nav class="valhalla-nav-links" id="main-nav">\n'
    for file, label in links:
        active_cls = ' class="active"' if file == active_file else ''
        html += f'          <a href="{file}"{active_cls}>{label}</a>\n'
    html += '          <a href="tel:7043323273" class="valhalla-btn-cta">Call (704) 332-3273</a>\n        </nav>'
    return html

def header_html(active_file):
    return f'''  <header class="valhalla-header">
    <div class="valhalla-topbar">
      <span>Viking &amp; Scandinavian Pub | Historic Brevard Court, 317 S Church St</span>
      <span>Patio &amp; Takeout Counter: <a href="tel:7043323273">(704) 332-3273</a></span>
    </div>
    <div class="valhalla-nav-container">
      <a href="index.html" class="valhalla-logo-group">
        <span class="valhalla-logo-badge">VP</span>
        <div>
          <span class="valhalla-logo-text">Valhalla Pub</span>
          <span class="valhalla-logo-sub">Scandinavian Eatery &amp; Taproom</span>
        </div>
      </a>
      <button class="valhalla-mobile-toggle" aria-controls="main-nav" aria-expanded="false" aria-label="Toggle navigation menu">Menu</button>
      {nav_html(active_file)}
    </div>
  </header>'''

def footer_html():
    return '''  <footer class="valhalla-footer">
    <div class="valhalla-footer-grid">
      <div class="valhalla-footer-col">
        <h4 class="valhalla-brand-title">Valhalla Pub &amp; Eatery</h4>
        <p>Uptown Charlotte's Scandinavian-inspired Viking tavern in historic Brevard Court. Scratch-made Norwegian meatballs, custom Viking blend burgers, craft Carolina beers on tap, and lively courtyard patio dining.</p>
        <p><strong>Nordic Scratch Kitchen | 10 Rotating Craft Taps | Brevard Court Patio</strong></p>
      </div>
      <div class="valhalla-footer-col">
        <h4>Navigation</h4>
        <ul class="valhalla-footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Full Menu</a></li>
          <li><a href="scandinavian-pub-fare-and-meatballs.html">Nordic Comfort</a></li>
          <li><a href="brevard-court-patio-and-taproom.html">Brevard Court Patio</a></li>
          <li><a href="feast-platters-and-gameday-packages.html">Feast Platters</a></li>
          <li><a href="visit.html">Visit &amp; Hours</a></li>
        </ul>
      </div>
      <div class="valhalla-footer-col">
        <h4>Pub &amp; Kitchen Hours</h4>
        <ul class="valhalla-footer-links">
          <li>Monday - Thursday: 11:00 AM - 11:00 PM</li>
          <li>Friday - Saturday: 11:00 AM - 12:00 AM</li>
          <li>Sunday: 10:00 AM - 10:00 PM (Brunch &amp; Game Watch)</li>
          <li>Kitchen closes 1 hour before bar</li>
        </ul>
      </div>
      <div class="valhalla-footer-col">
        <h4>Contact &amp; Location</h4>
        <p>317 S Church St (Brevard Court)<br>Charlotte, NC 28202</p>
        <p>Phone: <a href="tel:7043323273" style="color:#fef08a;">(704) 332-3273</a></p>
        <p>Email: <a href="mailto:contact@valhallapub.com" style="color:#fef08a;">contact@valhallapub.com</a></p>
      </div>
    </div>
    <div class="valhalla-footer-bottom">
      <p>&copy; 2026 Valhalla Pub &amp; Eatery. All rights reserved. Uptown Charlotte, North Carolina.</p>
    </div>
  </footer>
  <script src="site.js"></script>
</body>
</html>'''
