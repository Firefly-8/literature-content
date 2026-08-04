#!/usr/bin/env python3
"""Generate 500 quiz questions in batches."""
import json, os, time, requests, re

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

def parse_json(text):
    if not text:
        return None
    # Remove code fences
    text = re.sub(r'^```json?\s*', '', text.strip())
    text = re.sub(r'\s*```$', '', text.strip())
    # Find JSON array
    match = re.search(r'\[.*\]', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except:
            pass
    try:
        return json.loads(text)
    except:
        pass
    return None

def gen_batch(level, topics, count, batch_num):
    prompt = (
        "生成" + str(count) + "道" + level + "文学常识题，主题：" + "、".join(topics) + "。"
        "题型包括选择题、填空题、判断题。"
        "以JSON数组输出，每题：{\"question\":\"题干\",\"type\":\"choice|fill|judge\","
        "\"options\":[\"A.x\",\"B.x\",\"C.x\",\"D.x\"],\"answer\":\"A\",\"explanation\":\"解析\"}"
        "只输出JSON数组。"
    )
    print(f"  Batch {batch_num} ({count} questions)...", end=" ", flush=True)
    text = call(prompt, max_tokens=4096)
    data = parse_json(text)
    if data:
        print(f"OK ({len(data)} questions)")
        return data
    print("FAILED")
    return []

def main():
    os.makedirs(os.path.join(CONTENT_DIR, "quiz"), exist_ok=True)

    # Primary: 150 questions in 3 batches of 50
    primary = []
    batches = [
        (["唐诗宋词","成语故事"], 50),
        (["古代作家","必背古诗"], 50),
        (["四大名著基础","寓言故事"], 50),
    ]
    for i, (topics, count) in enumerate(batches, 1):
        q = gen_batch("小学", topics, count, i)
        primary.extend(q)
    with open(os.path.join(CONTENT_DIR, "quiz", "quiz-primary.json"), "w") as f:
        json.dump(primary, f, ensure_ascii=False, indent=2)
    print(f"Primary total: {len(primary)}")

    # Middle: 200 questions in 4 batches
    middle = []
    batches = [
        (["唐宋八大家","古诗词赏析"], 50),
        (["文言文","古代文学流派"], 50),
        (["名著导读","修辞手法"], 50),
        (["作家作品","文学常识"], 50),
    ]
    for i, (topics, count) in enumerate(batches, 1):
        q = gen_batch("初中", topics, count, i)
        middle.extend(q)
    with open(os.path.join(CONTENT_DIR, "quiz", "quiz-middle.json"), "w") as f:
        json.dump(middle, f, ensure_ascii=False, indent=2)
    print(f"Middle total: {len(middle)}")

    # High: 150 questions in 3 batches
    high = []
    batches = [
        (["先秦诸子","楚辞汉赋","唐诗"], 50),
        (["宋词","元曲","明清小说"], 50),
        (["现代文学","外国文学"], 50),
    ]
    for i, (topics, count) in enumerate(batches, 1):
        q = gen_batch("高中", topics, count, i)
        high.extend(q)
    with open(os.path.join(CONTENT_DIR, "quiz", "quiz-high.json"), "w") as f:
        json.dump(high, f, ensure_ascii=False, indent=2)
    print(f"High total: {len(high)}")

    print(f"\nTotal: {len(primary) + len(middle) + len(high)} questions")

if __name__ == "__main__":
    main()
