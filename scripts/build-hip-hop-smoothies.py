import os

nav_template = '''
      <nav class="hhs-nav" aria-label="Primary Navigation">
        <ul class="hhs-nav-list">
          <li><a href="index.html" class="hhs-nav-link {nav_index}">Home</a></li>
          <li><a href="menu.html" class="hhs-nav-link {nav_menu}">Tracklist Menu</a></li>
          <li><a href="culture-and-community.html" class="hhs-nav-link {nav_culture}">Culture &amp; Roots</a></li>
          <li><a href="signature-smoothies.html" class="hhs-nav-link {nav_smoothies}">Hit Smoothies</a></li>
          <li><a href="acai-bowls-and-boosts.html" class="hhs-nav-link {nav_bowls}">Bowls &amp; Boosts</a></li>
          <li><a href="visit.html" class="hhs-nav-link hhs-nav-cta {nav_visit}">Visit &amp; Order</a></li>
        </ul>
      </nav>
'''

footer_content = '''
  <footer class="hhs-footer">
    <div class="hhs-footer-container">
      <div class="hhs-footer-brand">
        <h4>Hip Hop Smoothies</h4>
        <p>Charlotte’s music-infused fresh smoothie and superfood acai bar founded by Shamika &amp; Carlos Brooks. Promoting vibrant wellness and culture across Camp North End and Uptown.</p>
      </div>
      <div class="hhs-footer-nav">
        <h5>Explore Demo</h5>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Tracklist Menu</a></li>
          <li><a href="culture-and-community.html">Culture &amp; Roots</a></li>
          <li><a href="signature-smoothies.html">Hit Smoothies</a></li>
          <li><a href="acai-bowls-and-boosts.html">Bowls &amp; Boosts</a></li>
          <li><a href="visit.html">Locations &amp; Hours</a></li>
        </ul>
      </div>
      <div class="hhs-footer-hours">
        <h5>Locations &amp; Contact</h5>
        <p style="color: #9d96aa; font-size: 0.88rem; margin-bottom: 0.4rem;"><strong>Camp North End:</strong> 1824 Statesville Ave (Boileryard)</p>
        <p style="color: #9d96aa; font-size: 0.88rem; margin-bottom: 0.4rem;"><strong>7th St Market:</strong> 224 E 7th St Uptown</p>
        <p style="color: #9d96aa; font-size: 0.88rem; margin-bottom: 0.4rem;"><strong>Direct Phone:</strong> (704) 900-8438</p>
        <p style="color: #9d96aa; font-size: 0.88rem;">Mon - Sat: 8:00 AM - 7:00 PM<br>Sunday: 10:00 AM - 5:00 PM</p>
      </div>
    </div>
    <div class="hhs-footer-bottom">
      <p>&copy; 2026 Hip Hop Smoothies. All rights reserved. Culinary &amp; lifestyle showcase demo for Charlotte, NC.</p>
    </div>
  </footer>
'''

