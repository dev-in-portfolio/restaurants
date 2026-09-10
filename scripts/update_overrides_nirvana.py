with open("portal-overrides.js", "r", encoding="utf-8") as fh:
    content = fh.read()

target = '  { name: "Johnny Burrito", status: "premium", href: "johnny-burrito/index.html" },'
replacement = '  { name: "Johnny Burrito", status: "premium", href: "johnny-burrito/index.html" },\n  { name: "Nirvana II", status: "premium", href: "nirvana-ii/index.html" },'

if target in content and "Nirvana II" not in content:
    content = content.replace(target, replacement, 1)
    with open("portal-overrides.js", "w", encoding="utf-8") as fh:
        fh.write(content)
    print("Updated portal-overrides.js for Nirvana II successfully")
else:
    print("Target not found or already registered")
