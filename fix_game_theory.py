import requests, json

API_URL = "https://api.longcat.chat/anthropic/v1/messages"
API_KEY = "ak_2Im54r5bp9cU62h03x3Qs9Xe3Cx2l"
HEADERS = {
    "Authorization": "Bearer " + API_KEY,
    "Content-Type": "application/json",
    "anthropic-version": "2023-06-01",
}

prompt = (
    "你是一位资深的经济学学者和文学评论家。请为《博弈论》撰写深度阅读指南，"
    "严格按如下结构输出 Markdown（不要限制字数，尽可能讲清楚）：\n\n"
    "# 《博弈论》\n\n"
    "## 一、内容摘要\n"
    "- 作者背景（国籍、生平、学术地位）\n"
    "- 核心论点\n"
    "- 章节脉络（每章讲什么）\n"
    "- 关键概念/术语解释\n\n"
    "## 二、如何阅读这本书\n"
    "### 问题一：这本书在讲什么（整体框架）\n"
    "### 问题二：作者细部说了什么，怎么说的（论点+论据）\n"
    "### 问题三：这本书说得有道理吗（评论，包括局限性）\n"
    "### 问题四：这本书跟你有什么关系（应用/启发）\n\n"
    "要求：内容详实、有深度、有个人见解。每个部分至少300字。"
)

r = requests.post(API_URL, headers=HEADERS, json={
    "model": "LongCat-2.0",
    "max_tokens": 4096,
    "messages": [{"role": "user", "content": prompt}]
}, timeout=300)

data = r.json()
texts = [c["text"] for c in data.get("content", []) if c.get("type") == "text" and "text" in c]
text = "\n\n".join(texts) if texts else data.get("content", [{}])[0].get("text", "")

path = "/root/wx-study-helper/content/books/economics/04-博弈论.md"
with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("Written:", len(text), "chars")
print("Usage:", data.get("usage", {}))
