import json, re

with open(r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\queue\showcase-exclusions.json", "r", encoding="utf-8") as f:
    excl = json.load(f)

# The sweep exclusions are in excl['sweep']['exclusions']
sweep_excl_slugs = {item["slug"] for item in excl.get("sweep", {}).get("exclusions", [])}

with open(r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\queue\sweep-2026-08-28.js", "r", encoding="utf-8") as f:
    txt = f.read()

m = re.search(r"=\s*(\[[\s\S]*\])\s*;?", txt)
if m:
    sweep_queue = json.loads(m.group(1))

print(f"Total in sweep queue: {len(sweep_queue)}")
print(f"Sweep excluded count: {len(sweep_excl_slugs)}")

admitted = [row for row in sweep_queue if row[1] not in sweep_excl_slugs]
print(f"Admitted sweep items: {len(admitted)}")

print("\n--- ADMITTED SWEEP A+ ITEMS ---")
for row in admitted:
    if row[2] == "A+":
        print(f"[{row[3]}] {row[0]} ({row[1]})")

print("\n--- ADMITTED SWEEP A ITEMS ---")
for row in admitted:
    if row[2] == "A":
        print(f"[{row[3]}] {row[0]} ({row[1]})")

print("\n--- ADMITTED SWEEP B ITEMS ---")
for row in admitted:
    if row[2] == "B":
        print(f"[{row[3]}] {row[0]} ({row[1]})")
