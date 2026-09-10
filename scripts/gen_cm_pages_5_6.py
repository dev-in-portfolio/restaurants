# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("scripts")
from cm_builder import header_html, footer_html

# Page 5: gameday-packages-and-events.html
events_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gameday Packages &amp; VIP Events | Cheers Mate Bar &amp; Lounge Charlotte</title>
  <meta name="description" content="Book group watch parties, tailgate packages, and VIP lounge sections at Cheers Mate Bar &amp; Lounge in Uptown Charlotte. Custom slider platters and wing boxes.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("gameday-packages-and-events.html")}

  <section class="cm-hero-compact">
    <div class="cm-container">
      <span class="cm-badge">Group Feasts &amp; VIP Lounge</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Gameday Packages &amp; Private Events</h1>
      <p style="font-size:1.1rem; color:#cbd5e1; max-width:720px; margin:0 auto;">Turnkey party packages designed for Panthers tailgates, Hornets watch parties, birthday celebrations, and corporate gatherings.</p>
    </div>
  </section>

  <main class="cm-container" style="padding:60px 24px;">
    <!-- Interactive Estimator & Package Overview -->
    <div class="cm-grid-2" style="gap:40px; margin-bottom:60px; align-items:start;">
      <div>
        <span class="cm-tag">Tailored Hospitality</span>
        <h2 style="font-size:2rem; color:#0f172a; margin:15px 0; font-weight:800;">High-Impact Party Platter Packages</h2>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:15px;">
          Whether you are celebrating in our lounge or taking food to an Uptown stadium tailgate, Cheers Mate Bar &amp; Lounge prepares high-energy, crowd-pleasing sharing boxes packed hot and fresh.
        </p>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:20px;">
          All packages include serving platters, napkins, house dipping sauces, and celery and carrots where applicable.
        </p>
        
        <div class="cm-calc-box">
          <h3 style="color:#0f172a; font-size:1.3rem; margin-bottom:12px;">Interactive Gameday &amp; Party Calculator</h3>
          <p style="color:#4b5563; font-size:0.9rem; margin-bottom:14px;">Select your group size and celebration type:</p>
          
          <label style="font-weight:600; font-size:0.9rem; color:#374151;">Expected Number of Guests:</label>
          <select id="cm-calc-guests" class="cm-calc-select">
            <option value="10">10 Guests</option>
            <option value="15">15 Guests</option>
            <option value="20" selected>20 Guests</option>
            <option value="30">30 Guests</option>
            <option value="50">50 Guests</option>
          </select>

          <label style="font-weight:600; font-size:0.9rem; color:#374151;">Occasion / Package Type:</label>
          <select id="cm-calc-type" class="cm-calc-select">
            <option value="gameday" selected>Panthers / Hornets Gameday Watch</option>
            <option value="brunch">Weekend Daytime Brunch Party</option>
            <option value="vip">VIP Booth Lounge &amp; Nightlife</option>
          </select>

          <div id="cm-calc-output" class="cm-calc-res">
            <!-- Populated via site.js -->
          </div>
        </div>
      </div>

      <div>
        <img src="images/crispy-wings.jpg" alt="Party platter of crispy wings and sliders at Cheers Mate" style="width:100%; height:360px; object-fit:cover; border-radius:12px; box-shadow:var(--cm-shadow-lg); margin-bottom:25px;">
        <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:24px; box-shadow:var(--cm-shadow);">
          <h4 style="color:#0f172a; font-size:1.15rem; margin-bottom:8px;">VIP Booths &amp; Group Inquiries</h4>
          <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:14px;">
            For VIP booth reservations with dedicated bottle service or large takeout orders (20+ people), please give our events team a call directly.
          </p>
          <a href="tel:9802999000" class="cm-btn-primary" style="display:block; text-align:center;">Call Events: (980) 299-9000</a>
        </div>
      </div>
    </div>

    <!-- Package Trays Grid -->
    <h2 style="font-size:1.9rem; color:#0f172a; text-align:center; margin-bottom:35px;">Signature Group Sharing Platters</h2>

    <div class="cm-grid-3" style="gap:28px; margin-bottom:60px;">
      <div class="cm-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Varsity 50-Wing Tailgate Box</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">50 crispy jumbo bone-in wings tossed in up to two flavors (Lemon Pepper, Honey Hot, Garlic Parm, or Sweet Chili). Served with ranch, blue cheese, celery, and carrots.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.2rem;">$72.00</span>
          <span class="cm-tag">50 Wings</span>
        </div>
      </div>

      <div class="cm-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Slider Party Crate (16 Sliders)</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">16 assorted sliders on brioche buns: 8 Classic 2AM Angus Smash, 4 Crispy Hot Honey Chicken, and 4 Smoked Pulled Pork BBQ sliders with house sauces.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.2rem;">$65.00</span>
          <span class="cm-tag">16 Sliders</span>
        </div>
      </div>

      <div class="cm-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Loaded Truffle Fries Party Pan</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Serves 8 - 10 guests. Huge pan of crispy shoestring fries tossed in white truffle oil, shaved Parmesan cheese, and fresh herbs with bowls of garlic aioli.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.2rem;">$42.00</span>
          <span class="cm-tag">Serves 8-10</span>
        </div>
      </div>

      <div class="cm-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Brunch Chicken &amp; Waffle Pan</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Serves 6 - 8 guests. 12 mini Belgian sugar waffles, 16 hand-breaded crispy chicken tenders, hot honey drizzle, whipped honey butter, and warm bourbon syrup.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.2rem;">$68.00</span>
          <span class="cm-tag">Brunch Box</span>
        </div>
      </div>

      <div class="cm-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Street Dog &amp; Pretzel Board</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Serves 6 - 8 guests. 8 quarter-pound all-beef franks sliced on buns with chili cheese sauce, diced onions, warm pretzel bites, and stone-ground beer mustard.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.2rem;">$54.00</span>
          <span class="cm-tag">Pub Board</span>
        </div>
      </div>

      <div class="cm-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Hangover Tots Breakfast Tray</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Serves 8 - 10 guests. Full party pan of crispy tater tots layered with cheddar cheese sauce, crumbled bacon, sausage, jalapenos, and chipotle crema.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.2rem;">$48.00</span>
          <span class="cm-tag">Brunch Platter</span>
        </div>
      </div>
    </div>

    <!-- CTA Banner -->
    <div class="cm-banner-strip">
      <h2 style="color:#ffffff; font-size:2rem; margin-bottom:12px;">Ready to Lock In Your Gameday Party?</h2>
      <p style="color:#cbd5e1; max-width:650px; margin:0 auto 20px;">Contact our management team directly to coordinate VIP booths, TV screens, or curbside tailgate pickups.</p>
      <a href="tel:9802999000" class="cm-btn-primary">Call (980) 299-9000</a>
    </div>
  </main>

