import os
import glob
import re

html_files = glob.glob("*.html")

for file in html_files:
    if file in ["dashboard.html", "login.html", "register.html"]:
        continue

    with open(file, "r", encoding="utf-8") as f:
        html = f.read()

    # Destroy the Owl Carousel so javascript stops ruining the grid
    html = re.sub(r'class="[^"]*owl-carousel[^"]*"', 'class="diverse-tiles-grid"', html)
    
    # Strip any inline styling that owl-carousel or Elementor injected
    html = re.sub(r'style="width:[^"]*"', '', html)
    html = re.sub(r'style="transform:[^"]*"', '', html)

    # Force the other list containers to use our grid class
    html = html.replace('class="hr-features__list"', 'class="diverse-tiles-grid"')
    html = html.replace('class="hrl-features-list"', 'class="diverse-tiles-grid"')
    html = html.replace('class="hrl-pricing-cards"', 'class="diverse-tiles-grid"')
    
    # Hide the slider navigation buttons which are now useless
    html = re.sub(r'<div class="hrl-owl-carousel-navigation">.*?</div>', '', html, flags=re.DOTALL)
    html = re.sub(r'<div class="hrl-owl-carousel-progress">.*?</div>', '', html, flags=re.DOTALL)

    # Update cache buster to v=4
    html = html.replace('diverse-tiles.css?v=3', 'diverse-tiles.css?v=4')
        
    with open(file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Shattered old layout and enforced diverse-tiles-grid in {file}")

print("Done destroying Horilla layouts!")