pages = {
  'index.html': {
    'title': 'Hip Hop Smoothies - Music-Themed Smoothies & Acai Bowls in Charlotte NC',
    'nav': {'index': 'active', 'menu': '', 'culture': '', 'smoothies': '', 'bowls': '', 'visit': ''},
    'body': '''
    <main>
      <section class="hhs-hero">
        <div class="hhs-hero-grid">
          <div class="hhs-hero-content">
            <span class="hhs-hero-badge">Camp North End &bull; 7th St Market Uptown &bull; Charlotte</span>
            <h1 class="hhs-hero-title">Fuel Your Day with <span>Rhythm &amp; Fresh Fruit</span></h1>
            <p class="hhs-hero-lead">Founded by Shamika and Carlos Brooks, Hip Hop Smoothies blends 100% whole fruits, dairy-free milks, and superfoods named after the greatest hip-hop anthems of all time.</p>
            <div class="hhs-hero-actions">
              <a href="menu.html" class="hhs-btn-primary">View Tracklist Menu</a>
              <a href="signature-smoothies.html" class="hhs-btn-secondary">The Hit Smoothies</a>
            </div>
          </div>
          <div class="hhs-hero-img-wrap">
            <img src="images/hero.jpg" alt="Vibrant fresh fruit smoothies and acai bowls with berries and granola" width="600" height="420">
          </div>
        </div>
      </section>

      <section class="hhs-features">
        <div class="hhs-feature-grid">
          <div class="hhs-feature-card">
            <div class="hhs-feature-tag">100% Whole Fruit</div>
            <h2 class="hhs-feature-title">Pure Real Ingredients</h2>
            <p class="hhs-feature-desc">Never packed with artificial syrups or fillers. Blended fresh with real mangos, strawberries, and pineapples.</p>
          </div>
          <div class="hhs-feature-card">
            <div class="hhs-feature-tag">Iconic Tracklist</div>
            <h2 class="hhs-feature-title">Hip-Hop Themed Hits</h2>
            <p class="hhs-feature-desc">From Rapper’s Delight to C.R.E.A.M. and Gangsta Paradise, each blend is a tribute to hip-hop legends.</p>
          </div>
          <div class="hhs-feature-card">
            <div class="hhs-feature-tag">Organic Superfoods</div>
            <h2 class="hhs-feature-title">A&ccedil;a&iacute; &amp; Pitaya Bowls</h2>
            <p class="hhs-feature-desc">Thick superfood bases loaded with gluten-free granola, chia seeds, fresh sliced fruit, and local honey.</p>
          </div>
        </div>
      </section>

      <section class="hhs-section">
        <div class="hhs-story-grid">
          <div class="hhs-story-img-wrap">
            <img src="images/smoothies.jpg" alt="Lineup of colorful fruit smoothies in clear cups with straws" width="600" height="380">
          </div>
          <div class="hhs-story-content">
            <span class="hhs-section-eyebrow">Culture Meets Wellness</span>
            <h3>Healthy Living with Unmatched Energy</h3>
            <p>Shamika and Carlos Brooks founded Hip Hop Smoothies with a mission: make wholesome, nutrient-dense nutrition accessible, fun, and culturally celebrated.</p>
            <p>Whether you need an energy boost before a workout, a midday refresher at Camp North End, or an executive smoothie bar pop-up, our team delivers high-frequency good vibes.</p>
            <a href="culture-and-community.html" class="hhs-btn-primary" style="margin-top: 0.5rem;">Our Community Story</a>
          </div>
        </div>
      </section>

      <section class="hhs-section" style="background: #ffffff; border-top: 1px solid var(--hhs-border); border-bottom: 1px solid var(--hhs-border);">
        <div class="hhs-section-header">
          <span class="hhs-section-eyebrow">Corporate Wellness &amp; Mobile Events</span>
          <h2 class="hhs-section-title">Pop-Up Smoothie Bar &amp; Event Estimator</h2>
          <p class="hhs-section-subtitle">Planning a corporate wellness day, 5K race, school event, or private party? Estimate your smoothie and bowl counts below.</p>
        </div>

        <div class="hhs-calc-card">
          <div class="hhs-calc-controls">
            <div class="hhs-calc-field">
              <label for="hhs-guest-count">Attendees: <span id="hhs-guest-display" style="color: var(--hhs-primary); font-weight: 800;">25 People</span></label>
              <input type="range" id="hhs-guest-count" class="hhs-range-slider" min="10" max="150" step="5" value="25">
            </div>
            <div class="hhs-calc-field">
              <label for="hhs-platter-style">Event Package</label>
              <select id="hhs-platter-style" class="hhs-calc-select">
                <option value="smoothies">All-Star Smoothies (Full 16oz Blends)</option>
                <option value="bowls">Superfood Bowl Bar (Loaded Acai &amp; Pitaya)</option>
              </select>
            </div>
          </div>
          <div class="hhs-calc-results">
            <div class="hhs-result-box">
              <span class="num" id="hhs-smoothie-total">25 16oz Smoothies</span>
              <span class="label">Fresh Blended Cups</span>
            </div>
            <div class="hhs-result-box">
              <span class="num" id="hhs-bowl-total">10 Acai / Pitaya Bowls</span>
              <span class="label">Superfood Bowls</span>
            </div>
            <div class="hhs-result-box">
              <span class="num" id="hhs-boost-total">25 Superfood Boosts</span>
              <span class="label">Chia / Maca / Sea Moss</span>
            </div>
          </div>
        </div>
      </section>
    </main>
'''
  },
  'menu.html': {
    'title': 'Tracklist Menu - Hip Hop Smoothies Charlotte NC',
    'nav': {'index': '', 'menu': 'active', 'culture': '', 'smoothies': '', 'bowls': '', 'visit': ''},
    'body': '''
    <main class="hhs-section">
      <div class="hhs-section-header">
        <span class="hhs-section-eyebrow">The Tracklist</span>
        <h1 class="hhs-section-title">Hip Hop Smoothies Menu</h1>
        <p class="hhs-section-subtitle">Explore our hit smoothie tracks, superfood açaí bowls, energy boosters, and wellness elixirs.</p>
      </div>

      <div class="hhs-filter-tabs" role="tablist" aria-label="Menu Filter Tabs">
        <button type="button" class="hhs-filter-btn active" data-filter="all">All Tracks</button>
        <button type="button" class="hhs-filter-btn" data-filter="smoothies">Hit Smoothies</button>
        <button type="button" class="hhs-filter-btn" data-filter="bowls">Superfood Bowls</button>
        <button type="button" class="hhs-filter-btn" data-filter="protein">Protein &amp; Energy</button>
        <button type="button" class="hhs-filter-btn" data-filter="boosts">Boosts &amp; Brews</button>
      </div>

      <div class="hhs-menu-grid">
        <div class="hhs-menu-item" data-category="smoothies">
          <div class="hhs-menu-item-header">
            <span class="hhs-menu-item-name">Rapper’s Delight</span>
            <span class="hhs-menu-item-price">$8.95 / $10.95</span>
          </div>
          <p class="hhs-menu-item-desc">Tropical fruit punch base blended with sweet ripe mangos, golden pineapples, and fresh strawberries.</p>
          <div class="hhs-menu-item-badges">
            <span class="hhs-badge hhs-badge-orange">Classic Hit</span>
            <span class="hhs-badge">100% Vegan</span>
          </div>
        </div>

        <div class="hhs-menu-item" data-category="smoothies">
          <div class="hhs-menu-item-header">
            <span class="hhs-menu-item-name">Gangsta Paradise</span>
            <span class="hhs-menu-item-price">$8.95 / $10.95</span>
          </div>
          <p class="hhs-menu-item-desc">Creamy almond milk, ripe bananas, sweet strawberries, and a touch of raw local honey for smooth sweetness.</p>
          <div class="hhs-menu-item-badges">
            <span class="hhs-badge hhs-badge-purple">Top Seller</span>
          </div>
        </div>

        <div class="hhs-menu-item" data-category="smoothies">
          <div class="hhs-menu-item-header">
            <span class="hhs-menu-item-name">C.R.E.A.M.</span>
            <span class="hhs-menu-item-price">$9.25 / $11.25</span>
          </div>
          <p class="hhs-menu-item-desc">Coconut milk, juicy sweet pineapples, bananas, and pure Madagascar vanilla extract. Cash Rules Everything Around Me!</p>
          <div class="hhs-menu-item-badges">
            <span class="hhs-badge hhs-badge-cyan">Tropical Dream</span>
          </div>
        </div>

        <div class="hhs-menu-item" data-category="protein">
          <div class="hhs-menu-item-header">
            <span class="hhs-menu-item-name">Nuttin But Love</span>
            <span class="hhs-menu-item-price">$9.75 / $11.75</span>
          </div>
          <p class="hhs-menu-item-desc">Almond milk, ripe bananas, creamy all-natural peanut butter, dark Dutch cocoa, vanilla plant protein, and honey.</p>
          <div class="hhs-menu-item-badges">
            <span class="hhs-badge hhs-badge-purple">25g Protein</span>
          </div>
        </div>

        <div class="hhs-menu-item" data-category="protein">
          <div class="hhs-menu-item-header">
            <span class="hhs-menu-item-name">Fight The Power</span>
            <span class="hhs-menu-item-price">$9.50 / $11.50</span>
          </div>
          <p class="hhs-menu-item-desc">Coconut milk, antioxidant-loaded wild blackberries, ripe bananas, chia seeds, and plant-based vanilla protein.</p>
          <div class="hhs-menu-item-badges">
            <span class="hhs-badge hhs-badge-purple">Antioxidant Power</span>
          </div>
        </div>

        <div class="hhs-menu-item" data-category="bowls">
          <div class="hhs-menu-item-header">
            <span class="hhs-menu-item-name">The Hip Hop A&ccedil;a&iacute; Bowl</span>
            <span class="hhs-menu-item-price">$12.50</span>
          </div>
          <p class="hhs-menu-item-desc">Thick organic a&ccedil;a&iacute; base topped with gluten-free granola, sliced strawberries, bananas, blueberries, hemp seeds, and honey drizzle.</p>
          <div class="hhs-menu-item-badges">
            <span class="hhs-badge hhs-badge-purple">Superfood Fuel</span>
          </div>
        </div>

        <div class="hhs-menu-item" data-category="bowls">
          <div class="hhs-menu-item-header">
            <span class="hhs-menu-item-name">Dragon Queen Pitaya Bowl</span>
            <span class="hhs-menu-item-price">$12.95</span>
          </div>
          <p class="hhs-menu-item-desc">Vibrant magenta dragonfruit puree layered with coconut chips, sliced kiwi, strawberries, chia seeds, and agave.</p>
          <div class="hhs-menu-item-badges">
            <span class="hhs-badge hhs-badge-cyan">Vibrant Pink</span>
          </div>
        </div>

        <div class="hhs-menu-item" data-category="boosts">
          <div class="hhs-menu-item-header">
            <span class="hhs-menu-item-name">Cold Brew Rhythm</span>
            <span class="hhs-menu-item-price">$5.50</span>
          </div>
          <p class="hhs-menu-item-desc">Locally roasted cold brew coffee blended with oat milk and Madagascar vanilla or mocha swirl.</p>
          <div class="hhs-menu-item-badges">
            <span class="hhs-badge">Caffeine Boost</span>
          </div>
        </div>
      </div>
    </main>
'''
  },
  'culture-and-community.html': {
    'title': 'Culture & Roots - Hip Hop Smoothies',
    'nav': {'index': '', 'menu': '', 'culture': 'active', 'smoothies': '', 'bowls': '', 'visit': ''},
    'body': '''
    <main class="hhs-section">
      <div class="hhs-section-header">
        <span class="hhs-section-eyebrow">Our Story &amp; Founders</span>
        <h1 class="hhs-section-title">The Hip Hop Smoothies Journey</h1>
        <p class="hhs-section-subtitle">How Shamika and Carlos Brooks fused hip-hop heritage and health to create a Charlotte phenomenon.</p>
      </div>

      <div class="hhs-story-grid">
        <div class="hhs-story-content">
          <h3>From Mobile Trailer to Cultural Hub</h3>
          <p>In 2018, Shamika and Roberto (Carlos) Brooks launched Hip Hop Smoothies out of a custom mobile trailer. Growing up on the beats and storytelling of 80s and 90s hip-hop, the Brooks family wanted to bridge the gap between urban culture and clean, health-conscious living.</p>
          <p>They proved that healthy food does not need to feel sterile or clinical &mdash; it can be vibrant, flavorful, music-filled, and deeply rooted in community empowerment.</p>
        </div>
        <div class="hhs-story-img-wrap">
          <img src="images/culture.jpg" alt="Vibrant hip hop smoothie bar counter and blending station" width="600" height="380">
        </div>
      </div>

      <div class="hhs-story-grid" style="margin-top: 4.5rem;">
        <div class="hhs-story-img-wrap">
          <img src="images/ingredients.jpg" alt="Fresh whole pineapples, bananas, strawberries, and superfoods" width="600" height="380">
        </div>
        <div class="hhs-story-content">
          <h3>Community First at Camp North End &amp; Beyond</h3>
          <p>Today, with thriving brick-and-mortar storefronts at Camp North End and The Market at 7th Street Uptown, Hip Hop Smoothies has become an essential community gathering spot.</p>
          <p>From sponsoring community fitness bootcamps to hosting youth wellness days and DJ sets, Shamika and Carlos continue to bring people together through the universal languages of music and good nutrition.</p>
        </div>
      </div>
    </main>
'''
  },
  'signature-smoothies.html': {
    'title': 'Hit Smoothies - Hip Hop Smoothies',
    'nav': {'index': '', 'menu': '', 'culture': '', 'smoothies': 'active', 'bowls': '', 'visit': ''},
    'body': '''
    <main class="hhs-section">
      <div class="hhs-section-header">
        <span class="hhs-section-eyebrow">The Classic Tracks</span>
        <h1 class="hhs-section-title">Signature Hip-Hop Smoothies</h1>
        <p class="hhs-section-subtitle">Discover our most famous blends inspired by classic hip-hop culture.</p>
      </div>

      <div class="hhs-story-grid">
        <div class="hhs-story-img-wrap">
          <img src="images/smoothies.jpg" alt="Freshly blended colorful fruit smoothies in glasses" width="600" height="380">
        </div>
        <div class="hhs-story-content">
          <h3>The Greatest Hits</h3>
          <p><strong>Rapper’s Delight:</strong> The iconic track that started it all. Sweet tropical mangoes, juicy pineapples, and strawberries blended with fruit punch for a bright, sunshine-filled refresher.</p>
          <p><strong>Gangsta Paradise:</strong> A silky, comforting harmony of almond milk, sweet ripe bananas, strawberries, and a touch of raw clover honey.</p>
          <p><strong>C.R.E.A.M.:</strong> Pure coconut milk, sweet pineapple chunks, bananas, and real Madagascar vanilla bean extract.</p>
        </div>
      </div>

      <div class="hhs-story-grid" style="margin-top: 4.5rem;">
        <div class="hhs-story-content">
          <h3>Performance &amp; Protein Blends</h3>
          <p><strong>Nuttin But Love:</strong> Packed with all-natural creamy peanut butter, dark Dutch cocoa, bananas, almond milk, and 25 grams of clean plant protein.</p>
          <p><strong>Fight The Power:</strong> Deep purple wild blackberries, bananas, and coconut milk blended with organic chia seeds and protein for peak vitality.</p>
        </div>
        <div class="hhs-story-img-wrap">
          <img src="images/hero.jpg" alt="Smoothie spread with fruit garnishes" width="600" height="380">
        </div>
      </div>
    </main>
'''
  },
  'acai-bowls-and-boosts.html': {
    'title': 'Bowls & Boosts - Hip Hop Smoothies',
    'nav': {'index': '', 'menu': '', 'culture': '', 'smoothies': '', 'bowls': 'active', 'visit': ''},
    'body': '''
    <main class="hhs-section">
      <div class="hhs-section-header">
        <span class="hhs-section-eyebrow">Superfood Nutrition</span>
        <h1 class="hhs-section-title">A&ccedil;a&iacute; Bowls &amp; Wellness Boosts</h1>
        <p class="hhs-section-subtitle">Thick organic smoothie bowls and functional superfood add-ins.</p>
      </div>

      <div class="hhs-story-grid">
        <div class="hhs-story-content">
          <h3>Loaded Superfood Bowls</h3>
          <p>Our smoothie bowls are blended extra thick and served in generous portions loaded with texture and antioxidants:</p>
          <p><strong>The Hip Hop A&ccedil;a&iacute; Bowl:</strong> Grade-A wild Brazilian a&ccedil;a&iacute; topped with organic crunchy granola, fresh sliced bananas, strawberries, blueberries, chia seeds, and raw local honey.</p>
          <p><strong>Dragon Queen Pitaya:</strong> Vibrant magenta dragonfruit puree loaded with toasted coconut flakes, sliced kiwi, strawberries, and organic agave nectar.</p>
        </div>
        <div class="hhs-story-img-wrap">
          <img src="images/acai-bowls.jpg" alt="Superfood acai bowl loaded with kiwi, berries, and chia seeds" width="600" height="380">
        </div>
      </div>

      <div class="hhs-story-grid" style="margin-top: 4.5rem;">
        <div class="hhs-story-img-wrap">
          <img src="images/ingredients.jpg" alt="Superfood ingredients including chia seeds, hemp hearts, and berries" width="600" height="380">
        </div>
        <div class="hhs-story-content">
          <h3>Superfood Boost Add-Ins</h3>
          <p>Customize any smoothie or bowl with our functional wellness boosters:</p>
          <p><strong>Wildcrafted Sea Moss:</strong> Packed with 92 essential minerals to support gut health and immunity.</p>
          <p><strong>Organic Maca Root:</strong> Ancient Peruvian adaptogen for sustained stamina and balanced energy.</p>
          <p><strong>Hemp Hearts &amp; Chia Seeds:</strong> Rich in plant-based Omega-3 fatty acids and clean fiber.</p>
        </div>
      </div>
    </main>
'''
  },
  'visit.html': {
    'title': 'Visit & Order - Hip Hop Smoothies Charlotte NC',
    'nav': {'index': '', 'menu': '', 'culture': '', 'smoothies': '', 'bowls': '', 'visit': 'active'},
    'body': '''
    <main class="hhs-section">
      <div class="hhs-section-header">
        <span class="hhs-section-eyebrow">Locations &amp; Mobile Events</span>
        <h1 class="hhs-section-title">Visit Hip Hop Smoothies</h1>
        <p class="hhs-section-subtitle">Stop by our flagship at Camp North End, 7th Street Market Uptown, or book our mobile trailer for your event.</p>
      </div>

      <div class="hhs-contact-grid">
        <div class="hhs-contact-card">
          <h3>Camp North End Flagship</h3>
          <p style="color: var(--hhs-text-muted); margin-bottom: 0.8rem;">Located in the vibrant Boileryard district of Camp North End with indoor seating and outdoor courtyard.</p>
          <p><strong>Address:</strong> 1824 Statesville Ave, Charlotte, NC 28206</p>
          <p style="margin-top: 0.4rem;"><strong>Hours:</strong> Mon - Sat: 8:00 AM - 7:00 PM | Sun: 10:00 AM - 5:00 PM</p>
          <div style="margin-top: 1.5rem;">
            <a href="tel:7049008438" class="hhs-btn-primary" style="width: 100%; text-align: center;">Call Flagship: (704) 900-8438</a>
          </div>
        </div>

        <div class="hhs-contact-card">
          <h3>The Market at 7th Street (Uptown)</h3>
          <p style="color: var(--hhs-text-muted); margin-bottom: 0.8rem;">Inside Uptown Charlotte’s premier urban market hall adjacent to the 7th St light rail station.</p>
          <p><strong>Address:</strong> 224 E 7th St, Charlotte, NC 28202</p>
          <p style="margin-top: 0.4rem;"><strong>Hours:</strong> Mon - Sun: 8:30 AM - 6:00 PM</p>
          <div style="margin-top: 1.5rem; background: var(--hhs-surface-alt); padding: 1rem; border-radius: var(--hhs-radius-sm);">
            <p style="font-size: 0.85rem; color: var(--hhs-primary); font-weight: 700;">Express counter service. Light rail validated parking available for market guests.</p>
          </div>
        </div>

        <div class="hhs-contact-card">
          <h3>Mobile Truck &amp; Corporate Pop-Ups</h3>
          <p style="color: var(--hhs-text-muted); margin-bottom: 0.8rem;">Book the Hip Hop Smoothies mobile truck or indoor smoothie bar for corporate campus events, festivals, and athletics.</p>
          <p><strong>Booking:</strong> Inquire online with headcount and date details.</p>
          <div style="margin-top: 1.5rem;">
            <a href="mailto:events@hiphopsmoothies.com" class="hhs-btn-secondary" style="width: 100%; text-align: center;">Inquire for Event Booking</a>
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
    nav_culture=data['nav']['culture'],
    nav_smoothies=data['nav']['smoothies'],
    nav_bowls=data['nav']['bowls'],
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
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Syne:wght@600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="site.css">
</head>
<body>
  <header class="hhs-header">
    <div class="hhs-nav-container">
      <a href="index.html" class="hhs-brand">
        <span class="hhs-brand-title">Hip Hop Smoothies</span>
        <span class="hhs-brand-subtitle">Camp North End &bull; Uptown Charlotte</span>
      </a>
      <button class="hhs-nav-toggle" type="button" aria-label="Toggle navigation menu" aria-expanded="false">Menu</button>
{cur_nav}
    </div>
  </header>

{data['body']}

{footer_content}
  <script src="site.js"></script>
</body>
</html>'''

  filepath = os.path.join('hip-hop-smoothies', filename)
  with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html_doc.strip() + '\n')
  print(f'Wrote {filename}')

print('All 6 HTML pages for Hip Hop Smoothies written successfully')
