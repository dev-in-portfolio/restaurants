# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\scripts")
from room112_builder import header_html, footer_html

DIR = r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\room-112"

# 3. signature-rolls-and-sashimi-lounge.html
sushi_lounge_page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Signature Rolls &amp; Boutique Sushi Lounge | Room 112 Charlotte</title>
  <meta name="description" content="Discover boutique sushi artistry at Room 112 in Uptown Charlotte: Cherry Blossom roll, Upper Manhattan roll, 112 Deluxe Samplers, and pristine sashimi.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
{header_html("signature-rolls-and-sashimi-lounge.html")}

  <section class="room112-hero" style="padding: 50px 20px;">
    <div class="room112-hero-inner">
      <span class="room112-hero-pill">Artistic Raw Bar Excellence</span>
      <h1>Signature Maki Rolls &amp; Sushi Lounge Craft</h1>
      <p>Where modern aesthetics and culinary discipline create stunning sushi roll presentations in the heart of Uptown Charlotte.</p>
    </div>
  </section>

  <main class="room112-container">
    <div class="room112-spotlight">
      <div>
        <img src="images/cherry-blossom-roll.jpg" alt="The iconic Cherry Blossom roll with sculpted salmon rosettes" class="room112-card-image" style="height:100%; object-fit:cover;">
      </div>
      <div class="room112-spotlight-content">
        <span class="room112-card-badge">The Room 112 Icon</span>
        <h3>The Craft of the Cherry Blossom Roll</h3>
        <p>A feast for both the eyes and the palate, our signature Cherry Blossom Roll starts with a core of hand-minced spicy yellowfin tuna, blue crab salad, and buttery avocado rolled in seasoned rice.</p>
        <p>Our sushi masters sculpt delicate rose petals from sashimi-cut Scottish salmon across the top, finished with a brush of citrus yuzu glaze, unagi reduction, and micro cilantro leaves. A beloved Charlotte favorite for over a decade.</p>
        <div style="margin-top:16px;">
          <a href="menu.html" class="room112-btn-cta">View All Rolls</a>
        </div>
      </div>
    </div>

    <div class="room112-section-title" style="margin-top:60px;">
      <h2>Signature Specialty Maki Showcase</h2>
      <p>Hand-rolled to order with sashimi-grade fish and premium soy wraps.</p>
    </div>

    <div class="room112-grid-3">
      <div class="room112-card">
        <div class="room112-card-body">
          <span class="room112-card-badge">Boutique Selection</span>
          <h3>Upper Manhattan Roll</h3>
          <p>Crispy soft-shell crab, spicy tuna, and asparagus inside, draped with seared Japanese yellowtail, black tobiko caviar, and white truffle ponzu.</p>
          <div class="room112-card-footer">
            <span class="room112-price">$16.99</span>
          </div>
        </div>
      </div>

      <div class="room112-card">
        <div class="room112-card-body">
          <span class="room112-card-badge">Soy Paper Roll</span>
          <h3>Pink Floyd Roll</h3>
          <p>Smoked salmon, Philadelphia cream cheese, and sliced jalapeno rolled in pink soy paper, crowned with spicy tuna tempura crunch and raspberry reduction.</p>
          <div class="room112-card-footer">
            <span class="room112-price">$15.50</span>
          </div>
        </div>
      </div>

      <div class="room112-card">
        <div class="room112-card-body">
          <span class="room112-card-badge">Salmon Lovers</span>
          <h3>Salmon Dream Roll</h3>
          <p>Pristine raw Scottish salmon and avocado inside, draped with torched salmon belly, spicy aioli, masago caviar, and crispy fried shallots.</p>
          <div class="room112-card-footer">
            <span class="room112-price">$16.00</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Raw Bar Sourcing Card -->
    <div class="room112-card" style="margin-top:40px; padding:36px; background:linear-gradient(135deg, #fdf4ff, #fafafa); border: 2px solid var(--room112-border);">
      <h3 style="color:var(--room112-dark); margin-bottom:12px;">Sashimi-Grade Sourcing &amp; Koshihikari Shari</h3>
      <p style="color:var(--room112-text); font-size:1rem; line-height:1.7;">At Room 112, we believe that great sushi requires immaculate foundational standards. Our sushi rice (shari) is seasoned with aged red vinegar and sea salt, kept at body temperature, and paired with sustainable wild-caught yellowfin tuna, Scottish salmon, and yellowtail hamachi cut with Japanese high-carbon steel knives.</p>
    </div>

    <div class="room112-cta-banner" style="margin-top:50px;">
      <h2>Experience Uptown’s Favorite Sushi Lounge</h2>
      <p>Reserve a table for dinner or call ahead for pickup at 112 S Tryon St.</p>
      <div class="room112-cta-btns">
        <a href="tel:7043357112" class="room112-btn-hero-primary">Call (704) 335-7112</a>
        <a href="menu.html" class="room112-btn-hero-secondary">Explore Menu</a>
      </div>
    </div>
  </main>

