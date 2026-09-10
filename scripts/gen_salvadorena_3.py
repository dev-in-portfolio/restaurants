# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\scripts")
from salvadorena_builder import header_html, footer_html

DIR = r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\restaurante-y-panaderia-salvadorena"

# 4. panaderia-dulce-and-quesadillas.html
bakery_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Panaderia Dulce &amp; Quesadilla Salvadorena | Charlotte NC</title>
  <meta name="description" content="Artisanal Salvadoran bakery in Charlotte NC. Oven-warm Quesadillas Salvadorenas with queso duro and sesame seeds, Semita de Pina, Salpores, and Marquesote.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
{header_html("panaderia-dulce-and-quesadillas.html")}

  <section class="salvadorena-hero" style="padding: 50px 20px;">
    <div class="salvadorena-hero-inner">
      <span class="salvadorena-hero-pill">Artisanal Panaderia Tradicional</span>
      <h1>Salvadoran Sweet Bakery &amp; Quesadillas</h1>
      <p>Step into the aroma of fresh baking butter, panela sugarcane, and toasted sesame. Our master bakers produce authentic Central American pastries and breads twice daily.</p>
    </div>
  </section>

  <main class="salvadorena-container">
    <div class="salvadorena-spotlight">
      <div>
        <img src="images/pan-dulce.jpg" alt="Golden baked Quesadilla Salvadorena and assorted Salvadoran pan dulce" class="salvadorena-card-image" style="height:100%; object-fit:cover;">
      </div>
      <div class="salvadorena-spotlight-content">
        <span class="salvadorena-card-badge">National Pride of Salvadoran Baking</span>
        <h3>The Authentic Quesadilla Salvadorena</h3>
        <p>Unlike Mexican savoury quesadillas made with tortillas, a <strong>Quesadilla Salvadorena</strong> is a rich, dense, sweet-and-savory cake that is the crown jewel of Salvadoran panaderias.</p>
        <p>Our traditional recipe blends imported aged Salvadoran queso duro blanco, rich sour crema, farm butter, sugar, and a blend of rice and wheat flour, crowned with golden toasted sesame seeds (ajonjoli). The result is an addictive balance of sweet custard crumb and salty cheese depth.</p>
        <p>Sold by the slice or as whole sheet cakes for your family celebrations.</p>
        <div style="margin-top:16px;">
          <a href="tel:7045254550" class="salvadorena-btn-cta">Order Whole Cakes: (704) 525-4550</a>
        </div>
      </div>
    </div>

    <div class="salvadorena-section-title" style="margin-top:60px;">
      <h2>Our Showcase Bakery Specialties</h2>
      <p>Each recipe has been preserved and perfected through generations of Salvadoran bakers.</p>
    </div>

    <div class="salvadorena-grid-3">
      <div class="salvadorena-card">
        <div class="salvadorena-card-body">
          <span class="salvadorena-card-badge">Pan Dulce Icon</span>
          <h3>Semita de Pina (Semita Alta)</h3>
          <p>Buttery crumb layers enveloping a thick center of slow-simmered caramelized pineapple preserves and rich unrefined brown sugar (dulce de panela), topped with a delicate criss-cross lattice.</p>
          <div class="salvadorena-card-footer">
            <span class="salvadorena-price">$3.75 / Piece</span>
          </div>
        </div>
      </div>

      <div class="salvadorena-card">
        <div class="salvadorena-card-body">
          <span class="salvadorena-card-badge">Gluten-Friendly Rice Base</span>
          <h3>Salpores de Arroz</h3>
          <p>Traditional melt-in-your-mouth shortbread biscuits made with fine rice flour, butter, and cinnamon, dusted with glistening sugar crystals. A delicate accompaniment to morning coffee.</p>
          <div class="salvadorena-card-footer">
            <span class="salvadorena-price">$2.25 / Piece</span>
          </div>
        </div>
      </div>

      <div class="salvadorena-card">
        <div class="salvadorena-card-body">
          <span class="salvadorena-card-badge">Custard Favorite</span>
          <h3>Relampagos de Caramelo</h3>
          <p>Salvadoran choux pastry rolls generously piped with silky vanilla egg custard cream (leche poleada) and smothered in glossy caramel dulce de leche.</p>
          <div class="salvadorena-card-footer">
            <span class="salvadorena-price">$3.50 / Piece</span>
          </div>
        </div>
      </div>

      <div class="salvadorena-card">
        <div class="salvadorena-card-body">
          <span class="salvadorena-card-badge">Coffee Dipper</span>
          <h3>Marquesote Tipico</h3>
          <p>An airy, golden sponge cake baked in traditional ring molds, scented with orange peel and cinnamon. Specifically baked dry to absorb sweet Cafe con Leche or hot chocolate.</p>
          <div class="salvadorena-card-footer">
            <span class="salvadorena-price">$2.50 / Piece</span>
          </div>
        </div>
      </div>

      <div class="salvadorena-card">
        <div class="salvadorena-card-body">
          <span class="salvadorena-card-badge">Heritage Loaf</span>
          <h3>Pan Frances Salvadoreno</h3>
          <p>Crisp on the outside and pillowy within, our Salvadoran French bread rolls are baked fresh every morning to accompany eggs, beans, and comforting soups.</p>
          <div class="salvadorena-card-footer">
            <span class="salvadorena-price">$0.75 / Roll</span>
          </div>
        </div>
      </div>

      <div class="salvadorena-card">
        <div class="salvadorena-card-body">
          <span class="salvadorena-card-badge">Layered Delight</span>
          <h3>Maria Luisa Cake</h3>
          <p>Golden vanilla sheet sponge layered with warm spiced fruit jam and delicate vanilla cream frosting, sprinkled with powdered sugar.</p>
          <div class="salvadorena-card-footer">
            <span class="salvadorena-price">$3.25 / Piece</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Merienda Afternoon Coffee Banner -->
    <div class="salvadorena-card" style="margin-top:40px; padding:36px; background:linear-gradient(135deg, #fefce8, #eff6ff); border: 2px solid var(--salvadorena-border);">
      <h3 style="color:var(--salvadorena-primary-dark); margin-bottom:12px;">The Salvadoran Merienda: Afternoon Coffee &amp; Pan Dulce</h3>
      <p style="color:var(--salvadorena-text); font-size:1rem; line-height:1.7;">Between 3:00 PM and 5:00 PM across El Salvador, communities pause for <em>la merienda</em>—a cherished daily ritual of unwinding with hot highland coffee and oven-warm pan dulce. Stop by our South Blvd location in the afternoon to grab a bakery tray, select your favorite sweet breads, and enjoy the authentic taste of home.</p>
    </div>

    <div class="salvadorena-cta-banner" style="margin-top:50px;">
      <h2>Need a Custom Bakery Box or Whole Quesadilla?</h2>
      <p>We prepare custom bakery boxes for office meetings, family parties, and weekend breakfasts.</p>
      <div class="salvadorena-cta-btns">
        <a href="pupusa-catering-and-bakery-boxes.html" class="salvadorena-btn-hero-primary">Explore Party Boxes</a>
        <a href="tel:7045254550" class="salvadorena-btn-hero-secondary">Call Bakery: (704) 525-4550</a>
      </div>
    </div>
  </main>

