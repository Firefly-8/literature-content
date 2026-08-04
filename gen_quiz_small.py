#!/usr/bin/env python3
"""Generate quiz in small batches of 20."""
import json, os, time, requests, re

API_URL = "https://api.longcat.chat/anthropic/v1/messages"
API_KEY = "ak_2Im54r5bp9cU62h03x3Qs9Xe3Cx2l"
HEADERS = {
    "Authorization": "Bearer " + API_KEY,
    "Content-Type": "application/json",
    "anthropic-version": "2023-06-01",
}
CONTENT_DIR = "/root/wx-study-helper/content"

def call(prompt, max_tokens=3000):
    for attempt in range(3):
        try:
            r = requests.post(API_URL, headers=HEADERS, json={
                "model": "LongCat-2.0",
                "max_tokens": max_tokens,
                "messages": [{"role": "user", "content": prompt}]
            }, timeout=180)
            if r.status_code == 200:
                data = r.json()
                parts = []
                for c in data.get("content", []):
                    if c.get("type") == "text" and c.get("text"):
                        parts.append(c["text"])
                return "".join(parts)
        except Exception as e:
            print(f"  Error: {e}")
            time.sleep(3)
    return None

def parse_json(text):
    if not text:
        return None
    text = re.sub(r'^```json?\s*', '', text.strip())
    text = re.sub(r'\s*```$', '', text.strip())
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

def gen(level, topics, count):
    prompt = (
        "生成" + str(count) + "道" + level + "文学常识题，主题：" + "、".join(topics) + "。"
        "题型包括选择题、填空题、判断题。"
        "输出JSON数组：[{\"question\":\"题干\",\"type\":\"choice|fill|judge\","
        "\"options\":[\"A.x\",\"B.x\",\"C.x\",\"D.x\"],\"answer\":\"A\",\"explanation\":\"解析\"}]"
    )
    text = call(prompt, max_tokens=3000)
    return parse_json(text) or []

def main():
    os.makedirs(os.path.join(CONTENT_DIR, "quiz"), exist_ok=True)

    # Load existing primary
    primary_path = os.path.join(CONTENT_DIR, "quiz", "quiz-primary.json")
    primary = []
    if os.path.exists(primary_path):
        with open(primary_path) as f:
            primary = json.load(f)

    # Generate more primary in batches of 20
    topics_list = [
        ["唐诗宋词","成语故事"], ["古代作家","必背古诗"], ["四大名著","寓言故事"],
        ["神话传说","汉字基础"]
    ]
    for topics in topics_list:
        q = gen("小学", topics, 20)
        primary.extend(q)
        print(f"  primary +{len(q)} = {len(primary)}")
    with open(primary_path, "w") as f:
        json.dump(primary, f, ensure_ascii=False, indent=2)

    # Middle
    middle = []
    topics_list = [
        ["唐宋八大家","古诗词赏析"], ["文言文","文学流派"], ["名著","修辞"],
        ["作家作品","古代文化常识"]
    ]
    for topics in topics_list:
        q = gen("初中", topics, 20)
        middle.extend(q)
        print(f"  middle +{len(q)} = {len(middle)}")
    with open(os.path.join(CONTENT_DIR, "quiz", "quiz-middle.json"), "w") as f:
        json.dump(middle, f, ensure_ascii=False, indent=2)

    # High
    high = []
    topics_list = [
        ["先秦诸子","楚辞汉赋"], ["唐诗","宋词"], ["元曲","明清小说"],
        ["现代文学","外国文学"]
    ]
    for topics in topics_list:
        q = gen("高中", topics, 20)
        high.extend(q)
        print(f"  high +{len(q)} = {len(high)}")
    with open(os.path.join(CONTENT_DIR, "quiz", "quiz-high.json"), "w") as f:
        json.dump(high, f, ensure_ascii=False, indent=2)

    print(f"\nTotals: primary={len(primary)}, middle={len(middle)}, high={len(high)}, all={len(primary)+len(middle)+len(high)}")

if __name__ == "__main__":
    main()
