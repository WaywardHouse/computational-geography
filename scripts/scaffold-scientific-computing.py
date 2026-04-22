import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET_DIR = os.path.join(ROOT_DIR, "scientific-computing")

if not os.path.exists(TARGET_DIR):
    os.makedirs(TARGET_DIR)

files_and_titles = {
    "index.qmd": "Scientific Computing Foundations",
    "why-scientific-computing-matters.qmd": "Why Scientific Computing Matters",
    "your-first-python-script.qmd": "Your First Python Script",
    "command-line-essentials.qmd": "How Your Computer Thinks: Command Line Essentials",
    "installing-python.qmd": "Installing Python: Anaconda vs. Venv",
    "virtual-environments.qmd": "Virtual Environments: Why One Environment per Project",
    "package-management.qmd": "Installing & Managing Packages (pip, conda, requirements.txt)",
    "your-first-jupyter-notebook.qmd": "Jupyter Notebooks: Interactive Computing in Your Browser",
    "running-and-debugging-code.qmd": "Running Your Code: Scripts, Notebooks, and Debugging Basics",
    "ides-and-editors.qmd": "IDEs and Editors: VSCode, PyCharm, and When to Use Which",
    "git-and-version-control.qmd": "Git and Version Control: Tracking Your Work and Collaborating"
}

scaffold_template = """---
title: "{title}"
type: chapter
book-part: "scientific-computing"
---

## Before You Start

**You should know:**
- Placeholders for prerequisites

**You will learn:**
- Placeholder for outcomes

## Introduction

This chapter will be fully drafted soon.

## Verify Your Work

- Make sure you check this section.

## Next Steps

Ready for the next concept!
"""

index_template = """---
title: "{title}"
type: chapter
book-part: "scientific-computing"
---

# Introduction to Scientific Computing

Welcome to the foundation of your computational environment!
"""

for fname, title in files_and_titles.items():
    fpath = os.path.join(TARGET_DIR, fname)
    if not os.path.exists(fpath):
        with open(fpath, "w", encoding="utf-8") as f:
            if fname == "index.qmd":
                 f.write(index_template.format(title=title))
            else:
                 f.write(scaffold_template.format(title=title))
        print(f"Scaffolded {fname}")
    else:
        print(f"Skipped {fname} (already exists)")
