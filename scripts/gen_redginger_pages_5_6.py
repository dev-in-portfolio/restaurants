# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\scripts")
from redginger_builder import header_html, footer_html

DIR = r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\red-ginger"

# 5. private-dining-and-group-events.html
events_page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Private Dining &amp; Corporate Events | Red Ginger Charlotte</title>
  <meta name="description" content="Host your corporate dinner, celebration, or private event at Red Ginger in Uptown Charlotte: private teppanyaki tables, sushi lounge buyouts, and customized tasting menus.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
{header_html("private-dining-and-group-events.html")}

  <section class="redginger-hero" style="padding: 50px 20px;">
    <div class="redginger-hero-inner">
      <span class="redginger-hero-pill">Uptown Charlotte Event Venue</span>
      <h1>Private Dining &amp; Corporate Celebrations</h1>
      <p>Elevate your corporate board dinner, client reception, birthday celebration, or rehearsal dinner with private teppanyaki tables and dedicated sushi lounge spaces on South Tryon.</p>
    </div>
  </section>

  <main class="redginger-container">
    <div class="redginger-section-title">
      <h2>Private Event Dining Options</h2>
      <p>Tailored group packages that combine the theatrical excitement of teppanyaki with the sophistication of our sushi bar.</p>
    </div>

    <div class="redginger-grid-3">
      <div class="redginger-card">
        <div class="redginger-card-body">
          <span class="redginger-card-badge">Teppan Group Dining</span>
          <h3>Private Hibachi Table Rooms</h3>
          <p>Reserve dedicated teppanyaki tables for groups of 8 to 24 guests. Includes private master chef performance, customized multi-course steak &amp; seafood menus, and dedicated server attention.</p>
          <div class="redginger-card-footer">
            <span class="redginger-price">From $48 / Guest</span>
            <span style="font-size:0.85rem; color:var(--redginger-text-muted);">8 - 24 Guests</span>
          </div>
        </div>
      </div>

      <div class="redginger-card">
        <div class="redginger-card-body">
          <span class="redginger-card-badge">Cocktail Reception</span>
          <h3>Sushi Lounge Cocktail Buyout</h3>
          <p>Host an upscale standing cocktail reception with passed specialty maki, raw bar platters, gyoza skewers, craft sake, and signature cocktails for corporate networking and mixers.</p>
          <div class="redginger-card-footer">
            <span class="redginger-price">From $35 / Guest</span>
            <span style="font-size:0.85rem; color:var(--redginger-text-muted);">20 - 50 Guests</span>
          </div>
        </div>
      </div>

      <div class="redginger-card">
        <div class="redginger-card-body">
          <span class="redginger-card-badge">Executive Dining</span>
          <h3>Imperial Multi-Course Banquet</h3>
          <p>A multi-course dinner featuring A5 Wagyu appetizers, twin lobster tails, center-cut Filet Mignon, chef omakase nigiri, and Japanese matcha dessert.</p>
          <div class="redginger-card-footer">
            <span class="redginger-price">From $68 / Guest</span>
            <span style="font-size:0.85rem; color:var(--redginger-text-muted);">10 - 40 Guests</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Interactive Event Calculator -->
    <div class="redginger-section-title" style="margin-top:60px;">
      <h2>Interactive Private Event Estimator</h2>
      <p>Plan guest count, teppan table configurations, dining tiers, and pricing for your upcoming gathering.</p>
    </div>

    <div class="redginger-calc-box">
      <div class="redginger-calc-row">
        <label for="calc-party-size">Number of Guests: <span id="calc-party-size-val" style="color:var(--redginger-primary-dark);">16 Guests</span></label>
        <input type="range" id="calc-party-size" min="8" max="60" step="2" value="16" class="redginger-range-control">
      </div>

      <div class="redginger-calc-row">
        <label for="calc-dining-tier">Select Dining Experience Tier</label>
        <select id="calc-dining-tier" class="redginger-select-control">
          <option value="48.00" selected>Classic Teppanyaki Feast ($48.00 / guest - Steak, Chicken &amp; Shrimp)</option>
          <option value="68.00">Imperial Steakhouse &amp; Lobster Banquet ($68.00 / guest - Filet Mignon &amp; Lobster)</option>
          <option value="88.00">Executive Omakase &amp; Wagyu Experience ($88.00 / guest - Multi-Course Chef Tasting)</option>
        </select>
      </div>

      <div class="redginger-calc-row">
        <label for="calc-lounge-addon">Add Cocktail or Sushi Reception</label>
        <select id="calc-lounge-addon" class="redginger-select-control">
          <option value="0" selected>No Welcome Reception</option>
          <option value="14.00">Add Passed Specialty Sushi Welcome Reception (+$14.00 / guest)</option>
          <option value="22.00">Add Premium Sake &amp; Cocktail Pairing (+$22.00 / guest)</option>
        </select>
      </div>

      <div class="redginger-calc-results">
        <div class="redginger-result-line">
          <span>Table Allocation:</span>
          <strong id="calc-tables-info">Accommodates in 2 Dedicated Teppanyaki Chef Table(s) / Private Lounge Area</strong>
        </div>
        <div class="redginger-result-line">
          <span>Included Courses:</span>
          <strong id="calc-courses-info">Includes Soup, House Salad, Hibachi Vegetables, Fried Rice, Noodles, and Sorbet</strong>
        </div>
        <div class="redginger-result-total">
          <span>Estimated Total:</span>
          <span id="calc-total-price">$768.00</span>
        </div>
      </div>

      <div style="margin-top:24px; text-align:center;">
        <a href="tel:9808198837" class="redginger-btn-hero-primary" style="display:inline-block; width:100%;">Call (980) 819-8837 to Inquire About Event Dates</a>
      </div>
    </div>

    <!-- Booking Guidelines -->
    <div class="redginger-grid-2" style="margin-top:50px;">
      <div class="redginger-card" style="padding:28px;">
        <h4 style="color:var(--redginger-primary-dark); margin-bottom:10px;">Deposit &amp; Cancellation Policy</h4>
        <p style="color:var(--redginger-text-muted); font-size:0.95rem;">Private teppanyaki room reservations for groups over 12 require a 48-hour advance confirmation. Dedicated full-lounge buyouts require a signed agreement and deposit 1 week prior to the event date.</p>
      </div>

      <div class="redginger-card" style="padding:28px;">
        <h4 style="color:var(--redginger-primary-dark); margin-bottom:10px;">Dietary &amp; Custom Menu Options</h4>
        <p style="color:var(--redginger-text-muted); font-size:0.95rem;">Our chefs gladly customize menus for vegetarian, gluten-free, and shellfish-allergic guests by preparing dedicated grilled tofu, gluten-free fried rice, and vegetable tempura.</p>
      </div>
    </div>
  </main>

