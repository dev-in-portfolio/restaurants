import os
import urllib.request

os.makedirs("landmark-restaurant-diner/images", exist_ok=True)

images = {
    "landmark-hero-diner.jpg": "https://images.unsplash.com/photo-1528605248644-14dd04022da1?auto=format&fit=crop&w=1600&q=80",
    "landmark-greek-gyro.jpg": "https://images.unsplash.com/photo-1529042410759-befb1204b468?auto=format&fit=crop&w=1200&q=80",
    "landmark-bakery-cake.jpg": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=1200&q=80",
    "landmark-comfort-food.jpg": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=1200&q=80",
    "landmark-diner-interior.jpg": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=1200&q=80"
}

headers = {'User-Agent': 'Mozilla/5.0'}
for filename, url in images.items():
    filepath = os.path.join("landmark-restaurant-diner/images", filename)
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp, open(filepath, 'wb') as f:
        f.write(resp.read())
    print(f"Downloaded {filename}: {os.path.getsize(filepath)} bytes")
