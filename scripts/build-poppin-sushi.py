import os

nav_template = '''
      <nav class="poppin-nav" aria-label="Primary Navigation">
        <ul class="poppin-nav-list">
          <li><a href="index.html" class="poppin-nav-link {nav_index}">Home</a></li>
          <li><a href="menu.html" class="poppin-nav-link {nav_menu}">Menu</a></li>
          <li><a href="poke-craft-and-quality.html" class="poppin-nav-link {nav_craft}">Poke Craft</a></li>
          <li><a href="specialty-sushi-rolls.html" class="poppin-nav-link {nav_sushi}">Specialty Rolls</a></li>
          <li><a href="appetizers-and-sides.html" class="poppin-nav-link {nav_apps}">Starters &amp; Sides</a></li>
          <li><a href="visit.html" class="poppin-nav-link poppin-nav-cta {nav_visit}">Visit &amp; Order</a></li>
        </ul>
      </nav>
'''

footer_content = '''
  <footer class="poppin-footer">
    <div class="poppin-footer-container">
      <div class="poppin-footer-brand">
        <h4>Poppin Sushi &amp; Poke</h4>
        <p>Fresh-catch poke bowls, creative chef-crafted maki rolls, and Japanese street starters in the heart of Uptown Charlotte, North Carolina.</p>
      </div>
      <div class="poppin-footer-nav">
        <h5>Explore Demo</h5>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Full Menu</a></li>
          <li><a href="poke-craft-and-quality.html">Poke Craft &amp; Quality</a></li>
          <li><a href="specialty-sushi-rolls.html">Specialty Rolls</a></li>
          <li><a href="appetizers-and-sides.html">Starters &amp; Sides</a></li>
          <li><a href="visit.html">Location &amp; Hours</a></li>
        </ul>
      </div>
      <div class="poppin-footer-hours">
        <h5>Location &amp; Contact</h5>
        <p style="color: #8fa5ac; font-size: 0.88rem; margin-bottom: 0.4rem;"><strong>Uptown Charlotte:</strong> 210 N Church St, Suite B</p>
        <p style="color: #8fa5ac; font-size: 0.88rem; margin-bottom: 0.4rem;"><strong>Direct Phone:</strong> (704) 372-2828</p>
        <p style="color: #8fa5ac; font-size: 0.88rem;">Mon - Fri: 11:00 AM - 8:30 PM<br>Saturday: 12:00 PM - 8:00 PM<br>Sunday: Closed</p>
      </div>
    </div>
    <div class="poppin-footer-bottom">
      <p>&copy; 2026 Poppin Sushi &amp; Poke. All rights reserved. Restaurant showcase demo for Charlotte, NC.</p>
    </div>
  </footer>
'''

