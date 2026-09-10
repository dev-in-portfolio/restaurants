with open('portal-overrides.js', 'r', encoding='utf-8') as f:
    content = f.read()

target = '  { name: "Valhalla Pub & Eatery", status: "premium", href: "valhalla-pub-and-eatery/index.html" },'
addition = '  { name: "Valhalla Pub & Eatery", status: "premium", href: "valhalla-pub-and-eatery/index.html" },\n  { name: "French Quarter Restaurant", status: "premium", href: "french-quarter-restaurant/index.html" },'

if target in content:
    content = content.replace(target, addition, 1)
    with open('portal-overrides.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully added French Quarter Restaurant to portal-overrides.js")
else:
    print("Target string not found!")
