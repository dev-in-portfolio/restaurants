# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\scripts")
from redginger_builder import header_html, footer_html

DIR = r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\red-ginger"

# 3. teppanyaki-hibachi-experience.html
teppanyaki_page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Teppanyaki Hibachi Experience | Red Ginger Charlotte</title>
  <meta name="description" content="Witness live table-side teppanyaki cooking in Uptown Charlotte: flaming onion volcanoes, prime filet mignon, lobster tails, and master chef knife artistry.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
{header_html("teppanyaki-hibachi-experience.html")}

  <section class="redginger-hero" style="padding: 50px 20px;">
    <div class="redginger-hero-inner">
      <span class="redginger-hero-pill">Live Table-Side Artistry</span>
      <h1>The Theatrical Teppanyaki Experience</h1>
      <p>Gather around our sizzling high-carbon steel teppan grills as master chefs transform premium steaks, seafood, and vegetables into an unforgettable dining performance.</p>
    </div>
  </section>

  <main class="redginger-container">
    <div class="redginger-spotlight">
      <div>
        <img src="images/teppanyaki-steak-lobster.jpg" alt="Master chef grilling Filet Mignon and Lobster Tail on teppanyaki grill" class="redginger-card-image" style="height:100%; object-fit:cover;">
      </div>
      <div class="redginger-spotlight-content">
        <span class="redginger-card-badge">Master Craftsmanship</span>
        <h3>Flames, Flavor &amp; Culinary Precision</h3>
        <p>Teppanyaki dining at Red Ginger is an immersive multi-sensory feast. Our seasoned teppanyaki masters combine lightning-fast spatula tricks and towering onion volcanoes with disciplined heat control.</p>
        <p>Every cut of meat and seafood is seared at over 500 degrees with clarified garlic butter, seasoned soy glaze, and cracked peppercorn, locking in moisture and delivering that signature smoky caramelized crust.</p>
        <div style="margin-top:16px;">
          <a href="tel:9808198837" class="redginger-btn-cta">Reserve a Teppan Table: (980) 819-8837</a>
        </div>
      </div>
    </div>

    <div class="redginger-section-title" style="margin-top:60px;">
      <h2>Signature Teppan Cuts &amp; Seafood</h2>
      <p>Only the highest grade meats and sustainably harvested seafood grace our grills.</p>
    </div>

    <div class="redginger-grid-3">
      <div class="redginger-card" style="padding:28px;">
        <span class="redginger-card-badge">Center-Cut Prime</span>
        <h4 style="color:var(--redginger-primary-dark); margin:12px 0; font-size:1.25rem;">USDA Choice Filet Mignon</h4>
        <p style="color:var(--redginger-text-muted); font-size:0.95rem;">Extremely tender and mild, carved into bite-sized medallions table-side, basted with clarified garlic butter and teriyaki reduction.</p>
      </div>

      <div class="redginger-card" style="padding:28px;">
        <span class="redginger-card-badge">Cold-Water Harvest</span>
        <h4 style="color:var(--redginger-primary-dark); margin:12px 0; font-size:1.25rem;">Twin Lobster Tails</h4>
        <p style="color:var(--redginger-text-muted); font-size:0.95rem;">Sweet, firm cold-water lobster tails split and seared in lemon butter right on the hot grill until lightly charred and juicy.</p>
      </div>

      <div class="redginger-card" style="padding:28px;">
        <span class="redginger-card-badge">House Scratch Sauces</span>
        <h4 style="color:var(--redginger-primary-dark); margin:12px 0; font-size:1.25rem;">Signature Ginger &amp; Yum Yum</h4>
        <p style="color:var(--redginger-text-muted); font-size:0.95rem;">Served with our famous house-whipped ginger dipping sauce for steaks and rich creamy pink Yum Yum sauce for rice and shrimp.</p>
      </div>
    </div>

    <!-- The Teppan Course Progression -->
    <div class="redginger-card" style="margin-top:40px; padding:36px; background-color:var(--redginger-surface-card); border: 2px solid var(--redginger-border);">
      <h3 style="color:var(--redginger-primary-dark); margin-bottom:14px;">The Complete Teppanyaki Dinner Progression</h3>
      <p style="color:var(--redginger-text); font-size:0.95rem; margin-bottom:16px;">Every guest seated at our hibachi tables enjoys a generous multi-course journey:</p>
      <ol style="margin-left:20px; color:var(--redginger-text-muted); font-size:0.95rem; line-height:1.8;">
        <li><strong>Course 1: Japanese Onion Soup:</strong> Clear broth simmered with caramelized onions, scallions, and mushrooms.</li>
        <li><strong>Course 2: House Ginger Salad:</strong> Crisp iceberg lettuce, shredded red cabbage, and carrots topped with our famous fresh-grated ginger dressing.</li>
        <li><strong>Course 3: Hibachi Shrimp Appetizer:</strong> Sizzling appetizer shrimp seared table-side with lemon garlic butter.</li>
        <li><strong>Course 4: Seasoned Fried Rice &amp; Noodles:</strong> Wok-style egg fried rice with sweet carrots and stir-fried lo mein noodles.</li>
        <li><strong>Course 5: Main Teppan Entree &amp; Vegetables:</strong> Your choice of steak, chicken, or seafood served with zucchini, onions, and mushrooms.</li>
      </ol>
    </div>

    <div class="redginger-cta-banner" style="margin-top:50px;">
      <h2>Celebrate Your Next Special Occasion</h2>
      <p>Reserve a teppanyaki table for birthdays, anniversaries, or corporate team dinners on South Tryon.</p>
      <div class="redginger-cta-btns">
        <a href="tel:9808198837" class="redginger-btn-hero-primary">Call (980) 819-8837</a>
        <a href="menu.html" class="redginger-btn-hero-secondary">View Hibachi Menu</a>
      </div>
    </div>
  </main>

