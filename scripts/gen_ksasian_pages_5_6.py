# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\scripts")
from ksasian_builder import header_html, footer_html

DIR = r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\k-s-asian-xpress"

# 5. party-platters-and-family-bundles.html
party_page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Party Platters &amp; Family Bundles | K’s Asian Xpress Charlotte</title>
  <meta name="description" content="Feed your family or office gathering with generous Asian party platters, Hibachi bundles, dumpling trays, and wing packs in East Charlotte NC.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
</head>
<body>
{header_html("party-platters-and-family-bundles.html")}

  <section class="ksasian-hero" style="padding: 50px 20px;">
    <div class="ksasian-hero-inner">
      <span class="ksasian-hero-pill">Group Feasts &amp; Catering</span>
      <h1>Party Platters &amp; Family Bundles</h1>
      <p>Elevate your gameday watch party, office lunch, or family weekend dinner with generous party-sized hibachi pans, wok trays, and crispy appetizer samplers.</p>
    </div>
  </section>

  <main class="ksasian-container">
    <div class="ksasian-section-title">
      <h2>Curated Family &amp; Party Packages</h2>
      <p>All packages are packaged hot and ready for convenient counter pickup.</p>
    </div>

    <div class="ksasian-grid-3">
      <div class="ksasian-card">
        <div class="ksasian-card-body">
          <span class="ksasian-card-badge">Family Value</span>
          <h3>Family Hibachi Feast (Feeds 4-6)</h3>
          <p>Includes generous portions of Hibachi Steak &amp; Chicken, a large pan of egg fried rice, grilled zucchini &amp; mushrooms, 4 egg rolls, and 8 oz of Yum Yum sauce.</p>
          <div class="ksasian-card-footer">
            <span class="ksasian-price">$58.99</span>
            <span style="font-size:0.85rem; color:var(--ksasian-text-muted);">Feeds 4-6</span>
          </div>
        </div>
      </div>

      <div class="ksasian-card">
        <div class="ksasian-card-body">
          <span class="ksasian-card-badge">Office / Party Platter</span>
          <h3>Asian Wok &amp; Noodle Box (Feeds 8-10)</h3>
          <p>Choose 2 large wok entrees (General Tso, Beef Broccoli, or Honey Sesame), 1 pan of Pad Thai or Lo Mein, 1 pan of Fried Rice, and 12 Crab Rangoon.</p>
          <div class="ksasian-card-footer">
            <span class="ksasian-price">$119.99</span>
            <span style="font-size:0.85rem; color:var(--ksasian-text-muted);">Feeds 8-10</span>
          </div>
        </div>
      </div>

      <div class="ksasian-card">
        <div class="ksasian-card-body">
          <span class="ksasian-card-badge">Gameday Favorite</span>
          <h3>Wing &amp; Dumpling Sampler (30 Pcs)</h3>
          <p>15 Jumbo crispy wings in your choice of 2 sauces plus 15 pan-fried handmade pork potstickers with sweet chili and seasoned dumpling soy dips.</p>
          <div class="ksasian-card-footer">
            <span class="ksasian-price">$46.99</span>
            <span style="font-size:0.85rem; color:var(--ksasian-text-muted);">Feeds 6-8</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Interactive Catering Calculator -->
    <div class="ksasian-section-title" style="margin-top:60px;">
      <h2>Interactive Group Catering Estimator</h2>
      <p>Estimate the package price, sides, and sauce quantities needed for your group size.</p>
    </div>

    <div class="ksasian-calc-box">
      <div class="ksasian-calc-row">
        <label for="calc-guests">Number of Guests: <span id="calc-guests-val" style="color:var(--ksasian-primary);">12 Guests</span></label>
        <input type="range" id="calc-guests" min="6" max="60" step="2" value="12" class="ksasian-range-control">
      </div>

      <div class="ksasian-calc-row">
        <label for="calc-package-type">Select Catering Entree Package</label>
        <select id="calc-package-type" class="ksasian-select-control">
          <option value="14.50" selected>Family Hibachi Feast ($14.50 / person - Steak, Chicken &amp; Fried Rice)</option>
          <option value="13.50">Asian Wok &amp; Thai Combo ($13.50 / person - General Tso, Pad Thai &amp; Lo Mein)</option>
          <option value="16.50">Ultimate Supreme Asian Banquet ($16.50 / person - Hibachi Trio &amp; Wok Specials)</option>
        </select>
      </div>

      <div class="ksasian-calc-row">
        <label for="calc-dimsum-addon">Add Appetizer / Dim Sum Starter Pack</label>
        <select id="calc-dimsum-addon" class="ksasian-select-control">
          <option value="0" selected>No Starter Add-On</option>
          <option value="3.50">Add 2 Wings + 2 Dumplings per Person (+$3.50 / guest)</option>
          <option value="2.50">Add Crab Rangoon + Spring Rolls per Person (+$2.50 / guest)</option>
        </select>
      </div>

      <div class="ksasian-calc-results">
        <div class="ksasian-result-line">
          <span>Guest Capacity:</span>
          <strong id="calc-feeds-count">Serves 12 Hungry Guests with Generous Entree Portions</strong>
        </div>
        <div class="ksasian-result-line">
          <span>Included Rice &amp; Sauces:</span>
          <strong id="calc-sides-info">Includes 2 Large Pan(s) of Fried Rice/Noodles + 2 Pint(s) of Yum Yum Sauce</strong>
        </div>
        <div class="ksasian-result-total">
          <span>Estimated Total:</span>
          <span id="calc-total-price">$174.00</span>
        </div>
      </div>

      <div style="margin-top:24px; text-align:center;">
        <a href="tel:9802019962" class="ksasian-btn-hero-primary" style="display:inline-block; width:100%;">Call (980) 201-9962 to Place Catering Order</a>
      </div>
    </div>

    <!-- Ordering Guidelines -->
    <div class="ksasian-grid-2" style="margin-top:50px;">
      <div class="ksasian-card" style="padding:28px;">
        <h4 style="color:var(--ksasian-dark); margin-bottom:10px;">Pickup &amp; Advance Notice</h4>
        <p style="color:var(--ksasian-text-muted); font-size:0.95rem;">Standard family bundles can be ordered with just 20-30 minutes notice. For large party platters for 20+ guests, please call at least 2-3 hours in advance so our kitchen can prepare fresh hot batches.</p>
      </div>

      <div class="ksasian-card" style="padding:28px;">
        <h4 style="color:var(--ksasian-dark); margin-bottom:10px;">Custom Dietary Requests</h4>
        <p style="color:var(--ksasian-text-muted); font-size:0.95rem;">We can customize catering pans for gluten-sensitive guests (using rice noodles and gluten-free tamari upon request) and vegetarian groups (tofu hibachi, vegetable lo mein, spring rolls).</p>
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
  <title>Visit &amp; Hours | K’s Asian Xpress Charlotte NC</title>
  <meta name="description" content="Plan your visit to K’s Asian Xpress at 10102 Albemarle Rd in Charlotte NC. Operating hours, contact telephone, parking information, and FAQs.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
