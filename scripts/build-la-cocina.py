import os

nav_template = '''
      <nav class="cocina-nav" aria-label="Primary Navigation">
        <ul class="cocina-nav-list">
          <li><a href="index.html" class="cocina-nav-link {nav_index}">Home</a></li>
          <li><a href="menu.html" class="cocina-nav-link {nav_menu}">Menu</a></li>
          <li><a href="traditional-mexican-craft.html" class="cocina-nav-link {nav_craft}">Mexican Craft</a></li>
          <li><a href="tacos-and-specialties.html" class="cocina-nav-link {nav_tacos}">Tacos &amp; Specialties</a></li>
          <li><a href="aguas-frescas-and-sides.html" class="cocina-nav-link {nav_sides}">Aguas &amp; Sides</a></li>
          <li><a href="visit.html" class="cocina-nav-link cocina-nav-cta {nav_visit}">Visit &amp; Order</a></li>
        </ul>
      </nav>
'''

footer_content = '''
  <footer class="cocina-footer">
    <div class="cocina-footer-container">
      <div class="cocina-footer-brand">
        <h4>La Cocina Mexicana</h4>
        <p>Honoring traditional Mexican culinary heritage with heirloom corn masa, slow-simmered regional braises, and hand-crafted aguas frescas in Charlotte, NC.</p>
      </div>
      <div class="cocina-footer-nav">
        <h5>Explore Demo</h5>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Full Menu</a></li>
          <li><a href="traditional-mexican-craft.html">Traditional Craft</a></li>
          <li><a href="tacos-and-specialties.html">Tacos &amp; Specialties</a></li>
          <li><a href="aguas-frescas-and-sides.html">Aguas Frescas &amp; Sides</a></li>
          <li><a href="visit.html">Visit &amp; Hours</a></li>
        </ul>
      </div>
      <div class="cocina-footer-hours">
        <h5>Hours &amp; Location</h5>
        <p style="color: #99938a; font-size: 0.9rem; margin-bottom: 0.5rem;">Charlotte, North Carolina</p>
        <p style="color: #99938a; font-size: 0.9rem;">Mon - Sat: 11:00 AM - 9:30 PM<br>Sunday: 11:00 AM - 8:00 PM</p>
      </div>
    </div>
    <div class="cocina-footer-bottom">
      <p>&copy; 2026 La Cocina Mexicana. All rights reserved. Culinary showcase demo for Charlotte dining.</p>
    </div>
  </footer>
'''

