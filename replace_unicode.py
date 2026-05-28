import glob
import os

svg_html = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" style="margin-left: 5px; display: inline-block;"><polyline points="6 9 12 15 18 9"></polyline></svg>'
unicode_arrow = '<span style="color: black; margin-left: 5px; font-size: 14px;">&#9660;</span>'

html_files = glob.glob(r'c:\Users\yukes\Documents\Agentic AI CRM\*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    content = content.replace(svg_html, unicode_arrow)

    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Replaced SVG with Unicode arrow in {os.path.basename(file_path)}")

print("Done.")
