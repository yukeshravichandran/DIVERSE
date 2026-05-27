from PIL import Image, ImageDraw

dest_path = r"c:\Users\yukes\Documents\Agentic AI CRM\wp-content\themes\diverse-wp-theme-main\assets\images\brand\search-icon.png"

# We want a 2:1 aspect ratio, say 64x32
width, height = 80, 40
img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

border_width = 4
corner_radius = 8

# Colors based on the uploaded image
left_bg = "#E6F4FB"
right_bg = "#B1EBF2"
border_color = "black"

# Draw the left background (rounded rect)
draw.rounded_rectangle(
    [0, 0, width-1, height-1],
    radius=corner_radius,
    fill=left_bg,
    outline=border_color,
    width=border_width
)

# Draw the right background (we can draw a rectangle on the right side, but we need to keep the right corners rounded)
# So we'll draw a right rounded rect, then a flat rect to cover the left part of it
right_width = width // 3
right_x = width - right_width

# Draw filled rectangle for right section
draw.rectangle([right_x, border_width//2, width - corner_radius - 1, height - border_width//2 - 1], fill=right_bg)

# Draw rounded corner for right section (bottom right)
draw.pieslice([width - 2*corner_radius - border_width//2, height - 2*corner_radius - border_width//2, width - border_width//2, height - border_width//2], 0, 90, fill=right_bg)
# Top right
draw.pieslice([width - 2*corner_radius - border_width//2, border_width//2, width - border_width//2, 2*corner_radius + border_width//2], 270, 360, fill=right_bg)
# Fill the gaps
draw.rectangle([right_x, border_width//2, width - border_width//2, height - corner_radius], fill=right_bg)
draw.rectangle([right_x, corner_radius, width - border_width//2, height - border_width//2 - 1], fill=right_bg)

# Draw the vertical divider line
draw.line([right_x, 0, right_x, height], fill=border_color, width=border_width)

# Redraw the outer border to make sure it's clean on top
draw.rounded_rectangle(
    [0, 0, width-1, height-1],
    radius=corner_radius,
    outline=border_color,
    width=border_width
)

# Draw the magnifying glass inside the right section
glass_x = right_x + 6
glass_y = 10
glass_size = 10
draw.ellipse([glass_x, glass_y, glass_x + glass_size, glass_y + glass_size], outline=border_color, width=3)
# Handle
handle_start = (glass_x + glass_size - 1, glass_y + glass_size - 1)
handle_end = (glass_x + glass_size + 4, glass_y + glass_size + 4)
draw.line([handle_start, handle_end], fill=border_color, width=3)

# Save the image
img.save(dest_path, "PNG")
print(f"Saved custom search bar icon to {dest_path}")
