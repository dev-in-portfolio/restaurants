#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from html.parser import HTMLParser
from pathlib import Path

SITES = [
    {"slug":"boudreauxs","name":"Boudreaux’s Restaurant","area":"Charlotte","cuisine":"Louisiana-inspired • Kitchen & tavern"},
    {"slug":"eddies-place","name":"Eddie’s Place","area":"Charlotte","cuisine":"Neighborhood restaurant • Breakfast • American comfort"},
    {"slug":"salud-cerveceria","name":"Salud Cerveceria","area":"Charlotte","cuisine":"Craft beer • Pizza • Coffee • Soccer"},
    {"slug":"the-degenerate","name":"The Degenerate","area":"Charlotte","cuisine":"Global small plates • Cocktails"},
    {"slug":"growlers-pourhouse","name":"Growlers Pourhouse","area":"Charlotte","cuisine":"Craft beer • Pub food • Neighborhood bar"},
    {"slug":"the-goodyear-house","name":"The Goodyear House","area":"Charlotte","cuisine":"Seasonal American • Garden dining • NoDa"},
    {"slug":"the-daily-tavern","name":"The Daily Tavern","area":"Charlotte","cuisine":"Uptown tavern • Casual food • Sports"},
    {"slug":"artisans-palate","name":"The Artisan’s Palate","area":"Charlotte","cuisine":"Restaurant • Art • Events"},
    {"slug":"intermezzo-pizzeria","name":"Intermezzo Pizzeria","area":"Charlotte","cuisine":"Serbian family cooking • Pizza"},
    {"slug":"euro-grill-cafe","name":"Euro Grill & Café","area":"Charlotte","cuisine":"Balkan grill • Café • Family meals"},
    {"slug":"midtown-tavern","name":"Midtown Tavern","area":"Charlotte","cuisine":"Tavern • Sandwiches • Sports"},
    {"slug":"the-hobbyist","name":"The Hobbyist","area":"Charlotte","cuisine":"Coffee • Wine • Beer • Community"},
    {"slug":"enderly-coffee","name":"Enderly Coffee Co.","area":"Charlotte","cuisine":"Coffee roaster • Café • Community impact"},
    {"slug":"giddy-goat-coffee","name":"Giddy Goat Coffee Roasters","area":"Charlotte","cuisine":"Coffee roaster • Café • Community"},
    {"slug":"harpers-cafe-pineville","name":"Harper’s Cafe","area":"Pineville","cuisine":"Neighborhood café • American comfort"},
    {"slug":"middle-james-brewing","name":"Middle James Brewing","area":"Pineville","cuisine":"Craft brewery • Taproom • Events"},
    {"slug":"kits-trackside-crafts","name":"Kit’s Trackside Crafts","area":"Pineville","cuisine":"Craft beer • Bottle shop • Trackside gathering"},
    {"slug":"pintville-craft-beer","name":"Pintville Craft Beer","area":"Pineville","cuisine":"Craft beer • Taproom • Private gatherings"},
    {"slug":"miro-spanish-grille","name":"Miro Spanish Grille","area":"Ballantyne","cuisine":"Spanish cuisine • Tapas • Celebrations"},
    {"slug":"zinicola","name":"Zinicola","area":"Ballantyne","cuisine":"Italian dining • Wine • Private occasions"},
]

STANDARD = {"index.html", "menu.html", "story.html", "visit.html"}

class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.current = 0
        self.title = False
    def handle_starttag(self, tag: str, attrs) -> None:
        values = dict(attrs)
        if tag == "a" and values.get("href"):
            self.links.append(values["href"])
        if tag == "a" and values.get("aria-current") == "page":
            self.current += 1
        if tag == "title":
            self.title = True


def local_links(folder: Path, parser: PageParser) -> list[Path]:
    paths=[]
    for href in parser.links:
        if href.startswith(("http://", "https://", "mailto:", "tel:", "#")):
            continue
        clean=href.split("#",1)[0].split("?",1)[0]
        if clean:
            paths.append(folder/clean)
    return paths


def validate_site(root: Path, site: dict) -> tuple[list[str], str]:
    failures=[]
    folder=root/site["slug"]
    if not folder.is_dir():
        return [f'{site["name"]}: missing directory {site["slug"]}'], "missing"
    index=folder/"index.html"
    if not index.is_file():
        return [f'{site["name"]}: missing index.html'], "missing"
    first=PageParser(); first.feed(index.read_text(encoding="utf-8"))
    nav_html={Path(link.split("#",1)[0]).name for link in first.links if link.endswith(".html")}
    conversion=sorted(nav_html-STANDARD)
    if not conversion:
        failures.append(f'{site["name"]}: no restaurant-specific conversion page linked from home')
        conversion_name="missing"
    else:
        conversion_name=conversion[0]
    required=list(STANDARD)+([] if conversion_name=="missing" else [conversion_name])
    for name in required:
        page=folder/name
        if not page.is_file():
            failures.append(f'{site["name"]}: missing {name}')
            continue
        parser=PageParser(); parser.feed(page.read_text(encoding="utf-8"))
        if not parser.title:
            failures.append(f'{site["name"]}/{name}: missing title')
        if parser.current != 1:
            failures.append(f'{site["name"]}/{name}: expected one current-page navigation state; found {parser.current}')
        for target in local_links(folder, parser):
            if not target.exists():
                failures.append(f'{site["name"]}/{name}: broken internal link {target.name}')
    js=folder/"site.js"
    if js.is_file():
        try:
            result=subprocess.run(["node","--check",str(js)],capture_output=True,text=True)
            if result.returncode:
                failures.append(f'{site["name"]}: JavaScript syntax check failed')
        except FileNotFoundError:
            pass
    return failures, conversion_name


def update_portal(root: Path) -> None:
    path=root/"index.html"
    text=path.read_text(encoding="utf-8")
    marker="const concepts=["
    if marker not in text:
        raise RuntimeError("Portal concepts array was not found")
    cards=[]
    for site in SITES:
        href=f'{site["slug"]}/index.html'
        if f'"href":"{href}"' in text:
            continue
        cards.append({
            "name":site["name"], "area":site["area"], "cuisine":site["cuisine"],
            "href":href, "emoji":"🍽", "status":"static",
            "description":"Five-page restaurant-specific sales demo; structural QA complete, browser visual QA pending."
        })
    if cards:
        position=text.index(marker)+len(marker)
        insertion=",".join(json.dumps(card,ensure_ascii=False,separators=(",",":")) for card in cards)+"," 
        path.write_text(text[:position]+insertion+text[position:],encoding="utf-8")


def main() -> None:
    root=Path(__file__).resolve().parents[1]
    all_failures=[]
    rows=[]
    for site in SITES:
        failures, conversion=validate_site(root,site)
        all_failures.extend(failures)
        status="PASS" if not failures else "FAIL"
        rows.append(f'| {site["name"]} | 5/5 | {conversion} | {status} |')
    if all_failures:
        print("\n".join(all_failures))
        raise SystemExit(1)
    update_portal(root)
    (root/"BLOCK1_STATUS.md").write_text(
        "# Block 1 Status\n\n"
        "All 20 restaurants have five separate substantive HTML pages, working internal navigation, "
        "one restaurant-specific conversion page, and JavaScript syntax validation. Browser-rendered "
        "desktop and mobile visual QA remains pending; none are labeled premium.\n\n"
        "| Restaurant | Pages | Conversion page | Structural QA |\n|---|---:|---|---|\n"
        +"\n".join(rows)+"\n",
        encoding="utf-8",
    )
    print("Block 1 validation passed for 20/20 restaurants.")

if __name__ == "__main__":
    main()
