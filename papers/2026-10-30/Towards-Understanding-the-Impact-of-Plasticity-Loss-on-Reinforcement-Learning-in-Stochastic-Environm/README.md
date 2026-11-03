---
title: "Towards Understanding the Impact of Plasticity Loss on Reinforcement Learning in Stochastic Environments"
arxiv: "2610.42100"
url: https://arxiv.org/abs/2610.42100
authors: "Philipp Bordne, André Biedenkapp"
published: 2026-10-30
tagline: "噪声环境下，保住网络可塑性能让 RL 学得更稳"
---

## 一句话概括

这是一篇系统性的实证研究，考察环境噪声和神经网络“可塑性丧失”怎样相互作用，并检验保持可塑性的方法能否让 RL 在噪声下仍然学得会。

## 核心方法

作者在 3 个 DeepMind Control 本体感知任务上训练 SAC，并人为加入强度可控的观测噪声和动作噪声。对比的方法有三种：周期性重置（reset）、层归一化（LayerNorm），以及两者叠加。训练过程中，作者定期用一个改进的回归探测任务来测量网络还能“学动多少”，同时跟踪最大 Q 值，以此把渐进的可塑性丧失和 TD 不稳定（Q 值发散）这两种失败原因区分开。

## 关键结果

- 在两个较难的任务上，保持可塑性的方法（尤其是 reset）提升了学习鲁棒性，观测噪声越大，优势越明显。
- reset 叠加 LayerNorm 在所有观测噪声强度下都不如只用 reset。
- 噪声在难任务上会加速可塑性丧失；在简单任务上反而像正则项，有助于维持可塑性。
- 可塑性丧失主要发生在训练早期。在最难的高噪声设置下，主要的失败原因变成了 TD 不稳定，而不是可塑性的逐渐丧失。

## 为什么值得关注

真实场景中传感器有噪声、执行器不精确，而这方面的研究长期缺位。本文把“RL 脆弱”的原因落到了可以测量的可塑性和 TD 不稳定上，对工程实践有直接参考：在噪声环境里优先考虑 reset，不要想当然地把各种技巧叠在一起，同时要监控 Q 值是否发散。
