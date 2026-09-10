import os
from hasaki_core import wrap_page

index_content = """
    <section class="hasaki-hero">
      <div class="hasaki-hero-content">
        <span class="hasaki-badge hasaki-badge-wasabi">440 S Church St &bull; Ally Center 1st Floor</span>
        <h1 class="hasaki-hero-title">Sizzling Teppan Hibachi &amp; <span>Craft Sushi</span></h1>
        <p class="hasaki-hero-lead">Fast-casual Japanese excellence in Uptown Charlotte. Flame-seared hibachi steak &amp; chicken, multi-compartment executive bento boxes, and fresh specialty sushi rolls.</p>
        <div class="hasaki-hero-actions">
          <a href="menu.html" class="hasaki-btn hasaki-btn-primary">View Full Menu</a>
          <a href="teppan-hibachi-and-bento-boxes.html" class="hasaki-btn hasaki-btn-secondary">Build Bento Box</a>
          <a href="corporate-catering-and-sushi-platters.html" class="hasaki-btn hasaki-btn-wasabi">Sushi Platters &amp; Catering</a>
        </div>
        <div class="hasaki-hero-highlights">
          <div class="hasaki-highlight-box">
            <div class="hasaki-highlight-title">Teppan Hibachi</div>
            <div class="hasaki-highlight-desc">High-flame seared NY strip, chicken, shrimp, and sweet caramelized onions.</div>
          </div>
          <div class="hasaki-highlight-box">
            <div class="hasaki-highlight-title">Executive Bentos</div>
            <div class="hasaki-highlight-desc">Complete lunch with entree, fried rice, pork gyoza, California roll, and salad.</div>
          </div>
          <div class="hasaki-highlight-box">
            <div class="hasaki-highlight-title">Specialty Sushi</div>
            <div class="hasaki-highlight-desc">Volcano Roll, Queen City Roll, Spicy Tuna Crunch, and fresh nigiri platters.</div>
          </div>
          <div class="hasaki-highlight-box">
            <div class="hasaki-highlight-title">Ally Center Pickup</div>
            <div class="hasaki-highlight-desc">Call ahead at (980) 819-9580 for rapid weekday lunch pickup.</div>
          </div>
        </div>
      </div>
    </section>

    <div class="hasaki-container">
      <div class="hasaki-info-box" style="margin-top: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
          <div>
            <span class="hasaki-badge hasaki-badge-wasabi" style="margin-bottom: 6px;">Ally Center Dining Hub</span>
            <h2 style="font-family: var(--hasaki-font-display); color: var(--hasaki-charcoal); font-size: 1.6rem; font-weight: 800;">Fast, Fresh, High-Heat Japanese Flavors</h2>
            <p style="color: var(--hasaki-text-muted); font-size: 0.95rem;">Located on the ground floor of the Ally Center across from Romare Bearden Park, Hasaki delivers speed without cutting corners on authentic Japanese ingredients.</p>
          </div>
          <a href="visit.html" class="hasaki-btn hasaki-btn-primary">Find 440 S Church &rarr;</a>
        </div>
      </div>

      <section class="hasaki-section">
        <div class="hasaki-section-header">
          <span class="hasaki-badge">Japanese Classics</span>
          <h2 class="hasaki-title">Signature Hibachi &amp; Fresh Rolls</h2>
          <p class="hasaki-subtitle">Prepared to order with grade-A meats, fresh sushi-grade seafood, and house-blended sauces.</p>
        </div>

        <div class="hasaki-grid-3">
          <div class="hasaki-card">
            <div class="hasaki-card-img-wrap">
              <img src="images/sizzling-hibachi-steak-chicken.jpg" alt="Sizzling Hibachi Steak and Chicken" class="hasaki-card-img">
              <span class="hasaki-card-tag">Teppan Sizzle</span>
            </div>
            <div class="hasaki-card-body">
              <div class="hasaki-card-header">
                <h3 class="hasaki-card-title">Hibachi Steak &amp; Chicken</h3>
                <span class="hasaki-card-price">$16.95</span>
              </div>
              <p class="hasaki-card-desc">Tender NY strip steak and chicken breast seared with garlic butter, soy, and sesame seeds, served over teppan fried rice and hibachi zucchini and onions.</p>
              <div class="hasaki-card-meta">
                <span class="hasaki-meta-pill">Yum Yum Sauce</span>
                <span class="hasaki-meta-pill">Fried Rice Included</span>
              </div>
              <a href="teppan-hibachi-and-bento-boxes.html" class="hasaki-btn hasaki-btn-primary" style="text-align: center; width: 100%;">Customize Hibachi</a>
            </div>
          </div>

          <div class="hasaki-card">
            <div class="hasaki-card-img-wrap">
              <img src="images/chef-specialty-sushi-rolls.jpg" alt="Chef Specialty Sushi Rolls" class="hasaki-card-img">
              <span class="hasaki-card-tag">Chef Roll</span>
            </div>
            <div class="hasaki-card-body">
              <div class="hasaki-card-header">
                <h3 class="hasaki-card-title">The Volcano Roll</h3>
                <span class="hasaki-card-price">$14.50</span>
              </div>
              <p class="hasaki-card-desc">California roll base topped with warm baked spicy crab salad, scallops, crunchy tempura flakes, scallions, eel sauce, and spicy sriracha glaze.</p>
              <div class="hasaki-card-meta">
                <span class="hasaki-meta-pill">Warm Baked Roll</span>
                <span class="hasaki-meta-pill">Spicy Crab Topping</span>
              </div>
              <a href="specialty-sushi-rolls-and-sashimi.html" class="hasaki-btn hasaki-btn-primary" style="text-align: center; width: 100%;">View Sushi Rolls</a>
            </div>
          </div>

          <div class="hasaki-card">
            <div class="hasaki-card-img-wrap">
              <img src="images/japanese-lunch-bento-box.jpg" alt="Japanese Lunch Bento Box" class="hasaki-card-img">
              <span class="hasaki-card-tag">Complete Lunch</span>
            </div>
            <div class="hasaki-card-body">
              <div class="hasaki-card-header">
                <h3 class="hasaki-card-title">Executive Bento Box</h3>
                <span class="hasaki-card-price">$15.50</span>
              </div>
              <p class="hasaki-card-desc">Choice of Teriyaki Chicken, Salmon, or Steak with 4-piece California roll, pan-seared pork gyoza, ginger salad, fried rice, and sweet Yum Yum sauce.</p>
              <div class="hasaki-card-meta">
                <span class="hasaki-meta-pill">California Roll (4pc)</span>
                <span class="hasaki-meta-pill">Gyoza &amp; Salad</span>
              </div>
              <a href="teppan-hibachi-and-bento-boxes.html" class="hasaki-btn hasaki-btn-secondary" style="text-align: center; width: 100%;">Build Bento</a>
            </div>
          </div>
        </div>
      </section>
    </div>
"""

