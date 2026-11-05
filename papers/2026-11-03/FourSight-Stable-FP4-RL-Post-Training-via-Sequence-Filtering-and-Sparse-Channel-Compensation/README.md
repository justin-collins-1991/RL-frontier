---
title: "FourSight: Stable FP4 RL Post-Training via Sequence Filtering and Sparse Channel Compensation"
arxiv: "2611.04887"
url: https://arxiv.org/abs/2611.04887
authors: "Yining Wei, Tianyuan Wu, Gu Gong, Yuechen Tao, Yinghao Yu, Xiaowen Chu, et al."
published: 2026-11-03
tagline: "过滤坏轨迹加少量通道补精度，让 FP4 强化学习稳定训练"
---

## 一句话概括

NVFP4（W4A4）下做 RL 后训练容易中途崩溃。FourSight 发现问题集中在少数“跑偏”的轨迹和少数激活通道上，于是只对这两处做针对性处理，基本达到 BF16 的精度，速度几乎不比纯 FP4 慢。

## 核心方法

- **按训推失配过滤序列**：如果 rollout 采出的 token 在训练端算出来的概率接近 0，就把它记为“尾部 token”。一条轨迹里尾部 token 总数太多，或者连续出现很长一段（说明生成已经崩了），就把这条轨迹的 advantage 置零，整条丢掉；偶尔出现几个则放过。GRPO 里同一轨迹的所有 token 共用一个 advantage，所以只裁剪单个 token 挡不住坏梯度。
- **稀疏精度补偿**：RL 训练中权重本身变化很小，量化误差主要来自少数高方差激活通道。每次 rollout 前，每个投影层只把方差最高的 64 个通道保留为 BF16，其余继续用原生 NVFP4。
- **SpliceGEMM 融合算子**：把 BF16 修正直接融合进 NVFP4 GEMM，并为 prefill/训练和 decode 分别设计数据通路，省掉额外的残差计算路径。

## 关键结果

- 在 Qwen3-8B（DAPO）和 Qwen3-1.7B（GRPO）上，验证精度紧跟 BF16。与最强量化基线 QaRL 相比，达到 AIME24 20% 所需步数少 1.76–2.60 倍。
- 用 FP4 部署时，1.7B 模型比 BF16 训练出的模型高 12.7–16.4 个百分点；8B 模型在 10 组基准-引擎组合中有 9 组持平或超过所有量化基线。
- 从 8B 到 120B MoE，每步耗时与纯 FP4 相差不超过 2.3%，比 BF16 最多快 1.40 倍。

## 为什么值得关注

FP4 正逐渐成为大模型训练和部署的主流格式，但 RL 里的训推失配一直是个隐患。这篇论文先定位到误差集中在哪里，再只做低成本的局部修补，避免了“稳定性和效率只能二选一”。两项技术都容易接入 veRL/vLLM 这类现有框架，对想用 FP4 降低 RL 成本的团队有直接参考价值。
