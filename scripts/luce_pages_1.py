import os
from luce_core import wrap_page

index_content = """
    <section class="luce-hero">
      <div class="luce-hero-content">
        <span class="luce-badge luce-badge-gold">Conte Restaurant Group &bull; Truist Center Plaza</span>
        <h1 class="luce-hero-title">Tuscan Culinary Artistry in <span>Uptown Charlotte</span></h1>
        <p class="luce-hero-lead">Handmade scratch pastas, slow-braised wild boar ragù, prime veal ossobuco, an exquisite Italian wine cellar, and dining beneath genuine Murano glass.</p>
        <div class="luce-hero-actions">
          <a href="menu.html" class="luce-btn luce-btn-primary">View Dinner Menu</a>
          <a href="handmade-pastas-and-tuscan-classics.html" class="luce-btn luce-btn-secondary">Explore Tasting Menu</a>
          <a href="private-dining-and-plaza-events.html" class="luce-btn luce-btn-gold">Private Dining &amp; Plaza</a>
        </div>
        <div class="luce-hero-highlights">
          <div class="luce-highlight-box">
            <div class="luce-highlight-title">Scratch Primi</div>
            <div class="luce-highlight-desc">Hand-rolled pappardelle, delicate tagliolini, and potato gnocchi crafted daily.</div>
          </div>
          <div class="luce-highlight-box">
            <div class="luce-highlight-title">Tuscan Cellar</div>
            <div class="luce-highlight-desc">Curated selection of Super Tuscans, Brunello di Montalcino, and Piedmont Barolos.</div>
          </div>
          <div class="luce-highlight-box">
            <div class="luce-highlight-title">Plaza Patio &amp; Murano</div>
            <div class="luce-highlight-desc">Romantic indoor chandelier room and intimate covered Truist Center Plaza patio.</div>
          </div>
          <div class="luce-highlight-box">
            <div class="luce-highlight-title">Evening Validation</div>
            <div class="luce-highlight-desc">Complimentary 2-hour parking validation in Truist Center deck after 5:00 PM.</div>
          </div>
        </div>
      </div>
    </section>

    <div class="luce-container">
      <div class="luce-info-box" style="margin-top: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
          <div>
            <span class="luce-badge" style="margin-bottom: 6px;">Fine Dining Tradition</span>
            <h2 style="font-family: var(--luce-font-display); color: var(--luce-charcoal); font-size: 1.7rem;">An Intimate Italian Escape in Truist Center Plaza</h2>
            <p style="color: var(--luce-text-muted); font-size: 0.95rem;">Tucked within the plaza of 214 N Tryon Street, Luce offers fine Italian hospitality, white tablecloth service, and authentic regional culinary heritage.</p>
          </div>
          <a href="visit.html" class="luce-btn luce-btn-primary">Find Location &amp; Parking &rarr;</a>
        </div>
      </div>

      <section class="luce-section">
        <div class="luce-section-header">
          <span class="luce-badge">Chef's Signatures</span>
          <h2 class="luce-title">Timeless Flavors of Florence &amp; Milan</h2>
          <p class="luce-subtitle">Prepared with imported Italian flours, San Marzano tomatoes, Parmigiano-Reggiano, and prime heritage meats.</p>
        </div>

        <div class="luce-grid-3">
          <div class="luce-card">
            <div class="luce-card-img-wrap">
              <img src="images/handmade-pappardelle-pasta.jpg" alt="Pappardelle al Cinghiale" class="luce-card-img">
              <span class="luce-card-tag">Signature Primi</span>
            </div>
            <div class="luce-card-body">
              <div class="luce-card-header">
                <h3 class="luce-card-title">Pappardelle al Cinghiale</h3>
                <span class="luce-card-price">$28.00</span>
              </div>
              <p class="luce-card-desc">Wide ribbon egg pasta hand-rolled in-house, tossed in a slow-braised wild boar ragù with juniper berries, Chianti red wine, and aged pecorino toscano.</p>
              <div class="luce-card-meta">
                <span class="luce-meta-pill">Handmade Fresh</span>
                <span class="luce-meta-pill">Tuscan Heritage</span>
              </div>
              <a href="handmade-pastas-and-tuscan-classics.html" class="luce-btn luce-btn-primary" style="text-align: center; width: 100%;">View Pastas</a>
            </div>
          </div>

          <div class="luce-card">
            <div class="luce-card-img-wrap">
              <img src="images/prime-veal-ossobuco.jpg" alt="Ossobuco di Vitello alla Milanese" class="luce-card-img">
              <span class="luce-card-tag">Secondi Piatti</span>
            </div>
            <div class="luce-card-body">
              <div class="luce-card-header">
                <h3 class="luce-card-title">Ossobuco alla Milanese</h3>
                <span class="luce-card-price">$44.00</span>
              </div>
              <p class="luce-card-desc">Tender braised Dutch veal shank simmered in white wine and aromatic mirepoix, served with creamy saffron saffron risotto and fresh citrus gremolata.</p>
              <div class="luce-card-meta">
                <span class="luce-meta-pill">Saffron Risotto</span>
                <span class="luce-meta-pill">Braised Veal Shank</span>
              </div>
              <a href="handmade-pastas-and-tuscan-classics.html" class="luce-btn luce-btn-primary" style="text-align: center; width: 100%;">Tasting Pairings</a>
            </div>
          </div>

          <div class="luce-card">
            <div class="luce-card-img-wrap">
              <img src="images/italian-wine-cellar-cocktails.jpg" alt="Italian Wine Cellar and Aperitivi" class="luce-card-img">
              <span class="luce-card-tag">Sommelier Cellar</span>
            </div>
            <div class="luce-card-body">
              <div class="luce-card-header">
                <h3 class="luce-card-title">The Italian Cellar</h3>
                <span class="luce-card-price">Curated</span>
              </div>
              <p class="luce-card-desc">An encyclopedic collection of premier Italian vintages spanning Tuscany, Piedmont, and the Veneto, alongside bespoke Negronis and herbal Amari.</p>
              <div class="luce-card-meta">
                <span class="luce-meta-pill">Super Tuscans</span>
                <span class="luce-meta-pill">Brunello DOCG</span>
              </div>
              <a href="wine-cellar-and-aperitivo-cocktails.html" class="luce-btn luce-btn-secondary" style="text-align: center; width: 100%;">Explore Wine List</a>
            </div>
          </div>
        </div>
      </section>
    </div>
"""

