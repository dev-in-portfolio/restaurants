# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("scripts")
from gw_builder import header_html, footer_html

# Page 3: chef-specialties-and-combos.html
combos_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chef Specialties &amp; Combos | Great Wok Chinese Charlotte NC</title>
  <meta name="description" content="Discover sizzling Chinese chef specialties and value combination platters at Great Wok in Uptown Charlotte: General Tso's, Sesame Chicken, Pepper Steak, and combos.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("chef-specialties-and-combos.html")}

  <section class="gw-hero-compact">
    <div class="gw-container">
      <span class="gw-badge">Signature Wok Creations</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Chef Specialties &amp; Combination Platters</h1>
      <p style="font-size:1.1rem; color:#cbd5e1; max-width:720px; margin:0 auto;">Crispy glazes, savory gravies, tender meats, and complete combo meals with pork fried rice and egg rolls.</p>
    </div>
  </section>

  <main class="gw-container" style="padding:60px 24px;">
    <!-- General Tso Feature -->
    <div class="gw-grid-2" style="align-items:center; margin-bottom:60px;">
      <div>
        <span class="gw-tag">The House Standard</span>
        <h2 style="font-size:2.1rem; color:#0f172a; margin:15px 0; font-weight:800;">Our Signature General Tso's Chicken</h2>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:15px;">
          What makes Great Wok's General Tso's chicken an Uptown Charlotte favorite is the balance of texture and heat. We lightly batter tender chicken pieces and double-fry them until the exterior achieves a shatteringly crisp crust.
        </p>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:15px;">
          The chicken is instantly tossed in a flaming wok with dried whole red chilis, minced ginger, crushed garlic, and our savory-sweet tang sauce. Served with fresh steamed broccoli florets and white or fried rice.
        </p>
        <div style="background:#fef2f2; border-left:4px solid #dc2626; padding:16px; border-radius:6px; margin-top:20px;">
          <h4 style="color:#991b1b; margin-bottom:4px;">Combination Value Available All Day</h4>
          <p style="color:#7f1d1d; font-size:0.95rem; margin:0;">Upgrade any specialty to a full combination platter for just a few dollars more, complete with our signature roast pork fried rice and an egg roll.</p>
        </div>
      </div>
      <div>
        <img src="images/general-tsos-chicken.jpg" alt="Crispy glazed General Tso's Chicken with broccoli at Great Wok" style="width:100%; height:400px; object-fit:cover; border-radius:12px; box-shadow:var(--gw-shadow-lg);">
      </div>
    </div>

    <!-- Specialties & Combos Grid -->
    <h2 style="font-size:1.9rem; color:#0f172a; text-align:center; margin-bottom:35px;">Popular Specialties &amp; Combos</h2>
    
    <div class="gw-grid-3" style="gap:28px; margin-bottom:60px;">
      <div class="gw-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">General Tso's Chicken Combo</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Crispy dark meat chicken in spicy sweet garlic sauce, served with a mound of roast pork fried rice and a crispy pork egg roll.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#dc2626; font-size:1.15rem;">$11.95</span>
          <span class="gw-tag">Combo Platter</span>
        </div>
      </div>

      <div class="gw-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Crispy Sesame Chicken Combo</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Tender crispy chicken glazed in sweet honey sesame sauce with toasted sesame seeds, served with pork fried rice and an egg roll.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#dc2626; font-size:1.15rem;">$11.95</span>
          <span class="gw-tag">Sweet &amp; Crisp</span>
        </div>
      </div>

      <div class="gw-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Honey Walnut Jumbo Shrimp</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Jumbo battered shrimp tossed in sweet cream glaze with candied walnuts and steamed broccoli. Served with white jasmine rice.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#dc2626; font-size:1.15rem;">$15.50</span>
          <span class="gw-tag">Chef Feature</span>
        </div>
      </div>

      <div class="gw-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Beef with Broccoli Combo</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Sliced flank steak sauteed with fresh broccoli florets and carrots in rich brown soy garlic sauce with pork fried rice and egg roll.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#dc2626; font-size:1.15rem;">$12.50</span>
          <span class="gw-tag">Beef Combo</span>
        </div>
      </div>

      <div class="gw-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Crispy Orange Flank Steak</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Crispy beef strips glazed in a zesty, aromatic orange peel chili reduction with red peppers and scallions. Served with white rice.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#dc2626; font-size:1.15rem;">$15.50</span>
          <span class="gw-tag">Spicy Orange</span>
        </div>
      </div>

      <div class="gw-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Shrimp with Lobster Sauce Combo</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Plump shrimp simmered in traditional Cantonese minced pork egg sauce with peas and water chestnuts, pork fried rice, and egg roll.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#dc2626; font-size:1.15rem;">$12.95</span>
          <span class="gw-tag">Seafood Combo</span>
        </div>
      </div>
    </div>

    <!-- Call to Action Banner -->
    <div class="gw-banner-strip">
      <h2 style="color:#ffffff; font-size:2rem; margin-bottom:12px;">Order Hot &amp; Fresh Chinese Takeout</h2>
      <p style="color:#cbd5e1; max-width:650px; margin:0 auto 20px;">Ready in minutes at our Gateway Village location at 718 W Trade Street.</p>
      <a href="tel:7043330080" class="gw-btn-primary">Call (704) 333-0080</a>
    </div>
  </main>

