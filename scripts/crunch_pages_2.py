import os
from crunch_core import wrap_page

flatbreads_content = """
    <div class="crunch-container">
      <div class="crunch-section-header">
        <span class="crunch-badge">Oven Baked &amp; Pressed</span>
        <h1 class="crunch-title">Artisan Lavash Flatbreads &amp; Wraps</h1>
        <p class="crunch-subtitle">Ultra-crisp ancient grain lavash crusts and warm pressed whole wheat wraps made to order at 401 N Tryon.</p>
      </div>

      <div class="crunch-grid-2" style="align-items: center; margin-bottom: 48px;">
        <div>
          <span class="crunch-badge crunch-badge-lime">Crisp, Light &amp; Golden</span>
          <h2 class="crunch-title" style="font-size: 2rem;">Why Lavash Makes The Perfect Flatbread</h2>
          <p style="color: var(--crunch-text-muted); font-size: 1.05rem; margin-bottom: 16px;">
            Our Mediterranean lavash flatbreads offer a shatteringly crisp texture with fewer carbs and zero heavy dough. Topped with fresh local vegetables, hormone-free meats, and melted artisan cheeses, they bake in under four minutes.
          </p>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 10px; font-size: 0.95rem; margin-bottom: 20px;">
            <li><strong>Caprese Flatbread:</strong> Fresh mozzarella, sweet grape tomatoes, basil ribbons, and aged balsamic glaze.</li>
            <li><strong>Smoky BBQ Chicken:</strong> Herb chicken, smoked gouda, red onion, and tangy clean barbecue reduction.</li>
            <li><strong>Salad-to-Wrap Option:</strong> Prefer a handheld lunch? Any signature salad can be rolled into a warm whole wheat wrap!</li>
          </ul>
        </div>
        <div>
          <img src="images/artisan-lavash-flatbread.jpg" alt="Artisan Lavash Flatbread" style="width: 100%; border-radius: var(--crunch-radius-lg); box-shadow: var(--crunch-shadow-lg); border: 2px solid var(--crunch-border);">
        </div>
      </div>

      <div class="crunch-section-header">
        <h2 class="crunch-title" style="font-size: 2rem;">Featured Warm Wraps</h2>
      </div>

      <div class="crunch-grid-3">
        <div class="crunch-card" style="padding: 24px;">
          <h3 style="font-family: var(--crunch-font-display); font-size: 1.25rem; color: var(--crunch-emerald); margin-bottom: 8px;">Thai Peanut Crunch Wrap</h3>
          <p style="font-size: 0.9rem; color: var(--crunch-text-muted); margin-bottom: 12px;">Grilled chicken, shredded purple cabbage, edamame, carrots, crispy wontons, and Thai peanut sauce in a whole wheat wrap.</p>
          <span class="crunch-card-price">$11.75</span>
        </div>
        <div class="crunch-card" style="padding: 24px;">
          <h3 style="font-family: var(--crunch-font-display); font-size: 1.25rem; color: var(--crunch-emerald); margin-bottom: 8px;">Southwest Chipotle Wrap</h3>
          <p style="font-size: 0.9rem; color: var(--crunch-text-muted); margin-bottom: 12px;">Seared chicken, black beans, roasted corn, pepper jack, avocado, tortilla strips, and chipotle lime drizzle.</p>
          <span class="crunch-card-price">$11.95</span>
        </div>
        <div class="crunch-card" style="padding: 24px;">
          <h3 style="font-family: var(--crunch-font-display); font-size: 1.25rem; color: var(--crunch-emerald); margin-bottom: 8px;">Green Goddess Veggie Wrap</h3>
          <p style="font-size: 0.9rem; color: var(--crunch-text-muted); margin-bottom: 12px;">Organic kale, cucumber, Haas avocado, organic baked tofu, spiced chickpeas, and house creamy green goddess.</p>
          <span class="crunch-card-price">$11.25</span>
        </div>
      </div>
    </div>
"""

