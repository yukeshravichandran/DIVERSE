import os
from PIL import Image

generated_img_path = r"C:\Users\yukes\.gemini\antigravity-ide\brain\1521e92f-6bc0-4dcc-a1a9-4ef3900e7329\search_bar_icon_1779879170750.png"
dest_path = r"c:\Users\yukes\Documents\Agentic AI CRM\wp-content\themes\diverse-wp-theme-main\assets\images\brand\search-icon.png"

# Open the image
img = Image.open(generated_img_path).convert("RGBA")

# Resize to a reasonable icon size (e.g. 32x32)
img = img.resize((32, 32), Image.Resampling.LANCZOS)

# Save to the website directory
img.save(dest_path, "PNG")
print(f"Saved optimized search icon to {dest_path}")
