#!/usr/bin/env python3
"""Generate ancient poems in batches."""
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

def save(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

PRIMARY = [
    "静夜思","春晓","咏鹅","悯农（其一）","悯农（其二）","游子吟","江雪","寻隐者不遇",
    "登鹳雀楼","相思","鹿柴","鸟鸣涧","九月九日忆山东兄弟","望庐山瀑布","黄鹤楼送孟浩然之广陵",
    "早发白帝城","望天门山","绝句（两个黄鹂）","春夜喜雨","绝句（迟日江山丽）","枫桥夜泊",
    "滁州西涧","渔歌子","望洞庭","浪淘沙","江南春","山行","清明",
    "赠汪伦","芙蓉楼送辛渐","凉州词（王之涣）","凉州词（王翰）","出塞","别董大",
    "蜂","江上渔者","元日","泊船瓜洲","书湖阴先生壁","饮湖上初晴后雨",
    "惠崇春江晚景","题西林壁","示儿","秋夜将晓出篱门迎凉有感","四时田园杂兴（昼出耘田）",
    "四时田园杂兴（梅子金黄）","小池","晓出净慈寺送林子方","春日","乡村四月","村居",
    "所见","竹石","己亥杂诗","石灰吟","墨梅","回乡偶书","咏柳","长歌行",
    "敕勒歌","风","江南","古朗月行","明日歌","苔","画","梅花",
    "夜书所见","乞巧","嫦娥","题临安邸","秋夕","嫦娥","商山早行","山中送别"
]

MIDDLE = [
    "观沧海","次北固山下","闻王昌龄左迁龙标遥有此寄","天净沙·秋思","夜雨寄北",
    "木兰诗","登幽州台歌","望岳","春望","茅屋为秋风所破歌","白雪歌送武判官归京",
    "酬乐天扬州初逢席上见赠","卖炭翁","钱塘湖春行","雁门太守行","赤壁","泊秦淮",
    "无题（相见时难）","相见欢","渔家傲·秋思","浣溪沙","登飞来岳",
    "江城子·密州出猎","水调歌头","破阵子","过零丁洋","山坡羊·潼关怀古",
    "满江红","南乡子·登京口北固亭有怀","十五从军征","行军九日思长安故园",
    "夜上受降城闻笛","江南逢李龟年","春夜洛城闻笛","逢入京使","晚春","竹里馆",
    "峨眉山月歌","十一月四日风雨大作","过松源晨炊漆公店","约客","游山西村",
    "野望","黄鹤楼","使至塞上","渡荆门送别","饮酒","渔家傲","蒹葭",
    "关雎","式微","子衿","送杜少府之任蜀州","望洞庭湖赠张丞相",
    "北冥有鱼","虽有嘉肴","大道之行也","马说","石壕吏","题破山寺后禅院",
    "送友人","卜算子·黄州定慧院寓居作","卜算子·咏梅","沁园春·雪","行路难",
    "鱼我所欲也","唐雎不辱使命","邹忌讽齐王纳谏","陈涉世家","出师表",
    "生于忧患死于安乐","愚公移山","周亚夫军细柳","核舟记","桃花源记",
    "小石潭记","醉翁亭记","岳阳楼记","爱莲说","记承天寺夜游","三峡",
    "答谢中书书","与朱元思书","送东阳马生序","曹刿论战"
]

HIGH = [
    "离骚（节选）","蜀道难","琵琶行","锦瑟","虞美人","念奴娇·赤壁怀古",
    "永遇乐·京口北固亭怀古","声声慢","醉花阴","水龙吟·登建康赏心亭",
    "摸鱼儿","六国论","阿房宫赋","滕王阁序","师说","劝学",
    "逍遥游（节选）","陈情表","归去来兮辞","兰亭集序","春江花月夜",
    "将进酒","燕歌行","梦游天姥吟留别","蜀相","登高","登岳阳楼",
    "石头城","李凭箜篌引","菩萨蛮","雨霖铃","桂枝香·金陵怀古",
    "江城子·乙卯正月二十日夜记梦","念奴娇·过临江","定风波",
    "临江仙·夜登小阁忆洛中旧游","青玉案·元夕","扬州慢",
    "沁园春·长沙","再别康桥","雨巷","大堰河我的保姆",
    "短歌行","白马篇","咏怀","咏史","饮酒","归园田居",
    "拟行路难","夜泊牛渚怀中","春江花月夜","山居秋暝","终南山",
    "燕歌行","走马川行奉送出师西征","蜀道难","长恨歌","卖炭翁",
    "观刈麦","雁门太守行","赤壁","泊秦淮","夜雨寄北","无题",
    "虞美人","雨霖铃","桂枝香","念奴娇·赤壁怀古","声声慢"
]

def generate_poem(poem_name, level, idx):
    level_map = {"primary": "小学", "middle": "初中", "high": "高中"}
    prompt = (
        "请为" + level_map[level] + "语文必背古诗文《" + poem_name + "》撰写详细赏析，"
        "严格按如下 Markdown 格式输出：\n\n"
        "## " + poem_name + "\n\n"
        "**作者**：作者名（朝代）\n\n"
        "**原文**：全文\n\n"
        "**创作背景**：100-200字\n\n"
        "**字词注释**：关键词解释\n\n"
        "**翻译**：白话译文\n\n"
        "**赏析**：300-500字艺术特色分析\n\n"
        "要求：内容准确、有深度。"
    )
    text = call(prompt, max_tokens=2000)
    if text:
        filename = str(idx).zfill(3) + "-" + poem_name + ".md"
        save(os.path.join(CONTENT_DIR, "poems", level, filename), text)
        return True
    return False

def main():
    for level, poems in [("primary", PRIMARY), ("middle", MIDDLE), ("high", HIGH)]:
        print(f"\n=== {level}: {len(poems)} poems ===")
        idx = 1
        for poem in poems:
            print("  " + poem + "...", end=" ", flush=True)
            if generate_poem(poem, level, idx):
                print("OK")
                idx += 1
            else:
                print("FAILED")

if __name__ == "__main__":
    main()
