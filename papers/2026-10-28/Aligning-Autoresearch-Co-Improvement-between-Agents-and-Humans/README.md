---
title: "Aligning Autoresearch: Co-Improvement between Agents and Humans"
arxiv: "2610.38882"
url: https://arxiv.org/abs/2610.38882
authors: "Tianjian Li, Chuanyang Jin, Seungone Kim, Tong Chen, John Hoffman, Yoram Bachrach amd Pedro Rodriguez, et al."
published: 2026-10-28
tagline: "让科研智能体与人类协同进化，而非单打独斗"
---

## 一句话概括

FAIR 团队认为，科研智能体与其完全自主地自我改进，不如和人类一起做研究（co-improvement）。论文给出了配套的评测方法和训练方法。

## 核心方法

- **AutoBenchmark**：让智能体端到端地造 benchmark。它根据解题模型的轨迹和得分、加上 LLM 评审对质量的打分，反复修改题目。另外用不参与循环的外部解题模型来检查它有没有专门针对循环内模型“刷难度”。实验对比了四种人类参与程度：无反馈、一句话方向、详细规格、详细规格加过程指导。
- **HackBench**：专门测智能体能否发现并定位 reward hacking。
- **人类模拟器做 RL**：训练时用模拟的人类来代替真人，教智能体和人更好地交互。
- **专家对齐的 rubric RL**：用和人类专家判断一致的评分细则做奖励，提升模型写作和沟通的质量。

## 关键结果

- 没有人类参与时，智能体造出的 benchmark 接近饱和，解题模型得分超过 80。
- 人类给出的指导越具体，题目越难：详细指导能让解题得分减半，一句话方向只有很小的帮助。可见人类在构思阶段仍然很关键。
- 在 HackBench 上，现有智能体没有对齐，定位 hack 的能力也不够。

## 为什么值得关注

大家都在关注自动科研和递归自我改进，这篇论文用实验说明了人类在其中的作用。它把“和人协作”当成可以训练、可以评测的能力，给减少 reward hacking、做更安全的科研智能体提供了一套可以落地的方案。