menu_content = """
    <div class="luce-container">
      <div class="luce-section-header">
        <span class="luce-badge">Cucina Toscana</span>
        <h1 class="luce-title">Luce Ristorante Dinner Menu</h1>
        <p class="luce-subtitle">Seasonal Italian fine dining prepared by executive culinary artisans in Truist Center Plaza.</p>
      </div>

      <div class="luce-grid-2">
        <!-- Antipasti & Insalate -->
        <div class="luce-card" style="padding: 28px;">
          <h3 class="luce-card-title" style="margin-bottom: 20px; border-bottom: 2px solid var(--luce-border); padding-bottom: 10px;">Antipasti &amp; Insalate</h3>
          
          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--luce-charcoal);">Burrata Pugliese con Prosciutto</span>
              <span style="color: var(--luce-wine);">$18.00</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--luce-text-muted);">Creamy imported burrata cheese, 24-month aged Prosciutto di Parma, roasted cherry tomatoes, balsamic glaze, and grilled crostini.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--luce-charcoal);">Pepata di Cozze e Vongole</span>
              <span style="color: var(--luce-wine);">$19.50</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--luce-text-muted);">Steamed Mediterranean mussels and Manila clams in a spicy garlic, white wine, crushed black pepper, and San Marzano tomato broth.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--luce-charcoal);">Polpettine di Manzo</span>
              <span style="color: var(--luce-wine);">$16.00</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--luce-text-muted);">Handmade prime beef and veal meatballs braised in rich tomato ragù, topped with shaved ricotta salata and fresh basil.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--luce-charcoal);">Insalata Spinaci e Pere</span>
              <span style="color: var(--luce-wine);">$14.00</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--luce-text-muted);">Baby spinach, sliced d'Anjou pears, candied walnuts, crumbled gorgonzola dolce, and aged balsamic shallot vinaigrette.</p>
          </div>
        </div>

        <!-- Primi Hand-Made Pastas -->
        <div class="luce-card" style="padding: 28px;">
          <h3 class="luce-card-title" style="margin-bottom: 20px; border-bottom: 2px solid var(--luce-border); padding-bottom: 10px;">Primi Piatti (Fresh Pastas)</h3>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--luce-charcoal);">Pappardelle al Cinghiale</span>
              <span style="color: var(--luce-wine);">$28.00</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--luce-text-muted);">House-made wide egg ribbon pasta tossed with slow-braised wild boar ragù, Chianti wine reduction, and rosemary pecorino.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--luce-charcoal);">Tagliolini al Tartufo Nero</span>
              <span style="color: var(--luce-wine);">$32.00</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--luce-text-muted);">Delicate egg tagliolini tossed with European black summer truffle butter, Parmigiano-Reggiano Vacche Rosse, and cracked pepper.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--luce-charcoal);">Ravioli di Vitello</span>
              <span style="color: var(--luce-wine);">$29.00</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--luce-text-muted);">Braised veal and wild mushroom stuffed ravioli in a velvety brown butter sage and veal jus reduction.</p>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem;">
              <span style="color: var(--luce-charcoal);">Gnocchi alla Sorrentina</span>
              <span style="color: var(--luce-wine);">$25.00</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--luce-text-muted);">Handmade potato gnocchi baked with San Marzano plum tomato sauce, melted buffalo mozzarella, and fresh sweet basil.</p>
          </div>
        </div>
      </div>

      <!-- Secondi Piatti -->
      <div class="luce-grid-2" style="margin-top: 30px;">
        <div class="luce-card" style="padding: 28px;">
          <h3 class="luce-card-title" style="margin-bottom: 16px;">Secondi Piatti (Carne e Pesce)</h3>
          <div style="margin-bottom: 14px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Ossobuco alla Milanese</span>
              <span style="color: var(--luce-wine);">$44.00</span>
            </div>
            <small style="color: var(--luce-text-muted);">Braised veal shank in white wine mirepoix, saffron risotto, and lemon herb gremolata.</small>
          </div>
          <div style="margin-bottom: 14px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Filetto di Manzo al Barolo</span>
              <span style="color: var(--luce-wine);">$48.00</span>
            </div>
            <small style="color: var(--luce-text-muted);">Prime 8oz beef tenderloin with Barolo wine reduction, truffle potato puree, and grilled asparagus.</small>
          </div>
          <div>
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Branzino Mediterraneo al Forno</span>
              <span style="color: var(--luce-wine);">$39.00</span>
            </div>
            <small style="color: var(--luce-text-muted);">Pan-roasted Mediterranean sea bass fillet with caperberries, cherry tomatoes, and Sicilian lemon emulsion.</small>
          </div>
        </div>

        <div class="luce-card" style="padding: 28px;">
          <h3 class="luce-card-title" style="margin-bottom: 16px;">Dolci &amp; Digestivi</h3>
          <div style="margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Tiramisù Tradizionale</span>
              <span style="color: var(--luce-wine);">$12.00</span>
            </div>
            <small style="color: var(--luce-text-muted);">Espresso-soaked ladyfingers, whipped mascarpone cream, and Valrhona cocoa powder.</small>
          </div>
          <div style="margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Panna Cotta ai Frutti di Bosco</span>
              <span style="color: var(--luce-wine);">$11.00</span>
            </div>
            <small style="color: var(--luce-text-muted);">Vanilla bean custard cream served with wild raspberry coulis and fresh mint.</small>
          </div>
          <div>
            <div style="display: flex; justify-content: space-between; font-weight: 700;">
              <span>Italian Digestivi (Grappa &amp; Amari)</span>
              <span style="color: var(--luce-wine);">$14.00 &ndash; $22.00</span>
            </div>
            <small style="color: var(--luce-text-muted);">Nonino Grappa di Moscato, Amaro Nonino, Montenegro, and Fernet-Branca.</small>
          </div>
        </div>
      </div>
    </div>
"""

