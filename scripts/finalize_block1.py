#!/usr/bin/env python3
from __future__ import annotations

import subprocess
from html.parser import HTMLParser
from pathlib import Path

SITES = [
    ("Boudreaux’s Restaurant", "boudreauxs"),
    ("Eddie’s Place", "eddies-place"),
    ("Salud Cerveceria", "salud-cerveceria"),
    ("The Degenerate", "the-degenerate"),
    ("Growlers Pourhouse", "growlers-pourhouse"),
    ("The Goodyear House", "goodyear-house"),
    ("The Daily Tavern", "the-daily-tavern"),
    ("The Artisan’s Palate", "the-artisans-palate"),
    ("Intermezzo Pizzeria", "intermezzo-pizzeria"),
    ("Euro Grill & Café", "euro-grill-cafe"),
    ("Midtown Tavern", "midtown-tavern"),
    ("The Hobbyist", "the-hobbyist"),
    ("Enderly Coffee Co.", "enderly-coffee-co"),
    ("Giddy Goat Coffee Roasters", "giddy-goat-coffee-roasters"),
    ("Harper’s Cafe", "harpers-cafe"),
    ("Middle James Brewing", "middle-james-brewing"),
    ("Kit’s Trackside Crafts", "kits-trackside-crafts"),
    ("Pintville Craft Beer", "pintville-craft-beer"),
    ("Miro Spanish Grille", "miro-spanish-grille"),
    ("Zinicola", "zinicola"),
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

def parse(path: Path) -> PageParser:
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser

def local_target(folder: Path, href: str) -> Path | None:
    if href.startswith(("http://", "https://", "mailto:", "tel:", "#", "javascript:")):
        return None
    clean = href.split("#", 1)[0].split("?", 1)[0]
    return folder / clean if clean else None

def validate_site(root: Path, name: str, slug: str) -> list[str]:
    failures: list[str] = []
    folder = root / slug
    home = folder / "index.html"
    if not home.is_file():
        return [f"{name}: missing {slug}/index.html"]
    home_parser = parse(home)
    nav_pages: list[str] = []
    for href in home_parser.links:
        target = local_target(folder, href)
        if target and target.suffix == ".html" and target.parent == folder and target.name not in nav_pages:
            nav_pages.append(target.name)
    story = "story.html" if (folder / "story.html").is_file() else "about.html"
    visit = "visit.html" if (folder / "visit.html").is_file() else "contact.html"
    conversion = next((page for page in nav_pages if page not in STANDARD), None)
    if not conversion:
        failures.append(f"{name}: no restaurant-specific conversion page linked from Home")
        return failures
    required = ["index.html", "menu.html", story, conversion, visit]
    if len(set(required)) != 5:
        failures.append(f"{name}: five-page set is not distinct")
    for page_name in required:
        page = folder / page_name
        if not page.is_file():
            failures.append(f"{name}: missing {page_name}")
            continue
        parser = parse(page)
        if not parser.has_title:
            failures.append(f"{name}/{page_name}: missing title")
        if parser.current != 1:
            failures.append(f"{name}/{page_name}: expected one current-page navigation state; found {parser.current}")
        for href in parser.links:
            target = local_target(folder, href)
            if target and not target.exists():
                failures.append(f"{name}/{page_name}: broken internal link {href}")
    js = folder / "site.js"
    if js.is_file():
        try:
            result = subprocess.run(["node", "--check", str(js)], capture_output=True, text=True)
            if result.returncode:
                failures.append(f"{name}: JavaScript syntax check failed")
        except FileNotFoundError:
            pass
    return failures

def main() -> None:
    root = Path(__file__).resolve().parents[1]
    failures = [failure for name, slug in SITES for failure in validate_site(root, name, slug)]
    if failures:
        print("\n".join(failures))
        raise SystemExit(1)
    print("Block 1 validation passed for 20/20 restaurants.")

if __name__ == "__main__":
    main()
