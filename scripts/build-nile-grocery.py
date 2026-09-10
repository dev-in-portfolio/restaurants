import os

nav_template = '''
      <nav class="nile-nav" aria-label="Primary Navigation">
        <ul class="nile-nav-list">
          <li><a href="index.html" class="nile-nav-link {nav_index}">Home</a></li>
          <li><a href="menu.html" class="nile-nav-link {nav_menu}">Menu</a></li>
          <li><a href="ethiopian-culinary-traditions.html" class="nile-nav-link {nav_traditions}">Traditions</a></li>
          <li><a href="tibs-and-doro-wat.html" class="nile-nav-link {nav_tibs}">Tibs &amp; Doro Wat</a></li>
          <li><a href="vegan-beyaynetu-and-coffee.html" class="nile-nav-link {nav_vegan}">Vegan &amp; Coffee</a></li>
          <li><a href="visit.html" class="nile-nav-link nile-nav-cta {nav_visit}">Visit &amp; Order</a></li>
        </ul>
      </nav>
'''

footer_content = '''
  <footer class="nile-footer">
    <div class="nile-footer-container">
      <div class="nile-footer-brand">
        <h4>Nile Grocery &amp; Cafe</h4>
        <p>Authentic Ethiopian home-style cooking and specialty market in East Charlotte. Serving rich doro wat, sizzling beef tibs, vegan beyaynetu on teff injera, and ceremonial coffee.</p>
      </div>
      <div class="nile-footer-nav">
        <h5>Explore Demo</h5>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Full Menu</a></li>
          <li><a href="ethiopian-culinary-traditions.html">Ethiopian Traditions</a></li>
          <li><a href="tibs-and-doro-wat.html">Tibs &amp; Doro Wat</a></li>
          <li><a href="vegan-beyaynetu-and-coffee.html">Vegan &amp; Coffee</a></li>
          <li><a href="visit.html">Location &amp; Hours</a></li>
        </ul>
      </div>
      <div class="nile-footer-hours">
        <h5>Location &amp; Contact</h5>
        <p style="color: #9ea2ab; font-size: 0.88rem; margin-bottom: 0.4rem;"><strong>East Charlotte:</strong> 3113 N Sharon Amity Rd</p>
        <p style="color: #9ea2ab; font-size: 0.88rem; margin-bottom: 0.4rem;"><strong>Direct Phone:</strong> (704) 568-8090</p>
        <p style="color: #9ea2ab; font-size: 0.88rem;">Mon - Sat: 11:00 AM - 9:00 PM<br>Sunday: 12:00 PM - 8:00 PM</p>
      </div>
    </div>
    <div class="nile-footer-bottom">
      <p>&copy; 2026 Nile Grocery &amp; Cafe. All rights reserved. Ethiopian culinary showcase demo for Charlotte, NC.</p>
    </div>
  </footer>
'''

