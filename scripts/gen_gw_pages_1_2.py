# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("scripts")
from gw_builder import header_html, footer_html

# Page 1: index.html
index_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Great Wok | Fast-Casual Chinese Takeout Uptown Charlotte NC</title>
  <meta name="description" content="Welcome to Great Wok Chinese Kitchen in Uptown Charlotte Gateway Village. High-flame wok cooking, General Tso's chicken, Lo Mein, combo platters, and catering.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("index.html")}

  <section class="gw-hero">
    <div class="gw-container">
      <span class="gw-badge">High-Flame Wok Cooking Since Day One</span>
      <h1 style="font-size:2.8rem; font-weight:900; margin:15px 0; letter-spacing:-0.02em;">Fresh, Fast &amp; Sizzling Chinese Classics</h1>
      <p style="font-size:1.15rem; color:#e2e8f0; max-width:760px; margin:0 auto 25px;">
        Located at 718 W Trade St in Gateway Village, Great Wok serves piping-hot Cantonese and Sichuan comfort favorites, generous combination platters, and fast takeout for Uptown Charlotte.
      </p>
      <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
        <a href="menu.html" class="gw-btn-primary">View Full Menu</a>
        <a href="chef-specialties-and-combos.html" class="gw-btn-outline">Chef Combos</a>
        <a href="tel:7043330080" class="gw-btn-primary" style="background:#b91c1c; color:#fff;">Order Takeout: (704) 333-0080</a>
      </div>
    </div>
  </section>

  <!-- Key Pillars Section -->
  <section style="background-color:#ffffff; border-bottom:1px solid #e2e8f0; padding:28px 0;">
    <div class="gw-container">
      <div class="gw-grid-4" style="text-align:center;">
        <div>
          <h3 style="color:#991b1b; font-size:1.35rem; font-weight:800;">High-Flame Wok</h3>
          <p style="color:#475569; font-size:0.9rem;">Authentic Wok Hei Sear</p>
        </div>
        <div>
          <h3 style="color:#991b1b; font-size:1.35rem; font-weight:800;">Daily Combos</h3>
          <p style="color:#475569; font-size:0.9rem;">With Pork Fried Rice &amp; Egg Roll</p>
        </div>
        <div>
          <h3 style="color:#991b1b; font-size:1.35rem; font-weight:800;">Fast Pickup</h3>
          <p style="color:#475569; font-size:0.9rem;">Gateway Village Counter</p>
        </div>
        <div>
          <h3 style="color:#991b1b; font-size:1.35rem; font-weight:800;">Party Catering</h3>
          <p style="color:#475569; font-size:0.9rem;">Half &amp; Full Sized Pans</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Main Narrative Section -->
  <main class="gw-container" style="padding:60px 24px;">
    <div class="gw-grid-2" style="align-items:center; margin-bottom:60px;">
      <div>
        <span class="gw-tag">Wok Fired Excellence</span>
        <h2 style="font-size:2.2rem; color:#0f172a; margin:15px 0; font-weight:800;">Generous Portions, Fresh Ingredients, Real Fire</h2>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:16px;">
          At Great Wok, we take pride in authentic wok cooking done right. Every dish is prepared quickly over roaring high-output burners, searing tender meats, crisp vegetables, and savory sauces to lock in unbeatable fresh flavor and aroma.
        </p>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:20px;">
          Whether you need a swift lunch combo between meetings or an abundant family dinner for home, our kitchen prepares each order fresh from scratch with generous portions and warm hospitality.
        </p>
        <div style="display:flex; gap:12px; flex-wrap:wrap;">
          <a href="menu.html" class="gw-btn-primary">Browse All Dishes</a>
          <a href="visit.html" class="gw-btn-outline" style="color:#0f172a; border-color:#0f172a;">Location &amp; Hours</a>
        </div>
      </div>
      <div>
        <img src="images/general-tsos-chicken.jpg" alt="Crispy General Tso's Chicken at Great Wok Charlotte" style="width:100%; height:400px; object-fit:cover; border-radius:12px; box-shadow:var(--gw-shadow-lg);">
      </div>
    </div>

    <!-- Featured Dishes Grid -->
    <div style="text-align:center; margin-bottom:40px;">
      <span class="gw-tag">Customer Favorites</span>
      <h2 style="font-size:2rem; color:#0f172a; margin-top:10px;">Signature House Specials</h2>
    </div>

    <div class="gw-grid-3" style="margin-bottom:60px;">
      <div class="gw-feature-card">
        <img src="images/general-tsos-chicken.jpg" alt="General Tso's Chicken" class="gw-feature-img">
        <div class="gw-feature-body">
          <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
            <h3 style="color:#0f172a; font-size:1.25rem;">General Tso's Chicken</h3>
            <span style="font-weight:700; color:#dc2626; font-size:1.1rem;">$13.95</span>
          </div>
          <p style="color:#4b5563; font-size:0.95rem; margin-bottom:16px;">Chunks of crispy breaded dark meat chicken glazed in our spicy sweet garlic ginger sauce with steamed fresh broccoli florets.</p>
          <span class="gw-tag">Bestseller</span>
        </div>
      </div>

      <div class="gw-feature-card">
        <img src="images/house-special-lo-mein.jpg" alt="House Special Lo Mein" class="gw-feature-img">
        <div class="gw-feature-body">
          <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
            <h3 style="color:#0f172a; font-size:1.25rem;">House Special Lo Mein</h3>
            <span style="font-weight:700; color:#dc2626; font-size:1.1rem;">$12.95</span>
          </div>
          <p style="color:#4b5563; font-size:0.95rem; margin-bottom:16px;">Egg noodles wok-tossed with jumbo shrimp, roast pork, tender chicken, and fresh crisp vegetables in a rich brown garlic sauce.</p>
          <span class="gw-tag">Wok Favorite</span>
        </div>
      </div>

      <div class="gw-feature-card">
        <img src="images/honey-walnut-shrimp.jpg" alt="Honey Walnut Shrimp" class="gw-feature-img">
        <div class="gw-feature-body">
          <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
            <h3 style="color:#0f172a; font-size:1.25rem;">Honey Walnut Jumbo Shrimp</h3>
            <span style="font-weight:700; color:#dc2626; font-size:1.1rem;">$15.50</span>
          </div>
          <p style="color:#4b5563; font-size:0.95rem; margin-bottom:16px;">Crispy fried jumbo shrimp tossed in sweet creamy honey aioli, topped with candied walnuts and served with steamed broccoli.</p>
          <span class="gw-tag">Chef Feature</span>
        </div>
      </div>
    </div>

    <!-- Family & Office Catering Strip -->
    <div class="gw-banner-strip">
      <span class="gw-badge" style="background:rgba(220,38,38,0.3); border-color:#ef4444; color:#ffffff;">Office &amp; Family Feasts</span>
      <h2 style="font-size:2rem; margin:12px 0 16px; color:#ffffff;">Feeding the Office or Family Tonight?</h2>
      <p style="max-width:700px; margin:0 auto 24px; color:#cbd5e1; font-size:1.05rem;">
        Order our party pans of General Tso's, Sesame Chicken, Lo Mein, and egg rolls for your corporate team meeting or family weekend feast.
      </p>
      <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
        <a href="family-feasts-and-catering.html" class="gw-btn-primary">View Catering Packages</a>
        <a href="tel:7043330080" class="gw-btn-outline">Call (704) 333-0080</a>
      </div>
    </div>
  </main>

