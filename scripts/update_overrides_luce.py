with open("portal-overrides.js", "r", encoding="utf-8") as fh:
    content = fh.read()

target = '  { name: "Crunch Bistro", status: "premium", href: "crunch-bistro/index.html" },'
replacement = '  { name: "Crunch Bistro", status: "premium", href: "crunch-bistro/index.html" },\n  { name: "Luce Ristorante", status: "premium", href: "luce-ristorante/index.html" },'

if target in content and "Luce Ristorante" not in content:
    content = content.replace(target, replacement, 1)
    with open("portal-overrides.js", "w", encoding="utf-8") as fh:
        fh.write(content)
    print("Updated portal-overrides.js for Luce Ristorante successfully")
else:
    print("Target not found or already registered")
