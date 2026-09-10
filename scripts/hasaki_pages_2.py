import os
from hasaki_core import wrap_page

sushi_content = """
    <div class="hasaki-container">
      <div class="hasaki-section-header">
        <span class="hasaki-badge">Craft Sushi Bar</span>
        <h1 class="hasaki-title">Specialty Sushi Rolls, Sashimi &amp; Poke</h1>
        <p class="hasaki-subtitle">Fresh sushi-grade Atlantic salmon, yellowfin tuna, sweet eel, and spicy crab rolled to order at 440 S Church St.</p>
      </div>

      <div class="hasaki-grid-2" style="align-items: center; margin-bottom: 48px;">
        <div>
          <span class="hasaki-badge hasaki-badge-wasabi">Fresh &amp; Flame-Kissed</span>
          <h2 class="hasaki-title" style="font-size: 2rem;">Chef-Inspired Roll Creations</h2>
          <p style="color: var(--hasaki-text-muted); font-size: 1.05rem; margin-bottom: 16px;">
            Whether craving warm baked rolls dripping in spicy crab and unagi sauce or cool fresh slices of sashimi over seasoned sushi rice, our sushi masters craft every piece with precision.
          </p>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 10px; font-size: 0.95rem; margin-bottom: 20px;">
            <li><strong>The Volcano Roll:</strong> Baked spicy crab and bay scallops over a California roll with tempura crunch.</li>
            <li><strong>Queen City Roll:</strong> Crispy shrimp tempura and cream cheese topped with spicy tuna and avocado.</li>
            <li><strong>Godzilla Crunch Roll:</strong> Panko-crusted deep fried roll with spicy salmon, cream cheese, and unagi drizzle.</li>
          </ul>
        </div>
        <div>
          <img src="images/chef-specialty-sushi-rolls.jpg" alt="Chef Specialty Sushi Rolls" style="width: 100%; border-radius: var(--hasaki-radius-lg); box-shadow: var(--hasaki-shadow-lg); border: 2px solid var(--hasaki-border);">
        </div>
      </div>

      <div class="hasaki-section-header">
        <h2 class="hasaki-title" style="font-size: 2rem;">Signature Roll Lineup</h2>
      </div>

      <div class="hasaki-grid-4">
        <div class="hasaki-card" style="padding: 20px;">
          <h3 style="font-family: var(--hasaki-font-display); font-size: 1.2rem; color: var(--hasaki-red); margin-bottom: 8px;">Volcano Roll</h3>
          <p style="font-size: 0.85rem; color: var(--hasaki-text-muted); margin-bottom: 10px;">Baked spicy crab, scallops, eel sauce, spicy mayo.</p>
          <span class="hasaki-card-price">$14.50</span>
        </div>
        <div class="hasaki-card" style="padding: 20px;">
          <h3 style="font-family: var(--hasaki-font-display); font-size: 1.2rem; color: var(--hasaki-red); margin-bottom: 8px;">Queen City Roll</h3>
          <p style="font-size: 0.85rem; color: var(--hasaki-text-muted); margin-bottom: 10px;">Shrimp tempura, cream cheese, spicy tuna, avocado.</p>
          <span class="hasaki-card-price">$14.95</span>
        </div>
        <div class="hasaki-card" style="padding: 20px;">
          <h3 style="font-family: var(--hasaki-font-display); font-size: 1.2rem; color: var(--hasaki-red); margin-bottom: 8px;">Dragon Roll</h3>
          <p style="font-size: 0.85rem; color: var(--hasaki-text-muted); margin-bottom: 10px;">Eel and cucumber inside, draped with ripe avocado.</p>
          <span class="hasaki-card-price">$13.95</span>
        </div>
        <div class="hasaki-card" style="padding: 20px;">
          <h3 style="font-family: var(--hasaki-font-display); font-size: 1.2rem; color: var(--hasaki-red); margin-bottom: 8px;">Rainbow Roll</h3>
          <p style="font-size: 0.85rem; color: var(--hasaki-text-muted); margin-bottom: 10px;">Tuna, salmon, yellowtail, and avocado over California roll.</p>
          <span class="hasaki-card-price">$14.50</span>
        </div>
      </div>
    </div>
"""

