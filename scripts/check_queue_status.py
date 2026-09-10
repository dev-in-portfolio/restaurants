import json, os

with open("queue/charlotte-prospect-sweep-2026-08-28.json", "r", encoding="utf-8") as fh:
    data = json.load(fh)

records = data.get("records", [])

# check existing directories
existing = set(d for d in os.listdir(".") if os.path.isdir(d) and os.path.exists(os.path.join(d, "index.html")))

print("=== SWEEP ADMITTED LEADS STATUS ===")
for i, r in enumerate(records, 1):
    slug = r.get("slug")
    name = r.get("name")
    grade = r.get("grade")
    built = slug in existing
    status_str = "BUILT" if built else "PENDING"
    print(f"{i:2d}. [{status_str}] {name} ({slug}) - Grade {grade}")
