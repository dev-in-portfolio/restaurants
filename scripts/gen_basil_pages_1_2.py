# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("scripts")
from basil_builder import header_html, footer_html

# Page 1: index.html
index_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Basil Thai Cuisine | Contemporary Thai Dining in Uptown Charlotte</title>
  <meta name="description" content="Experience contemporary Thai culinary artistry at Basil Thai Cuisine in Uptown Charlotte. Signature crispy Basil Duck, scratch coconut curries, Pad Thai, and cocktail lounge.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("index.html")}

  <section class="basil-hero">
    <div class="basil-container">
      <span class="basil-badge">Uptown Charlotte Contemporary Thai</span>
      <h1 style="font-size:2.8rem; font-weight:900; margin:15px 0; letter-spacing:-0.02em;">Elevated Thai Gastronomy &amp; Modern Urban Ambiance</h1>
      <p style="font-size:1.15rem; color:#e2e8f0; max-width:760px; margin:0 auto 25px;">
        Located on North Church Street, Basil Thai Cuisine merges authentic Southeast Asian heritage with modern culinary refinement, featuring handcrafted curries, sizzling wok specialties, and our famed Crispy Basil Duck.
      </p>
      <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
        <a href="menu.html" class="basil-btn-primary">View Full Menu</a>
        <a href="chef-specialties-and-curries.html" class="basil-btn-outline">Chef Specialties</a>
        <a href="tel:7043327212" class="basil-btn-primary" style="background:#047857; color:#fff;">Reserve or Order: (704) 332-7212</a>
      </div>
    </div>
  </section>

  <!-- Key Pillars Section -->
  <section style="background-color:#ffffff; border-bottom:1px solid #e2e8f0; padding:28px 0;">
    <div class="basil-container">
      <div class="basil-grid-4" style="text-align:center;">
        <div>
          <h3 style="color:#064e3b; font-size:1.35rem; font-weight:800;">Crispy Basil Duck</h3>
          <p style="color:#475569; font-size:0.9rem;">Our Celebrated Signature</p>
        </div>
        <div>
          <h3 style="color:#064e3b; font-size:1.35rem; font-weight:800;">Scratch Curries</h3>
          <p style="color:#475569; font-size:0.9rem;">Simmered Coconut &amp; Herbs</p>
        </div>
        <div>
          <h3 style="color:#064e3b; font-size:1.35rem; font-weight:800;">Express Lunch</h3>
          <p style="color:#475569; font-size:0.9rem;">Uptown Corporate Dining</p>
        </div>
        <div>
          <h3 style="color:#064e3b; font-size:1.35rem; font-weight:800;">Craft Lounge</h3>
          <p style="color:#475569; font-size:0.9rem;">Thai Infused Cocktails &amp; Wine</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Main Narrative Section -->
  <main class="basil-container" style="padding:60px 24px;">
    <div class="basil-grid-2" style="align-items:center; margin-bottom:60px;">
      <div>
        <span class="basil-tag">Culinary Mastery</span>
        <h2 style="font-size:2.2rem; color:#064e3b; margin:15px 0; font-weight:800;">The Harmony of the Five Thai Flavor Profiles</h2>
        <p style="color:#475569; line-height:1.7; margin-bottom:16px;">
          At Basil Thai Cuisine, every dish honors the fundamental philosophy of Thai cooking: an exquisite equilibrium among sweet, sour, salty, spicy, and umami. Fresh lemongrass, kaffir lime leaves, galangal root, and fragrant Thai holy basil are prepared daily by our culinary team.
        </p>
        <p style="color:#475569; line-height:1.7; margin-bottom:20px;">
          Whether joining us for an efficient weekday business lunch or an intimate multi-course dinner with vintage wine, guests enjoy warm, impeccable service in a sophisticated dining room.
        </p>
        <div style="display:flex; gap:12px; flex-wrap:wrap;">
          <a href="menu.html" class="basil-btn-primary">Browse All Dishes</a>
          <a href="visit.html" class="basil-btn-outline" style="color:#064e3b; border-color:#064e3b;">Hours &amp; Location</a>
        </div>
      </div>
      <div>
        <img src="images/basil-duck-specialty.jpg" alt="Signature Crispy Basil Duck specialty at Basil Thai Charlotte" style="width:100%; height:400px; object-fit:cover; border-radius:12px; box-shadow:var(--basil-shadow-lg);">
      </div>
    </div>

    <!-- Featured Dishes -->
    <div style="text-align:center; margin-bottom:40px;">
      <span class="basil-tag">House Favorites</span>
      <h2 style="font-size:2rem; color:#064e3b; margin-top:10px;">Signature Creations</h2>
    </div>

    <div class="basil-grid-3" style="margin-bottom:60px;">
      <div class="basil-feature-card">
        <img src="images/basil-duck-specialty.jpg" alt="Crispy Basil Duck" class="basil-feature-img">
        <div class="basil-feature-body">
          <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
            <h3 style="color:#064e3b; font-size:1.25rem;">Crispy Basil Duck</h3>
            <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$27.95</span>
          </div>
          <p style="color:#475569; font-size:0.95rem; margin-bottom:16px;">Crispy half roasted duck breast sliced over sauteed bell peppers, sweet onions, and crisp green beans in our spicy Thai basil garlic chili reduction.</p>
          <span class="basil-tag">Chef's Crown Jewel</span>
        </div>
      </div>

      <div class="basil-feature-card">
        <img src="images/pad-thai-noodles.jpg" alt="Traditional Wok Pad Thai" class="basil-feature-img">
        <div class="basil-feature-body">
          <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
            <h3 style="color:#064e3b; font-size:1.25rem;">Authentic Pad Thai</h3>
            <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$18.50</span>
          </div>
          <p style="color:#475569; font-size:0.95rem; margin-bottom:16px;">Wok-seared thin rice noodles tossed with egg, bean sprouts, crushed toasted peanuts, scallions, and tangy house tamarind palm sugar sauce.</p>
          <span class="basil-tag">Classic Favorite</span>
        </div>
      </div>

      <div class="basil-feature-card">
        <img src="images/thai-curry-bowl.jpg" alt="Fragrant Green Coconut Curry" class="basil-feature-img">
        <div class="basil-feature-body">
          <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
            <h3 style="color:#064e3b; font-size:1.25rem;">Royal Green Curry</h3>
            <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$19.50</span>
          </div>
          <p style="color:#475569; font-size:0.95rem; margin-bottom:16px;">Fragrant green chili coconut broth simmered with tender bamboo shoots, eggplant, red bell peppers, and fresh Thai basil leaves with jasmine rice.</p>
          <span class="basil-tag">Scratch Simmered</span>
        </div>
      </div>
    </div>

    <!-- Corporate Lunch & Evening Dining Strip -->
    <div class="basil-banner-strip">
      <span class="basil-badge" style="background:rgba(255,255,255,0.15); border-color:#ffffff; color:#ffffff;">Executive Dining</span>
      <h2 style="font-size:2rem; margin:12px 0 16px; color:#ffffff;">Express Lunch &amp; Private Evening Gatherings</h2>
      <p style="max-width:700px; margin:0 auto 24px; color:#e2e8f0; font-size:1.05rem;">
        Hosting clients or ordering lunch for your Uptown office? Discover our streamlined bento combinations, group catering pans, and reserved dining sections.
      </p>
      <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
        <a href="executive-lunch-and-catering.html" class="basil-btn-primary">Explore Catering &amp; Lunch</a>
        <a href="tel:7043327212" class="basil-btn-outline">Call (704) 332-7212</a>
      </div>
    </div>
  </main>

