import os
import urllib.request

os.makedirs("pho-an-hoa/images", exist_ok=True)

images = {
    "pho-hero-bowl.jpg": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?auto=format&fit=crop&w=1600&q=80",
    "pho-fresh-rolls.jpg": "https://images.unsplash.com/photo-1541696432-82c6da8ce7bf?auto=format&fit=crop&w=1200&q=80",
    "pho-vermicelli-bowl.jpg": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=1200&q=80",
    "pho-iced-coffee-boba.jpg": "https://images.unsplash.com/photo-1551024709-8f23befc6f87?auto=format&fit=crop&w=1200&q=80",
    "pho-diner-interior.jpg": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=1200&q=80"
}

headers = {'User-Agent': 'Mozilla/5.0'}
for filename, url in images.items():
    filepath = os.path.join("pho-an-hoa/images", filename)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp, open(filepath, 'wb') as f:
            f.write(resp.read())
        print(f"Downloaded {filename}: {os.path.getsize(filepath)} bytes")
    except Exception as e:
        print(f"Error {filename}: {e}")
