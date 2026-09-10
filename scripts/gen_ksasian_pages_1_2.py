# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\scripts")
from ksasian_builder import header_html, footer_html

DIR = r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\k-s-asian-xpress"

# 1. index.html
index_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>K’s Asian Xpress | Hibachi, Thai &amp; Wok Fusion in Charlotte NC</title>
  <meta name="description" content="Experience high-heat Japanese hibachi, wok-tossed Thai noodles, and crispy Chinese classics at K’s Asian Xpress on Albemarle Rd in Charlotte. Fast pickup and dine-in.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
</head>
<body>
{header_html("index.html")}

  <section class="ksasian-hero">
    <div class="ksasian-hero-inner">
      <span class="ksasian-hero-pill">Albemarle Road Asian Fusion Destination</span>
      <h1>Sizzling Teppan Hibachi, Fiery Wok &amp; Street-Style Thai</h1>
      <p>Quick, flavorful, and generously portioned Asian comfort cuisine in East Charlotte. From garlic butter hibachi combos and velvety coconut curries to crispy wings and wok-tossed noodles made fresh in minutes.</p>
      <div class="ksasian-hero-actions">
        <a href="menu.html" class="ksasian-btn-hero-primary">Explore Full Menu</a>
        <a href="hibachi-grill-and-wok-specials.html" class="ksasian-btn-hero-secondary">Hibachi &amp; Wok Specials</a>
        <a href="party-platters-and-family-bundles.html" class="ksasian-btn-hero-secondary">Family Bundles</a>
      </div>
    </div>
  </section>

  <main class="ksasian-container">
    <div class="ksasian-section-title">
      <h2>Crafted with High Heat &amp; Bold Flavors</h2>
      <p>Explore our signature culinary pillars spanning Japanese teppanyaki, Thai street noodles, and classic Chinese wok traditions.</p>
    </div>

    <div class="ksasian-grid-3">
      <div class="ksasian-card">
        <img src="images/hibachi-combo.jpg" alt="Sizzling Hibachi Steak and Shrimp combo with fried rice" class="ksasian-card-image">
        <div class="ksasian-card-body">
          <span class="ksasian-card-badge">Teppanyaki Specialty</span>
          <h3>Hibachi Steak &amp; Chicken Combo</h3>
          <p>Tender grilled sirloin steak and juicy chicken breast seared with garlic butter and soy teriyaki glaze. Served over seasoned egg fried rice with zucchini, mushrooms, onions, and house Yum Yum sauce.</p>
          <div class="ksasian-card-footer">
            <span class="ksasian-price">$16.50</span>
            <a href="hibachi-grill-and-wok-specials.html" class="ksasian-btn-cta">View Hibachi</a>
          </div>
        </div>
      </div>

      <div class="ksasian-card">
        <img src="images/thai-noodles.jpg" alt="Authentic wok-tossed Pad Thai noodles with shrimp and lime" class="ksasian-card-image">
        <div class="ksasian-card-body">
          <span class="ksasian-card-badge">Thai Street Favorite</span>
          <h3>Traditional Pad Thai &amp; Drunken Noodles</h3>
          <p>Rice noodles wok-tossed in tangy tamarind sauce with jumbo shrimp, eggs, bean sprouts, scallions, and crushed roasted peanuts. Available in your choice of customized spice levels from mild to Thai hot.</p>
          <div class="ksasian-card-footer">
            <span class="ksasian-price">$13.99</span>
            <a href="thai-noodles-and-curry-bowls.html" class="ksasian-btn-cta">Explore Thai</a>
          </div>
        </div>
      </div>

      <div class="ksasian-card">
        <img src="images/general-tso-curry.jpg" alt="Crispy General Tso Chicken with steamed broccoli" class="ksasian-card-image">
        <div class="ksasian-card-body">
          <span class="ksasian-card-badge">Wok Classic</span>
          <h3>Crispy General Tso’s Chicken or Tofu</h3>
          <p>Golden-crisped bites tossed in our signature sweet and spicy ginger garlic glaze with roasted chili peppers and fresh broccoli florets. Also available with crispy vegetarian tofu.</p>
          <div class="ksasian-card-footer">
            <span class="ksasian-price">$12.99</span>
            <a href="menu.html" class="ksasian-btn-cta">See Entrees</a>
          </div>
        </div>
      </div>
    </div>

    <!-- Spotlight Section -->
    <div class="ksasian-spotlight">
      <div>
        <img src="images/dumplings-wings.jpg" alt="Handmade pork dumplings and crispy seasoned wings" class="ksasian-card-image" style="height:100%; object-fit:cover;">
      </div>
      <div class="ksasian-spotlight-content">
        <span class="ksasian-card-badge">Starters &amp; Party Favorites</span>
        <h3>Handmade Dumplings &amp; Crispy Jumbo Wings</h3>
        <p>Start your meal with our pan-fried pork dumplings folded with fresh scallions, ginger, and garlic, served with house chili-soy dipping sauce. Pair them with golden fried Crab Rangoon or our famous jumbo chicken wings tossed in Lemon Pepper, Sweet Thai Chili, or Sweet Teriyaki.</p>
        <p>Great as an appetizer for dine-in or bundled into 20-piece party trays for gamedays and office gatherings.</p>
        <div style="margin-top:20px;">
          <a href="party-platters-and-family-bundles.html" class="ksasian-btn-cta">Explore Party Packs</a>
        </div>
      </div>
    </div>

    <!-- Express Highlights -->
    <div class="ksasian-section-title" style="margin-top:60px;">
      <h2>Why Charlotte Diners Love K’s Asian Xpress</h2>
      <p>Speed, generous portions, and authentic cooking methods make us a favorite in East Charlotte.</p>
    </div>

    <div class="ksasian-grid-3">
      <div class="ksasian-card" style="padding:28px;">
        <h4 style="color:var(--ksasian-primary); margin-bottom:12px; font-size:1.2rem;">Speed Without Compromise</h4>
        <p style="color:var(--ksasian-text-muted); font-size:0.95rem;">Every entree is cooked fresh to order on our flaming woks and flat-top teppan griddles in 10-15 minutes, preserving vegetable crispness and succulent meats.</p>
      </div>
      <div class="ksasian-card" style="padding:28px;">
        <h4 style="color:var(--ksasian-primary); margin-bottom:12px; font-size:1.2rem;">Customizable Heat Levels</h4>
        <p style="color:var(--ksasian-text-muted); font-size:0.95rem;">Whether you enjoy soothing mild teriyaki, medium citrus curry, or searing Thai hot bird's eye chilies, our chefs tailor every dish to your exact palate.</p>
      </div>
      <div class="ksasian-card" style="padding:28px;">
        <h4 style="color:var(--ksasian-primary); margin-bottom:12px; font-size:1.2rem;">Generous Value Portions</h4>
        <p style="color:var(--ksasian-text-muted); font-size:0.95rem;">Our hibachi combos, fried rice bowls, and noodle boxes come packed to the brim with proteins, fresh vegetables, and complementary Yum Yum sauces.</p>
      </div>
    </div>

    <!-- CTA Section -->
    <div class="ksasian-cta-banner" style="margin-top:50px;">
      <h2>Hungry for Express Asian Flavor?</h2>
      <p>Order takeout over the phone for rapid pickup at 10102 Albemarle Rd or dine in with us today.</p>
      <div class="ksasian-cta-btns">
        <a href="tel:9802019962" class="ksasian-btn-hero-primary">Call (980) 201-9962</a>
        <a href="visit.html" class="ksasian-btn-hero-secondary">View Location &amp; Hours</a>
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
  <title>Full Asian Fusion Menu | K’s Asian Xpress Charlotte</title>
  <meta name="description" content="Explore the full menu at K’s Asian Xpress in Charlotte: Japanese Hibachi, Thai Noodles, Coconut Curries, Chinese Wok Favorites, Wings, Dumplings, and Boba.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
