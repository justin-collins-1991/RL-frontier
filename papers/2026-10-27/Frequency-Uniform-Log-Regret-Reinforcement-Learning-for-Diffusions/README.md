---
title: "Frequency-Uniform Log-Regret Reinforcement Learning for Diffusions"
arxiv: "2610.36758"
url: https://arxiv.org/abs/2610.36758
authors: "Jose Blanchet, Lutong Hao, Renyuan Xu"
published: 2026-10-27
tagline: "时间步再细，扩散控制的值方法RL仍保持对数遗憾"
---

## 一句话概括

决策频率越高，传统遗憾界越差；本文证明在受控扩散的 Euler 离散模型上，值方法 RL 可保持对数遗憾，且常数对步长 δ 一致。

## 核心方法

T 固定时，步长越小、步数 H=T/δ 越多，已有界随 H 多项式膨胀。作者利用单步动作信号随 δ 缩小的尺度关系：critic 动作梯度误差为 δ/√k 时，每步损失约 δ/k，每回合约 T/k，累加后 δ 被抵消。

算法 CD-FQ 面向漂移对未知参数线性、协方差为未知常数的模型：先估计模型，再模拟并倒推拟合受约束 critic，最后贪心决策，靠自身数据持续探索。

## 关键结果

- 通用条件下遗憾为 O(log K)，常数对 δ 一致
- CD-FQ 高概率达到 O(log K·log log K)
- 系数随 T 指数增长，在该问题类下不可避免
- 基准是同步长 Euler 最优策略，不含离散化误差；观测量和计算量仍可能增长

## 为什么值得关注

它把控制难度与时间分辨率带来的代价分开，为选择观测和决策频率提供理论参照。排队实验考察了步长稳定性和策略迁移，但已超出定理假设范围。
