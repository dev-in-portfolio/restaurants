import os

nav_template = '''
      <nav class="jamile-nav" aria-label="Primary Navigation">
        <ul class="jamile-nav-list">
          <li><a href="index.html" class="jamile-nav-link {nav_index}">Home</a></li>
          <li><a href="menu.html" class="jamile-nav-link {nav_menu}">Menu</a></li>
          <li><a href="somali-culinary-heritage.html" class="jamile-nav-link {nav_heritage}">Heritage</a></li>
          <li><a href="goat-and-spiced-rice.html" class="jamile-nav-link {nav_goat}">Goat &amp; Spiced Rice</a></li>
          <li><a href="sambusas-and-shaah-tea.html" class="jamile-nav-link {nav_tea}">Sambusas &amp; Tea</a></li>
          <li><a href="visit.html" class="jamile-nav-link jamile-nav-cta {nav_visit}">Visit &amp; Order</a></li>
        </ul>
      </nav>
'''

footer_content = '''
  <footer class="jamile-footer">
    <div class="jamile-footer-container">
      <div class="jamile-footer-brand">
        <h4>Jamile’s Cuisine International</h4>
        <p>Authentic Somali and East African halal cuisine on Charlotte’s Central Avenue. Serving slow-braised goat, fragrant cardamom rice, crispy sambusas, and traditional spiced milk tea.</p>
      </div>
      <div class="jamile-footer-nav">
        <h5>Explore Demo</h5>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Full Menu</a></li>
          <li><a href="somali-culinary-heritage.html">Somali Heritage</a></li>
          <li><a href="goat-and-spiced-rice.html">Goat &amp; Spiced Rice</a></li>
          <li><a href="sambusas-and-shaah-tea.html">Sambusas &amp; Tea</a></li>
          <li><a href="visit.html">Location &amp; Hours</a></li>
        </ul>
      </div>
      <div class="jamile-footer-hours">
        <h5>Location &amp; Hours</h5>
        <p style="color: #9a9ea6; font-size: 0.88rem; margin-bottom: 0.4rem;"><strong>East Charlotte:</strong> 4808 Central Ave, Ste G</p>
        <p style="color: #9a9ea6; font-size: 0.88rem; margin-bottom: 0.4rem;"><strong>Direct Phone:</strong> (704) 531-1180</p>
        <p style="color: #9a9ea6; font-size: 0.88rem;">Tue - Sun: 12:00 PM - 8:00 PM<br>Monday: Closed</p>
      </div>
    </div>
    <div class="jamile-footer-bottom">
      <p>&copy; 2026 Jamile’s Cuisine International. All rights reserved. East African culinary showcase demo for Charlotte, NC.</p>
    </div>
  </footer>
'''

