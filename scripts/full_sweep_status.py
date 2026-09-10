import json

with open("queue/charlotte-prospect-sweep-2026-08-28.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open("portal-overrides.js", "r", encoding="utf-8") as f:
    po = f.read()

for r in data["records"]:
    pos = r.get("position")
    name = r.get("name")
    slug = r.get("slug")
    grade = r.get("grade")
    status = r.get("reconciliation", {}).get("status")
    in_po = (f'"{name}"' in po) or (slug and f'"{slug}/' in po)
    print(f"#{pos:02d} | Grade {grade:2s} | Status: {status:10s} | In Overrides: {str(in_po):5s} | {name} ({slug})")
