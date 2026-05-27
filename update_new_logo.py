import os
from PIL import Image

def remove_bg_crop_and_save(src_path, dest_paths):
    print(f"Processing {src_path}")
    img = Image.open(src_path).convert("RGBA")
    
    # Get top-left pixel as background color
    bg_color = img.getpixel((0, 0))
    data = img.getdata()
    new_data = []
    
    tolerance = 45 # Slightly higher tolerance to remove artifacts
    
    for item in data:
        if abs(item[0] - bg_color[0]) < tolerance and \
           abs(item[1] - bg_color[1]) < tolerance and \
           abs(item[2] - bg_color[2]) < tolerance:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
        
    for dest in dest_paths:
        img.save(dest, "PNG")
        print(f"Saved to {dest}")

artifact_logo = r"C:\Users\yukes\.gemini\antigravity-ide\brain\1521e92f-6bc0-4dcc-a1a9-4ef3900e7329\diverse_logo_cognizant_style_1779855109677.png"

base_path = r"c:\Users\yukes\Documents\Agentic AI CRM\wp-content\themes\diverse-wp-theme-main\assets\images"
brand_logo = os.path.join(base_path, "brand", "diverse-logo.png")
black_logo = os.path.join(base_path, "home-screenshots", "diverse-logo-black.png")

try:
    remove_bg_crop_and_save(artifact_logo, [brand_logo, black_logo])
except Exception as e:
    print(f"Error: {e}")
