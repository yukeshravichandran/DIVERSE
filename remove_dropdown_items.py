import glob
import os
import re

html_files = glob.glob(r'c:\Users\yukes\Documents\Agentic AI CRM\*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Remove HR menu item
    # <li ... id="menu-item-1199"><a href="...">HR</a></li>
    content = re.sub(r'<li[^>]*id="menu-item-1199"[^>]*>.*?</a></li>', '', content, flags=re.DOTALL)
    
    # Remove CRM menu item under features
    # <li ... id="menu-item-12137"><a href="...">CRM</a></li>
    content = re.sub(r'<li[^>]*id="menu-item-12137"[^>]*>.*?</a></li>', '', content, flags=re.DOTALL)

    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Removed HR and CRM from {os.path.basename(file_path)}")

print("Done.")
