# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("scripts")
from basil_builder import header_html, footer_html

# Page 3: chef-specialties-and-curries.html
curries_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chef Specialties &amp; Curries | Basil Thai Cuisine Uptown Charlotte</title>
  <meta name="description" content="Discover signature Thai culinary masterpieces at Basil Thai Cuisine Charlotte: Crispy Basil Duck, Chilean Sea Bass, slow-simmered Masaman, Green, and Panang Curries.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("chef-specialties-and-curries.html")}

  <section class="basil-hero-compact">
    <div class="basil-container">
      <span class="basil-badge">Culinary Signatures</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Chef Specialties &amp; Scratch Curries</h1>
      <p style="font-size:1.1rem; color:#cbd5e1; max-width:720px; margin:0 auto;">Artisanal creations highlighting premium ingredients, slow-simmered coconut reductions, and fresh Southeast Asian aromatics.</p>
    </div>
  </section>

  <main class="basil-container" style="padding:60px 24px;">
    <!-- Duck Spotlight Section -->
    <div class="basil-grid-2" style="align-items:center; margin-bottom:60px;">
      <div>
        <span class="basil-tag">Charlotte's Renowned Duck</span>
        <h2 style="font-size:2.1rem; color:#064e3b; margin:15px 0; font-weight:800;">The Art of Our Crispy Basil Duck</h2>
        <p style="color:#475569; line-height:1.7; margin-bottom:15px;">
          Our signature Crispy Basil Duck has earned acclaim across Charlotte as an absolute benchmark of Thai culinary technique. Every duck is spiced with star anise and cinnamon, slow-roasted until tender, and then flash-crisped to create an irresistibly crunchy skin while retaining maximum juiciness.
        </p>
        <p style="color:#475569; line-height:1.7; margin-bottom:15px;">
          The carved duck is then wok-finished with aromatic garlic cloves, spicy bird chilis, sweet vidalia onions, crisp bell peppers, and handfuls of fragrant holy basil leaves in our savory glaze.
        </p>
        <div style="background:#ecfdf5; border-left:4px solid #047857; padding:16px; border-radius:6px; margin-top:20px;">
          <h4 style="color:#065f46; margin-bottom:4px;">Chef's Wine Pairing Note</h4>
          <p style="color:#047857; font-size:0.95rem; margin:0;">Pairs exceptionally well with our curated Oregon Pinot Noir or a chilled German Riesling, balancing the dish's spicy basil kick with bright acidity.</p>
        </div>
      </div>
      <div>
        <img src="images/basil-duck-specialty.jpg" alt="Crispy roasted Thai duck with herbs and chili glaze" style="width:100%; height:400px; object-fit:cover; border-radius:12px; box-shadow:var(--basil-shadow-lg);">
      </div>
    </div>

    <!-- Curries Section -->
    <h2 style="font-size:1.9rem; color:#064e3b; text-align:center; margin-bottom:35px;">Slow-Simmered Traditional Curries</h2>
    
    <div class="basil-grid-3" style="gap:28px; margin-bottom:60px;">
      <div class="basil-card">
        <h3 style="color:#064e3b; margin-bottom:8px;">Royal Masaman Curry</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Silky Southern Thai curry made from whole roasted spices (cardamom, coriander, cinnamon) with coconut cream, Idaho potatoes, sweet onions, and roasted whole cashew nuts.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$18.95</span>
          <span class="basil-tag">Mild &amp; Rich</span>
        </div>
      </div>

      <div class="basil-card">
        <h3 style="color:#064e3b; margin-bottom:8px;">Panang Curry</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Rich and creamy red curry reduction simmered with thick coconut cream, green bell peppers, hand-torn kaffir lime leaves, and choice of tender sliced protein.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$18.95</span>
          <span class="basil-tag">Medium Heat</span>
        </div>
      </div>

      <div class="basil-card">
        <h3 style="color:#064e3b; margin-bottom:8px;">Emerald Green Curry</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Fresh green bird chili paste pounded with lemongrass and galangal, simmered in coconut milk with tender bamboo shoots, Thai eggplant, and fresh holy basil.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$18.95</span>
          <span class="basil-tag">Spicy &amp; Fresh</span>
        </div>
      </div>

      <div class="basil-card">
        <h3 style="color:#064e3b; margin-bottom:8px;">Crispy Chilean Sea Bass</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Pan-seared Chilean sea bass filet over steamed baby bok choy and julienned vegetables, finished with sweet chili garlic reduction or tamarind sauce.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$32.00</span>
          <span class="basil-tag">Chef Feature</span>
        </div>
      </div>

      <div class="basil-card">
        <h3 style="color:#064e3b; margin-bottom:8px;">Flame-Grilled Lamb Lollipops</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Tender herb-crusted lamb chops grilled over open flame, served over roasted asparagus with a drizzle of spiced aromatic massaman curry reduction.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$29.50</span>
          <span class="basil-tag">Premium Cut</span>
        </div>
      </div>

      <div class="basil-card">
        <h3 style="color:#064e3b; margin-bottom:8px;">Red Curry with Roasted Duck</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Roasted sliced duck breast simmered in rich red coconut curry with sweet pineapple chunks, cherry tomatoes, bell peppers, and fresh Thai basil leaves.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$24.50</span>
          <span class="basil-tag">Sweet &amp; Savory</span>
        </div>
      </div>
    </div>

    <!-- Call to Action Banner -->
    <div class="basil-banner-strip">
      <h2 style="color:#ffffff; font-size:2rem; margin-bottom:12px;">Experience Unmatched Thai Flavors</h2>
      <p style="color:#cbd5e1; max-width:650px; margin:0 auto 20px;">Reserve a table for dinner or place a carryout order for prompt kitchen preparation.</p>
      <a href="tel:7043327212" class="basil-btn-primary">Call (704) 332-7212</a>
    </div>
  </main>

