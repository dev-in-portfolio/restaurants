# -*- coding: utf-8 -*-

def nav_html(active_file):
    links = [
        ("index.html", "Home"),
        ("menu.html", "Full Menu"),
        ("cajun-and-creole-specialties.html", "Cajun &amp; Creole"),
        ("brevard-court-courtyard-dining.html", "Courtyard Patio"),
        ("gameday-tailgates-and-catering.html", "Gameday &amp; Catering"),
        ("visit.html", "Visit &amp; Hours")
    ]
    html = '<nav class="fq-nav-links" id="main-nav">\n'
    for file, label in links:
        active_cls = ' class="active"' if file == active_file else ''
        html += f'          <a href="{file}"{active_cls}>{label}</a>\n'
    html += '          <a href="tel:7043771715" class="fq-nav-btn">Call (704) 377-1715</a>\n        </nav>'
    return html

def header_html(active_file):
    return f'''  <header class="fq-header">
    <div class="fq-topbar">
      <span>New Orleans Cajun &amp; Creole Pub | Established 1986 | Brevard Court</span>
      <span>Daily Lunch &amp; Patio Service: <a href="tel:7043771715">(704) 377-1715</a></span>
    </div>
    <div class="fq-nav-container">
      <a href="index.html" class="fq-logo-group">
        <span class="fq-logo-badge">FQ</span>
        <div>
          <span class="fq-logo-title">French Quarter</span>
          <span class="fq-logo-sub">Restaurant &amp; Pub Charlotte</span>
        </div>
      </a>
      <button class="fq-mobile-toggle" aria-controls="main-nav" aria-expanded="false" aria-label="Toggle navigation menu">Menu</button>
      {nav_html(active_file)}
    </div>
  </header>'''

def footer_html():
    return '''  <footer class="fq-footer">
    <div class="fq-footer-grid">
      <div>
        <h4 style="color:#f59e0b;">French Quarter Restaurant</h4>
        <p>Serving Uptown Charlotte for over 35 years from historic Brevard Court. Authentic Louisiana Cajun &amp; Creole specialties, legendary Salt &amp; Pepper wings, handcrafted sandwiches, and open-air courtyard patio hospitality.</p>
        <p style="margin-top:12px;"><strong>Established 1986 | Brevard Court Entrance | Charlotte, NC</strong></p>
      </div>
      <div>
        <h4>Explore</h4>
        <ul class="fq-footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Full Menu</a></li>
          <li><a href="cajun-and-creole-specialties.html">Cajun &amp; Creole Specialties</a></li>
          <li><a href="brevard-court-courtyard-dining.html">Courtyard Patio Dining</a></li>
          <li><a href="gameday-tailgates-and-catering.html">Gameday &amp; Catering</a></li>
          <li><a href="visit.html">Visit &amp; Hours</a></li>
        </ul>
      </div>
      <div>
        <h4>Hours of Operation</h4>
        <ul class="fq-footer-links">
          <li>Monday - Thursday: 11:00 AM - 10:00 PM</li>
          <li>Friday - Saturday: 11:00 AM - 11:00 PM</li>
          <li>Sunday: 12:00 PM - 9:00 PM (Gamedays Open Early)</li>
          <li>Kitchen open daily for lunch &amp; dinner</li>
        </ul>
      </div>
      <div>
        <h4>Contact &amp; Location</h4>
        <p>321 S Church St (Brevard Court)<br>Charlotte, NC 28202</p>
        <p style="margin-top:8px;">Phone: <a href="tel:7043771715" style="color:#f59e0b; font-weight:700;">(704) 377-1715</a></p>
        <p>Email: <a href="mailto:info@frenchquartercharlotte.com" style="color:#f59e0b;">info@frenchquartercharlotte.com</a></p>
      </div>
    </div>
    <div class="fq-footer-bottom">
      <p>&copy; 2026 French Quarter Restaurant. All rights reserved. Uptown Charlotte, North Carolina.</p>
    </div>
  </footer>
  <script src="site.js"></script>
</body>
</html>'''
