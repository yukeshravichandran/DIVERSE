import glob
import re

html_files = glob.glob("*.html")

for file in html_files:
    if file in ["dashboard.html", "login.html", "register.html"]:
        continue

    with open(file, "r", encoding="utf-8") as f:
        html = f.read()

    # Remove all favicon links
    html = re.sub(r'<link[^>]*rel=["\']icon["\'][^>]*>', '', html, flags=re.IGNORECASE)
    html = re.sub(r'<link[^>]*rel=["\']apple-touch-icon["\'][^>]*>', '', html, flags=re.IGNORECASE)
    html = re.sub(r'<meta[^>]*name=["\']msapplication-TileImage["\'][^>]*>', '', html, flags=re.IGNORECASE)
    
    # Also, if they meant "white" horilla logo text we injected earlier, let's remove it and let the CSS handle it, or just remove the fake span logo entirely.
    # The user said "remove the vite of horilla logo". Let's remove the white span we injected.
    html = re.sub(r'<span style="font-size: 2rem; font-weight: bold; color: #fff;">Diverse</span>', '', html)
    html = re.sub(r'<span style="font-size: 2rem; font-weight: bold; color: #000;">Diverse</span>', '', html)

    with open(file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Removed favicons and text logos from {file}")

print("Done!")
