# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("scripts")
from halfpenny_builder import header_html, footer_html

# Page 1: index.html
index_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Halfpenny's Cafe | Concourse Breakfast &amp; Deli Uptown Charlotte</title>
  <meta name="description" content="Welcome to Halfpenny's Cafe at 301 S Tryon St in Uptown Charlotte. Scratch buttermilk biscuits, made-to-order omelets, artisan deli sandwiches, and corporate catering.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("index.html")}

  <section class="halfpenny-hero">
    <div class="halfpenny-container">
      <span class="halfpenny-badge">Uptown Concourse Staple at 301 S Tryon</span>
      <h1 style="font-size:2.8rem; font-weight:900; margin:15px 0; letter-spacing:-0.02em;">Fresh Morning Biscuits &amp; Artisan Deli Comfort</h1>
      <p style="font-size:1.15rem; color:#e2e8f0; max-width:760px; margin:0 auto 25px;">
        Located on the lower concourse level of 301 South Tryon Street, Halfpenny's Cafe has served Uptown Charlotte with made-from-scratch breakfast biscuits, custom omelets, and premium deli subs for decades.
      </p>
      <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
        <a href="menu.html" class="halfpenny-btn-primary">View Full Menu</a>
        <a href="concourse-breakfast-and-omelets.html" class="halfpenny-btn-outline">Breakfast &amp; Omelets</a>
        <a href="tel:7043429697" class="halfpenny-btn-primary" style="background:#b45309; color:#fff;">Order: (704) 342-9697</a>
      </div>
    </div>
  </section>

  <!-- Key Highlights Bar -->
  <section style="background-color:#ffffff; border-bottom:1px solid #e2e8f0; padding:28px 0;">
    <div class="halfpenny-container">
      <div class="halfpenny-grid-4" style="text-align:center;">
        <div>
          <h3 style="color:#0f172a; font-size:1.35rem; font-weight:800;">7:00 AM Open</h3>
          <p style="color:#475569; font-size:0.9rem;">Uptown Concourse Breakfast</p>
        </div>
        <div>
          <h3 style="color:#0f172a; font-size:1.35rem; font-weight:800;">Hot Biscuits</h3>
          <p style="color:#475569; font-size:0.9rem;">Scratch Southern Buttermilk</p>
        </div>
        <div>
          <h3 style="color:#0f172a; font-size:1.35rem; font-weight:800;">Custom Omelets</h3>
          <p style="color:#475569; font-size:0.9rem;">3-Egg Made to Order</p>
        </div>
        <div>
          <h3 style="color:#0f172a; font-size:1.35rem; font-weight:800;">Tower Catering</h3>
          <p style="color:#475569; font-size:0.9rem;">Tryon St Meeting Boxes</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Main Narrative Section -->
  <main class="halfpenny-container" style="padding:60px 24px;">
    <div class="halfpenny-grid-2" style="align-items:center; margin-bottom:60px;">
      <div>
        <span class="halfpenny-tag">Concourse Heritage</span>
        <h2 style="font-size:2.2rem; color:#0f172a; margin:15px 0; font-weight:800;">Quick, Wholesome &amp; Friendly Service</h2>
        <p style="color:#475569; line-height:1.7; margin-bottom:16px;">
          Tucked directly downstairs on the lower concourse of 301 S Tryon, Halfpenny's Cafe is the cherished morning ritual for banking executives, legal teams, and office workers. We pride ourselves on knowing our regulars by name and getting your breakfast hot and ready without delay.
        </p>
        <p style="color:#475569; line-height:1.7; margin-bottom:20px;">
          From our fluffy Southern buttermilk breakfast biscuits to our signature Tarragon Chicken Salad and stacked Triple Decker Clubs, every item is made with fresh deli meats, real cheeses, and crisp produce.
        </p>
        <div style="display:flex; gap:12px; flex-wrap:wrap;">
          <a href="menu.html" class="halfpenny-btn-primary">Browse Full Menu</a>
          <a href="visit.html" class="halfpenny-btn-outline" style="color:#0f172a; border-color:#0f172a;">Find Our Counter</a>
        </div>
      </div>
      <div>
        <img src="images/breakfast-biscuit-omelet.jpg" alt="Made to order breakfast biscuit and omelet at Halfpenny's Cafe" style="width:100%; height:400px; object-fit:cover; border-radius:12px; box-shadow:var(--halfpenny-shadow-lg);">
      </div>
    </div>

    <!-- Featured Food Grid -->
    <div style="text-align:center; margin-bottom:40px;">
      <span class="halfpenny-tag">Concourse Staples</span>
      <h2 style="font-size:2rem; color:#0f172a; margin-top:10px;">Customer Favorites</h2>
    </div>

    <div class="halfpenny-grid-3" style="margin-bottom:60px;">
      <div class="halfpenny-feature-card">
        <img src="images/breakfast-biscuit-omelet.jpg" alt="Southern Bacon Egg Cheese Biscuit" class="halfpenny-feature-img">
        <div class="halfpenny-feature-body">
          <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
            <h3 style="color:#0f172a; font-size:1.25rem;">Southern Breakfast Biscuit</h3>
            <span style="font-weight:700; color:#b45309; font-size:1.1rem;">$7.50</span>
          </div>
          <p style="color:#475569; font-size:0.95rem; margin-bottom:16px;">Warm scratch-baked buttermilk biscuit with folded egg, melted sharp cheddar, and choice of thick bacon, country sausage, or country ham.</p>
          <span class="halfpenny-tag">Morning Benchmark</span>
        </div>
      </div>

      <div class="halfpenny-feature-card">
        <img src="images/deli-club-sandwich.jpg" alt="Triple Decker Turkey Club" class="halfpenny-feature-img">
        <div class="halfpenny-feature-body">
          <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
            <h3 style="color:#0f172a; font-size:1.25rem;">Tryon Triple Decker Club</h3>
            <span style="font-weight:700; color:#b45309; font-size:1.1rem;">$12.95</span>
          </div>
          <p style="color:#475569; font-size:0.95rem; margin-bottom:16px;">Roasted turkey breast, honey ham, applewood bacon, Swiss cheese, crisp lettuce, ripe tomato, and mayo on toasted sourdough with kettle chips.</p>
          <span class="halfpenny-tag">Deli Classic</span>
        </div>
      </div>

      <div class="halfpenny-feature-card">
        <img src="images/tarragon-chicken-salad.jpg" alt="Tarragon Chicken Salad Croissant" class="halfpenny-feature-img">
        <div class="halfpenny-feature-body">
          <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
            <h3 style="color:#0f172a; font-size:1.25rem;">Tarragon Chicken Salad</h3>
            <span style="font-weight:700; color:#b45309; font-size:1.1rem;">$11.95</span>
          </div>
          <p style="color:#475569; font-size:0.95rem; margin-bottom:16px;">Poached chicken breast tossed with fresh chopped tarragon, dried cranberries, celery, and light mayo on a flaky French croissant.</p>
          <span class="halfpenny-tag">House Specialty</span>
        </div>
      </div>
    </div>

    <!-- Corporate Tower Catering Banner -->
    <div class="halfpenny-banner-strip">
      <span class="halfpenny-badge" style="background:rgba(217,119,6,0.25); border-color:#f59e0b; color:#ffffff;">Office Breakfast &amp; Box Lunches</span>
      <h2 style="font-size:2rem; margin:12px 0 16px; color:#ffffff;">Corporate Catering for South Tryon Towers</h2>
      <p style="max-width:700px; margin:0 auto 24px; color:#cbd5e1; font-size:1.05rem;">
        Ordering breakfast biscuits, bagel platters, or box lunches for your firm? We provide direct tower delivery and pickup packaging across Uptown.
      </p>
      <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
        <a href="office-catering-and-breakfast-boxes.html" class="halfpenny-btn-primary">View Catering Packages</a>
        <a href="tel:7043429697" class="halfpenny-btn-outline">Call (704) 342-9697</a>
      </div>
    </div>
  </main>

