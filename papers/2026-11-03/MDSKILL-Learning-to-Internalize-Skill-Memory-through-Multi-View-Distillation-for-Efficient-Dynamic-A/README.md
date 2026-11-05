---
title: "MDSKILL: Learning to Internalize Skill Memory through Multi-View Distillation for Efficient Dynamic Agent Self-Evolution"
arxiv: "2611.05313"
url: https://arxiv.org/abs/2611.05313
authors: "Dian Jin, Jinluan Yang, Kairong Han, Baohong Li, Zijing Hu, Yi He, et al."
published: 2026-11-03
tagline: "把技能记忆按功能拆成多视角再自蒸馏，让智能体把经验内化进参数"
---

## 一句话概括

智能体自己总结的技能记忆往往有噪声，而且不同用途的经验混在一起，直接蒸馏效果不好。MDSKILL 先把技能按功能拆成几个视角，再做多视角的在线自蒸馏，把经验稳定地学进模型参数。

## 核心方法

- **先分析蒸馏方向**：作者对比后发现，“带技能分支教不带技能分支”的正向蒸馏监督信号不稳定；反过来让不带技能分支去纠正被技能误导的行为，效果反而最好。由此判断，症结在于技能噪声和知识纠缠。
- **动态筛选技能**：为每条技能维护“可靠性”和“优势”两个指标，随训练持续更新并按时间衰减，再用 Thompson 采样挑出当前真正有用的技能。
- **三视角拆分**：把技能分成状态理解（grounding）、动作规划（planning）、执行控制（control）三类，各自引导一个推理分支，另有一个综合分支和一个无技能分支。
- **多视角蒸馏**：只拿成功轨迹和失败轨迹配对，按结果决定蒸馏方向，包括正向、反向和跨视角三种迁移，最后叠加在 GiGPO 强化学习目标上，共同更新同一套共享策略。

## 关键结果

在 ALFWorld、WebShop、Search-QA 三个基准上，对比不依赖更强外部教师的 RL、技能增强和自蒸馏基线，MDSKILL 在不增加计算开销的前提下，比 SOTA 分别最多高出 7.1%（ALFWorld）和 8.1%（WebShop）。Qwen3-1.7B 在 ALFWorld 上达到 93.8%。带技能和不带技能两个分支都有提升，说明经验确实被内化进了参数，而不是一直依赖外挂记忆。

## 为什么值得关注

它直接回应了“自生成记忆不可靠”这个自进化智能体的老问题，给出了一个不需要更强教师模型的可行方案：先把经验按功能解耦、筛选质量，再去蒸馏。另外，“反向蒸馏比正向更有效”这一发现，对所有做 OPSD 或技能内化的工作都有参考价值。
