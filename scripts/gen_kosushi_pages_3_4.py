# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\scripts")
from kosushi_builder import header_html, footer_html

DIR = r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\k-o-sushi"

# 3. specialty-maki-and-poke-craft.html
maki_page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Specialty Maki &amp; Poke Craft | K.O. Sushi Charlotte</title>
  <meta name="description" content="Explore the artisanal sushi craft behind K.O. Sushi in Uptown Charlotte: sashimi-grade fish, seasoned sushi rice, house dressings, and customizable poke bowls.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
{header_html("specialty-maki-and-poke-craft.html")}

  <section class="kosushi-hero" style="padding: 50px 20px;">
    <div class="kosushi-hero-inner">
      <span class="kosushi-hero-pill">Artisanal Precision</span>
      <h1>The Craft of Specialty Maki &amp; Fresh Poke</h1>
      <p>Mastery of Japanese culinary discipline requires top-grade ingredients, disciplined knife techniques, and carefully balanced seasoning in every grain of rice.</p>
    </div>
  </section>

  <main class="kosushi-container">
    <div class="kosushi-spotlight">
      <div>
        <img src="images/specialty-rolls.jpg" alt="Artisanal rolled specialty maki with fresh salmon and tobiko" class="kosushi-card-image" style="height:100%; object-fit:cover;">
      </div>
      <div class="kosushi-spotlight-content">
        <span class="kosushi-card-badge">The Foundation of Sushi</span>
        <h3>Koshihikari Rice &amp; Red Vinegar Seasoning</h3>
        <p>Great sushi begins with the rice (shari). We use premium Japanese short-grain Koshihikari rice, washed through multiple cycles until the water runs crystal clear, then steamed and seasoned with aged rice vinegar, natural sea salt, and a touch of mirin.</p>
        <p>Maintained at precise body temperature behind our counter, our rice cradles fresh salmon and yellowfin tuna without overwhelming their delicate natural sweetness.</p>
        <div style="margin-top:16px;">
          <a href="menu.html" class="kosushi-btn-cta">See All Maki Rolls</a>
        </div>
      </div>
    </div>

    <div class="kosushi-section-title" style="margin-top:60px;">
      <h2>Pillars of Our Raw Bar</h2>
      <p>We adhere to strict sashimi-grade standards to ensure pure flavor and nutritional integrity.</p>
    </div>

    <div class="kosushi-grid-3">
      <div class="kosushi-card" style="padding:28px;">
        <span class="kosushi-card-badge">Cold Water Sourced</span>
        <h4 style="color:var(--kosushi-primary-dark); margin:12px 0; font-size:1.25rem;">Scottish Atlantic Salmon</h4>
        <p style="color:var(--kosushi-text-muted); font-size:0.95rem;">Rich in healthy omega-3 fatty acids, our salmon arrives whole and is filleted daily to yield buttery, melt-in-your-mouth sashimi and signature nigiri cuts.</p>
      </div>

      <div class="kosushi-card" style="padding:28px;">
        <span class="kosushi-card-badge">Line Caught Quality</span>
        <h4 style="color:var(--kosushi-primary-dark); margin:12px 0; font-size:1.25rem;">Yellowfin Ahi Tuna</h4>
        <p style="color:var(--kosushi-text-muted); font-size:0.95rem;">Deep ruby red and firm in texture, our yellowfin tuna is cut into clean sashimi slices and hand-tossed with toasted sesame oil for our poke bowls.</p>
      </div>

      <div class="kosushi-card" style="padding:28px;">
        <span class="kosushi-card-badge">Scratch Sauces</span>
        <h4 style="color:var(--kosushi-primary-dark); margin:12px 0; font-size:1.25rem;">Artisanal Unagi &amp; Ponzu</h4>
        <p style="color:var(--kosushi-text-muted); font-size:0.95rem;">We simmer our unagi eel glaze with reduced mirin, soy, and sake, while our citrus ponzu is infused with fresh yuzu and grated Japanese ginger.</p>
      </div>
    </div>

    <!-- Poke Bowl Breakdown -->
    <div class="kosushi-section-title" style="margin-top:60px;">
      <h2>How We Build Your Poke Bowl</h2>
      <p>A balanced, energizing lunch crafted to your exact dietary goals in four simple steps.</p>
    </div>

    <div class="kosushi-grid-2">
      <div class="kosushi-card" style="padding:32px;">
        <h3 style="color:var(--kosushi-primary-dark); margin-bottom:12px; font-size:1.35rem;">1. Base &amp; Premium Proteins</h3>
        <p style="color:var(--kosushi-text-muted); font-size:0.95rem; margin-bottom:12px;">Choose between warm seasoned sushi rice, nutty organic brown rice, or crisp organic spring mix. Then select generous scoops of diced Ahi Tuna, Scottish Salmon, Cooked Shrimp, or Marinated Organic Tofu.</p>
        <p style="color:var(--kosushi-text-muted); font-size:0.95rem;">Every protein scoop is cubed fresh upon ordering to preserve cellular texture and moisture.</p>
      </div>

      <div class="kosushi-card" style="padding:32px;">
        <h3 style="color:var(--kosushi-primary-dark); margin-bottom:12px; font-size:1.35rem;">2. Fresh Mix-Ins &amp; House Dressings</h3>
        <p style="color:var(--kosushi-text-muted); font-size:0.95rem; margin-bottom:12px;">Layer on nutrient-dense mix-ins: steamed edamame, seasoned wakame seaweed salad, Hass avocado, crisp cucumbers, sweet mango, and pickled red ginger.</p>
        <p style="color:var(--kosushi-text-muted); font-size:0.95rem;">Finish with your choice of dressing: Spicy Sriracha Mayo, Toasted Sesame Soy, Sweet Citrus Ponzu, or Ginger Wasabi Vinaigrette.</p>
      </div>
    </div>

    <div class="kosushi-cta-banner" style="margin-top:50px;">
      <h2>Experience Fresh Poke &amp; Maki Today</h2>
      <p>Order takeout for quick pickup at 230 S Tryon St in Uptown Charlotte.</p>
      <div class="kosushi-cta-btns">
        <a href="tel:7043727757" class="kosushi-btn-hero-primary">Call (704) 372-7757</a>
        <a href="menu.html" class="kosushi-btn-hero-secondary">View Menu &amp; Pricing</a>
      </div>
    </div>
  </main>

