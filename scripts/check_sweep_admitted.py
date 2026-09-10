import json

with open(r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\queue\showcase-exclusions.json", "r", encoding="utf-8") as f:
    excl = json.load(f)

print("excl['sweep'] keys:", list(excl.get("sweep", {}).keys()))
print("excludedCount:", excl.get("sweep", {}).get("excludedCount"))
print("admittedCount:", excl.get("sweep", {}).get("admittedCount"))
print("admittedByGrade:", excl.get("sweep", {}).get("admittedByGrade"))

admitted = excl.get("sweep", {}).get("admitted", [])
print(f"Total admitted in sweep: {len(admitted)}")
print("\nAdmitted A+ items:")
for item in admitted:
    if item.get("grade") == "A+":
        print(f"  [{item.get('position')}] {item.get('restaurant')} ({item.get('slug')})")

print("\nAdmitted A items:")
for item in admitted:
    if item.get("grade") == "A":
        print(f"  [{item.get('position')}] {item.get('restaurant')} ({item.get('slug')})")

