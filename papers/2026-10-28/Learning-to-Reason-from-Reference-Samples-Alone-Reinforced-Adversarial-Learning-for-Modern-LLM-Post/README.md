---
title: "Learning to Reason from Reference Samples Alone: Reinforced Adversarial Learning for Modern LLM Post-Training"
arxiv: "2610.38851"
url: https://arxiv.org/abs/2610.38851
authors: "Albert Bou, Javier Valdes-Aleman, Jon M. Laurent, Samuel G. Rodriques, Andrew D. White, Michaela Hinks, et al."
published: 2026-10-28
tagline: "只靠参考答案和共训判别器，训练出比肩 RLVR 的推理模型"
---

## 一句话概括

不用验证器和推理过程示范，只给参考答案，让共同训练的 LLM 判别器打分，就能把推理模型训练到接近 RLVR 的水平。

## 核心方法

RAL 同时训练两个独立 LLM。判别器只看题目和最终答案，判断答案来自参考集还是生成器；其“参考概率”是生成器唯一的奖励，生成器用 GRPO 更新，推理能力从答案层面的反馈中自行涌现。对抗过程相当于课程：表层特征被模仿后失去区分力，迫使判别器关注更深层性质。

## 关键结果

- 乘法、算术表达式合成、SMILES 转分子式任务中，验证器仅用于评估；判别器够强、训练够久时追平 RLVR。
- 医学摘要生成：提示不指定领域，生成器也能学到参考摘要的领域，且保持多样性。
- NIH 基金摘要：人类科学家和多个 LLM 判别器都更难将其与真实摘要区分，优于前沿 LLM 基线。

## 为什么值得关注

很多高价值场景里，好答案易收集却难写成可靠奖励，RAL 提供了从样例学奖励的路径。注意：判别器能力和共训时长是关键；摘要实验衡量的是“像不像真的”，不等于内容正确。
