---
title: "RPEG: Training Reasoning Language Models Scalably and Cost-Effectively"
arxiv: "2611.09207"
url: https://arxiv.org/abs/2611.09207
authors: "Maciej Besta, Leonard Schmidt, Pierre Pang, Patrik Okanovic, Robert Gerstenberger, Torsten Hoefler"
published: 2026-11-06
tagline: "用图表示统一优化 RL 训练流水线的结构与执行"
---

## 一句话概括

ETH SPCL 提出 RPEG：把推理模型的 RL 训练流水线写成一张可搜索的图，同时优化“流水线怎么搭”和“怎么跑”，在 256 张 GH200 上比 ReaL、verl 明显更快。

## 核心方法

- **问题**：PPO/GRPO 每一步都要串起生成、打分、训练三个阶段，牵涉 actor、critic、reward、reference 多个大模型。现有系统通常只优化其中一部分（放置策略、异步、资源调度），可这些选择是互相牵制的。
- **统一表示**：把一个配置拆成“稳态图 + 执行计划”。图描述流水线结构，并把有界异步、actor-critic 共享骨干这类结构选择也当作可调变量；执行计划负责每个调用落到哪些 GPU、用哪种多维并行、怎么切 microbatch。
- **图变换**：分阶段把候选配置展开成带硬件信息的可调度图，包括阶段融合（比如先给已生成完的回复打分）和细粒度子调用调度。
- **解析性能模型**：同时建模计算、通信、显存，以及 GPU/节点/机柜三级层次通信。模型用实测硬件数据校准，因此能快速筛选大量方案，再交给分布式运行时执行。

## 关键结果

- 端到端性能最高达到 ReaL 的 2 倍。
- 与 verl 做受控的同步对比（actor 与 critic 分开）时，单步耗时最多降低 2.48 倍，中位数为 1.49 倍。
- 硬件利用率最多提升 30%；优化后的同步方案比全共置基线快 1.25–1.47 倍。
- 精度与 verl 相差不超过 0.47%；规划器在 2k GPU 规模下开销仍可忽略。

## 为什么值得关注

RL 后训练的算力开销越来越大，agentic 场景下更明显。RPEG 把流水线结构本身也纳入优化，并配上可校准的代价模型，为大规模 RL 训练系统提供了一个系统化的“编译器式”基础，代码已开源，可以直接参考。
