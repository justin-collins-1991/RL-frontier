---
title: "When All Rollouts Fail: Policy-Compatible Joint Decoding for Hard-Problem Reasoning"
arxiv: "2610.36849"
url: https://arxiv.org/abs/2610.36849
authors: "Zehao Wang, Hanzhu Chen, Runquan Gui, Zhe Wang, Lin Yang"
published: 2026-10-27
tagline: "用专家引导的联合解码，让 RLVR 在全错难题上也能学"
---

## 一句话概括

当难题上所有 rollout 全部失败、GRPO 类方法优势归零时，PICO 用"专家引导但贴合学生策略"的联合解码，造出既正确又与当前策略兼容的轨迹，让模型在难题上继续获得有效学习信号。

## 核心方法

- **问题诊断**：RLVR 在超出模型能力的题目上会遇到"学习悬崖"——全错样本不含正确信息，组内相对优势全为零；直接塞专家轨迹又落在学生的低概率区域，更新幅度大，容易退化成表面模仿。
- **策略兼容的联合解码**：解码时由专家数据在 token 级给出方向，但保留学生模型自身的相对 token 概率；再用动态 top-k 把采样分布限制在有限的分布偏移预算内，生成的轨迹天然"可验证正确 + 离当前策略不远"。
- **混合行为目标**：把这些引导轨迹与常规 on-policy rollout 一起训练，用重要性采样修正二者的分布差异。

## 关键结果

在多个推理数据集和 agent 类基准上，PICO 稳定优于标准 RLVR 以及已有的 off-policy（引入专家数据）基线。（基于摘要）

## 为什么值得关注

"全错题没信号"是 RLVR 扩展到更难任务的核心瓶颈。PICO 给出的思路很实用：外部监督不仅要对，还要让当前策略"够得着"。它把 SFT 混合、off-policy 引导这类做法的失效原因讲清楚了，也给出了可落地的折中办法，对做难题推理和 agent RL 训练的团队有直接参考价值。
