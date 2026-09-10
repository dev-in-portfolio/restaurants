import os
from jb_core import wrap_page

tamale_content = """
    <div class="jb-container">
      <div class="jb-section-header">
        <span class="jb-badge jb-badge-lime">Two Days A Week Only</span>
        <h1 class="jb-title">Tuesday &amp; Friday Homemade Tamale Tradition</h1>
        <p class="jb-subtitle">Since 1998, Tuesdays and Fridays in the Two Wells Fargo Concourse mean steaming batches of authentic hand-wrapped Mexican tamales.</p>
      </div>

      <div class="jb-grid-2" style="align-items: center; margin-bottom: 48px;">
        <div>
          <span class="jb-badge jb-badge-red">The Early Bird Rule</span>
          <h2 class="jb-title" style="font-size: 2rem;">Why We Sell Out By 1:30 PM</h2>
          <p style="color: var(--jb-text-muted); font-size: 1.05rem; margin-bottom: 16px;">
            Every Tuesday and Friday morning before sunrise, our kitchen whips fresh masa, fills each portion with seasoned meats and cheeses, and rolls them inside natural corn husks for slow steaming.
          </p>
          <p style="color: var(--jb-text-muted); font-size: 1.05rem; margin-bottom: 20px;">
            Because they are made from scratch without shortcuts or preservatives, quantities are strictly limited each day. Concourse regulars know to arrive between 11:00 AM and 12:45 PM to guarantee their favorites before the steamers run dry.
          </p>
          <div style="background: #ffedd5; border-left: 4px solid var(--jb-terracotta); padding: 16px; border-radius: 6px;">
            <strong style="color: var(--jb-charcoal); display: block;">Individual &amp; Dozen Pricing:</strong>
            <span style="color: var(--jb-terracotta); font-size: 1.1rem; font-weight: 800;">$3.95 each &bull; $42.00 per dozen (Mixed varieties welcome)</span>
          </div>
        </div>
        <div>
          <img src="images/scratch-homemade-tamales.jpg" alt="Scratch Steamed Tamales" style="width: 100%; border-radius: var(--jb-radius-lg); box-shadow: var(--jb-shadow-lg); border: 2px solid var(--jb-border);">
        </div>
      </div>

      <div class="jb-section-header">
        <h2 class="jb-title" style="font-size: 2rem;">Our 4 Rotating Tamale Fillings</h2>
      </div>

      <div class="jb-grid-4">
        <div class="jb-card" style="padding: 20px;">
          <h3 style="font-family: var(--jb-font-display); font-size: 1.2rem; color: var(--jb-terracotta); margin-bottom: 8px;">Chicken Salsa Verde</h3>
          <p style="font-size: 0.875rem; color: var(--jb-text-muted);">Juicy pulled chicken breast simmered with roasted tomatillos, jalapeño, cilantro, and garlic in light fluffy masa.</p>
        </div>
        <div class="jb-card" style="padding: 20px;">
          <h3 style="font-family: var(--jb-font-display); font-size: 1.2rem; color: var(--jb-terracotta); margin-bottom: 8px;">Picadillo Beef</h3>
          <p style="font-size: 0.875rem; color: var(--jb-text-muted);">Seasoned ground beef with diced potatoes, caramelized onion, and Mexican chili powder. Hearty and savory.</p>
        </div>
        <div class="jb-card" style="padding: 20px;">
          <h3 style="font-family: var(--jb-font-display); font-size: 1.2rem; color: var(--jb-terracotta); margin-bottom: 8px;">Smoked BBQ Pork</h3>
          <p style="font-size: 0.875rem; color: var(--jb-text-muted);">Slow-roasted pork shoulder tossed in Johnny's signature tangy sweet barbecue chili glaze.</p>
        </div>
        <div class="jb-card" style="padding: 20px;">
          <h3 style="font-family: var(--jb-font-display); font-size: 1.2rem; color: var(--jb-terracotta); margin-bottom: 8px;">Sweet Corn Veggie</h3>
          <p style="font-size: 0.875rem; color: var(--jb-text-muted);">Vegetarian masa packed with whole sweet corn kernels, poblano pepper strips, and melted Monterey Jack cheese.</p>
        </div>
      </div>

      <div class="jb-builder-card" style="margin-top: 48px;">
        <h3 style="font-family: var(--jb-font-display); color: var(--jb-charcoal); font-size: 1.4rem; margin-bottom: 8px;">Office Tamale Reservation &amp; Dozen Estimator</h3>
        <p style="color: var(--jb-text-muted); font-size: 0.95rem; margin-bottom: 24px;">Planning a Tuesday or Friday team lunch in Two Wells Fargo or nearby towers? Calculate your dozen order.</p>
        
        <div class="jb-grid-2">
          <div>
            <label style="display: block; font-weight: 700; margin-bottom: 6px; color: var(--jb-slate);">Number of Tamales</label>
            <input type="number" id="jb-tamale-qty" min="1" max="100" value="12" style="width: 100%; padding: 12px; border: 2px solid var(--jb-border); border-radius: var(--jb-radius); font-size: 1.1rem; font-weight: 700;">
          </div>
          <div>
            <label style="display: block; font-weight: 700; margin-bottom: 6px; color: var(--jb-slate);">Primary Flavor</label>
            <select id="jb-tamale-flavor" style="width: 100%; padding: 12px; border: 2px solid var(--jb-border); border-radius: var(--jb-radius); font-size: 1rem; font-weight: 700;">
              <option value="Mixed Assortment (All 4 Flavors)">Mixed Assortment (All 4 Flavors)</option>
              <option value="Chicken Salsa Verde">Chicken Salsa Verde</option>
              <option value="Picadillo Beef">Picadillo Beef</option>
              <option value="Smoked BBQ Pork">Smoked BBQ Pork</option>
              <option value="Sweet Corn Vegetarian">Sweet Corn Vegetarian</option>
            </select>
          </div>
        </div>

        <div style="background: var(--jb-slate); color: #ffffff; padding: 20px; border-radius: var(--jb-radius); margin-top: 24px;">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
            <div>
              <span style="font-size: 0.8rem; text-transform: uppercase; color: #94a3b8;">Estimated Subtotal</span>
              <div id="jb-tamale-price" style="font-family: var(--jb-font-display); font-size: 1.6rem; color: var(--jb-maize-light);">$42.00 (Cash-Eesh: $39.90)</div>
            </div>
            <a href="tel:7043714448" class="jb-btn jb-btn-primary">Call (704) 371-4448 to Reserve</a>
          </div>
          <p id="jb-tamale-output" style="font-size: 0.9rem; color: #cbd5e1; margin-top: 10px; border-top: 1px solid #475569; padding-top: 10px;">Reservation estimation for 12 x Mixed Assortment. Steamed fresh Tuesday &amp; Friday mornings.</p>
        </div>
      </div>
    </div>
"""

