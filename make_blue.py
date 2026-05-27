with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

blue_style = """
<style>
    /* Force deep blue background on all major sections */
    body, html, .hr-header, .hrl-hero-section, footer, .elementor-section, .elementor-widget-container, main, section {
        background-color: #0d47a1 !important; /* Dark professional blue */
        background-image: none !important;
        color: #ffffff !important;
    }
    
    /* Ensure all text is readable on the dark blue background */
    h1, h2, h3, h4, h5, h6, p, a, li, span {
        color: #ffffff !important;
    }

    /* Specifically target and hide any lingering image logos */
    img[src*="logo"] {
        display: none !important;
    }
</style>
</head>
"""

if "/* Force deep blue background on all major sections */" not in html:
    html = html.replace("</head>", blue_style)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Background set to blue!")
