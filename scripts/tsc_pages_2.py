import os
from tsc_core import wrap_page

breakfast_content = """
    <div class="tsc-container">
      <div class="tsc-section-header">
        <span class="tsc-badge tsc-badge-mustard">Served 7:00 AM &ndash; 10:30 AM</span>
        <h1 class="tsc-title">Morning Breakfast &amp; Biscuit Bar</h1>
        <p class="tsc-subtitle">Fueling Uptown Charlotte early risers with scratch buttermilk biscuits, buttery croissant egg melts, breakfast burritos, and freshly brewed coffee.</p>
      </div>

      <div class="tsc-grid-2" style="align-items: center; margin-bottom: 48px;">
        <div>
          <span class="tsc-badge tsc-badge-green">Early Morning Rush Ready</span>
          <h2 class="tsc-title" style="font-size: 2rem;">Scratch Biscuits &amp; Flaky Croissants</h2>
          <p style="color: var(--tsc-text-muted); font-size: 1.05rem; margin-bottom: 16px;">
            Starting at 7:00 AM every weekday morning, our griddle fires up to prepare hot made-to-order breakfast sandwiches. Whether you're heading to the office tower or walking through The Green, grab a hearty hot breakfast in minutes.
          </p>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 10px; font-size: 0.95rem; margin-bottom: 20px;">
            <li><strong>Scratch Southern Biscuits:</strong> Baked golden brown, split and griddled with eggs, sharp cheddar, bacon, or sausage.</li>
            <li><strong>Gourmet Croissant Melts:</strong> Two eggs folded with French brie, hardwood bacon, and baby spinach.</li>
            <li><strong>Hearty Breakfast Burritos:</strong> Packed with scrambled eggs, cheddar, black beans, chorizo, and fresh salsa.</li>
          </ul>
        </div>
        <div>
          <img src="images/breakfast-biscuit-egg-bacon.jpg" alt="Breakfast Biscuit with Egg and Bacon" style="width: 100%; border-radius: var(--tsc-radius-lg); box-shadow: var(--tsc-shadow-lg); border: 2px solid var(--tsc-border);">
        </div>
      </div>

      <!-- Breakfast Calculator -->
      <div class="tsc-builder-card">
        <div class="tsc-section-header" style="margin-bottom: 24px;">
          <h2 class="tsc-title" style="font-size: 1.8rem;">Breakfast Group &amp; Individual Estimator</h2>
          <p class="tsc-subtitle" style="font-size: 1rem;">Order ahead for your morning team meeting at 435 S Tryon.</p>
        </div>

        <div class="tsc-grid-3">
          <div>
            <label style="display: block; font-weight: 700; margin-bottom: 6px; color: var(--tsc-slate);">Quantity</label>
            <input type="number" id="tsc-bk-qty" min="1" max="50" value="6" style="width: 100%; padding: 12px; border: 2px solid var(--tsc-border); border-radius: var(--tsc-radius); font-size: 1.1rem; font-weight: 700;">
          </div>
          <div>
            <label style="display: block; font-weight: 700; margin-bottom: 6px; color: var(--tsc-slate);">Breakfast Specialty</label>
            <select id="tsc-bk-item" style="width: 100%; padding: 12px; border: 2px solid var(--tsc-border); border-radius: var(--tsc-radius); font-size: 1rem; font-weight: 700;">
              <option value="biscuit">Buttermilk Biscuit Sandwich ($5.95)</option>
              <option value="croissant">Croissant Egg &amp; Brie Melt ($7.25)</option>
              <option value="burrito">Uptown Breakfast Burrito ($7.95)</option>
            </select>
          </div>
          <div>
            <label style="display: block; font-weight: 700; margin-bottom: 10px; color: var(--tsc-slate);">Coffee Addition</label>
            <label style="display: flex; align-items: center; gap: 8px; font-weight: 600; cursor: pointer;">
              <input type="checkbox" id="tsc-bk-coffee" style="width: 20px; height: 20px;">
              <span>Add Colombian Drip Coffee (+$2.75/ea)</span>
            </label>
          </div>
        </div>

        <div class="tsc-summary-panel">
          <div class="tsc-summary-metrics">
            <div class="tsc-metric-item">
              <span class="tsc-metric-label">Estimated Total</span>
              <span id="tsc-bk-total" class="tsc-metric-val">$35.70</span>
            </div>
          </div>
          <div style="flex-basis: 100%; border-top: 1px solid #44403c; padding-top: 16px; margin-top: 10px;">
            <p id="tsc-bk-desc" style="color: #d6d3d1; font-size: 0.95rem;">Order includes 6 freshly grilled breakfast portions served piping hot from our 7:00 AM weekday kitchen at 435 S Tryon St.</p>
          </div>
          <div style="flex-basis: 100%; margin-top: 16px;">
            <a href="tel:7043441975" class="tsc-btn tsc-btn-primary">Call (704) 344-1975 for Express Morning Pickup</a>
          </div>
        </div>
      </div>
    </div>
"""

