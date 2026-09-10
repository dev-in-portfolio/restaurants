import os
import urllib.request

path = r"C:\Users\dtoro\.gemini\antigravity\scratch\restaurants\valhalla-pub-and-eatery\images\fish-chips-wings.jpg"
url = "https://images.unsplash.com/photo-1526234362653-3b75a0c07438?w=800&q=80"
headers = {"User-Agent": "Mozilla/5.0"}
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp, open(path, "wb") as f:
    f.write(resp.read())
print(f"Downloaded fish-chips-wings.jpg ({os.path.getsize(path)} bytes)")
