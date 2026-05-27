import re

with open("c:\\Users\\yukes\\Documents\\Agentic AI CRM\\style.css", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Root Variables
content = re.sub(r'--bg-dark:\s*#[0-9a-fA-F]+;', '--bg-dark: #f0f4f8;', content)
content = re.sub(r'--bg-panel:\s*rgba\([^)]+\);', '--bg-panel: #ffffff;', content)
content = re.sub(r'--bg-card:\s*rgba\([^)]+\);', '--bg-card: #ffffff;', content)
content = re.sub(r'--border-color:\s*rgba\([^)]+\);', '--border-color: #e2e8f0;', content)
content = re.sub(r'--text-main:\s*#[0-9a-fA-F]+;', '--text-main: #1e293b;', content)
content = re.sub(r'--text-muted:\s*#[0-9a-fA-F]+;', '--text-muted: #64748b;', content)
content = re.sub(r'--text-dim:\s*#[0-9a-fA-F]+;', '--text-dim: #94a3b8;', content)

# 2. Update Neon Colors to Horilla Solid Colors
content = re.sub(r'--neon-purple:\s*#[0-9a-fA-F]+;', '--neon-purple: #7c3aed;', content)
content = re.sub(r'--neon-purple-glow:\s*rgba\([^)]+\);', '--neon-purple-glow: rgba(124, 58, 237, 0.1);', content)
content = re.sub(r'--neon-green:\s*#[0-9a-fA-F]+;', '--neon-green: #10b981;', content)
content = re.sub(r'--neon-green-glow:\s*rgba\([^)]+\);', '--neon-green-glow: rgba(16, 185, 129, 0.1);', content)
content = re.sub(r'--neon-blue:\s*#[0-9a-fA-F]+;', '--neon-blue: #2563eb;', content) # Primary Horilla Blue
content = re.sub(r'--neon-blue-glow:\s*rgba\([^)]+\);', '--neon-blue-glow: rgba(37, 99, 235, 0.1);', content)
content = re.sub(r'--neon-amber:\s*#[0-9a-fA-F]+;', '--neon-amber: #f59e0b;', content)
content = re.sub(r'--neon-amber-glow:\s*rgba\([^)]+\);', '--neon-amber-glow: rgba(245, 158, 11, 0.1);', content)
content = re.sub(r'--neon-rose:\s*#[0-9a-fA-F]+;', '--neon-rose: #ef4444;', content)
content = re.sub(r'--neon-rose-glow:\s*rgba\([^)]+\);', '--neon-rose-glow: rgba(239, 68, 68, 0.1);', content)

content = re.sub(r'--shadow-glow:\s*[^;]+;', '--shadow-glow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);', content)

# 3. Body Background
content = re.sub(r'background-image:[\s\S]*?background-size:[^;]+;', '', content) # Remove dark radial gradients

# 4. Header
content = re.sub(r'background:\s*rgba\(7, 10, 19, 0\.8\);', 'background: #ffffff;', content)
content = re.sub(r'color:\s*white;', 'color: var(--text-main);', content)

# 5. Buttons
content = re.sub(r'background:\s*linear-gradient\([^)]+\);', 'background: var(--neon-blue);', content)
content = re.sub(r'color:\s*white;', 'color: #ffffff;', content)
content = re.sub(r'box-shadow:\s*0 4px 15px rgba\([^)]+\);', 'box-shadow: 0 2px 4px rgba(37, 99, 235, 0.2);', content)

# 6. Inputs & Selects
content = re.sub(r'background:\s*rgba\(7, 10, 19, [0-9.]+\);', 'background: #ffffff;', content)

# 7. Agent Status Bar
content = re.sub(r'background:\s*rgba\(15, 23, 42, 0\.4\);', 'background: #f8fafc;', content)

# 8. Logs Console (keep it slightly dark but not #04060b, maybe very light or standard dark terminal)
# We will make it a standard dark terminal for contrast
content = re.sub(r'background:\s*#04060b;', 'background: #1e293b;', content)

# 9. Modals
content = re.sub(r'background:\s*#0f172a;', 'background: #ffffff;', content)

# 10. Cards
content = re.sub(r'border-color:\s*rgba\(255,\s*255,\s*255,\s*0\.15\);', 'border-color: var(--neon-blue);', content)
content = re.sub(r'background:\s*rgba\(255,\s*255,\s*255,\s*0\.0[0-9]\);', 'background: #f1f5f9;', content)
content = re.sub(r'rgba\(255,\s*255,\s*255,\s*0\.05\)', '#e2e8f0', content)
content = re.sub(r'rgba\(255,\s*255,\s*255,\s*0\.1\)', '#cbd5e1', content)

with open("c:\\Users\\yukes\\Documents\\Agentic AI CRM\\style.css", "w", encoding="utf-8") as f:
    f.write(content)