menu_content = """
    <div class="hasaki-container">
      <div class="hasaki-section-header">
        <span class="hasaki-badge">Ally Center Menu</span>
        <h1 class="hasaki-title">Hasaki Grill &amp; Sushi Full Menu</h1>
        <p class="hasaki-subtitle">Teppan grilled hibachi, artisan sushi rolls, Japanese lunch bentos, and appetizers served daily in Uptown Charlotte.</p>
      </div>

      <div class="hasaki-grid-2">
        <!-- Hibachi Entrees -->
        <div class="hasaki-card" style="padding: 28px;">
          <h3 class="hasaki-card-title" style="margin-bottom: 20px; border-bottom: 2px solid var(--hasaki-border); padding-bottom: 10px;">Teppanyaki Hibachi Entrees</h3>
          
          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--hasaki-charcoal);">Hibachi Teriyaki Chicken</span>
              <span style="color: var(--hasaki-red);">$13.95</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--hasaki-text-muted);">Juicy chicken breast glazed in sweet ginger teriyaki, teppan fried rice, sweet zucchini and onions, and Yum Yum sauce.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--hasaki-charcoal);">Hibachi NY Strip Steak</span>
              <span style="color: var(--hasaki-red);">$16.50</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--hasaki-text-muted);">Prime NY strip steak seared on the teppan flat top with garlic butter and soy reduction glaze.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--hasaki-charcoal);">Hibachi Jumbo Gulf Shrimp</span>
              <span style="color: var(--hasaki-red);">$15.95</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--hasaki-text-muted);">Succulent tail-on Gulf shrimp seared with lemon herb butter and soy, served with fried rice.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--hasaki-charcoal);">Hibachi Steak, Chicken &amp; Shrimp Trio</span>
              <span style="color: var(--hasaki-red);">$20.95</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--hasaki-text-muted);">The ultimate feast. Sizzling combination of steak, tender chicken, and gulf shrimp with extra fried rice.</p>
          </div>
        </div>

        <!-- Specialty Sushi Rolls -->
        <div class="hasaki-card" style="padding: 28px;">
          <h3 class="hasaki-card-title" style="margin-bottom: 20px; border-bottom: 2px solid var(--hasaki-border); padding-bottom: 10px;">Specialty Sushi Rolls</h3>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--hasaki-charcoal);">The Volcano Roll</span>
              <span style="color: var(--hasaki-red);">$14.50</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--hasaki-text-muted);">California roll topped with baked spicy crab, bay scallops, tempura flakes, scallions, eel sauce, and spicy mayo.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--hasaki-charcoal);">Queen City Roll</span>
              <span style="color: var(--hasaki-red);">$14.95</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--hasaki-text-muted);">Tempura shrimp and cream cheese inside, topped with spicy tuna, avocado, eel sauce, and masago.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--hasaki-charcoal);">Godzilla Crunch Roll</span>
              <span style="color: var(--hasaki-red);">$13.95</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--hasaki-text-muted);">Spicy salmon, cream cheese, and avocado roll deep fried in crispy panko, drizzled with spicy unagi glaze.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--hasaki-charcoal);">Rainbow Roll</span>
              <span style="color: var(--hasaki-red);">$14.50</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--hasaki-text-muted);">Crab salad and cucumber roll draped with fresh Atlantic salmon, yellowfin tuna, yellowtail, and avocado.</p>
          </div>
        </div>
      </div>

      <!-- Bentos & Appetizers -->
      <div class="hasaki-grid-2" style="margin-top: 30px;">
        <div class="hasaki-card" style="padding: 28px;">
          <h3 class="hasaki-card-title" style="margin-bottom: 16px;">Lunch Bento Boxes</h3>
          <div style="margin-bottom: 14px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Teriyaki Chicken Bento</span>
              <span style="color: var(--hasaki-red);">$14.50</span>
            </div>
            <small style="color: var(--hasaki-text-muted);">Chicken teriyaki, 4pc California roll, 2pc pork gyoza, fried rice, and ginger salad.</small>
          </div>
          <div style="margin-bottom: 14px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Hibachi Steak Bento</span>
              <span style="color: var(--hasaki-red);">$16.50</span>
            </div>
            <small style="color: var(--hasaki-text-muted);">NY strip steak, 4pc California roll, 2pc gyoza, fried rice, and ginger salad.</small>
          </div>
          <div>
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Salmon Teriyaki Bento</span>
              <span style="color: var(--hasaki-red);">$16.95</span>
            </div>
            <small style="color: var(--hasaki-text-muted);">Pan-seared Atlantic salmon in sweet teriyaki glaze with complete bento fixings.</small>
          </div>
        </div>

        <div class="hasaki-card" style="padding: 28px;">
          <h3 class="hasaki-card-title" style="margin-bottom: 16px;">Appetizers, Soups &amp; Drinks</h3>
          <div style="margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Pan-Seared Pork Gyoza (6 pcs)</span>
              <span style="color: var(--hasaki-red);">$6.95</span>
            </div>
            <small style="color: var(--hasaki-text-muted);">Crispy Japanese dumplings with pork and scallions, served with sesame soy dip.</small>
          </div>
          <div style="margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Steamed Edamame with Sea Salt</span>
              <span style="color: var(--hasaki-red);">$5.25</span>
            </div>
            <small style="color: var(--hasaki-text-muted);">Fresh young soybeans steamed and tossed with coarse Japanese sea salt.</small>
          </div>
          <div>
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Japanese Beers &amp; Chilled Sake</span>
              <span style="color: var(--hasaki-red);">$6.00 &ndash; $11.00</span>
            </div>
            <small style="color: var(--hasaki-text-muted);">Sapporo, Asahi Super Dry, Kirin Ichiban, and premium Junmai Ginjo sake.</small>
          </div>
        </div>
      </div>
    </div>
"""

