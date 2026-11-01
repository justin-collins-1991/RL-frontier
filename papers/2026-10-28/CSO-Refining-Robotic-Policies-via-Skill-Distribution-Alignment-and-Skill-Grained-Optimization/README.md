---
title: "CSO: Refining Robotic Policies via Skill Distribution Alignment and Skill-Grained Optimization"
arxiv: "2610.38357"
url: https://arxiv.org/abs/2610.38357
authors: "Zhiyuan Xiang, Xiang Deng, Wanjie Tao, Xu Chen, Zhao Jielun, Weili Guan"
published: 2026-10-28
tagline: "先拒绝采样微调稳住编码器，再按技能粒度做RL后训练"
---

## 一句话概括

针对用 VQ-VAE 等把动作离散成“技能”的机器人策略，CSO 提出两阶段后训练：先用成功轨迹做监督微调对齐分布，再以“整个技能”为单位做强化学习，大幅提升成功率。

## 核心方法

- **问题**：离散化带来量化误差，模仿学习策略执行时误差累积、偏离专家分布；直接上 RL 又面临两个坑：成败样本不均衡导致观测编码器更新不稳，以及 token 级 / 整条 episode 级的重要性采样粒度都和“技能”这一实际决策单位不匹配。
- **阶段一 R-SFT（拒绝采样监督微调）**：用高温采样在线探索，只保留成功轨迹（同一初始状态连续 N 次失败就换一个），在这些数据上做监督微调，把“观测→技能”映射对齐到成功分布，然后冻结观测编码器。
- **阶段二 SPO（技能策略优化）**：在冻结编码器的基础上做无 critic 的组内相对优势 RL，对每个完整技能单独计算并裁剪重要性比率，既不像 token 级那样把一个技能拆散，也不像 GSPO 那样全 episode 共用一次裁剪（失败超时的轨迹往往更长，会带来偏差）。

## 关键结果

- LIBERO 四个套件整体成功率从 80.1% 提升到 97.5%（+17.4 个百分点），基于轻量 QueST 式策略。
- 在 RoboTwin2.0 上同样有提升；真机五个单臂任务平均成功率 61.0%。
- 换用 FAST、离散 BEAST 等动作表示同样有效，并优于同预算的固定数据 IQL。

## 为什么值得关注

它把 LLM 后训练里成熟的“拒绝采样 SFT + 组相对 RL”迁移到机器人，并点出关键差异：优化单位应与执行单位（技能）对齐。方法不依赖价值网络、只需稀疏成败奖励，工程上简单，对已有离散动作 tokenizer 的 VLA / 技能策略是低成本的后训练方案。