</head>
<body>
{header_html("menu.html")}

  <section class="ksasian-hero" style="padding: 50px 20px;">
    <div class="ksasian-hero-inner">
      <span class="ksasian-hero-pill">Fresh Made to Order</span>
      <h1>Full Asian Fusion Menu</h1>
      <p>Select your favorite category to explore our flat-top hibachi bowls, authentic Thai street noodles, wok classics, crispy appetizers, and beverage options.</p>
    </div>
  </section>

  <main class="ksasian-container">
    <div class="ksasian-tabs">
      <button class="ksasian-tab-btn active" data-target="tab-hibachi">Japanese Hibachi</button>
      <button class="ksasian-tab-btn" data-target="tab-thai">Thai Noodles &amp; Curries</button>
      <button class="ksasian-tab-btn" data-target="tab-wok">Chinese Wok Classics</button>
      <button class="ksasian-tab-btn" data-target="tab-appetizers">Wings &amp; Appetizers</button>
      <button class="ksasian-tab-btn" data-target="tab-rice">Rice, Lo Mein &amp; Drinks</button>
    </div>

    <!-- Group 1: Hibachi -->
    <div class="ksasian-menu-group active" id="tab-hibachi">
      <div class="ksasian-section-title">
        <h2>Japanese Hibachi Griddle Platters</h2>
        <p>Served with seasoned egg fried rice, hibachi sweet carrots, grilled zucchini, onions, mushrooms, and house Yum Yum dipping sauce.</p>
      </div>

      <div class="ksasian-grid-2">
        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Hibachi Chicken</h4>
            <span class="ksasian-item-price">$12.99</span>
          </div>
          <p class="ksasian-item-desc">Tender diced chicken breast seared with garlic butter, soy sauce, and a touch of lemon on our teppanyaki flat top.</p>
          <div class="ksasian-item-tags">
            <span class="ksasian-tag ksasian-tag-popular">Popular</span>
          </div>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Hibachi Sirloin Steak</h4>
            <span class="ksasian-item-price">$15.50</span>
          </div>
          <p class="ksasian-item-desc">Juicy USDA sirloin steak cubes seared to your preferred temperature with garlic butter and savory hibachi glaze.</p>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Hibachi Jumbo Shrimp</h4>
            <span class="ksasian-item-price">$15.99</span>
          </div>
          <p class="ksasian-item-desc">Plump tail-on shrimp seared quickly with lemon garlic butter and scallions, served with double Yum Yum sauce.</p>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Hibachi Salmon Fillet</h4>
            <span class="ksasian-item-price">$16.99</span>
          </div>
          <p class="ksasian-item-desc">Fresh Atlantic salmon seared with a caramelized sweet teriyaki crust and cracked black pepper.</p>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Hibachi Steak &amp; Chicken Combo</h4>
            <span class="ksasian-item-price">$16.50</span>
          </div>
          <p class="ksasian-item-desc">The ultimate duo: tender sirloin steak paired with juicy seasoned chicken breast and grilled vegetables.</p>
          <div class="ksasian-item-tags">
            <span class="ksasian-tag ksasian-tag-popular">Guest Favorite</span>
          </div>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Hibachi Triple Combo (Steak, Chicken, Shrimp)</h4>
            <span class="ksasian-item-price">$19.99</span>
          </div>
          <p class="ksasian-item-desc">A generous feast featuring sirloin steak, chicken breast, and jumbo shrimp over mountains of fried rice.</p>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Hibachi Tofu &amp; Vegetable Platter</h4>
            <span class="ksasian-item-price">$11.50</span>
          </div>
          <p class="ksasian-item-desc">Crisp golden tofu cubes, broccoli, mushrooms, zucchini, carrots, and sweet onions seared with vegetarian soy garlic butter.</p>
          <div class="ksasian-item-tags">
            <span class="ksasian-tag ksasian-tag-veg">Vegetarian</span>
          </div>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Teriyaki Chicken Bowl (Express)</h4>
            <span class="ksasian-item-price">$10.99</span>
          </div>
          <p class="ksasian-item-desc">Glazed chicken breast over steamed white or fried rice with steamed broccoli and sesame seeds.</p>
        </div>
      </div>
    </div>

    <!-- Group 2: Thai -->
    <div class="ksasian-menu-group" id="tab-thai">
      <div class="ksasian-section-title">
        <h2>Thai Street Noodles &amp; Coconut Curries</h2>
        <p>Customizable spice levels: Mild, Medium, Hot, or Thai Spicy. Choice of Chicken, Beef, Shrimp, or Tofu.</p>
      </div>

      <div class="ksasian-grid-2">
        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Traditional Pad Thai</h4>
            <span class="ksasian-item-price">$13.50</span>
          </div>
          <p class="ksasian-item-desc">Thin rice noodles stir-fried in authentic tamarind sauce with egg, crisp bean sprouts, scallions, lime wedge, and crushed roasted peanuts.</p>
          <div class="ksasian-item-tags">
            <span class="ksasian-tag ksasian-tag-popular">Signature Dish</span>
          </div>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Drunken Noodles (Pad Kee Mao)</h4>
            <span class="ksasian-item-price">$13.99</span>
          </div>
          <p class="ksasian-item-desc">Wide flat rice noodles wok-charred with sweet Thai basil leaves, bell peppers, white onions, egg, and spicy chili garlic puree.</p>
          <div class="ksasian-item-tags">
            <span class="ksasian-tag ksasian-tag-spicy">Spicy</span>
          </div>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Pad See Ew</h4>
            <span class="ksasian-item-price">$13.50</span>
          </div>
          <p class="ksasian-item-desc">Broad rice noodles caramelized in dark sweet soy sauce with Chinese broccoli, egg, garlic, and your choice of protein.</p>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Thai Red Coconut Curry</h4>
            <span class="ksasian-item-price">$14.25</span>
          </div>
          <p class="ksasian-item-desc">Fragrant red chili curry simmered with rich coconut milk, bamboo shoots, red bell peppers, zucchini, and fresh Thai basil. Served with jasmine rice.</p>
          <div class="ksasian-item-tags">
            <span class="ksasian-tag ksasian-tag-spicy">Spicy</span>
          </div>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Thai Green Coconut Curry</h4>
            <span class="ksasian-item-price">$14.25</span>
          </div>
          <p class="ksasian-item-desc">Aromatic green chili paste, kaffir lime leaf, coconut cream, green beans, eggplant, and sweet basil leaves. Served with jasmine rice.</p>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Tom Yum Fried Rice</h4>
            <span class="ksasian-item-price">$12.99</span>
          </div>
          <p class="ksasian-item-desc">Jasmine rice tossed with lemony lemongrass, galangal, kaffir lime, chili paste, egg, and jumbo shrimp.</p>
          <div class="ksasian-item-tags">
            <span class="ksasian-tag ksasian-tag-spicy">Tangy &amp; Spicy</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Group 3: Wok -->
    <div class="ksasian-menu-group" id="tab-wok">
      <div class="ksasian-section-title">
        <h2>Chinese Wok Classics</h2>
        <p>Wok-seared at 800 degrees with fresh vegetables and house sauces. Served with steamed or fried rice.</p>
      </div>

      <div class="ksasian-grid-2">
        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>General Tso’s Chicken</h4>
            <span class="ksasian-item-price">$12.99</span>
          </div>
          <p class="ksasian-item-desc">Crispy fried chicken chunks tossed in a savory, tangy, sweet chili garlic glaze with steamed broccoli.</p>
          <div class="ksasian-item-tags">
            <span class="ksasian-tag ksasian-tag-spicy">Mild Heat</span>
            <span class="ksasian-tag ksasian-tag-popular">Bestseller</span>
          </div>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Beef with Broccoli</h4>
            <span class="ksasian-item-price">$14.50</span>
          </div>
          <p class="ksasian-item-desc">Marinated tender flank steak slices flash-seared with fresh broccoli crowns in a rich ginger-oyster brown sauce.</p>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Honey Sesame Chicken</h4>
            <span class="ksasian-item-price">$12.99</span>
          </div>
          <p class="ksasian-item-desc">Crispy chicken breast bites coated in sweet honey sesame reduction and toasted white sesame seeds.</p>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Pepper Steak with Onions</h4>
            <span class="ksasian-item-price">$14.50</span>
          </div>
          <p class="ksasian-item-desc">Tender beef slices stir-fried with green bell peppers, sweet yellow onions, and crushed black peppercorn sauce.</p>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Orange Peel Crispy Chicken</h4>
            <span class="ksasian-item-price">$12.99</span>
          </div>
          <p class="ksasian-item-desc">Crisp chicken morsels tossed in a caramelized mandarin orange peel sauce with whole dried red chilies.</p>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Kung Pao Chicken or Shrimp</h4>
            <span class="ksasian-item-price">$13.50</span>
          </div>
          <p class="ksasian-item-desc">Wok-fired with roasted crunchy peanuts, diced zucchini, celery, chili peppers, and Sichuan peppercorns.</p>
          <div class="ksasian-item-tags">
            <span class="ksasian-tag ksasian-tag-spicy">Spicy</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Group 4: Appetizers -->
    <div class="ksasian-menu-group" id="tab-appetizers">
      <div class="ksasian-section-title">
        <h2>Appetizers, Wings &amp; Dim Sum</h2>
        <p>Crispy starters and fresh dumplings hand-folded daily in our kitchen.</p>
      </div>

      <div class="ksasian-grid-2">
        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Handmade Pork Dumplings (6 pcs)</h4>
            <span class="ksasian-item-price">$7.99</span>
          </div>
          <p class="ksasian-item-desc">Pan-fried (potstickers) or steamed with minced pork, scallions, cabbage, and ginger. Served with dumpling soy dip.</p>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Crab Rangoon (6 pcs)</h4>
            <span class="ksasian-item-price">$6.99</span>
          </div>
          <p class="ksasian-item-desc">Crispy fried wonton wrappers filled with rich cream cheese, real crabmeat, and scallions. Served with sweet and sour sauce.</p>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Jumbo Crispy Wings (6 pcs / 10 pcs)</h4>
            <span class="ksasian-item-price">$8.99 / $13.99</span>
          </div>
          <p class="ksasian-item-desc">Crisp jumbo party wings tossed in your choice of sauce: Lemon Pepper, Sweet Thai Chili, Honey Teriyaki, or Spicy Buffalo.</p>
          <div class="ksasian-item-tags">
            <span class="ksasian-tag ksasian-tag-popular">Fan Favorite</span>
          </div>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Crispy Pork or Shrimp Egg Rolls (2 pcs)</h4>
            <span class="ksasian-item-price">$4.25</span>
          </div>
          <p class="ksasian-item-desc">Golden blistered rolls stuffed with seasoned cabbage, carrots, and savory meat filling.</p>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Vegetarian Spring Rolls (3 pcs)</h4>
            <span class="ksasian-item-price">$4.50</span>
          </div>
          <p class="ksasian-item-desc">Crisp thin-crust rolls filled with shredded wood ear mushrooms, carrots, glass noodles, and cabbage.</p>
          <div class="ksasian-item-tags">
            <span class="ksasian-tag ksasian-tag-veg">Vegetarian</span>
          </div>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Edamame with Sea Salt &amp; Garlic</h4>
            <span class="ksasian-item-price">$5.50</span>
          </div>
          <p class="ksasian-item-desc">Steamed tender young soybean pods tossed in coarse Himalayan sea salt and toasted garlic oil.</p>
          <div class="ksasian-item-tags">
            <span class="ksasian-tag ksasian-tag-veg">Vegetarian</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Group 5: Rice, Noodles & Drinks -->
    <div class="ksasian-menu-group" id="tab-rice">
      <div class="ksasian-section-title">
        <h2>Wok Fried Rice, Lo Mein &amp; Beverages</h2>
        <p>Comforting sides, hearty noodle bowls, and chilled Asian specialty drinks.</p>
      </div>

      <div class="ksasian-grid-2">
        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>House Special Fried Rice</h4>
            <span class="ksasian-item-price">$12.50</span>
          </div>
          <p class="ksasian-item-desc">Wok-tossed jasmine rice with chicken, sirloin steak, jumbo shrimp, eggs, peas, carrots, and scallions.</p>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>House Special Lo Mein</h4>
            <span class="ksasian-item-price">$12.99</span>
          </div>
          <p class="ksasian-item-desc">Soft egg wheat noodles stir-fried with chicken, beef, shrimp, shredded cabbage, carrots, and bean sprouts in dark garlic sauce.</p>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Thai Iced Tea with Sweet Cream</h4>
            <span class="ksasian-item-price">$4.25</span>
          </div>
          <p class="ksasian-item-desc">Brewed Ceylon black tea infused with star anise and orange blossom, topped with rich sweetened condensed milk.</p>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Brown Sugar Boba Milk Tea</h4>
            <span class="ksasian-item-price">$4.95</span>
          </div>
          <p class="ksasian-item-desc">Creamy black milk tea swirled with warm brown sugar syrup and chewy tapioca pearls.</p>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Extra House Yum Yum Sauce (4 oz)</h4>
            <span class="ksasian-item-price">$1.50</span>
          </div>
          <p class="ksasian-item-desc">Our signature Japanese steakhouse pink sauce with sweet paprika, garlic, and cream.</p>
        </div>

        <div class="ksasian-menu-item">
          <div class="ksasian-item-header">
            <h4>Japanese Ginger Salad Dressing (4 oz)</h4>
            <span class="ksasian-item-price">$1.50</span>
          </div>
          <p class="ksasian-item-desc">Zesty house-blended grated ginger, sweet onion, and rice vinegar dressing.</p>
        </div>
      </div>
    </div>

    <!-- Bottom Order CTA -->
    <div class="ksasian-cta-banner" style="margin-top:50px;">
      <h2>Ready to Place Your Pickup Order?</h2>
      <p>Call our Albemarle Road kitchen directly for hot, speedy takeout in 10-15 minutes.</p>
      <div class="ksasian-cta-btns">
        <a href="tel:9802019962" class="ksasian-btn-hero-primary">Call (980) 201-9962</a>
        <a href="party-platters-and-family-bundles.html" class="ksasian-btn-hero-secondary">View Party Bundles</a>
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
