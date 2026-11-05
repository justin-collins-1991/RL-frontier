---
title: "Language Model Augmented Decision Transformer for Multi-Task Offline Reinforcement Learning"
arxiv: "2611.04031"
url: https://arxiv.org/abs/2611.04031
authors: "Xinbo Zhao, Yuhang Liu, Xin Zhang, Lei Le, Zhaohan Xi, Yu Yang, et al."
published: 2026-11-02
tagline: "同一个 LLM 先按任务描述造轨迹，再当多任务决策 Transformer"
---

## 一句话概括

LaMA-DT 用一个大语言模型同时做两件事：根据自然语言任务描述生成补充轨迹，再作为多任务 Decision Transformer 学策略，专门应对离线多任务 RL 中每个任务数据少、跨任务泛化差的问题。

## 核心方法

- **用文字描述任务**：轨迹数据少，但任务名、目标、环境、数据水平等信息基本都有。论文用固定模板把这些信息写成一段描述，作为 LLM 的条件输入。
- **多目标微调学会生成轨迹**：用 LoRA 微调 LLM，训练目标包括预测动力学（下一状态）、轨迹插值、前向生成、反向生成，另外加两个“任务–轨迹对齐”目标，防止生成的轨迹偏到别的任务。
- **打分过滤**：大量生成候选轨迹，用各目标下的似然综合打分，只留每个任务的 top-K。
- **同一个模型当策略**：复用 LLM 和共享 LoRA，以任务描述为提示、加一个标记数据来源（真实/生成）的 token，在真实数据和增强数据的混合集上训练成 Decision Transformer。

## 关键结果

在 Meta-World 和 MuJoCo 多任务基准上，LaMA-DT 稳定优于 CDS、HarmoDT 等基线，低数据场景下优势最大，说明用语言引导数据增强确实能改善跨任务泛化。

## 为什么值得关注

它把“缺数据”和“难泛化”放到一个 LLM 框架里一起处理，相比依赖辅助数据或隐空间技能学习的方法，对数据量的要求更低。“任务描述 → 生成数据 → 过滤 → 训练策略”这条流程，也适用于机器人等采集成本高的场景。不过 LLM 生成连续控制轨迹在物理上是否可靠、算力开销有多大，还需要再看。
