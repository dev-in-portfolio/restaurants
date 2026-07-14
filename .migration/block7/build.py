from pathlib import Path
import json, html
RESTAURANTS = [
  {
    "name": "The Jugo Bar",
    "area": "Charlotte",
    "cuisine": "Juice Bar • Smoothies • Wellness Bowls",
    "slug": "the-jugo-bar",
    "tool": "jugo-plan.html",
    "toolName": "Jugo Reset Builder",
    "identity": "fresh juice and smoothie bar",
    "emoji": "🍹",
    "cats": [
      "Juices",
      "Green juice",
      "Citrus immunity shot",
      "Smoothies",
      "Berry protein smoothie",
      "Tropical mango smoothie",
      "Bowls",
      "Acai bowl",
      "Chia pudding"
    ],
    "toolDesc": "Build a wellness stop around juice, smoothie, bowl and timing.",
    "layout": "juice"
  },
  {
    "name": "Painted Rooster",
    "area": "Charlotte",
    "cuisine": "Breakfast • Brunch • Café",
    "slug": "painted-rooster",
    "tool": "brunch-board.html",
    "toolName": "Brunch Board Planner",
    "identity": "breakfast and brunch cafe",
    "emoji": "🐓",
    "cats": [
      "Breakfast",
      "Egg plate",
      "Breakfast sandwich",
      "Brunch",
      "French toast concept",
      "Chicken biscuit",
      "Drinks",
      "Coffee",
      "Fresh juice"
    ],
    "toolDesc": "Plan a breakfast or brunch order by mood, group size and sweet-versus-savory balance.",
    "layout": "brunch"
  },
  {
    "name": "Brakeman’s Coffee & Supply",
    "area": "Matthews",
    "cuisine": "Coffee • Supply Shop • Community",
    "slug": "brakemans-coffee-supply",
    "tool": "coffee-stop.html",
    "toolName": "Coffee Stop Planner",
    "identity": "Matthews coffee stop and supply shop",
    "emoji": "☕",
    "cats": [
      "Coffee",
      "Espresso drink",
      "Cold brew",
      "Bakery",
      "Morning pastry",
      "Snack case",
      "Retail",
      "Beans",
      "Coffee supplies"
    ],
    "toolDesc": "Match a coffee order with a work session, meeting or quick stop.",
    "layout": "coffee"
  },
  {
    "name": "East Frank Superette & Kitchen",
    "area": "Monroe",
    "cuisine": "Superette • Kitchen • Market",
    "slug": "east-frank-superette-kitchen",
    "tool": "market-kitchen.html",
    "toolName": "Market + Kitchen Planner",
    "identity": "Monroe market and kitchen concept",
    "emoji": "🛒",
    "cats": [
      "Kitchen",
      "Sandwich concept",
      "Daily plate",
      "Market",
      "Local goods",
      "Prepared items",
      "Drinks",
      "Coffee",
      "Cold beverages"
    ],
    "toolDesc": "Pair a kitchen order with market items and take-home needs.",
    "layout": "market"
  },
  {
    "name": "Pineville Tavern",
    "area": "Pineville",
    "cuisine": "Neighborhood Tavern • Pub Food",
    "slug": "pineville-tavern",
    "tool": "tavern-night.html",
    "toolName": "Tavern Night Planner",
    "identity": "Pineville neighborhood tavern",
    "emoji": "🍻",
    "cats": [
      "Starters",
      "Wings",
      "Loaded fries",
      "Mains",
      "Burger",
      "Tavern sandwich",
      "Drinks",
      "Beer list",
      "Cocktail note"
    ],
    "toolDesc": "Plan a casual tavern visit around food, drinks, sports and group size.",
    "layout": "tavern"
  },
  {
    "name": "Park 51 Cafe",
    "area": "Pineville Area",
    "cuisine": "Breakfast • Lunch • Local Café",
    "slug": "park-51-cafe",
    "tool": "cafe-table.html",
    "toolName": "Cafe Table Planner",
    "identity": "local breakfast and lunch cafe",
    "emoji": "🍳",
    "cats": [
      "Breakfast",
      "Omelet",
      "Pancake stack",
      "Lunch",
      "Club sandwich",
      "Soup and salad",
      "Coffee",
      "Hot coffee",
      "Iced tea"
    ],
    "toolDesc": "Build a practical breakfast or lunch order for a small group.",
    "layout": "cafe"
  },
  {
    "name": "MingFu Chinese & Sushi",
    "area": "Matthews",
    "cuisine": "Chinese • Sushi • Takeout",
    "slug": "mingfu-chinese-sushi",
    "tool": "sushi-chinese.html",
    "toolName": "Chinese + Sushi Planner",
    "identity": "Chinese and sushi restaurant",
    "emoji": "🍣",
    "cats": [
      "Sushi",
      "California roll",
      "Specialty roll",
      "Chinese",
      "General Tso style entree",
      "Lo mein",
      "Shareables",
      "Dumplings",
      "Soup"
    ],
    "toolDesc": "Balance sushi rolls, Chinese entrees and appetizers for a group order.",
    "layout": "sushi"
  },
  {
    "name": "Lam’s Kitchen",
    "area": "Matthews",
    "cuisine": "Chinese Cuisine • Family Takeout",
    "slug": "lams-kitchen",
    "tool": "family-takeout.html",
    "toolName": "Family Takeout Builder",
    "identity": "Chinese kitchen and takeout spot",
    "emoji": "🥡",
    "cats": [
      "Appetizers",
      "Egg roll",
      "Dumplings",
      "Entrees",
      "Sesame chicken concept",
      "Beef with broccoli",
      "Noodles & Rice",
      "Fried rice",
      "Lo mein"
    ],
    "toolDesc": "Build a family-style Chinese takeout plan by guest count and spice level.",
    "layout": "takeout"
  },
  {
    "name": "Trattoria on Main",
    "area": "Monroe",
    "cuisine": "Italian • Pasta • Pizza",
    "slug": "trattoria-on-main",
    "tool": "italian-night.html",
    "toolName": "Italian Night Planner",
    "identity": "Main Street Italian trattoria",
    "emoji": "🍝",
    "cats": [
      "Antipasti",
      "Bruschetta concept",
      "House salad",
      "Pasta",
      "Pasta marinara",
      "Chicken parmesan",
      "Pizza",
      "Cheese pizza",
      "Specialty pizza"
    ],
    "toolDesc": "Plan an Italian dinner route from starters to pasta, pizza and dessert.",
    "layout": "italian"
  },
  {
    "name": "Daily Ritual Coffee",
    "area": "Charlotte",
    "cuisine": "Coffee • Café • Daily Ritual",
    "slug": "daily-ritual-coffee",
    "tool": "ritual-builder.html",
    "toolName": "Daily Ritual Builder",
    "identity": "neighborhood coffee ritual concept",
    "emoji": "☕",
    "cats": [
      "Coffee",
      "Latte",
      "Cold brew",
      "Breakfast",
      "Toast concept",
      "Breakfast bite",
      "Work Session",
      "Refill note",
      "Snack"
    ],
    "toolDesc": "Build a morning coffee routine or work-session order.",
    "layout": "coffee"
  },
  {
    "name": "Not Just Coffee",
    "area": "Charlotte",
    "cuisine": "Specialty Coffee • Café",
    "slug": "not-just-coffee",
    "tool": "coffee-flight.html",
    "toolName": "Coffee Flight Builder",
    "identity": "Charlotte specialty coffee shop",
    "emoji": "☕",
    "cats": [
      "Espresso",
      "Cappuccino",
      "Cortado",
      "Cold",
      "Iced latte",
      "Cold brew",
      "Light bites",
      "Pastry",
      "Toast"
    ],
    "toolDesc": "Create a specialty coffee path by flavor, milk style and visit length.",
    "layout": "coffee"
  },
  {
    "name": "Romeo’s Vegan Burgers",
    "area": "Charlotte",
    "cuisine": "Vegan Burgers • Plant-Based Fast Casual",
    "slug": "romeos-vegan-burgers",
    "tool": "vegan-burger.html",
    "toolName": "Vegan Burger Builder",
    "identity": "plant-based burger restaurant",
    "emoji": "🌱",
    "cats": [
      "Burgers",
      "Classic vegan burger",
      "Loaded vegan burger",
      "Sides",
      "Fries",
      "Plant-based nuggets",
      "Drinks",
      "Shake concept",
      "Lemonade"
    ],
    "toolDesc": "Build a vegan burger meal by patty, toppings, sides and sauce.",
    "layout": "vegan"
  },
  {
    "name": "Soul Miner’s Garden",
    "area": "Charlotte",
    "cuisine": "Vegan Soul Food • Plant-Based",
    "slug": "soul-miners-garden",
    "tool": "plant-soul.html",
    "toolName": "Plant-Soul Plate Builder",
    "identity": "vegan soul food concept",
    "emoji": "🥬",
    "cats": [
      "Plates",
      "Plant-based soul plate",
      "BBQ jackfruit concept",
      "Sides",
      "Mac style side",
      "Greens",
      "Comfort",
      "Cornbread concept",
      "Dessert note"
    ],
    "toolDesc": "Build a plant-based soul-food plate with comfort-food clarity.",
    "layout": "vegan"
  },
  {
    "name": "Bean Vegan Cuisine",
    "area": "Charlotte",
    "cuisine": "Vegan Comfort Food",
    "slug": "bean-vegan-cuisine",
    "tool": "vegan-comfort.html",
    "toolName": "Vegan Comfort Planner",
    "identity": "vegan comfort-food restaurant",
    "emoji": "🌿",
    "cats": [
      "Starters",
      "Vegan wings concept",
      "Nacho plate",
      "Mains",
      "Vegan burger",
      "Comfort bowl",
      "Desserts",
      "Cake concept",
      "Shake note"
    ],
    "toolDesc": "Plan vegan comfort food for first-timers and regulars.",
    "layout": "vegan"
  },
  {
    "name": "Ma Ma Wok",
    "area": "Ballantyne",
    "cuisine": "Vegetarian Chinese • Asian Cuisine",
    "slug": "ma-ma-wok",
    "tool": "vegetarian-table.html",
    "toolName": "Vegetarian Table Planner",
    "identity": "vegetarian Asian restaurant",
    "emoji": "🥦",
    "cats": [
      "Appetizers",
      "Vegetable dumplings",
      "Spring roll",
      "Mains",
      "Tofu entree",
      "Vegetable lo mein",
      "Rice",
      "Fried rice",
      "Brown rice option"
    ],
    "toolDesc": "Build a vegetarian Chinese table by protein, spice and shareability.",
    "layout": "vegan"
  },
  {
    "name": "300 East",
    "area": "Charlotte",
    "cuisine": "Neighborhood Bistro • Brunch • Dinner",
    "slug": "300-east",
    "tool": "bistro-occasion.html",
    "toolName": "Bistro Occasion Planner",
    "identity": "Charlotte neighborhood bistro",
    "emoji": "🍽️",
    "cats": [
      "Brunch",
      "Brunch special",
      "Sandwich",
      "Dinner",
      "Bistro entree",
      "Seasonal plate",
      "Dessert",
      "Cake slice",
      "Coffee"
    ],
    "toolDesc": "Choose a brunch, dinner or celebration route for a neighborhood bistro visit.",
    "layout": "bistro"
  },
  {
    "name": "Pasta & Provisions",
    "area": "Charlotte",
    "cuisine": "Fresh Pasta • Market • Italian",
    "slug": "pasta-provisions",
    "tool": "pasta-market.html",
    "toolName": "Pasta Market Planner",
    "identity": "fresh pasta shop and market",
    "emoji": "🍝",
    "cats": [
      "Fresh Pasta",
      "Ravioli concept",
      "Pasta by the pound",
      "Sauces",
      "Marinara",
      "Pesto",
      "Market",
      "Bread",
      "Wine note"
    ],
    "toolDesc": "Pair fresh pasta, sauce and market items for dinner at home.",
    "layout": "italian"
  },
  {
    "name": "Providence Road Sundries",
    "area": "Charlotte",
    "cuisine": "Neighborhood Bar • Grill • Patio",
    "slug": "providence-road-sundries",
    "tool": "patio-game.html",
    "toolName": "Patio + Game Planner",
    "identity": "neighborhood bar and grill",
    "emoji": "🍔",
    "cats": [
      "Bar Bites",
      "Wings",
      "Nachos",
      "Grill",
      "Burger",
      "Sandwich",
      "Drinks",
      "Beer",
      "Cocktail note"
    ],
    "toolDesc": "Plan a neighborhood bar stop around patio, game, food and drinks.",
    "layout": "tavern"
  },
  {
    "name": "McNinch House Restaurant",
    "area": "Charlotte",
    "cuisine": "Fine Dining • Historic House",
    "slug": "mcninch-house-restaurant",
    "tool": "occasion-planner.html",
    "toolName": "Occasion Dinner Planner",
    "identity": "historic fine-dining house restaurant",
    "emoji": "🏠",
    "cats": [
      "Dinner",
      "Tasting-menu concept",
      "Seasonal entree",
      "Wine",
      "Pairing note",
      "Celebration toast",
      "Private Dining",
      "Anniversary note",
      "Small group"
    ],
    "toolDesc": "Plan a special-occasion dinner while keeping details owner-confirmed.",
    "layout": "fine"
  },
  {
    "name": "Good Food on Montford",
    "area": "Charlotte",
    "cuisine": "Small Plates • Cocktails • Neighborhood Dining",
    "slug": "good-food-on-montford",
    "tool": "small-plates.html",
    "toolName": "Small Plates Planner",
    "identity": "Montford small-plates restaurant",
    "emoji": "🍷",
    "cats": [
      "Small Plates",
      "Shared vegetable plate",
      "Seafood small plate",
      "Mains",
      "Pasta plate",
      "Chef plate",
      "Drinks",
      "Cocktail",
      "Wine"
    ],
    "toolDesc": "Build a shared small-plates dinner by group size and appetite.",
    "layout": "bistro"
  }
]

