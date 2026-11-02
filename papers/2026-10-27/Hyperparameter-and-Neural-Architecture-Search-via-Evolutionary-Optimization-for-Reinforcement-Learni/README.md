---
title: "Hyperparameter and Neural Architecture Search via Evolutionary Optimization for Reinforcement Learning: HPNAS-RL"
arxiv: "2610.36882"
url: https://arxiv.org/abs/2610.36882
authors: "Nihal Acharya Adde, Hanno Gottschalk"
published: 2026-10-27
tagline: "用进化算法同时搜网络结构和PPO超参，让自动驾驶RL更强更小"
---

## 一句话概括

把"网络结构搜索"和"超参数调优"放进同一个进化算法里一起做，用来自动设计自动驾驶场景下的强化学习智能体。

## 核心方法

- **双分支进化**：一支沿用作者此前的 EMNAS，搜索策略网络中负责视觉特征提取的卷积部分（cell 式结构，候选算子包括可分离卷积、空洞卷积、池化、跳连等）；另一支调 PPO 的关键超参，如学习率、batch size、折扣因子、时间跨度。
- **统一多目标选择**：两支共享同一套适应度评估，同时追求奖励更高、计算量更低、参数更少，用 NSGA-II 保留一批折中最优的候选。
- **提效手段**：多个候选并行训练评估，并用 teacher-student 策略迁移，让新个体继承已有策略，减少从零训练的开销。

## 关键结果

在 Unity3D 三车道驾驶仿真中（输入为语义分割图像，输出未来轨迹点），联合搜索稳定优于只搜结构的 EMNAS：累计奖励更高、模型参数更少、训练更稳定。（摘要与已给正文中没有具体数值。）

## 为什么值得关注

RL 对超参极其敏感，只搜结构很容易被一组糟糕的超参拖累。这篇工作说明结构和训练超参应当一起优化，给"自动化设计 RL 智能体"提供了一个工程上可落地的思路。不过实验只覆盖单一仿真任务，基线也只有自家的 EMNAS，泛化性还需要更多验证。
