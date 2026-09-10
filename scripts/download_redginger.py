import os
import urllib.request

out_dir = r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\red-ginger\images"
os.makedirs(out_dir, exist_ok=True)

images = {
    "hero.jpg": "https://images.unsplash.com/photo-1544025162-d76694265947?w=1200&q=80",
    "teppanyaki-steak-lobster.jpg": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=800&q=80",
    "specialty-sushi-lounge.jpg": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=800&q=80",
    "yellowtail-tartar.jpg": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?w=800&q=80",
    "private-dining-lounge.jpg": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&q=80"
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