{footer_html()}
"""

with open("cheers-mate-bar-and-lounge/gameday-packages-and-events.html", "w", encoding="utf-8") as f:
    f.write(events_content)
print("Written: cheers-mate-bar-and-lounge/gameday-packages-and-events.html")

# Page 6: visit.html
visit_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Visit &amp; Hours | Cheers Mate Bar &amp; Lounge Uptown Charlotte NC</title>
  <meta name="description" content="Plan your visit to Cheers Mate Bar &amp; Lounge at 521 N College St in Uptown Charlotte. Hours, late night kitchen times, parking tips, directions, and contact.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("visit.html")}

  <section class="cm-hero-compact">
    <div class="cm-container">
      <span class="cm-badge">First Ward District</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Visit Cheers Mate Bar &amp; Lounge</h1>
      <p style="font-size:1.1rem; color:#cbd5e1; max-width:720px; margin:0 auto;">Located at 521 North College Street in Uptown Charlotte, between 8th and 9th Streets.</p>
    </div>
  </section>

  <main class="cm-container" style="padding:60px 24px;">
    <div class="cm-grid-2" style="gap:40px; margin-bottom:60px;">
      <!-- Contact & Directions -->
      <div class="cm-card" style="padding:32px;">
        <h2 style="color:#0f172a; margin-top:0; font-size:1.6rem; border-bottom:2px solid #e2e8f0; padding-bottom:12px;">Location &amp; Contact</h2>
        
        <div style="margin:20px 0; line-height:1.8; color:#374151;">
          <p><strong>Physical Address:</strong><br>521 N College St<br>Charlotte, NC 28202</p>
          <p><strong>District:</strong> Uptown Charlotte / First Ward</p>
          <p><strong>Phone:</strong> <a href="tel:9802999000" style="color:#d97706; font-weight:700;">(980) 299-9000</a></p>
          <p><strong>Email:</strong> <a href="mailto:info@cheersmatesclt.com" style="color:#d97706;">info@cheersmatesclt.com</a></p>
        </div>

        <h3 style="color:#0f172a; font-size:1.25rem; margin-top:24px;">Getting Here</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6;">
          Situated on North College Street, we are conveniently located near 7th Street Public Market, First Ward Park, and the Charlotte Rail Trail. Just minutes from Spectrum Center and Bank of America Stadium.
        </p>

        <h3 style="color:#0f172a; font-size:1.25rem; margin-top:20px;">Parking &amp; Transit Options</h3>
        <ul style="color:#475569; font-size:0.95rem; line-height:1.6; padding-left:20px;">
          <li>Metered on-street parking along N College St and 9th St</li>
          <li>7th Street Station Parking Garage (3 blocks south)</li>
          <li>Surface parking lots available on College and Brevard Streets</li>
          <li>CATS LYNX Blue Line: 7th St Station or 9th St Station (3-minute walk)</li>
        </ul>
      </div>

      <!-- Hours & Kitchen Policies -->
      <div class="cm-card" style="padding:32px;">
        <h2 style="color:#0f172a; margin-top:0; font-size:1.6rem; border-bottom:2px solid #e2e8f0; padding-bottom:12px;">Hours of Operation</h2>
        
        <table style="width:100%; border-collapse:collapse; margin-top:20px; color:#374151; font-size:1rem;">
          <tr style="border-bottom:1px solid #f3f4f6;">
            <td style="padding:12px 0; font-weight:600;">Monday - Thursday</td>
            <td style="padding:12px 0; text-align:right;">4:00 PM - 2:00 AM</td>
          </tr>
          <tr style="border-bottom:1px solid #f3f4f6;">
            <td style="padding:12px 0; font-weight:600;">Friday</td>
            <td style="padding:12px 0; text-align:right;">3:00 PM - 2:00 AM</td>
          </tr>
          <tr style="border-bottom:1px solid #f3f4f6;">
            <td style="padding:12px 0; font-weight:600;">Saturday</td>
            <td style="padding:12px 0; text-align:right;">11:00 AM - 2:00 AM</td>
          </tr>
          <tr>
            <td style="padding:12px 0; font-weight:600;">Sunday</td>
            <td style="padding:12px 0; text-align:right;">11:00 AM - 2:00 AM</td>
          </tr>
        </table>

        <div style="background:#fef3c7; border:1px solid #fde68a; border-radius:8px; padding:16px; margin-top:24px;">
          <h4 style="color:#92400e; margin-bottom:4px;">Late-Night Kitchen &amp; Brunch Schedule</h4>
          <p style="color:#78350f; font-size:0.9rem; margin:0;">
            <strong>Weekend Brunch:</strong> Saturday &amp; Sunday, 11:00 AM – 4:00 PM.<br>
            <strong>Late Night Kitchen:</strong> Food orders served nightly until 1:30 AM.
          </p>
        </div>
      </div>
    </div>

    <!-- Contact Banner -->
    <div class="cm-banner-strip">
      <h2 style="color:#ffffff; font-size:2rem; margin-bottom:12px;">We Look Forward to Seeing You</h2>
      <p style="color:#cbd5e1; max-width:600px; margin:0 auto 20px;">Call us directly for table reservations, VIP party sections, or takeout orders.</p>
      <a href="tel:9802999000" class="cm-btn-primary">Call (980) 299-9000</a>
    </div>
  </main>

{footer_html()}
"""

with open("cheers-mate-bar-and-lounge/visit.html", "w", encoding="utf-8") as f:
    f.write(visit_content)
print("Written: cheers-mate-bar-and-lounge/visit.html")

