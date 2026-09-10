# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("scripts")
from lotties_builder import header_html, footer_html

# Page 5: morning-catering-and-coffee-boxes.html
catering_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Morning Catering &amp; Coffee Boxes | Lottie's Cafe Charlotte NC</title>
  <meta name="description" content="Order breakfast catering, bakery croissant trays, and 96oz travel coffee boxes from Lottie's Cafe in Uptown Charlotte. Perfect for corporate meetings.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("morning-catering-and-coffee-boxes.html")}

  <section class="lottie-hero-compact">
    <div class="lottie-container">
      <span class="lottie-badge">Corporate Breakfast &amp; Meetings</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Morning Catering &amp; Coffee Boxes</h1>
      <p style="font-size:1.1rem; color:#f5f5f4; max-width:720px; margin:0 auto;">Turnkey breakfast packages, artisan sandwich boxes, freshly baked pastry crates, and insulated coffee carafes for Uptown Charlotte.</p>
    </div>
  </section>

  <main class="lottie-container" style="padding:60px 24px;">
    <!-- Interactive Estimator & Overview -->
    <div class="lottie-grid-2" style="gap:40px; margin-bottom:60px; align-items:start;">
      <div>
        <span class="lottie-tag">Powering Uptown Meetings</span>
        <h2 style="font-size:2rem; color:#451a03; margin:15px 0; font-weight:800;">Seamless Office Breakfast Catering</h2>
        <p style="color:#57534e; line-height:1.7; margin-bottom:15px;">
          Elevate your morning corporate meetings, board presentations, and team workshops with scratch-made breakfast from Lottie's Cafe.
        </p>
        <p style="color:#57534e; line-height:1.7; margin-bottom:20px;">
          All coffee carafes include compostable cups, lids, sleeves, stirrers, raw sugars, and fresh dairy and oat milk creamers.
        </p>
        
        <div class="lottie-calc-box">
          <h3 style="color:#451a03; font-size:1.3rem; margin-bottom:12px;">Interactive Morning Meeting Calculator</h3>
          <p style="color:#57534e; font-size:0.9rem; margin-bottom:14px;">Select your group size and meeting package format:</p>
          
          <label style="font-weight:600; font-size:0.9rem; color:#44403c;">Expected Attendees:</label>
          <select id="lottie-calc-guests" class="lottie-calc-select">
            <option value="10">10 Attendees</option>
            <option value="15">15 Attendees</option>
            <option value="20" selected>20 Attendees</option>
            <option value="30">30 Attendees</option>
            <option value="50">50 Attendees</option>
          </select>

          <label style="font-weight:600; font-size:0.9rem; color:#44403c;">Package Type:</label>
          <select id="lottie-calc-type" class="lottie-calc-select">
            <option value="breakfast" selected>Full Breakfast Sandwiches &amp; Coffee Box</option>
            <option value="pastry">Continental Bakery Croissant &amp; Fruit Spread</option>
            <option value="lunch">Executive Lunch Paninis &amp; Cold Brew Carafes</option>
          </select>

          <div id="lottie-calc-output" class="lottie-calc-res">
            <!-- Populated via site.js -->
          </div>
        </div>
      </div>

      <div>
        <img src="images/fresh-pastries-croissants.jpg" alt="Bakery croissants and morning pastries at Lottie's Cafe" style="width:100%; height:360px; object-fit:cover; border-radius:12px; box-shadow:var(--lottie-shadow-lg); margin-bottom:25px;">
        <div style="background:#ffffff; border:1px solid #e7e5e4; border-radius:12px; padding:24px; box-shadow:var(--lottie-shadow);">
          <h4 style="color:#451a03; font-size:1.15rem; margin-bottom:8px;">How to Place Catering Orders</h4>
          <p style="color:#57534e; font-size:0.95rem; line-height:1.6; margin-bottom:14px;">
            We recommend placing morning catering orders 12 to 24 hours in advance. Urgent same-morning coffee boxes can be prepared in 30 minutes.
          </p>
          <a href="tel:7047893135" class="lottie-btn-primary" style="display:block; text-align:center;">Call Catering: (704) 789-3135</a>
        </div>
      </div>
    </div>

    <!-- Package Trays Grid -->
    <h2 style="font-size:1.9rem; color:#451a03; text-align:center; margin-bottom:35px;">Signature Catering Packages</h2>

    <div class="lottie-grid-3" style="gap:28px; margin-bottom:60px;">
      <div class="lottie-card">
        <h3 style="color:#451a03; margin-bottom:8px;">Breakfast Brioche Crate (12 Sandwiches)</h3>
        <p style="color:#57534e; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">12 individually wrapped breakfast sandwiches: 6 Bacon Egg &amp; Cheddar, 3 Sausage Egg &amp; Gouda, and 3 Avocado Egg &amp; Tomato on brioche.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e7e5e4; padding-top:12px;">
          <span style="font-weight:700; color:#ea580c; font-size:1.2rem;">$115.00</span>
          <span class="lottie-tag">12 Sandwiches</span>
        </div>
      </div>

      <div class="lottie-card">
        <h3 style="color:#451a03; margin-bottom:8px;">96oz Traveler Coffee Box</h3>
        <p style="color:#57534e; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Serves 8 - 10 cups. Insulated dispenser filled with fresh-brewed single-origin drip coffee. Includes 10 cups, lids, sleeves, sugars, and oat/dairy milks.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e7e5e4; padding-top:12px;">
          <span style="font-weight:700; color:#ea580c; font-size:1.2rem;">$28.00</span>
          <span class="lottie-tag">96oz Carafe</span>
        </div>
      </div>

      <div class="lottie-card">
        <h3 style="color:#451a03; margin-bottom:8px;">Beattie's Bagel Box (Dozen)</h3>
        <p style="color:#57534e; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">12 assorted fresh Beattie's bagels sliced and served with two 8oz tubs of plain and whipped chive cream cheese, sweet butter, and preserves.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e7e5e4; padding-top:12px;">
          <span style="font-weight:700; color:#ea580c; font-size:1.2rem;">$38.00</span>
          <span class="lottie-tag">12 Bagels</span>
        </div>
      </div>

      <div class="lottie-card">
        <h3 style="color:#451a03; margin-bottom:8px;">Artisanal Bakery Basket (16pc)</h3>
        <p style="color:#57534e; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Assortment of 16 fresh-baked pastries: butter croissants, almond cream croissants, blueberry lemon scones, and chocolate chip muffins.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e7e5e4; padding-top:12px;">
          <span style="font-weight:700; color:#ea580c; font-size:1.2rem;">$55.00</span>
          <span class="lottie-tag">16 Pastries</span>
        </div>
      </div>

      <div class="lottie-card">
        <h3 style="color:#451a03; margin-bottom:8px;">Avocado Tartine Platter</h3>
        <p style="color:#57534e; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Serves 8 - 10 guests. 10 thick slices of toasted sourdough topped with smashed avocado, cherry tomatoes, pickled shallots, everything seasoning, and microgreens.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e7e5e4; padding-top:12px;">
          <span style="font-weight:700; color:#ea580c; font-size:1.2rem;">$75.00</span>
          <span class="lottie-tag">Tartine Tray</span>
        </div>
      </div>

      <div class="lottie-card">
        <h3 style="color:#451a03; margin-bottom:8px;">Executive Lunch Panini Tray (12 Half Subs)</h3>
        <p style="color:#451a03; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">12 half-paninis on focaccia and ciabatta (Turkey Avocado, Tuscan Caprese, Roast Beef Cheddar) with individual kettle chips.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e7e5e4; padding-top:12px;">
          <span style="font-weight:700; color:#ea580c; font-size:1.2rem;">$78.00</span>
          <span class="lottie-tag">Lunch Platter</span>
        </div>
      </div>
    </div>

    <!-- CTA Banner -->
    <div class="lottie-banner-strip">
      <h2 style="color:#ffffff; font-size:2rem; margin-bottom:12px;">Book Morning Catering for Your Team</h2>
      <p style="color:#fed7aa; max-width:650px; margin:0 auto 20px;">Contact our catering team directly to set up recurring office coffee orders or special event breakfasts.</p>
      <a href="tel:7047893135" class="lottie-btn-primary">Call (704) 789-3135</a>
    </div>
  </main>

