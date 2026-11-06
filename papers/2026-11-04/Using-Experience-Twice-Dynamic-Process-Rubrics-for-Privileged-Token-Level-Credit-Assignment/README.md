---
title: "Using Experience Twice: Dynamic Process Rubrics for Privileged Token-Level Credit Assignment"
arxiv: "2611.06543"
url: https://arxiv.org/abs/2611.06543
authors: "Shumao Wu, Kongcheng Zhang, Jianqiang Huang, Baisheng Lai"
published: 2026-11-04
tagline: "自生成过程评分标准作特权信息，实现token级信用分配"
---

## 一句话概括

ORSD 让策略模型对比自己同一批轨迹的成败，总结出自然语言的“过程评分标准（rubric）”，再把它当作特权上下文，给 GRPO 补上 token 级的信用分配。

## 核心方法

- **在线生成 rubric**：同一任务采样一组轨迹后，当前策略根据“成功和失败的轨迹有什么不同”，独立生成多份候选 rubric 包（如“先核验再行动”“不要重复操作”）。
- **按对齐度挑选**：冻结的验证器给每条轨迹逐项打分，选出满足度与任务成败相关性最高的那一份，过滤掉低质量 rubric。
- **特权重放算信用**：把选中的 rubric 加进上下文，重新计算原轨迹每个 token 的对数概率。“加了 rubric 后更可能出现”的 token 获得正向加分，反之扣分。这个差值叠加到 GRPO 的轨迹级优势上。rubric 只在训练时使用，推理时不需要。

整个过程复用已有轨迹，不需要额外 rollout 或环境交互。

## 关键结果

在 ALFWorld 和 WebShop 上，用 Qwen3-1.7B 和 Qwen3-4B 测试。环境交互预算相同时，ORSD 比 GRPO 提升更快，最终成功率也更高。消融实验表明，“在线生成 rubric”和“rubric–奖励对齐筛选”都有贡献。

## 为什么值得关注

稀疏奖励下，同一条轨迹里的好决策和坏决策拿到的是同一份信号，这是 Agent RL 的老问题。ORSD 不训练过程奖励模型，也不依赖人工预设标准，而是让模型从自身经验中提炼标准，并用自蒸馏把它转成 token 级信号。rubric 会跟着策略一起演化，额外开销基本只有推理计算。这为多轮 Agent 的细粒度信用分配提供了一条低成本思路。
