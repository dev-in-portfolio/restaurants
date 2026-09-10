# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("scripts")
from frenchquarter_builder import header_html, footer_html

# Page 5: gameday-tailgates-and-catering.html
catering_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gameday Tailgates &amp; Catering | French Quarter Restaurant Charlotte NC</title>
  <meta name="description" content="Order large party platters, gameday wing packages, and Louisiana catering from French Quarter Restaurant in Uptown Charlotte. Perfect for tailgates and office lunches.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("gameday-tailgates-and-catering.html")}

  <section class="fq-hero-compact">
    <div class="fq-container">
      <span class="fq-badge">Group Packages &amp; Stadium Tailgates</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Gameday Platters &amp; Corporate Catering</h1>
      <p style="font-size:1.1rem; color:#cbd5e1; max-width:720px; margin:0 auto;">Feed your crew with legendary Salt &amp; Pepper wings, slider party trays, and family-style gumbo pots in Uptown Charlotte.</p>
    </div>
  </section>

  <main class="fq-container" style="padding:60px 24px;">
    <!-- Interactive Calculator & Package Overview -->
    <div class="fq-grid-2" style="gap:40px; margin-bottom:60px; align-items:start;">
      <div>
        <span class="fq-pill-tag">Plan Your Gathering</span>
        <h2 style="font-size:2rem; color:#1e0a45; margin:15px 0; font-weight:800;">Turnkey Event &amp; Tailgate Feasts</h2>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:15px;">
          Whether you are hosting an Uptown Charlotte office luncheon, a football tailgate on Mint Street, or an at-home watch party, French Quarter Restaurant delivers proven crowd-pleasers packed hot and ready for convenient pickup.
        </p>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:20px;">
          All packages include appropriate serving utensils, condiments, house-made dressings, and sliced French bread where applicable.
        </p>
        
        <div class="fq-calc-box">
          <h3 style="color:#1e0a45; font-size:1.3rem; margin-bottom:12px;">Interactive Catering Estimator</h3>
          <p style="color:#4b5563; font-size:0.9rem; margin-bottom:14px;">Select your group size and occasion to calculate recommended food quantities:</p>
          
          <label style="font-weight:600; font-size:0.9rem; color:#374151;">Expected Number of Guests:</label>
          <select id="fq-calc-guests" class="fq-calc-select">
            <option value="10">10 Guests</option>
            <option value="15">15 Guests</option>
            <option value="20" selected>20 Guests</option>
            <option value="30">30 Guests</option>
            <option value="50">50 Guests</option>
          </select>

          <label style="font-weight:600; font-size:0.9rem; color:#374151;">Event / Occasion Type:</label>
          <select id="fq-calc-type" class="fq-calc-select">
            <option value="tailgate" selected>Panthers / Stadium Tailgate</option>
            <option value="office">Corporate Office Lunch</option>
            <option value="party">Casual House Party / Watch Event</option>
          </select>

          <div id="fq-calc-output" class="fq-calc-res">
            <!-- Populated via site.js -->
          </div>
        </div>
      </div>

      <div>
        <img src="images/salt-pepper-wings.jpg" alt="Party platters of Salt and Pepper Wings" style="width:100%; height:360px; object-fit:cover; border-radius:12px; box-shadow:var(--fq-shadow-lg); margin-bottom:25px;">
        <div style="background:#ffffff; border:1px solid #e5e7eb; border-radius:12px; padding:24px; box-shadow:var(--fq-shadow);">
          <h4 style="color:#1e0a45; font-size:1.15rem; margin-bottom:8px;">How to Place Group Orders</h4>
          <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:14px;">
            Please provide 2 to 24 hours advance notice for large party platters and gallon gumbo pots. Curbside pickup is available along Church Street.
          </p>
          <a href="tel:7043771715" class="fq-btn-primary" style="display:block; text-align:center;">Call (704) 377-1715 to Order</a>
        </div>
      </div>
    </div>

    <!-- Package Trays -->
    <h2 style="font-size:1.9rem; color:#1e0a45; text-align:center; margin-bottom:35px;">Signature Party Platters</h2>

    <div class="fq-grid-3" style="gap:28px; margin-bottom:60px;">
      <div class="fq-card">
        <h3 style="color:#1e0a45; margin-bottom:8px;">50-Piece Gameday Wings Platter</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">50 jumbo crispy wings. Choose up to two styles: Famous Salt &amp; Pepper, Cajun Dry Rub, or Bourbon BBQ. Served with fresh celery, carrots, ranch, and blue cheese.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e5e7eb; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.2rem;">$72.00</span>
          <span class="fq-pill-tag">Tailgate Essential</span>
        </div>
      </div>

      <div class="fq-card">
        <h3 style="color:#1e0a45; margin-bottom:8px;">Cajun Gumbo Party Pot (Gallon)</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Serves 10 - 12 guests. One full gallon of dark roux chicken and andouille gumbo, accompanied by a half-pan of steamed white rice and two loaves of sliced French bread.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e5e7eb; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.2rem;">$85.00</span>
          <span class="fq-pill-tag">Serves 10-12</span>
        </div>
      </div>

      <div class="fq-card">
        <h3 style="color:#1e0a45; margin-bottom:8px;">Assorted Po'boy &amp; Sub Tray</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">16 half-sized specialty subs on French baguettes: French Dip with au jus cups, Turkey Club, Roast Beef &amp; Cheddar, and Blackened Chicken.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e5e7eb; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.2rem;">$68.00</span>
          <span class="fq-pill-tag">16 Half Subs</span>
        </div>
      </div>

      <div class="fq-card">
        <h3 style="color:#1e0a45; margin-bottom:8px;">Cajun Chicken Pasta Party Pan</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Serves 8 - 10 guests. Full deep half-pan of penne pasta with blackened chicken strips, bell peppers, and creamy spiced Parmesan garlic sauce with garlic bread.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e5e7eb; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.2rem;">$78.00</span>
          <span class="fq-pill-tag">Serves 8-10</span>
        </div>
      </div>

      <div class="fq-card">
        <h3 style="color:#1e0a45; margin-bottom:8px;">Red Beans &amp; Rice Catering Pan</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Serves 10 - 12 guests. Half-pan of simmered New Orleans red beans and grilled sliced andouille sausage served with fluffy white rice.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e5e7eb; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.2rem;">$62.00</span>
          <span class="fq-pill-tag">Southern Feast</span>
        </div>
      </div>

      <div class="fq-card">
        <h3 style="color:#1e0a45; margin-bottom:8px;">Pub Garden Salad Bowl</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Serves 10 - 12 guests. Large bowl of fresh mixed greens, cucumbers, tomatoes, carrots, and croutons with two 8oz bottles of house dressings.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e5e7eb; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.2rem;">$38.00</span>
          <span class="fq-pill-tag">Fresh Side</span>
        </div>
      </div>
    </div>

    <!-- CTA Strip -->
    <div class="fq-banner-strip">
      <h2 style="color:#ffffff; font-size:2rem; margin-bottom:12px;">Need Custom Event Menus?</h2>
      <p style="color:#cbd5e1; max-width:650px; margin:0 auto 20px;">Contact our management team directly to coordinate special party timings, tax-exempt orders, or stadium drop-offs.</p>
      <a href="tel:7043771715" class="fq-btn-primary">Call (704) 377-1715</a>
    </div>
  </main>

