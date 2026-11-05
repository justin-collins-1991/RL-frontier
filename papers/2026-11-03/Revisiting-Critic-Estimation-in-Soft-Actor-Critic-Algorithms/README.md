---
title: "Revisiting Critic Estimation in Soft Actor-Critic Algorithms"
arxiv: "2611.05666"
url: https://arxiv.org/abs/2611.05666
authors: "Jan Felix Kleuker, Koen Ponse, Aske Plaat, Thomas M. Moerland"
published: 2026-11-03
tagline: "SAC 换评论家：回放数据上的多步 λ-return 最有效"
---

## 一句话概括

系统比较 SAC 的六种评论家（critic）设计后发现：改学优势函数、改用 soft GAE 都没有带来提升。真正有效的是在回放缓冲区的轨迹片段上训练多步 λ-return 评论家，而且不需要做任何离策略修正。

## 核心方法

策略更新保持不变，只改评论家，沿三个维度展开：
- **学什么**：学 soft Q 值，还是学 soft 优势（显式优势网络 SAC-A，或 dueling 结构 SAC-DA）；
- **目标看几步**：单步 TD，还是包含完整熵项的多步 soft λ-return / soft GAE；
- **数据从哪来**：仿照 PQN 用并行环境做 on-policy 采样，还是从回放缓冲区取轨迹片段（SAC-λ-R、SAC-GAE-R），且不加重要性权重，也不截断 trace。

评测时把超参数当作算法的一部分：每个变体都在 14 个任务上跑完整的随机超参搜索，同时比较回报和对超参的鲁棒性。

## 关键结果

- 学优势函数在回报和鲁棒性上都不比学 Q 值好；
- soft GAE 评论家相比更简单的 λ-return 评论家没有额外收益；
- 在连续控制任务上，收益主要来自"回放"，而不是"更深的回报"：在采样的超参范围内，调大 λ 或拉长 horizon 都没有帮助，换成用回放片段训练才明显提升；
- 回放数据带来的离策略偏差没有抵消数据复用的好处，这一点对包含逐步熵项的完整 soft λ-return 也同样成立。

## 为什么值得关注

这几个改动只涉及评论家，几乎可以零成本接入现有的 SAC 实现。论文给了一个直接可用的工程结论：多步目标可以直接配合回放使用，不必引入 Retrace/V-trace 之类的修正。同时，它也澄清了"优势函数更好学"这一直觉在 SAC 上并不成立。这些结论也可以推广到其他带熵正则的 actor-critic 算法。
