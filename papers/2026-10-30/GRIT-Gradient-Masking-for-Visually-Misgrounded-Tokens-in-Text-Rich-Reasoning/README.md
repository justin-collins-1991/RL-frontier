---
title: "GRIT: Gradient Masking for Visually Misgrounded Tokens in Text-Rich Reasoning"
arxiv: "2610.41629"
url: https://arxiv.org/abs/2610.41629
authors: "Chanseul Cho, Noori Bae, Dongheon Lee, Youngmin Ro"
published: 2026-10-30
tagline: "屏蔽看错图的 token 梯度，让 VLM 的 RLVR 不再奖励蒙对的推理"
---

## 一句话概括

VLM 在文字密集图像上做推理时，常常中间步骤看错了图却碰巧答对。GRIT 在 RLVR 训练中找出这些"看错"的 token，并屏蔽它们的梯度，不让错误的视觉感知被一起强化。

## 核心方法

- **发现问题**：作者把"答案对、但中间步骤看错图"的现象称为 CVMR。标准 RLVR 只看最终答案对不对，会把这类推理和真正看对图的推理一样奖励。
- **定位错误 token**：token 级分析发现，CVMR token 的注意力分布和看对图的 token 有系统性差异，可以据此把它们识别出来。
- **梯度屏蔽**：训练时对这些看错图的 token 屏蔽梯度（即标题中的 Gradient Masking），把视觉 grounding 信号加进 RLVR，只强化真正"看对了"的推理。
- **新基准 GRIT-Bench**：可以按文本长度和推理深度两个维度系统评测文字密集型推理。

## 关键结果

相比现有 RLVR 方法，GRIT 的推理准确率和视觉 grounding 准确度都有显著提升。（基于摘要）

## 为什么值得关注

它指出了结果奖励的一个盲区：答案对不等于过程对。对多模态 RL 来说，"蒙对"会被持续强化。GRIT 不需要额外标注过程奖励，只用模型自身的注意力信号做 token 级的信用分配，成本低、易接入。对做文档、图表、OCR 类推理的团队有直接参考价值。