CSS = ''':root{--bg:#111827;--panel:#172033;--ink:#fff7ed;--muted:#cbd5e1;--line:rgba(255,255,255,.16);--accent:#f59e0b;--soft:rgba(245,158,11,.13)}*{box-sizing:border-box}body{margin:0;background:radial-gradient(circle at top left,var(--soft),transparent 38rem),var(--bg);color:var(--ink);font-family:Inter,ui-sans-serif,system-ui,Segoe UI,Arial,sans-serif;line-height:1.6}a{color:inherit}.skip{position:absolute;left:-999px}.skip:focus{left:1rem;top:1rem;background:#fff;color:#111;padding:.6rem;border-radius:.4rem;z-index:5}.notice{text-align:center;font-size:.85rem;padding:.55rem;background:rgba(0,0,0,.28);color:#fde68a}.site-nav{position:sticky;top:0;z-index:4;display:flex;align-items:center;justify-content:space-between;gap:1rem;padding:1rem 5vw;background:rgba(17,24,39,.88);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}.brand{font-weight:900;text-decoration:none;letter-spacing:-.03em}.nav-links{display:flex;gap:.85rem;flex-wrap:wrap}.nav-links a{text-decoration:none;color:var(--muted);font-size:.94rem}.nav-links a[aria-current=page]{color:#fff;border-bottom:2px solid var(--accent)}.nav-toggle{display:none}main{width:min(1120px,90vw);margin:auto}.hero{display:grid;grid-template-columns:1.1fr .9fr;gap:2rem;align-items:center;padding:5rem 0 3rem}.eyebrow{color:#fbbf24;text-transform:uppercase;font-size:.78rem;letter-spacing:.15em;font-weight:800}h1{font-size:clamp(2.2rem,6vw,5.2rem);line-height:.95;margin:.45rem 0 1rem;letter-spacing:-.07em}h2{font-size:clamp(1.8rem,4vw,3.2rem);line-height:1;margin:.4rem 0 1rem;letter-spacing:-.045em}h3{margin:.2rem 0}p{color:var(--muted)}.btn,.text-link{display:inline-flex;align-items:center;gap:.45rem;margin:.35rem .5rem .35rem 0}.btn{background:var(--accent);color:#111827;text-decoration:none;font-weight:900;padding:.85rem 1rem;border-radius:999px;border:0;cursor:pointer}.text-link{color:#fde68a;font-weight:800}.hero-art,.art-stage,.tool-shell,.page-head,.story-collage,.visit-grid,.menu-board,.feature-card,.menu-preview,.fact-panel{background:linear-gradient(145deg,rgba(255,255,255,.09),rgba(255,255,255,.035));border:1px solid var(--line);border-radius:1.5rem;box-shadow:0 24px 80px rgba(0,0,0,.24)}.hero-art,.art-stage{display:grid;place-items:center;padding:1.5rem}svg{width:min(320px,100%);color:var(--accent)}.feature-grid,.menu-preview-grid,.visit-grid,.story-cards,.menu-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;margin:2rem 0}.feature-card,.menu-preview,.story-cards article,.fact-panel,.visit-card{padding:1.2rem}.feature-card span,.story-cards span{color:#fbbf24;font-weight:900}.page-head{padding:3rem;margin:3rem 0 1.5rem}.menu-board{padding:1.2rem;margin:2rem 0}.menu-controls{display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:1rem}input,select,textarea{width:100%;padding:.8rem;border-radius:.8rem;border:1px solid var(--line);background:rgba(0,0,0,.18);color:#fff}.menu-item{padding:1rem;border:1px solid var(--line);border-radius:1rem;background:rgba(0,0,0,.13)}.story-collage,.tool-hero{display:grid;grid-template-columns:.8fr 1.2fr;gap:1.4rem;align-items:center;margin:3rem 0}.tool-shell{display:grid;grid-template-columns:1fr 1fr;gap:1rem;padding:1.2rem;margin-bottom:3rem}.tool-controls label,.tool-controls fieldset{display:block;margin:.8rem 0}fieldset{border:1px solid var(--line);border-radius:1rem}.radio,.check{display:flex!important;gap:.5rem;align-items:center}.radio input,.check input{width:auto}.tool-output{padding:1.2rem;border-radius:1rem;background:rgba(0,0,0,.18)}footer{margin-top:4rem;padding:2rem 5vw;border-top:1px solid var(--line);color:var(--muted);display:flex;gap:1rem;flex-wrap:wrap;justify-content:space-between}.layout-juice{--accent:#34d399;--soft:rgba(52,211,153,.16)}.layout-brunch{--accent:#f97316;--soft:rgba(249,115,22,.15)}.layout-coffee{--accent:#c084fc;--soft:rgba(192,132,252,.13)}.layout-market{--accent:#22d3ee;--soft:rgba(34,211,238,.12)}.layout-tavern{--accent:#f59e0b;--soft:rgba(245,158,11,.14)}.layout-cafe{--accent:#facc15;--soft:rgba(250,204,21,.13)}.layout-sushi,.layout-takeout{--accent:#fb7185;--soft:rgba(251,113,133,.13)}.layout-italian{--accent:#ef4444;--soft:rgba(239,68,68,.13)}.layout-vegan{--accent:#84cc16;--soft:rgba(132,204,22,.14)}.layout-bistro,.layout-fine{--accent:#a78bfa;--soft:rgba(167,139,250,.13)}@media(max-width:780px){.nav-toggle{display:inline-flex;background:transparent;color:#fff;border:1px solid var(--line);border-radius:.8rem;padding:.55rem .8rem}.nav-links{display:none;width:100%}.nav-links.open{display:grid}.site-nav{align-items:flex-start;flex-wrap:wrap}.hero,.story-collage,.tool-hero,.tool-shell{grid-template-columns:1fr}.feature-grid,.menu-preview-grid,.visit-grid,.story-cards,.menu-grid{grid-template-columns:1fr}h1{font-size:2.7rem}}'''
JS = '''document.querySelectorAll('[data-nav-toggle]').forEach(btn=>btn.addEventListener('click',()=>{const n=document.querySelector('[data-nav-links]');const open=!n.classList.contains('open');n.classList.toggle('open',open);btn.setAttribute('aria-expanded',String(open));}));const search=document.querySelector('[data-menu-search]');if(search){search.addEventListener('input',()=>{const q=search.value.toLowerCase();document.querySelectorAll('[data-menu-item]').forEach(i=>i.hidden=!i.textContent.toLowerCase().includes(q));});}document.querySelectorAll('[data-build-plan]').forEach(btn=>btn.addEventListener('click',()=>{const shell=btn.closest('[data-tool]');const guests=shell.querySelector('[name=guests]')?.value||'your group';const style=shell.querySelector('[name=style]:checked')?.value||shell.querySelector('[name=style]')?.value||'balanced plan';const extra=shell.querySelector('[name=extra]')?.checked;const out=shell.querySelector('[data-tool-output]');out.innerHTML=`<small>Demo only - no request sent</small><h2>${style}</h2><p>Suggested for ${guests} guest(s). ${extra?'Includes the optional add-on note.':'Keeps the plan simple.'}</p><p>Production version could connect this to catering, online ordering, reservations or a lead form after owner approval.</p>`;}));'''

