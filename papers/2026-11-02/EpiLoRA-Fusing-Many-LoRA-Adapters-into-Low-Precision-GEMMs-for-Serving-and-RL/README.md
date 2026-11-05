---
title: "EpiLoRA: Fusing Many LoRA Adapters into Low-Precision GEMMs for Serving and RL"
arxiv: "2611.03899"
url: https://arxiv.org/abs/2611.03899
authors: "Hieu Tran, Hong Yu"
published: 2026-11-02
tagline: "多LoRA融入低精度GEMM尾声，服务与RL共用FP8底座"
---

## 一句话概括

基座模型换成 FP8/FP4 后，矩阵乘变快了，LoRA 的开销却没变，在每步解码里占比越来越高。EpiLoRA 把多个租户的 LoRA 计算塞进低精度 GEMM 内部，把这部分延迟基本藏掉；同一份 FP8 权重还能直接拿来做 LoRA 强化学习训练。

## 核心方法

- **关键观察**：GEMM 只在最后写输出的阶段（epilogue）才需要 LoRA 的降维结果。所以先启动降维 kernel，再用 Hopper 的 PDL（programmatic dependent launch，让后一个 kernel 提前开跑）启动 GEMM，并把等待点从开头挪到 epilogue 前面。这样 GEMM 读权重的主循环和降维同时进行，最后在 epilogue 里按行分组，加上各租户各自的升维结果。
- **多租户与精度一致**：同一个输出 tile 里可能混着不同 adapter 的 token，要分别处理；激活量化方式和 vLLM 完全一致。整个系统以 vLLM 插件形式提供，支持 CUDA Graph 和张量并行。
- **RL 训练**：trainer 直接在推理引擎的 FP8 权重上做前向和反向，不再单独保留一份 bf16 副本。如果引擎也把激活保持在 bf16（W8A16），rollout 和训练两边的分布基本对齐。

## 关键结果

- Hopper 上单请求解码：每 token 时延是 vLLM 最快配置的 0.76–0.88 倍，也快于 SGLang 和 TensorRT-LLM，72B 模型上同样领先。
- 32 个租户时：9 组 GPU–模型组合中有 7 组吞吐达到 vLLM 的 1.05–1.09 倍。
- 一张 48GB 的 L40S 就能对 27B 模型做 LoRA RL 训练。

## 为什么值得关注

多租户 LoRA 服务和 LoRA RL（训练即服务）正在变成主流部署方式。这篇论文指出，低精度时代真正的瓶颈是 LoRA 那几个小 kernel 的延迟，并给出了可以直接用的工程方案。对 RL 来说，省掉 bf16 副本能大幅降低显存门槛；精度对齐后的引擎还减少了对重要性采样修正的依赖，是“训推一体”方向一个很实用的参考。
