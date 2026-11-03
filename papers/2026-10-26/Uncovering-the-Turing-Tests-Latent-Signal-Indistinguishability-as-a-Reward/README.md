---
title: "Uncovering the Turing Test's Latent Signal: Indistinguishability as a Reward"
arxiv: "2610.34781"
url: https://arxiv.org/abs/2610.34781
authors: "Emanuele Rimoldi, Riccardo Neumarker, Tomaso Poggio, Daniel Mitropolsky"
published: 2026-10-26
tagline: "让学生模型骗过老师的图灵测试，本身就是有效的RL奖励"
---

## 一句话概括

把"让强模型误以为这是自己写的"当作强化学习奖励，不需要标准答案，也不需要老师生成回答，小模型的真实任务能力就能提升。

## 核心方法

- 提出"领域版师生图灵测试"：强老师模型同时是模仿对象和判别者，弱学生模型负责模仿。
- 学生针对每道题采样多个回答，老师只回答一个问题："这是我写的吗？"，取老师判"是"的对数概率作为奖励，再用 GRPO 只更新学生。
- 整个训练过程不用 ground-truth，老师也不用生成任何回答，只需要两个 token 的 logprob；对完全黑盒的老师，也可以用多次采样单 token 输出来估计这个概率。

## 关键结果

- 学生用 Qwen2.5-1.5B，老师用 DeepSeek V4 Flash，在 CommonsenseQA、GSM8K、KodCode、Spider 四个领域的留出测试集上，准确率分别提升 12.4、13.0、5.4、11.9 个百分点。
- 与 SFT、正确性 oracle 奖励、老师判对错奖励相比，在每个领域都和最优方法相差不到 3.1 个百分点；在 CommonsenseQA 和 Spider 上甚至超过了 oracle 奖励。
- 换成纯黑盒的 GPT-5 Mini 当判别者，4 个领域中有 3 个仍然有提升。
- 分析显示："像老师"和答案是否正确强相关，影响远大于格式变化，而且对部分正确的答案也会给奖励，所以信号比 0/1 正确性更密。

## 为什么值得关注

它给出了一种很便宜的蒸馏思路：老师可以是私有、高成本或半黑盒的 API，只要能拿到判别概率就能训练，不需要标注数据和老师生成的数据。同时它也说明"不可区分性"不只是用来评估的指标，也可以直接作为学习信号。需要警惕的是老师的自我偏好偏差，可能被学生钻空子（reward hacking）。
