---
title: "What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?"
arxiv: "2611.06483"
url: https://arxiv.org/abs/2611.06483
authors: "Kejian Zhu, Zhuoran Jin, Shangqing Tu, Tianyi Men, Yupu Hao, Jiachun Li, et al."
published: 2026-11-04
tagline: "多轮 Agent RL 强在纠错续航，交互轮数一紧收益就缩水"
---

## 一句话概括

多轮 Agent RL 并没有让每一步决策都更好，它主要提升的是出错后纠正和长程坚持的能力，所以只有在交互轮数充足时才能明显胜过基座模型。

## 核心方法

作者用 Pass@(K,T) 从两个方向评估模型：K 是采样多少条轨迹，T 是每条轨迹最多交互几轮。实验基于 Qwen3-4B/8B 和 GRPO，覆盖 DeepCoder-MT、BFCL、InterCode-SQL、FrozenLake 四个任务。他们在相同状态下对比 RL 模型和基座模型的单步动作质量，并做了对数似然和训练动态分析。最后讨论了过程监督的利弊，并提出 BudgetMix RL：训练时随机改变交互轮数预算。

## 关键结果

- 和单轮 RL 不同，多轮 RL 能把 Pass@K 推到基座模型的能力边界之外。
- T 越大，RL 的优势越明显；轮数收紧后优势缩小，有些任务上甚至不如基座。
- 单步动作质量没有全面提高，有时还会下降。RL 的优势主要出现在出错之后和轨迹后半段。
- RL 生成的单个动作在基座模型看来也算合理，提升主要来自把这些动作串成完整长轨迹的能力。
- BudgetMix RL 在不同预算下都更稳，也减轻了单步质量下降的问题。

## 为什么值得关注

只看轨迹成功率，会掩盖一个部署风险：如果线上对交互轮数有严格限制，或者错误不可逆，RL 模型的收益可能会消失。论文提醒我们，评测 Agent 时要同时扫描交互预算这个维度。BudgetMix 改法简单，几乎不增加成本，可以直接加到现有训练流程里。
