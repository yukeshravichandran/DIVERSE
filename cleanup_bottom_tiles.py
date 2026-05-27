from bs4 import BeautifulSoup

file_path = r"c:\Users\yukes\Documents\Agentic AI CRM\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# 1. Remove the "Experience Smart HR with Diverse Mobile App" section completely
app_container = soup.find("div", class_="hrl-home-app-container")
if app_container:
    # Find the parent section to remove
    app_section = app_container.find_parent("section")
    if app_section:
        app_section.decompose()
        print("Removed Mobile App section.")
    else:
        app_container.decompose()

# 2. Convert the "It's Free, It's Open Source" and "For queries contact" sections to the Diverse Glass Panel layout
old_heroes = soup.find_all("section", class_="hrl-hero")
for hero in old_heroes:
    # We already converted the main top hero to `diverse-hero-section`, so anything still named `hrl-hero` is the old bottom tiles
    
    # Check if it has a heading 3
    h3 = hero.find("h3")
    if h3:
        # Convert to a glass panel CTA
        hero['class'] = ['diverse-glass-panel', 'diverse-cta-panel']
        
        # Remove any stray images from horilla in these sections
        img_container = hero.find("div", class_="hrl-hero__cta-image-container")
        if img_container:
            img_container.decompose()
            
        video_container = hero.find("div", class_="hrl-home-video-container")
        if video_container:
            video_container.decompose()

        # Update text classes
        h3['class'] = ['diverse-card-title']
        lead = hero.find("p", class_="hrl-hero__lead")
        if lead:
            lead['class'] = ['diverse-card-desc']
            
        actions = hero.find("div", class_="hrl-heo__actions")
        if actions:
            actions['class'] = ['diverse-hero-actions']

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Restructured remaining old Horilla tiles.")
