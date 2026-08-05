#!/usr/bin/env python3
"""重生成 index.json 中的 poems 字段，路径含年级"""
import os
import json

ROOT = "/root/wx-study-helper"
POEMS = f"{ROOT}/content/poems"

with open(f"{ROOT}/index.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

# 清空旧 poems，重建
data['poems'] = {}
total = 0
for stage in ['primary', 'middle', 'high']:
    data['poems'][stage] = []
    stage_dir = f"{POEMS}/{stage}"
    for grade in sorted(os.listdir(stage_dir)):
        grade_dir = f"{stage_dir}/{grade}"
        if not os.path.isdir(grade_dir):
            continue
        for fn in sorted(os.listdir(grade_dir)):
            if not fn.endswith('.md'):
                continue
            # 提取标题（去编号和.md）
            title = fn.replace('.md', '').lstrip('0123456789-').strip()
            data['poems'][stage].append({
                'name': title,
                'grade': grade,
                'file': f"poems/{stage}/{grade}/{fn}",
                'size': os.path.getsize(f"{grade_dir}/{fn}")
            })
            total += 1

with open(f"{ROOT}/index.json", 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 更新统计
data['stats']['total_poems'] = total
with open(f"{ROOT}/index.json", 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"重建 poems 完成: {total} 首")
for stage in ['primary', 'middle', 'high']:
    print(f"  {stage}: {len(data['poems'][stage])} 首")