pages = {
  'index.html': {
    'title': 'Nile Grocery & Cafe - Authentic Ethiopian Restaurant in Charlotte NC',
    'nav': {'index': 'active', 'menu': '', 'traditions': '', 'tibs': '', 'vegan': '', 'visit': ''},
    'body': '''
    <main>
      <section class="nile-hero">
        <div class="nile-hero-grid">
          <div class="nile-hero-content">
            <span class="nile-hero-badge">East Charlotte &bull; Authentic Ethiopian Cafe &amp; Market</span>
            <h1 class="nile-hero-title">Warm Injera, <span>Simmered Berbere Wats</span></h1>
            <p class="nile-hero-lead">Experience the ancient culinary soul of Ethiopia on Sharon Amity Road. Savor rich Doro Wat chicken stew, sizzling rosemary Beef Tibs, colorful vegan Beyaynetu, and freshly roasted ceremonial Jebena coffee.</p>
            <div class="nile-hero-actions">
              <a href="menu.html" class="nile-btn-primary">Explore Full Menu</a>
              <a href="ethiopian-culinary-traditions.html" class="nile-btn-secondary">Our Injera Craft</a>
            </div>
          </div>
          <div class="nile-hero-img-wrap">
            <img src="images/hero.jpg" alt="Rich Ethiopian feast platter with injera, doro wat, beef tibs, and colorful vegan sides" width="600" height="420">
          </div>
        </div>
      </section>

      <section class="nile-features">
        <div class="nile-feature-grid">
          <div class="nile-feature-card">
            <div class="nile-feature-tag">House Fermented</div>
            <h2 class="nile-feature-title">Pure Teff Injera</h2>
            <p class="nile-feature-desc">Naturally fermented sourdough flatbread with an airy, spongy texture crafted to scoop every bite by hand.</p>
          </div>
          <div class="nile-feature-card">
            <div class="nile-feature-tag">Berbere Simmered</div>
            <h2 class="nile-feature-title">Doro Wat &amp; Tibs</h2>
            <p class="nile-feature-desc">Slow-braised chicken infused with sun-dried red chili blend, spiced niter kibbeh butter, and hard-boiled egg.</p>
          </div>
          <div class="nile-feature-card">
            <div class="nile-feature-tag">100% Plant-Based</div>
            <h2 class="nile-feature-title">Vegan Beyaynetu</h2>
            <p class="nile-feature-desc">Vibrant sampler platter featuring spicy red lentils (Misir), split yellow peas, collard greens, and shiro.</p>
          </div>
        </div>
      </section>

      <section class="nile-section">
        <div class="nile-story-grid">
          <div class="nile-story-img-wrap">
            <img src="images/tibs.jpg" alt="Sizzling hot skillet of beef tibs with rosemary, onions, and jalapeños" width="600" height="380">
          </div>
          <div class="nile-story-content">
            <span class="nile-section-eyebrow">Communal Messob Hospitality</span>
            <h3>Eating Together as One Family</h3>
            <p>In Ethiopia, eating from a shared messob (woven straw table) with injera is a symbol of friendship, trust, and community bond. At Nile Grocery &amp; Cafe, our recipes are handed down through generations of home cooks.</p>
            <p>Whether you choose our sizzling Awaze Beef Tibs tossed with fresh rosemary or our nourishing vegan combo, every meal is prepared with patience and love.</p>
            <a href="tibs-and-doro-wat.html" class="nile-btn-primary" style="margin-top: 0.5rem;">Discover Our Meat Specialties</a>
          </div>
        </div>
      </section>

      <section class="nile-section" style="background: #ffffff; border-top: 1px solid var(--nile-border); border-bottom: 1px solid var(--nile-border);">
        <div class="nile-section-header">
          <span class="nile-section-eyebrow">Family Feasts &amp; Gatherings</span>
          <h2 class="nile-section-title">Messob Communal Platter Estimator</h2>
          <p class="nile-section-subtitle">Planning a family dinner or community celebration? Calculate your injera rolls, simmered wats, and ceremonial coffee pots below.</p>
        </div>

        <div class="nile-calc-card">
          <div class="nile-calc-controls">
            <div class="nile-calc-field">
              <label for="nile-guest-count">Number of Diners: <span id="nile-guest-display" style="color: var(--nile-primary); font-weight: 800;">12 People</span></label>
              <input type="range" id="nile-guest-count" class="nile-range-slider" min="4" max="60" step="2" value="12">
            </div>
            <div class="nile-calc-field">
              <label for="nile-platter-style">Platter Style</label>
              <select id="nile-platter-style" class="nile-calc-select">
                <option value="combination">Grand Messob Combo (Meat Wats + Vegan Sides)</option>
                <option value="vegan-only">100% Vegan Beyaynetu Feast</option>
              </select>
            </div>
          </div>
          <div class="nile-calc-results">
            <div class="nile-result-box">
              <span class="num" id="nile-injera-total">36 Fresh Teff Injera Rolls</span>
              <span class="label">Sourdough Flatbread</span>
            </div>
            <div class="nile-result-box">
              <span class="num" id="nile-wat-total">8.4 lbs Mixed Wats &amp; Tibs</span>
              <span class="label">Simmered Stews Total</span>
            </div>
            <div class="nile-result-box">
              <span class="num" id="nile-coffee-total">2 Jebena Coffee Pots</span>
              <span class="label">Ceremonial Buna</span>
            </div>
          </div>
        </div>
      </section>
    </main>
'''
  },
  'menu.html': {
    'title': 'Menu - Nile Grocery & Cafe Charlotte NC',
    'nav': {'index': '', 'menu': 'active', 'traditions': '', 'tibs': '', 'vegan': '', 'visit': ''},
    'body': '''
    <main class="nile-section">
      <div class="nile-section-header">
        <span class="nile-section-eyebrow">Authentic Offerings</span>
        <h1 class="nile-section-title">Nile Grocery &amp; Cafe Menu</h1>
        <p class="nile-section-subtitle">Traditional Ethiopian meat stews, sizzling tibs, vegan sampler platters, and ceremonial coffee.</p>
      </div>

      <div class="nile-filter-tabs" role="tablist" aria-label="Menu Filter Tabs">
        <button type="button" class="nile-filter-btn active" data-filter="all">All Selections</button>
        <button type="button" class="nile-filter-btn" data-filter="meat">Meat Wats &amp; Tibs</button>
        <button type="button" class="nile-filter-btn" data-filter="vegan">Vegan Beyaynetu</button>
        <button type="button" class="nile-filter-btn" data-filter="starters">Starters &amp; Sambusas</button>
        <button type="button" class="nile-filter-btn" data-filter="drinks">Coffee &amp; Teas</button>
      </div>

      <div class="nile-menu-grid">
        <div class="nile-menu-item" data-category="meat">
          <div class="nile-menu-item-header">
            <span class="nile-menu-item-name">Doro Wat (Ethiopian National Stew)</span>
            <span class="nile-menu-item-price">$16.95</span>
          </div>
          <p class="nile-menu-item-desc">Slow-simmered tender chicken leg and thigh cooked in rich berbere sauce with caramelized red onions, garlic, spiced niter kibbeh butter, and a hard-boiled egg. Served on fresh injera.</p>
          <div class="nile-menu-item-badges">
            <span class="nile-badge nile-badge-gold">National Dish</span>
            <span class="nile-badge">Medium Spice</span>
          </div>
        </div>

        <div class="nile-menu-item" data-category="meat">
          <div class="nile-menu-item-header">
            <span class="nile-menu-item-name">Awaze Beef Tibs</span>
            <span class="nile-menu-item-price">$16.50</span>
          </div>
          <p class="nile-menu-item-desc">Tender cubes of lean beef seared with red onions, fresh rosemary, garlic, jalapeño peppers, and spicy Awaze chili paste.</p>
          <div class="nile-menu-item-badges">
            <span class="nile-badge nile-badge-gold">Sizzling Sensation</span>
          </div>
        </div>

        <div class="nile-menu-item" data-category="meat">
          <div class="nile-menu-item-header">
            <span class="nile-menu-item-name">Lega Lamb Tibs</span>
            <span class="nile-menu-item-price">$17.50</span>
          </div>
          <p class="nile-menu-item-desc">Succulent lamb morsels sautéed mild with ginger, sweet onions, tomatoes, and herbal butter, served with a side of house salad.</p>
          <div class="nile-menu-item-badges">
            <span class="nile-badge">Mild &amp; Savory</span>
          </div>
        </div>

        <div class="nile-menu-item" data-category="vegan">
          <div class="nile-menu-item-header">
            <span class="nile-menu-item-name">Vegan Beyaynetu Combo Platter</span>
            <span class="nile-menu-item-price">$15.95</span>
          </div>
          <p class="nile-menu-item-desc">A vibrant rainbow feast: Misir Wat (spicy red lentils), Kik Alicha (mild yellow split peas), Gomen (braised collards), Atakilt Wat (cabbage &amp; carrots), and Shiro (chickpea stew) over teff injera.</p>
          <div class="nile-menu-item-badges">
            <span class="nile-badge nile-badge-green">100% Plant-Based</span>
            <span class="nile-badge">Gluten-Friendly Teff</span>
          </div>
        </div>

        <div class="nile-menu-item" data-category="vegan">
          <div class="nile-menu-item-header">
            <span class="nile-menu-item-name">Shiro Mitten Wat</span>
            <span class="nile-menu-item-price">$13.50</span>
          </div>
          <p class="nile-menu-item-desc">Slow-simmered organic spiced chickpea flour cooked with garlic, onions, and berbere in a bubbling clay pot with warm injera.</p>
          <div class="nile-menu-item-badges">
            <span class="nile-badge nile-badge-green">Vegan Comfort</span>
          </div>
        </div>

        <div class="nile-menu-item" data-category="starters">
          <div class="nile-menu-item-header">
            <span class="nile-menu-item-name">Lentil Sambusas (3)</span>
            <span class="nile-menu-item-price">$5.75</span>
          </div>
          <p class="nile-menu-item-desc">Crispy golden pastry shells stuffed with seasoned brown lentils, scallions, and green chilies, served with spicy awaze dip.</p>
          <div class="nile-menu-item-badges">
            <span class="nile-badge nile-badge-green">Vegan Appetizer</span>
          </div>
        </div>

        <div class="nile-menu-item" data-category="drinks">
          <div class="nile-menu-item-header">
            <span class="nile-menu-item-name">Traditional Buna Coffee Ceremony</span>
            <span class="nile-menu-item-price">$9.50</span>
          </div>
          <p class="nile-menu-item-desc">Freshly pan-roasted Ethiopian Yirgacheffe coffee beans brewed in a traditional clay Jebena pot, served in small cups with freshly popped stovetop corn.</p>
          <div class="nile-menu-item-badges">
            <span class="nile-badge nile-badge-gold">Cultural Ceremony</span>
          </div>
        </div>

        <div class="nile-menu-item" data-category="drinks">
          <div class="nile-menu-item-header">
            <span class="nile-menu-item-name">Spiced Ethiopian Tea</span>
            <span class="nile-menu-item-price">$3.25</span>
          </div>
          <p class="nile-menu-item-desc">Black tea steeped with whole cloves, cinnamon bark, and crushed cardamom pods.</p>
          <div class="nile-menu-item-badges">
            <span class="nile-badge">Aromatic Brew</span>
          </div>
        </div>
      </div>
    </main>
'''
  },
  'ethiopian-culinary-traditions.html': {
    'title': 'Ethiopian Traditions - Nile Grocery & Cafe',
    'nav': {'index': '', 'menu': '', 'traditions': 'active', 'tibs': '', 'vegan': '', 'visit': ''},
    'body': '''
    <main class="nile-section">
      <div class="nile-section-header">
        <span class="nile-section-eyebrow">Heritage &amp; Craft</span>
        <h1 class="nile-section-title">The Ancient Craft of Ethiopian Cooking</h1>
        <p class="nile-section-subtitle">Discover how naturally fermented teff injera, hand-blended berbere spices, and the communal table shape our culinary identity.</p>
      </div>

      <div class="nile-story-grid">
        <div class="nile-story-content">
          <h3>The Fermented Miracle of Teff Injera</h3>
          <p>Injera is the beating heart of Ethiopian dining. Made from teff &mdash; a tiny, mineral-dense ancient grain native to the Ethiopian highlands &mdash; the batter is naturally fermented for three to four days with wild sourdough cultures.</p>
          <p>Poured onto a hot circular griddle (mitad), thousands of tiny steam vents called <em>ayen</em> (eyes) form across its surface. The resulting flatbread is spongy, pleasantly sour, and acts as plate, utensil, and bread all in one.</p>
        </div>
        <div class="nile-story-img-wrap">
          <img src="images/injera.jpg" alt="Traditional fermented teff injera rolls on woven presentation" width="600" height="380">
        </div>
      </div>

      <div class="nile-story-grid" style="margin-top: 4.5rem;">
        <div class="nile-story-img-wrap">
          <img src="images/vegan.jpg" alt="Rich vibrant Ethiopian spices and lentil stews" width="600" height="380">
        </div>
        <div class="nile-story-content">
          <h3>Berbere &amp; Niter Kibbeh: The Soul Spices</h3>
          <p>The intoxicating depth of Ethiopian cuisine relies on two cornerstone preparations:</p>
          <p><strong>Berbere:</strong> A fiery, complex spice rub composed of sun-dried red chili peppers, fenugreek, korarima (Ethiopian cardamom), ginger, allspice, and cloves slowly ground to a velvety crimson powder.</p>
          <p><strong>Niter Kibbeh:</strong> Clarified butter simmered with garlic, ginger, sacred basil (kosseret), and turmeric, infusing every braise with unctuous aromatic richness.</p>
        </div>
      </div>
    </main>
'''
  },
  'tibs-and-doro-wat.html': {
    'title': 'Tibs & Doro Wat - Nile Grocery & Cafe',
    'nav': {'index': '', 'menu': '', 'traditions': '', 'tibs': 'active', 'vegan': '', 'visit': ''},
    'body': '''
    <main class="nile-section">
      <div class="nile-section-header">
        <span class="nile-section-eyebrow">Celebrated Meat Specialties</span>
        <h1 class="nile-section-title">Sizzling Tibs &amp; Classic Doro Wat</h1>
        <p class="nile-section-subtitle">Deep dive into Ethiopia’s most revered savory braises and sizzling skillet preparations.</p>
      </div>

      <div class="nile-story-grid">
        <div class="nile-story-img-wrap">
          <img src="images/hero.jpg" alt="Doro wat chicken stew with hard-boiled egg and injera" width="600" height="380">
        </div>
        <div class="nile-story-content">
          <h3>Doro Wat: The National Treasure</h3>
          <p>Doro Wat is the ultimate celebratory dish of Ethiopia, served on holidays and joyful family milestones. Its preparation is an act of deep patience: pounds of sweet red onions are slowly caramelized without oil for hours until they break down into a luscious, sweet paste.</p>
          <p>Infused with berbere, garlic, ginger, and niter kibbeh, chicken pieces are gently braised until they fall off the bone. Pierced hard-boiled eggs are simmered in the sauce, soaking up the crimson aromatics.</p>
        </div>
      </div>

      <div class="nile-story-grid" style="margin-top: 4.5rem;">
        <div class="nile-story-content">
          <h3>Awaze Beef &amp; Lamb Tibs</h3>
          <p>For a flash-cooked, sizzling experience, nothing compares to Tibs. We cube tender grass-fed beef or lamb, searing it in an iron skillet over high heat with rosemary sprigs, red onions, garlic, and fresh green jalapeños.</p>
          <p>Tossed with our signature Awaze sauce (berbere and honey wine vinegar reduction), it delivers an unforgettable smoky, spicy, and herbal punch.</p>
        </div>
        <div class="nile-story-img-wrap">
          <img src="images/tibs.jpg" alt="Sizzling pan of beef tibs with jalapeño and rosemary" width="600" height="380">
        </div>
      </div>
    </main>
'''
  },
  'vegan-beyaynetu-and-coffee.html': {
    'title': 'Vegan Beyaynetu & Coffee - Nile Grocery & Cafe',
    'nav': {'index': '', 'menu': '', 'traditions': '', 'tibs': '', 'vegan': 'active', 'visit': ''},
    'body': '''
    <main class="nile-section">
      <div class="nile-section-header">
        <span class="nile-section-eyebrow">Plant-Based Heritage &amp; Ritual</span>
        <h1 class="nile-section-title">Vegan Beyaynetu &amp; The Buna Ceremony</h1>
        <p class="nile-section-subtitle">Centuries of fasting tradition have created one of the world’s greatest vegan cuisines.</p>
      </div>

      <div class="nile-story-grid">
        <div class="nile-story-content">
          <h3>The Art of Vegan Beyaynetu</h3>
          <p>Due to the Ethiopian Orthodox fasting calendar (Tsom), Ethiopian cooking has perfected rich, protein-dense vegan stews over hundreds of years. Our Beyaynetu sampler includes:</p>
          <p><strong>Misir Wat:</strong> Red lentils stewed in spicy, aromatic berbere sauce.</p>
          <p><strong>Kik Alicha:</strong> Yellow split peas gently simmered with turmeric and garlic.</p>
          <p><strong>Gomen:</strong> Tender collard greens slow-braised with ginger and mild spices.</p>
          <p><strong>Shiro Wat:</strong> Velvety ground chickpea flour whipped into a comforting, savory gravy.</p>
        </div>
        <div class="nile-story-img-wrap">
          <img src="images/vegan.jpg" alt="Colorful vegan Ethiopian sampler platter with lentils and vegetables" width="600" height="380">
        </div>
      </div>

      <div class="nile-story-grid" style="margin-top: 4.5rem;">
        <div class="nile-story-img-wrap">
          <img src="images/coffee.jpg" alt="Traditional Ethiopian clay jebena coffee pot with small ceramic cups" width="600" height="380">
        </div>
        <div class="nile-story-content">
          <h3>The Buna Coffee Ceremony</h3>
          <p>Ethiopia is the historical birthplace of coffee. The <strong>Buna Ceremony</strong> is a sacred ritual of hospitality and gratitude. Raw green coffee beans are washed and pan-roasted over open flame before guests, filling the room with sweet coffee aroma and fragrant frankincense smoke.</p>
          <p>Ground by hand and boiled in a traditional clay <em>Jebena</em> pot, the coffee is poured from high above into handleless ceramic cups and served with fresh stovetop popcorn.</p>
        </div>
      </div>
    </main>
'''
  },
  'visit.html': {
    'title': 'Visit & Order - Nile Grocery & Cafe Charlotte NC',
    'nav': {'index': '', 'menu': '', 'traditions': '', 'tibs': '', 'vegan': '', 'visit': 'active'},
    'body': '''
    <main class="nile-section">
      <div class="nile-section-header">
        <span class="nile-section-eyebrow">Dine In &bull; Grocery Market &bull; Catering</span>
        <h1 class="nile-section-title">Visit Nile Grocery &amp; Cafe</h1>
        <p class="nile-section-subtitle">Located on North Sharon Amity Road in East Charlotte. Join us for lunch, dinner, or shop authentic imported Ethiopian goods.</p>
      </div>

      <div class="nile-contact-grid">
        <div class="nile-contact-card">
          <h3>East Charlotte Location</h3>
          <p style="color: var(--nile-text-muted); margin-bottom: 0.8rem;">Conveniently located near Central Avenue and Sharon Amity shopping centers with ample parking.</p>
          <p><strong>Address:</strong> 3113 N Sharon Amity Rd, Charlotte, NC 28205</p>
          <p style="margin-top: 0.4rem;"><strong>Setting:</strong> Casual, family-friendly cafe combined with an Ethiopian specialty grocery.</p>
          <div style="margin-top: 1.5rem;">
            <a href="tel:7045688090" class="nile-btn-primary" style="width: 100%; text-align: center;">Call to Order: (704) 568-8090</a>
          </div>
        </div>

        <div class="nile-contact-card">
          <h3>Operating Hours</h3>
          <div class="nile-hours-row">
            <span>Monday &ndash; Saturday</span>
            <span>11:00 AM &ndash; 9:00 PM</span>
          </div>
          <div class="nile-hours-row">
            <span>Sunday</span>
            <span>12:00 PM &ndash; 8:00 PM</span>
          </div>
          <div style="margin-top: 1.5rem; background: var(--nile-surface-alt); padding: 1rem; border-radius: var(--nile-radius-sm);">
            <p style="font-size: 0.85rem; color: var(--nile-primary-dark); font-weight: 700;">Fresh Injera baked daily. Calling ahead is recommended for large groups or traditional coffee ceremonies.</p>
          </div>
        </div>

        <div class="nile-contact-card">
          <h3>Family Feasts &amp; Event Catering</h3>
          <p style="color: var(--nile-text-muted); margin-bottom: 0.8rem;">Custom Messob platters of Doro Wat, Beef Tibs, Vegan Beyaynetu, and bulk bags of fresh teff injera for private events and celebrations.</p>
          <p><strong>Notice:</strong> Please call at least 24 hours in advance for catering platters.</p>
          <div style="margin-top: 1.5rem;">
            <a href="mailto:catering@nilegrocerycafe.com" class="nile-btn-secondary" style="width: 100%; text-align: center;">Inquire for Catering</a>
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
    nav_traditions=data['nav']['traditions'],
    nav_tibs=data['nav']['tibs'],
    nav_vegan=data['nav']['vegan'],
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
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="site.css">
</head>
<body>
  <header class="nile-header">
    <div class="nile-nav-container">
      <a href="index.html" class="nile-brand">
        <span class="nile-brand-title">Nile Grocery &amp; Cafe</span>
        <span class="nile-brand-subtitle">Authentic Ethiopian &bull; East Charlotte</span>
      </a>
      <button class="nile-nav-toggle" type="button" aria-label="Toggle navigation menu" aria-expanded="false">Menu</button>
{cur_nav}
    </div>
  </header>

{data['body']}

{footer_content}
  <script src="site.js"></script>
</body>
</html>'''

  filepath = os.path.join('nile-grocery-and-cafe', filename)
  with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html_doc.strip() + '\n')
  print(f'Wrote {filename}')

print('All 6 HTML pages for Nile Grocery & Cafe written successfully')
