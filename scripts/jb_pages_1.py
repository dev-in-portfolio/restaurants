import os
from jb_core import wrap_page

index_content = """
    <section class="jb-hero">
      <div class="jb-hero-content">
        <span class="jb-badge jb-badge-lime">Two Wells Fargo Concourse &bull; Est. 1998</span>
        <h1 class="jb-hero-title">Uptown Charlotte's Legendary <span>Burrito Bar</span></h1>
        <p class="jb-hero-lead">Subterranean speed, massive custom burritos, five scratch salsas, and the city's most beloved Tuesday &amp; Friday tamale tradition.</p>
        <div class="jb-hero-actions">
          <a href="menu.html" class="jb-btn jb-btn-primary">View Concourse Menu</a>
          <a href="famous-burritos-and-bowls.html" class="jb-btn jb-btn-secondary">Build Your Burrito</a>
          <a href="tuesday-friday-tamale-tradition.html" class="jb-btn jb-btn-lime">Tamale Special Days</a>
        </div>
        <div class="jb-hero-highlights">
          <div class="jb-highlight-box">
            <div class="jb-highlight-title">Walk The Line</div>
            <div class="jb-highlight-desc">Custom assemble your 12-inch or Big Burrito in under 90 seconds.</div>
          </div>
          <div class="jb-highlight-box">
            <div class="jb-highlight-title">Tamale Tue &amp; Fri</div>
            <div class="jb-highlight-desc">Steamed in real corn husks. Get here before 1:30 PM before sellout.</div>
          </div>
          <div class="jb-highlight-box">
            <div class="jb-highlight-title">5-Tier Salsa Bar</div>
            <div class="jb-highlight-desc">Scratch-made daily from fresh Pico de Gallo to fiery El Diablo.</div>
          </div>
          <div class="jb-highlight-box">
            <div class="jb-highlight-title">Cash-Eesh Perks</div>
            <div class="jb-highlight-desc">Express cash discount honored on all concourse counter tickets.</div>
          </div>
        </div>
      </div>
    </section>

    <div class="jb-container">
      <div class="jb-tamale-alert-banner">
        <div>
          <div class="jb-tamale-alert-title">Tuesday &amp; Friday Tamale Alert</div>
          <div class="jb-tamale-alert-desc">Freshly steamed homemade chicken verde, picadillo beef, smoked BBQ pork, and sweet corn vegetarian tamales. Early lunch arrival recommended!</div>
        </div>
        <a href="tuesday-friday-tamale-tradition.html" class="jb-btn jb-btn-primary">Learn About Tamale Days &rarr;</a>
      </div>

      <section class="jb-section">
        <div class="jb-section-header">
          <span class="jb-badge">Concourse Staples</span>
          <h2 class="jb-title">Fast, Flavorful, Fuel for Uptown</h2>
          <p class="jb-subtitle">Whether rushing between board meetings in Two Wells Fargo or grabbing an express office lunch, Johnny delivers unbeatable flavor and value.</p>
        </div>

        <div class="jb-grid-3">
          <div class="jb-card">
            <div class="jb-card-img-wrap">
              <img src="images/massive-california-burrito.jpg" alt="Massive California Burrito" class="jb-card-img">
              <span class="jb-card-tag">Signature</span>
            </div>
            <div class="jb-card-body">
              <div class="jb-card-header">
                <h3 class="jb-card-title">California Burrito</h3>
                <span class="jb-card-price">$9.75+</span>
              </div>
              <p class="jb-card-desc">Warm pressed tortilla stuffed with seasoned chicken, flank steak, or picadillo beef, cilantro-lime rice, black beans, Monterey Jack, and your choice of fresh salsa.</p>
              <div class="jb-card-meta">
                <span class="jb-meta-pill">Flour / Wheat / Spinach</span>
                <span class="jb-meta-pill">Regular or Big Size</span>
              </div>
              <a href="famous-burritos-and-bowls.html" class="jb-btn jb-btn-primary" style="text-align: center; width: 100%;">Customize Online</a>
            </div>
          </div>

          <div class="jb-card">
            <div class="jb-card-img-wrap">
              <img src="images/scratch-homemade-tamales.jpg" alt="Scratch Homemade Tamales" class="jb-card-img">
              <span class="jb-card-tag">Tue &amp; Fri Only</span>
            </div>
            <div class="jb-card-body">
              <div class="jb-card-header">
                <h3 class="jb-card-title">Scratch Tamales</h3>
                <span class="jb-card-price">$3.95 ea</span>
              </div>
              <p class="jb-card-desc">Hand-rolled in real corn husks, steamed piping hot twice a week. Four rotating fillings including chicken salsa verde, tender beef, smoked pork, and veggie squash.</p>
              <div class="jb-card-meta">
                <span class="jb-meta-pill">Steamed Fresh</span>
                <span class="jb-meta-pill">Sellout Warning: 1:30 PM</span>
              </div>
              <a href="tuesday-friday-tamale-tradition.html" class="jb-btn jb-btn-lime" style="text-align: center; width: 100%;">Tamale Details</a>
            </div>
          </div>

          <div class="jb-card">
            <div class="jb-card-img-wrap">
              <img src="images/salsa-bar-chips-queso.jpg" alt="Chips, Queso and Salsa Bar" class="jb-card-img">
              <span class="jb-card-tag">Scratch Crafted</span>
            </div>
            <div class="jb-card-body">
              <div class="jb-card-header">
                <h3 class="jb-card-title">Salsa Bar &amp; Queso</h3>
                <span class="jb-card-price">$4.25+</span>
              </div>
              <p class="jb-card-desc">Crisp golden tortilla chips paired with warm spiced concourse queso, fresh hand-smashed guacamole, and five signature house salsas ranging from mild to El Diablo.</p>
              <div class="jb-card-meta">
                <span class="jb-meta-pill">5 Heat Levels</span>
                <span class="jb-meta-pill">Catering Pans Available</span>
              </div>
              <a href="salsa-bar-and-concourse-catering.html" class="jb-btn jb-btn-secondary" style="text-align: center; width: 100%;">Explore Salsas</a>
            </div>
          </div>
        </div>
      </section>

      <section class="jb-section jb-section-alt" style="border-radius: var(--jb-radius-lg); padding: 48px 32px; margin-top: 20px;">
        <div class="jb-grid-2" style="align-items: center;">
          <div>
            <span class="jb-badge jb-badge-red">Concourse Secrets</span>
            <h2 class="jb-title">How To Find Johnny Burrito</h2>
            <p style="color: var(--jb-text-muted); font-size: 1.05rem; margin-bottom: 20px;">
              Located underground inside the Two Wells Fargo Center concourse at 301 S Tryon Street. If you're on street level, enter the Two Wells Fargo glass atrium, head straight for the escalators, ride them down, and turn immediately to your right!
            </p>
            <ul class="jb-steps-list">
              <li class="jb-steps-item">
                <div class="jb-steps-num">1</div>
                <div class="jb-steps-text">
                  <h4>Enter Two Wells Fargo Atrium</h4>
                  <p style="font-size: 0.9rem; color: var(--jb-text-muted);">Access from S Tryon St or the connected Overstreet Mall walkway.</p>
                </div>
              </li>
              <li class="jb-steps-item">
                <div class="jb-steps-num">2</div>
                <div class="jb-steps-text">
                  <h4>Take The Escalator Down</h4>
                  <p style="font-size: 0.9rem; color: var(--jb-text-muted);">Descend into the lower concourse retail level.</p>
                </div>
              </li>
              <li class="jb-steps-item">
                <div class="jb-steps-num">3</div>
                <div class="jb-steps-text">
                  <h4>Turn Right &amp; Walk The Line</h4>
                  <p style="font-size: 0.9rem; color: var(--jb-text-muted);">Look for the colorful Johnny Burrito sign and fast-moving lunch queue.</p>
                </div>
              </li>
            </ul>
            <a href="visit.html" class="jb-btn jb-btn-primary">Detailed Directions &amp; Maps &rarr;</a>
          </div>
          <div>
            <img src="images/concourse-counter-lunch.jpg" alt="Concourse Counter Lunch" style="width: 100%; border-radius: var(--jb-radius-lg); box-shadow: var(--jb-shadow-lg); border: 2px solid var(--jb-border);">
          </div>
        </div>
      </section>
    </div>
"""

