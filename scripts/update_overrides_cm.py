with open('portal-overrides.js', 'r', encoding='utf-8') as f:
    content = f.read()

target = '  { name: "Basil Thai Cuisine", status: "premium", href: "basil-thai-cuisine/index.html" },'
addition = '  { name: "Basil Thai Cuisine", status: "premium", href: "basil-thai-cuisine/index.html" },\n  { name: "Cheers Mate Bar & Lounge", status: "premium", href: "cheers-mate-bar-and-lounge/index.html" },'

if target in content:
    content = content.replace(target, addition, 1)
    with open('portal-overrides.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully added Cheers Mate Bar & Lounge to portal-overrides.js")
else:
    print("Target string not found!")
