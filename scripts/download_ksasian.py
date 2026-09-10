import os
import urllib.request

out_dir = r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\k-s-asian-xpress\images"
os.makedirs(out_dir, exist_ok=True)

images = {
    "hero.jpg": "https://images.unsplash.com/photo-1541696432-82c6da8ce7bf?w=1200&q=80",
    "hibachi-combo.jpg": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800&q=80",
    "thai-noodles.jpg": "https://images.unsplash.com/photo-1559847844-5315695dadae?w=800&q=80",
    "dumplings-wings.jpg": "https://images.unsplash.com/photo-1563245372-f21724e3856d?w=800&q=80",
    "general-tso-curry.jpg": "https://images.unsplash.com/photo-1525755662778-989d0524087e?w=800&q=80"
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
