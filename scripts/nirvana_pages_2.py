import os
from nirvana_core import wrap_page

curries_content = """
    <div class="nirvana-container">
      <div class="nirvana-section-header">
        <span class="nirvana-badge">Traditional Mastery</span>
        <h1 class="nirvana-title">Tandoori Curries &amp; Vegetarian Classics</h1>
        <p class="nirvana-subtitle">Slow-simmered sauces, tandoori marinades, and fresh vegetarian culinary traditions crafted daily at 401 S Tryon St.</p>
      </div>

      <div class="nirvana-grid-2" style="margin-bottom: 48px;">
        <div class="nirvana-card" style="padding: 28px;">
          <h2 class="nirvana-card-title" style="font-size: 1.5rem; margin-bottom: 16px;">Tandoori &amp; Non-Veg Curries</h2>
          
          <div style="margin-bottom: 18px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.05rem;">
              <span style="color: var(--nirvana-charcoal);">Chicken Tikka Masala</span>
              <span style="color: var(--nirvana-crimson);">$14.50</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--nirvana-muted);">Marinated boneless chicken cubes skewered in tandoor, then finished in a silky tomato fenugreek cream reduction.</p>
          </div>

          <div style="margin-bottom: 18px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.05rem;">
              <span style="color: var(--nirvana-charcoal);">Butter Chicken (Murgh Makhani)</span>
              <span style="color: var(--nirvana-crimson);">$14.50</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--nirvana-muted);">A Delhi classic. Shredded tender chicken simmered with rich butter, cashew paste, and aromatic cinnamon.</p>
          </div>

          <div style="margin-bottom: 18px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.05rem;">
              <span style="color: var(--nirvana-charcoal);">Lamb Rogan Josh</span>
              <span style="color: var(--nirvana-crimson);">$16.95</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--nirvana-muted);">Tender boneless lamb slow-cooked with aromatic whole spices, yogurt, Kashmiri chili, and ginger.</p>
          </div>

          <div>
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.05rem;">
              <span style="color: var(--nirvana-charcoal);">Chicken Korma</span>
              <span style="color: var(--nirvana-crimson);">$14.50</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--nirvana-muted);">Mild and creamy almond-cashew sauce delicately seasoned with green cardamom and saffron.</p>
          </div>
        </div>

        <div class="nirvana-card" style="padding: 28px;">
          <h2 class="nirvana-card-title" style="font-size: 1.5rem; margin-bottom: 16px;">Pure Vegetarian &amp; Vegan Fare</h2>

          <div style="margin-bottom: 18px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.05rem;">
              <span style="color: var(--nirvana-charcoal);">Saag Paneer</span>
              <span style="color: var(--nirvana-crimson);">$13.50</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--nirvana-muted);">Creamed fresh spinach, mustard greens, and homemade Indian paneer cheese cubes lightly spiced.</p>
          </div>

          <div style="margin-bottom: 18px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.05rem;">
              <span style="color: var(--nirvana-charcoal);">Chana Masala (Vegan)</span>
              <span style="color: var(--nirvana-crimson);">$12.50</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--nirvana-muted);">Organic chickpeas simmered with crushed tomatoes, ginger root, amchoor dried mango, and coriander.</p>
          </div>

          <div style="margin-bottom: 18px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.05rem;">
              <span style="color: var(--nirvana-charcoal);">Dal Makhani</span>
              <span style="color: var(--nirvana-crimson);">$12.50</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--nirvana-muted);">Black urad lentils and kidney beans slow simmered with creamy butter, garlic, and plum tomatoes.</p>
          </div>

          <div>
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.05rem;">
              <span style="color: var(--nirvana-charcoal);">Aloo Gobi (Vegan)</span>
              <span style="color: var(--nirvana-crimson);">$12.50</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--nirvana-muted);">Fresh cauliflower florets and tender potatoes pan-roasted with turmeric, cumin seeds, and fresh cilantro.</p>
          </div>
        </div>
      </div>

      <!-- Spice Meter -->
      <div class="nirvana-info-box">
        <h3 style="font-family: var(--nirvana-font-display); color: var(--nirvana-crimson); font-size: 1.6rem; margin-bottom: 8px;">Our Spice Intensity Scale</h3>
        <p style="color: var(--nirvana-muted); font-size: 0.95rem; margin-bottom: 24px;">All curries are customized to your exact heat preference upon ordering.</p>
        
        <div class="nirvana-grid-4">
          <div style="background: #fffbeb; border: 1px solid var(--nirvana-border); padding: 18px; border-radius: var(--nirvana-radius);">
            <strong style="color: var(--nirvana-saffron-dark); font-size: 1.1rem; display: block; margin-bottom: 4px;">Level 1: Mild</strong>
            <p style="font-size: 0.85rem; color: var(--nirvana-muted);">Rich aromatic spices without heat. Smooth, sweet cream and gentle cumin notes.</p>
          </div>
          <div style="background: #fffbeb; border: 1px solid var(--nirvana-border); padding: 18px; border-radius: var(--nirvana-radius);">
            <strong style="color: var(--nirvana-saffron-dark); font-size: 1.1rem; display: block; margin-bottom: 4px;">Level 2: Medium</strong>
            <p style="font-size: 0.85rem; color: var(--nirvana-muted);">Balanced warmth with gentle green chili and black pepper. The authentic crowd favorite.</p>
          </div>
          <div style="background: #fffbeb; border: 1px solid var(--nirvana-border); padding: 18px; border-radius: var(--nirvana-radius);">
            <strong style="color: var(--nirvana-crimson); font-size: 1.1rem; display: block; margin-bottom: 4px;">Level 3: Indian Hot</strong>
            <p style="font-size: 0.85rem; color: var(--nirvana-muted);">Authentic subcontinental spice level with Kashmiri red chili and toasted cloves.</p>
          </div>
          <div style="background: #fee2e2; border: 1px solid #fecaca; padding: 18px; border-radius: var(--nirvana-radius);">
            <strong style="color: var(--nirvana-crimson-dark); font-size: 1.1rem; display: block; margin-bottom: 4px;">Level 4: Desi Fire</strong>
            <p style="font-size: 0.85rem; color: #7f1d1d;">For true spice aficionados. Fresh bird's eye chilies and habanero-infused curry gravy.</p>
          </div>
        </div>
      </div>
    </div>
"""

