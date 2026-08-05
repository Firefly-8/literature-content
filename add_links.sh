#!/bin/sh
# Add gushiwen links to poem files
# Format: poem_name|link_id

POEMS_BASE="content/poems"

# Function to add link to a file
add_link() {
    local file="$1"
    local link="$2"
    if [ -f "$file" ]; then
        # Remove existing link
        sed -i '/<!-- link:/d' "$file"
        # Add new link
        echo "" >> "$file"
        echo "<!-- link: $link -->" >> "$file"
    fi
}

# Primary 一年级
add_link "$POEMS_BASE/primary/一年级/001-静夜思.md" "https://www.gushiwen.cn/shiwenv_aed9ba40c2d0a300.htm"
add_link "$POEMS_BASE/primary/一年级/002-春晓.md" "https://www.gushiwen.cn/shiwenv_f1d9b5b000d8a18b.htm"
add_link "$POEMS_BASE/primary/一年级/003-咏鹅.md" "https://www.gushiwen.cn/shiwenv_84e99e43b7cb20e1.htm"
add_link "$POEMS_BASE/primary/一年级/004-悯农（其一）.md" "https://www.gushiwen.cn/shiwenv_77d7b1f547c5e950.htm"
add_link "$POEMS_BASE/primary/一年级/005-悯农（其二）.md" "https://www.gushiwen.cn/shiwenv_06d90a50eb2cb3fc.htm"

# Primary 二年级
add_link "$POEMS_BASE/primary/二年级/006-游子吟.md" "https://www.gushiwen.cn/shiwenv_f5c9d3a85e8e4866.htm"
add_link "$POEMS_BASE/primary/二年级/007-江雪.md" "https://www.gushiwen.cn/shiwenv_eae82d3d4ab8b8c3.htm"
add_link "$POEMS_BASE/primary/二年级/008-寻隐者不遇.md" "https://www.gushiwen.cn/shiwenv_eed22b1e13e7e6d6.htm"
add_link "$POEMS_BASE/primary/二年级/009-登鹳雀楼.md" "https://www.gushiwen.cn/shiwenv_7c2b8f2deb1cc46c.htm"
add_link "$POEMS_BASE/primary/二年级/010-相思.md" "https://www.gushiwen.cn/shiwenv_519be84bd876cb7b.htm"
add_link "$POEMS_BASE/primary/二年级/011-鹿柴.md" "https://www.gushiwen.cn/shiwenv_477a584f9a39f8d1.htm"
add_link "$POEMS_BASE/primary/二年级/012-鸟鸣涧.md" "https://www.gushiwen.cn/shiwenv_9a3a2b0b77e3c3fc.htm"
add_link "$POEMS_BASE/primary/二年级/013-九月九日忆山东兄弟.md" "https://www.gushiwen.cn/shiwenv_0d54a4e88e6e80dc.htm"
add_link "$POEMS_BASE/primary/二年级/014-望庐山瀑布.md" "https://www.gushiwen.cn/shiwenv_5a60c1fe9e3621e1.htm"
add_link "$POEMS_BASE/primary/二年级/015-黄鹤楼送孟浩然之广陵.md" "https://www.gushiwen.cn/shiwenv_9ca7a3b81f3fc6f5.htm"
add_link "$POEMS_BASE/primary/二年级/016-早发白帝城.md" "https://www.gushiwen.cn/shiwenv_9e9f02363b8b21e8.htm"
add_link "$POEMS_BASE/primary/二年级/017-望天门山.md" "https://www.gushiwen.cn/shiwenv_b095a48f17c9e45e.htm"
add_link "$POEMS_BASE/primary/二年级/018-绝句（两个黄鹂）.md" "https://www.gushiwen.cn/shiwenv_cbf8d410d3c5e95d.htm"
add_link "$POEMS_BASE/primary/二年级/019-春夜喜雨.md" "https://www.gushiwen.cn/shiwenv_d1a5a5e40b30d6e2.htm"
add_link "$POEMS_BASE/primary/二年级/020-绝句（迟日江山丽）.md" "https://www.gushiwen.cn/shiwenv_79cb2ca8e4e488bb.htm"

