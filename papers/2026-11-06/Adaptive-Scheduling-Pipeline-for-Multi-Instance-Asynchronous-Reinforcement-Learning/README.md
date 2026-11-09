---
title: "Adaptive Scheduling Pipeline for Multi-Instance Asynchronous Reinforcement Learning"
arxiv: "2611.08864"
url: https://arxiv.org/abs/2611.08864
authors: "Salah Chikhi, Luis Zuin, Entong Li, Zeng Li"
published: 2026-11-06
tagline: "离线调度 rollout，消除三类气泡，异步 RL 提速 3 倍"
---

## 一句话概括

ASP 是一个面向大模型异步 RL 的离线 rollout 调度器。它在训练开始前做一次预处理，同时减少多推理实例 rollout 中的三类空转（"气泡"），并且让生成样本以平稳的节奏送到训练端。

## 核心方法

- **三类气泡**：同一个 minibatch 里回复长短不一，短的先写完只能干等长的（padding 气泡）；少数超长输出拖住解码尾段（skewness 气泡）；如果简单按长度排序派发，会先送短批、后送长批，训练队列前期堆积、后期断供（sorting 气泡，这是本文新提出的一类）。
- **三步离线调度**：先预测每条 prompt 的输出长度，再用动态规划把长度相近的 prompt 组成 minibatch，最后把这些 minibatch 重新排成总负载均衡的批组，使样本到达训练端的速率保持稳定。
- **异步架构**：训练单元、生成单元、控制单元三者解耦，用训练队列做缓冲和反压，并定期刷新权重，让策略滞后可观测、有上界。

## 关键结果

- 端到端吞吐最高提升 3.22×；迭代时间相比 MindSpeed-RL 最多减少 76.8%，相比 verl 最多减少 62.5%。
- 只看调度这一环，平均迭代时间减少 10.9%。增加生成资源时，ASP 的扩展性比两个基线更好，在有界滞后的条件下没有看到明显的收敛退化。
- 已用于一个内部电信领域的后训练流程，训练周期从三个多月缩短到约两个月。

## 为什么值得关注

它指出了多实例 rollout 中"局部效率"和"全局供给节奏"之间的冲突：只按长度排序虽然局部更快，却会让训练端时而积压、时而断供。ASP 的解法完全离线，不增加在线开销，并且可以和 StreamRL、AReaL 等路由或 staleness 控制方案叠加使用，工程上容易落地。
