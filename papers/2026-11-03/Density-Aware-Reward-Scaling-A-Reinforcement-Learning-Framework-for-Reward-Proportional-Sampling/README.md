---
title: "Density-Aware Reward Scaling: A Reinforcement Learning Framework for Reward-Proportional Sampling"
arxiv: "2611.04792"
url: https://arxiv.org/abs/2611.04792
authors: "Ria Shekhawat, Abhijeet Sinha, Yingtao Zhu, Dianbo Liu"
published: 2026-11-03
tagline: "按组内局部密度缩放奖励，让 GRPO 不再只收敛到单一模式"
---

## 一句话概括

DARS 在 GRPO 计算优势之前，按组内样本的"拥挤程度"给奖励打折。这样策略的输出分布会逼近"按奖励比例采样"，不再全部挤到某一个高奖励解上。

## 核心方法

- 问题：最大化期望回报会形成"富者愈富"的循环，越常被采到的结果越被强化，最后坍缩到单一模式。
- 做法：把每个 rollout 的结果映射到一个特征空间（比如图像或文本的 embedding）。在同一组 rollout 内用高斯核估算每个样本附近有多少"邻居"，再把原始奖励除以这个局部密度。扎堆区域的奖励被压低，稀有但高奖励的区域相对获益。
- 改动只在奖励处理这一步，GRPO 的目标函数、裁剪、模型结构都不用动。不需要额外训练密度模型、critic 或辅助损失，开销只是组内两两计算距离。核宽度 h 是唯一的关键超参。

## 关键结果

- 二维导航任务（四个等权高斯奖励峰）：GRPO 把全部概率质量压到一个峰上，召回率只有 0.03。DARS-GRPO 四个峰的质量都接近 0.25，召回率 0.985，JSD 从 0.649 降到 0.041，在多项分布距离指标上与 GFlowNet 相当甚至更好。
- 文生图 prompt 改写：在不同数据集、策略 LM 和奖励设置下，图像和 prompt 的多样性都稳定提升，语义对齐基本保持。

## 为什么值得关注

GFlowNet 能做按奖励比例采样，但要换掉整套训练目标。DARS 只需在现有 GRPO 管线里加几行奖励后处理，就能缓解 RL 后训练中的多样性坍缩，工程上很容易接入。凡是"多个不同答案都有价值"的场景都可以用上，比如创意生成、科学发现、多解推理。需要注意的是，效果依赖 embedding 的质量和核宽度的选择。
