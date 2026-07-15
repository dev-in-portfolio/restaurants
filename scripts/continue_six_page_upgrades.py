#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import html
import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
OVERRIDES = ROOT / "portal-overrides.js"
WORKFLOW = ROOT / ".github/workflows/continue-six-page-upgrades.yml"
SELF = ROOT / "scripts/continue_six_page_upgrades.py"
REPORT = ROOT / "docs/SIX_PAGE_UPGRADE_REPORT.md"

EXCLUDED = {
    ".git", ".github", ".migration", "_build-reports", "docs", "scripts",
    "node_modules", "vendor", "assets", "images", "img", "css", "js"
}

@dataclass(frozen=True)
class Experience:
    filename: str
    nav_label: str
    title: str
    eyebrow: str
    intro: str
    selectors: tuple[tuple[str, tuple[str, ...]], ...]
    emoji: str

def run(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(args),
        cwd=ROOT,
        check=check,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

def git(*args: str, check: bool = True) -> str:
    return run("git", *args, check=check).stdout.strip()

def normalize_spaces(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(value)).strip()

def strip_tags(value: str) -> str:
    return normalize_spaces(re.sub(r"<[^>]+>", " ", value))

def display_name(index_text: str, slug: str) -> str:
    patterns = [
        r'class=["\'][^"\']*nav-logo[^"\']*["\'][^>]*>(.*?)</a>',
        r'<h1[^>]*>(.*?)</h1>',
        r'<title[^>]*>(.*?)</title>',
    ]
    for pattern in patterns:
        match = re.search(pattern, index_text, re.I | re.S)
        if not match:
            continue
        candidate = strip_tags(match.group(1))
        candidate = re.split(r"\s+[·|—–-]\s+| \| ", candidate)[0].strip()
        if candidate and len(candidate) <= 80:
            return candidate
    return slug.replace("-", " ").title()

def existing_override_slugs(text: str) -> set[str]:
    return set(re.findall(r'href:\s*"([^"]+)/index\.html"', text))

def combined_text(files: Iterable[Path]) -> str:
    chunks = []
    for path in files:
        try:
            chunks.append(path.read_text(encoding="utf-8", errors="ignore"))
        except OSError:
            pass
    return " ".join(chunks).lower()

def choose_experience(name: str, text: str) -> Experience:
    haystack = f"{name} {text}".lower()
    candidates: list[tuple[tuple[str, ...], Experience]] = [
        (("coffee", "espresso", "matcha", "roaster", "café", "cafe"), Experience(
            "drink-lab.html", "Drink Lab", "Build Your Cafe Ritual", "A SIXTH-PAGE INTERACTIVE",
            "Shape a demonstration drink route around the mood, format, and flavor profile that sound right today.",
            (("Format", ("Espresso-led", "Cold & refreshing", "Slow-sipped")),
             ("Texture", ("Classic", "Creamy", "Bright")),
             ("Finish", ("Comforting", "Balanced", "Adventurous"))), "☕")),
        (("pizza", "pizzeria"), Experience(
            "pizza-studio.html", "Pizza Studio", "Compose a House Pie", "FROM CRUST TO FINISH",
            "Use the studio to sketch a demonstration pie direction before browsing the restaurant’s current menu.",
            (("Base", ("Red sauce", "White sauce", "Olive oil")),
             ("Center", ("Classic", "Vegetable-forward", "Hearty")),
             ("Finish", ("Herbs", "Heat", "Extra crunch"))), "🍕")),
        (("taco", "mexican", "latin", "cuban", "peruvian", "dominican"), Experience(
            "flavor-table.html", "Flavor Table", "Plan a Flavor Table", "A SHAREABLE SIXTH PAGE",
            "Build a demonstration table around brightness, richness, and heat without pretending to place an order.",
            (("Starting point", ("Street-style", "Family table", "Celebration")),
             ("Energy", ("Bright", "Deep & savory", "Spicy")),
             ("Share style", ("Individual plates", "Pass-around", "Mixed tasting"))), "🌮")),
        (("brewery", "beer", "pub", "tavern", "taproom", "bar", "wine"), Experience(
            "flight-planner.html", "Flight Planner", "Design a Tasting Flight", "POUR-BY-POUR PLANNING",
            "Map a demonstration tasting progression from familiar to adventurous, then use the live menu for actual availability.",
            (("Opening pour", ("Crisp", "Mellow", "Fruit-forward")),
             ("Middle pour", ("Roasty", "Hoppy", "Spiced")),
             ("Final pour", ("Bold", "Rare", "Dessert-like"))), "🍺")),
        (("steak", "steakhouse", "grill", "barbecue", "bbq"), Experience(
            "grill-guide.html", "Grill Guide", "Build a Grill Route", "FIRE, TEXTURE, BALANCE",
            "Create a demonstration grill route that balances the centerpiece, sides, and finishing character.",
            (("Centerpiece", ("Classic cut", "Seafood", "Vegetable-led")),
             ("Side direction", ("Comforting", "Fresh", "Shareable")),
             ("Finish", ("Peppery", "Smoky", "Bright"))), "🔥")),
        (("sushi", "japanese", "seafood", "oyster", "fish"), Experience(
            "chef-selection.html", "Chef Selection", "Shape a Chef Selection", "RAW, COOKED, OR MIXED",
            "Use this demonstration guide to describe the kind of progression you enjoy before checking the current menu.",
            (("Approach", ("Raw-forward", "Cooked-forward", "Balanced")),
             ("Pace", ("Light", "Progressive", "Celebratory")),
             ("Finish", ("Clean", "Rich", "Surprising"))), "🍣")),
        (("bakery", "donut", "ice cream", "dessert", "sweet", "creamery"), Experience(
            "box-builder.html", "Box Builder", "Build a Sharing Box", "A SWEET SIXTH PAGE",
            "Sketch a demonstration assortment for a morning run, office share, or celebration.",
            (("Occasion", ("Just because", "Office share", "Celebration")),
             ("Mix", ("Classic", "Seasonal", "Adventurous")),
             ("Size", ("Small taste", "Mixed box", "Crowd table"))), "🍩")),
        (("breakfast", "diner", "family", "soul", "southern", "comfort"), Experience(
            "comfort-plate.html", "Comfort Plate", "Build a Comfort Plate", "FAMILIAR FAVORITES, YOUR WAY",
            "Choose a demonstration plate direction that connects the restaurant’s comfort-food identity with the meal you are planning.",
            (("Meal", ("Breakfast", "Lunch", "Dinner")),
             ("Plate mood", ("Classic", "Lighter", "Extra comforting")),
             ("Table style", ("Quick stop", "Family meal", "Weekend gathering"))), "🍳")),
        (("italian", "pasta", "osteria", "trattoria"), Experience(
            "pasta-pairing.html", "Pasta Pairing", "Plan a Pasta Pairing", "SAUCE, SHAPE, FINISH",
            "Build a demonstration pasta route around texture and mood, then confirm the restaurant’s current offerings.",
            (("Sauce direction", ("Tomato", "Creamy", "Olive oil")),
             ("Texture", ("Silky", "Rustic", "Baked")),
             ("Finish", ("Herbal", "Cheesy", "Peppery"))), "🍝")),
        (("thai", "indian", "vietnamese", "ethiopian", "korean", "asian", "mediterranean", "greek"), Experience(
            "flavor-guide.html", "Flavor Guide", "Navigate the Flavor Map", "A SIXTH-PAGE TASTE GUIDE",
            "Describe the balance you want—comfort, brightness, depth, or heat—before exploring the current menu.",
            (("Foundation", ("Rice", "Noodles", "Shared plates")),
             ("Intensity", ("Gentle", "Layered", "Bold")),
             ("Balance", ("Fresh", "Savory", "Warming"))), "🥢")),
    ]
    for keywords, experience in candidates:
        if any(keyword in haystack for keyword in keywords):
            return experience
    return Experience(
        "signature-experience.html", "Signature Experience", "Build a Signature Visit",
        "A RESTAURANT-SPECIFIC SIXTH PAGE",
        "Use this demonstration planner to shape the pace, purpose, and flavor direction of a future visit.",
        (("Occasion", ("Everyday meal", "Date night", "Group gathering")),
         ("Pace", ("Quick", "Relaxed", "Celebratory")),
         ("Direction", ("Familiar", "Seasonal", "Surprising"))), "🍽️")

def unique_filename(folder: Path, preferred: str) -> str:
    if not (folder / preferred).exists():
        return preferred
    stem = Path(preferred).stem
    for index in range(2, 20):
        candidate = f"{stem}-{index}.html"
        if not (folder / candidate).exists():
            return candidate
    raise RuntimeError(f"Unable to choose a unique sixth-page filename for {folder.name}")

def palette(slug: str) -> tuple[str, str, str]:
    digest = hashlib.sha256(slug.encode("utf-8")).hexdigest()
    hue = int(digest[:4], 16) % 360
    accent_hue = (hue + 38 + int(digest[4:6], 16) % 70) % 360
    return (
        f"hsl({hue} 45% 10%)",
        f"hsl({accent_hue} 68% 52%)",
        f"hsl({(hue + 190) % 360} 38% 86%)",
    )

def page_label(path: Path) -> str:
    if path.name == "index.html":
        return "Home"
    label = path.stem.replace("-", " ").replace("_", " ").title()
    aliases = {"Contact": "Find Us", "Visit": "Visit", "Story": "Our Story", "About": "About"}
    return aliases.get(label, label)

def build_page(name: str, slug: str, folder: Path, experience: Experience, filename: str) -> str:
    dark, accent, light = palette(slug)
    existing = sorted(folder.glob("*.html"), key=lambda p: (p.name != "index.html", p.name))
    links = "\n".join(
        f'        <a href="{html.escape(path.name)}">{html.escape(page_label(path))}</a>'
        for path in existing[:5]
    )
    selectors = []
    for idx, (label, options) in enumerate(experience.selectors, start=1):
        option_html = "\n".join(f'              <option>{html.escape(option)}</option>' for option in options)
        selectors.append(f'''          <label>
            <span>{html.escape(label)}</span>
            <select id="choice-{idx}">
{option_html}
            </select>
          </label>''')
    selector_html = "\n".join(selectors)
    title = html.escape(name)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{title} interactive concept experience.">
  <title>{html.escape(experience.title)} | {title}</title>
  <link rel="stylesheet" href="../site-core.css">
  <style>
    :root{{--ink:{dark};--accent:{accent};--paper:{light};--muted:color-mix(in srgb,var(--paper) 62%,transparent)}}
    *{{box-sizing:border-box}}
    body{{margin:0;background:radial-gradient(circle at 85% 8%,color-mix(in srgb,var(--accent) 22%,transparent),transparent 34%),var(--ink);color:var(--paper);font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}
    a{{color:inherit}}
    .site-nav{{position:sticky;top:0;z-index:20;display:flex;justify-content:space-between;gap:1.5rem;align-items:center;padding:1rem clamp(1rem,4vw,3.5rem);background:color-mix(in srgb,var(--ink) 88%,transparent);backdrop-filter:blur(16px);border-bottom:1px solid color-mix(in srgb,var(--paper) 14%,transparent)}}
    .brand{{font-weight:900;letter-spacing:.02em;text-decoration:none}}
    .nav-links{{display:flex;flex-wrap:wrap;justify-content:flex-end;gap:.85rem}}
    .nav-links a{{font-size:.76rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;text-decoration:none;opacity:.72}}
    .nav-links a:hover,.nav-links a[aria-current="page"]{{opacity:1;color:var(--accent)}}
    main{{max-width:1120px;margin:0 auto;padding:clamp(3.5rem,8vw,7rem) clamp(1rem,4vw,3rem)}}
    .eyebrow{{color:var(--accent);font-size:.76rem;font-weight:900;letter-spacing:.2em;text-transform:uppercase}}
    h1{{max-width:820px;margin:.7rem 0 1rem;font-size:clamp(2.7rem,7vw,6.7rem);line-height:.92;letter-spacing:-.055em}}
    .lede{{max-width:720px;color:var(--muted);font-size:clamp(1rem,2vw,1.2rem);line-height:1.75}}
    .planner{{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(280px,.8fr);gap:1.25rem;margin-top:3rem}}
    .panel{{border:1px solid color-mix(in srgb,var(--paper) 16%,transparent);border-radius:1.5rem;background:color-mix(in srgb,var(--paper) 6%,transparent);box-shadow:0 26px 80px rgba(0,0,0,.25);padding:clamp(1.2rem,3vw,2rem)}}
    .controls{{display:grid;gap:1rem}}
    label span{{display:block;margin-bottom:.45rem;color:var(--muted);font-size:.74rem;font-weight:900;letter-spacing:.12em;text-transform:uppercase}}
    select{{width:100%;border:1px solid color-mix(in srgb,var(--paper) 18%,transparent);border-radius:.85rem;background:color-mix(in srgb,var(--ink) 72%,black);color:var(--paper);padding:.95rem 1rem;font:inherit}}
    button{{margin-top:.35rem;border:0;border-radius:999px;background:var(--accent);color:#080808;padding:.9rem 1.25rem;font-weight:900;cursor:pointer}}
    .result{{display:flex;min-height:100%;flex-direction:column;justify-content:space-between}}
    .result-icon{{font-size:3rem}}
    .result h2{{margin:.8rem 0 .4rem;font-size:clamp(1.7rem,3vw,2.7rem)}}
    #summary{{color:var(--muted);line-height:1.7}}
    .note{{margin-top:1.5rem;padding-top:1rem;border-top:1px solid color-mix(in srgb,var(--paper) 12%,transparent);color:color-mix(in srgb,var(--paper) 48%,transparent);font-size:.8rem;line-height:1.55}}
    @media(max-width:760px){{.site-nav{{align-items:flex-start;flex-direction:column}}.nav-links{{justify-content:flex-start}}.planner{{grid-template-columns:1fr}}}}
  </style>
</head>
<body>
  <nav class="site-nav" aria-label="Main navigation">
    <a class="brand" href="index.html">{title}</a>
    <div class="nav-links">
{links}
      <a href="{html.escape(filename)}" aria-current="page">{html.escape(experience.nav_label)}</a>
    </div>
  </nav>
  <main>
    <p class="eyebrow">{html.escape(experience.eyebrow)}</p>
    <h1>{html.escape(experience.title)}</h1>
    <p class="lede">{html.escape(experience.intro)}</p>
    <section class="planner" aria-label="{html.escape(experience.title)} interactive planner">
      <div class="panel controls">
{selector_html}
        <button type="button" id="build-plan">Build My Demonstration Plan</button>
      </div>
      <div class="panel result" aria-live="polite">
        <div>
          <div class="result-icon" aria-hidden="true">{experience.emoji}</div>
          <h2>Your {html.escape(experience.nav_label)}</h2>
          <p id="summary">Choose one option from each field, then build a demonstration plan.</p>
        </div>
        <p class="note">Concept demonstration only. This tool does not submit an order, reservation, or personal information. Confirm current menu items, pricing, hours, and availability directly with the restaurant.</p>
      </div>
    </section>
  </main>
  <script>
    (() => {{
      const button = document.getElementById('build-plan');
      const fields = [...document.querySelectorAll('select')];
      const summary = document.getElementById('summary');
      button.addEventListener('click', () => {{
        const values = fields.map(field => field.value);
        summary.textContent = `Start with ${{values[0]}}; keep the experience ${{values[1].toLowerCase()}}; finish with ${{values[2].toLowerCase()}}. Use this as a conversation starter, then confirm the restaurant's current offerings.`;
      }});
    }})();
  </script>
</body>
</html>
'''

def inject_nav_link(text: str, filename: str, label: str) -> str:
    if filename in text:
        return text
    link = f'<a href="{filename}">{html.escape(label)}</a>'
    nav_match = re.search(r"<nav\b[^>]*>.*?</nav>", text, re.I | re.S)
    if not nav_match:
        return text

    nav = nav_match.group(0)
    if re.search(r"<ul\b", nav, re.I) and re.search(r"</ul>", nav, re.I):
        nav_new = re.sub(r"</ul>", f'<li>{link}</li></ul>', nav, count=1, flags=re.I)
    elif re.search(r'class=["\'][^"\']*nav-links[^"\']*["\']', nav, re.I):
        nav_new = re.sub(r"</div>\s*</nav>", f"  {link}\n  </div>\n</nav>", nav, count=1, flags=re.I)
        if nav_new == nav:
            nav_new = nav.replace("</nav>", f"  {link}\n</nav>", 1)
    else:
        nav_new = nav.replace("</nav>", f"  {link}\n</nav>", 1)

    return text[:nav_match.start()] + nav_new + text[nav_match.end():]

def validate_folder(folder: Path, generated: Path) -> None:
    html_files = sorted(folder.glob("*.html"))
    if len(html_files) != 6:
        raise RuntimeError(f"{folder.name}: expected 6 HTML files after upgrade, found {len(html_files)}")
    generated_text = generated.read_text(encoding="utf-8")
    required = ("<!DOCTYPE html>", "name=\"viewport\"", "<select", "Concept demonstration only")
    for token in required:
        if token not in generated_text:
            raise RuntimeError(f"{folder.name}: generated page missing {token!r}")
    for page in html_files:
        text = page.read_text(encoding="utf-8", errors="ignore")
        for href in re.findall(r'href=["\']([^"\']+\.html)(?:#[^"\']*)?["\']', text, re.I):
            if re.match(r"^(?:https?:|mailto:|tel:|/)", href):
                continue
            target = (page.parent / href).resolve()
            if not target.exists():
                raise RuntimeError(f"{folder.name}: broken local link {page.name} -> {href}")

def append_override(text: str, name: str, slug: str, experience: Experience) -> str:
    entry = f'''  {{
    name: {json.dumps(name, ensure_ascii=False)},
    area: "Charlotte area",
    cuisine: "Six-Page Restaurant Experience",
    description: {json.dumps(f"Six-page concept upgraded with a custom {experience.nav_label.lower()} and interactive planner. Static validation passed; desktop/mobile browser QA remains pending.", ensure_ascii=False)},
    emoji: {json.dumps(experience.emoji, ensure_ascii=False)},
    href: "{slug}/index.html",
    gradient: "linear-gradient(135deg,#172033,#334155 52%,#0f172a)",
    status: "qa"
  }},
'''
    marker = "\n];"
    index = text.rfind(marker)
    if index < 0:
        raise RuntimeError("portal-overrides.js closing marker not found")
    before = text[:index].rstrip()
    if before.endswith("}"):
        before += ","
    return before + "\n" + entry.rstrip(",\n") + "\n];\n"

def eligible_folders(overrides: set[str]) -> list[Path]:
    result = []
    for folder in ROOT.iterdir():
        if not folder.is_dir() or folder.name in EXCLUDED or folder.name.startswith("."):
            continue
        if folder.name in overrides or not (folder / "index.html").exists():
            continue
        html_files = list(folder.glob("*.html"))
        if len(html_files) == 5:
            result.append(folder)
    return sorted(result, key=lambda p: p.name)

def ensure_clean_start() -> None:
    status = git("status", "--short")
    allowed = {
        ".github/workflows/continue-six-page-upgrades.yml",
        "scripts/continue_six_page_upgrades.py",
    }
    unexpected = []
    for line in status.splitlines():
        path = line[3:].strip()
        if path not in allowed:
            unexpected.append(line)
    if unexpected:
        raise RuntimeError("Unexpected starting changes:\n" + "\n".join(unexpected))

def commit_restaurant(folder: Path, name: str, experience: Experience) -> str:
    git("add", str(folder.relative_to(ROOT)), str(OVERRIDES.relative_to(ROOT)))
    staged = git("diff", "--cached", "--name-only").splitlines()
    allowed_prefix = folder.name + "/"
    for path in staged:
        if path != "portal-overrides.js" and not path.startswith(allowed_prefix):
            raise RuntimeError(f"{folder.name}: out-of-scope staged path {path}")
    message = (
        f"{folder.name}: upgrade to 6-page QA status with custom "
        f"{experience.nav_label.lower()} and interactive planner"
    )
    git("commit", "-m", message)
    return git("rev-parse", "HEAD")

def main() -> None:
    ensure_clean_start()
    git("config", "user.name", "restaurant-upgrade-bot")
    git("config", "user.email", "actions@users.noreply.github.com")

    override_text = OVERRIDES.read_text(encoding="utf-8")
    overrides = existing_override_slugs(override_text)
    queue = eligible_folders(overrides)
    processed: list[tuple[str, str, str, str]] = []
    failures: list[str] = []

    for folder in queue:
        try:
            existing_pages = sorted(folder.glob("*.html"))
            index_text = (folder / "index.html").read_text(encoding="utf-8", errors="ignore")
            name = display_name(index_text, folder.name)
            experience = choose_experience(name, combined_text(existing_pages))
            filename = unique_filename(folder, experience.filename)
            generated = folder / filename
            generated.write_text(
                build_page(name, folder.name, folder, experience, filename),
                encoding="utf-8",
            )

            for page in existing_pages:
                text = page.read_text(encoding="utf-8", errors="ignore")
                updated = inject_nav_link(text, filename, experience.nav_label)
                if updated != text:
                    page.write_text(updated, encoding="utf-8")

            validate_folder(folder, generated)
            override_text = append_override(override_text, name, folder.name, experience)
            OVERRIDES.write_text(override_text, encoding="utf-8")
            commit_sha = commit_restaurant(folder, name, experience)
            processed.append((folder.name, name, filename, commit_sha))
        except Exception as exc:
            failures.append(f"{folder.name}: {exc}")
            git("reset", "--hard", "HEAD")
            override_text = OVERRIDES.read_text(encoding="utf-8")
            continue

    report_lines = [
        "# Six-Page Restaurant Upgrade Report",
        "",
        "Generated by the controlled continuation workflow.",
        "",
        f"- Starting premium/QA overrides: {len(overrides)}",
        f"- Eligible five-page folders found: {len(queue)}",
        f"- Successfully upgraded: {len(processed)}",
        f"- Failed or skipped after validation: {len(failures)}",
        "",
        "## Successfully upgraded",
        "",
    ]
    if processed:
        report_lines.extend(
            f"- **{name}** (`{slug}`) — `{filename}` — `{sha[:12]}`"
            for slug, name, filename, sha in processed
        )
    else:
        report_lines.append("- None")
    report_lines.extend(["", "## Failures", ""])
    if failures:
        report_lines.extend(f"- {failure}" for failure in failures)
    else:
        report_lines.append("- None")
    report_lines.extend([
        "",
        "## Status policy",
        "",
        "Each generated site is marked `qa`, not `premium`. The workflow verifies six direct HTML pages, generated-page structure, scoped commits, and local HTML links. Human desktop/mobile browser review is still required before promotion to `premium`.",
        "",
    ])
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(report_lines), encoding="utf-8")

    git("rm", "-f", str(SELF.relative_to(ROOT)), str(WORKFLOW.relative_to(ROOT)))
    git("add", str(REPORT.relative_to(ROOT)))
    git("commit", "-m", "Document continued six-page restaurant upgrades and remove temporary automation")

    print(f"PROCESSED={len(processed)}")
    print(f"FAILED={len(failures)}")
    for failure in failures:
        print("FAILURE:", failure)

if __name__ == "__main__":
    main()
