import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

pricing_html = """
<!-- DIVERSE PRICING & FEATURES SECTION -->
<section id="diverse-pricing" class="elementor-section" style="padding: 80px 0; background-color: #0d47a1; color: #fff;">
    <div style="max-width: 1200px; margin: 0 auto; text-align: center; padding: 0 20px;">
        <h2 style="font-size: 3rem; margin-bottom: 20px; font-weight: bold; color: #fff;">Simple, Transparent Pricing</h2>
        <p style="font-size: 1.2rem; margin-bottom: 60px; color: #e0f2fe;">Get started with the world's most powerful open-source HRMS.</p>

        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 30px;">
            <!-- Free Tier -->
            <div style="background: rgba(255,255,255,0.1); border-radius: 12px; padding: 40px; width: 350px; text-align: left; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
                <h3 style="font-size: 2rem; margin-bottom: 15px; color: #fff;">Community</h3>
                <div style="font-size: 3rem; font-weight: bold; margin-bottom: 20px; color: #fff;">$0<span style="font-size: 1.2rem; font-weight: normal; color: #e0f2fe;">/forever</span></div>
                <p style="color: #e0f2fe; margin-bottom: 30px;">Perfect for small teams and developers.</p>
                <ul style="list-style: none; padding: 0; margin-bottom: 40px; color: #fff; line-height: 2;">
                    <li>✓ Core HR & Employees</li>
                    <li>✓ Basic Recruitment</li>
                    <li>✓ Community Support</li>
                    <li>✓ Self-Hosted</li>
                </ul>
                <a href="register.html" style="display: block; text-align: center; background: #fff; color: #0d47a1; padding: 15px; border-radius: 8px; font-weight: bold; text-decoration: none;">Get Started Free</a>
            </div>

            <!-- Enterprise Tier -->
            <div style="background: #ffffff; border-radius: 12px; padding: 40px; width: 350px; text-align: left; box-shadow: 0 10px 30px rgba(0,0,0,0.3); transform: scale(1.05);">
                <div style="background: #0d6efd; color: #fff; text-align: center; padding: 5px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; margin-bottom: 15px; width: 100px; display: inline-block;">RECOMMENDED</div>
                <h3 style="font-size: 2rem; margin-bottom: 15px; color: #0d47a1;">Enterprise</h3>
                <div style="font-size: 3rem; font-weight: bold; margin-bottom: 20px; color: #0d47a1;">$49<span style="font-size: 1.2rem; font-weight: normal; color: #666;">/user/mo</span></div>
                <p style="color: #666; margin-bottom: 30px;">For growing companies needing full power.</p>
                <ul style="list-style: none; padding: 0; margin-bottom: 40px; color: #333; line-height: 2;">
                    <li>✓ Everything in Community</li>
                    <li>✓ Advanced Payroll & Tax</li>
                    <li>✓ AI-Powered Recruitment</li>
                    <li>✓ 24/7 Priority Support</li>
                </ul>
                <a href="register.html" style="display: block; text-align: center; background: #0d6efd; color: #fff; padding: 15px; border-radius: 8px; font-weight: bold; text-decoration: none;">Start Free Trial</a>
            </div>
        </div>
    </div>
</section>
<!-- END DIVERSE PRICING -->
"""

if "DIVERSE PRICING & FEATURES SECTION" not in html:
    # Inject right before the footer
    html = re.sub(r'(<footer)', f'{pricing_html}\n\\1', html, count=1, flags=re.IGNORECASE)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Pricing section injected!")
else:
    print("Pricing section already exists!")
