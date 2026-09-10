# -*- coding: utf-8 -*-

def nav_html(active_file):
    links = [
        ("index.html", "Home"),
        ("menu.html", "Full Menu"),
        ("hibachi-grill-and-wok-specials.html", "Hibachi & Wok"),
        ("thai-noodles-and-curry-bowls.html", "Thai Specialties"),
        ("party-platters-and-family-bundles.html", "Party Bundles"),
        ("visit.html", "Visit & Hours")
    ]
    html = '<nav class="ksasian-nav-links" id="main-nav">\n'
    for file, label in links:
        active_cls = ' class="active"' if file == active_file else ''
        html += f'          <a href="{file}"{active_cls}>{label}</a>\n'
    html += '          <a href="tel:9802019962" class="ksasian-btn-cta">Call (980) 201-9962</a>\n        </nav>'
    return html

def header_html(active_file):
    return f'''  <header class="ksasian-header">
    <div class="ksasian-topbar">
      <span>Fast-Casual Asian Fusion &amp; Hibachi | 10102 Albemarle Rd, Charlotte, NC</span>
      <span>Quick Takeout &amp; Express Counter: <a href="tel:9802019962">(980) 201-9962</a></span>
    </div>
    <div class="ksasian-nav-container">
      <a href="index.html" class="ksasian-logo-group">
        <span class="ksasian-logo-badge">KAX</span>
        <div>
          <span class="ksasian-logo-text">K’s Asian Xpress</span>
          <span class="ksasian-logo-sub">Hibachi &bull; Wok &bull; Thai Fusion</span>
        </div>
      </a>
      <button class="ksasian-mobile-toggle" aria-controls="main-nav" aria-expanded="false" aria-label="Toggle navigation menu">Menu</button>
      {nav_html(active_file)}
    </div>
  </header>'''

def footer_html():
    return '''  <footer class="ksasian-footer">
    <div class="ksasian-footer-grid">
      <div class="ksasian-footer-col">
        <h4 class="ksasian-brand-title">K’s Asian Xpress</h4>
        <p>East Charlotte's destination for sizzling flat-top Japanese hibachi, wok-charred Chinese classics, street-style Thai curries and noodles, and crispy wings prepared fresh in minutes.</p>
        <p><strong>Fast Takeout | Casual Dine-In | Family Bundles</strong></p>
      </div>
      <div class="ksasian-footer-col">
        <h4>Navigation</h4>
        <ul class="ksasian-footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Full Menu</a></li>
          <li><a href="hibachi-grill-and-wok-specials.html">Hibachi &amp; Wok</a></li>
          <li><a href="thai-noodles-and-curry-bowls.html">Thai Specialties</a></li>
          <li><a href="party-platters-and-family-bundles.html">Party Bundles</a></li>
          <li><a href="visit.html">Visit &amp; Hours</a></li>
        </ul>
      </div>
      <div class="ksasian-footer-col">
        <h4>Kitchen Hours</h4>
        <ul class="ksasian-footer-links">
          <li>Monday - Thursday: 11:00 AM - 9:30 PM</li>
          <li>Friday - Saturday: 11:00 AM - 10:00 PM</li>
          <li>Sunday: 12:00 PM - 9:00 PM</li>
          <li>Fast Pickup &amp; Delivery Ready</li>
        </ul>
      </div>
      <div class="ksasian-footer-col">
        <h4>Contact &amp; Location</h4>
        <p>10102 Albemarle Rd, Suite 3<br>Charlotte, NC 28227</p>
        <p>Phone: <a href="tel:9802019962" style="color:#fef08a;">(980) 201-9962</a></p>
        <p>Email: <a href="mailto:orders@ksasianxpressclt.com" style="color:#fef08a;">orders@ksasianxpressclt.com</a></p>
      </div>
    </div>
    <div class="ksasian-footer-bottom">
      <p>&copy; 2026 K’s Asian Xpress. All rights reserved. Charlotte, North Carolina.</p>
    </div>
  </footer>
  <script src="site.js"></script>
</body>
</html>'''
