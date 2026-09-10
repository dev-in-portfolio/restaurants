with open("portal-overrides.js", "r", encoding="utf-8") as fh:
    content = fh.read()

target = '  { name: "The Sandwich Club", status: "premium", href: "the-sandwich-club/index.html" },'
replacement = '  { name: "The Sandwich Club", status: "premium", href: "the-sandwich-club/index.html" },\n  { name: "Crunch Bistro", status: "premium", href: "crunch-bistro/index.html" },'

if target in content and "Crunch Bistro" not in content:
    content = content.replace(target, replacement, 1)
    with open("portal-overrides.js", "w", encoding="utf-8") as fh:
        fh.write(content)
    print("Updated portal-overrides.js for Crunch Bistro successfully")
else:
    print("Target not found or already registered")