{footer_html()}'''

# 4. hot-udon-and-bulgogi-kitchen.html
udon_page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hot Udon Noodle Soups &amp; Beef Bulgogi | K.O. Sushi Charlotte</title>
  <meta name="description" content="Warm up with Japanese Tempura Udon noodle soups and savory-sweet Korean Beef Bulgogi rice bowls at K.O. Sushi on South Tryon in Uptown Charlotte.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
{header_html("hot-udon-and-bulgogi-kitchen.html")}

  <section class="kosushi-hero" style="padding: 50px 20px;">
    <div class="kosushi-hero-inner">
      <span class="kosushi-hero-pill">Hot Asian Kitchen Comforts</span>
      <h1>Steaming Dashi Udon &amp; Sizzling Beef Bulgogi</h1>
      <p>When you crave warming comfort in Uptown Charlotte, our hot kitchen serves slow-simmered Japanese noodle broths and authentic Korean marinated meats.</p>
    </div>
  </section>

  <main class="kosushi-container">
    <div class="kosushi-spotlight">
      <div>
        <img src="images/udon-bulgogi.jpg" alt="Steaming Udon noodle bowl with tempura shrimp and green scallions" class="kosushi-card-image" style="height:100%; object-fit:cover;">
      </div>
      <div class="kosushi-spotlight-content">
        <span class="kosushi-card-badge">Traditional Dashi Broth</span>
        <h3>The Sanuki Udon Tradition</h3>
        <p>Our udon bowls feature thick, springy Sanuki-style wheat noodles simmered in a clear, golden dashi broth steeped with wild kombu kelp, smoked bonito flakes, and light Japanese soy.</p>
        <p>Served piping hot with sliced narutomaki fish cakes, green scallions, and accompanied by crispy, golden tempura jumbo shrimp prepared fresh upon order.</p>
        <div style="margin-top:16px;">
          <a href="tel:7043727757" class="kosushi-btn-cta">Call for Hot Pickup: (704) 372-7757</a>
        </div>
      </div>
    </div>

    <div class="kosushi-section-title" style="margin-top:60px;">
      <h2>Hot Kitchen Specialties</h2>
      <p>Satisfying lunch and dinner bowls that fuel your workday.</p>
    </div>

    <div class="kosushi-grid-3">
      <div class="kosushi-card">
        <div class="ksasian-card-body kosushi-card-body">
          <span class="kosushi-card-badge">Korean Classic</span>
          <h3>Korean Beef Bulgogi Bowl</h3>
          <p>Thinly shaved ribeye steak marinated for 24 hours in grated Asian pear, garlic, ginger, sesame oil, and sweet soy sauce. Wok-seared with sweet yellow onions over steamed rice with spicy aged kimchi.</p>
          <div class="kosushi-card-footer">
            <span class="kosushi-price">$14.50</span>
          </div>
        </div>
      </div>

      <div class="kosushi-card">
        <div class="ksasian-card-body kosushi-card-body">
          <span class="kosushi-card-badge">Crisp &amp; Savory</span>
          <h3>Chicken Katsu Donburi</h3>
          <p>Tender chicken breast coated in Japanese panko breadcrumbs, fried until golden and crisp, sliced over warm jasmine rice with sweet and tangy fruit-vegetable katsu sauce.</p>
          <div class="kosushi-card-footer">
            <span class="kosushi-price">$12.99</span>
          </div>
        </div>
      </div>

      <div class="kosushi-card">
        <div class="ksasian-card-body kosushi-card-body">
          <span class="kosushi-card-badge">Plant-Based Warmth</span>
          <h3>Shiitake &amp; Tofu Udon</h3>
          <p>Chewy udon noodles in rich 100% vegetarian kombu mushroom broth with braised shiitake mushrooms, baby bok choy, carrots, and fried bean curd (aburaage).</p>
          <div class="kosushi-card-footer">
            <span class="kosushi-price">$11.50</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Hot Lunch Fast Combo Card -->
    <div class="kosushi-card" style="margin-top:40px; padding:36px; background:linear-gradient(135deg, #f0fdf4, #f0f9ff); border: 2px solid var(--kosushi-border);">
      <h3 style="color:var(--kosushi-primary-dark); margin-bottom:12px;">The Uptown Business Lunch Express Combo</h3>
      <p style="color:var(--kosushi-text); font-size:1rem; line-height:1.7;">Pressed for time between meetings? Our hot kitchen prepares Bulgogi Rice Bowls and Tempura Udon in under 10 minutes. Pair any hot entree with a 4-piece California roll or cup of Miso Soup for the ultimate energizing Uptown lunch.</p>
    </div>

    <div class="kosushi-cta-banner" style="margin-top:50px;">
      <h2>Ready for Warm Comfort?</h2>
      <p>Order takeout for pickup at 230 S Tryon St, Suite R1 in Charlotte.</p>
      <div class="kosushi-cta-btns">
        <a href="tel:7043727757" class="kosushi-btn-hero-primary">Call (704) 372-7757</a>
        <a href="menu.html" class="kosushi-btn-hero-secondary">Explore Full Menu</a>
      </div>
    </div>
  </main>

{footer_html()}'''

with open(os.path.join(DIR, "specialty-maki-and-poke-craft.html"), "w", encoding="utf-8") as f:
    f.write(maki_page)
print("Wrote specialty-maki-and-poke-craft.html")

with open(os.path.join(DIR, "hot-udon-and-bulgogi-kitchen.html"), "w", encoding="utf-8") as f:
    f.write(udon_page)
print("Wrote hot-udon-and-bulgogi-kitchen.html")
