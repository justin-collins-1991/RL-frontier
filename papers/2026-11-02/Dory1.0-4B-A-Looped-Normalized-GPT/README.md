---
title: "Dory1.0-4B: A Looped Normalized-GPT"
arxiv: "2611.03998"
url: https://arxiv.org/abs/2611.03998
authors: "Maxim Fishman, Simeng Sun, Shantanu Acharya, Faisal Ladhak, Brian Chmiel, Santiago Akle Serano, et al."
published: 2026-11-02
tagline: "可调循环深度的 4B 模型，用潜空间计算换精度与更短输出"
---

## 一句话概括

NVIDIA 开源的 4B 循环（latent-recurrent）语言模型：同一个 checkpoint 推理时可以选择把中间块循环跑 1~4 次，用更多的潜空间计算换更高的精度，而不是靠生成更长的思维链。

## 核心方法

- **结构**：基于归一化 Transformer（nGPT），72 层切成“输入块 16 层 + 共享循环块 40 层 + 输出块 16 层”。循环块权重共享，每轮都重新注入输入块的输出，注意力层按 3:1 混合滑窗和全局注意力。
- **预训练**：共 6T token。前 4.5T 先按普通非循环模型用 NVFP4 训练（比 BF16 快约 20%），之后改用 BF16 继续训练，每步随机采样循环次数 1~4，反向传播只穿过最后一轮循环（截断反传），最后把上下文扩展到 256K。
- **后训练**：SFT 之后接 200 步异步 GRPO（RLVR），覆盖 23 个环境。关键设计是**按难度分配循环深度的课程**：通过率低的难题优先分给深循环的 rollout worker。
- **省显存**：只缓存最后一轮循环的 KV，所以不管循环几次，KV cache 都和非循环模型一样大。

## 关键结果

- 12 项基准平均分：1 轮循环 35.2，2 轮 39.7，4 轮 40.6。2 轮及以上就超过 Qwen3.5-9B、Gemma 4 12B 和 Gemma 4 26B-A4B，离总参数约 9 倍的 Qwen3.6-35B-A3B 只差 1.7 分。
- 代码、agent 和长上下文任务提升最大。4 轮时 SWE-Bench Verified 61.8%，Gemma 4 26B-A4B 为 57.4%。
- 难度课程让 4 轮时的 Terminal-Bench 从 14.0% 涨到 21.4%。
- 在 agent 任务上，4 轮比 1 轮少生成 1.3~2.5 倍的 token。
- 只缓存最后一轮 KV 时，分数变化在 -2.1 到 +0.4 分之间。

## 为什么值得关注

它给 test-time compute 增加了一个新维度——“想得更深”，而不只是“写得更长”。同一份权重可以按请求动态调节算力，KV 显存也不随循环次数增长，对部署很友好。对 RL 研究来说，“按题目难度分配推理深度”的课程是一个可以借鉴的思路：把 RL 训练和自适应算力结合起来。模型同时开源了 BF16、MXFP8、NVFP4 和 GGUF 版本，方便直接复现。
