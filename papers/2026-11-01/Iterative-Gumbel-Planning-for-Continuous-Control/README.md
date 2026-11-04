---
title: "Iterative Gumbel Planning for Continuous Control"
arxiv: "2611.02236"
url: https://arxiv.org/abs/2611.02236
authors: "Shaohuai Liu, Weirui Ye, Yilun Du, Le Xie"
published: 2026-11-01
tagline: "按维离散策略加迭代Gumbel搜索，根治高斯蒸馏的方差膨胀"
---

## 一句话概括

把连续控制中的高斯策略换成“每个动作维度独立的离散分布”，让 MuZero 式搜索的输出能被策略直接吸收，再用多轮 Gumbel 搜索反复精炼，在高维控制上取得 SOTA。

## 核心方法

作者指出，搜索只评估有限个候选动作，而连续 RL 通常用高斯策略。把搜索选出的“赢家动作”蒸馏回高斯时，为了覆盖离均值较远的样本，策略会被推着放大方差，最终拉低回报。IGP 的做法是：把每个动作维度离散成若干档，用按维分解的类别分布表示策略，参数量只随维度线性增长；每一维用 Gumbel Top-K 无放回采样，再按排名拼成 K 个联合候选动作；并借鉴 MPPI，在同一状态上多轮搜索、反复更新根策略。这样就消除了投影误差，只剩一个随网格精度可控的离散化误差。

## 关键结果

基于 EfficientZero-Multitask 实现，在 DMControl 和 HumanoidBench 的高维运动与人形全身控制任务上，总体表现和样本效率都达到 SOTA，超过 TD-MPC2、BRC 等强基线；评估时动作序列的时间方差更低，控制更平滑。

## 为什么值得关注

它清楚解释了搜索类方法在连续控制上为什么不如在离散领域那么强，并给出了简单、可扩展的解法。动作更平稳这一点，对真实机器人部署也很有价值。
