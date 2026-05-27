import urllib.request
import re

url = "https://www.horilla.com/"
output_path = "c:\\Users\\yukes\\Documents\\Agentic AI CRM\\index.html"

print("Fetching https://www.horilla.com/ ...")
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    html = response.read().decode('utf-8')

print("Rewriting relative paths to absolute URLs...")
# Replace href="/..." with href="https://www.horilla.com/..."
html = re.sub(r'href="/(?!/)', 'href="https://www.horilla.com/', html)
# Replace src="/..." with src="https://www.horilla.com/..."
html = re.sub(r'src="/(?!/)', 'src="https://www.horilla.com/', html)
# Replace url(/...) with url(https://www.horilla.com/...)
html = re.sub(r'url\("/(?!/)', 'url("https://www.horilla.com/', html)
html = re.sub(r"url\('/(?!/)", "url('https://www.horilla.com/", html)

# Some wordpress assets use wp-content directly without a leading slash
html = html.replace('href="wp-content/', 'href="https://www.horilla.com/wp-content/')
html = html.replace('src="wp-content/', 'src="https://www.horilla.com/wp-content/')

with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Saved to index.html successfully.")
