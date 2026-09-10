# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("scripts")
from halfpenny_builder import header_html, footer_html

# Page 5: office-catering-and-breakfast-boxes.html
catering_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Office Catering &amp; Breakfast Boxes | Halfpenny's Cafe Charlotte</title>
  <meta name="description" content="Order office breakfast sandwich crates, corporate box lunches, and 96oz travel coffee boxes from Halfpenny's Cafe in 301 S Tryon Uptown Charlotte.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("office-catering-and-breakfast-boxes.html")}

  <section class="halfpenny-hero-compact">
    <div class="halfpenny-container">
      <span class="halfpenny-badge">Corporate Tower Catering</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Office Catering &amp; Breakfast Boxes</h1>
      <p style="font-size:1.1rem; color:#cbd5e1; max-width:720px; margin:0 auto;">Reliable breakfast sandwich platters, executive boxed deli lunches, and hot coffee travelers for South Tryon towers.</p>
    </div>
  </section>

  <main class="halfpenny-container" style="padding:60px 24px;">
    <!-- Interactive Estimator & Overview -->
    <div class="halfpenny-grid-2" style="gap:40px; margin-bottom:60px; align-items:start;">
      <div>
        <span class="halfpenny-tag">Serving Uptown Offices</span>
        <h2 style="font-size:2rem; color:#0f172a; margin:15px 0; font-weight:800;">Convenient Concourse Catering</h2>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:15px;">
          Halfpenny's Cafe is the trusted catering partner for legal practices, banking groups, and corporate departments throughout Uptown Charlotte.
        </p>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:20px;">
          Whether you need 15 hot breakfast biscuits for a 7:30 AM client presentation or individual deli box lunches for a noon board meeting, we ensure every order is fresh, labeled, and complete with all condiments and paper goods.
        </p>
        
        <div class="halfpenny-calc-box">
          <h3 style="color:#0f172a; font-size:1.3rem; margin-bottom:12px;">Interactive Corporate Catering Calculator</h3>
          <p style="color:#4b5563; font-size:0.9rem; margin-bottom:14px;">Select your group size and meeting format:</p>
          
          <label style="font-weight:600; font-size:0.9rem; color:#374151;">Expected Attendees:</label>
          <select id="hp-calc-guests" class="halfpenny-calc-select">
            <option value="10">10 Attendees</option>
            <option value="15">15 Attendees</option>
            <option value="20" selected>20 Attendees</option>
            <option value="30">30 Attendees</option>
            <option value="50">50 Attendees</option>
          </select>

          <label style="font-weight:600; font-size:0.9rem; color:#374151;">Package Format:</label>
          <select id="hp-calc-type" class="halfpenny-calc-select">
            <option value="breakfast" selected>Hot Breakfast Biscuit Crate &amp; Coffee Box</option>
            <option value="deli">Executive Deli Boxed Lunches</option>
            <option value="buffet">Full Morning Boardroom Buffet Spread</option>
          </select>

          <div id="hp-calc-output" class="halfpenny-calc-res">
            <!-- Populated via site.js -->
          </div>
        </div>
      </div>

      <div>
        <img src="images/artisan-coffee-latte.jpg" alt="Hot coffee travelers and morning catering at Halfpenny's Cafe" style="width:100%; height:360px; object-fit:cover; border-radius:12px; box-shadow:var(--halfpenny-shadow-lg); margin-bottom:25px;">
        <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:24px; box-shadow:var(--halfpenny-shadow);">
          <h4 style="color:#0f172a; font-size:1.15rem; margin-bottom:8px;">How to Place Tower Orders</h4>
          <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:14px;">
            Please call our concourse counter at least 2 to 12 hours in advance for group trays. Pickup is fast and simple on the lower level of 301 S Tryon.
          </p>
          <a href="tel:7043429697" class="halfpenny-btn-primary" style="display:block; text-align:center;">Call Catering: (704) 342-9697</a>
        </div>
      </div>
    </div>

    <!-- Package Trays Grid -->
    <h2 style="font-size:1.9rem; color:#0f172a; text-align:center; margin-bottom:35px;">Signature Office Platters</h2>

    <div class="halfpenny-grid-3" style="gap:28px; margin-bottom:60px;">
      <div class="halfpenny-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Hot Biscuit Breakfast Crate (12 Biscuits)</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">12 made-to-order buttermilk biscuit sandwiches (6 Bacon Egg &amp; Cheddar, 4 Sausage Egg &amp; Cheese, 2 Egg &amp; Cheese) individually wrapped.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#b45309; font-size:1.2rem;">$85.00</span>
          <span class="halfpenny-tag">12 Biscuits</span>
        </div>
      </div>

      <div class="halfpenny-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">96oz Traveler Coffee Box</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Serves 8 - 10 cups. Insulated coffee container filled with freshly brewed medium or dark roast. Includes 10 cups, sleeves, sugars, and creamers.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#b45309; font-size:1.2rem;">$26.00</span>
          <span class="halfpenny-tag">96oz Carafe</span>
        </div>
      </div>

      <div class="halfpenny-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Executive Deli Lunch Box (Per Person)</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Choice of deli sandwich (Club, Tarragon Chicken Salad, Turkey Avocado, or Tuna Melt), bag of kettle chips, kosher pickle, and fresh baked cookie.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#b45309; font-size:1.2rem;">$15.50 / person</span>
          <span class="halfpenny-tag">Min 8 Boxes</span>
        </div>
      </div>

      <div class="halfpenny-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Fresh Bagel &amp; Pastry Platter (16pc)</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">8 assorted sliced bagels with cream cheese tubs, plus 8 fresh baked butter croissants and blueberry muffins with fruit preserves.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#b45309; font-size:1.2rem;">$48.00</span>
          <span class="halfpenny-tag">16 Pieces</span>
        </div>
      </div>

      <div class="halfpenny-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Crispy Hashbrown Party Pan</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Serves 10 - 12 guests. Half deep hotel pan of crispy golden seasoned hashbrown potatoes, accompanied by ketchup and hot sauce bottles.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#b45309; font-size:1.2rem;">$38.00</span>
          <span class="halfpenny-tag">Side Pan</span>
        </div>
      </div>

      <div class="halfpenny-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Fresh Seasonal Fruit Bowl</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Serves 10 - 12 guests. Large catering bowl filled with cut cantaloupe, honeydew melon, fresh pineapple, strawberries, and red grapes.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#b45309; font-size:1.2rem;">$45.00</span>
          <span class="halfpenny-tag">Fresh Fruit</span>
        </div>
      </div>
    </div>

    <!-- CTA Banner -->
    <div class="halfpenny-banner-strip">
      <h2 style="color:#ffffff; font-size:2rem; margin-bottom:12px;">Plan Your Office Meeting Breakfast</h2>
      <p style="color:#cbd5e1; max-width:650px; margin:0 auto 20px;">Contact our staff directly to arrange convenient concourse pickup or tower delivery.</p>
      <a href="tel:7043429697" class="halfpenny-btn-primary">Call (704) 342-9697</a>
    </div>
  </main>

