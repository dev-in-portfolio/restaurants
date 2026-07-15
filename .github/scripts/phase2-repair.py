#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html as html_lib
import json
import os
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(os.environ.get('WORK_ROOT', '.')).resolve()
OUT = Path(os.environ.get('OUT_DIR', 'out')).resolve()
MARKER = 'PHASE2-CONTENT-EXPANSION'

TARGETS = [
    {'group':'A','name':'AJ Family Restaurant','c':['aj-family-restaurant'],'expand':[('comfort-plate.html','comfort','family-style breakfast and comfort-food dining')],'main':[]},
    {'group':'A','name':'Alice Jules Coffee House','c':['alice-jules-coffee-house'],'expand':[('drink-lab.html','drink','coffeehouse drinks, flavor choices, and bakery-friendly pairings')],'main':[]},
    {'group':'A','name':'Amina','c':['amina'],'expand':[('signature-experience.html','experience','a polished contemporary dining experience shaped by African-inspired flavors'),('visit.html','visit','planning a relaxed visit for dinner, celebrations, or an evening out')],'main':[]},
    {'group':'A','name':'Anatolia Cafe & Cuisine','c':['anatolia-cafe-and-cuisine','anatolia-cafe-cuisine'],'expand':[('flavor-guide.html','flavor','Turkish and Mediterranean flavor profiles, shareable plates, and balanced meals')],'main':[]},
    {'group':'A','name':'Food For Your Soul CLT','c':['food-soul','food-for-your-soul-clt'],'expand':[('comfort-plate.html','comfort','soul-food comfort, generous plates, and familiar Southern flavors')],'main':[]},
    {'group':'A','name':"Hathaway's Fried Chicken",'c':['hathaways-fried-chicken'],'expand':[('comfort-plate.html','comfort','fried-chicken meals, classic sides, and straightforward family dining')],'main':[]},
    {'group':'A','name':'House of Leng','c':['house-of-leng'],'expand':[('flavor-guide.html','flavor','Chinese restaurant favorites, contrasting textures, and shareable ordering')],'main':[]},
    {'group':'A','name':"Kit's Trackside Crafts",'c':['kits-trackside-crafts'],'expand':[('flight-planner.html','flight','craft beverage tasting, measured pours, and an easy progression from light to bold')],'main':[]},
    {'group':'A','name':'Lang Van','c':['lang-van'],'expand':[('flavor-guide.html','flavor','Vietnamese herbs, broths, grilled dishes, and bright savory balance')],'main':[]},
    {'group':'A','name':'Laurel Market','c':['laurel-market'],'expand':[('signature-experience.html','experience','a neighborhood market-and-cafe experience built around quick meals and thoughtful choices')],'main':[]},
    {'group':'A','name':'Le Kebab Grill','c':['le-kebab-grill'],'expand':[('flavor-guide.html','flavor','Mediterranean grilled meats, fresh sides, sauces, and customizable plates')],'main':[]},
    {'group':'A','name':"Le's Sandwiches & Café",'c':['les-sandwiches-cafe','les-sandwiches-and-cafe'],'expand':[('flavor-guide.html','flavor','Vietnamese sandwiches, crisp herbs, savory fillings, and contrasting textures')],'main':[]},
    {'group':'A','name':'Machu Picchu Peruvian Cuisine','c':['machu-picchu'],'expand':[('flavor-table.html','flavor','Peruvian flavor combinations, bright sauces, grilled preparations, and shareable plates')],'main':[]},
    {'group':'A','name':'Matthews Social House','c':['matthews-social-house'],'expand':[('flight-planner.html','flight','a social tasting plan that helps groups compare drinks and pace an evening together')],'main':[]},
    {'group':'A','name':"Miguel's Restaurant",'c':['miguels-restaurant','miguels'],'expand':[('flavor-table.html','flavor','Mexican restaurant flavors, salsas, grilled choices, and mix-and-match meals')],'main':[]},
    {'group':'A','name':'MJ Donuts','c':['mj-donuts'],'expand':[('box-builder.html','box','building a varied donut box for individuals, families, offices, or gatherings')],'main':[]},
    {'group':'A','name':"Picadeli's Pub-In-Deli",'c':['picadelis-pub-in-deli','picadelis-pub-deli'],'expand':[('flight-planner.html','flight','pub-style beverage tasting paired with a casual deli-and-grill meal')],'main':[]},
    {'group':'A','name':"Queen's Soul Food",'c':['queens-soul','queens-soul-food'],'expand':[('comfort-plate.html','comfort','soul-food plates, familiar sides, and a satisfying meal built around comfort')],'main':[]},
    {'group':'A','name':'República Restaurant & Lounge','c':['republica'],'expand':[('flavor-table.html','flavor','Latin-inspired dining, layered seasoning, shareable courses, and a lounge-paced evening')],'main':[]},
    {'group':'A','name':'The Dive N','c':['the-dive-n','dive-n'],'expand':[('comfort-plate.html','comfort','classic drive-in comfort food, simple combinations, and casual group ordering')],'main':[]},
    {'group':'A','name':'The Palace Restaurant','c':['palace-monroe','the-palace-restaurant','palace-restaurant'],'expand':[('comfort-plate.html','comfort','a traditional family-restaurant meal with familiar choices and an unhurried pace')],'main':[]},
    {'group':'A','name':'The Portrait Gallery','c':['portrait-gallery','the-portrait-gallery'],'expand':[('flight-planner.html','flight','a cocktail-and-lounge tasting sequence designed for conversation and comparison')],'main':[]},
    {'group':'B','name':"DB's Tavern",'c':['dbs-tavern'],'expand':[],'main':['*']},
    {'group':'B','name':"Doan's Vietnamese Cuisine",'c':['doans-vietnamese-cuisine','doans'],'expand':[],'main':['*']},
    {'group':'B','name':'Dolce Osteria','c':['dolce-osteria'],'expand':[],'main':['*']},
    {'group':'B','name':'East 74 Restaurant','c':['east-74','east-74-restaurant'],'expand':[],'main':['*']},
    {'group':'B','name':'El Valle Mexican Restaurant','c':['el-valle','el-valle-mexican-restaurant'],'expand':[],'main':['*']},
    {'group':'B','name':"Geno D's Pizza",'c':['geno-ds','geno-ds-pizza'],'expand':[],'main':['*']},
    {'group':'B','name':'Giddy Goat Coffee Roasters','c':['giddy-goat','giddy-goat-coffee-roasters'],'expand':[],'main':['*']},
    {'group':'B','name':'Gotcha Matcha & Espresso','c':['gotcha-matcha','gotcha-matcha-espresso'],'expand':[],'main':['MISSING']},
    {'group':'B','name':"Grey's Diner",'c':['greys-diner'],'expand':[],'main':['MISSING']},
    {'group':'C','name':'Deejai Thai','c':['deejai-thai'],'expand':[('contact.html','contact','questions about dining, group needs, takeout, and current restaurant information'),('locations.html','locations','choosing the most convenient location and confirming location-specific details')],'main':['*']},
    {'group':'C','name':"Devil's Logic Brewing",'c':['devils-logic-brewing','devils-logic'],'expand':[('contact.html','contact','taproom questions, event planning, group visits, and current availability')],'main':['*']},
    {'group':'C','name':"Dom's Dive Bar",'c':['doms-dive-bar','doms-dive'],'expand':[('contact.html','contact','planning a visit, asking about events, and confirming current bar information')],'main':['*']},
    {'group':'C','name':'DŌZO Japanese-American Kitchen','c':['dozo','dozo-japanese-american-kitchen'],'expand':[('contact.html','contact','reservations, dining questions, dietary conversations, and current service details')],'main':['*']},
    {'group':'C','name':"Duke's Grill",'c':['dukes-grill'],'expand':[('contact.html','contact','family dining questions, group planning, and current restaurant details')],'main':['*']},
    {'group':'C','name':"Fenian's Keep",'c':['fenians-keep'],'expand':[('flight-planner.html','flight','a pub tasting sequence that moves from approachable pours to fuller flavors')],'main':['contact.html','drinks.html','events.html','index.html','story.html']},
    {'group':'C','name':'Flour Shop','c':['flour-shop'],'expand':[('pasta-pairing.html','pasta','matching pasta styles, sauce weight, seasonal ingredients, and beverage choices')],'main':['about.html','index.html','menu.html','reserve.html','visit.html']},
    {'group':'C','name':"Harper's Cafe",'c':['harpers-cafe'],'expand':[('comfort-plate.html','comfort','a neighborhood-cafe meal built around familiar favorites and flexible portions')],'main':['catering.html','contact.html','index.html','menu.html','story.html']},
    {'group':'C','name':'Lula Bánh Mì + Bakery','c':['lula-banh-mi-and-bakery','lula-banh-mi-bakery'],'expand':[('flavor-guide.html','flavor','bánh mì balance, bakery textures, fresh herbs, savory fillings, and bright accents')],'main':['contact.html','events.html','index.html','menu.html','story.html']},
    {'group':'C','name':"Maria's Mexican Restaurant",'c':['marias-mexican-restaurant'],'expand':[('flavor-table.html','flavor','Mexican family-dining flavors, sauces, grilled choices, and shareable ordering')],'main':['contact.html','events.html','index.html','menu.html','story.html']},
]

