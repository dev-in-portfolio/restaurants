import json

with open(r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\queue\showcase-exclusions.json", "r", encoding="utf-8") as f:
    excl = json.load(f)

print("Keys:", list(excl.keys()))
if "meta" in excl:
    print("Meta:", json.dumps(excl["meta"], indent=2))
