import os

nav_template = '''
      <nav class="kili-nav" aria-label="Primary Navigation">
        <ul class="kili-nav-list">
          <li><a href="index.html" class="kili-nav-link {nav_index}">Home</a></li>
          <li><a href="menu.html" class="kili-nav-link {nav_menu}">Menu</a></li>
          <li><a href="somali-and-east-african-tradition.html" class="kili-nav-link {nav_tradition}">Tradition</a></li>
          <li><a href="lamb-shank-and-goat.html" class="kili-nav-link {nav_meat}">Lamb Shank &amp; Goat</a></li>
          <li><a href="chapati-malawax-and-sambusas.html" class="kili-nav-link {nav_breads}">Chapati &amp; Sambusas</a></li>
          <li><a href="visit.html" class="kili-nav-link kili-nav-cta {nav_visit}">Visit &amp; Order</a></li>
        </ul>
      </nav>
'''

footer_content = '''
  <footer class="kili-footer">
    <div class="kili-footer-container">
      <div class="kili-footer-brand">
        <h4>Kilimanjaro Kitchen</h4>
        <p>100% Halal authentic Somali and East African cuisine at 4450 The Plaza in Charlotte. Famous for braised lamb shank, slow-cooked goat, warm chapati, and sweet malawax crepes.</p>
      </div>
      <div class="kili-footer-nav">
        <h5>Explore Demo</h5>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Full Menu</a></li>
          <li><a href="somali-and-east-african-tradition.html">East African Tradition</a></li>
          <li><a href="lamb-shank-and-goat.html">Lamb Shank &amp; Goat</a></li>
          <li><a href="chapati-malawax-and-sambusas.html">Chapati &amp; Sambusas</a></li>
          <li><a href="visit.html">Location &amp; Hours</a></li>
        </ul>
      </div>
      <div class="kili-footer-hours">
        <h5>Location &amp; Hours</h5>
        <p style="color: #9d9991; font-size: 0.88rem; margin-bottom: 0.4rem;"><strong>The Plaza:</strong> 4450 The Plaza, Suite F</p>
        <p style="color: #9d9991; font-size: 0.88rem; margin-bottom: 0.4rem;"><strong>Direct Phone:</strong> (704) 531-9005</p>
        <p style="color: #9d9991; font-size: 0.88rem;">Tue - Sun: 12:00 PM - 9:00 PM<br>Monday: Closed</p>
      </div>
    </div>
    <div class="kili-footer-bottom">
      <p>&copy; 2026 Kilimanjaro Kitchen. All rights reserved. Culinary showcase demo for Charlotte, NC.</p>
    </div>
  </footer>
'''