pastas_content = """
    <div class="luce-container">
      <div class="luce-section-header">
        <span class="luce-badge">Sommelier &amp; Tasting Studio</span>
        <h1 class="luce-title">Handmade Pastas &amp; Tuscan Course Selector</h1>
        <p class="luce-subtitle">Curate your personalized multi-course Tuscan dining experience. Select your antipasto, handmade primi pasta, prime secondo, and optional sommelier wine flight.</p>
      </div>

      <div class="luce-builder-card luce-tasting-builder">
        <div class="luce-builder-step">
          <div class="luce-step-label">
            <span class="luce-step-number">1</span>
            <span>Antipasti Course</span>
          </div>
          <div class="luce-options-grid">
            <button class="luce-opt-btn luce-opt-antipasti active" data-name="Burrata Pugliese con Prosciutto" data-price="18.00">Burrata con Prosciutto - $18</button>
            <button class="luce-opt-btn luce-opt-antipasti" data-name="Pepata di Cozze e Vongole" data-price="19.50">Cozze e Vongole - $19.50</button>
            <button class="luce-opt-btn luce-opt-antipasti" data-name="Polpettine di Manzo e Vitello" data-price="16.00">Polpettine di Manzo - $16</button>
            <button class="luce-opt-btn luce-opt-antipasti" data-name="Carpaccio di Manzo al Tartufo" data-price="18.50">Carpaccio al Tartufo - $18.50</button>
          </div>
        </div>

        <div class="luce-builder-step">
          <div class="luce-step-label">
            <span class="luce-step-number">2</span>
            <span>Primi Piatti (Hand-Rolled Pasta)</span>
          </div>
          <div class="luce-options-grid">
            <button class="luce-opt-btn luce-opt-primi active" data-name="Pappardelle al Cinghiale" data-price="28.00">Pappardelle Cinghiale - $28</button>
            <button class="luce-opt-btn luce-opt-primi" data-name="Tagliolini al Tartufo Nero" data-price="32.00">Tagliolini al Tartufo - $32</button>
            <button class="luce-opt-btn luce-opt-primi" data-name="Ravioli di Vitello e Funghi" data-price="29.00">Ravioli di Vitello - $29</button>
            <button class="luce-opt-btn luce-opt-primi" data-name="Gnocchi alla Sorrentina" data-price="25.00">Gnocchi Sorrentina - $25</button>
          </div>
        </div>

        <div class="luce-builder-step">
          <div class="luce-step-label">
            <span class="luce-step-number">3</span>
            <span>Secondi Piatti (Carne e Pesce)</span>
          </div>
          <div class="luce-options-grid">
            <button class="luce-opt-btn luce-opt-secondi active" data-name="Ossobuco di Vitello alla Milanese" data-price="44.00">Ossobuco alla Milanese - $44</button>
            <button class="luce-opt-btn luce-opt-secondi" data-name="Filetto di Manzo al Barolo" data-price="48.00">Filetto al Barolo - $48</button>
            <button class="luce-opt-btn luce-opt-secondi" data-name="Branzino Mediterraneo al Forno" data-price="39.00">Branzino al Forno - $39</button>
          </div>
        </div>

        <div class="luce-builder-step">
          <div class="luce-step-label">
            <span class="luce-step-number">4</span>
            <span>Sommelier Italian Wine Pairing</span>
          </div>
          <div class="luce-options-grid">
            <button class="luce-opt-btn luce-opt-wine active" data-name="No Wine Pairing Selected" data-price="0.00">No Pairing</button>
            <button class="luce-opt-btn luce-opt-wine" data-name="Classico Italian Flight (Chianti & Vermentino)" data-price="38.00">Classico Flight (+$38)</button>
            <button class="luce-opt-btn luce-opt-wine" data-name="Riserva Sommelier Flight (Brunello & Barolo)" data-price="65.00">Riserva Grand Cru (+$65)</button>
          </div>
        </div>

        <div class="luce-builder-step">
          <div class="luce-step-label">
            <span class="luce-step-number">5</span>
            <span>Dolci Finale</span>
          </div>
          <div class="luce-options-grid">
            <button id="luce-toggle-dolci" class="luce-opt-btn active">Tiramisù Tradizionale (+$12.00)</button>
          </div>
        </div>

        <div class="luce-summary-panel">
          <div class="luce-summary-metrics">
            <div class="luce-metric-item">
              <span class="luce-metric-label">Tasting Total</span>
              <span id="luce-builder-price" class="luce-metric-val">$102.00</span>
            </div>
          </div>
          <div style="flex-basis: 100%; border-top: 1px solid rgba(255,255,255,0.15); padding-top: 16px; margin-top: 10px;">
            <strong style="color: #fed7aa; display: block; font-size: 0.85rem; text-transform: uppercase;">Curated Multi-Course Journey:</strong>
            <p id="luce-builder-summary" style="color: #ffffff; font-size: 1rem; margin-top: 4px;">Burrata Pugliese con Prosciutto di Parma followed by Pappardelle al Cinghiale and Ossobuco di Vitello alla Milanese + Espresso Tiramisù Tradizionale. Served with warm Tuscan focaccia and Sicilian olive oil.</p>
          </div>
          <div style="flex-basis: 100%; margin-top: 16px;">
            <a href="tel:7043449222" class="luce-btn luce-btn-secondary">Reserve Table for This Experience</a>
          </div>
        </div>
      </div>
    </div>
"""

pages = {
    "index.html": ("Home", index_content),
    "menu.html": ("Full Menu", menu_content),
    "handmade-pastas-and-tuscan-classics.html": ("Handmade Pastas", pastas_content)
}

for filename, (label, content) in pages.items():
    html = wrap_page(label, filename, content)
    with open(os.path.join("luce-ristorante", filename), "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"Generated {filename}")
