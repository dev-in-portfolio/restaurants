
def nav_html(active_file):
    links = [
        ("index.html", "Home"),
        ("menu.html", "Full Menu"),
        ("ropa-vieja-and-lechon-asado.html", "Meats & Pernil"),
        ("mofongo-and-caribbean-specialties.html", "Mofongo & Seafood"),
        ("family-catering-and-platters.html", "Party Platters"),
        ("visit.html", "Visit & Hours")
    ]
    html = '<nav class="caridad-nav-links" id="main-nav">\n'
    for file, label in links:
        active_cls = ' class="active"' if file == active_file else ''
        html += f'          <a href="{file}"{active_cls}>{label}</a>\n'
    html += '          <a href="tel:7045378890" class="caridad-btn-cta">Call (704) 537-8890</a>\n        </nav>'
    return html

def header_html(active_file):
    return f'''  <header class="caridad-header">
    <div class="caridad-topbar">
      <span>Authentic Dominican & Cuban Kitchen | 4421 N Sharon Amity Rd, Charlotte, NC</span>
      <span>Call for Takeout & Catering: <a href="tel:7045378890">(704) 537-8890</a></span>
    </div>
    <div class="caridad-nav-container">
      <a href="index.html" class="caridad-logo-group">
        <span class="caridad-logo-badge">LC</span>
        <div>
          <span class="caridad-logo-text">La Caridad</span>
          <span class="caridad-logo-sub">Cocina Latina Charlotte</span>
        </div>
      </a>
      <button class="caridad-mobile-toggle" aria-controls="main-nav" aria-expanded="false" aria-label="Toggle navigation menu">Menu</button>
      {nav_html(active_file)}
    </div>
  </header>'''

def footer_html():
    return '''  <footer class="caridad-footer">
    <div class="caridad-footer-grid">
      <div class="caridad-footer-col">
        <h4 class="caridad-brand-title">La Caridad Cocina Latina</h4>
        <p>Bringing authentic Caribbean homestyle flavors to East Charlotte. From slow-roasted pernil asado and shredded ropa vieja to plantain mofongo and golden empanadas.</p>
        <p><strong>Dine-In | Takeout | Catering Trays</strong></p>
      </div>
      <div class="caridad-footer-col">
        <h4>Navigation</h4>
        <ul class="caridad-footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Full Menu</a></li>
          <li><a href="ropa-vieja-and-lechon-asado.html">Meats & Pernil</a></li>
          <li><a href="mofongo-and-caribbean-specialties.html">Mofongo & Seafood</a></li>
          <li><a href="family-catering-and-platters.html">Party Platters</a></li>
          <li><a href="visit.html">Visit & Hours</a></li>
        </ul>
      </div>
      <div class="caridad-footer-col">
        <h4>Hours of Operation</h4>
        <ul class="caridad-footer-links">
          <li>Monday - Thursday: 10:00 AM - 8:30 PM</li>
          <li>Friday - Saturday: 10:00 AM - 9:30 PM</li>
          <li>Sunday: 11:00 AM - 7:30 PM</li>
        </ul>
      </div>
      <div class="caridad-footer-col">
        <h4>Contact & Location</h4>
        <p>4421 N Sharon Amity Rd<br>Charlotte, NC 28205</p>
        <p>Phone: <a href="tel:7045378890" style="color:#fef08a;">(704) 537-8890</a></p>
        <p>Email: <a href="mailto:info@lacaridadcharlotte.com" style="color:#fef08a;">info@lacaridadcharlotte.com</a></p>
      </div>
    </div>
    <div class="caridad-footer-bottom">
      <p>&copy; 2026 La Caridad Cocina Latina. All rights reserved. Charlotte, North Carolina.</p>
    </div>
  </footer>
  <script src="site.js"></script>
</body>
</html>'''
