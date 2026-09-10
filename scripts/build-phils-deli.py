import os

nav_template = '''
      <nav class="pdeli-nav" aria-label="Primary Navigation">
        <ul class="pdeli-nav-list">
          <li><a href="index.html" class="pdeli-nav-link {nav_index}">Home</a></li>
          <li><a href="menu.html" class="pdeli-nav-link {nav_menu}">Deli Menu</a></li>
          <li><a href="new-york-deli-tradition.html" class="pdeli-nav-link {nav_tradition}">Deli Tradition</a></li>
          <li><a href="reubens-and-pastrami.html" class="pdeli-nav-link {nav_reubens}">Reubens &amp; Pastrami</a></li>
          <li><a href="matzo-soup-and-sides.html" class="pdeli-nav-link {nav_soup}">Soup &amp; Sides</a></li>
          <li><a href="visit.html" class="pdeli-nav-link pdeli-nav-cta {nav_visit}">Visit &amp; Order</a></li>
        </ul>
      </nav>
'''

footer_content = '''
  <footer class="pdeli-footer">
    <div class="pdeli-footer-container">
      <div class="pdeli-footer-brand">
        <h4>Phil’s Deli To Go</h4>
        <p>A Charlotte tradition since 1979 founded by Phil Levine. Serving hot pastrami, famous grilled Reubens, fluffy matzo ball soup, and overstuffed deli classics.</p>
      </div>
      <div class="pdeli-footer-nav">
        <h5>Explore Demo</h5>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="menu.html">Full Menu</a></li>
          <li><a href="new-york-deli-tradition.html">Deli Tradition</a></li>
          <li><a href="reubens-and-pastrami.html">Reubens &amp; Pastrami</a></li>
          <li><a href="matzo-soup-and-sides.html">Matzo Soup &amp; Sides</a></li>
          <li><a href="visit.html">Locations &amp; Hours</a></li>
        </ul>
      </div>
      <div class="pdeli-footer-hours">
        <h5>Locations &amp; Contact</h5>
        <p style="color: #9cb1c9; font-size: 0.88rem; margin-bottom: 0.4rem;"><strong>Providence Road:</strong> 4223 Providence Rd #6</p>
        <p style="color: #9cb1c9; font-size: 0.88rem; margin-bottom: 0.4rem;"><strong>Direct Phone:</strong> (704) 366-8811</p>
        <p style="color: #9cb1c9; font-size: 0.88rem;">Mon - Sat: 7:00 AM - 8:00 PM<br>Sunday: 8:00 AM - 3:00 PM</p>
      </div>
    </div>
    <div class="pdeli-footer-bottom">
      <p>&copy; 2026 Phil’s Deli To Go. All rights reserved. Delicatessen showcase demo for Charlotte, NC.</p>
    </div>
  </footer>
'''