pages = {
  'index.html': {
    'title': 'La Cocina Mexicana - Traditional Mexican Taqueria & Kitchen in Charlotte NC',
    'nav': {'index': 'active', 'menu': '', 'craft': '', 'tacos': '', 'sides': '', 'visit': ''},
    'body': '''
    <main>
      <section class="cocina-hero">
        <div class="cocina-hero-grid">
          <div class="cocina-hero-content">
            <span class="cocina-hero-badge">Traditional Mexican Kitchen &bull; Charlotte, NC</span>
            <h1 class="cocina-hero-title">Authentic Heritage Flavors, <span>Pressed Daily</span></h1>
            <p class="cocina-hero-lead">Experience the vibrant culinary soul of Mexico with stone-ground heirloom corn tortillas, 12-hour slow-cooked birria de res, and refreshing house-brewed aguas frescas.</p>
            <div class="cocina-hero-actions">
              <a href="menu.html" class="cocina-btn-primary">Explore Full Menu</a>
              <a href="traditional-mexican-craft.html" class="cocina-btn-secondary">Our Masa Craft</a>
            </div>
          </div>
          <div class="cocina-hero-img-wrap">
            <img src="images/hero.jpg" alt="Traditional Mexican food feast with tacos, salsas, and fresh lime" width="600" height="420">
          </div>
        </div>
      </section>

      <section class="cocina-features">
        <div class="cocina-feature-grid">
          <div class="cocina-feature-card">
            <div class="cocina-feature-tag">Heirloom Masa</div>
            <h2 class="cocina-feature-title">Nixtamal Corn Tortillas</h2>
            <p class="cocina-feature-desc">Pressed on the comal upon every order for tender, aromatic tacos that honor ancestral techniques.</p>
          </div>
          <div class="cocina-feature-card">
            <div class="cocina-feature-tag">Slow Braised</div>
            <h2 class="cocina-feature-title">Birria &amp; Carnitas</h2>
            <p class="cocina-feature-desc">Rich chili-infused consom&eacute; and golden Michoac&aacute;n-style pork braised with Mexican canela and orange peel.</p>
          </div>
          <div class="cocina-feature-card">
            <div class="cocina-feature-tag">Natural Refreshment</div>
            <h2 class="cocina-feature-title">House Aguas Frescas</h2>
            <p class="cocina-feature-desc">Daily small-batch Horchata, steeped Agua de Jamaica, and zesty Tamarindo crafted from real whole ingredients.</p>
          </div>
        </div>
      </section>

      <section class="cocina-section">
        <div class="cocina-story-grid">
          <div class="cocina-story-img-wrap">
            <img src="images/tacos.jpg" alt="Authentic street tacos on warm corn tortillas with cilantro and diced onions" width="600" height="380">
          </div>
          <div class="cocina-story-content">
            <span class="cocina-section-eyebrow">Signature Specialties</span>
            <h3>Street Tacos Rooted in Tradition</h3>
            <p>At La Cocina Mexicana, we believe that great tacos begin with great tortillas. We source heirloom corn and press each tortilla fresh on the hot griddle.</p>
            <p>From tender marinated Al Pastor with roasted pineapple to rich Carne Asada grilled over high heat, every plate is finished with hand-minced cilantro, sweet white onions, and our signature roasted tomatillo salsas.</p>
            <a href="tacos-and-specialties.html" class="cocina-btn-primary" style="margin-top: 1rem;">View Taco Lineup</a>
          </div>
        </div>
      </section>

      <section class="cocina-section" style="background: var(--cocina-surface); border-top: 1px solid var(--cocina-border); border-bottom: 1px solid var(--cocina-border);">
        <div class="cocina-section-header">
          <span class="cocina-section-eyebrow">Event &amp; Family Catering</span>
          <h2 class="cocina-section-title">Interactive Party Platter Estimator</h2>
          <p class="cocina-section-subtitle">Planning a family gathering, tailgate, or office luncheon? Calculate your taco platter and side requirements below.</p>
        </div>

        <div class="cocina-calc-card">
          <div class="cocina-calc-controls">
            <div class="cocina-calc-field">
              <label for="cocina-guest-count">Estimated Number of Guests: <span id="cocina-guest-display" style="color: var(--cocina-primary); font-weight: 800;">20 Guests</span></label>
              <input type="range" id="cocina-guest-count" class="cocina-range-slider" min="10" max="100" step="5" value="20">
            </div>
            <div class="cocina-calc-field">
              <label for="cocina-platter-style">Appetite / Serving Style</label>
              <select id="cocina-platter-style" class="cocina-calc-select">
                <option value="standard">Standard Buffet (3 Tacos / Person)</option>
                <option value="hearty">Hearty Appetite (4 Tacos / Person)</option>
              </select>
            </div>
          </div>
          <div class="cocina-calc-results">
            <div class="cocina-result-box">
              <span class="num" id="cocina-taco-total">60 Tacos</span>
              <span class="label">Hand-Pressed Tacos</span>
            </div>
            <div class="cocina-result-box">
              <span class="num" id="cocina-side-total">7.0 lbs (Rice &amp; Beans)</span>
              <span class="label">Fresh Sides Total</span>
            </div>
            <div class="cocina-result-box">
              <span class="num" id="cocina-salsa-total">3 Pints Salsa &amp; Chips</span>
              <span class="label">House Salsas &amp; Totopos</span>
            </div>
          </div>
        </div>
      </section>
    </main>
'''
  },
  'menu.html': {
    'title': 'Menu - La Cocina Mexicana Charlotte NC',
    'nav': {'index': '', 'menu': 'active', 'craft': '', 'tacos': '', 'sides': '', 'visit': ''},
    'body': '''
    <main class="cocina-section">
      <div class="cocina-section-header">
        <span class="cocina-section-eyebrow">Authentic Offerings</span>
        <h1 class="cocina-section-title">La Cocina Mexicana Menu</h1>
        <p class="cocina-section-subtitle">Explore our comprehensive selection of hand-pressed tacos, traditional specialties, savory sides, and house-brewed drinks.</p>
      </div>

      <div class="cocina-filter-tabs" role="tablist" aria-label="Menu Categories">
        <button type="button" class="cocina-filter-btn active" data-filter="all">All Selections</button>
        <button type="button" class="cocina-filter-btn" data-filter="tacos">Street Tacos</button>
        <button type="button" class="cocina-filter-btn" data-filter="especiales">Especialidades</button>
        <button type="button" class="cocina-filter-btn" data-filter="antojitos">Antojitos &amp; Sides</button>
        <button type="button" class="cocina-filter-btn" data-filter="bebidas">Aguas &amp; Bebidas</button>
      </div>

      <div class="cocina-menu-grid">
        <div class="cocina-menu-item" data-category="tacos">
          <div class="cocina-menu-item-header">
            <span class="cocina-menu-item-name">Tacos de Birria de Res (3)</span>
            <span class="cocina-menu-item-price">$14.50</span>
          </div>
          <p class="cocina-menu-item-desc">Slow-braised shredded beef tucked in griddled corn tortillas with melted Oaxaca cheese, cilantro, onions, and a bowl of rich dipping consom&eacute;.</p>
          <div class="cocina-menu-item-badges">
            <span class="cocina-badge cocina-badge-spice">House Favorite</span>
            <span class="cocina-badge cocina-badge-gf">Gluten-Friendly</span>
          </div>
        </div>

        <div class="cocina-menu-item" data-category="tacos">
          <div class="cocina-menu-item-header">
            <span class="cocina-menu-item-name">Tacos Al Pastor (3)</span>
            <span class="cocina-menu-item-price">$12.95</span>
          </div>
          <p class="cocina-menu-item-desc">Achiote-marinated pork roasted with charred pineapple relish, chopped sweet white onion, fresh cilantro, and salsa roja.</p>
          <div class="cocina-menu-item-badges">
            <span class="cocina-badge cocina-badge-spice">Medium Spice</span>
            <span class="cocina-badge cocina-badge-gf">Heirloom Masa</span>
          </div>
        </div>

        <div class="cocina-menu-item" data-category="tacos">
          <div class="cocina-menu-item-header">
            <span class="cocina-menu-item-name">Carnitas Michoac&aacute;n (3)</span>
            <span class="cocina-menu-item-price">$12.50</span>
          </div>
          <p class="cocina-menu-item-desc">Traditional copper-kettle confit pork shoulder, crispy exterior, tender interior, served with pickled red onions and salsa verde cruda.</p>
          <div class="cocina-menu-item-badges">
            <span class="cocina-badge cocina-badge-gf">Gluten-Friendly</span>
          </div>
        </div>

        <div class="cocina-menu-item" data-category="tacos">
          <div class="cocina-menu-item-header">
            <span class="cocina-menu-item-name">Carne Asada Tacos (3)</span>
            <span class="cocina-menu-item-price">$13.95</span>
          </div>
          <p class="cocina-menu-item-desc">Citrus-marinated skirt steak seared over high heat, served on double corn tortillas with grilled green cebollitas and avocado crema.</p>
          <div class="cocina-menu-item-badges">
            <span class="cocina-badge cocina-badge-gf">Gluten-Friendly</span>
          </div>
        </div>

        <div class="cocina-menu-item" data-category="especiales">
          <div class="cocina-menu-item-header">
            <span class="cocina-menu-item-name">Enchiladas Suizas</span>
            <span class="cocina-menu-item-price">$15.25</span>
          </div>
          <p class="cocina-menu-item-desc">Three hand-rolled corn tortillas filled with shredded chicken tinga, smothered in creamy roasted tomatillo sauce and melted Chihuahua cheese, with Mexican rice and refried black beans.</p>
          <div class="cocina-menu-item-badges">
            <span class="cocina-badge">Plato Fuerte</span>
          </div>
        </div>

        <div class="cocina-menu-item" data-category="especiales">
          <div class="cocina-menu-item-header">
            <span class="cocina-menu-item-name">Sizzling Fajitas Mixtas</span>
            <span class="cocina-menu-item-price">$18.95</span>
          </div>
          <p class="cocina-menu-item-desc">Marinated skirt steak, jumbo gulf shrimp, and seasoned chicken breast grilled with bell peppers and Spanish onions on a piping cast iron skillet.</p>
          <div class="cocina-menu-item-badges">
            <span class="cocina-badge">Served with Warm Masa</span>
          </div>
        </div>

        <div class="cocina-menu-item" data-category="antojitos">
          <div class="cocina-menu-item-header">
            <span class="cocina-menu-item-name">Guacamole en Molcajete</span>
            <span class="cocina-menu-item-price">$9.50</span>
          </div>
          <p class="cocina-menu-item-desc">Fresh Hass avocados crushed tableside style with lime, serrano pepper, cilantro, sea salt, and warm crispy tortilla totopos.</p>
          <div class="cocina-menu-item-badges">
            <span class="cocina-badge cocina-badge-gf">Vegetarian</span>
          </div>
        </div>

        <div class="cocina-menu-item" data-category="antojitos">
          <div class="cocina-menu-item-header">
            <span class="cocina-menu-item-name">Elote Callejero</span>
            <span class="cocina-menu-item-price">$5.75</span>
          </div>
          <p class="cocina-menu-item-desc">Charred sweet corn on the cob brushed with chipotle crema, dusted with cotija cheese, chile piqu&iacute;n, and fresh lime wedge.</p>
          <div class="cocina-menu-item-badges">
            <span class="cocina-badge">Street Favorite</span>
          </div>
        </div>

        <div class="cocina-menu-item" data-category="bebidas">
          <div class="cocina-menu-item-header">
            <span class="cocina-menu-item-name">Agua de Horchata Fresca</span>
            <span class="cocina-menu-item-price">$4.25</span>
          </div>
          <p class="cocina-menu-item-desc">House-made rice and almond milk infused with Mexican canela cinnamon and pure cane sugar, served iced.</p>
          <div class="cocina-menu-item-badges">
            <span class="cocina-badge cocina-badge-gf">Hand-Crafted</span>
          </div>
        </div>

        <div class="cocina-menu-item" data-category="bebidas">
          <div class="cocina-menu-item-header">
            <span class="cocina-menu-item-name">Agua de Jamaica</span>
            <span class="cocina-menu-item-price">$4.25</span>
          </div>
          <p class="cocina-menu-item-desc">Tart and refreshing cold-steeped wild hibiscus flower tea sweetened lightly with piloncillo.</p>
          <div class="cocina-menu-item-badges">
            <span class="cocina-badge cocina-badge-gf">Antioxidant Rich</span>
          </div>
        </div>
      </div>
    </main>
'''
  },
  'traditional-mexican-craft.html': {
    'title': 'Traditional Mexican Craft - La Cocina Mexicana',
    'nav': {'index': '', 'menu': '', 'craft': 'active', 'tacos': '', 'sides': '', 'visit': ''},
    'body': '''
    <main class="cocina-section">
      <div class="cocina-section-header">
        <span class="cocina-section-eyebrow">Heritage &amp; Process</span>
        <h1 class="cocina-section-title">The Craft of Traditional Mexican Cooking</h1>
        <p class="cocina-section-subtitle">Discover how time-honored culinary practices, heirloom ingredients, and artisanal techniques shape every recipe at La Cocina Mexicana.</p>
      </div>

      <div class="cocina-story-grid">
        <div class="cocina-story-content">
          <h3>The Art of Nixtamal Masa</h3>
          <p>The foundation of authentic Mexican cuisine is the tortilla. We begin with non-GMO heirloom maize, soaking and simmering whole corn kernels in alkaline mineral water &mdash; the millennia-old Mesoamerican process known as nixtamalization.</p>
          <p>Ground on volcanic stone mills into silky, pliable masa, each tortilla is pressed and griddled on a blistering comal seconds before reaching your plate. The result is an unmistakable fragrant aroma, delicate chew, and natural sweetness.</p>
        </div>
        <div class="cocina-story-img-wrap">
          <img src="images/craft.jpg" alt="Traditional cooking and fresh ingredients for Mexican cuisine" width="600" height="380">
        </div>
      </div>

      <div class="cocina-story-grid" style="margin-top: 5rem;">
        <div class="cocina-story-img-wrap">
          <img src="images/specialties.jpg" alt="Sizzling pan of traditional Mexican braised meats and spices" width="600" height="380">
        </div>
        <div class="cocina-story-content">
          <h3>Slow-Simmered Guisados &amp; Recetas</h3>
          <p>In Mexican homes and fondas, great flavors cannot be rushed. Our braises, known as guisados, develop complex depths through hours of gentle simmering.</p>
          <p>Dried chiles &mdash; smoky ancho, fruity guajillo, and piquant pasilla &mdash; are toasted on the dry comal before being blended with Mexican oregano, cumin, garlic, and citrus. This rich adobo marinates meats for over 24 hours before slow braising to melting tenderness.</p>
        </div>
      </div>
    </main>
'''
  },
  'tacos-and-specialties.html': {
    'title': 'Tacos & Specialties - La Cocina Mexicana',
    'nav': {'index': '', 'menu': '', 'craft': '', 'tacos': 'active', 'sides': '', 'visit': ''},
    'body': '''
    <main class="cocina-section">
      <div class="cocina-section-header">
        <span class="cocina-section-eyebrow">Culinary Showcase</span>
        <h1 class="cocina-section-title">Signature Tacos &amp; House Specialties</h1>
        <p class="cocina-section-subtitle">Explore our authentic regional taco varieties and hearty platters prepared with scratch ingredients and uncompromising quality.</p>
      </div>

      <div class="cocina-story-grid">
        <div class="cocina-story-img-wrap">
          <img src="images/tacos.jpg" alt="Platter of street tacos garnished with lime wedges and cilantro" width="600" height="380">
        </div>
        <div class="cocina-story-content">
          <h3>Regional Taco Showcase</h3>
          <p><strong>Birria de Res:</strong> Jalisco-style chuck roast slow-braised with guajillo chilies and cloves. Griddled until crisp with Oaxaca cheese and served alongside rich beef consom&eacute; for dipping.</p>
          <p><strong>Tacos Al Pastor:</strong> Thin slices of pork tenderloin steeped in achiote and citrus marinade, griddled with sweet pineapple cubes and cilantro.</p>
          <p><strong>Carnitas Tradicionales:</strong> Michoac&aacute;n-style pork shoulder slowly simmered in copper calderos with canela and orange zest, crispy on the edges and exceptionally tender.</p>
          <p><strong>Pollo en Tinga:</strong> Shredded chicken simmered in a smoky chipotle-tomato broth with sweet caramelized Spanish onions.</p>
        </div>
      </div>

      <div class="cocina-story-grid" style="margin-top: 5rem;">
        <div class="cocina-story-content">
          <h3>Especialidades de la Casa</h3>
          <p>Beyond our tacos, we serve iconic Mexican comfort dishes crafted with the same commitment to ancestral technique:</p>
          <p><strong>Enchiladas Suizas:</strong> Soft corn tortillas filled with seasoned chicken, bathed in our velvety roasted tomatillo-cream sauce, and gratinated under melted Chihuahua cheese.</p>
          <p><strong>Carne Asada al Carb&oacute;n:</strong> Prime flank steak marinated in citrus mojo, seared over open flame, and paired with charro beans, Mexican red rice, grilled bulb onions, and fresh guacamole.</p>
        </div>
        <div class="cocina-story-img-wrap">
          <img src="images/specialties.jpg" alt="House specialty sizzling skillet with fajitas and traditional sides" width="600" height="380">
        </div>
      </div>
    </main>
'''
  },
  'aguas-frescas-and-sides.html': {
    'title': 'Aguas Frescas & Sides - La Cocina Mexicana',
    'nav': {'index': '', 'menu': '', 'craft': '', 'tacos': '', 'sides': 'active', 'visit': ''},
    'body': '''
    <main class="cocina-section">
      <div class="cocina-section-header">
        <span class="cocina-section-eyebrow">Bebidas y Acompa&ntilde;amientos</span>
        <h1 class="cocina-section-title">House-Brewed Aguas Frescas &amp; Authentic Sides</h1>
        <p class="cocina-section-subtitle">Complement your meal with natural fruit beverages, handcrafted molcajete guacamole, and traditional side dishes.</p>
      </div>

      <div class="cocina-story-grid">
        <div class="cocina-story-content">
          <h3>Handcrafted Aguas Frescas</h3>
          <p>In Mexico, no meal is complete without an icy glass of fresh agua fresca. We craft each variety from scratch every morning with pure natural ingredients:</p>
          <p><strong>Horchata de Arroz:</strong> Soaked long-grain rice, sweet almonds, Ceylon canela cinnamon, and vanilla, strained to silky perfection.</p>
          <p><strong>Agua de Jamaica:</strong> Sun-dried hibiscus blossoms steeped in small batches for a brisk, floral, ruby-red tonic.</p>
          <p><strong>Tamarindo Natural:</strong> Sweet-sour whole tamarind pulp simmered and chilled with raw piloncillo sugar.</p>
        </div>
        <div class="cocina-story-img-wrap">
          <img src="images/drinks.jpg" alt="Chilled refreshing beverage glasses garnished with fresh fruit" width="600" height="380">
        </div>
      </div>

      <div class="cocina-story-grid" style="margin-top: 5rem;">
        <div class="cocina-story-img-wrap">
          <img src="images/hero.jpg" alt="Freshly made guacamole and tortilla chips with sides" width="600" height="380">
        </div>
        <div class="cocina-story-content">
          <h3>Signature Complements &amp; Sides</h3>
          <p><strong>Guacamole en Molcajete:</strong> Fresh ripe Hass avocados hand-mashed with diced serrano peppers, cilantro, lime juice, and sea salt, served with fresh warm tortilla totopos.</p>
          <p><strong>Elote Callejero:</strong> Sweet corn on the cob griddled over flame, painted with tangy chipotle crema, grated cotija cheese, and chile de &aacute;rbol powder.</p>
          <p><strong>Frijoles Charros:</strong> Slow-simmered pinto beans prepared with smoked bacon, roasted jalape&ntilde;os, Roma tomatoes, and fresh cilantro.</p>
        </div>
      </div>
    </main>
'''
  },
  'visit.html': {
    'title': 'Visit & Order - La Cocina Mexicana Charlotte NC',
    'nav': {'index': '', 'menu': '', 'craft': '', 'tacos': '', 'sides': '', 'visit': 'active'},
    'body': '''
    <main class="cocina-section">
      <div class="cocina-section-header">
        <span class="cocina-section-eyebrow">Dine In, Takeout &amp; Catering</span>
        <h1 class="cocina-section-title">Visit La Cocina Mexicana</h1>
        <p class="cocina-section-subtitle">Join us for lunch, dinner, or take home authentic tacos and house-crafted specialties in Charlotte, NC.</p>
      </div>

      <div class="cocina-contact-grid">
        <div class="cocina-contact-card">
          <h3>Location &amp; Dining</h3>
          <p style="color: var(--cocina-text-muted); margin-bottom: 1rem;">Conveniently serving the greater Charlotte metropolitan area with fast-casual dine-in, express counter pickup, and family meal packages.</p>
          <p><strong>Address:</strong> Charlotte, North Carolina</p>
          <p style="margin-top: 0.5rem;"><strong>Atmosphere:</strong> Casual, family-friendly taqueria with indoor seating and outdoor patio tables.</p>
          <div style="margin-top: 1.5rem;">
            <a href="tel:7045358820" class="cocina-btn-primary" style="width: 100%; text-align: center;">Call for Takeout: (704) 535-8820</a>
          </div>
        </div>

        <div class="cocina-contact-card">
          <h3>Operating Hours</h3>
          <div class="cocina-hours-row">
            <span>Monday &ndash; Thursday</span>
            <span>11:00 AM &ndash; 9:00 PM</span>
          </div>
          <div class="cocina-hours-row">
            <span>Friday &ndash; Saturday</span>
            <span>11:00 AM &ndash; 9:30 PM</span>
          </div>
          <div class="cocina-hours-row">
            <span>Sunday</span>
            <span>11:00 AM &ndash; 8:00 PM</span>
          </div>
          <div style="margin-top: 1.5rem; background: var(--cocina-surface-alt); padding: 1rem; border-radius: var(--cocina-radius-sm);">
            <p style="font-size: 0.85rem; color: var(--cocina-primary-dark); font-weight: 600;">Direct phone ordering available for quick pickup. Catering orders recommended 24 hours in advance.</p>
          </div>
        </div>

        <div class="cocina-contact-card">
          <h3>Catering &amp; Group Orders</h3>
          <p style="color: var(--cocina-text-muted); margin-bottom: 1rem;">Bring the flavors of our scratch Mexican kitchen to your office lunch, birthday fiesta, or private gathering.</p>
          <p><strong>Taco Bar Packages:</strong> Includes warm handmade corn tortillas, choice of 3 meats, sides of Mexican rice &amp; beans, house salsas, chips, and garnishes.</p>
          <div style="margin-top: 1.5rem;">
            <a href="mailto:catering@lacocinamexicanaclt.com" class="cocina-btn-secondary" style="width: 100%; text-align: center;">Inquire for Catering</a>
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
    nav_tacos=data['nav']['tacos'],
    nav_sides=data['nav']['sides'],
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
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="site.css">
</head>
<body>
  <header class="cocina-header">
    <div class="cocina-nav-container">
      <a href="index.html" class="cocina-brand">
        <span class="cocina-brand-title">La Cocina Mexicana</span>
        <span class="cocina-brand-subtitle">Taqueria &amp; Cocina Tradicional</span>
      </a>
      <button class="cocina-nav-toggle" type="button" aria-label="Toggle navigation menu" aria-expanded="false">Menu</button>
{cur_nav}
    </div>
  </header>

{data['body']}

{footer_content}
  <script src="site.js"></script>
</body>
</html>'''

  filepath = os.path.join('la-cocina-mexicana', filename)
  with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html_doc.strip() + '\n')
  print(f'Wrote {filename}')

print('All 6 HTML pages written successfully')
