import os
from tsc_core import wrap_page

index_content = """
    <section class="tsc-hero">
      <div class="tsc-hero-content">
        <span class="tsc-badge tsc-badge-mustard">435 S Tryon St &bull; Uptown Charlotte Institution</span>
        <h1 class="tsc-hero-title">Home of <span>30+ Handcrafted</span> Sandwiches</h1>
        <p class="tsc-hero-lead">Triple-decker toasted clubs, buttery croissant melts, early 7:00 AM breakfast biscuits, and Charlotte's premier office boxed lunch catering.</p>
        <div class="tsc-hero-actions">
          <a href="menu.html" class="tsc-btn tsc-btn-primary">View Full Deli Menu</a>
          <a href="triple-decker-clubs-and-gourmet-melts.html" class="tsc-btn tsc-btn-secondary">Build Custom Sandwich</a>
          <a href="corporate-lunch-boxes-and-platters.html" class="tsc-btn tsc-btn-green">Corporate Boxed Lunches</a>
        </div>
        <div class="tsc-hero-highlights">
          <div class="tsc-highlight-box">
            <div class="tsc-highlight-title">The Sandwich Club</div>
            <div class="tsc-highlight-desc">Triple-stacked toasted wheat with scratch chicken salad, bacon, lettuce, and tomato.</div>
          </div>
          <div class="tsc-highlight-box">
            <div class="tsc-highlight-title">The Grand Brie</div>
            <div class="tsc-highlight-desc">Warm rotisserie turkey, bacon, creamy brie cheese, arugula, and apple butter.</div>
          </div>
          <div class="tsc-highlight-box">
            <div class="tsc-highlight-title">7:00 AM Breakfast</div>
            <div class="tsc-highlight-desc">Scratch buttermilk biscuits, egg croissant melts, and fresh drip coffee.</div>
          </div>
          <div class="tsc-highlight-box">
            <div class="tsc-highlight-title">Uptown Delivery</div>
            <div class="tsc-highlight-desc">Individually labeled boxed lunches delivered to your corporate tower floor.</div>
          </div>
        </div>
      </div>
    </section>

    <div class="tsc-container">
      <div class="tsc-info-box" style="margin-top: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
          <div>
            <span class="tsc-badge tsc-badge-green" style="margin-bottom: 6px;">Old-School Uptown Soul</span>
            <h2 style="font-family: var(--tsc-font-display); color: var(--tsc-charcoal); font-size: 1.6rem;">Crafting Charlotte's Best Lunches Since 1993</h2>
            <p style="color: var(--tsc-text-muted); font-size: 0.95rem;">Located right across from The Green pocket park at 435 S Tryon Street, we take pride in slicing premium meats, baking daily breads, and assembling over thirty distinct recipes.</p>
          </div>
          <a href="visit.html" class="tsc-btn tsc-btn-primary">Visit 435 S Tryon &rarr;</a>
        </div>
      </div>

      <section class="tsc-section">
        <div class="tsc-section-header">
          <span class="tsc-badge">Deli Signatures</span>
          <h2 class="tsc-title">Uptown's Favorite Handcrafted Classics</h2>
          <p class="tsc-subtitle">Made to order with premium deli meats, artisan cheeses, scratch chicken salads, and house-blended dressings.</p>
        </div>

        <div class="tsc-grid-3">
          <div class="tsc-card">
            <div class="tsc-card-img-wrap">
              <img src="images/triple-decker-club-sandwich.jpg" alt="The Sandwich Club Triple-Decker" class="tsc-card-img">
              <span class="tsc-card-tag">Flagship #1</span>
            </div>
            <div class="tsc-card-body">
              <div class="tsc-card-header">
                <h3 class="tsc-card-title">The Sandwich Club</h3>
                <span class="tsc-card-price">$11.25</span>
              </div>
              <p class="tsc-card-desc">Our namesake icon. Homemade tarragon chicken salad, thick hardwood bacon, crisp romaine, and ripe vine tomato layered on triple-stacked toasted wheat.</p>
              <div class="tsc-card-meta">
                <span class="tsc-meta-pill">Triple Wheat Toast</span>
                <span class="tsc-meta-pill">Includes Chips &amp; Pickle</span>
              </div>
              <a href="triple-decker-clubs-and-gourmet-melts.html" class="tsc-btn tsc-btn-primary" style="text-align: center; width: 100%;">Customize Club</a>
            </div>
          </div>

          <div class="tsc-card">
            <div class="tsc-card-img-wrap">
              <img src="images/grand-brie-croissant-melt.jpg" alt="The Grand Brie Croissant Melt" class="tsc-card-img">
              <span class="tsc-card-tag">Gourmet Melt</span>
            </div>
            <div class="tsc-card-body">
              <div class="tsc-card-header">
                <h3 class="tsc-card-title">The Grand Brie</h3>
                <span class="tsc-card-price">$12.50</span>
              </div>
              <p class="tsc-card-desc">Oven-roasted rotisserie turkey, crispy bacon, melted French brie cheese, peppery baby arugula, and house spiced apple butter on a warm flaky croissant.</p>
              <div class="tsc-card-meta">
                <span class="tsc-meta-pill">Warm Croissant</span>
                <span class="tsc-meta-pill">Spiced Apple Butter</span>
              </div>
              <a href="triple-decker-clubs-and-gourmet-melts.html" class="tsc-btn tsc-btn-primary" style="text-align: center; width: 100%;">Order Melt</a>
            </div>
          </div>

          <div class="tsc-card">
            <div class="tsc-card-img-wrap">
              <img src="images/corporate-boxed-lunch-spread.jpg" alt="Corporate Boxed Lunch Spread" class="tsc-card-img">
              <span class="tsc-card-tag">Office Catering</span>
            </div>
            <div class="tsc-card-body">
              <div class="tsc-card-header">
                <h3 class="tsc-card-title">Corporate Lunch Boxes</h3>
                <span class="tsc-card-price">$14.50+</span>
              </div>
              <p class="tsc-card-desc">Individually packaged bento lunch boxes featuring any signature sandwich, gourmet kettle chips, Sweet Girl freshly baked cookie, and deli pickle spear.</p>
              <div class="tsc-card-meta">
                <span class="tsc-meta-pill">Sweet Girl Cookie</span>
                <span class="tsc-meta-pill">Tower Delivery</span>
              </div>
              <a href="corporate-lunch-boxes-and-platters.html" class="tsc-btn tsc-btn-green" style="text-align: center; width: 100%;">Catering Estimator</a>
            </div>
          </div>
        </div>
      </section>
    </div>
"""

