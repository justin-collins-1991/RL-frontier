---
title: "Beyond Validation Loss: Coverage and Reliability Dynamics in Robot Policy Pretraining"
arxiv: "2611.01565"
url: https://arxiv.org/abs/2611.01565
authors: "Zhanyi Sun, Max Simchowitz, Shuran Song"
published: 2026-11-01
tagline: "用 pass@k 挑机器人预训练检查点，兼顾覆盖与可靠"
---

## 一句话概括

机器人策略预训练越往后，平均成功率可能还在涨，但"多试几次能成功"的覆盖能力已经在下降。只看验证损失或 pass@1 挑检查点，会挑出不利于后训练的模型。

## 核心方法

- **闭环 fixed-start pass@k**：从同一初始状态跑 k 次，看至少成功一次的概率。pass@1 就是平均成功率（可靠性），大 k 的 pass@k 反映覆盖率，也就是难的初始状态是否还"有希望"成功。
- **离线检查点选择**：真机上跑大量闭环 rollout 成本太高，作者改用留出集上动作误差的分位数曲线：好的尾部对应覆盖，典型分位对应可靠性，据此选出两者平衡的检查点。不需要闭环评估，不用选 k，也没有要调的权重。
- **生成式数据增强**：训练一个观测-动作联合生成模型，把监督数据扩展到有限演示之外，让训练后期也不丢覆盖。

## 关键结果

- 在 MimicGen 单任务 Diffusion Policy 和 RoboCasa 65 任务 π0.5 预训练中，k 越大，pass@k 的峰值出现得越早。训练后期成功率会往本来就容易的初始状态集中。
- 两个检查点 pass@1 相近时，大 k pass@k 更高的那个，在 Filtered BC、critic 引导、残差 RL、SFT 等多种后训练后表现明显更好。
- 数据增强在保持甚至提升 pass@1 的同时保住了覆盖，把成功率与覆盖率之间的 Pareto 前沿整体往上推。

## 为什么值得关注

"预训练 + RL/SFT 后训练"已经是机器人学习的主流流程，但交给后训练的检查点通常还是按验证损失挑，或者直接用最后一个。这篇工作说明，预训练应该为后训练服务，同时给出了能直接接进现有训练流程的离线选检查点方法，并把 LLM 领域"覆盖决定 RL 上限"的观点验证到了连续控制上。
