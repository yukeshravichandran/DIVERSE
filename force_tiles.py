import os
import glob
import re

html_files = glob.glob("*.html")

link_tag = '\n    <link rel="stylesheet" href="diverse-tiles.css?v=3">\n'

for file in html_files:
    if file in ["dashboard.html", "login.html", "register.html"]:
        continue

    with open(file, "r", encoding="utf-8") as f:
        html = f.read()

    # Aggressive replace to remove older CSS injections
    html = re.sub(r'<link rel="stylesheet" href="diverse-theme\.css[^>]*>', '', html)
    html = re.sub(r'<link rel="stylesheet" href="diverse-tiles\.css[^>]*>', '', html)
    
    html = html.replace('</head>', link_tag + '</head>')
        
    with open(file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Force-injected cache-busting diverse-tiles.css?v=3 into {file}")

print("Done!")