acai_catering_content = """
    <div class="crunch-container">
      <div class="crunch-section-header">
        <span class="crunch-badge crunch-badge-berry">Superfoods &amp; Catering</span>
        <h1 class="crunch-title">Organic Açaí Bowls &amp; Wellness Catering</h1>
        <p class="crunch-subtitle">Antioxidant-rich Brazilian açaí superfruit bowls and individually packaged healthy boxed lunches for Uptown corporate teams.</p>
      </div>

      <div class="crunch-grid-2" style="margin-bottom: 48px;">
        <div class="crunch-card" style="padding: 28px;">
          <span class="crunch-badge crunch-badge-berry" style="margin-bottom: 12px;">Superfruit Power</span>
          <h2 class="crunch-card-title" style="font-size: 1.5rem; margin-bottom: 12px;">Organic Brazilian Açaí</h2>
          <p style="color: var(--crunch-text-muted); font-size: 0.95rem; margin-bottom: 16px;">
            Pure organic açaí berries blended thick with frozen bananas for a creamy, dairy-free, antioxidant-dense bowl.
          </p>
          
          <!-- Interactive Acai Widget -->
          <div style="background: #fdf2f8; border: 1px solid #fbcfe8; padding: 20px; border-radius: var(--crunch-radius); margin-top: 16px;">
            <div style="margin-bottom: 12px;">
              <label style="display: block; font-weight: 700; font-size: 0.9rem; color: var(--crunch-charcoal); margin-bottom: 4px;">Bowl Size</label>
              <select id="crunch-acai-size" style="width: 100%; padding: 10px; border-radius: 6px; border: 1px solid #f472b6; font-weight: 700;">
                <option value="regular">Regular 16oz ($9.95)</option>
                <option value="large">Mega Superfood 24oz ($12.50)</option>
              </select>
            </div>
            <div style="margin-bottom: 14px;">
              <label style="display: block; font-weight: 700; font-size: 0.9rem; color: var(--crunch-charcoal); margin-bottom: 4px;">Superfood Drizzle</label>
              <select id="crunch-acai-drizzle" style="width: 100%; padding: 10px; border-radius: 6px; border: 1px solid #f472b6; font-weight: 700;">
                <option value="honey">Raw Local Wildflower Honey ($0.00)</option>
                <option value="almond-butter">Organic Creamy Almond Butter (+$1.50)</option>
                <option value="chia-maple">Chia Seed Pure Maple Drizzle ($0.00)</option>
              </select>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #fbcfe8; padding-top: 12px;">
              <div>
                <span style="font-size: 0.8rem; text-transform: uppercase; color: #9d174d;">Estimated Price</span>
                <div id="crunch-acai-total" style="font-family: var(--crunch-font-display); font-size: 1.4rem; font-weight: 800; color: var(--crunch-berry);">$9.95</div>
              </div>
              <a href="tel:9804985774" class="crunch-btn crunch-btn-berry" style="padding: 10px 18px; font-size: 0.9rem;">Call to Order</a>
            </div>
            <p id="crunch-acai-desc" style="font-size: 0.85rem; color: #831843; margin-top: 10px;">Pure organic Brazilian açaí puree blended thick with banana, layered with GF coconut granola, fresh strawberries, blueberries, chia seeds, and raw local honey.</p>
          </div>
        </div>

        <div class="crunch-card" style="padding: 28px;">
          <span class="crunch-badge crunch-badge-lime" style="margin-bottom: 12px;">Corporate Wellness</span>
          <h2 class="crunch-card-title" style="font-size: 1.5rem; margin-bottom: 12px;">Office Catering Packages</h2>
          <p style="color: var(--crunch-text-muted); font-size: 0.95rem; margin-bottom: 16px;">
            Fuel your team with clean energy that enhances afternoon focus without the carb crash.
          </p>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 8px; font-size: 0.9rem; color: var(--crunch-slate);">
            <li>&bull; Individual Chopped Salad &amp; Wrap Boxes with multigrain crisps</li>
            <li>&bull; Build-Your-Own Warm Quinoa &amp; Salad Bar Buffets</li>
            <li>&bull; Mini Açaí Superfood Parfait Cups for morning meetings</li>
            <li>&bull; Cold-Pressed Juice Gallons &amp; Herbal Iced Teas</li>
          </ul>
        </div>
      </div>

      <!-- Catering Calculator -->
      <div class="crunch-builder-card">
        <div class="crunch-section-header" style="margin-bottom: 24px;">
          <h2 class="crunch-title" style="font-size: 1.8rem;">Corporate Wellness Catering Estimator</h2>
          <p class="crunch-subtitle" style="font-size: 1rem;">Calculate an instant budget estimate for your next corporate meeting.</p>
        </div>

        <div class="crunch-grid-3">
          <div>
            <label style="display: block; font-weight: 700; margin-bottom: 6px; color: var(--crunch-slate);">Headcount</label>
            <input type="number" id="crunch-cat-guests" min="5" max="300" value="20" style="width: 100%; padding: 12px; border: 2px solid var(--crunch-border); border-radius: var(--crunch-radius); font-size: 1.1rem; font-weight: 700;">
          </div>
          <div>
            <label style="display: block; font-weight: 700; margin-bottom: 6px; color: var(--crunch-slate);">Catering Tier</label>
            <select id="crunch-cat-tier" style="width: 100%; padding: 12px; border: 2px solid var(--crunch-border); border-radius: var(--crunch-radius); font-size: 1rem; font-weight: 700;">
              <option value="box">Individual Salad / Wrap Bento Box ($14.50/person)</option>
              <option value="grain-bar">Build-Your-Own Quinoa &amp; Salad Buffet ($17.50/person)</option>
            </select>
          </div>
          <div>
            <label style="display: block; font-weight: 700; margin-bottom: 10px; color: var(--crunch-slate);">Dessert Superfood</label>
            <label style="display: flex; align-items: center; gap: 8px; font-weight: 600; cursor: pointer;">
              <input type="checkbox" id="crunch-cat-acai" style="width: 20px; height: 20px;">
              <span>Add Mini Açaí Parfait Cups (+$4.00/person)</span>
            </label>
          </div>
        </div>

        <div class="crunch-summary-panel">
          <div class="crunch-summary-metrics">
            <div class="crunch-metric-item">
              <span class="crunch-metric-label">Estimated Invoice</span>
              <span id="crunch-cat-total" class="crunch-metric-val">$290.00</span>
            </div>
          </div>
          <div style="flex-basis: 100%; border-top: 1px solid #334155; padding-top: 16px; margin-top: 10px;">
            <p id="crunch-cat-summary" style="color: #cbd5e1; font-size: 0.95rem;">Includes 20 wellness-focused customized portions with house-made scratch dressings, fresh multigrain crisps, disposable eco-friendly cutlery, and tower messenger delivery coordination.</p>
          </div>
          <div style="flex-basis: 100%; margin-top: 16px;">
            <a href="tel:9804985774" class="crunch-btn crunch-btn-primary">Call (980) 498-5774 to Book Catering</a>
          </div>
        </div>
      </div>
    </div>
"""

