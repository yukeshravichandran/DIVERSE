import re
import os
import urllib.request
import urllib.error

# Pages found previously
PAGES = ['videos', 'docs', 'crm', 'sitemap', 'compare', 'contact-us', 'features', 'what-is-horilla', 'implementation', 'blogs', 'locations', 'crm-features', 'pricing', 'privacy-policy', 'web-stories', 'about']

base_url = "https://www.horilla.com"

# Rebrand function (merging aggressive_rebrand.py, make_blue.py, patch_logos.py logic)
def process_html(html):
    # 1. Text replacement
    html = html.replace("Horilla", "Diverse")
    html = html.replace("HORILLA", "DIVERSE")
    html = html.replace("horilla", "diverse")
    
    # Repair URLs that need to be intact for static assets
    html = html.replace("diverse.com", "horilla.com")
    html = html.replace("diverse-", "horilla-")
    html = html.replace("/diverse/", "/horilla/")
    html = html.replace("diverse_wp", "horilla_wp")
    html = html.replace("-diverse", "-horilla")
    html = html.replace("wp-content/themes/diverse", "wp-content/themes/horilla")

    # 2. Patch Logos (replace with text)
    html = re.sub(r'<img[^>]*class="[^"]*hr-header__logo[^"]*"[^>]*>', '<span style="font-size: 2rem; font-weight: bold; color: #fff;">Diverse</span>', html)
    html = re.sub(r'<img[^>]*class="[^"]*footer-widget__logo[^"]*"[^>]*>', '<span style="font-size: 2rem; font-weight: bold; color: #fff;">Diverse</span>', html)
    html = re.sub(r'<img[^>]*class="[^"]*hrl-footer__logo[^"]*"[^>]*>', '<span style="font-size: 2rem; font-weight: bold; color: #000;">Diverse</span>', html)
    html = re.sub(r'<img[^>]*src="[^"]*horilla-logo[^"]*"[^>]*>', '<span style="font-size: 2rem; font-weight: bold; color: #000;">Diverse</span>', html)
    html = re.sub(r'<link rel="shortcut icon"[^>]*>', '', html)

    # 3. Apply Blue Background
    blue_style = """
    <style>
        /* Force deep blue background on all major sections */
        body, html, .hr-header, .hrl-hero-section, footer, .elementor-section, .elementor-widget-container, main, section {
            background-color: #0d47a1 !important; /* Dark professional blue */
            background-image: none !important;
            color: #ffffff !important;
        }
        
        /* Ensure all text is readable on the dark blue background */
        h1, h2, h3, h4, h5, h6, p, a, li, span {
            color: #ffffff !important;
        }

        /* Specifically target and hide any lingering image logos */
        img[src*="logo"] {
            display: none !important;
        }
    </style>
    </head>
    """
    if "/* Force deep blue background" not in html:
        html = html.replace("</head>", blue_style)
        
    return html

def rewrite_links(html):
    # Change absolute links to Horilla subpages into local links
    # For example: href="https://www.horilla.com/features/" -> href="features.html"
    for page in PAGES:
        # Match https://www.horilla.com/page/ or https://www.horilla.com/page
        html = re.sub(rf'href=["\']https://www\.horilla\.com/{page}/?["\']', f'href="{page}.html"', html, flags=re.IGNORECASE)
        # In case the URL was already rebranded to diverse.com (which we reverted, but just in case)
        html = re.sub(rf'href=["\']https://www\.diverse\.com/{page}/?["\']', f'href="{page}.html"', html, flags=re.IGNORECASE)
        # Match relative links like href="/features/"
        html = re.sub(rf'href=["\']/{page}/?["\']', f'href="{page}.html"', html, flags=re.IGNORECASE)
    
    # Redirect root links back to index.html
    html = re.sub(r'href=["\']https://www\.horilla\.com/?["\']', 'href="index.html"', html, flags=re.IGNORECASE)
    html = re.sub(r'href=["\']/?["\']', 'href="index.html"', html)
    
    return html

print("Starting Deep Site Clone...")

# Download and process subpages
for page in PAGES:
    url = f"{base_url}/{page}/"
    try:
        print(f"Downloading {page}...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        page_html = response.read().decode('utf-8')
        
        # Apply logic
        page_html = process_html(page_html)
        page_html = rewrite_links(page_html)
        
        # Save locally
        with open(f"{page}.html", "w", encoding="utf-8") as f:
            f.write(page_html)
    except Exception as e:
        print(f"Failed to download {page}: {e}")

# Process existing index.html to rewrite its links too
print("Rewriting links in index.html...")
if os.path.exists("index.html"):
    with open("index.html", "r", encoding="utf-8") as f:
        idx_html = f.read()
    
    # We already ran process_html on index.html historically, just need to rewrite links
    idx_html = rewrite_links(idx_html)
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(idx_html)

print("Deep clone and link rewrite complete!")
