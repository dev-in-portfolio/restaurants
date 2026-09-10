# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("scripts")
from cm_builder import header_html, footer_html

# Page 1: index.html
index_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cheers Mate Bar &amp; Lounge | Uptown Charlotte Sports Bar &amp; Sliders</title>
  <meta name="description" content="Welcome to Cheers Mate Bar &amp; Lounge in Uptown Charlotte. High-definition sports screens, gourmet smash sliders, jumbo wings, late-night bites, and weekend brunch.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("index.html")}

  <section class="cm-hero">
    <div class="cm-container">
      <span class="cm-badge">Uptown Charlotte Sports &amp; Social Lounge</span>
      <h1 style="font-size:2.8rem; font-weight:900; margin:15px 0; letter-spacing:-0.02em;">High Energy Sports, Gourmet Sliders &amp; Nightlife</h1>
      <p style="font-size:1.15rem; color:#e2e8f0; max-width:760px; margin:0 auto 25px;">
        Your prime Uptown destination at 521 N College St for Panthers, Hornets, and Charlotte FC watch parties, craveable 2AM sliders, crispy wings, signature cocktails, and weekend brunch parties.
      </p>
      <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
        <a href="menu.html" class="cm-btn-primary">View Full Menu</a>
        <a href="weekend-brunch-and-mimosas.html" class="cm-btn-outline">Weekend Brunch</a>
        <a href="tel:9802999000" class="cm-btn-primary" style="background:#2563eb; color:#fff;">Call (980) 299-9000</a>
      </div>
    </div>
  </section>

  <!-- Key Pillars Section -->
  <section style="background-color:#ffffff; border-bottom:1px solid #e2e8f0; padding:28px 0;">
    <div class="cm-container">
      <div class="cm-grid-4" style="text-align:center;">
        <div>
          <h3 style="color:#0f172a; font-size:1.35rem; font-weight:800;">Gourmet Sliders</h3>
          <p style="color:#475569; font-size:0.9rem;">2AM Smash &amp; Impossible</p>
        </div>
        <div>
          <h3 style="color:#0f172a; font-size:1.35rem; font-weight:800;">Jumbo Wings</h3>
          <p style="color:#475569; font-size:0.9rem;">Lemon Pepper &amp; Honey Hot</p>
        </div>
        <div>
          <h3 style="color:#0f172a; font-size:1.35rem; font-weight:800;">Weekend Brunch</h3>
          <p style="color:#475569; font-size:0.9rem;">Sat &amp; Sun 11am - 4pm</p>
        </div>
        <div>
          <h3 style="color:#0f172a; font-size:1.35rem; font-weight:800;">Late Night Eats</h3>
          <p style="color:#475569; font-size:0.9rem;">Kitchen Open until 1:30 AM</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Main Narrative Section -->
  <main class="cm-container" style="padding:60px 24px;">
    <div class="cm-grid-2" style="align-items:center; margin-bottom:60px;">
      <div>
        <span class="cm-tag">Electric Uptown Vibe</span>
        <h2 style="font-size:2.2rem; color:#0f172a; margin:15px 0; font-weight:800;">The Ultimate Uptown Gathering Place</h2>
        <p style="color:#475569; line-height:1.7; margin-bottom:16px;">
          Positioned on the vibrant North College Street corridor, Cheers Mate Bar &amp; Lounge delivers an energetic sports bar atmosphere fused with upscale lounge aesthetics. With walls lined with high-definition screens, you will never miss a second of NFL, NBA, MLS, or college game day action.
        </p>
        <p style="color:#475569; line-height:1.7; margin-bottom:20px;">
          Our kitchen focuses on high-impact pub fare: fresh-pressed Angus smash sliders on toasted brioche buns, double-fried crispy chicken wings tossed in signature sauces, and loaded gourmet fries served late into the night.
        </p>
        <div style="display:flex; gap:12px; flex-wrap:wrap;">
          <a href="gourmet-sliders-and-wings.html" class="cm-btn-primary">Explore Sliders &amp; Wings</a>
          <a href="visit.html" class="cm-btn-outline" style="color:#0f172a; border-color:#0f172a;">Location &amp; Hours</a>
        </div>
      </div>
      <div>
        <img src="images/gourmet-sliders.jpg" alt="Artisan mini smash sliders served at Cheers Mate Bar" style="width:100%; height:400px; object-fit:cover; border-radius:12px; box-shadow:var(--cm-shadow-lg);">
      </div>
    </div>

    <!-- Featured Food & Drinks Grid -->
    <div style="text-align:center; margin-bottom:40px;">
      <span class="cm-tag">Crowd Favorites</span>
      <h2 style="font-size:2rem; color:#0f172a; margin-top:10px;">Lounge Highlights</h2>
    </div>

    <div class="cm-grid-3" style="margin-bottom:60px;">
      <div class="cm-feature-card">
        <img src="images/gourmet-sliders.jpg" alt="2AM Smash Sliders" class="cm-feature-img">
        <div class="cm-feature-body">
          <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
            <h3 style="color:#0f172a; font-size:1.25rem;">The 2AM Sliders (3pc)</h3>
            <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$14.50</span>
          </div>
          <p style="color:#475569; font-size:0.95rem; margin-bottom:16px;">Trio of custom Angus beef smash patties with melted American cheese, griddled onions, pickles, and secret lounge burger sauce on toasted brioche slider buns.</p>
          <span class="cm-tag">House Signature</span>
        </div>
      </div>

      <div class="cm-feature-card">
        <img src="images/crispy-wings.jpg" alt="Crispy Sauced Jumbo Wings" class="cm-feature-img">
        <div class="cm-feature-body">
          <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
            <h3 style="color:#0f172a; font-size:1.25rem;">Jumbo Wings (10pc)</h3>
            <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$15.95</span>
          </div>
          <p style="color:#475569; font-size:0.95rem; margin-bottom:16px;">Jumbo bone-in wings tossed in choice of Lemon Pepper Dry Rub, Honey Hot Buffalo, Garlic Parmesan, or Bourbon BBQ with celery and ranch.</p>
          <span class="cm-tag">Gameday Essential</span>
        </div>
      </div>

      <div class="cm-feature-card">
        <img src="images/craft-cocktails.jpg" alt="Signature Craft Cocktails" class="cm-feature-img">
        <div class="cm-feature-body">
          <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
            <h3 style="color:#0f172a; font-size:1.25rem;">College St. Mule</h3>
            <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$13.00</span>
          </div>
          <p style="color:#475569; font-size:0.95rem; margin-bottom:16px;">Craft vodka infused with fresh blackberries, spicy ginger beer, fresh squeezed lime juice, and aromatic mint sprig in a chilled copper mug.</p>
          <span class="cm-tag">Craft Mixology</span>
        </div>
      </div>
    </div>

    <!-- VIP & Event Strip -->
    <div class="cm-banner-strip">
      <span class="cm-badge">VIP &amp; Group Hospitality</span>
      <h2 style="font-size:2rem; margin:12px 0 16px; color:#ffffff;">Planning a Game Day Watch Party or Birthday?</h2>
      <p style="max-width:700px; margin:0 auto 24px; color:#cbd5e1; font-size:1.05rem;">
        Reserve private VIP lounge sections, customize slider and wing sharing platters, and enjoy dedicated table service during major sporting events.
      </p>
      <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
        <a href="gameday-packages-and-events.html" class="cm-btn-primary">View Gameday Packages</a>
        <a href="tel:9802999000" class="cm-btn-outline">Call (980) 299-9000</a>
      </div>
    </div>
  </main>

