import glob
import os

svg_chevron = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>'

html_files = glob.glob(r'c:\Users\yukes\Documents\Agentic AI CRM\*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    content = content.replace('<ion-icon name="chevron-down-outline"></ion-icon>', svg_chevron)

    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Replaced ion-icon with SVG in {os.path.basename(file_path)}")

print("Done.")
