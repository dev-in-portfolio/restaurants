import os
from luce_core import wrap_page

wine_content = """
    <div class="luce-container">
      <div class="luce-section-header">
        <span class="luce-badge luce-badge-gold">Enacoteca Italiana</span>
        <h1 class="luce-title">The Italian Wine Cellar &amp; Aperitivi</h1>
        <p class="luce-subtitle">An encyclopedic collection of premier Italian terroirs alongside classic Venetian and Milanese aperitivo cocktails.</p>
      </div>

      <div class="luce-grid-2" style="align-items: center; margin-bottom: 48px;">
        <div>
          <span class="luce-badge">Sommelier Curated</span>
          <h2 class="luce-title" style="font-size: 2rem;">Vintages From Tuscany, Piedmont &amp; Beyond</h2>
          <p style="color: var(--luce-text-muted); font-size: 1.05rem; margin-bottom: 16px;">
            Our sommelier team has assembled exceptional vintages ranging from classic Chianti Classico Gran Selezione and prestigious Brunello di Montalcino DOCG to legendary Super Tuscans from Bolgheri and noble Barolos from the Langhe hills.
          </p>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 10px; font-size: 0.95rem; margin-bottom: 20px;">
            <li><strong>Super Tuscans:</strong> Tenuta San Guido Sassicaia, Ornellaia, and Tignanello available by the bottle.</li>
            <li><strong>Piedmont Jewels:</strong> Barolo Cannubi and Barbaresco Asili paired with prime meats and truffles.</li>
            <li><strong>Crisp Coastal Whites:</strong> Vermentino di Bolgheri, Gavi di Gavi, and Pinot Grigio Alto Adige.</li>
          </ul>
        </div>
        <div>
          <img src="images/italian-wine-cellar-cocktails.jpg" alt="Italian Wine Cellar and Aperitivi" style="width: 100%; border-radius: var(--luce-radius-lg); box-shadow: var(--luce-shadow-lg); border: 2px solid var(--luce-border);">
        </div>
      </div>

      <div class="luce-section-header">
        <h2 class="luce-title" style="font-size: 2rem;">Handcrafted Italian Aperitivo Cocktails</h2>
      </div>

      <div class="luce-grid-3">
        <div class="luce-card" style="padding: 24px;">
          <h3 style="font-family: var(--luce-font-display); font-size: 1.25rem; color: var(--luce-wine); margin-bottom: 8px;">Negroni Classico</h3>
          <p style="font-size: 0.9rem; color: var(--luce-text-muted); margin-bottom: 12px;">Campari, Carpano Antica Formula sweet vermouth, London dry gin, expressed orange peel over hand-carved ice sphere.</p>
          <span class="luce-card-price">$16.00</span>
        </div>
        <div class="luce-card" style="padding: 24px;">
          <h3 style="font-family: var(--luce-font-display); font-size: 1.25rem; color: var(--luce-wine); margin-bottom: 8px;">Aperol Spritz Veneziano</h3>
          <p style="font-size: 0.9rem; color: var(--luce-text-muted); margin-bottom: 12px;">Aperol, Prosecco Superiore di Valdobbiadene DOCG, splash of club soda, Castelvetrano olive and fresh orange wheel.</p>
          <span class="luce-card-price">$15.00</span>
        </div>
        <div class="luce-card" style="padding: 24px;">
          <h3 style="font-family: var(--luce-font-display); font-size: 1.25rem; color: var(--luce-wine); margin-bottom: 8px;">Tuscan Smoked Old Fashioned</h3>
          <p style="font-size: 0.9rem; color: var(--luce-text-muted); margin-bottom: 12px;">Woodford Reserve bourbon, Amaro Nonino, rosemary-infused demerara, Angostura bitters, smoked rosemary sprig.</p>
          <span class="luce-card-price">$18.00</span>
        </div>
      </div>
    </div>
"""

