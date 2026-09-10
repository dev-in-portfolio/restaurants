import os, urllib.request

os.makedirs("johnny-burrito/images", exist_ok=True)

images = {
    "hero.jpg": "https://images.unsplash.com/photo-1626700051175-6818013e1d4f?auto=format&fit=crop&w=1400&q=80",
    "massive-california-burrito.jpg": "https://images.unsplash.com/photo-1566740933430-b5e70b06d2d5?auto=format&fit=crop&w=1000&q=80",
    "scratch-homemade-tamales.jpg": "https://images.unsplash.com/photo-1625938144755-652e08e359b7?auto=format&fit=crop&w=1000&q=80",
    "salsa-bar-chips-queso.jpg": "https://images.unsplash.com/photo-1574894709920-11b28e7367e3?auto=format&fit=crop&w=1000&q=80",
    "concourse-counter-lunch.jpg": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=1000&q=80"
}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

for filename, url in images.items():
    dest = os.path.join("johnny-burrito", "images", filename)
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp, open(dest, "wb") as out:
        out.write(resp.read())
    print(f"Downloaded {filename} ({os.path.getsize(dest)} bytes)")
