# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("scripts")
from cm_builder import header_html, footer_html

# Page 3: gourmet-sliders-and-wings.html
sliders_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gourmet Sliders &amp; Jumbo Wings | Cheers Mate Bar &amp; Lounge Charlotte</title>
  <meta name="description" content="Indulge in artisanal smash sliders and crispy jumbo wings at Cheers Mate Bar &amp; Lounge Charlotte: 2AM sliders, hot honey chicken, Impossible vegan, and dry rubs.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("gourmet-sliders-and-wings.html")}

  <section class="cm-hero-compact">
    <div class="cm-container">
      <span class="cm-badge">Craft Pub Fare</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Gourmet Smash Sliders &amp; Jumbo Wings</h1>
      <p style="font-size:1.1rem; color:#cbd5e1; max-width:720px; margin:0 auto;">Handcrafted mini burgers pressed fresh on the flat-top, paired with jumbo double-fried chicken wings tossed in signature sauces.</p>
    </div>
  </section>

  <main class="cm-container" style="padding:60px 24px;">
    <!-- Deep Dive: The 2AM Slider Philosophy -->
    <div class="cm-grid-2" style="align-items:center; margin-bottom:60px;">
      <div>
        <span class="cm-tag">The Art of the Smash</span>
        <h2 style="font-size:2.1rem; color:#0f172a; margin:15px 0; font-weight:800;">Why Our 2AM Sliders Stand Apart</h2>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:15px;">
          At Cheers Mate Bar &amp; Lounge, we believe sliders should never be treated as an afterthought. We take fresh custom-ground Angus beef, press each patty ultra-thin against a searing hot flat-top grill to develop crispy caramelized lacy edges, and lock in the flavorful juices.
        </p>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:15px;">
          Topped with melting American cheese, sweet griddled onions, crunch dill pickles, and our proprietary house sauce, each bite on a warm butter-toasted brioche bun is pure comfort food satisfaction.
        </p>
        <div style="background:#fef3c7; border-left:4px solid #f59e0b; padding:16px; border-radius:6px; margin-top:20px;">
          <h4 style="color:#92400e; margin-bottom:4px;">Late-Night Kitchen Commitment</h4>
          <p style="color:#78350f; font-size:0.95rem; margin:0;">Our kitchen stays firing until 1:30 AM every night of the week, making Cheers Mate the premier spot in Uptown Charlotte for high-quality late-night cravings.</p>
        </div>
      </div>
      <div>
        <img src="images/gourmet-sliders.jpg" alt="Flight of gourmet smash sliders at Cheers Mate Charlotte" style="width:100%; height:400px; object-fit:cover; border-radius:12px; box-shadow:var(--cm-shadow-lg);">
      </div>
    </div>

    <!-- Sliders & Wings Grid -->
    <h2 style="font-size:1.9rem; color:#0f172a; text-align:center; margin-bottom:35px;">The Full Flight &amp; Wing Lineup</h2>
    
    <div class="cm-grid-3" style="gap:28px; margin-bottom:60px;">
      <div class="cm-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">The 2AM Classic Smash (3pc)</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Angus beef smash patties, American cheese, caramelized onions, dill pickles, and house secret sauce on toasted brioche buns.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$14.50</span>
          <span class="cm-tag">Bestseller</span>
        </div>
      </div>

      <div class="cm-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Hot Honey Crispy Chicken (3pc)</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Buttermilk marinated fried chicken tenders tossed in spicy clover hot honey glaze with crunchy cabbage slaw and sweet pickles.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$14.50</span>
          <span class="cm-tag">Spicy Crunch</span>
        </div>
      </div>

      <div class="cm-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Plant-Based Impossible Sliders (3pc)</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">100% plant-based Impossible meat griddled with vegan cheddar, lettuce, tomato, red onion, and chipotle garlic aioli on dairy-free buns.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$15.50</span>
          <span class="cm-tag">Vegan Friendly</span>
        </div>
      </div>

      <div class="cm-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Lemon Pepper Wings (10pc)</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Crispy bone-in jumbo wings dusted in bright lemon zest and coarse black pepper, finished with garlic clarified butter drizzle.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$15.95</span>
          <span class="cm-tag">Dry Rub</span>
        </div>
      </div>

      <div class="cm-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Sweet Thai Chili Wings (10pc)</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Jumbo wings tossed in sticky sweet Thai red chili and ginger glaze, sprinkled with toasted sesame seeds and fresh scallions.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$15.95</span>
          <span class="cm-tag">Sweet &amp; Tangy</span>
        </div>
      </div>

      <div class="cm-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Smoked Bacon BBQ Sliders (3pc)</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Angus beef smash patties topped with smoked applewood bacon, sharp cheddar cheese, crispy fried onion ring strings, and bourbon barbecue.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$15.00</span>
          <span class="cm-tag">Bacon Cheddar</span>
        </div>
      </div>
    </div>

    <!-- Call to Action Banner -->
    <div class="cm-banner-strip">
      <h2 style="color:#ffffff; font-size:2rem; margin-bottom:12px;">Grab Your Flight of Sliders &amp; Wings</h2>
      <p style="color:#cbd5e1; max-width:650px; margin:0 auto 20px;">Stop by our bar on North College Street or call ahead for swift takeout pickup.</p>
      <a href="tel:9802999000" class="cm-btn-primary">Call (980) 299-9000</a>
    </div>
  </main>

