---
title: "CalibraRL: Confidence-Calibrated Reinforcement Learning for Mitigating Hallucinations in RAG"
arxiv: "2610.35142"
url: https://arxiv.org/abs/2610.35142
authors: "Qianchi Zhang, Hainan Zhang, Liang Pang, Hongwei Zheng, Zhiming Zheng"
published: 2026-10-26
tagline: "让奖励看置信度和同题证据，重罚自信的错答、少做多余拒答"
---

## 一句话概括

TruthRL 一类方法用固定的"对 +1 / 错 -1 / 拒答 0"三值奖励。CalibraRL 在此基础上，让奖励同时参考模型自身的置信度和同一问题其他采样的表现，在 RAG 问答中减少幻觉，也避免不必要的拒答。

## 核心方法

在 GRPO 框架下改造奖励，分两部分：

- **作答样本**：在对错奖励之外，加一个 Brier 式校准惩罚。置信度取生成 token 的平均概率。置信度越高却答错，罚得越重；答对但置信度低，也会受到轻微惩罚。
- **拒答样本**：用同组 rollout 里非拒答回答的对错次数，构造一个 Beta 后验，估计"这道题模型其实答得对"的概率。如果模型答这题的准确率很可能低于阈值，就奖励拒答；如果其他采样大多答对了，就惩罚这次拒答。

整套方法直接复用训练时的 rollout，不需要额外标注"模型知不知道这道题"。

## 关键结果

- 在三个 QA 数据集、两个基座模型上，答案精确率和整体真实性都优于 TruthRL 等强基线，幻觉更少。
- 平均 ECE（期望校准误差）下降 30.8%。
- 消融实验显示，置信度惩罚和后验拒答奖励两部分都有贡献。

## 为什么值得关注

"什么时候该说不知道"是 RAG 落地中的老问题。这篇论文给了一个几乎零额外成本的做法：只改奖励函数，就能把校准能力训进模型，不需要额外标注，也不需要多一轮推理。用 Beta 后验来处理"小样本下估计不准"的思路，也可以借鉴到其他基于组采样的 RL 奖励设计里。
