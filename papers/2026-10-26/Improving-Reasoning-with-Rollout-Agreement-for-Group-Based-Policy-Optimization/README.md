---
title: "Improving Reasoning with Rollout Agreement for Group-Based Policy Optimization"
arxiv: "2610.34951"
url: https://arxiv.org/abs/2610.34951
authors: "Sohyun Son, Yerim Hong, Jaeyun Park, Mujeen Sung"
published: 2026-10-26
tagline: "奖励与同组推理一致的正确 rollout，减少蒙对式推理"
---

## 一句话概括

GRPO 只看最终答案，但答对的 rollout 里混着"蒙对"的错误推理。作者发现，推理过程和同组其他 rollout 差别越大的正确答案，越可能藏着没解决的错误。据此提出 RoAR：答对的 rollout 如果推理和同组一致，就多给一份奖励。

## 核心方法

- **诊断**：用 GRPO 训练的 1.5B 模型，在 126 道题上盲评同一道题里一致性最高和最低的两条正确轨迹。低一致性那条的虚假推理率更高（35% vs 22%），问题主要是前后矛盾、公式用错、误用题目条件。
- **RoAR**：对每个 rollout 的思考过程，算它和同组其余 rollout 的平均相似度（语义向量相似度和词级重合度各占一半），只有答对的 rollout 才拿这份奖励，之后照常走 GRPO 更新。不需要人工推理标注、额外采样或单独训练的过程奖励模型，可以直接插进现有流程。

## 关键结果

- DeepSeek-R1-Distill-Qwen-1.5B 只用 7K 道训练题，在五个数学基准上平均 pass@1 达到 55.5%，比 GRPO 和 GRPO-CARE 分别高 6.0 和 5.5 个点；论文还在 Qwen3-4B 上做了验证。
- 在四个模型都答对的 100 道题上盲审，虚假推理率分别是：RoAR 18%、GRPO 32%、GRPO-CARE 27%、DRA-GRPO 37%。

## 为什么值得关注

最近不少工作在鼓励 rollout 多样性，这篇给了反面证据：在答对的前提下，"与众不同"更多是错误而不是创新。RoAR 几乎不增加成本，就把推理是否靠谱纳入了奖励，适合小模型、低资源的 RLVR 训练。它也提醒大家，设计多样性奖励时要分清有用的探索和噪声。