menu_content = """
    <div class="jb-container">
      <div class="jb-section-header">
        <span class="jb-badge">Uptown Walk-The-Line</span>
        <h1 class="jb-title">Johnny Burrito Menu &amp; Pricing</h1>
        <p class="jb-subtitle">Everything is made fresh in front of your eyes. Pick your format, choose your premium protein, and top with our scratch salsas and sides.</p>
      </div>

      <div class="jb-info-box">
        <div class="jb-info-box-header">
          <span class="jb-badge jb-badge-lime" style="margin-bottom:0;">CASH-EESH DISCOUNT</span>
          <h3 style="font-family: var(--jb-font-display); color: var(--jb-charcoal); font-size: 1.25rem;">Save When You Pay Cash!</h3>
        </div>
        <p style="color: var(--jb-text-muted); font-size: 0.95rem;">
          Johnny Burrito happily offers an instant Cash-Eesh discount for cash payments at the concourse register. Speed up the line and keep dollars in your pocket!
        </p>
      </div>

      <div class="jb-grid-2">
        <!-- Burritos & Bowls -->
        <div class="jb-card" style="padding: 28px;">
          <h3 class="jb-card-title" style="margin-bottom: 20px; border-bottom: 2px solid var(--jb-border); padding-bottom: 10px;">Custom Burritos &amp; Bowls</h3>
          
          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 800; font-size: 1.1rem; color: var(--jb-charcoal);">
              <span>Regular Burrito (12-inch)</span>
              <span style="color: var(--jb-terracotta);">$9.75</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--jb-text-muted);">Choice of Warm Flour, Whole Wheat, or Spinach Tortilla. Stuffed with seasoned rice, choice of black or pinto beans, Monterey Jack cheese, and salsa.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 800; font-size: 1.1rem; color: var(--jb-charcoal);">
              <span>The Big Burrito (Mega 14-inch)</span>
              <span style="color: var(--jb-terracotta);">$11.75</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--jb-text-muted);">Double rice, double beans, and generous extra fillings wrapped tight for serious appetites.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 800; font-size: 1.1rem; color: var(--jb-charcoal);">
              <span>Nacho Salad Bowl</span>
              <span style="color: var(--jb-terracotta);">$9.95</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--jb-text-muted);">Served in a crisp fried flour tortilla shell with chopped romaine, black/pinto beans, rice, shredded cheese, sour cream, and house salsa.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 800; font-size: 1.1rem; color: var(--jb-charcoal);">
              <span>Burrito Bowl (Gluten-Conscious)</span>
              <span style="color: var(--jb-terracotta);">$9.75</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--jb-text-muted);">All the burrito goodness without the wrap. Base of cilantro-lime rice and beans with crisp romaine topper.</p>
          </div>
        </div>

        <!-- Proteins & Add-Ons -->
        <div class="jb-card" style="padding: 28px;">
          <h3 class="jb-card-title" style="margin-bottom: 20px; border-bottom: 2px solid var(--jb-border); padding-bottom: 10px;">Proteins &amp; Premium Add-Ons</h3>

          <div style="margin-bottom: 16px;">
            <strong style="color: var(--jb-charcoal);">Citrus Grilled Chicken</strong>
            <p style="font-size: 0.9rem; color: var(--jb-text-muted);">Tender breast marinated in lime, garlic, cumin, and Mexican oregano, flame-seared.</p>
          </div>

          <div style="margin-bottom: 16px;">
            <strong style="color: var(--jb-charcoal);">Marinated Flank Steak</strong>
            <p style="font-size: 0.9rem; color: var(--jb-text-muted);">Carne asada-style seasoned beef sliced thin and grilled to juicy perfection (+ $1.00).</p>
          </div>

          <div style="margin-bottom: 16px;">
            <strong style="color: var(--jb-charcoal);">Picadillo Ground Beef</strong>
            <p style="font-size: 0.9rem; color: var(--jb-text-muted);">Classic Mexican simmered ground beef with diced potatoes, onions, and warm spices.</p>
          </div>

          <div style="margin-bottom: 16px;">
            <strong style="color: var(--jb-charcoal);">Saut&eacute;ed Veggie Medley</strong>
            <p style="font-size: 0.9rem; color: var(--jb-text-muted);">Fresh zucchini, yellow squash, sweet bell peppers, and caramelized onions.</p>
          </div>

          <div style="border-top: 1px dashed var(--jb-border); padding-top: 14px; margin-top: 14px;">
            <div style="display: flex; justify-content: space-between; font-size: 0.95rem; margin-bottom: 6px;">
              <span>Hand-Mashed Fresh Guacamole</span>
              <strong style="color: var(--jb-terracotta);">+$2.25</strong>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 0.95rem; margin-bottom: 6px;">
              <span>Concourse Warm Queso Dip</span>
              <strong style="color: var(--jb-terracotta);">+$2.00</strong>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 0.95rem;">
              <span>Double Meat Extra Scoop</span>
              <strong style="color: var(--jb-terracotta);">+$3.50</strong>
            </div>
          </div>
        </div>
      </div>

      <!-- Tamales & Sides -->
      <div class="jb-grid-2" style="margin-top: 30px;">
        <div class="jb-card" style="padding: 28px;">
          <span class="jb-badge jb-badge-lime" style="float: right;">Tues &amp; Fri</span>
          <h3 class="jb-card-title" style="margin-bottom: 16px;">Scratch Homemade Tamales</h3>
          <p style="font-size: 0.9rem; color: var(--jb-text-muted); margin-bottom: 16px;">
            Hand-made in corn husks every Tuesday and Friday. $3.95 each or $42.00 per dozen.
          </p>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 10px; font-size: 0.95rem;">
            <li><strong>Chicken Salsa Verde:</strong> Shredded chicken simmered in tangy tomatillo cilantro sauce.</li>
            <li><strong>Picadillo Beef:</strong> Spiced ground beef with diced potatoes and chilies.</li>
            <li><strong>Smoked BBQ Pork:</strong> Carolina-meets-Baja pulled pork in smoky chili barbecue glaze.</li>
            <li><strong>Sweet Corn Vegetarian:</strong> Whipped masa with tender sweet corn kernels and mild poblanos.</li>
          </ul>
        </div>

        <div class="jb-card" style="padding: 28px;">
          <h3 class="jb-card-title" style="margin-bottom: 16px;">Sides, Snacks &amp; Slushies</h3>
          <div style="margin-bottom: 14px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Fresh Tortilla Chips &amp; Salsa</span>
              <span style="color: var(--jb-terracotta);">$3.50</span>
            </div>
            <small style="color: var(--jb-text-muted);">Crisp house chips with 4oz cup of your favorite salsa.</small>
          </div>
          <div style="margin-bottom: 14px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Chips with Warm Queso or Guac</span>
              <span style="color: var(--jb-terracotta);">$4.95</span>
            </div>
            <small style="color: var(--jb-text-muted);">4oz cup of warm melted cheese dip or hand-mashed avocado guacamole.</small>
          </div>
          <div style="margin-bottom: 14px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Frozen Fruit Slushies</span>
              <span style="color: var(--jb-terracotta);">$3.25</span>
            </div>
            <small style="color: var(--jb-text-muted);">Rotating flavors including Mango Lime, Strawberry, and Blue Raspberry.</small>
          </div>
          <div>
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Sweet Treats (Moon Pies, Brownies)</span>
              <span style="color: var(--jb-terracotta);">$1.75 &ndash; $2.50</span>
            </div>
            <small style="color: var(--jb-text-muted);">Rice Krispy treats, chocolate fudge brownies, and vintage Moon Pies.</small>
          </div>
        </div>
      </div>
    </div>
"""

