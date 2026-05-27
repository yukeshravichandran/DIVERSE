from PIL import Image, ImageChops

def remove_bg_and_crop(filepath):
    print(f"Processing {filepath}")
    img = Image.open(filepath).convert("RGBA")
    
    # Assuming the background is the color of the top-left pixel
    bg_color = img.getpixel((0, 0))
    
    data = img.getdata()
    new_data = []
    
    # Allow some tolerance for anti-aliasing/compression
    tolerance = 30
    
    for item in data:
        if abs(item[0] - bg_color[0]) < tolerance and \
           abs(item[1] - bg_color[1]) < tolerance and \
           abs(item[2] - bg_color[2]) < tolerance:
            new_data.append((255, 255, 255, 0)) # Transparent
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    
    # Auto-crop to the bounding box of non-transparent pixels
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
        
    img.save(filepath, "PNG")
    print(f"Saved {filepath}")

base_path = r"c:\Users\yukes\Documents\Agentic AI CRM\wp-content\themes\diverse-wp-theme-main\assets\images"
brand_logo = f"{base_path}\\brand\\diverse-logo.png"
black_logo = f"{base_path}\\home-screenshots\\diverse-logo-black.png"

try:
    remove_bg_and_crop(brand_logo)
    remove_bg_and_crop(black_logo)
except Exception as e:
    print(f"Error processing images: {e}")