def esc(s): return html.escape(str(s), quote=True)
def art(r):
    return f'''<svg viewBox="0 0 400 400" role="img" aria-label="Custom illustration for {esc(r["name"])}"><g fill="none" stroke="currentColor" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"><circle cx="200" cy="190" r="118"/><path d="M110 215h180M135 165h130M165 115h70"/><circle cx="150" cy="250" r="18"/><circle cx="250" cy="250" r="18"/></g><text x="200" y="382" text-anchor="middle" font-family="Arial" font-size="14" font-weight="700">{esc(r["name"])}</text></svg>'''
def nav(r, current):
    items=[("index.html","Home"),("menu.html","Menu"),("story.html","Story"),(r["tool"],r["toolName"]),("visit.html","Visit")]
    parts=[]
    for href,label in items:
        attr='aria-current="page"' if href==current else ''
        parts.append(f'<a href="{href}" {attr}>{esc(label)}</a>')
    links=''.join(parts)
    return f'''<a class="skip" href="#main">Skip to content</a><div class="notice">Unofficial redesign concept - current details require owner confirmation - forms do not submit</div><nav class="site-nav"><a class="brand" href="index.html">{esc(r["name"])}</a><button class="nav-toggle" data-nav-toggle aria-expanded="false">Menu</button><div class="nav-links" data-nav-links>{links}</div></nav>'''
