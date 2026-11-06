---
title: "FewStepRL: Fine-tuning Few-step Diffusion Models with Reinforcement Learning"
arxiv: "2611.08240"
url: https://arxiv.org/abs/2611.08240
authors: "Haitao Lin, Minsi Ren, Yang Li, Xingtong Ge, Zheyuan Hu, Peiyan Hu, et al."
published: 2026-11-05
tagline: "把主流扩散 RL 目标系统性迁移到少步生成模型的统一框架"
---

## 一句话概括

腾讯混元与西湖大学提出一套通用方法，把 FlowGRPO、AWM、DiffusionNFT、DiffusionOPSD、ReFL 等扩散 RL 算法系统地改造到 1~4 步的少步模型上，大幅降低 RL 训练中 rollout 的开销。

## 核心方法

现有扩散 RL 默认模型预测“瞬时速度”并用几十步采样，而少步模型（MeanFlow、DMD/AnyFlow 蒸馏）学的是“区间平均速度”，直接套用会出问题。作者分三步解决：
- **转换**：把各类目标（基于密度、速度或奖励）统一换算成对干净样本 x 的预测，让不同方法可以直接比较；
- **分解**：证明这些目标的梯度都可写成“向参考策略回归”加“奖励增强”两项，不同方法只是选的锚点和权重不同；
- **适配**：用少步模型在轨迹终点或沿切线计算锚点，所需的瞬时速度由网络自身（MeanFlow）或辅助网络（DMD）给出。

所有方法放进同一套模块化代码，新变体只需改锚点和权重。

## 关键结果

- 在 AnyFlow 蒸馏的 SD3.5-Medium（图像）和 Wan2.1-1.3B（视频）上，改造后的版本均优于“直接拿平均速度替代瞬时速度”的朴素做法；
- 奖励可微且梯度不贵时，基于奖励梯度的方法最好，单用 ReFL 就是强基线；否则 DiffusionNFT 类方法迭代次数少就能达到高奖励；
- DMD 变体在图像上单步更快、视频上更慢，且往往伴随更大的泛化退化；
- 推理时增加步数整体无系统性提升，仅部分样本在 2~4 倍步数下肉眼可见变好。

## 为什么值得关注

RL 后训练的主要成本来自 rollout，视频场景尤甚。少步模型 + RL 是降本的自然路线，但此前都是一个算法单独适配。本文给出统一视角和开源代码，并附带“该选哪种方法”的实操建议，对做图像/视频生成对齐的团队有直接参考价值。
