# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("scripts")
from lotties_builder import header_html, footer_html

# Page 3: all-day-breakfast-and-sandwiches.html
breakfast_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>All-Day Breakfast &amp; Handhelds | Lottie's Cafe Uptown Charlotte NC</title>
  <meta name="description" content="Savor all-day breakfast sandwiches, Beattie's bagels, Hugo's skillet hash, and artisan paninis at Lottie's Cafe in Queen City Quarter, Uptown Charlotte.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("all-day-breakfast-and-sandwiches.html")}

  <section class="lottie-hero-compact">
    <div class="lottie-container">
      <span class="lottie-badge">All-Day Morning Kitchen</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">All-Day Breakfast &amp; Handcrafted Sandwiches</h1>
      <p style="font-size:1.1rem; color:#f5f5f4; max-width:720px; margin:0 auto;">Made to order with pasture-raised eggs, artisan Beattie's bagels, toasted brioche buns, and house-made spreads.</p>
    </div>
  </section>

  <main class="lottie-container" style="padding:60px 24px;">
    <!-- Sandwich Spotlight -->
    <div class="lottie-grid-2" style="align-items:center; margin-bottom:60px;">
      <div>
        <span class="lottie-tag">Our Breakfast Benchmark</span>
        <h2 style="font-size:2.1rem; color:#451a03; margin:15px 0; font-weight:800;">The Bacon, Egg &amp; Cheese Philosophy</h2>
        <p style="color:#57534e; line-height:1.7; margin-bottom:15px;">
          At Lottie's Cafe, we take breakfast sandwiches seriously. We fold two fresh cage-free farm eggs with real butter, layer them with thick-cut smoky applewood bacon, melt sharp aged Vermont cheddar, and finish with a swipe of our handcrafted maple aioli on a toasted brioche roll.
        </p>
        <p style="color:#57534e; line-height:1.7; margin-bottom:15px;">
          Served warm and wrapped for easy on-the-go commuting or enjoyed in our sunlit cafe lounge, it delivers the ultimate morning comfort to kickstart your Uptown day.
        </p>
        <div style="background:#fff7ed; border-left:4px solid #ea580c; padding:16px; border-radius:6px; margin-top:20px;">
          <h4 style="color:#9a3412; margin-bottom:4px;">Beattie's Bagel Partnership</h4>
          <p style="color:#7c2d12; font-size:0.95rem; margin:0;">We proudly feature fresh Charlotte-made Beattie's Bagels (Plain, Everything, Sesame, and Asiago) boiled and baked daily for perfect chewy crusts.</p>
        </div>
      </div>
      <div>
        <img src="images/breakfast-sandwich-bagel.jpg" alt="Artisan breakfast sandwich on brioche at Lottie's Cafe" style="width:100%; height:400px; object-fit:cover; border-radius:12px; box-shadow:var(--lottie-shadow-lg);">
      </div>
    </div>

    <!-- Breakfast Grid -->
    <h2 style="font-size:1.9rem; color:#451a03; text-align:center; margin-bottom:35px;">Signature Handhelds &amp; Plates</h2>
    
    <div class="lottie-grid-3" style="gap:28px; margin-bottom:60px;">
      <div class="lottie-card">
        <h3 style="color:#451a03; margin-bottom:8px;">Bacon Egg &amp; Cheese Brioche</h3>
        <p style="color:#57534e; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Two folded eggs, thick applewood smoked bacon, aged Vermont cheddar, and house maple aioli on toasted buttered brioche.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e7e5e4; padding-top:12px;">
          <span style="font-weight:700; color:#ea580c; font-size:1.15rem;">$10.50</span>
          <span class="lottie-tag">House Benchmark</span>
        </div>
      </div>

      <div class="lottie-card">
        <h3 style="color:#451a03; margin-bottom:8px;">Beattie's Lox &amp; Cream Cheese</h3>
        <p style="color:#57534e; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Everything Beattie's bagel with Nova cold-smoked salmon, whipped chive cream cheese, capers, shaved shallots, and fresh dill.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e7e5e4; padding-top:12px;">
          <span style="font-weight:700; color:#ea580c; font-size:1.15rem;">$13.95</span>
          <span class="lottie-tag">Local Bagel</span>
        </div>
      </div>

      <div class="lottie-card">
        <h3 style="color:#451a03; margin-bottom:8px;">Hugo's Skillet Hash</h3>
        <p style="color:#57534e; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Crispy Yukon gold potatoes roasted with chorizo sausage, bell peppers, caramelized onions, two sunny eggs, and avocado crema.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e7e5e4; padding-top:12px;">
          <span style="font-weight:700; color:#ea580c; font-size:1.15rem;">$13.50</span>
          <span class="lottie-tag">Skillet Hash</span>
        </div>
      </div>

      <div class="lottie-card">
        <h3 style="color:#451a03; margin-bottom:8px;">Queen City Avocado Tartine</h3>
        <p style="color:#57534e; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Thick-cut toasted sourdough, fresh smashed avocado, cherry tomatoes, pickled shallots, everything seasoning, and microgreens.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e7e5e4; padding-top:12px;">
          <span style="font-weight:700; color:#ea580c; font-size:1.15rem;">$11.95</span>
          <span class="lottie-tag">Plant-Forward</span>
        </div>
      </div>

      <div class="lottie-card">
        <h3 style="color:#451a03; margin-bottom:8px;">Smoked Turkey Avocado Panini</h3>
        <p style="color:#57534e; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Herb-roasted turkey breast, sliced avocado, melted smoked provolone, baby spinach, and sun-dried tomato pesto on grilled focaccia.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e7e5e4; padding-top:12px;">
          <span style="font-weight:700; color:#ea580c; font-size:1.15rem;">$13.50</span>
          <span class="lottie-tag">Lunch Panini</span>
        </div>
      </div>

      <div class="lottie-card">
        <h3 style="color:#451a03; margin-bottom:8px;">Sausage Egg &amp; Gouda Croissant</h3>
        <p style="color:#451a03; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Savory sage pork sausage, fluffy egg, melted smoked gouda cheese, and honey mustard aioli on a warm flaky butter croissant.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e7e5e4; padding-top:12px;">
          <span style="font-weight:700; color:#ea580c; font-size:1.15rem;">$11.00</span>
          <span class="lottie-tag">Bakery Sandwich</span>
        </div>
      </div>
    </div>

    <!-- Call to Action Banner -->
    <div class="lottie-banner-strip">
      <h2 style="color:#ffffff; font-size:2rem; margin-bottom:12px;">Start Your Morning with Lottie's</h2>
      <p style="color:#fed7aa; max-width:650px; margin:0 auto 20px;">Stop by our counter in Queen City Quarter or call ahead for quick pickup.</p>
      <a href="tel:7047893135" class="lottie-btn-primary">Call (704) 789-3135</a>
    </div>
  </main>

