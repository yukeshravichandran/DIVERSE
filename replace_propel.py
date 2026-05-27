import re

files_to_update = [
    "c:\\Users\\yukes\\Documents\\Agentic AI CRM\\app.js",
    "c:\\Users\\yukes\\Documents\\Agentic AI CRM\\index.html"
]

for file_path in files_to_update:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace Propel with Horilla
    content = re.sub(r'Propel', 'Horilla', content)
    content = re.sub(r'propelhrms', 'horillahrms', content)
    content = re.sub(r'propel-hrms', 'horilla-hrms', content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