salsa_catering_content = """
    <div class="jb-container">
      <div class="jb-section-header">
        <span class="jb-badge">5-Tier Scratch Salsas</span>
        <h1 class="jb-title">The Salsa Lab &amp; Corporate Catering</h1>
        <p class="jb-subtitle">Every salsa is blended in-house using whole charred peppers, fresh cilantro, lime juice, and secret spice blends. Plus easy office catering for Uptown corporate teams.</p>
      </div>

      <div class="jb-grid-2" style="margin-bottom: 48px;">
        <div>
          <h2 class="jb-title" style="font-size: 1.8rem; margin-bottom: 16px;">Interactive Heat Index Matrix</h2>
          <p style="color: var(--jb-text-muted); margin-bottom: 24px;">Click any salsa below to reveal tasting notes, heat rating, and optimal burrito pairing.</p>
          
          <div class="jb-heat-meter-container">
            <div class="jb-salsa-card" data-name="Pico de Gallo" data-heat="1" data-scoville="500 - 1,000 SHU" data-notes="Crisp diced Roma tomatoes, sweet white onion, chopped fresh cilantro, diced jalapeño, and freshly squeezed lime juice. Refreshing and bright.">
              <div>
                <strong style="color: var(--jb-charcoal); font-size: 1.05rem;">1. Fresh Pico de Gallo</strong>
                <div style="font-size: 0.85rem; color: var(--jb-text-muted);">Mild &bull; Fresh Herbaceous</div>
              </div>
              <div class="jb-heat-level">
                <span class="jb-heat-dot active-1"></span>
                <span class="jb-heat-dot"></span>
                <span class="jb-heat-dot"></span>
                <span class="jb-heat-dot"></span>
                <span class="jb-heat-dot"></span>
              </div>
            </div>

            <div class="jb-salsa-card" data-name="Medium Salsa Verde" data-heat="2" data-scoville="1,500 - 2,500 SHU" data-notes="Roasted green tomatillos, charred serrano peppers, garlic, and fresh lime. Tangy with a smooth medium kick. Perfect with citrus grilled chicken.">
              <div>
                <strong style="color: var(--jb-charcoal); font-size: 1.05rem;">2. Medium Salsa Verde</strong>
                <div style="font-size: 0.85rem; color: var(--jb-text-muted);">Medium &bull; Tangy Tomatillo</div>
              </div>
              <div class="jb-heat-level">
                <span class="jb-heat-dot active-1"></span>
                <span class="jb-heat-dot active-2"></span>
                <span class="jb-heat-dot"></span>
                <span class="jb-heat-dot"></span>
                <span class="jb-heat-dot"></span>
              </div>
            </div>

            <div class="jb-salsa-card" data-name="Smoked Chipotle Salsa" data-heat="3" data-scoville="3,500 - 5,000 SHU" data-notes="Smoked morita jalapeños with roasted plum tomatoes and toasted cumin. Rich, smoky warmth that cuts through queso and beef.">
              <div>
                <strong style="color: var(--jb-charcoal); font-size: 1.05rem;">3. Smoked Chipotle Salsa</strong>
                <div style="font-size: 0.85rem; color: var(--jb-text-muted);">Medium-Hot &bull; Rich &amp; Smoky</div>
              </div>
              <div class="jb-heat-level">
                <span class="jb-heat-dot active-1"></span>
                <span class="jb-heat-dot active-2"></span>
                <span class="jb-heat-dot active-3"></span>
                <span class="jb-heat-dot"></span>
                <span class="jb-heat-dot"></span>
              </div>
            </div>

            <div class="jb-salsa-card" data-name="Roasted Habanero" data-heat="4" data-scoville="15,000 - 30,000 SHU" data-notes="Fire-roasted orange habaneros blended with charred garlic and citrus. Fruity front note with an intense lingering thermal kick.">
              <div>
                <strong style="color: var(--jb-charcoal); font-size: 1.05rem;">4. Roasted Habanero</strong>
                <div style="font-size: 0.85rem; color: var(--jb-text-muted);">Hot &bull; Fruity &amp; Intense</div>
              </div>
              <div class="jb-heat-level">
                <span class="jb-heat-dot active-1"></span>
                <span class="jb-heat-dot active-2"></span>
                <span class="jb-heat-dot active-3"></span>
                <span class="jb-heat-dot active-4"></span>
                <span class="jb-heat-dot"></span>
              </div>
            </div>

            <div class="jb-salsa-card" data-name="El Diablo (Extreme Heat)" data-heat="5" data-scoville="50,000+ SHU" data-notes="Johnny Burrito's legendary concourse dare. Pure fire-roasted habaneros, ghost chilies, and black pepper. Approach with caution!">
              <div>
                <strong style="color: var(--jb-habanero); font-size: 1.05rem;">5. El Diablo Salsa</strong>
                <div style="font-size: 0.85rem; color: var(--jb-text-muted);">Fiery Extreme &bull; Concourse Challenge</div>
              </div>
              <div class="jb-heat-level">
                <span class="jb-heat-dot active-1"></span>
                <span class="jb-heat-dot active-2"></span>
                <span class="jb-heat-dot active-3"></span>
                <span class="jb-heat-dot active-4"></span>
                <span class="jb-heat-dot active-5"></span>
              </div>
            </div>
          </div>
        </div>

        <div>
          <div id="jb-heat-detail-box" style="background: #ffffff; border: 2px solid var(--jb-border); border-radius: var(--jb-radius-lg); padding: 32px; box-shadow: var(--jb-shadow); height: 100%; display: flex; flex-direction: column; justify-content: center;">
            <span class="jb-badge jb-badge-lime" style="align-self: flex-start;">Select Any Salsa</span>
            <h3 style="font-family: var(--jb-font-display); color: var(--jb-charcoal); font-size: 1.5rem; margin: 12px 0;">Medium Salsa Verde (Heat Level: 2/5)</h3>
            <p style="font-size: 0.95rem; color: var(--jb-text-muted); margin-bottom: 8px;"><strong>Estimated Scoville:</strong> 1,500 - 2,500 SHU</p>
            <p style="font-size: 0.95rem; color: var(--jb-slate); line-height: 1.6;">
              Roasted green tomatillos, charred serrano peppers, garlic, and fresh lime. Tangy with a smooth medium kick. Perfect with citrus grilled chicken and nacho bowls.
            </p>
          </div>
        </div>
      </div>

      <!-- Catering Calculator -->
      <div class="jb-builder-card">
        <div class="jb-section-header" style="margin-bottom: 30px;">
          <span class="jb-badge">Corporate Catering</span>
          <h2 class="jb-title" style="font-size: 2rem;">Uptown Office Lunch Estimator</h2>
          <p class="jb-subtitle">Individual boxed burritos or build-your-own fiesta bars delivered or staged for seamless concourse pick-up.</p>
        </div>

        <div class="jb-grid-3">
          <div>
            <label style="display: block; font-weight: 700; margin-bottom: 6px; color: var(--jb-slate);">Guest Count</label>
            <input type="number" id="jb-cat-guests" min="5" max="250" value="20" style="width: 100%; padding: 12px; border: 2px solid var(--jb-border); border-radius: var(--jb-radius); font-size: 1.1rem; font-weight: 700;">
          </div>
          <div>
            <label style="display: block; font-weight: 700; margin-bottom: 6px; color: var(--jb-slate);">Package Type</label>
            <select id="jb-cat-type" style="width: 100%; padding: 12px; border: 2px solid var(--jb-border); border-radius: var(--jb-radius); font-size: 1rem; font-weight: 700;">
              <option value="boxed">Individual Burrito Box ($13.50/ea)</option>
              <option value="fiesta-bar">Build-Your-Own Fiesta Bar ($15.75/ea)</option>
              <option value="tamale-fiesta">Tamale &amp; Burrito Combo Feast ($16.50/ea)</option>
            </select>
          </div>
          <div>
            <label style="display: block; font-weight: 700; margin-bottom: 10px; color: var(--jb-slate);">Drink Add-On</label>
            <label style="display: flex; align-items: center; gap: 8px; font-weight: 600; cursor: pointer;">
              <input type="checkbox" id="jb-cat-slushies" style="width: 20px; height: 20px;">
              <span>Add Frozen Fruit Slushies (+$3.00/person)</span>
            </label>
          </div>
        </div>

        <div class="jb-summary-panel" style="margin-top: 30px;">
          <div class="jb-summary-metrics">
            <div class="jb-metric-item">
              <span class="jb-metric-label">Estimated Invoice</span>
              <span id="jb-cat-total" class="jb-metric-val">$270.00</span>
            </div>
            <div class="jb-metric-item">
              <span class="jb-metric-label">Cash-Eesh Discount Price</span>
              <span id="jb-cat-cash" class="jb-metric-val" style="color: #4ade80;">$256.50</span>
              <span class="jb-cash-discount-badge">Save $13.50 with Cash</span>
            </div>
          </div>
          <div style="flex-basis: 100%; border-top: 1px solid #475569; padding-top: 16px; margin-top: 10px;">
            <p id="jb-cat-breakdown" style="color: #cbd5e1; font-size: 0.95rem;">Includes 20 customized portions, fresh tortilla chips, house salsa bar sampler, jalapeños, napkins, and serving utensils.</p>
          </div>
        </div>
      </div>
    </div>
"""