{footer_html()}
"""

with open("lottie-s-cafe/morning-catering-and-coffee-boxes.html", "w", encoding="utf-8") as f:
    f.write(catering_content)
print("Written: lottie-s-cafe/morning-catering-and-coffee-boxes.html")

# Page 6: visit.html
visit_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Visit &amp; Hours | Lottie's Cafe Uptown Charlotte NC</title>
  <meta name="description" content="Plan your visit to Lottie's Cafe at 210 E Trade St in Queen City Quarter, Uptown Charlotte. Hours, Light Rail transit access, directions, and phone number.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("visit.html")}

  <section class="lottie-hero-compact">
    <div class="lottie-container">
      <span class="lottie-badge">Queen City Quarter Hub</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Visit Lottie's Cafe</h1>
      <p style="font-size:1.1rem; color:#f5f5f4; max-width:720px; margin:0 auto;">Located at 210 East Trade Street, inside Queen City Quarter in the center of Uptown Charlotte.</p>
    </div>
  </section>

  <main class="lottie-container" style="padding:60px 24px;">
    <div class="lottie-grid-2" style="gap:40px; margin-bottom:60px;">
      <!-- Contact & Directions -->
      <div class="lottie-card" style="padding:32px;">
        <h2 style="color:#451a03; margin-top:0; font-size:1.6rem; border-bottom:2px solid #e7e5e4; padding-bottom:12px;">Location &amp; Contact</h2>
        
        <div style="margin:20px 0; line-height:1.8; color:#44403c;">
          <p><strong>Physical Address:</strong><br>210 E Trade St (Queen City Quarter)<br>Charlotte, NC 28202</p>
          <p><strong>Neighborhood:</strong> Uptown Charlotte / Center City</p>
          <p><strong>Phone:</strong> <a href="tel:7047893135" style="color:#ea580c; font-weight:700;">(704) 789-3135</a></p>
          <p><strong>Email:</strong> <a href="mailto:info@lottiesclt.com" style="color:#ea580c;">info@lottiesclt.com</a></p>
        </div>

        <h3 style="color:#451a03; font-size:1.25rem; margin-top:24px;">Finding Us in Queen City Quarter</h3>
        <p style="color:#57534e; font-size:0.95rem; line-height:1.6;">
          Enter the central plaza of Queen City Quarter from East Trade Street or College Street. We are located on the ground promenade level directly next to the CATS light rail pedestrian bridge.
        </p>

        <h3 style="color:#451a03; font-size:1.25rem; margin-top:20px;">Parking &amp; Transit Options</h3>
        <ul style="color:#57534e; font-size:0.95rem; line-height:1.6; padding-left:20px;">
          <li>Direct access from CATS LYNX Blue Line: CTC / Arena Station</li>
          <li>CATS CityLYNX Gold Line: CTC / Arena Stop</li>
          <li>Underground parking garage at Queen City Quarter (enter via Trade St or 4th St)</li>
          <li>7th Street Station Parking Deck (2 blocks north)</li>
        </ul>
      </div>

      <!-- Hours & Ordering Policies -->
      <div class="lottie-card" style="padding:32px;">
        <h2 style="color:#451a03; margin-top:0; font-size:1.6rem; border-bottom:2px solid #e7e5e4; padding-bottom:12px;">Cafe Hours</h2>
        
        <table style="width:100%; border-collapse:collapse; margin-top:20px; color:#44403c; font-size:1rem;">
          <tr style="border-bottom:1px solid #f5f5f4;">
            <td style="padding:12px 0; font-weight:600;">Monday</td>
            <td style="padding:12px 0; text-align:right;">7:00 AM - 4:00 PM</td>
          </tr>
          <tr style="border-bottom:1px solid #f5f5f4;">
            <td style="padding:12px 0; font-weight:600;">Tuesday</td>
            <td style="padding:12px 0; text-align:right;">7:00 AM - 4:00 PM</td>
          </tr>
          <tr style="border-bottom:1px solid #f5f5f4;">
            <td style="padding:12px 0; font-weight:600;">Wednesday</td>
            <td style="padding:12px 0; text-align:right;">7:00 AM - 4:00 PM</td>
          </tr>
          <tr style="border-bottom:1px solid #f5f5f4;">
            <td style="padding:12px 0; font-weight:600;">Thursday</td>
            <td style="padding:12px 0; text-align:right;">7:00 AM - 4:00 PM</td>
          </tr>
          <tr style="border-bottom:1px solid #f5f5f4;">
            <td style="padding:12px 0; font-weight:600;">Friday</td>
            <td style="padding:12px 0; text-align:right;">7:00 AM - 4:00 PM</td>
          </tr>
          <tr style="border-bottom:1px solid #f5f5f4;">
            <td style="padding:12px 0; font-weight:600;">Saturday</td>
            <td style="padding:12px 0; text-align:right;">7:00 AM - 4:00 PM</td>
          </tr>
          <tr>
            <td style="padding:12px 0; font-weight:600;">Sunday</td>
            <td style="padding:12px 0; text-align:right;">8:00 AM - 4:00 PM</td>
          </tr>
        </table>

        <div style="background:#fff7ed; border:1px solid #fed7aa; border-radius:8px; padding:16px; margin-top:24px;">
          <h4 style="color:#9a3412; margin-bottom:4px;">All-Day Kitchen &amp; Espresso</h4>
          <p style="color:#7c2d12; font-size:0.9rem; margin:0;">
            Our full breakfast and espresso menu is served throughout all open hours until 4:00 PM daily.
          </p>
        </div>
      </div>
    </div>

    <!-- Contact Banner -->
    <div class="lottie-banner-strip">
      <h2 style="color:#ffffff; font-size:2rem; margin-bottom:12px;">We Look Forward to Welcoming You</h2>
      <p style="color:#fed7aa; max-width:600px; margin:0 auto 20px;">Call ahead for rapid counter pickup or to arrange your office breakfast order.</p>
      <a href="tel:7047893135" class="lottie-btn-primary">Call (704) 789-3135</a>
    </div>
  </main>

{footer_html()}
"""

with open("lottie-s-cafe/visit.html", "w", encoding="utf-8") as f:
    f.write(visit_content)
print("Written: lottie-s-cafe/visit.html")

