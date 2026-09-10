# -*- coding: utf-8 -*-
import os
from valhalla_builder import header_html, footer_html

pages = {}

# Page 3: scandinavian-pub-fare-and-meatballs.html
pages["scandinavian-pub-fare-and-meatballs.html"] = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Scandinavian Pub Fare &amp; Meatballs | Valhalla Pub &amp; Eatery Uptown Charlotte</title>
  <meta name="description" content="Discover scratch-made Scandinavian pub comfort foods at Valhalla Pub in Brevard Court Charlotte: authentic Swedish meatballs, lingonberry preserves, cured salmon, and artisan tavern specialties.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("scandinavian-pub-fare-and-meatballs.html")}

  <section class="valhalla-hero-compact">
    <div class="valhalla-section-inner">
      <span class="valhalla-badge">Nordic Comfort Heritage</span>
      <h1 style="color:#ffffff; font-size:2.5rem; font-weight:800; margin:15px 0;">Scandinavian Pub Fare &amp; Scratch Meatballs</h1>
      <p style="color:#cbd5e1; max-width:700px; margin:0 auto; font-size:1.1rem;">Honoring traditional Nordic recipes infused with hearty tavern warmth in the heart of Uptown Charlotte.</p>
    </div>
  </section>

  <main class="valhalla-section-inner" style="padding: 50px 20px;">
    <div class="valhalla-grid-2" style="margin-bottom: 50px; align-items:center;">
      <div>
        <span class="valhalla-tag">Our Crown Jewel</span>
        <h2 style="font-size:2rem; margin:15px 0; color:#0f172a;">The Story of Our Swedish Meatballs</h2>
        <p style="color:#475569; line-height:1.7; margin-bottom:15px;">
          At Valhalla Pub &amp; Eatery, we refuse shortcuts. Our signature Swedish Meatballs are rolled by hand daily from a master blend of premium ground beef and pork, infused with white pepper, ground allspice, nutmeg, and caramelized yellow onions.
        </p>
        <p style="color:#475569; line-height:1.7; margin-bottom:15px;">
          Simmered slowly in an aromatic brown velouté gravy enriched with heavy cream and fresh herbs, every portion is served over velvety Yukon gold potato mash with tart wild Scandinavian lingonberry preserves and house-pickled cucumbers.
        </p>
        <div style="background:#f1f5f9; padding:20px; border-left:4px solid #d97706; border-radius:6px; margin-top:20px;">
          <h4 style="margin:0 0 5px 0; color:#0f172a;">Authentic Nordic Accompaniments</h4>
          <p style="margin:0; color:#475569; font-size:0.95rem;">Imported Swedish lingonberries provide the essential tart counterpoint to our rich pan gravy, balanced by crisp quick-pickled dill cucumbers.</p>
        </div>
      </div>
      <div>
        <img src="images/swedish-meatballs.jpg" alt="Swedish Meatballs with gravy and lingonberry preserves" class="valhalla-img-card" style="width:100%; height:380px; object-fit:cover; border-radius:12px; box-shadow:0 10px 25px rgba(0,0,0,0.1);">
      </div>
    </div>

    <h2 style="font-size:1.8rem; margin:40px 0 25px; text-align:center; color:#0f172a;">Nordic Pub Specialties</h2>
    
    <div class="valhalla-grid-3" style="gap:25px; margin-bottom:50px;">
      <div class="valhalla-card">
        <h3 style="color:#0f172a; margin-top:0;">Classic Swedish Meatball Platter</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6;">Half-pound of handmade beef &amp; pork meatballs simmered in rich cream gravy, served over buttered Yukon gold mash with lingonberry jam and pickled cucumbers.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:20px; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#b45309; font-size:1.15rem;">$18.50</span>
          <span class="valhalla-tag">House Signature</span>
        </div>
      </div>

      <div class="valhalla-card">
        <h3 style="color:#0f172a; margin-top:0;">Copenhagen Fish &amp; Chips</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6;">Fresh Atlantic cod dipped in our house craft blonde ale batter, fried golden and crisp. Served with hand-cut tavern chips, fresh remoulade slaw, and house caper tartar.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:20px; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#b45309; font-size:1.15rem;">$17.95</span>
          <span class="valhalla-tag">Fresh Catch</span>
        </div>
      </div>

      <div class="valhalla-card">
        <h3 style="color:#0f172a; margin-top:0;">Smoked Salmon Smørrebrød</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6;">Artisanal Danish open-face sandwich on dark dense rye with dill cream cheese, thinly sliced cold-smoked salmon, capers, shaved shallots, and microgreens.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:20px; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#b45309; font-size:1.15rem;">$15.50</span>
          <span class="valhalla-tag">Cold Nordic</span>
        </div>
      </div>

      <div class="valhalla-card">
        <h3 style="color:#0f172a; margin-top:0;">Nordic Gravlax Flatbread</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6;">Stone-baked flatbread spread with herbed creme fraiche, house-cured gravlax salmon, baby arugula, pickled mustard seeds, and fresh dill sprigs.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:20px; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#b45309; font-size:1.15rem;">$16.00</span>
          <span class="valhalla-tag">Stone Hearth</span>
        </div>
      </div>

      <div class="valhalla-card">
        <h3 style="color:#0f172a; margin-top:0;">Stockholm Meatball Sub</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6;">Handcrafted Scandinavian meatballs tucked into a toasted brioche hoagie roll, melted Havarti cheese, rich brown gravy drizzle, and side of lingonberry dip.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:20px; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#b45309; font-size:1.15rem;">$16.50</span>
          <span class="valhalla-tag">Lunch Favorite</span>
        </div>
      </div>

      <div class="valhalla-card">
        <h3 style="color:#0f172a; margin-top:0;">Skillet Sausage &amp; Potato Hash</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6;">Traditional Pyttipanna-style hash with seared smoked bratwurst, diced Yukon potatoes, caramelized onions, topped with a fried farm egg and pickled beets.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:20px; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#b45309; font-size:1.15rem;">$16.95</span>
          <span class="valhalla-tag">Cast Iron</span>
        </div>
      </div>
    </div>

    <div style="background: linear-gradient(135deg, #1e293b, #0f172a); color:#fff; border-radius:12px; padding:35px; text-align:center;">
      <h3 style="color:#fef08a; font-size:1.6rem; margin-top:0;">Join Us at the Hearth</h3>
      <p style="color:#cbd5e1; max-width:600px; margin:0 auto 20px;">Experience true Viking hospitality and comforting Scandinavian flavors in Charlotte's historic Brevard Court alleyway.</p>
      <a href="tel:7043323273" class="valhalla-btn-primary">Call (704) 332-3273 for Orders</a>
    </div>
  </main>

