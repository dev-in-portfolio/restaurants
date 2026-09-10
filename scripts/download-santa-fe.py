import os
import urllib.request

os.makedirs("santa-fe-mexican-restaurant-central-ave/images", exist_ok=True)

images = {
    "santa-fe-hero-fajitas.jpg": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=1600&q=80",
    "santa-fe-street-tacos.jpg": "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?auto=format&fit=crop&w=1200&q=80",
    "santa-fe-molcajete.jpg": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=1200&q=80",
    "santa-fe-margarita-cantina.jpg": "https://images.unsplash.com/photo-1551024709-8f23befc6f87?auto=format&fit=crop&w=1200&q=80",
    "santa-fe-cantina-interior.jpg": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=1200&q=80"
}

headers = {'User-Agent': 'Mozilla/5.0'}
for filename, url in images.items():
    filepath = os.path.join("santa-fe-mexican-restaurant-central-ave/images", filename)
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp, open(filepath, 'wb') as f:
        f.write(resp.read())
    print(f"Downloaded {filename}: {os.path.getsize(filepath)} bytes")