</head>
<body>
{header_html("visit.html")}

  <section class="ksasian-hero" style="padding: 50px 20px;">
    <div class="ksasian-hero-inner">
      <span class="ksasian-hero-pill">Albemarle Road Shopping Center</span>
      <h1>Visit &amp; Kitchen Hours</h1>
      <p>Stop by for fast counter service dine-in or call ahead for convenient hot takeout pickup in East Charlotte.</p>
    </div>
  </section>

  <main class="ksasian-container">
    <div class="ksasian-visit-grid">
      <div class="ksasian-info-card">
        <h3>Location &amp; Contact</h3>
        
        <div class="ksasian-info-item">
          <strong>Street Address</strong>
          <p>10102 Albemarle Rd, Suite 3<br>Charlotte, NC 28227<br>United States</p>
        </div>

        <div class="ksasian-info-item">
          <strong>Direct Phone Orders</strong>
          <p><a href="tel:9802019962" style="font-weight:700; font-size:1.15rem; color:var(--ksasian-primary);">(980) 201-9962</a></p>
        </div>

        <div class="ksasian-info-item">
          <strong>Email Inquiries</strong>
          <p><a href="mailto:orders@ksasianxpressclt.com">orders@ksasianxpressclt.com</a></p>
        </div>

        <div class="ksasian-info-item">
          <strong>Location &amp; Parking</strong>
          <p>Located in the Albemarle Road retail strip near Lawyers Road. Features ample free strip-mall parking spaces directly in front of the restaurant entrance for easy pickup.</p>
        </div>
      </div>

      <div class="ksasian-info-card">
        <h3>Kitchen Hours</h3>
        
        <div class="ksasian-info-item">
          <strong>Monday - Thursday</strong>
          <p>11:00 AM - 9:30 PM<br><small style="color:var(--ksasian-text-muted);">Lunch specials available 11:00 AM - 3:00 PM</small></p>
        </div>

        <div class="ksasian-info-item">
          <strong>Friday - Saturday</strong>
          <p>11:00 AM - 10:00 PM<br><small style="color:var(--ksasian-text-muted);">Late-night takeout &amp; weekend family bundles</small></p>
        </div>

        <div class="ksasian-info-item">
          <strong>Sunday</strong>
          <p>12:00 PM - 9:00 PM<br><small style="color:var(--ksasian-text-muted);">Sunday dinner &amp; express takeout</small></p>
        </div>

        <div class="ksasian-info-item">
          <strong>Service Styles</strong>
          <p>Casual Dine-In Counter | Phone Call-In Takeout | Delivery Platform Pickup</p>
        </div>
      </div>
    </div>

    <!-- FAQ Accordion -->
    <div class="ksasian-section-title" style="margin-top:60px;">
      <h2>Frequently Asked Questions</h2>
      <p>Common questions regarding ordering, preparation times, and dietary preferences.</p>
    </div>

    <div style="max-width:800px; margin:0 auto;">
      <div class="ksasian-accordion">
        <div class="ksasian-accordion-header">
          <span>How fast is takeout order preparation?</span>
          <span class="ksasian-accordion-icon">+</span>
        </div>
        <div class="ksasian-accordion-content">
          <p>Most standard individual and family takeout orders are prepared fresh from scratch in approximately 10 to 15 minutes after calling (980) 201-9962.</p>
        </div>
      </div>

      <div class="ksasian-accordion">
        <div class="ksasian-accordion-header">
          <span>Can I customize the spice levels of Thai dishes?</span>
          <span class="ksasian-accordion-icon">+</span>
        </div>
        <div class="ksasian-accordion-content">
          <p>Yes, all Thai noodle and curry dishes can be customized from Level 0 (Mild/No Spice) up to Level 3 (Thai Hot with fresh bird's eye chilies).</p>
        </div>
      </div>

      <div class="ksasian-accordion">
        <div class="ksasian-accordion-header">
          <span>Do you offer vegetarian and tofu options?</span>
          <span class="ksasian-accordion-icon">+</span>
        </div>
        <div class="ksasian-accordion-content">
          <p>Absolutely! We prepare Hibachi Tofu &amp; Vegetable platters, General Tso Tofu, Vegetable Pad Thai, Vegetable Lo Mein, and Crispy Spring Rolls.</p>
        </div>
      </div>

      <div class="ksasian-accordion">
        <div class="ksasian-accordion-header">
          <span>Are party platters available for same-day pickup?</span>
          <span class="ksasian-accordion-icon">+</span>
        </div>
        <div class="ksasian-accordion-content">
          <p>Yes, family bundles and small platters can be prepared with 30-45 minutes notice. Large group catering orders (20+ guests) are best ordered 2-3 hours ahead.</p>
        </div>
      </div>
    </div>

    <div class="ksasian-cta-banner" style="margin-top:50px;">
      <h2>We Look Forward to Cooking for You</h2>
      <p>10102 Albemarle Rd, Suite 3, Charlotte, NC 28227 | Call (980) 201-9962</p>
      <div class="ksasian-cta-btns">
        <a href="tel:9802019962" class="ksasian-btn-hero-primary">Call (980) 201-9962</a>
        <a href="menu.html" class="ksasian-btn-hero-secondary">Explore Menu</a>
      </div>
    </div>
  </main>

{footer_html()}'''

with open(os.path.join(DIR, "party-platters-and-family-bundles.html"), "w", encoding="utf-8") as f:
    f.write(party_page)
print("Wrote party-platters-and-family-bundles.html")

with open(os.path.join(DIR, "visit.html"), "w", encoding="utf-8") as f:
    f.write(visit_page)
print("Wrote visit.html")
