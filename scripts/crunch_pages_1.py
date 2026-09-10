import os
from crunch_core import wrap_page

index_content = """
    <section class="crunch-hero">
      <div class="crunch-hero-content">
        <span class="crunch-badge crunch-badge-lime">401 N Tryon St &bull; Uptown Charlotte</span>
        <h1 class="crunch-hero-title">Fuel Your Day With <span>Nutritious Clean Eats</span></h1>
        <p class="crunch-hero-lead">Custom chopped greens, warm ancient grain bowls, crispy lavash flatbreads, and organic Brazilian açaí bowls made fresh daily in Uptown Charlotte.</p>
        <div class="crunch-hero-actions">
          <a href="menu.html" class="crunch-btn crunch-btn-primary">View Clean Menu</a>
          <a href="signature-chopped-salads-and-warm-bowls.html" class="crunch-btn crunch-btn-secondary">Build Custom Bowl</a>
          <a href="superfruit-acai-and-corporate-catering.html" class="crunch-btn crunch-btn-berry">Açaí &amp; Catering</a>
        </div>
        <div class="crunch-hero-highlights">
          <div class="crunch-highlight-box">
            <div class="crunch-highlight-title">Chopped Fresh</div>
            <div class="crunch-highlight-desc">Organic leafy greens hand-chopped and tossed with house-crafted dressings.</div>
          </div>
          <div class="crunch-highlight-box">
            <div class="crunch-highlight-title">Warm Grain Bowls</div>
            <div class="crunch-highlight-desc">Tricolor quinoa, wild brown rice, roasted root veggies, and clean lean proteins.</div>
          </div>
          <div class="crunch-highlight-box">
            <div class="crunch-highlight-title">Lavash Flatbreads</div>
            <div class="crunch-highlight-desc">Thin crispy flatbreads baked to perfection with gourmet artisanal toppings.</div>
          </div>
          <div class="crunch-highlight-box">
            <div class="crunch-highlight-title">Salad-to-Wrap</div>
            <div class="crunch-highlight-desc">Any signature salad recipe can be spun into a warm pressed whole wheat wrap.</div>
          </div>
        </div>
      </div>
    </section>

    <div class="crunch-container">
      <div class="crunch-info-box" style="margin-top: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
          <div>
            <span class="crunch-badge crunch-badge-lime" style="margin-bottom: 6px;">Uptown Health Hub</span>
            <h2 style="font-family: var(--crunch-font-display); color: var(--crunch-charcoal); font-size: 1.6rem; font-weight: 800;">Fast, Wholesome, Chef-Crafted Lunch</h2>
            <p style="color: var(--crunch-text-muted); font-size: 0.95rem;">Located at 401 N Tryon Street, we serve Uptown's busy professionals healthy lunches that never compromise on rich taste or nutritional density.</p>
          </div>
          <a href="visit.html" class="crunch-btn crunch-btn-primary">Visit 401 N Tryon &rarr;</a>
        </div>
      </div>

      <section class="crunch-section">
        <div class="crunch-section-header">
          <span class="crunch-badge">Menu Highlights</span>
          <h2 class="crunch-title">Vibrant Bowls &amp; Wholesome Plates</h2>
          <p class="crunch-subtitle">Freshly chopped daily ingredients paired with scratch dressings and nutrient-rich grains.</p>
        </div>

        <div class="crunch-grid-3">
          <div class="crunch-card">
            <div class="crunch-card-img-wrap">
              <img src="images/signature-chopped-salad-bowl.jpg" alt="Signature Chopped Salad Bowl" class="crunch-card-img">
              <span class="crunch-card-tag">Signature Greens</span>
            </div>
            <div class="crunch-card-body">
              <div class="crunch-card-header">
                <h3 class="crunch-card-title">Green Goddess Crunch</h3>
                <span class="crunch-card-price">$12.50</span>
              </div>
              <p class="crunch-card-desc">Chopped kale, baby spinach, herb-seared chicken breast, Hass avocado, cucumber, edamame, spiced chickpeas, and house creamy green goddess dressing.</p>
              <div class="crunch-card-meta">
                <span class="crunch-meta-pill">High Protein</span>
                <span class="crunch-meta-pill">Gluten-Conscious</span>
              </div>
              <a href="signature-chopped-salads-and-warm-bowls.html" class="crunch-btn crunch-btn-primary" style="text-align: center; width: 100%;">Customize Salad</a>
            </div>
          </div>

          <div class="crunch-card">
            <div class="crunch-card-img-wrap">
              <img src="images/warm-quinoa-grain-bowl.jpg" alt="Warm Quinoa Grain Bowl" class="crunch-card-img">
              <span class="crunch-card-tag">Warm Ancient Grains</span>
            </div>
            <div class="crunch-card-body">
              <div class="crunch-card-header">
                <h3 class="crunch-card-title">Santa Fe Quinoa Bowl</h3>
                <span class="crunch-card-price">$13.25</span>
              </div>
              <p class="crunch-card-desc">Warm tricolor quinoa, seasoned black beans, fire-roasted corn, grape tomatoes, grilled chicken or tofu, pickled red onion, and chipotle lime drizzle.</p>
              <div class="crunch-card-meta">
                <span class="crunch-meta-pill">Fiber Rich</span>
                <span class="crunch-meta-pill">Warm Bowl</span>
              </div>
              <a href="signature-chopped-salads-and-warm-bowls.html" class="crunch-btn crunch-btn-primary" style="text-align: center; width: 100%;">Customize Bowl</a>
            </div>
          </div>

          <div class="crunch-card">
            <div class="crunch-card-img-wrap">
              <img src="images/organic-acai-superfruit-bowl.jpg" alt="Organic Acai Superfruit Bowl" class="crunch-card-img">
              <span class="crunch-card-tag">Superfruit Energy</span>
            </div>
            <div class="crunch-card-body">
              <div class="crunch-card-header">
                <h3 class="crunch-card-title">Brazilian Açaí Bowl</h3>
                <span class="crunch-card-price">$9.95+</span>
              </div>
              <p class="crunch-card-desc">Thick organic açaí base topped with gluten-free toasted coconut granola, fresh sliced strawberries, wild blueberries, chia seeds, and raw local honey drizzle.</p>
              <div class="crunch-card-meta">
                <span class="crunch-meta-pill">Antioxidant Rich</span>
                <span class="crunch-meta-pill">Dairy Free</span>
              </div>
              <a href="superfruit-acai-and-corporate-catering.html" class="crunch-btn crunch-btn-berry" style="text-align: center; width: 100%;">Explore Açaí</a>
            </div>
          </div>
        </div>
      </section>
    </div>
"""

