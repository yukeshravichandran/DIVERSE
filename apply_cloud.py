import glob
import re

html_files = glob.glob("*.html")

for file in html_files:
    if file in ["dashboard.html", "login.html", "register.html"]:
        continue

    with open(file, "r", encoding="utf-8") as f:
        html = f.read()

    # Switch CSS from premium to cloud
    html = html.replace('href="diverse-premium.css"', 'href="diverse-cloud.css"')
    if 'href="diverse-cloud.css"' not in html:
        html = html.replace('</head>', '\n    <link rel="stylesheet" href="diverse-cloud.css">\n</head>')

    # Inject Logo into Header and Footer
    logo_img = '<img src="diverse-logo.png" class="diverse-custom-logo" alt="Diverse">'
    
    # We find the links containing the original logos and prepend our custom logo.
    # The CSS already hides the original ones.
    if 'diverse-custom-logo' not in html:
        html = html.replace('<a class="navbar-brand hr-header__logo" href="index.html">', '<a class="navbar-brand hr-header__logo" href="index.html">' + logo_img)
        html = html.replace('<a href="index.html" class="footer-widget__logo">', '<a href="index.html" class="footer-widget__logo">' + logo_img)

    # Specific Homepage changes
    if file == "index.html":
        # 1. Change Hero Text
        html = re.sub(r'Empower Your HR Team with <span\s*class="hrl-hero__highlight">\s*Free\s*</span> Open Source Software', 
                      'The Future of <span class="hrl-hero__highlight">Diverse</span> HR Cloud Management', html)
        
        # Also just in case the formatting is slightly different:
        html = html.replace('Empower Your HR Team with <span\n                    class="hrl-hero__highlight"> Free</span> Open Source Software',
                            'The Future of <span class="hrl-hero__highlight">Diverse</span> HR Cloud Management')
        
        # 2. Replace the Mockup Images.
        # hrl-hero__lead-image-5 was diverse-home-dash-1.png (Chat widget with Nancy)
        html = re.sub(r'src="[^"]*diverse-home-dash-1\.png"', 'src="diverse-chat.png"', html)
        
        # Hide the other dashboard mockup image so the new chat mockup stands out cleanly
        html = re.sub(r'<img[^>]*diverse-home-dash-2\.png[^>]*>', '', html)
        
        # Hide the announcement icon
        # Looking for the announcement block. It usually has 'announcement' or 'megaphone' in it.
        # But wait, earlier I decided to hide all SVGs and icons via CSS:
        # svg, img[src$=".svg"], .hr-feature-item__icon-container { display: none !important; }
        # This globally hides the announcement icon! So no HTML change strictly needed for the icon.

    with open(file, "w", encoding="utf-8") as f:
        f.write(html)
        
    print(f"Applied Cloud Design to {file}")

print("Cloud Aesthetic successfully applied!")
