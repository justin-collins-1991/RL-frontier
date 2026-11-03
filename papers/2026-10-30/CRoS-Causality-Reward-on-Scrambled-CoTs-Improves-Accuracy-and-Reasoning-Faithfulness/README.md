---
title: "CRoS: Causality Reward on Scrambled CoTs Improves Accuracy and Reasoning Faithfulness"
arxiv: "2610.42054"
url: https://arxiv.org/abs/2610.42054
authors: "Xiao Yu, Justin Chih-Yao Chen, Zaid Khan, Hyunji Lee, Mohit Bansal"
published: 2026-10-30
tagline: "打乱推理步骤顺序衡量 CoT 因果性，作为 RL 辅助奖励"
---

## 一句话概括

只按结果对错给奖励的 RLVR 管不住"先有答案、再编理由"的 CoT。CRoS 把推理步骤的顺序打乱、内容不动，看原答案的概率掉了多少，用这个变化来衡量 CoT 对答案的因果贡献，并把它作为辅助奖励加进训练。

## 核心方法

- 以往的因果性指标靠删步骤或往步骤里插错误来扰动 CoT，但这样会顺带改掉信息。分数高可能只是模型对信息变化敏感，不一定说明真的依赖推理。拿它们当奖励训练，模型会学坏：CoT 信息量变少，探索和自我纠错也变少。
- CRoS 按换行把 CoT 切成步骤，打乱顺序后，比较原答案在原始 CoT 和打乱后 CoT 下的概率。概率降得越多，说明推理链的结构越在起作用，因果性越强。
- 训练时用 GRPO，把 CRoS 作为辅助奖励，和结果奖励一起使用。

## 关键结果

在 Gemma-3-4B 上用 Reasoning Gym 的 AIW 和 Survo 两个数据集训练：
- 5 个没见过的逻辑/游戏数据集上，平均准确率 46.8%，最强基线 43.8%，只用结果奖励 41.8%。
- 域内题目越难，领先越明显。
- CoT-Pass@K 在 K=1 到 128 范围内都领先，平均 43.4% 对 41.4%。
- 忠实度方面，提示承认率（hint acknowledgment，即推理里是否如实承认用了题目给的提示）34.0%，基线 20.2%。

## 为什么值得关注

这个方法给"奖励推理过程"提供了一个便宜的信号：不需要外部评审模型，也不需要过程标注，只多做一次前向计算答案概率。它同时提升了泛化能力和 CoT 的可监控性，对想在 RLVR 里加过程约束的团队有直接参考价值。
