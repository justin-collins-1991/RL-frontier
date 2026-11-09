---
title: "Encoding Memory in World Models with Test-Time Model-Based Reinforcement Learning"
arxiv: "2611.09625"
url: https://arxiv.org/abs/2611.09625
authors: "Maxime Burchi, Fayaz Ali Dharejo, Radu Timofte"
published: 2026-11-06
tagline: "测试时用梯度下降把记忆写进世界模型参数"
---

## 一句话概括

不再靠改架构来增强世界模型的长时记忆，而是在测试时对每个 episode 在线微调世界模型，把这一局的观测“写进”参数里。

## 核心方法

TT-MBRL 基于 Dreamer 系列框架。每个评估 episode 开始时，用训练好的权重初始化一份世界模型、actor 和 critic，并为这一局单独建一个测试时 replay buffer，边交互边做梯度更新。这样每局都有自己专属的世界模型，除了上下文记忆，还多了一份“参数记忆”。几个关键工程细节：
- 每个 mini-batch 一半采自训练 buffer，一半采自当前局的 buffer，相当于正则，防止在少量测试数据上过拟合；
- 冻结编码器和解码器，去掉重建损失，只更新序列网络和动力学部分，这样更省算力，也保住训练时学到的视觉表征。

方法和架构无关，在 RNN（DreamerV3）、Transformer（TWISTER）、SSM（R2I）三类世界模型上都能用。

## 关键结果

- 在自建的 Memory Maze 2D 上，三种架构都有稳定提升；
- 在 3D Memory Maze 基准上取得新的 SOTA；
- 收益随测试时交互步数增加而变大：在 15×15 迷宫上跑 4000 步后，R2I 每步拿到的奖励提升 53.7%；
- 在 DeepMind Control、Atari 100k 这类不考验记忆的任务上，性能基本没有下降。

## 为什么值得关注

它把 test-time training 引入 MBRL，给长时记忆问题提供了“架构设计”之外的另一条路：靠参数而不只是上下文来记住环境结构。做法简单、可以直接叠加到现有世界模型上，对部分可观测、需要长期探索的任务（导航、具身智能）很有参考价值。代价是测试时要额外做梯度计算，部署时需要权衡延迟和算力。
