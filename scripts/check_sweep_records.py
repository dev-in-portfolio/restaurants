import json

with open("queue/charlotte-prospect-sweep-2026-08-28.json", "r", encoding="utf-8") as f:
    data = json.load(f)

records = data["records"]

with open("portal-overrides.js", "r", encoding="utf-8") as f:
    overrides = f.read()

with open("queue/showcase-exclusions.json", "r", encoding="utf-8") as f:
    excl = json.load(f)

print(f"Total records in sweep: {len(records)}")

remaining = []
for r in records:
    name = r.get("name", "")
    grade = r.get("admitGrade", "")
    # Check if name is in overrides
    if f'"{name}"' in overrides:
        continue
    remaining.append(r)

print(f"Remaining in sweep: {len(remaining)}")
for i, r in enumerate(remaining, 1):
    print(f"{i}. [{r.get('admitGrade')}] {r.get('name')} | {r.get('address')} | {r.get('phone')} | {r.get('cuisineType')}")