visit_content = """
    <div class="crunch-container">
      <div class="crunch-section-header">
        <span class="crunch-badge">Location &amp; Access</span>
        <h1 class="crunch-title">Visit Crunch Bistro</h1>
        <p class="crunch-subtitle">Located in Uptown Charlotte at 401 N Tryon Street for fast weekday lunch pickups, dine-in, and desk delivery.</p>
      </div>

      <div class="crunch-grid-2" style="margin-bottom: 40px;">
        <div class="crunch-card" style="padding: 32px;">
          <h2 class="crunch-card-title" style="font-size: 1.6rem; margin-bottom: 20px;">Restaurant Location</h2>
          
          <div style="margin-bottom: 20px;">
            <strong style="color: var(--crunch-charcoal); display: block; font-size: 1.1rem;">Street Address</strong>
            <p style="color: var(--crunch-text-muted); font-size: 1rem;">
              401 N Tryon St<br>
              Uptown Charlotte, NC 28202
            </p>
          </div>

          <div style="margin-bottom: 20px;">
            <strong style="color: var(--crunch-charcoal); display: block; font-size: 1.1rem;">Uptown Transit Access</strong>
            <p style="color: var(--crunch-text-muted); font-size: 0.95rem; line-height: 1.7;">
              Situated on N Tryon Street between 7th and 8th Streets. Short walk from the 7th St LYNX Blue Line Station and connected corporate tower breezeways.
            </p>
          </div>

          <div style="margin-bottom: 20px;">
            <strong style="color: var(--crunch-charcoal); display: block; font-size: 1.1rem;">Service Hours</strong>
            <p style="color: var(--crunch-text-muted); font-size: 1rem;">
              <strong>Monday &ndash; Friday:</strong> 10:00 AM &ndash; 3:30 PM<br>
              <strong>Saturday &ndash; Sunday:</strong> Closed
            </p>
          </div>
        </div>

        <div class="crunch-card" style="padding: 32px;">
          <h2 class="crunch-card-title" style="font-size: 1.6rem; margin-bottom: 20px;">Direct Orders &amp; Takeout</h2>

          <div style="margin-bottom: 24px;">
            <strong style="color: var(--crunch-charcoal); display: block; font-size: 1.1rem;">Phone Call-Ahead Line</strong>
            <p style="color: var(--crunch-text-muted); font-size: 0.95rem; margin-bottom: 12px;">
              Call our team to have your custom chopped salad or warm quinoa bowl freshly tossed and ready for express pickup:
            </p>
            <a href="tel:9804985774" class="crunch-btn crunch-btn-primary" style="display: inline-block;">Call (980) 498-5774</a>
          </div>

          <div style="background: #ecfdf5; border: 1px solid var(--crunch-border); padding: 18px; border-radius: var(--crunch-radius);">
            <strong style="color: var(--crunch-emerald-dark); font-size: 1rem; display: block; margin-bottom: 4px;">Online Takeout Ordering</strong>
            <p style="color: #065f46; font-size: 0.9rem;">
              Order directly via crunchbistro.com or Toast platform for contactless pickup or speedy delivery throughout Uptown Charlotte.
            </p>
          </div>
        </div>
      </div>
    </div>
"""

pages = {
    "artisan-lavash-flatbreads-and-wraps.html": ("Flatbreads & Wraps", flatbreads_content),
    "superfruit-acai-and-corporate-catering.html": ("Acai & Catering", acai_catering_content),
    "visit.html": ("Visit & Location", visit_content)
}

for filename, (label, content) in pages.items():
    html = wrap_page(label, filename, content)
    with open(os.path.join("crunch-bistro", filename), "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"Generated {filename}")
