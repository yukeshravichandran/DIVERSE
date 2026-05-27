import os
import shutil

workspace = r"c:\Users\yukes\Documents\Agentic AI CRM"
artifact_dir = r"C:\Users\yukes\.gemini\antigravity-ide\brain\1521e92f-6bc0-4dcc-a1a9-4ef3900e7329"

# 1. Fix 'index.htmlwp-content' to 'wp-content' in all HTML files
for root, dirs, files in os.walk(workspace):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # The scraper also might have done index.html/wp-content or similar, let's just replace index.htmlwp-content
            new_content = content.replace("index.htmlwp-content", "wp-content")
            
            # Also fix potential index.html/wp-content if any
            new_content = new_content.replace("index.html/wp-content", "wp-content")
            
            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Fixed paths in {file}")

# 2. Copy the artifact logo to the target locations
logo_artifact = os.path.join(artifact_dir, "diverse_logo_1779779911436.png")
if os.path.exists(logo_artifact):
    brand_dir = os.path.join(workspace, "wp-content", "themes", "diverse-wp-theme-main", "assets", "images", "brand")
    screenshots_dir = os.path.join(workspace, "wp-content", "themes", "diverse-wp-theme-main", "assets", "images", "home-screenshots")
    
    os.makedirs(brand_dir, exist_ok=True)
    os.makedirs(screenshots_dir, exist_ok=True)
    
    target1 = os.path.join(brand_dir, "diverse-logo.png")
    target2 = os.path.join(screenshots_dir, "diverse-logo-black.png")
    
    shutil.copy2(logo_artifact, target1)
    shutil.copy2(logo_artifact, target2)
    print("Logo successfully copied to brand directories.")

# 3. Add CSS to hide the orange icon in the hero title
css_path = os.path.join(workspace, "diverse-cloud.css")
if os.path.exists(css_path):
    with open(css_path, "a", encoding="utf-8") as f:
        f.write("\n/* Hide orange highlight icon in hero title */\n.hrl-hero__title:after {\n    display: none !important;\n}\n")
    print("Added CSS to hide orange hero icon.")

print("All fixes applied successfully.")
