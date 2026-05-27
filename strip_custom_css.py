import glob
import re

html_files = glob.glob("*.html")
for file in html_files:
    if file in ["dashboard.html", "login.html", "register.html"]:
        continue
    with open(file, "r", encoding="utf-8") as f:
        html = f.read()
    
    html = html.replace('<link rel="stylesheet" href="diverse-ultimate.css?v=1">', '')
    html = html.replace('<link rel="stylesheet" href="diverse-professional.css">', '')
    html = html.replace('<link rel="stylesheet" href="diverse-tiles.css?v=4">', '')
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(html)
print("Removed custom CSS!")
