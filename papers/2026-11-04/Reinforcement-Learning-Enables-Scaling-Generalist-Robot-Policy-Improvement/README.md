---
title: "Reinforcement Learning Enables Scaling Generalist Robot Policy Improvement"
arxiv: "2611.06905"
url: https://arxiv.org/abs/2611.06905
authors: "Michal Korniak, Marco Bagatella, Ralf Römer, Michal Nauman, Yarden As, Pranav Vignesh, et al."
published: 2026-11-04
tagline: "多任务在线RL让机器人基座模型在未见任务上也变强"
---

## 一句话概括

机器人 VLA 的 RL 微调不必一次只练一个任务：在大量不同任务上一起做在线 RL，既能整体提升，还能提升没训练过的任务。

## 核心方法

作者先搭了一套评测：在线 RL 只在一部分任务上做，再到未见过的场景和物体类型上测泛化能力。然后在同一框架下比较三类后训练做法：
- **直接微调**：只拿成功轨迹做过滤式 SFT（FSFT）；
- **critic 引导的测试时选择**：训练一个 Q 函数，推理时采样 N 个动作，挑分最高的（BoN）；
- **critic 引导的策略提取**：用 critic 直接更新策略（OGPO，另外也做了 AWR 等消融）。

同时系统地改变训练任务的数量（1→144）和类型，看哪种任务分布能带来泛化。

## 关键结果

- 训练任务越多、越多样，未见任务上的成功率越高；两种 critic 方法都有这个趋势，FSFT 则容易遗忘，泛化差很多。
- OGPO 明显强于 BoN，并且能泛化到新场景，甚至新物体类型。
- 关键是解题策略要多样，光堆任务数量不够；另外，基于价值函数的 RL 是必需的。

## 为什么值得关注

这是较早证明机器人基座模型能做“通才式”在线自我提升的工作之一。它给出了可落地的配方：先学好 critic，再在多样任务上统一做 RL。这样每个新部署任务就不用再单独做一轮在线微调，把 RL 后训练从“逐任务定制”推向“规模化、可复用”的方向。
