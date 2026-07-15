#!/usr/bin/env python3
"""Run the validated six-page generator against an explicit reviewed target list."""

from __future__ import annotations

import subprocess
import sys
import types
from pathlib import Path

BASE_COMMIT = "6f98f3c62cf8bacd18391f0faf846d768147c87d"
BASE_PATH = "scripts/continue_six_page_upgrades.py"

TARGETS = {'ace-no-3': ('ACE No. 3', 'grill'),
 'aj-family-restaurant': ('AJ Family Restaurant', 'comfort'),
 'alexander-michaels': ("Alexander Michael's", 'beer'),
 'alice-jules-coffee-house': ('Alice Jules Coffee House', 'cafe'),
 'amelies-french-bakery-and-cafe': ("Amélie's French Bakery & Café", 'dessert'),
 'amina': ('Amina', 'signature'),
 'anatolia-cafe-and-cuisine': ('Anatolia Cafe & Cuisine', 'asian'),
 'fenians-keep': ("Fenian's Keep", 'beer'),
 'fiamma-ristorante': ('Fiamma Ristorante', 'italian'),
 'fin-and-fino': ('Fin & Fino', 'seafood'),
 'flame-asian-bistro-and-bar': ('Flame Asian Bistro & Bar', 'asian'),
 'flour-shop': ('Flour Shop', 'italian'),
 'flower-child': ('Flower Child', 'signature'),
 'food-soul': ('Food For Your Soul CLT', 'comfort'),
 'free-range-brewing': ('Free Range Brewing', 'beer'),
 'futo-buta': ('Futo Buta', 'asian'),
 'haberdish': ('Haberdish', 'comfort'),
 'harpers-cafe': ("Harper's Cafe", 'comfort'),
 'hathaways-fried-chicken': ("Hathaway's Fried Chicken", 'comfort'),
 'hawthornes-ny-pizza-and-bar': ("Hawthorne's NY Pizza & Bar", 'pizza'),
 'heist-brewery': ('Heist Brewery', 'beer'),
 'hello-sailor': ('Hello, Sailor', 'seafood'),
 'hex-coffee': ('HEX Coffee', 'cafe'),
 'hopfly-brewing': ('HopFly Brewing Company', 'beer'),
 'house-of-leng': ('House of Leng', 'asian'),
 'humbug': ('Humbug', 'beer'),
 'idlewild': ('Idlewild', 'beer'),
 'ink-n-ivy': ('Ink N Ivy', 'beer'),
 'intermezzo-pizzeria': ('Intermezzo Pizzeria', 'pizza'),
 'kabab-je': ('Kabab-Je', 'asian'),
 'kid-cashew': ('Kid Cashew', 'asian'),
 'kindred': ('Kindred', 'signature'),
 'kits-trackside-crafts': ("Kit's Trackside Crafts", 'beer'),
 'la-belle-helene': ('La Belle Hélène', 'signature'),
 'la-shish-kabob': ('La Shish Kabob', 'asian'),
 'lang-van': ('Lang Van', 'asian'),
 'laurel-market': ('Laurel Market', 'signature'),
 'le-kebab-grill': ('Le Kebab Grill', 'asian'),
 'legion-brewing': ('Legion Brewing', 'beer'),
 'leluia-hall': ('Leluia Hall', 'latin'),
 'lenny-boy-brewing': ('Lenny Boy Brewing Co.', 'beer'),
 'les-sandwiches-cafe': ("Le's Sandwiches & Café", 'asian'),
 'link-and-pin': ('Link & Pin', 'grill'),
 'little-mamas-italian': ("Little Mama's Italian", 'italian'),
 'local-loaf': ('Local Loaf', 'signature'),
 'lostrica': ("L'Ostrica", 'seafood'),
 'loyalist-market': ('The Loyalist Market', 'beer'),
 'luisas-brick-oven-pizzeria': ("Luisa's Brick Oven Pizzeria", 'pizza'),
 'lula-banh-mi-and-bakery': ('Lula Bánh Mì + Bakery', 'asian'),
 'lupies-cafe': ("Lupie's Cafe", 'comfort'),
 'machu-picchu': ('Machu Picchu Peruvian Cuisine', 'latin'),
 'manolos-latin-bakery': ("Manolo's Latin Bakery", 'dessert'),
 'marias-mexican-restaurant': ("Maria's Mexican Restaurant", 'latin'),
 'matthews-social-house': ('Matthews Social House', 'beer'),
 'mckoys-smokehouse-and-saloon': ("McKoy's Smokehouse & Saloon", 'grill'),
 'menya-daruma': ('Menya Daruma', 'asian'),
 'miguels-restaurant': ("Miguel's Restaurant", 'latin'),
 'mj-donuts': ('MJ Donuts', 'dessert'),
 'open-kitchen': ('Open Kitchen', 'italian'),
 'pacos-tacos-tequila': ("Paco's Tacos & Tequila", 'latin'),
 'palace-monroe': ('The Palace Restaurant', 'comfort'),
 'picadelis-pub-in-deli': ("Picadeli's Pub-In-Deli", 'beer'),
 'portofinos': ("Portofino's", 'italian'),
 'portrait-gallery': ('The Portrait Gallery', 'beer'),
 'queens-soul': ("Queen's Soul Food", 'comfort'),
 'republica': ('República Restaurant & Lounge', 'latin'),
 'royal-cafe': ('Royal Cafe & Creperie', 'dessert'),
 'sante': ('Santé', 'signature'),
 'seaboard-brewing': ('Seaboard Brewing', 'beer'),
 'tacos-el-nevado': ('Tacos El Nevado', 'latin'),
 'thai-taste': ('Thai Taste Matthews', 'asian'),
 'the-dive-n': ('The Dive N', 'comfort'),
 'the-goodyear-house': ('The Goodyear House', 'signature'),
 'umami-sushi-grill': ('Umami Sushi & Grill', 'seafood'),
 'waldhorn-restaurant': ('Waldhorn Restaurant', 'beer')}