SKIP_DIRS = {'.git', '.github', 'node_modules', 'out', 'dist', 'build'}

def norm(value: str) -> str:
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    return re.sub(r'[^a-z0-9]+', '', value.lower())

def strip_html(raw: str) -> str:
    raw = re.sub(r'<!--[\s\S]*?-->', ' ', raw)
    raw = re.sub(r'<script[\s\S]*?</script>', ' ', raw, flags=re.I)
    raw = re.sub(r'<style[\s\S]*?</style>', ' ', raw, flags=re.I)
    raw = re.sub(r'<[^>]+>', ' ', raw)
    return re.sub(r'\s+', ' ', html_lib.unescape(raw)).strip()

def html_files(directory: Path) -> list[Path]:
    return sorted(p for p in directory.rglob('*.html') if not any(part in SKIP_DIRS for part in p.parts))

def candidate_paths(slug: str) -> list[Path]:
    return [ROOT / slug, ROOT / 'restaurants' / slug]

def resolve_dir(target: dict) -> Path:
    requested = [f for f, _, _ in target['expand']]
    for slug in target['c']:
        for path in candidate_paths(slug):
            if path.is_dir() and all((path / f).is_file() for f in requested):
                return path
    required = requested or ['index.html']
    options: list[tuple[int, Path]] = []
    for index in ROOT.rglob('index.html'):
        directory = index.parent
        if any(part in SKIP_DIRS for part in directory.parts):
            continue
        if not all((directory / f).is_file() for f in required):
            continue
        sample = ''
        for file in [index] + [(directory / f) for f in requested]:
            try:
                sample += ' ' + file.read_text(encoding='utf-8', errors='ignore')[:30000]
            except OSError:
                pass
        sample_key = norm(strip_html(sample))
        name_key = norm(target['name'])
        score = 100 if name_key and name_key in sample_key else 0
        for token in re.findall(r'[a-z0-9]+', unicodedata.normalize('NFKD', target['name']).encode('ascii','ignore').decode('ascii').lower()):
            if len(token) > 2 and token in sample_key:
                score += 3
        for slug in target['c']:
            if norm(directory.name) == norm(slug):
                score += 50
        options.append((score, directory))
    options.sort(key=lambda item: (-item[0], str(item[1])))
    if not options or options[0][0] < 6:
        raise RuntimeError(f"Could not resolve folder for {target['name']}; candidates={target['c']}")
    if len(options) > 1 and options[0][0] == options[1][0]:
        raise RuntimeError(f"Ambiguous folder for {target['name']}: {options[:3]}")
    return options[0][1]

