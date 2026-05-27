import os
import urllib.request
from PIL import Image, ImageDraw, ImageFont

# 1. Download a modern font (e.g., Inter Bold)
# 1. Use system font
font_path = r"C:\Windows\Fonts\seguisb.ttf"
if not os.path.exists(font_path):
    # Fallback to Arial
    font_path = r"C:\Windows\Fonts\arialbd.ttf"


# 2. Paths
emblem_path = r"C:\Users\yukes\.gemini\antigravity-ide\brain\1521e92f-6bc0-4dcc-a1a9-4ef3900e7329\diverse_logo_1779779911436.png"
base_path = r"c:\Users\yukes\Documents\Agentic AI CRM\wp-content\themes\diverse-wp-theme-main\assets\images"
brand_logo = os.path.join(base_path, "brand", "diverse-logo.png")
black_logo = os.path.join(base_path, "home-screenshots", "diverse-logo-black.png")

# 3. Process the emblem (remove background)
print("Processing emblem...")
emblem = Image.open(emblem_path).convert("RGBA")
bg_color = emblem.getpixel((0, 0))
data = emblem.getdata()
new_data = []
tolerance = 45

for item in data:
    if abs(item[0] - bg_color[0]) < tolerance and \
       abs(item[1] - bg_color[1]) < tolerance and \
       abs(item[2] - bg_color[2]) < tolerance:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)
        
emblem.putdata(new_data)
bbox = emblem.getbbox()
if bbox:
    emblem = emblem.crop(bbox)

# Resize emblem to a fixed height, e.g., 150px
target_height = 150
aspect_ratio = emblem.width / emblem.height
target_width = int(target_height * aspect_ratio)
emblem = emblem.resize((target_width, target_height), Image.Resampling.LANCZOS)

# 4. Create text image
print("Rendering text...")
text = "diverse"
font_size = 140
font = ImageFont.truetype(font_path, font_size)

# Estimate text size
# A simple way to get text size in newer Pillow is draw.textbbox
dummy_img = Image.new("RGBA", (1, 1))
draw = ImageDraw.Draw(dummy_img)
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# 5. Create final canvas
padding = 40 # space between emblem and text
canvas_width = target_width + padding + text_width
canvas_height = max(target_height, text_height) + 40 # extra padding

canvas = Image.new("RGBA", (canvas_width, canvas_height), (255, 255, 255, 0))

# Paste emblem vertically centered
emblem_y = (canvas_height - target_height) // 2
canvas.paste(emblem, (0, emblem_y), emblem)

# Draw text vertically centered
# The text 'diverse' has ascenders (d) and standard height for others. 
# Cognizant uses dark blue, almost navy: #000048 or #0f172a
text_color = (15, 23, 42, 255) # Dark slate/navy blue
draw = ImageDraw.Draw(canvas)
# Calculate text Y to visually center with emblem
text_y = (canvas_height - text_height) // 2 - text_bbox[1]
draw.text((target_width + padding, text_y), text, font=font, fill=text_color)

# 6. Final crop to tight bounding box
final_bbox = canvas.getbbox()
if final_bbox:
    canvas = canvas.crop(final_bbox)

# 7. Save to project directories
canvas.save(brand_logo, "PNG")
canvas.save(black_logo, "PNG")

print("Successfully created combined logo and saved to brand directories.")
