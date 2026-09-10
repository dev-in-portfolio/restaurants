# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("scripts")
from halfpenny_builder import header_html, footer_html

# Page 3: concourse-breakfast-and-omelets.html
breakfast_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Concourse Breakfast &amp; Omelets | Halfpenny's Cafe Charlotte NC</title>
  <meta name="description" content="Discover made-to-order breakfast biscuits, custom 3-egg omelets, gluten-free breakfast wraps, and hashbrowns at Halfpenny's Cafe inside 301 S Tryon Uptown Charlotte.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("concourse-breakfast-and-omelets.html")}

  <section class="halfpenny-hero-compact">
    <div class="halfpenny-container">
      <span class="halfpenny-badge">Scratch Morning Grill</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Concourse Breakfast &amp; Custom Omelets</h1>
      <p style="font-size:1.1rem; color:#cbd5e1; max-width:720px; margin:0 auto;">Served hot and fast starting at 7:00 AM every weekday morning on the lower level of 301 South Tryon.</p>
    </div>
  </section>

  <main class="halfpenny-container" style="padding:60px 24px;">
    <!-- Biscuit & Omelet Focus -->
    <div class="halfpenny-grid-2" style="align-items:center; margin-bottom:60px;">
      <div>
        <span class="halfpenny-tag">Scratch Kitchen Tradition</span>
        <h2 style="font-size:2.1rem; color:#0f172a; margin:15px 0; font-weight:800;">Hot Breakfast Made Fresh Daily</h2>
        <p style="color:#475569; line-height:1.7; margin-bottom:15px;">
          At Halfpenny's Cafe, we know mornings in Uptown Charlotte move quickly. That's why our grill cooks prepare everything to order in minutes: cracking whole farm eggs, searing crisp bacon on the flat-top, and baking our golden buttermilk biscuits every morning.
        </p>
        <p style="color:#475569; line-height:1.7; margin-bottom:15px;">
          Prefer your eggs customized? Our three-egg omelets can be loaded with your choice of ham, sausage, bacon, spinach, mushrooms, peppers, onions, and melted cheeses, served with crispy hashbrowns and warm toast or biscuits.
        </p>
        <div style="background:#fef3c7; border-left:4px solid #b45309; padding:16px; border-radius:6px; margin-top:20px;">
          <h4 style="color:#92400e; margin-bottom:4px;">Gluten-Free &amp; Healthy Accommodations</h4>
          <p style="color:#78350f; font-size:0.95rem; margin:0;">We offer gluten-free bread, egg white substitutions, and fresh fruit cups so everyone can enjoy a hearty, nourishing breakfast.</p>
        </div>
      </div>
      <div>
        <img src="images/breakfast-biscuit-omelet.jpg" alt="Golden Southern breakfast biscuit and custom omelet platter at Halfpenny's" style="width:100%; height:400px; object-fit:cover; border-radius:12px; box-shadow:var(--halfpenny-shadow-lg);">
      </div>
    </div>

    <!-- Breakfast Menu Grid -->
    <h2 style="font-size:1.9rem; color:#0f172a; text-align:center; margin-bottom:35px;">Morning Grill Selections</h2>
    
    <div class="halfpenny-grid-3" style="gap:28px; margin-bottom:60px;">
      <div class="halfpenny-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Bacon Egg &amp; Cheese Biscuit</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Warm scratch-made buttermilk biscuit, folded egg, thick applewood smoked bacon, and melted sharp cheddar cheese.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#b45309; font-size:1.15rem;">$7.50</span>
          <span class="halfpenny-tag">House Benchmark</span>
        </div>
      </div>

      <div class="halfpenny-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Western 3-Egg Omelet</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Diced smoked ham, green bell peppers, sweet onions, and cheddar cheese folded into three eggs. Served with hashbrowns and biscuit.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#b45309; font-size:1.15rem;">$11.95</span>
          <span class="halfpenny-tag">Omelet Platter</span>
        </div>
      </div>

      <div class="halfpenny-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Country Sausage &amp; Egg Biscuit</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Savory sage pork sausage patty, folded egg, and melted American cheese on a freshly baked Southern biscuit.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#b45309; font-size:1.15rem;">$7.25</span>
          <span class="halfpenny-tag">Southern Classic</span>
        </div>
      </div>

      <div class="halfpenny-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Garden Spinach &amp; Feta Omelet</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Three eggs with sauteed button mushrooms, fresh spinach, diced tomatoes, onions, and crumbled Greek feta with hashbrowns.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#b45309; font-size:1.15rem;">$11.50</span>
          <span class="halfpenny-tag">Vegetarian</span>
        </div>
      </div>

      <div class="halfpenny-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Tryon Power Breakfast Platter</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Two eggs cooked to order, choice of three bacon strips or two sausage patties, crispy hashbrowns, and biscuit with butter and jelly.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#b45309; font-size:1.15rem;">$12.50</span>
          <span class="halfpenny-tag">Full Breakfast</span>
        </div>
      </div>

      <div class="halfpenny-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Egg White &amp; Avocado Wrap (GF)</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Fluffy scrambled egg whites, fresh sliced avocado, baby spinach, and Swiss cheese inside a gluten-free spinach tortilla.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#b45309; font-size:1.15rem;">$8.50</span>
          <span class="halfpenny-tag">Gluten-Free</span>
        </div>
      </div>
    </div>

    <!-- Call to Action Banner -->
    <div class="halfpenny-banner-strip">
      <h2 style="color:#ffffff; font-size:2rem; margin-bottom:12px;">Your Uptown Morning Starts at Halfpenny's</h2>
      <p style="color:#cbd5e1; max-width:650px; margin:0 auto 20px;">Stop by our counter on the lower level of 301 S Tryon or call ahead for quick pickup.</p>
      <a href="tel:7043429697" class="halfpenny-btn-primary">Call (704) 342-9697</a>
    </div>
  </main>

