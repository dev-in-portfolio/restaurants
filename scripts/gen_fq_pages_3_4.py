# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("scripts")
from frenchquarter_builder import header_html, footer_html

# Page 3: cajun-and-creole-specialties.html
cajun_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cajun &amp; Creole Specialties | French Quarter Restaurant Charlotte NC</title>
  <meta name="description" content="Discover scratch-made Louisiana Cajun gumbo, Shrimp Creole, Blackened Catfish, and Cajun Chicken Pasta at French Quarter Restaurant in Uptown Charlotte.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("cajun-and-creole-specialties.html")}

  <section class="fq-hero-compact">
    <div class="fq-container">
      <span class="fq-badge">Louisiana Culinary Heritage</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Authentic Cajun &amp; Creole Specialties</h1>
      <p style="font-size:1.1rem; color:#cbd5e1; max-width:720px; margin:0 auto;">Handcrafted with traditional dark roux, holy trinity aromatics, imported Gulf seafood, and decades of time-tested family technique.</p>
    </div>
  </section>

  <main class="fq-container" style="padding:60px 24px;">
    <!-- Deep Dive: The Gumbo Story -->
    <div class="fq-grid-2" style="align-items:center; margin-bottom:60px;">
      <div>
        <span class="fq-pill-tag">Simmered Daily from Scratch</span>
        <h2 style="font-size:2.1rem; color:#1e0a45; margin:15px 0; font-weight:800;">The Secret of Our Dark Roux Gumbo</h2>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:15px;">
          True Louisiana gumbo starts with patience and a hand-stirred roux cooked slowly in heavy cast iron until it reaches a deep chocolate hue. At French Quarter Restaurant, our kitchen team adheres strictly to this timeless standard.
        </p>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:15px;">
          We fold in diced yellow onions, green bell peppers, and crisp celery—the iconic "holy trinity"—followed by savory smoked andouille sausage, pulled chicken, okra, and concentrated bone stock. Simmered for hours, each bowl yields a rich, velvety body balanced with authentic bay leaf and cayenne heat.
        </p>
        <div style="background:#fef3c7; border-left:4px solid #d97706; padding:16px; border-radius:6px; margin-top:20px;">
          <h4 style="color:#92400e; margin-bottom:4px;">Catering &amp; Family Pots Available</h4>
          <p style="color:#78350f; font-size:0.95rem; margin:0;">Planning a gathering or Panthers watch party? Order our homemade gumbo by the half-gallon and gallon with long-grain white rice and crusty French bread.</p>
        </div>
      </div>
      <div>
        <img src="images/cajun-gumbo-creole.jpg" alt="Rich homemade Louisiana Gumbo at French Quarter Charlotte" style="width:100%; height:420px; object-fit:cover; border-radius:12px; box-shadow:var(--fq-shadow-lg);">
      </div>
    </div>

    <!-- Feature Showcase Grid -->
    <h2 style="font-size:1.9rem; color:#1e0a45; text-align:center; margin-bottom:35px;">Signature Bayou Dishes</h2>
    
    <div class="fq-grid-3" style="gap:28px; margin-bottom:60px;">
      <div class="fq-card">
        <h3 style="color:#1e0a45; margin-bottom:8px;">Shrimp &amp; Crawfish Creole</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Plump Gulf shrimp and tender Louisiana crawfish tails braised in a piquant tomato-herb Creole sauce enriched with garlic, shallots, white wine, and fresh parsley over steamed rice.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e5e7eb; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$18.95</span>
          <span class="fq-pill-tag">Creole Classic</span>
        </div>
      </div>

      <div class="fq-card">
        <h3 style="color:#1e0a45; margin-bottom:8px;">Blackened Cajun Chicken Pasta</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Juicy chicken breast coated in cast-iron blackened spices, sliced over al dente penne pasta tossed in our decadent spiced garlic Parmesan cream sauce with sauteed bell peppers.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e5e7eb; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$17.50</span>
          <span class="fq-pill-tag">Bestseller</span>
        </div>
      </div>

      <div class="fq-card">
        <h3 style="color:#1e0a45; margin-bottom:8px;">Louisiana Red Beans &amp; Rice</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Slow-cooked red kidney beans simmered with smoked ham shank and Cajun seasonings until thick and creamy, topped with grilled split andouille sausage and sliced scallions.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e5e7eb; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$15.50</span>
          <span class="fq-pill-tag">Southern Tradition</span>
        </div>
      </div>

      <div class="fq-card">
        <h3 style="color:#1e0a45; margin-bottom:8px;">Cast-Iron Blackened Catfish</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Farm-raised catfish filet seared in roaring hot cast iron with butter and house blackened seasoning. Served with Creole yellow rice and garlic-steamed green beans.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e5e7eb; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$18.50</span>
          <span class="fq-pill-tag">Seafood Favorite</span>
        </div>
      </div>

      <div class="fq-card">
        <h3 style="color:#1e0a45; margin-bottom:8px;">Bourbon Chicken &amp; Rice</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Tender grilled chicken thigh pieces tossed in sweet brown sugar, Kentucky bourbon, and ginger glaze, served over fluffy rice with grilled seasoned vegetables.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e5e7eb; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$16.95</span>
          <span class="fq-pill-tag">Glazed Specialty</span>
        </div>
      </div>

      <div class="fq-card">
        <h3 style="color:#1e0a45; margin-bottom:8px;">Blackened Shrimp Alfredo</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6; margin-bottom:16px;">Sauteed blackened Gulf jumbo shrimp served over fettuccine in a rich house-made garlic Alfredo sauce, garnished with shaved Parmesan and fresh cracked black pepper.</p>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e5e7eb; padding-top:12px;">
          <span style="font-weight:700; color:#d97706; font-size:1.15rem;">$19.50</span>
          <span class="fq-pill-tag">Rich &amp; Decadent</span>
        </div>
      </div>
    </div>

    <!-- Call to Action -->
    <div class="fq-banner-strip">
      <h2 style="color:#ffffff; font-size:2rem; margin-bottom:12px;">Taste 35+ Years of Cajun Perfection</h2>
      <p style="color:#cbd5e1; max-width:650px; margin:0 auto 20px;">Stop by during lunch or dinner to experience genuine Louisiana hospitality right here in Uptown Charlotte.</p>
      <a href="tel:7043771715" class="fq-btn-primary">Call (704) 377-1715 for Orders</a>
    </div>
  </main>