{footer_html()}
"""

with open("great-wok/index.html", "w", encoding="utf-8") as f:
    f.write(index_content)
print("Written: great-wok/index.html")

# Page 2: menu.html
menu_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Full Menu | Great Wok Chinese Takeout Uptown Charlotte</title>
  <meta name="description" content="Browse the full takeout menu at Great Wok Charlotte: appetizers, dumplings, General Tso's, beef broccoli, Lo Mein, fried rice, and lunch combos.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("menu.html")}

  <section class="gw-hero-compact">
    <div class="gw-container">
      <span class="gw-badge">Takeout &amp; Dine-In Menu</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Our Complete Chinese Menu</h1>
      <p style="font-size:1.1rem; color:#cbd5e1; max-width:700px; margin:0 auto;">Wok-tossed entrees, sizzling noodles, crispy appetizers, and value combination platters.</p>
    </div>
  </section>

  <main class="gw-container" style="padding:40px 24px 60px;">
    <!-- Interactive Filter Buttons -->
    <div class="gw-filters">
      <button class="gw-filter-btn active" data-filter="all">All Items</button>
      <button class="gw-filter-btn" data-filter="specialties">Chef Specialties</button>
      <button class="gw-filter-btn" data-filter="combos">Combination Platters</button>
      <button class="gw-filter-btn" data-filter="noodles">Lo Mein &amp; Mei Fun</button>
      <button class="gw-filter-btn" data-filter="rice">Fried Rice &amp; Egg Foo Young</button>
      <button class="gw-filter-btn" data-filter="appetizers">Appetizers &amp; Soups</button>
    </div>

    <!-- Menu Grid -->
    <div class="gw-grid-3" id="menu-items-grid" style="gap:24px;">
      <!-- Chef Specialties -->
      <div class="gw-card gw-menu-item" data-category="specialties">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">General Tso's Chicken</h3>
          <span style="font-weight:700; color:#dc2626; font-size:1.1rem;">$13.95</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Crispy dark meat chicken chunks tossed in spicy sweet garlic chili glaze with steamed broccoli. Served with white rice.</p>
        <span class="gw-tag">House Benchmark</span>
      </div>

      <div class="gw-card gw-menu-item" data-category="specialties">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Crispy Sesame Chicken</h3>
          <span style="font-weight:700; color:#dc2626; font-size:1.1rem;">$13.95</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Crispy chicken coated in our sweet and savory sesame honey glaze, garnished with toasted sesame seeds and broccoli.</p>
        <span class="gw-tag">Customer Favorite</span>
      </div>

      <div class="gw-card gw-menu-item" data-category="specialties">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Orange Peel Beef</h3>
          <span style="font-weight:700; color:#dc2626; font-size:1.1rem;">$15.50</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Crispy flank steak slices glazed in a zesty, aromatic orange peel chili reduction with red peppers and scallions.</p>
        <span class="gw-tag">Crispy Beef</span>
      </div>

      <div class="gw-card gw-menu-item" data-category="specialties">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Beef with Broccoli</h3>
          <span style="font-weight:700; color:#dc2626; font-size:1.1rem;">$14.50</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Tender sliced flank steak wok-stirred with fresh broccoli florets and carrots in our rich brown garlic soy sauce.</p>
        <span class="gw-tag">Classic Stir Fry</span>
      </div>

      <!-- Combos -->
      <div class="gw-card gw-menu-item" data-category="combos">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">General Tso Combo Platter</h3>
          <span style="font-weight:700; color:#dc2626; font-size:1.1rem;">$11.95</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Generous portion of General Tso's chicken served with roast pork fried rice and a crispy golden egg roll.</p>
        <span class="gw-tag">Value Combo</span>
      </div>

      <div class="gw-card gw-menu-item" data-category="combos">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Sweet &amp; Sour Chicken Combo</h3>
          <span style="font-weight:700; color:#dc2626; font-size:1.1rem;">$11.50</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Golden fried chicken nuggets with sweet &amp; sour sauce on the side, roast pork fried rice, and an egg roll.</p>
        <span class="gw-tag">Value Combo</span>
      </div>

      <div class="gw-card gw-menu-item" data-category="combos">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Pepper Steak with Onions Combo</h3>
          <span style="font-weight:700; color:#dc2626; font-size:1.1rem;">$12.50</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Sliced tender beef sauteed with green bell peppers and sweet onions in brown sauce, served with pork fried rice and an egg roll.</p>
        <span class="gw-tag">Value Combo</span>
      </div>

      <!-- Noodles -->
      <div class="gw-card gw-menu-item" data-category="noodles">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">House Special Lo Mein</h3>
          <span style="font-weight:700; color:#dc2626; font-size:1.1rem;">$12.95</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Soft egg noodles tossed with shrimp, chicken, roast pork, cabbage, carrots, and scallions in savory wok sauce.</p>
        <span class="gw-tag">Wok Lo Mein</span>
      </div>

      <div class="gw-card gw-menu-item" data-category="noodles">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Singapore Rice Mei Fun</h3>
          <span style="font-weight:700; color:#dc2626; font-size:1.1rem;">$13.50</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Thin rice vermicelli noodles stir-fried with curry powder, egg, shrimp, roast pork, bell peppers, and bean sprouts.</p>
        <span class="gw-tag">Spicy Curry</span>
      </div>

      <!-- Rice & Egg Foo Young -->
      <div class="gw-card gw-menu-item" data-category="rice">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">House Special Fried Rice</h3>
          <span style="font-weight:700; color:#dc2626; font-size:1.1rem;">$11.95</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Jasmine rice stir-fried in a hot wok with shrimp, chicken, roast pork, peas, carrots, onions, and scrambled egg.</p>
        <span class="gw-tag">House Rice</span>
      </div>

      <div class="gw-card gw-menu-item" data-category="rice">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Roast Pork Egg Foo Young (3pc)</h3>
          <span style="font-weight:700; color:#dc2626; font-size:1.1rem;">$12.50</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Three deep-fried Chinese egg omelets packed with roast pork, bean sprouts, and onions, smothered in rich brown gravy.</p>
        <span class="gw-tag">Traditional</span>
      </div>

      <!-- Appetizers -->
      <div class="gw-card gw-menu-item" data-category="appetizers">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Steamed Pork Dumplings (8pc)</h3>
          <span style="font-weight:700; color:#dc2626; font-size:1.1rem;">$8.50</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Hand-folded dumplings filled with seasoned pork and scallions, served with our house ginger soy dipping sauce.</p>
        <span class="gw-tag">Handmade</span>
      </div>

      <div class="gw-card gw-menu-item" data-category="appetizers">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Crab Rangoon (6pc)</h3>
          <span style="font-weight:700; color:#dc2626; font-size:1.1rem;">$7.50</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Crispy fried wonton pockets filled with rich cream cheese and imitation crab meat, served with sweet duck sauce.</p>
        <span class="gw-tag">Crispy Wonton</span>
      </div>
    </div>

    <!-- Takeout CTA -->
    <div style="text-align:center; margin-top:50px; background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:30px; box-shadow:var(--gw-shadow);">
      <h3 style="color:#0f172a; font-size:1.5rem; margin-bottom:10px;">Call to Order for Quick Counter Pickup</h3>
      <p style="color:#4b5563; max-width:600px; margin:0 auto 20px;">Most orders are hot and ready in 15 minutes at our 718 W Trade St pickup counter.</p>
      <a href="tel:7043330080" class="gw-btn-primary">Call (704) 333-0080</a>
    </div>
  </main>

{footer_html()}
"""

with open("great-wok/menu.html", "w", encoding="utf-8") as f:
    f.write(menu_content)
print("Written: great-wok/menu.html")

