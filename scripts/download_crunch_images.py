import os, urllib.request

os.makedirs("crunch-bistro/images", exist_ok=True)

images = {
    "hero.jpg": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=1400&q=80",
    "signature-chopped-salad-bowl.jpg": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=1000&q=80",
    "warm-quinoa-grain-bowl.jpg": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=1000&q=80",
    "artisan-lavash-flatbread.jpg": "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=1000&q=80",
    "organic-acai-superfruit-bowl.jpg": "https://images.unsplash.com/photo-1590301157890-4810ed352733?auto=format&fit=crop&w=1000&q=80"
}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

for filename, url in images.items():
    dest = os.path.join("crunch-bistro", "images", filename)
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp, open(dest, "wb") as out:
        out.write(resp.read())
    print(f"Downloaded {filename} ({os.path.getsize(dest)} bytes)")
