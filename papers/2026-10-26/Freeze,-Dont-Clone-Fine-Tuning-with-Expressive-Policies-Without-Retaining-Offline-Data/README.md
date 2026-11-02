---
title: "Freeze, Don't Clone: Fine-Tuning with Expressive Policies Without Retaining Offline Data"
arxiv: "2610.36247"
url: https://arxiv.org/abs/2610.36247
authors: "Sami Nur Islam, Johan Obando-Ceron, Doina Precup, Aaron Courville, Pablo Samuel Castro"
published: 2026-10-26
tagline: "离线数据删除后冻结行为先验，只让价值学习继续改进"
---

## 一句话概括

离线数据无法保留时，在线微调应停止行为克隆（BC），冻结预训练的表达型先验，只继续做价值学习。

## 核心方法

此前多归因于 critic 重新校准，本文指出 actor 侧也会出问题：数据删除后，BC 拟合的只剩有限且多变的在线经验。

做法是冻结 flow 先验，critic 和算法自身的改进机制照常更新：IFQL 由 critic 从候选动作中择优，FQL 继续训练向先验蒸馏的单步 actor，QC 更新动作块价值。

## 关键结果

- 在 7 个 OGBench 域、35 个任务上，冻结先验明显改善三种算法，IFQL 提升最大。
- 继续 BC 会迅速抹除先验，引发表征坍塌和动作多样性下降，使 critic 缺少有用探索。
- BC 权重调到 0.1 到 10 倍仍会崩溃，问题在目标本身而非超参。
- 先验换成简单高斯同样崩溃，必须能表达多峰分布。

## 为什么值得关注

存储、隐私和授权限制常使离线数据无法长期保留。该方法改动小，只需停掉在线 BC，并与 critic 侧的稳定手段互补。
