# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\scripts")
from kosushi_builder import header_html, footer_html

DIR = r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\k-o-sushi"

# 1. index.html
index_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>K.O. Sushi | Uptown Charlotte QC Artisanal Sushi &amp; Poke</title>
  <meta name="description" content="Artisanal sushi, signature maki rolls, custom poke bowls, and hot udon noodle soups in the heart of Uptown Charlotte on S Tryon St. Fast lunch pickup and catering.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
{header_html("index.html")}

  <section class="kosushi-hero">
    <div class="kosushi-hero-inner">
      <span class="kosushi-hero-pill">Uptown South Tryon Sushi Landmark</span>
      <h1>Artisanal Precision Sushi, Poke &amp; Asian Comfort</h1>
      <p>Elevate your Uptown Charlotte dining experience. Fresh sashimi-grade salmon, yellowfin tuna, handcrafted specialty rolls, custom poke bowls, and comforting hot udon noodle broths prepared swiftly for the city's fast-paced professionals.</p>
      <div class="kosushi-hero-actions">
        <a href="menu.html" class="kosushi-btn-hero-primary">Explore Full Menu</a>
        <a href="specialty-maki-and-poke-craft.html" class="kosushi-btn-hero-secondary">Signature Maki &amp; Poke</a>
        <a href="corporate-catering-and-party-trays.html" class="kosushi-btn-hero-secondary">Corporate Catering Trays</a>
      </div>
    </div>
  </section>

  <main class="kosushi-container">
    <div class="kosushi-section-title">
      <h2>Handmade Daily with Sashimi-Grade Precision</h2>
      <p>Every roll, nigiri piece, and poke bowl is sculpted to order using imported Japanese ingredients, seasoned rice, and pristine cuts of fish.</p>
    </div>

    <div class="kosushi-grid-3">
      <div class="kosushi-card">
        <img src="images/specialty-rolls.jpg" alt="Artisanal specialty sushi rolls topped with fresh salmon and tobiko" class="kosushi-card-image">
        <div class="kosushi-card-body">
          <span class="kosushi-card-badge">QC Signature Maki</span>
          <h3>The Charlotte &amp; K.O. Roll</h3>
          <p>Our celebrated house creations: tempura shrimp and spicy tuna topped with seared salmon, ripe avocado, unagi eel glaze, spicy mayo, and golden tobiko caviar.</p>
          <div class="kosushi-card-footer">
            <span class="kosushi-price">$14.50 / Roll</span>
            <a href="specialty-maki-and-poke-craft.html" class="kosushi-btn-cta">View Rolls</a>
          </div>
        </div>
      </div>

      <div class="kosushi-card">
        <img src="images/poke-bowl.jpg" alt="Colorful poke bowl with marinated tuna, salmon, edamame, and avocado" class="kosushi-card-image">
        <div class="kosushi-card-body">
          <span class="kosushi-card-badge">Custom Fresh Bowl</span>
          <h3>Build-Your-Own Poke Bowl</h3>
          <p>Layer seasoned sushi rice or crisp spring greens with cubed ahi tuna, Atlantic salmon, shelled edamame, seaweed salad, cucumber, avocado, and toasted sesame ponzu.</p>
          <div class="kosushi-card-footer">
            <span class="kosushi-price">$13.99 / Bowl</span>
            <a href="menu.html" class="kosushi-btn-cta">Customize</a>
          </div>
        </div>
      </div>

      <div class="kosushi-card">
        <img src="images/udon-bulgogi.jpg" alt="Steaming Udon noodle soup with tempura and Korean bulgogi beef" class="kosushi-card-image">
        <div class="kosushi-card-body">
          <span class="kosushi-card-badge">Warm Comfort Broth</span>
          <h3>Tempura Udon &amp; Beef Bulgogi</h3>
          <p>Thick Japanese sanuki udon noodles in a clear, slow-simmered dashi kombu broth with crisp tempura shrimp, scallions, and comforting sweet-soy marinated Korean bulgogi.</p>
          <div class="kosushi-card-footer">
            <span class="kosushi-price">$13.50</span>
            <a href="hot-udon-and-bulgogi-kitchen.html" class="kosushi-btn-cta">See Hot Dishes</a>
          </div>
        </div>
      </div>
    </div>

    <!-- Spotlight Section -->
    <div class="kosushi-spotlight">
      <div>
        <img src="images/party-platter.jpg" alt="Grand 38-piece K.O. Deluxe Sushi Catering Platter" class="kosushi-card-image" style="height:100%; object-fit:cover;">
      </div>
      <div class="kosushi-spotlight-content">
        <span class="kosushi-card-badge">Uptown Corporate Catering</span>
        <h3>Impress Your Team with 38-Piece K.O. Deluxe Trays</h3>
        <p>Hosting an executive board meeting, client presentation, or office celebration in Uptown? Our 38-piece and 50-piece sushi party platters arrive exquisitely arranged with chef's choice nigiri, sashimi, and signature specialty rolls.</p>
        <p>Includes individual soy dipping cups, real wasabi, pickled sushi ginger, and chopsticks. Delivered directly to your office floor or ready for fast pickup on South Tryon.</p>
        <div style="margin-top:20px;">
          <a href="corporate-catering-and-party-trays.html" class="kosushi-btn-cta">Explore Catering Packages</a>
        </div>
      </div>
    </div>

    <!-- Features -->
    <div class="kosushi-section-title" style="margin-top:60px;">
      <h2>The K.O. Sushi Experience</h2>
      <p>Precision, speed, and uncompromising quality for the Queen City.</p>
    </div>

    <div class="kosushi-grid-3">
      <div class="kosushi-card" style="padding:28px;">
        <h4 style="color:var(--kosushi-primary-dark); margin-bottom:12px; font-size:1.2rem;">Daily Sourced Fresh Fish</h4>
        <p style="color:var(--kosushi-text-muted); font-size:0.95rem;">Our sushi chefs receive pristine fresh Atlantic salmon, yellowfin tuna, hamachi yellowtail, and unagi daily, filleted with artisanal Japanese knives.</p>
      </div>
      <div class="kosushi-card" style="padding:28px;">
        <h4 style="color:var(--kosushi-primary-dark); margin-bottom:12px; font-size:1.2rem;">Express Uptown Lunch Rush</h4>
        <p style="color:var(--kosushi-text-muted); font-size:0.95rem;">We understand corporate schedules. Pre-order by phone for seamless 10-minute counter pickup during the peak 11:30 AM to 1:30 PM lunch hour.</p>
      </div>
      <div class="kosushi-card" style="padding:28px;">
        <h4 style="color:var(--kosushi-primary-dark); margin-bottom:12px; font-size:1.2rem;">Healthy &amp; Dietary Friendly</h4>
        <p style="color:var(--kosushi-text-muted); font-size:0.95rem;">Enjoy gluten-conscious sashimi cuts, low-carb seaweed salad bases, brown rice options, and rich vegetarian maki loaded with avocado and crisp cucumber.</p>
      </div>
    </div>

    <!-- CTA Section -->
    <div class="kosushi-cta-banner" style="margin-top:50px;">
      <h2>Craving Fresh Sushi in Uptown Charlotte?</h2>
      <p>Visit us at 230 S Tryon St, Suite R1 or call ahead for rapid express pickup.</p>
      <div class="kosushi-cta-btns">
        <a href="tel:7043727757" class="kosushi-btn-hero-primary">Call (704) 372-7757</a>
        <a href="visit.html" class="kosushi-btn-hero-secondary">View Hours &amp; Directions</a>
      </div>
    </div>
  </main>