catering_content = """
    <div class="nirvana-container">
      <div class="nirvana-section-header">
        <span class="nirvana-badge">Corporate Catering</span>
        <h1 class="nirvana-title">Corporate Indian Catering &amp; Lunch Boxes</h1>
        <p class="nirvana-subtitle">Full-service buffet chaffing setups or individually packaged executive thali bento boxes delivered across Uptown Charlotte.</p>
      </div>

      <div class="nirvana-grid-2" style="align-items: center; margin-bottom: 48px;">
        <div>
          <span class="nirvana-badge nirvana-badge-crimson">Uptown Office Specialists</span>
          <h2 class="nirvana-title" style="font-size: 2rem;">Seamless Catering For Banking &amp; Corporate Teams</h2>
          <p style="color: var(--nirvana-muted); font-size: 1.05rem; margin-bottom: 16px;">
            From board meetings on S Tryon to office-wide quarterly celebrations, Nirvana II delivers authentic Indian cuisine that caters seamlessly to diverse dietary preferences (Halal, Vegetarian, Vegan, Gluten-Conscious).
          </p>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 10px; font-size: 0.95rem; margin-bottom: 20px;">
            <li><strong>Individually Labeled Boxes:</strong> Eliminate buffet mess with custom name-tagged thali meal containers.</li>
            <li><strong>Chaffing Pan Buffets:</strong> Full stainless chafing racks and sternos provided for warm team self-service.</li>
            <li><strong>Fresh Tandoor Naan Guarantee:</strong> Breads baked immediately prior to your scheduled delivery window.</li>
          </ul>
        </div>
        <div>
          <img src="images/fresh-garlic-naan-samosa.jpg" alt="Garlic Naan and Samosas" style="width: 100%; border-radius: var(--nirvana-radius-lg); box-shadow: var(--nirvana-shadow-lg); border: 2px solid var(--nirvana-border);">
        </div>
      </div>

      <!-- Catering Calculator -->
      <div class="nirvana-builder-card">
        <div class="nirvana-section-header" style="margin-bottom: 24px;">
          <h2 class="nirvana-title" style="font-size: 1.8rem;">Catering Package Estimator</h2>
          <p class="nirvana-subtitle" style="font-size: 1rem;">Select your headcount and desired presentation style for an instant estimate.</p>
        </div>

        <div class="nirvana-grid-3">
          <div>
            <label style="display: block; font-weight: 700; margin-bottom: 6px; color: var(--nirvana-slate);">Guest Count</label>
            <input type="number" id="nirvana-cat-guests" min="10" max="300" value="25" style="width: 100%; padding: 12px; border: 2px solid var(--nirvana-border); border-radius: var(--nirvana-radius); font-size: 1.1rem; font-weight: 700;">
          </div>
          <div>
            <label style="display: block; font-weight: 700; margin-bottom: 6px; color: var(--nirvana-slate);">Package Tier</label>
            <select id="nirvana-cat-tier" style="width: 100%; padding: 12px; border: 2px solid var(--nirvana-border); border-radius: var(--nirvana-radius); font-size: 1rem; font-weight: 700;">
              <option value="box">Individual Executive Thali Boxes ($15.00/person)</option>
              <option value="buffet-silver">Silver Buffet (2 Curries + Naan + Samosas) ($18.50/person)</option>
              <option value="buffet-gold">Gold Feast (3 Curries + Dum Biryani + Naan + Dessert) ($22.00/person)</option>
            </select>
          </div>
          <div>
            <label style="display: block; font-weight: 700; margin-bottom: 10px; color: var(--nirvana-slate);">Drink Addition</label>
            <label style="display: flex; align-items: center; gap: 8px; font-weight: 600; cursor: pointer;">
              <input type="checkbox" id="nirvana-cat-drink" style="width: 20px; height: 20px;">
              <span>Include Mango Lassi Smoothies (+$3.50/person)</span>
            </label>
          </div>
        </div>

        <div class="nirvana-summary-panel">
          <div class="nirvana-summary-metrics">
            <div class="nirvana-metric-item">
              <span class="nirvana-metric-label">Estimated Total</span>
              <span id="nirvana-cat-total" class="nirvana-metric-val">$375.00</span>
            </div>
          </div>
          <div style="flex-basis: 100%; border-top: 1px solid #3f3f46; padding-top: 16px; margin-top: 10px;">
            <p id="nirvana-cat-summary" style="color: #d4d4d8; font-size: 0.95rem;">Estimated catering package for 25 guests. Includes warm chaffing setups or individual labeled bento containers, fresh baked naan, rice, chutneys, and disposable cutlery.</p>
          </div>
          <div style="flex-basis: 100%; margin-top: 16px;">
            <a href="tel:9802907002" class="nirvana-btn nirvana-btn-primary">Call (980) 290-7002 to Book Catering</a>
          </div>
        </div>
      </div>
    </div>
"""

