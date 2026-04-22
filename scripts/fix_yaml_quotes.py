import os
import glob
import re

LAB_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAB_DIR = os.path.join(LAB_DIR, "laboratory")
files = glob.glob(os.path.join(LAB_DIR, "*.qmd"))

def fix_yaml():
    for fpath in files:
        if os.path.basename(fpath) == "index.qmd" or os.path.basename(fpath) == "laboratory-navigation.qmd":
            continue
            
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # Fix section-title
        new_content = re.sub(r'^section-title:\s*([^"\n].*?)$', r'section-title: "\1"', content, flags=re.MULTILINE)
        
        # In case `section-code` also needs quotes (e.g. section-code: A)
        new_content = re.sub(r'^section-code:\s*([^"\n].*?)$', r'section-code: "\1"', new_content, flags=re.MULTILINE)

        if new_content != content:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Fixed quotes in {os.path.basename(fpath)}")

if __name__ == "__main__":
    fix_yaml()
