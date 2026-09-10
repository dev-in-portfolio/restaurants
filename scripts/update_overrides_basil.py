with open('portal-overrides.js', 'r', encoding='utf-8') as f:
    content = f.read()

target = '  { name: "French Quarter Restaurant", status: "premium", href: "french-quarter-restaurant/index.html" },'
addition = '  { name: "French Quarter Restaurant", status: "premium", href: "french-quarter-restaurant/index.html" },\n  { name: "Basil Thai Cuisine", status: "premium", href: "basil-thai-cuisine/index.html" },'

if target in content:
    content = content.replace(target, addition, 1)
    with open('portal-overrides.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully added Basil Thai Cuisine to portal-overrides.js")
else:
    print("Target string not found!")