{footer_html()}
"""

with open("halfpenny-s-cafe/index.html", "w", encoding="utf-8") as f:
    f.write(index_content)
print("Written: halfpenny-s-cafe/index.html")

# Page 2: menu.html
menu_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Full Cafe &amp; Deli Menu | Halfpenny's Cafe Uptown Charlotte</title>
  <meta name="description" content="Explore the full menu at Halfpenny's Cafe in 301 S Tryon Charlotte: breakfast biscuits, custom 3-egg omelets, deli sandwiches, tarragon chicken salad, and coffee.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("menu.html")}

  <section class="halfpenny-hero-compact">
    <div class="halfpenny-container">
      <span class="halfpenny-badge">Concourse Cafe &amp; Deli</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Our Complete Cafe Menu</h1>
      <p style="font-size:1.1rem; color:#cbd5e1; max-width:700px; margin:0 auto;">Scratch morning biscuits, customized omelets, handcrafted deli subs, crisp salads, and fresh coffee.</p>
    </div>
  </section>

  <main class="halfpenny-container" style="padding:40px 24px 60px;">
    <!-- Interactive Filter Buttons -->
    <div class="halfpenny-filters">
      <button class="halfpenny-filter-btn active" data-filter="all">All Items</button>
      <button class="halfpenny-filter-btn" data-filter="biscuits">Breakfast Biscuits &amp; Handhelds</button>
      <button class="halfpenny-filter-btn" data-filter="omelets">Custom Omelets &amp; Platters</button>
      <button class="halfpenny-filter-btn" data-filter="deli">Artisan Deli Sandwiches</button>
      <button class="halfpenny-filter-btn" data-filter="salads">Fresh Salads &amp; Bowls</button>
      <button class="halfpenny-filter-btn" data-filter="coffee">Espresso &amp; Coffee</button>
    </div>

    <!-- Menu Grid -->
    <div class="halfpenny-grid-3" id="menu-items-grid" style="gap:24px;">
      <!-- Biscuits & Handhelds -->
      <div class="halfpenny-card halfpenny-menu-item" data-category="biscuits">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Southern Bacon Egg &amp; Cheese</h3>
          <span style="font-weight:700; color:#b45309; font-size:1.1rem;">$7.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Fluffy scrambled egg, thick applewood bacon, and melted sharp cheddar on a scratch-made buttermilk biscuit.</p>
        <span class="halfpenny-tag">House Benchmark</span>
      </div>

      <div class="halfpenny-card halfpenny-menu-item" data-category="biscuits">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Country Sausage &amp; Egg Biscuit</h3>
          <span style="font-weight:700; color:#b45309; font-size:1.1rem;">$7.25</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Savory sage pork sausage patty and folded egg with melted American cheese on a warm golden biscuit.</p>
        <span class="halfpenny-tag">Southern Classic</span>
      </div>

      <div class="halfpenny-card halfpenny-menu-item" data-category="biscuits">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Egg White &amp; Avocado Wrap (GF)</h3>
          <span style="font-weight:700; color:#b45309; font-size:1.1rem;">$8.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Fluffy egg whites, fresh avocado, baby spinach, and Swiss cheese wrapped in a gluten-free spinach tortilla.</p>
        <span class="halfpenny-tag">Gluten-Free</span>
      </div>

      <!-- Omelets & Platters -->
      <div class="halfpenny-card halfpenny-menu-item" data-category="omelets">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Western 3-Egg Omelet</h3>
          <span style="font-weight:700; color:#b45309; font-size:1.1rem;">$11.95</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Three farm eggs folded with diced smoked ham, green bell peppers, sweet onions, and cheddar cheese. Served with hashbrowns and toast.</p>
        <span class="halfpenny-tag">Omelet Platter</span>
      </div>

      <div class="halfpenny-card halfpenny-menu-item" data-category="omelets">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Garden Veggie &amp; Feta Omelet</h3>
          <span style="font-weight:700; color:#b45309; font-size:1.1rem;">$11.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Mushrooms, baby spinach, diced tomatoes, onions, and crumbled Greek feta cheese, served with crispy potatoes and biscuit.</p>
        <span class="halfpenny-tag">Vegetarian</span>
      </div>

      <div class="halfpenny-card halfpenny-menu-item" data-category="omelets">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Tryon Power Breakfast Platter</h3>
          <span style="font-weight:700; color:#b45309; font-size:1.1rem;">$12.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Two eggs any style, choice of three bacon strips or two sausage patties, crispy seasoned hashbrowns, and a buttermilk biscuit with jelly.</p>
        <span class="halfpenny-tag">Full Platter</span>
      </div>

      <!-- Deli Sandwiches -->
      <div class="halfpenny-card halfpenny-menu-item" data-category="deli">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Tryon Triple Decker Club</h3>
          <span style="font-weight:700; color:#b45309; font-size:1.1rem;">$12.95</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Sliced roast turkey, smoked ham, bacon, Swiss cheese, lettuce, tomato, and mayonnaise layered on toasted sourdough with kettle chips.</p>
        <span class="halfpenny-tag">Bestseller</span>
      </div>

      <div class="halfpenny-card halfpenny-menu-item" data-category="deli">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Tarragon Chicken Salad Croissant</h3>
          <span style="font-weight:700; color:#b45309; font-size:1.1rem;">$11.95</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">House-poached chicken salad with fresh tarragon, dried cranberries, and celery on a flaky butter croissant with side pasta salad.</p>
        <span class="halfpenny-tag">House Specialty</span>
      </div>

      <div class="halfpenny-card halfpenny-menu-item" data-category="deli">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Hot Pastrami &amp; Swiss on Rye</h3>
          <span style="font-weight:700; color:#b45309; font-size:1.1rem;">$12.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Warm sliced New York pastrami, melted Swiss cheese, and spicy stone-ground brown mustard on grilled marbled rye with deli pickle spear.</p>
        <span class="halfpenny-tag">Hot Deli</span>
      </div>

      <div class="halfpenny-card halfpenny-menu-item" data-category="deli">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Turkey Avocado Bacon Melt</h3>
          <span style="font-weight:700; color:#b45309; font-size:1.1rem;">$12.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Sliced turkey breast, applewood bacon, fresh avocado, melted provolone, and herb aioli grilled warm on multigrain bread.</p>
        <span class="halfpenny-tag">Warm Melt</span>
      </div>

      <!-- Salads & Bowls -->
      <div class="halfpenny-card halfpenny-menu-item" data-category="salads">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Halfpenny's Chef Salad</h3>
          <span style="font-weight:700; color:#b45309; font-size:1.1rem;">$12.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Crisp mixed greens, sliced turkey, ham, cheddar and Swiss cheeses, hard-boiled egg, cucumbers, tomatoes, and house ranch dressing.</p>
        <span class="halfpenny-tag">Chef Salad</span>
      </div>

      <!-- Coffee -->
      <div class="halfpenny-card halfpenny-menu-item" data-category="coffee">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Fresh Brewed Drip Coffee</h3>
          <span style="font-weight:700; color:#b45309; font-size:1.1rem;">$3.00</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Locally roasted medium and dark roast beans brewed fresh continuously all morning. Whole milk, half &amp; half, and oat milk available.</p>
        <span class="halfpenny-tag">Fresh Brew</span>
      </div>

      <div class="halfpenny-card halfpenny-menu-item" data-category="coffee">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#0f172a; font-size:1.2rem;">Iced Caramel Vanilla Latte</h3>
          <span style="font-weight:700; color:#b45309; font-size:1.1rem;">$5.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Double espresso shot poured over ice with vanilla bean syrup, whole or oat milk, and rich salted caramel drizzle.</p>
        <span class="halfpenny-tag">Iced Latte</span>
      </div>
    </div>

    <!-- Takeout CTA -->
    <div style="text-align:center; margin-top:50px; background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:30px; box-shadow:var(--halfpenny-shadow);">
      <h3 style="color:#0f172a; font-size:1.5rem; margin-bottom:10px;">Call Ahead for Fast Concourse Pickup</h3>
      <p style="color:#475569; max-width:600px; margin:0 auto 20px;">Avoid the morning rush by calling your breakfast or deli order ahead directly to Suite 30.</p>
      <a href="tel:7043429697" class="halfpenny-btn-primary">Call (704) 342-9697</a>
    </div>
  </main>

{footer_html()}
"""

with open("halfpenny-s-cafe/menu.html", "w", encoding="utf-8") as f:
    f.write(menu_content)
print("Written: halfpenny-s-cafe/menu.html")

