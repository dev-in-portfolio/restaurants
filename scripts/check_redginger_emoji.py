import os, re

dir_path = r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\red-ginger"
emoji_pattern = re.compile(r"[\U00010000-\U0010ffff\u2600-\u26ff\u2700-\u27bf]", flags=re.UNICODE)

found = 0
for root, dirs, files in os.walk(dir_path):
    for f in files:
        if f.endswith((".html", ".css", ".js", ".md", ".json")):
            p = os.path.join(root, f)
            with open(p, "r", encoding="utf-8", errors="ignore") as fh:
                txt = fh.read()
                matches = emoji_pattern.findall(txt)
                if matches:
                    print(f"Emoji found in {f}: {matches}")
                    found += 1

if found == 0:
    print("Zero emojis verified in all files.")
