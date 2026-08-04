# 用户指令变更：2026-08-05 01:15

## ⚠️ 用户要求暂停 Phase 2，立即切换任务

Phase 2 仍在跑（小学古诗 17/84 完成），但用户已经拿到 Phase 1 的 90 本书 + GitHub 推送结果，**这是用户的硬指标已达成**。

用户接下来要的是：
1. **立即停止 Phase 2 内容生成**
2. **kill 掉 phase2.py 进程**
3. **立即开始新任务**：从小红书收集"个人开发者 / IAA 变现 / 小程序方向"的爆款笔记和问题笔记
4. **筛选出 5 个最容易实现 + 容易形成 IAA 营收转换的小程序方向**

## 新任务执行步骤

1. **kill 进程**：
   ```bash
   pkill -f phase2.py
   ```

2. **完成 git 提交**（Phase 2 已完成的部分）：
   ```bash
   cd /root/wx-study-helper/
   git add -A
   git commit -m "Phase 2 partial: 17 primary poems + 3 character files"
   git push
   ```

3. **开始小红书调研任务**：
   - 关键词列表：
     - 小程序开发
     - IAA变现
     - 独立开发者小程序
     - 个人开发者小程序
     - 小程序副业
     - 微信小程序赚钱
     - IAA小游戏
     - 个人开发者赚钱
     - 个人开发者产品
     - 小程序独立开发
   - 每个关键词收集 30-50 条笔记
   - 笔记字段：title, author, likes, comments, content, url, published_at, tags
   - 收集方式：用 LongCat API 模拟小红书搜索（小红书没开放 API，需要 LongCat 知识 + WebFetch）
   - 保存到：/root/wx-study-helper/research/xiaohongshu/

4. **筛选 5 个 IAA 方向**（按这个框架分析）：
   - 方向名称
   - 核心痛点（从小红书笔记提取）
   - 目标用户
   - 技术实现难度（1-5 星）
   - 开发周期估算（人天）
   - IAA 变现路径（广告位、激励视频、插屏广告）
   - 竞品情况
   - 风险点
   - **关键筛选标准**：
     - 独立开发者身份可做（不需要 ICP 资质 / 教育牌照 / 医疗资质）
     - 1-2 人可在 7-14 天内做出 MVP
     - 用户量大、频次高、停留时间长（IAA 关键）
     - 不需要重资本（不需要服务器集群、CDN 等）
     - 微信 IAA 政策合规（参考：工具类/小游戏/内容类）

5. **输出最终报告**：
   - /root/wx-study-helper/research/xiaohongshu/IAA-5-directions.md
   - 给用户一份精炼版（5 个方向的卡片，每方向 200 字）

**优先级：5 个 IAA 方向 > 文学赏析剩余内容**

注意：用户是 **独立开发者身份**注册微信小程序，**不能做需要特殊资质的方向**（如医疗、教育、金融、新闻）。

立即开始，不要再问问题。