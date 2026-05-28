import urllib.request
from PIL import Image

# Use Wikimedia Commons thumbnail for the white GitHub logo (Invertocat)
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/GitHub_Invertocat_Logo.svg/200px-GitHub_Invertocat_Logo.svg.png"
dest_path = r"c:\Users\yukes\Documents\Agentic AI CRM\wp-content\themes\diverse-wp-theme-main\assets\images\brand\github-icon.png"

print("Downloading GitHub logo from Wikimedia...")
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response, open(dest_path, 'wb') as out_file:
    out_file.write(response.read())

print("Resizing for optimal web performance...")
img = Image.open(dest_path)
img = img.convert("RGBA")
# Resize to 64x64 icon size
img = img.resize((64, 64), Image.Resampling.LANCZOS)
img.save(dest_path, "PNG")

print(f"GitHub icon saved to {dest_path}")
