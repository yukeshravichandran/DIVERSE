import glob
import re

html_files = glob.glob("*.html")

for file in html_files:
    if file in ["dashboard.html", "login.html", "register.html"]:
        continue

    with open(file, "r", encoding="utf-8") as f:
        html = f.read()

    # The banner starts with <div class="hr-banner-wrapper"> and ends with a matching </div>
    # Using regex to remove this block. We'll search for the wrapper and remove it.
    html = re.sub(r'<div class="hr-banner-wrapper">.*?</div>\s*</div>', '', html, flags=re.DOTALL)
    
    # Just in case the regex misses due to nesting, let's also add it to CSS
    if 'href="diverse-premium.css"' in html:
        pass

    with open(file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Removed banner from {file}")

# Let's also forcefully hide it in CSS
with open("diverse-premium.css", "a", encoding="utf-8") as f:
    f.write("\n/* Hide the App Download Banner */\n.hr-banner-wrapper, #ad-banner { display: none !important; }\n")

print("Banner successfully removed!")