{footer_html()}
"""

with open("basil-thai-cuisine/chef-specialties-and-curries.html", "w", encoding="utf-8") as f:
    f.write(curries_content)
print("Written: basil-thai-cuisine/chef-specialties-and-curries.html")

# Page 4: wok-noodles-and-street-fare.html
noodles_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Wok Noodles &amp; Street Fare | Basil Thai Cuisine Charlotte NC</title>
  <meta name="description" content="Savor authentic wok-fired Thai noodles and street specialties at Basil Thai Cuisine Charlotte: Pad Thai, Pad See Eu, drunken noodles (Pad Kee Mao), and basil fried rice.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("wok-noodles-and-street-fare.html")}

  <section class="basil-hero-compact">
    <div class="basil-container">
      <span class="basil-badge">High Heat Wok Artistry</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Artisanal Wok Noodles &amp; Street Fare</h1>
      <p style="font-size:1.1rem; color:#cbd5e1; max-width:720px; margin:0 auto;">Wok-charred noodles, fragrant jasmine fried rice, and savory street stir-fries cooked to order over intense flame.</p>
    </div>
  </section>

  <main class="basil-container" style="padding:60px 24px;">
    <div class="basil-grid-2" style="align-items:center; margin-bottom:60px;">
      <div>
        <span class="basil-tag">The Flame &amp; The Wok</span>
        <h2 style="font-size:2.1rem; color:#064e3b; margin:15px 0; font-weight:800;">Authentic Wok Hei Technique</h2>
        <p style="color:#475569; line-height:1.7; margin-bottom:15px;">
          The soul of Thai noodle cooking is "Wok Hei"—the distinct breath of the wok achieved only through intense heat and rapid continuous tossing. This caramelizes sauces instantly, imparting smoky complexity while locking in the fresh crispness of vegetables.
        </p>
        <p style="color:#475569; line-height:1.7; margin-bottom:15px;">
          From our signature sweet-savory Pad Thai sauce made from pure tamarind pulp and palm sugar to the wide-noodle sear of Pad See Eu, every plate is cooked individually upon your order.
        </p>
        <ul style="color:#334155; line-height:1.8; padding-left:20px; margin-top:15px;">
          <li>Customizable spice levels: Mild, Medium, Hot, or Authentic Thai Hot</li>
          <li>Fresh proteins: Chicken, Prime Beef, Jumbo Gulf Shrimp, or Organic Fried Tofu</li>
          <li>Gluten-free and vegan preparation upon request</li>
        </ul>
      </div>
      <div>
        <img src="images/pad-thai-noodles.jpg" alt="Artisanal wok-charred Pad Thai noodles at Basil Thai Charlotte" style="width:100%; height:400px; object-fit:cover; border-radius:12px; box-shadow:var(--basil-shadow-lg);">
      </div>
    </div>

    <!-- Noodles & Street Dishes Grid -->
    <h2 style="font-size:1.9rem; color:#064e3b; text-align:center; margin-bottom:35px;">Wok Specialties</h2>

    <div class="basil-grid-3" style="gap:28px; margin-bottom:60px;">
      <div class="basil-card">
        <h3 style="color:#064e3b; margin-bottom:8px;">Signature Pad Thai</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Delicate rice noodles tossed with farm egg, fresh bean sprouts, toasted crushed peanuts, scallions, and pure tamarind glaze. Choice of chicken, shrimp, beef, or tofu.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$18.50</span>
          <span class="basil-tag">House Benchmark</span>
        </div>
      </div>

      <div class="basil-card">
        <h3 style="color:#064e3b; margin-bottom:8px;">Pad See Eu (Soy Wide Noodles)</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Fresh broad rice noodles wok-charred with sweet dark molasses soy, fresh Chinese broccoli (gai lan), farm egg, and crushed garlic white pepper seasoning.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$18.50</span>
          <span class="basil-tag">Smoky &amp; Savory</span>
        </div>
      </div>

      <div class="basil-card">
        <h3 style="color:#064e3b; margin-bottom:8px;">Drunken Noodles (Pad Kee Mao)</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Wide rice noodles seared with crushed garlic, bird eye chilis, sweet onions, ripe tomatoes, bell peppers, and handfuls of fragrant holy basil leaves.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$18.50</span>
          <span class="basil-tag">Spicy Street Flavor</span>
        </div>
      </div>

      <div class="basil-card">
        <h3 style="color:#064e3b; margin-bottom:8px;">Spicy Basil Fried Rice</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Fragrant Thai jasmine rice wok-fried with minced garlic, red bird chilis, onions, bell peppers, fresh basil leaves, and farm egg. Served with lime wedge.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$17.50</span>
          <span class="basil-tag">Aromatic Rice</span>
        </div>
      </div>

      <div class="basil-card">
        <h3 style="color:#064e3b; margin-bottom:8px;">Pad Woon Sen (Glass Noodles)</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Delicate clear bean thread noodles stir-fried with egg, wood ear mushrooms, cabbage, celery, carrots, and sweet onions in light sesame oyster sauce.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$18.00</span>
          <span class="basil-tag">Light &amp; Savory</span>
        </div>
      </div>

      <div class="basil-card">
        <h3 style="color:#064e3b; margin-bottom:8px;">Pineapple Cashew Fried Rice</h3>
        <p style="color:#475569; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Jasmine rice stir-fried with yellow curry powder, sweet golden pineapple chunks, raisins, toasted whole cashews, onions, and farm egg.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$18.00</span>
          <span class="basil-tag">Sweet &amp; Nutty</span>
        </div>
      </div>
    </div>

    <!-- CTA Box -->
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:32px; box-shadow:var(--basil-shadow); text-align:center;">
      <h3 style="color:#064e3b; font-size:1.4rem; margin-bottom:10px;">Craving Fresh Wok-Tossed Noodles Tonight?</h3>
      <p style="color:#475569; max-width:600px; margin:0 auto 20px;">Call our host stand directly for swift takeout packaging and quick pickup on North Church Street.</p>
      <a href="tel:7043327212" class="basil-btn-primary">Call (704) 332-7212 to Order</a>
    </div>
  </main>

{footer_html()}
"""

with open("basil-thai-cuisine/wok-noodles-and-street-fare.html", "w", encoding="utf-8") as f:
    f.write(noodles_content)
print("Written: basil-thai-cuisine/wok-noodles-and-street-fare.html")

