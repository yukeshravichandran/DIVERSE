import os
import urllib.request
from urllib.parse import urljoin, urlparse
import re

BASE_URL = "https://www.horilla.com"
pages = [
    "/",
    "/features/",
    "/pricing/",
    "/contact-us/",
    "/blogs/",
    "/crm/",
    "/implementation/",
    "/videos/",
    "/web-stories/",
    "/locations/",
    "/docs/",
    "/crm-features/",
    "/what-is-horilla/",
    "/privacy-policy/",
    "/sitemap/"
]

def get_filename(url):
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if not path:
        return "index.html"
    return f"{path}.html".replace("/", "_")

def fetch_and_clean():
    for page in pages:
        url = urljoin(BASE_URL, page)
        filename = get_filename(url)
        print(f"Downloading {url} -> {filename}")
        
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as response:
                html = response.read().decode('utf-8')
            
            # Rewrite global navigation links to local files
            for p in pages:
                target_url = urljoin(BASE_URL, p)
                target_file = get_filename(target_url)
                html = html.replace(target_url, target_file)
            
            # Additional rewrite for relative and absolute paths that missed
            html = re.sub(r'href="https://www.horilla.com/?([^"]*)"', lambda m: 'href="' + (get_filename('https://www.horilla.com/' + m.group(1)) if m.group(1) else 'index.html') + '"', html)
            
            with open(filename, "w", encoding="utf-8") as f:
                f.write(html)
        except Exception as e:
            print(f"Failed {url}: {e}")

if __name__ == "__main__":
    fetch_and_clean()
    print("Clean restoration complete!")
