---
title: "Co-Evolving Policy and Rubric via Capability Awareness for Open-Ended Generation"
arxiv: "2610.38566"
url: https://arxiv.org/abs/2610.38566
authors: "Chengsheng Zhang, Wenshen Xu, Yuchuan Wu, Zhiyuan Yu, Junfeng Fang, Tianlong Wang, et al."
published: 2026-10-28
tagline: "让评分细则难度随策略能力动态演化的 Rubric RL"
---

## 一句话概括

CoCA 让评分细则（rubric）和策略模型一起进化：按模型当前能力诊断每条评分标准的难度并加以调整，避免奖励信号“太简单”或“够不着”。

## 核心方法

- **逐条诊断**：对同一问题分别做“只给问题”和“附带 rubric 提示”两种采样，对比结果来判断每条标准对当前策略来说是已饱和、太难，还是“有提示能做到、没提示做不到”的能力缺口。
- **重新校准**：改写难度不匹配的标准，让奖励重新具备区分度。
- **两条学习路径**：对能力前沿上的缺口，用 rubric 引导的优化继续拓展前沿；对已经可靠的提升，通过 on-policy 自蒸馏迁移回“只给问题”的行为。
- **闭环**：策略更新后诊断更准，蒸馏也更可靠，形成策略与 rubric 共同进化的循环。

## 关键结果

在多个基准和不同 LLM 上，CoCA 稳定优于现有基于 rubric 的 RL 方法；模型能把“有提示才会”的能力内化为无提示时的默认行为，同时缓解了能力退化问题。（基于摘要）

## 为什么值得关注

开放式生成缺少可验证奖励，rubric RL 是主流替代方案，但静态 rubric 很快会饱和或失效。CoCA 把“奖励难度应匹配模型能力前沿”这一课程学习思路落到了逐条标准的粒度，并把引导采样和自蒸馏结合起来，对做写作、对话等非可验证任务 RL 的团队有直接参考价值。
