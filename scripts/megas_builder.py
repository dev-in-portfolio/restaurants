
def nav_html(active_file):
    links = [
        ("index.html", "Home"),
        ("menu.html", "Full Menu"),
        ("tortas-gigantes-and-cubana.html", "Tortas Gigantes"),
        ("tacos-al-pastor-and-trompo.html", "Tacos & Trompo"),
        ("torta-builder-and-catering.html", "Party Boxes"),
        ("visit.html", "Visit & Hours")
    ]
    html = '<nav class="megas-nav-links" id="main-nav">\n'
    for file, label in links:
        active_cls = ' class="active"' if file == active_file else ''
        html += f'          <a href="{file}"{active_cls}>{label}</a>\n'
    html += '          <a href="tel:7045272285" class="megas-btn-cta">Call (704) 527-2285</a>\n        </nav>'
    return html

def header_html(active_file):
    return f'''  <header class="megas-header">
    <div class="megas-topbar">
      <span>Mexico City Style Tortas Gigantes & Tacos al Pastor | 4835 South Blvd, Charlotte, NC</span>
      <span>Call for Fast Takeout: <a href="tel:7045272285">(704) 527-2285</a></span>
    </div>
    <div class="megas-nav-container">
      <a href="index.html" class="megas-logo-group">
        <span class="megas-logo-badge">MT</span>
        <div>
          <span class="megas-logo-text">Las Megas Tortas</span>
          <span class="megas-logo-sub">Autentico Sabor Chilango</span>
        </div>
      </a>
      <button class="megas-mobile-toggle" aria-controls="main-nav" aria-expanded="false" aria-label="Toggle navigation menu">Menu</button>
      {nav_html(active_file)}
    </div>
  </header>'''

def footer_html():
    return '''  <footer class="megas-footer">
    <div class="megas-footer-grid">
      <div class="megas-footer-col">
        <h4 class="megas-brand-title">Las Megas Tortas</h4>
        <p>Charlotte's authentic Mexico City street sandwich epicenter. Loaded 10-inch toasted teleras, vertical trompo Al Pastor with roasted pineapple, handmade huaraches, and fresh aguas frescas.</p>
        <p><strong>Dine-In | Takeout Orders | Party Bundles</strong></p>
      </div>
      <div class="megas-footer-col">
        <h4>Navigation</h4>
        <ul class="megas-footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Full Menu</a></li>
          <li><a href="tortas-gigantes-and-cubana.html">Tortas Gigantes</a></li>
          <li><a href="tacos-al-pastor-and-trompo.html">Tacos & Trompo</a></li>
          <li><a href="torta-builder-and-catering.html">Party Boxes</a></li>
          <li><a href="visit.html">Visit & Hours</a></li>
        </ul>
      </div>
      <div class="megas-footer-col">
        <h4>Weekly Hours</h4>
        <ul class="megas-footer-links">
          <li>Monday - Thursday: 10:00 AM - 10:00 PM</li>
          <li>Friday - Saturday: 10:00 AM - 11:30 PM</li>
          <li>Sunday: 10:00 AM - 9:30 PM</li>
        </ul>
      </div>
      <div class="megas-footer-col">
        <h4>Contact & Location</h4>
        <p>4835 South Blvd<br>Charlotte, NC 28217</p>
        <p>Phone: <a href="tel:7045272285" style="color:var(--megas-gold);">(704) 527-2285</a></p>
        <p>Email: <a href="mailto:contacto@lasmegastortasclt.com" style="color:var(--megas-gold);">contacto@lasmegastortasclt.com</a></p>
      </div>
    </div>
    <div class="megas-footer-bottom">
      <p>&copy; 2026 Las Megas Tortas. All rights reserved. Charlotte, North Carolina.</p>
    </div>
  </footer>
  <script src="site.js"></script>
</body>
</html>'''
