import os
import urllib.request

os.makedirs("lottie-s-cafe/images", exist_ok=True)

images = {
    "hero.jpg": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=1200&q=80",
    "breakfast-sandwich-bagel.jpg": "https://images.unsplash.com/photo-1525351484163-7529414344d8?auto=format&fit=crop&w=800&q=80",
    "artisan-espresso-latte.jpg": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?auto=format&fit=crop&w=800&q=80",
    "avocado-toast-bowl.jpg": "https://images.unsplash.com/photo-1525351484163-7529414344d8?auto=format&fit=crop&w=800&q=80",
    "fresh-pastries-croissants.jpg": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80"
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for fname, url in images.items():
    dest = os.path.join("lottie-s-cafe/images", fname)
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp, open(dest, 'wb') as f:
            f.write(resp.read())
        size = os.path.getsize(dest)
        print(f"Downloaded {fname} ({size} bytes)")
    except Exception as e:
        print(f"Failed {fname}: {e}")
