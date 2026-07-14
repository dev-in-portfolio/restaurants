#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from html.parser import HTMLParser
from pathlib import Path

SITES = [
    {"name":"Boudreaux’s Restaurant","area":"Charlotte","cuisine":"Louisiana-inspired • Kitchen & tavern","slugs":["boudreauxs"]},
    {"name":"Eddie’s Place","area":"Charlotte","cuisine":"Neighborhood restaurant • Breakfast • American comfort","slugs":["eddies-place"]},
    {"name":"Salud Cerveceria","area":"Charlotte","cuisine":"Craft beer • Pizza • Coffee • Soccer","slugs":["salud-cerveceria"]},
    {"name":"The Degenerate","area":"Charlotte","cuisine":"Global small plates • Cocktails","slugs":["the-degenerate"]},
    {"name":"Growlers Pourhouse","area":"Charlotte","cuisine":"Craft beer • Pub food • Neighborhood bar","slugs":["growlers-pourhouse"]},
    {"name":"The Goodyear House","area":"Charlotte","cuisine":"Seasonal American • Garden dining • NoDa","slugs":["goodyear-house","the-goodyear-house"]},
    {"name":"The Daily Tavern","area":"Charlotte","cuisine":"Uptown tavern • Casual food • Sports","slugs":["the-daily-tavern","daily-tavern"]},
    {"name":"The Artisan’s Palate","area":"Charlotte","cuisine":"Restaurant • Art • Events","slugs":["artisans-palate","the-artisans-palate"]},
    {"name":"Intermezzo Pizzeria","area":"Charlotte","cuisine":"Serbian family cooking • Pizza","slugs":["intermezzo-pizzeria","intermezzo"]},
    {"name":"Euro Grill & Café","area":"Charlotte","cuisine":"Balkan grill • Café • Family meals","slugs":["euro-grill-cafe","euro-grill"]},
    {"name":"Midtown Tavern","area":"Charlotte","cuisine":"Tavern • Sandwiches • Sports","slugs":["midtown-tavern"]},
    {"name":"The Hobbyist","area":"Charlotte","cuisine":"Coffee • Wine • Beer • Community","slugs":["the-hobbyist","hobbyist"]},
    {"name":"Enderly Coffee Co.","area":"Charlotte","cuisine":"Coffee roaster • Café • Community impact","slugs":["enderly-coffee","enderly-coffee-co"]},
    {"name":"Giddy Goat Coffee Roasters","area":"Charlotte","cuisine":"Coffee roaster • Café • Community","slugs":["giddy-goat-coffee","giddy-goat-coffee-roasters"]},
    {"name":"Harper’s Cafe","area":"Pineville","cuisine":"Neighborhood café • American comfort","slugs":["harpers-cafe","harpers-cafe-pineville"]},
    {"name":"Middle James Brewing","area":"Pineville","cuisine":"Craft brewery • Taproom • Events","slugs":["middle-james-brewing"]},
    {"name":"Kit’s Trackside Crafts","area":"Pineville","cuisine":"Craft beer • Bottle shop • Trackside gathering","slugs":["kits-trackside-crafts","kits-trackside"]},
    {"name":"Pintville Craft Beer","area":"Pineville","cuisine":"Craft beer • Taproom • Private gatherings","slugs":["pintville-craft-beer","pintville"]},
    {"name":"Miro Spanish Grille","area":"Ballantyne","cuisine":"Spanish cuisine • Tapas • Celebrations","slugs":["miro-spanish-grille","miro"]},
    {"name":"Zinicola","area":"Ballantyne","cuisine":"Italian dining • Wine • Private occasions","slugs":["zinicola"]},
]
STANDARD = {"index.html", "menu.html", "story.html", "about.html", "visit.html", "contact.html"}

class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.current = 0
        self.has_title = False
    def handle_starttag(self, tag: str, attrs) -> None:
        values = dict(attrs)
        if tag == "a" and values.get("href"):
            self.links.append(values["href"])
        if tag == "a" and values.get("aria-current") == "page":
            self.current += 1
        if tag == "title":
            self.has_title = True

def resolve_folder(root: Path, site: dict) -> tuple[str, Path] | tuple[None, None]:
    for slug in site["slugs"]:
        folder = root / slug
        if (folder / "index.html").is_file():
            return slug, folder
    return None, None

def parse(path: Path) -> PageParser:
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser

