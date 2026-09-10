import json

with open("queue/charlotte-prospect-sweep-2026-08-28.json", "r", encoding="utf-8") as f:
    sweep = json.load(f)

with open("portal-overrides.js", "r", encoding="utf-8") as f:
    overrides = f.read()

a_grade = [x for x in sweep if x.get("tier") == "A" or x.get("grade") == "A"]
remaining_a = []
for x in sweep:
    grade = x.get("grade") or x.get("tier")
    if grade != "A":
        continue
    name = x.get("name")
    # check slug
    slug = x.get("slug")
    if (slug and slug in overrides) or (name and name in overrides):
        continue
    remaining_a.append(x)

print(f"Total Sweep Grade A: {len([x for x in sweep if (x.get('grade') or x.get('tier')) == 'A'])}")
print(f"Remaining Grade A: {len(remaining_a)}")
for i, x in enumerate(remaining_a, 1):
    print(f"{i}. {x.get('name')} | phone: {x.get('phone')} | addr: {x.get('address')} | cuisine: {x.get('cuisine')} | reason: {x.get('pitchReason') or x.get('notes')}")
