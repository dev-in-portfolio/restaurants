import json

with open(r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\queue\showcase-exclusions.json", "r", encoding="utf-8") as f:
    excl = json.load(f)

print("Sweep keys/summary:", json.dumps(excl.get("sweep", {}).get("summary"), indent=2))
print("Remaining by bucket:", json.dumps(excl.get("remainingByBucket"), indent=2))