{footer_html()}
"""

with open("great-wok/chef-specialties-and-combos.html", "w", encoding="utf-8") as f:
    f.write(combos_content)
print("Written: great-wok/chef-specialties-and-combos.html")

# Page 4: wok-noodles-and-fried-rice.html
noodles_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lo Mein &amp; Fried Rice | Great Wok Chinese Charlotte NC</title>
  <meta name="description" content="Enjoy wok-tossed Lo Mein, Singapore Mei Fun, Chow Fun, and fried rice at Great Wok Charlotte. Searing high heat, fresh vegetables, and rich savory sauces.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("wok-noodles-and-fried-rice.html")}

  <section class="gw-hero-compact">
    <div class="gw-container">
      <span class="gw-badge">High Heat Wok Noodles</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Lo Mein, Mei Fun &amp; Sizzling Rice</h1>
      <p style="font-size:1.1rem; color:#cbd5e1; max-width:720px; margin:0 auto;">Soft egg noodles, thin curry vermicelli, flat rice chow fun, and wok-charred jasmine fried rice cooked to order.</p>
    </div>
  </section>

  <main class="gw-container" style="padding:60px 24px;">
    <div class="gw-grid-2" style="align-items:center; margin-bottom:60px;">
      <div>
        <span class="gw-tag">High Heat Precision</span>
        <h2 style="font-size:2.1rem; color:#0f172a; margin:15px 0; font-weight:800;">The Science of Wok-Charred Noodles</h2>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:15px;">
          True noodle stir frying requires immense burner heat and swift hand coordination. At Great Wok, our seasoned carbon steel woks caramelize garlic, soy, and sesame oil in seconds, coating each strand of noodle without making it greasy or soggy.
        </p>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:15px;">
          From our classic soft egg Lo Mein to the aromatic yellow curry turmeric kick of Singapore Mei Fun, every order is packed with generous portions of meats and crisp shredded vegetables.
        </p>
        <ul style="color:#334155; line-height:1.8; padding-left:20px; margin-top:15px;">
          <li>Choice of proteins: Roast Pork, Chicken, Beef, Jumbo Shrimp, or House Special combo</li>
          <li>Vegetarian options with fried bean curd and seasonal greens</li>
          <li>Singapore Mei Fun cooked with pure Madras yellow curry</li>
        </ul>
      </div>
      <div>
        <img src="images/house-special-lo-mein.jpg" alt="House Special Lo Mein wok tossed noodles at Great Wok" style="width:100%; height:400px; object-fit:cover; border-radius:12px; box-shadow:var(--gw-shadow-lg);">
      </div>
    </div>

    <!-- Noodles & Rice Grid -->
    <h2 style="font-size:1.9rem; color:#0f172a; text-align:center; margin-bottom:35px;">Noodle &amp; Rice Highlights</h2>

    <div class="gw-grid-3" style="gap:28px; margin-bottom:60px;">
      <div class="gw-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">House Special Lo Mein</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Egg noodles wok-stirred with shrimp, chicken, roast pork, shredded Napa cabbage, carrots, and sweet onions in savory garlic soy.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#dc2626; font-size:1.15rem;">$12.95</span>
          <span class="gw-tag">House Benchmark</span>
        </div>
      </div>

      <div class="gw-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Singapore Mei Fun (Curry)</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Thin rice vermicelli noodles seared with yellow curry powder, farm egg, shrimp, roast pork, red bell peppers, and fresh bean sprouts.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#dc2626; font-size:1.15rem;">$13.50</span>
          <span class="gw-tag">Curry Noodles</span>
        </div>
      </div>

      <div class="gw-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Beef Chow Fun (Flat Noodles)</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Wide flat rice noodles wok-charred with tender flank steak slices, bean sprouts, and scallions in dark savory soy sauce.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#dc2626; font-size:1.15rem;">$13.95</span>
          <span class="gw-tag">Cantonese Classic</span>
        </div>
      </div>

      <div class="gw-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">House Special Fried Rice</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Jasmine rice stir-fried over roaring flame with shrimp, chicken, roast pork, farm egg, sweet green peas, and diced carrots.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#dc2626; font-size:1.15rem;">$11.95</span>
          <span class="gw-tag">Deluxe Rice</span>
        </div>
      </div>

      <div class="gw-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Roast Pork Fried Rice</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Tender diced sweet Chinese BBQ pork, farm egg, onions, and scallions wok-tossed with jasmine rice and rich soy sauce.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#dc2626; font-size:1.15rem;">$10.50</span>
          <span class="gw-tag">Classic Takeout</span>
        </div>
      </div>

      <div class="gw-card">
        <h3 style="color:#0f172a; margin-bottom:8px;">Vegetable Lo Mein</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Egg noodles tossed with fresh broccoli, mushrooms, baby corn, snow peas, carrots, and cabbage in light sesame garlic sauce.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#dc2626; font-size:1.15rem;">$10.95</span>
          <span class="gw-tag">Vegetarian</span>
        </div>
      </div>
    </div>

    <!-- Takeout Box -->
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:32px; box-shadow:var(--gw-shadow); text-align:center;">
      <h3 style="color:#0f172a; font-size:1.4rem; margin-bottom:10px;">Hot Noodle Takeout Ready in 15 Minutes</h3>
      <p style="color:#4b5563; max-width:600px; margin:0 auto 20px;">Call ahead and your food will be packed steaming hot when you arrive at our West Trade Street counter.</p>
      <a href="tel:7043330080" class="gw-btn-primary">Call (704) 333-0080</a>
    </div>
  </main>

{footer_html()}
"""

with open("great-wok/wok-noodles-and-fried-rice.html", "w", encoding="utf-8") as f:
    f.write(noodles_content)
print("Written: great-wok/wok-noodles-and-fried-rice.html")