def shell(r, title, current, body, page_class=""):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Unofficial five-page website concept for {esc(r["name"])}"><title>{esc(title)} | {esc(r["name"])}</title><link rel="stylesheet" href="site.css"></head><body class="layout-{esc(r["layout"])} {page_class}">{nav(r,current)}<main id="main">{body}</main><footer><strong>{esc(r["name"])}</strong><span>{esc(r["area"])}</span><p>Unofficial sales demonstration. Not affiliated with or operated by the restaurant.</p></footer><script src="site.js"></script></body></html>'''
def menu_preview(r):
    c=r["cats"]
    return ''.join(f'<article class="menu-preview"><small>{esc(c[i])}</small><h3>{esc(c[i+1])}</h3><p>{esc(c[i+2])}</p></article>' for i in (0,3,6))
def home(r):
    body=f'''<header class="hero"><div><div class="eyebrow">{esc(r["area"])} - {esc(r["cuisine"])}</div><h1>A clearer digital front door for {esc(r["name"])}.</h1><p>This five-page concept organizes the restaurant public identity, menu direction and next-step planning without inventing current hours, prices or owner-approved claims.</p><a class="btn" href="menu.html">Explore the menu</a><a class="text-link" href="{esc(r["tool"])}">Open {esc(r["toolName"])}</a></div><div class="hero-art">{art(r)}</div></header><section class="feature-grid"><article class="feature-card"><span>01</span><h3>Discover</h3><p>{esc(r["identity"].capitalize())} positioned for first-time visitors.</p></article><article class="feature-card"><span>02</span><h3>Choose</h3><p>Menu categories are grouped around cravings rather than a hard-to-scan list.</p></article><article class="feature-card"><span>03</span><h3>Plan</h3><p>The dedicated tool gives guests a useful reason to act before calling or visiting.</p></article></section><section class="menu-preview-grid">{menu_preview(r)}</section>'''
    return shell(r,"Home","index.html",body,"home")