{footer_html()}
"""

with open("halfpenny-s-cafe/concourse-breakfast-and-omelets.html", "w", encoding="utf-8") as f:
    f.write(breakfast_content)
print("Written: halfpenny-s-cafe/concourse-breakfast-and-omelets.html")

# Page 4: artisan-deli-and-specialty-subs.html
deli_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Artisan Deli &amp; Specialty Subs | Halfpenny's Cafe Charlotte NC</title>
  <meta name="description" content="Savor handcrafted deli subs, Triple Decker Clubs, Tarragon Chicken Salad croissants, and Hot Pastrami on Rye at Halfpenny's Cafe in Uptown Charlotte.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("artisan-deli-and-specialty-subs.html")}

  <section class="halfpenny-hero-compact">
    <div class="halfpenny-container">
      <span class="halfpenny-badge">Handcrafted Lunch Counter</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Artisan Deli Sandwiches &amp; Specialty Subs</h1>
      <p style="font-size:1.1rem; color:#cbd5e1; max-width:720px; margin:0 auto;">Stacked high on freshly delivered bakery breads with premium deli meats, aged cheeses, and house dressings.</p>
    </div>
  </section>

  <main class="halfpenny-container" style="padding:60px 24px;">
    <div class="halfpenny-grid-2" style="align-items:center; margin-bottom:60px;">
      <div>
        <span class="halfpenny-tag">Generous Portions</span>
        <h2 style="font-size:2.1rem; color:#0f172a; margin:15px 0; font-weight:800;">Authentic Concourse Deli Craft</h2>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:15px;">
          When lunchtime arrives in Uptown Charlotte, Halfpenny's Cafe delivers satisfying, unpretentious deli perfection. Every sandwich is built to order with generous portions of thinly shaved roast turkey, hot pastrami, and applewood bacon.
        </p>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:15px;">
          Our house-made Tarragon Chicken Salad features tender poached chicken tossed with fresh herbs, celery, and sweet dried cranberries on flaky croissants, while our classic Triple Decker Club remains an all-time South Tryon favorite.
        </p>
        <ul style="color:#334155; line-height:1.8; padding-left:20px; margin-top:15px;">
          <li>Served with crispy kettle chips and kosher dill pickle spears</li>
          <li>Choice of fresh breads: Sourdough, Marbled Rye, Multigrain, Croissant, or Gluten-Free</li>
          <li>House-made side salads: Potato salad, pasta salad, or fresh fruit</li>
        </ul>
      </div>
      <div>
        <img src="images/deli-club-sandwich.jpg" alt="Artisan Triple Decker Club sandwich at Halfpenny's Cafe Charlotte" style="width:100%; height:400px; object-fit:cover; border-radius:12px; box-shadow:var(--halfpenny-shadow-lg);">
      </div>
    </div>

    <!-- Deli Sandwich Grid -->
    <h2 style="font-size:1.9rem; color:#0f172a; text-align:center; margin-bottom:35px;">Signature Deli Sandwiches</h2>

    <div class="halfpenny-grid-3" style="gap:28px; margin-bottom:60px;">
      <div class="halfpenny-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Tryon Triple Decker Club</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Thinly sliced roast turkey breast, smoked ham, applewood bacon, Swiss cheese, crisp lettuce, tomato, and mayo on toasted sourdough.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#b45309; font-size:1.15rem;">$12.95</span>
          <span class="halfpenny-tag">House Benchmark</span>
        </div>
      </div>

      <div class="halfpenny-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Tarragon Chicken Salad</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Handmade poached chicken salad with fresh chopped tarragon, dried cranberries, celery, and light mayo on a flaky French croissant.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#b45309; font-size:1.15rem;">$11.95</span>
          <span class="halfpenny-tag">House Specialty</span>
        </div>
      </div>

      <div class="halfpenny-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Hot Pastrami &amp; Swiss on Rye</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Warm sliced New York style pastrami, melted Swiss cheese, and spicy brown mustard on grilled marbled rye with deli pickle spear.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#b45309; font-size:1.15rem;">$12.50</span>
          <span class="halfpenny-tag">Hot Deli</span>
        </div>
      </div>

      <div class="halfpenny-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Turkey Bacon Avocado Melt</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Roasted turkey, crispy applewood bacon, fresh avocado, melted provolone cheese, and garlic herb aioli grilled on multigrain bread.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#b45309; font-size:1.15rem;">$12.50</span>
          <span class="halfpenny-tag">Warm Melt</span>
        </div>
      </div>

      <div class="halfpenny-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Classic Tuna Melt</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Albacore white tuna salad with celery and red onion, topped with sliced tomato and melted sharp cheddar cheese grilled golden on sourdough.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#b45309; font-size:1.15rem;">$11.95</span>
          <span class="halfpenny-tag">Classic Melt</span>
        </div>
      </div>

      <div class="halfpenny-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Halfpenny's Chef Salad Bowl</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Crisp mixed salad greens, sliced roasted turkey, ham, cheddar and Swiss, hard-boiled egg, tomatoes, cucumbers, and house ranch dressing.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#b45309; font-size:1.15rem;">$12.50</span>
          <span class="halfpenny-tag">Salad Bowl</span>
        </div>
      </div>
    </div>

    <!-- Takeout Box -->
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:32px; box-shadow:var(--halfpenny-shadow); text-align:center;">
      <h3 style="color:#0f172a; font-size:1.4rem; margin-bottom:10px;">Fast Concourse Lunch Pickup</h3>
      <p style="color:#4b5563; max-width:600px; margin:0 auto 20px;">Call ahead and we will have your sandwich wrapped and bagged ready on the counter.</p>
      <a href="tel:7043429697" class="halfpenny-btn-primary">Call (704) 342-9697 to Order</a>
    </div>
  </main>

{footer_html()}
"""

with open("halfpenny-s-cafe/artisan-deli-and-specialty-subs.html", "w", encoding="utf-8") as f:
    f.write(deli_content)
print("Written: halfpenny-s-cafe/artisan-deli-and-specialty-subs.html")

