#!/usr/bin/env python3
"""Generate 70 book summaries."""
import os, time, requests

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
            }, timeout=300)
            if r.status_code == 200:
                data = r.json()
                texts = [c["text"] for c in data.get("content", []) if c.get("type") == "text" and "text" in c]
                return "\n\n".join(texts) if texts else data.get("content", [{}])[0].get("text", "")
        except Exception as e:
            print(f"  Error: {e}")
            time.sleep(5)
    return None

WESTERN = [
    "傲慢与偏见","简·爱","呼啸山庄","双城记","雾都孤儿","大卫·科波菲尔","远大前程",
    "红字","白鲸","老人与海","了不起的盖茨比","麦田里的守望者","杀死一只知更鸟",
    "1984","动物农场","美丽新世界","我们","百年孤独","霍乱时期的爱情",
    "追忆似水年华","尤利西斯","变形记","局外人","西西弗神话","鼠疫",
    "悲惨世界","巴黎圣母院","红与黑","高老头","欧也妮·葛朗台","包法利夫人",
    "安娜·卡列尼娜","战争与和平","复活","罪与罚","卡拉马佐夫兄弟",
    "堂吉诃德","哈姆雷特","罗密欧与朱丽叶","李尔王","麦克白"
]

CHINESE_MODERN = [
    "呐喊","彷徨","围城","边城","骆驼祥子","子夜","家","春","秋",
    "雷雨","日出","北京人","茶馆","活着","平凡的世界","白鹿原",
    "红高粱","蛙","生死疲劳","蛙","尘埃落定"
]

EASTERN = [
    "源氏物语","罗生门","雪国","挪威的森林","人间失格","我是猫","春琴抄",
    "古都","千只鹤","伊豆的舞女"
]

def generate_summary(book, author, idx):
    prompt = (
        "请为《" + book + "》（" + author + "）撰写名著导读，"
        "严格按如下 Markdown 格式输出：\n\n"
        "# 《" + book + "》 — " + author + "\n\n"
        "**基本信息**：首版时间、国籍、文学类别\n\n"
        "**故事梗概**：500-800字，不剧透关键结局\n\n"
        "**核心主题**：列出3-5个\n\n"
        "**艺术特色**：300字\n\n"
        "**为什么读这本书**：200字\n\n"
        "要求：内容详实、有深度。"
    )
    text = call(prompt, max_tokens=2500)
    if text:
        filename = str(idx).zfill(2) + "-" + book + ".md"
        path = os.path.join(CONTENT_DIR, "books-summary", filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        return True
    return False

def main():
    idx = 1
    for book in WESTERN:
        print(f"  {book}...", end=" ", flush=True)
        author = "西方作家"
        if generate_summary(book, author, idx):
            print("OK")
            idx += 1
        else:
            print("FAILED")

    for book in CHINESE_MODERN:
        print(f"  {book}...", end=" ", flush=True)
        if generate_summary(book, "中国作家", idx):
            print("OK")
            idx += 1
        else:
            print("FAILED")

    for book in EASTERN:
        print(f"  {book}...", end=" ", flush=True)
        if generate_summary(book, "日本作家", idx):
            print("OK")
            idx += 1
        else:
            print("FAILED")

if __name__ == "__main__":
    main()
