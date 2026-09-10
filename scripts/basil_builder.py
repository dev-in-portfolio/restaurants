# -*- coding: utf-8 -*-

def nav_html(active_file):
    links = [
        ("index.html", "Home"),
        ("menu.html", "Full Menu"),
        ("chef-specialties-and-curries.html", "Chef Curries &amp; Duck"),
        ("wok-noodles-and-street-fare.html", "Wok &amp; Noodles"),
        ("executive-lunch-and-catering.html", "Lunch &amp; Catering"),
        ("visit.html", "Visit &amp; Hours")
    ]
    html = '<nav class="basil-nav-links" id="main-nav">\n'
    for file, label in links:
        active_cls = ' class="active"' if file == active_file else ''
        html += f'          <a href="{file}"{active_cls}>{label}</a>\n'
    html += '          <a href="tel:7043327212" class="basil-nav-btn">Call (704) 332-7212</a>\n        </nav>'
    return html

def header_html(active_file):
    return f'''  <header class="basil-header">
    <div class="basil-topbar">
      <span>Contemporary Thai Cuisine | 210 N Church St, Uptown Charlotte</span>
      <span>Lunch &amp; Dinner Reservations: <a href="tel:7043327212">(704) 332-7212</a></span>
    </div>
    <div class="basil-nav-container">
      <a href="index.html" class="basil-logo-group">
        <span class="basil-logo-badge">BT</span>
        <div>
          <span class="basil-logo-title">Basil Thai Cuisine</span>
          <span class="basil-logo-sub">Contemporary Thai &amp; Bar</span>
        </div>
      </a>
      <button class="basil-mobile-toggle" aria-controls="main-nav" aria-expanded="false" aria-label="Toggle navigation menu">Menu</button>
      {nav_html(active_file)}
    </div>
  </header>'''

def footer_html():
    return '''  <footer class="basil-footer">
    <div class="basil-footer-grid">
      <div>
        <h4 style="color:#fbbf24;">Basil Thai Cuisine</h4>
        <p>Uptown Charlotte's distinguished venue for modern Thai cuisine, scratch-crafted coconut curries, artisanal wok noodles, signature Crispy Basil Duck, and an upscale cocktail lounge.</p>
        <p style="margin-top:12px;"><strong>210 N Church St | Fourth Ward Corridor | Charlotte, NC</strong></p>
      </div>
      <div>
        <h4>Menu &amp; Highlights</h4>
        <ul class="basil-footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Full Menu</a></li>
          <li><a href="chef-specialties-and-curries.html">Chef Curries &amp; Duck</a></li>
          <li><a href="wok-noodles-and-street-fare.html">Wok &amp; Street Noodles</a></li>
          <li><a href="executive-lunch-and-catering.html">Executive Lunch &amp; Catering</a></li>
          <li><a href="visit.html">Visit &amp; Hours</a></li>
        </ul>
      </div>
      <div>
        <h4>Dining Hours</h4>
        <ul class="basil-footer-links">
          <li><strong>Lunch:</strong> Mon - Thu: 11:30 AM - 2:00 PM</li>
          <li><strong>Dinner:</strong> Mon - Sun: 5:00 PM - 9:00 PM</li>
          <li>Full Bar &amp; Carryout Available Daily</li>
        </ul>
      </div>
      <div>
        <h4>Location &amp; Contact</h4>
        <p>210 N Church St<br>Charlotte, NC 28202</p>
        <p style="margin-top:8px;">Phone: <a href="tel:7043327212" style="color:#fbbf24; font-weight:700;">(704) 332-7212</a></p>
        <p>Email: <a href="mailto:info@eatatbasil.com" style="color:#fbbf24;">info@eatatbasil.com</a></p>
      </div>
    </div>
    <div class="basil-footer-bottom">
      <p>&copy; 2026 Basil Thai Cuisine. All rights reserved. Uptown Charlotte, North Carolina.</p>
    </div>
  </footer>
  <script src="site.js"></script>
</body>
</html>'''
