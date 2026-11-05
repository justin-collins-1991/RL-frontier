---
title: "Found by Search, Broken by a Shortcut: Transfer and Tampering of Searched Intrinsic Rewards"
arxiv: "2611.04838"
url: https://arxiv.org/abs/2611.04838
authors: "Chase J. Metoyer"
published: 2026-11-03
tagline: "搜索出的内在奖励能迁移，却挡不住搜索时没见过的捷径"
---

## 一句话概括

用 CMA-ES 搜索"内在驱动力"式的内在奖励，能帮 PPO 学习并迁移到新任务；但只要出现搜索时没有的作弊动作（免费重置需求），智能体照样会钻空子，学习直接崩掉。

## 核心方法

- 奖励形式固定为稳态（homeostatic）驱动：4 种通用事件（看到新画面、拾取、放下、开关门/箱），每种对应一个"需求"，各有权重、缓解量和回涨速度，共 12 个参数。
- 在 MiniGrid 的 DoorKey-8x8 和 UnlockPickup 上，用 CMA-ES 和同等预算的随机搜索各挑出一个奖励（E、R），共 1560 次 PPO 训练。
- 全流程三阶段预注册，搜索协议在出结果前就公开提交并带时间戳，所有检验（包括没通过的）全部报告。

## 关键结果

- 迁移：在没参与搜索的 KeyCorridorS3R2 上，E 在 3 项预注册比较中全部胜过纯任务 PPO、episodic novelty 和 R。
- 但前作手工设计、在该任务上接入了专用事件的饱足奖励更强（20/20 个种子解出 vs E 的 4/20）。
- 训练任务上 E 与 R 没有显著差异，CMA-ES 的优势主要体现在迁移上。
- 篡改测试：加入免费的"重置需求"动作后，E 在 DoorKey-8x8 上的学习曲线面积从 0.829 跌到 0.136，甚至不如纯任务 PPO。

## 为什么值得关注

它说明"把奖励交给搜索"不能自动避免 reward hacking：搜索只针对当时的环境做优化，环境里多出一个漏洞，奖励就可能失效。另外，论文的公开预注册和"失败结果也报告"的做法，值得 RL 实证研究参考。
