import os
from nirvana_core import wrap_page

index_content = """
    <section class="nirvana-hero">
      <div class="nirvana-hero-content">
        <span class="nirvana-badge nirvana-badge-teal">401 S Tryon St &bull; Uptown Charlotte</span>
        <h1 class="nirvana-hero-title">Experience True <span>Indian Culinary Mastery</span></h1>
        <p class="nirvana-hero-lead">Fast-casual weekday perfection. Fragrant slow-cooked dum biryanis, velvety butter chicken, freshly baked garlic naan, and custom executive thali combos.</p>
        <div class="nirvana-hero-actions">
          <a href="menu.html" class="nirvana-btn nirvana-btn-primary">Explore Full Menu</a>
          <a href="signature-biryanis-and-thali-combos.html" class="nirvana-btn nirvana-btn-secondary">Build Custom Thali</a>
          <a href="corporate-catering-and-lunch-boxes.html" class="nirvana-btn nirvana-btn-crimson">Corporate Catering</a>
        </div>
        <div class="nirvana-hero-highlights">
          <div class="nirvana-highlight-box">
            <div class="nirvana-highlight-title">Aged Dum Biryani</div>
            <div class="nirvana-highlight-desc">Long-grain basmati layered with saffron, fried onions, and whole spices.</div>
          </div>
          <div class="nirvana-highlight-box">
            <div class="nirvana-highlight-title">Executive Thalis</div>
            <div class="nirvana-highlight-desc">Complete balanced lunch box with curry, cumin rice, naan, and raita.</div>
          </div>
          <div class="nirvana-highlight-box">
            <div class="nirvana-highlight-title">Tandoor Breads</div>
            <div class="nirvana-highlight-desc">Hand-stretched garlic naan, butter roti, and crispy spiced samosas.</div>
          </div>
          <div class="nirvana-highlight-box">
            <div class="nirvana-highlight-title">Express Pickup</div>
            <div class="nirvana-highlight-desc">Call ahead at (980) 290-7002 for swift weekday counter pickup.</div>
          </div>
        </div>
      </div>
    </section>

    <div class="nirvana-container">
      <div class="nirvana-thali-banner">
        <div>
          <div class="nirvana-thali-title">Weekday Executive Lunch Combos</div>
          <p style="color: #78350f; font-size: 0.95rem;">Served Monday through Friday from 11:30 AM to 3:30 PM. Complete multicourse Indian thali boxes tailored for busy Uptown schedules.</p>
        </div>
        <a href="signature-biryanis-and-thali-combos.html" class="nirvana-btn nirvana-btn-crimson">Build Lunch Box &rarr;</a>
      </div>

      <section class="nirvana-section">
        <div class="nirvana-section-header">
          <span class="nirvana-badge">Culinary Signatures</span>
          <h2 class="nirvana-title">Rich Aromatics &amp; Authentic Flavors</h2>
          <p class="nirvana-subtitle">Prepared with whole toasted spices, simmered sauces, and premium halal meats in Uptown Charlotte.</p>
        </div>

        <div class="nirvana-grid-3">
          <div class="nirvana-card">
            <div class="nirvana-card-img-wrap">
              <img src="images/chicken-tikka-masala-curry.jpg" alt="Chicken Tikka Masala Curry" class="nirvana-card-img">
              <span class="nirvana-card-tag">House Favorite</span>
            </div>
            <div class="nirvana-card-body">
              <div class="nirvana-card-header">
                <h3 class="nirvana-card-title">Chicken Tikka Masala</h3>
                <span class="nirvana-card-price">$14.50</span>
              </div>
              <p class="nirvana-card-desc">Tandoor-charred chicken breast cubes enveloped in a velvety spiced tomato, cream, fenugreek, and ginger reduction.</p>
              <div class="nirvana-card-meta">
                <span class="nirvana-meta-pill">Includes Basmati Rice</span>
                <span class="nirvana-meta-pill">Mild / Med / Hot</span>
              </div>
              <a href="tandoori-curries-and-vegetarian-classics.html" class="nirvana-btn nirvana-btn-primary" style="text-align: center; width: 100%;">View Curries</a>
            </div>
          </div>

          <div class="nirvana-card">
            <div class="nirvana-card-img-wrap">
              <img src="images/fragrant-dum-biryani.jpg" alt="Hyderabadi Dum Biryani" class="nirvana-card-img">
              <span class="nirvana-card-tag">Slow Dum Cooked</span>
            </div>
            <div class="nirvana-card-body">
              <div class="nirvana-card-header">
                <h3 class="nirvana-card-title">Hyderabadi Dum Biryani</h3>
                <span class="nirvana-card-price">$13.95+</span>
              </div>
              <p class="nirvana-card-desc">Royal saffron basmati rice steam-cooked in a sealed vessel with spiced bone-in chicken, tender lamb, or garden vegetables and cooling cucumber raita.</p>
              <div class="nirvana-card-meta">
                <span class="nirvana-meta-pill">Chicken / Lamb / Veg</span>
                <span class="nirvana-meta-pill">Served with Salan &amp; Raita</span>
              </div>
              <a href="signature-biryanis-and-thali-combos.html" class="nirvana-btn nirvana-btn-primary" style="text-align: center; width: 100%;">Explore Biryanis</a>
            </div>
          </div>

          <div class="nirvana-card">
            <div class="nirvana-card-img-wrap">
              <img src="images/thali-lunch-combo-platter.jpg" alt="Thali Lunch Combo Platter" class="nirvana-card-img">
              <span class="nirvana-card-tag">All-In-One Box</span>
            </div>
            <div class="nirvana-card-body">
              <div class="nirvana-card-header">
                <h3 class="nirvana-card-title">Executive Thali Combo</h3>
                <span class="nirvana-card-price">$15.00</span>
              </div>
              <p class="nirvana-card-desc">The ultimate corporate lunch. Choice of entree, aromatic cumin basmati rice, warm butter garlic naan, Punjabi samosa, and yogurt raita.</p>
              <div class="nirvana-card-meta">
                <span class="nirvana-meta-pill">Vegetarian or Meat</span>
                <span class="nirvana-meta-pill">Complete Meal</span>
              </div>
              <a href="signature-biryanis-and-thali-combos.html" class="nirvana-btn nirvana-btn-secondary" style="text-align: center; width: 100%;">Customize Thali</a>
            </div>
          </div>
        </div>
      </section>
    </div>
"""