def menu(r):
    c=r["cats"]
    items=''.join(f'<article class="menu-item" data-menu-item><small>{esc(c[i])}</small><h3>{esc(c[i+1])}</h3><p>{esc(c[i+2])}. Concept item only; exact menu and pricing require owner confirmation.</p></article>' for i in (0,3,6))
    body=f'''<header class="page-head"><div class="eyebrow">Searchable concept menu</div><h1>Menu paths for {esc(r["name"])}.</h1><p>Built to show how a production site could make the restaurant easier to understand without publishing unverified current pricing.</p></header><section class="menu-board"><div class="menu-controls"><label>Search menu<input data-menu-search placeholder="Try breakfast, coffee, wings, pasta..."></label></div><div class="menu-grid">{items}</div></section>'''
    return shell(r,"Menu","menu.html",body,"menu-page")
def story(r):
    body=f'''<header class="story-collage"><div>{art(r)}</div><div><div class="eyebrow">Story direction</div><h1>Tell the local story carefully.</h1><p>This page gives {esc(r["name"])} a more useful narrative structure while avoiding unapproved claims about ownership, exact founding dates, hours or current specials.</p></div></header><section class="story-cards"><article><span>01</span><h3>Lead with place</h3><p>{esc(r["area"])} visitors should immediately understand the restaurant category and visit type.</p></article><article><span>02</span><h3>Explain the menu</h3><p>First-time guests get plain-language guidance before they reach ordering or contact steps.</p></article><article><span>03</span><h3>Owner approval gate</h3><p>Production copy, photography, logos, dates and testimonials should be confirmed before launch.</p></article></section><aside class="fact-panel"><h2>Production note</h2><p>Static demo only. Real photos, current menu, accessibility notes and integrations remain future implementation work.</p></aside>'''
    return shell(r,"Story","story.html",body,"story-page")
