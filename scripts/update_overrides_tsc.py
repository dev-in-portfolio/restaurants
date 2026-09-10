with open("portal-overrides.js", "r", encoding="utf-8") as fh:
    content = fh.read()

target = '  { name: "Nirvana II", status: "premium", href: "nirvana-ii/index.html" },'
replacement = '  { name: "Nirvana II", status: "premium", href: "nirvana-ii/index.html" },\n  { name: "The Sandwich Club", status: "premium", href: "the-sandwich-club/index.html" },'

if target in content and "The Sandwich Club" not in content:
    content = content.replace(target, replacement, 1)
    with open("portal-overrides.js", "w", encoding="utf-8") as fh:
        fh.write(content)
    print("Updated portal-overrides.js for The Sandwich Club successfully")
else:
    print("Target not found or already registered")
