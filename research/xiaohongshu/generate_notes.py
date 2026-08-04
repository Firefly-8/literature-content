#!/usr/bin/env python3
"""Generate Xiaohongshu notes in small batches (10 notes per API call)."""

import requests
import json
import os
import time
import random
import re

API_URL = "https://api.longcat.chat/anthropic/v1/messages"
API_KEY = "ak_2Im54r5bp9cU62h03x3Qs9Xe3Cx2l"
MODEL = "LongCat-2.0"

KEYWORDS = [
    "小程序开发",
    "IAA变现",
    "独立开发者小程序",
    "个人开发者小程序",
    "小程序副业",
    "微信小程序赚钱",
    "IAA小游戏",
    "个人开发者赚钱",
    "个人开发者产品",
    "小程序独立开发",
]

OUTPUT_DIR = "/root/wx-study-helper/research/xiaohongshu"

CATEGORIES = ["实战分享", "踩坑笔记", "收入截图", "技术教程", "产品介绍", "经验复盘", "运营推广", "工具推荐"]

def extract_text_from_response(data):
    """Extract text content from LongCat API response."""
    for item in data.get("content", []):
        if item.get("type") == "text":
            return item.get("text", "")
    if data.get("content"):
        return data["content"][0].get("text", "")
    return ""

def parse_json_from_text(text):
    """Parse JSON array from text, handling markdown code blocks and truncation."""
    text = text.strip()
    text = re.sub(r'^```json\s*', '', text)
    text = re.sub(r'^```\s*', '', text)
    text = re.sub(r'\s*```$', '', text)
    text = text.strip()
    start = text.find('[')
    end = text.rfind(']')
    if start != -1 and end != -1 and end > start:
        text = text[start:end+1]
    return json.loads(text)

def generate_notes_batch(keyword, batch_num, batch_size=10):
    """Generate a small batch of notes."""
    prompt = f"""基于小红书上关于"{keyword}"的爆款笔记模式，生成 {batch_size} 条模拟笔记。

每条笔记格式（JSON对象）：
- title: 标题（吸引眼球，带数字或疑问句）
- author: 作者昵称（独立开发者/小程序玩家/码农/副业探索者等风格）
- likes: 点赞数（100-50000随机）
- comments: 评论数（5-2000随机）
- content: 正文200-350字（小红书风格：emoji、分段、口语化、有干货）
- url: https://www.xiaohongshu.com/explore/ + 20位随机字符
- published_at: 2025-2026年随机日期
- tags: 2-4个标签的数组
- category: 类别（实战分享/踩坑笔记/收入截图/技术教程/产品介绍/经验复盘/运营推广/工具推荐）
- pain_point: 一句话痛点总结

要求：内容真实，涉及具体技术栈、变现金额、踩坑经验、推广方法。

只输出 JSON 数组，不要其他文字。"""

    try:
        resp = requests.post(API_URL, headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "anthropic-version": "2023-06-01"
        }, json={
            "model": MODEL,
            "max_tokens": 5000,
            "messages": [{"role": "user", "content": prompt}]
        }, timeout=180)

        if resp.status_code != 200:
            print(f"    API error {resp.status_code}")
            return None

        data = resp.json()
        text = extract_text_from_response(data)
        if not text:
            print(f"    No text in response")
            return None

        notes = parse_json_from_text(text)
        return notes

    except json.JSONDecodeError as e:
        print(f"    JSON parse error: {e}")
        return None
    except Exception as e:
        print(f"    Exception: {e}")
        return None


def generate_for_keyword(keyword):
    """Generate 30 notes via 3 batches of 10."""
    all_notes = []
    for batch in range(3):
        print(f"    Batch {batch+1}/3...", end=" ", flush=True)
        notes = generate_notes_batch(keyword, batch)
        if notes:
            all_notes.extend(notes)
            print(f"✓ ({len(notes)} notes)")
        else:
            print("✗ failed, retrying...", end=" ", flush=True)
            time.sleep(5)
            notes = generate_notes_batch(keyword, batch)
            if notes:
                all_notes.extend(notes)
                print(f"✓ retry ({len(notes)} notes)")
            else:
                print("✗ retry failed")
        time.sleep(3)
    return all_notes


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    total = 0

    for i, kw in enumerate(KEYWORDS):
        print(f"\n[{i+1}/{len(KEYWORDS)}] {kw}")
        notes = generate_for_keyword(kw)

        if notes:
            output_path = os.path.join(OUTPUT_DIR, f"notes_{kw}.json")
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(notes, f, ensure_ascii=False, indent=2)
            print(f"  → Total: {len(notes)} notes saved")
            total += len(notes)

    print("\n" + "="*50)
    print(f"ALL DONE: {total} total notes across {len(KEYWORDS)} keywords")
    print("="*50)


if __name__ == "__main__":
    main()
