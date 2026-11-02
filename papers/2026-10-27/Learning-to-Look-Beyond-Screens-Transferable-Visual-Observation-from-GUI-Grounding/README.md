---
title: "Learning to Look Beyond Screens: Transferable Visual Observation from GUI Grounding"
arxiv: "2610.37093"
url: https://arxiv.org/abs/2610.37093
authors: "Ruilin Yao, Xinyu Qiu, Tianyu Zou, Yi Rong, Shengwu Xiong, Shuheng Shen, et al."
published: 2026-10-27
tagline: "用 GUI 定位数据训练会“裁剪细看”的视觉策略，并迁移到通用感知"
---

## 一句话概括

GUI 定位数据自带目标框标注，作者用它来监督模型“看哪里、看多大、要不要再看”。这样学到的主动观察能力不只在界面任务上有用，也能迁移到自然图像和图表理解。

## 核心方法

LBS 分两阶段训练：

- **冷启动 SFT**：先用代码合成 HTML 界面并自动抽取目标框，再由 Qwen3.8-Max 生成多轮“裁剪-查看”的定位轨迹，只保留最终答对的轨迹给学生模型模仿。这一步让模型学会调用 crop 工具。
- **多轮 Agentic RL（GRPO）**：只看最终答案是否正确，无法区分有用的裁剪和多余的裁剪。所以作者把训练时才能看到的目标框变成过程奖励：最终答对时才奖励覆盖目标的裁剪，小目标额外加分，和任务无关的中间轮次不参与梯度更新。

训练全程只用 GUI 定位数据，没有加入任何通用 VQA 数据。推理时各个领域共用同一套 crop 接口。

## 关键结果

- 在 Qwen3.5-35B-A3B 和 Qwen3.8-27B 两个底座上，RL 比 SFT 在 ScreenSpot-Pro 上分别提升 1.83 和 6.13 个百分点，在 PerceptionBench 上分别提升约 3.0 和 7.1 个百分点。
- Qwen3.5 版本在 HR-Bench 4K/8K 和 ChartQAPro 上也有提升。
- 只用结果奖励的 RL 能提高 GUI 定位分数，但 PerceptionBench 反而下降。说明定位准确率高不等于迁移能力强，对中间观察步骤的监督才是迁移的关键。

## 为什么值得关注

它给出了一条低成本的路线：GUI 数据可以大规模合成、标注天然精确，适合用来教 VLM 主动观察，不必为每个下游领域单独构造观察轨迹。另外，结论“SFT 学会看的基本动作，RL 学会把观察花在有用的地方”，对设计多模态智能体的过程奖励有直接参考价值。代码和模型均已开源。
