---
title: "Causal DAG-Guided Reinforcement Learning for Long-Term Physical Activity Maintenance: Using Prior Data to Inform Future Deployment"
arxiv: "2610.36019"
url: https://arxiv.org/abs/2610.36019
authors: "Xueqing Liu, Young Hyun Cho, Bhanu Teja Gullapalli, Predrag Klasnja, Susan Murphy"
published: 2026-10-26
tagline: "用专家因果图驱动个性化在线RL，助力长期运动习惯养成"
---

## 一句话概括

这篇论文为 ADAPT 试验设计了一套在线 RL 系统，每天两次决定是否推送运动建议，目标是改善用户对运动的情感体验，让人长期坚持。

## 核心方法

难点有四个：个人数据少，问卷和传感器常缺失，每周 12 次决策只对应 1 次周度奖励，推送还可能让人反感。作者用一张专家给出的因果 DAG 统一应对：

- 只保留关键的周度状态和中介变量，压缩状态维度；
- 推断缺失的潜在状态，并保留不确定性；
- 同时建模"提升情感"的收益路径和"降低效用感"的负担路径；
- 借助中介变量把周度奖励分配到周内的每次决策上。

此外，作者用以往微随机试验的数据校准了一个模拟器，在部署前比较各种设计。

## 关键结果

主要产出是方法框架和开源的模拟平台，系统计划部署到一项有 75 人参与、为期 36 周的试验中。

## 为什么值得关注

在数据少、奖励延迟、观测不全的场景下，这篇论文给出了一套可复用的思路：用因果知识构造 RL 问题，再用历史数据在上线前验证方案。