pages = {
  'index.html': {
    'title': 'Poppin Sushi & Poke - Fresh Poke Bowls & Specialty Sushi in Uptown Charlotte NC',
    'nav': {'index': 'active', 'menu': '', 'craft': '', 'sushi': '', 'apps': '', 'visit': ''},
    'body': '''
    <main>
      <section class="poppin-hero">
        <div class="poppin-hero-grid">
          <div class="poppin-hero-content">
            <span class="poppin-hero-badge">Uptown Charlotte &bull; 210 N Church St</span>
            <h1 class="poppin-hero-title">Fresh Ocean Flavors, <span>Rolled to Order</span></h1>
            <p class="poppin-hero-lead">Experience Charlotte’s premier fast-casual poke bar and sushi kitchen. Savor sustainably sourced ahi tuna, Atlantic salmon, house-made sauces, and creative specialty maki.</p>
            <div class="poppin-hero-actions">
              <a href="menu.html" class="poppin-btn-primary">View Full Menu</a>
              <a href="poke-craft-and-quality.html" class="poppin-btn-secondary">Our Fresh Craft</a>
            </div>
          </div>
          <div class="poppin-hero-img-wrap">
            <img src="images/hero.jpg" alt="Vibrant fresh poke bowl loaded with salmon, avocado, edamame, and sesame toppings" width="600" height="420">
          </div>
        </div>
      </section>

      <section class="poppin-features">
        <div class="poppin-feature-grid">
          <div class="poppin-feature-card">
            <div class="poppin-feature-tag">Sustainably Sourced</div>
            <h2 class="poppin-feature-title">Sushi-Grade Catch</h2>
            <p class="poppin-feature-desc">Yellowfin ahi tuna, rich Atlantic salmon, and tender yellowtail sliced fresh each morning.</p>
          </div>
          <div class="poppin-feature-card">
            <div class="poppin-feature-tag">Custom Crafted</div>
            <h2 class="poppin-feature-title">Build Your Own Poke</h2>
            <p class="poppin-feature-desc">Choose your base, premium proteins, fresh mix-ins, house ponzu dressings, and crunchy toppers.</p>
          </div>
          <div class="poppin-feature-card">
            <div class="poppin-feature-tag">Chef Maki</div>
            <h2 class="poppin-feature-title">Specialty Sushi Rolls</h2>
            <p class="poppin-feature-desc">From the fiery Poppin Crunch to the Uptown Dragon, our maki combines crunch, spice, and freshness.</p>
          </div>
        </div>
      </section>

      <section class="poppin-section">
        <div class="poppin-story-grid">
          <div class="poppin-story-img-wrap">
            <img src="images/poke.jpg" alt="Ahi tuna and salmon poke bowl topped with avocado and seaweed salad" width="600" height="380">
          </div>
          <div class="poppin-story-content">
            <span class="poppin-section-eyebrow">Pure Refreshment</span>
            <h3>Wholesome Nutrition Packed with Flavor</h3>
            <p>At Poppin Sushi &amp; Poke, healthy eating never means compromising on vibrant taste. Our Hawaiian-inspired poke bowls are layered with nutrient-rich proteins, crisp cucumbers, creamy avocado, and antioxidant-loaded seaweed salad.</p>
            <p>Paired with our scratch citrus shoyu, spicy sesame mayo, or roasted unagi drizzle, every bowl is a colorful masterpiece tailored to your palate.</p>
            <a href="specialty-sushi-rolls.html" class="poppin-btn-primary" style="margin-top: 0.5rem;">Explore Signature Rolls</a>
          </div>
        </div>
      </section>

      <section class="poppin-section" style="background: #ffffff; border-top: 1px solid var(--poppin-border); border-bottom: 1px solid var(--poppin-border);">
        <div class="poppin-section-header">
          <span class="poppin-section-eyebrow">Corporate &amp; Party Catering</span>
          <h2 class="poppin-section-title">Uptown Sushi &amp; Poke Platter Estimator</h2>
          <p class="poppin-section-subtitle">Hosting a team lunch, client meeting, or celebration? Calculate your party sushi platter and poke bowl counts below.</p>
        </div>

        <div class="poppin-calc-card">
          <div class="poppin-calc-controls">
            <div class="poppin-calc-field">
              <label for="poppin-guest-count">Number of Guests: <span id="poppin-guest-display" style="color: var(--poppin-primary); font-weight: 800;">15 Guests</span></label>
              <input type="range" id="poppin-guest-count" class="poppin-range-slider" min="5" max="60" step="5" value="15">
            </div>
            <div class="poppin-calc-field">
              <label for="poppin-platter-style">Menu Focus</label>
              <select id="poppin-platter-style" class="poppin-calc-select">
                <option value="balanced">Balanced Mix (Sushi Rolls &amp; Mini Poke Bowls)</option>
                <option value="rolls">Maki Platter Focus (Assorted Specialty Rolls)</option>
              </select>
            </div>
          </div>
          <div class="poppin-calc-results">
            <div class="poppin-result-box">
              <span class="num" id="poppin-roll-total">90 Specialty Roll Pieces</span>
              <span class="label">Chef Maki Cuts</span>
            </div>
            <div class="poppin-result-box">
              <span class="num" id="poppin-poke-total">11 Mini Poke Bowls</span>
              <span class="label">Custom Poke Cups</span>
            </div>
            <div class="poppin-result-box">
              <span class="num" id="poppin-gyoza-total">30 Pan-Seared Gyoza</span>
              <span class="label">Warm Starters</span>
            </div>
          </div>
        </div>
      </section>
    </main>
'''
  },
  'menu.html': {
    'title': 'Menu - Poppin Sushi & Poke Charlotte NC',
    'nav': {'index': '', 'menu': 'active', 'craft': '', 'sushi': '', 'apps': '', 'visit': ''},
    'body': '''
    <main class="poppin-section">
      <div class="poppin-section-header">
        <span class="poppin-section-eyebrow">Fresh Offerings</span>
        <h1 class="poppin-section-title">Poppin Sushi &amp; Poke Menu</h1>
        <p class="poppin-section-subtitle">Signature poke bowls, custom build options, specialty rolls, and authentic Japanese starters.</p>
      </div>

      <div class="poppin-filter-tabs" role="tablist" aria-label="Menu Filter Tabs">
        <button type="button" class="poppin-filter-btn active" data-filter="all">All Selections</button>
        <button type="button" class="poppin-filter-btn" data-filter="poke">Signature Poke Bowls</button>
        <button type="button" class="poppin-filter-btn" data-filter="maki">Specialty Maki Rolls</button>
        <button type="button" class="poppin-filter-btn" data-filter="classic">Classic Sushi</button>
        <button type="button" class="poppin-filter-btn" data-filter="apps">Starters &amp; Drinks</button>
      </div>

      <div class="poppin-menu-grid">
        <div class="poppin-menu-item" data-category="poke">
          <div class="poppin-menu-item-header">
            <span class="poppin-menu-item-name">The Poppin Classic Poke</span>
            <span class="poppin-menu-item-price">$14.95</span>
          </div>
          <p class="poppin-menu-item-desc">Fresh ahi tuna &amp; Atlantic salmon on seasoned sushi rice with edamame, cucumber, sweet onions, avocado, house sesame shoyu, and crispy tempura flakes.</p>
          <div class="poppin-menu-item-badges">
            <span class="poppin-badge poppin-badge-coral">House Signature</span>
            <span class="poppin-badge">High Protein</span>
          </div>
        </div>

        <div class="poppin-menu-item" data-category="poke">
          <div class="poppin-menu-item-header">
            <span class="poppin-menu-item-name">Spicy Salmon &amp; Crab Crunch</span>
            <span class="poppin-menu-item-price">$14.50</span>
          </div>
          <p class="poppin-menu-item-desc">Spicy diced salmon, snow crab salad, avocado, jalapeño slices, masago, spicy aioli, and unagi drizzle over warm brown rice.</p>
          <div class="poppin-menu-item-badges">
            <span class="poppin-badge poppin-badge-coral">Spicy Kick</span>
          </div>
        </div>

        <div class="poppin-menu-item" data-category="poke">
          <div class="poppin-menu-item-header">
            <span class="poppin-menu-item-name">Zen Vegan Tofu Bowl</span>
            <span class="poppin-menu-item-price">$12.95</span>
          </div>
          <p class="poppin-menu-item-desc">Organic ginger-marinated tofu over mixed greens, edamame, shredded carrots, avocado, seaweed salad, and citrus ponzu dressing.</p>
          <div class="poppin-menu-item-badges">
            <span class="poppin-badge poppin-badge-gold">100% Plant-Based</span>
          </div>
        </div>

        <div class="poppin-menu-item" data-category="maki">
          <div class="poppin-menu-item-header">
            <span class="poppin-menu-item-name">Poppin Crunch Roll (8 pcs)</span>
            <span class="poppin-menu-item-price">$15.25</span>
          </div>
          <p class="poppin-menu-item-desc">Shrimp tempura and avocado inside, topped with spicy tuna, crispy sweet potato strings, scallions, spicy mayo, and eel sauce.</p>
          <div class="poppin-menu-item-badges">
            <span class="poppin-badge poppin-badge-coral">Top Seller</span>
          </div>
        </div>

        <div class="poppin-menu-item" data-category="maki">
          <div class="poppin-menu-item-header">
            <span class="poppin-menu-item-name">Church Street Dragon Roll</span>
            <span class="poppin-menu-item-price">$15.95</span>
          </div>
          <p class="poppin-menu-item-desc">Crisp tempura soft shell crab and cucumber topped with grilled barbecue unagi, avocado ribbons, toasted sesame, and sweet glaze.</p>
          <div class="poppin-menu-item-badges">
            <span class="poppin-badge">Chef Specialty</span>
          </div>
        </div>

        <div class="poppin-menu-item" data-category="classic">
          <div class="poppin-menu-item-header">
            <span class="poppin-menu-item-name">Rainbow Roll (8 pcs)</span>
            <span class="poppin-menu-item-price">$14.75</span>
          </div>
          <p class="poppin-menu-item-desc">Crab salad and cucumber roll draped in fresh ahi tuna, Atlantic salmon, yellowtail, and ripe avocado slices.</p>
          <div class="poppin-menu-item-badges">
            <span class="poppin-badge">Sashimi Lover</span>
          </div>
        </div>

        <div class="poppin-menu-item" data-category="apps">
          <div class="poppin-menu-item-header">
            <span class="poppin-menu-item-name">Pan-Seared Pork Gyoza (6)</span>
            <span class="poppin-menu-item-price">$7.50</span>
          </div>
          <p class="poppin-menu-item-desc">Japanese dumplings stuffed with seasoned pork and scallions, crisped golden on the griddle with sesame dipping sauce.</p>
          <div class="poppin-menu-item-badges">
            <span class="poppin-badge">Warm Starter</span>
          </div>
        </div>

        <div class="poppin-menu-item" data-category="apps">
          <div class="poppin-menu-item-header">
            <span class="poppin-menu-item-name">Sesame Seaweed Salad</span>
            <span class="poppin-menu-item-price">$5.95</span>
          </div>
          <p class="poppin-menu-item-desc">Tender wakame seaweed tossed with toasted sesame oil, rice vinegar, and a pinch of red chili flakes.</p>
          <div class="poppin-menu-item-badges">
            <span class="poppin-badge poppin-badge-gold">Light &amp; Crisp</span>
          </div>
        </div>
      </div>
    </main>
'''
  },
  'poke-craft-and-quality.html': {
    'title': 'Poke Craft & Quality - Poppin Sushi & Poke',
    'nav': {'index': '', 'menu': '', 'craft': 'active', 'sushi': '', 'apps': '', 'visit': ''},
    'body': '''
    <main class="poppin-section">
      <div class="poppin-section-header">
        <span class="poppin-section-eyebrow">Our Philosophy &amp; Sourcing</span>
        <h1 class="poppin-section-title">The Craft of Fresh Poke &amp; Sushi</h1>
        <p class="poppin-section-subtitle">How premium raw ingredients, traditional Japanese techniques, and modern flavor profiles come together.</p>
      </div>

      <div class="poppin-story-grid">
        <div class="poppin-story-content">
          <h3>Sushi-Grade Sourcing Standards</h3>
          <p>Great sushi and poke start with impeccable seafood. We partner exclusively with certified sustainable fisheries to source pristine yellowfin ahi tuna, rich cold-water Atlantic salmon, and hamachi yellowtail.</p>
          <p>Delivered fresh daily, our fish undergoes rigorous temperature controls and is hand-filleted by skilled culinary staff each morning, ensuring pure texture, vibrant color, and clean flavor in every bite.</p>
        </div>
        <div class="poppin-story-img-wrap">
          <img src="images/ingredients.jpg" alt="Sushi grade salmon, tuna, and fresh bowl toppings" width="600" height="380">
        </div>
      </div>

      <div class="poppin-story-grid" style="margin-top: 4.5rem;">
        <div class="poppin-story-img-wrap">
          <img src="images/poke.jpg" alt="Beautifully composed poke bowl with sesame glaze and fresh garnishes" width="600" height="380">
        </div>
        <div class="poppin-story-content">
          <h3>House-Blended Sauces &amp; Toppings</h3>
          <p>A poke bowl is only as good as its dressing. We formulate our sauces in-house using authentic Japanese mirin, barrel-aged tamari, yuzu juice, and toasted sesame oil.</p>
          <p>From our light, tangy Citrus Ponzu to our velvety Spicy Mayo and savory Sweet Unagi Glaze, our dressings accentuate the natural delicacy of the seafood without overpowering it.</p>
        </div>
      </div>
    </main>
'''
  },
  'specialty-sushi-rolls.html': {
    'title': 'Specialty Sushi Rolls - Poppin Sushi & Poke',
    'nav': {'index': '', 'menu': '', 'craft': '', 'sushi': 'active', 'apps': '', 'visit': ''},
    'body': '''
    <main class="poppin-section">
      <div class="poppin-section-header">
        <span class="poppin-section-eyebrow">Chef Creations</span>
        <h1 class="poppin-section-title">Specialty Sushi Rolls Showcase</h1>
        <p class="poppin-section-subtitle">Explore our signature maki rolls crafted with premium ingredients and dynamic flavor combinations.</p>
      </div>

      <div class="poppin-story-grid">
        <div class="poppin-story-img-wrap">
          <img src="images/sushi.jpg" alt="Artfully plated specialty sushi rolls garnished with microgreens and sauce" width="600" height="380">
        </div>
        <div class="poppin-story-content">
          <h3>Signature Roll Highlights</h3>
          <p><strong>The Poppin Crunch Roll:</strong> Golden crispy shrimp tempura and avocado rolled inside, topped with spicy chopped ahi tuna, crispy shredded sweet potato, spicy mayo, and sweet eel glaze.</p>
          <p><strong>Church Street Dragon:</strong> Crispy soft shell crab and cool cucumber draped in savory unagi barbecue eel, sliced ripe avocado, and toasted sesame seeds.</p>
          <p><strong>Fire Salmon Roll:</strong> Spicy salmon and cucumber topped with torched salmon belly, jalapeño rings, sriracha dots, and citrus ponzu sauce.</p>
        </div>
      </div>

      <div class="poppin-story-grid" style="margin-top: 4.5rem;">
        <div class="poppin-story-content">
          <h3>Classic Maki &amp; Fresh Nigiri</h3>
          <p>For purists, we offer meticulously prepared traditional rolls and nigiri pairs. Enjoy classic California rolls with genuine snow crab, Spicy Tuna maki, and buttery Atlantic salmon nigiri served over seasoned sushi rice seasoned with rice vinegar and sea salt.</p>
        </div>
        <div class="poppin-story-img-wrap">
          <img src="images/hero.jpg" alt="Sushi and poke platter showcase" width="600" height="380">
        </div>
      </div>
    </main>
'''
  },
  'appetizers-and-sides.html': {
    'title': 'Starters & Sides - Poppin Sushi & Poke',
    'nav': {'index': '', 'menu': '', 'craft': '', 'sushi': '', 'apps': 'active', 'visit': ''},
    'body': '''
    <main class="poppin-section">
      <div class="poppin-section-header">
        <span class="poppin-section-eyebrow">Japanese Small Bites</span>
        <h1 class="poppin-section-title">Starters, Sides &amp; Refreshments</h1>
        <p class="poppin-section-subtitle">Crispy dumplings, nourishing miso soup, and refreshing Japanese beverages.</p>
      </div>

      <div class="poppin-story-grid">
        <div class="poppin-story-content">
          <h3>Japanese Street Starters</h3>
          <p><strong>Pan-Seared Gyoza:</strong> Pork or vegetable dumplings pan-crisped to order, served with seasoned soy-sesame dip.</p>
          <p><strong>Steamed Edamame:</strong> Tender whole soybean pods steamed fresh and tossed in coarse sea salt or spicy garlic shoyu.</p>
          <p><strong>Wakame Seaweed Salad:</strong> Chilled seaweed marinated in sesame oil, rice vinegar, and mirin with toasted sesame seeds.</p>
          <p><strong>Traditional Miso Soup:</strong> Dashi broth infused with red and white miso, silken tofu cubes, wakame, and fresh scallions.</p>
        </div>
        <div class="poppin-story-img-wrap">
          <img src="images/appetizers.jpg" alt="Warm pan seared gyoza dumplings and edamame" width="600" height="380">
        </div>
      </div>

      <div class="poppin-story-grid" style="margin-top: 4.5rem;">
        <div class="poppin-story-img-wrap">
          <img src="images/poke.jpg" alt="Healthy fresh bowl complement" width="600" height="380">
        </div>
        <div class="poppin-story-content">
          <h3>Japanese Teas &amp; Drinks</h3>
          <p>Complement your meal with cold-steeped Japanese green tea, sparkling yuzu lemonades, Calpico fruit refreshments, or Ramune Japanese sodas.</p>
        </div>
      </div>
    </main>
'''
  },
  'visit.html': {
    'title': 'Visit & Order - Poppin Sushi & Poke Charlotte NC',
    'nav': {'index': '', 'menu': '', 'craft': '', 'sushi': '', 'apps': '', 'visit': 'active'},
    'body': '''
    <main class="poppin-section">
      <div class="poppin-section-header">
        <span class="poppin-section-eyebrow">Dine In &bull; Takeout &bull; Catering</span>
        <h1 class="poppin-section-title">Visit Poppin Sushi &amp; Poke</h1>
        <p class="poppin-section-subtitle">Located in Uptown Charlotte at 210 N Church St, Suite B. Stop in for lunch, dinner, or order ahead for express pickup.</p>
      </div>

      <div class="poppin-contact-grid">
        <div class="poppin-contact-card">
          <h3>Uptown Charlotte Location</h3>
          <p style="color: var(--poppin-text-muted); margin-bottom: 0.8rem;">Conveniently located near Fourth Ward Park, Tryon Street offices, and Uptown transit.</p>
          <p><strong>Address:</strong> 210 N Church St, Suite B, Charlotte, NC 28202</p>
          <p style="margin-top: 0.4rem;"><strong>Setting:</strong> Fast-casual counter with modern dine-in tables and swift pickup rack.</p>
          <div style="margin-top: 1.5rem;">
            <a href="tel:7043722828" class="poppin-btn-primary" style="width: 100%; text-align: center;">Call to Order: (704) 372-2828</a>
          </div>
        </div>

        <div class="poppin-contact-card">
          <h3>Operating Hours</h3>
          <div class="poppin-hours-row">
            <span>Monday &ndash; Friday</span>
            <span>11:00 AM &ndash; 8:30 PM</span>
          </div>
          <div class="poppin-hours-row">
            <span>Saturday</span>
            <span>12:00 PM &ndash; 8:00 PM</span>
          </div>
          <div class="poppin-hours-row">
            <span>Sunday</span>
            <span>Closed</span>
          </div>
          <div style="margin-top: 1.5rem; background: var(--poppin-surface-alt); padding: 1rem; border-radius: var(--poppin-radius-sm);">
            <p style="font-size: 0.85rem; color: var(--poppin-primary-dark); font-weight: 700;">Online pickup and phone orders ready in 15 minutes. High-efficiency lunch rush fulfillment.</p>
          </div>
        </div>

        <div class="poppin-contact-card">
          <h3>Corporate &amp; Event Catering</h3>
          <p style="color: var(--poppin-text-muted); margin-bottom: 0.8rem;">Assorted specialty roll platters, mini poke bowl stations, and individual bento boxes for Uptown business meetings and private parties.</p>
          <p><strong>Notice:</strong> Catering orders recommended 24 hours in advance.</p>
          <div style="margin-top: 1.5rem;">
            <a href="mailto:catering@poppinsushipoke.com" class="poppin-btn-secondary" style="width: 100%; text-align: center;">Inquire for Catering</a>
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
    nav_sushi=data['nav']['sushi'],
    nav_apps=data['nav']['apps'],
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
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="site.css">
</head>
<body>
  <header class="poppin-header">
    <div class="poppin-nav-container">
      <a href="index.html" class="poppin-brand">
        <span class="poppin-brand-title">Poppin Sushi &amp; Poke</span>
        <span class="poppin-brand-subtitle">Fresh Poke &amp; Specialty Maki</span>
      </a>
      <button class="poppin-nav-toggle" type="button" aria-label="Toggle navigation menu" aria-expanded="false">Menu</button>
{cur_nav}
    </div>
  </header>

{data['body']}

{footer_content}
  <script src="site.js"></script>
</body>
</html>'''

  filepath = os.path.join('poppin-sushi-and-poke', filename)
  with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html_doc.strip() + '\n')
  print(f'Wrote {filename}')

print('All 6 HTML pages for Poppin Sushi & Poke written successfully')
