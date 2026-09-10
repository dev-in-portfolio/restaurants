import json

with open("queue/charlotte-prospect-sweep-2026-08-28.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Type of data:", type(data))
if isinstance(data, dict):
    print("Keys:", list(data.keys()))
    if "prospects" in data:
        print("Prospects count:", len(data["prospects"]))
        print("Sample:", data["prospects"][0])
elif isinstance(data, list):
    print("Length:", len(data))
    print("Sample:", data[0])