pages = {
  'index.html': {
    'title': 'Kilimanjaro Kitchen - 100% Halal Somali Cuisine on The Plaza Charlotte NC',
    'nav': {'index': 'active', 'menu': '', 'tradition': '', 'meat': '', 'breads': '', 'visit': ''},
    'body': '''
    <main>
      <section class="kili-hero">
        <div class="kili-hero-grid">
          <div class="kili-hero-content">
            <span class="kili-hero-badge">4450 The Plaza &bull; 100% Halal Somali Kitchen</span>
            <h1 class="kili-hero-title">Rich Horn of Africa Flavors, <span>Slow Braised</span></h1>
            <p class="kili-hero-lead">Experience the comforting hospitality of Somalia in East Charlotte. Savor tender Waslad lamb shanks, slow-roasted Hilib Ari goat, fragrant cardamom rice with banana, and warm griddled chapati.</p>
            <div class="kili-hero-actions">
              <a href="menu.html" class="kili-btn-primary">View Full Menu</a>
              <a href="lamb-shank-and-goat.html" class="kili-btn-secondary">The Shank &amp; Goat Feast</a>
            </div>
          </div>
          <div class="kili-hero-img-wrap">
            <img src="images/hero.jpg" alt="Rich Somali braised lamb shank and goat meat platter with spiced basmati rice" width="600" height="420">
          </div>
        </div>
      </section>

      <section class="kili-features">
        <div class="kili-feature-grid">
          <div class="kili-feature-card">
            <div class="kili-feature-tag">100% Halal Certified</div>
            <h2 class="kili-feature-title">Waslad Lamb Shank</h2>
            <p class="kili-feature-desc">Slow-simmered whole lamb shank with cardamom, cloves, and rosemary until meat falls from the bone.</p>
          </div>
          <div class="kili-feature-card">
            <div class="kili-feature-tag">House Specialty</div>
            <h2 class="kili-feature-title">Hilib Ari Goat Feast</h2>
            <p class="kili-feature-desc">Succulent goat braised in traditional spices, served over fragrant basmati rice with a fresh banana.</p>
          </div>
          <div class="kili-feature-card">
            <div class="kili-feature-tag">Griddled Fresh</div>
            <h2 class="kili-feature-title">Chapati &amp; Malawax</h2>
            <p class="kili-feature-desc">Warm flaky multi-layered flatbread and sweet spiced Somali crepes pan-seared to golden perfection.</p>
          </div>
        </div>
      </section>

      <section class="kili-section">
        <div class="kili-story-grid">
          <div class="kili-story-img-wrap">
            <img src="images/lamb-shank.jpg" alt="Tender lamb shank roasted with savory spices on rice" width="600" height="380">
          </div>
          <div class="kili-story-content">
            <span class="kili-section-eyebrow">East Charlotte Community Anchor</span>
            <h3>Generous Portions, Authentic Recipes</h3>
            <p>At Kilimanjaro Kitchen, our mission is to share the rich culinary heritage of Somalia with Charlotte food lovers. Every pot of stew is simmered low and slow, allowing aromatic spices like coriander, cumin, cardamom, and cinnamon to penetrate deep into each cut of halal meat.</p>
            <p>Pair your meal with our house-crafted green Basbaas chili sauce and finish with a piping cup of sweet spiced tea.</p>
            <a href="somali-and-east-african-tradition.html" class="kili-btn-primary" style="margin-top: 0.5rem;">Learn Our Story</a>
          </div>
        </div>
      </section>

      <section class="kili-section" style="background: #ffffff; border-top: 1px solid var(--kili-border); border-bottom: 1px solid var(--kili-border);">
        <div class="kili-section-header">
          <span class="kili-section-eyebrow">Family Banquets &amp; Celebrations</span>
          <h2 class="kili-section-title">Communal Banquet &amp; Tray Estimator</h2>
          <p class="kili-section-subtitle">Planning a community feast, wedding celebration, or family gathering? Calculate your lamb shank, goat, and chapati portions below.</p>
        </div>

        <div class="kili-calc-card">
          <div class="kili-calc-controls">
            <div class="kili-calc-field">
              <label for="kili-guest-count">Guest Headcount: <span id="kili-guest-display" style="color: var(--kili-primary); font-weight: 800;">15 Diners</span></label>
              <input type="range" id="kili-guest-count" class="kili-range-slider" min="5" max="80" step="5" value="15">
            </div>
            <div class="kili-calc-field">
              <label for="kili-platter-style">Feast Tier</label>
              <select id="kili-platter-style" class="kili-calc-select">
                <option value="standard">Standard Somali Tray (Goat / Beef Suqaar + Rice)</option>
                <option value="grand">Grand Kilimanjaro Feast (Whole Lamb Shanks + Goat + Chapati)</option>
              </select>
            </div>
          </div>
          <div class="kili-calc-results">
            <div class="kili-result-box">
              <span class="num" id="kili-meat-total">9.8 lbs Lamb Shank &amp; Goat</span>
              <span class="label">Halal Braised Meats</span>
            </div>
            <div class="kili-result-box">
              <span class="num" id="kili-rice-total">8.3 lbs Spiced Basmati Rice</span>
              <span class="label">Aromatic Basmati</span>
            </div>
            <div class="kili-result-box">
              <span class="num" id="kili-bread-total">15 Fresh Chapati / Malawax</span>
              <span class="label">Griddled Breads</span>
            </div>
          </div>
        </div>
      </section>
    </main>
'''
  },
  'menu.html': {
    'title': 'Menu - Kilimanjaro Kitchen Charlotte NC',
    'nav': {'index': '', 'menu': 'active', 'tradition': '', 'meat': '', 'breads': '', 'visit': ''},
    'body': '''
    <main class="kili-section">
      <div class="kili-section-header">
        <span class="kili-section-eyebrow">100% Halal Selections</span>
        <h1 class="kili-section-title">Kilimanjaro Kitchen Menu</h1>
        <p class="kili-section-subtitle">Tender slow-cooked lamb shanks, braised goat, sizzling suqaar, freshly griddled breads, and crispy sambusas.</p>
      </div>

      <div class="hhs-filter-tabs kili-filter-tabs" role="tablist" aria-label="Menu Filter Tabs">
        <button type="button" class="kili-filter-btn active" data-filter="all">All Selections</button>
        <button type="button" class="kili-filter-btn" data-filter="entrees">Halal Entrees</button>
        <button type="button" class="kili-filter-btn" data-filter="suqaar">Sautéed Suqaar</button>
        <button type="button" class="kili-filter-btn" data-filter="breads">Breads &amp; Crepes</button>
        <button type="button" class="kili-filter-btn" data-filter="apps">Sambusas &amp; Drinks</button>
      </div>

      <div class="kili-menu-grid">
        <div class="kili-menu-item" data-category="entrees">
          <div class="kili-menu-item-header">
            <span class="kili-menu-item-name">Waslad (Braised Lamb Shank)</span>
            <span class="kili-menu-item-price">$18.95</span>
          </div>
          <p class="kili-menu-item-desc">Giant whole bone-in lamb shank slow-cooked in rich rosemary, garlic, and Xawaash broth. Served with fragrant spiced basmati rice, a fresh banana, and house salad.</p>
          <div class="kili-menu-item-badges">
            <span class="kili-badge kili-badge-gold">House Signature</span>
            <span class="kili-badge">Fall Off Bone</span>
          </div>
        </div>

        <div class="kili-menu-item" data-category="entrees">
          <div class="kili-menu-item-header">
            <span class="kili-menu-item-name">Hilib Ari (Somali Goat Platter)</span>
            <span class="kili-menu-item-price">$17.50</span>
          </div>
          <p class="kili-menu-item-desc">Tender cuts of bone-in halal goat meat braised with whole cloves and cumin seeds, served over aromatic basmati rice with spicy green Basbaas sauce.</p>
          <div class="kili-menu-item-badges">
            <span class="kili-badge kili-badge-gold">Traditional Hit</span>
          </div>
        </div>

        <div class="kili-menu-item" data-category="suqaar">
          <div class="kili-menu-item-header">
            <span class="kili-menu-item-name">Beef Suqaar Plate</span>
            <span class="kili-menu-item-price">$14.95</span>
          </div>
          <p class="kili-menu-item-desc">Lean bite-sized halal beef flash-sautéed with colorful bell peppers, red onions, garlic, and mild turmeric sauce with choice of rice or chapati.</p>
          <div class="kili-menu-item-badges">
            <span class="kili-badge">Sautéed Hot</span>
          </div>
        </div>

        <div class="kili-menu-item" data-category="suqaar">
          <div class="kili-menu-item-header">
            <span class="kili-menu-item-name">Chicken Suqaar</span>
            <span class="kili-menu-item-price">$13.95</span>
          </div>
          <p class="kili-menu-item-desc">Diced tender chicken breast simmered with sweet onions, green peppers, ginger, and aromatic Somali herbs.</p>
          <div class="kili-menu-item-badges">
            <span class="kili-badge">High Protein</span>
          </div>
        </div>

        <div class="kili-menu-item" data-category="breads">
          <div class="kili-menu-item-header">
            <span class="kili-menu-item-name">Fresh Griddled Chapati</span>
            <span class="kili-menu-item-price">$3.50</span>
          </div>
          <p class="kili-menu-item-desc">Flaky, multi-layered East African flatbread griddled with butter, perfect for tearing and dipping into savory meat gravies.</p>
          <div class="kili-menu-item-badges">
            <span class="kili-badge kili-badge-brown">Baked Fresh</span>
          </div>
        </div>

        <div class="kili-menu-item" data-category="breads">
          <div class="kili-menu-item-header">
            <span class="kili-menu-item-name">Sweet Malawax Crepes (2)</span>
            <span class="kili-menu-item-price">$4.25</span>
          </div>
          <p class="kili-menu-item-desc">Traditional Somali sweet pancake crepes spiced with ground cardamom, ginger, and sugar, served warm with honey drizzle.</p>
          <div class="kili-menu-item-badges">
            <span class="kili-badge kili-badge-gold">Sweet Treat</span>
          </div>
        </div>

        <div class="kili-menu-item" data-category="apps">
          <div class="kili-menu-item-header">
            <span class="kili-menu-item-name">Crispy Halal Sambusas (3)</span>
            <span class="kili-menu-item-price">$6.00</span>
          </div>
          <p class="kili-menu-item-desc">Crispy fried triangular pastry pockets filled with seasoned ground beef, onions, and jalapeños, served with tangy green Basbaas sauce.</p>
          <div class="kili-menu-item-badges">
            <span class="kili-badge kili-badge-gold">Appetizer Favorite</span>
          </div>
        </div>

        <div class="kili-menu-item" data-category="apps">
          <div class="kili-menu-item-header">
            <span class="kili-menu-item-name">Spiced Somali Milk Tea</span>
            <span class="kili-menu-item-price">$3.50</span>
          </div>
          <p class="kili-menu-item-desc">Sweetened black tea brewed with crushed cardamom pods, whole cinnamon bark, cloves, and whole milk.</p>
          <div class="kili-menu-item-badges">
            <span class="kili-badge">Warm &amp; Comforting</span>
          </div>
        </div>
      </div>
    </main>
'''
  },
  'somali-and-east-african-tradition.html': {
    'title': 'East African Tradition - Kilimanjaro Kitchen',
    'nav': {'index': '', 'menu': '', 'tradition': 'active', 'meat': '', 'breads': '', 'visit': ''},
    'body': '''
    <main class="kili-section">
      <div class="kili-section-header">
        <span class="kili-section-eyebrow">Our Heritage &amp; Roots</span>
        <h1 class="kili-section-title">Somali &amp; East African Food Culture</h1>
        <p class="kili-section-subtitle">Discover the time-honored hospitality, spice balance, and communal rituals of Somali culinary culture.</p>
      </div>

      <div class="kili-story-grid">
        <div class="kili-story-content">
          <h3>The Art of Slow-Simmered Hospitality</h3>
          <p>In the Horn of Africa, welcoming a guest with generous platters of slow-cooked meats and aromatic rice is a core pillar of cultural heritage. At Kilimanjaro Kitchen on The Plaza, we preserve these traditions with authentic recipes and 100% halal preparation.</p>
          <p>Our meats are seasoned with whole spices and braised gently in sealed pots for hours so the marrow and spices merge into a rich, fragrant sauce that coats every grain of basmati.</p>
        </div>
        <div class="kili-story-img-wrap">
          <img src="images/hero.jpg" alt="Rich Somali feast with braised lamb, basmati rice, and sides" width="600" height="380">
        </div>
      </div>

      <div class="kili-story-grid" style="margin-top: 4.5rem;">
        <div class="kili-story-img-wrap">
          <img src="images/goat-rice.jpg" alt="Somali spiced rice served with fresh banana" width="600" height="380">
        </div>
        <div class="kili-story-content">
          <h3>The Banana Pairing (Moos)</h3>
          <p>Every traditional Somali rice entrée is served with a ripe whole banana. Slicing fresh banana with bites of savory braised goat and cardamom rice creates a delightful sweet-and-savory balance that is iconic to Somali dining.</p>
        </div>
      </div>
    </main>
'''
  },
  'lamb-shank-and-goat.html': {
    'title': 'Lamb Shank & Goat - Kilimanjaro Kitchen',
    'nav': {'index': '', 'menu': '', 'tradition': '', 'meat': 'active', 'breads': '', 'visit': ''},
    'body': '''
    <main class="kili-section">
      <div class="kili-section-header">
        <span class="kili-section-eyebrow">Signature Feasts</span>
        <h1 class="kili-section-title">Waslad Lamb Shank &amp; Hilib Ari Goat</h1>
        <p class="kili-section-subtitle">A deep dive into our most celebrated slow-braised halal entrées.</p>
      </div>

      <div class="kili-story-grid">
        <div class="kili-story-img-wrap">
          <img src="images/lamb-shank.jpg" alt="Waslad braised lamb shank falling off bone with spiced basmati rice" width="600" height="380">
        </div>
        <div class="kili-story-content">
          <h3>Waslad: The Crown Lamb Shank</h3>
          <p>Our Waslad is a whole premium bone-in lamb shank marinated in garlic, crushed ginger, ground cardamom, and coriander. Braised low and slow until the meat becomes remarkably tender and gelatinous, it pulls effortlessly from the bone with just a fork.</p>
          <p>Served over our golden Bariis basmati rice infused with caramelized onions, raisins, and cinnamon sticks.</p>
        </div>
      </div>

      <div class="kili-story-grid" style="margin-top: 4.5rem;">
        <div class="kili-story-content">
          <h3>Hilib Ari: Slow-Roasted Somali Goat</h3>
          <p>Goat meat is the traditional centerpiece of celebratory banquets in Somalia. We select high-grade halal goat cuts, searing them with whole spices before gentle oven braising.</p>
          <p>The result is a deeply savory, aromatic meat that highlights the authentic spices of the Horn of Africa, paired with our fiery green Basbaas chili sauce.</p>
        </div>
        <div class="kili-story-img-wrap">
          <img src="images/hero.jpg" alt="Generous platter of Somali goat meat and spiced rice" width="600" height="380">
        </div>
      </div>
    </main>
'''
  },
  'chapati-malawax-and-sambusas.html': {
    'title': 'Chapati, Malawax & Sambusas - Kilimanjaro Kitchen',
    'nav': {'index': '', 'menu': '', 'tradition': '', 'meat': '', 'breads': 'active', 'visit': ''},
    'body': '''
    <main class="kili-section">
      <div class="kili-section-header">
        <span class="kili-section-eyebrow">Fresh Griddled &amp; Hand-Folded</span>
        <h1 class="kili-section-title">Chapati, Sweet Malawax &amp; Sambusas</h1>
        <p class="kili-section-subtitle">Artisanal East African breads, sweet crepes, and golden savory pastries.</p>
      </div>

      <div class="kili-story-grid">
        <div class="kili-story-content">
          <h3>Fresh Pan-Griddled Chapati</h3>
          <p>East African Chapati is famously flaky and layered. We knead our dough fresh daily, roll it with butter, and pan-griddle it on high heat until puffed with golden blisters.</p>
          <p>Sturdy yet tender, chapati is the quintessential vehicle for scooping up tender meat suqaar and savory sauces.</p>
        </div>
        <div class="kili-story-img-wrap">
          <img src="images/chapati.jpg" alt="Warm layered chapati flatbread folded on presentation board" width="600" height="380">
        </div>
      </div>

      <div class="kili-story-grid" style="margin-top: 4.5rem;">
        <div class="kili-story-img-wrap">
          <img src="images/sambusa.jpg" alt="Crispy golden beef sambusas with green dipping sauce" width="600" height="380">
        </div>
        <div class="kili-story-content">
          <h3>Sweet Malawax &amp; Crispy Sambusas</h3>
          <p><strong>Malawax Crepes:</strong> Sweet and delicate, these Somali crepes are infused with cardamom and ginger, cooked on a dry griddle and drizzled with honey.</p>
          <p><strong>Crispy Sambusas:</strong> Stuffed with spiced halal ground beef, onions, and jalapeños, fried golden brown for an unforgettable crispy crunch.</p>
        </div>
      </div>
    </main>
'''
  },
  'visit.html': {
    'title': 'Visit & Order - Kilimanjaro Kitchen Charlotte NC',
    'nav': {'index': '', 'menu': '', 'tradition': '', 'meat': '', 'breads': '', 'visit': 'active'},
    'body': '''
    <main class="kili-section">
      <div class="kili-section-header">
        <span class="kili-section-eyebrow">Dine In &bull; Takeout &bull; Catering</span>
        <h1 class="kili-section-title">Visit Kilimanjaro Kitchen</h1>
        <p class="kili-section-subtitle">Located on The Plaza in East Charlotte. Join us for lunch, dinner, or order authentic family feast platters.</p>
      </div>

      <div class="kili-contact-grid">
        <div class="kili-contact-card">
          <h3>The Plaza Location</h3>
          <p style="color: var(--kili-text-muted); margin-bottom: 0.8rem;">Conveniently located in East Charlotte shopping plaza with convenient front parking.</p>
          <p><strong>Address:</strong> 4450 The Plaza, Suite F, Charlotte, NC 28215</p>
          <p style="margin-top: 0.4rem;"><strong>Certification:</strong> 100% Halal certified meats and ingredients.</p>
          <div style="margin-top: 1.5rem;">
            <a href="tel:7045319005" class="kili-btn-primary" style="width: 100%; text-align: center;">Call to Order: (704) 531-9005</a>
          </div>
        </div>

        <div class="kili-contact-card">
          <h3>Operating Hours</h3>
          <div class="kili-hours-row">
            <span>Tuesday &ndash; Sunday</span>
            <span>12:00 PM &ndash; 9:00 PM</span>
          </div>
          <div class="kili-hours-row">
            <span>Monday</span>
            <span>Closed</span>
          </div>
          <div style="margin-top: 1.5rem; background: var(--kili-surface-alt); padding: 1rem; border-radius: var(--kili-radius-sm);">
            <p style="font-size: 0.85rem; color: var(--kili-primary-dark); font-weight: 700;">Fresh batches of lamb shank and goat prepared daily. Call ahead for quick pickup.</p>
          </div>
        </div>

        <div class="kili-contact-card">
          <h3>Community &amp; Banquet Catering</h3>
          <p style="color: var(--kili-text-muted); margin-bottom: 0.8rem;">Large banquet trays of Waslad lamb shanks, braised goat, basmati rice, and bulk sambusas for Eid celebrations, weddings, and community feasts.</p>
          <p><strong>Notice:</strong> Please place large catering orders 24 hours in advance.</p>
          <div style="margin-top: 1.5rem;">
            <a href="mailto:catering@kilimanjarokitchenclt.com" class="kili-btn-secondary" style="width: 100%; text-align: center;">Inquire for Catering</a>
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
    nav_tradition=data['nav']['tradition'],
    nav_meat=data['nav']['meat'],
    nav_breads=data['nav']['breads'],
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
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,700;0,9..144,800;1,9..144,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="site.css">
</head>
<body>
  <header class="kili-header">
    <div class="kili-nav-container">
      <a href="index.html" class="kili-brand">
        <span class="kili-brand-title">Kilimanjaro Kitchen</span>
        <span class="kili-brand-subtitle">100% Halal Somali &bull; The Plaza</span>
      </a>
      <button class="kili-nav-toggle" type="button" aria-label="Toggle navigation menu" aria-expanded="false">Menu</button>
{cur_nav}
    </div>
  </header>

{data['body']}

{footer_content}
  <script src="site.js"></script>
</body>
</html>'''

  filepath = os.path.join('kilimanjaro-kitchen', filename)
  with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html_doc.strip() + '\n')
  print(f'Wrote {filename}')

print('All 6 HTML pages for Kilimanjaro Kitchen written successfully')
