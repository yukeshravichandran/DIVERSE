from PIL import Image, ImageDraw

dest_path = r"c:\Users\yukes\Documents\Agentic AI CRM\wp-content\themes\diverse-wp-theme-main\assets\images\brand\fast-forward-icon.png"

size = 256
img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

color = "white"
width = 20

# Draw thick white circle
draw.ellipse((24, 24, 232, 232), outline=color, width=width)

# Draw Chevron 1 (Left)
c1 = [(80, 90), (120, 128), (80, 166)]
draw.line(c1, fill=color, width=width, joint="curve")

# Draw Chevron 2 (Right)
c2 = [(130, 90), (170, 128), (130, 166)]
draw.line(c2, fill=color, width=width, joint="curve")

# Add rounded caps to the ends of the chevrons for a premium look
cap_r = width // 2
for pt in [c1[0], c1[2], c2[0], c2[2]]:
    draw.ellipse((pt[0]-cap_r, pt[1]-cap_r, pt[0]+cap_r, pt[1]+cap_r), fill=color)

# Smooth edges with Lanczos resampling
img = img.resize((64, 64), Image.Resampling.LANCZOS)
img.save(dest_path, "PNG")
print("Fast Forward icon saved!")
