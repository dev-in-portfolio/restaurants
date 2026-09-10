# -*- coding: utf-8 -*-

def nav_html(active_file):
    links = [
        ("index.html", "Home"),
        ("menu.html", "Full Menu"),
        ("signature-rolls-and-sashimi-lounge.html", "Sushi Lounge"),
        ("modern-asian-bistro-and-wok.html", "Bistro Wok"),
        ("sushi-platters-and-executive-dining.html", "Platters &amp; Events"),
        ("visit.html", "Visit &amp; Hours")
    ]
    html = '<nav class="room112-nav-links" id="main-nav">\n'
    for file, label in links:
        active_cls = ' class="active"' if file == active_file else ''
        html += f'          <a href="{file}"{active_cls}>{label}</a>\n'
    html += '          <a href="tel:7043357112" class="room112-btn-cta">Call (704) 335-7112</a>\n        </nav>'
    return html

def header_html(active_file):
    return f'''  <header class="room112-header">
    <div class="room112-topbar">
      <span>Chic Modern Asian Bistro &amp; Sushi Lounge | 112 S Tryon St, Uptown Charlotte</span>
      <span>Lunch &amp; Evening Orders: <a href="tel:7043357112">(704) 335-7112</a></span>
    </div>
    <div class="room112-nav-container">
      <a href="index.html" class="room112-logo-group">
        <span class="room112-logo-badge">112</span>
        <div>
          <span class="room112-logo-text">Room 112</span>
          <span class="room112-logo-sub">Modern Asian Bistro &amp; Sushi</span>
        </div>
      </a>
      <button class="room112-mobile-toggle" aria-controls="main-nav" aria-expanded="false" aria-label="Toggle navigation menu">Menu</button>
      {nav_html(active_file)}
    </div>
  </header>'''

def footer_html():
    return '''  <footer class="room112-footer">
    <div class="room112-footer-grid">
      <div class="room112-footer-col">
        <h4 class="room112-brand-title">Room 112</h4>
        <p>Uptown Charlotte's intimate boutique Asian bistro on South Tryon Street. Creative signature maki rolls, 112 Deluxe sushi platters, honey walnut prawns, crispy tangerine beef, and craft cocktails.</p>
        <p><strong>Boutique Sushi Lounge | Elevated Wok Cuisine | Corporate Platters</strong></p>
      </div>
      <div class="room112-footer-col">
        <h4>Navigation</h4>
        <ul class="room112-footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Full Menu</a></li>
          <li><a href="signature-rolls-and-sashimi-lounge.html">Sushi Lounge</a></li>
          <li><a href="modern-asian-bistro-and-wok.html">Bistro Wok</a></li>
          <li><a href="sushi-platters-and-executive-dining.html">Platters &amp; Events</a></li>
          <li><a href="visit.html">Visit &amp; Hours</a></li>
        </ul>
      </div>
      <div class="room112-footer-col">
        <h4>Operating Hours</h4>
        <ul class="room112-footer-links">
          <li>Monday - Friday: 11:00 AM - 9:00 PM</li>
          <li>Saturday: 11:30 AM - 9:00 PM</li>
          <li>Sunday: Closed (Available for Private Lounge Buyouts)</li>
          <li>Uptown Express Lunch &amp; Evening Dining</li>
        </ul>
      </div>
      <div class="room112-footer-col">
        <h4>Contact &amp; Location</h4>
        <p>112 S Tryon St<br>Charlotte, NC 28284</p>
        <p>Phone: <a href="tel:7043357112" style="color:#f5d0fe;">(704) 335-7112</a></p>
        <p>Email: <a href="mailto:contact@rm112.com" style="color:#f5d0fe;">contact@rm112.com</a></p>
      </div>
    </div>
    <div class="room112-footer-bottom">
      <p>&copy; 2026 Room 112. All rights reserved. Uptown Charlotte, North Carolina.</p>
    </div>
  </footer>
  <script src="site.js"></script>
</body>
</html>'''