{footer_html()}
"""

# Page 4: brevard-court-patio-and-taproom.html
pages["brevard-court-patio-and-taproom.html"] = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Brevard Court Patio &amp; Taproom | Valhalla Pub Uptown Charlotte</title>
  <meta name="description" content="Relax on Valhalla Pub's lively outdoor patio nestled in historic Brevard Court Uptown Charlotte. Enjoy 10 rotating craft taps, local Carolina brews, and European pub ambiance.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("brevard-court-patio-and-taproom.html")}

  <section class="valhalla-hero-compact">
    <div class="valhalla-section-inner">
      <span class="valhalla-badge">Historic Brevard Court</span>
      <h1 style="color:#ffffff; font-size:2.5rem; font-weight:800; margin:15px 0;">Brevard Court Patio &amp; Craft Taproom</h1>
      <p style="color:#cbd5e1; max-width:700px; margin:0 auto; font-size:1.1rem;">Uptown Charlotte's premier open-air gathering spot, nestled in the European cobblestone passageway between Church Street and Romare Bearden Park.</p>
    </div>
  </section>

  <main class="valhalla-section-inner" style="padding: 50px 20px;">
    <div class="valhalla-grid-2" style="margin-bottom: 50px; align-items:center;">
      <div>
        <span class="valhalla-tag">Al Fresco Charm</span>
        <h2 style="font-size:2rem; margin:15px 0; color:#0f172a;">The Brevard Court Experience</h2>
        <p style="color:#475569; line-height:1.7; margin-bottom:15px;">
          Built in the 1920s as a vibrant open-air arcade, Brevard Court remains one of Uptown Charlotte's best-kept secrets. Strolling down the brick pavers surrounded by vintage architecture transports guests to a European pedestrian lane.
        </p>
        <p style="color:#475569; line-height:1.7; margin-bottom:15px;">
          Valhalla Pub &amp; Eatery anchors the court with expansive outdoor bistro seating, overhead string lights, and full beverage service right in the courtyard breeze.
        </p>
        <ul style="color:#334155; line-height:1.8; margin-top:15px; padding-left:20px;">
          <li>Steps away from Romare Bearden Park and Truist Field</li>
          <li>Easy 5-minute walk to Bank of America Stadium for game days</li>
          <li>Heated patio sections during cooler autumn and winter evenings</li>
          <li>Dog-friendly outdoor courtyard dining tables</li>
        </ul>
      </div>
      <div>
        <img src="images/brevard-patio-pretzel.jpg" alt="Valhalla Pub outdoor seating in Brevard Court" class="valhalla-img-card" style="width:100%; height:380px; object-fit:cover; border-radius:12px; box-shadow:0 10px 25px rgba(0,0,0,0.1);">
      </div>
    </div>

    <h2 style="font-size:1.8rem; margin:40px 0 25px; text-align:center; color:#0f172a;">Draft Lines &amp; Nordic Libations</h2>
    
    <div class="valhalla-grid-3" style="gap:25px; margin-bottom:50px;">
      <div class="valhalla-card">
        <h3 style="color:#0f172a; margin-top:0;">Rotating Craft Beers on Tap</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6;">Featuring 10 temperature-controlled tap lines pouring the freshest local Charlotte IPAs, crisp Scandinavian pilsners, rich stouts, and seasonal sour ales from Olde Mecklenburg, Sycamore, and Legion.</p>
        <div style="margin-top:15px; padding-top:10px; border-top:1px solid #e2e8f0; font-size:0.9rem; color:#b45309; font-weight:600;">
          10 Rotating Taps | 16oz Pints &amp; 20oz Steins
        </div>
      </div>

      <div class="valhalla-card">
        <h3 style="color:#0f172a; margin-top:0;">Viking Mead &amp; Scandinavian Ciders</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6;">Sample our hand-selected traditional honey meads, crisp dry apple ciders, and imported Scandinavian lingonberry and pear ciders served in chilled glassware.</p>
        <div style="margin-top:15px; padding-top:10px; border-top:1px solid #e2e8f0; font-size:0.9rem; color:#b45309; font-weight:600;">
          Traditional &amp; Berry Infusions Available
        </div>
      </div>

      <div class="valhalla-card">
        <h3 style="color:#0f172a; margin-top:0;">Handcrafted Tavern Cocktails</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6;">Signature libations including the Norse Old Fashioned with smoked oak bitters, Valkyrie Mule with fresh ginger puree, and Odin's Bloody Mary for weekend brunch.</p>
        <div style="margin-top:15px; padding-top:10px; border-top:1px solid #e2e8f0; font-size:0.9rem; color:#b45309; font-weight:600;">
          Full Liquor Bar &amp; Signature Infusions
        </div>
      </div>
    </div>

    <div class="valhalla-grid-2" style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:30px; gap:30px;">
      <div>
        <h3 style="color:#0f172a; margin-top:0;">Patio Hours &amp; Happy Hours</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6;">Join us after work for weekday pub specials and courtyard conversations:</p>
        <ul style="color:#334155; font-size:0.95rem; line-height:1.8; padding-left:20px;">
          <li><strong>Monday - Friday Happy Hour:</strong> 4:00 PM - 7:00 PM</li>
          <li><strong>Game Day Watch Parties:</strong> Panthers, Charlotte FC &amp; European Soccer matches on high-def screens</li>
          <li><strong>Weekend Courtyard Brunch:</strong> Saturday &amp; Sunday starting at 10:00 AM</li>
        </ul>
      </div>
      <div>
        <h3 style="color:#0f172a; margin-top:0;">Courtyard Seating Policy</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6;">Outdoor patio tables are available on a walk-in, first-come first-served basis. For large parties (8+) visiting before sporting events or corporate gatherings, please give us a call ahead.</p>
        <a href="tel:7043323273" class="valhalla-btn-primary" style="margin-top:10px; display:inline-block;">Call Taproom: (704) 332-3273</a>
      </div>
    </div>
  </main>

{footer_html()}
"""

