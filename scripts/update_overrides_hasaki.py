with open("portal-overrides.js", "r", encoding="utf-8") as fh:
    content = fh.read()

target = '  { name: "Luce Ristorante", status: "premium", href: "luce-ristorante/index.html" },'
replacement = '  { name: "Luce Ristorante", status: "premium", href: "luce-ristorante/index.html" },\n  { name: "Hasaki Grill & Sushi", status: "premium", href: "hasaki-grill-and-sushi/index.html" },'

if target in content and "Hasaki Grill & Sushi" not in content:
    content = content.replace(target, replacement, 1)
    with open("portal-overrides.js", "w", encoding="utf-8") as fh:
        fh.write(content)
    print("Updated portal-overrides.js for Hasaki Grill & Sushi successfully")
else:
    print("Target not found or already registered")
