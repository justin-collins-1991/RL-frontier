---
title: "TalentRL: Strategy-Guided Reinforcement Learning for Hierarchical Skill Routing"
arxiv: "2610.41143"
url: https://arxiv.org/abs/2610.41143
authors: "Huancheng Chen, Xiaodi Sun, Zhaoqiong Huang, Michelle Chang, Jingwen Lu"
published: 2026-10-30
tagline: "先选策略再取技能，用对照干预给路由决策单独记功"
---

## 一句话概括

给 LLM Agent 的技能库加一层“策略（talent）”。模型先挑一个高层策略，再按这个策略去检索具体技能；路由决策用对照实验式的奖励差单独训练。

## 核心方法

- **两级记忆**：粗粒度的 talent 表示“怎么用技能”的常见策略，细粒度的 skill 是可以直接执行的步骤。两者都由 LLM 从成功和失败的轨迹里提炼出来，RL 过程中会继续演化。
- **策略引导检索**：同一个策略模型先输出 talent，talent 的指导语会注入执行过程。检索时，talent 关联的技能在相似度排序上获得软性加权。
- **路由信用分配**：只看最终奖励，分不清是选对了策略，还是执行做得好。所以对同一个任务，额外跑几组受控对照：不给技能、缩小检索预算、去掉 talent 指导和先验。用“锚点 rollout 和对照组的奖励差”来训练路由 token，执行 token 仍然用 GRPO 式的组内相对优势。
- **SFT 热启动**：先用成对 rollout 比较各个 talent 的收益，只保留确实带来正收益的轨迹作为路由和执行的示范数据。

## 关键结果

- 在 7 个开放域和多跳问答基准上，talent-aware SFT 比零样本基线高 6.7%～9.2%（覆盖 Qwen2.5-7B、Qwen3-8B、Llama-3.1-8B）。在此基础上做 RL，再提升 7.6%～9.3%，三个基座上的平均成功率都是所有对比方法中最高的。
- ALFWorld 成功率 99.3%，WebShop 得分 90.7，均为对比方法中最高。

## 为什么值得关注

技能库越做越大以后，扁平检索容易召回一堆相关但用不上的技能。TalentRL 把“选策略”变成一个可学习的显式动作，并用匹配干预把它的贡献从终局奖励中拆出来。这为分层 Agent 的信用分配提供了一个简单可复用的思路，也让策略选择过程更容易解释和排查。
