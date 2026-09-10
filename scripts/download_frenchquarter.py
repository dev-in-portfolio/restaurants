import os
import urllib.request

os.makedirs("french-quarter-restaurant/images", exist_ok=True)

# 5 high-res relevant culinary images from Unsplash
images = {
    "hero.jpg": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=1200&q=80", # Vibrant atmospheric restaurant/pub
    "cajun-gumbo-creole.jpg": "https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=800&q=80", # Rich hearty soup/gumbo bowl
    "cajun-chicken-pasta.jpg": "https://images.unsplash.com/photo-1621996346565-e3d5d6281206?auto=format&fit=crop&w=800&q=80", # Creamy pasta dish
    "salt-pepper-wings.jpg": "https://images.unsplash.com/photo-1567620832903-9fc6debc209f?auto=format&fit=crop&w=800&q=80", # Crispy glazed/seasoned wings
    "monte-cristo-poboy.jpg": "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?auto=format&fit=crop&w=800&q=80", # Gourmet sandwich / po'boy with fries
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for fname, url in images.items():
    dest = os.path.join("french-quarter-restaurant/images", fname)
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp, open(dest, 'wb') as f:
            f.write(resp.read())
        size = os.path.getsize(dest)
        print(f"Downloaded {fname} ({size} bytes)")
    except Exception as e:
        print(f"Failed {fname}: {e}")

