import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace footer logo specifically
html = re.sub(r'<img[^>]*class="[^"]*hrl-footer__logo[^"]*"[^>]*>', '<span style="font-size: 2rem; font-weight: bold; color: #000;">Diverse</span>', html)

# Replace ANY image tag that has horilla-logo in the src (in case they have mobile logos, sticky logos, etc.)
html = re.sub(r'<img[^>]*src="[^"]*horilla-logo[^"]*"[^>]*>', '<span style="font-size: 2rem; font-weight: bold; color: #000;">Diverse</span>', html)

# Remove the horilla favicon
html = re.sub(r'<link rel="shortcut icon"[^>]*>', '', html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Remaining logos patched!")
