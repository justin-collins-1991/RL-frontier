---
title: "Statistical Foundations of Reinforcement Learning: A Non-Asymptotic Perspective"
arxiv: "2610.41903"
url: https://arxiv.org/abs/2610.41903
authors: "Yuxin Chen, Yuejie Chi, Jianqing Fan, Gen Li, Yuting Wei, Yuling Yan"
published: 2026-10-30
tagline: "系统梳理有限样本下强化学习样本复杂度理论的专著"
---

## 一句话概括

这是一本近 300 页的专著，系统回答一个问题：在数据有限时，强化学习到底需要多少样本才能学好，以及哪些算法能做到最省。

## 核心方法

全书基于表格型 MDP，按“数据怎么来”把问题分成三类：可随意采样的模拟器（生成模型）、边交互边学的在线 RL，以及只能用历史数据的离线 RL。每一类都对比基于模型（先估计环境再规划）和无模型（直接学价值或策略，如 TD、Q-learning）两种路线。分析主线是非渐近的样本复杂度：先给出任何算法都绕不过的下界，再设计或分析能贴近下界的算法。在线部分以 UCB 式乐观探索（UCB-VI、MVP）为核心，离线部分则用 LCB 式悲观估计来应对数据覆盖不足。

## 关键结果

- 三种采样设定下都给出了极小极大最优（minimax-optimal）的算法，并强调不需要很大“预热样本量”（burn-in）就能达到最优。
- 对 TD、Q-learning 等常用算法给出了紧的样本复杂度刻画，说明它们与最优界之间到底差多少。
- 扩展讨论了鲁棒 RL、多智能体博弈、联邦 RL、不确定性量化和 RLHF。

## 为什么值得关注

这本书把近几年分散的有限样本 RL 理论整理成一套统一、基本自包含的框架，并配有直观解释，适合研究者系统入门。它解释了“乐观探索、悲观离线”等设计原则为什么有效，可以为 LLM 后训练（RLHF/RLVR）等数据昂贵场景下的算法设计提供理论参照。
