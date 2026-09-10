# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("scripts")
from frenchquarter_builder import header_html, footer_html

# Page 1: index.html
index_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>French Quarter Restaurant | Uptown Charlotte Brevard Court Cajun &amp; Creole Pub</title>
  <meta name="description" content="Welcome to French Quarter Restaurant in Uptown Charlotte's historic Brevard Court. Authentic New Orleans Cajun gumbo, Creole specialties, famous salt &amp; pepper wings, and courtyard patio dining since 1986.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("index.html")}

  <section class="fq-hero">
    <div class="fq-container">
      <span class="fq-badge">Historic Brevard Court Landmark Since 1986</span>
      <h1 style="font-size:2.8rem; font-weight:900; margin:15px 0; letter-spacing:-0.02em;">New Orleans Soul in the Heart of Uptown Charlotte</h1>
      <p style="font-size:1.15rem; color:#e2e8f0; max-width:760px; margin:0 auto 25px;">
        For over 35 years, French Quarter Restaurant has welcomed Charlotte locals and visitors with genuine Southern Louisiana warmth, scratch-simmered Gumbo, legendary Salt &amp; Pepper wings, and sunlit courtyard dining.
      </p>
      <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
        <a href="menu.html" class="fq-btn-primary">Explore Full Menu</a>
        <a href="brevard-court-courtyard-dining.html" class="fq-btn-outline">Courtyard Patio</a>
        <a href="tel:7043771715" class="fq-btn-primary" style="background:#b91c1c; color:#fff;">Call (704) 377-1715</a>
      </div>
    </div>
  </section>

  <!-- Highlight Highlights Bar -->
  <section style="background-color:#ffffff; border-bottom:1px solid #e5e7eb; padding:28px 0;">
    <div class="fq-container">
      <div class="fq-grid-4" style="text-align:center;">
        <div>
          <h3 style="color:#2e1065; font-size:1.4rem; font-weight:800;">35+ Years</h3>
          <p style="color:#4b5563; font-size:0.9rem;">Uptown Charlotte Tradition</p>
        </div>
        <div>
          <h3 style="color:#2e1065; font-size:1.4rem; font-weight:800;">Scratch Kitchen</h3>
          <p style="color:#4b5563; font-size:0.9rem;">Louisiana Gumbo &amp; Creole</p>
        </div>
        <div>
          <h3 style="color:#2e1065; font-size:1.4rem; font-weight:800;">Famous Wings</h3>
          <p style="color:#4b5563; font-size:0.9rem;">Crispy Salt &amp; Pepper Style</p>
        </div>
        <div>
          <h3 style="color:#2e1065; font-size:1.4rem; font-weight:800;">Brevard Court</h3>
          <p style="color:#4b5563; font-size:0.9rem;">Open-Air Brick Courtyard</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Main Feature Section -->
  <main class="fq-container" style="padding:60px 24px;">
    <div class="fq-grid-2" style="align-items:center; margin-bottom:60px;">
      <div>
        <span class="fq-pill-tag">Authentic Louisiana Heritage</span>
        <h2 style="font-size:2.2rem; color:#1e0a45; margin:15px 0; font-weight:800;">Comfort Food Rooted in Tradition &amp; Community</h2>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:16px;">
          Tucked right at the Church Street archway into historic Brevard Court, French Quarter Restaurant delivers an unpretentious, high-flavor pub experience. We have been a steadfast gathering place for Uptown workers, neighborhood regulars, and sports crowds for decades.
        </p>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:20px;">
          From our dark roux Louisiana seafood and chicken gumbo to the spiced Cajun Chicken Alfredo, every recipe is crafted in-house to deliver unmistakable depth and generous portions.
        </p>
        <div style="display:flex; gap:12px; flex-wrap:wrap;">
          <a href="cajun-and-creole-specialties.html" class="fq-btn-primary">Learn About Our Cajun Menu</a>
          <a href="visit.html" class="fq-btn-outline" style="color:#2e1065; border-color:#2e1065;">Find Our Location</a>
        </div>
      </div>
      <div>
        <img src="images/cajun-gumbo-creole.jpg" alt="Rich homemade Louisiana Cajun Gumbo served at French Quarter Charlotte" style="width:100%; height:400px; object-fit:cover; border-radius:12px; box-shadow:var(--fq-shadow-lg);">
      </div>
    </div>

    <!-- Featured Specialties Grid -->
    <div style="text-align:center; margin-bottom:40px;">
      <span class="fq-pill-tag">Customer Favorites</span>
      <h2 style="font-size:2rem; color:#1e0a45; margin-top:10px;">Signature Offerings</h2>
    </div>

    <div class="fq-grid-3" style="margin-bottom:60px;">
      <div class="fq-feature-card">
        <img src="images/salt-pepper-wings.jpg" alt="Crispy Salt &amp; Pepper Chicken Wings" class="fq-feature-img">
        <div class="fq-feature-body">
          <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
            <h3 style="color:#1e0a45; font-size:1.25rem;">Salt &amp; Pepper Wings</h3>
            <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$15.95</span>
          </div>
          <p style="color:#4b5563; font-size:0.95rem; margin-bottom:16px;">Our iconic jumbo wings fried extra crisp and tossed in house salt and crushed pepper blend with sliced jalapenos and celery.</p>
          <span class="fq-pill-tag">Charlotte Legend</span>
        </div>
      </div>

      <div class="fq-feature-card">
        <img src="images/cajun-chicken-pasta.jpg" alt="Cajun Blackened Chicken Pasta" class="fq-feature-img">
        <div class="fq-feature-body">
          <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
            <h3 style="color:#1e0a45; font-size:1.25rem;">Cajun Chicken Pasta</h3>
            <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$17.50</span>
          </div>
          <p style="color:#4b5563; font-size:0.95rem; margin-bottom:16px;">Tender blackened chicken breast strips tossed with penne pasta in a spicy garlic Parmesan cream sauce with sweet bell peppers.</p>
          <span class="fq-pill-tag">House Favorite</span>
        </div>
      </div>

      <div class="fq-feature-card">
        <img src="images/monte-cristo-poboy.jpg" alt="Classic Monte Cristo Sandwich and Fresh Fries" class="fq-feature-img">
        <div class="fq-feature-body">
          <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
            <h3 style="color:#1e0a45; font-size:1.25rem;">The Monte Cristo</h3>
            <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$14.95</span>
          </div>
          <p style="color:#4b5563; font-size:0.95rem; margin-bottom:16px;">Sliced smoked ham, roast turkey, and Swiss cheese on thick French toast, griddled golden and dusted with powdered sugar with raspberry preserves.</p>
          <span class="fq-pill-tag">Lunch Classic</span>
        </div>
      </div>
    </div>

    <!-- Banner Callout -->
    <div class="fq-banner-strip">
      <span class="fq-badge" style="background:rgba(255,255,255,0.15); border-color:#ffffff; color:#ffffff;">Gameday Central</span>
      <h2 style="font-size:2rem; margin:12px 0 16px; color:#ffffff;">Heading to Bank of America Stadium or Truist Field?</h2>
      <p style="max-width:700px; margin:0 auto 24px; color:#e2e8f0; font-size:1.05rem;">
        French Quarter Restaurant is just a short 5-minute stroll from Charlotte's premier sports venues. Meet your crew on the patio for pre-game wings, cold pitchers, and tailgate platters.
      </p>
      <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
        <a href="gameday-tailgates-and-catering.html" class="fq-btn-primary">View Gameday Packages</a>
        <a href="tel:7043771715" class="fq-btn-outline">Call Pub: (704) 377-1715</a>
      </div>
    </div>
  </main>