menu_content = """
    <div class="nirvana-container">
      <div class="nirvana-section-header">
        <span class="nirvana-badge">Uptown Charlotte</span>
        <h1 class="nirvana-title">Nirvana II Complete Menu</h1>
        <p class="nirvana-subtitle">Authentic recipes prepared fresh daily for fast-casual dining, executive lunch pickups, and office catering.</p>
      </div>

      <div class="nirvana-grid-2">
        <!-- Curries -->
        <div class="nirvana-card" style="padding: 28px;">
          <h3 class="nirvana-card-title" style="margin-bottom: 20px; border-bottom: 2px solid var(--nirvana-border); padding-bottom: 10px;">Classic &amp; Signature Curries</h3>
          
          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--nirvana-charcoal);">Chicken Tikka Masala</span>
              <span style="color: var(--nirvana-crimson);">$14.50</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--nirvana-muted);">Tender clay-oven chicken in a rich tomato cream sauce infused with dried fenugreek leaves and garam masala.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--nirvana-charcoal);">Butter Chicken (Murgh Makhani)</span>
              <span style="color: var(--nirvana-crimson);">$14.50</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--nirvana-muted);">Shredded tandoori chicken simmered in a velvety buttery cashew and plum tomato gravy with honey kiss.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--nirvana-charcoal);">Lamb Rogan Josh</span>
              <span style="color: var(--nirvana-crimson);">$16.95</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--nirvana-muted);">Braised tender boneless lamb in a Kashmiri red chili, caramelized onion, and black cardamom sauce.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--nirvana-charcoal);">Chicken Vindaloo</span>
              <span style="color: var(--nirvana-crimson);">$14.50</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--nirvana-muted);">Fiery Goan curry cooked with roasted red chilies, cider vinegar, garlic, and tender potatoes.</p>
          </div>
        </div>

        <!-- Vegetarian Classics -->
        <div class="nirvana-card" style="padding: 28px;">
          <h3 class="nirvana-card-title" style="margin-bottom: 20px; border-bottom: 2px solid var(--nirvana-border); padding-bottom: 10px;">Vegetarian Specialties</h3>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--nirvana-charcoal);">Saag Paneer</span>
              <span style="color: var(--nirvana-crimson);">$13.50</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--nirvana-muted);">Fresh Indian cottage cheese cubes simmered with pureed baby spinach, garlic, ginger, and cream.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--nirvana-charcoal);">Paneer Tikka Masala</span>
              <span style="color: var(--nirvana-crimson);">$13.95</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--nirvana-muted);">Grilled paneer cubes in our signature velvety spiced tomato cream masala.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--nirvana-charcoal);">Chana Masala (Vegan)</span>
              <span style="color: var(--nirvana-crimson);">$12.50</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--nirvana-muted);">Chickpeas simmered with crushed tomatoes, ginger, pomegranate seed powder, and roasted cumin.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--nirvana-charcoal);">Dal Makhani</span>
              <span style="color: var(--nirvana-crimson);">$12.50</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--nirvana-muted);">Slow-simmered black lentils and kidney beans cooked overnight with butter and aromatic spices.</p>
          </div>
        </div>
      </div>

      <!-- Biryanis & Tandoor Breads -->
      <div class="nirvana-grid-2" style="margin-top: 30px;">
        <div class="nirvana-card" style="padding: 28px;">
          <h3 class="nirvana-card-title" style="margin-bottom: 16px;">Dum Biryanis</h3>
          <div style="margin-bottom: 14px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Chicken Dum Biryani</span>
              <span style="color: var(--nirvana-crimson);">$15.50</span>
            </div>
            <small style="color: var(--nirvana-muted);">Marinated chicken layered with aged saffron basmati rice, mint, and fried onions.</small>
          </div>
          <div style="margin-bottom: 14px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Vegetable Dum Biryani</span>
              <span style="color: var(--nirvana-crimson);">$13.95</span>
            </div>
            <small style="color: var(--nirvana-muted);">Fresh cauliflower, carrots, peas, and potatoes simmered in saffron rice.</small>
          </div>
          <div>
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Lamb &amp; Goat Dum Biryani</span>
              <span style="color: var(--nirvana-crimson);">$17.50</span>
            </div>
            <small style="color: var(--nirvana-muted);">Succulent bone-in goat or lamb layered with rich spices and golden basmati.</small>
          </div>
        </div>

        <div class="nirvana-card" style="padding: 28px;">
          <h3 class="nirvana-card-title" style="margin-bottom: 16px;">Appetizers, Breads &amp; Drinks</h3>
          <div style="margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Punjabi Samosas (2 pcs)</span>
              <span style="color: var(--nirvana-crimson);">$4.95</span>
            </div>
            <small style="color: var(--nirvana-muted);">Crisp pastry stuffed with spiced potatoes and green peas with mint and tamarind chutneys.</small>
          </div>
          <div style="margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Fresh Garlic Naan</span>
              <span style="color: var(--nirvana-crimson);">$3.50</span>
            </div>
            <small style="color: var(--nirvana-muted);">Tandoor-baked flatbread brushed with garlic butter and fresh cilantro.</small>
          </div>
          <div style="margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Chilled Mango Lassi</span>
              <span style="color: var(--nirvana-crimson);">$3.95</span>
            </div>
            <small style="color: var(--nirvana-muted);">Creamy whipped yogurt smoothie with Alphonso mango pulp and cardamom.</small>
          </div>
        </div>
      </div>
    </div>
"""

