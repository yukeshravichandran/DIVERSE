import os
import re

workspace = r"c:\Users\yukes\Documents\Agentic AI CRM"

for root, dirs, files in os.walk(workspace):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Use regex to find the logo tag and update dimensions
            # Old: width="124" height="35" or height="35" ... width="124"
            # It's easier to just replace specific strings based on what we saw
            new_content = re.sub(r'width="124"', 'width="250"', content)
            new_content = re.sub(r'height="35"', 'height="40"', new_content)
            
            # Let's also be safe and use a more flexible regex for the brand logo
            # <img ... diverse-logo.png ... >
            def replace_logo_dims(match):
                tag = match.group(0)
                tag = re.sub(r'width="[^"]+"', 'width="250"', tag)
                tag = re.sub(r'height="[^"]+"', 'height="40"', tag)
                return tag
            
            new_content = re.sub(r'<img[^>]*diverse-logo\.png[^>]*>', replace_logo_dims, content)
            
            # And for the footer logo (diverse-logo-black.png)
            new_content = re.sub(r'<img[^>]*diverse-logo-black\.png[^>]*>', replace_logo_dims, new_content)
            
            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated logo dimensions in {file}")

# Update CSS as well
css_path = os.path.join(workspace, "diverse-cloud.css")
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

# I previously added height: 55px !important to diverse-custom-logo
# Let's change it to 40px to match the user's request.
css_content = re.sub(r'height:\s*55px\s*!important;', 'height: 40px !important;', css_content)
css_content = re.sub(r'height:\s*45px;', 'height: 40px !important;', css_content)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css_content)
print("Updated CSS dimensions.")
