import json
with open("queue/audit-ab-master.json", "r", encoding="utf-8") as f:
    d = json.load(f)
print(type(d), list(d.keys()) if isinstance(d, dict) else len(d))
