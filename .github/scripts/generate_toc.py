#!/usr/bin/env python3
"""
Simple TOC generator for README.md.
It replaces the content between <!-- TOC START --> and <!-- TOC END --> with a generated
Table of Contents based on Markdown headings (levels 2 and 3).

Usage: python .github/scripts/generate_toc.py README.md
"""
import re
import sys
from pathlib import Path


def slugify(text):
    # create a GitHub-style anchor slug
    slug = text.strip().lower()
    slug = re.sub(r"[^a-z0-9 \-]", "", slug)
    slug = re.sub(r"\s+", "-", slug)
    return slug


def build_toc(md_text):
    lines = md_text.splitlines()
    toc_lines = []
    for line in lines:
        if line.startswith("## "):
            title = line.lstrip('# ').strip()
            anchor = slugify(title)
            toc_lines.append(f"- [{title}](#{anchor})")
        elif line.startswith("### "):
            title = line.lstrip('# ').strip()
            anchor = slugify(title)
            toc_lines.append(f"  - [{title}](#{anchor})")
    return "\n".join(toc_lines)


def replace_toc(md_path: Path):
    text = md_path.read_text(encoding='utf-8')
    start_marker = '<!-- TOC START -->'
    end_marker = '<!-- TOC END -->'
    if start_marker not in text or end_marker not in text:
        print('TOC markers not found in', md_path)
        return 1
    before, rest = text.split(start_marker, 1)
    _, after = rest.split(end_marker, 1)
    toc = build_toc(text)
    new_text = before + start_marker + "\n" + toc + "\n" + end_marker + after
    if new_text != text:
        md_path.write_text(new_text, encoding='utf-8')
        print('Updated TOC in', md_path)
        return 0
    else:
        print('No changes needed')
        return 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: generate_toc.py README.md')
        sys.exit(1)
    path = Path(sys.argv[1])
    sys.exit(replace_toc(path))