{footer_html()}
"""

with open("basil-thai-cuisine/index.html", "w", encoding="utf-8") as f:
    f.write(index_content)
print("Written: basil-thai-cuisine/index.html")

# Page 2: menu.html
menu_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Full Food &amp; Drink Menu | Basil Thai Cuisine Uptown Charlotte</title>
  <meta name="description" content="View the full menu at Basil Thai Cuisine Charlotte: appetizers, Basil rolls, coconut curries, Pad Thai, Pad See Eu, Basil Duck, sea bass, and craft cocktails.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("menu.html")}

  <section class="basil-hero-compact">
    <div class="basil-container">
      <span class="basil-badge">Culinary Menu</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Our Complete Menu</h1>
      <p style="font-size:1.1rem; color:#cbd5e1; max-width:700px; margin:0 auto;">Handcrafted curries, sizzling wok noodles, signature duck creations, and refreshing specialty drinks.</p>
    </div>
  </section>

  <main class="basil-container" style="padding:40px 24px 60px;">
    <!-- Interactive Filter Buttons -->
    <div class="basil-filters">
      <button class="basil-filter-btn active" data-filter="all">All Items</button>
      <button class="basil-filter-btn" data-filter="starters">Appetizers &amp; Rolls</button>
      <button class="basil-filter-btn" data-filter="specialties">Chef Specialties &amp; Duck</button>
      <button class="basil-filter-btn" data-filter="curries">Traditional Curries</button>
      <button class="basil-filter-btn" data-filter="noodles">Wok Noodles &amp; Rice</button>
      <button class="basil-filter-btn" data-filter="lunch">Lunch Express</button>
    </div>

    <!-- Menu Grid -->
    <div class="basil-grid-3" id="menu-items-grid" style="gap:24px;">
      <!-- Starters -->
      <div class="basil-card basil-menu-item" data-category="starters">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#064e3b; font-size:1.2rem;">Fresh Basil Rolls (2pc)</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$8.95</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Delicate rice paper filled with tender shrimp, crisp lettuce, cucumber, rice vermicelli, cilantro, and fresh Thai basil. Served with warm crushed peanut dipping sauce.</p>
        <span class="basil-tag">House Specialty</span>
      </div>

      <div class="basil-card basil-menu-item" data-category="starters">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#064e3b; font-size:1.2rem;">Chicken Satay Skewers (4pc)</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$10.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Grilled marinated chicken tenderloin skewers basted in turmeric and coconut milk. Served with roasted peanut sauce and fresh cucumber vinaigrette relish.</p>
        <span class="basil-tag">Grilled Classic</span>
      </div>

      <div class="basil-card basil-menu-item" data-category="starters">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#064e3b; font-size:1.2rem;">Crispy Fried Wontons (6pc)</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$8.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Crispy golden wonton pastry parcels packed with seasoned minced pork and scallions, served with sweet plum dipping sauce.</p>
        <span class="basil-tag">Crispy Starter</span>
      </div>

      <div class="basil-card basil-menu-item" data-category="starters">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#064e3b; font-size:1.2rem;">Tom Kha Coconut Soup</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">Cup $7.00 / Bowl $12.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Aromatic galangal and lemongrass infused coconut broth with sliced chicken breast, button mushrooms, kaffir lime leaves, and fresh lime juice.</p>
        <span class="basil-tag">Aromatic Soup</span>
      </div>

      <!-- Specialties -->
      <div class="basil-card basil-menu-item" data-category="specialties">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#064e3b; font-size:1.2rem;">Crispy Basil Duck</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$27.95</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Half roasted duck crisped to perfection, carved and sautéed with fresh garlic, Thai bird chilis, sweet onions, bell peppers, and fragrant holy basil leaves.</p>
        <span class="basil-tag">Chef's Signature</span>
      </div>

      <div class="basil-card basil-menu-item" data-category="specialties">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#064e3b; font-size:1.2rem;">Crispy Chilean Sea Bass</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$32.00</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Pan-seared Chilean sea bass filet over steamed bok choy and baby carrots, finished with a choice of sweet chili garlic reduction or ginger tamarind glaze.</p>
        <span class="basil-tag">Premium Seafood</span>
      </div>

      <div class="basil-card basil-menu-item" data-category="specialties">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#064e3b; font-size:1.2rem;">Grilled Lamb Lollipops</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$29.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Herb-crusted lamb chops flame-grilled to medium, resting over roasted asparagus and fingerling potatoes, dressed with aromatic massaman curry reduction.</p>
        <span class="basil-tag">Specialty Feature</span>
      </div>

      <!-- Curries -->
      <div class="basil-card basil-menu-item" data-category="curries">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#064e3b; font-size:1.2rem;">Masaman Curry</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$18.95</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Rich Southern Thai curry infused with cardamom, cinnamon, and cloves in coconut cream with tender Idaho potatoes, sweet onions, and roasted cashew nuts.</p>
        <span class="basil-tag">Rich &amp; Nutty</span>
      </div>

      <div class="basil-card basil-menu-item" data-category="curries">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#064e3b; font-size:1.2rem;">Panang Curry</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$18.95</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Thick, savory red curry paste simmered with coconut milk, green bell peppers, shredded kaffir lime leaves, and choice of chicken, beef, or tofu.</p>
        <span class="basil-tag">Creamy Spice</span>
      </div>

      <div class="basil-card basil-menu-item" data-category="curries">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#064e3b; font-size:1.2rem;">Green Coconut Curry</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$18.95</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Spicy green chili curry with crisp bamboo shoots, Thai eggplant, bell peppers, and fresh holy basil in silky coconut milk with jasmine rice.</p>
        <span class="basil-tag">Spicy &amp; Fresh</span>
      </div>

      <!-- Noodles & Rice -->
      <div class="basil-card basil-menu-item" data-category="noodles">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#064e3b; font-size:1.2rem;">Pad Thai</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$18.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Wok-seared thin rice noodles with farm egg, bean sprouts, crushed peanuts, scallions, and signature tamarind sauce. Choice of chicken, shrimp, beef, or tofu.</p>
        <span class="basil-tag">Bestseller</span>
      </div>

      <div class="basil-card basil-menu-item" data-category="noodles">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#064e3b; font-size:1.2rem;">Pad See Eu</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$18.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Wide rice noodles wok-charred with sweet dark soy sauce, fresh Chinese broccoli (gai lan), farm egg, and savory garlic white pepper sauce.</p>
        <span class="basil-tag">Wok Charred</span>
      </div>

      <div class="basil-card basil-menu-item" data-category="noodles">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#064e3b; font-size:1.2rem;">Drunken Noodles (Pad Kee Mao)</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$18.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Broad rice noodles stir-fried with hot Thai bird chilis, fresh basil leaves, tomatoes, sweet onions, and crisp red bell peppers.</p>
        <span class="basil-tag">Spicy Street Noodles</span>
      </div>

      <div class="basil-card basil-menu-item" data-category="noodles">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#064e3b; font-size:1.2rem;">Basil Fried Rice</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$17.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Fragrant jasmine rice wok-fried with fresh garlic, bird chilis, onions, bell peppers, egg, and holy basil leaves. Choice of protein.</p>
        <span class="basil-tag">Fragrant Rice</span>
      </div>

      <!-- Lunch Express -->
      <div class="basil-card basil-menu-item" data-category="lunch">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#064e3b; font-size:1.2rem;">Executive Lunch Pad Thai Set</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$14.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Express portion of classic chicken or tofu Pad Thai, served with one crispy spring roll and house ginger salad. Available Mon-Thu 11:30 AM - 2:00 PM.</p>
        <span class="basil-tag">Lunch Special</span>
      </div>

      <div class="basil-card basil-menu-item" data-category="lunch">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#064e3b; font-size:1.2rem;">Curry Express Combo Bento</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$15.50</span>
        </div>
        <p style="color:#475569; font-size:0.95rem; margin-bottom:12px;">Choice of Red, Green, or Masaman Curry with chicken or tofu, steamed jasmine rice, fried wonton, and ginger salad.</p>
        <span class="basil-tag">Lunch Special</span>
      </div>
    </div>

    <!-- Carryout CTA -->
    <div style="text-align:center; margin-top:50px; background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:30px; box-shadow:var(--basil-shadow);">
      <h3 style="color:#064e3b; font-size:1.5rem; margin-bottom:10px;">Carryout Orders &amp; Reservations</h3>
      <p style="color:#475569; max-width:600px; margin:0 auto 20px;">Contact our dining room directly to place pickup orders or coordinate table arrangements.</p>
      <a href="tel:7043327212" class="basil-btn-primary">Call (704) 332-7212</a>
    </div>
  </main>

{footer_html()}
"""

with open("basil-thai-cuisine/menu.html", "w", encoding="utf-8") as f:
    f.write(menu_content)
print("Written: basil-thai-cuisine/menu.html")