{footer_html()}'''

# 5. pupusa-catering-and-bakery-boxes.html
catering_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pupusa Catering &amp; Bakery Party Boxes | Charlotte NC</title>
  <meta name="description" content="Cater your Charlotte gatherings with handcrafted pupusa party boxes, assorted Salvadoran bakery crates, tangy curtido jars, and authentic breakfast buffets.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
{header_html("pupusa-catering-and-bakery-boxes.html")}

  <section class="salvadorena-hero" style="padding: 50px 20px;">
    <div class="salvadorena-hero-inner">
      <span class="salvadorena-hero-pill">Events, Parties &amp; Gatherings</span>
      <h1>Pupusa Catering &amp; Bakery Boxes</h1>
      <p>Bring the warmth of Salvadoran hospitality to your next corporate lunch, birthday celebration, church gathering, or family weekend. Fresh, hot, and fully packaged.</p>
    </div>
  </section>

  <main class="salvadorena-container">
    <div class="salvadorena-section-title">
      <h2>Curated Catering Packages</h2>
      <p>Every pupusa package arrives piping hot in insulated packaging, accompanied by abundant curtido and tomato salsa.</p>
    </div>

    <div class="salvadorena-grid-3">
      <div class="salvadorena-card">
        <div class="salvadorena-card-body">
          <span class="salvadorena-card-badge">Small Group Favorite</span>
          <h3>Fiesta Box (25 Pupusas)</h3>
          <p>Choose up to 3 pupusa varieties (revueltas, loroco con queso, chicharron, frijol con queso). Includes 2 quart jars of house curtido and 1 quart of warm tomato salsa.</p>
          <div class="salvadorena-card-footer">
            <span class="salvadorena-price">$79.99</span>
            <span style="font-size:0.85rem; color:var(--salvadorena-text-muted);">Feeds 8-10 Guests</span>
          </div>
        </div>
      </div>

      <div class="salvadorena-card">
        <div class="salvadorena-card-body">
          <span class="salvadorena-card-badge">Community Banquet</span>
          <h3>Gran Banquete (50 Pupusas)</h3>
          <p>Choose up to 5 pupusa varieties with mixed corn and rice masa options. Includes 4 quart jars of curtido, 2 quarts of tomato salsa, and disposable serving tongs.</p>
          <div class="salvadorena-card-footer">
            <span class="salvadorena-price">$154.99</span>
            <span style="font-size:0.85rem; color:var(--salvadorena-text-muted);">Feeds 16-20 Guests</span>
          </div>
        </div>
      </div>

      <div class="salvadorena-card">
        <div class="salvadorena-card-body">
          <span class="salvadorena-card-badge">Bakery Assortment</span>
          <h3>Pan Dulce Party Crate (24 Pcs)</h3>
          <p>An assorted bakery crate featuring Quesadilla Salvadorena wedges, Semitas de Pina, Salpores de Arroz, Marquesote slices, and Relampagos.</p>
          <div class="salvadorena-card-footer">
            <span class="salvadorena-price">$54.99</span>
            <span style="font-size:0.85rem; color:var(--salvadorena-text-muted);">Feeds 20-24 Guests</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Interactive Calculator -->
    <div class="salvadorena-section-title" style="margin-top:60px;">
      <h2>Interactive Party Order Calculator</h2>
      <p>Estimate your pupusa count, curtido requirements, bakery additions, and pricing for your upcoming event.</p>
    </div>

    <div class="salvadorena-calc-box">
      <div class="salvadorena-calc-row">
        <label for="calc-pupusas">Number of Pupusas: <span id="calc-pupusas-val" style="color:var(--salvadorena-ochre);">24 Handcrafted Pupusas</span></label>
        <input type="range" id="calc-pupusas" min="12" max="120" step="6" value="24" class="salvadorena-range-control">
      </div>

      <div class="salvadorena-calc-row">
        <label for="calc-pupusa-type">Select Masa Style &amp; Filling Mix</label>
        <select id="calc-pupusa-type" class="salvadorena-select-control">
          <option value="3.25" selected>Heirloom Corn Masa Classic Mix ($3.25/ea)</option>
          <option value="3.50">Rice Flour (Masa de Arroz) Special ($3.50/ea)</option>
          <option value="3.35">Half Corn &amp; Half Rice Masa Blend ($3.35/ea)</option>
        </select>
      </div>

      <div class="salvadorena-calc-row">
        <label for="calc-bakery">Bakery Add-on Per Guest</label>
        <select id="calc-bakery" class="salvadorena-select-control">
          <option value="0" selected>No Bakery Add-On</option>
          <option value="1.50">Add Quesadilla Salvadorena Slices (+$1.50 / guest)</option>
          <option value="1.25">Add Mixed Pan Dulce Assortment (+$1.25 / guest)</option>
        </select>
      </div>

      <div class="salvadorena-calc-results">
        <div class="salvadorena-result-line">
          <span>Estimated Serving Capacity:</span>
          <strong id="calc-feeds-count">Feeds ~8 Guests (3 pupusas each)</strong>
        </div>
        <div class="salvadorena-result-line">
          <span>Complimentary Curtido &amp; Salsa:</span>
          <strong id="calc-curtido-jars">2 Quart Jar(s) of Tangy Curtido &amp; Salsa</strong>
        </div>
        <div class="salvadorena-result-total">
          <span>Estimated Total:</span>
          <span id="calc-total-price">$78.00</span>
        </div>
      </div>

      <div style="margin-top:24px; text-align:center;">
        <a href="tel:7045254550" class="salvadorena-btn-hero-primary" style="display:inline-block; width:100%;">Call (704) 525-4550 to Place Catering Order</a>
      </div>
    </div>

    <!-- Ordering Policies -->
    <div class="salvadorena-grid-2" style="margin-top:50px;">
      <div class="salvadorena-card" style="padding:28px;">
        <h4 style="color:var(--salvadorena-primary-dark); margin-bottom:10px;">Pickup &amp; Advance Notice</h4>
        <p style="color:var(--salvadorena-text-muted); font-size:0.95rem;">For orders of 25 to 50 pupusas, please provide at least 2 hours advance notice so our pupuseras can pat and griddle everything fresh. Orders over 50 pupusas or whole sheet quesadillas should be placed 24 hours in advance.</p>
      </div>

      <div class="salvadorena-card" style="padding:28px;">
        <h4 style="color:var(--salvadorena-primary-dark); margin-bottom:10px;">Dietary &amp; Masa Accommodations</h4>
        <p style="color:var(--salvadorena-text-muted); font-size:0.95rem;">We happily prepare 100% vegetarian party boxes (loroco con queso, frijol con queso, ayote/squash) and gluten-friendly rice flour pupusa platters upon request at no extra hassle.</p>
      </div>
    </div>
  </main>

{footer_html()}'''

