
def nav_html(active_file):
    links = [
        ("index.html", "Home"),
        ("menu.html", "Full Menu"),
        ("nicaraguan-vigoron-and-nacatamales.html", "Nica Heritage"),
        ("guatemalan-pepian-and-hilachas.html", "Chapin Kitchen"),
        ("central-american-catering-and-events.html", "Feasts & Catering"),
        ("visit.html", "Visit & Hours")
    ]
    html = '<nav class="nicachapin-nav-links" id="main-nav">\n'
    for file, label in links:
        active_cls = ' class="active"' if file == active_file else ''
        html += f'          <a href="{file}"{active_cls}>{label}</a>\n'
    html += '          <a href="tel:7045688889" class="nicachapin-btn-cta">Call (704) 568-8889</a>\n        </nav>'
    return html

def header_html(active_file):
    return f'''  <header class="nicachapin-header">
    <div class="nicachapin-topbar">
      <span>Authentic Nicaraguan & Guatemalan Kitchen | 4833 Central Ave, Charlotte, NC</span>
      <span>Call for Takeout & Catering: <a href="tel:7045688889">(704) 568-8889</a></span>
    </div>
    <div class="nicachapin-nav-container">
      <a href="index.html" class="nicachapin-logo-group">
        <span class="nicachapin-logo-badge">NC</span>
        <div>
          <span class="nicachapin-logo-text">Nica Chapin</span>
          <span class="nicachapin-logo-sub">Tradicion Centroamericana</span>
        </div>
      </a>
      <button class="nicachapin-mobile-toggle" aria-controls="main-nav" aria-expanded="false" aria-label="Toggle navigation menu">Menu</button>
      {nav_html(active_file)}
    </div>
  </header>'''

def footer_html():
    return '''  <footer class="nicachapin-footer">
    <div class="nicachapin-footer-grid">
      <div class="nicachapin-footer-col">
        <h4 class="nicachapin-brand-title">Nica Chapin</h4>
        <p>Celebrating the culinary bridge between Nicaragua and Guatemala on Central Avenue in Charlotte. From banana-leaf steamed nacatamales and crispy vigoron to Mayan pepian and handmade garnachas.</p>
        <p><strong>Dine-In | Takeout | Party Catering Pans</strong></p>
      </div>
      <div class="nicachapin-footer-col">
        <h4>Navigation</h4>
        <ul class="nicachapin-footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Full Menu</a></li>
          <li><a href="nicaraguan-vigoron-and-nacatamales.html">Nica Heritage</a></li>
          <li><a href="guatemalan-pepian-and-hilachas.html">Chapin Kitchen</a></li>
          <li><a href="central-american-catering-and-events.html">Feasts & Catering</a></li>
          <li><a href="visit.html">Visit & Hours</a></li>
        </ul>
      </div>
      <div class="nicachapin-footer-col">
        <h4>Hours of Operation</h4>
        <ul class="nicachapin-footer-links">
          <li>Tuesday - Thursday: 10:00 AM - 8:30 PM</li>
          <li>Friday - Saturday: 9:00 AM - 9:30 PM</li>
          <li>Sunday: 9:00 AM - 8:00 PM</li>
          <li>Monday: Closed</li>
        </ul>
      </div>
      <div class="nicachapin-footer-col">
        <h4>Contact & Location</h4>
        <p>4833 Central Ave<br>Charlotte, NC 28205</p>
        <p>Phone: <a href="tel:7045688889" style="color:#fef08a;">(704) 568-8889</a></p>
        <p>Email: <a href="mailto:info@nicachapinclt.com" style="color:#fef08a;">info@nicachapinclt.com</a></p>
      </div>
    </div>
    <div class="nicachapin-footer-bottom">
      <p>&copy; 2026 Nica Chapin. All rights reserved. Charlotte, North Carolina.</p>
    </div>
  </footer>
  <script src="site.js"></script>
</body>
</html>'''
