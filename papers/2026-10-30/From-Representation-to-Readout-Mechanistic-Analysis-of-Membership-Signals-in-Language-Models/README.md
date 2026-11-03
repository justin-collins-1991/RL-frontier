---
title: "From Representation to Readout: Mechanistic Analysis of Membership Signals in Language Models"
arxiv: "2610.41445"
url: https://arxiv.org/abs/2610.41445
authors: "Wenxi Dai, Jingyu Hu, Yanting Yang, Mengnan Du"
published: 2026-10-30
tagline: "成员信号由 SFT 写进表征，RL 主要改变读出"
---

## 一句话概括

这篇论文把大模型里的"训练数据成员信号"拆成两部分：表征里存了多少信息，模型读出时又用上了多少。结论是 SFT 两部分都会改，RL 类方法主要改读出。

## 核心方法

- **DUG 指标**：在每一层上，用线性探针衡量隐藏状态里能解码出多少目标 token 信息，记为 Decodable；再看模型自身读出路径实际用到多少，记为 Used；两者之差就是 Readout Accessibility Gap，即"存了但没读出来"的那部分信息。
- **双重差分**：拿"成员 vs 非成员"和"训练后 vs 基座"两组差异相减，扣掉训练对所有样本都有的共同影响，只留下成员特有的变化。
- **激活修补**：用因果干预定位这种成员特有效应是在哪些层形成的。

## 关键结果

- 在没有额外训练的公开模型里，成员身份已经能用线性探针解码，WikiMIA 上 AUROC 最高约 0.78。
- SFT 下，成员特有效应同时出现在可解码信息和读出两端；RL 类成员推断方法则主要体现在读出端。
- 这种效应集中在中间层。
- 在 RLVR 污染场景（奖励和参考答案无关）下，模型行为会变，但基于似然的成员推断信号并不随之上升。

## 为什么值得关注

做 RL 数据污染检测的人需要注意：只看 loss 或困惑度可能漏掉 RLVR 带来的污染，行为层面的信号和似然信号并不同步。另外，"记忆"不能一概而论，区分"存储"和"读出"，能帮助更准确地评估隐私风险，设计更有针对性的审计手段。