def add_main_id(raw: str) -> str:
    return re.sub(r'<main(?![^>]*\bid=)([^>]*)>', r'<main id="main"\1>', raw, count=1, flags=re.I)

def normalize_skip_links(raw: str) -> str:
    pattern = re.compile(r'(<a\b[^>]*\bclass=["\'][^"\']*skip[^"\']*["\'][^>]*\bhref=)["\'][^"\']*["\']', re.I)
    raw = pattern.sub(r'\1"#main"', raw)
    pattern2 = re.compile(r'(<a\b[^>]*\bhref=)["\'][^"\']*["\']([^>]*\bclass=["\'][^"\']*skip[^"\']*["\'])', re.I)
    return pattern2.sub(r'\1"#main"\2', raw)

def ensure_main(raw: str, file: Path) -> tuple[str, bool]:
    openings = list(re.finditer(r'<main\b[^>]*>', raw, flags=re.I))
    closings = list(re.finditer(r'</main\s*>', raw, flags=re.I))
    if len(openings) == 1 and len(closings) == 1:
        updated = normalize_skip_links(add_main_id(raw))
        return updated, updated != raw
    if openings or closings:
        raise RuntimeError(f'{file}: malformed existing main elements ({len(openings)} open/{len(closings)} close)')
    body = re.search(r'<body\b[^>]*>', raw, flags=re.I)
    if not body:
        raise RuntimeError(f'{file}: missing body element')
    footer = re.search(r'<footer\b', raw, flags=re.I)
    scripts = list(re.finditer(r'<script\b', raw, flags=re.I))
    body_close = re.search(r'</body\s*>', raw, flags=re.I)
    end = footer.start() if footer else (scripts[-1].start() if scripts else (body_close.start() if body_close else len(raw)))
    segment = raw[body.end():end]
    header_open = re.search(r'<header\b', segment, flags=re.I)
    header_closes = list(re.finditer(r'</header\s*>', segment, flags=re.I))
    nav_closes = list(re.finditer(r'</nav\s*>', segment, flags=re.I))
    start = body.end()
    if header_open and header_closes:
        hc = body.end() + header_closes[0].end()
        if nav_closes and header_open.start() <= nav_closes[0].start():
            start = hc
        elif header_open.start() < 500:
            start = hc
    if start == body.end() and nav_closes:
        start = body.end() + nav_closes[0].end()
    if start >= end:
        raise RuntimeError(f'{file}: unable to find content boundaries for main wrapper')
    updated = raw[:start] + '\n<main id="main">\n' + raw[start:end] + '\n</main>\n' + raw[end:]
    return normalize_skip_links(updated), True

