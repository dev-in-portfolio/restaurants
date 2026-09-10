# -*- coding: utf-8 -*-

def nav_html(active_file):
    links = [
        ("index.html", "Home"),
        ("menu.html", "Full Menu"),
        ("chef-specialties-and-combos.html", "Specialties &amp; Combos"),
        ("wok-noodles-and-fried-rice.html", "Lo Mein &amp; Rice"),
        ("family-feasts-and-catering.html", "Family &amp; Catering"),
        ("visit.html", "Visit &amp; Hours")
    ]
    html = '<nav class="gw-nav-links" id="main-nav">\n'
    for file, label in links:
        active_cls = ' class="active"' if file == active_file else ''
        html += f'          <a href="{file}"{active_cls}>{label}</a>\n'
    html += '          <a href="tel:7043330080" class="gw-nav-btn">Call (704) 333-0080</a>\n        </nav>'
    return html

def header_html(active_file):
    return f'''  <header class="gw-header">
    <div class="gw-topbar">
      <span>High-Flame Chinese Takeout &amp; Catering | 718 W Trade St Suite M, Uptown Charlotte</span>
      <span>Quick Pickup Counter: <a href="tel:7043330080">(704) 333-0080</a></span>
    </div>
    <div class="gw-nav-container">
      <a href="index.html" class="gw-logo-group">
        <span class="gw-logo-badge">GW</span>
        <div>
          <span class="gw-logo-title">Great Wok</span>
          <span class="gw-logo-sub">Chinese Takeout &amp; Kitchen</span>
        </div>
      </a>
      <button class="gw-mobile-toggle" aria-controls="main-nav" aria-expanded="false" aria-label="Toggle navigation menu">Menu</button>
      {nav_html(active_file)}
    </div>
  </header>'''

def footer_html():
    return '''  <footer class="gw-footer">
    <div class="gw-footer-grid">
      <div>
        <h4 style="color:#fbbf24;">Great Wok Chinese Kitchen</h4>
        <p>Uptown Charlotte's favorite high-flame Chinese kitchen at Gateway Village. Sizzling General Tso's chicken, classic Lo Mein, egg foo young, generous lunch combos, and family catering pans.</p>
        <p style="margin-top:12px;"><strong>718 W Trade St, Suite M | Gateway Village | Charlotte, NC</strong></p>
      </div>
      <div>
        <h4>Menu Navigation</h4>
        <ul class="gw-footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Full Menu</a></li>
          <li><a href="chef-specialties-and-combos.html">Specialties &amp; Combos</a></li>
          <li><a href="wok-noodles-and-fried-rice.html">Lo Mein &amp; Fried Rice</a></li>
          <li><a href="family-feasts-and-catering.html">Family Feasts &amp; Catering</a></li>
          <li><a href="visit.html">Visit &amp; Hours</a></li>
        </ul>
      </div>
      <div>
        <h4>Hours of Operation</h4>
        <ul class="gw-footer-links">
          <li>Monday - Thursday: 11:00 AM - 9:30 PM</li>
          <li>Friday: 11:00 AM - 10:00 PM</li>
          <li>Saturday: 12:00 PM - 10:00 PM</li>
          <li>Sunday: Closed</li>
          <li>Fast Lunch Combos 11:00 AM - 3:00 PM</li>
        </ul>
      </div>
      <div>
        <h4>Location &amp; Contact</h4>
        <p>718 W Trade St, Suite M<br>Charlotte, NC 28202</p>
        <p style="margin-top:8px;">Phone: <a href="tel:7043330080" style="color:#fbbf24; font-weight:700;">(704) 333-0080</a></p>
        <p>Email: <a href="mailto:orders@charlottegreatwok.com" style="color:#fbbf24;">orders@charlottegreatwok.com</a></p>
      </div>
    </div>
    <div class="gw-footer-bottom">
      <p>&copy; 2026 Great Wok Chinese Kitchen. All rights reserved. Uptown Charlotte, North Carolina.</p>
    </div>
  </footer>
  <script src="site.js"></script>
</body>
</html>'''
