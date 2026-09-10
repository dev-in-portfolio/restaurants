with open("portal-overrides.js", "r", encoding="utf-8") as fh:
    content = fh.read()

target = '  { name: "Halfpenny\'s Cafe", status: "premium", href: "halfpenny-s-cafe/index.html" },'
replacement = '  { name: "Halfpenny\'s Cafe", status: "premium", href: "halfpenny-s-cafe/index.html" },\n  { name: "Johnny Burrito", status: "premium", href: "johnny-burrito/index.html" },'

if target in content and "Johnny Burrito" not in content:
    content = content.replace(target, replacement, 1)
    with open("portal-overrides.js", "w", encoding="utf-8") as fh:
        fh.write(content)
    print("Updated portal-overrides.js for Johnny Burrito successfully")
else:
    print("Target not found or already registered")
