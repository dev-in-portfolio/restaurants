with open("portal-overrides.js", "r", encoding="utf-8") as fh:
    content = fh.read()

target = '  { name: "Lottie\'s Cafe", status: "premium", href: "lottie-s-cafe/index.html" },'
replacement = '  { name: "Lottie\'s Cafe", status: "premium", href: "lottie-s-cafe/index.html" },\n  { name: "Halfpenny\'s Cafe", status: "premium", href: "halfpenny-s-cafe/index.html" },'

if target in content and "Halfpenny's Cafe" not in content:
    content = content.replace(target, replacement, 1)
    with open("portal-overrides.js", "w", encoding="utf-8") as fh:
        fh.write(content)
    print("Updated portal-overrides.js successfully")
else:
    print("Target not found or already updated")
