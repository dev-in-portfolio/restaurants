import json

with open("queue/charlotte-prospect-sweep-2026-08-28.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open("portal-overrides.js", "r", encoding="utf-8") as f:
    overrides = f.read()

records = data["records"]
remaining = []
for r in records:
    name = r.get("name", "")
    slug = r.get("slug", "")
    status = r.get("reconciliation", {}).get("status")
    if status != "admitted":
        continue
    # check if in overrides
    if f'"{name}"' in overrides or (slug and f'"{slug}/' in overrides):
        continue
    remaining.append(r)

print(f"Total admitted remaining: {len(remaining)}")
for i, r in enumerate(remaining, 1):
    print(f"{i}. Pos #{r.get('position')} | Grade: {r.get('grade')} | {r.get('name')} (slug: {r.get('slug')})")