{footer_html()}'''

# 2. menu.html
menu_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Full Sushi &amp; Asian Kitchen Menu | K.O. Sushi Charlotte</title>
  <meta name="description" content="Browse the complete menu of handcrafted specialty maki rolls, nigiri, sashimi, build-your-own poke bowls, and hot udon soups at K.O. Sushi in Uptown Charlotte.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
{header_html("menu.html")}

  <section class="kosushi-hero" style="padding: 50px 20px;">
    <div class="kosushi-hero-inner">
      <span class="kosushi-hero-pill">Handcrafted in Uptown Charlotte</span>
      <h1>Full Sushi &amp; Kitchen Menu</h1>
      <p>Select your favorite category to discover our specialty maki rolls, sashimi-grade nigiri, customizable poke bowls, and warm Asian comfort dishes.</p>
    </div>
  </section>

  <main class="kosushi-container">
    <div class="kosushi-tabs">
      <button class="kosushi-tab-btn active" data-target="tab-specialty">Specialty Maki Rolls</button>
      <button class="kosushi-tab-btn" data-target="tab-classic">Classic Rolls &amp; Nigiri</button>
      <button class="kosushi-tab-btn" data-target="tab-poke">Poke Bowls &amp; Salads</button>
      <button class="kosushi-tab-btn" data-target="tab-hot">Hot Udon &amp; Bulgogi</button>
      <button class="kosushi-tab-btn" data-target="tab-appetizers">Appetizers &amp; Drinks</button>
    </div>

    <!-- Group 1: Specialty Maki -->
    <div class="kosushi-menu-group active" id="tab-specialty">
      <div class="kosushi-section-title">
        <h2>Chef’s Signature Specialty Maki</h2>
        <p>Expertly rolled 8-piece premium rolls featuring multi-layered seafood textures, house sauces, and tobiko.</p>
      </div>

      <div class="kosushi-grid-2">
        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>K.O. Roll (Signature)</h4>
            <span class="kosushi-item-price">$14.99</span>
          </div>
          <p class="kosushi-item-desc">Spicy tuna and crisp cucumber topped with seared Atlantic salmon, spicy mayo, eel glaze, masago, and crunchy tempura flakes.</p>
          <div class="kosushi-item-tags">
            <span class="kosushi-tag kosushi-tag-raw">Raw</span>
            <span class="kosushi-tag kosushi-tag-spicy">Spicy</span>
          </div>
        </div>

        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Charlotte Roll</h4>
            <span class="kosushi-item-price">$14.50</span>
          </div>
          <p class="kosushi-item-desc">Tempura shrimp and avocado wrapped inside, crowned with fresh spicy salmon, sliced jalapenos, and sweet unagi drizzle.</p>
          <div class="kosushi-item-tags">
            <span class="kosushi-tag kosushi-tag-raw">Raw</span>
            <span class="kosushi-tag kosushi-tag-spicy">Mild Kick</span>
          </div>
        </div>

        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Queen City Roll</h4>
            <span class="kosushi-item-price">$15.50</span>
          </div>
          <p class="kosushi-item-desc">Fresh yellowfin tuna, yellowtail, and salmon rolled with avocado and asparagus, topped with red and black tobiko and ponzu sauce.</p>
          <div class="kosushi-item-tags">
            <span class="kosushi-tag kosushi-tag-raw">Raw</span>
          </div>
        </div>

        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Volcano Roll (Baked)</h4>
            <span class="kosushi-item-price">$14.99</span>
          </div>
          <p class="kosushi-item-desc">California roll topped with hot baked spicy scallops, krabmeat, scallions, masago, and rich toasted sesame dynamite sauce.</p>
          <div class="kosushi-item-tags">
            <span class="kosushi-tag kosushi-tag-cooked">Cooked</span>
            <span class="kosushi-tag kosushi-tag-spicy">Warm &amp; Rich</span>
          </div>
        </div>

        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Dragon Roll</h4>
            <span class="kosushi-item-price">$14.25</span>
          </div>
          <p class="kosushi-item-desc">Tempura shrimp and cucumber inside, draped with grilled freshwater eel (unagi), thin avocado slices, and sweet kabayaki sauce.</p>
          <div class="kosushi-item-tags">
            <span class="kosushi-tag kosushi-tag-cooked">Cooked</span>
          </div>
        </div>

        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Rainbow Roll</h4>
            <span class="kosushi-item-price">$14.50</span>
          </div>
          <p class="kosushi-item-desc">Classic kani crab and avocado core draped with five vibrant chef selections of fresh salmon, tuna, white fish, and avocado.</p>
          <div class="kosushi-item-tags">
            <span class="kosushi-tag kosushi-tag-raw">Raw</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Group 2: Classic Rolls & Nigiri -->
    <div class="kosushi-menu-group" id="tab-classic">
      <div class="kosushi-section-title">
        <h2>Classic Rolls &amp; Nigiri / Sashimi (2 pcs)</h2>
        <p>Traditional Japanese maki rolls and hand-sliced sashimi over seasoned sushi rice.</p>
      </div>

      <div class="kosushi-grid-2">
        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Spicy Tuna Crunch Roll</h4>
            <span class="kosushi-item-price">$8.50</span>
          </div>
          <p class="kosushi-item-desc">Minced yellowfin tuna mixed with Sriracha sesame oil, scallions, and toasted tempura crunchies.</p>
          <div class="kosushi-item-tags">
            <span class="kosushi-tag kosushi-tag-raw">Raw</span>
            <span class="kosushi-tag kosushi-tag-spicy">Spicy</span>
          </div>
        </div>

        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Classic California Roll</h4>
            <span class="kosushi-item-price">$7.25</span>
          </div>
          <p class="kosushi-item-desc">Sweet kani krab salad, creamy Hass avocado, and fresh crisp cucumber with toasted sesame seeds.</p>
          <div class="kosushi-item-tags">
            <span class="kosushi-tag kosushi-tag-cooked">Cooked</span>
          </div>
        </div>

        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Salmon Avocado Roll (Sake)</h4>
            <span class="kosushi-item-price">$8.25</span>
          </div>
          <p class="kosushi-item-desc">Fresh Scottish salmon and ripe avocado rolled in seasoned sushi rice and nori.</p>
          <div class="kosushi-item-tags">
            <span class="kosushi-tag kosushi-tag-raw">Raw</span>
          </div>
        </div>

        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Philly Roll</h4>
            <span class="kosushi-item-price">$8.50</span>
          </div>
          <p class="kosushi-item-desc">Smoked salmon, Philadelphia cream cheese, and cucumber.</p>
        </div>

        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Fresh Salmon (Sake) Nigiri / Sashimi</h4>
            <span class="kosushi-item-price">$6.00</span>
          </div>
          <p class="kosushi-item-desc">Two thick cuts of pristine Atlantic salmon over seasoned sushi rice balls or served neat.</p>
          <div class="kosushi-item-tags">
            <span class="kosushi-tag kosushi-tag-raw">Raw</span>
          </div>
        </div>

        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Yellowfin Tuna (Maguro) Nigiri / Sashimi</h4>
            <span class="kosushi-item-price">$6.50</span>
          </div>
          <p class="kosushi-item-desc">Two slices of deep ruby-red sashimi-grade yellowfin tuna.</p>
          <div class="kosushi-item-tags">
            <span class="kosushi-tag kosushi-tag-raw">Raw</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Group 3: Poke Bowls -->
    <div class="kosushi-menu-group" id="tab-poke">
      <div class="kosushi-section-title">
        <h2>Fresh Poke Bowls &amp; QC Salads</h2>
        <p>Healthy, vitamin-packed Hawaiian bowls assembled fresh with your choice of protein and dressings.</p>
      </div>

      <div class="kosushi-grid-2">
        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Signature QC Ahi Tuna Poke Bowl</h4>
            <span class="kosushi-item-price">$14.25</span>
          </div>
          <p class="kosushi-item-desc">Cubed yellowfin tuna marinated in sesame soy, served over sushi rice with edamame, seaweed salad, cucumber, avocado, tobiko, and spicy mayo.</p>
        </div>

        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Atlantic Salmon Poke Bowl</h4>
            <span class="kosushi-item-price">$13.99</span>
          </div>
          <p class="kosushi-item-desc">Fresh diced salmon, mango slices, shelled edamame, sliced radish, scallions, furikake seasoning, and sweet citrus ponzu dressing.</p>
        </div>

        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Tofu &amp; Avocado Green Poke Bowl</h4>
            <span class="kosushi-item-price">$11.99</span>
          </div>
          <p class="kosushi-item-desc">Organic marinated tofu cubes, mixed baby greens, avocado, shredded carrots, pickled ginger, and toasted sesame ginger dressing.</p>
          <div class="kosushi-item-tags">
            <span class="kosushi-tag kosushi-tag-veg">Vegetarian</span>
          </div>
        </div>

        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Japanese Seaweed Salad (Hiyashi Wakame)</h4>
            <span class="kosushi-item-price">$5.99</span>
          </div>
          <p class="kosushi-item-desc">Tender seasoned seaweed tossed in sesame oil, rice vinegar, and toasted white sesame seeds.</p>
          <div class="kosushi-item-tags">
            <span class="kosushi-tag kosushi-tag-veg">Vegetarian</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Group 4: Hot Kitchen -->
    <div class="kosushi-menu-group" id="tab-hot">
      <div class="kosushi-section-title">
        <h2>Hot Japanese Udon &amp; Bulgogi Kitchen</h2>
        <p>Comforting warm dishes prepared fresh for lunch and dinner on South Tryon.</p>
      </div>

      <div class="kosushi-grid-2">
        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Tempura Shrimp Udon Noodle Soup</h4>
            <span class="kosushi-item-price">$13.50</span>
          </div>
          <p class="kosushi-item-desc">Steaming Japanese dashi broth with chewy sanuki udon noodles, scallions, fish cake (narutomaki), and 2 crispy tempura shrimp served on the side.</p>
        </div>

        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Beef Bulgogi Rice Bowl</h4>
            <span class="kosushi-item-price">$14.50</span>
          </div>
          <p class="kosushi-item-desc">Thinly sliced ribeye steak marinated in sweet garlic soy sauce and sesame oil, served over steamed rice with sauteed sweet onions and spicy kimchi.</p>
        </div>

        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Chicken Katsu Bowl</h4>
            <span class="kosushi-item-price">$12.99</span>
          </div>
          <p class="kosushi-item-desc">Panko-crusted crispy chicken cutlet sliced over steamed jasmine rice, drizzled with Japanese katsu sauce and served with shredded cabbage salad.</p>
        </div>

        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Vegetable Udon Noodle Soup</h4>
            <span class="kosushi-item-price">$11.50</span>
          </div>
          <p class="kosushi-item-desc">Clear vegetable kombu broth with udon noodles, shiitake mushrooms, baby bok choy, carrots, and silken tofu.</p>
          <div class="kosushi-item-tags">
            <span class="kosushi-tag kosushi-tag-veg">Vegetarian</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Group 5: Appetizers & Drinks -->
    <div class="kosushi-menu-group" id="tab-appetizers">
      <div class="kosushi-section-title">
        <h2>Appetizers, Soups &amp; Beverages</h2>
        <p>The perfect accompaniments to complete your Uptown lunch or dinner.</p>
      </div>

      <div class="kosushi-grid-2">
        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Pan-Fried Pork Gyoza (6 pcs)</h4>
            <span class="kosushi-item-price">$6.99</span>
          </div>
          <p class="kosushi-item-desc">Japanese dumplings filled with seasoned minced pork and scallions, pan-seared to a golden crisp. Served with gyoza dipping sauce.</p>
        </div>

        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Steamed Shrimp Shumai (6 pcs)</h4>
            <span class="kosushi-item-price">$6.99</span>
          </div>
          <p class="kosushi-item-desc">Delicate open-topped steamed dumplings packed with sweet minced shrimp and water chestnuts.</p>
        </div>

        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Edamame with Sea Salt</h4>
            <span class="kosushi-item-price">$4.99</span>
          </div>
          <p class="kosushi-item-desc">Steamed young soybean pods tossed in coarse sea salt.</p>
          <div class="kosushi-item-tags">
            <span class="kosushi-tag kosushi-tag-veg">Vegetarian</span>
          </div>
        </div>

        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Traditional Miso Soup</h4>
            <span class="kosushi-item-price">$3.25</span>
          </div>
          <p class="kosushi-item-desc">Fermented soybean dashi broth with cubed silken tofu, dried wakame seaweed, and sliced green scallions.</p>
        </div>

        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Japanese Roasted Green Tea (Genmaicha)</h4>
            <span class="kosushi-item-price">$2.99</span>
          </div>
          <p class="kosushi-item-desc">Aromatic brewed green tea blended with roasted brown rice grains.</p>
        </div>

        <div class="kosushi-menu-item">
          <div class="kosushi-item-header">
            <h4>Japanese Ramune Soda (Original / Lychee)</h4>
            <span class="kosushi-item-price">$3.50</span>
          </div>
          <p class="kosushi-item-desc">Traditional marble-sealed Japanese fruit soda.</p>
        </div>
      </div>
    </div>

    <!-- Bottom Order CTA -->
    <div class="kosushi-cta-banner" style="margin-top:50px;">
      <h2>Ordering for Lunch or Dinner?</h2>
      <p>Call our South Tryon counter directly for lightning-fast takeout pickup in 10-15 minutes.</p>
      <div class="kosushi-cta-btns">
        <a href="tel:7043727757" class="kosushi-btn-hero-primary">Call (704) 372-7757</a>
        <a href="corporate-catering-and-party-trays.html" class="kosushi-btn-hero-secondary">View Corporate Trays</a>
      </div>
    </div>
  </main>

{footer_html()}'''

with open(os.path.join(DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_content)
print("Wrote index.html")

with open(os.path.join(DIR, "menu.html"), "w", encoding="utf-8") as f:
    f.write(menu_content)
print("Wrote menu.html")