catering_content = """
    <div class="hasaki-container">
      <div class="hasaki-section-header">
        <span class="hasaki-badge">Corporate Catering</span>
        <h1 class="hasaki-title">Corporate Sushi Platters &amp; Hibachi Pans</h1>
        <p class="hasaki-subtitle">Feed your Uptown corporate team with grand chef sushi party trays, sizzling hibachi buffet pans, or individually labeled executive bento boxes.</p>
      </div>

      <div class="hasaki-grid-2" style="align-items: center; margin-bottom: 48px;">
        <div>
          <span class="hasaki-badge hasaki-badge-wasabi">Uptown Office Specialists</span>
          <h2 class="hasaki-title" style="font-size: 2rem;">Effortless Group Catering</h2>
          <p style="color: var(--hasaki-text-muted); font-size: 1.05rem; margin-bottom: 16px;">
            From bank tower team lunches to evening celebrations, Hasaki delivers freshly prepared Japanese cuisine with all necessary utensils, ginger, wasabi, and signature Yum Yum sauce.
          </p>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 8px; font-size: 0.9rem; color: var(--hasaki-slate);">
            <li>&bull; Grand Sushi Platters: 48 to 96-piece beautifully arranged party trays</li>
            <li>&bull; Hot Hibachi Buffet Trays: Stainless chaffing ready pans with fried rice &amp; proteins</li>
            <li>&bull; Individual Bento Boxes: Labeled and packed for fast boardroom meetings</li>
          </ul>
        </div>
        <div>
          <img src="images/grand-sushi-catering-platter.jpg" alt="Grand Sushi Catering Platter" style="width: 100%; border-radius: var(--hasaki-radius-lg); box-shadow: var(--hasaki-shadow-lg); border: 2px solid var(--hasaki-border);">
        </div>
      </div>

      <!-- Catering Calculator -->
      <div class="hasaki-builder-card">
        <div class="hasaki-section-header" style="margin-bottom: 24px;">
          <h2 class="hasaki-title" style="font-size: 1.8rem;">Corporate Catering Estimator</h2>
          <p class="hasaki-subtitle" style="font-size: 1rem;">Estimate your Japanese office catering package.</p>
        </div>

        <div class="hasaki-grid-3">
          <div>
            <label style="display: block; font-weight: 700; margin-bottom: 6px; color: var(--hasaki-slate);">Guest Count</label>
            <input type="number" id="hasaki-cat-guests" min="5" max="300" value="20" style="width: 100%; padding: 12px; border: 2px solid var(--hasaki-border); border-radius: var(--hasaki-radius); font-size: 1.1rem; font-weight: 700;">
          </div>
          <div>
            <label style="display: block; font-weight: 700; margin-bottom: 6px; color: var(--hasaki-slate);">Catering Package</label>
            <select id="hasaki-cat-tier" style="width: 100%; padding: 12px; border: 2px solid var(--hasaki-border); border-radius: var(--hasaki-radius); font-size: 1rem; font-weight: 700;">
              <option value="bento">Individual Executive Bento Boxes ($15.50/person)</option>
              <option value="hibachi-pans">Sizzling Hibachi Buffet Pans ($18.00/person)</option>
              <option value="sushi-grand">Grand Sushi &amp; Nigiri Platter Feast ($22.00/person)</option>
            </select>
          </div>
          <div>
            <label style="display: block; font-weight: 700; margin-bottom: 10px; color: var(--hasaki-slate);">Appetizer Add-On</label>
            <label style="display: flex; align-items: center; gap: 8px; font-weight: 600; cursor: pointer;">
              <input type="checkbox" id="hasaki-cat-gyoza" style="width: 20px; height: 20px;">
              <span>Include Pork Gyoza &amp; Edamame (+$3.50/person)</span>
            </label>
          </div>
        </div>

        <div class="hasaki-summary-panel">
          <div class="hasaki-summary-metrics">
            <div class="hasaki-metric-item">
              <span class="hasaki-metric-label">Estimated Invoice</span>
              <span id="hasaki-cat-total" class="hasaki-metric-val">$310.00</span>
            </div>
          </div>
          <div style="flex-basis: 100%; border-top: 1px solid #27272a; padding-top: 16px; margin-top: 10px;">
            <p id="hasaki-cat-summary" style="color: #d4d4d8; font-size: 0.95rem;">Corporate catering package for 20 guests. Includes authentic Japanese presentation, individual chopsticks, soy sauce packets, wasabi, pickled ginger, and Yum Yum sauce bottles.</p>
          </div>
          <div style="flex-basis: 100%; margin-top: 16px;">
            <a href="tel:9808199580" class="hasaki-btn hasaki-btn-primary">Call (980) 819-9580 to Book Catering</a>
          </div>
        </div>
      </div>
    </div>
"""

