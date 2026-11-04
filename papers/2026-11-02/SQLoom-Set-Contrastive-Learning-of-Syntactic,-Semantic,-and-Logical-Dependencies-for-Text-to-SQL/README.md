---
title: "SQLoom: Set-Contrastive Learning of Syntactic, Semantic, and Logical Dependencies for Text-to-SQL"
arxiv: "2611.03298"
url: https://arxiv.org/abs/2611.03298
authors: "Hao Fu, Degang Sun, Wan Wei, Jinxia Wei, Chun Long, Peng Gao"
published: 2026-11-02
tagline: "用集合对比监督教小模型写对 SQL 的语法、语义与逻辑"
---

## 一句话概括

SQLoom 不再让模型逐 token 模仿唯一的参考 SQL，而是在语法、语义、逻辑三个层面拿"正确集合"和"只差一处的错误集合"做对比。这样一来，1.7B 的小模型单次生成就超过了 70B 级别的系统和基于 GPT-4 的 agent。

## 核心方法

- **问题**：SFT 把 SQL 当普通文本处理，别名写错一个、运算符用错一个（`>` 和 `>=`），query 就废了，可这类错误在 loss 里几乎没有分量。执行奖励只看整条 query 的结果，定位不到出错的地方，碰巧答对的错 SQL 也会拿到奖励。
- **集合对比目标**：在 SFT 之外加一个统一的对比损失，让模型偏好正确输出的集合，压低只有细微差别的错误集合。
  - **语法**：用带 schema 作用域的增量解析器算出每个位置合法的 token，作为正确集合。模型在训练阶段就学会了语法，推理时不用再挂 parser。
  - **语义**：把问题里的短语对齐到 SQL 片段（比如"至少两个"对应 `>= 2`），再拿模型自己容易混淆的片段做对比。
  - **逻辑**：根据子句依赖图改写问题，逼某个子句必须变化，再对比"依赖子句跟着改"和"只改了一处"两种 query。两者的区别靠在反例数据库上执行来验证。
- 语义和逻辑这两层的样本由 4 个 LLM agent 合成，再经过解析器和执行双重校验。作者还顺带修正了 378 条错误的 Spider 标注，发布为 Spider-Refined。

## 关键结果

- Qwen3-1.7B 在 Spider Dev 上的 EX 从 62.9% 提到 88.7%，Spider Test 达到 89.2%，BIRD Dev 达到 73.4%，超过所有基线，包括零样本的 Qwen3-235B 和 GPT-4。
- 用同样的数据只做 SFT，Spider Test 低 8.8 个点，BIRD Dev 低 10.3 个点，说明提升主要来自训练目标本身。
- 在三个扰动版 Spider 上最多只掉 0.6 个点，agent 方法则掉 8.8~12.1 个点。
- 单次生成每条 query 耗时 0.42s，比基于 GPT-4 的 agent 方法快 23 倍。

## 为什么值得关注

对结构化输出来说，用 parser 和执行器自动造出细粒度的正负集合，比 query 级别的 DPO 或 RL 奖励更能把功劳分到具体出错的位置。这个思路也能迁移到代码生成、工具调用这类强约束的生成任务上。另外，它给"小模型单次推理就能替代昂贵的多轮 agent"提供了一条现实可行的路线。
