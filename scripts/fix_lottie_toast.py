import urllib.request

url = "https://images.unsplash.com/photo-1588137378633-dea1336ce1e2?auto=format&fit=crop&w=800&q=80"
dest = "lottie-s-cafe/images/avocado-toast-bowl.jpg"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=15) as resp, open(dest, 'wb') as f:
    f.write(resp.read())
print("Downloaded distinct avocado-toast-bowl.jpg successfully")