{footer_html()}'''

# 4. modern-asian-bistro-and-wok.html
wok_page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Modern Asian Bistro &amp; Wok Specialties | Room 112 Charlotte</title>
  <meta name="description" content="Savor elevated Chinese and Asian bistro cuisine at Room 112 in Charlotte NC: Honey Walnut Prawns, Crispy Tangerine Beef, Singapore street noodles, and Peking duck.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
{header_html("modern-asian-bistro-and-wok.html")}

  <section class="room112-hero" style="padding: 50px 20px;">
    <div class="room112-hero-inner">
      <span class="room112-hero-pill">High-Heat Culinary Art</span>
      <h1>Elevated Asian Bistro &amp; Wok Gastronomy</h1>
      <p>Beyond our raw bar, Room 112 celebrates classic Chinese and Pan-Asian wok traditions prepared with modern culinary flair and top-tier ingredients.</p>
    </div>
  </section>

  <main class="room112-container">
    <div class="room112-spotlight">
      <div>
        <img src="images/walnut-prawns-wok.jpg" alt="Crispy Honey Glazed Walnut Prawns with sweet cream sauce" class="room112-card-image" style="height:100%; object-fit:cover;">
      </div>
      <div class="room112-spotlight-content">
        <span class="room112-card-badge">Bistro Favorite</span>
        <h3>The Perfect Harmony of Honey &amp; Walnut</h3>
        <p>Our Honey Glazed Walnut Prawns showcase the delicate balance of contrasting textures. Jumbo wild tiger prawns are lightly tempura-battered and flash-fried to an airy crisp, then gently enrobed in our house-made sweetened condensed honey cream glaze.</p>
        <p>Topped with house-candied honey walnuts and served alongside steamed broccoli crowns and fluffy jasmine rice, it remains one of Uptown Charlotte's most requested bistro entrees.</p>
        <div style="margin-top:16px;">
          <a href="tel:7043357112" class="room112-btn-cta">Order for Pickup: (704) 335-7112</a>
        </div>
      </div>
    </div>

    <div class="room112-section-title" style="margin-top:60px;">
      <h2>Featured Wok Entrees</h2>
      <p>Prepared at 800 degrees to capture the essential wok hei aroma.</p>
    </div>

    <div class="room112-grid-3">
      <div class="room112-card">
        <div class="room112-card-body">
          <span class="room112-card-badge">Crisp &amp; Citrus</span>
          <h3>Crispy Tangerine Flank Steak</h3>
          <p>Thinly carved flank steak flash-crisped and glazed in a reduction of aged sun-dried tangerine peel, Sichuan red chilies, and garlic soy sauce.</p>
          <div class="room112-card-footer">
            <span class="room112-price">$18.50</span>
          </div>
        </div>
      </div>

      <div class="room112-card">
        <div class="room112-card-body">
          <span class="room112-card-badge">Roast Poultry</span>
          <h3>Peking Style Roast Duck</h3>
          <p>Slow-roasted duck breast with shattering crispy skin, carved and served with sweet hoisin plum reduction, shredded scallions, and steamed lotus buns.</p>
          <div class="room112-card-footer">
            <span class="room112-price">$22.00</span>
          </div>
        </div>
      </div>

      <div class="room112-card">
        <div class="room112-card-body">
          <span class="room112-card-badge">Curry Noodles</span>
          <h3>Singapore Street Rice Noodles</h3>
          <p>Delicate rice vermicelli wok-tossed with aromatic Madras yellow curry, wild shrimp, chicken, eggs, bell peppers, and crisp bean sprouts.</p>
          <div class="room112-card-footer">
            <span class="room112-price">$15.50</span>
          </div>
        </div>
      </div>
    </div>

    <div class="room112-cta-banner" style="margin-top:50px;">
      <h2>Taste Modern Asian Flavor on South Tryon</h2>
      <p>Dine in with colleagues or call in your order for fast 15-minute pickup at 112 S Tryon St.</p>
      <div class="room112-cta-btns">
        <a href="tel:7043357112" class="room112-btn-hero-primary">Call (704) 335-7112</a>
        <a href="menu.html" class="room112-btn-hero-secondary">View Menu &amp; Prices</a>
      </div>
    </div>
  </main>

{footer_html()}'''

with open(os.path.join(DIR, "signature-rolls-and-sashimi-lounge.html"), "w", encoding="utf-8") as f:
    f.write(sushi_lounge_page)
print("Wrote signature-rolls-and-sashimi-lounge.html")

with open(os.path.join(DIR, "modern-asian-bistro-and-wok.html"), "w", encoding="utf-8") as f:
    f.write(wok_page)
print("Wrote modern-asian-bistro-and-wok.html")
