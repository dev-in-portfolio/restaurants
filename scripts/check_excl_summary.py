import json

with open(r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\queue\showcase-exclusions.json", "r", encoding="utf-8") as f:
    excl = json.load(f)

print("Summary:", json.dumps(excl.get("summary"), indent=2))
print("Audit master net active:", excl.get("summary", {}).get("auditNetActive"))
