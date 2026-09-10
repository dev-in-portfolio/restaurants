import os

nav_template = '''
      <nav class="subone-nav" aria-label="Primary Navigation">
        <ul class="subone-nav-list">
          <li><a href="index.html" class="subone-nav-link {nav_index}">Home</a></li>
          <li><a href="menu.html" class="subone-nav-link {nav_menu}">Hoagie Menu</a></li>
          <li><a href="fourth-ward-heritage.html" class="subone-nav-link {nav_heritage}">Heritage</a></li>
          <li><a href="nj-steak-and-special-sauce.html" class="subone-nav-link {nav_steak}">NJ Steak &amp; Sauce</a></li>
          <li><a href="hot-and-cold-hoagies.html" class="subone-nav-link {nav_hoagies}">Sub Lineup</a></li>
          <li><a href="visit.html" class="subone-nav-link subone-nav-cta {nav_visit}">Visit &amp; Order</a></li>
        </ul>
      </nav>
'''

footer_content = '''
  <footer class="subone-footer">
    <div class="subone-footer-container">
      <div class="subone-footer-brand">
        <h4>Sub One Hoagie House</h4>
        <p>Serving Uptown Charlotte and the Historic Fourth Ward since September 1992. Veteran and family-owned home of the New Jersey Steak Sub and famous Special Sauce.</p>
      </div>
      <div class="subone-footer-nav">
        <h5>Explore Demo</h5>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Full Menu</a></li>
          <li><a href="fourth-ward-heritage.html">Fourth Ward Heritage</a></li>
          <li><a href="nj-steak-and-special-sauce.html">NJ Steak &amp; Sauce</a></li>
          <li><a href="hot-and-cold-hoagies.html">Hot &amp; Cold Hoagies</a></li>
          <li><a href="visit.html">Location &amp; Hours</a></li>
        </ul>
      </div>
      <div class="subone-footer-hours">
        <h5>Location &amp; Contact</h5>
        <p style="color: #9297a1; font-size: 0.88rem; margin-bottom: 0.4rem;"><strong>Fourth Ward:</strong> 516 N Graham St, Charlotte, NC 28202</p>
        <p style="color: #9297a1; font-size: 0.88rem; margin-bottom: 0.4rem;"><strong>Direct Phone:</strong> (704) 332-1555</p>
        <p style="color: #9297a1; font-size: 0.88rem;">Mon - Fri: 10:30 AM - 7:00 PM<br>Saturday: 11:00 AM - 6:00 PM<br>Sunday: Closed</p>
      </div>
    </div>
    <div class="subone-footer-bottom">
      <p>&copy; 2026 Sub One Hoagie House. All rights reserved. Restaurant showcase demo for Charlotte, NC.</p>
    </div>
  </footer>
'''