# 6. visit.html
visit_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Visit &amp; Hours | Restaurante Y Panaderia Salvadorena</title>
  <meta name="description" content="Plan your visit to Restaurante Y Panaderia Salvadorena at 4325 South Blvd, Charlotte NC. View bakery hours, hot kitchen times, weekend soup schedules, and contact info.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
{header_html("visit.html")}

  <section class="salvadorena-hero" style="padding: 50px 20px;">
    <div class="salvadorena-hero-inner">
      <span class="salvadorena-hero-pill">Charlotte South Blvd Location</span>
      <h1>Visit &amp; Operating Hours</h1>
      <p>We welcome you to enjoy warm pupusas fresh off the comal, hot morning breakfasts, and sweet baked treats every day of the week.</p>
    </div>
  </section>

  <main class="salvadorena-container">
    <div class="salvadorena-visit-grid">
      <div class="salvadorena-info-card">
        <h3>Location &amp; Contact</h3>
        
        <div class="salvadorena-info-item">
          <strong>Street Address</strong>
          <p>4325 South Blvd<br>Charlotte, NC 28209<br>United States</p>
        </div>

        <div class="salvadorena-info-item">
          <strong>Direct Telephone</strong>
          <p><a href="tel:7045254550" style="font-weight:700; font-size:1.1rem; color:var(--salvadorena-primary);">(704) 525-4550</a></p>
        </div>

        <div class="salvadorena-info-item">
          <strong>Email Inquiries</strong>
          <p><a href="mailto:info@panaderiasalvadorenaclt.com">info@panaderiasalvadorenaclt.com</a></p>
        </div>

        <div class="salvadorena-info-item">
          <strong>Neighborhood &amp; Parking</strong>
          <p>Conveniently situated on South Blvd near Scaleybark Road with a dedicated private parking lot directly in front of the bakery and restaurant entrance. Accessible via CATS Bus Route 16 and close to the LYNX Blue Line Scaleybark Station.</p>
        </div>
      </div>

      <div class="salvadorena-info-card">
        <h3>Hours of Operation</h3>
        
        <div class="salvadorena-info-item">
          <strong>Monday - Thursday</strong>
          <p>7:30 AM - 9:00 PM<br><small style="color:var(--salvadorena-text-muted);">Hot breakfast starts at 7:30 AM | Pupusas served all day</small></p>
        </div>

        <div class="salvadorena-info-item">
          <strong>Friday - Saturday</strong>
          <p>7:30 AM - 9:00 PM<br><small style="color:var(--salvadorena-text-muted);">Weekend Pan Dulce bakes &amp; Sopa de Res ready by 10:30 AM</small></p>
        </div>

        <div class="salvadorena-info-item">
          <strong>Sunday</strong>
          <p>7:30 AM - 8:30 PM<br><small style="color:var(--salvadorena-text-muted);">Sopa de Res, Sopa de Pata &amp; Fresh Horchata de Morro</small></p>
        </div>

        <div class="salvadorena-info-item">
          <strong>Bakery Oven Schedule</strong>
          <p>First Fresh Bake: 7:30 AM<br>Second Afternoon Bake: 2:30 PM (Fresh Merienda Pan Dulce)</p>
        </div>
      </div>
    </div>

    <!-- FAQ Accordion -->
    <div class="salvadorena-section-title" style="margin-top:60px;">
      <h2>Frequently Asked Questions</h2>
      <p>Everything you need to know about dining in, takeout, and dietary options.</p>
    </div>

    <div style="max-width:800px; margin:0 auto;">
      <div class="salvadorena-accordion">
        <div class="salvadorena-accordion-header">
          <span>Are your pupusas made fresh or pre-made?</span>
          <span class="salvadorena-accordion-icon">+</span>
        </div>
        <div class="salvadorena-accordion-content">
          <p>Every single pupusa is hand-patted and grilled to order on our hot comal. We never reheat or pre-make pupusas, ensuring the crispy exterior and melted cheese interior are always at their absolute peak.</p>
        </div>
      </div>

      <div class="salvadorena-accordion">
        <div class="salvadorena-accordion-header">
          <span>What is the difference between corn and rice pupusas?</span>
          <span class="salvadorena-accordion-icon">+</span>
        </div>
        <div class="salvadorena-accordion-content">
          <p>Corn masa pupusas offer a rich, hearty, traditional corn flavor with a chewy texture. Rice masa (masa de arroz) pupusas, originating from Olocuilta, are lighter, crispier on the edges, silky in texture, and naturally gluten-free.</p>
        </div>
      </div>

      <div class="salvadorena-accordion">
        <div class="salvadorena-accordion-header">
          <span>Do you have vegetarian and gluten-free choices?</span>
          <span class="salvadorena-accordion-icon">+</span>
        </div>
        <div class="salvadorena-accordion-content">
          <p>Yes! We have several vegetarian pupusas including Queso con Loroco, Frijol con Queso, and Ayote (Zucchini) con Queso. Our rice flour pupusas and corn pupusas are prepared with naturally gluten-free ingredients.</p>
        </div>
      </div>

      <div class="salvadorena-accordion">
        <div class="salvadorena-accordion-header">
          <span>Can I order whole Quesadillas Salvadorenas or large catering boxes?</span>
          <span class="salvadorena-accordion-icon">+</span>
        </div>
        <div class="salvadorena-accordion-content">
          <p>Absolutely. We bake whole sheet Quesadillas Salvadorenas and prepare 25-pupusa and 50-pupusa catering boxes with jars of homemade curtido and salsa. Please call (704) 525-4550 to order.</p>
        </div>
      </div>
    </div>

    <div class="salvadorena-cta-banner" style="margin-top:50px;">
      <h2>We Look Forward to Serving You</h2>
      <p>4325 South Blvd, Charlotte, NC 28209 | Call (704) 525-4550</p>
      <div class="salvadorena-cta-btns">
        <a href="tel:7045254550" class="salvadorena-btn-hero-primary">Call (704) 525-4550</a>
        <a href="menu.html" class="salvadorena-btn-hero-secondary">Explore Menu</a>
      </div>
    </div>
  </main>

{footer_html()}'''

with open(os.path.join(DIR, "panaderia-dulce-and-quesadillas.html"), "w", encoding="utf-8") as f:
    f.write(bakery_content)
print("Wrote panaderia-dulce-and-quesadillas.html")

with open(os.path.join(DIR, "pupusa-catering-and-bakery-boxes.html"), "w", encoding="utf-8") as f:
    f.write(catering_content)
print("Wrote pupusa-catering-and-bakery-boxes.html")

with open(os.path.join(DIR, "visit.html"), "w", encoding="utf-8") as f:
    f.write(visit_content)
print("Wrote visit.html")
