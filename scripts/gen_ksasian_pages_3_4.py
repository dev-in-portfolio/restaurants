# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\scripts")
from ksasian_builder import header_html, footer_html

DIR = r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\k-s-asian-xpress"

# 3. hibachi-grill-and-wok-specials.html
hibachi_page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Japanese Hibachi &amp; Fiery Wok Specials | K’s Asian Xpress</title>
  <meta name="description" content="Discover our teppan flat-top Japanese hibachi platters and 800-degree wok-charred specials in Charlotte NC. Sirloin steak, shrimp, chicken, and house Yum Yum sauce.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
</head>
<body>
{header_html("hibachi-grill-and-wok-specials.html")}

  <section class="ksasian-hero" style="padding: 50px 20px;">
    <div class="ksasian-hero-inner">
      <span class="ksasian-hero-pill">Teppanyaki &amp; Wok Masters</span>
      <h1>Teppan Hibachi &amp; Flaming Wok Specials</h1>
      <p>High-heat sear seals in natural juices and creates unforgettable caramelized edges on every protein and vegetable we prepare.</p>
    </div>
  </section>

  <main class="ksasian-container">
    <div class="ksasian-spotlight">
      <div>
        <img src="images/hibachi-combo.jpg" alt="Sizzling Teppanyaki Hibachi grill platter with steak, chicken, and shrimp" class="ksasian-card-image" style="height:100%; object-fit:cover;">
      </div>
      <div class="ksasian-spotlight-content">
        <span class="ksasian-card-badge">Teppan Technique</span>
        <h3>The Secret to Our Sizzling Hibachi Platters</h3>
        <p>At K’s Asian Xpress, we bring authentic Japanese steakhouse teppan cooking into a fast-casual format. Our high-carbon steel flat top reaches searing temperatures that caramelize sweet onions, tender zucchini, sliced mushrooms, and seasoned meats in seconds.</p>
        <p>Each platter is finished with our house-whipped garlic butter, toasted sesame seeds, and a squeeze of fresh lemon, accompanied by generous containers of creamy pink Yum Yum sauce.</p>
        <div style="margin-top:16px;">
          <a href="menu.html" class="ksasian-btn-cta">See Hibachi Combos</a>
        </div>
      </div>
    </div>

    <div class="ksasian-section-title" style="margin-top:60px;">
      <h2>The Teppan &amp; Wok Difference</h2>
      <p>Why searing temperatures and fresh scratch-made sauces produce restaurant-quality meals in minutes.</p>
    </div>

    <div class="ksasian-grid-3">
      <div class="ksasian-card" style="padding:28px;">
        <span class="ksasian-card-badge">Scratch Made</span>
        <h4 style="color:var(--ksasian-dark); margin:12px 0; font-size:1.2rem;">Signature Yum Yum Sauce</h4>
        <p style="color:var(--ksasian-text-muted); font-size:0.95rem;">Our celebrated Japanese steakhouse sauce is whipped fresh in-house with real sweet cream, smoked paprika, garlic puree, and rice vinegar. Smooth, slightly tangy, and endlessly dippable.</p>
      </div>

      <div class="ksasian-card" style="padding:28px;">
        <span class="ksasian-card-badge">Wok Hei Magic</span>
        <h4 style="color:var(--ksasian-dark); margin:12px 0; font-size:1.2rem;">800-Degree Wok Searing</h4>
        <p style="color:var(--ksasian-text-muted); font-size:0.95rem;">Our Chinese wok dishes capture the elusive "breath of the wok" (wok hei), creating a smoky aroma and locking in crisp vegetable snap without greasiness.</p>
      </div>

      <div class="ksasian-card" style="padding:28px;">
        <span class="ksasian-card-badge">Daily Fresh Prep</span>
        <h4 style="color:var(--ksasian-dark); margin:12px 0; font-size:1.2rem;">Hand-Trimmed Proteins</h4>
        <p style="color:var(--ksasian-text-muted); font-size:0.95rem;">We trim and marinate our USDA sirloin steak, chicken breast, and wild jumbo shrimp daily in light soy, ginger, and garlic marinades for tenderness.</p>
      </div>
    </div>

    <!-- Wok Masterpieces Section -->
    <div class="ksasian-section-title" style="margin-top:60px;">
      <h2>Popular Wok Classics</h2>
      <p>Pair with steamed jasmine rice or seasoned wok-fried egg rice.</p>
    </div>

    <div class="ksasian-grid-2">
      <div class="ksasian-card" style="padding:32px;">
        <h3 style="color:var(--ksasian-dark); margin-bottom:12px; font-size:1.35rem;">General Tso’s &amp; Orange Peel Crispy Glaze</h3>
        <p style="color:var(--ksasian-text-muted); font-size:0.95rem; margin-bottom:12px;">We double-fry our crispy protein chunks to ensure a shatteringly crisp exterior that stays crunchy even when tossed in our house sweet chili garlic or citrus orange peel glaze.</p>
        <p style="color:var(--ksasian-text-muted); font-size:0.95rem;">Available with chicken breast, tail-on shrimp, or crispy organic tofu for our plant-based guests.</p>
      </div>

      <div class="ksasian-card" style="padding:32px;">
        <h3 style="color:var(--ksasian-dark); margin-bottom:12px; font-size:1.35rem;">Beef with Broccoli &amp; Pepper Steak</h3>
        <p style="color:var(--ksasian-text-muted); font-size:0.95rem; margin-bottom:12px;">Marinated flank steak seared at flash heat with crunchy broccoli crowns or sweet bell peppers and yellow onions in rich black pepper oyster gravy.</p>
        <p style="color:var(--ksasian-text-muted); font-size:0.95rem;">A classic Chinese comfort dish served with plenty of savory sauce to coat every grain of fluffy rice.</p>
      </div>
    </div>

    <div class="ksasian-cta-banner" style="margin-top:50px;">
      <h2>Taste the Sizzle Tonight</h2>
      <p>Call in your order for fast 10-minute takeout pickup at 10102 Albemarle Rd.</p>
      <div class="ksasian-cta-btns">
        <a href="tel:9802019962" class="ksasian-btn-hero-primary">Call (980) 201-9962</a>
        <a href="menu.html" class="ksasian-btn-hero-secondary">View Menu &amp; Prices</a>
      </div>
    </div>
  </main>

