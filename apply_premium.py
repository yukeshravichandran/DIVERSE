import glob

html_files = glob.glob("*.html")

link_tag = '\n    <link rel="stylesheet" href="diverse-premium.css">\n'

for file in html_files:
    if file in ["dashboard.html", "login.html", "register.html"]:
        continue

    with open(file, "r", encoding="utf-8") as f:
        html = f.read()

    # Inject the premium CSS after diverse-core.css
    if 'href="diverse-premium.css"' not in html:
        html = html.replace('</head>', link_tag + '</head>')
        
    with open(file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Applied Premium Glassmorphism to {file}")

print("Premium Theme Applied!")