{footer_html()}
"""

with open("french-quarter-restaurant/gameday-tailgates-and-catering.html", "w", encoding="utf-8") as f:
    f.write(catering_content)
print("Written: french-quarter-restaurant/gameday-tailgates-and-catering.html")

# Page 6: visit.html
visit_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Visit &amp; Hours | French Quarter Restaurant Charlotte NC</title>
  <meta name="description" content="Find French Quarter Restaurant at 321 S Church St in historic Brevard Court Uptown Charlotte. Hours, walking directions, parking info, and contact details.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("visit.html")}

  <section class="fq-hero-compact">
    <div class="fq-container">
      <span class="fq-badge">Brevard Court Entrance</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Visit French Quarter Restaurant</h1>
      <p style="font-size:1.1rem; color:#cbd5e1; max-width:720px; margin:0 auto;">Located at 321 South Church Street, right at the historic entrance to Brevard Court in Uptown Charlotte.</p>
    </div>
  </section>

  <main class="fq-container" style="padding:60px 24px;">
    <div class="fq-grid-2" style="gap:40px; margin-bottom:60px;">
      <!-- Contact & Directions -->
      <div class="fq-card" style="padding:32px;">
        <h2 style="color:#1e0a45; margin-top:0; font-size:1.6rem; border-bottom:2px solid #e5e7eb; padding-bottom:12px;">Location &amp; Contact</h2>
        
        <div style="margin:20px 0; line-height:1.8; color:#374151;">
          <p><strong>Physical Address:</strong><br>321 S Church St (Brevard Court Entrance)<br>Charlotte, NC 28202</p>
          <p><strong>Neighborhood:</strong> Uptown Charlotte / Third Ward</p>
          <p><strong>Phone:</strong> <a href="tel:7043771715" style="color:#d97706; font-weight:700;">(704) 377-1715</a></p>
          <p><strong>Email:</strong> <a href="mailto:info@frenchquartercharlotte.com" style="color:#d97706;">info@frenchquartercharlotte.com</a></p>
        </div>

        <h3 style="color:#1e0a45; font-size:1.25rem; margin-top:24px;">How to Find Us</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6;">
          We are located at 321 S Church Street on the west side of the street, right where the pedestrian cobblestone walkway of Brevard Court begins. Look for our classic wrought-iron French Quarter sign.
        </p>

        <h3 style="color:#1e0a45; font-size:1.25rem; margin-top:20px;">Parking &amp; Transit</h3>
        <ul style="color:#4b5563; font-size:0.95rem; line-height:1.6; padding-left:20px;">
          <li>Metered street parking along S Church St, S Mint St, and W 3rd St</li>
          <li>BB&amp;T / Truist Center Parking Deck (1 block east on 3rd St)</li>
          <li>Surface lots along Mint St adjacent to Truist Field and Romare Bearden Park</li>
          <li>CATS LYNX Blue Line: 3rd St / Convention Center Station (4-minute walk)</li>
        </ul>
      </div>

      <!-- Hours & Pub Policies -->
      <div class="fq-card" style="padding:32px;">
        <h2 style="color:#1e0a45; margin-top:0; font-size:1.6rem; border-bottom:2px solid #e5e7eb; padding-bottom:12px;">Hours of Operation</h2>
        
        <table style="width:100%; border-collapse:collapse; margin-top:20px; color:#374151; font-size:1rem;">
          <tr style="border-bottom:1px solid #f3f4f6;">
            <td style="padding:12px 0; font-weight:600;">Monday</td>
            <td style="padding:12px 0; text-align:right;">11:00 AM - 10:00 PM</td>
          </tr>
          <tr style="border-bottom:1px solid #f3f4f6;">
            <td style="padding:12px 0; font-weight:600;">Tuesday</td>
            <td style="padding:12px 0; text-align:right;">11:00 AM - 10:00 PM</td>
          </tr>
          <tr style="border-bottom:1px solid #f3f4f6;">
            <td style="padding:12px 0; font-weight:600;">Wednesday</td>
            <td style="padding:12px 0; text-align:right;">11:00 AM - 10:00 PM</td>
          </tr>
          <tr style="border-bottom:1px solid #f3f4f6;">
            <td style="padding:12px 0; font-weight:600;">Thursday</td>
            <td style="padding:12px 0; text-align:right;">11:00 AM - 10:00 PM</td>
          </tr>
          <tr style="border-bottom:1px solid #f3f4f6;">
            <td style="padding:12px 0; font-weight:600;">Friday</td>
            <td style="padding:12px 0; text-align:right;">11:00 AM - 11:00 PM</td>
          </tr>
          <tr style="border-bottom:1px solid #f3f4f6;">
            <td style="padding:12px 0; font-weight:600;">Saturday</td>
            <td style="padding:12px 0; text-align:right;">11:00 AM - 11:00 PM</td>
          </tr>
          <tr>
            <td style="padding:12px 0; font-weight:600;">Sunday</td>
            <td style="padding:12px 0; text-align:right;">12:00 PM - 9:00 PM (Gamedays 10:00 AM)</td>
          </tr>
        </table>

        <div style="background:#fef3c7; border:1px solid #fde68a; border-radius:8px; padding:16px; margin-top:24px;">
          <h4 style="color:#92400e; margin-bottom:4px;">Gameday &amp; Stadium Events</h4>
          <p style="color:#78350f; font-size:0.9rem; margin:0;">
            On Carolina Panthers and Charlotte FC home matchdays, our kitchen opens early for pre-game courtyard service. Patio tables fill up rapidly!
          </p>
        </div>
      </div>
    </div>

    <!-- Contact Banner -->
    <div class="fq-banner-strip">
      <h2 style="color:#ffffff; font-size:2rem; margin-bottom:12px;">We Look Forward to Welcoming You</h2>
      <p style="color:#cbd5e1; max-width:600px; margin:0 auto 20px;">Give us a call for takeout orders, daily specials, or large group arrangements.</p>
      <a href="tel:7043771715" class="fq-btn-primary">Call (704) 377-1715</a>
    </div>
  </main>

{footer_html()}
"""

with open("french-quarter-restaurant/visit.html", "w", encoding="utf-8") as f:
    f.write(visit_content)
print("Written: french-quarter-restaurant/visit.html")

