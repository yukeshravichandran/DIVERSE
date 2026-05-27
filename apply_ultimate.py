import glob

html_files = glob.glob("*.html")

link_tag = '\n    <link rel="stylesheet" href="diverse-ultimate.css?v=1">\n'

for file in html_files:
    if file in ["dashboard.html", "login.html", "register.html"]:
        continue

    with open(file, "r", encoding="utf-8") as f:
        html = f.read()

    # Remove the old professional CSS
    html = html.replace('<link rel="stylesheet" href="diverse-professional.css">', '')
    html = html.replace('<link rel="stylesheet" href="diverse-tiles.css?v=4">', '')
    html = html.replace('<link rel="stylesheet" href="diverse-tiles.css?v=3">', '')

    # Inject the ultimate CSS
    if 'href="diverse-ultimate.css' not in html:
        html = html.replace('</head>', link_tag + '</head>')
        
    with open(file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Applied Ultimate CSS to {file}")

print("Ultimate Theme Applied!")
