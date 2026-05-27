from bs4 import BeautifulSoup

file_path = r"c:\Users\yukes\Documents\Agentic AI CRM\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# 1. Inject Google Fonts (Outfit & Inter)
head = soup.find("head")
if head:
    fonts = soup.new_tag("link", rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Outfit:wght@500;700;800&display=swap")
    head.append(fonts)
    
    # Inject diverse-premium-ui.css
    premium_css = soup.new_tag("link", rel="stylesheet", href="diverse-premium-ui.css")
    head.append(premium_css)

# 2. Transform the Home Modules (The old alternating screenshot/text sections)
modules = soup.find_all("div", class_="hrl-home-modules")
for i, mod in enumerate(modules):
    mod['class'] = ['diverse-glass-panel', f'panel-variant-{i%2}']
    left = mod.find("div", class_="hrl-home-modules__left")
    right = mod.find("div", class_="hrl-home-modules__right")
    
    if left:
        left['class'] = ['diverse-panel-content']
        # Convert lists to floating glass cards
        features_ul = left.find("ul", class_="hrl-home-modules__features")
        if features_ul:
            features_ul['class'] = ['diverse-feature-cards']
            for li in features_ul.find_all("li"):
                li['class'] = ['diverse-card']
                title = li.find("h3")
                if title: title['class'] = ['diverse-card-title']
                desc = li.find("p")
                if desc: desc['class'] = ['diverse-card-desc']
                
    if right:
        right['class'] = ['diverse-panel-media']
        img = right.find("img")
        if img:
            img['class'] = ['diverse-media-img']

# 3. Transform the Feature Grid (The original 12 block tiles)
feature_grid = soup.find("div", class_="hr-feature-grid")
if feature_grid:
    feature_grid['class'] = ['diverse-masonry-grid']
    for item in feature_grid.find_all("div", class_="hr-feature-item"):
        item['class'] = ['diverse-masonry-item']
        link = item.find("a")
        if link: link['class'] = ['diverse-masonry-link']

# 4. Transform Hero Section
hero = soup.find("section", class_="hrl-hero")
if hero:
    hero['class'] = ['diverse-hero-section']
    title = hero.find("h1")
    if title: title['class'] = ['diverse-hero-title']
    lead = hero.find("p")
    if lead: lead['class'] = ['diverse-hero-lead']
    actions = hero.find("div", class_="hrl-heo__actions")
    if actions: actions['class'] = ['diverse-hero-actions']
    
    # Remove the standard screenshots in the hero to replace with CSS glowing orb background
    img_container = soup.find("div", class_="hrl-hero__lead-image-container")
    if img_container:
        img_container.decompose()

# 5. Transform Testimonials
testimonials = soup.find_all("div", class_="testimonial-card")
for t in testimonials:
    t['class'] = ['diverse-glass-testimonial']

# Save the transformed HTML
with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Successfully restructured index.html!")
