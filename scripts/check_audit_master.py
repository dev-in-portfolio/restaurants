import json

with open("queue/audit-ab-master.json", "r", encoding="utf-8") as f:
    audit = json.load(f)

with open("portal-overrides.js", "r", encoding="utf-8") as f:
    po = f.read()

print(f"Total in audit-ab-master: {len(audit)}")
remaining_audit = []
for item in audit:
    name = item.get("name", "")
    slug = item.get("slug", "")
    if f'"{name}"' in po or (slug and f'"{slug}/' in po):
        continue
    remaining_audit.append(item)

print(f"Remaining in audit-ab-master: {len(remaining_audit)}")
for i, item in enumerate(remaining_audit[:10], 1):
    print(f"{i}. Grade: {item.get('grade')} | {item.get('name')} (slug: {item.get('slug')})")