burritos_content = """
    <div class="jb-container">
      <div class="jb-section-header">
        <span class="jb-badge">Interactive Customizer</span>
        <h1 class="jb-title">Famous Burritos &amp; Nacho Bowls</h1>
        <p class="jb-subtitle">Walk the line digitally! Configure your dream Johnny Burrito, calculate real-time nutritional estimates, and see your Cash-Eesh savings.</p>
      </div>

      <div class="jb-builder-card jb-builder-container">
        <div class="jb-builder-step">
          <div class="jb-step-label">
            <span class="jb-step-number">1</span>
            <span>Choose Your Format &amp; Size</span>
          </div>
          <div class="jb-options-grid">
            <button class="jb-opt-btn jb-opt-format active" data-name="Regular Burrito (12-inch)" data-price="9.75" data-cal="580">Regular Burrito (12") - $9.75</button>
            <button class="jb-opt-btn jb-opt-format" data-name="Big Burrito (14-inch)" data-price="11.75" data-cal="850">The Big Burrito (14") - $11.75</button>
            <button class="jb-opt-btn jb-opt-format" data-name="Nacho Salad Bowl" data-price="9.95" data-cal="620">Nacho Salad Bowl - $9.95</button>
            <button class="jb-opt-btn jb-opt-format" data-name="Burrito Rice Bowl" data-price="9.75" data-cal="520">Burrito Rice Bowl - $9.75</button>
          </div>
        </div>

        <div class="jb-builder-step">
          <div class="jb-step-label">
            <span class="jb-step-number">2</span>
            <span>Select Tortilla Style</span>
          </div>
          <div class="jb-options-grid">
            <button class="jb-opt-btn jb-opt-tortilla active" data-name="Warm Flour Tortilla" data-cal="210">Warm Flour</button>
            <button class="jb-opt-btn jb-opt-tortilla" data-name="Whole Wheat Tortilla" data-cal="190">Whole Wheat</button>
            <button class="jb-opt-btn jb-opt-tortilla" data-name="Spinach Herb Tortilla" data-cal="200">Spinach Herb</button>
            <button class="jb-opt-btn jb-opt-tortilla" data-name="Crisp Tortilla Bowl" data-cal="280">Crisp Fried Shell</button>
          </div>
        </div>

        <div class="jb-builder-step">
          <div class="jb-step-label">
            <span class="jb-step-number">3</span>
            <span>Choose Seasoned Protein</span>
          </div>
          <div class="jb-options-grid">
            <button class="jb-opt-btn jb-opt-protein active" data-name="Citrus-Grilled Chicken" data-cal="180">Grilled Chicken</button>
            <button class="jb-opt-btn jb-opt-protein" data-name="Marinated Flank Steak" data-cal="220">Flank Steak</button>
            <button class="jb-opt-btn jb-opt-protein" data-name="Picadillo Ground Beef" data-cal="240">Picadillo Beef</button>
            <button class="jb-opt-btn jb-opt-protein" data-name="Sautéed Veggie Medley" data-cal="90">Sautéed Veggies</button>
            <button class="jb-opt-btn jb-opt-protein" data-name="Steak & Chicken Combo" data-cal="200">Steak/Chicken Combo</button>
          </div>
        </div>

        <div class="jb-builder-step">
          <div class="jb-step-label">
            <span class="jb-step-number">4</span>
            <span>Select Rice &amp; Bean Base</span>
          </div>
          <div class="jb-options-grid">
            <button class="jb-opt-btn jb-opt-base active" data-name="Johnny Rice & Black Beans" data-cal="220">Rice + Black Beans</button>
            <button class="jb-opt-btn jb-opt-base" data-name="Johnny Rice & Pinto Beans" data-cal="230">Rice + Pinto Beans</button>
            <button class="jb-opt-btn jb-opt-base" data-name="Black & Pinto Beans (No Rice)" data-cal="200">Double Beans (No Rice)</button>
            <button class="jb-opt-btn jb-opt-base" data-name="Extra Cilantro Rice (No Beans)" data-cal="240">Extra Rice (No Beans)</button>
          </div>
        </div>

        <div class="jb-builder-step">
          <div class="jb-step-label">
            <span class="jb-step-number">5</span>
            <span>Choose Scratch Salsa Tier</span>
          </div>
          <div class="jb-options-grid">
            <button class="jb-opt-btn jb-opt-salsa" data-name="Fresh Pico de Gallo (Mild)" data-cal="15">Mild Pico</button>
            <button class="jb-opt-btn jb-opt-salsa active" data-name="Medium Salsa Verde" data-cal="25">Med Salsa Verde</button>
            <button class="jb-opt-btn jb-opt-salsa" data-name="Smoked Chipotle (Medium-Hot)" data-cal="30">Smoked Chipotle</button>
            <button class="jb-opt-btn jb-opt-salsa" data-name="Roasted Habanero (Hot)" data-cal="25">Roasted Habanero</button>
            <button class="jb-opt-btn jb-opt-salsa" data-name="El Diablo (Fiery Extreme)" data-cal="20">El Diablo (Fiery)</button>
          </div>
        </div>

        <div class="jb-builder-step">
          <div class="jb-step-label">
            <span class="jb-step-number">6</span>
            <span>Premium Add-Ons &amp; Extras</span>
          </div>
          <div class="jb-options-grid">
            <button id="jb-toggle-guac" class="jb-opt-btn">Fresh Guacamole (+$2.25)</button>
            <button id="jb-toggle-queso" class="jb-opt-btn">Concourse Queso (+$2.00)</button>
            <button id="jb-toggle-meat" class="jb-opt-btn">Double Meat Scoop (+$3.50)</button>
          </div>
        </div>

        <div class="jb-summary-panel">
          <div class="jb-summary-metrics">
            <div class="jb-metric-item">
              <span class="jb-metric-label">Estimated Price</span>
              <span id="jb-builder-price" class="jb-metric-val">$9.75</span>
            </div>
            <div class="jb-metric-item">
              <span class="jb-metric-label">Cash-Eesh Price</span>
              <span id="jb-builder-cash-price" class="jb-metric-val" style="color: #4ade80;">$9.26</span>
              <span class="jb-cash-discount-badge">Save 5% with Cash</span>
            </div>
            <div class="jb-metric-item">
              <span class="jb-metric-label">Nutritional Value</span>
              <span id="jb-builder-calories" class="jb-metric-val" style="color: #67e8f9;">1205 kcal</span>
            </div>
          </div>
          <div style="flex-basis: 100%; border-top: 1px solid #475569; padding-top: 16px; margin-top: 10px;">
            <strong style="color: #cbd5e1; display: block; font-size: 0.85rem; text-transform: uppercase;">Custom Build Summary:</strong>
            <p id="jb-builder-summary-text" style="color: #ffffff; font-size: 1rem; margin-top: 4px;">Regular Burrito on Warm Flour with Citrus Chicken, Rice &amp; Black Beans, Salsa Verde.</p>
          </div>
        </div>
      </div>
    </div>
"""

pages = {
    "index.html": ("Home", index_content),
    "menu.html": ("Full Menu", menu_content),
    "famous-burritos-and-bowls.html": ("Burritos & Bowls", burritos_content)
}

for filename, (label, content) in pages.items():
    html = wrap_page(label, filename, content)
    with open(os.path.join("johnny-burrito", filename), "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"Generated {filename}")
