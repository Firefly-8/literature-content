#!/usr/bin/env python3
"""Build final index.json with accurate counts."""
import os, json, glob, re

CONTENT_DIR = "/root/wx-study-helper/content"

def count_headings(path, level="###"):
    if not os.path.exists(path):
        return 0
    with open(path, "r", encoding="utf-8") as f:
        return sum(1 for line in f if line.startswith(level))

index = {
    "books": {"psychology": [], "economics": [], "philosophy": []},
    "poems": {"primary": [], "middle": [], "high": []},
    "characters": {},
    "books_summary": [],
    "quiz": {}
}

# Books
for cat in ["psychology", "economics", "philosophy"]:
    d = os.path.join(CONTENT_DIR, "books", cat)
    if os.path.isdir(d):
        for f in sorted(glob.glob(os.path.join(d, "*.md"))):
            name = os.path.basename(f).replace(".md", "")
            index["books"][cat].append({
                "name": name,
                "file": "books/" + cat + "/" + os.path.basename(f),
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
                "file": "poems/" + level + "/" + os.path.basename(f),
                "size": os.path.getsize(f)
            })

# Characters - count headings in each file
for fname in ["hongloumeng.md", "xiyouji.md", "sanguoyanyi.md", "shuihuzhuan.md"]:
    path = os.path.join(CONTENT_DIR, "characters", fname)
    novel = fname.replace(".md", "")
    count = count_headings(path)
    index["characters"][novel] = {
        "file": "characters/" + fname,
        "count": count,
        "size": os.path.getsize(path) if os.path.exists(path) else 0
    }

# Books summary
d = os.path.join(CONTENT_DIR, "books-summary")
if os.path.isdir(d):
    for f in sorted(glob.glob(os.path.join(d, "*.md"))):
        name = os.path.basename(f).replace(".md", "")
        index["books_summary"].append({
            "name": name,
            "file": "books-summary/" + os.path.basename(f),
            "size": os.path.getsize(f)
        })

# Quiz - count questions in each JSON
for level in ["primary", "middle", "high"]:
    path = os.path.join(CONTENT_DIR, "quiz", "quiz-" + level + ".json")
    if os.path.exists(path):
        with open(path) as f:
            questions = json.load(f)
        index["quiz"][level] = {
            "file": "quiz/quiz-" + level + ".json",
            "count": len(questions),
            "size": os.path.getsize(path)
        }

# Stats
total_chars = sum(v["count"] for v in index["characters"].values())
total_quiz = sum(v["count"] for v in index["quiz"].values())
stats = {
    "total_books": sum(len(v) for v in index["books"].values()),
    "total_poems": sum(len(v) for v in index["poems"].values()),
    "total_characters": total_chars,
    "total_books_summary": len(index["books_summary"]),
    "total_quiz": total_quiz,
    "total_files": sum(len(v) for v in index["books"].values()) +
                  sum(len(v) for v in index["poems"].values()) +
                  len(index["characters"]) + len(index["books_summary"]) + len(index["quiz"]) +
                  2  # README, index.json
}
index["stats"] = stats

with open("/root/wx-study-helper/index.json", "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, indent=2)

print("Final index:")
print(json.dumps(stats, ensure_ascii=False, indent=2))
