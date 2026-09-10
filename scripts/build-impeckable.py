import os

nav_template = '''
      <nav class="impeck-nav" aria-label="Primary Navigation">
        <ul class="impeck-nav-list">
          <li><a href="index.html" class="impeck-nav-link {nav_index}">Home</a></li>
          <li><a href="menu.html" class="impeck-nav-link {nav_menu}">Menu</a></li>
          <li><a href="buttermilk-craft-and-brine.html" class="impeck-nav-link {nav_craft}">Brine &amp; Craft</a></li>
          <li><a href="sandwiches-and-tenders.html" class="impeck-nav-link {nav_sandwiches}">Sandwiches &amp; Tenders</a></li>
          <li><a href="wings-sides-and-sauces.html" class="impeck-nav-link {nav_wings}">Wings &amp; Sauces</a></li>
          <li><a href="visit.html" class="impeck-nav-link impeck-nav-cta {nav_visit}">Visit &amp; Order</a></li>
        </ul>
      </nav>
'''

footer_content = '''
  <footer class="impeck-footer">
    <div class="impeck-footer-container">
      <div class="impeck-footer-brand">
        <h4>Impeckable Chicken</h4>
        <p>Hand-breaded buttermilk chicken tenders, towering brioche sandwiches, jumbo crispy wings, and seasoned waffle fries inside Monarch Market in Uptown Charlotte, NC.</p>
      </div>
      <div class="impeck-footer-nav">
        <h5>Explore Demo</h5>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Full Menu</a></li>
          <li><a href="buttermilk-craft-and-brine.html">Brine &amp; Craft</a></li>
          <li><a href="sandwiches-and-tenders.html">Sandwiches &amp; Tenders</a></li>
          <li><a href="wings-sides-and-sauces.html">Wings, Sides &amp; Sauces</a></li>
          <li><a href="visit.html">Location &amp; Hours</a></li>
        </ul>
      </div>
      <div class="impeck-footer-hours">
        <h5>Location &amp; Hours</h5>
        <p style="color: #9698a3; font-size: 0.88rem; margin-bottom: 0.4rem;"><strong>Monarch Market:</strong> 101 N Tryon St, Charlotte, NC 28202</p>
        <p style="color: #9698a3; font-size: 0.88rem; margin-bottom: 0.4rem;"><strong>Direct Phone:</strong> (704) 910-1500</p>
        <p style="color: #9698a3; font-size: 0.88rem;">Sun - Thu: 11:00 AM - 9:00 PM<br>Fri - Sat: 11:00 AM - 10:00 PM</p>
      </div>
    </div>
    <div class="impeck-footer-bottom">
      <p>&copy; 2026 Impeckable Chicken. All rights reserved. Culinary showcase demo for Charlotte, NC.</p>
    </div>
  </footer>
'''

