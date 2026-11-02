---
title: "EnvSched: Environment-Aware Scheduling for Rollout-Efficient Agent Reinforcement Learning"
arxiv: "2610.37609"
url: https://arxiv.org/abs/2610.37609
authors: "Sihan Yang, Weichen Bai, Ruichuan An, Yiming Cheng, Zhiyuan Feng, Tianyi Jiang, et al."
published: 2026-10-27
tagline: "按环境调度训练任务，用三分之一步数追平随机选题的 Agent RL"
---

## 一句话概括

在 Agent RL 里，把“任务 + 可执行环境”当作调度单位，在线挑出既有学习信号又能覆盖更多环境的任务，用更少 rollout 训出更强的工具调用模型。

## 核心方法

- **问题出发点**：GRPO 这类组内相对方法里，同一任务多次 rollout 的奖励如果都一样（全对或全错），这个任务就几乎没有梯度信号；而反复在少数环境上训练，模型见到的工具、状态和校验方式又太单一。
- **双关系图**：训练前用 LLM 把每个任务抽取成结构化的操作描述，再建两类边。环境内的边看任务语义、工具、状态和 verifier 是否相似；跨环境的边先去掉具体业务名词，只比较抽象的执行流程（比如“查询→资格校验→关系替换→状态校验”），这样历史经验能在不同业务环境之间迁移。
- **预测 + 调度**：沿两类边传播历史 rollout 统计，预测每个任务当前的组内奖励方差。每个 batch 一半给预测方差高的任务（利用），一半给观测少的环境和任务（覆盖），再加上环境配额和相似度惩罚来避免扎堆、减少冗余。整个过程不需要额外的试探 rollout。

## 关键结果

- Qwen3-8B 在 BFCL-v3、τ-Bench、ACEBench-Agent 上训练 40 步平均得分 48.81，超过随机选题训练 120 步内达到的最高分。
- 在相同训练预算下，不同尺寸的模型都有提升。在 Qwen3-4B 上，选中任务的组内奖励方差从 0.032 升到 0.043，每个 batch 覆盖的环境数从 36.5 升到 46.0。
- 消融实验表明，“奖励区分度”和“环境覆盖”只用其中一个都不够，两者互补。

## 为什么值得关注

现在 Agent RL 的环境规模已经到了几千上万个，rollout 和验证成本很高。已有的在线选题方法大多只看 prompt 或任务本身，没把环境放进来。EnvSched 把数据管理提升到“环境级”，做法轻量，不需要额外 rollout，可以直接接到 GRPO 类训练流程里，对算力有限、想提高 rollout 利用率的团队有直接的参考价值。
