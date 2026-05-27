import urllib.request

url = "https://img.icons8.com/ios-glyphs/60/ffffff/github.png"
dest_path = r"c:\Users\yukes\Documents\Agentic AI CRM\wp-content\themes\diverse-wp-theme-main\assets\images\brand\github-icon-raster.png"

print("Downloading guaranteed white PNG from Icons8...")
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response, open(dest_path, 'wb') as f:
    f.write(response.read())

print("Saved!")
