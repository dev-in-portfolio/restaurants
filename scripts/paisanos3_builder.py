
def nav_html(active_file):
    links = [
        ("index.html", "Home"),
        ("menu.html", "Full Menu"),
        ("tortilleria-nixtamal-and-fresh-masa.html", "Nixtamal Tortilleria"),
        ("carnitas-michoacanas-and-cazo.html", "Cazo de Carnitas"),
        ("taqueria-packs-and-meat-orders.html", "Fiesta Packs"),
        ("visit.html", "Visit & Hours")
    ]
    html = '<nav class="paisanos3-nav-links" id="main-nav">\n'
    for file, label in links:
        active_cls = ' class="active"' if file == active_file else ''
        html += f'          <a href="{file}"{active_cls}>{label}</a>\n'
    html += '          <a href="tel:7045354422" class="paisanos3-btn-cta">Call (704) 535-4422</a>\n        </nav>'
    return html

def header_html(active_file):
    return f'''  <header class="paisanos3-header">
    <div class="paisanos3-topbar">
      <span>Authentic Nixtamal Tortilleria, Carniceria & Taqueria | 4434 Central Ave, Charlotte, NC</span>
      <span>Meat Market & Hot Food: <a href="tel:7045354422">(704) 535-4422</a></span>
    </div>
    <div class="paisanos3-nav-container">
      <a href="index.html" class="paisanos3-logo-group">
        <span class="paisanos3-logo-badge">LP3</span>
        <div>
          <span class="paisanos3-logo-text">Los Paisanos 3</span>
          <span class="paisanos3-logo-sub">Tortilleria & Carniceria</span>
        </div>
      </a>
      <button class="paisanos3-mobile-toggle" aria-controls="main-nav" aria-expanded="false" aria-label="Toggle navigation menu">Menu</button>
      {nav_html(active_file)}
    </div>
  </header>'''

def footer_html():
    return '''  <footer class="paisanos3-footer">
    <div class="paisanos3-footer-grid">
      <div class="paisanos3-footer-col">
        <h4 class="paisanos3-brand-title">Los Paisanos 3</h4>
        <p>East Charlotte's premier artisanal nixtamal tortilleria, traditional butcher carniceria, and hot copper cazo carnitas kitchen on Central Avenue.</p>
        <p><strong>Tortilleria Fresca | Carniceria Fina | Taqueria Caliente</strong></p>
      </div>
      <div class="paisanos3-footer-col">
        <h4>Navigation</h4>
        <ul class="paisanos3-footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Full Menu</a></li>
          <li><a href="tortilleria-nixtamal-and-fresh-masa.html">Nixtamal Tortilleria</a></li>
          <li><a href="carnitas-michoacanas-and-cazo.html">Cazo de Carnitas</a></li>
          <li><a href="taqueria-packs-and-meat-orders.html">Fiesta Packs</a></li>
          <li><a href="visit.html">Visit & Hours</a></li>
        </ul>
      </div>
      <div class="paisanos3-footer-col">
        <h4>Market & Kitchen Hours</h4>
        <ul class="paisanos3-footer-links">
          <li>Monday - Saturday: 8:00 AM - 9:00 PM</li>
          <li>Sunday: 8:00 AM - 8:30 PM (Barbacoa & Menudo)</li>
          <li>Fresh Hot Tortillas & Carnitas Available Daily</li>
        </ul>
      </div>
      <div class="paisanos3-footer-col">
        <h4>Contact & Location</h4>
        <p>4434 Central Ave<br>Charlotte, NC 28205</p>
        <p>Phone: <a href="tel:7045354422" style="color:var(--paisanos3-gold);">(704) 535-4422</a></p>
        <p>Email: <a href="mailto:info@lospaisanos3clt.com" style="color:var(--paisanos3-gold);">info@lospaisanos3clt.com</a></p>
      </div>
    </div>
    <div class="paisanos3-footer-bottom">
      <p>&copy; 2026 Tortilleria Y Carniceria Los Paisanos 3. All rights reserved. Charlotte, North Carolina.</p>
    </div>
  </footer>
  <script src="site.js"></script>
</body>
</html>'''