menu_content = """
    <div class="crunch-container">
      <div class="crunch-section-header">
        <span class="crunch-badge">Complete Wellness Menu</span>
        <h1 class="crunch-title">Nutrient-Dense Bistro Offerings</h1>
        <p class="crunch-subtitle">Freshly prepared with whole food ingredients, non-GMO grains, clean proteins, and scratch-made dressings.</p>
      </div>

      <div class="crunch-grid-2">
        <!-- Salads & Bowls -->
        <div class="crunch-card" style="padding: 28px;">
          <h3 class="crunch-card-title" style="margin-bottom: 20px; border-bottom: 2px solid var(--crunch-border); padding-bottom: 10px;">Signature Chopped Salads</h3>
          
          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--crunch-charcoal);">Green Goddess Avocado Chicken</span>
              <span style="color: var(--crunch-emerald);">$12.50</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--crunch-text-muted);">Chopped kale, baby spinach, herb chicken, avocado, cucumber, spiced chickpeas, and house green goddess dressing.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--crunch-charcoal);">Thai Sesame Peanut Crunch</span>
              <span style="color: var(--crunch-emerald);">$12.75</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--crunch-text-muted);">Shredded cabbage, romaine, grilled chicken or tofu, edamame, carrots, cilantro, crispy wontons, and Thai peanut dressing.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--crunch-charcoal);">Mediterranean Harvest</span>
              <span style="color: var(--crunch-emerald);">$12.25</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--crunch-text-muted);">Romaine, cucumber, Kalamata olives, grape tomatoes, pickled red onions, crumbled feta cheese, and lemon herb vinaigrette.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--crunch-charcoal);">Baja Chipotle Lime</span>
              <span style="color: var(--crunch-emerald);">$12.50</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--crunch-text-muted);">Crisp romaine, black beans, roasted sweet corn, diced peppers, pepper jack cheese, tortilla strips, and chipotle ranch.</p>
          </div>
        </div>

        <!-- Warm Grain Bowls & Flatbreads -->
        <div class="crunch-card" style="padding: 28px;">
          <h3 class="crunch-card-title" style="margin-bottom: 20px; border-bottom: 2px solid var(--crunch-border); padding-bottom: 10px;">Warm Grain Bowls &amp; Flatbreads</h3>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--crunch-charcoal);">Warm Santa Fe Quinoa Bowl</span>
              <span style="color: var(--crunch-emerald);">$13.25</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--crunch-text-muted);">Warm tricolor quinoa, seasoned black beans, fire-roasted corn, avocado, grilled chicken, and cilantro chimichurri.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--crunch-charcoal);">Tuscan Roasted Veggie Grain Bowl</span>
              <span style="color: var(--crunch-emerald);">$12.95</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--crunch-text-muted);">Warm ancient grains, roasted sweet potatoes, charred broccoli florets, goat cheese, pumpkin seeds, and balsamic glaze.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--crunch-charcoal);">Crispy Caprese Lavash Flatbread</span>
              <span style="color: var(--crunch-emerald);">$10.95</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--crunch-text-muted);">Thin lavash crust baked crisp with fresh mozzarella, grape tomatoes, fresh basil ribbons, and aged balsamic drizzle.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--crunch-charcoal);">Smoky BBQ Chicken Lavash</span>
              <span style="color: var(--crunch-emerald);">$11.50</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--crunch-text-muted);">Grilled chicken, smoked gouda, red onion slivers, cilantro, and tangy clean barbecue reduction on lavash flatbread.</p>
          </div>
        </div>
      </div>

      <!-- Superfruit & Soups -->
      <div class="crunch-grid-2" style="margin-top: 30px;">
        <div class="crunch-card" style="padding: 28px;">
          <h3 class="crunch-card-title" style="margin-bottom: 16px;">Superfruit Açaí Bowls &amp; Parfaits</h3>
          <div style="margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Classic Brazilian Açaí Bowl</span>
              <span style="color: var(--crunch-emerald);">$9.95 / $12.50</span>
            </div>
            <small style="color: var(--crunch-text-muted);">Organic açaí base with GF granola, banana, strawberries, blueberries, and raw honey.</small>
          </div>
          <div style="margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Almond Butter Superfood Bowl</span>
              <span style="color: var(--crunch-emerald);">$11.45</span>
            </div>
            <small style="color: var(--crunch-text-muted);">Thick açaí base with organic creamy almond butter, chia seeds, cacao nibs, and coconut flakes.</small>
          </div>
          <div>
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Greek Yogurt Berry Parfait</span>
              <span style="color: var(--crunch-emerald);">$6.95</span>
            </div>
            <small style="color: var(--crunch-text-muted);">High-protein Greek yogurt layered with house chia berry compote and toasted coconut crunch.</small>
          </div>
        </div>

        <div class="crunch-card" style="padding: 28px;">
          <h3 class="crunch-card-title" style="margin-bottom: 16px;">Scratch Kettle Soups &amp; Beverages</h3>
          <div style="margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Daily Scratch Kettle Soup</span>
              <span style="color: var(--crunch-emerald);">$5.95</span>
            </div>
            <small style="color: var(--crunch-text-muted);">Rotating options: Roasted Tomato Basil, Lemon Chicken Orzo, or Vegan Lentil Vegetable.</small>
          </div>
          <div style="margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Cold-Pressed Wellness Juices</span>
              <span style="color: var(--crunch-emerald);">$6.50</span>
            </div>
            <small style="color: var(--crunch-text-muted);">Fresh ginger green detox, citrus immunity, and beet apple vitality blends.</small>
          </div>
          <div>
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Hibiscus Berry Iced Tea</span>
              <span style="color: var(--crunch-emerald);">$3.25</span>
            </div>
            <small style="color: var(--crunch-text-muted);">Unsweetened organic herbal infusion with citrus notes.</small>
          </div>
        </div>
      </div>
    </div>
"""

