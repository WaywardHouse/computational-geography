import os
import glob
import re

LAB_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAB_DIR = os.path.join(LAB_DIR, "laboratory")
QMD_FILES = glob.glob(os.path.join(LAB_DIR, "*.qmd"))

def process_file(filepath):
    if os.path.basename(filepath) in ["index.qmd", "laboratory-navigation.qmd"]:
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    fm_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not fm_match: return
    
    fm_text = fm_match.group(1)
    body = content[fm_match.end():]

    if "## Before You Start This Investigation" in body:
        return
        
    prereqs = []
    m_prereq = re.search(r'^pathway-prerequisites:\n((?:\s+-\s+[^\n]+(?:\n|$))+)', fm_text, re.MULTILINE)
    if m_prereq:
        for line in m_prereq.group(1).split('\n'):
            if '-' in line:
                val = re.sub(r'^\s+-\s+"?(.*?)"?$', r'\1', line).strip()
                if val: prereqs.append(val)
                
    if not prereqs: return
    
    est = re.search(r'^est-hours:\s*(.+)$', fm_text, re.MULTILINE)
    est_val = est.group(1).strip() if est else "?"
    
    bw = re.search(r'^backward-link:\s*"([^"]+)"', fm_text, re.MULTILINE)
    bw_val = bw.group(1).strip() if bw else ""

    # Extract existing subfields
    m_learn = re.search(r'\*\*You will learn.*?\*\*\s*\n(.*?)(?=\n\n\*\*|\n\n\n|\n\n[^\*\s])', body, re.DOTALL)
    learn_val = m_learn.group(1).strip() if m_learn else ""
    if learn_val and not learn_val.startswith('-'): learn_val = "- " + learn_val
    
    m_matters = re.search(r'\*\*Why this matters.*?\*\*\s*\n(.*?)(?=\n\n\*\*|\n\n\n|\n\n[^\*\s])', body, re.DOTALL)
    matters_val = m_matters.group(1).strip() if m_matters else ""
    
    m_hard = re.search(r'\*\*If this gets hard.*?\*\*\s*\n(.*?)(?=\n\n\*\*|\n\n\n|\n\n[^\*\s])', body, re.DOTALL | re.IGNORECASE)
    hard_val = m_hard.group(1).strip() if m_hard else ""

    # Delete the old block including headers
    body_cleaned = re.sub(r'^## Before You Start\b.*?\n(?=\n{2,}[A-Za-z])', '', body, count=1, flags=re.DOTALL | re.MULTILINE)
    body_cleaned = body_cleaned.lstrip()

    # Build the new block
    new_block = "## Before You Start This Investigation\n\n**You should have completed:**\n"
    for p in prereqs:
        new_block += f"- {p}\n"
    if learn_val:
        new_block += f"\n**You will learn:**\n{learn_val}\n"
    else:
        new_block += "\n**You will learn:**\n- Specific outcomes outlined in the investigation.\n"
        
    new_block += f"\n**Estimated time:** {est_val} hours\n"
    if bw_val:
        new_block += f"\n**See also:** {bw_val}\n"
        
    if matters_val:
        new_block += f"\n**Why this matters:**\n{matters_val}\n"
    if hard_val:
        new_block += f"\n**If this gets hard, focus on:**\n{hard_val}\n"
        
    # Find insertion point
    # We look for a line starting with `## 1.` or `## ` or `---` followed by `## `
    m_header = re.search(r'\n(?:---[ \t]*\n)?## \d?\.', "\n" + body_cleaned)
    if m_header:
        insert_pos = m_header.start()
        # The intro is before insert_pos
        intro = body_cleaned[:insert_pos].strip()
        rest = body_cleaned[insert_pos:].strip()
        final_body = intro + "\n\n" + new_block + "\n\n" + rest + "\n"
    else:
        final_body = new_block + "\n\n" + body_cleaned

    final_content = f"---\n{fm_text}\n---\n\n{final_body}"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print(f"Updated {os.path.basename(filepath)}")

for f in QMD_FILES:
    process_file(f)
