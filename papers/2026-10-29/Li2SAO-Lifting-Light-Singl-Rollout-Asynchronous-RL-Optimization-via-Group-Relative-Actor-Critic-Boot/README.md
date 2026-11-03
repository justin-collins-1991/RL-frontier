---
title: "Li$^{2}$SAO: Lifting Light Singl-Rollout Asynchronous RL Optimization via Group-Relative Actor-Critic Bootstrapping"
arxiv: "2610.40726"
url: https://arxiv.org/abs/2610.40726
authors: "Zichen Bai, Yanli Wang, Yang Liu, Junhao Shi, Xueqin Liu, Jinguo Sun, et al."
published: 2026-10-29
tagline: "先用组内对比热启动 critic，再切单 rollout GAE 做异步 RL"
---

## 一句话概括

单 rollout 异步 RL（SAO）原本要靠一个闭源、经过大规模预训练的价值模型。本文不用这个模型：训练前期先用 GRPO 式的组内对比把 actor 和 critic 一起带起来，critic 校准好之后再切到单 rollout GAE，补上了冷启动阶段落后的那段差距。

## 核心方法

- **LiSAO 轻量复现**：在开源框架 SLIME 上实现 in-flight 权重更新的异步 RL（权重更新时不丢弃已生成的部分轨迹），沿用 SAO 的单 rollout、跳过环境观测 token 的 GAE 和双边重要性采样截断，只是 critic 直接从策略模型初始化。
- **冷 critic 诊断**：GRPO 在单轮数学推理上更强，LiSAO 在多轮工具调用上更强；但两类任务里 LiSAO 在训练早期都明显落后。原因是 critic 还没校准，GAE 的估计噪声很大。
- **Li²SAO**：critic 冷启动阶段，每个 prompt 采一小组回答，actor 用组内归一化优势训练，critic 拟合减去组均值后的回报；判断 critic 已校准后，一次性切换到单 rollout GAE，此后不再等组。

## 关键结果

在 AIME 2024/2025/2026 上，单轮推理和 ReTool 多轮工具调用两种设置都测了。Li²SAO 在训练早期追平或超过 GRPO，后期的性能上限也进一步提高。

## 为什么值得关注

异步 RL 正在成为 LLM 后训练的主流做法，但 GRPO 需要等同一 prompt 的整组回答，和异步训练天然冲突；单 rollout 方法又卡在没有好的价值模型。本文给了一个不依赖闭源价值预训练、可以复现的折中方案，代码也已开源。对做 agentic RL 的团队来说，"前期组内对比、后期 token 级信用分配"这种分阶段思路可以直接借鉴。
