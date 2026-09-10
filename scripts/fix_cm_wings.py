import urllib.request

url = "https://images.unsplash.com/photo-1567620832903-9fc6debc209f?auto=format&fit=crop&w=800&q=80"
dest = "cheers-mate-bar-and-lounge/images/crispy-wings.jpg"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=15) as resp, open(dest, 'wb') as f:
    f.write(resp.read())
print("Downloaded crispy-wings.jpg successfully")