visit_content = """
    <div class="hasaki-container">
      <div class="hasaki-section-header">
        <span class="hasaki-badge">Location &amp; Access</span>
        <h1 class="hasaki-title">Visit Hasaki Grill &amp; Sushi</h1>
        <p class="hasaki-subtitle">Located on the first floor of the Ally Center at 440 S Church Street in Uptown Charlotte.</p>
      </div>

      <div class="hasaki-grid-2" style="margin-bottom: 40px;">
        <div class="hasaki-card" style="padding: 32px;">
          <h2 class="hasaki-card-title" style="font-size: 1.6rem; margin-bottom: 20px;">Restaurant Location</h2>
          
          <div style="margin-bottom: 20px;">
            <strong style="color: var(--hasaki-charcoal); display: block; font-size: 1.1rem;">Street Address</strong>
            <p style="color: var(--hasaki-text-muted); font-size: 1rem;">
              440 S Church St, Suite 104<br>
              Ally Center (1st Floor)<br>
              Charlotte, NC 28202
            </p>
          </div>

          <div style="margin-bottom: 20px;">
            <strong style="color: var(--hasaki-charcoal); display: block; font-size: 1.1rem;">Landmarks &amp; Transit</strong>
            <p style="color: var(--hasaki-text-muted); font-size: 0.95rem; line-height: 1.7;">
              Situated on S Church Street directly across from Romare Bearden Park and steps from Truist Field (Knights Stadium) and Bank of America Stadium. Accessible via LYNX 3rd St Station.
            </p>
          </div>

          <div style="margin-bottom: 20px;">
            <strong style="color: var(--hasaki-charcoal); display: block; font-size: 1.1rem;">Service Hours</strong>
            <p style="color: var(--hasaki-text-muted); font-size: 1rem;">
              <strong>Monday &ndash; Thursday:</strong> 11:00 AM &ndash; 9:00 PM<br>
              <strong>Friday &ndash; Saturday:</strong> 11:00 AM &ndash; 10:00 PM<br>
              <strong>Sunday:</strong> Closed
            </p>
          </div>
        </div>

        <div class="hasaki-card" style="padding: 32px;">
          <h2 class="hasaki-card-title" style="font-size: 1.6rem; margin-bottom: 20px;">Express Ordering &amp; Pickup</h2>

          <div style="margin-bottom: 24px;">
            <strong style="color: var(--hasaki-charcoal); display: block; font-size: 1.1rem;">Direct Phone Line</strong>
            <p style="color: var(--hasaki-text-muted); font-size: 0.95rem; margin-bottom: 12px;">
              Call ahead to have your sizzling hibachi combos and fresh sushi rolls boxed and ready for swift counter pickup:
            </p>
            <a href="tel:9808199580" class="hasaki-btn hasaki-btn-primary" style="display: inline-block;">Call (980) 819-9580</a>
          </div>

          <div style="background: #fff1f2; border: 1px solid var(--hasaki-border); padding: 18px; border-radius: var(--hasaki-radius);">
            <strong style="color: var(--hasaki-red); font-size: 1rem; display: block; margin-bottom: 4px;">Online Takeout &amp; Delivery</strong>
            <p style="color: #881337; font-size: 0.9rem;">
              Order directly via hasakigrill.com for rapid contactless pickup in the Ally Center lobby or desk delivery across Uptown.
            </p>
          </div>
        </div>
      </div>
    </div>
"""

pages = {
    "specialty-sushi-rolls-and-sashimi.html": ("Specialty Sushi", sushi_content),
    "corporate-catering-and-sushi-platters.html": ("Corporate Catering", catering_content),
    "visit.html": ("Visit & Location", visit_content)
}

for filename, (label, content) in pages.items():
    html = wrap_page(label, filename, content)
    with open(os.path.join("hasaki-grill-and-sushi", filename), "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"Generated {filename}")