# Page 5: feast-platters-and-gameday-packages.html
pages["feast-platters-and-gameday-packages.html"] = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Feast Platters &amp; Game Day Packages | Valhalla Pub Uptown Charlotte</title>
  <meta name="description" content="Feed your Viking crew with Valhalla Pub's large-format feast platters, game day wings, Swedish meatball pans, and slider trays in Uptown Charlotte.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("feast-platters-and-gameday-packages.html")}

  <section class="valhalla-hero-compact">
    <div class="valhalla-section-inner">
      <span class="valhalla-badge">Group Feasts &amp; Tailgates</span>
      <h1 style="color:#ffffff; font-size:2.5rem; font-weight:800; margin:15px 0;">Viking Feast Platters &amp; Game Day Packages</h1>
      <p style="color:#cbd5e1; max-width:700px; margin:0 auto; font-size:1.1rem;">Designed for Panthers tailgates, Charlotte FC watch parties, corporate team lunches, and lively celebrations in Uptown Charlotte.</p>
    </div>
  </section>

  <main class="valhalla-section-inner" style="padding: 50px 20px;">
    <div class="valhalla-grid-2" style="margin-bottom: 50px; align-items:center;">
      <div>
        <span class="valhalla-tag">Feed the Entire Clan</span>
        <h2 style="font-size:2rem; margin:15px 0; color:#0f172a;">Generous Tavern Sharing Platters</h2>
        <p style="color:#475569; line-height:1.7; margin-bottom:15px;">
          Whether you are hosting friends at home, celebrating in Brevard Court, or prepping for kickoff at Bank of America Stadium, Valhalla Pub prepares high-energy feast platters packed with savory tavern favorites.
        </p>
        <p style="color:#475569; line-height:1.7; margin-bottom:15px;">
          From towering warm Bavarian pretzels and crispy jumbo chicken wings to large trays of Swedish meatballs and Angus smash sliders, our feast menu delivers unbeatable flavor and hearty satisfaction.
        </p>
        <div style="background:#f1f5f9; padding:15px 20px; border-radius:8px; border-left:4px solid #d97706;">
          <p style="margin:0; font-size:0.95rem; color:#334155;"><strong>Advance Notice:</strong> Tailgate packages and party trays can be ordered 2 to 24 hours in advance for easy curbside pickup on Church Street.</p>
        </div>
      </div>
      <div>
        <img src="images/fish-chips-wings.jpg" alt="Viking Feast Platters with wings and pub snacks" class="valhalla-img-card" style="width:100%; height:380px; object-fit:cover; border-radius:12px; box-shadow:0 10px 25px rgba(0,0,0,0.1);">
      </div>
    </div>

    <h2 style="font-size:1.8rem; margin:40px 0 25px; text-align:center; color:#0f172a;">Signature Group Feast Packages</h2>

    <div class="valhalla-grid-3" style="gap:25px; margin-bottom:50px;">
      <div class="valhalla-card">
        <h3 style="color:#0f172a; margin-top:0;">The Valhalla Grand Feast</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6;">Serves 6 - 8 guests. Includes 24 handcrafted Swedish meatballs with gravy &amp; lingonberry, 20 crispy jumbo wings (choice of 2 sauces), 8 Viking smash sliders, and 2 giant warm Bavarian pretzels with beer cheese.</p>
        <div style="margin-top:20px; border-top:1px solid #e2e8f0; padding-top:12px; display:flex; justify-content:space-between; align-items:center;">
          <span style="font-weight:700; color:#b45309; font-size:1.2rem;">$125.00</span>
          <span class="valhalla-tag">Serves 6-8</span>
        </div>
      </div>

      <div class="valhalla-card">
        <h3 style="color:#0f172a; margin-top:0;">Game Day Wing Platter (50 Wings)</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6;">50 crispy jumbo bone-in wings tossed in up to 3 signature sauces: Honey Lingonberry BBQ, Nordic Dry Rub, or Buffalo Valkyrie Fire. Served with celery, carrot sticks, and house blue cheese.</p>
        <div style="margin-top:20px; border-top:1px solid #e2e8f0; padding-top:12px; display:flex; justify-content:space-between; align-items:center;">
          <span style="font-weight:700; color:#b45309; font-size:1.2rem;">$75.00</span>
          <span class="valhalla-tag">Tailgate Classic</span>
        </div>
      </div>

      <div class="valhalla-card">
        <h3 style="color:#0f172a; margin-top:0;">Swedish Meatball Party Pan</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6;">Serves 8 - 10 guests. Half hotel pan containing 40 handmade Swedish meatballs swimming in piping hot cream gravy, accompanied by a side pan of mashed potatoes, lingonberry jam, and house pickles.</p>
        <div style="margin-top:20px; border-top:1px solid #e2e8f0; padding-top:12px; display:flex; justify-content:space-between; align-items:center;">
          <span style="font-weight:700; color:#b45309; font-size:1.2rem;">$89.00</span>
          <span class="valhalla-tag">Serves 8-10</span>
        </div>
      </div>

      <div class="valhalla-card">
        <h3 style="color:#0f172a; margin-top:0;">Viking Slider Box (12 Sliders)</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6;">12 mini tavern burgers on toasted brioche slider buns: choice of aged white cheddar with caramelized onions, bacon smoked gouda, or crispy chicken remoulade.</p>
        <div style="margin-top:20px; border-top:1px solid #e2e8f0; padding-top:12px; display:flex; justify-content:space-between; align-items:center;">
          <span style="font-weight:700; color:#b45309; font-size:1.2rem;">$48.00</span>
          <span class="valhalla-tag">Box of 12</span>
        </div>
      </div>

      <div class="valhalla-card">
        <h3 style="color:#0f172a; margin-top:0;">Brevard Pretzel &amp; Brat Board</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6;">Serves 5 - 6 guests. 3 giant Bavarian pretzels, grilled sliced smoked bratwurst sausages, warm craft beer cheese fondue, spicy stone-ground mustard, and pickled red cabbage.</p>
        <div style="margin-top:20px; border-top:1px solid #e2e8f0; padding-top:12px; display:flex; justify-content:space-between; align-items:center;">
          <span style="font-weight:700; color:#b45309; font-size:1.2rem;">$52.00</span>
          <span class="valhalla-tag">Pub Board</span>
        </div>
      </div>

      <div class="valhalla-card">
        <h3 style="color:#0f172a; margin-top:0;">Fish &amp; Chips Tavern Box</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6;">Serves 4 - 6 guests. 12 pieces of craft beer-battered Atlantic cod, mounds of hand-cut tavern chips, pint of remoulade slaw, tartar sauce, and lemon wedges.</p>
        <div style="margin-top:20px; border-top:1px solid #e2e8f0; padding-top:12px; display:flex; justify-content:space-between; align-items:center;">
          <span style="font-weight:700; color:#b45309; font-size:1.2rem;">$58.00</span>
          <span class="valhalla-tag">Seafood Box</span>
        </div>
      </div>
    </div>

    <div style="background:#0f172a; color:#fff; border-radius:12px; padding:35px; text-align:center;">
      <h3 style="color:#fef08a; font-size:1.6rem; margin-top:0;">Planning a Large Gathering?</h3>
      <p style="color:#cbd5e1; max-width:650px; margin:0 auto 20px;">Call our catering desk directly to coordinate custom menus, stadium pickups, or patio reservations for your group.</p>
      <a href="tel:7043323273" class="valhalla-btn-primary">Call (704) 332-3273 to Order Platters</a>
    </div>
  </main>

