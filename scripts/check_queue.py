import json

with open("queue/charlotte-prospect-sweep-2026-08-28.json", "r", encoding="utf-8") as fh:
    data = json.load(fh)

records = data.get("records", [])
print(f"Total records: {len(records)}")
for i, r in enumerate(records[:20], 1):
    print(f"{i}. {r.get('name')} | Slug: {r.get('slug')} | Decision: {r.get('decision')} | Grade: {r.get('grade')} | Priority: {r.get('priorityCategory')}")
