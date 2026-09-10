import os, urllib.request

os.makedirs("the-sandwich-club/images", exist_ok=True)

images = {
    "hero.jpg": "https://images.unsplash.com/photo-1509722747041-616f39b57569?auto=format&fit=crop&w=1400&q=80",
    "triple-decker-club-sandwich.jpg": "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?auto=format&fit=crop&w=1000&q=80",
    "grand-brie-croissant-melt.jpg": "https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=1000&q=80",
    "breakfast-biscuit-egg-bacon.jpg": "https://images.unsplash.com/photo-1525351484163-7529414344d8?auto=format&fit=crop&w=1000&q=80",
    "corporate-boxed-lunch-spread.jpg": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=1000&q=80"
}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

for filename, url in images.items():
    dest = os.path.join("the-sandwich-club", "images", filename)
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp, open(dest, "wb") as out:
        out.write(resp.read())
    print(f"Downloaded {filename} ({os.path.getsize(dest)} bytes)")