def expansion_copy(name: str, kind: str, focus: str, uid: str) -> str:
    titles = {'comfort':'Build a meal that fits the moment','drink':'Find a drink profile that feels right','experience':'Shape the experience around your occasion','visit':'Plan the visit before you leave home','flavor':'Use flavor, texture, and appetite as your guide','flight':'Taste with a clear progression','box':'Build variety into every box','contact':'Send the details that help the team respond','locations':'Choose the location that matches the plan','pasta':'Pair by sauce, texture, and pace'}
    intros = {
        'comfort':f"A satisfying visit to {name} starts with the kind of comfort you are looking for. Think first about appetite and pace: a complete plate for one person, a lighter combination, or several familiar items shared across the table. This guide keeps the decision practical while leaving room for the personal choices that make comfort food feel familiar.",
        'drink':f"The easiest way to explore {name} is to begin with the drink experience you want rather than a long list of names. Decide whether the moment calls for something bright and refreshing, rich and slow-sipping, gently sweet, or direct and coffee-forward. From there, temperature, texture, and a food pairing can narrow the choice without taking the fun out of discovery.",
        'experience':f"A visit to {name} can be planned around the occasion instead of a rigid sequence. A quick meal, an unhurried dinner, and a celebration each need a different rhythm. Use this page to think through arrival, sharing, pacing, and the point in the meal when the table wants to slow down and enjoy the atmosphere.",
        'visit':f"A smooth visit to {name} begins with a few simple checks before leaving home. Confirm the current service window, decide whether the group needs extra time or accessibility considerations, and keep the restaurant’s current contact channel available in case plans change. A little preparation protects the relaxed part of the experience once everyone arrives.",
        'flavor':f"Ordering at {name} becomes easier when the table talks about flavor and texture before choosing individual dishes. Some guests may want familiar, savory comfort; others may prefer brightness, heat, freshness, or a more adventurous combination. This guide helps the group build a meal with contrast instead of accidentally ordering several dishes that fill the same role.",
        'flight':f"A tasting flight at {name} works best when each selection has a purpose. Begin with an approachable option, move toward fuller aroma or body, and save the most intense choice for later. That order gives every pour enough room to be noticed and makes it easier for a group to compare preferences without rushing through the experience.",
        'box':f"A well-built box from {name} should feel varied without becoming random. Start with the number of people, then balance familiar choices with a few different textures or flavor directions. A thoughtful mix makes the box useful for a household, an office, or a gathering because guests can recognize an easy first choice and still discover something new.",
        'contact':f"The most useful message to {name} is short, specific, and easy to act on. Lead with the reason for reaching out, include the date or general timing when it matters, and explain the size of the group or order. Clear details reduce back-and-forth while still giving the restaurant room to confirm what is currently available.",
        'locations':f"Choosing a {name} location is about more than whichever address appears first. Compare the route, the needs of the group, and the service you expect to use. Location-specific hours, menus, ordering options, and event availability can change, so the best choice is the one confirmed for the actual day and purpose of the visit.",
        'pasta':f"A useful pasta pairing at {name} starts with structure. Consider whether the sauce is light or rich, whether the pasta is delicate or sturdy, and whether the meal should feel bright, comforting, or celebratory. Matching those elements creates balance and helps a beverage or side support the plate rather than compete with it.",
    }
    bullets = {
        'comfort':['Choose the appetite level before choosing individual components.','Use contrasting sides or textures to keep the plate balanced.','For groups, include at least one widely familiar option and one flexible choice.'],
        'drink':['Choose hot, iced, sparkling, creamy, or straightforward first.','Match sweetness and intensity to the food or time of day.','When trying something new, change one variable at a time so the comparison is useful.'],
        'experience':['Match the pace of the meal to the occasion.','Decide early whether the table plans to share or order individually.','Leave room for a final course, conversation, or a second round instead of over-ordering at once.'],
        'visit':['Confirm current hours and any reservation or walk-in expectations.','Plan parking, accessibility, and group arrival before the busiest part of the outing.','Use the restaurant’s current official contact information for time-sensitive questions.'],
        'flavor':['Balance rich dishes with something fresh, acidic, crisp, or herb-forward.','Ask the table about heat tolerance and dietary needs before ordering.','Share strategically so each person can compare flavors without every dish becoming a duplicate.'],
        'flight':['Move from lighter or cleaner profiles toward stronger or sweeter selections.','Use water and food between tastes to reset the palate.','Compare aroma, body, finish, and personal preference rather than looking for one correct winner.'],
        'box':['Plan quantity around the event and how long the box will be served.','Mix familiar favorites with different textures, finishes, or flavor families.','Confirm current availability and dietary handling before relying on a specific assortment.'],
        'contact':['State the reason for the message in the first sentence.','Include timing, group size, and the best way to respond.','For urgent or same-day needs, use the restaurant’s confirmed direct contact method.'],
        'locations':['Compare travel time and the needs of everyone in the group.','Confirm location-specific hours, menus, and services.','Use the official location listing before relying on older directory information.'],
        'pasta':['Pair delicate sauces with a lighter overall meal and richer sauces with enough acidity or freshness.','Use texture as a guide: tender, crisp, creamy, chewy, or slow-cooked.','Confirm current menu details before planning around a particular preparation.'],
    }
    closing = f"This page is organized around {focus}. It is meant to make the choice clearer, not to replace a conversation with the restaurant. Specific dishes, ingredients, prices, hours, availability, service options, and policies can change. Confirm time-sensitive details through the restaurant’s current official channel, especially for allergies, large groups, events, or a visit built around one particular item."
    lis = ''.join(f'<li>{html_lib.escape(item)}</li>' for item in bullets[kind])
    return f'''\n<!-- {MARKER} -->\n<section class="phase2-expanded-content" aria-labelledby="phase2-{uid}" style="max-width:72rem;margin:clamp(2rem,6vw,5rem) auto;padding:clamp(1.25rem,4vw,2.5rem);border:1px solid rgba(127,127,127,.28);border-radius:1rem;line-height:1.75;">\n  <p style="font-size:.78rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;opacity:.72;margin:0 0 .55rem;">Plan with confidence</p>\n  <h2 id="phase2-{uid}" style="margin:.1rem 0 1rem;">{html_lib.escape(titles[kind])}</h2>\n  <p>{html_lib.escape(intros[kind])}</p>\n  <h3 style="margin-top:1.5rem;">A simple way to decide</h3>\n  <ul>{lis}</ul>\n  <p>{html_lib.escape(closing)}</p>\n</section>\n'''