pages = {
  'index.html': {
    'title': 'Impeckable Chicken - Hand-Breaded Crispy Chicken at Monarch Market Charlotte NC',
    'nav': {'index': 'active', 'menu': '', 'craft': '', 'sandwiches': '', 'wings': '', 'visit': ''},
    'body': '''
    <main>
      <section class="impeck-hero">
        <div class="impeck-hero-grid">
          <div class="impeck-hero-content">
            <span class="impeck-hero-badge">Monarch Market &bull; 101 N Tryon St Uptown</span>
            <h1 class="impeck-hero-title">Crispy, Juicy, <span>Impeckable Flavor</span></h1>
            <p class="impeck-hero-lead">Charlotte’s ultimate fried chicken experience. Double-dredged chicken tenders, gourmet brioche sandwiches, jumbo wings, and seasoned waffle fries fried golden to order.</p>
            <div class="impeck-hero-actions">
              <a href="menu.html" class="impeck-btn-primary">Explore Full Menu</a>
              <a href="sandwiches-and-tenders.html" class="impeck-btn-secondary">The Sandwich Lineup</a>
            </div>
          </div>
          <div class="impeck-hero-img-wrap">
            <img src="images/hero.jpg" alt="Towering crispy buttermilk fried chicken sandwich with pickles on toasted brioche" width="600" height="420">
          </div>
        </div>
      </section>

      <section class="impeck-features">
        <div class="impeck-feature-grid">
          <div class="impeck-feature-card">
            <div class="impeck-feature-tag">24-Hour Brine</div>
            <h2 class="impeck-feature-title">Spiced Buttermilk Soak</h2>
            <p class="impeck-feature-desc">Every piece of chicken is submerged in herb-infused buttermilk for maximum tenderness and deep moisture.</p>
          </div>
          <div class="impeck-feature-card">
            <div class="impeck-feature-tag">Double Dredged</div>
            <h2 class="impeck-feature-title">Ultra-Crunch Crust</h2>
            <p class="impeck-feature-desc">Seasoned flour dredge with secret spices creating a shatteringly crisp exterior that locks in savory juices.</p>
          </div>
          <div class="impeck-feature-card">
            <div class="impeck-feature-tag">Scratch Crafted</div>
            <h2 class="impeck-feature-title">Signature Sauces</h2>
            <p class="impeck-feature-desc">House Impeckable Sauce, Hot Honey drizzle, Carolina Gold, and Garlic Herb Ranch crafted daily.</p>
          </div>
        </div>
      </section>

      <section class="impeck-section">
        <div class="impeck-story-grid">
          <div class="impeck-story-img-wrap">
            <img src="images/tenders.jpg" alt="Golden crispy hand-breaded chicken tenders with dipping sauce" width="600" height="380">
          </div>
          <div class="impeck-story-content">
            <span class="impeck-section-eyebrow">Monarch Market Sensation</span>
            <h3>Hand-Breaded Tenders Done Right</h3>
            <p>At Impeckable Chicken, we refuse to cut corners. We use whole whole-muscle tenderloins, seasoned flour, and hot frying oil calibrated to perfection so every bite delivers a distinct crunch followed by steaming, juicy chicken.</p>
            <p>Served with our hot seasoned waffle fries and your choice of house-crafted dipping sauces, it is comfort food elevated for Uptown Charlotte food lovers.</p>
            <a href="wings-sides-and-sauces.html" class="impeck-btn-primary" style="margin-top: 0.5rem;">Explore Sauces &amp; Wings</a>
          </div>
        </div>
      </section>

      <section class="impeck-section" style="background: #ffffff; border-top: 1px solid var(--impeck-border); border-bottom: 1px solid var(--impeck-border);">
        <div class="impeck-section-header">
          <span class="impeck-section-eyebrow">Corporate Lunch &amp; Game Day Catering</span>
          <h2 class="impeck-section-title">Office Tender Platter Estimator</h2>
          <p class="impeck-section-subtitle">Hosting an office gathering, team celebration, or weekend tailgate? Calculate your crispy tender and side requirements below.</p>
        </div>

        <div class="impeck-calc-card">
          <div class="impeck-calc-controls">
            <div class="impeck-calc-field">
              <label for="impeck-guest-count">Headcount: <span id="impeck-guest-display" style="color: var(--impeck-primary); font-weight: 800;">20 People</span></label>
              <input type="range" id="impeck-guest-count" class="impeck-range-slider" min="5" max="80" step="5" value="20">
            </div>
            <div class="impeck-calc-field">
              <label for="impeck-platter-style">Platter Style</label>
              <select id="impeck-platter-style" class="impeck-calc-select">
                <option value="tenders-only">Crispy Tender Box (4 Tenders / Person)</option>
                <option value="tenders-wings">Combo Feast (3 Tenders + 2 Jumbo Wings / Person)</option>
              </select>
            </div>
          </div>
          <div class="impeck-calc-results">
            <div class="impeck-result-box">
              <span class="num" id="impeck-tender-total">80 Crispy Tenders</span>
              <span class="label">Hand-Breaded Tenders</span>
            </div>
            <div class="impeck-result-box">
              <span class="num" id="impeck-fry-total">7.0 lbs Seasoned Waffle Fries</span>
              <span class="label">Crisp Hot Sides</span>
            </div>
            <div class="impeck-result-box">
              <span class="num" id="impeck-sauce-total">40 Dipping Sauce Cups</span>
              <span class="label">House Dipping Sauces</span>
            </div>
          </div>
        </div>
      </section>
    </main>
'''
  },
  'menu.html': {
    'title': 'Menu - Impeckable Chicken Charlotte NC',
    'nav': {'index': '', 'menu': 'active', 'craft': '', 'sandwiches': '', 'wings': '', 'visit': ''},
    'body': '''
    <main class="impeck-section">
      <div class="impeck-section-header">
        <span class="impeck-section-eyebrow">Flavor-Packed Lineup</span>
        <h1 class="impeck-section-title">Impeckable Chicken Menu</h1>
        <p class="impeck-section-subtitle">Gourmet crispy chicken sandwiches, hand-breaded tender baskets, jumbo wings, and seasoned waffle fries.</p>
      </div>

      <div class="impeck-filter-tabs" role="tablist" aria-label="Menu Filter Tabs">
        <button type="button" class="impeck-filter-btn active" data-filter="all">All Selections</button>
        <button type="button" class="impeck-filter-btn" data-filter="sandwiches">Sandwiches</button>
        <button type="button" class="impeck-filter-btn" data-filter="tenders">Tender Plates</button>
        <button type="button" class="impeck-filter-btn" data-filter="wings">Jumbo Wings</button>
        <button type="button" class="impeck-filter-btn" data-filter="sides">Sides &amp; Sauces</button>
      </div>

      <div class="impeck-menu-grid">
        <div class="impeck-menu-item" data-category="sandwiches">
          <div class="impeck-menu-item-header">
            <span class="impeck-menu-item-name">The Impeckable Classic</span>
            <span class="impeck-menu-item-price">$12.50</span>
          </div>
          <p class="impeck-menu-item-desc">Giant buttermilk fried chicken breast, thick crinkle-cut dill pickles, and signature Impeckable sauce on a toasted buttered brioche bun with waffle fries.</p>
          <div class="impeck-menu-item-badges">
            <span class="impeck-badge impeck-badge-red">Top Seller</span>
            <span class="impeck-badge">Includes Fries</span>
          </div>
        </div>

        <div class="impeck-menu-item" data-category="sandwiches">
          <div class="impeck-menu-item-header">
            <span class="impeck-menu-item-name">Hot Honey Crunch</span>
            <span class="impeck-menu-item-price">$13.25</span>
          </div>
          <p class="impeck-menu-item-desc">Crispy fried chicken breast drenched in chili-infused wildflower honey, crunchy apple cider slaw, and roasted garlic aioli on brioche.</p>
          <div class="impeck-menu-item-badges">
            <span class="impeck-badge impeck-badge-gold">Sweet &amp; Spicy</span>
          </div>
        </div>

        <div class="impeck-menu-item" data-category="sandwiches">
          <div class="impeck-menu-item-header">
            <span class="impeck-menu-item-name">Nashville Fire Sandwich</span>
            <span class="impeck-menu-item-price">$13.50</span>
          </div>
          <p class="impeck-menu-item-desc">Dipped in authentic cayenne-lard spice glaze, loaded with double dill pickles and cool buttermilk ranch on toasted brioche.</p>
          <div class="impeck-menu-item-badges">
            <span class="impeck-badge impeck-badge-red">High Heat</span>
          </div>
        </div>

        <div class="impeck-menu-item" data-category="tenders">
          <div class="impeck-menu-item-header">
            <span class="impeck-menu-item-name">5-Piece Hand-Breaded Tender Plate</span>
            <span class="impeck-menu-item-price">$13.95</span>
          </div>
          <p class="impeck-menu-item-desc">Five crispy whole-muscle buttermilk tenders served with seasoned waffle fries, buttery Texas toast, and two house dipping sauces.</p>
          <div class="impeck-menu-item-badges">
            <span class="impeck-badge impeck-badge-red">Fan Favorite</span>
          </div>
        </div>

        <div class="impeck-menu-item" data-category="tenders">
          <div class="impeck-menu-item-header">
            <span class="impeck-menu-item-name">3-Piece Express Tender Box</span>
            <span class="impeck-menu-item-price">$10.50</span>
          </div>
          <p class="impeck-menu-item-desc">Three crispy chicken tenders with seasoned waffle fries, pickle chips, and one house dipping sauce for a swift lunch.</p>
          <div class="impeck-menu-item-badges">
            <span class="impeck-badge">Lunch Express</span>
          </div>
        </div>

        <div class="impeck-menu-item" data-category="wings">
          <div class="impeck-menu-item-header">
            <span class="impeck-menu-item-name">8 Jumbo Crispy Wings</span>
            <span class="impeck-menu-item-price">$14.50</span>
          </div>
          <p class="impeck-menu-item-desc">Jumbo bone-in wings fried extra crispy and tossed in your choice of Lemon Pepper Dry Rub, Buffalo, Hot Honey, or Carolina Gold.</p>
          <div class="impeck-menu-item-badges">
            <span class="impeck-badge impeck-badge-gold">Tossed to Order</span>
          </div>
        </div>

        <div class="impeck-menu-item" data-category="sides">
          <div class="impeck-menu-item-header">
            <span class="impeck-menu-item-name">Loaded Chicken Waffle Fries</span>
            <span class="impeck-menu-item-price">$9.95</span>
          </div>
          <p class="impeck-menu-item-desc">Crispy waffle fries smothered in chopped fried chicken tenders, warm cheddar cheese sauce, bacon crumbles, and ranch drizzle.</p>
          <div class="impeck-menu-item-badges">
            <span class="impeck-badge">Shareable</span>
          </div>
        </div>

        <div class="impeck-menu-item" data-category="sides">
          <div class="impeck-menu-item-header">
            <span class="impeck-menu-item-name">Southern Pimento Mac Bites (5)</span>
            <span class="impeck-menu-item-price">$6.75</span>
          </div>
          <p class="impeck-menu-item-desc">Creamy pimento cheese macaroni breaded in panko crumbs and fried golden brown with hot honey dip.</p>
          <div class="impeck-menu-item-badges">
            <span class="impeck-badge">Cheesy Starter</span>
          </div>
        </div>
      </div>
    </main>
'''
  },
  'buttermilk-craft-and-brine.html': {
    'title': 'Brine & Craft - Impeckable Chicken',
    'nav': {'index': '', 'menu': '', 'craft': 'active', 'sandwiches': '', 'wings': '', 'visit': ''},
    'body': '''
    <main class="impeck-section">
      <div class="impeck-section-header">
        <span class="impeck-section-eyebrow">Culinary Technique</span>
        <h1 class="impeck-section-title">The Science of Buttermilk Brining</h1>
        <p class="impeck-section-subtitle">How our 24-hour marination and double-dredge method produce unrivaled tenderness and crunch.</p>
      </div>

      <div class="impeck-story-grid">
        <div class="impeck-story-content">
          <h3>The 24-Hour Spiced Buttermilk Brine</h3>
          <p>Buttermilk is the secret soul of great Southern fried chicken. The natural lactic acid in whole cultured buttermilk gently breaks down muscle fibers without turning the meat stringy, while infusing moisture deep into every tender.</p>
          <p>We blend our buttermilk with sea salt, cracked black pepper, smoked paprika, garlic, and fresh thyme, allowing every batch to rest for a full 24 hours before cooking.</p>
        </div>
        <div class="impeck-story-img-wrap">
          <img src="images/sandwich.jpg" alt="Thick crispy chicken breast on toasted brioche bun" width="600" height="380">
        </div>
      </div>

      <div class="impeck-story-grid" style="margin-top: 4.5rem;">
        <div class="impeck-story-img-wrap">
          <img src="images/tenders.jpg" alt="Golden crispy tenders with crunchy double-dredged crust" width="600" height="380">
        </div>
        <div class="impeck-story-content">
          <h3>The Double-Dredge Technique</h3>
          <p>To achieve that signature jagged, ultra-crunchy crust, our chicken undergoes a rigorous two-step coating process.</p>
          <p>Dredged first in seasoned unbleached flour, dipped back into cold buttermilk wash, and pressed firmly into a second seasoned flour bath, creating ripples that fry into an airy, shatteringly crisp exterior that stays crunchy to the last bite.</p>
        </div>
      </div>
    </main>
'''
  },
  'sandwiches-and-tenders.html': {
    'title': 'Sandwiches & Tenders - Impeckable Chicken',
    'nav': {'index': '', 'menu': '', 'craft': '', 'sandwiches': 'active', 'wings': '', 'visit': ''},
    'body': '''
    <main class="impeck-section">
      <div class="impeck-section-header">
        <span class="impeck-section-eyebrow">Signature Creations</span>
        <h1 class="impeck-section-title">Sandwiches &amp; Hand-Breaded Tenders</h1>
        <p class="impeck-section-subtitle">Explore our chef-crafted brioche sandwiches and tender platters.</p>
      </div>

      <div class="impeck-story-grid">
        <div class="impeck-story-img-wrap">
          <img src="images/hero.jpg" alt="Crispy chicken sandwich with crinkle cut pickles and house sauce" width="600" height="380">
        </div>
        <div class="impeck-story-content">
          <h3>The Sandwich Showcase</h3>
          <p><strong>The Impeckable Classic:</strong> Our flagship sandwich featuring a jumbo buttermilk chicken breast, double thickness dill pickles, and creamy Impeckable sauce on a griddled brioche bun.</p>
          <p><strong>Hot Honey Crunch:</strong> Drizzled with warm chili honey and topped with cool house-made cider slaw for the perfect contrast of sweetness, heat, and crunch.</p>
          <p><strong>Nashville Fire:</strong> Dipped in hot pepper oil and seasoned with ghost-cayenne dust for serious spice lovers.</p>
        </div>
      </div>

      <div class="impeck-story-grid" style="margin-top: 4.5rem;">
        <div class="impeck-story-content">
          <h3>Whole-Muscle Tender Baskets</h3>
          <p>Never formed or processed, our tenders are 100% all-natural whole-muscle chicken tenderloins. Battered and fried fresh upon every order, our 3-piece, 5-piece, and 8-piece baskets are served alongside piping seasoned waffle fries and Texas toast.</p>
        </div>
        <div class="impeck-story-img-wrap">
          <img src="images/tenders.jpg" alt="Platter of golden brown crispy tenders with side sauces" width="600" height="380">
        </div>
      </div>
    </main>
'''
  },
  'wings-sides-and-sauces.html': {
    'title': 'Wings, Sides & Sauces - Impeckable Chicken',
    'nav': {'index': '', 'menu': '', 'craft': '', 'sandwiches': '', 'wings': 'active', 'visit': ''},
    'body': '''
    <main class="impeck-section">
      <div class="impeck-section-header">
        <span class="impeck-section-eyebrow">Complements &amp; Sauces</span>
        <h1 class="impeck-section-title">Jumbo Wings, Sides &amp; House Sauces</h1>
        <p class="impeck-section-subtitle">Crispy seasoned wings, waffle fries, and scratch dipping sauces.</p>
      </div>

      <div class="impeck-story-grid">
        <div class="impeck-story-content">
          <h3>Jumbo Crispy Wings</h3>
          <p>Our jumbo chicken wings are cooked to a golden crisp and tossed in signature rubs and glazes:</p>
          <p><strong>Lemon Pepper Dry Rub:</strong> Tangy lemon zest, cracked black pepper, and garlic herb seasoning.</p>
          <p><strong>Carolina Gold BBQ:</strong> Mustard-forward barbecue sauce with a touch of brown sugar sweetness and vinegar tang.</p>
          <p><strong>Sweet Heat Buffalo:</strong> Classic aged cayenne hot sauce enriched with pure butter and wildflower honey.</p>
        </div>
        <div class="impeck-story-img-wrap">
          <img src="images/wings.jpg" alt="Crispy tossed chicken wings garnished with herbs" width="600" height="380">
        </div>
      </div>

      <div class="impeck-story-grid" style="margin-top: 4.5rem;">
        <div class="impeck-story-img-wrap">
          <img src="images/sides.jpg" alt="Seasoned waffle fries with dipping sauce cups" width="600" height="380">
        </div>
        <div class="impeck-story-content">
          <h3>Scratch Dipping Sauces</h3>
          <p><strong>Impeckable House Sauce:</strong> Creamy, peppery, and tangy with a hint of garlic and horseradish.</p>
          <p><strong>Garlic Herb Buttermilk Ranch:</strong> Made fresh daily with dill, chives, buttermilk, and roasted garlic.</p>
          <p><strong>Hot Honey Drizzle:</strong> Pure wildflower honey infused with habanero and red pepper flakes.</p>
        </div>
      </div>
    </main>
'''
  },
  'visit.html': {
    'title': 'Visit & Order - Impeckable Chicken Charlotte NC',
    'nav': {'index': '', 'menu': '', 'craft': '', 'sandwiches': '', 'wings': '', 'visit': 'active'},
    'body': '''
    <main class="impeck-section">
      <div class="impeck-section-header">
        <span class="impeck-section-eyebrow">Monarch Market Uptown</span>
        <h1 class="impeck-section-title">Visit Impeckable Chicken</h1>
        <p class="impeck-section-subtitle">Located inside Monarch Market at One South Tryon (101 N Tryon St). Dine in at the food hall or order online for fast pickup.</p>
      </div>

      <div class="impeck-contact-grid">
        <div class="impeck-contact-card">
          <h3>Monarch Market Food Hall</h3>
          <p style="color: var(--impeck-text-muted); margin-bottom: 0.8rem;">Conveniently located at the intersection of Trade and Tryon in the heart of Uptown Charlotte.</p>
          <p><strong>Address:</strong> 101 N Tryon St, Charlotte, NC 28202</p>
          <p style="margin-top: 0.4rem;"><strong>Setting:</strong> Vibrant culinary food hall with indoor seating, bar seating, and outdoor patio plaza.</p>
          <div style="margin-top: 1.5rem;">
            <a href="tel:7049101500" class="impeck-btn-primary" style="width: 100%; text-align: center;">Call Stall: (704) 910-1500</a>
          </div>
        </div>

        <div class="impeck-contact-card">
          <h3>Operating Hours</h3>
          <div class="impeck-hours-row">
            <span>Sunday &ndash; Thursday</span>
            <span>11:00 AM &ndash; 9:00 PM</span>
          </div>
          <div class="impeck-hours-row">
            <span>Friday &ndash; Saturday</span>
            <span>11:00 AM &ndash; 10:00 PM</span>
          </div>
          <div style="margin-top: 1.5rem; background: var(--impeck-surface-alt); padding: 1rem; border-radius: var(--impeck-radius-sm);">
            <p style="font-size: 0.85rem; color: var(--impeck-primary-dark); font-weight: 700;">Fast counter turnaround. Online pickup available through Monarch Market digital ordering.</p>
          </div>
        </div>

        <div class="impeck-contact-card">
          <h3>Office &amp; Party Catering</h3>
          <p style="color: var(--impeck-text-muted); margin-bottom: 0.8rem;">Large tender platters, boxed chicken sandwich combos, and jumbo wing trays for Uptown corporate lunches and private celebrations.</p>
          <p><strong>Notice:</strong> Catering orders recommended 24 hours in advance.</p>
          <div style="margin-top: 1.5rem;">
            <a href="mailto:catering@impeckablechickenclt.com" class="impeck-btn-secondary" style="width: 100%; text-align: center;">Inquire for Catering</a>
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
    nav_craft=data['nav']['craft'],
    nav_sandwiches=data['nav']['sandwiches'],
    nav_wings=data['nav']['wings'],
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
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="site.css">
</head>
<body>
  <header class="impeck-header">
    <div class="impeck-nav-container">
      <a href="index.html" class="impeck-brand">
        <span class="impeck-brand-title">Impeckable Chicken</span>
        <span class="impeck-brand-subtitle">Monarch Market &bull; Uptown Charlotte</span>
      </a>
      <button class="impeck-nav-toggle" type="button" aria-label="Toggle navigation menu" aria-expanded="false">Menu</button>
{cur_nav}
    </div>
  </header>

{data['body']}

{footer_content}
  <script src="site.js"></script>
</body>
</html>'''

  filepath = os.path.join('impeckable-chicken', filename)
  with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html_doc.strip() + '\n')
  print(f'Wrote {filename}')

print('All 6 HTML pages for Impeckable Chicken written successfully')