events_content = """
    <div class="luce-container">
      <div class="luce-section-header">
        <span class="luce-badge">Corporate &amp; Social Celebrations</span>
        <h1 class="luce-title">Private Dining &amp; Truist Plaza Patio</h1>
        <p class="luce-subtitle">Intimate corporate dinners, rehearsal banquets, and cocktail receptions beneath Murano glass or on the covered Truist Center Plaza.</p>
      </div>

      <div class="luce-grid-2" style="align-items: center; margin-bottom: 48px;">
        <div>
          <span class="luce-badge luce-badge-gold">Unrivaled Uptown Ambiance</span>
          <h2 class="luce-title" style="font-size: 2rem;">Host Your Gathering at Luce</h2>
          <p style="color: var(--luce-text-muted); font-size: 1.05rem; margin-bottom: 16px;">
            Whether hosting executive banking leadership in the private chandelier dining room or celebrating on the serene covered plaza patio, Luce provides flawless multi-course hospitality.
          </p>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 8px; font-size: 0.9rem; color: var(--luce-slate);">
            <li>&bull; Dedicated Sommelier wine service and custom menu printing</li>
            <li>&bull; Audio-visual capability for corporate board presentations</li>
            <li>&bull; 2-hour validated evening parking for all attendees</li>
          </ul>
        </div>
        <div>
          <img src="images/murano-plaza-patio-dining.jpg" alt="Murano Plaza Patio Dining" style="width: 100%; border-radius: var(--luce-radius-lg); box-shadow: var(--luce-shadow-lg); border: 2px solid var(--luce-border);">
        </div>
      </div>

      <!-- Event Estimator -->
      <div class="luce-builder-card">
        <div class="luce-section-header" style="margin-bottom: 24px;">
          <h2 class="luce-title" style="font-size: 1.8rem;">Private Event Budget Estimator</h2>
          <p class="luce-subtitle" style="font-size: 1rem;">Select your party size, dining venue, and multi-course dining package.</p>
        </div>

        <div class="luce-grid-3">
          <div>
            <label style="display: block; font-weight: 700; margin-bottom: 6px; color: var(--luce-slate);">Number of Guests</label>
            <input type="number" id="luce-event-guests" min="6" max="75" value="12" style="width: 100%; padding: 12px; border: 2px solid var(--luce-border); border-radius: var(--luce-radius); font-size: 1.1rem; font-weight: 700;">
          </div>
          <div>
            <label style="display: block; font-weight: 700; margin-bottom: 6px; color: var(--luce-slate);">Venue Setting</label>
            <select id="luce-event-room" style="width: 100%; padding: 12px; border: 2px solid var(--luce-border); border-radius: var(--luce-radius); font-size: 1rem; font-weight: 700;">
              <option value="murano">Murano Chandelier Dining Room</option>
              <option value="patio">Covered Truist Plaza Patio</option>
              <option value="main">Full Restaurant Buyout</option>
            </select>
          </div>
          <div>
            <label style="display: block; font-weight: 700; margin-bottom: 6px; color: var(--luce-slate);">Menu Tier</label>
            <select id="luce-event-menu" style="width: 100%; padding: 12px; border: 2px solid var(--luce-border); border-radius: var(--luce-radius); font-size: 1rem; font-weight: 700;">
              <option value="classic">3-Course Classic Tuscan ($85.00/person)</option>
              <option value="tuscan-feast">4-Course Executive Feast ($115.00/person)</option>
              <option value="sommelier-grand">5-Course Grand Sommelier Pairing ($160.00/person)</option>
            </select>
          </div>
        </div>

        <div class="luce-summary-panel">
          <div class="luce-summary-metrics">
            <div class="luce-metric-item">
              <span class="luce-metric-label">Estimated Food &amp; Wine</span>
              <span id="luce-event-total" class="luce-metric-val">$1,020.00</span>
            </div>
          </div>
          <div style="flex-basis: 100%; border-top: 1px solid rgba(255,255,255,0.15); padding-top: 16px; margin-top: 10px;">
            <p id="luce-event-summary" style="color: #d6d3d1; font-size: 0.95rem;">Private event proposal for 12 guests in the Murano Chandelier Dining Room. Includes personalized printed menu cards, dedicated Italian service staff, sommelier wine service, and 2-hour validated parking in Truist Center deck.</p>
          </div>
          <div style="flex-basis: 100%; margin-top: 16px;">
            <a href="tel:7043449222" class="luce-btn luce-btn-secondary">Call (704) 344-9222 to Inquire</a>
          </div>
        </div>
      </div>
    </div>
"""