pages = {
  'index.html': {
    'title': 'Sub One Hoagie House - Fourth Ward Uptown Charlotte Landmark Since 1992',
    'nav': {'index': 'active', 'menu': '', 'heritage': '', 'steak': '', 'hoagies': '', 'visit': ''},
    'body': '''
    <main>
      <section class="subone-hero">
        <div class="subone-hero-grid">
          <div class="subone-hero-content">
            <span class="subone-hero-badge">Fourth Ward Institution &bull; Est. 1992</span>
            <h1 class="subone-hero-title">Uptown Charlotte’s <span>Original Hoagie House</span></h1>
            <p class="subone-hero-lead">Founded by U.S. Army veteran Richard Jones in 1992, Sub One Hoagie House has served generations of Charlotteans with sizzling New Jersey steak subs, secret Special Sauce, and warm neighborhood hospitality.</p>
            <div class="subone-hero-actions">
              <a href="menu.html" class="subone-btn-primary">View Full Menu</a>
              <a href="nj-steak-and-special-sauce.html" class="subone-btn-secondary">The Famous NJ Steak</a>
            </div>
          </div>
          <div class="subone-hero-img-wrap">
            <img src="images/hero.jpg" alt="Sizzling steak hoagie with melted cheese, lettuce, and tomatoes on Italian roll" width="600" height="400">
          </div>
        </div>
      </section>

      <section class="subone-features">
        <div class="subone-feature-grid">
          <div class="subone-feature-card">
            <div class="subone-feature-tag">Iconic Signature</div>
            <h2 class="subone-feature-title">New Jersey Steak Sub</h2>
            <p class="subone-feature-desc">Chopped ribeye steak griddled hot with sweet onions, melted cheese, shredded lettuce, tomatoes, and secret Special Sauce.</p>
          </div>
          <div class="subone-feature-card">
            <div class="subone-feature-tag">Over 30 Years</div>
            <h2 class="subone-feature-title">Family &amp; Veteran Owned</h2>
            <p class="subone-feature-desc">Proudly serving Fourth Ward neighbors and Uptown workers since September 1992 with steadfast quality.</p>
          </div>
          <div class="subone-feature-card">
            <div class="subone-feature-tag">Made to Order</div>
            <h2 class="subone-feature-title">The Italian &amp; Veggie Options</h2>
            <p class="subone-feature-desc">Generous multi-meat deli cold cuts and wholesome soy-protein vegetarian subs prepared on fresh bakery rolls.</p>
          </div>
        </div>
      </section>

      <section class="subone-section">
        <div class="subone-story-grid">
          <div class="subone-story-img-wrap">
            <img src="images/steak-sub.jpg" alt="Chopped steak cheesesteak sub with melted cheese on toasted Italian roll" width="600" height="380">
          </div>
          <div class="subone-story-content">
            <span class="subone-section-eyebrow">A Queen City Cornerstone</span>
            <h3>Real Griddle Flavors, No Shortcuts</h3>
            <p>At Sub One Hoagie House, every hot sub begins on our seasoned flat-top griddle. We chop tender steak and chicken fresh to order, melt cheese into every crevice, and slide it onto bakery-fresh Italian rolls.</p>
            <p>Topped with crisp shredded iceberg lettuce, vine-ripened tomatoes, oregano, oil, vinegar, and our unmistakable Special Sauce, it is a flavor combination that has kept Charlotte coming back for over three decades.</p>
            <a href="nj-steak-and-special-sauce.html" class="subone-btn-primary" style="margin-top: 0.5rem;">Learn About Our Sauce</a>
          </div>
        </div>
      </section>

      <section class="subone-section" style="background: #ffffff; border-top: 1px solid var(--subone-border); border-bottom: 1px solid var(--subone-border);">
        <div class="subone-section-header">
          <span class="subone-section-eyebrow">Office Luncheons &amp; Events</span>
          <h2 class="subone-section-title">Party Platter &amp; Box Lunch Estimator</h2>
          <p class="subone-section-subtitle">Planning a downtown corporate meeting or weekend game day tailgate? Calculate your sub requirements below.</p>
        </div>

        <div class="subone-calc-card">
          <div class="subone-calc-controls">
            <div class="subone-calc-field">
              <label for="subone-guest-count">Headcount: <span id="subone-guest-display" style="color: var(--subone-primary); font-weight: 800;">20 People</span></label>
              <input type="range" id="subone-guest-count" class="subone-range-slider" min="5" max="100" step="5" value="20">
            </div>
            <div class="subone-calc-field">
              <label for="subone-platter-style">Serving Style</label>
              <select id="subone-platter-style" class="subone-calc-select">
                <option value="party">Party Platter (Cut into 3-inch Finger Subs)</option>
                <option value="individual">Individual Full Box Lunches (Whole Hoagie)</option>
              </select>
            </div>
          </div>
          <div class="subone-calc-results">
            <div class="subone-result-box">
              <span class="num" id="subone-sub-total">15 Whole Hoagies (Cut &amp; Boxed)</span>
              <span class="label">Total Hoagie Volume</span>
            </div>
            <div class="subone-result-box">
              <span class="num" id="subone-chip-total">20 Bags Kettle Chips</span>
              <span class="label">Assorted Chip Bags</span>
            </div>
            <div class="subone-result-box">
              <span class="num" id="subone-tea-total">2 Gallons Sweet Tea</span>
              <span class="label">Fresh Brewed Beverage</span>
            </div>
          </div>
        </div>
      </section>
    </main>
'''
  },
  'menu.html': {
    'title': 'Menu - Sub One Hoagie House Charlotte NC',
    'nav': {'index': '', 'menu': 'active', 'heritage': '', 'steak': '', 'hoagies': '', 'visit': ''},
    'body': '''
    <main class="subone-section">
      <div class="subone-section-header">
        <span class="subone-section-eyebrow">Classic Sub Selections</span>
        <h1 class="subone-section-title">Sub One Hoagie House Menu</h1>
        <p class="subone-section-subtitle">Hot griddled steak subs, cold deli hoagies, chicken cheesesteaks, and vegetarian options made fresh to order.</p>
      </div>

      <div class="subone-filter-tabs" role="tablist" aria-label="Menu Filter Tabs">
        <button type="button" class="subone-filter-btn active" data-filter="all">All Selections</button>
        <button type="button" class="subone-filter-btn" data-filter="hot">Hot Griddled Subs</button>
        <button type="button" class="subone-filter-btn" data-filter="cold">Cold Deli Hoagies</button>
        <button type="button" class="subone-filter-btn" data-filter="chicken">Chicken &amp; Turkey</button>
        <button type="button" class="subone-filter-btn" data-filter="sides">Sides &amp; Drinks</button>
      </div>

      <div class="subone-menu-grid">
        <div class="subone-menu-item" data-category="hot">
          <div class="subone-menu-item-header">
            <span class="subone-menu-item-name">New Jersey Steak Sub</span>
            <span class="subone-menu-item-price">$11.75 / $14.50</span>
          </div>
          <p class="subone-menu-item-desc">Tender chopped steak griddled with sweet onions, melted cheese, shredded lettuce, ripe tomatoes, oil, vinegar, and signature Special Sauce.</p>
          <div class="subone-menu-item-badges">
            <span class="subone-badge subone-badge-red">House Favorite</span>
            <span class="subone-badge">Hot Griddled</span>
          </div>
        </div>

        <div class="subone-menu-item" data-category="hot">
          <div class="subone-menu-item-header">
            <span class="subone-menu-item-name">Philly Cheesesteak</span>
            <span class="subone-menu-item-price">$11.25 / $13.95</span>
          </div>
          <p class="subone-menu-item-desc">Classic chopped ribeye steak with sautéed green bell peppers, grilled Spanish onions, and melted provolone or white American cheese.</p>
          <div class="subone-menu-item-badges">
            <span class="subone-badge">Griddle Classic</span>
          </div>
        </div>

        <div class="subone-menu-item" data-category="cold">
          <div class="subone-menu-item-header">
            <span class="subone-menu-item-name">The Italian Sub</span>
            <span class="subone-menu-item-price">$10.95 / $13.50</span>
          </div>
          <p class="subone-menu-item-desc">Served hot or cold: Turkey ham, turkey salami, beef pepperoni, and beef summer sausage with melted provolone, shredded lettuce, tomato, oil &amp; vinegar.</p>
          <div class="subone-menu-item-badges">
            <span class="subone-badge subone-badge-gold">Popular Classic</span>
          </div>
        </div>

        <div class="subone-menu-item" data-category="chicken">
          <div class="subone-menu-item-header">
            <span class="subone-menu-item-name">Chicken Cheesesteak</span>
            <span class="subone-menu-item-price">$11.25 / $13.95</span>
          </div>
          <p class="subone-menu-item-desc">Seasoned chopped chicken breast seared with sweet onions, melted white cheese, crisp lettuce, tomato, and Special Sauce on an Italian sub roll.</p>
          <div class="subone-menu-item-badges">
            <span class="subone-badge">Lean &amp; Savory</span>
          </div>
        </div>

        <div class="subone-menu-item" data-category="chicken">
          <div class="subone-menu-item-header">
            <span class="subone-menu-item-name">Turkey, Bacon &amp; Swiss</span>
            <span class="subone-menu-item-price">$11.50 / $14.25</span>
          </div>
          <p class="subone-menu-item-desc">Sliced roasted turkey breast, crispy smoked bacon, melted Swiss cheese, lettuce, tomato, and mayonnaise served hot or cold.</p>
          <div class="subone-menu-item-badges">
            <span class="subone-badge">Deli Favorite</span>
          </div>
        </div>

        <div class="subone-menu-item" data-category="cold">
          <div class="subone-menu-item-header">
            <span class="subone-menu-item-name">Vegetarian Sub</span>
            <span class="subone-menu-item-price">$10.25 / $12.75</span>
          </div>
          <p class="subone-menu-item-desc">Savory soy-protein deli cuts, melted provolone cheese, crisp shredded lettuce, tomatoes, sweet pickles, oil, vinegar, and Special Sauce.</p>
          <div class="subone-menu-item-badges">
            <span class="subone-badge subone-badge-green">Plant-Based</span>
          </div>
        </div>

        <div class="subone-menu-item" data-category="sides">
          <div class="subone-menu-item-header">
            <span class="subone-menu-item-name">Crinkle-Cut French Fries</span>
            <span class="subone-menu-item-price">$3.75 / $4.95</span>
          </div>
          <p class="subone-menu-item-desc">Crispy golden crinkle-cut fries seasoned lightly with sea salt, served piping hot.</p>
          <div class="subone-menu-item-badges">
            <span class="subone-badge">Hot Side</span>
          </div>
        </div>

        <div class="subone-menu-item" data-category="sides">
          <div class="subone-menu-item-header">
            <span class="subone-menu-item-name">Southern Sweet Tea</span>
            <span class="subone-menu-item-price">$2.50 / $3.25</span>
          </div>
          <p class="subone-menu-item-desc">Freshly brewed daily in-house with pure cane sugar and served ice-cold.</p>
          <div class="subone-menu-item-badges">
            <span class="subone-badge">Fresh Brewed</span>
          </div>
        </div>
      </div>
    </main>
'''
  },
  'fourth-ward-heritage.html': {
    'title': 'Fourth Ward Heritage - Sub One Hoagie House',
    'nav': {'index': '', 'menu': '', 'heritage': 'active', 'steak': '', 'hoagies': '', 'visit': ''},
    'body': '''
    <main class="subone-section">
      <div class="subone-section-header">
        <span class="subone-section-eyebrow">Our Story &amp; Roots</span>
        <h1 class="subone-section-title">The Fourth Ward Heritage</h1>
        <p class="subone-section-subtitle">More than 30 years of veteran leadership, family dedication, and community connection in Uptown Charlotte.</p>
      </div>

      <div class="subone-story-grid">
        <div class="subone-story-content">
          <h3>Founded by Richard Jones in 1992</h3>
          <p>In September 1992, Richard Jones &mdash; a proud U.S. Army veteran and Certified Public Accountant &mdash; stepped away from the corporate desk to build an enduring small business in the historic Fourth Ward neighborhood of Uptown Charlotte.</p>
          <p>Jones recognized that Charlotte needed an authentic, high-quality hoagie shop where food was cooked with care, portions were honest, and guests were treated like family. For decades, Sub One has served as the first job for countless local youth and family members, maintaining a welcoming atmosphere that never wavers.</p>
        </div>
        <div class="subone-story-img-wrap">
          <img src="images/history.jpg" alt="Classic neighborhood sub shop interior and welcoming counter" width="600" height="380">
        </div>
      </div>

      <div class="subone-story-grid" style="margin-top: 4.5rem;">
        <div class="subone-story-img-wrap">
          <img src="images/hero.jpg" alt="Griddled hoagie sandwiches being prepared on seasoned flat-top" width="600" height="380">
        </div>
        <div class="subone-story-content">
          <h3>A Constant in a Growing City</h3>
          <p>While the Uptown Charlotte skyline has transformed dramatically over the past thirty years, Sub One Hoagie House at 516 N Graham St has stood as a dependable, beloved culinary anchor.</p>
          <p>City workers, neighborhood residents, Panthers game-day fans, and visitors all gather around the counter for the timeless taste of griddled steak subs and secret Special Sauce.</p>
        </div>
      </div>
    </main>
'''
  },
  'nj-steak-and-special-sauce.html': {
    'title': 'NJ Steak & Special Sauce - Sub One Hoagie House',
    'nav': {'index': '', 'menu': '', 'heritage': '', 'steak': 'active', 'hoagies': '', 'visit': ''},
    'body': '''
    <main class="subone-section">
      <div class="subone-section-header">
        <span class="subone-section-eyebrow">The Signature Legend</span>
        <h1 class="subone-section-title">The New Jersey Steak Sub &amp; Special Sauce</h1>
        <p class="subone-section-subtitle">The recipe that put Sub One Hoagie House on Charlotte’s culinary map.</p>
      </div>

      <div class="subone-story-grid">
        <div class="subone-story-img-wrap">
          <img src="images/steak-sub.jpg" alt="New Jersey steak sub packed with chopped steak, onions, cheese, and special sauce" width="600" height="380">
        </div>
        <div class="subone-story-content">
          <h3>The New Jersey Style Technique</h3>
          <p>The New Jersey Steak Sub is not your standard cheesesteak. Originating in the tri-state deli tradition, the NJ style balances hot, deeply savory griddled steak and melted cheese with cool, crisp garden toppings.</p>
          <p>Finely shredded steak is seared with caramelized sweet onions on our hot griddle, blanketed with melted cheese, and immediately loaded with cool shredded lettuce and ripe sliced tomatoes on a soft, sturdy Italian roll.</p>
        </div>
      </div>

      <div class="subone-story-grid" style="margin-top: 4.5rem;">
        <div class="subone-story-content">
          <h3>The Famous "Special Sauce"</h3>
          <p>What ties the New Jersey Steak Sub together is Sub One’s proprietary <strong>Special Sauce</strong>. Created in-house, this creamy, tangy, and subtly spiced condiment elevates the savory steak and crisp veggies.</p>
          <p>Paired with a drizzle of red wine vinegar and Italian herbs, the Special Sauce penetrates the bread crumb, creating a harmonious bite that Charlotte sub enthusiasts swear by.</p>
        </div>
        <div class="subone-story-img-wrap">
          <img src="images/hero.jpg" alt="Close up of steak sandwich with sauce and garnishes" width="600" height="380">
        </div>
      </div>
    </main>
'''
  },
  'hot-and-cold-hoagies.html': {
    'title': 'Hot & Cold Hoagies - Sub One Hoagie House',
    'nav': {'index': '', 'menu': '', 'heritage': '', 'steak': '', 'hoagies': 'active', 'visit': ''},
    'body': '''
    <main class="subone-section">
      <div class="subone-section-header">
        <span class="subone-section-eyebrow">Hand-Crafted Sandwiches</span>
        <h1 class="subone-section-title">The Complete Sub Lineup</h1>
        <p class="subone-section-subtitle">From Italian cold cut classics to grilled chicken cheesesteaks and plant-based options.</p>
      </div>

      <div class="subone-story-grid">
        <div class="subone-story-content">
          <h3>The Italian &amp; Cold Deli Classics</h3>
          <p><strong>The Italian Sub:</strong> A customer favorite featuring sliced turkey ham, turkey salami, beef pepperoni, and beef summer sausage layered with provolone cheese, shredded iceberg lettuce, vine tomatoes, oil, vinegar, and oregano. Order it chilled or toasted in the oven.</p>
          <p><strong>Turkey Bacon Swiss:</strong> Tender turkey breast, crispy smoked bacon, and nutty Swiss cheese balanced with mayo and crisp veggies.</p>
        </div>
        <div class="subone-story-img-wrap">
          <img src="images/italian-sub.jpg" alt="Italian hoagie stacked with deli meats, cheese, lettuce, and tomatoes" width="600" height="380">
        </div>
      </div>

      <div class="subone-story-grid" style="margin-top: 4.5rem;">
        <div class="subone-story-img-wrap">
          <img src="images/sides.jpg" alt="Crispy crinkle cut french fries and sub meal combo" width="600" height="380">
        </div>
        <div class="subone-story-content">
          <h3>Chicken &amp; Vegetarian Craft</h3>
          <p><strong>Chicken Cheesesteak:</strong> 100% white-meat chicken breast chopped fine on the griddle with sweet onions and melted cheese, finished with our signature Special Sauce.</p>
          <p><strong>Vegetarian Sub:</strong> We have proudly offered a savory soy-based vegetarian deli sub for decades, ensuring non-meat eaters can experience our iconic toppings, cheese, and sauce.</p>
        </div>
      </div>
    </main>
'''
  },
  'visit.html': {
    'title': 'Visit & Order - Sub One Hoagie House Charlotte NC',
    'nav': {'index': '', 'menu': '', 'heritage': '', 'steak': '', 'hoagies': '', 'visit': 'active'},
    'body': '''
    <main class="subone-section">
      <div class="subone-section-header">
        <span class="subone-section-eyebrow">Counter Service &amp; Takeout</span>
        <h1 class="subone-section-title">Visit Sub One Hoagie House</h1>
        <p class="subone-section-subtitle">Stop by our Fourth Ward counter in Uptown Charlotte or call ahead for express lunch pickup.</p>
      </div>

      <div class="subone-contact-grid">
        <div class="subone-contact-card">
          <h3>Fourth Ward Location</h3>
          <p style="color: var(--subone-text-muted); margin-bottom: 0.8rem;">Conveniently located on North Graham Street near Uptown businesses, Bank of America Stadium, and Truist Field.</p>
          <p><strong>Address:</strong> 516 N Graham St, Charlotte, NC 28202</p>
          <p style="margin-top: 0.4rem;"><strong>Neighborhood:</strong> Historic Fourth Ward / Uptown</p>
          <div style="margin-top: 1.5rem;">
            <a href="tel:7043321555" class="subone-btn-primary" style="width: 100%; text-align: center;">Call to Order: (704) 332-1555</a>
          </div>
        </div>

        <div class="subone-contact-card">
          <h3>Operating Hours</h3>
          <div class="subone-hours-row">
            <span>Monday &ndash; Friday</span>
            <span>10:30 AM &ndash; 7:00 PM</span>
          </div>
          <div class="subone-hours-row">
            <span>Saturday</span>
            <span>11:00 AM &ndash; 6:00 PM</span>
          </div>
          <div class="subone-hours-row">
            <span>Sunday</span>
            <span>Closed</span>
          </div>
          <div style="margin-top: 1.5rem; background: var(--subone-surface-alt); padding: 1rem; border-radius: var(--subone-radius-sm);">
            <p style="font-size: 0.85rem; color: var(--subone-primary); font-weight: 700;">Fast counter turnaround. Call ahead during weekday lunch peak (11:30 AM - 1:30 PM) for speedy pickup.</p>
          </div>
        </div>

        <div class="subone-contact-card">
          <h3>Catering &amp; Office Platters</h3>
          <p style="color: var(--subone-text-muted); margin-bottom: 0.8rem;">Party sub platters, individual box lunches with chips and drinks, and custom orders for office luncheons and community events.</p>
          <p><strong>Notice:</strong> Please call ahead at least 24 hours for large corporate platters.</p>
          <div style="margin-top: 1.5rem;">
            <a href="mailto:catering@subonehoagiehouse.com" class="subone-btn-secondary" style="width: 100%; text-align: center;">Inquire About Catering</a>
          </div>
        </div>
      </div>
    </main>
'''
  }
}

for filename, data in pages.items():
  cur_nav = nav_template.format(
    nav_index=data['nav']['index'],
    nav_menu=data['nav']['menu'],
    nav_heritage=data['nav']['heritage'],
    nav_steak=data['nav']['steak'],
    nav_hoagies=data['nav']['hoagies'],
    nav_visit=data['nav']['visit']
  )

  html_doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{data['title']}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Archivo:wght@700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="site.css">
</head>
<body>
  <header class="subone-header">
    <div class="subone-nav-container">
      <a href="index.html" class="subone-brand">
        <span class="subone-brand-title">Sub One Hoagie House</span>
        <span class="subone-brand-subtitle">Fourth Ward Landmark &bull; Est. 1992</span>
      </a>
      <button class="subone-nav-toggle" type="button" aria-label="Toggle navigation menu" aria-expanded="false">Menu</button>
{cur_nav}
    </div>
  </header>

{data['body']}

{footer_content}
  <script src="site.js"></script>
</body>
</html>'''

  filepath = os.path.join('sub-one-hoagie-house', filename)
  with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html_doc.strip() + '\n')
  print(f'Wrote {filename}')

print('All 6 HTML pages for Sub One Hoagie House written successfully')
