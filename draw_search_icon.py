from PIL import Image, ImageDraw

dest_path = r"c:\Users\yukes\Documents\Agentic AI CRM\wp-content\themes\diverse-wp-theme-main\assets\images\brand\search-icon.png"

# Create a truly transparent 32x32 image
img = Image.new("RGBA", (32, 32), (255, 255, 255, 0))
draw = ImageDraw.Draw(img)

# Draw the magnifying glass circle (outline only, completely transparent inside)
draw.ellipse((4, 4, 22, 22), outline="white", width=3)

# Draw the handle
draw.line((18, 18, 28, 28), fill="white", width=3)

# Save to the website directory, overwriting the old AI generated one
img.save(dest_path, "PNG")
print(f"Saved perfect transparent search icon to {dest_path}")
