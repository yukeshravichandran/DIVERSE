import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Aggressive text replacement across everything (attributes, scripts, etc.)
html = html.replace("Horilla", "Diverse")
html = html.replace("HORILLA", "DIVERSE")
html = html.replace("horilla", "diverse")

# 2. Repair URLs that were broken by the aggressive replace
html = html.replace("diverse.com", "horilla.com")
html = html.replace("diverse-", "horilla-")
html = html.replace("/diverse/", "/horilla/")
html = html.replace("diverse_wp", "horilla_wp")
html = html.replace("-diverse", "-horilla")

# Fix specific known WordPress paths
html = html.replace("wp-content/themes/diverse", "wp-content/themes/horilla")

# 3. Replace the physical image logo in the header and footer with text so the user doesn't see the Horilla picture
html = re.sub(r'<img[^>]*class="[^"]*hr-header__logo[^"]*"[^>]*>', '<span style="font-size: 2rem; font-weight: bold; color: #fff;">Diverse</span>', html)
html = re.sub(r'<img[^>]*class="[^"]*footer-widget__logo[^"]*"[^>]*>', '<span style="font-size: 2rem; font-weight: bold; color: #fff;">Diverse</span>', html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Aggressive rebrand complete!")
