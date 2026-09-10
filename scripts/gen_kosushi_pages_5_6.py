# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\scripts")
from kosushi_builder import header_html, footer_html

DIR = r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\k-o-sushi"

# 5. corporate-catering-and-party-trays.html
catering_page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Corporate Sushi Catering &amp; Party Platters | K.O. Sushi Charlotte</title>
  <meta name="description" content="Elevate your Uptown Charlotte corporate lunch or celebration with 38-piece K.O. Deluxe sushi platters, nigiri trays, and custom bento boxes.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
{header_html("corporate-catering-and-party-trays.html")}

  <section class="kosushi-hero" style="padding: 50px 20px;">
    <div class="kosushi-hero-inner">
      <span class="kosushi-hero-pill">Uptown Executive Catering</span>
      <h1>Corporate Sushi Catering &amp; Party Trays</h1>
      <p>Artisanal sushi platters designed specifically for Uptown Charlotte corporate boardrooms, client lunches, firm receptions, and private events.</p>
    </div>
  </section>

  <main class="kosushi-container">
    <div class="kosushi-section-title">
      <h2>Curated Sushi Party Platters</h2>
      <p>Artfully arranged on elegant catering platters with individual chopsticks, pickled ginger, and wasabi.</p>
    </div>

    <div class="kosushi-grid-3">
      <div class="kosushi-card">
        <div class="kosushi-card-body">
          <span class="kosushi-card-badge">Signature Platter</span>
          <h3>K.O. Deluxe Platter (38 Pcs)</h3>
          <p>Includes 2 Chef Specialty Rolls (Charlotte Roll &amp; K.O. Roll), 2 Classic Rolls (Spicy Tuna &amp; California), plus 10 pieces of assorted Salmon, Tuna, and Yellowtail Nigiri.</p>
          <div class="kosushi-card-footer">
            <span class="kosushi-price">$69.99</span>
            <span style="font-size:0.85rem; color:var(--kosushi-text-muted);">Feeds 6-8</span>
          </div>
        </div>
      </div>

      <div class="kosushi-card">
        <div class="kosushi-card-body">
          <span class="kosushi-card-badge">Executive Feast</span>
          <h3>Queen City Executive Box (52 Pcs)</h3>
          <p>Features 4 Specialty Rolls (Queen City, Dragon, Volcano, Rainbow) plus 20 pieces of premium Nigiri &amp; Sashimi (Sake, Maguro, Hamachi, Unagi).</p>
          <div class="kosushi-card-footer">
            <span class="kosushi-price">$98.99</span>
            <span style="font-size:0.85rem; color:var(--kosushi-text-muted);">Feeds 10-12</span>
          </div>
        </div>
      </div>

      <div class="kosushi-card">
        <div class="kosushi-card-body">
          <span class="kosushi-card-badge">Classic Office Mix</span>
          <h3>Maki Roll Sampler (48 Pcs)</h3>
          <p>An accessible assortment of California Rolls, Spicy Salmon Crunch, Philadelphia Rolls, Cucumber Avocado, and Shrimp Tempura Rolls.</p>
          <div class="kosushi-card-footer">
            <span class="kosushi-price">$58.99</span>
            <span style="font-size:0.85rem; color:var(--kosushi-text-muted);">Feeds 8-10</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Interactive Catering Calculator -->
    <div class="kosushi-section-title" style="margin-top:60px;">
      <h2>Interactive Corporate Catering Estimator</h2>
      <p>Plan sushi quantities, pieces per guest, hot side add-ons, and pricing for your upcoming meeting.</p>
    </div>

    <div class="kosushi-calc-box">
      <div class="kosushi-calc-row">
        <label for="calc-people">Number of Colleagues / Guests: <span id="calc-people-val" style="color:var(--kosushi-coral);">12 Guests / Colleagues</span></label>
        <input type="range" id="calc-people" min="6" max="60" step="2" value="12" class="kosushi-range-control">
      </div>

      <div class="kosushi-calc-row">
        <label for="calc-platter-tier">Select Sushi Platter Tier</label>
        <select id="calc-platter-tier" class="kosushi-select-control">
          <option value="18.50" selected>K.O. Deluxe Assortment ($18.50 / person - Specialty Rolls &amp; Nigiri)</option>
          <option value="22.50">Queen City Executive Tier ($22.50 / person - Premium Nigiri &amp; Sashimi)</option>
          <option value="14.50">Classic Maki Office Assortment ($14.50 / person - Popular Rolls)</option>
        </select>
      </div>

      <div class="kosushi-calc-row">
        <label for="calc-hot-addon">Add Appetizer or Soup Service</label>
        <select id="calc-hot-addon" class="kosushi-select-control">
          <option value="0" selected>No Appetizer Add-On</option>
          <option value="3.50">Add Gyoza Dumplings &amp; Edamame Pan (+$3.50 / person)</option>
          <option value="2.00">Add Hot Miso Soup Service with Cups (+$2.00 / person)</option>
        </select>
      </div>

      <div class="kosushi-calc-results">
        <div class="kosushi-result-line">
          <span>Total Sushi Pieces:</span>
          <strong id="calc-piece-count">Approx. 60 Handcrafted Pieces (~2 Party Platter Trays)</strong>
        </div>
        <div class="kosushi-result-line">
          <span>Included Condiments:</span>
          <strong id="calc-catering-sides">Includes Pickled Ginger, Real Wasabi, Low-Sodium Soy &amp; Chopsticks for 12</strong>
        </div>
        <div class="kosushi-result-total">
          <span>Estimated Total:</span>
          <span id="calc-total-price">$222.00</span>
        </div>
      </div>

      <div style="margin-top:24px; text-align:center;">
        <a href="tel:7043727757" class="kosushi-btn-hero-primary" style="display:inline-block; width:100%;">Call (704) 372-7757 to Book Corporate Catering</a>
      </div>
    </div>

    <!-- Ordering Policies -->
    <div class="kosushi-grid-2" style="margin-top:50px;">
      <div class="kosushi-card" style="padding:28px;">
        <h4 style="color:var(--kosushi-primary-dark); margin-bottom:10px;">Advance Notice &amp; Uptown Delivery</h4>
        <p style="color:var(--kosushi-text-muted); font-size:0.95rem;">Platters of 1 to 3 trays can be fulfilled with 1-2 hours advance notice during weekdays. For large firm-wide orders of 4+ platters or weekend events, please place orders 24 hours ahead.</p>
      </div>

      <div class="kosushi-card" style="padding:28px;">
        <h4 style="color:var(--kosushi-primary-dark); margin-bottom:10px;">Individual Boxed Bento Options</h4>
        <p style="color:var(--kosushi-text-muted); font-size:0.95rem;">We also prepare individually labeled corporate bento boxes (featuring a specialty roll, 2 pcs nigiri, edamame, and seaweed salad) to streamline boardroom distribution.</p>
      </div>
    </div>
  </main>