{footer_html()}'''

# 6. visit.html
visit_page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Visit &amp; Reservations | Red Ginger Japanese Steakhouse Charlotte</title>
  <meta name="description" content="Visit Red Ginger Japanese Steakhouse & Sushi at 401 S Tryon St in Uptown Charlotte NC. Operating hours, table reservations, parking directions, and FAQs.">
  <link rel="stylesheet" href="site.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
{header_html("visit.html")}

  <section class="redginger-hero" style="padding: 50px 20px;">
    <div class="redginger-hero-inner">
      <span class="redginger-hero-pill">Uptown South Tryon Location</span>
      <h1>Visit &amp; Reservations</h1>
      <p>Located in the heart of Uptown Charlotte’s cultural and financial district on South Tryon Street, welcoming guests for executive lunch, dinner, and celebrations.</p>
    </div>
  </section>

  <main class="redginger-container">
    <div class="redginger-visit-grid">
      <div class="redginger-info-card">
        <h3>Location &amp; Contact</h3>
        
        <div class="redginger-info-item">
          <strong>Street Address</strong>
          <p>401 S Tryon St, Suite 130<br>Charlotte, NC 28202<br>United States</p>
        </div>

        <div class="redginger-info-item">
          <strong>Direct Reservations &amp; Inquiries</strong>
          <p><a href="tel:9808198837" style="font-weight:700; font-size:1.15rem; color:var(--redginger-primary);">(980) 819-8837</a></p>
        </div>

        <div class="redginger-info-item">
          <strong>Email Inquiries</strong>
          <p><a href="mailto:contact@redgingercharlotte.com">contact@redgingercharlotte.com</a></p>
        </div>

        <div class="redginger-info-item">
          <strong>Neighborhood &amp; Parking</strong>
          <p>Located on South Tryon Street at Two Wells Fargo Center, directly across from the Mint Museum Uptown and the Knight Theater. Convenient validated parking available in the adjacent Two Wells Fargo parking deck, and easily accessible from the LYNX Blue Line 3rd St/Convention Center station.</p>
        </div>
      </div>

      <div class="redginger-info-card">
        <h3>Hours of Operation</h3>
        
        <div class="redginger-info-item">
          <strong>Monday - Thursday</strong>
          <p>11:00 AM - 2:30 PM (Executive Lunch)<br>4:30 PM - 10:00 PM (Teppanyaki Dinner &amp; Sushi Lounge)</p>
        </div>

        <div class="redginger-info-item">
          <strong>Friday</strong>
          <p>11:00 AM - 2:30 PM (Lunch)<br>4:30 PM - 11:00 PM (Dinner, Cocktails &amp; Late Night)</p>
        </div>

        <div class="redginger-info-item">
          <strong>Saturday</strong>
          <p>4:30 PM - 11:00 PM<br><small style="color:var(--redginger-text-muted);">Dinner Service, Celebrations &amp; Lounge</small></p>
        </div>

        <div class="redginger-info-item">
          <strong>Sunday</strong>
          <p>11:30 AM - 9:30 PM<br><small style="color:var(--redginger-text-muted);">Continuous All-Day Hibachi &amp; Sushi Dining</small></p>
        </div>
      </div>
    </div>

    <!-- FAQ Accordion -->
    <div class="redginger-section-title" style="margin-top:60px;">
      <h2>Frequently Asked Questions</h2>
      <p>Everything you need to know before visiting Red Ginger on South Tryon.</p>
    </div>

    <div style="max-width:800px; margin:0 auto;">
      <div class="redginger-accordion">
        <div class="redginger-accordion-header">
          <span>Are reservations required for teppanyaki tables?</span>
          <span class="redginger-accordion-icon">+</span>
        </div>
        <div class="redginger-accordion-content">
          <p>While walk-ins are always welcomed in our sushi lounge and bar area, we strongly recommend calling (980) 819-8837 to reserve teppanyaki hibachi tables, especially for weekend evenings and larger groups.</p>
        </div>
      </div>

      <div class="redginger-accordion">
        <div class="redginger-accordion-header">
          <span>Can I order sushi at the teppanyaki hibachi tables?</span>
          <span class="redginger-accordion-icon">+</span>
        </div>
        <div class="redginger-accordion-content">
          <p>Yes, our full sushi bar menu, appetizers, and signature maki rolls can be ordered directly from your teppanyaki table to enjoy before or alongside your grilled entree.</p>
        </div>
      </div>

      <div class="redginger-accordion">
        <div class="redginger-accordion-header">
          <span>What parking options are available in Uptown?</span>
          <span class="redginger-accordion-icon">+</span>
        </div>
        <div class="redginger-accordion-content">
          <p>Guests can park in the Two Wells Fargo Center parking garage (entrance off S Church St or MLK Jr Blvd). We provide parking validation for evening dinner guests.</p>
        </div>
      </div>

      <div class="redginger-accordion">
        <div class="redginger-accordion-header">
          <span>Do you offer takeout and delivery for lunch and dinner?</span>
          <span class="redginger-accordion-icon">+</span>
        </div>
        <div class="redginger-accordion-content">
          <p>Yes, our full sushi menu, lunch bento boxes, and kitchen entrees are available for fast phone takeout pickup by calling (980) 819-8837.</p>
        </div>
      </div>
    </div>

    <div class="redginger-cta-banner" style="margin-top:50px;">
      <h2>We Look Forward to Welcoming You</h2>
      <p>401 S Tryon St, Suite 130, Charlotte, NC 28202 | Call (980) 819-8837</p>
      <div class="redginger-cta-btns">
        <a href="tel:9808198837" class="redginger-btn-hero-primary">Call (980) 819-8837</a>
        <a href="menu.html" class="redginger-btn-hero-secondary">Explore Menu</a>
      </div>
    </div>
  </main>

{footer_html()}'''

with open(os.path.join(DIR, "private-dining-and-group-events.html"), "w", encoding="utf-8") as f:
    f.write(events_page)
print("Wrote private-dining-and-group-events.html")

with open(os.path.join(DIR, "visit.html"), "w", encoding="utf-8") as f:
    f.write(visit_page)
print("Wrote visit.html")