{footer_html()}
"""

with open("halfpenny-s-cafe/office-catering-and-breakfast-boxes.html", "w", encoding="utf-8") as f:
    f.write(catering_content)
print("Written: halfpenny-s-cafe/office-catering-and-breakfast-boxes.html")

# Page 6: visit.html
visit_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Visit &amp; Hours | Halfpenny's Cafe 301 S Tryon Charlotte NC</title>
  <meta name="description" content="Find Halfpenny's Cafe on the lower concourse level of 301 S Tryon St (Suite 30) in Uptown Charlotte. Hours, building directions, transit, and phone number.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("visit.html")}

  <section class="halfpenny-hero-compact">
    <div class="halfpenny-container">
      <span class="halfpenny-badge">Two Wells Fargo / 301 S Tryon</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Visit Halfpenny's Cafe</h1>
      <p style="font-size:1.1rem; color:#cbd5e1; max-width:720px; margin:0 auto;">Located at 301 South Tryon Street, Suite 30, on the lower concourse level in Uptown Charlotte.</p>
    </div>
  </section>

  <main class="halfpenny-container" style="padding:60px 24px;">
    <div class="halfpenny-grid-2" style="gap:40px; margin-bottom:60px;">
      <!-- Contact & Directions -->
      <div class="halfpenny-card" style="padding:32px;">
        <h2 style="color:#0f172a; margin-top:0; font-size:1.6rem; border-bottom:2px solid #e2e8f0; padding-bottom:12px;">Location &amp; Contact</h2>
        
        <div style="margin:20px 0; line-height:1.8; color:#374151;">
          <p><strong>Physical Address:</strong><br>301 S Tryon St, Suite 30 (Lower Level Concourse)<br>Charlotte, NC 28282</p>
          <p><strong>Neighborhood:</strong> Uptown Charlotte / South Tryon Financial District</p>
          <p><strong>Phone:</strong> <a href="tel:7043429697" style="color:#b45309; font-weight:700;">(704) 342-9697</a></p>
          <p><strong>Email:</strong> <a href="mailto:info@halfpennyscafe.com" style="color:#b45309;">info@halfpennyscafe.com</a></p>
        </div>

        <h3 style="color:#0f172a; font-size:1.25rem; margin-top:24px;">How to Reach Our Lower Concourse Counter</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6;">
          Enter the main lobby of 301 S Tryon Street (Two Wells Fargo building). Take the central escalators or elevators down to the lower level retail concourse. We are located at Suite 30, directly along the concourse corridor.
        </p>

        <h3 style="color:#0f172a; font-size:1.25rem; margin-top:20px;">Transit &amp; Parking</h3>
        <ul style="color:#475569; font-size:0.95rem; line-height:1.6; padding-left:20px;">
          <li>CATS LYNX Blue Line: 3rd St / Convention Center Station (2-minute walk)</li>
          <li>Direct connection via Overstreet Mall pedestrian walkways</li>
          <li>Two Wells Fargo Parking Garage (underground building parking)</li>
          <li>Metered street parking on 3rd St, 4th St, and Church St</li>
        </ul>
      </div>

      <!-- Hours & Weekday Schedule -->
      <div class="halfpenny-card" style="padding:32px;">
        <h2 style="color:#0f172a; margin-top:0; font-size:1.6rem; border-bottom:2px solid #e2e8f0; padding-bottom:12px;">Concourse Hours</h2>
        
        <table style="width:100%; border-collapse:collapse; margin-top:20px; color:#374151; font-size:1rem;">
          <tr style="border-bottom:1px solid #f3f4f6;">
            <td style="padding:12px 0; font-weight:600;">Monday</td>
            <td style="padding:12px 0; text-align:right;">7:00 AM - 3:30 PM</td>
          </tr>
          <tr style="border-bottom:1px solid #f3f4f6;">
            <td style="padding:12px 0; font-weight:600;">Tuesday</td>
            <td style="padding:12px 0; text-align:right;">7:00 AM - 3:30 PM</td>
          </tr>
          <tr style="border-bottom:1px solid #f3f4f6;">
            <td style="padding:12px 0; font-weight:600;">Wednesday</td>
            <td style="padding:12px 0; text-align:right;">7:00 AM - 3:30 PM</td>
          </tr>
          <tr style="border-bottom:1px solid #f3f4f6;">
            <td style="padding:12px 0; font-weight:600;">Thursday</td>
            <td style="padding:12px 0; text-align:right;">7:00 AM - 3:30 PM</td>
          </tr>
          <tr style="border-bottom:1px solid #f3f4f6;">
            <td style="padding:12px 0; font-weight:600;">Friday</td>
            <td style="padding:12px 0; text-align:right;">7:00 AM - 3:00 PM</td>
          </tr>
          <tr style="border-bottom:1px solid #f3f4f6;">
            <td style="padding:12px 0; font-weight:600;">Saturday</td>
            <td style="padding:12px 0; text-align:right; color:#94a3b8;">Closed</td>
          </tr>
          <tr>
            <td style="padding:12px 0; font-weight:600;">Sunday</td>
            <td style="padding:12px 0; text-align:right; color:#94a3b8;">Closed</td>
          </tr>
        </table>

        <div style="background:#fef3c7; border:1px solid #fde68a; border-radius:8px; padding:16px; margin-top:24px;">
          <h4 style="color:#92400e; margin-bottom:4px;">Express Morning Pickup</h4>
          <p style="color:#78350f; font-size:0.9rem; margin:0;">
            Call your biscuit or lunch order ahead to (704) 342-9697 and your food will be bagged and waiting on the counter when you arrive.
          </p>
        </div>
      </div>
    </div>

    <!-- Contact Banner -->
    <div class="halfpenny-banner-strip">
      <h2 style="color:#ffffff; font-size:2rem; margin-bottom:12px;">We Look Forward to Serving You</h2>
      <p style="color:#cbd5e1; max-width:600px; margin:0 auto 20px;">Visit our concourse counter at 301 S Tryon or call ahead for prompt preparation.</p>
      <a href="tel:7043429697" class="halfpenny-btn-primary">Call (704) 342-9697</a>
    </div>
  </main>

{footer_html()}
"""

with open("halfpenny-s-cafe/visit.html", "w", encoding="utf-8") as f:
    f.write(visit_content)
print("Written: halfpenny-s-cafe/visit.html")