visit_content = """
    <div class="luce-container">
      <div class="luce-section-header">
        <span class="luce-badge">Guest Guidelines &amp; Parking</span>
        <h1 class="luce-title">Visit Luce Ristorante e Bar</h1>
        <p class="luce-subtitle">Located inside the Truist Center Plaza at 214 N Tryon Street in Uptown Charlotte.</p>
      </div>

      <div class="luce-grid-2" style="margin-bottom: 40px;">
        <div class="luce-card" style="padding: 32px;">
          <h2 class="luce-card-title" style="font-size: 1.6rem; margin-bottom: 20px;">Plaza Navigation &amp; Address</h2>
          
          <div style="margin-bottom: 20px;">
            <strong style="color: var(--luce-charcoal); display: block; font-size: 1.1rem;">Street Address</strong>
            <p style="color: var(--luce-text-muted); font-size: 1rem;">
              214 N Tryon St, Suite J<br>
              Truist Center Plaza (formerly Hearst Tower)<br>
              Charlotte, NC 28202
            </p>
          </div>

          <div style="margin-bottom: 20px;">
            <strong style="color: var(--luce-charcoal); display: block; font-size: 1.1rem;">Finding The Entrance</strong>
            <p style="color: var(--luce-text-muted); font-size: 0.95rem; line-height: 1.7;">
              Luce is tucked into the central outdoor plaza of the Truist Center. Walk into the plaza courtyard from N Tryon Street or College Street to enter our dining room and covered patio.
            </p>
          </div>

          <div style="margin-bottom: 20px;">
            <strong style="color: var(--luce-charcoal); display: block; font-size: 1.1rem;">Validated Evening Parking</strong>
            <p style="color: var(--luce-text-muted); font-size: 0.95rem; line-height: 1.7;">
              Complimentary <strong>2-hour parking validation</strong> is provided for guests parking in the Truist Center parking deck (entrance located on 5th Street) after 5:00 PM. Please bring your parking ticket to our host stand.
            </p>
          </div>
        </div>

        <div class="luce-card" style="padding: 32px;">
          <h2 class="luce-card-title" style="font-size: 1.6rem; margin-bottom: 20px;">Reservations &amp; Etiquette</h2>

          <div style="margin-bottom: 20px;">
            <strong style="color: var(--luce-charcoal); display: block; font-size: 1.1rem;">Telephone Reservations</strong>
            <p style="color: var(--luce-text-muted); font-size: 0.95rem; margin-bottom: 12px;">
              Table reservations are strongly recommended for evening dinner service:
            </p>
            <a href="tel:7043449222" class="luce-btn luce-btn-primary" style="display: inline-block;">Call (704) 344-9222</a>
          </div>

          <div style="background: #ffedd5; border: 1px solid var(--luce-border); padding: 18px; border-radius: var(--luce-radius); margin-bottom: 20px;">
            <strong style="color: var(--luce-wine-dark); font-size: 1rem; display: block; margin-bottom: 4px;">Dress Code Policy</strong>
            <p style="color: #451a03; font-size: 0.9rem;">
              Smart casual or business attire is requested. Athletic wear, flip-flops, and sleeveless shirts are respectfully discouraged in the main dining room.
            </p>
          </div>

          <div>
            <strong style="color: var(--luce-charcoal); display: block; font-size: 1.1rem;">Hours of Service</strong>
            <p style="color: var(--luce-text-muted); font-size: 0.95rem;">
              <strong>Monday &ndash; Thursday:</strong> 11:30 AM &ndash; 2:30 PM, 5:00 PM &ndash; 10:00 PM<br>
              <strong>Friday:</strong> 11:30 AM &ndash; 2:30 PM, 5:00 PM &ndash; 10:30 PM<br>
              <strong>Saturday:</strong> 5:00 PM &ndash; 10:30 PM (Dinner only)<br>
              <strong>Sunday:</strong> Closed
            </p>
          </div>
        </div>
      </div>
    </div>
"""

pages = {
    "wine-cellar-and-aperitivo-cocktails.html": ("Wine Cellar", wine_content),
    "private-dining-and-plaza-events.html": ("Private Events", events_content),
    "visit.html": ("Visit & Parking", visit_content)
}

for filename, (label, content) in pages.items():
    html = wrap_page(label, filename, content)
    with open(os.path.join("luce-ristorante", filename), "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"Generated {filename}")