menu_content = """
    <div class="tsc-container">
      <div class="tsc-section-header">
        <span class="tsc-badge">Over 30 Specialties</span>
        <h1 class="tsc-title">The Sandwich Club Menu</h1>
        <p class="tsc-subtitle">Handcrafted deli sandwiches, hot panini melts, fresh wraps, and scratch breakfast served Monday through Friday.</p>
      </div>

      <div class="tsc-grid-2">
        <!-- Signature Clubs & Melts -->
        <div class="tsc-card" style="padding: 28px;">
          <h3 class="tsc-card-title" style="margin-bottom: 20px; border-bottom: 2px solid var(--tsc-border); padding-bottom: 10px;">Signature Clubs &amp; Paninis</h3>
          
          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--tsc-charcoal);">The Sandwich Club (Triple Stack)</span>
              <span style="color: var(--tsc-burgundy);">$11.25</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--tsc-text-muted);">Homemade tarragon chicken salad, thick hardwood bacon, romaine, tomato, and mayo on triple-decker toasted wheat.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--tsc-charcoal);">The Grand Brie</span>
              <span style="color: var(--tsc-burgundy);">$12.50</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--tsc-text-muted);">Rotisserie turkey breast, crispy bacon, creamy French brie, arugula, and spiced apple butter on a toasted croissant.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--tsc-charcoal);">The Gobbler</span>
              <span style="color: var(--tsc-burgundy);">$11.75</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--tsc-text-muted);">Roasted turkey breast, savory herb stuffing, tart cranberry relish, and mayo on toasted sourdough.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--tsc-charcoal);">Italian Combo Sub</span>
              <span style="color: var(--tsc-burgundy);">$11.50</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--tsc-text-muted);">Capicola ham, Genoa salami, pepperoni, sharp provolone, shredded lettuce, tomato, banana peppers, and oregano oil.</p>
          </div>
        </div>

        <!-- Specialty Wraps & Hot Grills -->
        <div class="tsc-card" style="padding: 28px;">
          <h3 class="tsc-card-title" style="margin-bottom: 20px; border-bottom: 2px solid var(--tsc-border); padding-bottom: 10px;">Wraps, Grills &amp; Veggie Delights</h3>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--tsc-charcoal);">Mama Zuma's Revenge</span>
              <span style="color: var(--tsc-burgundy);">$11.95</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--tsc-text-muted);">Grilled chicken breast, fiery pepper jack cheese, ripe avocado, crushed jalapeño potato chips, and chipotle ranch.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--tsc-charcoal);">Roast Beef Italiano</span>
              <span style="color: var(--tsc-burgundy);">$11.95</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--tsc-text-muted);">Thin-sliced medium-rare roast beef, roasted red peppers, smoked provolone, and garlic herb aioli on ciabatta.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--tsc-charcoal);">Chicken Caesar Wrap</span>
              <span style="color: var(--tsc-burgundy);">$10.95</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--tsc-text-muted);">Grilled chicken, crisp chopped romaine, shaved parmesan, house croutons, and creamy Caesar dressing in spinach wrap.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--tsc-charcoal);">Avocado Caprese Melt (Veg)</span>
              <span style="color: var(--tsc-burgundy);">$10.50</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--tsc-text-muted);">Fresh mozzarella, vine ripe tomatoes, sliced avocado, fresh basil, and balsamic reduction glaze on pressed focaccia.</p>
          </div>
        </div>
      </div>

      <!-- Breakfast & Cookies -->
      <div class="tsc-grid-2" style="margin-top: 30px;">
        <div class="tsc-card" style="padding: 28px;">
          <h3 class="tsc-card-title" style="margin-bottom: 16px;">Morning Breakfast Bar (7:00 AM &ndash; 10:30 AM)</h3>
          <div style="margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Scratch Buttermilk Biscuit Sandwich</span>
              <span style="color: var(--tsc-burgundy);">$5.95</span>
            </div>
            <small style="color: var(--tsc-text-muted);">Fluffy Southern biscuit with folded egg, sharp cheddar, and choice of bacon or country sausage.</small>
          </div>
          <div style="margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Croissant Egg &amp; Brie Melt</span>
              <span style="color: var(--tsc-burgundy);">$7.25</span>
            </div>
            <small style="color: var(--tsc-text-muted);">Toasted buttery croissant with two eggs, melted French brie, hardwood bacon, and baby spinach.</small>
          </div>
          <div>
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Uptown Breakfast Burrito</span>
              <span style="color: var(--tsc-burgundy);">$7.95</span>
            </div>
            <small style="color: var(--tsc-text-muted);">Scrambled eggs, cheddar, black beans, chorizo sausage, and salsa in a toasted flour wrap.</small>
          </div>
        </div>

        <div class="tsc-card" style="padding: 28px;">
          <h3 class="tsc-card-title" style="margin-bottom: 16px;">Sides, Snacks &amp; Sweet Treats</h3>
          <div style="margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Sweet Girl Cookies (Charlotte Local)</span>
              <span style="color: var(--tsc-burgundy);">$2.75</span>
            </div>
            <small style="color: var(--tsc-text-muted);">Locally baked gourmet chocolate chunk, oatmeal cranberry, and peanut butter cookies.</small>
          </div>
          <div style="margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Gourmet Kettle Chips &amp; Deli Pickles</span>
              <span style="color: var(--tsc-burgundy);">$1.95</span>
            </div>
            <small style="color: var(--tsc-text-muted);">Dirty Chips (Jalapeno, Sea Salt, BBQ, Salt &amp; Vinegar) and crisp whole garlic dill pickles.</small>
          </div>
          <div>
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Fresh Brewed Coffee &amp; Cold Brew</span>
              <span style="color: var(--tsc-burgundy);">$2.50 &ndash; $3.95</span>
            </div>
            <small style="color: var(--tsc-text-muted);">Dark roast Colombian drip coffee, Southern sweet iced tea, and unsweet lemon tea.</small>
          </div>
        </div>
      </div>
    </div>
"""

