#!/usr/bin/env python3
"""Generate quiz with better JSON extraction."""
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
                # Get ALL text blocks concatenated
                parts = []
                for c in data.get("content", []):
                    if c.get("type") == "text" and c.get("text"):
                        parts.append(c["text"].strip())
                if parts:
                    return "\n".join(parts)
                return data.get("content", [{}])[0].get("text", "")
        except Exception as e:
            print(f"  Error: {e}")
            time.sleep(5)
    return None

def extract_json(text):
    """Extract JSON array from text, handling markdown code blocks."""
    if not text:
        return None
    # Remove markdown code fences
    text = text.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        # Remove first line (```json or ```) and last line (```)
        text = "\n".join(lines[1:-1] if lines[-1].strip() == "```" else lines[1:])
    # Find first [ and last ]
    start = text.find("[")
    end = text.rfind("]")
    if start >= 0 and end > start:
        try:
            return json.loads(text[start:end+1])
        except:
            pass
    # Try parsing the whole thing
    try:
        return json.loads(text)
    except:
        pass
    return None

def gen_quiz(level, topics, count):
    prompt = (
        "生成" + str(count) + "道" + level + "文学常识题，主题：" + "、".join(topics) + "。\n"
        "包含选择题、填空题、判断题。\n"
        "以JSON数组输出，每题格式：\n"
        "{\"question\":\"题干\",\"type\":\"choice|fill|judge\","
        "\"options\":[\"A.内容\",\"B.内容\",\"C.内容\",\"D.内容\"],"
        "\"answer\":\"A\",\"explanation\":\"解析\"}\n"
        "只输出JSON数组，无其他内容。"
    )
    text = call(prompt, max_tokens=4096)
    if not text:
        return None
    print(f"  Got {len(text)} chars")
    return extract_json(text)

def save_quiz(level, questions):
    path = os.path.join(CONTENT_DIR, "quiz", "quiz-" + level + ".json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"  Saved {len(questions)} questions to quiz-{level}.json")

def main():
    q = gen_quiz("primary", ["唐诗宋词","成语故事","古代作家","必背古诗","四大名著"], 100)
    if q:
        save_quiz("primary", q)
    else:
        # Save raw for debugging
        print("  primary FAILED - trying smaller batch")
        q = gen_quiz("primary", ["唐诗宋词","成语故事"], 50)
        if q:
            save_quiz("primary", q)

    q = gen_quiz("middle", ["唐宋八大家","古诗词","文言文","名著","修辞"], 100)
    if q:
        save_quiz("middle", q)
    else:
        print("  middle FAILED")

    q = gen_quiz("high", ["先秦诸子","楚辞汉赋","唐诗宋词","元曲","明清小说","现代文学"], 100)
    if q:
        save_quiz("high", q)
    else:
        print("  high FAILED")

if __name__ == "__main__":
    main()
