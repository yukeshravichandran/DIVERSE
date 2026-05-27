import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace any link that goes to the demo site (which is the login for Horilla)
html = html.replace('href="https://demo.horilla.com"', 'href="login.html"')
html = html.replace('href="https://demo.horilla.com/"', 'href="login.html"')

# Also replace any login links specifically
html = re.sub(r'href="[^"]*/login/?([^"]*)"', 'href="login.html"', html, flags=re.IGNORECASE)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Links updated!")
