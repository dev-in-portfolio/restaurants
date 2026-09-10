import json

with open("queue/charlotte-prospect-sweep-2026-08-28.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("First record keys:", list(data["records"][0].keys()))
print("Sample record:", json.dumps(data["records"][0], indent=2))