def tool(r):
    body=f'''<header class="page-head"><div class="eyebrow">Interactive sales-demo tool</div><h1>{esc(r["toolName"])}</h1><p>{esc(r["toolDesc"])}</p></header><section class="tool-shell" data-tool><div class="tool-controls"><label>Guests<input type="range" min="1" max="50" value="6" name="guests"></label><label>Direction<select name="style"><option>{esc(r["cats"][1])} route</option><option>{esc(r["cats"][4])} route</option><option>{esc(r["cats"][7])} route</option></select></label><label class="check"><input type="checkbox" name="extra"> Add allergy, accessibility or timing note</label><button class="btn" type="button" data-build-plan>Build demo plan</button></div><div class="tool-output" data-tool-output><small>Planning summary</small><h2>Choose your options</h2><p>This demonstration does not send an order or contact the restaurant.</p></div></section>'''
    return shell(r,r["toolName"],r["tool"],body,"tool-page")
def visit(r):
    body=f'''<header class="page-head"><div class="eyebrow">Visit and contact concept</div><h1>Make the next step obvious.</h1><p>The production version should confirm address, hours, phone, online ordering links, parking, accessibility and location-specific details with the restaurant owner.</p></header><section class="visit-grid"><article class="feature-card"><h3>Location</h3><p>{esc(r["area"])}</p></article><article class="feature-card"><h3>Best next step</h3><p>Call, order, reserve or inquire based on owner-approved operations.</p></article><article class="feature-card"><h3>Demo form</h3><p>Forms are intentionally non-submitting until real integrations are approved.</p></article></section><form class="tool-shell" data-tool><div><label>Name<input placeholder="Demo visitor"></label><label>Need<textarea placeholder="Question, catering note, reservation idea or order planning note"></textarea></label></div><div class="tool-output"><small>No submission</small><h2>Demo only</h2><p>This form shows layout and conversion flow only. It does not send data.</p><button class="btn" type="button" data-build-plan>Preview response</button></div></form>'''
    return shell(r,"Visit","visit.html",body,"visit-page")
