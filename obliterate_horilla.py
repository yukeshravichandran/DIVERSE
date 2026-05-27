import glob
import re

html_files = glob.glob("*.html")

for file in html_files:
    if file in ["dashboard.html", "login.html", "register.html"]:
        continue

    with open(file, "r", encoding="utf-8") as f:
        html = f.read()

    # We will do a brutal replacement of the word horilla in all its forms
    html = html.replace("Horilla", "Diverse")
    html = html.replace("HORILLA", "DIVERSE")
    
    # For lowercase horilla, we need to be careful not to break the CDN links if we want styles to load
    # Wait, the styles are loaded from `https://www.horilla.com/wp-content/themes/horilla-wp-theme-main/assets/css/home.style.min.css`
    # If I replace 'horilla', the CSS won't load, and the site will look completely broken.
    # So I will only replace 'horilla' if it's NOT part of a URL.
    # Better yet, I'll replace it in text nodes, but let's just do it carefully.
    
    # Replace horilla.com links that are visible to the user:
    html = html.replace(">https://www.horilla.com", ">https://www.diverse.com")
    html = html.replace(">horilla.com", ">diverse.com")
    html = html.replace("@horilla.com", "@diverse.com")
    html = html.replace("horilla-opensource/horilla-crm", "diverse-opensource/diverse-crm")
    
    # Replace "horilla" in alt text and titles
    html = re.sub(r'alt="([^"]*)horilla([^"]*)"', r'alt="\1diverse\2"', html, flags=re.IGNORECASE)
    html = re.sub(r'title="([^"]*)horilla([^"]*)"', r'title="\1diverse\2"', html, flags=re.IGNORECASE)

    # Any standalone 'horilla' in text
    html = re.sub(r'\bhorilla\b', 'diverse', html)
    
    # Fix the navigation links that still point to horilla subdomains
    html = html.replace("https://cloud.horilla.com/", "#")
    html = html.replace("http://docs.horilla.com/", "docs.html")
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Obliterated Horilla references in {file}")

print("Total rebrand complete!")
