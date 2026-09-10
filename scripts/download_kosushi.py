import os
import urllib.request

out_dir = r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\k-o-sushi\images"
os.makedirs(out_dir, exist_ok=True)

images = {
    "hero.jpg": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=1200&q=80",
    "specialty-rolls.jpg": "https://images.unsplash.com/photo-1611143669185-af224c5e3252?w=800&q=80",
    "poke-bowl.jpg": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=800&q=80",
    "udon-bulgogi.jpg": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=800&q=80",
    "party-platter.jpg": "https://images.unsplash.com/photo-1617196034796-73dfa7b1fd56?w=800&q=80"
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