biryanis_content = """
    <div class="nirvana-container">
      <div class="nirvana-section-header">
        <span class="nirvana-badge">Custom Combo Studio</span>
        <h1 class="nirvana-title">Dum Biryanis &amp; Executive Thali Combos</h1>
        <p class="nirvana-subtitle">Construct your personalized Indian lunch box. Select your entree, grain, tandoor bread, and side treats with live calorie and pricing calculation.</p>
      </div>

      <div class="nirvana-builder-card nirvana-thali-builder">
        <div class="nirvana-builder-step">
          <div class="nirvana-step-label">
            <span class="nirvana-step-number">1</span>
            <span>Choose Your Main Curry / Entree</span>
          </div>
          <div class="nirvana-options-grid">
            <button class="nirvana-opt-btn nirvana-opt-curry active" data-name="Chicken Tikka Masala" data-price="14.50" data-cal="520">Chicken Tikka Masala - $14.50</button>
            <button class="nirvana-opt-btn nirvana-opt-curry" data-name="Butter Chicken (Makhani)" data-price="14.50" data-cal="560">Butter Chicken - $14.50</button>
            <button class="nirvana-opt-btn nirvana-opt-curry" data-name="Lamb Rogan Josh" data-price="16.95" data-cal="610">Lamb Rogan Josh - $16.95</button>
            <button class="nirvana-opt-btn nirvana-opt-curry" data-name="Saag Paneer" data-price="13.50" data-cal="440">Saag Paneer - $13.50</button>
            <button class="nirvana-opt-btn nirvana-opt-curry" data-name="Chana Masala (Vegan)" data-price="12.50" data-cal="380">Chana Masala - $12.50</button>
          </div>
        </div>

        <div class="nirvana-builder-step">
          <div class="nirvana-step-label">
            <span class="nirvana-step-number">2</span>
            <span>Select Aromatic Rice Base</span>
          </div>
          <div class="nirvana-options-grid">
            <button class="nirvana-opt-btn nirvana-opt-rice active" data-name="Aromatic Basmati Cumin Rice" data-cal="210">Basmati Cumin Rice</button>
            <button class="nirvana-opt-btn nirvana-opt-rice" data-name="Saffron Biryani Rice" data-cal="240">Saffron Biryani Rice</button>
            <button class="nirvana-opt-btn nirvana-opt-rice" data-name="Brown Basmati Rice" data-cal="190">Brown Basmati</button>
            <button class="nirvana-opt-btn nirvana-opt-rice" data-name="No Rice (Extra Naan)" data-cal="0">No Rice</button>
          </div>
        </div>

        <div class="nirvana-builder-step">
          <div class="nirvana-step-label">
            <span class="nirvana-step-number">3</span>
            <span>Choose Hand-Stretched Bread</span>
          </div>
          <div class="nirvana-options-grid">
            <button class="nirvana-opt-btn nirvana-opt-bread active" data-name="Butter Garlic Naan" data-cal="260">Garlic Naan</button>
            <button class="nirvana-opt-btn nirvana-opt-bread" data-name="Plain Butter Naan" data-cal="230">Plain Butter Naan</button>
            <button class="nirvana-opt-btn nirvana-opt-bread" data-name="Tandoori Whole Wheat Roti" data-cal="160">Whole Wheat Roti</button>
            <button class="nirvana-opt-btn nirvana-opt-bread" data-name="Layered Paratha" data-cal="280">Layered Paratha</button>
          </div>
        </div>

        <div class="nirvana-builder-step">
          <div class="nirvana-step-label">
            <span class="nirvana-step-number">4</span>
            <span>Select Side Appetizer</span>
          </div>
          <div class="nirvana-options-grid">
            <button class="nirvana-opt-btn nirvana-opt-side active" data-name="Punjabi Samosa (1 pc)" data-cal="180">Punjabi Samosa</button>
            <button class="nirvana-opt-btn nirvana-opt-side" data-name="Crispy Onion Pakoras" data-cal="160">Onion Pakoras</button>
            <button class="nirvana-opt-btn nirvana-opt-side" data-name="Cucumber Raita Salad" data-cal="80">Cucumber Raita</button>
            <button class="nirvana-opt-btn nirvana-opt-side" data-name="Spiced Pappadums (2 pcs)" data-cal="90">Spiced Pappadums</button>
          </div>
        </div>

        <div class="nirvana-builder-step">
          <div class="nirvana-step-label">
            <span class="nirvana-step-number">5</span>
            <span>Beverage &amp; Dessert Add-Ons</span>
          </div>
          <div class="nirvana-options-grid">
            <button id="nirvana-toggle-lassi" class="nirvana-opt-btn">Chilled Mango Lassi (+$3.95)</button>
            <button id="nirvana-toggle-gulab" class="nirvana-opt-btn">Gulab Jamun Dessert (+$2.50)</button>
          </div>
        </div>

        <div class="nirvana-summary-panel">
          <div class="nirvana-summary-metrics">
            <div class="nirvana-metric-item">
              <span class="nirvana-metric-label">Estimated Price</span>
              <span id="nirvana-thali-price" class="nirvana-metric-val">$14.50</span>
            </div>
            <div class="nirvana-metric-item">
              <span class="nirvana-metric-label">Approximate Nutrition</span>
              <span id="nirvana-thali-calories" class="nirvana-metric-val" style="color: #67e8f9;">1170 kcal</span>
            </div>
          </div>
          <div style="flex-basis: 100%; border-top: 1px solid #3f3f46; padding-top: 16px; margin-top: 10px;">
            <strong style="color: #a1a1aa; display: block; font-size: 0.85rem; text-transform: uppercase;">Your Customized Thali Plate:</strong>
            <p id="nirvana-thali-summary" style="color: #ffffff; font-size: 1rem; margin-top: 4px;">Chicken Tikka Masala served with Basmati Cumin Rice, Butter Garlic Naan, and Punjabi Samosa. Includes cooling cucumber raita.</p>
          </div>
        </div>
      </div>
    </div>
"""

pages = {
    "index.html": ("Home", index_content),
    "menu.html": ("Full Menu", menu_content),
    "signature-biryanis-and-thali-combos.html": ("Biryanis & Thalis", biryanis_content)
}

for filename, (label, content) in pages.items():
    html = wrap_page(label, filename, content)
    with open(os.path.join("nirvana-ii", filename), "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"Generated {filename}")
