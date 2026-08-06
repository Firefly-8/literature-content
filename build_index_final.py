#!/usr/bin/env python3
"""Build final index.json with accurate counts. v2: adds modern + shorts."""
import os, json, glob, re

CONTENT_DIR = "/root/wx-study-helper/content"

def count_headings(path, level="###"):
    if not os.path.exists(path):
        return 0
    with open(path, "r", encoding="utf-8") as f:
        return sum(1 for line in f if line.startswith(level))

def parse_md_frontmatter(path):
    """Extract 文体/年代/主题 from first lines of modern/shorts files."""
    info = {"文体": "", "年代": "", "主题": "", "难度": "", "字数": ""}
    try:
        with open(path, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                if i > 15:  # only scan header
                    break
                m = re.match(r'\*\*(.+?)\*\*\s*[：:](.*)', line)
                if m:
                    key = m.group(1).strip()
                    val = m.group(2).strip()
                    if key in info:
                        info[key] = val
    except Exception:
        pass
    return info

def extract_title_author(path):
    """Extract title and author from # 《xxx》- 作者."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            first = f.readline().strip()
        m = re.match(r'^#\s*[《](.+?)[》]\s*[—\-]\s*(.+?)$', first)
        if m:
            return m.group(1).strip(), m.group(2).strip()
    except Exception:
        pass
    return "", ""

def classify_modern(path):
    """散文 vs 短篇小说 from filename or 文体 field."""
    info = parse_md_frontmatter(path)
    if info["文体"]:
        return info["文体"]
    return "散文" if "散文" in path else "短篇小说"

index = {
    "books": {"psychology": [], "economics": [], "philosophy": [], "life": [], "cultivation": []},
    "poems": {"primary": [], "middle": [], "high": []},
    "characters": {},
    "books_summary": [],
    "modern": [],
    "shorts": [],
    "quiz": {}
}

# Books
for cat in ["psychology", "economics", "philosophy", "life", "cultivation"]:
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

# Modern (现当代散文 + 短篇小说)
d = os.path.join(CONTENT_DIR, "modern")
if os.path.isdir(d):
    for f in sorted(glob.glob(os.path.join(d, "*.md"))):
        title, author = extract_title_author(f)
        meta = parse_md_frontmatter(f)
        index["modern"].append({
            "name": f"{title}-{author}" if title else os.path.basename(f).replace(".md", ""),
            "title": title,
            "author": author,
            "category": classify_modern(f),
            "era": meta["年代"],
            "theme": meta["主题"],
            "difficulty": meta["难度"],
            "file": "modern/" + os.path.basename(f),
            "size": os.path.getsize(f)
        })

# Shorts (外国经典短篇)
d = os.path.join(CONTENT_DIR, "shorts")
if os.path.isdir(d):
    for f in sorted(glob.glob(os.path.join(d, "*.md"))):
        title, author = extract_title_author(f)
        meta = parse_md_frontmatter(f)
        index["shorts"].append({
            "name": f"{title}-{author}" if title else os.path.basename(f).replace(".md", ""),
            "title": title,
            "author": author,
            "category": meta["文体"] or "短篇小说",
            "era": meta["年代"],
            "theme": meta["主题"],
            "difficulty": meta["难度"],
            "file": "shorts/" + os.path.basename(f),
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
    "total_modern": len(index["modern"]),
    "total_shorts": len(index["shorts"]),
    "total_quiz": total_quiz,
    "total_files": sum(len(v) for v in index["books"].values()) +
                  sum(len(v) for v in index["poems"].values()) +
                  len(index["characters"]) + len(index["books_summary"]) +
                  len(index["modern"]) + len(index["shorts"]) + len(index["quiz"]) +
                  2  # README, index.json
}
index["stats"] = stats

with open("/root/wx-study-helper/index.json", "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, indent=2)

print("Final index:")
print(json.dumps(stats, ensure_ascii=False, indent=2))
print(f"\nmodern samples: {index['modern'][:3]}")
print(f"shorts samples: {index['shorts'][:3]}")