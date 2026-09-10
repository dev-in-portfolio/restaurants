# -*- coding: utf-8 -*-

def nav_html(active_file):
    links = [
        ("index.html", "Home"),
        ("menu.html", "Full Menu"),
        ("all-day-breakfast-and-sandwiches.html", "Breakfast &amp; Sandwiches"),
        ("espresso-bar-and-specialty-drinks.html", "Espresso Bar"),
        ("morning-catering-and-coffee-boxes.html", "Catering &amp; Coffee"),
        ("visit.html", "Visit &amp; Hours")
    ]
    html = '<nav class="lottie-nav-links" id="main-nav">\n'
    for file, label in links:
        active_cls = ' class="active"' if file == active_file else ''
        html += f'          <a href="{file}"{active_cls}>{label}</a>\n'
    html += '          <a href="tel:7047893135" class="lottie-nav-btn">Call (704) 789-3135</a>\n        </nav>'
    return html

def header_html(active_file):
    return f'''  <header class="lottie-header">
    <div class="lottie-topbar">
      <span>Artisanal Cafe &amp; Espresso Bar | Queen City Quarter, 210 E Trade St</span>
      <span>Morning Counter &amp; Call Ahead: <a href="tel:7047893135">(704) 789-3135</a></span>
    </div>
    <div class="lottie-nav-container">
      <a href="index.html" class="lottie-logo-group">
        <span class="lottie-logo-badge">LC</span>
        <div>
          <span class="lottie-logo-title">Lottie's Cafe</span>
          <span class="lottie-logo-sub">Artisanal Coffee &amp; Kitchen</span>
        </div>
      </a>
      <button class="lottie-mobile-toggle" aria-controls="main-nav" aria-expanded="false" aria-label="Toggle navigation menu">Menu</button>
      {nav_html(active_file)}
    </div>
  </header>'''

def footer_html():
    return '''  <footer class="lottie-footer">
    <div class="lottie-footer-grid">
      <div>
        <h4 style="color:#fde68a;">Lottie's Cafe</h4>
        <p>Uptown Charlotte's destination for artisanal coffee, handcrafted all-day breakfast sandwiches, scratch-made lunch paninis, power grain bowls, and corporate morning meeting catering.</p>
        <p style="margin-top:12px;"><strong>210 E Trade St | Queen City Quarter | Charlotte, NC</strong></p>
      </div>
      <div>
        <h4>Explore</h4>
        <ul class="lottie-footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Full Menu</a></li>
          <li><a href="all-day-breakfast-and-sandwiches.html">Breakfast &amp; Sandwiches</a></li>
          <li><a href="espresso-bar-and-specialty-drinks.html">Espresso &amp; Lattes</a></li>
          <li><a href="morning-catering-and-coffee-boxes.html">Morning Catering</a></li>
          <li><a href="visit.html">Visit &amp; Hours</a></li>
        </ul>
      </div>
      <div>
        <h4>Cafe Hours</h4>
        <ul class="lottie-footer-links">
          <li>Monday - Saturday: 7:00 AM - 4:00 PM</li>
          <li>Sunday: 8:00 AM - 4:00 PM</li>
          <li>All-Day Breakfast &amp; Espresso Daily</li>
        </ul>
      </div>
      <div>
        <h4>Location &amp; Contact</h4>
        <p>210 E Trade St<br>Charlotte, NC 28202</p>
        <p style="margin-top:8px;">Phone: <a href="tel:7047893135" style="color:#fde68a; font-weight:700;">(704) 789-3135</a></p>
        <p>Email: <a href="mailto:info@lottiesclt.com" style="color:#fde68a;">info@lottiesclt.com</a></p>
      </div>
    </div>
    <div class="lottie-footer-bottom">
      <p>&copy; 2026 Lottie's Cafe. All rights reserved. Uptown Charlotte, North Carolina.</p>
    </div>
  </footer>
  <script src="site.js"></script>
</body>
</html>'''
