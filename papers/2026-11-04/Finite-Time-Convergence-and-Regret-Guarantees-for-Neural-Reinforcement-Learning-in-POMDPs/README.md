---
title: "Finite-Time Convergence and Regret Guarantees for Neural Reinforcement Learning in POMDPs"
arxiv: "2611.07069"
url: https://arxiv.org/abs/2611.07069
authors: "Jingjuan Huang, Zhiyao Zhang, Alvaro Velasquez, Nathaniel D. Bastian, Jia Liu"
published: 2026-11-04
tagline: "首个有限记忆POMDP下神经网络RL的亚线性遗憾保证"
---

## 一句话概括

用“最近 ℓ 步历史”把部分可观测问题近似成普通 MDP，再用神经网络 critic + 策略镜像下降求解，并首次在真实轨迹采样（非 i.i.d.）下证明了有限时间的亚线性遗憾。

## 核心方法

- **有限记忆超状态**：只保留最近 ℓ 个“动作-观测”对作为超状态，相当于理论化的“帧堆叠”。在滤波稳定性假设下，作者给出逐点的价值近似误差界，误差随窗口长度指数衰减，奖励和转移的失配也由同一误差控制。
- **神经 TD 评估**：critic 用 POMDP 真实轨迹做标准 TD 学习，目标是超状态 MDP 的 Bellman 不动点。针对“采样来自 POMDP、目标定义在代理 MDP”的模型失配和样本时间相关性，作者设计了新的 Lyapunov 分析，把误差拆成轨迹采样、网络拟合、部分可观测三部分。
- **策略镜像下降（PMD）**：PMD 统一了 NPG/TRPO/PPO 等算法。作者把神经 critic 的误差界接入 PMD，再借助集中性假设处理策略迭代过程中访问分布不断漂移的问题。

## 关键结果

- 证明了神经 critic 的有限时间误差界，不依赖 i.i.d. 采样假设。
- 整体算法相对最优 POMDP 价值取得有限时间亚线性遗憾，遗憾界清楚拆分为 critic 误差、记忆截断误差和策略优化误差三项。
- 数值实验与理论趋势一致。

## 为什么值得关注

此前的理论要么只覆盖线性函数近似，表达力不够，会留下无法消除的偏差；要么假设 i.i.d. 采样，与实际的 on-policy 轨迹不符。本文让“帧堆叠 + 神经网络 + PPO 类算法”这一常见工程做法有了较完整的理论依据，也给窗口长度的选择提供了“精度换内存”的量化参考。对机器人、自动驾驶、Agent 等部分可观测场景来说，这是理论走向实践的重要一步。