{footer_html()}'''

# 6. visit.html
visit_page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Visit &amp; Operating Hours | K.O. Sushi Uptown Charlotte</title>
  <meta name="description" content="Visit K.O. Sushi at 230 S Tryon St Suite R1 in Uptown Charlotte NC. Hours of operation, telephone orders, parking, Overstreet Mall walking directions, and FAQs.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
{header_html("visit.html")}

  <section class="kosushi-hero" style="padding: 50px 20px;">
    <div class="kosushi-hero-inner">
      <span class="kosushi-hero-pill">Uptown South Tryon Corridor</span>
      <h1>Visit &amp; Service Hours</h1>
      <p>Conveniently located in the heart of Uptown Charlotte for quick takeaway, counter dining, and corporate catering pickups.</p>
    </div>
  </section>

  <main class="kosushi-container">
    <div class="kosushi-visit-grid">
      <div class="kosushi-info-card">
        <h3>Location &amp; Contact</h3>
        
        <div class="kosushi-info-item">
          <strong>Street Address</strong>
          <p>230 S Tryon St, Suite R1<br>Charlotte, NC 28202<br>United States</p>
        </div>

        <div class="kosushi-info-item">
          <strong>Direct Phone Orders</strong>
          <p><a href="tel:7043727757" style="font-weight:700; font-size:1.15rem; color:var(--kosushi-coral);">(704) 372-7757</a></p>
        </div>

        <div class="kosushi-info-item">
          <strong>Email Inquiries</strong>
          <p><a href="mailto:info@kosushioftheqc.com">info@kosushioftheqc.com</a></p>
        </div>

        <div class="kosushi-info-item">
          <strong>Uptown Access &amp; Transit</strong>
          <p>Situated on South Tryon Street between 3rd and 4th Streets, accessible directly from the street level or via the Overstreet Mall network. Steps from the LYNX Blue Line CTC/Arena and 3rd St/Convention Center light rail stations.</p>
        </div>
      </div>

      <div class="kosushi-info-card">
        <h3>Hours of Operation</h3>
        
        <div class="kosushi-info-item">
          <strong>Monday</strong>
          <p>11:00 AM - 3:00 PM<br><small style="color:var(--kosushi-text-muted);">Lunch Rush Counter Service</small></p>
        </div>

        <div class="kosushi-info-item">
          <strong>Tuesday - Thursday</strong>
          <p>11:00 AM - 3:00 PM (Lunch)<br>4:30 PM - 8:00 PM (Dinner &amp; Evening Takeout)</p>
        </div>

        <div class="kosushi-info-item">
          <strong>Friday</strong>
          <p>11:00 AM - 3:00 PM<br><small style="color:var(--kosushi-text-muted);">Friday Executive Lunch &amp; Platter Pickup</small></p>
        </div>

        <div class="kosushi-info-item">
          <strong>Saturday &amp; Sunday</strong>
          <p>Closed for General Dining<br><small style="color:var(--kosushi-text-muted);">Large Corporate &amp; Private Catering available by advance booking</small></p>
        </div>
      </div>
    </div>

    <!-- FAQ Accordion -->
    <div class="kosushi-section-title" style="margin-top:60px;">
      <h2>Frequently Asked Questions</h2>
      <p>Helpful details about pickup times, dietary options, and corporate ordering.</p>
    </div>

    <div style="max-width:800px; margin:0 auto;">
      <div class="kosushi-accordion">
        <div class="kosushi-accordion-header">
          <span>How fast is takeout during the Uptown lunch rush?</span>
          <span class="kosushi-accordion-icon">+</span>
        </div>
        <div class="kosushi-accordion-content">
          <p>When you call ahead at (704) 372-7757, most specialty roll and poke orders are ready for grab-and-go pickup within 10 to 12 minutes, allowing you to breeze through your lunch break.</p>
        </div>
      </div>

      <div class="kosushi-accordion">
        <div class="kosushi-accordion-header">
          <span>Do you accommodate raw fish allergies or cooked sushi preferences?</span>
          <span class="kosushi-accordion-icon">+</span>
        </div>
        <div class="kosushi-accordion-content">
          <p>Yes, we offer numerous fully cooked options including the Volcano Roll, Dragon Roll, California Roll, Tempura Shrimp Roll, and hot entrees like Tempura Udon and Beef Bulgogi.</p>
        </div>
      </div>

      <div class="kosushi-accordion">
        <div class="kosushi-accordion-header">
          <span>Can I customize ingredients in the poke bowls?</span>
          <span class="kosushi-accordion-icon">+</span>
        </div>
        <div class="kosushi-accordion-content">
          <p>Absolutely. You can choose your base (sushi rice, brown rice, or spring mix), pick your proteins, and add any mix of vegetables, fruits, and dressings at our counter.</p>
        </div>
      </div>

      <div class="kosushi-accordion">
        <div class="kosushi-accordion-header">
          <span>How far in advance should corporate platters be ordered?</span>
          <span class="kosushi-accordion-icon">+</span>
        </div>
        <div class="kosushi-accordion-content">
          <p>For 1 to 3 party platters (up to 120 pieces), ordering 2 hours ahead is sufficient. For large corporate events over 150 pieces, please contact us 24 hours in advance.</p>
        </div>
      </div>
    </div>

    <div class="kosushi-cta-banner" style="margin-top:50px;">
      <h2>We Look Forward to Welcoming You</h2>
      <p>230 S Tryon St, Suite R1, Charlotte, NC 28202 | Call (704) 372-7757</p>
      <div class="kosushi-cta-btns">
        <a href="tel:7043727757" class="kosushi-btn-hero-primary">Call (704) 372-7757</a>
        <a href="menu.html" class="kosushi-btn-hero-secondary">Explore Menu</a>
      </div>
    </div>
  </main>

{footer_html()}'''

with open(os.path.join(DIR, "corporate-catering-and-party-trays.html"), "w", encoding="utf-8") as f:
    f.write(catering_page)
print("Wrote corporate-catering-and-party-trays.html")

with open(os.path.join(DIR, "visit.html"), "w", encoding="utf-8") as f:
    f.write(visit_page)
print("Wrote visit.html")