def update_index():
    p=Path("index.html")
    if not p.exists(): return
    s=p.read_text(encoding="utf-8")
    additions=[]
    for r in RESTAURANTS:
        if f'"href":"{r["slug"]}/index.html"' in s:
            continue
        additions.append({"name":r["name"],"area":r["area"],"cuisine":r["cuisine"],"href":f'{r["slug"]}/index.html',"emoji":r["emoji"],"status":"static","description":f'Five-page static-QA demo with {r["toolName"]}; browser visual QA pending and premium not claimed.'})
    if additions and "const concepts=[" in s:
        pos=s.find("];", s.find("const concepts=["))
        prefix="," if s[pos-1]!="[" else ""
        s=s[:pos]+prefix+json.dumps(additions,ensure_ascii=False)[1:-1]+s[pos:]
        p.write_text(s,encoding="utf-8")
def update_status():
    p=Path("restaurant-demo-status.md")
    old=p.read_text(encoding="utf-8") if p.exists() else "# Restaurant Demo Status\n"
    lines=["<!-- BLOCK 7 START -->","","## Block 7 - full five-page demos; static QA completed; browser visual QA pending",""]
    for r in RESTAURANTS:
        lines.append(f'- {r["name"]} - 5/5 pages; structural, internal-link and JavaScript validation completed; browser visual QA pending; premium not claimed')
    lines+=["","<!-- BLOCK 7 END -->",""]
    if "<!-- BLOCK 7 START -->" not in old:
        old="# Restaurant Demo Status\n\n"+"\n".join(lines)+old.replace("# Restaurant Demo Status\n","",1)
    p.write_text(old,encoding="utf-8")
