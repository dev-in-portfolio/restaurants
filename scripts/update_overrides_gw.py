with open('portal-overrides.js', 'r', encoding='utf-8') as f:
    content = f.read()

target = '  { name: "Cheers Mate Bar & Lounge", status: "premium", href: "cheers-mate-bar-and-lounge/index.html" },'
addition = '  { name: "Cheers Mate Bar & Lounge", status: "premium", href: "cheers-mate-bar-and-lounge/index.html" },\n  { name: "Great Wok", status: "premium", href: "great-wok/index.html" },'

if target in content:
    content = content.replace(target, addition, 1)
    with open('portal-overrides.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully added Great Wok to portal-overrides.js")
else:
    print("Target string not found!")
