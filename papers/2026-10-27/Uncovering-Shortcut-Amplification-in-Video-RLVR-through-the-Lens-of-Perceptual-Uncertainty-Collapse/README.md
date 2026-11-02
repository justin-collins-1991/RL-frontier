---
title: "Uncovering Shortcut Amplification in Video RLVR through the Lens of Perceptual Uncertainty Collapse"
arxiv: "2610.37211"
url: https://arxiv.org/abs/2610.37211
authors: "Jiafeng Liang, Xianhao Ou, Tao Ren, Rongchuan Mu, Runxuan Liu, Dandan Tu, et al."
published: 2026-10-27
tagline: "视频RLVR会放大文本捷径，BSPO用双焦自蒸馏拉回视觉依据"
---

## 一句话概括

视频 RLVR 训练会让模型越来越"自信"，但这份自信主要来自文本先验，而不是看懂视频；作者把这种现象叫"感知不确定性坍缩"，并提出 BSPO 加以纠正。

## 核心方法

- **诊断**：作者对比模型在"有视频"和"只有文本"两种输入下的预测熵。RL 训练让有视频时的熵持续下降，但两者的差距（也就是视频真正贡献的那部分信息）也在缩小。梯度方向分析进一步说明，训练中的更新越来越偏向压缩文本先验，与视觉证据的关系越来越弱。
- **BSPO**：一个自蒸馏框架，包含两个信号：
  1. 对比同组 rollout 中的正确与错误轨迹，总结出推理原则，定位对推理关键的 token，做更细粒度的信用分配；
  2. 削弱视频中与任务相关的证据，如果预测几乎不变，说明模型没在看视频，就对其施加惩罚。

  这两个信号只调整原始 RL 优势值的大小，不改变方向。

## 关键结果

在替换关键视频片段的反事实测试集上，标准 GRPO 训练的模型越来越倾向于选择文本捷径答案。BSPO 的视频推理表现优于主流 RLVR 基线，同时保住了视觉带来的熵差，视觉忠实度更高。

## 为什么值得关注

它指出"准确率上涨"可能掩盖了模型并没有在看视频的事实，这个问题是 outcome reward 本身导致的。论文提供了可复用的诊断指标（视觉熵差、视觉特异性压缩），以及一个不需要额外标注、能直接接到 GRPO 上的修正方案，对多模态 RL 后训练有直接参考价值。
