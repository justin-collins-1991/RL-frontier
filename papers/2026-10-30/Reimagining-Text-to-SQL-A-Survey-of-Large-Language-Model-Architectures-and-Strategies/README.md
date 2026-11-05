---
title: "Reimagining Text-to-SQL: A Survey of Large Language Model Architectures and Strategies"
arxiv: "2611.00171"
url: https://arxiv.org/abs/2611.00171
authors: "Shikhar Dave, Bhaskarjit Sarmah, Stefano Pasquali"
published: 2026-10-30
tagline: "用五大范式梳理LLM时代Text-to-SQL，首次把RL推理单列一类"
---

## 一句话概括

这是一篇 LLM 时代 Text-to-SQL 的综述，覆盖 2022–2026 年 100 多篇论文和技术资料，把方法归入五大范式，并首次把强化学习（RL）推理模型单独列为一个方向。

## 核心方法

作者提出了统一的五范式分类：上下文学习（如 DIN-SQL、DAIL-SQL）、全参/参数高效微调、多智能体与工具增强编排（如 MAC-SQL、CHASE-SQL、ReFoRCE）、检索增强生成，以及基于执行结果奖励的强化学习（如 Arctic-Text2SQL-R1、SQL-R1、Reasoning-SQL、ExCoT）。每个系统还从三个角度刻画：单体还是模块化、零样本/微调/RL 哪种监督方式、直接解码还是分步推理。此外，文章专门讨论了生产落地中的语义层（知识图谱、Wren AI 的 MDL）、负责任 AI（隐私、安全、治理），以及缓存、schema 管理、推理调度等工程实践。

## 关键结果

- 2025 年以来，用 GRPO、可验证奖励（RLVR）、DPO 等训练的 RL 推理模型，已占据 BIRD 榜单前列。
- 撰写时 BIRD test 的最好公开成绩来自 Agentar-Scale-SQL，执行准确率 81.67%，它结合了测试时扩展和多种范式。
- 2026 年出现了多轮智能体 RL 和以数据为中心的 RL 方法（SQL-Trail、TRUST-SQL、ReViSQL）。
- 尚未解决的问题包括：大规模 schema、问题表述有歧义、值对齐（value grounding）、跨领域泛化，以及推理效率。

## 为什么值得关注

Text-to-SQL 的结果可以直接执行验证，是 RLVR 天然适合的试验场。这篇综述把 SQL 方向 RL 的进展（奖励设计、GRPO、多轮智能体 RL）放到同一框架里比较，方便做 RL 推理的研究者找到基线、借鉴奖励设计。关于语义层和部署实践的章节，也对企业落地有直接参考价值。
