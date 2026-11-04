---
title: "RLVR 的再审视：锐化、上尾与策略退化"
date: 2026-11-04
type: deep-dive
papers: 5
tagline: "五个独立团队用不同方法得到同一图景：RLVR 是概率质量的重新分配，而非能力的增长"
---

# RLVR 的再审视：锐化、上尾与策略退化

本周（10-29 ~ 11-04）agent 共收录约 200 篇 RL 论文，其中有一个非常显眼的集群：**针对 RLVR / RL 后训练的机理审视**。五个互相独立的团队，用完全不同的方法，拼出了同一幅图景。这篇笔记把它们串起来读。

## 统一叙事

**RLVR 做的事情是"重新分配概率质量"，而不是"创造新能力"。** 这个判断在三个层面各自拿到了证据：

### 1. 表征层：内部推理没有变

[RLVR Sharpens the Pencil, Not the Mind](https://arxiv.org/abs/2611.02574) 逐个检查了 OLMo-2-1B 在 GSM8K 上 RLVR 训练的全部 13 个 checkpoint：错误检测探针的 AUROC 全程稳定在 0.80~0.84，模型内部对推理的理解没有变化；唯一明显改变的是最终答案 token（AUROC 0.93）。也就是说，RLVR 只是让模型**更频繁地把已有的好解法排在前面**——"削尖铅笔，而不是升级大脑"。

### 2. 分布层：上尾被压缩，Best-of-N 反被基座反超

如果 RLVR 只是重排概率质量，那么它必然"中间变厚、两端变薄"——这正是两篇论文分别在不同模态上量到的：

- [Do Visual RL Gains Scale at Test Time?](https://arxiv.org/abs/2611.02366) 在视觉生成上发现：RL 后训练提升单样本（Best-of-1）质量，但奖励分布的**上尾**（稀有的极好样本）被压缩。N 变大时 RL 模型的优势缩小甚至被基座反超。对策 QUPO：在训练目标里直接优化多个 Best-of-k 效用的加权组合。
- [Controlling Sharpening in LLM Post-Training](https://arxiv.org/abs/2611.03146) 在数学/代码上给出闭式分析：pass@k 目标的最优策略与 @1 形式相同，只是 KL 系数变成**随题目难度自适应**——会做的题少动、不会的题多动。由此提出 KAPPO，单条采样即可追平多采样 @k 优化器。

### 3. 行为层：学到的策略是脆的

[Not All Reasoning Generalizes](https://arxiv.org/abs/2611.03627) 设计了可观测推理策略的受控实验：MONO（只在原任务上训练）在分布内推导规范，但 OOD（更长输出、更多解、未见函数）下整体退化为**暴力枚举**；训练时混入"单解双射"辅助任务（MIXED）即可明显恢复。失败既不是能力不足也不是 reward hacking，而是学到的策略本身不迁移。

### 4. 过程层：难题的"从零到一"停滞

概率重排视角还解释了一个训练动力学问题：GRPO 对全错组给不出梯度（组内无对比信号）。[What Drives the Zero-to-One Jump?](https://arxiv.org/abs/2611.02747) 发现即将突破的难题，其失败 rollout 的**开头熵**显著更高（还在分岔探索而非走进死胡同），据此提出 NAPO：用"早期分岔比"给全错组内的负样本分配不同的优势值，AIME24 pass@256 提升 10 分。

## 交叉印证

值得注意的是证据链的多样性：探针（表征）、奖励分位数（分布）、策略标注（行为）、token 熵（过程）——四类观测、五个团队、同一结论。这比单一论文的单一方法可信得多。

## 对训练配方的可操作建议

| 问题 | 手段 | 论文 |
|------|------|------|
| 多样性/上尾萎缩 | 训练目标里显式加权 Best-of-k 效用 | QUPO |
| 简单题刷分、难题停滞 | 难度自适应 KL 系数或奖励倍数 | KAPPO |
| 策略 OOD 退化 | 混入"唯一解"类辅助任务做数据配比 | MIXED |
| 全错组无梯度 | 按开头熵给负样本分配差异化优势 | NAPO |
| 评估失真 | 评 pass@k / 上尾而非只看 pass@1，且多 checkpoint 跟踪 | Pencil / Quantile |

一个朴素的组合：**KAPPO 式难度自适应压力 + 双射类辅助任务配比 + NAPO 式负采样 + 评估看上尾**——四者互不冲突，都几乎零成本接入现有 GRPO 流水线。

## 开放问题

1. **能力增长何时发生？** 五篇论文的任务里 RLVR 都没有创造新能力，但 pass@256 也在涨（Pencil: 94.5%→96.9%）——"重排"与"扩展边界"的界限在哪里？规模化（更大模型、更长训练、更难任务）会改变结论吗？Pencil 只测了 1B + 小学算术，这是它自己承认的局限。
2. **上尾保护与锐化的最优权衡**是什么？QUPO 的 k 加权、KAPPO 的 k 旋钮目前都靠手调。
3. **策略退化的早期预警**：MIXED 的 probing 能否做成在线监测器，在训练中检测"正在滑向枚举"？

## 论文清单

- [RLVR Sharpens the Pencil, Not the Mind](https://arxiv.org/abs/2611.02574) · 2611.02574
- [Do Visual RL Gains Scale at Test Time? A Quantile View of Post-Training](https://arxiv.org/abs/2611.02366) · 2611.02366
- [Controlling Sharpening in LLM Post-Training](https://arxiv.org/abs/2611.03146) · 2611.03146
- [Not All Reasoning Generalizes](https://arxiv.org/abs/2611.03627) · 2611.03627
- [What Drives the Zero-to-One Jump?](https://arxiv.org/abs/2611.02747) · 2611.02747

*笔记由仓库维护者基于 daily agent 的解读交叉精读写成（2026-11-04）；各论文详细解读见 `papers/2026-11-02/` 对应目录。*
