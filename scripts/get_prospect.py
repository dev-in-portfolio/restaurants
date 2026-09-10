import json

with open("queue/charlotte-prospect-sweep-2026-08-28.json", "r", encoding="utf-8") as fh:
    data = json.load(fh)

records = data.get("records", [])
for r in records:
    if r.get("slug") == "johnny-burrito":
        print(json.dumps(r, indent=2))
        break