{footer_html()}
"""

with open("cheers-mate-bar-and-lounge/index.html", "w", encoding="utf-8") as f:
    f.write(index_content)
print("Written: cheers-mate-bar-and-lounge/index.html")

# Page 2: menu.html
menu_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Full Food &amp; Drink Menu | Cheers Mate Bar &amp; Lounge Charlotte</title>
  <meta name="description" content="Explore the full menu at Cheers Mate Bar &amp; Lounge Charlotte: smash sliders, crispy jumbo wings, loaded fries, brunch chicken &amp; waffles, and craft cocktails.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("menu.html")}

  <section class="cm-hero-compact">
    <div class="cm-container">
      <span class="cm-badge">Lounge Kitchen &amp; Bar</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Our Complete Food &amp; Drink Menu</h1>
      <p style="font-size:1.1rem; color:#cbd5e1; max-width:700px; margin:0 auto;">Artisan smash sliders, sauced jumbo wings, loaded pub fries, weekend brunch, and signature cocktails.</p>
    </div>
  </section>

  <main class="cm-container" style="padding:40px 24px 60px;">
    <!-- Interactive Filter Buttons -->
    <div class="cm-filters">
      <button class="cm-filter-btn active" data-filter="all">All Items</button>
      <button class="cm-filter-btn" data-filter="sliders">Gourmet Sliders</button>
      <button class="cm-filter-btn" data-filter="wings">Jumbo Wings</button>
      <button class="cm-filter-btn" data-filter="fries">Loaded Fries &amp; Dogs</button>
      <button class="cm-filter-btn" data-filter="brunch">Weekend Brunch</button>
      <button class="cm-filter-btn" data-filter="drinks">Cocktails &amp; Brews</button>
    </div>

    <!-- Menu Grid -->
    <div class="cm-grid-3" id="menu-items-grid" style="gap:24px;">
      <!-- Sliders -->
      <div class="cm-card cm-menu-item" data-category="sliders">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">The 2AM Smash Sliders (3pc)</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$14.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Three Angus smash patties, melted American cheese, caramelized onions, dill pickles, and house burger sauce on toasted buttered brioche slider buns.</p>
        <span class="cm-tag">House Signature</span>
      </div>

      <div class="cm-card cm-menu-item" data-category="sliders">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Crispy Hot Honey Chicken Sliders (3pc)</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$14.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Buttermilk-fried crispy chicken breast fillets tossed in cayenne hot honey glaze, topped with creamy cabbage slaw and bread &amp; butter pickles.</p>
        <span class="cm-tag">Spicy &amp; Sweet</span>
      </div>

      <div class="cm-card cm-menu-item" data-category="sliders">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Smoked Pulled Pork Sliders (3pc)</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$14.00</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Slow-smoked Carolina pulled pork shoulder piled high on slider buns with tangy vinegar barbecue sauce, crispy fried onion straws, and pickle chips.</p>
        <span class="cm-tag">Carolina BBQ</span>
      </div>

      <div class="cm-card cm-menu-item" data-category="sliders">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Impossible Smash Sliders (3pc, Vegan)</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$15.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Plant-based Impossible patties griddled with vegan cheddar cheese, lettuce, tomato, sliced red onion, and vegan spicy chipotle mayo.</p>
        <span class="cm-tag">Plant Based</span>
      </div>

      <!-- Wings -->
      <div class="cm-card cm-menu-item" data-category="wings">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Lemon Pepper Dry Rub Wings (10pc)</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$15.95</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Extra crispy fried wings tossed in rich lemon zest and crushed black peppercorn seasoning, brushed with garlic clarified butter.</p>
        <span class="cm-tag">Crowd Favorite</span>
      </div>

      <div class="cm-card cm-menu-item" data-category="wings">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Honey Hot Buffalo Wings (10pc)</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$15.95</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Jumbo wings tossed in our sweet and fiery blend of clover honey and classic aged cayenne pepper sauce. Served with blue cheese dressing.</p>
        <span class="cm-tag">Sweet &amp; Fiery</span>
      </div>

      <div class="cm-card cm-menu-item" data-category="wings">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Garlic Parmesan Wings (10pc)</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$15.95</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Crispy wings coated in roasted garlic butter, finely grated aged Parmesan cheese, fresh Italian parsley, and cracked black pepper.</p>
        <span class="cm-tag">Savory Rich</span>
      </div>

      <!-- Loaded Fries & Dogs -->
      <div class="cm-card cm-menu-item" data-category="fries">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Varsity Loaded Truffle Fries</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$11.95</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Crispy shoestring fries tossed in white truffle oil, shaved Parmesan cheese, fresh chopped rosemary, served with roasted garlic aioli.</p>
        <span class="cm-tag">Sharing Plate</span>
      </div>

      <div class="cm-card cm-menu-item" data-category="fries">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Chili Cheese Street Dog</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$10.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">All-beef quarter-pound frankfurter on a toasted split-top potato roll, topped with house Texas beef chili, cheddar cheese sauce, and diced onions.</p>
        <span class="cm-tag">Pub Classic</span>
      </div>

      <!-- Weekend Brunch -->
      <div class="cm-card cm-menu-item" data-category="brunch">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Lounge Chicken &amp; Waffles</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$16.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Golden Belgian pearl sugar waffle topped with hand-breaded crispy chicken tenders, hot honey drizzle, whipped honey butter, and warm bourbon maple syrup.</p>
        <span class="cm-tag">Brunch Benchmark</span>
      </div>

      <div class="cm-card cm-menu-item" data-category="brunch">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Sunrise Breakfast Sliders (3pc)</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$14.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Scrambled eggs, thick-cut applewood bacon, melted cheddar cheese, and maple aioli nestled inside three toasted warm brioche buns with crispy tater tots.</p>
        <span class="cm-tag">Brunch Feature</span>
      </div>

      <!-- Drinks -->
      <div class="cm-card cm-menu-item" data-category="drinks">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Cheers Signature Margarita</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$13.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">100% Blue Agave Reposado tequila, Grand Marnier, fresh lime juice, organic agave nectar, with a smoked chili salt rim.</p>
        <span class="cm-tag">Cocktail Favorite</span>
      </div>
    </div>

    <!-- Takeout CTA -->
    <div style="text-align:center; margin-top:50px; background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:30px; box-shadow:var(--cm-shadow);">
      <h3 style="color:#0f172a; font-size:1.5rem; margin-bottom:10px;">Order Takeout or Reserve a Table</h3>
      <p style="color:#475569; max-width:600px; margin:0 auto 20px;">Contact our staff directly for quick carryout pickup or VIP table arrangements.</p>
      <a href="tel:9802999000" class="cm-btn-primary">Call (980) 299-9000</a>
    </div>
  </main>

{footer_html()}
"""

with open("cheers-mate-bar-and-lounge/menu.html", "w", encoding="utf-8") as f:
    f.write(menu_content)
print("Written: cheers-mate-bar-and-lounge/menu.html")

