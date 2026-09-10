# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\scripts")
from redginger_builder import header_html, footer_html

DIR = r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\red-ginger"

# 1. index.html
index_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Red Ginger | Japanese Steakhouse &amp; Sushi Lounge Uptown Charlotte</title>
  <meta name="description" content="Experience table-side teppanyaki, prime filet mignon, cold-water lobster tails, and artisanal sushi on South Tryon Street in Uptown Charlotte NC.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
{header_html("index.html")}

  <section class="redginger-hero">
    <div class="redginger-hero-inner">
      <span class="redginger-hero-pill">Uptown South Tryon Culinary Landmark</span>
      <h1>Table-Side Teppanyaki &amp; Artisan Sushi Lounge</h1>
      <p>Immerse yourself in Uptown Charlotte’s premier Japanese dining destination. Sizzling prime filet mignon, butterflied cold-water lobster tails, flaming onion volcanoes, innovative sushi creations, and executive weekday bento boxes.</p>
      <div class="redginger-hero-actions">
        <a href="menu.html" class="redginger-btn-hero-primary">Explore Full Menu</a>
        <a href="teppanyaki-hibachi-experience.html" class="redginger-btn-hero-secondary">The Teppanyaki Show</a>
        <a href="private-dining-and-group-events.html" class="redginger-btn-hero-secondary">Private Events &amp; VIP</a>
      </div>
    </div>
  </section>

  <main class="redginger-container">
    <div class="redginger-section-title">
      <h2>Culinary Artistry Across Every Table</h2>
      <p>From theatrical high-heat teppan grills to refined sushi master craftsmanship, discover our signature dining dimensions.</p>
    </div>

    <div class="redginger-grid-3">
      <div class="redginger-card">
        <img src="images/teppanyaki-steak-lobster.jpg" alt="Sizzling Filet Mignon and Lobster Tail on teppanyaki hibachi grill" class="redginger-card-image">
        <div class="redginger-card-body">
          <span class="redginger-card-badge">Steakhouse Masterpiece</span>
          <h3>Imperial Filet Mignon &amp; Lobster</h3>
          <p>Tender center-cut USDA Choice Filet Mignon and succulent cold-water lobster tail seared table-side with clarified garlic butter, served with hibachi noodles, fried rice, and house sauces.</p>
          <div class="redginger-card-footer">
            <span class="redginger-price">$46.00</span>
            <a href="teppanyaki-hibachi-experience.html" class="redginger-btn-cta">See Hibachi</a>
          </div>
        </div>
      </div>

      <div class="redginger-card">
        <img src="images/specialty-sushi-lounge.jpg" alt="Artisanal specialty sushi roll platter with tuna and salmon" class="redginger-card-image">
        <div class="redginger-card-body">
          <span class="redginger-card-badge">Raw Bar Innovation</span>
          <h3>The Red Ginger &amp; Tryon Rolls</h3>
          <p>Signature maki rolls featuring spicy bluefin tuna, seared salmon, king crab, avocado, and tobiko, drizzled with chef’s house unagi reduction and spicy truffle aioli.</p>
          <div class="redginger-card-footer">
            <span class="redginger-price">$17.50</span>
            <a href="sushi-bar-and-omakase-craft.html" class="redginger-btn-cta">Explore Sushi</a>
          </div>
        </div>
      </div>

      <div class="redginger-card">
        <img src="images/yellowtail-tartar.jpg" alt="Yellowtail Jalapeno sashimi appetizer with yuzu ponzu" class="redginger-card-image">
        <div class="redginger-card-body">
          <span class="redginger-card-badge">Izakaya Starter</span>
          <h3>Yellowtail Jalapeno with Yuzu</h3>
          <p>Thinly sliced Japanese hamachi sashimi accented with fresh serrano jalapeno rounds, micro cilantro, and white truffle yuzu ponzu vinaigrette.</p>
          <div class="redginger-card-footer">
            <span class="redginger-price">$15.50</span>
            <a href="menu.html" class="redginger-btn-cta">View Starters</a>
          </div>
        </div>
      </div>
    </div>

    <!-- Spotlight Section -->
    <div class="redginger-spotlight">
      <div>
        <img src="images/private-dining-lounge.jpg" alt="Elegant private dining room at Red Ginger Uptown Charlotte" class="redginger-card-image" style="height:100%; object-fit:cover;">
      </div>
      <div class="redginger-spotlight-content">
        <span class="redginger-card-badge">Corporate &amp; Celebratory Dining</span>
        <h3>Uptown Private Events &amp; Boardroom Dinners</h3>
        <p>Located on South Tryon Street adjacent to the Levine Center for the Arts and Two Wells Fargo Center, Red Ginger provides the quintessential backdrop for celebratory corporate dinners, convention gatherings, client entertainment, and birthdays.</p>
        <p>Choose between semi-private teppanyaki chef tables, dedicated cocktail lounge receptions, or customized multi-course tasting menus paired with artisanal Japanese sake and fine wines.</p>
        <div style="margin-top:20px;">
          <a href="private-dining-and-group-events.html" class="redginger-btn-cta">Plan Your Event</a>
        </div>
      </div>
    </div>

    <!-- Highlights -->
    <div class="redginger-section-title" style="margin-top:60px;">
      <h2>The Red Ginger Distinction</h2>
      <p>Excellence in ingredients, presentation, and hospitality.</p>
    </div>

    <div class="redginger-grid-3">
      <div class="redginger-card" style="padding:28px;">
        <h4 style="color:var(--redginger-primary-dark); margin-bottom:12px; font-size:1.25rem;">Table-Side Theatrics</h4>
        <p style="color:var(--redginger-text-muted); font-size:0.95rem;">Our certified master teppanyaki chefs dazzle guests of all ages with razor-sharp knife juggling, soaring onion volcanoes, and fiery grill performances.</p>
      </div>
      <div class="redginger-card" style="padding:28px;">
        <h4 style="color:var(--redginger-primary-dark); margin-bottom:12px; font-size:1.25rem;">Power Lunch Bento Boxes</h4>
        <p style="color:var(--redginger-text-muted); font-size:0.95rem;">Designed for Uptown executives on a tight schedule: complete multi-compartment bento meals featuring steak, chicken teriyaki, tempura, and California rolls served promptly.</p>
      </div>
      <div class="redginger-card" style="padding:28px;">
        <h4 style="color:var(--redginger-primary-dark); margin-bottom:12px; font-size:1.25rem;">Craft Cocktails &amp; Sake</h4>
        <p style="color:var(--redginger-text-muted); font-size:0.95rem;">Complement your dinner with curated Junmai Daiginjo sakes, Japanese whiskies, smoked lychee martinis, and ginger-infused signature craft cocktails.</p>
      </div>
    </div>

    <!-- CTA Section -->
    <div class="redginger-cta-banner" style="margin-top:50px;">
      <h2>Reserve Your Table on South Tryon Today</h2>
      <p>Experience the excitement of live teppanyaki or relax in our refined sushi lounge at 401 S Tryon St.</p>
      <div class="redginger-cta-btns">
        <a href="tel:9808198837" class="redginger-btn-hero-primary">Call (980) 819-8837</a>
        <a href="visit.html" class="redginger-btn-hero-secondary">View Hours &amp; Location</a>
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
  <title>Full Steakhouse &amp; Sushi Menu | Red Ginger Charlotte</title>
  <meta name="description" content="Explore the full menu of table-side hibachi teppanyaki, chef specialty sushi rolls, sashimi cuts, and weekday lunch bento boxes at Red Ginger in Uptown Charlotte.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
{header_html("menu.html")}

  <section class="redginger-hero" style="padding: 50px 20px;">
    <div class="redginger-hero-inner">
      <span class="redginger-hero-pill">Uptown South Tryon Dining</span>
      <h1>Full Steakhouse &amp; Sushi Menu</h1>
      <p>From table-side teppanyaki dinners and chef signature rolls to executive lunch bento boxes and izakaya small plates.</p>
    </div>
  </section>

  <main class="redginger-container">
    <div class="redginger-tabs">
      <button class="redginger-tab-btn active" data-target="tab-teppanyaki">Teppanyaki Hibachi</button>
      <button class="redginger-tab-btn" data-target="tab-specialty-sushi">Specialty Sushi Rolls</button>
      <button class="redginger-tab-btn" data-target="tab-raw-bar">Raw Bar &amp; Sashimi</button>
      <button class="redginger-tab-btn" data-target="tab-bento">Lunch Bento Boxes</button>
      <button class="redginger-tab-btn" data-target="tab-izakaya">Starters &amp; Kitchen</button>
    </div>

    <!-- Group 1: Teppanyaki -->
    <div class="redginger-menu-group active" id="tab-teppanyaki">
      <div class="redginger-section-title">
        <h2>Table-Side Teppanyaki Hibachi Dinners</h2>
        <p>All dinners include Japanese Onion Soup, House Ginger Salad, Hibachi Vegetables, Seasoned Fried Rice, Noodles, and Signature Ginger &amp; Yum Yum Sauces.</p>
      </div>

      <div class="redginger-grid-2">
        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Center-Cut Filet Mignon (8 oz)</h4>
            <span class="redginger-item-price">$36.00</span>
          </div>
          <p class="redginger-item-desc">Tender center-cut beef tenderloin grilled to your exact specification with house clarified garlic butter and soy glaze.</p>
          <div class="redginger-item-tags">
            <span class="redginger-tag redginger-tag-prime">Prime Cut</span>
          </div>
        </div>

        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>New York Angus Strip Steak (10 oz)</h4>
            <span class="redginger-item-price">$31.00</span>
          </div>
          <p class="redginger-item-desc">Well-marbled Angus strip steak seared on the high-heat teppan grill with garlic butter and button mushrooms.</p>
        </div>

        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Twin Cold-Water Lobster Tails</h4>
            <span class="redginger-item-price">$44.00</span>
          </div>
          <p class="redginger-item-desc">Two succulent cold-water lobster tails butterflied and seared with lemon herb garlic butter on the flaming comal.</p>
          <div class="redginger-item-tags">
            <span class="redginger-tag redginger-tag-signature">Signature Seafood</span>
          </div>
        </div>

        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Colossal Sea Scallops</h4>
            <span class="redginger-item-price">$34.00</span>
          </div>
          <p class="redginger-item-desc">Jumbo wild sea scallops seared until caramelized golden brown on the outside and tender inside.</p>
        </div>

        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Land &amp; Sea Combo (Filet Mignon &amp; Lobster)</h4>
            <span class="redginger-item-price">$46.00</span>
          </div>
          <p class="redginger-item-desc">The ultimate steakhouse luxury: center-cut filet mignon paired with a whole butterflied cold-water lobster tail.</p>
          <div class="redginger-item-tags">
            <span class="redginger-tag redginger-tag-signature">House Favorite</span>
          </div>
        </div>

        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Hibachi Chicken &amp; Tiger Shrimp</h4>
            <span class="redginger-item-price">$29.00</span>
          </div>
          <p class="redginger-item-desc">Tender chicken breast paired with wild jumbo tiger shrimp, seared with fresh lemon and garlic teriyaki.</p>
        </div>
      </div>
    </div>

    <!-- Group 2: Specialty Sushi -->
    <div class="redginger-menu-group" id="tab-specialty-sushi">
      <div class="redginger-section-title">
        <h2>Chef’s Signature Specialty Rolls</h2>
        <p>Hand-rolled with sashimi-grade fish, seasonal microgreens, and artisanal reductions.</p>
      </div>

      <div class="redginger-grid-2">
        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Red Ginger Signature Roll</h4>
            <span class="redginger-item-price">$17.50</span>
          </div>
          <p class="redginger-item-desc">Spicy bluefin tuna and avocado wrapped inside, topped with fresh Scottish salmon, sliced pickled red ginger, unagi sauce, and microgreens.</p>
          <div class="redginger-item-tags">
            <span class="redginger-tag redginger-tag-raw">Raw</span>
            <span class="redginger-tag redginger-tag-signature">House Roll</span>
          </div>
        </div>

        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Tryon Street Roll</h4>
            <span class="redginger-item-price">$16.50</span>
          </div>
          <p class="redginger-item-desc">Tempura shrimp and cream cheese topped with spicy crab salad, sliced avocado, toasted sesame, and sweet kabayaki reduction.</p>
        </div>

        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Uptown Queen Roll</h4>
            <span class="redginger-item-price">$18.00</span>
          </div>
          <p class="redginger-item-desc">Real Alaskan king crab and asparagus inside, crowned with seared A5 Wagyu beef slices, black truffle oil, and scallions.</p>
          <div class="redginger-item-tags">
            <span class="redginger-tag redginger-tag-prime">Luxury Selection</span>
          </div>
        </div>

        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Fire Dragon Roll (Torched)</h4>
            <span class="redginger-item-price">$16.99</span>
          </div>
          <p class="redginger-item-desc">Spicy salmon and cucumber inside, draped with BBQ eel, avocado, spicy aioli, and torched sweet unagi glaze.</p>
        </div>

        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Sexy Jalapeno Roll</h4>
            <span class="redginger-item-price">$16.50</span>
          </div>
          <p class="redginger-item-desc">Yellowtail, spicy tuna, and cilantro inside, topped with white tuna (escolar), fresh jalapeno slices, and yuzu sauce.</p>
          <div class="redginger-item-tags">
            <span class="redginger-tag redginger-tag-raw">Raw</span>
          </div>
        </div>

        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Rainbow Supreme Roll</h4>
            <span class="redginger-item-price">$16.00</span>
          </div>
          <p class="redginger-item-desc">California roll draped with five fresh cuts of tuna, salmon, yellowtail, striped bass, and avocado.</p>
        </div>
      </div>
    </div>

    <!-- Group 3: Raw Bar & Sashimi -->
    <div class="redginger-menu-group" id="tab-raw-bar">
      <div class="redginger-section-title">
        <h2>Pristine Raw Bar &amp; Sashimi Cuts</h2>
        <p>A la carte Nigiri / Sashimi (2 pieces per order) and composed raw starters.</p>
      </div>

      <div class="redginger-grid-2">
        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Yellowtail Jalapeno Carpaccio</h4>
            <span class="redginger-item-price">$15.50</span>
          </div>
          <p class="redginger-item-desc">Six delicate slices of Japanese hamachi sashimi with fresh serrano chili, white truffle oil, and yuzu soy.</p>
        </div>

        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Spicy Tuna Tartar on Crispy Nori</h4>
            <span class="redginger-item-price">$14.50</span>
          </div>
          <p class="redginger-item-desc">Finely diced yellowfin tuna tossed with sesame oil, scallions, and caviar, served over crispy tempura nori chips.</p>
        </div>

        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Bluefin Tuna (Maguro) Nigiri / Sashimi</h4>
            <span class="redginger-item-price">$8.00</span>
          </div>
          <p class="redginger-item-desc">Two pristine cuts of deep ruby Bluefin tuna served over seasoned shari or sashimi style.</p>
        </div>

        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Scottish Salmon (Sake) Nigiri / Sashimi</h4>
            <span class="redginger-item-price">$7.00</span>
          </div>
          <p class="redginger-item-desc">Two buttery cuts of fresh Atlantic salmon.</p>
        </div>

        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Japanese Yellowtail (Hamachi)</h4>
            <span class="redginger-item-price">$8.00</span>
          </div>
          <p class="redginger-item-desc">Two slices of sweet, rich hamachi with scallion crown.</p>
        </div>

        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Freshwater BBQ Eel (Unagi)</h4>
            <span class="redginger-item-price">$7.50</span>
          </div>
          <p class="redginger-item-desc">Warm grilled eel glazed with sweet kabayaki sauce.</p>
        </div>
      </div>
    </div>

    <!-- Group 4: Lunch Bento -->
    <div class="redginger-menu-group" id="tab-bento">
      <div class="redginger-section-title">
        <h2>Uptown Executive Lunch Bento Boxes</h2>
        <p>Available Monday – Friday 11:00 AM – 2:30 PM. Served with Miso Soup, Salad, 4 pcs California Roll, Shrimp Shumai, and Jasmine Rice.</p>
      </div>

      <div class="redginger-grid-2">
        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Hibachi Steak Lunch Bento</h4>
            <span class="redginger-item-price">$17.50</span>
          </div>
          <p class="redginger-item-desc">Grilled sirloin steak with mushrooms, California roll, steamed shrimp shumai, house ginger salad, and miso soup.</p>
        </div>

        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Teriyaki Salmon Lunch Bento</h4>
            <span class="redginger-item-price">$16.99</span>
          </div>
          <p class="redginger-item-desc">Fresh pan-seared Atlantic salmon with sweet teriyaki reduction, California roll, shumai, salad, and soup.</p>
        </div>

        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Chicken Katsu Lunch Bento</h4>
            <span class="redginger-item-price">$15.50</span>
          </div>
          <p class="redginger-item-desc">Crispy panko-breaded chicken cutlet with Japanese katsu sauce, California roll, steamed dumplings, and sides.</p>
        </div>

        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Sushi &amp; Sashimi Lunch Combo</h4>
            <span class="redginger-item-price">$18.50</span>
          </div>
          <p class="redginger-item-desc">4 pieces of chef’s assorted nigiri, 6 pieces of sashimi, and a spicy tuna roll with miso soup and house salad.</p>
        </div>
      </div>
    </div>

    <!-- Group 5: Starters & Kitchen -->
    <div class="redginger-menu-group" id="tab-izakaya">
      <div class="redginger-section-title">
        <h2>Izakaya Starters, Soups &amp; Desserts</h2>
        <p>Shareable small plates to begin your evening on South Tryon.</p>
      </div>

      <div class="redginger-grid-2">
        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Pan-Seared Pork or Veggie Gyoza (6 pcs)</h4>
            <span class="redginger-item-price">$7.50</span>
          </div>
          <p class="redginger-item-desc">Crispy golden dumplings filled with seasoned pork or mixed greens, served with scallion-soy dip.</p>
        </div>

        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Rock Shrimp Tempura</h4>
            <span class="redginger-item-price">$12.50</span>
          </div>
          <p class="redginger-item-desc">Crispy bite-sized tempura shrimp tossed in spicy creamy aioli and dusted with shichimi togarashi pepper.</p>
        </div>

        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Chilean Sea Bass with Miso Glaze</h4>
            <span class="redginger-item-price">$28.00</span>
          </div>
          <p class="redginger-item-desc">Broiled Chilean sea bass marinated for 48 hours in sweet saikyo miso, served with baby bok choy.</p>
        </div>

        <div class="redginger-menu-item">
          <div class="redginger-item-header">
            <h4>Artisanal Green Tea Mochi Ice Cream (3 pcs)</h4>
            <span class="redginger-item-price">$6.50</span>
          </div>
          <p class="redginger-item-desc">Sweet chewy rice dough filled with premium Japanese matcha green tea and strawberry ice cream.</p>
        </div>
      </div>
    </div>

    <!-- Bottom Order CTA -->
    <div class="redginger-cta-banner" style="margin-top:50px;">
      <h2>Planning Lunch, Dinner, or Private Dining?</h2>
      <p>Call our South Tryon host team for table reservations, executive bento orders, and private event bookings.</p>
      <div class="redginger-cta-btns">
        <a href="tel:9808198837" class="redginger-btn-hero-primary">Call (980) 819-8837</a>
        <a href="private-dining-and-group-events.html" class="redginger-btn-hero-secondary">Explore Private Dining</a>
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
