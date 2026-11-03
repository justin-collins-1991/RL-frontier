---
title: "S3AC: Stabilized, Selective, and Scalable Actor-Critic for LLM Reasoning"
arxiv: "2610.35518"
url: https://arxiv.org/abs/2610.35518
authors: "Shuo Shen, Guangran Cheng, Chengqi Lyu, Xiangsen Wang, Yanan Sun, Wenwei Zhang"
published: 2026-10-26
tagline: "把 critic 训稳，让长 CoT 的 RLVR 重回 Actor-Critic"
---

## 一句话概括

给出一套能把 critic 训稳的实用方案，让长思维链 RLVR 重新用上 Actor-Critic：critic 提供逐 token 的信用分配和按题目给出的基线，还能在生成之前帮忙挑题。

## 核心方法

- **critic 训练配方**：用强弱不同的多个策略采样轨迹来预训练 critic，覆盖长短不一、对错都有的回答；value head 用很小的初始化，critic 的梯度裁剪阈值从 1 提高到 10，避免新初始化的 head 在早期主导梯度、把主干更新压得太小。
- **逐 token 优势**：在线更新的 critic 配合 GAE 计算 token 级优势，同一条回答里不同推理步骤拿到的信号可以不同；actor 侧用 CISPO 目标。
- **DAPS 选题**：生成前用 critic 对题目的初始价值估计难度，再结合历史通过率，优先选中等难度的题。不需要离线初始化难度，也不用额外训练难度模型，组采样和单采样都能用。

## 关键结果

- 在 1.5B 到 397B 的稠密模型和 MoE 模型上，组采样设置下平均性能都有提升；35B 在 7 个评测集、397B 在 5 个评测集上全部超过 GRPO-X。
- 35B 单采样（每题只生成一条回答）训练能持续保持稳定，而测试的几种 critic-free 基线在初期提升后都出现退化。
- 与均匀采样相比，DAPS 在两种采样设置下都带来进一步提升，组过滤丢掉的轨迹也更少。

## 为什么值得关注

现在主流做法默认用 GRPO 这类 critic-free 方法。这篇工作说明，只要解决好轨迹覆盖不足和 value head 主导早期梯度这两个问题，critic 在超大模型上同样可以训稳。它带来的细粒度信用分配、不依赖组采样的单采样训练，以及生成前选题，对降低 rollout 成本、缓解长尾等待都有直接的工程价值。
