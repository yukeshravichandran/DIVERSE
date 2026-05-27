import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

def replace_text(match):
    text = match.group(1)
    # Only replace in the text node
    text = text.replace("Horilla", "Diverse")
    text = text.replace("HORILLA", "DIVERSE")
    text = text.replace("horilla", "diverse")
    return f">{text}<"

# Match text between tags
new_html = re.sub(r'>([^<]+)<', replace_text, html)

# Explicitly replace <title> just in case
new_html = new_html.replace("<title>Horilla", "<title>Diverse")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("Branding replaced safely!")
