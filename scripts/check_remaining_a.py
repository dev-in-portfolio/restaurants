import json

with open("queue/sweep-leads-admitted.json", "r", encoding="utf-8") as f:
    admitted = json.load(f)

with open("portal-overrides.js", "r", encoding="utf-8") as f:
    overrides = f.read()

a_grade = [x for x in admitted if x.get("grade") == "A"]
remaining_a = []
for x in a_grade:
    slug = x.get("slug")
    name = x.get("name")
    if (slug and slug in overrides) or (name and name in overrides):
        continue
    remaining_a.append(x)

print(f"Total Admitted Grade A: {len(a_grade)}")
print(f"Remaining Admitted Grade A: {len(remaining_a)}")
for i, x in enumerate(remaining_a[:15], 1):
    print(f"{i}. {x.get('name')} | slug: {x.get('slug')} | phone: {x.get('phone')} | addr: {x.get('address')} | cuisine: {x.get('cuisine')}")
