import re
import os

file_path = r"c:\Users\yukes\Documents\Agentic AI CRM\employee-management.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update title
content = content.replace("<title>Diverse - HR Features</title>", "<title>Diverse - Employee Management</title>")

# Update hero section
content = re.sub(
    r'<h1 class="hr-heading hrl-heading--h1 hrl-hero__title">Explore Our HR\s*<span\s*class="hrl-hero__highlight">\s*Features</span>\s*</h1>\s*<p class="hrl-hero__lead">\s*From hiring to offboarding, all features in one platform.\s*</p>',
    '''<h1 class="hr-heading hrl-heading--h1 hrl-hero__title">Explore <span class="hrl-hero__highlight">Employee Management</span> </h1>
            <p class="hrl-hero__lead">
            Store and manage all employee records securely in one centralized platform.
            </p>''',
    content,
    flags=re.IGNORECASE | re.MULTILINE | re.DOTALL
)

# Update features heading
content = content.replace("<h3> Our  Features</h3>", "<h3> Employee Management Features</h3>")

# Replace all the rows with our 3 features
features_html = """
          <div class="row">
            <div class="column">
                <div class="hrl-ft__content">
                  <div class="hrl-ft__content-head">
                    <img src="wp-content/themes/diverse-wp-theme-main/assets/images/feature/people-outline.png"
                       class="hrl-ft__icon" alt="Centralized Data">
                    <h2>Centralized Data</h2>
                  </div>
                  <p>Store and manage all employee records securely in one place, from personal details to job history and documents.</p>
                </div>
            </div>

            <div class="column">
                <div class="hrl-ft__content">
                  <div class="hrl-ft__content-head">
                    <img src="wp-content/themes/diverse-wp-theme-main/assets/images/feature/checkmark-circle-outline.png"
                      class="hrl-ft__icon" alt="Access Control">
                    <h2>Role-Based Access</h2>
                  </div>
                  <p>Ensure data privacy and security by defining specific access levels for different roles within your organization.</p>
                </div>
            </div>

            <div class="column">
                <div class="hrl-ft__content">
                  <div class="hrl-ft__content-head">
                  <img src="wp-content/themes/diverse-wp-theme-main/assets/images/feature/laptop-outline.png"
                    class="hrl-ft__icon" alt="Self-Service Portal">
                  <h2>Self-Service</h2>
                </div>
                  <p>Empower employees to update their own profiles, request time off, and access payslips.</p>
                </div>
            </div>
          </div>
"""

# Find the start of the first row and the end of the last row
start_pattern = r'<div class="row">'
end_pattern = r'<!-- End of features -->' # wait, there is no end comment. 
# It ends right before: </div>\s*</div>\s*</section>

# Let's use regex to replace everything between <div class="row"> and </div>\s*</div>\s*</section>
content = re.sub(
    r'(<div class="row">.*?)</div>\s*</div>\s*</section>',
    features_html + '\n        </div>\n      </div>\n    </section>',
    content,
    flags=re.IGNORECASE | re.DOTALL
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated employee-management.html")
