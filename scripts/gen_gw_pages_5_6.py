# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("scripts")
from gw_builder import header_html, footer_html

# Page 5: family-feasts-and-catering.html
catering_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Family Feasts &amp; Catering | Great Wok Chinese Takeout Charlotte NC</title>
  <meta name="description" content="Order party pans and family dinner feasts from Great Wok in Uptown Charlotte. Half and full pans of General Tso's chicken, Lo Mein, fried rice, and egg rolls.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("family-feasts-and-catering.html")}

  <section class="gw-hero-compact">
    <div class="gw-container">
      <span class="gw-badge">Party Trays &amp; Office Feasts</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Family Feasts &amp; Group Catering Trays</h1>
      <p style="font-size:1.1rem; color:#cbd5e1; max-width:720px; margin:0 auto;">Generous party-size pans of Chinese classics for office lunches, university student events, and family gatherings.</p>
    </div>
  </section>

  <main class="gw-container" style="padding:60px 24px;">
    <!-- Interactive Estimator & Catering Overview -->
    <div class="gw-grid-2" style="gap:40px; margin-bottom:60px; align-items:start;">
      <div>
        <span class="gw-tag">Feed the Entire Team</span>
        <h2 style="font-size:2rem; color:#0f172a; margin:15px 0; font-weight:800;">Turnkey Catering Solutions in Uptown</h2>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:15px;">
          Whether you are feeding a corporate department at Gateway Village, hosting a study session at Johnson &amp; Wales, or having family over for dinner, Great Wok makes group dining easy and affordable.
        </p>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:20px;">
          Our catering pans come piping hot with serving spoons, fortune cookies, soy sauce packets, and duck sauce.
        </p>
        
        <div class="gw-calc-box">
          <h3 style="color:#0f172a; font-size:1.3rem; margin-bottom:12px;">Interactive Catering &amp; Feast Calculator</h3>
          <p style="color:#4b5563; font-size:0.9rem; margin-bottom:14px;">Select your group size and catering format:</p>
          
          <label style="font-weight:600; font-size:0.9rem; color:#374151;">Expected Number of Guests:</label>
          <select id="gw-calc-guests" class="gw-calc-select">
            <option value="10">10 Guests</option>
            <option value="15">15 Guests</option>
            <option value="20" selected>20 Guests</option>
            <option value="30">30 Guests</option>
            <option value="50">50 Guests</option>
          </select>

          <label style="font-weight:600; font-size:0.9rem; color:#374151;">Catering Package Format:</label>
          <select id="gw-calc-type" class="gw-calc-select">
            <option value="family" selected>Buffet-Style Family Party Pans</option>
            <option value="office">Individual Combination Bento Boxes</option>
            <option value="deluxe">Deluxe Seafood &amp; Dim Sum Buffet</option>
          </select>

          <div id="gw-calc-output" class="gw-calc-res">
            <!-- Populated via site.js -->
          </div>
        </div>
      </div>

      <div>
        <img src="images/steamed-dumplings-dimsum.jpg" alt="Steamed dumplings and dim sum platters at Great Wok" style="width:100%; height:360px; object-fit:cover; border-radius:12px; box-shadow:var(--gw-shadow-lg); margin-bottom:25px;">
        <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:24px; box-shadow:var(--gw-shadow);">
          <h4 style="color:#0f172a; font-size:1.15rem; margin-bottom:8px;">How to Order Group Trays</h4>
          <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:14px;">
            Please provide 1 to 3 hours notice for large catering orders. Quick curbside pickup is available at 718 W Trade Street.
          </p>
          <a href="tel:7043330080" class="gw-btn-primary" style="display:block; text-align:center;">Call (704) 333-0080 to Order</a>
        </div>
      </div>
    </div>

    <!-- Package Trays Grid -->
    <h2 style="font-size:1.9rem; color:#0f172a; text-align:center; margin-bottom:35px;">Signature Catering Trays</h2>

    <div class="gw-grid-3" style="gap:28px; margin-bottom:60px;">
      <div class="gw-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">General Tso's Party Pan (Half Pan)</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Serves 8 - 10 guests. Full half-deep hotel pan of crispy General Tso's chicken with broccoli florets, accompanied by a separate pan of white or fried rice.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#dc2626; font-size:1.2rem;">$65.00</span>
          <span class="gw-tag">Serves 8-10</span>
        </div>
      </div>

      <div class="gw-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">House Special Lo Mein Party Pan</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Serves 8 - 10 guests. Half hotel pan of egg noodles tossed with shrimp, chicken, roast pork, and crisp vegetables in savory brown sauce.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#dc2626; font-size:1.2rem;">$55.00</span>
          <span class="gw-tag">Serves 8-10</span>
        </div>
      </div>

      <div class="gw-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Pork Fried Rice Catering Pan</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Serves 10 - 12 guests. Half pan of wok-charred jasmine fried rice with diced roast pork, egg, onions, and sweet peas.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#dc2626; font-size:1.2rem;">$42.00</span>
          <span class="gw-tag">Side Pan</span>
        </div>
      </div>

      <div class="gw-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Egg Roll &amp; Rangoon Platter (24pc)</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">12 crispy pork egg rolls and 12 fried cream cheese crab rangoons, served with sweet duck sauce and spicy Chinese mustard.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#dc2626; font-size:1.2rem;">$45.00</span>
          <span class="gw-tag">24 Pieces</span>
        </div>
      </div>

      <div class="gw-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Steamed Dumpling Tray (30pc)</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">30 handmade steamed pork and scallion dumplings packed in a party tray with a large tub of ginger soy dipping sauce.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#dc2626; font-size:1.2rem;">$48.00</span>
          <span class="gw-tag">30 Dumplings</span>
        </div>
      </div>

      <div class="gw-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Sesame Chicken Party Pan</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Serves 8 - 10 guests. Half hotel pan of crispy sweet honey sesame chicken with broccoli florets and a separate pan of jasmine white rice.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#dc2626; font-size:1.2rem;">$65.00</span>
          <span class="gw-tag">Serves 8-10</span>
        </div>
      </div>
    </div>

    <!-- CTA Banner -->
    <div class="gw-banner-strip">
      <h2 style="color:#ffffff; font-size:2rem; margin-bottom:12px;">Place Your Group Catering Order Today</h2>
      <p style="color:#cbd5e1; max-width:650px; margin:0 auto 20px;">Call our counter staff directly to arrange exact pickup timing and dietary requests.</p>
      <a href="tel:7043330080" class="gw-btn-primary">Call (704) 333-0080</a>
    </div>
  </main>

