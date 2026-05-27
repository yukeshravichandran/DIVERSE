import os
import glob
import re

html_files = glob.glob("*.html")

link_tag = '\n    <link rel="stylesheet" href="diverse-tiles.css">\n'

for file in html_files:
    if file in ["dashboard.html", "login.html", "register.html"]:
        # Skip our custom built non-marketing pages
        continue

    with open(file, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. The Orange Purge (Find & Replace directly in HTML)
    html = re.sub(r'#e54f38', '#0d6efd', html, flags=re.IGNORECASE)
    html = re.sub(r'#f96b24', '#0d6efd', html, flags=re.IGNORECASE)
    html = re.sub(r'#ff8a50', '#0d6efd', html, flags=re.IGNORECASE) # Light orange
    html = re.sub(r'#ff5722', '#0d6efd', html, flags=re.IGNORECASE) # Deep orange
    # Also replace any string "orange" if it's used as a class or style, though risky, we can replace "color: orange"
    html = re.sub(r'color:\s*orange', 'color: #0d6efd', html, flags=re.IGNORECASE)

    # 2. Remove previous diverse-theme.css injection if it exists
    html = html.replace('<link rel="stylesheet" href="diverse-theme.css">', '')
    
    # 3. Inject new diverse-tiles.css
    if '<link rel="stylesheet" href="diverse-tiles.css">' not in html:
        html = html.replace('</head>', link_tag + '</head>')
        
    with open(file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Purged orange and injected diverse-tiles.css into {file}")

print("Tile UI update complete!")
