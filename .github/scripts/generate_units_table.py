#!/usr/bin/env python3
"""
Generate a Units/Lessons table for the repo README.
It replaces content between <!-- UNITS START --> and <!-- UNITS END --> with a markdown table.

Usage: python .github/scripts/generate_units_table.py README.md
"""
from pathlib import Path
import sys


def scan_units(root: Path):
    units = []
    for unit_dir in sorted(root.glob('Unit-*')):
        if not unit_dir.is_dir():
            continue
        lessons = []
        for lesson_dir in sorted(unit_dir.glob('Lesson-*')):
            if not lesson_dir.is_dir():
                continue
            readme = lesson_dir / 'README.md'
            lessons.append((lesson_dir.name, readme.exists()))
        units.append((unit_dir.name, lessons))
    return units


def build_table(units):
    header = "| Unit | Lesson | Ready |\n|------|--------|:-----:|\n"
    rows = []
    for unit_name, lessons in units:
        if not lessons:
            rows.append(f'| {unit_name} | - | - |')
            continue
        for i, (lesson_name, exists) in enumerate(lessons):
            checkbox = '[x]' if exists else '[ ]'
            if i == 0:
                rows.append(f'| {unit_name} | {lesson_name} | {checkbox} |')
            else:
                rows.append(f'|  | {lesson_name} | {checkbox} |')
    return header + '\n'.join(rows) + '\n'


def replace_section(md_path: Path):
    text = md_path.read_text(encoding='utf-8')
    start = '<!-- UNITS START -->'
    end = '<!-- UNITS END -->'
    if start not in text or end not in text:
        print('Markers not found')
        return 1
    before, rest = text.split(start, 1)
    _, after = rest.split(end, 1)
    units = scan_units(md_path.parent)
    table = build_table(units)
    new_text = before + start + '\n' + table + '\n' + end + after
    if new_text != text:
        md_path.write_text(new_text, encoding='utf-8')
        print('Updated units table')
        return 0
    else:
        print('No changes needed')
        return 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: generate_units_table.py README.md')
        sys.exit(1)
    path = Path(sys.argv[1])
    sys.exit(replace_section(path))
