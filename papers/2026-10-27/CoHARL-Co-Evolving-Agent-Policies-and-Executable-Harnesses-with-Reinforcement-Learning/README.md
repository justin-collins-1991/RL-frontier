---
title: "CoHARL: Co-Evolving Agent Policies and Executable Harnesses with Reinforcement Learning"
arxiv: "2610.36469"
url: https://arxiv.org/abs/2610.36469
authors: "Jianwen Chen, Peng Xia, Kaide Zeng, Siwei Han, Zhen-Yu Zhang, Charles Fleming, et al."
published: 2026-10-27
tagline: "用RL让智能体策略与可执行Harness协同进化"
---

## 一句话概括

LLM 智能体靠 harness（管理工具调用和环境反馈的可执行代码）与环境交互。CoHARL 不再把 harness 当作固定不变的外壳，而是在 RL 训练过程中让策略和 harness 一起进化。

## 核心方法

- **问题**：只给固定策略搜 harness，忽略了策略在训练中会变；只在固定 harness 下训练策略，产生训练经验的接口又一直不变。两头各自优化都不够。
- **做法**：基于种群的 RL 框架。维护**一个共享策略**和**一组可执行 harness**：策略同时从各个 harness 产生的 rollout 中学习；另有一个 proposer 读取执行轨迹，在训练过程中直接改写 harness 代码，让接口跟着策略一起变好。

## 关键结果

- SWE-rebench 平均解决率 27.6%，比只搜索 harness 的方案高 6.4 个百分点。
- 在 SWE-bench Verified 和 Terminal-Bench 2.0 上，软件工程和终端类任务都有提升。
- 训练预算相同时，它优于两种基线：RL 前先一次性搜好 harness，以及策略更新与单个 harness 的修改交替进行。

（基于摘要）

## 为什么值得关注

Agent 工程中，harness 往往靠人工反复调，和模型训练是两条分开的线。CoHARL 把 harness 也纳入优化闭环，说明"接口设计"本身就能和策略一起学。种群化方案胜过"先搜后训"和"交替单 harness"，说明多样的 harness 对 RL 训练有实际价值。这对做代码/终端智能体 RL 的团队有直接参考意义。
