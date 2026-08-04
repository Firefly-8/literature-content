#!/usr/bin/env python3
"""Generate 四大名著人物志 200 characters."""
import json, os, time, requests

API_URL = "https://api.longcat.chat/anthropic/v1/messages"
API_KEY = "ak_2Im54r5bp9cU62h03x3Qs9Xe3Cx2l"
HEADERS = {
    "Authorization": "Bearer " + API_KEY,
    "Content-Type": "application/json",
    "anthropic-version": "2023-06-01",
}
CONTENT_DIR = "/root/wx-study-helper/content"

def call(prompt, max_tokens=4096, retries=3):
    for attempt in range(retries):
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

def save(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# Character lists for each novel
HONGLOU_CHARACTERS = [
    "贾宝玉","林黛玉","薛宝钗","王熙凤","贾母","贾政","王夫人","贾琏","贾元春",
    "贾迎春","贾探春","贾惜春","史湘云","妙玉","李纨","秦可卿","平儿","袭人",
    "晴雯","紫鹃","鸳鸯","司棋","小红","刘姥姥","贾雨村","薛蟠","贾环","赵姨娘",
    "邢夫人","尤二姐","尤三姐","芳官","龄官","智能儿","秦钟","柳湘莲","蒋玉菡",
    "薛宝琴","邢岫烟","李纹","李绮","喜儿","寿儿","昭儿","兴儿","旺儿","林之孝"
]

XIYOU_CHARACTERS = [
    "孙悟空","唐僧","猪八戒","沙僧","白龙马","观音菩萨","如来佛祖","玉皇大帝",
    "太上老君","太白金星","哪吒","二郎神","托塔李天王","嫦娥","镇元子","红孩儿",
    "牛魔王","铁扇公主","白骨精","金角大王","银角大王","黄袍怪","蜘蛛精","蝎子精",
    "黑熊精","黄狮精","金翅大鹏","九头虫","灵感大王","独角兕","黄眉老佛","赛太岁",
    "蜈蚣精","狐狸精","老鼠精","玉兔精","金鼻白毛老鼠精","杏仙","树精","虎力大仙",
    "鹿力大仙","羊力大仙","镇元大仙","赤脚大仙","弥勒佛","灵吉菩萨","毗蓝婆菩萨"
]

SANGUO_CHARACTERS = [
    "刘备","关羽","张飞","诸葛亮","曹操","孙权","赵云","周瑜","司马懿","吕布",
    "貂蝉","董卓","袁绍","袁术","刘表","孙策","鲁肃","黄盖","甘宁","太史慈",
    "马超","黄忠","魏延","姜维","庞统","法正","徐庶","关兴","张苞","关平",
    "周仓","廖化","王平","张翼","诸葛瞻","邓艾","钟会","羊祜","杜预","陆抗",
    "华佗","张仲景","左慈","于吉","司马师","司马昭","曹丕","曹植","曹叡","刘禅"
]

SHUIHU_CHARACTERS = [
    "宋江","卢俊义","吴用","林冲","武松","鲁智深","李逵","花荣","燕青","公孙胜",
    "关胜","秦明","呼延灼","柴进","李应","朱仝","雷横","杨志","徐宁","索超",
    "戴宗","刘唐","史进","穆弘","雷横","李俊","阮小二","阮小五","阮小七","张顺",
    "张横","杨雄","石秀","解珍","解宝","朱武","黄信","孙立","宣赞","郝思文",
    "韩滔","彭玘","单廷珪","魏定国","萧让","裴宣","欧鹏","邓飞","燕顺","杨林"
]

def generate_novel_characters(novel_name, characters, filename):
    """Generate all characters for a novel in one large batch."""
    char_list = "\n".join([f"- {c}" for c in characters])
    prompt = (
        f"请为《{novel_name}》中的以下人物撰写人物志。每个人物严格按如下 Markdown 格式输出：\n\n"
        f"### 人物名\n\n"
        f"**身份**：...\n\n"
        f"**关键事件**：3-5个\n\n"
        f"**性格特点**：...\n\n"
        f"**人物关系**：...\n\n"
        f"**经典语录**：...\n\n"
        f"**赏析**：200-300字\n\n"
        f"需要撰写的人物（共{len(characters)}个）：\n{char_list}\n\n"
        f"请为所有人物撰写，不要遗漏。输出完整 Markdown。"
    )
    print(f"Generating {novel_name} ({len(characters)} characters)...")
    text = call(prompt, max_tokens=4096)
    if text:
        # The model may not fit all in one call, save what we got
        save(os.path.join(CONTENT_DIR, "characters", filename), text)
        print(f"  Saved {len(text)} chars")
        return True
    return False

def main():
    generate_novel_characters("红楼梦", HONGLOU_CHARACTERS, "hongloumeng.md")
    generate_novel_characters("西游记", XIYOU_CHARACTERS, "xiyouji.md")
    generate_novel_characters("三国演义", SANGUO_CHARACTERS, "sanguoyanyi.md")
    generate_novel_characters("水浒传", SHUIHU_CHARACTERS, "shuihuzhuan.md")
    print("Characters done!")

if __name__ == "__main__":
    main()
