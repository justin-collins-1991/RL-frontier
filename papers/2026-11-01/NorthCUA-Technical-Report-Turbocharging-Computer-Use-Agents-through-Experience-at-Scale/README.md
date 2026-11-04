---
title: "NorthCUA Technical Report: Turbocharging Computer-Use Agents through Experience at Scale"
arxiv: "2611.02102"
url: https://arxiv.org/abs/2611.02102
authors: "Chaoyun Zhang, Bingxuan Li, Pinxue Guo, Yangfan Gao, Zikun Cai, Tianci Xie, et al."
published: 2026-11-01
tagline: "用规模化经验飞轮加桌面-网页联合 RL 打造开源电脑操作智能体"
---

## 一句话概括

NorthCUA 是一套电脑操作智能体（CUA）的完整训练系统：先大规模产出可验证的交互经验，再分阶段训练策略模型，最后用强化学习把“产经验”和“改策略”串成闭环。

## 核心方法

- **Harness（执行环境）**：支撑长程交互，记录每一步决策，并自动检查任务是否真正完成，为后续训练提供可信信号。
- **Experience Flywheel（经验飞轮）**：持续提供多样、可执行的任务，并从执行记录里筛出经过验证的轨迹。对暂时做不出来的任务，通过递归自我改进沉淀可复用的“技能”，同时保存已验证的中间里程碑，后续尝试可以接着之前的进度做，不必从头来。
- **Staged Learning（分阶段训练）**：先用 GUI 定位（grounding）数据做 mid-training 打基础，再做长程 SFT，最后在同一个 Harness 里做桌面与网页的联合 RL。
- **Ultrafast 变体**：基于 RL 前的 Nano 模型，把直接选动作和开放式生成结合起来，面向对响应速度要求高的网页场景。

## 关键结果

- 推出 Nano / Mini / Pro 三个尺寸的模型。在论文报告的评测设置下，它们在 GUI 定位、桌面任务执行、网页交互三类基准上都达到开源模型的 SOTA。
- NorthCUA-Ultrafast 在质量和延迟之间给出了可量化的折中。

（基于摘要）

## 为什么值得关注

CUA 的瓶颈正在从单步点击准确率转向长程任务能否做完。NorthCUA 的思路是把重点放在经验数据上：结果可验证、做不完的任务保留里程碑和技能、RL 和数据生产共用同一个环境。这套工程化的闭环方案对想自建 agent 训练流水线的团队有直接参考价值。同时，它在多个尺寸上都提供了开源 SOTA 基线，Ultrafast 也照顾到了实际部署时的延迟需求。
