import os
import urllib.request

os.makedirs("cheers-mate-bar-and-lounge/images", exist_ok=True)

images = {
    "hero.jpg": "https://images.unsplash.com/photo-1572116469696-31de0f17cc34?auto=format&fit=crop&w=1200&q=80",
    "gourmet-sliders.jpg": "https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=800&q=80",
    "crispy-wings.jpg": "https://images.unsplash.com/photo-1527477321055-436158a2b00d?auto=format&fit=crop&w=800&q=80",
    "weekend-brunch.jpg": "https://images.unsplash.com/photo-1533089860892-a7c6f0a88666?auto=format&fit=crop&w=800&q=80",
    "craft-cocktails.jpg": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?auto=format&fit=crop&w=800&q=80"
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for fname, url in images.items():
    dest = os.path.join("cheers-mate-bar-and-lounge/images", fname)
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp, open(dest, 'wb') as f:
            f.write(resp.read())
        size = os.path.getsize(dest)
        print(f"Downloaded {fname} ({size} bytes)")
    except Exception as e:
        print(f"Failed {fname}: {e}")
