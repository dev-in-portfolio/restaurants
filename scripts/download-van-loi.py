import os
import urllib.request

os.makedirs("van-loi-chinese-barbecue/images", exist_ok=True)

images = {
    "van-loi-hero-duck.jpg": "https://images.unsplash.com/photo-1518492104633-130d0cc84637?auto=format&fit=crop&w=1600&q=80",
    "van-loi-crispy-pork.jpg": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=1200&q=80",
    "van-loi-char-siu.jpg": "https://images.unsplash.com/photo-1563245372-f21724e3856d?auto=format&fit=crop&w=1200&q=80",
    "van-loi-noodle-platter.jpg": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=1200&q=80",
    "van-loi-roast-display.jpg": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=1200&q=80"
}

headers = {'User-Agent': 'Mozilla/5.0'}
for filename, url in images.items():
    filepath = os.path.join("van-loi-chinese-barbecue/images", filename)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp, open(filepath, 'wb') as f:
            f.write(resp.read())
        print(f"Downloaded {filename}: {os.path.getsize(filepath)} bytes")
    except Exception as e:
        print(f"Error {filename}: {e}")