{footer_html()}
"""

with open("great-wok/family-feasts-and-catering.html", "w", encoding="utf-8") as f:
    f.write(catering_content)
print("Written: great-wok/family-feasts-and-catering.html")

# Page 6: visit.html
visit_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Visit &amp; Hours | Great Wok Chinese Takeout Charlotte NC</title>
  <meta name="description" content="Find Great Wok at 718 W Trade St Suite M in Uptown Charlotte Gateway Village. Hours, pickup counter instructions, parking info, and telephone contact.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("visit.html")}

  <section class="gw-hero-compact">
    <div class="gw-container">
      <span class="gw-badge">Gateway Village Corridor</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Visit Great Wok Chinese Kitchen</h1>
      <p style="font-size:1.1rem; color:#cbd5e1; max-width:720px; margin:0 auto;">Located at 718 West Trade Street, Suite M, right in the Gateway Village complex in Uptown Charlotte.</p>
    </div>
  </section>

  <main class="gw-container" style="padding:60px 24px;">
    <div class="gw-grid-2" style="gap:40px; margin-bottom:60px;">
      <!-- Contact & Directions -->
      <div class="gw-card" style="padding:32px;">
        <h2 style="color:#0f172a; margin-top:0; font-size:1.6rem; border-bottom:2px solid #e2e8f0; padding-bottom:12px;">Location &amp; Contact</h2>
        
        <div style="margin:20px 0; line-height:1.8; color:#374151;">
          <p><strong>Physical Address:</strong><br>718 W Trade St, Suite M<br>Charlotte, NC 28202</p>
          <p><strong>Neighborhood:</strong> Uptown Charlotte / Gateway Village / Fourth Ward</p>
          <p><strong>Phone:</strong> <a href="tel:7043330080" style="color:#dc2626; font-weight:700;">(704) 333-0080</a></p>
          <p><strong>Email:</strong> <a href="mailto:orders@charlottegreatwok.com" style="color:#dc2626;">orders@charlottegreatwok.com</a></p>
        </div>

        <h3 style="color:#0f172a; font-size:1.25rem; margin-top:24px;">Storefront Location</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6;">
          We are located on West Trade Street near Cedar Street, directly across from the Johnson &amp; Wales University campus in the Gateway Village retail center.
        </p>

        <h3 style="color:#0f172a; font-size:1.25rem; margin-top:20px;">Parking &amp; Pickup Options</h3>
        <ul style="color:#4b5563; font-size:0.95rem; line-height:1.6; padding-left:20px;">
          <li>Free short-term pickup parking bays in the Gateway Village retail surface lot</li>
          <li>Metered on-street parking on W Trade St and Cedar St</li>
          <li>Gateway Village Parking Deck adjacent to the center</li>
          <li>CATS CityLYNX Gold Line: Gateway Station (1-minute walk)</li>
        </ul>
      </div>

      <!-- Hours & Ordering Policies -->
      <div class="gw-card" style="padding:32px;">
        <h2 style="color:#0f172a; margin-top:0; font-size:1.6rem; border-bottom:2px solid #e2e8f0; padding-bottom:12px;">Hours of Operation</h2>
        
        <table style="width:100%; border-collapse:collapse; margin-top:20px; color:#374151; font-size:1rem;">
          <tr style="border-bottom:1px solid #f3f4f6;">
            <td style="padding:12px 0; font-weight:600;">Monday - Thursday</td>
            <td style="padding:12px 0; text-align:right;">11:00 AM - 9:30 PM</td>
          </tr>
          <tr style="border-bottom:1px solid #f3f4f6;">
            <td style="padding:12px 0; font-weight:600;">Friday</td>
            <td style="padding:12px 0; text-align:right;">11:00 AM - 10:00 PM</td>
          </tr>
          <tr style="border-bottom:1px solid #f3f4f6;">
            <td style="padding:12px 0; font-weight:600;">Saturday</td>
            <td style="padding:12px 0; text-align:right;">12:00 PM - 10:00 PM</td>
          </tr>
          <tr>
            <td style="padding:12px 0; font-weight:600;">Sunday</td>
            <td style="padding:12px 0; text-align:right; color:#dc2626; font-weight:600;">Closed</td>
          </tr>
        </table>

        <div style="background:#fef2f2; border:1px solid #fecaca; border-radius:8px; padding:16px; margin-top:24px;">
          <h4 style="color:#991b1b; margin-bottom:4px;">Lunch Special Times</h4>
          <p style="color:#7f1d1d; font-size:0.9rem; margin:0;">
            Lunch combination specials are served Monday through Friday from 11:00 AM to 3:00 PM, featuring choice of entree with roast pork fried rice and egg roll.
          </p>
        </div>
      </div>
    </div>

    <!-- Contact Banner -->
    <div class="gw-banner-strip">
      <h2 style="color:#ffffff; font-size:2rem; margin-bottom:12px;">Ready for Sizzling Chinese Food?</h2>
      <p style="color:#cbd5e1; max-width:600px; margin:0 auto 20px;">Call ahead and we will have your food packed hot and fresh for fast pickup.</p>
      <a href="tel:7043330080" class="gw-btn-primary">Call (704) 333-0080</a>
    </div>
  </main>

{footer_html()}
"""

with open("great-wok/visit.html", "w", encoding="utf-8") as f:
    f.write(visit_content)
print("Written: great-wok/visit.html")