visit_content = """
    <div class="jb-container">
      <div class="jb-section-header">
        <span class="jb-badge">Concourse Navigation</span>
        <h1 class="jb-title">Visit Johnny Burrito</h1>
        <p class="jb-subtitle">Located beneath Two Wells Fargo Center in Uptown Charlotte. Walk down the escalators into subterranean burrito paradise.</p>
      </div>

      <div class="jb-grid-2" style="margin-bottom: 40px;">
        <div class="jb-card" style="padding: 32px;">
          <h2 class="jb-card-title" style="font-size: 1.6rem; margin-bottom: 20px;">Location &amp; Concourse Access</h2>
          
          <div style="margin-bottom: 20px;">
            <strong style="color: var(--jb-charcoal); display: block; font-size: 1.1rem;">Street Address</strong>
            <p style="color: var(--jb-text-muted); font-size: 1rem;">
              301 S Tryon St, Concourse Level<br>
              Two Wells Fargo Atrium<br>
              Charlotte, NC 28202
            </p>
          </div>

          <div style="margin-bottom: 20px;">
            <strong style="color: var(--jb-charcoal); display: block; font-size: 1.1rem;">Underground Navigation Instructions</strong>
            <ol style="margin-left: 20px; color: var(--jb-text-muted); font-size: 0.95rem; line-height: 1.7;">
              <li>Enter the Two Wells Fargo glass atrium from S Tryon St or Overstreet Mall.</li>
              <li>Locate the central escalators leading to the lower retail concourse.</li>
              <li>Ride the escalator down and immediately turn to your right.</li>
              <li>Johnny Burrito is located right along the main concourse corridor.</li>
            </ol>
          </div>

          <div style="margin-bottom: 20px;">
            <strong style="color: var(--jb-charcoal); display: block; font-size: 1.1rem;">Operating Hours</strong>
            <p style="color: var(--jb-text-muted); font-size: 1rem;">
              <strong>Monday &ndash; Friday:</strong> 11:00 AM &ndash; 3:00 PM<br>
              <strong>Saturday &ndash; Sunday:</strong> Closed (Corporate Concourse)
            </p>
          </div>
        </div>

        <div class="jb-card" style="padding: 32px;">
          <h2 class="jb-card-title" style="font-size: 1.6rem; margin-bottom: 20px;">Direct Ordering Guidelines</h2>

          <div style="margin-bottom: 24px;">
            <strong style="color: var(--jb-charcoal); display: block; font-size: 1.1rem;">Phone Call-Ahead Ordering</strong>
            <p style="color: var(--jb-text-muted); font-size: 0.95rem; margin-bottom: 8px;">
              For express individual pick-up, call our counter directly:
            </p>
            <a href="tel:7043714448" class="jb-btn jb-btn-primary" style="display: inline-block;">Call (704) 371-4448</a>
          </div>

          <div style="margin-bottom: 24px;">
            <strong style="color: var(--jb-charcoal); display: block; font-size: 1.1rem;">Fax Ordering Protocols</strong>
            <p style="color: var(--jb-text-muted); font-size: 0.95rem; margin-bottom: 8px;">
              Fax number: <strong>(704) 371-4449</strong>. Please note that no fax orders are accepted during peak rush between <strong>10:45 AM &ndash; 1:30 PM</strong>. Submit before 10:45 AM for lunch pickup.
            </p>
          </div>

          <div style="background: #ecfccb; border: 1px solid #d9f99d; padding: 18px; border-radius: var(--jb-radius);">
            <strong style="color: var(--jb-lime-dark); font-size: 1rem; display: block; margin-bottom: 4px;">Cash-Eesh Advantage</strong>
            <p style="color: #365314; font-size: 0.9rem;">
              Remember to bring cash to take advantage of our express register cash discount!
            </p>
          </div>
        </div>
      </div>
    </div>
"""

pages = {
    "tuesday-friday-tamale-tradition.html": ("Tamale Tradition", tamale_content),
    "salsa-bar-and-concourse-catering.html": ("Salsas & Catering", salsa_catering_content),
    "visit.html": ("Visit & Concourse", visit_content)
}

for filename, (label, content) in pages.items():
    html = wrap_page(label, filename, content)
    with open(os.path.join("johnny-burrito", filename), "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"Generated {filename}")
