#!/usr/bin/env python3
"""Generate quiz - save raw output for debugging."""
import json, os, time, requests

API_URL = "https://api.longcat.chat/anthropic/v1/messages"
API_KEY = "ak_2Im54r5bp9cU62h03x3Qs9Xe3Cx2l"
HEADERS = {
    "Authorization": "Bearer " + API_KEY,
    "Content-Type": "application/json",
    "anthropic-version": "2023-06-01",
}
CONTENT_DIR = "/root/wx-study-helper/content"

def call(prompt, max_tokens=4096):
    for attempt in range(3):
        try:
            r = requests.post(API_URL, headers=HEADERS, json={
                "model": "LongCat-2.0",
                "max_tokens": max_tokens,
                "messages": [{"role": "user", "content": prompt}]
            }, timeout=300)
            if r.status_code == 200:
                data = r.json()
                parts = []
                for c in data.get("content", []):
                    if c.get("type") == "text" and c.get("text"):
                        parts.append(c["text"])
                return "".join(parts)
        except Exception as e:
            print(f"  Error: {e}")
            time.sleep(5)
    return None

def save_raw(text, fname):
    with open(os.path.join(CONTENT_DIR, "quiz", fname), "w", encoding="utf-8") as f:
        f.write(text)

def main():
    # Try a small batch first
    prompt = "生成10道小学文学常识选择题。输出JSON数组格式：[{\"question\":\"题干\",\"type\":\"choice\",\"options\":[\"A.x\",\"B.x\",\"C.x\",\"D.x\"],\"answer\":\"A\",\"explanation\":\"解析\"}]。只输出JSON。"
    text = call(prompt, max_tokens=2000)
    if text:
        print("Raw output (first 500 chars):")
        print(repr(text[:500]))
        save_raw(text, "quiz-raw.txt")
        # Try to find JSON
        import re
        # Find anything that looks like a JSON array
        matches = re.findall(r'\[.*\]', text, re.DOTALL)
        if matches:
            for m in matches:
                try:
                    data = json.loads(m)
                    print(f"Parsed {len(data)} questions!")
                    with open(os.path.join(CONTENT_DIR, "quiz", "quiz-primary.json"), "w") as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                    return
                except Exception as e:
                    print(f"JSON parse error: {e}")
        print("Could not parse JSON from output")
    else:
        print("API call failed")

if __name__ == "__main__":
    main()
