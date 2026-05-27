import math
from PIL import Image, ImageDraw

dest_path = r"c:\Users\yukes\Documents\Agentic AI CRM\wp-content\themes\diverse-wp-theme-main\assets\images\brand\play-icon.png"

# High res for anti-aliasing
img = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

color = "white"
width = 24

# The broken circle
# We draw from 215 degrees to 145 degrees (gap on the left)
start_angle = 215
end_angle = 145
draw.arc((32, 32, 224, 224), start=start_angle, end=end_angle, fill=color, width=width)

# Add rounded caps to the arc
r_arc = 96
x1 = 128 + r_arc * math.cos(math.radians(start_angle))
y1 = 128 + r_arc * math.sin(math.radians(start_angle))
x2 = 128 + r_arc * math.cos(math.radians(end_angle))
y2 = 128 + r_arc * math.sin(math.radians(end_angle))

cap_r = width // 2
draw.ellipse((x1-cap_r, y1-cap_r, x1+cap_r, y1+cap_r), fill=color)
draw.ellipse((x2-cap_r, y2-cap_r, x2+cap_r, y2+cap_r), fill=color)

# Play triangle (thick lines for rounded corners)
points = [(104, 88), (104, 168), (174, 128)]
draw.polygon(points, fill=color)
draw.line(points + [points[0]], fill=color, width=16)
for pt in points:
    draw.ellipse((pt[0]-8, pt[1]-8, pt[0]+8, pt[1]+8), fill=color)

img = img.resize((64, 64), Image.Resampling.LANCZOS)
img.save(dest_path, "PNG")
print("Custom Play icon saved!")
