import os

backend_dir = r"c:\Users\yukes\Documents\Diverse-Backend"

# Binary or compiled extensions to skip
skip_exts = {".pyc", ".png", ".jpg", ".jpeg", ".ico", ".pdf", ".sqlite3", ".zip", ".gif", ".woff", ".woff2", ".ttf", ".eot"}

def is_text_file(filename):
    ext = os.path.splitext(filename)[1].lower()
    if ext in skip_exts:
        return False
    # If no extension or unknown extension, check first few bytes
    try:
        with open(filename, 'tr') as check_file:
            check_file.read(1024)
            return True
    except:
        return False

print("Starting deep scrub of the backend...")

# 1. Replace text in files
files_modified = 0
for root, dirs, files in os.walk(backend_dir):
    # Skip .git directory entirely
    if '.git' in dirs:
        dirs.remove('.git')
    if 'venv' in dirs:
        dirs.remove('venv')

    for file in files:
        filepath = os.path.join(root, file)
        if is_text_file(filepath):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                if "Horilla" in content or "horilla" in content or "HORILLA" in content:
                    new_content = content.replace("Horilla", "Diverse")
                    new_content = new_content.replace("HORILLA", "DIVERSE")
                    new_content = new_content.replace("horilla", "diverse")
                    
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    files_modified += 1
            except Exception as e:
                pass # skip files that can't be read as utf-8

print(f"Replaced text in {files_modified} files.")

# 2. Rename files and directories (bottom-up traversal is crucial here)
renames = 0
for root, dirs, files in os.walk(backend_dir, topdown=False):
    # Rename files
    for file in files:
        if "horilla" in file.lower():
            old_path = os.path.join(root, file)
            new_name = file.replace("horilla", "diverse").replace("Horilla", "Diverse")
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)
            renames += 1
            
    # Rename directories
    for d in dirs:
        if "horilla" in d.lower():
            old_path = os.path.join(root, d)
            new_name = d.replace("horilla", "diverse").replace("Horilla", "Diverse")
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)
            renames += 1

print(f"Renamed {renames} files and folders.")
print("Backend rebranding complete!")
