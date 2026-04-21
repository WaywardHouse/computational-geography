# Scientific Computing Foundations: Chapter Outline

## Purpose
Bridge from "I've never written code" to "I can run Python, manage my environment, use Jupyter, and collaborate with git." Mandatory Part 1 section before readers choose Pathways A/B/C.

---

## Chapters

### 1. **Why Scientific Computing Matters**
By the end of this book, you'll run climate models, forecast floods, and analyze satellite images. None of that happens without a computer that knows how to compute. This chapter shows what becomes possible once you have the machinery set up, and why the technical foundation matters to geographers.

### 2. **Your First Python Script (No Installation Required)**
Write and run Python code right now, in your browser, without installing anything. We'll print text, do math, ask for input, and see what happens. This is just to get comfortable with the syntax and the idea that "code is instructions you write."

### 3. **How Your Computer Thinks: Files, Folders, and the Command Line**
Your computer stores everything in files and folders (directories). The command line is how you navigate them without clicking. Learn pwd, cd, ls, mkdir, and why this matters: when you run Python, it needs to know where your files are. We'll use the terminal (Windows PowerShell, Mac Terminal, Linux shell) interchangeably.

### 4. **Installing Python: Anaconda vs. Venv (Which One for You?)**
You have two main paths: Anaconda (heavier, all-in-one, easier for beginners) or venv (lightweight, built-in to Python, more control). We'll show both for Windows, Mac, and Linux, then help you choose. By the end, you'll have Python running on your machine and be able to verify it works.

### 5. **Virtual Environments: Why One Environment per Project**
Installing packages (like NumPy, matplotlib) can conflict if you're not careful. A virtual environment is like a sandbox: each project gets its own isolated Python installation with its own packages. This chapter teaches you to create, activate, and think about environments. You'll understand why it matters before you actually need it.

### 6. **Installing & Managing Packages (pip, conda, requirements.txt)**
Once you have an environment, you populate it with libraries (NumPy, SciPy, Matplotlib). We'll use pip (pip install numpy) and conda (conda install numpy) and explain when to use which. You'll also learn requirements.txt so you can share your setup with others.

### 7. **Jupyter Notebooks: Interactive Computing in Your Browser**
Jupyter lets you write Python in a notebook: cells of code that you run one at a time, see results immediately, and mix in text and visualizations. This is how you'll work through Pathways. We'll start a Jupyter server, write a simple notebook, and show why it's better than scripts for exploration and learning.

### 8. **Running Your Code: Scripts, Notebooks, and Debugging Basics**
Code lives in three forms: scripts (python my_script.py), notebooks (open Jupyter), and interactive mode (python on the command line). We'll run each, see what happens when code breaks, and learn to read error messages. "Why didn't that work?" becomes a puzzle you can solve.

### 9. **IDEs and Editors: VSCode, PyCharm, and When to Use Which**
If Jupyter is for exploration, an IDE (integrated development environment) is for building real projects. VSCode is free and lightweight; PyCharm is heavier but powerful. We'll compare them, show you how to run code in each, and let you pick your favorite.

### 10. **Git and Version Control: Tracking Your Work and Collaborating**
Git is version control: it tracks changes to your code so you can go back to old versions, collaborate with others, and not lose work. We'll clone a repository, make changes, commit them, and push to GitHub. By the end, you'll understand why researchers use it and how to use it yourself.

---

## Chapter Progression & Learning Arc

| Chapter | Key Concept | Outcome |
|---------|-------------|---------|
| 1 | **Motivation** | "I understand why I'm learning this" |
| 2 | **Syntax & experience** | "I've written and run Python code" |
| 3 | **File systems & navigation** | "I can find files and navigate folders from the command line" |
| 4 | **Installation** | "I have Python on my machine and verified it works" |
| 5 | **Isolation & management** | "I understand environments and why they matter" |
| 6 | **Dependencies** | "I can install and manage packages" |
| 7 | **Interactive workflow** | "I've used Jupyter and understand why it's good for exploration" |
| 8 | **Execution & debugging** | "I can run code, see errors, and understand what went wrong" |
| 9 | **Real projects** | "I know which tool (IDE) to use for different tasks" |
| 10 | **Collaboration & tracking** | "I can use git to track my work and collaborate" |

---

## Design Philosophy

1. **Hands-on first** — Write code before theory; understand why before learning how
2. **Cross-platform** — Every instruction works on Windows, Mac, and Linux
3. **No prerequisites** — Readers arrive here with no coding experience
4. **Bridge to pathways** — By Chapter 10, readers are ready for Pathway A (satellite analysis), B (modeling), or C (applications)
5. **Lean** — Each chapter ~20–30 min read + hands-on; focus on doing, not explaining every detail

---

## Implementation Notes

- **Chapter 2** should use a browser-based Python (repl.it or similar); no installation yet
- **Chapters 3–6** build incrementally: terminal → Python installation → environments → packages
- **Chapter 7** (Jupyter) is the first time readers use a Pathway-style workflow
- **Chapter 10** (git) introduces GitHub, which is needed for collaborative Vol II work
- All chapters include a "Verify Your Work" section: concrete steps to confirm you've set up correctly
- Each chapter ends with: "Now you're ready for [next chapter / one of the pathways]"

---

## Estimated Word Count & Time

| Chapter | Words | Reading | Hands-on | Total |
|---------|-------|---------|----------|-------|
| 1 | 1000 | 10 min | — | 10 min |
| 2 | 1500 | 15 min | 15 min | 30 min |
| 3 | 1200 | 15 min | 10 min | 25 min |
| 4 | 2000 | 20 min | 20 min | 40 min |
| 5 | 1500 | 15 min | 15 min | 30 min |
| 6 | 1500 | 15 min | 15 min | 30 min |
| 7 | 1800 | 15 min | 20 min | 35 min |
| 8 | 1500 | 15 min | 15 min | 30 min |
| 9 | 1200 | 10 min | 10 min | 20 min |
| 10 | 1800 | 15 min | 20 min | 35 min |
| **TOTAL** | **~16K** | **~2.5 hrs** | **~2.5 hrs** | **~5 hrs** |

Readers can complete Scientific Computing Foundations in a weekend or spread over 1–2 weeks.

