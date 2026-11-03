---
title: "Latent Reasoning in Continuous Space for Unified Multimodal Models"
arxiv: "2610.42149"
url: https://arxiv.org/abs/2610.42149
authors: "Byungwoo Jeon, Yoonwoo Jeong, Hyunseok Lee, Minsu Cho, Jinwoo Shin"
published: 2026-10-30
tagline: "让多模态模型在连续隐空间里思考，生图也能测试时扩展"
---

## 一句话概括

LARC 让统一多模态模型（UMM）不再用离散文字做推理，而是用连续隐状态"想"，再交给生图模块。这样 UMM 生图第一次做到了推理越多、效果越好。

## 核心方法

作者认为，现有带 CoT 的 UMM 生图收益有限，根源在于模态错位：推理在离散 token 空间里做，生图却在连续空间里做，文字链装不下图像需要的密集空间信息。LARC 借鉴 Coconut，把最后一层隐状态直接当作下一步输入，文字段和隐步骤交替出现，整条轨迹再通过 cross-attention 交给生图模块。训练分两阶段：

- **课程式 SFT**：先只训纯文本推理，再逐阶段把文字推理步替换成隐步骤，保证训练稳定；保留的文字段带来随机性，后面做 RL 需要这种 rollout 多样性。
- **信息增益 RL**：奖励来自模型自身，衡量推理轨迹让冻结参考模型对目标图像的预测提升了多少，另加一个防坍缩奖励维持轨迹多样性。整个过程不需要标注好的推理链，也不需要外部评审模型。

## 关键结果

基于 BAGEL，用 100 万条交错 CoT 数据训练。GenEval 总分 0.88，比 BAGEL 高约 7 个百分点，达到 SOTA，Position 和属性绑定两项提升最明显；OneIG-Bench 比 Uni-CoT 高 7.6 分；DPG-Bench 也有提升。在并行和串行两种测试时扩展方式下，表现都优于基于 token 的推理，增加隐推理算力带来单调提升。

## 为什么值得关注

它把"推理应该在哪个空间进行"讲清楚了，并给出了一套可以落地的方案，让 LLM 式的测试时扩展迁移到生图上。另外，用信息增益做自奖励、不依赖外部评审，这个思路也适用于其他难以人工评判的 RL 场景。
