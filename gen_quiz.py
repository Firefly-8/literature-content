#!/usr/bin/env python3
"""Generate 500 literature quiz questions."""
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
                texts = [c["text"] for c in data.get("content", []) if c.get("type") == "text" and "text" in c]
                return "\n\n".join(texts) if texts else data.get("content", [{}])[0].get("text", "")
        except Exception as e:
            print(f"  Error: {e}")
            time.sleep(5)
    return None

def gen_quiz(level, topics, count):
    prompt = (
        "请生成" + str(count) + "道" + level + "文学常识题目，涵盖以下主题：" + "、".join(topics) + "。\n"
        "题型包括选择题、填空题、判断题。\n"
        "每题格式如下（JSON数组）：\n"
        '{"question":"题目内容","type":"choice|fill|judge",'
        '"options":["A.xx","B.xx","C.xx","D.xx"],'
        '"answer":"A 或 答案内容","explanation":"解析"}\n'
        "输出纯JSON数组，不要其他内容。"
    )
    text = call(prompt, max_tokens=4096)
    if not text:
        return None
    # Try to parse JSON
    try:
        # Find JSON array in text
        start = text.find("[")
        end = text.rfind("]") + 1
        if start >= 0 and end > start:
            return json.loads(text[start:end])
    except:
        pass
    return None

def save_quiz(level, questions):
    path = os.path.join(CONTENT_DIR, "quiz", "quiz-" + level + ".json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"  Saved {len(questions)} questions to quiz-{level}.json")

def main():
    # Primary: 150 questions
    q = gen_quiz("primary",
        ["唐诗宋词","成语故事","古代作家","小学必背古诗","四大名著基础","寓言故事","神话传说"],
        150)
    if q:
        save_quiz("primary", q)
    else:
        print("  primary FAILED")

    # Middle: 200 questions
    q = gen_quiz("middle",
        ["唐宋八大家","古诗词赏析","文言文","古代文学流派","名著导读","修辞手法","作家作品"],
        200)
    if q:
        save_quiz("middle", q)
    else:
        print("  middle FAILED")

    # High: 150 questions
    q = gen_quiz("high",
        ["先秦诸子","楚辞汉赋","魏晋文学","唐诗","宋词","元曲","明清小说","现代文学","外国文学"],
        150)
    if q:
        save_quiz("high", q)
    else:
        print("  high FAILED")

if __name__ == "__main__":
    main()
