#!/usr/bin/env python3
"""
按年级细分古诗文件夹
- primary: 一年级5 / 二年级15 / 三年级15 / 四年级15 / 五年级15 / 六年级9 (共74)
- middle: 七年级25 / 八年级26 / 九年级26 (共77)
- high: 高一30 / 高二32 / 高三33 (共95)
"""
import os
import shutil
import re

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'content', 'poems')

# Grade definitions: (grade_name, count)
PRIMARY_GRADES = [
    ('一年级', 5),
    ('二年级', 15),
    ('三年级', 15),
    ('四年级', 15),
    ('五年级', 15),
    ('六年级', 9),
]

MIDDLE_GRADES = [
    ('七年级', 25),
    ('八年级', 26),
    ('九年级', 26),
]

HIGH_GRADES = [
    ('高一', 30),
    ('高二', 32),
    ('高三', 33),
]

def get_md_files(directory):
    """Get sorted list of .md files in directory"""
    files = [f for f in os.listdir(directory) if f.endswith('.md')]
    # Sort by numeric prefix
    def sort_key(f):
        m = re.match(r'^(\d+)', f)
        return int(m.group(1)) if m else 0
    return sorted(files, key=sort_key)

def classify_section(section_name, grades):
    section_dir = os.path.join(BASE, section_name)
    files = get_md_files(section_dir)
    print(f"\n=== {section_name} ({len(files)} 首) ===")

    # Create grade directories and move files
    idx = 0
    for grade_name, count in grades:
        grade_dir = os.path.join(section_dir, grade_name)
        os.makedirs(grade_dir, exist_ok=True)

        for i in range(count):
            if idx >= len(files):
                break
            src = os.path.join(section_dir, files[idx])
            dst = os.path.join(grade_dir, files[idx])
            shutil.move(src, dst)
            idx += 1
            print(f"  {files[idx-1]} → {grade_name}/")

    # Move any remaining files to last grade
    last_grade = grades[-1][0]
    while idx < len(files):
        src = os.path.join(section_dir, files[idx])
        dst = os.path.join(section_dir, last_grade, files[idx])
        shutil.move(src, dst)
        print(f"  {files[idx]} → {last_grade}/ (剩余)")
        idx += 1

def main():
    classify_section('primary', PRIMARY_GRADES)
    classify_section('middle', MIDDLE_GRADES)
    classify_section('high', HIGH_GRADES)
    print("\n✅ 年级分类完成")

if __name__ == '__main__':
    main()
