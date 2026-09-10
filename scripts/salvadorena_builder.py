# -*- coding: utf-8 -*-

def nav_html(active_file):
    links = [
        ("index.html", "Home"),
        ("menu.html", "Full Menu"),
        ("pupusas-artesanales-and-curtido.html", "Pupuseria"),
        ("panaderia-dulce-and-quesadillas.html", "Panaderia Dulce"),
        ("pupusa-catering-and-bakery-boxes.html", "Party Boxes"),
        ("visit.html", "Visit & Hours")
    ]
    html = '<nav class="salvadorena-nav-links" id="main-nav">\n'
    for file, label in links:
        active_cls = ' class="active"' if file == active_file else ''
        html += f'          <a href="{file}"{active_cls}>{label}</a>\n'
    html += '          <a href="tel:7045254550" class="salvadorena-btn-cta">Call (704) 525-4550</a>\n        </nav>'
    return html

def header_html(active_file):
    return f'''  <header class="salvadorena-header">
    <div class="salvadorena-topbar">
      <span>Authentic Salvadoran Pupuseria &amp; Panaderia | 4325 South Blvd, Charlotte, NC</span>
      <span>Bakery &amp; Hot Kitchen: <a href="tel:7045254550">(704) 525-4550</a></span>
    </div>
    <div class="salvadorena-nav-container">
      <a href="index.html" class="salvadorena-logo-group">
        <span class="salvadorena-logo-badge">RPS</span>
        <div>
          <span class="salvadorena-logo-text">La Salvadorena</span>
          <span class="salvadorena-logo-sub">Restaurante &amp; Panaderia</span>
        </div>
      </a>
      <button class="salvadorena-mobile-toggle" aria-controls="main-nav" aria-expanded="false" aria-label="Toggle navigation menu">Menu</button>
      {nav_html(active_file)}
    </div>
  </header>'''

def footer_html():
    return '''  <footer class="salvadorena-footer">
    <div class="salvadorena-footer-grid">
      <div class="salvadorena-footer-col">
        <h4 class="salvadorena-brand-title">Restaurante Y Panaderia Salvadorena</h4>
        <p>Charlotte's authentic Salvadoran hub on South Blvd. Savor handcrafted pupusas on corn and rice masa, oven-warm Quesadillas Salvadorenas, pineapple semitas, and hearty weekend stews.</p>
        <p><strong>Pupuseria Artesanal | Panaderia Tradicional | Desayunos Tipicos</strong></p>
      </div>
      <div class="salvadorena-footer-col">
        <h4>Navigation</h4>
        <ul class="salvadorena-footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Full Menu</a></li>
          <li><a href="pupusas-artesanales-and-curtido.html">Pupuseria</a></li>
          <li><a href="panaderia-dulce-and-quesadillas.html">Panaderia Dulce</a></li>
          <li><a href="pupusa-catering-and-bakery-boxes.html">Party Boxes</a></li>
          <li><a href="visit.html">Visit &amp; Hours</a></li>
        </ul>
      </div>
      <div class="salvadorena-footer-col">
        <h4>Bakery &amp; Kitchen Hours</h4>
        <ul class="salvadorena-footer-links">
          <li>Monday - Saturday: 7:30 AM - 9:00 PM</li>
          <li>Sunday: 7:30 AM - 8:30 PM (Sopa de Pata &amp; Res)</li>
          <li>Fresh Pan Dulce Baked Fresh Morning &amp; Afternoon</li>
        </ul>
      </div>
      <div class="salvadorena-footer-col">
        <h4>Contact &amp; Location</h4>
        <p>4325 South Blvd<br>Charlotte, NC 28209</p>
        <p>Phone: <a href="tel:7045254550" style="color:#fef08a;">(704) 525-4550</a></p>
        <p>Email: <a href="mailto:info@panaderiasalvadorenaclt.com" style="color:#fef08a;">info@panaderiasalvadorenaclt.com</a></p>
      </div>
    </div>
    <div class="salvadorena-footer-bottom">
      <p>&copy; 2026 Restaurante Y Panaderia Salvadorena. All rights reserved. Charlotte, North Carolina.</p>
    </div>
  </footer>
  <script src="site.js"></script>
</body>
</html>'''
