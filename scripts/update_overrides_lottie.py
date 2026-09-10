with open('portal-overrides.js', 'r', encoding='utf-8') as f:
    content = f.read()

target = '  { name: "Great Wok", status: "premium", href: "great-wok/index.html" },'
addition = '  { name: "Great Wok", status: "premium", href: "great-wok/index.html" },\n  { name: "Lottie\'s Cafe", status: "premium", href: "lottie-s-cafe/index.html" },'

if target in content:
    content = content.replace(target, addition, 1)
    with open('portal-overrides.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully added Lottie's Cafe to portal-overrides.js")
else:
    print("Target string not found!")