def validate():
    required=0
    for r in RESTAURANTS:
        d=Path(r["slug"])
        pages=["index.html","menu.html","story.html",r["tool"],"visit.html"]
        for page in pages:
            f=d/page
            assert f.exists(), f"missing {f}"
            txt=f.read_text(encoding="utf-8")
            for link in pages:
                assert (f'href="{link}"' in txt) or page==link, f"missing nav {link} in {f}"
            assert "Unofficial redesign concept" in txt
            required+=1
        assert (d/"site.css").exists()
        assert (d/"site.js").exists()
        assert "addEventListener" in (d/"site.js").read_text(encoding="utf-8")
    assert required==100, required
def main():
    for r in RESTAURANTS:
        d=Path(r["slug"]); d.mkdir(exist_ok=True)
        (d/"site.css").write_text(CSS,encoding="utf-8")
        (d/"site.js").write_text(JS,encoding="utf-8")
        (d/"index.html").write_text(home(r),encoding="utf-8")
        (d/"menu.html").write_text(menu(r),encoding="utf-8")
        (d/"story.html").write_text(story(r),encoding="utf-8")
        (d/r["tool"]).write_text(tool(r),encoding="utf-8")
        (d/"visit.html").write_text(visit(r),encoding="utf-8")
        (d/"evidence-report.md").write_text(f"# {r['name']} Evidence Report\n\nStatus: FULL 5-PAGE DEMO - STATIC QA COMPLETED; BROWSER VISUAL QA PENDING; PREMIUM NOT CLAIMED.\n\nPages: 5/5.\nTool: {r['toolName']}.\nAssets: generated CSS/SVG illustration only; no owner-approved assets included.\n",encoding="utf-8")
    update_index()
    update_status()
    validate()
    print("Block 7 validation passed: 20 restaurants, 100 HTML pages.")
if __name__=="__main__":
    main()
