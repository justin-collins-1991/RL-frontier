---
title: "Geometric Time Score Estimators: Bridging Self-Predictive Representations and Generative Occupancy Models For Reinforcement Learning"
arxiv: "2610.38901"
url: https://arxiv.org/abs/2610.38901
authors: "Aravind Venugopal, Grace Liu, Jeff Schneider, Benjamin Eysenbach"
published: 2026-10-28
tagline: "沿概率路径学时间分数，把生成式占用模型变成准确的密度估计器"
---

## 一句话概括

GTSE 用 TD 学习沿概率路径估计占用测度的“时间分数”，再积分得到未来状态密度。它把自预测表示和生成式占用模型这两条路线接了起来，在目标条件 RL 上比现有方法高 2~6 倍。

## 核心方法

- **发现问题**：在一个简单的多峰玩具 MDP 上，CRL、FB、TD-JEPA、TMD 这类自预测表示方法估出来的未来状态密度都不太准，尤其是远离数据集中区域的状态；原因是它们受限于低秩的内积表示。TD-flows 这类生成式占用模型能采出很好的样本，但本来就不是为了估密度训练的，用迹估计硬算出来的密度同样不准。
- **GTSE 的做法**：不直接拟合密度，而是学习“沿噪声到数据的插值路径走，log 密度每一步变化多少”，也就是时间分数，并用 TD 递推来训练；然后沿路径积分，就得到对数占用密度，可以直接当目标条件 Q 值用。
- **理论联系**：在双线性参数化下，这个积分可以拆成无穷多对“状态-动作 / 目标”表示的内积之和，相当于隐式提高了表示的秩。据此作者还给出一个变体，能显式导出状态-动作表示和目标表示。

## 关键结果

- 玩具 MDP 上，GTSE 的密度估计与真值的秩相关性明显高于各类基线（基线中较好的 ρ 约为 0.78）。
- 在 OGBench 的多个移动和操作类目标条件任务上，性能比 SOTA 高 2~6 倍。
- 学到的表示迁移到下游带奖励的 RL 任务后同样有效。

## 为什么值得关注

“学好未来状态密度”是 GCRL 和无监督表示学习的核心，但现有方法要么表达力不足，要么拿不到密度。GTSE 借用 time score matching，提供了一条兼顾表达力和可算密度的路线，还能导出可复用的表示，适合作为占用模型和后继表示（successor representation）研究的新基线。