{footer_html()}'''

# 4. thai-noodles-and-curry-bowls.html
thai_page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Thai Street Noodles &amp; Coconut Curries | K’s Asian Xpress Charlotte</title>
  <meta name="description" content="Savor authentic Thai tamarind Pad Thai, spicy basil Drunken Noodles, and slow-simmered red and green coconut curries in East Charlotte NC.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
</head>
<body>
{header_html("thai-noodles-and-curry-bowls.html")}

  <section class="ksasian-hero" style="padding: 50px 20px;">
    <div class="ksasian-hero-inner">
      <span class="ksasian-hero-pill">Authentic Street Flavors</span>
      <h1>Thai Street Noodles &amp; Rich Coconut Curries</h1>
      <p>Balance the four pillars of Thai gastronomy: sweet, sour, salty, and spicy in every handmade noodle bowl and fragrant coconut curry.</p>
    </div>
  </section>

  <main class="ksasian-container">
    <div class="ksasian-spotlight">
      <div>
        <img src="images/thai-noodles.jpg" alt="Authentic Pad Thai noodles with jumbo shrimp, bean sprouts, and crushed peanuts" class="ksasian-card-image" style="height:100%; object-fit:cover;">
      </div>
      <div class="ksasian-spotlight-content">
        <span class="ksasian-card-badge">Bangkok Street Classic</span>
        <h3>The Art of Real Tamarind Pad Thai</h3>
        <p>Unlike ordinary takeout spots that rely on ketchup or artificial food dyes, our Pad Thai starts with authentic steeped tamarind pulp, palm sugar, fish sauce, and shallots simmered into a glossy, complex sauce.</p>
        <p>Flash-fried with fresh rice noodles, scrambled egg, crisp scallions, and bean sprouts, each plate is served with a lime wedge and generous handful of crushed roasted peanuts.</p>
        <div style="margin-top:16px;">
          <a href="tel:9802019962" class="ksasian-btn-cta">Order for Pickup: (980) 201-9962</a>
        </div>
      </div>
    </div>

    <div class="ksasian-section-title" style="margin-top:60px;">
      <h2>Thai Noodle &amp; Curry Profiles</h2>
      <p>Every dish can be customized with your choice of protein and heat intensity.</p>
    </div>

    <div class="ksasian-grid-3">
      <div class="ksasian-card">
        <div class="ksasian-card-body">
          <span class="ksasian-card-badge">Spicy &amp; Fragrant</span>
          <h3>Drunken Noodles (Pad Kee Mao)</h3>
          <p>Extra-wide rice noodles wok-charred with sweet Thai basil, fresh garlic, crushed red chilies, bell peppers, and sweet yellow onions. Bold, aromatic, and invigoratingly spicy.</p>
          <div class="ksasian-card-footer">
            <span class="ksasian-price">$13.99</span>
          </div>
        </div>
      </div>

      <div class="ksasian-card">
        <div class="ksasian-card-body">
          <span class="ksasian-card-badge">Savory &amp; Sweet</span>
          <h3>Pad See Ew</h3>
          <p>Wide ribbon rice noodles caramelized in premium dark sweet soy sauce with Chinese broccoli, farm eggs, and toasted garlic. Savory comfort loved by all ages.</p>
          <div class="ksasian-card-footer">
            <span class="ksasian-price">$13.50</span>
          </div>
        </div>
      </div>

      <div class="ksasian-card">
        <div class="ksasian-card-body">
          <span class="ksasian-card-badge">Aromatic &amp; Rich</span>
          <h3>Thai Red Coconut Curry</h3>
          <p>Smooth, creamy coconut milk stewed with red chili paste, tender bamboo shoots, crisp zucchini, red bell pepper, and aromatic Thai basil leaves. Served with steamed jasmine rice.</p>
          <div class="ksasian-card-footer">
            <span class="ksasian-price">$14.25</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Spice Level Guide -->
    <div class="ksasian-card" style="margin-top:40px; padding:36px; background-color:var(--ksasian-surface-alt); border: 2px solid var(--ksasian-border);">
      <h3 style="color:var(--ksasian-dark); margin-bottom:14px;">Customized Thai Heat Scale</h3>
      <p style="color:var(--ksasian-text); font-size:0.95rem; margin-bottom:16px;">We prepare every Thai dish to your preferred spice preference upon order:</p>
      <ul style="margin-left:20px; color:var(--ksasian-text-muted); font-size:0.95rem; line-height:1.8;">
        <li><strong>Level 0 - Mild:</strong> Full flavor with zero chili heat; perfect for kids and mild palates.</li>
        <li><strong>Level 1 - Medium:</strong> A gentle warm chili tingle that highlights the coconut and herb notes.</li>
        <li><strong>Level 2 - Hot:</strong> Authentic heat for seasoned spicy food lovers with fresh sliced jalapenos and red chili flakes.</li>
        <li><strong>Level 3 - Thai Spicy:</strong> Intense heat with ground bird's eye chilies and hot chili oil for true spice aficionados.</li>
      </ul>
    </div>

    <div class="ksasian-cta-banner" style="margin-top:50px;">
      <h2>Satisfy Your Thai Noodle Cravings</h2>
      <p>Order takeout for pickup at 10102 Albemarle Rd in Charlotte.</p>
      <div class="ksasian-cta-btns">
        <a href="tel:9802019962" class="ksasian-btn-hero-primary">Call (980) 201-9962</a>
        <a href="menu.html" class="ksasian-btn-hero-secondary">View Full Menu</a>
      </div>
    </div>
  </main>

{footer_html()}'''

with open(os.path.join(DIR, "hibachi-grill-and-wok-specials.html"), "w", encoding="utf-8") as f:
    f.write(hibachi_page)
print("Wrote hibachi-grill-and-wok-specials.html")

with open(os.path.join(DIR, "thai-noodles-and-curry-bowls.html"), "w", encoding="utf-8") as f:
    f.write(thai_page)
print("Wrote thai-noodles-and-curry-bowls.html")