pages = {
  'index.html': {
    'title': 'Phil’s Deli To Go - Charlotte’s Landmark New York Deli Tradition',
    'nav': {'index': 'active', 'menu': '', 'tradition': '', 'reubens': '', 'soup': '', 'visit': ''},
    'body': '''
    <main>
      <section class="pdeli-hero">
        <div class="pdeli-hero-grid">
          <div class="pdeli-hero-content">
            <span class="pdeli-hero-badge">Charlotte Deli Institution &bull; Est. 1979</span>
            <h1 class="pdeli-hero-title">Overstuffed Classics, <span>Hand-Carved Daily</span></h1>
            <p class="pdeli-hero-lead">Founded by second-generation New Yorker Phil Levine, Phil’s Deli brings authentic hot pastrami, award-winning grilled Reubens, and comforting golden matzo ball soup to Charlotte.</p>
            <div class="pdeli-hero-actions">
              <a href="menu.html" class="pdeli-btn-primary">Explore Full Menu</a>
              <a href="reubens-and-pastrami.html" class="pdeli-btn-secondary">The Famous Reuben</a>
            </div>
          </div>
          <div class="pdeli-hero-img-wrap">
            <img src="images/hero.jpg" alt="Overstuffed pastrami sandwich on marble rye with deli pickle and sides" width="600" height="400">
          </div>
        </div>
      </section>

      <section class="pdeli-features">
        <div class="pdeli-feature-grid">
          <div class="pdeli-feature-card">
            <div class="pdeli-feature-tag">Charlotte Favorite</div>
            <h2 class="pdeli-feature-title">The Famous Reuben</h2>
            <p class="pdeli-feature-desc">Hot steamed corned beef, melted Swiss, crisp sauerkraut, and tangy Russian dressing on buttery griddled rye.</p>
          </div>
          <div class="pdeli-feature-card">
            <div class="pdeli-feature-tag">Steamed Hot</div>
            <h2 class="pdeli-feature-title">NYC Pastrami &amp; Brisket</h2>
            <p class="pdeli-feature-desc">Cured with coriander and black pepper, hand-sliced paper thin, and piled high with spicy deli brown mustard.</p>
          </div>
          <div class="pdeli-feature-card">
            <div class="pdeli-feature-tag">Scratch Simmered</div>
            <h2 class="pdeli-feature-title">Matzo Ball Soup</h2>
            <p class="pdeli-feature-desc">Golden rich chicken broth simmered for hours with fresh dill, carrots, and light, fluffy hand-rolled matzo dumplings.</p>
          </div>
        </div>
      </section>

      <section class="pdeli-section">
        <div class="pdeli-story-grid">
          <div class="pdeli-story-img-wrap">
            <img src="images/reuben.jpg" alt="Golden grilled Reuben sandwich with melted Swiss cheese and corned beef" width="600" height="360">
          </div>
          <div class="pdeli-story-content">
            <span class="pdeli-section-eyebrow">A True Charlotte Staple</span>
            <h3>Decades of Deli Heritage in the Queen City</h3>
            <p>For over forty years, Phil’s Deli has set the gold standard for delicatessen dining in Charlotte. Whether you visit our full dining room on Providence Road or grab lunch on the go, our commitment to generous portions and authentic recipes remains unchanged.</p>
            <p>Every sandwich is built on fresh bakery bread delivered daily, paired with kosher-style dill pickle spears and our scratch potato salad or coleslaw.</p>
            <a href="new-york-deli-tradition.html" class="pdeli-btn-primary" style="margin-top: 0.5rem;">Read Our Story</a>
          </div>
        </div>
      </section>

      <section class="pdeli-section" style="background: #ffffff; border-top: 1px solid var(--pdeli-border); border-bottom: 1px solid var(--pdeli-border);">
        <div class="pdeli-section-header">
          <span class="pdeli-section-eyebrow">Corporate &amp; Event Catering</span>
          <h2 class="pdeli-section-title">Office Luncheon &amp; Platter Estimator</h2>
          <p class="pdeli-section-subtitle">Calculate sandwich trays, side salads, and kosher pickle counts for your next office luncheon or family gathering.</p>
        </div>

        <div class="pdeli-calc-card">
          <div class="pdeli-calc-controls">
            <div class="pdeli-calc-field">
              <label for="pdeli-guest-count">Number of Attendees: <span id="pdeli-guest-display" style="color: var(--pdeli-primary); font-weight: 800;">15 People</span></label>
              <input type="range" id="pdeli-guest-count" class="pdeli-range-slider" min="5" max="80" step="5" value="15">
            </div>
            <div class="pdeli-calc-field">
              <label for="pdeli-platter-style">Packaging Format</label>
              <select id="pdeli-platter-style" class="pdeli-calc-select">
                <option value="platter">Shared Deli Platter (Assorted Sandwiches)</option>
                <option value="boxed">Individual Executive Box Lunches</option>
              </select>
            </div>
          </div>
          <div class="pdeli-calc-results">
            <div class="pdeli-result-box">
              <span class="num" id="pdeli-sandwich-total">19 Sandwiches</span>
              <span class="label">Assorted Deli Sandwiches</span>
            </div>
            <div class="pdeli-result-box">
              <span class="num" id="pdeli-side-total">6.0 lbs (Potato / Slaw)</span>
              <span class="label">Deli Salads Total</span>
            </div>
            <div class="pdeli-result-box">
              <span class="num" id="pdeli-pickle-total">15 Kosher Spear Halves</span>
              <span class="label">Crisp Kosher Dills</span>
            </div>
          </div>
        </div>
      </section>
    </main>
'''
  },
  'menu.html': {
    'title': 'Deli Menu - Phil’s Deli To Go Charlotte NC',
    'nav': {'index': '', 'menu': 'active', 'tradition': '', 'reubens': '', 'soup': '', 'visit': ''},
    'body': '''
    <main class="pdeli-section">
      <div class="pdeli-section-header">
        <span class="pdeli-section-eyebrow">Classic Delicatessen</span>
        <h1 class="pdeli-section-title">Phil’s Deli Menu</h1>
        <p class="pdeli-section-subtitle">Overstuffed hot deli sandwiches, cold sliced meats, fresh salads, comforting soups, and breakfast specialties.</p>
      </div>

      <div class="pdeli-filter-tabs" role="tablist" aria-label="Menu Filter Tabs">
        <button type="button" class="pdeli-filter-btn active" data-filter="all">All Selections</button>
        <button type="button" class="pdeli-filter-btn" data-filter="hot">Hot Overstuffed</button>
        <button type="button" class="pdeli-filter-btn" data-filter="cold">Cold Deli Classics</button>
        <button type="button" class="pdeli-filter-btn" data-filter="soup">Soups &amp; Salads</button>
        <button type="button" class="pdeli-filter-btn" data-filter="breakfast">Breakfast &amp; Bagels</button>
      </div>

      <div class="pdeli-menu-grid">
        <div class="pdeli-menu-item" data-category="hot">
          <div class="pdeli-menu-item-header">
            <span class="pdeli-menu-item-name">The Famous Charlotte Reuben</span>
            <span class="pdeli-menu-item-price">$15.95</span>
          </div>
          <p class="pdeli-menu-item-desc">Hot steamed corned beef, melted imported Swiss, barrel sauerkraut, and Russian dressing griddled golden on seeded Jewish rye bread.</p>
          <div class="pdeli-menu-item-badges">
            <span class="pdeli-badge pdeli-badge-gold">House Specialty</span>
            <span class="pdeli-badge">Served with Pickle &amp; Side</span>
          </div>
        </div>

        <div class="pdeli-menu-item" data-category="hot">
          <div class="pdeli-menu-item-header">
            <span class="pdeli-menu-item-name">Hot NYC Pastrami on Rye</span>
            <span class="pdeli-menu-item-price">$15.50</span>
          </div>
          <p class="pdeli-menu-item-desc">Peppercorn and coriander cured brisket steamed tender, sliced thin, piled half-pound high with spicy brown deli mustard.</p>
          <div class="pdeli-menu-item-badges">
            <span class="pdeli-badge pdeli-badge-gold">Deli Legend</span>
          </div>
        </div>

        <div class="pdeli-menu-item" data-category="hot">
          <div class="pdeli-menu-item-header">
            <span class="pdeli-menu-item-name">The Rachel (Turkey Reuben)</span>
            <span class="pdeli-menu-item-price">$14.95</span>
          </div>
          <p class="pdeli-menu-item-desc">Roasted breast of turkey, house coleslaw, Swiss cheese, and Russian dressing grilled crisp on marble rye.</p>
          <div class="pdeli-menu-item-badges">
            <span class="pdeli-badge">Grilled Hot</span>
          </div>
        </div>

        <div class="pdeli-menu-item" data-category="cold">
          <div class="pdeli-menu-item-header">
            <span class="pdeli-menu-item-name">Phil’s Homemade Chicken Salad</span>
            <span class="pdeli-menu-item-price">$13.25</span>
          </div>
          <p class="pdeli-menu-item-desc">Poached all-white chicken breast tossed with diced celery, Hellmann’s mayonnaise, and seasonings on toasted whole wheat or croissant.</p>
          <div class="pdeli-menu-item-badges">
            <span class="pdeli-badge pdeli-badge-green">Scratch Made Daily</span>
          </div>
        </div>

        <div class="pdeli-menu-item" data-category="cold">
          <div class="pdeli-menu-item-header">
            <span class="pdeli-menu-item-name">Triple Decker Club</span>
            <span class="pdeli-menu-item-price">$14.75</span>
          </div>
          <p class="pdeli-menu-item-desc">Roasted turkey breast, crisp smoked bacon, lettuce, tomato, and mayo layered on three slices of toasted sourdough.</p>
          <div class="pdeli-menu-item-badges">
            <span class="pdeli-badge">Lunch Classic</span>
          </div>
        </div>

        <div class="pdeli-menu-item" data-category="soup">
          <div class="pdeli-menu-item-header">
            <span class="pdeli-menu-item-name">Grandma’s Matzo Ball Soup</span>
            <span class="pdeli-menu-item-price">$7.95 / $9.95</span>
          </div>
          <p class="pdeli-menu-item-desc">Rich golden chicken broth, tender chicken morsels, diced carrots, celery, fresh dill, and a giant fluffy matzo dumpling.</p>
          <div class="pdeli-menu-item-badges">
            <span class="pdeli-badge pdeli-badge-gold">Comfort Classic</span>
          </div>
        </div>

        <div class="pdeli-menu-item" data-category="soup">
          <div class="pdeli-menu-item-header">
            <span class="pdeli-menu-item-name">Deli Chef Salad</span>
            <span class="pdeli-menu-item-price">$13.95</span>
          </div>
          <p class="pdeli-menu-item-desc">Crisp romaine and mixed greens topped with turkey, ham, Swiss, cheddar, hard-boiled egg, cucumbers, tomatoes, and house vinaigrette.</p>
          <div class="pdeli-menu-item-badges">
            <span class="pdeli-badge pdeli-badge-green">Fresh &amp; Hearty</span>
          </div>
        </div>

        <div class="pdeli-menu-item" data-category="breakfast">
          <div class="pdeli-menu-item-header">
            <span class="pdeli-menu-item-name">Nova Lox &amp; Cream Cheese Bagel</span>
            <span class="pdeli-menu-item-price">$14.50</span>
          </div>
          <p class="pdeli-menu-item-desc">Smoked Atlantic salmon, whipped cream cheese, sliced red onion, capers, and ripe tomato on a toasted New York bagel.</p>
          <div class="pdeli-menu-item-badges">
            <span class="pdeli-badge">Served All Morning</span>
          </div>
        </div>

        <div class="pdeli-menu-item" data-category="breakfast">
          <div class="pdeli-menu-item-header">
            <span class="pdeli-menu-item-name">Western Deli Omelet</span>
            <span class="pdeli-menu-item-price">$12.50</span>
          </div>
          <p class="pdeli-menu-item-desc">Three farm-fresh eggs folded with diced ham, bell peppers, onions, and American cheese, served with home fries and buttered toast.</p>
          <div class="pdeli-menu-item-badges">
            <span class="pdeli-badge">Breakfast Special</span>
          </div>
        </div>
      </div>
    </main>
'''
  },
  'new-york-deli-tradition.html': {
    'title': 'New York Deli Tradition - Phil’s Deli To Go',
    'nav': {'index': '', 'menu': '', 'tradition': 'active', 'reubens': '', 'soup': '', 'visit': ''},
    'body': '''
    <main class="pdeli-section">
      <div class="pdeli-section-header">
        <span class="pdeli-section-eyebrow">Our Story &amp; Heritage</span>
        <h1 class="pdeli-section-title">The Charlotte New York Deli Tradition</h1>
        <p class="pdeli-section-subtitle">How Phil Levine brought generational delicatessen standards and old-school hospitality to North Carolina.</p>
      </div>

      <div class="pdeli-story-grid">
        <div class="pdeli-story-content">
          <h3>Founded with Passion by Phil Levine</h3>
          <p>When Phil Levine arrived in Charlotte in the late 1970s, he noticed that the Queen City was missing an essential institution: an authentic, no-nonsense New York Jewish delicatessen where pastrami is cured right, corned beef is steamed to melting perfection, and the portions are unapologetically generous.</p>
          <p>Opening his first doors in Cotswold and later expanding to Strawberry Hill on Providence Road, Phil established a loyal community of regulars that span three generations of Charlotte families.</p>
        </div>
        <div class="pdeli-story-img-wrap">
          <img src="images/hero.jpg" alt="Deli heritage and classic sandwich preparation" width="600" height="360">
        </div>
      </div>

      <div class="pdeli-story-grid" style="margin-top: 4.5rem;">
        <div class="pdeli-story-img-wrap">
          <img src="images/pastrami.jpg" alt="Thinly sliced hot pastrami piled high on deli rye" width="600" height="360">
        </div>
        <div class="pdeli-story-content">
          <h3>Uncompromising Deli Standards</h3>
          <p>We believe great deli food requires respecting the methods of the old masters. That means properly brining beef briskets, slow-steaming meats before every service to lock in juiciness, and slicing against the grain to order.</p>
          <p>Our seeded and unseeded rye breads are baked to provide the sturdy crunch and dense crumb needed to hold overstuffed sandwiches together without going soggy.</p>
        </div>
      </div>
    </main>
'''
  },
  'reubens-and-pastrami.html': {
    'title': 'Reubens & Pastrami - Phil’s Deli To Go',
    'nav': {'index': '', 'menu': '', 'tradition': '', 'reubens': 'active', 'soup': '', 'visit': ''},
    'body': '''
    <main class="pdeli-section">
      <div class="pdeli-section-header">
        <span class="pdeli-section-eyebrow">Crown Jewels of the Deli</span>
        <h1 class="pdeli-section-title">The Famous Charlotte Reuben &amp; Hot Pastrami</h1>
        <p class="pdeli-section-subtitle">Deep dive into the craftsmanship behind our most celebrated sandwiches.</p>
      </div>

      <div class="pdeli-story-grid">
        <div class="pdeli-story-img-wrap">
          <img src="images/reuben.jpg" alt="Golden grilled Reuben sandwich with Swiss cheese and Russian dressing" width="600" height="360">
        </div>
        <div class="pdeli-story-content">
          <h3>Anatomy of the Perfect Reuben</h3>
          <p>The Phil’s Deli Reuben has been voted the best in Charlotte countless times for a reason. Here is how we build each sandwich:</p>
          <p><strong>1. The Corned Beef:</strong> Brined with whole cloves, bay leaves, and allspice, steamed until tender and sliced warm.</p>
          <p><strong>2. The Sauerkraut:</strong> Pressed dry so it retains crisp bite and acidity without saturating the bread.</p>
          <p><strong>3. The Swiss &amp; Dressing:</strong> Aged imported Swiss cheese for that rich nutty melt, paired with our house-blended Russian dressing.</p>
          <p><strong>4. The Comal Grill:</strong> Double-buttered marble rye griddled on the flat-top with a weighted press until golden brown and crackling.</p>
        </div>
      </div>

      <div class="pdeli-story-grid" style="margin-top: 4.5rem;">
        <div class="pdeli-story-content">
          <h3>Hot Pastrami on Seeded Rye</h3>
          <p>Pastrami is an art form. We rub premium beef briskets with a robust dry blend of cracked black pepper, toasted coriander, mustard seed, and garlic before smoking over hardwood.</p>
          <p>Steamed gently in our carving stations, the meat is hand-stacked high on fresh Jewish rye with a generous swipe of spicy Gulden’s brown mustard. Simple, classic, and completely satisfying.</p>
        </div>
        <div class="pdeli-story-img-wrap">
          <img src="images/pastrami.jpg" alt="Hot pastrami sandwich sliced in half showing juicy tender layers" width="600" height="360">
        </div>
      </div>
    </main>
'''
  },
  'matzo-soup-and-sides.html': {
    'title': 'Matzo Soup & Sides - Phil’s Deli To Go',
    'nav': {'index': '', 'menu': '', 'tradition': '', 'reubens': '', 'soup': 'active', 'visit': ''},
    'body': '''
    <main class="pdeli-section">
      <div class="pdeli-section-header">
        <span class="pdeli-section-eyebrow">Scratch Comfort Foods</span>
        <h1 class="pdeli-section-title">Matzo Ball Soup &amp; Deli Side Dishes</h1>
        <p class="pdeli-section-subtitle">Comforting homemade soups, crispy potato knishes, and hand-tossed deli salads.</p>
      </div>

      <div class="pdeli-story-grid">
        <div class="pdeli-story-content">
          <h3>Jewish Penicillin: Matzo Ball Soup</h3>
          <p>Known affectionately as Jewish Penicillin, our matzo ball soup is prepared from scratch every morning. We slow-simmer whole roasting chickens with sweet yellow onions, parsnips, carrots, and fresh dill to produce an aromatic golden broth.</p>
          <p>Our matzo balls are hand-formed with egg whites and schmaltz, creating a dumpling that is light, fluffy, and absorbs the rich savory soup flavors.</p>
        </div>
        <div class="pdeli-story-img-wrap">
          <img src="images/soup.jpg" alt="Steaming hot bowl of golden chicken soup with vegetables and matzo ball" width="600" height="360">
        </div>
      </div>

      <div class="pdeli-story-grid" style="margin-top: 4.5rem;">
        <div class="pdeli-story-img-wrap">
          <img src="images/sides.jpg" alt="Deli sides including potato salad, coleslaw, and kosher dill pickles" width="600" height="360">
        </div>
        <div class="pdeli-story-content">
          <h3>Essential Deli Sides</h3>
          <p><strong>Red Bliss Potato Salad:</strong> Steamed red potatoes tossed with chopped celery, scallions, and creamy mustard dressing.</p>
          <p><strong>Sweet &amp; Tangy Coleslaw:</strong> Crisp green cabbage and carrots shredded fine and dressed with our signature cider vinegar dressing.</p>
          <p><strong>Half-Sour Kosher Pickles:</strong> Crisp garlic-brined Kirby cucumbers with that classic loud snap.</p>
          <p><strong>Golden Potato Knishes:</strong> Flaky pastry pockets filled with seasoned mashed potatoes and caramelized onions.</p>
        </div>
      </div>
    </main>
'''
  },
  'visit.html': {
    'title': 'Visit & Order - Phil’s Deli To Go Charlotte NC',
    'nav': {'index': '', 'menu': '', 'tradition': '', 'reubens': '', 'soup': '', 'visit': 'active'},
    'body': '''
    <main class="pdeli-section">
      <div class="pdeli-section-header">
        <span class="pdeli-section-eyebrow">Dine In, Express Pickup &amp; Catering</span>
        <h1 class="pdeli-section-title">Visit Phil’s Deli</h1>
        <p class="pdeli-section-subtitle">Join us for breakfast, lunch, or arrange custom catering for your next corporate luncheon or family event.</p>
      </div>

      <div class="pdeli-contact-grid">
        <div class="pdeli-contact-card">
          <h3>Providence Road Flagship</h3>
          <p style="color: var(--pdeli-text-muted); margin-bottom: 0.8rem;">Full-service dining room, bakery case, breakfast counter, and takeout pickup.</p>
          <p><strong>Address:</strong> 4223 Providence Rd #6, Charlotte, NC 28211</p>
          <p style="margin-top: 0.4rem;"><strong>Shopping Center:</strong> Strawberry Hill Shopping Center</p>
          <div style="margin-top: 1.5rem;">
            <a href="tel:7043668811" class="pdeli-btn-primary" style="width: 100%; text-align: center;">Call Flagship: (704) 366-8811</a>
          </div>
        </div>

        <div class="pdeli-contact-card">
          <h3>Operating Hours</h3>
          <div class="pdeli-hours-row">
            <span>Monday &ndash; Friday</span>
            <span>7:00 AM &ndash; 8:00 PM</span>
          </div>
          <div class="pdeli-hours-row">
            <span>Saturday</span>
            <span>7:00 AM &ndash; 8:00 PM</span>
          </div>
          <div class="pdeli-hours-row">
            <span>Sunday</span>
            <span>8:00 AM &ndash; 3:00 PM</span>
          </div>
          <div style="margin-top: 1.5rem; background: var(--pdeli-surface-alt); padding: 1rem; border-radius: var(--pdeli-radius-sm);">
            <p style="font-size: 0.85rem; color: var(--pdeli-primary); font-weight: 600;">Breakfast served daily until 11:00 AM (all day Sunday). Takeout counter open all hours.</p>
          </div>
        </div>

        <div class="pdeli-contact-card">
          <h3>Office Catering &amp; Trays</h3>
          <p style="color: var(--pdeli-text-muted); margin-bottom: 0.8rem;">Assorted sandwich platters, executive box lunches, hot corned beef &amp; pastrami buffet setups, and bagel breakfast boxes.</p>
          <p><strong>Notice:</strong> 24-hour advance notice recommended for large corporate groups.</p>
          <div style="margin-top: 1.5rem;">
            <a href="mailto:catering@philsdelicharlotte.com" class="pdeli-btn-secondary" style="width: 100%; text-align: center;">Inquire About Catering</a>
          </div>
        </div>
      </div>
    </main>
'''
  }
}

for filename, data in pages.items():
  cur_nav = nav_template.format(
    nav_index=data['nav']['index'],
    nav_menu=data['nav']['menu'],
    nav_tradition=data['nav']['tradition'],
    nav_reubens=data['nav']['reubens'],
    nav_soup=data['nav']['soup'],
    nav_visit=data['nav']['visit']
  )

  html_doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{data['title']}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="site.css">
</head>
<body>
  <header class="pdeli-header">
    <div class="pdeli-nav-container">
      <a href="index.html" class="pdeli-brand">
        <span class="pdeli-brand-title">Phil’s Deli To Go</span>
        <span class="pdeli-brand-subtitle">New York Delicatessen &bull; Est. 1979</span>
      </a>
      <button class="pdeli-nav-toggle" type="button" aria-label="Toggle navigation menu" aria-expanded="false">Menu</button>
{cur_nav}
    </div>
  </header>

{data['body']}

{footer_content}
  <script src="site.js"></script>
</body>
</html>'''

  filepath = os.path.join('phil-s-deli-to-go', filename)
  with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html_doc.strip() + '\n')
  print(f'Wrote {filename}')

print('All 6 HTML pages for Phil’s Deli To Go written successfully')
