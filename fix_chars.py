#!/usr/bin/env python3
"""Fill missing characters."""
import os, time, requests

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

def append_to(path, content):
    with open(path, "a", encoding="utf-8") as f:
        f.write(content + "\n\n")

def gen(novel, chars, fname):
    char_list = "\n".join(["- " + c for c in chars])
    prompt = (
        "请为《" + novel + "》中的以下人物撰写人物志。"
        "每个人物严格按如下 Markdown 格式输出：\n\n"
        "### 人物名\n\n"
        "**身份**：...\n\n"
        "**关键事件**：3-5个\n\n"
        "**性格特点**：...\n\n"
        "**人物关系**：...\n\n"
        "**经典语录**：...\n\n"
        "**赏析**：200-300字\n\n"
        "需要撰写的人物：\n" + char_list
    )
    print(f"  {novel}: {chars[0]}...{chars[-1]}")
    text = call(prompt, max_tokens=4096)
    if text:
        append_to(os.path.join(CONTENT_DIR, "characters", fname), text)
        print(f"    Saved {len(text)} chars")
    else:
        print("    FAILED")

# 西游记 missing: 鹿力大仙 through 毗蓝婆菩萨
xiyou_missing = ["鹿力大仙","羊力大仙","镇元大仙","赤脚大仙","弥勒佛","灵吉菩萨","毗蓝婆菩萨",
                 "九头虫","灵感大王","黄狮精","金翅大鹏","黑熊精","蜘蛛精","蝎子精"]
gen("西游记", xiyou_missing, "xiyouji.md")

# 水浒传 missing: 韩滔 through 杨林
shuihu_missing = ["韩滔","彭玘","单廷珪","魏定国","萧让","裴宣","欧鹏","邓飞","燕顺","杨林"]
gen("水浒传", shuihu_missing, "shuihuzhuan.md")

print("Done!")
