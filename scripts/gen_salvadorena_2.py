# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\scripts")
from salvadorena_builder import header_html, footer_html

DIR = r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\restaurante-y-panaderia-salvadorena"

# 2. menu.html
menu_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Full Salvadoran Menu | Restaurante Y Panaderia Salvadorena</title>
  <meta name="description" content="Explore our complete menu of handcrafted Salvadoran pupusas, fresh baked pan dulce, hearty breakfast platters, traditional stews, and refrescos naturales.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
{header_html("menu.html")}

  <section class="salvadorena-hero" style="padding: 50px 20px;">
    <div class="salvadorena-hero-inner">
      <span class="salvadorena-hero-pill">Handmade Daily in Charlotte</span>
      <h1>Authentic Salvadoran Menu</h1>
      <p>From fresh corn and rice masa pupusas sizzling on our comal to traditional oven-warm pan dulce and weekend stews, explore our homestyle culinary heritage.</p>
    </div>
  </section>

  <main class="salvadorena-container">
    <div class="salvadorena-tabs">
      <button class="salvadorena-tab-btn active" data-target="tab-pupusas">Pupusas Artesanales</button>
      <button class="salvadorena-tab-btn" data-target="tab-panaderia">Panaderia &amp; Dulces</button>
      <button class="salvadorena-tab-btn" data-target="tab-desayunos">Platos &amp; Desayunos</button>
      <button class="salvadorena-tab-btn" data-target="tab-sopas">Sopas Tradicionales</button>
      <button class="salvadorena-tab-btn" data-target="tab-bebidas">Bebidas &amp; Refrescos</button>
    </div>

    <!-- Group 1: Pupusas -->
    <div class="salvadorena-menu-group active" id="tab-pupusas">
      <div class="salvadorena-section-title">
        <h2>Pupusas Artesanales (Corn or Rice Masa)</h2>
        <p>Hand-patted to order, served with homemade crunchy cabbage curtido and warm salsa de tomate roja. Available in heirloom corn masa or delicate rice flour (arroz).</p>
      </div>

      <div class="salvadorena-grid-2">
        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Pupusa Revuelta (Chicharron, Frijol, Queso)</h4>
            <span class="salvadorena-item-price">$3.25</span>
          </div>
          <p class="salvadorena-item-desc">The ultimate Salvadoran classic: slow-simmered seasoned pork chicharron, refried red beans, and melted Salvadoran quesillo cheese.</p>
          <span class="salvadorena-item-tag">Top Guest Favorite</span>
        </div>

        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Pupusa de Loroco con Quesillo</h4>
            <span class="salvadorena-item-price">$3.25</span>
          </div>
          <p class="salvadorena-item-desc">Edible fragrant loroco flower buds sauteed and blended with creamy melting quesillo. Floral, earthy, and distinctly Salvadoran.</p>
          <span class="salvadorena-item-tag">Vegetarian Friendly</span>
        </div>

        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Pupusa de Chicharron con Queso</h4>
            <span class="salvadorena-item-price">$3.25</span>
          </div>
          <p class="salvadorena-item-desc">Tender artisanal seasoned pork chicharron ground into a velvety paste and folded into gooey melted Salvadoran quesillo.</p>
        </div>

        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Pupusa de Frijol con Queso</h4>
            <span class="salvadorena-item-price">$3.00</span>
          </div>
          <p class="salvadorena-item-desc">Silky smooth refried Salvadoran red silk beans combined with melted quesillo inside your choice of masa.</p>
          <span class="salvadorena-item-tag">Vegetarian Friendly</span>
        </div>

        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Pupusa de Ayote (Zucchini Squash) con Queso</h4>
            <span class="salvadorena-item-price">$3.25</span>
          </div>
          <p class="salvadorena-item-desc">Finely grated tender summer squash seasoned with sweet onion and herbs, paired with rich melted quesillo.</p>
          <span class="salvadorena-item-tag">Vegetarian Friendly</span>
        </div>

        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Pupusa de Jalapeno con Queso</h4>
            <span class="salvadorena-item-price">$3.25</span>
          </div>
          <p class="salvadorena-item-desc">Diced mild pickled and fresh jalapeno peppers blended with stretchy quesillo for a bright, spicy kick.</p>
        </div>

        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Pupusa de Pollo con Queso</h4>
            <span class="salvadorena-item-price">$3.50</span>
          </div>
          <p class="salvadorena-item-desc">Shredded tender chicken breast stewed in tomato, garlic, and sweet bell pepper, wrapped with savory quesillo.</p>
        </div>

        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Pupusa Loca (Mega All-In Pupusa)</h4>
            <span class="salvadorena-item-price">$5.50</span>
          </div>
          <p class="salvadorena-item-desc">An extra-large double-sized pupusa stuffed with chicharron, shredded chicken, refried beans, loroco, jalapeno, and double quesillo.</p>
          <span class="salvadorena-item-tag">House Specialty</span>
        </div>
      </div>
    </div>

    <!-- Group 2: Panaderia -->
    <div class="salvadorena-menu-group" id="tab-panaderia">
      <div class="salvadorena-section-title">
        <h2>Panaderia Dulce &amp; Reposteria</h2>
        <p>Baked fresh twice daily in our bakery ovens. Perfect for breakfast or afternoon coffee.</p>
      </div>

      <div class="salvadorena-grid-2">
        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Quesadilla Salvadorena Tradicional</h4>
            <span class="salvadorena-item-price">$4.50 / Slice</span>
          </div>
          <p class="salvadorena-item-desc">Rich and buttery sweet pound cake enriched with imported aged Salvadoran queso duro and crema, topped with toasted sesame seeds.</p>
          <span class="salvadorena-item-tag">Signature Bakery Item</span>
        </div>

        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Semita de Pina (Semita Alta &amp; Pachita)</h4>
            <span class="salvadorena-item-price">$3.75</span>
          </div>
          <p class="salvadorena-item-desc">Golden flaky pastry layered with sweet artisanal pineapple jam and unrefined dulce de panela cane syrup with a latticed crust.</p>
        </div>

        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Salpores de Arroz</h4>
            <span class="salvadorena-item-price">$2.25</span>
          </div>
          <p class="salvadorena-item-desc">Tender crumbly shortbread biscuits made with rice flour and butter, lightly dusted with sugar.</p>
          <span class="salvadorena-item-tag">Gluten-Friendly Rice Base</span>
        </div>

        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Relampagos de Crema Pastelera</h4>
            <span class="salvadorena-item-price">$3.50</span>
          </div>
          <p class="salvadorena-item-desc">Salvadoran-style eclairs filled with house-made vanilla custard cream and glazed with rich caramel dulce de leche.</p>
        </div>

        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Marquesote Tradicional</h4>
            <span class="salvadorena-item-price">$2.50</span>
          </div>
          <p class="salvadorena-item-desc">Light and airy Salvadoran sponge cake baked with eggs, cane sugar, and a hint of cinnamon. Ideal for dipping in hot coffee or chocolate.</p>
        </div>

        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Maria Luisa</h4>
            <span class="salvadorena-item-price">$3.25</span>
          </div>
          <p class="salvadorena-item-desc">Layered golden cake with sweet milk custard (leche poleada) and citrus fruit preserves.</p>
        </div>
      </div>
    </div>

    <!-- Group 3: Desayunos & Platos -->
    <div class="salvadorena-menu-group" id="tab-desayunos">
      <div class="salvadorena-section-title">
        <h2>Platos Tipicos &amp; Desayunos</h2>
        <p>Hearty Salvadoran comfort platters served all day with warm handmade corn tortillas.</p>
      </div>

      <div class="salvadorena-grid-2">
        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Desayuno Tipico Salvadoreno Completo</h4>
            <span class="salvadorena-item-price">$11.99</span>
          </div>
          <p class="salvadorena-item-desc">Two eggs prepared sunny-side up or scrambled, sweet fried ripe plantains, silky refried beans, Salvadoran crema, queso duro blanco, and 2 hot tortillas.</p>
        </div>

        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Carne Asada con Chimol y Frijoles</h4>
            <span class="salvadorena-item-price">$15.99</span>
          </div>
          <p class="salvadorena-item-desc">Marinated grilled flank steak served with fresh chimol (radish, cilantro, tomato salsa), seasoned rice, refried beans, fried plantains, and tortillas.</p>
        </div>

        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Yuca Frita con Chicharron de Cerdo</h4>
            <span class="salvadorena-item-price">$12.50</span>
          </div>
          <p class="salvadorena-item-desc">Crisp golden cassava root spears topped with crunchy pork carnitas chicharron, shredded cabbage curtido, tomato sauce, and lime.</p>
        </div>

        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Pastelitos de Carne y Verduras (3 pcs)</h4>
            <span class="salvadorena-item-price">$8.50</span>
          </div>
          <p class="salvadorena-item-desc">Achiote-tinted crispy corn turnovers filled with seasoned minced beef and potatoes, served piping hot with tangy curtido.</p>
        </div>
      </div>
    </div>

    <!-- Group 4: Sopas -->
    <div class="salvadorena-menu-group" id="tab-sopas">
      <div class="salvadorena-section-title">
        <h2>Sopas Tradicionales Salvadorenas</h2>
        <p>Slow-simmered weekend stews made with wholesome vegetables and marrow bone broths.</p>
      </div>

      <div class="salvadorena-grid-2">
        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Sopa de Res (Beef Shank &amp; Vegetable Stew)</h4>
            <span class="salvadorena-item-price">$14.99</span>
          </div>
          <p class="salvadorena-item-desc">Hearty beef shank simmered with sweet corn on the cob, yuca root, green plantains, chayote squash, cabbage, and fresh mint. Served with rice and tortillas.</p>
          <span class="salvadorena-item-tag">Saturday &amp; Sunday Feature</span>
        </div>

        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Sopa de Pata (Mondongo &amp; Cow's Foot Broth)</h4>
            <span class="salvadorena-item-price">$15.99</span>
          </div>
          <p class="salvadorena-item-desc">Rich gelatinous marrow and tripe soup seasoned with achiote, sweet corn, green plantains, and cabbage, garnished with fresh cilantro and lime juice.</p>
          <span class="salvadorena-item-tag">Weekend Traditional Specialty</span>
        </div>

        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Sopa de Gallina India</h4>
            <span class="salvadorena-item-price">$14.50</span>
          </div>
          <p class="salvadorena-item-desc">Free-range chicken broth infused with aromatic garlic, bell peppers, fresh mint, and vegetables, served alongside grilled chicken quarters and seasoned rice.</p>
        </div>

        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Tamal de Pollo en Hoja de Platano</h4>
            <span class="salvadorena-item-price">$3.50</span>
          </div>
          <p class="salvadorena-item-desc">Silky smooth corn masa filled with seasoned chicken, potatoes, chickpeas, and olives, wrapped and steamed inside fragrant banana leaves.</p>
        </div>
      </div>
    </div>

    <!-- Group 5: Bebidas -->
    <div class="salvadorena-menu-group" id="tab-bebidas">
      <div class="salvadorena-section-title">
        <h2>Bebidas Tipicas &amp; Refrescos Naturales</h2>
        <p>Hand-blended artisanal refreshments and imported Salvadoran favorites.</p>
      </div>

      <div class="salvadorena-grid-2">
        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Horchata de Morro Tradicional</h4>
            <span class="salvadorena-item-price">$4.00</span>
          </div>
          <p class="salvadorena-item-desc">Ground seeds of the morro tree roasted with rice, cinnamon, cacao, coriander seeds, and vanilla. A rich, chocolatey, spiced Salvadoran staple.</p>
          <span class="salvadorena-item-tag">House Crafted Daily</span>
        </div>

        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Fresco de Ensalada de Frutas</h4>
            <span class="salvadorena-item-price">$4.25</span>
          </div>
          <p class="salvadorena-item-desc">Refreshing fruit drink made with pineapple juice, passionfruit syrup, watercress, and finely diced crisp apples, mamey, and pineapple bits.</p>
        </div>

        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Fresco de Cebada Rosada</h4>
            <span class="salvadorena-item-price">$3.75</span>
          </div>
          <p class="salvadorena-item-desc">Spiced barley beverage flavored with strawberry essence, cinnamon, cloves, and vanilla, served ice-cold.</p>
        </div>

        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Kolashampan Salvadoran Soda</h4>
            <span class="salvadorena-item-price">$2.99</span>
          </div>
          <p class="salvadorena-item-desc">The iconic sugarcane-based carbonated soft drink of El Salvador with a unique sweet cream soda citrus profile.</p>
        </div>

        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Cafe de Palo / Cafe con Leche</h4>
            <span class="salvadorena-item-price">$2.75</span>
          </div>
          <p class="salvadorena-item-desc">Dark roasted Salvadoran highland coffee brewed fresh, served hot or blended with steamed whole milk.</p>
        </div>

        <div class="salvadorena-menu-item">
          <div class="salvadorena-item-header">
            <h4>Agua de Tamarindo Natural</h4>
            <span class="salvadorena-item-price">$3.50</span>
          </div>
          <p class="salvadorena-item-desc">Tart and sweet natural tamarind pulp steeped and sweetened with pure cane sugar.</p>
        </div>
      </div>
    </div>

    <!-- Bottom Order CTA -->
    <div class="salvadorena-cta-banner" style="margin-top:50px;">
      <h2>Ready for Sizzling Pupusas or Fresh Pan Dulce?</h2>
      <p>Order takeout for pickup or dine in with family at 4325 South Blvd in Charlotte.</p>
      <div class="salvadorena-cta-btns">
        <a href="tel:7045254550" class="salvadorena-btn-hero-primary">Call to Order (704) 525-4550</a>
        <a href="pupusa-catering-and-bakery-boxes.html" class="salvadorena-btn-hero-secondary">View Catering Boxes</a>
      </div>
    </div>
  </main>

{footer_html()}'''

# 3. pupusas-artesanales-and-curtido.html
pupusas_page_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pupusas Artesanales &amp; Curtido | Restaurante Y Panaderia Salvadorena</title>
  <meta name="description" content="Discover the artisanal craft of Salvadoran pupusas made on corn or rice flour masa, accompanied by homemade cabbage curtido and fresh tomato salsa.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
{header_html("pupusas-artesanales-and-curtido.html")}

  <section class="salvadorena-hero" style="padding: 50px 20px;">
    <div class="salvadorena-hero-inner">
      <span class="salvadorena-hero-pill">Artisanal Pupuseria Tradition</span>
      <h1>The Craft of the Salvadoran Pupusa</h1>
      <p>Every pupusa at La Salvadorena is molded by hand upon order, packed with authentic Salvadoran fillings, and seared to golden perfection on our smoking hot comal griddle.</p>
    </div>
  </section>

  <main class="salvadorena-container">
    <div class="salvadorena-spotlight">
      <div>
        <img src="images/pupusas.jpg" alt="Freshly griddled corn and rice flour pupusas with melting cheese" class="salvadorena-card-image" style="height:100%; object-fit:cover;">
      </div>
      <div class="salvadorena-spotlight-content">
        <span class="salvadorena-card-badge">Two Heritage Masa Styles</span>
        <h3>Corn Masa vs. Rice Flour (Masa de Arroz)</h3>
        <p>In El Salvador, pupusa lovers passionately appreciate both classical heirloom corn and Olocuilta-style rice flour pupusas. At La Salvadorena, we master both daily:</p>
        <ul style="margin: 15px 0 20px 20px; color: var(--salvadorena-text-muted); font-size: 0.95rem;">
          <li style="margin-bottom:8px;"><strong>Masa de Maiz (Corn):</strong> Earthy, robust, with a slightly toasted exterior and chewy tender center.</li>
          <li style="margin-bottom:8px;"><strong>Masa de Arroz (Rice):</strong> Silky smooth, delicately crisp on the griddle edges, and naturally gluten-free. Originating from Olocuilta, La Paz.</li>
        </ul>
        <p>Specify your preferred masa when ordering. Each pupusa is hand-patted and grilled fresh.</p>
      </div>
    </div>

    <div class="salvadorena-section-title" style="margin-top:60px;">
      <h2>Authentic Fillings &amp; Salvadoran Ingredients</h2>
      <p>We source authentic ingredients to ensure our pupusas taste exactly like home in San Salvador, Santa Ana, or San Miguel.</p>
    </div>

    <div class="salvadorena-grid-3">
      <div class="salvadorena-card" style="padding:28px;">
        <span class="salvadorena-card-badge">Imported Herb</span>
        <h4 style="color:var(--salvadorena-primary-dark); margin:12px 0; font-size:1.2rem;">Loroco Flower Buds</h4>
        <p style="color:var(--salvadorena-text-muted); font-size:0.95rem;">The edible green flower bud of <em>Fernaldia pandurata</em>, indigenous to Central America. Its unique herbaceous, floral flavor blends sublimely with hot melted quesillo.</p>
      </div>

      <div class="salvadorena-card" style="padding:28px;">
        <span class="salvadorena-card-badge">Artisanal Dairy</span>
        <h4 style="color:var(--salvadorena-primary-dark); margin:12px 0; font-size:1.2rem;">Quesillo Salvadoreno</h4>
        <p style="color:var(--salvadorena-text-muted); font-size:0.95rem;">A semi-soft artisanal cheese prized across Central America for its stretchy melt, mild tang, and rich milky creaminess that bubbles through the pupusa crust on the comal.</p>
      </div>

      <div class="salvadorena-card" style="padding:28px;">
        <span class="salvadorena-card-badge">Slow Simmered</span>
        <h4 style="color:var(--salvadorena-primary-dark); margin:12px 0; font-size:1.2rem;">Chicharron Molido</h4>
        <p style="color:var(--salvadorena-text-muted); font-size:0.95rem;">Pork shoulder braised until fork-tender, seasoned with ripe tomatoes, garlic, and sweet bell peppers, then ground into a smooth, savory filling that stays moist during griddling.</p>
      </div>
    </div>

    <!-- Curtido and Salsa Section -->
    <div class="salvadorena-section-title" style="margin-top:60px;">
      <h2>The Essential Companions: Curtido &amp; Salsa Roja</h2>
      <p>No pupusa is complete without generous heaps of tangy pickled slaw and warm tomato salsa.</p>
    </div>

    <div class="salvadorena-grid-2">
      <div class="salvadorena-card" style="padding:32px;">
        <h3 style="color:var(--salvadorena-primary-dark); margin-bottom:14px; font-size:1.35rem;">House Fermented Curtido</h3>
        <p style="color:var(--salvadorena-text-muted); font-size:0.95rem; margin-bottom:12px;">Our curtido is prepared fresh daily with crisp green cabbage, julienned sweet carrots, yellow onion, sliced jalapenos, and wild Mexican oregano steeped in a light, refreshing apple cider vinegar pickle.</p>
        <p style="color:var(--salvadorena-text-muted); font-size:0.95rem;">The crunchy acidity balances the rich molten cheese and savory chicharron perfectly. We provide abundant curtido with every dine-in table and takeout container.</p>
      </div>

      <div class="salvadorena-card" style="padding:32px;">
        <h3 style="color:var(--salvadorena-primary-dark); margin-bottom:14px; font-size:1.35rem;">Warm Salsa de Tomate Casera</h3>
        <p style="color:var(--salvadorena-text-muted); font-size:0.95rem; margin-bottom:12px;">Unlike Mexican table salsas, authentic Salvadoran pupusa salsa is a smooth, cooked tomato sauce simmered with Roma tomatoes, sweet bell peppers, celery, garlic, and fresh herbs without overwhelming heat.</p>
        <p style="color:var(--salvadorena-text-muted); font-size:0.95rem;">Poured liberally over hot pupusas and crunchy curtido, it brings every bite together in harmonious comfort.</p>
      </div>
    </div>

    <!-- How to Eat Pupusas Guide -->
    <div class="salvadorena-card" style="margin-top:40px; padding:36px; background-color:var(--salvadorena-surface-card); border: 2px solid var(--salvadorena-border);">
      <h3 style="color:var(--salvadorena-primary-dark); margin-bottom:16px;">How to Enjoy a Pupusa Like a Salvadoran</h3>
      <ol style="margin-left:24px; color:var(--salvadorena-text); font-size:1rem; line-height:1.8;">
        <li><strong>No Utensils Needed:</strong> Tear off a small piece of steaming pupusa with your fingers.</li>
        <li><strong>Pile the Curtido:</strong> Top each bite with a generous pinch of crunchy curtido.</li>
        <li><strong>Drizzle the Salsa:</strong> Spoon warm tomato salsa over the top.</li>
        <li><strong>Savor the Contrast:</strong> Experience the harmony of crispy masa, gooey hot cheese, crunchy slaw, and soothing tomato broth in every bite.</li>
      </ol>
    </div>

    <div class="salvadorena-cta-banner" style="margin-top:50px;">
      <h2>Craving Hot Fresh Pupusas?</h2>
      <p>Visit our pupusa griddle station at 4325 South Blvd or call ahead for quick pickup.</p>
      <div class="salvadorena-cta-btns">
        <a href="tel:7045254550" class="salvadorena-btn-hero-primary">Call (704) 525-4550</a>
        <a href="menu.html" class="salvadorena-btn-hero-secondary">View Menu &amp; Varieties</a>
      </div>
    </div>
  </main>

{footer_html()}'''

with open(os.path.join(DIR, "menu.html"), "w", encoding="utf-8") as f:
    f.write(menu_content)
print("Wrote menu.html")

with open(os.path.join(DIR, "pupusas-artesanales-and-curtido.html"), "w", encoding="utf-8") as f:
    f.write(pupusas_page_content)
print("Wrote pupusas-artesanales-and-curtido.html")
