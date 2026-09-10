# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\scripts")
from room112_builder import header_html, footer_html

DIR = r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\room-112"

# 5. sushi-platters-and-executive-dining.html
platters_page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sushi Platters &amp; Corporate Catering | Room 112 Charlotte</title>
  <meta name="description" content="Host executive luncheons and cocktail parties with 112 Deluxe sushi platters, boutique maki trays, and modern Asian catering in Uptown Charlotte.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
{header_html("sushi-platters-and-executive-dining.html")}

  <section class="room112-hero" style="padding: 50px 20px;">
    <div class="room112-hero-inner">
      <span class="room112-hero-pill">Uptown Corporate Dining</span>
      <h1>Sushi Platters &amp; Executive Catering</h1>
      <p>Artisanal sushi platters and hot Asian bistro buffet trays designed for corporate board meetings, client presentations, firm receptions, and private celebrations.</p>
    </div>
  </section>

  <main class="room112-container">
    <div class="room112-section-title">
      <h2>Curated Sushi &amp; Bistro Party Platters</h2>
      <p>Exquisitely arranged on modern black presentation platters with individual chopsticks, wasabi, and pickled ginger.</p>
    </div>

    <div class="room112-grid-3">
      <div class="room112-card">
        <div class="room112-card-body">
          <span class="room112-card-badge">Signature Platter</span>
          <h3>112 Signature Platter (36 Pcs)</h3>
          <p>Includes 1 Cherry Blossom Roll, 1 Upper Manhattan Roll, 1 Spicy Tuna Crunch, plus 12 pieces of assorted Salmon, Tuna, and Yellowtail Nigiri.</p>
          <div class="room112-card-footer">
            <span class="room112-price">$72.00</span>
            <span style="font-size:0.85rem; color:var(--room112-text-muted);">Feeds 6-8</span>
          </div>
        </div>
      </div>

      <div class="room112-card">
        <div class="room112-card-body">
          <span class="room112-card-badge">Executive Feast</span>
          <h3>Queen City Deluxe Banquet (54 Pcs)</h3>
          <p>Features 4 Specialty Rolls (Cherry Blossom, Pink Floyd, Dragon, Salmon Dream) and 22 pieces of sashimi-grade Nigiri &amp; Sashimi cuts.</p>
          <div class="room112-card-footer">
            <span class="room112-price">$115.00</span>
            <span style="font-size:0.85rem; color:var(--room112-text-muted);">Feeds 10-12</span>
          </div>
        </div>
      </div>

      <div class="room112-card">
        <div class="room112-card-body">
          <span class="room112-card-badge">Wok &amp; Dim Sum Tray</span>
          <h3>Bistro Party Box (Feeds 8-10)</h3>
          <p>A full catering pan of Honey Glazed Walnut Prawns or Tangerine Beef, 1 pan of Singapore Street Noodles, and 16 Crispy Crab Wontons.</p>
          <div class="room112-card-footer">
            <span class="room112-price">$125.00</span>
            <span style="font-size:0.85rem; color:var(--room112-text-muted);">Feeds 8-10</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Interactive Catering Calculator -->
    <div class="room112-section-title" style="margin-top:60px;">
      <h2>Interactive Corporate Catering Estimator</h2>
      <p>Estimate piece quantities, platter tray configurations, appetizer add-ons, and pricing for your upcoming Uptown gathering.</p>
    </div>

    <div class="room112-calc-box">
      <div class="room112-calc-row">
        <label for="calc-party-size">Number of Guests / Colleagues: <span id="calc-party-size-val" style="color:var(--room112-primary);">12 Guests / Colleagues</span></label>
        <input type="range" id="calc-party-size" min="6" max="60" step="2" value="12" class="room112-range-control">
      </div>

      <div class="room112-calc-row">
        <label for="calc-platter-tier">Select Catering Tier</label>
        <select id="calc-platter-tier" class="room112-select-control">
          <option value="19.50" selected>112 Deluxe Signature Sampler ($19.50 / guest - Specialty Rolls &amp; Nigiri)</option>
          <option value="24.50">Upper Manhattan Executive Tier ($24.50 / guest - Sashimi &amp; Luxury Maki)</option>
          <option value="16.50">Modern Asian Bistro Buffet ($16.50 / guest - Walnut Prawns &amp; Wok Noodles)</option>
        </select>
      </div>

      <div class="room112-calc-row">
        <label for="calc-dimsum-addon">Add Starter / Dim Sum Service</label>
        <select id="calc-dimsum-addon" class="room112-select-control">
          <option value="0" selected>No Starter Add-On</option>
          <option value="4.00">Add Crispy Crab Wontons &amp; Pork Dumplings (+$4.00 / guest)</option>
          <option value="4.50">Add Rock Shrimp Tempura &amp; Edamame (+$4.50 / guest)</option>
        </select>
      </div>

      <div class="room112-calc-results">
        <div class="room112-result-line">
          <span>Estimated Portion Count:</span>
          <strong id="calc-piece-info">Approx. 60 Handcrafted Pieces (~2 Room 112 Signature Trays)</strong>
        </div>
        <div class="room112-result-line">
          <span>Included Service Elements:</span>
          <strong id="calc-sides-info">Includes House Aged Soy, Wasabi, Pickled Ginger &amp; Chopstick Sets for 12</strong>
        </div>
        <div class="room112-result-total">
          <span>Estimated Total:</span>
          <span id="calc-total-price">$234.00</span>
        </div>
      </div>

      <div style="margin-top:24px; text-align:center;">
        <a href="tel:7043357112" class="room112-btn-hero-primary" style="display:inline-block; width:100%;">Call (704) 335-7112 to Order Executive Platters</a>
      </div>
    </div>

    <!-- Ordering Policies -->
    <div class="room112-grid-2" style="margin-top:50px;">
      <div class="room112-card" style="padding:28px;">
        <h4 style="color:var(--room112-dark); margin-bottom:10px;">Advance Ordering &amp; Delivery</h4>
        <p style="color:var(--room112-text-muted); font-size:0.95rem;">Small platter orders (1-2 trays) can be prepared with 1-2 hours advance notice during business hours. For large office presentations over 3 trays, please place orders 24 hours in advance.</p>
      </div>

      <div class="room112-card" style="padding:28px;">
        <h4 style="color:var(--room112-dark); margin-bottom:10px;">Individual Bento Box Lunches</h4>
        <p style="color:var(--room112-text-muted); font-size:0.95rem;">We also prepare individually packaged and labeled executive bento boxes for convenient boardroom meetings with custom dietary tags for gluten-free and vegetarian guests.</p>
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
  <title>Visit &amp; Hours | Room 112 Modern Asian Bistro Charlotte</title>
  <meta name="description" content="Plan your visit to Room 112 at 112 S Tryon St in Uptown Charlotte NC. Operating hours, reservations policy, Overstreet Mall walking access, and FAQs.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
{header_html("visit.html")}

  <section class="room112-hero" style="padding: 50px 20px;">
    <div class="room112-hero-inner">
      <span class="room112-hero-pill">Trade &amp; Tryon Square</span>
      <h1>Visit &amp; Operating Hours</h1>
      <p>Conveniently located at 112 South Tryon Street in the absolute center of Uptown Charlotte for power lunch, evening dinner, and craft cocktails.</p>
    </div>
  </section>

  <main class="room112-container">
    <div class="room112-visit-grid">
      <div class="room112-info-card">
        <h3>Location &amp; Contact</h3>
        
        <div class="room112-info-item">
          <strong>Street Address</strong>
          <p>112 S Tryon St<br>Charlotte, NC 28284<br>United States</p>
        </div>

        <div class="room112-info-item">
          <strong>Direct Phone Orders &amp; Reservations</strong>
          <p><a href="tel:7043357112" style="font-weight:700; font-size:1.15rem; color:var(--room112-primary);">(704) 335-7112</a></p>
        </div>

        <div class="room112-info-item">
          <strong>Email Inquiries</strong>
          <p><a href="mailto:contact@rm112.com">contact@rm112.com</a></p>
        </div>

        <div class="room112-info-item">
          <strong>Uptown Access &amp; Transit</strong>
          <p>Located on South Tryon Street between Trade and 4th Streets. Direct indoor walking access via the Charlotte Overstreet Mall. Directly connected to the CTC/Arena LYNX Blue Line station and City Center bus hub.</p>
        </div>
      </div>

      <div class="room112-info-card">
        <h3>Operating Hours</h3>
        
        <div class="room112-info-item">
          <strong>Monday - Friday</strong>
          <p>11:00 AM - 9:00 PM<br><small style="color:var(--room112-text-muted);">Lunch Rush (11am-2:30pm) | Evening Dinner &amp; Lounge (4:30pm-9pm)</small></p>
        </div>

        <div class="room112-info-item">
          <strong>Saturday</strong>
          <p>11:30 AM - 9:00 PM<br><small style="color:var(--room112-text-muted);">Weekend Dinner, Date Nights &amp; Craft Cocktails</small></p>
        </div>

        <div class="room112-info-item">
          <strong>Sunday</strong>
          <p>Closed for General Dining<br><small style="color:var(--room112-text-muted);">Available for Private Lounge Buyouts &amp; Corporate Receptions</small></p>
        </div>

        <div class="room112-info-item">
          <strong>Lunch Reservations Policy</strong>
          <p>Lunch service is walk-in / fast counter priority. Evening dinner reservations accepted for parties of 2 to 8 guests.</p>
        </div>
      </div>
    </div>

    <!-- FAQ Accordion -->
    <div class="room112-section-title" style="margin-top:60px;">
      <h2>Frequently Asked Questions</h2>
      <p>Essential details for your dining experience at Room 112.</p>
    </div>

    <div style="max-width:800px; margin:0 auto;">
      <div class="room112-accordion">
        <div class="room112-accordion-header">
          <span>Do you take reservations for lunch?</span>
          <span class="room112-accordion-icon">+</span>
        </div>
        <div class="room112-accordion-content">
          <p>During the busy weekday lunch hours (11:00 AM – 2:00 PM), seating is first-come, first-served to ensure quick table turnover for Uptown workers. Call-ahead takeout orders are prepared in 10-15 minutes.</p>
        </div>
      </div>

      <div class="room112-accordion">
        <div class="room112-accordion-header">
          <span>What are your most popular signature dishes?</span>
          <span class="room112-accordion-icon">+</span>
        </div>
        <div class="room112-accordion-content">
          <p>Our most famous creations are the Cherry Blossom Roll (salmon roses, spicy tuna, crab), Honey Glazed Walnut Prawns, Crispy Tangerine Beef, and the 112 Deluxe Sushi Sampler.</p>
        </div>
      </div>

      <div class="room112-accordion">
        <div class="room112-accordion-header">
          <span>Can you accommodate gluten-free or vegetarian guests?</span>
          <span class="room112-accordion-icon">+</span>
        </div>
        <div class="room112-accordion-content">
          <p>Yes, we offer gluten-free soy sauce (tamari), fresh sashimi cuts, vegetable maki rolls, edamame, and wok-seared vegetarian tofu entrees upon request.</p>
        </div>
      </div>

      <div class="room112-accordion">
        <div class="room112-accordion-header">
          <span>Are catering platters available for pickup or delivery?</span>
          <span class="room112-accordion-icon">+</span>
        </div>
        <div class="room112-accordion-content">
          <p>Yes, our 36-piece and 54-piece executive sushi platters and hot bistro trays are available for corporate pickup on South Tryon. Call (704) 335-7112 to arrange your order.</p>
        </div>
      </div>
    </div>

    <div class="room112-cta-banner" style="margin-top:50px;">
      <h2>We Look Forward to Seeing You</h2>
      <p>112 S Tryon St, Charlotte, NC 28284 | Call (704) 335-7112</p>
      <div class="room112-cta-btns">
        <a href="tel:7043357112" class="room112-btn-hero-primary">Call (704) 335-7112</a>
        <a href="menu.html" class="room112-btn-hero-secondary">Explore Menu</a>
      </div>
    </div>
  </main>

{footer_html()}'''

with open(os.path.join(DIR, "sushi-platters-and-executive-dining.html"), "w", encoding="utf-8") as f:
    f.write(platters_page)
print("Wrote sushi-platters-and-executive-dining.html")

with open(os.path.join(DIR, "visit.html"), "w", encoding="utf-8") as f:
    f.write(visit_page)
print("Wrote visit.html")
