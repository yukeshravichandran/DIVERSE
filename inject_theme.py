import os
import glob

html_files = glob.glob("*.html")

link_tag = '\n    <link rel="stylesheet" href="diverse-theme.css">\n'

for file in html_files:
    if file in ["dashboard.html", "login.html", "register.html"]:
        # We might not want to touch our custom-built UI pages, just the cloned marketing ones
        # But wait, dashboard uses bootstrap. It's fine. We'll skip the custom ones.
        continue

    with open(file, "r", encoding="utf-8") as f:
        html = f.read()

    # Remove the old inline blue style we added in deep clone
    old_style_start = html.find('<style>\n        /* Force deep blue background')
    if old_style_start != -1:
        old_style_end = html.find('</style>\n    </head>', old_style_start)
        if old_style_end != -1:
            html = html[:old_style_start] + html[old_style_end + 18:]

    # Inject the new stylesheet right before </head>
    if '<link rel="stylesheet" href="diverse-theme.css">' not in html:
        html = html.replace('</head>', link_tag + '</head>')
        
        with open(file, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Injected diverse-theme.css into {file}")

print("Injection complete!")
