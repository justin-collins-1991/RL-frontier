---
title: "The Cost of Mismatch: Noise Amplification in Zeroth-Order Reinforcement Learning"
arxiv: "2611.03260"
url: https://arxiv.org/abs/2611.03260
authors: "Lianmin Chen, Junbin Qiu, Chenxing Wei, Yao Shu, Kun He"
published: 2026-11-02
tagline: "零阶优化做 RLVR 的瓶颈在数据不匹配，固定数据才能消噪"
---

## 一句话概括

零阶（ZO）优化直接用于在线 RL 会严重放大噪声，问题出在有限差分的两次评估用的不是同一批数据；换成固定数据的加权 SFT 目标（ZO-BOLT）就能把这部分噪声抵消掉。

## 核心方法

ZO 只用前向传播估梯度：把参数扰动一下，比较前后两次损失的差。作者把估计误差拆成"无噪声项"和"评估噪声项"，发现后者取决于两次评估的噪声是否相关。在线 RL 中，扰动前后的策略各自采样，数据互相独立，噪声无法抵消，且扰动越小放大越严重，形成降不下去的噪声底。而 BOLT 把 KL 正则的 RLVR 目标改写成固定数据集上的加权 SFT，两次评估可用同一批数据，噪声自然对消。据此提出 ZO-BOLT，并给出能区分两种情形的收敛保证。

## 关键结果

- 扰动尺度扫描实验验证了独立采样下噪声随扰动变小而急剧放大的理论预测；数据匹配与不匹配的端到端对比也印证了它对优化效果的影响。
- 在 Qwen2.5-1.5B/7B、DeepSeek-R1-Distill-Qwen-1.5B 上，ZO-BOLT 在 GSM8K 和 MATH 上都稳定超过预训练基线，显存占用接近纯推理。

## 为什么值得关注

它说清楚了"ZO 为什么在在线 RL 里不好用"：根因是数据不匹配，而不是调参问题。对显存受限、又想做 RLVR 后训练的团队，"先离线构造加权数据、再用 ZO 训练"是一条有理论支撑、可以落地的路线。
