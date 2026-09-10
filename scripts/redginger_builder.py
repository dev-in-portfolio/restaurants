# -*- coding: utf-8 -*-

def nav_html(active_file):
    links = [
        ("index.html", "Home"),
        ("menu.html", "Full Menu"),
        ("teppanyaki-hibachi-experience.html", "Teppanyaki"),
        ("sushi-bar-and-omakase-craft.html", "Sushi Lounge"),
        ("private-dining-and-group-events.html", "Private Dining"),
        ("visit.html", "Visit &amp; Hours")
    ]
    html = '<nav class="redginger-nav-links" id="main-nav">\n'
    for file, label in links:
        active_cls = ' class="active"' if file == active_file else ''
        html += f'          <a href="{file}"{active_cls}>{label}</a>\n'
    html += '          <a href="tel:9808198837" class="redginger-btn-cta">Call (980) 819-8837</a>\n        </nav>'
    return html

def header_html(active_file):
    return f'''  <header class="redginger-header">
    <div class="redginger-topbar">
      <span>Uptown Charlotte Japanese Steakhouse &amp; Sushi Lounge | 401 S Tryon St</span>
      <span>Reservations &amp; Takeout: <a href="tel:9808198837">(980) 819-8837</a></span>
    </div>
    <div class="redginger-nav-container">
      <a href="index.html" class="redginger-logo-group">
        <span class="redginger-logo-badge">RG</span>
        <div>
          <span class="redginger-logo-text">Red Ginger</span>
          <span class="redginger-logo-sub">Japanese Steakhouse &amp; Sushi</span>
        </div>
      </a>
      <button class="redginger-mobile-toggle" aria-controls="main-nav" aria-expanded="false" aria-label="Toggle navigation menu">Menu</button>
      {nav_html(active_file)}
    </div>
  </header>'''

def footer_html():
    return '''  <footer class="redginger-footer">
    <div class="redginger-footer-grid">
      <div class="redginger-footer-col">
        <h4 class="redginger-brand-title">Red Ginger Japanese Steakhouse</h4>
        <p>Uptown Charlotte's premier teppanyaki dining destination and artisanal sushi lounge on South Tryon Street. Sizzling table-side filet mignon, cold-water lobster tails, innovative sashimi, and executive power lunches.</p>
        <p><strong>Table-Side Teppanyaki | Artisan Sushi Bar | Private Dining</strong></p>
      </div>
      <div class="redginger-footer-col">
        <h4>Navigation</h4>
        <ul class="redginger-footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Full Menu</a></li>
          <li><a href="teppanyaki-hibachi-experience.html">Teppanyaki Experience</a></li>
          <li><a href="sushi-bar-and-omakase-craft.html">Sushi Lounge</a></li>
          <li><a href="private-dining-and-group-events.html">Private Dining</a></li>
          <li><a href="visit.html">Visit &amp; Hours</a></li>
        </ul>
      </div>
      <div class="redginger-footer-col">
        <h4>Operating Hours</h4>
        <ul class="redginger-footer-links">
          <li>Monday - Thursday: 11:00 AM - 2:30 PM | 4:30 PM - 10:00 PM</li>
          <li>Friday: 11:00 AM - 2:30 PM | 4:30 PM - 11:00 PM</li>
          <li>Saturday: 4:30 PM - 11:00 PM (Dinner &amp; Cocktails)</li>
          <li>Sunday: 11:30 AM - 9:30 PM (All-Day Dining)</li>
        </ul>
      </div>
      <div class="redginger-footer-col">
        <h4>Contact &amp; Location</h4>
        <p>401 S Tryon St, Suite 130<br>Charlotte, NC 28202</p>
        <p>Phone: <a href="tel:9808198837" style="color:#fef08a;">(980) 819-8837</a></p>
        <p>Email: <a href="mailto:contact@redgingercharlotte.com" style="color:#fef08a;">contact@redgingercharlotte.com</a></p>
      </div>
    </div>
    <div class="redginger-footer-bottom">
      <p>&copy; 2026 Red Ginger Japanese Steakhouse &amp; Sushi. All rights reserved. Uptown Charlotte, North Carolina.</p>
    </div>
  </footer>
  <script src="site.js"></script>
</body>
</html>'''