{footer_html()}
"""

with open("french-quarter-restaurant/index.html", "w", encoding="utf-8") as f:
    f.write(index_content)
print("Written: french-quarter-restaurant/index.html")

# Page 2: menu.html
menu_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Full Food &amp; Drink Menu | French Quarter Restaurant Charlotte NC</title>
  <meta name="description" content="Explore the full menu at French Quarter Restaurant in Brevard Court Charlotte: authentic Cajun gumbo, Creole shrimp, salt &amp; pepper wings, sandwiches, and draft beer.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("menu.html")}

  <section class="fq-hero-compact">
    <div class="fq-container">
      <span class="fq-badge">Handcrafted Pub Kitchen</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Our Complete Food &amp; Drink Menu</h1>
      <p style="font-size:1.1rem; color:#cbd5e1; max-width:700px; margin:0 auto;">Authentic New Orleans comfort cuisine, hearty tavern subs, crisp salads, and chilled Carolina craft brews.</p>
    </div>
  </section>

  <main class="fq-container" style="padding:40px 24px 60px;">
    <!-- Interactive Filter Buttons -->
    <div class="fq-filters">
      <button class="fq-filter-btn active" data-filter="all">All Items</button>
      <button class="fq-filter-btn" data-filter="cajun">Cajun &amp; Creole</button>
      <button class="fq-filter-btn" data-filter="wings">Famous Wings</button>
      <button class="fq-filter-btn" data-filter="sandwiches">Po'Boys &amp; Sandwiches</button>
      <button class="fq-filter-btn" data-filter="entrees">Entrees &amp; Pasta</button>
      <button class="fq-filter-btn" data-filter="starters">Appetizers &amp; Sides</button>
    </div>

    <!-- Menu Grid -->
    <div class="fq-grid-3" id="menu-items-grid" style="gap:24px;">
      <!-- Cajun Items -->
      <div class="fq-card fq-menu-item" data-category="cajun">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#1e0a45; font-size:1.2rem;">Authentic Louisiana Gumbo</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">Cup $7.50 / Bowl $12.95</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Dark chocolate roux slow-simmered with smoked andouille sausage, pulled chicken, okra, holy trinity vegetables, and steamed long-grain white rice.</p>
        <span class="fq-pill-tag">Scratch Simmered</span>
      </div>

      <div class="fq-card fq-menu-item" data-category="cajun">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#1e0a45; font-size:1.2rem;">Shrimp &amp; Crawfish Creole</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$18.95</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Plump Gulf shrimp and sweet Louisiana crawfish tails simmered in a spiced piquant tomato-herb Creole reduction served over rice with warm French bread.</p>
        <span class="fq-pill-tag">New Orleans Classic</span>
      </div>

      <div class="fq-card fq-menu-item" data-category="cajun">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#1e0a45; font-size:1.2rem;">Red Beans &amp; Rice with Andouille</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$15.50</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Creamy simmered red kidney beans seasoned with smoked ham hocks and cajun spices, topped with grilled andouille sausage links and scallions.</p>
        <span class="fq-pill-tag">Comfort Heritage</span>
      </div>

      <!-- Wings Items -->
      <div class="fq-card fq-menu-item" data-category="wings">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#1e0a45; font-size:1.2rem;">Famous Salt &amp; Pepper Wings (10pc)</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$15.95</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Our renowned crispy chicken wings wok-tossed with coarse sea salt, black pepper, cracked red pepper flakes, and sauteed sliced jalapenos.</p>
        <span class="fq-pill-tag">Signature Recipe</span>
      </div>

      <div class="fq-card fq-menu-item" data-category="wings">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#1e0a45; font-size:1.2rem;">Cajun Dry Rub Wings (10pc)</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$15.95</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Crispy jumbo wings dusted in a savory blackened Cajun spice blend of paprika, garlic, thyme, and cayenne. Served with house ranch.</p>
        <span class="fq-pill-tag">Spicy Kick</span>
      </div>

      <div class="fq-card fq-menu-item" data-category="wings">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#1e0a45; font-size:1.2rem;">Bourbon BBQ Glazed Wings (10pc)</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$15.95</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Tossed in our sweet and smoky Kentucky bourbon molasses barbecue glaze, finished with toasted sesame seeds and fresh scallions.</p>
        <span class="fq-pill-tag">Sweet &amp; Smoky</span>
      </div>

      <!-- Sandwiches Items -->
      <div class="fq-card fq-menu-item" data-category="sandwiches">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#1e0a45; font-size:1.2rem;">The Monte Cristo</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$14.95</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Triple-decker layered with smoked ham, roasted turkey, and Swiss cheese on egg-battered French bread, grilled golden with raspberry dipping preserves.</p>
        <span class="fq-pill-tag">Customer Favorite</span>
      </div>

      <div class="fq-card fq-menu-item" data-category="sandwiches">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#1e0a45; font-size:1.2rem;">Blackened Shrimp Po'Boy</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$16.50</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Plump shrimp seared in cast iron with blackening seasoning, dressed with shredded lettuce, sliced tomatoes, pickles, and spicy remoulade on a Leidenheimer roll.</p>
        <span class="fq-pill-tag">New Orleans Sub</span>
      </div>

      <div class="fq-card fq-menu-item" data-category="sandwiches">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#1e0a45; font-size:1.2rem;">French Dip Au Jus</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$15.50</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Shaved prime roast beef piled high on a toasted French baguette with melted provolone cheese and piping hot house beef au jus for dipping.</p>
        <span class="fq-pill-tag">Pub Classic</span>
      </div>

      <div class="fq-card fq-menu-item" data-category="sandwiches">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#1e0a45; font-size:1.2rem;">Church Street Burger</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$14.50</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Half-pound Angus beef patty grilled to order on a toasted brioche bun with sharp cheddar cheese, crisp lettuce, tomato, onion, and pub secret spread.</p>
        <span class="fq-pill-tag">Angus Beef</span>
      </div>

      <!-- Entrees & Pasta Items -->
      <div class="fq-card fq-menu-item" data-category="entrees">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#1e0a45; font-size:1.2rem;">Cajun Chicken Pasta</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$17.50</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Pan-seared blackened chicken breast, sweet bell peppers, red onions, and penne pasta folded in our signature cajun spiced garlic Parmesan cream sauce.</p>
        <span class="fq-pill-tag">Bestselling Pasta</span>
      </div>

      <div class="fq-card fq-menu-item" data-category="entrees">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#1e0a45; font-size:1.2rem;">Blackened Catfish Filet</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$18.50</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Cast iron seared farm-raised catfish filet coated in Creole spices, served over yellow rice with seasoned green beans and fresh lemon caper butter.</p>
        <span class="fq-pill-tag">Southern Seafood</span>
      </div>

      <div class="fq-card fq-menu-item" data-category="entrees">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#1e0a45; font-size:1.2rem;">Marinated Beef Tips with Rice</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$17.95</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Tender sirloin steak tips marinated in garlic, soy, and herbs, sauteed with portobello mushrooms and onions, served over buttered rice.</p>
        <span class="fq-pill-tag">House Specialty</span>
      </div>

      <!-- Starters & Sides -->
      <div class="fq-card fq-menu-item" data-category="starters">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#1e0a45; font-size:1.2rem;">Crispy Fried Pickles</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$9.50</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Crinkle cut dill pickle chips tossed in seasoned cornmeal batter, fried golden and served with homemade spicy Cajun ranch dipping sauce.</p>
        <span class="fq-pill-tag">Pub Starter</span>
      </div>

      <div class="fq-card fq-menu-item" data-category="starters">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#1e0a45; font-size:1.2rem;">Loaded Pub Fries</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$10.95</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Crispy skin-on French fries smothered in melted Monterey Jack and cheddar cheeses, crisp bacon crumbles, jalapenos, and chopped scallions with sour cream.</p>
        <span class="fq-pill-tag">Sharing Plate</span>
      </div>

      <div class="fq-card fq-menu-item" data-category="starters">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
          <h3 style="color:#1e0a45; font-size:1.2rem;">Brevard House Salad</h3>
          <span style="font-weight:700; color:#d97706; font-size:1.1rem;">$8.95</span>
        </div>
        <p style="color:#4b5563; font-size:0.95rem; margin-bottom:12px;">Crisp mixed greens, grape tomatoes, English cucumbers, shredded carrots, garlic butter croutons, and your choice of house balsamic, ranch, or blue cheese.</p>
        <span class="fq-pill-tag">Fresh Greens</span>
      </div>
    </div>

    <!-- Takeout CTA -->
    <div style="text-align:center; margin-top:50px; background:#f3f4f6; border:1px solid #e5e7eb; border-radius:12px; padding:30px;">
      <h3 style="color:#1e0a45; font-size:1.5rem; margin-bottom:10px;">Ready to Place an Order for Pickup?</h3>
      <p style="color:#4b5563; max-width:600px; margin:0 auto 20px;">Give our kitchen counter a direct call for fast carryout preparation and curbside pickup near Brevard Court.</p>
      <a href="tel:7043771715" class="fq-btn-primary">Call (704) 377-1715</a>
    </div>
  </main>

{footer_html()}
"""

with open("french-quarter-restaurant/menu.html", "w", encoding="utf-8") as f:
    f.write(menu_content)
print("Written: french-quarter-restaurant/menu.html")

