---
title: "Reap: Uncovering Monte Carlo proof search with a lightweight model"
arxiv: "2611.02678"
url: https://arxiv.org/abs/2611.02678
authors: "Yutong Wang, Xuanzhi Ren, Tianyi Xu, Ruitong Liu, Jingda Xu, Peihao Wu, et al."
published: 2026-11-02
tagline: "Lean 原生 MCTS 加 1.7B 模型，开源可观测的定理证明搜索"
---

## 一句话概括

把 AlphaProof 式的策略-价值引导 MCTS 直接写成 Lean 4 tactic，用一个 1.7B 小模型做到同尺寸开源证明器 SOTA，并借助完整搜索日志看清 RL 到底改变了证明策略的哪些方面。

## 核心方法

- **Lean 内原生搜索**：MCTS 主循环跑在 Lean 的 tactic monad 里，节点直接保存 Lean 证明状态，用 AND–OR 树处理多个子目标（OR 选 tactic，AND 要求所有子目标都证完）。推理和 RL rollout 共用同一套实现，训练与评测接口一致。
- **策略-价值共享骨干**：策略负责提出 tactic，价值估计"还剩多少步"，引导搜索偏向更短的证明；另配一个独立的前提检索器。
- **三阶段训练**：基于 Qwen3-1.7B 做继续预训练 → 监督 tactic 学习 → 迭代式 MCTS 搜索 RL，由分布式 Scythe-rl 流水线负责调度。
- **结构化日志**：记录每次模型调用、tactic 执行和耗时，便于事后分析。

## 关键结果

- miniF2F-test pass@32 达 79.9%，是同尺寸开源证明器中的 SOTA，与大得多的模型相比也有竞争力；在另外 4 个基准上迁移效果同样不错。
- 行为层面：随着 RL 推进，顶层证明轨迹变短，模型更常用 have 一类结构性 tactic 引入中间引理，少做反复的局部修补；同时单步 tactic 变得更复杂，一步里打包多个操作和求解器调用。

## 为什么值得关注

高性能证明器大多闭源或算力门槛高，Reap 开源了框架和权重，用小模型就能复现、研究搜索式 RL。它还指出一点：轨迹变短不全是"更聪明"，有一部分是计算被挪进了单步 tactic 里。评估 RL 收益时，搜索步数和执行成本要放在一起看。