{footer_html()}'''

# 4. sushi-bar-and-omakase-craft.html
sushi_page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Artisan Sushi Lounge &amp; Raw Bar | Red Ginger Charlotte</title>
  <meta name="description" content="Discover modern Japanese sushi artistry at Red Ginger in Uptown Charlotte: Yellowtail Jalapeno carpaccio, bluefin tuna tartar, and signature specialty rolls.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
{header_html("sushi-bar-and-omakase-craft.html")}

  <section class="redginger-hero" style="padding: 50px 20px;">
    <div class="redginger-hero-inner">
      <span class="redginger-hero-pill">Modern Raw Bar Excellence</span>
      <h1>Artisan Sushi Lounge &amp; Raw Bar Craft</h1>
      <p>Where contemporary Japanese culinary innovation meets timeless sushi tradition in a chic, atmospheric South Tryon lounge setting.</p>
    </div>
  </section>

  <main class="redginger-container">
    <div class="redginger-spotlight">
      <div>
        <img src="images/specialty-sushi-lounge.jpg" alt="Artisan sushi roll presentation with microgreens and unagi reduction" class="redginger-card-image" style="height:100%; object-fit:cover;">
      </div>
      <div class="redginger-spotlight-content">
        <span class="redginger-card-badge">Sushi Master Philosophy</span>
        <h3>Balancing Texture, Temperature &amp; Umami</h3>
        <p>Our sushi chefs craft every roll and sashimi cut as an artistic composition. We source sustainably harvested line-caught Bluefin and Yellowfin Tuna, Scottish Salmon, Japanese Hamachi, and real King Crab.</p>
        <p>Layered with house-infused white truffle oils, citrus yuzu ponzu, microgreens, and torched sweet reductions, each bite provides a symphony of contrasting textures and pure seafood umami.</p>
        <div style="margin-top:16px;">
          <a href="menu.html" class="redginger-btn-cta">Explore Sushi Menu</a>
        </div>
      </div>
    </div>

    <div class="redginger-section-title" style="margin-top:60px;">
      <h2>Signature Sushi Masterpieces</h2>
      <p>Innovative flavor pairings created exclusively for our South Tryon lounge.</p>
    </div>

    <div class="redginger-grid-3">
      <div class="redginger-card">
        <div class="redginger-card-body">
          <span class="redginger-card-badge">House Signature</span>
          <h3>The Red Ginger Roll</h3>
          <p>Spicy tuna and creamy avocado inside, wrapped with fresh Scottish salmon, sliced pickled ginger, sweet unagi reduction, and microgreens.</p>
          <div class="redginger-card-footer">
            <span class="redginger-price">$17.50</span>
          </div>
        </div>
      </div>

      <div class="redginger-card">
        <div class="redginger-card-body">
          <span class="redginger-card-badge">Uptown Landmark</span>
          <h3>The Tryon Street Roll</h3>
          <p>Crispy tempura shrimp and cream cheese rolled with spicy kani salad, topped with sliced ripe avocado, toasted sesame, and kabayaki drizzle.</p>
          <div class="redginger-card-footer">
            <span class="redginger-price">$16.50</span>
          </div>
        </div>
      </div>

      <div class="redginger-card">
        <div class="redginger-card-body">
          <span class="redginger-card-badge">Torched &amp; Smoky</span>
          <h3>Fire Dragon Roll</h3>
          <p>Spicy salmon and crisp cucumber draped with BBQ freshwater eel and avocado, flash-torched table-side with spicy aioli and unagi sauce.</p>
          <div class="redginger-card-footer">
            <span class="redginger-price">$16.99</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Sake & Cocktail Pairing Card -->
    <div class="redginger-card" style="margin-top:40px; padding:36px; background:linear-gradient(135deg, #fff1f2, #fffbf5); border: 2px solid var(--redginger-border);">
      <h3 style="color:var(--redginger-primary-dark); margin-bottom:12px;">Curated Sake &amp; Cocktail Pairings</h3>
      <p style="color:var(--redginger-text); font-size:1rem; line-height:1.7;">Elevate your sushi lounge experience with our premium beverage selection. From dry and crisp Junmai Ginjo sakes that cleanse the palate between rich salmon cuts to our signature <strong>Smoked Ginger Lychee Martini</strong>, our bar team curates pairings that complement each chef creation.</p>
    </div>

    <div class="redginger-cta-banner" style="margin-top:50px;">
      <h2>Join Us at the Sushi Bar Tonight</h2>
      <p>Walk-ins welcome at our sushi lounge or call for table reservations at 401 S Tryon St.</p>
      <div class="redginger-cta-btns">
        <a href="tel:9808198837" class="redginger-btn-hero-primary">Call (980) 819-8837</a>
        <a href="visit.html" class="redginger-btn-hero-secondary">View Lounge Hours</a>
      </div>
    </div>
  </main>

{footer_html()}'''

with open(os.path.join(DIR, "teppanyaki-hibachi-experience.html"), "w", encoding="utf-8") as f:
    f.write(teppanyaki_page)
print("Wrote teppanyaki-hibachi-experience.html")

with open(os.path.join(DIR, "sushi-bar-and-omakase-craft.html"), "w", encoding="utf-8") as f:
    f.write(sushi_page)
print("Wrote sushi-bar-and-omakase-craft.html")
