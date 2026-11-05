---
title: "Catalyzing Interactive HTML Generation Capabilities via High-Fidelity Reinforcement Learning"
arxiv: "2611.05151"
url: https://arxiv.org/abs/2611.05151
authors: "Xujia Wang, Yixuan Liu, Shaohan Huang, Furu Wei, Lei Hou, Bin Xu, et al."
published: 2026-11-03
tagline: "用小游戏做试验场，靠高保真浏览器交互反馈强化学习，提升 HTML 生成能力"
---

## 一句话概括

以小游戏为高难度试验场，让 GUI Agent 在真实浏览器里“玩”模型生成的页面，并据此给出高保真奖励来做 RL，显著提升 LLM 生成可交互 HTML 的能力。

## 核心方法

WebCatalyst 基于 GRPO，从三个方面提高反馈质量：
- **游戏级 GUI 评估器**：Agent 在 Playwright 中持续进行点击、按键、组合键等多步操作，由单步裁判和全局裁判分两级打分；执行与评估通过生产者-消费者队列并行，降低评估延迟。
- **Visual Anchor**：作者发现，只用 VLM 裁判时，模型会靠简化画面来换取功能分（reward hacking）。因此引入参考截图，对视觉退化进行扣分。
- **Action-Trace Credit**：记录每个成功操作在运行时的调用栈，把执行到的代码映射回生成的 token，再按调用深度重新分配优势，实现 token 级信用分配。

## 关键结果

在 Qwen3.6-35B-A3B 上，仅用不到 1K 条以游戏为主的训练请求：Cookie-Bench Mini Games 从 68.8 提升到 75.3，WebGen-Bench 从 48.8 提升到 56.9，各项指标的平均排名超过 Claude Opus 4.7。消融实验显示，只用 GUI 反馈会损害画面质量，Visual Anchor 能防止这种退化；Action-Trace Credit 则加快了功能指标的提升。

## 为什么值得关注

论文指出，代码 RL 的瓶颈往往是反馈不够真实，而不是数据量不足。它提出的“用运行时轨迹做信用分配”和“用参考锚点防 VLM 奖励作弊”两种做法，可以迁移到其他依赖执行反馈或 VLM 裁判的 RL 场景。