{footer_html()}
"""

with open("cheers-mate-bar-and-lounge/gourmet-sliders-and-wings.html", "w", encoding="utf-8") as f:
    f.write(sliders_content)
print("Written: cheers-mate-bar-and-lounge/gourmet-sliders-and-wings.html")

# Page 4: weekend-brunch-and-mimosas.html
brunch_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Weekend Brunch &amp; Mimosas | Cheers Mate Bar &amp; Lounge Charlotte</title>
  <meta name="description" content="Experience Uptown Charlotte's best weekend brunch at Cheers Mate Bar &amp; Lounge: Saturday &amp; Sunday 11am-4pm with chicken &amp; waffles, mimosa carafes, and sports watch parties.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("weekend-brunch-and-mimosas.html")}

  <section class="cm-hero-compact">
    <div class="cm-container">
      <span class="cm-badge">Every Saturday &amp; Sunday 11 AM - 4 PM</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Weekend Brunch &amp; Mimosa Experience</h1>
      <p style="font-size:1.1rem; color:#cbd5e1; max-width:720px; margin:0 auto;">Uptown Charlotte's premier weekend daytime party featuring indulgent chicken &amp; waffles, breakfast sliders, and sparkling carafes.</p>
    </div>
  </section>

  <main class="cm-container" style="padding:60px 24px;">
    <div class="cm-grid-2" style="align-items:center; margin-bottom:60px;">
      <div>
        <span class="cm-tag">The Weekend Destination</span>
        <h2 style="font-size:2.1rem; color:#0f172a; margin:15px 0; font-weight:800;">Brunch Meets Game Day Energy</h2>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:15px;">
          Saturdays and Sundays in Uptown Charlotte belong to brunch. At Cheers Mate Bar &amp; Lounge, we blend a vibrant social soundtrack, live sports broadcasts on our video wall, and a decadent brunch menu crafted to fuel your weekend.
        </p>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:15px;">
          From golden Belgian pearl sugar waffles topped with crispy fried chicken and bourbon maple syrup to breakfast taco flights and loaded brunch tots, our kitchen sets the standard for daytime flavor.
        </p>
        <ul style="color:#334155; line-height:1.8; padding-left:20px; margin-top:15px;">
          <li>Weekend hours: Saturday &amp; Sunday, 11:00 AM – 4:00 PM</li>
          <li>Mimosa carafes &amp; specialty bloody mary towers</li>
          <li>Live Premier League, College Football, and NFL broadcasts</li>
          <li>Large party and birthday group table reservations welcome</li>
        </ul>
      </div>
      <div>
        <img src="images/weekend-brunch.jpg" alt="Weekend brunch spread with chicken, waffles, and drinks at Cheers Mate" style="width:100%; height:400px; object-fit:cover; border-radius:12px; box-shadow:var(--cm-shadow-lg);">
      </div>
    </div>

    <!-- Brunch Menu Highlights Grid -->
    <h2 style="font-size:1.9rem; color:#0f172a; text-align:center; margin-bottom:35px;">Brunch Specials</h2>

    <div class="cm-grid-3" style="gap:28px; margin-bottom:60px;">
      <div class="cm-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Lounge Chicken &amp; Waffles</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Belgian sugar waffle, crispy buttermilk fried chicken breast tenders, cayenne hot honey drizzle, whipped honey butter, and warm bourbon maple syrup.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$16.50</span>
          <span class="cm-tag">Brunch Crown</span>
        </div>
      </div>

      <div class="cm-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Morning Sunrise Sliders (3pc)</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Fluffy scrambled eggs, thick applewood smoked bacon, melted cheddar cheese, and maple aioli on three toasted brioche slider buns with crispy tots.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$14.50</span>
          <span class="cm-tag">Handheld Brunch</span>
        </div>
      </div>

      <div class="cm-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Loaded Hangover Tots Platter</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Golden crispy tater tots smothered in melted cheese sauce, crumbled sausage, bacon bits, jalapeños, two sunny-side eggs, and spicy sriracha crema.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$13.95</span>
          <span class="cm-tag">Sharing Platter</span>
        </div>
      </div>

      <div class="cm-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Brunch Breakfast Tacos (3pc)</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Warm flour tortillas filled with chorizo sausage, scrambled eggs, shredded monterey jack cheese, fresh pico de gallo, and cilantro lime crema.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$13.50</span>
          <span class="cm-tag">Taco Flight</span>
        </div>
      </div>

      <div class="cm-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Sparkling Mimosa Carafe</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Full bottle of chilled sparkling wine served with your choice of classic fresh orange juice, peach puree, or strawberry lemonade.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$25.00</span>
          <span class="cm-tag">Table Carafe</span>
        </div>
      </div>

      <div class="cm-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Varsity Loaded Bloody Mary</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">House spiced tomato horseradish mix, premium vodka, rimmed with Old Bay and garnished with a crispy chicken slider, bacon strip, and olives.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$15.00</span>
          <span class="cm-tag">Signature Drink</span>
        </div>
      </div>
    </div>

    <!-- Booking Info Box -->
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:32px; box-shadow:var(--cm-shadow); text-align:center;">
      <h3 style="color:#0f172a; font-size:1.4rem; margin-bottom:10px;">Reserve a Brunch Table for Your Group</h3>
      <p style="color:#4b5563; max-width:600px; margin:0 auto 20px;">Brunch tables fill fast during game weekends. Call our host stand to reserve seating for groups of 4 or more.</p>
      <a href="tel:9802999000" class="cm-btn-primary">Call (980) 299-9000</a>
    </div>
  </main>

{footer_html()}
"""

with open("cheers-mate-bar-and-lounge/weekend-brunch-and-mimosas.html", "w", encoding="utf-8") as f:
    f.write(brunch_content)
print("Written: cheers-mate-bar-and-lounge/weekend-brunch-and-mimosas.html")

