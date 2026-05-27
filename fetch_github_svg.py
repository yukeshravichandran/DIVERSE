import urllib.request
import os

url = "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/github.svg"
dest_path = r"c:\Users\yukes\Documents\Agentic AI CRM\wp-content\themes\diverse-wp-theme-main\assets\images\brand\github-icon.svg"

print("Downloading pristine GitHub SVG...")
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    svg_data = response.read().decode('utf-8')

# The default SVG is usually black or unstyled, we need it to be white to match the button text
if '<svg ' in svg_data:
    svg_data = svg_data.replace('<svg ', '<svg fill="white" ')

with open(dest_path, 'w', encoding='utf-8') as f:
    f.write(svg_data)

print(f"Perfect white GitHub SVG icon saved to {dest_path}")
