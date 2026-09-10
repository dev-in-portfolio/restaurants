# -*- coding: utf-8 -*-

def nav_html(active_file):
    links = [
        ("index.html", "Home"),
        ("menu.html", "Full Menu"),
        ("specialty-maki-and-poke-craft.html", "Maki &amp; Poke"),
        ("hot-udon-and-bulgogi-kitchen.html", "Hot Kitchen"),
        ("corporate-catering-and-party-trays.html", "Corporate Trays"),
        ("visit.html", "Visit &amp; Hours")
    ]
    html = '<nav class="kosushi-nav-links" id="main-nav">\n'
    for file, label in links:
        active_cls = ' class="active"' if file == active_file else ''
        html += f'          <a href="{file}"{active_cls}>{label}</a>\n'
    html += '          <a href="tel:7043727757" class="kosushi-btn-cta">Call (704) 372-7757</a>\n        </nav>'
    return html

def header_html(active_file):
    return f'''  <header class="kosushi-header">
    <div class="kosushi-topbar">
      <span>Uptown Charlotte Artisanal Sushi &amp; Asian Kitchen | 230 S Tryon St</span>
      <span>Express Lunch &amp; Takeout: <a href="tel:7043727757">(704) 372-7757</a></span>
    </div>
    <div class="kosushi-nav-container">
      <a href="index.html" class="kosushi-logo-group">
        <span class="kosushi-logo-badge">KO</span>
        <div>
          <span class="kosushi-logo-text">K.O. Sushi</span>
          <span class="kosushi-logo-sub">QC Artisanal Sushi &amp; Poke</span>
        </div>
      </a>
      <button class="kosushi-mobile-toggle" aria-controls="main-nav" aria-expanded="false" aria-label="Toggle navigation menu">Menu</button>
      {nav_html(active_file)}
    </div>
  </header>'''

def footer_html():
    return '''  <footer class="kosushi-footer">
    <div class="kosushi-footer-grid">
      <div class="kosushi-footer-col">
        <h4 class="kosushi-brand-title">K.O. Sushi of the QC</h4>
        <p>Uptown Charlotte's premier fast-precision sushi destination on South Tryon Street. Handcrafted specialty maki, fresh Hawaiian poke bowls, steaming dashi udon, and 38-piece corporate catering trays.</p>
        <p><strong>Fresh Daily Fish | Fast Lunch Service | Corporate Catering</strong></p>
      </div>
      <div class="kosushi-footer-col">
        <h4>Navigation</h4>
        <ul class="kosushi-footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Full Menu</a></li>
          <li><a href="specialty-maki-and-poke-craft.html">Maki &amp; Poke Craft</a></li>
          <li><a href="hot-udon-and-bulgogi-kitchen.html">Hot Udon &amp; Bulgogi</a></li>
          <li><a href="corporate-catering-and-party-trays.html">Corporate Platters</a></li>
          <li><a href="visit.html">Visit &amp; Hours</a></li>
        </ul>
      </div>
      <div class="kosushi-footer-col">
        <h4>Uptown Hours</h4>
        <ul class="kosushi-footer-links">
          <li>Monday: 11:00 AM - 3:00 PM (Lunch)</li>
          <li>Tuesday - Thursday: 11:00 AM - 3:00 PM | 4:30 PM - 8:00 PM</li>
          <li>Friday: 11:00 AM - 3:00 PM (Lunch)</li>
          <li>Saturday &amp; Sunday: Closed (Corporate Catering by Advance Order)</li>
        </ul>
      </div>
      <div class="kosushi-footer-col">
        <h4>Contact &amp; Location</h4>
        <p>230 S Tryon St, Suite R1<br>Charlotte, NC 28202</p>
        <p>Phone: <a href="tel:7043727757" style="color:#fef08a;">(704) 372-7757</a></p>
        <p>Email: <a href="mailto:info@kosushioftheqc.com" style="color:#fef08a;">info@kosushioftheqc.com</a></p>
      </div>
    </div>
    <div class="kosushi-footer-bottom">
      <p>&copy; 2026 K.O. Sushi of the QC. All rights reserved. Uptown Charlotte, North Carolina.</p>
    </div>
  </footer>
  <script src="site.js"></script>
</body>
</html>'''
