import os
import re

def remove_gtm_from_html(directory):
    count = 0
    # Regex to match GTM and gtag scripts
    gtm_pattern1 = re.compile(r'<!-- Google Tag Manager( \(noscript\))? -->.*?<!-- End Google Tag Manager( \(noscript\))? -->', re.DOTALL | re.IGNORECASE)
    gtm_pattern2 = re.compile(r'<script.*?>.*?gtm\.start.*?gtm\.js.*?googletagmanager\.com/gtm\.js.*?</script>', re.DOTALL | re.IGNORECASE)
    gtm_pattern3 = re.compile(r'<script.*?>.*?loadGTM.*?GTM-[A-Z0-9]+.*?</script>', re.DOTALL | re.IGNORECASE)
    gtag_pattern = re.compile(r'<!-- Google tag \(gtag\.js\).*?-->.*?<script.*?>.*?gtag\(\).*?</script>', re.DOTALL | re.IGNORECASE)
    gtag_pattern2 = re.compile(r'<script[^>]*src=["\']https://www\.googletagmanager\.com/gtag/js[^>]*></script>\s*<script[^>]*>.*?dataLayer\.push.*?gtag\(.*?</script>', re.DOTALL | re.IGNORECASE)
    
    # Catch any generic script containing GTM-
    gtm_catchall = re.compile(r'<script[^>]*>.*?GTM-[A-Z0-9]+.*?</script>', re.DOTALL | re.IGNORECASE)
    
    # Noscript tag catchall
    noscript_gtm = re.compile(r'<noscript><iframe src="https://www\.googletagmanager\.com/ns\.html\?id=GTM-[A-Z0-9]+".*?</iframe></noscript>', re.DOTALL | re.IGNORECASE)

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    original_content = content
                    content = gtm_pattern1.sub('', content)
                    content = gtm_pattern2.sub('', content)
                    content = gtm_pattern3.sub('', content)
                    content = gtag_pattern.sub('', content)
                    content = gtag_pattern2.sub('', content)
                    content = gtm_catchall.sub('', content)
                    content = noscript_gtm.sub('', content)
                    
                    if content != original_content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
                        count += 1
                        print(f"Removed GTM/Gtag from: {filepath}")
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")
    print(f"Done! Modified {count} files.")

if __name__ == "__main__":
    remove_gtm_from_html(r"c:\Users\yukes\Documents\Agentic AI CRM")
