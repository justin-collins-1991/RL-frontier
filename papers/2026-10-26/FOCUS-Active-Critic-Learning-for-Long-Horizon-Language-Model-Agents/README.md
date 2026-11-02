---
title: "FOCUS: Active Critic Learning for Long-Horizon Language Model Agents"
arxiv: "2610.35801"
url: https://arxiv.org/abs/2610.35801
authors: "Zhengping Jiang, William Jurayj, Liaoyaqi Wang, Chunsheng Zuo, Anqi Liu, Benjamin Van Durme"
published: 2026-10-26
tagline: "把分支采样当主动学习，只在 critic 最不准的地方补 rollout"
---

## 一句话概括

长程 LLM Agent 只有最终奖励，很难判断前面哪一步做对了。FOCUS 把“从中间状态再分叉采样”当成 critic 的主动学习问题：只在最能修正 critic 估值误差的状态上补 rollout，用同样的生成预算拿到更准的逐步信用分配。

## 核心方法

- **以上下文压缩点切分步骤**：长任务中 Agent 会定期压缩上下文，每两次压缩之间的片段就算一“步”，压缩点就是可以分叉重来的中间状态。
- **critic 与实际采样结果融合**：在每个状态上，把 critic 的预测和从该状态分叉出的续写结果做加权平均。续写越多，越依赖实测结果。
- **按期望误差下降分配预算**：估算每个候选状态再多采一条续写能让估值误差下降多少，优先采收益最大的。critic 明显不准、样本又少的状态会先被补采。
- **双向受益**：修正后的估值给每个片段算 TD 优势来训练策略；采到的续写结果又作为 critic 的训练目标。上下文管理、rollout 分配、信用分配三者解耦，可以自由替换。

## 关键结果

在每步生成预算相同的条件下，FOCUS 在法律推理（DeonticBench）、深度搜索（BrowseComp-Plus）、代码定位（LocBench）三个基准上都超过了 GRPO 和 VinePPO。用 Qwen3.5-9B 时，BrowseComp-Plus 上比最强基线高 7.2 分（55.4 vs 48.2），DeonticBench 上高 4.1 分（56.5 vs 52.4）。诊断实验显示，预算增加时估值误差下降得更快。消融实验表明，提升不依赖某一种特定的压缩实现。

## 为什么值得关注

长程 Agent RL 的瓶颈主要是信用分配和采样成本。GRPO 这类方法不用 critic，只有轨迹级信号；VinePPO 靠均匀的蒙特卡洛分叉，成本很高。FOCUS 用“critic 加按需采样”的折中方案把预算花在关键位置，并把上下文压缩这一工程上的常用做法变成了 RL 的步骤划分，对训练深度搜索、代码类 Agent 有直接的参考价值。
