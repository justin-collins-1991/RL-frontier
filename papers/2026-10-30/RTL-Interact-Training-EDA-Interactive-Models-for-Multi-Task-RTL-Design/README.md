---
title: "RTL-Interact: Training EDA-Interactive Models for Multi-Task RTL Design"
arxiv: "2610.41225"
url: https://arxiv.org/abs/2610.41225
authors: "Wenxuan Shi, Yaoyu Zhu, Di Huang, Chongxiao Li, Xiaoyun Zhang, Muxin Song, et al."
published: 2026-10-30
tagline: "让单个模型学会调用 EDA 工具自查自改 RTL 代码"
---

## 一句话概括

训练一个 RTL 专用模型，让它在写硬件代码时自己调用仿真、Lint、综合等 EDA 工具检查，再根据反馈修改，不再需要额外的修复模型或适配器。

## 核心方法

- **多任务数据**：从开源的“规格-RTL”数据对出发，自动构造生成、补全、优化三类任务，由 DeepSeek-V3.2 作为教师生成带工具交互的轨迹，只保留通过验证的轨迹。
- **分阶段 SFT**：先用纯思维链数据学 RTL 推理，再用工具交互数据学怎么发起检查、怎么看懂反馈。
- **PAPO 强化学习**：在 GRPO 基础上，只有最终正确时才发奖励，并按检查方式细分：简洁且一次通过的检查奖励更高，有效的修改也能拿到奖励；同时按任务分组固定采样比例，避免某类任务在训练中被挤掉。

## 关键结果

- CVDP 上，32B 模型 Pass@1 48.7%、Pass@5 68.9%，超过教师 DeepSeek-V3.2；8B 模型 Pass@1 为 44.9%。
- 在 8B 模型上，RL 阶段让 Pass@1 提升 5.4%，平均工具调用次数减少 63.8%。
- 在 VerilogEval v2 和 RTLLM v2 上超过所有 RTL 专用基线。

## 为什么值得关注

在“智能体 + 工具”的 RL 训练中，只看最终对错会让模型反复调用工具。PAPO 用“正确才给奖励，再按交互方式细分奖励”的办法，同时提高了正确率和工具调用效率。这个思路可以迁移到代码、验证等其他依赖工具反馈的领域。
