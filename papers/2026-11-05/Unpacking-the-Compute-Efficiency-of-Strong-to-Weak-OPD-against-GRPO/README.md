---
title: "Unpacking the Compute Efficiency of Strong-to-Weak OPD against GRPO"
arxiv: "2611.08453"
url: https://arxiv.org/abs/2611.08453
authors: "Zeyu Leo Liu, Yang Li, Bo Pang, Emre Can Acikgoz, Xuan-Phi Nguyen, Anurag Koul, et al."
published: 2026-11-05
tagline: "按 FLOPs 算账：外部教师蒸馏不如 GRPO，先分域 RL 再多教师蒸馏才省"
---

## 一句话概括

在训练 FLOPs 对齐的前提下比较在线蒸馏（OPD）和 GRPO，结论是：拿现成的大模型当教师，OPD 通常比 GRPO 更费算力；先分领域各训一个 GRPO 专家，再用多教师 OPD 把它们合进一个学生，才真正省算力。

## 核心方法

- 统一用"累计训练 FLOPs 对应的 held-out 准确率"做度量，并对齐学生初始化、prompt、rollout 组大小等设置。OPD 每个 token 都要额外跑一次教师前向，这部分开销也计入。
- 实验覆盖任务难度、学生/教师规模、数学/代码等领域、思考模式、蒸馏目标等多个维度，学生用 Qwen3 1.7B/4B/8B，另外在 Olmo 上做了验证。
- 对比三类教师：外部后训练模型、在此基础上再做 GRPO 的模型、学生自己的 GRPO checkpoint（self-GRPO）。

## 关键结果

- 外部教师：同等 FLOPs 下 OPD 普遍不如 GRPO，即使是学生几乎做不出来、按理最该受益于稠密监督的难题也一样；而且回复长度会一路涨到上限，每步更贵。
- self-GRPO 教师：在数学上只用 GRPO 1/50 的蒸馏 FLOPs 就追平该 checkpoint，换成更大的学生、代码任务和另一模型家族也成立。不过在单领域里 GRPO 模型本身就已经是想要的结果，再蒸馏一遍只是多花算力。
- 多领域：把各领域 GRPO 专家用多教师 OPD 合并，蒸馏只多花专家训练 FLOPs 的 5.2%（2 域）/8.0%（4 域）；在 2 域上，总 FLOPs 比联合 GRPO 少 42%，就能达到同等效果。

## 为什么值得关注

"稠密 token 监督天然比 RL 高效"这一直觉被 FLOPs 层面的对照实验否定了。论文同时说明了 DeepSeek-V4、Kimi 等前沿模型为什么采用"分域 RL 专家 + 多教师蒸馏"：省算力的关键在于选什么来源的教师、怎么组织流程，而不是蒸馏本身。
