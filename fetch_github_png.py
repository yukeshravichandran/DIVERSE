import urllib.request
from PIL import Image

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/240px-Octicons-mark-github.svg.png"
dest_path = r"c:\Users\yukes\Documents\Agentic AI CRM\wp-content\themes\diverse-wp-theme-main\assets\images\brand\github-icon.png"

print("Downloading GitHub PNG...")
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response, open(dest_path, 'wb') as out_file:
    out_file.write(response.read())

print("Converting black to white for the dark theme...")
img = Image.open(dest_path).convert("RGBA")
pixels = img.getdata()

new_pixels = []
for r, g, b, a in pixels:
    # If the pixel is dark and opaque, make it pure white
    if r < 100 and g < 100 and b < 100 and a > 0:
        new_pixels.append((255, 255, 255, a))
    else:
        new_pixels.append((r, g, b, a))

img.putdata(new_pixels)
img = img.resize((64, 64), Image.Resampling.LANCZOS)
img.save(dest_path, "PNG")
print(f"Perfect white GitHub PNG saved to {dest_path}")