KIND_HINTS = {
    "cafe": "coffee",
    "pizza": "pizza",
    "latin": "mexican",
    "beer": "brewery",
    "grill": "steak",
    "seafood": "sushi",
    "dessert": "donut",
    "comfort": "diner",
    "italian": "pasta",
    "asian": "thai",
    "signature": "signature",
}


def load_base_source() -> str:
    result = subprocess.run(
        ["git", "show", f"{BASE_COMMIT}:{BASE_PATH}"],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return result.stdout


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    source = load_base_source()
    module_name = "validated_base_generator"
    module = types.ModuleType(module_name)
    module.__file__ = str(root / BASE_PATH)
    sys.modules[module_name] = module
    exec(compile(source, BASE_PATH, "exec"), module.__dict__)
    namespace = module.__dict__

    base_choose = namespace["choose_experience"]
    name_to_kind = {name: kind for name, kind in TARGETS.values()}

    def explicit_folders(overrides: set[str]) -> list[Path]:
        folders: list[Path] = []
        problems: list[str] = []
        for slug in sorted(TARGETS):
            folder = root / slug
            if slug in overrides:
                problems.append(f"{slug} already has a portal override")
                continue
            if not folder.is_dir():
                problems.append(f"{slug} folder is missing")
                continue
            count = len(list(folder.glob("*.html")))
            if count != 5:
                problems.append(f"{slug} has {count} HTML pages instead of 5")
                continue
            folders.append(folder)
        if problems:
            raise RuntimeError("Explicit-target preflight failed:\n" + "\n".join(problems))
        return folders

    def explicit_name(index_text: str, slug: str) -> str:
        del index_text
        return TARGETS[slug][0]

    def explicit_experience(name: str, text: str):
        del text
        kind = name_to_kind[name]
        return base_choose("", KIND_HINTS[kind])

    namespace["ROOT"] = root
    namespace["WORKFLOW"] = root / ".github/workflows/continue-six-page-upgrades-v2.yml"
    namespace["SELF"] = root / "scripts/continue_six_page_upgrades_v2.py"
    namespace["REPORT"] = root / "docs/SIX_PAGE_UPGRADE_REPORT.md"
    namespace["eligible_folders"] = explicit_folders
    namespace["display_name"] = explicit_name
    namespace["choose_experience"] = explicit_experience

    namespace["main"]()


if __name__ == "__main__":
    main()
