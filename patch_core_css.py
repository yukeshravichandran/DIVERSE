import os
import urllib.request
import glob
import re

css_urls = [
    "https://www.horilla.com/wp-content/themes/horilla-wp-theme-main/assets/css/style.min.css",
    "https://www.horilla.com/wp-content/themes/horilla-wp-theme-main/assets/css/home.style.min.css",
    "https://www.horilla.com/wp-content/themes/horilla-wp-theme-main/assets/css/home-style.css"
]

combined_css = ""

for url in css_urls:
    print(f"Downloading {url}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            css_text = response.read().decode('utf-8')
            
            # Fix relative URLs inside the CSS
            css_text = css_text.replace('url("../', 'url("https://www.horilla.com/wp-content/themes/horilla-wp-theme-main/assets/')
            css_text = css_text.replace("url('../", "url('https://www.horilla.com/wp-content/themes/horilla-wp-theme-main/assets/")
            
            combined_css += f"\n/* --- From {url.split('/')[-1]} --- */\n"
            combined_css += css_text
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")

print("Applying Deep Blue colors to the CSS...")
# The classic Horilla Orange is #e54f38. Secondary is #f96b24.
# We replace it with our Deep Blue: #0d47a1 and Accent: #0d6efd
combined_css = re.sub(r'(?i)#e54f38', '#0d47a1', combined_css)
combined_css = re.sub(r'(?i)#f96b24', '#0d6efd', combined_css)

# Also replace RGB versions
combined_css = re.sub(r'rgba?\(\s*229\s*,\s*79\s*,\s*56\s*(?:,[^)]+)?\)', '#0d47a1', combined_css)
combined_css = re.sub(r'rgba?\(\s*249\s*,\s*107\s*,\s*36\s*(?:,[^)]+)?\)', '#0d6efd', combined_css)

# Hide horilla specific logos in CSS if any
combined_css += """
/* Hide logos cleanly */
img[src*="logo-mascot"], 
img[src*="horilla-logo"],
.hr-header__logo img,
.footer-widget__logo img {
    display: none !important;
}
"""

with open("diverse-core.css", "w", encoding="utf-8") as f:
    f.write(combined_css)
print("Saved diverse-core.css")

print("Updating HTML files to use diverse-core.css...")
for file in glob.glob("*.html"):
    if file in ["dashboard.html", "login.html", "register.html"]:
        continue
    
    with open(file, "r", encoding="utf-8") as f:
        html = f.read()

    # Remove the broken references that obliterate_horilla.py created
    html = re.sub(r'<link rel=[\'"]stylesheet[\'"][^>]*href=[\'"][^\'"]*assets/css/[^\'"]*[\'"][^>]*>', '', html, flags=re.IGNORECASE)
    
    # Inject our combined core CSS
    link_tag = '\n    <link rel="stylesheet" href="diverse-core.css">\n'
    if 'href="diverse-core.css"' not in html:
        html = html.replace('</head>', link_tag + '</head>')
        
    with open(file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Updated {file}")

print("Done! Core CSS hijacked and patched.")