def insert_expansion(raw: str, section: str, file: Path) -> tuple[str, bool]:
    if MARKER in raw:
        return raw, False
    matches = list(re.finditer(r'</main\s*>', raw, flags=re.I))
    if len(matches) != 1:
        raise RuntimeError(f'{file}: expected exactly one main before expansion, found {len(matches)}')
    pos = matches[0].start()
    return raw[:pos] + section + raw[pos:], True

def local_ref_exists(file: Path, ref: str) -> bool:
    clean = ref.split('#',1)[0].split('?',1)[0].strip()
    if not clean or clean.startswith('#') or clean.startswith('/'):
        return True
    if re.match(r'^(https?:|//|mailto:|tel:|sms:|javascript:|data:|blob:)', clean, re.I):
        return True
    try:
        clean = unquote(clean)
    except Exception:
        pass
    return (file.parent / clean).resolve().exists()

def validate_build(target: dict, directory: Path) -> dict:
    files = html_files(directory)
    issues: list[str] = []
    if len(files) < 6:
        issues.append(f'only {len(files)} HTML pages')
    expansion_files = {f for f, _, _ in target['expand']}
    for file in files:
        raw = file.read_text(encoding='utf-8', errors='ignore')
        rel = file.relative_to(directory).as_posix()
        main_open = len(re.findall(r'<main\b', raw, flags=re.I))
        main_close = len(re.findall(r'</main\s*>', raw, flags=re.I))
        if main_open != 1 or main_close != 1:
            issues.append(f'{rel}: expected one main, found {main_open}/{main_close}')
        elif not re.search(r'<main\b[^>]*\bid=["\']main["\']', raw, flags=re.I):
            issues.append(f'{rel}: main is missing id="main"')
        title = re.search(r'<title[^>]*>([\s\S]*?)</title>', raw, flags=re.I)
        if not title or not strip_html(title.group(1)):
            issues.append(f'{rel}: missing title')
        if rel in expansion_files:
            words = re.findall(r"\b[\w’'-]+\b", strip_html(raw))
            if len(words) < 150:
                issues.append(f'{rel}: only {len(words)} visible words after expansion')
            if MARKER not in raw:
                issues.append(f'{rel}: missing expansion marker')
        refs = [m.group(1) for m in re.finditer(r'(?:src|href)=["\']([^"\']+)["\']', raw, flags=re.I)]
        broken = sorted({ref for ref in refs if not local_ref_exists(file, ref)})
        if broken:
            issues.append(f'{rel}: broken local refs {broken}')
    if issues:
        raise RuntimeError(f"{target['name']} validation failed: " + ' | '.join(issues))
    return {'name':target['name'],'group':target['group'],'slug':directory.name,'path':str(directory.relative_to(ROOT)),'pages':len(files),'expanded':sorted(expansion_files)}

