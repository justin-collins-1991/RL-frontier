---
title: "Learned Terminal Costs for Short-Horizon Model Predictive Control of Autonomous Trucks in Interactive Highway Traffic"
arxiv: "2610.40257"
url: https://arxiv.org/abs/2610.40257
authors: "Hooman Hamze, Benjamin Houshmand, Deepthi Pathare, Erik Börve, Morteza Haghir Chehreghani, Nikolce Murgovski"
published: 2026-10-29
tagline: "用DQN价值函数当终端代价，让短视MPC安全开卡车"
---

## 一句话概括

把预训练 DQN 学到的价值函数当作 MPC 的终端代价，让只看几步的短视域 MPC 也能做出有远见的高速卡车驾驶决策，同时保留 MPC 的约束处理能力。

## 核心方法

- **MPC 负责"守规矩"**：在离散化的状态-动作网格上用动态规划求解有限视域 MPC，同时决定加减速和是否变道；对周车预测的不确定性用机会约束处理，表现为随预测步数增大的安全距离。
- **RL 负责"看得远"**：离线在 SUMO 中训练 DQN，把它的价值估计直接塞进 DP 反向递推的末端，代替传统的零或手工终端代价。
- **对照组**：纯 MPC（零终端代价）、用基础策略往后模拟估计终端代价的 Rollout 方法、直接执行 DQN 的纯 RL。

## 关键结果

在周车会对自车做出反应的三车道 SUMO 高速场景中跑 100 个带噪声的回合：
- 视域只有 1 步时，纯 MPC 碰撞率 86%，混合方法为 0。
- 混合方法在 3 步视域时综合最佳（零碰撞，代价 329），优于 5 步纯 MPC（代价 754），安全代价低约 59%。
- Rollout 只能部分缓解问题；把模拟长度从 10 步拉到 20 步反而更差，因为基础策略越往后预测越不准。
- 纯 RL 虽然不撞车，但开得保守、速度偏低、加减速不平顺。

## 为什么值得关注

它为"MPC + RL"给出了一种清晰的分工：RL 不直接出动作，只提供远期价值估计。DQN 本身偏保守、单独使用效率不高，但正是这种谨慎让它适合做终端代价。结果是用 3 步这样便宜的短视域就能达到甚至超过长视域的效果，对需要实时计算的重载卡车自动驾驶比较实用。这也是把学习型终端代价用于离散变道决策、并在周车会做出反应的多车交通中验证的较早工作之一。
