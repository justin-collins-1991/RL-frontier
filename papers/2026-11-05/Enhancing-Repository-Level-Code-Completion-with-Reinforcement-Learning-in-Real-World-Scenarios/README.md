---
title: "Enhancing Repository-Level Code Completion with Reinforcement Learning in Real-World Scenarios"
arxiv: "2611.07510"
url: https://arxiv.org/abs/2611.07510
authors: "Zhenlong Dai, Zhuoluo Zhao, Xiu Tang, Sai Wu, Chang Yao, Zhipeng Gao, et al."
published: 2026-11-05
tagline: "用标识符意图奖励和选择性探索让7B模型学会跨文件补全"
---

## 一句话概括

IntentCoder 用 GRPO 在真实仓库数据上训练代码模型，靠更细的奖励和更有针对性的 token 级探索，让模型补全时能分清该看本文件还是跨文件的上下文。

## 核心方法

- **稠密的补全奖励**：只看是否精确匹配，奖励太稀疏，于是改用编辑距离相似度打连续分，再加上格式奖励和“只输出一行”的长度奖励，防止模型多写代码骗分。
- **标识符意图奖励**：先在 prompt 里要求模型推理补全意图，再把预测代码和真实代码中的变量名、函数名、类名抽出来算 F1，用它给编辑距离奖励加权。两个候选编辑距离差不多时，调用对了跨文件 API 的那个分更高。
- **选择性探索**：同一组采样里，各回答都一致的 token（比如类名）价值不大，真正决定对错的往往是有分歧的 token（比如来自另一个文件的泛型参数）。对“模型不自信、但优势高于组内平均”的 token 去掉 KL 约束，鼓励模型往这些方向探索。

## 关键结果

- 在 RepoBench Java/Python 上，基于 Qwen2.5-Coder-7B 训练的版本 Code EM 分别为 42.47% 和 35.93%，比 Qwen2.5-Coder-32B 高约 6 个点，比同尺寸的 aiXcoder-7B-v2 高 8~12 个点。
- 与对应基座相比，Code EM 最多提升 15~20 个点，也明显好于普通微调、原版 GRPO 和 CoLT。
- 消融实验中，去掉任何一个模块都会掉点。

## 为什么值得关注

仓库级补全是 IDE 里的高频场景，但它很难像数学题那样用对错直接验证。这篇论文给出了一套可借鉴的做法：用编辑距离加标识符匹配构造稠密且贴近语义的奖励，再把 credit assignment 落到关键 token 上。小模型因此能超过大好几倍的模型，对其他“没有执行器、只能软匹配”的 RL 任务也有参考价值。
