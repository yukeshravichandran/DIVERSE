import glob
import re

html_files = glob.glob("*.html")

link_tag = '\n    <link rel="stylesheet" href="diverse-professional.css">\n'

for file in html_files:
    if file in ["dashboard.html", "login.html", "register.html"]:
        continue

    with open(file, "r", encoding="utf-8") as f:
        html = f.read()

    # Inject the new professional CSS before </head>
    if '<link rel="stylesheet" href="diverse-professional.css">' not in html:
        html = html.replace('</head>', link_tag + '</head>')
        
    # Brutal string replacement for Horilla
    html = html.replace("Horilla", "Diverse")
    html = html.replace("HORILLA", "DIVERSE")
    
    html = html.replace(">https://www.horilla.com", ">https://www.diverse.com")
    html = html.replace(">horilla.com", ">diverse.com")
    html = html.replace("@horilla.com", "@diverse.com")
    html = html.replace("horilla-opensource/horilla-crm", "diverse-opensource/diverse-crm")
    
    # Text replacements in alt/title tags
    html = re.sub(r'alt="([^"]*)horilla([^"]*)"', r'alt="\1diverse\2"', html, flags=re.IGNORECASE)
    html = re.sub(r'title="([^"]*)horilla([^"]*)"', r'title="\1diverse\2"', html, flags=re.IGNORECASE)

    # Standalone 'horilla' in text
    html = re.sub(r'\bhorilla\b', 'diverse', html)

    # Clean up favicons
    html = re.sub(r'<link[^>]*rel=["\']icon["\'][^>]*>', '', html, flags=re.IGNORECASE)
    html = re.sub(r'<link[^>]*rel=["\']apple-touch-icon["\'][^>]*>', '', html, flags=re.IGNORECASE)

    with open(file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Applied Professional Styling and Text Rebrand to {file}")

print("Professional Restoration Complete!")