catering_content = """
    <div class="tsc-container">
      <div class="tsc-section-header">
        <span class="tsc-badge">Corporate Catering</span>
        <h1 class="tsc-title">Corporate Boxed Lunches &amp; Party Platters</h1>
        <p class="tsc-subtitle">Individually labeled gourmet boxed lunches and beautifully arranged sandwich platters delivered right to your Uptown corporate office.</p>
      </div>

      <div class="tsc-grid-2" style="margin-bottom: 48px;">
        <div class="tsc-card" style="padding: 28px;">
          <span class="tsc-badge tsc-badge-burgundy" style="margin-bottom: 12px;">Top Corporate Choice</span>
          <h2 class="tsc-card-title" style="font-size: 1.5rem; margin-bottom: 12px;">Classic Boxed Lunches</h2>
          <p style="color: var(--tsc-text-muted); font-size: 0.95rem; margin-bottom: 16px;">
            Each individual box is neatly labeled with the recipient's name and sandwich choice for effortless distribution in boardrooms and meeting spaces.
          </p>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 8px; font-size: 0.9rem; color: var(--tsc-slate);">
            <li>&bull; Choice of signature sandwich, wrap, or triple-stack club</li>
            <li>&bull; Bag of gourmet Dirty kettle chips</li>
            <li>&bull; Locally baked Sweet Girl gourmet cookie</li>
            <li>&bull; Whole crisp deli garlic dill pickle spear</li>
            <li>&bull; Napkin, wet wipe, and wrapped mint</li>
          </ul>
        </div>

        <div class="tsc-card" style="padding: 28px;">
          <span class="tsc-badge tsc-badge-green" style="margin-bottom: 12px;">Buffet Style</span>
          <h2 class="tsc-card-title" style="font-size: 1.5rem; margin-bottom: 12px;">Executive Sandwich Platters</h2>
          <p style="color: var(--tsc-text-muted); font-size: 0.95rem; margin-bottom: 16px;">
            Artfully garnished platters of assorted halved specialty sandwiches and pinwheel wraps served with bulk chip baskets and deli salads.
          </p>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 8px; font-size: 0.9rem; color: var(--tsc-slate);">
            <li>&bull; Assortment: The Club, Grand Brie, Gobbler, Italian, Roast Beef</li>
            <li>&bull; Side salads: Red bliss potato salad, pasta salad, or fruit bowl</li>
            <li>&bull; Cookie &amp; brownie dessert platters</li>
            <li>&bull; Gallons of fresh Southern sweet tea and lemonade</li>
          </ul>
        </div>
      </div>

      <!-- Catering Calculator -->
      <div class="tsc-builder-card">
        <div class="tsc-section-header" style="margin-bottom: 24px;">
          <h2 class="tsc-title" style="font-size: 1.8rem;">Corporate Catering Estimator</h2>
          <p class="tsc-subtitle" style="font-size: 1rem;">Estimate your office catering order for seamless tower delivery.</p>
        </div>

        <div class="tsc-grid-3">
          <div>
            <label style="display: block; font-weight: 700; margin-bottom: 6px; color: var(--tsc-slate);">Guest Count</label>
            <input type="number" id="tsc-cat-guests" min="5" max="300" value="20" style="width: 100%; padding: 12px; border: 2px solid var(--tsc-border); border-radius: var(--tsc-radius); font-size: 1.1rem; font-weight: 700;">
          </div>
          <div>
            <label style="display: block; font-weight: 700; margin-bottom: 6px; color: var(--tsc-slate);">Catering Format</label>
            <select id="tsc-cat-tier" style="width: 100%; padding: 12px; border: 2px solid var(--tsc-border); border-radius: var(--tsc-radius); font-size: 1rem; font-weight: 700;">
              <option value="classic">Classic Boxed Lunch ($14.50/person)</option>
              <option value="deluxe">Deluxe Box with Gourmet Side Salad ($17.00/person)</option>
            </select>
          </div>
          <div>
            <label style="display: block; font-weight: 700; margin-bottom: 10px; color: var(--tsc-slate);">Beverage Add-On</label>
            <label style="display: flex; align-items: center; gap: 8px; font-weight: 600; cursor: pointer;">
              <input type="checkbox" id="tsc-cat-drinks" style="width: 20px; height: 20px;">
              <span>Include Sweet Tea &amp; Lemonade ($2.50/person)</span>
            </label>
          </div>
        </div>

        <div class="tsc-summary-panel">
          <div class="tsc-summary-metrics">
            <div class="tsc-metric-item">
              <span class="tsc-metric-label">Estimated Invoice</span>
              <span id="tsc-cat-total" class="tsc-metric-val">$290.00</span>
            </div>
          </div>
          <div style="flex-basis: 100%; border-top: 1px solid #44403c; padding-top: 16px; margin-top: 10px;">
            <p id="tsc-cat-summary" style="color: #d6d3d1; font-size: 0.95rem;">Includes 20 individually labeled custom deli boxed lunches with signature sandwiches, gourmet chips, homemade Sweet Girl cookies, dill pickle spears, napkins, and cutlery.</p>
          </div>
          <div style="flex-basis: 100%; margin-top: 16px;">
            <a href="tel:7043441975" class="tsc-btn tsc-btn-primary">Call (704) 344-1975 to Book Office Catering</a>
          </div>
        </div>
      </div>
    </div>
"""

