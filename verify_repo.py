import requests

TOKEN = "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"
HEADERS = {
    "Authorization": "token " + TOKEN,
    "Accept": "application/vnd.github+json"
}

# Check repo
r = requests.get("https://api.github.com/repos/Firefly-8/literature-content",
                 headers=HEADERS, timeout=10)
print(f"Repo status: {r.status_code}")
if r.status_code == 200:
    data = r.json()
    print(f"Name: {data['full_name']}")
    print(f"Private: {data['private']}")
    print(f"Size: {data['size']} KB")

# Check file count via tree
r = requests.get("https://api.github.com/repos/Firefly-8/literature-content/git/trees/main?recursive=1",
                 headers=HEADERS, timeout=10)
print(f"\nTree status: {r.status_code}")
if r.status_code == 200:
    tree = r.json().get("tree", [])
    md_files = [t for t in tree if t["path"].endswith(".md")]
    print(f"Total .md files: {len(md_files)}")
    print(f"Total tree entries: {len(tree)}")
    # Show some paths
    for t in tree[:10]:
        print(f"  {t['path']}")
