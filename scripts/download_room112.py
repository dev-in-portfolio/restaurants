import os
import urllib.request

out_dir = r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\room-112\images"
os.makedirs(out_dir, exist_ok=True)

images = {
    "hero.jpg": "https://images.unsplash.com/photo-1553621042-f6e147245754?w=1200&q=80",
    "cherry-blossom-roll.jpg": "https://images.unsplash.com/photo-1611143669185-af224c5e3252?w=800&q=80",
    "walnut-prawns-wok.jpg": "https://images.unsplash.com/photo-1541696432-82c6da8ce7bf?w=800&q=80",
    "dim-sum-starters.jpg": "https://images.unsplash.com/photo-1563245372-f21724e3856d?w=800&q=80",
    "executive-sushi-sampler.jpg": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=800&q=80"
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
