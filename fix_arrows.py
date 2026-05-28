import os
import glob
import re

html_files = glob.glob(r'c:\Users\yukes\Documents\Agentic AI CRM\*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content

    # Add to Features
    content = content.replace(
        '<span class="menu-label">Features</span>',
        '<span class="menu-label">Features<span class="dropdown-icon"><ion-icon name="chevron-down-outline"></ion-icon></span></span>'
    )
    
    # Add to Pricing
    content = content.replace(
        '<span class="menu-label">Pricing</span>',
        '<span class="menu-label">Pricing<span class="dropdown-icon"><ion-icon name="chevron-down-outline"></ion-icon></span></span>'
    )

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(file_path)}")

print("Done.")
