---
title: "InterQ-RL: Interaction-Aware Correction of Execution Mismatch in Quantized Agentic RL"
arxiv: "2610.35303"
url: https://arxiv.org/abs/2610.35303
authors: "Yingbo Hao, Song Liu, Guanghua Yu, Zhaojing Zhou, Jianchen Zhu, Yi Zou"
published: 2026-10-26
tagline: "沿动作历史纠偏，让 8bit 量化 rollout 的多轮 Agent RL 追平 BF16"
---

## 一句话概括

多轮 Agent RL 用 8bit 量化做 rollout 能省算力和 KV 缓存，但量化执行器和训练端算出的策略有偏差，而且这个偏差会沿着多轮交互历史一路累积。InterQ-RL 在常规量化对齐之外，再对“走到当前状态的那段动作历史”做有界纠偏，在 W8A8-KV8 下基本追平 BF16。

## 核心方法

- **先对齐**：用 QAT 让训练端前向复现 rollout 的 W8A8 和 FP8 KV 量化规则。这样能消掉大部分逐 token 的偏差，但残差仍约为 BF16 的 20 倍。
- **再纠历史**：以往方法只修正当前 token 的概率比。作者指出，当前动作看起来对齐了，不代表它所在的状态是“同一个策略”走出来的。于是 InterQ-RL 只在策略生成的 token 上累加 rollout 与训练端的对数概率差，环境反馈不计入；累加结果按长度缩放后裁剪，作为不回传梯度的权重乘到 PPO/GRPO 损失上。
- **按支撑度分配**：以每个动作段为单位，按有效支撑度在固定预算内分配纠偏强度，避免个别片段被过度放大。
- 全程复用已有的 log prob，不需要额外的前向计算。

## 关键结果

- 实验覆盖 ALFWorld、WebShop、ScienceWorld 三个环境，模型是 4B–30B 的 Qwen3（含 Dense 和 MoE），所有量化组共用同一套 W8A8-KV8 rollout。
- 四组设置里，InterQ-RL 的最终成绩在所有量化方法中都是最好的：与 BF16 的差距不超过 0.7 分，其中两组还超过了 BF16。
- 相比只做 QAT，ALFWorld 成功率高 6.0 分，WebShop 得分高 2.8 分。学习速度不慢于 QAT，也没有 QAT 后期约 10 分的性能回退。

## 为什么值得关注

量化 rollout 是降低长程 Agent RL 成本的直接手段，但它带来的 off-policy 偏差在多轮场景下容易被低估。这篇工作把问题从“逐 token 对齐”推进到“轨迹历史纠偏”，几乎不增加开销，可以直接接到 verl 这类 PPO/GRPO 框架里，适合做低精度 Agent RL 训练的团队参考。
