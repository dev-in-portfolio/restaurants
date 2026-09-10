# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\scripts")
from valhalla_builder import header_html, footer_html

DIR = r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\valhalla-pub-and-eatery"

# 1. index.html
index_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Valhalla Pub &amp; Eatery | Scandinavian Viking Tavern Uptown Charlotte</title>
  <meta name="description" content="Authentic Viking &amp; Scandinavian-inspired pub in historic Brevard Court in Uptown Charlotte NC. Scratch-made Norwegian meatballs, custom burgers, craft taps, and patio.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
{header_html("index.html")}

  <section class="valhalla-hero">
    <div class="valhalla-hero-inner">
      <span class="valhalla-hero-pill">Historic Brevard Court Uptown Charlotte</span>
      <h1>Nordic Comfort, Viking Burgers &amp; Craft Taps</h1>
      <p>Gather your clan in Uptown Charlotte's one-of-a-kind Scandinavian tavern. From scratch-simmered Norwegian meatballs with lingonberries and custom beef-pork Viking burgers to North Sea fish &amp; chips and open-air courtyard patio drinking.</p>
      <div class="valhalla-hero-actions">
        <a href="menu.html" class="valhalla-btn-hero-primary">Explore Tavern Menu</a>
        <a href="scandinavian-pub-fare-and-meatballs.html" class="valhalla-btn-hero-secondary">Nordic Specialties</a>
        <a href="brevard-court-patio-and-taproom.html" class="valhalla-btn-hero-secondary">Brevard Court Patio</a>
      </div>
    </div>
  </section>

  <main class="valhalla-container">
    <div class="valhalla-section-title">
      <h2>Hearty Fare Fit for Warriors</h2>
      <p>Made-from-scratch pub comfort inspired by Scandinavian heritage and classic tavern hospitality.</p>
    </div>

    <div class="valhalla-grid-3">
      <div class="valhalla-card">
        <img src="images/swedish-meatballs.jpg" alt="Norwegian Meatballs plate with rich cream gravy and lingonberries" class="valhalla-card-image">
        <div class="valhalla-card-body">
          <span class="valhalla-card-badge">Nordic Heritage Recipe</span>
          <h3>Norwegian Meatball Plate</h3>
          <p>Hand-rolled beef and pork meatballs simmered in a velvety spiced cream gravy, served over buttery Yukon gold mashed potatoes with tart imported Swedish lingonberry jam.</p>
          <div class="valhalla-card-footer">
            <span class="valhalla-price">$16.50</span>
            <a href="scandinavian-pub-fare-and-meatballs.html" class="valhalla-btn-cta">Learn More</a>
          </div>
        </div>
      </div>

      <div class="valhalla-card">
        <img src="images/viking-burger.jpg" alt="Thick Viking burger with smoked gouda and bacon on brioche" class="valhalla-card-image">
        <div class="valhalla-card-body">
          <span class="valhalla-card-badge">Proprietary Tavern Grind</span>
          <h3>The Viking Blend Burger</h3>
          <p>Custom ground chuck, brisket, and seasoned pork patty topped with melted smoked gouda, applewood smoked bacon, caramelized sweet onions, and house garlic remoulade on brioche.</p>
          <div class="valhalla-card-footer">
            <span class="valhalla-price">$15.50</span>
            <a href="menu.html" class="valhalla-btn-cta">See Handhelds</a>
          </div>
        </div>
      </div>

      <div class="valhalla-card">
        <img src="images/fish-chips-wings.jpg" alt="Beer battered Atlantic cod fish and chips with crispy wings" class="valhalla-card-image">
        <div class="valhalla-card-body">
          <span class="valhalla-card-badge">North Sea Classic</span>
          <h3>Crispy Ale-Battered Fish &amp; Chips</h3>
          <p>Flaky Atlantic cod dipped in local craft beer batter and fried golden, served with hand-cut sea salt pub fries, creamy remoulade slaw, and house caper tartar sauce.</p>
          <div class="valhalla-card-footer">
            <span class="valhalla-price">$16.00</span>
            <a href="menu.html" class="valhalla-btn-cta">View Pub Fare</a>
          </div>
        </div>
      </div>
    </div>

    <!-- Spotlight Section -->
    <div class="valhalla-spotlight">
      <div>
        <img src="images/brevard-patio-pretzel.jpg" alt="Giant Bavarian soft pretzel board with beer cheese and mustard on patio" class="valhalla-card-image" style="height:100%; object-fit:cover;">
      </div>
      <div class="valhalla-spotlight-content">
        <span class="valhalla-card-badge">Brevard Court Cobblestone Alley</span>
        <h3>Open-Air Patio Dining &amp; Gameday Spirits</h3>
        <p>Tucked into historic Brevard Court directly across from Romare Bearden Park and Truist Field, Valhalla offers one of Uptown's most vibrant outdoor European cobblestone courtyards. Bring your dog, grab a picnic table, and enjoy 10 rotating craft taps from top North Carolina breweries.</p>
        <p>The premier meeting hub for Charlotte FC matchdays, Carolina Panthers tailgates, and lively weekend gatherings.</p>
        <div style="margin-top:20px;">
          <a href="brevard-court-patio-and-taproom.html" class="valhalla-btn-cta">Explore Patio &amp; Taps</a>
        </div>
      </div>
    </div>

    <!-- Highlights -->
    <div class="valhalla-section-title" style="margin-top:60px;">
      <h2>Why Charlotte Drinks &amp; Feasts at Valhalla</h2>
      <p>True Scandinavian hospitality meets Uptown energy.</p>
    </div>

    <div class="valhalla-grid-3">
      <div class="valhalla-card" style="padding:28px;">
        <h4 style="color:var(--valhalla-primary-dark); margin-bottom:12px; font-size:1.25rem;">100% From-Scratch Kitchen</h4>
        <p style="color:var(--valhalla-text-muted); font-size:0.95rem;">From our slow-simmered rich cream gravies and house-smoked jumbo wings to hand-patted burgers and fresh berry purees, we never cut corners on quality.</p>
      </div>
      <div class="valhalla-card" style="padding:28px;">
        <h4 style="color:var(--valhalla-primary-dark); margin-bottom:12px; font-size:1.25rem;">10 Carolina Craft Taps</h4>
        <p style="color:var(--valhalla-text-muted); font-size:0.95rem;">We rotate a curated lineup of IPAs, crisp lagers, seasonal stouts, hard ciders, and authentic Viking meads poured ice-cold at our solid wood bar.</p>
      </div>
      <div class="valhalla-card" style="padding:28px;">
        <h4 style="color:var(--valhalla-primary-dark); margin-bottom:12px; font-size:1.25rem;">Clan Feast Platters</h4>
        <p style="color:var(--valhalla-text-muted); font-size:0.95rem;">Feeding your team or tailgating at Bank of America Stadium? Order large shareable meatball pans, wing crates, and pretzel boards ready for fast pickup.</p>
      </div>
    </div>

    <!-- CTA Section -->
    <div class="valhalla-cta-banner" style="margin-top:50px;">
      <h2>Raise a Horn with Us in Brevard Court</h2>
      <p>Located at 317 S Church St in Uptown Charlotte. Dine inside our Viking hall or relax on the cobblestone patio.</p>
      <div class="valhalla-cta-btns">
        <a href="tel:7043323273" class="valhalla-btn-hero-primary">Call (704) 332-3273</a>
        <a href="visit.html" class="valhalla-btn-hero-secondary">View Hours &amp; Directions</a>
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
  <title>Tavern Menu | Valhalla Pub &amp; Eatery Uptown Charlotte</title>
  <meta name="description" content="Explore the full menu at Valhalla Pub & Eatery in Charlotte NC: Norwegian meatballs, Viking blend burgers, fish & chips, smoked wings, and craft beers on tap.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
{header_html("menu.html")}

  <section class="valhalla-hero" style="padding: 50px 20px;">
    <div class="valhalla-hero-inner">
      <span class="valhalla-hero-pill">Made From Scratch Daily</span>
      <h1>Full Tavern &amp; Taproom Menu</h1>
      <p>Hearty Scandinavian classics, proprietary blend burgers, crispy pub favorites, shareable boards, and ice-cold craft beers.</p>
    </div>
  </section>

  <main class="valhalla-container">
    <div class="valhalla-tabs">
      <button class="valhalla-tab-btn active" data-target="tab-scandinavian">Nordic Specialties</button>
      <button class="valhalla-tab-btn" data-target="tab-burgers">Viking Burgers &amp; Sandwiches</button>
      <button class="valhalla-tab-btn" data-target="tab-pubfare">Pub Classics &amp; Fish</button>
      <button class="valhalla-tab-btn" data-target="tab-wings">Smoked Wings &amp; Boards</button>
      <button class="valhalla-tab-btn" data-target="tab-drinks">Craft Taps &amp; Cocktails</button>
    </div>

    <!-- Group 1: Scandinavian -->
    <div class="valhalla-menu-group active" id="tab-scandinavian">
      <div class="valhalla-section-title">
        <h2>Scandinavian Specialties &amp; Comfort Fare</h2>
        <p>Traditional Norse family recipes prepared from scratch in our Uptown kitchen.</p>
      </div>

      <div class="valhalla-grid-2">
        <div class="valhalla-menu-item">
          <div class="valhalla-item-header">
            <h4>Norwegian Meatball Plate</h4>
            <span class="valhalla-item-price">$16.50</span>
          </div>
          <p class="valhalla-item-desc">Seasoned ground beef and pork meatballs simmered in rich Nordic cream gravy, served with Yukon gold mashed potatoes and imported Swedish lingonberry jam.</p>
          <div class="valhalla-item-tags">
            <span class="valhalla-tag valhalla-tag-nordic">Nordic Classic</span>
            <span class="valhalla-tag valhalla-tag-signature">House Favorite</span>
          </div>
        </div>

        <div class="valhalla-menu-item">
          <div class="valhalla-item-header">
            <h4>Scandinavian Smoked Salmon Toast</h4>
            <span class="valhalla-item-price">$14.50</span>
          </div>
          <p class="valhalla-item-desc">House-cured Atlantic smoked salmon on toasted dark rye bread with lemon-herb dill cream cheese, shaved red onions, and nonpareil capers.</p>
          <div class="valhalla-item-tags">
            <span class="valhalla-tag valhalla-tag-nordic">Smørrebrød Style</span>
          </div>
        </div>

        <div class="valhalla-menu-item">
          <div class="valhalla-item-header">
            <h4>Lodbrok’s Lamb Burger</h4>
            <span class="valhalla-item-price">$16.99</span>
          </div>
          <p class="valhalla-item-desc">Seasoned ground pasture-raised lamb patty topped with creamy feta cheese, baby arugula, pickled red onion, and cucumber tzatziki on toasted brioche.</p>
        </div>

        <div class="valhalla-menu-item">
          <div class="valhalla-item-header">
            <h4>Nordic Pork Shank (Braised)</h4>
            <span class="valhalla-item-price">$21.00</span>
          </div>
          <p class="valhalla-item-desc">Slow-braised bone-in pork shank glazed with apple cider and mustard demi-glace, served over braised red cabbage and roasted fingerling potatoes.</p>
        </div>
      </div>
    </div>

    <!-- Group 2: Burgers -->
    <div class="valhalla-menu-group" id="tab-burgers">
      <div class="valhalla-section-title">
        <h2>Viking Blend Burgers &amp; Handhelds</h2>
        <p>Served with hand-cut sea salt pub fries or house remoulade slaw.</p>
      </div>

      <div class="valhalla-grid-2">
        <div class="valhalla-menu-item">
          <div class="valhalla-item-header">
            <h4>The Odin Viking Burger</h4>
            <span class="valhalla-item-price">$15.50</span>
          </div>
          <p class="valhalla-item-desc">Custom beef-pork blend patty, thick melted smoked gouda, applewood smoked bacon, stout-braised caramelized onions, and garlic aioli on brioche.</p>
          <div class="valhalla-item-tags">
            <span class="valhalla-tag valhalla-tag-signature">Bestseller</span>
          </div>
        </div>

        <div class="valhalla-menu-item">
          <div class="valhalla-item-header">
            <h4>The Thor Jalapeno Smash Burger</h4>
            <span class="valhalla-item-price">$15.99</span>
          </div>
          <p class="valhalla-item-desc">Double smashed patties with pepper jack cheese, crispy fried pickled jalapenos, smoked bacon, and fiery habanero bacon jam.</p>
          <div class="valhalla-item-tags">
            <span class="valhalla-tag valhalla-tag-spicy">Fiery Heat</span>
          </div>
        </div>

        <div class="valhalla-menu-item">
          <div class="valhalla-item-header">
            <h4>Crispy Viking Fried Chicken Sandwich</h4>
            <span class="valhalla-item-price">$14.50</span>
          </div>
          <p class="valhalla-item-desc">Buttermilk fried chicken breast tossed in hot honey or sweet lingonberry BBQ sauce with crunchy dill pickles on buttered brioche.</p>
        </div>

        <div class="valhalla-menu-item">
          <div class="valhalla-item-header">
            <h4>Brevard Court B.L.T. &amp; Gouda</h4>
            <span class="valhalla-item-price">$13.50</span>
          </div>
          <p class="valhalla-item-desc">Thick-cut applewood bacon, crisp romaine, ripe beefsteak tomatoes, melted smoked gouda, and roasted garlic herb mayo on sourdough.</p>
        </div>
      </div>
    </div>

    <!-- Group 3: Pub Fare -->
    <div class="valhalla-menu-group" id="tab-pubfare">
      <div class="valhalla-section-title">
        <h2>Pub Classics &amp; North Sea Fish</h2>
        <p>Hearty comfort food made fresh to order.</p>
      </div>

      <div class="valhalla-grid-2">
        <div class="valhalla-menu-item">
          <div class="valhalla-item-header">
            <h4>North Sea Beer-Battered Fish &amp; Chips</h4>
            <span class="valhalla-item-price">$16.00</span>
          </div>
          <p class="valhalla-item-desc">Crispy golden Atlantic cod fillets dipped in local craft IPA batter, served with sea salt pub fries, house caper tartar sauce, and lemon wedge.</p>
        </div>

        <div class="valhalla-menu-item">
          <div class="valhalla-item-header">
            <h4>Bangers &amp; Mash with Onion Gravy</h4>
            <span class="valhalla-item-price">$15.50</span>
          </div>
          <p class="valhalla-item-desc">Two grilled artisan pork sausages over Yukon gold mashed potatoes smothered in rich caramelized Guinness onion gravy.</p>
        </div>

        <div class="valhalla-menu-item">
          <div class="valhalla-item-header">
            <h4>Tavern Shepherd’s Pie</h4>
            <span class="valhalla-item-price">$15.99</span>
          </div>
          <p class="valhalla-item-desc">Ground lamb and beef stewed with sweet peas, carrots, and sweet corn in savory herb gravy, topped with toasted cheddar mashed potatoes.</p>
        </div>

        <div class="valhalla-menu-item">
          <div class="valhalla-item-header">
            <h4>Cast Iron Mac &amp; Beer Cheese</h4>
            <span class="valhalla-item-price">$12.50</span>
          </div>
          <p class="valhalla-item-desc">Cavatappi pasta baked with local craft ale cheddar cheese fondue, topped with toasted pretzel breadcrumbs and scallions.</p>
        </div>
      </div>
    </div>

    <!-- Group 4: Wings & Boards -->
    <div class="valhalla-menu-group" id="tab-wings">
      <div class="valhalla-section-title">
        <h2>Smoked Wings &amp; Shared Tavern Boards</h2>
        <p>Perfect for sharing over a pint on the Brevard Court patio.</p>
      </div>

      <div class="valhalla-grid-2">
        <div class="valhalla-menu-item">
          <div class="valhalla-item-header">
            <h4>Hickory-Smoked Jumbo Wings (8 pcs / 16 pcs)</h4>
            <span class="valhalla-item-price">$12.99 / $22.99</span>
          </div>
          <p class="valhalla-item-desc">Slow-smoked and flash-crisped wings tossed in your choice: Viking Dry Rub, Lingonberry Sweet BBQ, Garlic Parmesan, or Fiery Habanero.</p>
          <div class="valhalla-item-tags">
            <span class="valhalla-tag valhalla-tag-signature">Tavern Smoked</span>
          </div>
        </div>

        <div class="valhalla-menu-item">
          <div class="valhalla-item-header">
            <h4>Brevard Giant Bavarian Pretzel Board</h4>
            <span class="valhalla-item-price">$13.50</span>
          </div>
          <p class="valhalla-item-desc">Warm, butter-brushed jumbo soft pretzel served on a wooden board with warm beer cheese fondue and coarse whole grain mustard.</p>
        </div>

        <div class="valhalla-menu-item">
          <div class="valhalla-item-header">
            <h4>Valhalla Tavern Poutine</h4>
            <span class="valhalla-item-price">$11.99</span>
          </div>
          <p class="valhalla-item-desc">Hand-cut pub fries smothered in melted Wisconsin white cheddar cheese curds, rich meatball gravy, and crispy bacon crumbles.</p>
        </div>

        <div class="valhalla-menu-item">
          <div class="valhalla-item-header">
            <h4>Crispy Cheese Curds with Lingonberry Dip</h4>
            <span class="valhalla-item-price">$9.50</span>
          </div>
          <p class="valhalla-item-desc">Beer-battered Wisconsin cheddar curds fried golden with tart sweet lingonberry jam dipping sauce.</p>
        </div>
      </div>
    </div>

    <!-- Group 5: Drinks -->
    <div class="valhalla-menu-group" id="tab-drinks">
      <div class="valhalla-section-title">
        <h2>Rotating Craft Taps &amp; Nordic Cocktails</h2>
        <p>10 rotating Carolina draft lines, handcrafted cocktails, and authentic Scandinavian meads.</p>
      </div>

      <div class="valhalla-grid-2">
        <div class="valhalla-menu-item">
          <div class="valhalla-item-header">
            <h4>Odin’s Old Fashioned</h4>
            <span class="valhalla-item-price">$12.50</span>
          </div>
          <p class="valhalla-item-desc">Bourbon, spiced lingonberry syrup, Angostura bitters, and flamed orange peel over a hand-carved ice sphere.</p>
        </div>

        <div class="valhalla-menu-item">
          <div class="valhalla-item-header">
            <h4>Valkyrie Mule</h4>
            <span class="valhalla-item-price">$11.50</span>
          </div>
          <p class="valhalla-item-desc">Vodka, Scandinavian cloudberry liqueur, spicy ginger beer, and fresh lime in a chilled copper mug.</p>
        </div>

        <div class="valhalla-menu-item">
          <div class="valhalla-item-header">
            <h4>Local Rotating Carolina Craft Pint</h4>
            <span class="valhalla-item-price">$7.00 - $8.50</span>
          </div>
          <p class="valhalla-item-desc">Featuring 10 rotating draft handles from Charlotte and North Carolina craft breweries (IPA, Pilsner, Stout, Sour).</p>
        </div>

        <div class="valhalla-menu-item">
          <div class="valhalla-item-header">
            <h4>Traditional Honey Mead (Goblet)</h4>
            <span class="valhalla-item-price">$9.00</span>
          </div>
          <p class="valhalla-item-desc">Semi-sweet fermented honey wine infused with wild chamomile and orange blossom.</p>
        </div>
      </div>
    </div>

    <!-- Bottom Order CTA -->
    <div class="valhalla-cta-banner" style="margin-top:50px;">
      <h2>Craving Hearty Comfort &amp; Cold Craft Beer?</h2>
      <p>Visit us in Brevard Court or call ahead for quick tavern takeout pickup at 317 S Church St.</p>
      <div class="valhalla-cta-btns">
        <a href="tel:7043323273" class="valhalla-btn-hero-primary">Call (704) 332-3273</a>
        <a href="feast-platters-and-gameday-packages.html" class="valhalla-btn-hero-secondary">View Feast Platters</a>
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
