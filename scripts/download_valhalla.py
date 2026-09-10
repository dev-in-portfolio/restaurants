import os
import urllib.request

out_dir = r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\valhalla-pub-and-eatery\images"
os.makedirs(out_dir, exist_ok=True)

images = {
    "hero.jpg": "https://images.unsplash.com/photo-1514933651103-005eec06c04b?w=1200&q=80",
    "swedish-meatballs.jpg": "https://images.unsplash.com/photo-1529042410759-befb1204b468?w=800&q=80",
    "viking-burger.jpg": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=800&q=80",
    "brevard-patio-pretzel.jpg": "https://images.unsplash.com/photo-1541544741938-0af808871cc0?w=800&q=80",
    "fish-chips-wings.jpg": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=800&q=80"
}

headers = {"User-Agent": "Mozilla/5.0"}

for name, url in images.items():
    path = os.path.join(out_dir, name)
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp, open(path, "wb") as f:
            f.write(resp.read())
        print(f"Downloaded {name} ({os.path.getsize(path)} bytes)")
    except Exception as e:
        print(f"Error downloading {name}: {e}")
