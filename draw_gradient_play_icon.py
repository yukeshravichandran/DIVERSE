from PIL import Image, ImageDraw

dest_path = r"c:\Users\yukes\Documents\Agentic AI CRM\wp-content\themes\diverse-wp-theme-main\assets\images\brand\gradient-play-icon.png"

size = 256

# 1. Create a diagonal gradient image
img = Image.new("RGBA", (size, size))
for y in range(size):
    for x in range(size):
        # Diagonal factor 0 to 1
        factor = (x + y) / (size * 2)
        # Cyan (#00d2ff -> 0, 210, 255) to Blue (#0d6efd -> 13, 110, 253)
        r = int(0 + (13 - 0) * factor)
        g = int(210 + (110 - 210) * factor)
        b = int(255 + (253 - 255) * factor)
        img.putpixel((x, y), (r, g, b, 255))

# 2. Create the mask (L mode)
# White means opaque, black means transparent
mask = Image.new("L", (size, size), 0)
mask_draw = ImageDraw.Draw(mask)

# Draw solid white circle (this is the opaque gradient part)
mask_draw.ellipse((16, 16, 240, 240), fill=255)

# Draw black triangle in the middle (this punches a transparent hole in the circle)
# Points for a right-pointing triangle
points = [(104, 88), (104, 168), (168, 128)]
mask_draw.polygon(points, fill=0)

# Add thick lines and rounded corners to the triangle so it looks premium
mask_draw.line(points + [points[0]], fill=0, width=16)
for pt in points:
    mask_draw.ellipse((pt[0]-8, pt[1]-8, pt[0]+8, pt[1]+8), fill=0)

# 3. Apply mask to the gradient image
img.putalpha(mask)

# Resize to smooth out the edges (anti-aliasing)
img = img.resize((64, 64), Image.Resampling.LANCZOS)
img.save(dest_path, "PNG")
print("Gradient Cutout Play icon saved!")
