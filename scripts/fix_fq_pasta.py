import urllib.request

url = "https://images.unsplash.com/photo-1608897013039-887f21d8c804?auto=format&fit=crop&w=800&q=80"
dest = "french-quarter-restaurant/images/cajun-chicken-pasta.jpg"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=15) as resp, open(dest, 'wb') as f:
    f.write(resp.read())
print("Downloaded cajun-chicken-pasta.jpg successfully")