{footer_html()}
"""

with open("lottie-s-cafe/all-day-breakfast-and-sandwiches.html", "w", encoding="utf-8") as f:
    f.write(breakfast_content)
print("Written: lottie-s-cafe/all-day-breakfast-and-sandwiches.html")

# Page 4: espresso-bar-and-specialty-drinks.html
coffee_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Espresso Bar &amp; Specialty Lattes | Lottie's Cafe Uptown Charlotte</title>
  <meta name="description" content="Discover specialty espresso, handcrafted lattes, cold brew, and matcha at Lottie's Cafe in Uptown Charlotte. Lavender honey lattes, brown sugar shaken espresso, and organic teas.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("espresso-bar-and-specialty-drinks.html")}

  <section class="lottie-hero-compact">
    <div class="lottie-container">
      <span class="lottie-badge">Specialty Coffee Program</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Artisanal Espresso &amp; Signature Lattes</h1>
      <p style="font-size:1.1rem; color:#f5f5f4; max-width:720px; margin:0 auto;">Single-origin espresso beans, house-made floral and spice syrups, micro-foamed milks, and refreshing draft cold brews.</p>
    </div>
  </section>

  <main class="lottie-container" style="padding:60px 24px;">
    <div class="lottie-grid-2" style="align-items:center; margin-bottom:60px;">
      <div>
        <span class="lottie-tag">Precision Extraction</span>
        <h2 style="font-size:2.1rem; color:#451a03; margin:15px 0; font-weight:800;">Our Coffee Craft</h2>
        <p style="color:#57534e; line-height:1.7; margin-bottom:15px;">
          Great coffee is a craft of exacting precision. Our baristas dial in the espresso grinders every morning, weighing every dose to the tenth of a gram to highlight subtle tasting notes of chocolate, caramel, and bright berry florals.
        </p>
        <p style="color:#57534e; line-height:1.7; margin-bottom:15px;">
          We simmer our signature syrups from real ingredients—such as Madagascar vanilla beans, fresh lavender buds, and organic brown sugar—never relying on artificial flavorings.
        </p>
        <ul style="color:#44403c; line-height:1.8; padding-left:20px; margin-top:15px;">
          <li>Plant-based milks: Oat milk, Almond milk, and Coconut milk available</li>
          <li>Cold Brew nitro tap pouring velvety chilled caffeine</li>
          <li>Ceremonial grade Uji Matcha &amp; spiced Masala Chai</li>
        </ul>
      </div>
      <div>
        <img src="images/artisan-espresso-latte.jpg" alt="Artisan espresso with latte art at Lottie's Cafe Charlotte" style="width:100%; height:400px; object-fit:cover; border-radius:12px; box-shadow:var(--lottie-shadow-lg);">
      </div>
    </div>

    <!-- Beverage Lineup Grid -->
    <h2 style="font-size:1.9rem; color:#451a03; text-align:center; margin-bottom:35px;">Barista Specialties</h2>

    <div class="lottie-grid-3" style="gap:28px; margin-bottom:60px;">
      <div class="lottie-card">
        <h3 style="color:#451a03; margin-bottom:8px;">Lavender Honey Latte</h3>
        <p style="color:#57534e; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Double espresso shot, organic French lavender syrup, raw wildflower honey, and velvety steamed whole or oat milk.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e7e5e4; padding-top:12px;">
          <span style="font-weight:700; color:#ea580c; font-size:1.15rem;">$6.25</span>
          <span class="lottie-tag">House Signature</span>
        </div>
      </div>

      <div class="lottie-card">
        <h3 style="color:#451a03; margin-bottom:8px;">Brown Sugar Shaken Espresso</h3>
        <p style="color:#57534e; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Espresso shaken vigorously over ice with dark brown sugar, ground Saigon cinnamon, topped with cold creamy oat milk.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e7e5e4; padding-top:12px;">
          <span style="font-weight:700; color:#ea580c; font-size:1.15rem;">$6.00</span>
          <span class="lottie-tag">Iced Feature</span>
        </div>
      </div>

      <div class="lottie-card">
        <h3 style="color:#451a03; margin-bottom:8px;">Vanilla Cardamom Cortado</h3>
        <p style="color:#57534e; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Equal parts double espresso and silky steamed milk infused with crushed green cardamom pods and real vanilla extract.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e7e5e4; padding-top:12px;">
          <span style="font-weight:700; color:#ea580c; font-size:1.15rem;">$5.25</span>
          <span class="lottie-tag">Cortado</span>
        </div>
      </div>

      <div class="lottie-card">
        <h3 style="color:#451a03; margin-bottom:8px;">Nitro Cold Brew Draft</h3>
        <p style="color:#57534e; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Slow-steeped single-origin cold brew charged with nitrogen for a rich, creamy texture and chocolate notes without milk.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e7e5e4; padding-top:12px;">
          <span style="font-weight:700; color:#ea580c; font-size:1.15rem;">$5.50</span>
          <span class="lottie-tag">On Tap</span>
        </div>
      </div>

      <div class="lottie-card">
        <h3 style="color:#451a03; margin-bottom:8px;">Ceremonial Matcha Oat Latte</h3>
        <p style="color:#57534e; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">First-harvest Japanese stone-ground matcha whisked smooth with pure vanilla and lightly sweetened oat milk.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e7e5e4; padding-top:12px;">
          <span style="font-weight:700; color:#ea580c; font-size:1.15rem;">$6.50</span>
          <span class="lottie-tag">Matcha</span>
        </div>
      </div>

      <div class="lottie-card">
        <h3 style="color:#451a03; margin-bottom:8px;">Spiced Masala Chai</h3>
        <p style="color:#57534e; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Slow-brewed black tea with whole ginger, cinnamon, clove, and black pepper, steamed with milk and dusted with nutmeg.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e7e5e4; padding-top:12px;">
          <span style="font-weight:700; color:#ea580c; font-size:1.15rem;">$5.75</span>
          <span class="lottie-tag">House Spiced</span>
        </div>
      </div>
    </div>

    <!-- CTA Box -->
    <div style="background:#ffffff; border:1px solid #e7e5e4; border-radius:12px; padding:32px; box-shadow:var(--lottie-shadow); text-align:center;">
      <h3 style="color:#451a03; font-size:1.4rem; margin-bottom:10px;">Need Your Morning Coffee Fast?</h3>
      <p style="color:#57534e; max-width:600px; margin:0 auto 20px;">Call ahead and our baristas will have your espresso and breakfast sandwich waiting hot on the counter.</p>
      <a href="tel:7047893135" class="lottie-btn-primary">Call (704) 789-3135 to Order</a>
    </div>
  </main>

{footer_html()}
"""

with open("lottie-s-cafe/espresso-bar-and-specialty-drinks.html", "w", encoding="utf-8") as f:
    f.write(coffee_content)
print("Written: lottie-s-cafe/espresso-bar-and-specialty-drinks.html")