def apply_target(target: dict, validate_only: bool) -> dict:
    directory = resolve_dir(target)
    changes: list[str] = []
    all_files = html_files(directory)
    main_spec = target['main']
    if main_spec == ['*']:
        main_targets = all_files
    elif main_spec == ['MISSING']:
        main_targets = [p for p in all_files if not re.search(r'<main\b', p.read_text(encoding='utf-8', errors='ignore'), flags=re.I)]
    else:
        main_targets = [directory / f for f in main_spec]
    for file in main_targets:
        if not file.is_file():
            raise RuntimeError(f"{target['name']}: missing semantic target {file.relative_to(directory)}")
        raw = file.read_text(encoding='utf-8', errors='ignore')
        updated, changed = ensure_main(raw, file)
        if changed and not validate_only:
            file.write_text(updated, encoding='utf-8')
            changes.append(file.relative_to(ROOT).as_posix())
    for filename, kind, focus in target['expand']:
        file = directory / filename
        if not file.is_file():
            raise RuntimeError(f"{target['name']}: missing expansion target {filename}")
        raw = file.read_text(encoding='utf-8', errors='ignore')
        raw2, main_changed = ensure_main(raw, file)
        uid = norm(target['name'] + '-' + filename)[:64]
        updated, content_changed = insert_expansion(raw2, expansion_copy(target['name'], kind, focus, uid), file)
        if (main_changed or content_changed) and not validate_only:
            file.write_text(updated, encoding='utf-8')
            changes.append(file.relative_to(ROOT).as_posix())
    result = validate_build(target, directory)
    result['changedFiles'] = sorted(set(changes))
    return result

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--validate-only', action='store_true')
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    report = {'validateOnly':args.validate_only,'root':str(ROOT),'targets':[],'groups':{'A':0,'B':0,'C':0},'changedFiles':[]}
    seen_dirs: set[Path] = set()
    for target in TARGETS:
        result = apply_target(target, args.validate_only)
        directory = (ROOT / result['path']).resolve()
        if directory in seen_dirs:
            raise RuntimeError(f'Duplicate resolved directory: {directory}')
        seen_dirs.add(directory)
        report['targets'].append(result)
        report['groups'][target['group']] += 1
        report['changedFiles'].extend(result['changedFiles'])
        print(f"[{target['group']}] {target['name']} -> {result['path']} ({result['pages']} pages, {len(result['changedFiles'])} changed)")
    report['changedFiles'] = sorted(set(report['changedFiles']))
    report['targetCount'] = len(report['targets'])
    report['changedFileCount'] = len(report['changedFiles'])
    if report['groups'] != {'A':22,'B':9,'C':10}:
        raise RuntimeError(f"Unexpected group counts: {report['groups']}")
    if len(report['targets']) != 41:
        raise RuntimeError(f"Expected 41 targets, got {len(report['targets'])}")
    (OUT / 'phase2-static-report.json').write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps({'targets':report['targetCount'],'groups':report['groups'],'changedFiles':report['changedFileCount']}, ensure_ascii=False))
    return 0

if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        raise
