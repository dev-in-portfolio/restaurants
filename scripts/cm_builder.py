# -*- coding: utf-8 -*-

def nav_html(active_file):
    links = [
        ("index.html", "Home"),
        ("menu.html", "Full Menu"),
        ("gourmet-sliders-and-wings.html", "Sliders &amp; Wings"),
        ("weekend-brunch-and-mimosas.html", "Weekend Brunch"),
        ("gameday-packages-and-events.html", "Gameday &amp; Events"),
        ("visit.html", "Visit &amp; Hours")
    ]
    html = '<nav class="cm-nav-links" id="main-nav">\n'
    for file, label in links:
        active_cls = ' class="active"' if file == active_file else ''
        html += f'          <a href="{file}"{active_cls}>{label}</a>\n'
    html += '          <a href="tel:9802999000" class="cm-nav-btn">Call (980) 299-9000</a>\n        </nav>'
    return html

def header_html(active_file):
    return f'''  <header class="cm-header">
    <div class="cm-topbar">
      <span>Sports Bar, Craft Lounge &amp; Late Night | 521 N College St, Uptown Charlotte</span>
      <span>VIP Tables &amp; Orders: <a href="tel:9802999000">(980) 299-9000</a></span>
    </div>
    <div class="cm-nav-container">
      <a href="index.html" class="cm-logo-group">
        <span class="cm-logo-badge">CM</span>
        <div>
          <span class="cm-logo-title">Cheers Mate</span>
          <span class="cm-logo-sub">Bar &amp; Sports Lounge</span>
        </div>
      </a>
      <button class="cm-mobile-toggle" aria-controls="main-nav" aria-expanded="false" aria-label="Toggle navigation menu">Menu</button>
      {nav_html(active_file)}
    </div>
  </header>'''

def footer_html():
    return '''  <footer class="cm-footer">
    <div class="cm-footer-grid">
      <div>
        <h4 style="color:#f59e0b;">Cheers Mate Bar &amp; Lounge</h4>
        <p>Uptown Charlotte's premier sports lounge, late-night kitchen, and weekend brunch hub on North College Street. Gourmet smash sliders, crispy jumbo wings, loaded fries, and signature craft mixology.</p>
        <p style="margin-top:12px;"><strong>521 N College St | First Ward Corridor | Charlotte, NC</strong></p>
      </div>
      <div>
        <h4>Quick Links</h4>
        <ul class="cm-footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Full Menu</a></li>
          <li><a href="gourmet-sliders-and-wings.html">Sliders &amp; Wings</a></li>
          <li><a href="weekend-brunch-and-mimosas.html">Weekend Brunch &amp; Mimosas</a></li>
          <li><a href="gameday-packages-and-events.html">Gameday &amp; VIP Events</a></li>
          <li><a href="visit.html">Visit &amp; Hours</a></li>
        </ul>
      </div>
      <div>
        <h4>Hours of Operation</h4>
        <ul class="cm-footer-links">
          <li>Monday - Thursday: 4:00 PM - 2:00 AM</li>
          <li>Friday: 3:00 PM - 2:00 AM</li>
          <li>Saturday: 11:00 AM - 2:00 AM (Brunch 11am-4pm)</li>
          <li>Sunday: 11:00 AM - 2:00 AM (Brunch 11am-4pm)</li>
          <li>Late Night Kitchen Open Until 1:30 AM</li>
        </ul>
      </div>
      <div>
        <h4>Location &amp; Contact</h4>
        <p>521 N College St<br>Charlotte, NC 28202</p>
        <p style="margin-top:8px;">Phone: <a href="tel:9802999000" style="color:#f59e0b; font-weight:700;">(980) 299-9000</a></p>
        <p>Email: <a href="mailto:info@cheersmatesclt.com" style="color:#f59e0b;">info@cheersmatesclt.com</a></p>
      </div>
    </div>
    <div class="cm-footer-bottom">
      <p>&copy; 2026 Cheers Mate Bar &amp; Lounge. All rights reserved. Uptown Charlotte, North Carolina.</p>
    </div>
  </footer>
  <script src="site.js"></script>
</body>
</html>'''
