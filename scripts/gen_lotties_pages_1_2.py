# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("scripts")
from lotties_builder import header_html, footer_html

# Page 1: index.html
index_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lottie's Cafe | Artisanal Coffee &amp; All-Day Breakfast Uptown Charlotte</title>
  <meta name="description" content="Welcome to Lottie's Cafe in Queen City Quarter, Uptown Charlotte. Handcrafted breakfast sandwiches, artisan bagels, espresso, specialty lattes, and lunch paninis.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("index.html")}

  <section class="lottie-hero">
    <div class="lottie-container">
      <span class="lottie-badge">Queen City Quarter Uptown Charlotte</span>
      <h1 style="font-size:2.8rem; font-weight:900; margin:15px 0; letter-spacing:-0.02em;">Artisanal Espresso &amp; All-Day Breakfast Comfort</h1>
      <p style="font-size:1.15rem; color:#f5f5f4; max-width:760px; margin:0 auto 25px;">
        Located at 210 E Trade St, Lottie's Cafe fuels Uptown Charlotte with specialty espresso drinks, scratch-made breakfast sandwiches on warm brioche, power bowls, and gourmet paninis.
      </p>
      <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
        <a href="menu.html" class="lottie-btn-primary">Explore Full Menu</a>
        <a href="all-day-breakfast-and-sandwiches.html" class="lottie-btn-outline">All-Day Breakfast</a>
        <a href="tel:7047893135" class="lottie-btn-primary" style="background:#78350f; color:#fff;">Call (704) 789-3135</a>
      </div>
    </div>
  </section>

  <!-- Key Pillars Section -->
  <section style="background-color:#ffffff; border-bottom:1px solid #e7e5e4; padding:28px 0;">
    <div class="lottie-container">
      <div class="lottie-grid-4" style="text-align:center;">
        <div>
          <h3 style="color:#451a03; font-size:1.35rem; font-weight:800;">7:00 AM Open</h3>
          <p style="color:#57534e; font-size:0.9rem;">Uptown Morning Commute</p>
        </div>
        <div>
          <h3 style="color:#451a03; font-size:1.35rem; font-weight:800;">Scratch Kitchen</h3>
          <p style="color:#57534e; font-size:0.9rem;">Brioche &amp; Bagel Sandwiches</p>
        </div>
        <div>
          <h3 style="color:#451a03; font-size:1.35rem; font-weight:800;">Artisan Espresso</h3>
          <p style="color:#57534e; font-size:0.9rem;">Single Origin &amp; House Syrups</p>
        </div>
        <div>
          <h3 style="color:#451a03; font-size:1.35rem; font-weight:800;">Office Catering</h3>
          <p style="color:#57534e; font-size:0.9rem;">Sandwich Trays &amp; Coffee Boxes</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Main Narrative Section -->
  <main class="lottie-container" style="padding:60px 24px;">
    <div class="lottie-grid-2" style="align-items:center; margin-bottom:60px;">
      <div>
        <span class="lottie-tag">Warm Neighborhood Soul</span>
        <h2 style="font-size:2.2rem; color:#451a03; margin:15px 0; font-weight:800;">Crafted with Care from Morning to Mid-Afternoon</h2>
        <p style="color:#57534e; line-height:1.7; margin-bottom:16px;">
          Set inside the revitalized Queen City Quarter directly adjoining the CTC / Arena transit hub, Lottie's Cafe offers an inviting oasis for coffee aficionados, morning commuters, and corporate teams.
        </p>
        <p style="color:#57534e; line-height:1.7; margin-bottom:20px;">
          We believe in real ingredients: cage-free eggs cooked to fluffy perfection, thick-cut applewood bacon, fresh avocado mashed daily, and locally roasted specialty beans pulled on a calibrated multi-boiler espresso machine.
        </p>
        <div style="display:flex; gap:12px; flex-wrap:wrap;">
          <a href="menu.html" class="lottie-btn-primary">Browse Cafe Menu</a>
          <a href="visit.html" class="lottie-btn-outline" style="color:#451a03; border-color:#451a03;">Hours &amp; Directions</a>
        </div>
      </div>
      <div>
        <img src="images/breakfast-sandwich-bagel.jpg" alt="Handcrafted brioche breakfast sandwich at Lottie's Cafe Charlotte" style="width:100%; height:400px; object-fit:cover; border-radius:12px; box-shadow:var(--lottie-shadow-lg);">
      </div>
    </div>

    <!-- Featured Dishes Grid -->
    <div style="text-align:center; margin-bottom:40px;">
      <span class="lottie-tag">Signature Favorites</span>
      <h2 style="font-size:2rem; color:#451a03; margin-top:10px;">Cafe Highlights</h2>
    </div>

    <div class="lottie-grid-3" style="margin-bottom:60px;">
      <div class="lottie-feature-card">
        <img src="images/breakfast-sandwich-bagel.jpg" alt="Signature Bacon Egg &amp; Cheese Brioche" class="lottie-feature-img">
        <div class="lottie-feature-body">
          <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
            <h3 style="color:#451a03; font-size:1.25rem;">Bacon Egg &amp; Aged Cheddar</h3>
            <span style="font-weight:700; color:#ea580c; font-size:1.1rem;">$10.50</span>
          </div>
          <p style="color:#57534e; font-size:0.95rem; margin-bottom:16px;">Two farm eggs, thick-cut applewood bacon, melted Vermont cheddar, and house maple aioli on a toasted butter brioche bun.</p>
          <span class="lottie-tag">Breakfast Benchmark</span>
        </div>
      </div>

      <div class="lottie-feature-card">
        <img src="images/artisan-espresso-latte.jpg" alt="Artisan Lavender Honey Latte" class="lottie-feature-img">
        <div class="lottie-feature-body">
          <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
            <h3 style="color:#451a03; font-size:1.25rem;">Lavender Honey Latte</h3>
            <span style="font-weight:700; color:#ea580c; font-size:1.1rem;">$6.25</span>
          </div>
          <p style="color:#57534e; font-size:0.95rem; margin-bottom:16px;">Double shot of specialty espresso, wild French lavender syrup, raw local wildflower honey, and velvety steamed whole or oat milk.</p>
          <span class="lottie-tag">Barista Specialty</span>
        </div>
      </div>

      <div class="lottie-feature-card">
        <img src="images/avocado-toast-bowl.jpg" alt="Loaded Avocado Tartine" class="lottie-feature-img">
        <div class="lottie-feature-body">
          <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
            <h3 style="color:#451a03; font-size:1.25rem;">Queen City Avocado Tartine</h3>
            <span style="font-weight:700; color:#ea580c; font-size:1.1rem;">$11.95</span>
          </div>
          <p style="color:#57534e; font-size:0.95rem; margin-bottom:16px;">Toasted artisanal sourdough, fresh smashed avocado, heirloom cherry tomatoes, pickled shallots, everything bagel spice, and organic microgreens.</p>
          <span class="lottie-tag">Fresh &amp; Healthy</span>
        </div>
      </div>
    </div>

    <!-- Corporate Breakfast & Lunch Strip -->
    <div class="lottie-banner-strip">
      <span class="lottie-badge" style="background:rgba(255,255,255,0.15); border-color:#ffffff; color:#ffffff;">Corporate Catering</span>
      <h2 style="font-size:2rem; margin:12px 0 16px; color:#ffffff;">Planning a Morning Meeting in Uptown Charlotte?</h2>
      <p style="max-width:700px; margin:0 auto 24px; color:#f5f5f4; font-size:1.05rem;">
        Order our fresh breakfast sandwich crates, bakery croissant boxes, and 96oz travel coffee carafes for your team meetings.
      </p>
      <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
        <a href="morning-catering-and-coffee-boxes.html" class="lottie-btn-primary">View Catering Packages</a>
        <a href="tel:7047893135" class="lottie-btn-outline">Call (704) 789-3135</a>
      </div>
    </div>
  </main>