visit_content = """
    <div class="tsc-container">
      <div class="tsc-section-header">
        <span class="tsc-badge">Location &amp; Hours</span>
        <h1 class="tsc-title">Visit The Sandwich Club</h1>
        <p class="tsc-subtitle">Located in the vibrant heart of Uptown Charlotte at 435 S Tryon Street, directly across from The Green pocket park.</p>
      </div>

      <div class="tsc-grid-2" style="margin-bottom: 40px;">
        <div class="tsc-card" style="padding: 32px;">
          <h2 class="tsc-card-title" style="font-size: 1.6rem; margin-bottom: 20px;">Deli Location &amp; Landmarks</h2>
          
          <div style="margin-bottom: 20px;">
            <strong style="color: var(--tsc-charcoal); display: block; font-size: 1.1rem;">Street Address</strong>
            <p style="color: var(--tsc-text-muted); font-size: 1rem;">
              435 S Tryon St<br>
              Uptown Charlotte, NC 28202
            </p>
          </div>

          <div style="margin-bottom: 20px;">
            <strong style="color: var(--tsc-charcoal); display: block; font-size: 1.1rem;">Surrounding Landmarks</strong>
            <p style="color: var(--tsc-text-muted); font-size: 0.95rem; line-height: 1.7;">
              Situated between Levine Avenue of the Arts and MLK Jr Blvd. Directly opposite The Green pocket park, the Ratcliffe condominiums, and steps away from the Mint Museum and Bechtler Museum of Modern Art.
            </p>
          </div>

          <div style="margin-bottom: 20px;">
            <strong style="color: var(--tsc-charcoal); display: block; font-size: 1.1rem;">Service Hours</strong>
            <p style="color: var(--tsc-text-muted); font-size: 1rem;">
              <strong>Monday &ndash; Friday:</strong> 7:00 AM &ndash; 3:00 PM<br>
              <strong>Breakfast:</strong> 7:00 AM &ndash; 10:30 AM<br>
              <strong>Lunch:</strong> 10:30 AM &ndash; 3:00 PM<br>
              <strong>Saturday &ndash; Sunday:</strong> Closed
            </p>
          </div>
        </div>

        <div class="tsc-card" style="padding: 32px;">
          <h2 class="tsc-card-title" style="font-size: 1.6rem; margin-bottom: 20px;">Fast Ordering &amp; Pickup Options</h2>

          <div style="margin-bottom: 24px;">
            <strong style="color: var(--tsc-charcoal); display: block; font-size: 1.1rem;">Phone Call-Ahead Ordering</strong>
            <p style="color: var(--tsc-text-muted); font-size: 0.95rem; margin-bottom: 12px;">
              Avoid the peak lunch rush line by calling ahead directly to our counter:
            </p>
            <a href="tel:7043441975" class="tsc-btn tsc-btn-primary" style="display: inline-block;">Call (704) 344-1975</a>
          </div>

          <div style="background: #ffe4e6; border: 1px solid #fecdd3; padding: 18px; border-radius: var(--tsc-radius);">
            <strong style="color: var(--tsc-burgundy); font-size: 1rem; display: block; margin-bottom: 4px;">Online Takeout &amp; Catering</strong>
            <p style="color: #4c0519; font-size: 0.9rem;">
              Order directly through sandwichclub2go.com or delivery services for quick desk delivery throughout Uptown corporate towers.
            </p>
          </div>
        </div>
      </div>
    </div>
"""

pages = {
    "morning-breakfast-and-biscuit-bar.html": ("Breakfast & Biscuits", breakfast_content),
    "corporate-lunch-boxes-and-platters.html": ("Corporate Catering", catering_content),
    "visit.html": ("Visit & Location", visit_content)
}

for filename, (label, content) in pages.items():
    html = wrap_page(label, filename, content)
    with open(os.path.join("the-sandwich-club", filename), "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"Generated {filename}")
