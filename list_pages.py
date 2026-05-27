import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

urls = re.findall(r'href="https://www.horilla.com/([^/"]+)/?"', html)
unique_pages = set(urls)

# filter out common static paths like wp-content
pages = [p for p in unique_pages if not p.startswith('wp-') and not '.' in p]
print("Pages to clone:", pages)
