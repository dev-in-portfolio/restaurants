# -*- coding: utf-8 -*-

def nav_html(active_file):
    links = [
        ("index.html", "Home"),
        ("menu.html", "Full Menu"),
        ("concourse-breakfast-and-omelets.html", "Breakfast &amp; Omelets"),
        ("artisan-deli-and-specialty-subs.html", "Deli &amp; Sandwiches"),
        ("office-catering-and-breakfast-boxes.html", "Catering &amp; Boxes"),
        ("visit.html", "Visit &amp; Hours")
    ]
    html = '<nav class="halfpenny-nav-links" id="main-nav">\n'
    for file, label in links:
        active_cls = ' class="active"' if file == active_file else ''
        html += f'          <a href="{file}"{active_cls}>{label}</a>\n'
    html += '          <a href="tel:7043429697" class="halfpenny-nav-btn">Call (704) 342-9697</a>\n        </nav>'
    return html

def header_html(active_file):
    return f'''  <header class="halfpenny-header">
    <div class="halfpenny-topbar">
      <span>Concourse Cafe &amp; Deli | 301 S Tryon St Suite 30 (Lower Level)</span>
      <span>Express Morning Counter: <a href="tel:7043429697">(704) 342-9697</a></span>
    </div>
    <div class="halfpenny-nav-container">
      <a href="index.html" class="halfpenny-logo-group">
        <span class="halfpenny-logo-badge">HC</span>
        <div>
          <span class="halfpenny-logo-title">Halfpenny's Cafe</span>
          <span class="halfpenny-logo-sub">Tryon St Concourse &amp; Deli</span>
        </div>
      </a>
      <button class="halfpenny-mobile-toggle" aria-controls="main-nav" aria-expanded="false" aria-label="Toggle navigation menu">Menu</button>
      {nav_html(active_file)}
    </div>
  </header>'''

def footer_html():
    return '''  <footer class="halfpenny-footer">
    <div class="halfpenny-footer-grid">
      <div>
        <h4 style="color:#f59e0b;">Halfpenny's Cafe</h4>
        <p>Uptown Charlotte's beloved concourse breakfast &amp; deli destination inside 301 S Tryon St. Scratch-made buttermilk biscuits, custom omelets, artisan triple-decker clubs, tarragon chicken salad, and corporate catering.</p>
        <p style="margin-top:12px;"><strong>301 S Tryon St, Suite 30 | Lower Concourse Level | Charlotte, NC</strong></p>
      </div>
      <div>
        <h4>Menu Navigation</h4>
        <ul class="halfpenny-footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Full Menu</a></li>
          <li><a href="concourse-breakfast-and-omelets.html">Breakfast &amp; Omelets</a></li>
          <li><a href="artisan-deli-and-specialty-subs.html">Deli &amp; Specialty Subs</a></li>
          <li><a href="office-catering-and-breakfast-boxes.html">Office Catering</a></li>
          <li><a href="visit.html">Visit &amp; Hours</a></li>
        </ul>
      </div>
      <div>
        <h4>Weekday Hours</h4>
        <ul class="halfpenny-footer-links">
          <li>Monday - Thursday: 7:00 AM - 3:30 PM</li>
          <li>Friday: 7:00 AM - 3:00 PM</li>
          <li>Saturday - Sunday: Closed</li>
          <li>Fast Concourse Pickup Daily</li>
        </ul>
      </div>
      <div>
        <h4>Location &amp; Contact</h4>
        <p>301 S Tryon St, Suite 30<br>Charlotte, NC 28282</p>
        <p style="margin-top:8px;">Phone: <a href="tel:7043429697" style="color:#f59e0b; font-weight:700;">(704) 342-9697</a></p>
        <p>Email: <a href="mailto:info@halfpennyscafe.com" style="color:#f59e0b;">info@halfpennyscafe.com</a></p>
      </div>
    </div>
    <div class="halfpenny-footer-bottom">
      <p>&copy; 2026 Halfpenny's Cafe. All rights reserved. Uptown Charlotte, North Carolina.</p>
    </div>
  </footer>
  <script src="site.js"></script>
</body>
</html>'''