hibachi_content = """
    <div class="hasaki-container">
      <div class="hasaki-section-header">
        <span class="hasaki-badge">Interactive Bento Studio</span>
        <h1 class="hasaki-title">Teppan Hibachi &amp; Bento Box Builder</h1>
        <p class="hasaki-subtitle">Custom configure your perfect Japanese bento box or hibachi platter. Calculate real-time pricing and calorie counts instantly.</p>
      </div>

      <div class="hasaki-builder-card hasaki-bento-builder">
        <div class="hasaki-builder-step">
          <div class="hasaki-step-label">
            <span class="hasaki-step-number">1</span>
            <span>Choose Your Teppan Protein</span>
          </div>
          <div class="hasaki-options-grid">
            <button class="hasaki-opt-btn hasaki-opt-protein active" data-name="Hibachi Teriyaki Chicken" data-price="13.95" data-cal="380">Teriyaki Chicken - $13.95</button>
            <button class="hasaki-opt-btn hasaki-opt-protein" data-name="Hibachi NY Strip Steak" data-price="16.50" data-cal="440">NY Strip Steak - $16.50</button>
            <button class="hasaki-opt-btn hasaki-opt-protein" data-name="Hibachi Jumbo Gulf Shrimp" data-price="15.95" data-cal="320">Gulf Shrimp - $15.95</button>
            <button class="hasaki-opt-btn hasaki-opt-protein" data-name="Steak & Chicken Combo" data-price="18.50" data-cal="510">Steak &amp; Chicken - $18.50</button>
            <button class="hasaki-opt-btn hasaki-opt-protein" data-name="Hibachi Sautéed Veggie & Tofu" data-price="12.50" data-cal="260">Veggie &amp; Tofu - $12.50</button>
          </div>
        </div>

        <div class="hasaki-builder-step">
          <div class="hasaki-step-label">
            <span class="hasaki-step-number">2</span>
            <span>Select Rice or Noodle Base</span>
          </div>
          <div class="hasaki-options-grid">
            <button class="hasaki-opt-btn hasaki-opt-base active" data-name="Teppan Hibachi Fried Rice" data-cal="260">Hibachi Fried Rice</button>
            <button class="hasaki-opt-btn hasaki-opt-base" data-name="Sautéed Yakisoba Noodles" data-cal="280">Yakisoba Noodles</button>
            <button class="hasaki-opt-btn hasaki-opt-base" data-name="Steamed Calrose White Rice" data-cal="210">Steamed White Rice</button>
            <button class="hasaki-opt-btn hasaki-opt-base" data-name="Double Hibachi Veggies (No Rice)" data-cal="110">Double Veggies</button>
          </div>
        </div>

        <div class="hasaki-builder-step">
          <div class="hasaki-step-label">
            <span class="hasaki-step-number">3</span>
            <span>Choose Bento Side Appetizer</span>
          </div>
          <div class="hasaki-options-grid">
            <button class="hasaki-opt-btn hasaki-opt-side active" data-name="Pan-Seared Pork Gyoza (3 pcs)" data-cal="180">Pork Gyoza (3pc)</button>
            <button class="hasaki-opt-btn hasaki-opt-side" data-name="California Sushi Roll (4 pcs)" data-cal="160">California Roll (4pc)</button>
            <button class="hasaki-opt-btn hasaki-opt-side" data-name="Crispy Veggie Spring Rolls (2 pcs)" data-cal="150">Spring Rolls (2pc)</button>
            <button class="hasaki-opt-btn hasaki-opt-side" data-name="Seasoned Seaweed Salad" data-cal="70">Seaweed Salad</button>
          </div>
        </div>

        <div class="hasaki-builder-step">
          <div class="hasaki-step-label">
            <span class="hasaki-step-number">4</span>
            <span>Select Signature Sauce</span>
          </div>
          <div class="hasaki-options-grid">
            <button class="hasaki-opt-btn hasaki-opt-sauce active" data-name="Signature White Yum Yum Sauce" data-cal="120">Yum Yum Sauce</button>
            <button class="hasaki-opt-btn hasaki-opt-sauce" data-name="Sweet Ginger Teriyaki Glaze" data-cal="80">Ginger Teriyaki</button>
            <button class="hasaki-opt-btn hasaki-opt-sauce" data-name="Spicy Sriracha Mayo" data-cal="110">Spicy Mayo</button>
            <button class="hasaki-opt-btn hasaki-opt-sauce" data-name="Double Sauce (Yum Yum + Ginger)" data-cal="200">Both Sauces</button>
          </div>
        </div>

        <div class="hasaki-builder-step">
          <div class="hasaki-step-label">
            <span class="hasaki-step-number">5</span>
            <span>Teppan Add-Ons</span>
          </div>
          <div class="hasaki-options-grid">
            <button id="hasaki-toggle-shrimp" class="hasaki-opt-btn">Add Gulf Shrimp 4pc (+$4.50)</button>
            <button id="hasaki-toggle-noodles" class="hasaki-opt-btn">Add Yakisoba Noodles (+$3.00)</button>
          </div>
        </div>

        <div class="hasaki-summary-panel">
          <div class="hasaki-summary-metrics">
            <div class="hasaki-metric-item">
              <span class="hasaki-metric-label">Estimated Price</span>
              <span id="hasaki-builder-price" class="hasaki-metric-val">$13.95</span>
            </div>
            <div class="hasaki-metric-item">
              <span class="hasaki-metric-label">Approx. Calories</span>
              <span id="hasaki-builder-calories" class="hasaki-metric-val" style="color: #67e8f9;">940 kcal</span>
            </div>
          </div>
          <div style="flex-basis: 100%; border-top: 1px solid #27272a; padding-top: 16px; margin-top: 10px;">
            <strong style="color: #a1a1aa; display: block; font-size: 0.85rem; text-transform: uppercase;">Your Customized Bento:</strong>
            <p id="hasaki-builder-summary" style="color: #ffffff; font-size: 1rem; margin-top: 4px;">Hibachi Teriyaki Chicken with Teppan Hibachi Fried Rice, Pan-Seared Pork Gyoza, and Signature White Yum Yum Sauce. Includes sweet hibachi zucchini, onions, mushrooms, and house ginger dressing salad.</p>
          </div>
        </div>
      </div>
    </div>
"""

pages = {
    "index.html": ("Home", index_content),
    "menu.html": ("Full Menu", menu_content),
    "teppan-hibachi-and-bento-boxes.html": ("Hibachi & Bentos", hibachi_content)
}

for filename, (label, content) in pages.items():
    html = wrap_page(label, filename, content)
    with open(os.path.join("hasaki-grill-and-sushi", filename), "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"Generated {filename}")