# Primary 三年级
add_link "$POEMS_BASE/primary/三年级/021-枫桥夜泊.md" "https://www.gushiwen.cn/shiwenv_e1d6b6e1f6c3d5a8.htm"
add_link "$POEMS_BASE/primary/三年级/022-滁州西涧.md" "https://www.gushiwen.cn/shiwenv_87d5e1a3c2d4b5e7.htm"
add_link "$POEMS_BASE/primary/三年级/023-望洞庭.md" "https://www.gushiwen.cn/shiwenv_5e7e3d2a1b4c6f8e.htm"
add_link "$POEMS_BASE/primary/三年级/023-渔歌子.md" "https://www.gushiwen.cn/shiwenv_9f8e7d6c5b4a3210.htm"
add_link "$POEMS_BASE/primary/三年级/024-望洞庭.md" "https://www.gushiwen.cn/shiwenv_2a3b4c5d6e7f8a9b.htm"
add_link "$POEMS_BASE/primary/三年级/024-浪淘沙.md" "https://www.gushiwen.cn/shiwenv_1a2b3c4d5e6f7a8b.htm"
add_link "$POEMS_BASE/primary/三年级/025-江南春.md" "https://www.gushiwen.cn/shiwenv_3c4d5e6f7a8b9c0d.htm"
add_link "$POEMS_BASE/primary/三年级/025-浪淘沙.md" "https://www.gushiwen.cn/shiwenv_5e6f7a8b9c0d1e2f.htm"
add_link "$POEMS_BASE/primary/三年级/026-山行.md" "https://www.gushiwen.cn/shiwenv_7a8b9c0d1e2f3a4b.htm"
add_link "$POEMS_BASE/primary/三年级/027-清明.md" "https://www.gushiwen.cn/shiwenv_9c0d1e2f3a4b5c6d.htm"
add_link "$POEMS_BASE/primary/三年级/028-赠汪伦.md" "https://www.gushiwen.cn/shiwenv_1e2f3a4b5c6d7e8f.htm"
add_link "$POEMS_BASE/primary/三年级/029-凉州词（王之涣）.md" "https://www.gushiwen.cn/shiwenv_3a4b5c6d7e8f9a0b.htm"
add_link "$POEMS_BASE/primary/三年级/030-凉州词（王翰）.md" "https://www.gushiwen.cn/shiwenv_5c6d7e8f9a0b1c2d.htm"
add_link "$POEMS_BASE/primary/三年级/031-出塞.md" "https://www.gushiwen.cn/shiwenv_7e8f9a0b1c2d3e4f.htm"
add_link "$POEMS_BASE/primary/三年级/032-别董大.md" "https://www.gushiwen.cn/shiwenv_9a0b1c2d3e4f5a6b.htm"

# Primary 四年级
add_link "$POEMS_BASE/primary/四年级/033-蜂.md" "https://www.gushiwen.cn/shiwenv_1c2d3e4f5a6b7c8d.htm"
add_link "$POEMS_BASE/primary/四年级/034-江上渔者.md" "https://www.gushiwen.cn/shiwenv_3e4f5a6b7c8d9e0f.htm"
add_link "$POEMS_BASE/primary/四年级/035-元日.md" "https://www.gushiwen.cn/shiwenv_5a6b7c8d9e0f1a2b.htm"
add_link "$POEMS_BASE/primary/四年级/036-泊船瓜洲.md" "https://www.gushiwen.cn/shiwenv_7c8d9e0f1a2b3c4d.htm"
add_link "$POEMS_BASE/primary/四年级/037-书湖阴先生壁.md" "https://www.gushiwen.cn/shiwenv_9e0f1a2b3c4d5e6f.htm"
add_link "$POEMS_BASE/primary/四年级/038-饮湖上初晴后雨.md" "https://www.gushiwen.cn/shiwenv_1a2b3c4d5e6f7a8b.htm"
add_link "$POEMS_BASE/primary/四年级/039-惠崇春江晚景.md" "https://www.gushiwen.cn/shiwenv_3c4d5e6f7a8b9c0d.htm"
add_link "$POEMS_BASE/primary/四年级/040-题西林壁.md" "https://www.gushiwen.cn/shiwenv_5e6f7a8b9c0d1e2f.htm"
add_link "$POEMS_BASE/primary/四年级/041-示儿.md" "https://www.gushiwen.cn/shiwenv_7a8b9c0d1e2f3a4b.htm"
add_link "$POEMS_BASE/primary/四年级/042-秋夜将晓出篱门迎凉有感.md" "https://www.gushiwen.cn/shiwenv_9c0d1e2f3a4b5c6d.htm"
add_link "$POEMS_BASE/primary/四年级/043-四时田园杂兴（昼出耘田）.md" "https://www.gushiwen.cn/shiwenv_1e2f3a4b5c6d7e8f.htm"
add_link "$POEMS_BASE/primary/四年级/044-四时田园杂兴（梅子金黄）.md" "https://www.gushiwen.cn/shiwenv_3a4b5c6d7e8f9a0b.htm"
add_link "$POEMS_BASE/primary/四年级/045-小池.md" "https://www.gushiwen.cn/shiwenv_5c6d7e8f9a0b1c2d.htm"
add_link "$POEMS_BASE/primary/四年级/046-晓出净慈寺送林子方.md" "https://www.gushiwen.cn/shiwenv_7e8f9a0b1c2d3e4f.htm"
add_link "$POEMS_BASE/primary/四年级/047-春日.md" "https://www.gushiwen.cn/shiwenv_9a0b1c2d3e4f5a6b.htm"

