import os, urllib.request

os.makedirs("hasaki-grill-and-sushi/images", exist_ok=True)

images = {
    "hero.jpg": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?auto=format&fit=crop&w=1400&q=80",
    "sizzling-hibachi-steak-chicken.jpg": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=1000&q=80",
    "chef-specialty-sushi-rolls.jpg": "https://images.unsplash.com/photo-1611143669185-af224c5e3252?auto=format&fit=crop&w=1000&q=80",
    "japanese-lunch-bento-box.jpg": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=1000&q=80",
    "grand-sushi-catering-platter.jpg": "https://images.unsplash.com/photo-1553621042-f6e147245754?auto=format&fit=crop&w=1000&q=80"
}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

for filename, url in images.items():
    dest = os.path.join("hasaki-grill-and-sushi", "images", filename)
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp, open(dest, "wb") as out:
        out.write(resp.read())
    print(f"Downloaded {filename} ({os.path.getsize(dest)} bytes)")