salads_content = """
    <div class="crunch-container">
      <div class="crunch-section-header">
        <span class="crunch-badge">Interactive Nutrition Studio</span>
        <h1 class="crunch-title">Signature Chopped Salads &amp; Warm Bowls</h1>
        <p class="crunch-subtitle">Design your personalized wellness bowl or wrap. Calculate real-time pricing, macro balance, and calories instantly.</p>
      </div>

      <div class="crunch-builder-card crunch-bowl-builder">
        <div class="crunch-builder-step">
          <div class="crunch-step-label">
            <span class="crunch-step-number">1</span>
            <span>Select Greens or Warm Grain Base</span>
          </div>
          <div class="crunch-options-grid">
            <button class="crunch-opt-btn crunch-opt-base active" data-name="Organic Chopped Kale & Romaine" data-price="11.50" data-cal="110">Kale &amp; Romaine - $11.50</button>
            <button class="crunch-opt-btn crunch-opt-base" data-name="Warm Tricolor Quinoa & Grains" data-price="12.50" data-cal="260">Warm Quinoa - $12.50</button>
            <button class="crunch-opt-btn crunch-opt-base" data-name="Baby Spinach & Wild Arugula" data-price="11.50" data-cal="90">Spinach &amp; Arugula - $11.50</button>
            <button class="crunch-opt-btn crunch-opt-base" data-name="Half Greens & Half Quinoa" data-price="12.00" data-cal="180">50/50 Greens &amp; Quinoa - $12.00</button>
            <button class="crunch-opt-btn crunch-opt-base" data-name="Whole Wheat Pressed Wrap Format" data-price="11.50" data-cal="240">Spin into Wrap - $11.50</button>
          </div>
        </div>

        <div class="crunch-builder-step">
          <div class="crunch-step-label">
            <span class="crunch-step-number">2</span>
            <span>Choose Clean Protein</span>
          </div>
          <div class="crunch-options-grid">
            <button class="crunch-opt-btn crunch-opt-protein active" data-name="Herb-Seared Chicken Breast" data-cal="180">Herb Chicken</button>
            <button class="crunch-opt-btn crunch-opt-protein" data-name="Grilled Gulf Shrimp (+$1.50)" data-cal="120">Gulf Shrimp (+$1.50)</button>
            <button class="crunch-opt-btn crunch-opt-protein" data-name="Sesame Baked Organic Tofu" data-cal="140">Organic Tofu</button>
            <button class="crunch-opt-btn crunch-opt-protein" data-name="Seared Flank Steak (+$2.00)" data-cal="210">Flank Steak (+$2.00)</button>
          </div>
        </div>

        <div class="crunch-builder-step">
          <div class="crunch-step-label">
            <span class="crunch-step-number">3</span>
            <span>Select House Scratch Dressing</span>
          </div>
          <div class="crunch-options-grid">
            <button class="crunch-opt-btn crunch-opt-dressing active" data-name="House Creamy Green Goddess" data-cal="90">Green Goddess</button>
            <button class="crunch-opt-btn crunch-opt-dressing" data-name="Lemon Tahini Herb Vinaigrette" data-cal="80">Lemon Tahini</button>
            <button class="crunch-opt-btn crunch-opt-dressing" data-name="Thai Sesame Ginger" data-cal="85">Sesame Ginger</button>
            <button class="crunch-opt-btn crunch-opt-dressing" data-name="Chipotle Lime Ranch" data-cal="95">Chipotle Ranch</button>
            <button class="crunch-opt-btn crunch-opt-dressing" data-name="Aged Balsamic Fig Glaze" data-cal="65">Balsamic Fig</button>
          </div>
        </div>

        <div class="crunch-builder-step">
          <div class="crunch-step-label">
            <span class="crunch-step-number">4</span>
            <span>Choose Signature Crunch Topper</span>
          </div>
          <div class="crunch-options-grid">
            <button class="crunch-opt-btn crunch-opt-crunch active" data-name="Spiced Crispy Chickpeas" data-cal="80">Spiced Chickpeas</button>
            <button class="crunch-opt-btn crunch-opt-crunch" data-name="Crispy Wonton Strips" data-cal="90">Wonton Strips</button>
            <button class="crunch-opt-btn crunch-opt-crunch" data-name="Toasted Sunflower & Pumpkin Seeds" data-cal="75">Toasted Seeds</button>
            <button class="crunch-opt-btn crunch-opt-crunch" data-name="Tortilla Strips" data-cal="85">Tortilla Strips</button>
          </div>
        </div>

        <div class="crunch-builder-step">
          <div class="crunch-step-label">
            <span class="crunch-step-number">5</span>
            <span>Superfood Boosters &amp; Add-Ons</span>
          </div>
          <div class="crunch-options-grid">
            <button id="crunch-toggle-avocado" class="crunch-opt-btn active">Hass Avocado (+$2.00)</button>
            <button id="crunch-toggle-cheese" class="crunch-opt-btn">Artisan Goat Cheese (+$1.75)</button>
            <button id="crunch-toggle-protein" class="crunch-opt-btn">Double Protein (+$3.50)</button>
          </div>
        </div>

        <div class="crunch-summary-panel">
          <div class="crunch-summary-metrics">
            <div class="crunch-metric-item">
              <span class="crunch-metric-label">Estimated Price</span>
              <span id="crunch-builder-price" class="crunch-metric-val">$13.50</span>
            </div>
            <div class="crunch-metric-item">
              <span class="crunch-metric-label">Approx. Calories</span>
              <span id="crunch-builder-calories" class="crunch-metric-val" style="color: #67e8f9;">570 kcal</span>
            </div>
          </div>
          <div style="flex-basis: 100%; border-top: 1px solid #334155; padding-top: 16px; margin-top: 10px;">
            <strong style="color: #94a3b8; display: block; font-size: 0.85rem; text-transform: uppercase;">Custom Bowl Configuration:</strong>
            <p id="crunch-builder-summary" style="color: #ffffff; font-size: 1rem; margin-top: 4px;">Herb-Seared Chicken Breast over Organic Chopped Kale &amp; Romaine with House Creamy Green Goddess and Spiced Crispy Chickpeas + Fresh Hass Avocado. Includes artisan multigrain crisps.</p>
          </div>
        </div>
      </div>
    </div>
"""

pages = {
    "index.html": ("Home", index_content),
    "menu.html": ("Full Menu", menu_content),
    "signature-chopped-salads-and-warm-bowls.html": ("Salads & Grain Bowls", salads_content)
}

for filename, (label, content) in pages.items():
    html = wrap_page(label, filename, content)
    with open(os.path.join("crunch-bistro", filename), "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"Generated {filename}")