{footer_html()}
"""

with open("french-quarter-restaurant/cajun-and-creole-specialties.html", "w", encoding="utf-8") as f:
    f.write(cajun_content)
print("Written: french-quarter-restaurant/cajun-and-creole-specialties.html")

# Page 4: brevard-court-courtyard-dining.html
patio_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Brevard Court Courtyard Dining | French Quarter Restaurant Charlotte</title>
  <meta name="description" content="Dine al fresco in historic Brevard Court at French Quarter Restaurant. Relax in Uptown Charlotte's iconic brick courtyard with craft beers, cocktails, and Cajun comfort food.">
  <link rel="stylesheet" href="site.css">
</head>
<body>
{header_html("brevard-court-courtyard-dining.html")}

  <section class="fq-hero-compact">
    <div class="fq-container">
      <span class="fq-badge">Historic Al Fresco Experience</span>
      <h1 style="font-size:2.6rem; font-weight:900; margin:15px 0;">Courtyard Patio Dining in Brevard Court</h1>
      <p style="font-size:1.1rem; color:#cbd5e1; max-width:720px; margin:0 auto;">Uptown Charlotte's premier pedestrian arcade, combining European charm with Southern pub warmth.</p>
    </div>
  </section>

  <main class="fq-container" style="padding:60px 24px;">
    <div class="fq-grid-2" style="align-items:center; margin-bottom:60px;">
      <div>
        <span class="fq-pill-tag">Pedestrian Promenade</span>
        <h2 style="font-size:2.1rem; color:#1e0a45; margin:15px 0; font-weight:800;">A Historic Gathering Place in the City Center</h2>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:15px;">
          Brevard Court was constructed in the early 20th century, modeling the grand open-air shopping arcades of Europe. Located between Church Street and Mint Street, this quaint brick-paved passageway offers a tranquil urban escape from the bustle of city skyscrapers.
        </p>
        <p style="color:#4b5563; line-height:1.7; margin-bottom:15px;">
          French Quarter Restaurant proudly anchors the Church Street entrance. Our outdoor courtyard tables invite you to unwind with friends, savor ice-cold draft beer, and enjoy our signature wings in the fresh breeze.
        </p>
        <ul style="color:#374151; line-height:1.8; padding-left:20px; margin-top:15px;">
          <li>Prime shaded patio tables and overhead evening string lighting</li>
          <li>Pet-friendly outdoor courtyard seating</li>
          <li>Immediate walking distance to Truist Field and Romare Bearden Park</li>
          <li>Quick, efficient lunch service tailored for busy Uptown office schedules</li>
        </ul>
      </div>
      <div>
        <img src="images/hero.jpg" alt="Outdoor dining courtyard atmosphere at French Quarter Restaurant Brevard Court" style="width:100%; height:400px; object-fit:cover; border-radius:12px; box-shadow:var(--fq-shadow-lg);">
      </div>
    </div>

    <!-- Atmosphere Highlights -->
    <h2 style="font-size:1.9rem; color:#1e0a45; text-align:center; margin-bottom:35px;">The Courtyard Advantage</h2>

    <div class="fq-grid-3" style="gap:28px; margin-bottom:60px;">
      <div class="fq-card">
        <h3 style="color:#1e0a45; margin-bottom:10px;">Weekday Lunch Haven</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6;">Take a break from your desk and step into Brevard Court. We specialize in fast, friendly lunch table service with daily specials that get you back to the office on time.</p>
        <div style="margin-top:16px; font-weight:600; color:#d97706; font-size:0.9rem;">Monday - Friday: 11:00 AM - 2:30 PM</div>
      </div>

      <div class="fq-card">
        <h3 style="color:#1e0a45; margin-bottom:10px;">Gameday Energy</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6;">Brevard Court comes alive on Panthers and Charlotte FC matchdays. Grab a seat under the trees, share platters of wings, and soak up the unbeatable stadium district atmosphere.</p>
        <div style="margin-top:16px; font-weight:600; color:#d97706; font-size:0.9rem;">5-Min Walk to Stadium Gates</div>
      </div>

      <div class="fq-card">
        <h3 style="color:#1e0a45; margin-bottom:10px;">Evening Happy Hours</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.6;">As the sun sets, string lights illuminate the court. Enjoy our rotating craft beer selection, chilled wine, and hearty pub bites with colleagues after work.</p>
        <div style="margin-top:16px; font-weight:600; color:#d97706; font-size:0.9rem;">Full Bar &amp; Draft Specials</div>
      </div>
    </div>

    <!-- Courtyard Seating Policy Info -->
    <div style="background:#ffffff; border:1px solid #e5e7eb; border-radius:12px; padding:32px; box-shadow:var(--fq-shadow);">
      <h3 style="color:#1e0a45; font-size:1.4rem; margin-bottom:12px;">Courtyard Seating Guidelines</h3>
      <p style="color:#4b5563; font-size:0.95rem; line-height:1.7;">
        Patio seating is open on a first-come, first-served basis. During major stadium events, peak lunch hours, and sunny Friday evenings, we recommend arriving early. For large corporate lunch groups or special pre-game arrangements, please call ahead.
      </p>
      <div style="margin-top:20px;">
        <a href="tel:7043771715" class="fq-btn-primary">Call Pub Staff: (704) 377-1715</a>
      </div>
    </div>
  </main>

{footer_html()}
"""

with open("french-quarter-restaurant/brevard-court-courtyard-dining.html", "w", encoding="utf-8") as f:
    f.write(patio_content)
print("Written: french-quarter-restaurant/brevard-court-courtyard-dining.html")