clubs_content = """
    <div class="tsc-container">
      <div class="tsc-section-header">
        <span class="tsc-badge">Interactive Deli Studio</span>
        <h1 class="tsc-title">Triple-Decker Clubs &amp; Gourmet Melts</h1>
        <p class="tsc-subtitle">Craft your ultimate custom sandwich. Choose your bread, deli proteins, artisanal cheeses, and gourmet spreads with instant calorie and pricing feedback.</p>
      </div>

      <div class="tsc-builder-card tsc-sandwich-builder">
        <div class="tsc-builder-step">
          <div class="tsc-step-label">
            <span class="tsc-step-number">1</span>
            <span>Choose Your Bread &amp; Stack Format</span>
          </div>
          <div class="tsc-options-grid">
            <button class="tsc-opt-btn tsc-opt-bread active" data-name="Triple-Stacked Toasted Wheat" data-price="10.95" data-cal="320">Triple-Stack Wheat - $10.95</button>
            <button class="tsc-opt-btn tsc-opt-bread" data-name="Flaky Butter Croissant" data-price="11.95" data-cal="380">Flaky Croissant - $11.95</button>
            <button class="tsc-opt-btn tsc-opt-bread" data-name="Grilled Sourdough" data-price="10.50" data-cal="280">Grilled Sourdough - $10.50</button>
            <button class="tsc-opt-btn tsc-opt-bread" data-name="Artisan Ciabatta" data-price="10.75" data-cal="290">Artisan Ciabatta - $10.75</button>
            <button class="tsc-opt-btn tsc-opt-bread" data-name="Marbled Rye" data-price="10.50" data-cal="260">Marbled Rye - $10.50</button>
          </div>
        </div>

        <div class="tsc-builder-step">
          <div class="tsc-step-label">
            <span class="tsc-step-number">2</span>
            <span>Select Premium Deli Protein</span>
          </div>
          <div class="tsc-options-grid">
            <button class="tsc-opt-btn tsc-opt-protein active" data-name="Homemade Tarragon Chicken Salad" data-cal="280">Scratch Chicken Salad</button>
            <button class="tsc-opt-btn tsc-opt-protein" data-name="Oven-Roasted Turkey Breast" data-cal="180">Rotisserie Turkey</button>
            <button class="tsc-opt-btn tsc-opt-protein" data-name="Thin-Sliced Roast Beef" data-cal="210">Roast Beef</button>
            <button class="tsc-opt-btn tsc-opt-protein" data-name="Italian Capicola & Salami" data-cal="260">Italian Meats</button>
            <button class="tsc-opt-btn tsc-opt-protein" data-name="Sautéed Veggie & Avocado" data-cal="130">Veggie &amp; Avocado</button>
          </div>
        </div>

        <div class="tsc-builder-step">
          <div class="tsc-step-label">
            <span class="tsc-step-number">3</span>
            <span>Choose Artisan Cheese</span>
          </div>
          <div class="tsc-options-grid">
            <button class="tsc-opt-btn tsc-opt-cheese active" data-name="Aged White Cheddar" data-cal="110">White Cheddar</button>
            <button class="tsc-opt-btn tsc-opt-cheese" data-name="Creamy French Brie" data-cal="130">Creamy Brie</button>
            <button class="tsc-opt-btn tsc-opt-cheese" data-name="Smoked Provolone" data-cal="100">Smoked Provolone</button>
            <button class="tsc-opt-btn tsc-opt-cheese" data-name="Spicy Pepper Jack" data-cal="110">Pepper Jack</button>
            <button class="tsc-opt-btn tsc-opt-cheese" data-name="Swiss Cheese" data-cal="105">Swiss Cheese</button>
          </div>
        </div>

        <div class="tsc-builder-step">
          <div class="tsc-step-label">
            <span class="tsc-step-number">4</span>
            <span>Select Gourmet Spread</span>
          </div>
          <div class="tsc-options-grid">
            <button class="tsc-opt-btn tsc-opt-spread active" data-name="Herb Garlic Aioli" data-cal="60">Herb Garlic Aioli</button>
            <button class="tsc-opt-btn tsc-opt-spread" data-name="House Spiced Apple Butter" data-cal="45">Spiced Apple Butter</button>
            <button class="tsc-opt-btn tsc-opt-spread" data-name="Whole Grain Honey Mustard" data-cal="40">Honey Mustard</button>
            <button class="tsc-opt-btn tsc-opt-spread" data-name="Tart Cranberry Relish" data-cal="35">Cranberry Relish</button>
            <button class="tsc-opt-btn tsc-opt-spread" data-name="Chipotle Pepper Mayo" data-cal="70">Chipotle Mayo</button>
          </div>
        </div>

        <div class="tsc-builder-step">
          <div class="tsc-step-label">
            <span class="tsc-step-number">5</span>
            <span>Premium Add-Ons</span>
          </div>
          <div class="tsc-options-grid">
            <button id="tsc-toggle-bacon" class="tsc-opt-btn active">Hardwood Bacon (+$1.75)</button>
            <button id="tsc-toggle-avocado" class="tsc-opt-btn">Fresh Avocado (+$1.95)</button>
            <button id="tsc-toggle-meat" class="tsc-opt-btn">Double Meat Scoop (+$3.25)</button>
          </div>
        </div>

        <div class="tsc-summary-panel">
          <div class="tsc-summary-metrics">
            <div class="tsc-metric-item">
              <span class="tsc-metric-label">Estimated Price</span>
              <span id="tsc-builder-price" class="tsc-metric-val">$12.70</span>
            </div>
            <div class="tsc-metric-item">
              <span class="tsc-metric-label">Approx. Calories</span>
              <span id="tsc-builder-calories" class="tsc-metric-val" style="color: #67e8f9;">910 kcal</span>
            </div>
          </div>
          <div style="flex-basis: 100%; border-top: 1px solid #44403c; padding-top: 16px; margin-top: 10px;">
            <strong style="color: #a8a29e; display: block; font-size: 0.85rem; text-transform: uppercase;">Custom Sandwich Configuration:</strong>
            <p id="tsc-builder-summary" style="color: #ffffff; font-size: 1rem; margin-top: 4px;">Homemade Tarragon Chicken Salad with Aged White Cheddar and Herb Garlic Aioli on Triple-Stacked Toasted Wheat + Hardwood Smoked Bacon. Includes kettle chips and crisp deli pickle spear.</p>
          </div>
        </div>
      </div>
    </div>
"""

pages = {
    "index.html": ("Home", index_content),
    "menu.html": ("Full Menu", menu_content),
    "triple-decker-clubs-and-gourmet-melts.html": ("Clubs & Melts", clubs_content)
}

for filename, (label, content) in pages.items():
    html = wrap_page(label, filename, content)
    with open(os.path.join("the-sandwich-club", filename), "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"Generated {filename}")
