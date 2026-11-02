---
title: "Nemotron 3.5 Super and Lightning: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Models for Agentic AI"
arxiv: "2610.38095"
url: https://arxiv.org/abs/2610.38095
authors: "NVIDIA,  :, Aastha Jhunjhunwala, Aayushi Ashokkumar Srivastava, Abhibha Gupta, Abhinav Garg, et al."
published: 2026-10-28
tagline: "NVIDIA 开源的高效 MoE 混合 Mamba 智能体模型，能力与推理吞吐兼顾"
---

## 一句话概括

NVIDIA 开源了两款 MoE 混合 Mamba-Transformer 模型：Super（总参 120B、激活 12B，多模态）和 Lightning（总参 30B、激活 3B，纯文本）。它们面向推理、长上下文和智能体任务，训练和部署时同时优化能力与效率。

## 核心方法

- **预训练阶段**：先单独预热一个可递归复用的 MTP 头，用作内置的投机解码草稿模型；再用更大一号的 Nemotron 模型做 1T token 蒸馏。Super 另外做了印度语系继续预训练、1M 上下文扩展，以及 256K 上下文下的软件工程智能体中训练（数据包括代码仓库、issue-PR 对、CI 日志和 agent 轨迹）。
- **后训练阶段**：SFT 把纯文本基座变成视觉语言模型，再接 RLVR 和 RLHF，环境覆盖竞赛编程、金融检索类工具调用等。Super 还先分别训练视频、视觉工具和对齐方向的专家教师，再用多教师在线策略蒸馏（MOPD）把这些能力合并到一个模型里。
- **部署阶段**：后训练之后再强化 MTP 头，提高投机解码的接受长度；做 NVFP4 量化并配合量化感知蒸馏；优化混合状态缓存和 GPU kernel。

## 关键结果

- Super 在 SWE-bench Pro 上得分 51.78%，激活参数少约 4.6 倍，仍超过 Nemotron 3 Ultra。
- 测试时并行运行多个 agent 并做自验证后，Terminal-Bench 2.1 从 62.7% 提升到 71.9%。
- 印度语系基准最多提升 9.82 个百分点。
- NVFP4 量化后精度中位数恢复到 BF16 的 99.62%，吞吐是 BF16 的 2.43 倍。
- 在单张 GB200 上最高达到 4856 tokens/s/GPU，约为 Qwen3.5 的 2.34 倍。

## 为什么值得关注

这是一份完整公开的“RL 后训练 + 工程落地”配方：多环境 RLVR/RLHF、专家教师 + 在线策略蒸馏的能力合并方式，以及智能体中训练对 RL 起点的增益，都有对照实验。权重、数据和训练配方全部开源，适合作为智能体 RL 研究的强基线。