{footer_html()}
"""

# Page 6: visit.html
pages["visit.html"] = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Visit &amp; Hours | Valhalla Pub &amp; Eatery Brevard Court Charlotte</title>
  <meta name="description" content="Plan your visit to Valhalla Pub &amp; Eatery at 317 S Church St in historic Brevard Court, Uptown Charlotte. Hours, directions, parking, and contact info.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("visit.html")}

  <section class="valhalla-hero-compact">
    <div class="valhalla-section-inner">
      <span class="valhalla-badge">Uptown Charlotte Destination</span>
      <h1 style="color:#ffffff; font-size:2.5rem; font-weight:800; margin:15px 0;">Visit Valhalla Pub &amp; Eatery</h1>
      <p style="color:#cbd5e1; max-width:700px; margin:0 auto; font-size:1.1rem;">Located inside historic Brevard Court, directly between South Church Street and South Mint Street.</p>
    </div>
  </section>

  <main class="valhalla-section-inner" style="padding: 50px 20px;">
    <div class="valhalla-grid-2" style="gap:40px; margin-bottom:50px;">
      <div class="valhalla-card" style="padding:30px;">
        <h2 style="color:#0f172a; margin-top:0; font-size:1.6rem; border-bottom:2px solid #e2e8f0; padding-bottom:10px;">Pub Location &amp; Directions</h2>
        <div style="margin:20px 0; line-height:1.8; color:#334155;">
          <p><strong>Physical Address:</strong><br>317 S Church St (Brevard Court)<br>Charlotte, NC 28202</p>
          <p><strong>Neighborhood:</strong> Uptown Third Ward / Brevard Court</p>
          <p><strong>Phone:</strong> <a href="tel:7043323273" style="color:#b45309; font-weight:700;">(704) 332-3273</a></p>
          <p><strong>Email:</strong> <a href="mailto:contact@valhallapub.com" style="color:#b45309;">contact@valhallapub.com</a></p>
        </div>
        
        <h3 style="color:#0f172a; font-size:1.2rem; margin-top:25px;">Walking Directions</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6;">
          Enter the cobblestone arcade of Brevard Court from either South Church Street (across from the Latta Arcade building) or South Mint Street (adjacent to Romare Bearden Park). Valhalla Pub is located centrally along the courtyard.
        </p>

        <h3 style="color:#0f172a; font-size:1.2rem; margin-top:20px;">Parking Information</h3>
        <ul style="color:#475569; font-size:0.95rem; line-height:1.6; padding-left:20px;">
          <li>Metered on-street parking along S Church St, S Mint St, and 3rd St</li>
          <li>BB&amp;T / Truist Center Parking Deck (1 block east)</li>
          <li>Surface parking lots along S Mint St across from Truist Field</li>
          <li>CATS LYNX Blue Line: 3rd St / Convention Center Station (4-minute walk)</li>
        </ul>
      </div>

      <div class="valhalla-card" style="padding:30px;">
        <h2 style="color:#0f172a; margin-top:0; font-size:1.6rem; border-bottom:2px solid #e2e8f0; padding-bottom:10px;">Hours of Operation</h2>
        <table style="width:100%; border-collapse:collapse; margin-top:20px; color:#334155; font-size:1rem;">
          <tr style="border-bottom:1px solid #f1f5f9;">
            <td style="padding:12px 0; font-weight:600;">Monday</td>
            <td style="padding:12px 0; text-align:right;">11:00 AM - 11:00 PM</td>
          </tr>
          <tr style="border-bottom:1px solid #f1f5f9;">
            <td style="padding:12px 0; font-weight:600;">Tuesday</td>
            <td style="padding:12px 0; text-align:right;">11:00 AM - 11:00 PM</td>
          </tr>
          <tr style="border-bottom:1px solid #f1f5f9;">
            <td style="padding:12px 0; font-weight:600;">Wednesday</td>
            <td style="padding:12px 0; text-align:right;">11:00 AM - 11:00 PM</td>
          </tr>
          <tr style="border-bottom:1px solid #f1f5f9;">
            <td style="padding:12px 0; font-weight:600;">Thursday</td>
            <td style="padding:12px 0; text-align:right;">11:00 AM - 11:00 PM</td>
          </tr>
          <tr style="border-bottom:1px solid #f1f5f9;">
            <td style="padding:12px 0; font-weight:600;">Friday</td>
            <td style="padding:12px 0; text-align:right;">11:00 AM - 12:00 AM</td>
          </tr>
          <tr style="border-bottom:1px solid #f1f5f9;">
            <td style="padding:12px 0; font-weight:600;">Saturday</td>
            <td style="padding:12px 0; text-align:right;">11:00 AM - 12:00 AM</td>
          </tr>
          <tr>
            <td style="padding:12px 0; font-weight:600;">Sunday</td>
            <td style="padding:12px 0; text-align:right;">10:00 AM - 10:00 PM</td>
          </tr>
        </table>

        <div style="background:#fef3c7; border:1px solid #fde68a; border-radius:8px; padding:15px; margin-top:25px;">
          <h4 style="margin:0 0 5px; color:#92400e;">Kitchen Notes</h4>
          <p style="margin:0; font-size:0.9rem; color:#78350f;">The kitchen closes 1 hour prior to pub closing each evening. Late night pub pretzels and bar snacks remain available until last call.</p>
        </div>
      </div>
    </div>

    <div style="background: linear-gradient(135deg, #1e293b, #0f172a); color:#fff; border-radius:12px; padding:35px; text-align:center;">
      <h3 style="color:#fef08a; font-size:1.6rem; margin-top:0;">Questions or Takeout Orders?</h3>
      <p style="color:#cbd5e1; max-width:600px; margin:0 auto 20px;">Contact our taproom staff directly during open hours for fast assistance and orders.</p>
      <a href="tel:7043323273" class="valhalla-btn-primary">Call (704) 332-3273</a>
    </div>
  </main>

{footer_html()}
"""

for fname, content in pages.items():
    path = os.path.join("valhalla-pub-and-eatery", fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {path}")

