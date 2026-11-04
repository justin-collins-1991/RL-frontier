---
title: "Do Visual RL Gains Scale at Test Time? A Quantile View of Post-Training"
arxiv: "2611.02366"
url: https://arxiv.org/abs/2611.02366
authors: "Austin Wang, Lexing Ying"
published: 2026-11-02
tagline: "视觉RL提升单样本质量，却可能削弱Best-of-N扩展能力"
---

## 一句话概括

视觉生成模型做完 RL 后训练，单张图质量变好了，但用 Best-of-N 多采样时，这个优势可能变小，甚至反过来输给基座模型。作者用"奖励分位数"解释了原因，并提出 QUPO 来缓解。

## 核心方法

- **诊断**：在 SD3.5-M 上对比 FlowGRPO、DiffusionNFT、GRPO-Guard、AWM 等方法与基座模型。每个 prompt 采 128 张图，画出 Best-of-N 质量随采样数变化的曲线，评测用的都是更难的 held-out prompt。
- **分位数视角**：Best-of-1 对奖励分布的各个分位一视同仁，N 越大越看重上尾，也就是少数特别好的样本。RL 往往把"平均样本"拉高，同时压缩甚至损伤了这些稀有的高分样本。
- **QUPO**：可直接替换原有目标函数，优化多个 Best-of-k 效用的可控加权组合，分别对应不同的推理预算，以此在训练时就照顾到上尾质量。

## 关键结果

- 组合生成（GenEval→GenEval2）：N 小时 RL 模型更强，N 大时被基座反超。
- 文字渲染：一直保持领先，但随 N 增大差距明显缩小，逐渐接近饱和。
- 偏好对齐（PickScore→HPSv2）：优势基本随 N 保持不变。
- 在 SD3.5-M 和 BAGEL 上，QUPO 都更好地保住了上尾质量，困难 held-out prompt 上的 Best-of-N 扩展明显好于标准 RL。

## 为什么值得关注

部署时常常会多采几张再挑最好的。只看单样本奖励，可能会选出"平均分高、上限低"的模型。这篇工作提醒我们，评估和训练都应该关注整个奖励分布，尤其是上尾。QUPO 改动很小，几乎可以直接接到现有 GRPO 类流程里。