pages = {
  'index.html': {
    'title': 'Jamile’s Cuisine International - Authentic Somali Restaurant in Charlotte NC',
    'nav': {'index': 'active', 'menu': '', 'heritage': '', 'goat': '', 'tea': '', 'visit': ''},
    'body': '''
    <main>
      <section class="jamile-hero">
        <div class="jamile-hero-grid">
          <div class="jamile-hero-content">
            <span class="jamile-hero-badge">Central Avenue &bull; Authentic Somali Halal Cuisine</span>
            <h1 class="jamile-hero-title">Fragrant Spices, <span>Tender Braised Meats</span></h1>
            <p class="jamile-hero-lead">Step into East African hospitality on Central Avenue. Enjoy slow-roasted Somali goat meat (Hilib Ari), cardamom-scented Bariis Iskukaris rice, hand-folded beef sambusas, and freshly brewed spiced milk tea.</p>
            <div class="jamile-hero-actions">
              <a href="menu.html" class="jamile-btn-primary">View Full Menu</a>
              <a href="goat-and-spiced-rice.html" class="jamile-btn-secondary">The Goat &amp; Rice Feast</a>
            </div>
          </div>
          <div class="jamile-hero-img-wrap">
            <img src="images/hero.jpg" alt="Fragrant Somali spiced basmati rice platter with tender braised goat meat and roasted vegetables" width="600" height="420">
          </div>
        </div>
      </section>

      <section class="jamile-features">
        <div class="jamile-feature-grid">
          <div class="jamile-feature-card">
            <div class="jamile-feature-tag">100% Halal</div>
            <h2 class="jamile-feature-title">Slow-Roasted Hilib Ari</h2>
            <p class="jamile-feature-desc">Bone-in goat meat gently braised with garlic, cloves, and Xawaash spice until fork-tender and aromatic.</p>
          </div>
          <div class="jamile-feature-card">
            <div class="jamile-feature-tag">Cardamom &amp; Cinnamon</div>
            <h2 class="jamile-feature-title">Bariis Iskukaris Rice</h2>
            <p class="jamile-feature-desc">Golden long-grain basmati steamed with raisins, sweet onions, and whole spices, traditionally served with fresh banana.</p>
          </div>
          <div class="jamile-feature-card">
            <div class="jamile-feature-tag">Hand-Crafted</div>
            <h2 class="jamile-feature-title">Crispy Sambusas</h2>
            <p class="jamile-feature-desc">Golden pastry triangles filled with seasoned ground beef and jalapeños, paired with spicy green Basbaas sauce.</p>
          </div>
        </div>
      </section>

      <section class="jamile-section">
        <div class="jamile-story-grid">
          <div class="jamile-story-img-wrap">
            <img src="images/goat.jpg" alt="Tender roasted Somali goat shank served over spiced basmati rice" width="600" height="380">
          </div>
          <div class="jamile-story-content">
            <span class="jamile-section-eyebrow">East African Tradition</span>
            <h3>Communal Dining on Central Avenue</h3>
            <p>In Somali culture, sharing a meal is an expression of deep warmth and connection. At Jamile’s Cuisine International, our generous platters are crafted for family and friends to gather around.</p>
            <p>Every dish is infused with our house-ground Xawaash &mdash; a centuries-old spice blend uniting turmeric, coriander, cumin, black peppercorn, and cardamom &mdash; delivering savory depth without excessive heat.</p>
            <a href="somali-culinary-heritage.html" class="jamile-btn-primary" style="margin-top: 0.5rem;">Discover Somali Heritage</a>
          </div>
        </div>
      </section>

      <section class="jamile-section" style="background: #ffffff; border-top: 1px solid var(--jamile-border); border-bottom: 1px solid var(--jamile-border);">
        <div class="jamile-section-header">
          <span class="jamile-section-eyebrow">Family Gatherings &amp; Community Feasts</span>
          <h2 class="jamile-section-title">Communal Feast &amp; Platter Estimator</h2>
          <p class="jamile-section-subtitle">Planning a family celebration, community gathering, or special event? Calculate your meat, rice, and sambusa portions below.</p>
        </div>

        <div class="jamile-calc-card">
          <div class="jamile-calc-controls">
            <div class="jamile-calc-field">
              <label for="jamile-guest-count">Guest Headcount: <span id="jamile-guest-display" style="color: var(--jamile-primary); font-weight: 800;">15 Guests</span></label>
              <input type="range" id="jamile-guest-count" class="jamile-range-slider" min="5" max="80" step="5" value="15">
            </div>
            <div class="jamile-calc-field">
              <label for="jamile-platter-style">Feast Scale</label>
              <select id="jamile-platter-style" class="jamile-calc-select">
                <option value="standard">Standard Somali Platter (Goat / Beef + Rice)</option>
                <option value="grand-feast">Grand Community Feast (Goat, Beef, Shanks &amp; Sambusas)</option>
              </select>
            </div>
          </div>
          <div class="jamile-calc-results">
            <div class="jamile-result-box">
              <span class="num" id="jamile-meat-total">9.0 lbs Spiced Goat &amp; Beef</span>
              <span class="label">Halal Braised Meats</span>
            </div>
            <div class="jamile-result-box">
              <span class="num" id="jamile-rice-total">7.5 lbs Bariis Iskukaris</span>
              <span class="label">Spiced Basmati Rice</span>
            </div>
            <div class="jamile-result-box">
              <span class="num" id="jamile-sambusa-total">30 Golden Sambusas</span>
              <span class="label">Hand-Folded Pastries</span>
            </div>
          </div>
        </div>
      </section>
    </main>
'''
  },
  'menu.html': {
    'title': 'Menu - Jamile’s Cuisine International Charlotte NC',
    'nav': {'index': '', 'menu': 'active', 'heritage': '', 'goat': '', 'tea': '', 'visit': ''},
    'body': '''
    <main class="jamile-section">
      <div class="jamile-section-header">
        <span class="jamile-section-eyebrow">Halal East African Specialties</span>
        <h1 class="jamile-section-title">Jamile’s Cuisine Menu</h1>
        <p class="jamile-section-subtitle">Traditional slow-cooked goat meat, seasoned beef suqaar, golden basmati rice, hand-folded sambusas, and spiced Somali milk tea.</p>
      </div>

      <div class="jamile-filter-tabs" role="tablist" aria-label="Menu Filter Tabs">
        <button type="button" class="jamile-filter-btn active" data-filter="all">All Selections</button>
        <button type="button" class="jamile-filter-btn" data-filter="feasts">Traditional Feasts</button>
        <button type="button" class="jamile-filter-btn" data-filter="suqaar">Suqaar &amp; Shanks</button>
        <button type="button" class="jamile-filter-btn" data-filter="sambusa">Sambusas &amp; Breads</button>
        <button type="button" class="jamile-filter-btn" data-filter="drinks">Tea &amp; Drinks</button>
      </div>

      <div class="jamile-menu-grid">
        <div class="jamile-menu-item" data-category="feasts">
          <div class="jamile-menu-item-header">
            <span class="jamile-menu-item-name">Hilib Ari (Slow-Roasted Goat)</span>
            <span class="jamile-menu-item-price">$17.95</span>
          </div>
          <p class="jamile-menu-item-desc">Tender bone-in goat meat slow-roasted with garlic, rosemary, and Xawaash spices. Served over a mound of fragrant Bariis basmati rice with a fresh banana, house salad, and spicy green Basbaas sauce.</p>
          <div class="jamile-menu-item-badges">
            <span class="jamile-badge jamile-badge-gold">House Signature</span>
            <span class="jamile-badge">100% Halal</span>
          </div>
        </div>

        <div class="jamile-menu-item" data-category="feasts">
          <div class="jamile-menu-item-header">
            <span class="jamile-menu-item-name">Braised Beef Shank Platter</span>
            <span class="jamile-menu-item-price">$16.50</span>
          </div>
          <p class="jamile-menu-item-desc">Rich beef shank slow-simmered in savory onion-tomato reduction with cardamom and cumin, paired with spiced basmati rice and lime.</p>
          <div class="jamile-menu-item-badges">
            <span class="jamile-badge jamile-badge-gold">Hearty Classic</span>
          </div>
        </div>

        <div class="jamile-menu-item" data-category="suqaar">
          <div class="jamile-menu-item-header">
            <span class="jamile-menu-item-name">Beef Suqaar</span>
            <span class="jamile-menu-item-price">$14.95</span>
          </div>
          <p class="jamile-menu-item-desc">Tender bite-sized beef cubes flash-sautéed with bell peppers, red onions, garlic, and turmeric. Served with warm Sabaayad flatbread or rice.</p>
          <div class="jamile-menu-item-badges">
            <span class="jamile-badge">Sautéed to Order</span>
          </div>
        </div>

        <div class="jamile-menu-item" data-category="suqaar">
          <div class="jamile-menu-item-header">
            <span class="jamile-menu-item-name">Chicken Suqaar</span>
            <span class="jamile-menu-item-price">$13.95</span>
          </div>
          <p class="jamile-menu-item-desc">Diced chicken breast cooked in aromatic ginger, cilantro, cumin, and mild green chili gravy with vegetables.</p>
          <div class="jamile-menu-item-badges">
            <span class="jamile-badge">Lean &amp; Aromatic</span>
          </div>
        </div>

        <div class="jamile-menu-item" data-category="sambusa">
          <div class="jamile-menu-item-header">
            <span class="jamile-menu-item-name">Crispy Beef Sambusas (3)</span>
            <span class="jamile-menu-item-price">$6.00</span>
          </div>
          <p class="jamile-menu-item-desc">Hand-rolled flaky pastry triangles stuffed with spiced minced halal beef, caramelized onions, cilantro, and green chilies, served with house Basbaas dip.</p>
          <div class="jamile-menu-item-badges">
            <span class="jamile-badge jamile-badge-gold">Appetizer Hit</span>
          </div>
        </div>

        <div class="jamile-menu-item" data-category="sambusa">
          <div class="jamile-menu-item-header">
            <span class="jamile-menu-item-name">Traditional Sabaayad Flatbread</span>
            <span class="jamile-menu-item-price">$3.50</span>
          </div>
          <p class="jamile-menu-item-desc">Pan-griddled layered Somali flatbread with a flaky, buttery texture, perfect for scooping up suqaar or enjoying with tea.</p>
          <div class="jamile-menu-item-badges">
            <span class="jamile-badge">Fresh Baked</span>
          </div>
        </div>

        <div class="jamile-menu-item" data-category="drinks">
          <div class="jamile-menu-item-header">
            <span class="jamile-menu-item-name">Shaah Cadays (Somali Milk Tea)</span>
            <span class="jamile-menu-item-price">$3.50</span>
          </div>
          <p class="jamile-menu-item-desc">Black tea brewed with whole cardamom pods, cinnamon bark, cloves, fresh ginger, sweetened condensed milk, and pure cane sugar.</p>
          <div class="jamile-menu-item-badges">
            <span class="jamile-badge jamile-badge-gold">Warm &amp; Spiced</span>
          </div>
        </div>

        <div class="jamile-menu-item" data-category="drinks">
          <div class="jamile-menu-item-header">
            <span class="jamile-menu-item-name">Fresh Mango Juice</span>
            <span class="jamile-menu-item-price">$4.25</span>
          </div>
          <p class="jamile-menu-item-desc">Chilled natural mango nectar pureed with a squeeze of fresh lime juice.</p>
          <div class="jamile-menu-item-badges">
            <span class="jamile-badge jamile-badge-green">Refreshing</span>
          </div>
        </div>
      </div>
    </main>
'''
  },
  'somali-culinary-heritage.html': {
    'title': 'Somali Culinary Heritage - Jamile’s Cuisine International',
    'nav': {'index': '', 'menu': '', 'heritage': 'active', 'goat': '', 'tea': '', 'visit': ''},
    'body': '''
    <main class="jamile-section">
      <div class="jamile-section-header">
        <span class="jamile-section-eyebrow">Culinary History &amp; Traditions</span>
        <h1 class="jamile-section-title">The Rich Heritage of Somali Cooking</h1>
        <p class="jamile-section-subtitle">Explore the ancient spice trade routes, communal hospitality, and unique flavor traditions that define Somali cuisine.</p>
      </div>

      <div class="jamile-story-grid">
        <div class="jamile-story-content">
          <h3>The Ancient Spice Trade Crossroads</h3>
          <p>Situated on the Horn of Africa, Somalia has for centuries been a vital crossroads of maritime spice trade connecting Africa, Arabia, Persia, and India. This rich geographical position gave birth to one of the world’s most distinctive spice heritages.</p>
          <p>Central to Somali cooking is <strong>Xawaash</strong> (pronounced ha-wa-ish), a master spice blend prepared by dry-toasting cumin seeds, coriander seeds, cardamom pods, cinnamon sticks, cloves, turmeric, and black peppercorns before grinding them fresh. This blend brings immense warmth, floral aroma, and golden color without fiery burn.</p>
        </div>
        <div class="jamile-story-img-wrap">
          <img src="images/suqaar.jpg" alt="Fragrant spiced Somali sautéed beef and bell peppers" width="600" height="380">
        </div>
      </div>

      <div class="jamile-story-grid" style="margin-top: 4.5rem;">
        <div class="jamile-story-img-wrap">
          <img src="images/hero.jpg" alt="Traditional Somali rice platter served with banana" width="600" height="380">
        </div>
        <div class="jamile-story-content">
          <h3>The Banana Tradition (Moos)</h3>
          <p>One of the most charming and delicious traditions in Somali dining is serving a whole fresh banana alongside every savory rice and meat platter.</p>
          <p>Diners peel the banana and slice bites of it together with the savory braised goat and spiced basmati rice. The cool, natural sweetness of the fruit provides a delicate contrast to the rich, slow-simmered spices, creating a balanced harmony found nowhere else.</p>
        </div>
      </div>
    </main>
'''
  },
  'goat-and-spiced-rice.html': {
    'title': 'Goat & Spiced Rice - Jamile’s Cuisine International',
    'nav': {'index': '', 'menu': '', 'heritage': '', 'goat': 'active', 'tea': '', 'visit': ''},
    'body': '''
    <main class="jamile-section">
      <div class="jamile-section-header">
        <span class="jamile-section-eyebrow">Signature Masterpiece</span>
        <h1 class="jamile-section-title">Hilib Ari &amp; Bariis Iskukaris</h1>
        <p class="jamile-section-subtitle">A deep dive into our most celebrated slow-roasted goat and aromatic spiced basmati rice.</p>
      </div>

      <div class="jamile-story-grid">
        <div class="jamile-story-img-wrap">
          <img src="images/goat.jpg" alt="Slow braised Somali goat meat with basmati rice" width="600" height="380">
        </div>
        <div class="jamile-story-content">
          <h3>The Craft of Slow-Roasted Hilib Ari</h3>
          <p>Goat meat (Hilib Ari) is the revered crown of Somali celebratory feasts. We select premium bone-in halal cuts and marinate them with crushed garlic, grated ginger, lemon juice, turmeric, and whole spices.</p>
          <p>Slow-roasted in a sealed braising pot for several hours, the collagen melts into an unctuous, deeply savory meat that easily pulls apart with a fork, retaining its natural juices and rich aromatics.</p>
        </div>
      </div>

      <div class="jamile-story-grid" style="margin-top: 4.5rem;">
        <div class="jamile-story-content">
          <h3>Bariis Iskukaris: The Spiced Rice</h3>
          <p>Our long-grain basmati rice is parboiled with saffron, whole cinnamon sticks, star anise, cardamom pods, and caramelized onions. Steamed gently with golden raisins and slivered carrots, each grain remains separate, fluffy, and fragrant.</p>
          <p>Served with a bowl of zesty, fiery green Basbaas sauce (jalapeño, garlic, cilantro, and lemon) to tailor the spice level to your preference.</p>
        </div>
        <div class="jamile-story-img-wrap">
          <img src="images/hero.jpg" alt="Platter of spiced basmati rice and garnishes" width="600" height="380">
        </div>
      </div>
    </main>
'''
  },
  'sambusas-and-shaah-tea.html': {
    'title': 'Sambusas & Tea - Jamile’s Cuisine International',
    'nav': {'index': '', 'menu': '', 'heritage': '', 'goat': '', 'tea': 'active', 'visit': ''},
    'body': '''
    <main class="jamile-section">
      <div class="jamile-section-header">
        <span class="jamile-section-eyebrow">Artisanal Small Bites &amp; Brews</span>
        <h1 class="jamile-section-title">Hand-Folded Sambusas &amp; Shaah Cadays</h1>
        <p class="jamile-section-subtitle">Crispy pastry appetizers and comforting Somali spiced milk tea.</p>
      </div>

      <div class="jamile-story-grid">
        <div class="jamile-story-content">
          <h3>Hand-Folded Crispy Sambusas</h3>
          <p>In East Africa, no gathering begins without hot, golden sambusas. Our chefs roll paper-thin pastry wrappers, folding them by hand into tight triangular envelopes.</p>
          <p>Stuffed with finely minced halal beef, sweet yellow onions, fresh cilantro, cumin, and diced green chilies, they are fried in clean oil until blistered, golden, and extraordinarily crisp.</p>
        </div>
        <div class="jamile-story-img-wrap">
          <img src="images/sambusa.jpg" alt="Crispy golden triangular sambusas served on platter" width="600" height="380">
        </div>
      </div>

      <div class="jamile-story-grid" style="margin-top: 4.5rem;">
        <div class="jamile-story-img-wrap">
          <img src="images/tea.jpg" alt="Steaming cups of spiced Somali milk tea with cinnamon and cardamom" width="600" height="380">
        </div>
        <div class="jamile-story-content">
          <h3>Shaah Cadays: Spiced Somali Milk Tea</h3>
          <p>Somali hospitality is sealed with a piping glass of <strong>Shaah Cadays</strong>. We simmer robust black tea leaves with bruised green cardamom pods, broken Ceylon cinnamon sticks, whole cloves, and crushed ginger.</p>
          <p>Blended with milk and sweetened to create an aromatic, warming beverage that soothes the spirit after a hearty meal.</p>
        </div>
      </div>
    </main>
'''
  },
  'visit.html': {
    'title': 'Visit & Order - Jamile’s Cuisine International Charlotte NC',
    'nav': {'index': '', 'menu': '', 'heritage': '', 'goat': '', 'tea': '', 'visit': 'active'},
    'body': '''
    <main class="jamile-section">
      <div class="jamile-section-header">
        <span class="jamile-section-eyebrow">Dine In &bull; Takeout &bull; Catering</span>
        <h1 class="jamile-section-title">Visit Jamile’s Cuisine</h1>
        <p class="jamile-section-subtitle">Located on Central Avenue in East Charlotte. Join us for lunch, dinner, or order authentic family platters for takeout.</p>
      </div>

      <div class="jamile-contact-grid">
        <div class="jamile-contact-card">
          <h3>Central Avenue Restaurant</h3>
          <p style="color: var(--jamile-text-muted); margin-bottom: 0.8rem;">Situated in East Charlotte’s multicultural dining corridor with adjoining market entrance.</p>
          <p><strong>Address:</strong> 4808 Central Ave, Ste G, Charlotte, NC 28205</p>
          <p style="margin-top: 0.4rem;"><strong>Halal Certified:</strong> 100% Halal meats prepared under strict culinary standards.</p>
          <div style="margin-top: 1.5rem;">
            <a href="tel:7045311180" class="jamile-btn-primary" style="width: 100%; text-align: center;">Call to Order: (704) 531-1180</a>
          </div>
        </div>

        <div class="jamile-contact-card">
          <h3>Operating Hours</h3>
          <div class="jamile-hours-row">
            <span>Tuesday &ndash; Sunday</span>
            <span>12:00 PM &ndash; 8:00 PM</span>
          </div>
          <div class="jamile-hours-row">
            <span>Monday</span>
            <span>Closed</span>
          </div>
          <div style="margin-top: 1.5rem; background: var(--jamile-surface-alt); padding: 1rem; border-radius: var(--jamile-radius-sm);">
            <p style="font-size: 0.85rem; color: var(--jamile-primary-dark); font-weight: 700;">Fresh batches of Hilib Ari and Bariis prepared daily. Call ahead for express takeout pickup.</p>
          </div>
        </div>

        <div class="jamile-contact-card">
          <h3>Family &amp; Event Catering</h3>
          <p style="color: var(--jamile-text-muted); margin-bottom: 0.8rem;">Large communal platters of roasted goat, beef suqaar, fragrant basmati rice trays, and bulk sambusa orders for weddings and community celebrations.</p>
          <p><strong>Notice:</strong> Catering orders recommended 24-48 hours in advance.</p>
          <div style="margin-top: 1.5rem;">
            <a href="mailto:catering@jamilescuisineclt.com" class="jamile-btn-secondary" style="width: 100%; text-align: center;">Inquire for Catering</a>
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
    nav_goat=data['nav']['goat'],
    nav_tea=data['nav']['tea'],
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
  <link href="https://fonts.googleapis.com/css2?family=Marcellus&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="site.css">
</head>
<body>
  <header class="jamile-header">
    <div class="jamile-nav-container">
      <a href="index.html" class="jamile-brand">
        <span class="jamile-brand-title">Jamile’s Cuisine International</span>
        <span class="jamile-brand-subtitle">Authentic Somali &bull; 100% Halal</span>
      </a>
      <button class="jamile-nav-toggle" type="button" aria-label="Toggle navigation menu" aria-expanded="false">Menu</button>
{cur_nav}
    </div>
  </header>

{data['body']}

{footer_content}
  <script src="site.js"></script>
</body>
</html>'''

  filepath = os.path.join('jamile-s-cuisine-international', filename)
  with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html_doc.strip() + '\n')
  print(f'Wrote {filename}')

print('All 6 HTML pages for Jamile’s Cuisine International written successfully')
