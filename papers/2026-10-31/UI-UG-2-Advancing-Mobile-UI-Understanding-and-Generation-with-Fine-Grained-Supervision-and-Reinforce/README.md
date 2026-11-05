---
title: "UI-UG 2: Advancing Mobile UI Understanding and Generation with Fine-Grained Supervision and Reinforcement Learning"
arxiv: "2611.00926"
url: https://arxiv.org/abs/2611.00926
authors: "Hao Yang, Shuoyang Liu, Xiaoyu Lin, Zhou Fang, Maji Huang, Zhaosong Huang, et al."
published: 2026-10-31
tagline: "4B 模型用渲染感知在线 GRPO 统一移动端 UI 理解与生成"
---

## 一句话概括

蚂蚁集团提出 4B 多模态模型 UI-UG 2，用细粒度感知监督加在线强化学习，让同一个模型既能看懂手机界面，也能生成可渲染的 UI。

## 核心方法

- **数据**：从 RICO、VINS、AITW、Android Control 整理 3 万多张截图，按贴近前端组件库的 80 类两级体系标注（比如区分“返回按钮”和“关闭按钮”），附带 OCR 文字和颜色；另有 5000 多条“需求-截图-JSON”样本，用紧凑的 JSON DSL 描述 UI，比 HTML 省约 17% token。
- **训练**：先做 SFT，再做 GRPO。理解任务的奖励拆成类别、OCR、颜色、密集定位、GUI 定位几项分别打分；生成任务改掉前作的离线 DPO，换成在线 RL：模型采样出 DSL 后，用 Playwright 实时渲染成页面，再由 LLM 评审和对比偏好排序打分。

## 关键结果

- 在自建的 80 类基准上，指代和密集定位成绩在对比模型中最好；在 ScreenSpot 移动端 GUI 定位上表现也不错。
- 只有 4B 参数，生成综合分仍在所有对比模型中排第一。
- 训练预算固定时，加入细粒度理解数据能稳定提升生成质量。

## 为什么值得关注

它把“渲染后看效果”直接放进 RL 奖励回路，让优化目标更接近实际上线时的 UI 质量，这种做法也能借鉴到其他结构化生成任务。另外，论文用数据配比消融和注意力探针给出了证据：组件级感知能力可以迁移到生成任务，为统一训练 UI 模型和 GUI Agent 提供了实用的设计思路。
