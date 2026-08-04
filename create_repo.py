import requests, json

TOKEN = "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"
HEADERS = {
    "Authorization": "token " + TOKEN,
    "Accept": "application/vnd.github+json",
    "Content-Type": "application/json"
}

r = requests.post("https://api.github.com/user/repos", headers=HEADERS, json={
    "name": "literature-content",
    "private": True,
    "description": "文学作品赏析内容资产"
}, timeout=30)

print("Status:", r.status_code)
print("Response:", r.text[:500])
