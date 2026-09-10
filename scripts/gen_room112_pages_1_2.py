# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\scripts")
from room112_builder import header_html, footer_html

DIR = r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\room-112"

# 1. index.html
index_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Room 112 | Modern Asian Bistro &amp; Boutique Sushi Lounge Charlotte</title>
  <meta name="description" content="Chic modern Asian bistro and boutique sushi lounge at 112 S Tryon St in Uptown Charlotte. Signature maki, honey walnut prawns, crispy tangerine beef, and corporate platters.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
{header_html("index.html")}

  <section class="room112-hero">
    <div class="room112-hero-inner">
      <span class="room112-hero-pill">Uptown South Tryon Boutique Dining</span>
      <h1>Modern Asian Bistro &amp; Boutique Sushi Lounge</h1>
      <p>Step into Uptown Charlotte’s most intimate Asian culinary escape. From our celebrated Cherry Blossom and Upper Manhattan sushi rolls to crispy tangerine beef, honey glazed walnut prawns, and stylish evening craft cocktails.</p>
      <div class="room112-hero-actions">
        <a href="menu.html" class="room112-btn-hero-primary">Explore Full Menu</a>
        <a href="signature-rolls-and-sashimi-lounge.html" class="room112-btn-hero-secondary">Signature Sushi</a>
        <a href="sushi-platters-and-executive-dining.html" class="room112-btn-hero-secondary">Executive Platters</a>
      </div>
    </div>
  </section>

  <main class="room112-container">
    <div class="room112-section-title">
      <h2>Contemporary Flavors in an Intimate Setting</h2>
      <p>A curated menu that balances artistic raw bar innovation with bold, high-heat Chinese wok craftsmanship.</p>
    </div>

    <div class="room112-grid-3">
      <div class="room112-card">
        <img src="images/cherry-blossom-roll.jpg" alt="Artistic Cherry Blossom sushi roll with salmon roses and avocado" class="room112-card-image">
        <div class="room112-card-body">
          <span class="room112-card-badge">Signature Masterpiece</span>
          <h3>The Cherry Blossom Roll</h3>
          <p>Spicy yellowfin tuna, lump crabmeat, and avocado wrapped inside, adorned with handcrafted Scottish salmon rosettes, micro cilantro, and sweet yuzu glaze.</p>
          <div class="room112-card-footer">
            <span class="room112-price">$16.50</span>
            <a href="signature-rolls-and-sashimi-lounge.html" class="room112-btn-cta">See Rolls</a>
          </div>
        </div>
      </div>

      <div class="room112-card">
        <img src="images/walnut-prawns-wok.jpg" alt="Honey glazed walnut jumbo prawns with broccoli crowns" class="room112-card-image">
        <div class="room112-card-body">
          <span class="room112-card-badge">Bistro Classic</span>
          <h3>Honey Glazed Walnut Prawns</h3>
          <p>Crispy tempura-crusted jumbo prawns tossed in a silky, sweet honey cream reduction, garnished with candied caramelized walnuts and steamed broccoli.</p>
          <div class="room112-card-footer">
            <span class="room112-price">$19.99</span>
            <a href="modern-asian-bistro-and-wok.html" class="room112-btn-cta">Explore Wok</a>
          </div>
        </div>
      </div>

      <div class="room112-card">
        <img src="images/executive-sushi-sampler.jpg" alt="112 Deluxe Sushi Sampler platter with nigiri and sashimi" class="room112-card-image">
        <div class="room112-card-body">
          <span class="room112-card-badge">Raw Bar Sampler</span>
          <h3>112 Deluxe Sushi Sampler</h3>
          <p>A full Dragon Roll paired with 6 pieces of chef-selected nigiri and 8 pieces of pristine sashimi (salmon, tuna, yellowtail, and white fish).</p>
          <div class="room112-card-footer">
            <span class="room112-price">$38.00</span>
            <a href="sushi-platters-and-executive-dining.html" class="room112-btn-cta">View Samplers</a>
          </div>
        </div>
      </div>
    </div>

    <!-- Spotlight Section -->
    <div class="room112-spotlight">
      <div>
        <img src="images/dim-sum-starters.jpg" alt="Steamed pork dumplings and crispy crab wontons" class="room112-card-image" style="height:100%; object-fit:cover;">
      </div>
      <div class="room112-spotlight-content">
        <span class="room112-card-badge">Uptown Lunch &amp; Evening Lounge</span>
        <h3>Boutique Energy on South Tryon</h3>
        <p>Whether you're stopping by for a brisk corporate power lunch, meeting colleagues for an after-work signature cocktail, or enjoying an intimate date night before a show at the Belk Theater, Room 112 offers an atmosphere that is both cosmopolitan and deeply welcoming.</p>
        <p>Enjoy our extensive selection of dim sum starters, crispy rock shrimp tempura, wok-charred noodles, and premium Japanese sakes.</p>
        <div style="margin-top:20px;">
          <a href="menu.html" class="room112-btn-cta">View Full Bistro Menu</a>
        </div>
      </div>
    </div>

    <!-- Highlights -->
    <div class="room112-section-title" style="margin-top:60px;">
      <h2>The Room 112 Philosophy</h2>
      <p>Precision, hospitality, and contemporary Asian design.</p>
    </div>

    <div class="room112-grid-3">
      <div class="room112-card" style="padding:28px;">
        <h4 style="color:var(--room112-primary); margin-bottom:12px; font-size:1.25rem;">Heart of Uptown</h4>
        <p style="color:var(--room112-text-muted); font-size:0.95rem;">Situated right at 112 S Tryon St next to Trade &amp; Tryon square, accessible easily from the Overstreet Mall and Uptown light rail stations.</p>
      </div>
      <div class="room112-card" style="padding:28px;">
        <h4 style="color:var(--room112-primary); margin-bottom:12px; font-size:1.25rem;">Artisanal Knife Craft</h4>
        <p style="color:var(--room112-text-muted); font-size:0.95rem;">Our sushi chefs slice pristine sashimi daily, balancing delicate fish with house-simmered sauces, torched unagi, and crisp tempura elements.</p>
      </div>
      <div class="room112-card" style="padding:28px;">
        <h4 style="color:var(--room112-primary); margin-bottom:12px; font-size:1.25rem;">Executive Corporate Trays</h4>
        <p style="color:var(--room112-text-muted); font-size:0.95rem;">Impress your business partners with customized 36-piece and 50-piece sushi banquet platters delivered promptly to your Uptown office.</p>
      </div>
    </div>

    <!-- CTA Section -->
    <div class="room112-cta-banner" style="margin-top:50px;">
      <h2>Join Us at Room 112 Today</h2>
      <p>Order takeout for fast pickup or reserve a table for evening dining at 112 S Tryon St.</p>
      <div class="room112-cta-btns">
        <a href="tel:7043357112" class="room112-btn-hero-primary">Call (704) 335-7112</a>
        <a href="visit.html" class="room112-btn-hero-secondary">View Hours &amp; Location</a>
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
  <title>Full Asian Bistro &amp; Sushi Menu | Room 112 Charlotte</title>
  <meta name="description" content="Explore the full menu at Room 112 in Uptown Charlotte: signature maki rolls, sashimi, honey walnut prawns, crispy tangerine beef, wok noodles, and dim sum.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
{header_html("menu.html")}

  <section class="room112-hero" style="padding: 50px 20px;">
    <div class="room112-hero-inner">
      <span class="room112-hero-pill">Uptown South Tryon Bistro</span>
      <h1>Full Asian Bistro &amp; Sushi Menu</h1>
      <p>Discover our creative specialty rolls, sashimi-grade raw bar, elevated wok classics, handmade dumplings, and craft beverages.</p>
    </div>
  </section>

  <main class="room112-container">
    <div class="room112-tabs">
      <button class="room112-tab-btn active" data-target="tab-specialty-maki">Signature Maki</button>
      <button class="room112-tab-btn" data-target="tab-bistro-wok">Modern Asian Wok</button>
      <button class="room112-tab-btn" data-target="tab-samplers">Sushi Samplers &amp; Nigiri</button>
      <button class="room112-tab-btn" data-target="tab-noodles">Noodles &amp; Fried Rice</button>
      <button class="room112-tab-btn" data-target="tab-dimsum">Dim Sum &amp; Cocktails</button>
    </div>

    <!-- Group 1: Signature Maki -->
    <div class="room112-menu-group active" id="tab-specialty-maki">
      <div class="room112-section-title">
        <h2>Chef’s Signature Specialty Maki</h2>
        <p>Inventive 8-piece boutique rolls featuring multi-layered textures and artisanal reductions.</p>
      </div>

      <div class="room112-grid-2">
        <div class="room112-menu-item">
          <div class="room112-item-header">
            <h4>Cherry Blossom Roll</h4>
            <span class="room112-item-price">$16.50</span>
          </div>
          <p class="room112-item-desc">Spicy tuna, real crab salad, and avocado wrapped inside, crowned with Scottish salmon rosettes, unagi glaze, and microgreens.</p>
          <div class="room112-item-tags">
            <span class="room112-tag room112-tag-raw">Raw</span>
            <span class="room112-tag room112-tag-signature">Signature Favorite</span>
          </div>
        </div>

        <div class="room112-menu-item">
          <div class="room112-item-header">
            <h4>Upper Manhattan Roll</h4>
            <span class="room112-item-price">$16.99</span>
          </div>
          <p class="room112-item-desc">Tempura soft-shell crab, spicy tuna, and asparagus topped with seared yellowtail, black caviar, and truffle ponzu.</p>
          <div class="room112-item-tags">
            <span class="room112-tag room112-tag-raw">Raw</span>
          </div>
        </div>

        <div class="room112-menu-item">
          <div class="room112-item-header">
            <h4>Pink Floyd Roll</h4>
            <span class="room112-item-price">$15.50</span>
          </div>
          <p class="room112-item-desc">Smoked salmon, cream cheese, and jalapeno rolled in pink soy paper, topped with spicy tuna crunch and sweet raspberry drizzle.</p>
          <div class="room112-item-tags">
            <span class="room112-tag room112-tag-raw">Raw</span>
            <span class="room112-tag room112-tag-spicy">Mild Heat</span>
          </div>
        </div>

        <div class="room112-menu-item">
          <div class="room112-item-header">
            <h4>Sapporo Roll</h4>
            <span class="room112-item-price">$15.99</span>
          </div>
          <p class="room112-item-desc">Tempura shrimp and cucumber draped with fresh yellowfin tuna, ripe avocado, spicy mayo, and toasted sesame crunchies.</p>
        </div>

        <div class="room112-menu-item">
          <div class="room112-item-header">
            <h4>Salmon Dream Roll</h4>
            <span class="room112-item-price">$16.00</span>
          </div>
          <p class="room112-item-desc">Fresh salmon and avocado inside, topped with torched salmon belly, spicy aioli, masago, and crispy shallots.</p>
          <div class="room112-item-tags">
            <span class="room112-tag room112-tag-raw">Raw</span>
          </div>
        </div>

        <div class="room112-menu-item">
          <div class="room112-item-header">
            <h4>Dragon Roll</h4>
            <span class="room112-item-price">$14.50</span>
          </div>
          <p class="room112-item-desc">Tempura shrimp core draped with grilled BBQ eel, avocado, and sweet kabayaki reduction.</p>
        </div>
      </div>
    </div>

    <!-- Group 2: Modern Asian Wok -->
    <div class="room112-menu-group" id="tab-bistro-wok">
      <div class="room112-section-title">
        <h2>Modern Asian Bistro Entrees</h2>
        <p>Wok-seared with fresh produce and artisanal reductions. Served with steamed jasmine or brown rice.</p>
      </div>

      <div class="room112-grid-2">
        <div class="room112-menu-item">
          <div class="room112-item-header">
            <h4>Honey Glazed Walnut Prawns</h4>
            <span class="room112-item-price">$19.99</span>
          </div>
          <p class="room112-item-desc">Jumbo tempura prawns tossed in sweet honey cream reduction, served with caramelized candied walnuts and broccoli.</p>
          <div class="room112-item-tags">
            <span class="room112-tag room112-tag-signature">House Specialty</span>
          </div>
        </div>

        <div class="room112-menu-item">
          <div class="room112-item-header">
            <h4>Crispy Tangerine Beef</h4>
            <span class="room112-item-price">$18.50</span>
          </div>
          <p class="room112-item-desc">Thin slices of flank steak flash-fried to a crisp, tossed in a sun-dried tangerine peel chili glaze with sweet peppers.</p>
          <div class="room112-item-tags">
            <span class="room112-tag room112-tag-spicy">Spicy</span>
          </div>
        </div>

        <div class="room112-menu-item">
          <div class="room112-item-header">
            <h4>Peking Style Roast Duck Breast</h4>
            <span class="room112-item-price">$22.00</span>
          </div>
          <p class="room112-item-desc">Crisp-skinned sliced roast duck breast served with sweet hoisin plum reduction, scallions, and steamed lotus buns.</p>
        </div>

        <div class="room112-menu-item">
          <div class="room112-item-header">
            <h4>Room 112 General Tso’s Chicken</h4>
            <span class="room112-item-price">$15.50</span>
          </div>
          <p class="room112-item-desc">Tender chicken breast morsels tossed in a tangy ginger garlic chili sauce with broccoli crowns.</p>
        </div>
      </div>
    </div>

    <!-- Group 3: Samplers & Nigiri -->
    <div class="room112-menu-group" id="tab-samplers">
      <div class="room112-section-title">
        <h2>Sushi Samplers &amp; Raw Bar Cuts</h2>
        <p>Composed raw bar platters and a la carte Nigiri / Sashimi (2 pieces per order).</p>
      </div>

      <div class="room112-grid-2">
        <div class="room112-menu-item">
          <div class="room112-item-header">
            <h4>112 Deluxe Sushi Sampler</h4>
            <span class="room112-item-price">$38.00</span>
          </div>
          <p class="room112-item-desc">Includes 1 Dragon Roll, 6 pieces of chef-selected nigiri, and 8 pieces of pristine sashimi with miso soup and salad.</p>
          <div class="room112-item-tags">
            <span class="room112-tag room112-tag-signature">Chef Choice</span>
          </div>
        </div>

        <div class="room112-menu-item">
          <div class="room112-item-header">
            <h4>Sushi Lover For 2</h4>
            <span class="room112-item-price">$62.00</span>
          </div>
          <p class="room112-item-desc">Includes 1 California Roll, 1 Rainbow Roll, 1 Cherry Blossom Roll, 8 pieces of nigiri, and 9 pieces of sashimi.</p>
        </div>

        <div class="room112-menu-item">
          <div class="room112-item-header">
            <h4>House Sushi Sampler</h4>
            <span class="room112-item-price">$24.00</span>
          </div>
          <p class="room112-item-desc">1 California Roll paired with 8 pieces of chef’s assorted daily nigiri.</p>
        </div>

        <div class="room112-menu-item">
          <div class="room112-item-header">
            <h4>Yellowfin Tuna (Maguro) Nigiri / Sashimi</h4>
            <span class="room112-item-price">$6.50</span>
          </div>
          <p class="room112-item-desc">Two cuts of sashimi-grade yellowfin tuna.</p>
        </div>

        <div class="room112-menu-item">
          <div class="room112-item-header">
            <h4>Scottish Salmon (Sake) Nigiri / Sashimi</h4>
            <span class="room112-item-price">$6.00</span>
          </div>
          <p class="room112-item-desc">Two cuts of fresh buttery Atlantic salmon.</p>
        </div>

        <div class="room112-menu-item">
          <div class="room112-item-header">
            <h4>Japanese Yellowtail (Hamachi)</h4>
            <span class="room112-item-price">$7.00</span>
          </div>
          <p class="room112-item-desc">Two slices of sweet, rich hamachi yellowtail.</p>
        </div>
      </div>
    </div>

    <!-- Group 4: Noodles & Rice -->
    <div class="room112-menu-group" id="tab-noodles">
      <div class="room112-section-title">
        <h2>Wok Noodles &amp; Specialty Fried Rice</h2>
        <p>Comforting wok-tossed noodles and signature fried rice dishes.</p>
      </div>

      <div class="room112-grid-2">
        <div class="room112-menu-item">
          <div class="room112-item-header">
            <h4>Singapore Street Rice Noodles</h4>
            <span class="room112-item-price">$15.50</span>
          </div>
          <p class="room112-item-desc">Thin vermicelli rice noodles wok-charred with yellow curry, shrimp, chicken, egg, bell peppers, and bean sprouts.</p>
          <div class="room112-item-tags">
            <span class="room112-tag room112-tag-spicy">Curry Spiced</span>
          </div>
        </div>

        <div class="room112-menu-item">
          <div class="room112-item-header">
            <h4>Roast Duck Fried Rice</h4>
            <span class="room112-item-price">$16.50</span>
          </div>
          <p class="room112-item-desc">Jasmine rice wok-tossed with shredded roast duck, eggs, scallions, sweet onions, and light soy seasoning.</p>
        </div>

        <div class="room112-menu-item">
          <div class="room112-item-header">
            <h4>Room 112 House Lo Mein</h4>
            <span class="room112-item-price">$14.50</span>
          </div>
          <p class="room112-item-desc">Egg wheat noodles stir-fried with chicken, beef, shrimp, and fresh julienned vegetables.</p>
        </div>

        <div class="room112-menu-item">
          <div class="room112-item-header">
            <h4>Classic Pad Thai</h4>
            <span class="room112-item-price">$14.99</span>
          </div>
          <p class="room112-item-desc">Rice noodles stir-fried in tamarind sauce with shrimp, egg, bean sprouts, lime, and crushed peanuts.</p>
        </div>
      </div>
    </div>

    <!-- Group 5: Dim Sum & Drinks -->
    <div class="room112-menu-group" id="tab-dimsum">
      <div class="room112-section-title">
        <h2>Dim Sum Starters &amp; Craft Cocktails</h2>
        <p>Small plates to share and signature boutique drinks.</p>
      </div>

      <div class="room112-grid-2">
        <div class="room112-menu-item">
          <div class="room112-item-header">
            <h4>Crispy Crab Wontons (6 pcs)</h4>
            <span class="room112-item-price">$7.50</span>
          </div>
          <p class="room112-item-desc">Handmade crispy wontons filled with cream cheese, crabmeat, and scallions. Served with sweet chili plum sauce.</p>
        </div>

        <div class="room112-menu-item">
          <div class="room112-item-header">
            <h4>Steamed or Pan-Fried Pork Dumplings (6 pcs)</h4>
            <span class="room112-item-price">$7.99</span>
          </div>
          <p class="room112-item-desc">Minced pork and chive potstickers with ginger-soy dipping sauce.</p>
        </div>

        <div class="room112-menu-item">
          <div class="room112-item-header">
            <h4>Rock Shrimp Tempura</h4>
            <span class="room112-item-price">$11.50</span>
          </div>
          <p class="room112-item-desc">Crispy rock shrimp tossed in spicy creamy aioli over baby greens.</p>
        </div>

        <div class="room112-menu-item">
          <div class="room112-item-header">
            <h4>Room 112 Orchid Cocktail</h4>
            <span class="room112-item-price">$13.00</span>
          </div>
          <p class="room112-item-desc">Vodka, elderflower liqueur, fresh lychee juice, and a float of sparkling prosecco with an edible orchid blossom.</p>
        </div>
      </div>
    </div>

    <!-- Bottom Order CTA -->
    <div class="room112-cta-banner" style="margin-top:50px;">
      <h2>Ready for Modern Asian Dining?</h2>
      <p>Call our South Tryon host team for takeout orders, lunch pickups, and evening dinner reservations.</p>
      <div class="room112-cta-btns">
        <a href="tel:7043357112" class="room112-btn-hero-primary">Call (704) 335-7112</a>
        <a href="sushi-platters-and-executive-dining.html" class="room112-btn-hero-secondary">View Catering Platters</a>
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
