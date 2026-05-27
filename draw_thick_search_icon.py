from PIL import Image, ImageDraw

dest_path = r"c:\Users\yukes\Documents\Agentic AI CRM\wp-content\themes\diverse-wp-theme-main\assets\images\brand\search-icon.png"

# Draw at high res (256x256) for perfect smooth edges
size = 256
img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# They requested blue earlier
color = "#00d2ff" 
width = 36 # Very thick border to match the uploaded image

# Circle bounds
draw.ellipse((40, 40, 160, 160), outline=color, width=width)

# Handle
# Start at bottom right of circle, end near bottom right corner
draw.line((140, 140, 220, 220), fill=color, width=width)

# Round caps for the handle to match the image exactly
r = width // 2
draw.ellipse((140-r, 140-r, 140+r, 140+r), fill=color)
draw.ellipse((220-r, 220-r, 220+r, 220+r), fill=color)

# Resize down with Lanczos to get beautiful anti-aliasing
img = img.resize((64, 64), Image.Resampling.LANCZOS)
img.save(dest_path, "PNG")
print(f"Saved custom thick search icon to {dest_path}")