{footer_html()}
"""

with open("lottie-s-cafe/index.html", "w", encoding="utf-8") as f:
    f.write(index_content)
print("Written: lottie-s-cafe/index.html")

# Page 2: menu.html
menu_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Full Cafe Menu | Lottie's Cafe Uptown Charlotte NC</title>
  <meta name="description" content="View the complete menu at Lottie's Cafe in Queen City Quarter Charlotte: breakfast sandwiches, Beattie's bagels, Hugo's hash, paninis, espresso, and lattes.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("menu.html")}

  <section class="lottie-hero-compact">
    <div class="lottie-container">
      <span class="lottie-badge">Kitchen &amp; Espresso Bar</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Our Complete Cafe Menu</h1>
      <p style="font-size:1.1rem; color:#f5f5f4; max-width:700px; margin:0 auto;">All-day breakfast handhelds, artisan bagels, fresh power bowls, crafted paninis, and specialty coffee.</p>
    </div>
  </section>

  <main class="lottie-container" style="padding:40px 24px 60px;">
    <!-- Interactive Filter Buttons -->
    <div class="lottie-filters">
      <button class="lottie-filter-btn active" data-filter="all">All Items</button>
      <button class="lottie-filter-btn" data-filter="breakfast">Breakfast &amp; Sandwiches</button>
      <button class="lottie-filter-btn" data-filter="bagels">Beattie's Bagels</button>
      <button class="lottie-filter-btn" data-filter="lunch">Lunch Paninis &amp; Bowls</button>
      <button class="lottie-filter-btn" data-filter="coffee">Espresso &amp; Lattes</button>
      <button class="lottie-filter-btn" data-filter="bakery">Bakery &amp; Pastries</button>
    </div>

    <!-- Menu Grid -->
    <div class="lottie-grid-3" id="menu-items-grid" style="gap:24px;">
      <!-- Breakfast Handhelds -->
      <div class="lottie-card lottie-menu-item" data-category="breakfast">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#451a03; font-size:1.2rem;">Bacon Egg &amp; Cheese Brioche</h3>
          <span style="font-weight:700; color:#ea580c; font-size:1.1rem;">$10.50</span>
        </div>
        <p style="color:#57534e; font-size:0.95rem; margin-bottom:12px;">Folded farm eggs, thick applewood bacon, melted sharp cheddar, and maple aioli on a toasted butter brioche bun.</p>
        <span class="lottie-tag">House Signature</span>
      </div>

      <div class="lottie-card lottie-menu-item" data-category="breakfast">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#451a03; font-size:1.2rem;">Hugo's Skillet Hash</h3>
          <span style="font-weight:700; color:#ea580c; font-size:1.1rem;">$13.50</span>
        </div>
        <p style="color:#57534e; font-size:0.95rem; margin-bottom:12px;">Crispy Yukon gold potatoes roasted with chorizo sausage, bell peppers, caramelized onions, topped with two sunny eggs and avocado crema.</p>
        <span class="lottie-tag">Skillet Hash</span>
      </div>

      <div class="lottie-card lottie-menu-item" data-category="breakfast">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#451a03; font-size:1.2rem;">Sausage Egg &amp; Gouda Croissant</h3>
          <span style="font-weight:700; color:#ea580c; font-size:1.1rem;">$11.00</span>
        </div>
        <p style="color:#57534e; font-size:0.95rem; margin-bottom:12px;">Savory sage pork sausage patty, fluffy egg, melted smoked gouda cheese, and honey mustard on a warm flaky butter croissant.</p>
        <span class="lottie-tag">Bakery Sandwich</span>
      </div>

      <!-- Bagels -->
      <div class="lottie-card lottie-menu-item" data-category="bagels">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#451a03; font-size:1.2rem;">Beattie's Lox &amp; Cream Cheese</h3>
          <span style="font-weight:700; color:#ea580c; font-size:1.1rem;">$13.95</span>
        </div>
        <p style="color:#57534e; font-size:0.95rem; margin-bottom:12px;">Toasted Everything Beattie's bagel, Nova cold-smoked salmon, whipped chive cream cheese, capers, shaved red onion, and fresh dill.</p>
        <span class="lottie-tag">Bagel Benchmark</span>
      </div>

      <div class="lottie-card lottie-menu-item" data-category="bagels">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#451a03; font-size:1.2rem;">Beattie's Avocado &amp; Tomato Bagel</h3>
          <span style="font-weight:700; color:#ea580c; font-size:1.1rem;">$9.50</span>
        </div>
        <p style="color:#57534e; font-size:0.95rem; margin-bottom:12px;">Toasted sesame bagel layered with fresh smashed avocado, ripe vine tomato slices, sea salt, lemon juice, and microgreens.</p>
        <span class="lottie-tag">Vegetarian</span>
      </div>

      <!-- Lunch Paninis & Bowls -->
      <div class="lottie-card lottie-menu-item" data-category="lunch">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#451a03; font-size:1.2rem;">Smoked Turkey &amp; Avocado Panini</h3>
          <span style="font-weight:700; color:#ea580c; font-size:1.1rem;">$13.50</span>
        </div>
        <p style="color:#57534e; font-size:0.95rem; margin-bottom:12px;">Herb-roasted turkey breast, fresh avocado, smoked provolone cheese, baby spinach, and sun-dried tomato pesto on grilled focaccia.</p>
        <span class="lottie-tag">Lunch Favorite</span>
      </div>

      <div class="lottie-card lottie-menu-item" data-category="lunch">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#451a03; font-size:1.2rem;">Tuscan Caprese Panini</h3>
          <span style="font-weight:700; color:#ea580c; font-size:1.1rem;">$12.50</span>
        </div>
        <p style="color:#57534e; font-size:0.95rem; margin-bottom:12px;">Fresh mozzarella, heirloom tomatoes, fresh basil leaves, extra virgin olive oil, and aged balsamic glaze pressed on crusty ciabatta.</p>
        <span class="lottie-tag">Vegetarian</span>
      </div>

      <div class="lottie-card lottie-menu-item" data-category="lunch">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#451a03; font-size:1.2rem;">Trade St. Power Grain Bowl</h3>
          <span style="font-weight:700; color:#ea580c; font-size:1.1rem;">$13.00</span>
        </div>
        <p style="color:#57534e; font-size:0.95rem; margin-bottom:12px;">Organic quinoa, roasted sweet potatoes, charred broccoli, chickpeas, avocado slices, pickled onions, and lemon tahini dressing.</p>
        <span class="lottie-tag">Healthy Grain Bowl</span>
      </div>

      <!-- Coffee & Lattes -->
      <div class="lottie-card lottie-menu-item" data-category="coffee">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#451a03; font-size:1.2rem;">Lavender Honey Latte</h3>
          <span style="font-weight:700; color:#ea580c; font-size:1.1rem;">$6.25</span>
        </div>
        <p style="color:#57534e; font-size:0.95rem; margin-bottom:12px;">Espresso, organic French lavender syrup, raw wildflower honey, and silky steamed whole or oat milk.</p>
        <span class="lottie-tag">Specialty Latte</span>
      </div>

      <div class="lottie-card lottie-menu-item" data-category="coffee">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#451a03; font-size:1.2rem;">Brown Sugar Shaken Espresso</h3>
          <span style="font-weight:700; color:#ea580c; font-size:1.1rem;">$6.00</span>
        </div>
        <p style="color:#57534e; font-size:0.95rem; margin-bottom:12px;">Espresso shaken over ice with brown sugar, ground cinnamon, and topped with creamy oat milk.</p>
        <span class="lottie-tag">Iced Specialty</span>
      </div>

      <div class="lottie-card lottie-menu-item" data-category="coffee">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#451a03; font-size:1.2rem;">Cold Brew Nitro Draft</h3>
          <span style="font-weight:700; color:#ea580c; font-size:1.1rem;">$5.50</span>
        </div>
        <p style="color:#57534e; font-size:0.95rem; margin-bottom:12px;">Single-origin beans steeped for 20 hours and infused with nitrogen for a cascading velvet head and natural sweetness.</p>
        <span class="lottie-tag">Draft Nitro</span>
      </div>

      <!-- Bakery -->
      <div class="lottie-card lottie-menu-item" data-category="bakery">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#451a03; font-size:1.2rem;">Almond Cream Croissant</h3>
          <span style="font-weight:700; color:#ea580c; font-size:1.1rem;">$5.25</span>
        </div>
        <p style="color:#57534e; font-size:0.95rem; margin-bottom:12px;">Twice-baked butter croissant filled with rich almond frangipane cream, dusted with toasted sliced almonds and powdered sugar.</p>
        <span class="lottie-tag">Fresh Baked</span>
      </div>

      <div class="lottie-card lottie-menu-item" data-category="bakery">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#451a03; font-size:1.2rem;">Blueberry Lemon Scone</h3>
          <span style="font-weight:700; color:#ea580c; font-size:1.1rem;">$4.50</span>
        </div>
        <p style="color:#57534e; font-size:0.95rem; margin-bottom:12px;">Tender house-baked butter scone studded with fresh blueberries, finished with tart lemon zest glaze.</p>
        <span class="lottie-tag">Bakery Item</span>
      </div>
    </div>

    <!-- Takeout CTA -->
    <div style="text-align:center; margin-top:50px; background:#ffffff; border:1px solid #e7e5e4; border-radius:12px; padding:30px; box-shadow:var(--lottie-shadow);">
      <h3 style="color:#451a03; font-size:1.5rem; margin-bottom:10px;">Order Ahead for Express Counter Pickup</h3>
      <p style="color:#57534e; max-width:600px; margin:0 auto 20px;">Call our cafe counter directly to place morning drink orders and hot breakfast sandwiches.</p>
      <a href="tel:7047893135" class="lottie-btn-primary">Call (704) 789-3135</a>
    </div>
  </main>

{footer_html()}
"""

with open("lottie-s-cafe/menu.html", "w", encoding="utf-8") as f:
    f.write(menu_content)
print("Written: lottie-s-cafe/menu.html")

