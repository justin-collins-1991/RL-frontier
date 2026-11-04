---
title: "ModelBlaster: Closing the Performance Gap through Learning-Augmented Agents Across Models, Kernels and Hardware Backends"
arxiv: "2611.04104"
url: https://arxiv.org/abs/2611.04104
authors: "Shengjun Kris Dong, Dima Nikiforov, Sahil Modi, Sana Damani, Edward C Lin, Siva Kumar Sastry Hari, et al."
published: 2026-11-03
tagline: "用可持续积累的经验库让 LLM 智能体跨硬件优化算子与整模型"
---

## 一句话概括

ModelBlaster 不更新模型权重，而是把“优化经验”存进一个持久知识库当作策略。这样 LLM 智能体能在不同算子、不同模型、不同硬件之间复用经验，做算子级和整模型级的性能优化。

## 核心方法

- **记忆增强的上下文内 RL（MAIC-RL）**：策略就是一个结构化知识库，记录“性能状态 → 尝试的动作 → 实测结果/约束”，失败的尝试也会记下来。
- **Actor-Critic 文本梯度**：Actor 参考知识库生成代码改写；Critic 根据编译、正确性、profiling 和性能差距写出文字点评，再用这些点评更新知识库。
- **图与算子联动**：从 PyTorch 计算图出发提出融合、切分等改写，交给算子智能体生成 kernel。只有验证后的 kernel 确实带来整模型提速，图改写才会保留。
- **一套框架覆盖多后端**：CUDA、OpenCL、RVV 共用同一套流程和知识库格式，每个后端只需单独实现代码下沉和测量这两层。

## 关键结果

- KernelBench L1/L2/L3 相对 PyTorch 的几何平均加速分别为 1.85×、5.58×、5.18×；在 B200 上跑 SOL-ExecBench，加速 1.69×。
- 高通 Adreno GPU 上，比厂商 SDK 快 5.8×，比 TVM 快 1.7×。
- RISC-V 向量核上跑 70 个问题，比 ExecuTorch+XNNPACK 快 2.7×。

## 为什么值得关注

它把 RL 的“策略改进”从更新权重换成了更新外部记忆，不需要针对目标硬件的训练数据，所以适合资源少的新硬件。经验能跨任务、跨硬件迁移，也解决了现有 kernel 智能体“每个任务从零开始”的问题。代码已开源。