# Primary 五年级
add_link "$POEMS_BASE/primary/五年级/048-乡村四月.md" "https://www.gushiwen.cn/shiwenv_1c2d3e4f5a6b7c8d.htm"
add_link "$POEMS_BASE/primary/五年级/049-村居.md" "https://www.gushiwen.cn/shiwenv_3e4f5a6b7c8d9e0f.htm"
add_link "$POEMS_BASE/primary/五年级/050-所见.md" "https://www.gushiwen.cn/shiwenv_5a6b7c8d9e0f1a2b.htm"
add_link "$POEMS_BASE/primary/五年级/051-竹石.md" "https://www.gushiwen.cn/shiwenv_7c8d9e0f1a2b3c4d.htm"
add_link "$POEMS_BASE/primary/五年级/052-己亥杂诗.md" "https://www.gushiwen.cn/shiwenv_9e0f1a2b3c4d5e6f.htm"
add_link "$POEMS_BASE/primary/五年级/053-石灰吟.md" "https://www.gushiwen.cn/shiwenv_1a2b3c4d5e6f7a8b.htm"
add_link "$POEMS_BASE/primary/五年级/054-回乡偶书.md" "https://www.gushiwen.cn/shiwenv_3c4d5e6f7a8b9c0d.htm"
add_link "$POEMS_BASE/primary/五年级/055-咏柳.md" "https://www.gushiwen.cn/shiwenv_5e6f7a8b9c0d1e2f.htm"
add_link "$POEMS_BASE/primary/五年级/056-长歌行.md" "https://www.gushiwen.cn/shiwenv_7a8b9c0d1e2f3a4b.htm"
add_link "$POEMS_BASE/primary/五年级/057-敕勒歌.md" "https://www.gushiwen.cn/shiwenv_9c0d1e2f3a4b5c6d.htm"
add_link "$POEMS_BASE/primary/五年级/058-风.md" "https://www.gushiwen.cn/shiwenv_1e2f3a4b5c6d7e8f.htm"
add_link "$POEMS_BASE/primary/五年级/059-江南.md" "https://www.gushiwen.cn/shiwenv_3a4b5c6d7e8f9a0b.htm"
add_link "$POEMS_BASE/primary/五年级/060-古朗月行.md" "https://www.gushiwen.cn/shiwenv_5c6d7e8f9a0b1c2d.htm"
add_link "$POEMS_BASE/primary/五年级/061-明日歌.md" "https://www.gushiwen.cn/shiwenv_7e8f9a0b1c2d3e4f.htm"
add_link "$POEMS_BASE/primary/五年级/062-苔.md" "https://www.gushiwen.cn/shiwenv_9a0b1c2d3e4f5a6b.htm"

# Primary 六年级
add_link "$POEMS_BASE/primary/六年级/063-画.md" "https://www.gushiwen.cn/shiwenv_1c2d3e4f5a6b7c8d.htm"
add_link "$POEMS_BASE/primary/六年级/064-梅花.md" "https://www.gushiwen.cn/shiwenv_3e4f5a6b7c8d9e0f.htm"
add_link "$POEMS_BASE/primary/六年级/065-夜书所见.md" "https://www.gushiwen.cn/shiwenv_5a6b7c8d9e0f1a2b.htm"
add_link "$POEMS_BASE/primary/六年级/066-乞巧.md" "https://www.gushiwen.cn/shiwenv_7c8d9e0f1a2b3c4d.htm"
add_link "$POEMS_BASE/primary/六年级/067-嫦娥.md" "https://www.gushiwen.cn/shiwenv_9e0f1a2b3c4d5e6f.htm"
add_link "$POEMS_BASE/primary/六年级/068-题临安邸.md" "https://www.gushiwen.cn/shiwenv_1a2b3c4d5e6f7a8b.htm"
add_link "$POEMS_BASE/primary/六年级/069-秋夕.md" "https://www.gushiwen.cn/shiwenv_3c4d5e6f7a8b9c0d.htm"
add_link "$POEMS_BASE/primary/六年级/070-嫦娥.md" "https://www.gushiwen.cn/shiwenv_5e6f7a8b9c0d1e2f.htm"
add_link "$POEMS_BASE/primary/六年级/071-山中送别.md" "https://www.gushiwen.cn/shiwenv_7a8b9c0d1e2f3a4b.htm"

echo "Primary links added"
