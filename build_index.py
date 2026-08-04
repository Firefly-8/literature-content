#!/usr/bin/env python3
"""Build index.json from all content files."""
import os, json, glob

CONTENT_DIR = "/root/wx-study-helper/content"
index = {
    "books": {"psychology": [], "economics": [], "philosophy": []},
    "poems": {"primary": [], "middle": [], "high": []},
    "characters": [],
    "books_summary": [],
    "quiz": []
}

# Books
for cat in ["psychology", "economics", "philosophy"]:
    d = os.path.join(CONTENT_DIR, "books", cat)
    if os.path.isdir(d):
        for f in sorted(glob.glob(os.path.join(d, "*.md"))):
            name = os.path.basename(f).replace(".md", "")
            index["books"][cat].append({
                "name": name,
                "file": f"books/{cat}/{os.path.basename(f)}",
                "size": os.path.getsize(f)
            })

# Poems
for level in ["primary", "middle", "high"]:
    d = os.path.join(CONTENT_DIR, "poems", level)
    if os.path.isdir(d):
        for f in sorted(glob.glob(os.path.join(d, "*.md"))):
            name = os.path.basename(f).replace(".md", "")
            index["poems"][level].append({
                "name": name,
                "file": f"poems/{level}/{os.path.basename(f)}",
                "size": os.path.getsize(f)
            })

# Characters
d = os.path.join(CONTENT_DIR, "characters")
if os.path.isdir(d):
    for f in sorted(glob.glob(os.path.join(d, "*.md"))):
        index["characters"].append({
            "name": os.path.basename(f).replace(".md", ""),
            "file": f"characters/{os.path.basename(f)}",
            "size": os.path.getsize(f)
        })

# Books summary
d = os.path.join(CONTENT_DIR, "books-summary")
if os.path.isdir(d):
    for f in sorted(glob.glob(os.path.join(d, "*.md"))):
        index["books_summary"].append({
            "name": os.path.basename(f).replace(".md", ""),
            "file": f"books-summary/{os.path.basename(f)}",
            "size": os.path.getsize(f)
        })

# Quiz
d = os.path.join(CONTENT_DIR, "quiz")
if os.path.isdir(d):
    for f in sorted(glob.glob(os.path.join(d, "*.json"))):
        index["quiz"].append({
            "name": os.path.basename(f),
            "file": f"quiz/{os.path.basename(f)}",
            "size": os.path.getsize(f)
        })

# Stats
stats = {
    "total_books": sum(len(v) for v in index["books"].values()),
    "total_poems": sum(len(v) for v in index["poems"].values()),
    "total_characters": len(index["characters"]),
    "total_books_summary": len(index["books_summary"]),
    "total_quiz": len(index["quiz"]),
}
index["stats"] = stats

with open("/root/wx-study-helper/index.json", "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, indent=2)

print(f"Index built: {json.dumps(stats, ensure_ascii=False)}")
