import json

with open(r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\queue\showcase-exclusions.json", "r", encoding="utf-8") as f:
    excl = json.load(f)

with open(r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\queue\charlotte-prospect-sweep-2026-08-28.json", "r", encoding="utf-8") as f:
    sweep = json.load(f)

excluded_slugs = {item["slug"] for item in excl.get("sweepExcluded", [])}

active_sweep = []
for item in sweep.get("leads", []):
    slug = item.get("slug")
    if slug not in excluded_slugs:
        active_sweep.append(item)

print(f"Total active sweep leads: {len(active_sweep)}")
print("\nActive A+ sweep leads:")
for item in active_sweep:
    if item.get("grade") == "A+":
        print(f"  [{item.get('position')}] {item.get('name')} ({item.get('slug')})")

print("\nActive A sweep leads:")
for item in active_sweep:
    if item.get("grade") == "A":
        print(f"  [{item.get('position')}] {item.get('name')} ({item.get('slug')})")

print("\nActive B sweep leads:")
for item in active_sweep:
    if item.get("grade") == "B":
        print(f"  [{item.get('position')}] {item.get('name')} ({item.get('slug')})")