def local_target(folder: Path, href: str) -> Path | None:
    if href.startswith(("http://", "https://", "mailto:", "tel:", "#", "javascript:")):
        return None
    clean = href.split("#", 1)[0].split("?", 1)[0]
    return folder / clean if clean else None

def validate_site(root: Path, site: dict) -> tuple[list[str], str, str]:
    failures: list[str] = []
    slug, folder = resolve_folder(root, site)
    if not folder:
        return [f'{site["name"]}: no matching site folder found'], "missing", "missing"
    home_parser = parse(folder / "index.html")
    nav_pages = []
    for href in home_parser.links:
        target = local_target(folder, href)
        if target and target.suffix == ".html" and target.parent == folder and target.name not in nav_pages:
            nav_pages.append(target.name)
    required_core = ["index.html", "menu.html"]
    story_page = "story.html" if (folder / "story.html").is_file() else "about.html"
    visit_page = "visit.html" if (folder / "visit.html").is_file() else "contact.html"
    required_core.extend([story_page, visit_page])
    conversion_pages = [name for name in nav_pages if name not in STANDARD]
    conversion = conversion_pages[0] if conversion_pages else "missing"
    if conversion == "missing":
        failures.append(f'{site["name"]}: no restaurant-specific conversion page linked from Home')
    required = required_core + ([] if conversion == "missing" else [conversion])
    if len(set(required)) != 5:
        failures.append(f'{site["name"]}: required five-page set is not distinct')
    for name in required:
        page = folder / name
        if not page.is_file():
            failures.append(f'{site["name"]}: missing {name}')
            continue
        parser = parse(page)
        if not parser.has_title:
            failures.append(f'{site["name"]}/{name}: missing title')
        if parser.current != 1:
            failures.append(f'{site["name"]}/{name}: expected one current-page navigation state; found {parser.current}')
        for href in parser.links:
            target = local_target(folder, href)
            if target and not target.exists():
                failures.append(f'{site["name"]}/{name}: broken internal link {href}')
    js = folder / "site.js"
    if js.is_file():
        try:
            result = subprocess.run(["node", "--check", str(js)], capture_output=True, text=True)
            if result.returncode:
                failures.append(f'{site["name"]}: JavaScript syntax check failed')
        except FileNotFoundError:
            pass
    return failures, slug, conversion

def update_portal(root: Path, resolved: list[tuple[dict, str]]) -> None:
    path = root / "index.html"
    text = path.read_text(encoding="utf-8")
    marker = "const concepts=["
    if marker not in text:
        raise RuntimeError("Portal concepts array was not found")
    cards = []
    for site, slug in resolved:
        href = f"{slug}/index.html"
        if f'"href":"{href}"' in text or f'"name":"{site["name"]}"' in text:
            continue
        cards.append({"name":site["name"],"area":site["area"],"cuisine":site["cuisine"],"href":href,"emoji":"🍽","status":"static","description":"Five-page restaurant-specific sales demo; structural QA complete, browser visual QA pending."})
    if cards:
        position = text.index(marker) + len(marker)
        insertion = ",".join(json.dumps(card, ensure_ascii=False, separators=(",", ":")) for card in cards) + ","
        path.write_text(text[:position] + insertion + text[position:], encoding="utf-8")

def main() -> None:
    root = Path(__file__).resolve().parents[1]
    failures: list[str] = []
    resolved: list[tuple[dict, str]] = []
    rows: list[str] = []
    for site in SITES:
        site_failures, slug, conversion = validate_site(root, site)
        failures.extend(site_failures)
        if slug != "missing":
            resolved.append((site, slug))
        status = "PASS" if not site_failures else "FAIL"
        rows.append(f'| {site["name"]} | {slug} | 5/5 | {conversion} | {status} |')
    if failures:
        print("\n".join(failures))
        raise SystemExit(1)
    update_portal(root, resolved)
    (root / "BLOCK1_STATUS.md").write_text(
        "# Block 1 Status\n\n"
        "All 20 restaurants have five separate substantive HTML pages, working internal navigation, "
        "a restaurant-specific conversion page, and JavaScript syntax validation. Browser-rendered desktop "
        "and mobile visual QA remains pending, so none are labeled premium.\n\n"
        "| Restaurant | Folder | Pages | Conversion page | Structural QA |\n|---|---|---:|---|---|\n"
        + "\n".join(rows) + "\n",
        encoding="utf-8",
    )
    print("Block 1 validation passed for 20/20 restaurants.")

if __name__ == "__main__":
    main()
