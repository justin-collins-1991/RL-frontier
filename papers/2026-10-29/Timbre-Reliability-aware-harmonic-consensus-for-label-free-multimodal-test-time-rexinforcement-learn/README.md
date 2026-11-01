---
title: "Timbre: Reliability-aware harmonic consensus for label-free multimodal test-time rexinforcement learning"
arxiv: "2610.39439"
url: https://arxiv.org/abs/2610.39439
authors: "Haotian Lyu, Haoyu Wang, Ru Wang, Feng Ji, Ziwen Li, Jiaxian Guo, et al."
published: 2026-10-29
tagline: "四视图加权调和共识，让多模态测试时RL伪标签更可靠"
---

## 一句话概括

TIMBRE 用“原图/扰动图 × 直接解/改写再解”四个视图做加权调和投票选伪标签，减少无标签多模态测试时 RL 中“一致但错误”的自我强化。

## 核心方法

- **痛点**：TTRL/TTRV 用多数投票当伪标签，模型看错图或被题面误导时，错误共识会被 RL 越练越强。
- **四视图**：图像做亮度/对比度/噪声扰动，文本让模型先改写题目再解，组成 2×2 视图网格。
- **调和共识**：按权重对各视图答案分布取调和平均，任一视图支持弱的答案都会被压低；作者证明它是加权 χ² 重心问题的唯一解，不再依赖“正确答案跨视图概率不变”的假设。
- **自适应权重**：变换后伪标签置信度掉得越多，说明该模态变换越不可靠，就降低其权重（批平均 + 时间平滑）。

## 关键结果

在 6 个多模态推理基准、3 个 Qwen3-VL 规模上，相同 rollout 预算下，适应集 18 组设置中 16 组超过 TTRV，未参与更新的留出集 17/18 组胜出，说明能迁移到新样本。

## 为什么值得关注

无标签自奖励 RL 的最大风险是强化自身错误。TIMBRE 提供了一个可插拔的伪标签选择器：多视图交叉验证 + 视图可靠性自适应，且理论假设比 Self-Harmony 更弱，对部署期 VLM 自适应有直接参考价值。