visit_content = """
    <div class="nirvana-container">
      <div class="nirvana-section-header">
        <span class="nirvana-badge">Location &amp; Access</span>
        <h1 class="nirvana-title">Visit Nirvana II</h1>
        <p class="nirvana-subtitle">Conveniently positioned on S Tryon St in Uptown Charlotte for fast weekday lunch pickups, dine-in, and delivery.</p>
      </div>

      <div class="nirvana-grid-2" style="margin-bottom: 40px;">
        <div class="nirvana-card" style="padding: 32px;">
          <h2 class="nirvana-card-title" style="font-size: 1.6rem; margin-bottom: 20px;">Restaurant Information</h2>
          
          <div style="margin-bottom: 20px;">
            <strong style="color: var(--nirvana-charcoal); display: block; font-size: 1.1rem;">Address</strong>
            <p style="color: var(--nirvana-muted); font-size: 1rem;">
              401 S Tryon St<br>
              Uptown Charlotte, NC 28202
            </p>
          </div>

          <div style="margin-bottom: 20px;">
            <strong style="color: var(--nirvana-charcoal); display: block; font-size: 1.1rem;">Transit &amp; Parking</strong>
            <p style="color: var(--nirvana-muted); font-size: 0.95rem; line-height: 1.7;">
              Steps from the LYNX Blue Line 3rd St / Convention Center station and connected to the Overstreet Mall skywalk network. Validated parking decks and quick-turn pickup spaces available nearby.
            </p>
          </div>

          <div style="margin-bottom: 20px;">
            <strong style="color: var(--nirvana-charcoal); display: block; font-size: 1.1rem;">Service Hours</strong>
            <p style="color: var(--nirvana-muted); font-size: 1rem;">
              <strong>Monday &ndash; Friday:</strong> 11:30 AM &ndash; 3:30 PM<br>
              <strong>Saturday &ndash; Sunday:</strong> Closed
            </p>
          </div>
        </div>

        <div class="nirvana-card" style="padding: 32px;">
          <h2 class="nirvana-card-title" style="font-size: 1.6rem; margin-bottom: 20px;">Express Takeout &amp; Phone Orders</h2>

          <div style="margin-bottom: 24px;">
            <strong style="color: var(--nirvana-charcoal); display: block; font-size: 1.1rem;">Direct Line for Call-Ahead Pickup</strong>
            <p style="color: var(--nirvana-muted); font-size: 0.95rem; margin-bottom: 12px;">
              Call ahead to have your butter chicken, dum biryanis, and fresh garlic naans hot and packed for quick counter pickup:
            </p>
            <a href="tel:9802907002" class="nirvana-btn nirvana-btn-crimson" style="display: inline-block;">Call (980) 290-7002</a>
          </div>

          <div style="background: #fef3c7; border: 1px solid var(--nirvana-border); padding: 18px; border-radius: var(--nirvana-radius);">
            <strong style="color: var(--nirvana-saffron-dark); font-size: 1rem; display: block; margin-bottom: 4px;">Online Delivery Platforms</strong>
            <p style="color: #78350f; font-size: 0.9rem;">
              Order directly for desk delivery across Uptown Charlotte via Uber Eats, Postmates, and official ordering portals.
            </p>
          </div>
        </div>
      </div>
    </div>
"""

pages = {
    "tandoori-curries-and-vegetarian-classics.html": ("Curries & Tandoor", curries_content),
    "corporate-catering-and-lunch-boxes.html": ("Corporate Catering", catering_content),
    "visit.html": ("Visit & Location", visit_content)
}

for filename, (label, content) in pages.items():
    html = wrap_page(label, filename, content)
    with open(os.path.join("nirvana-ii", filename), "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"Generated {filename}")
