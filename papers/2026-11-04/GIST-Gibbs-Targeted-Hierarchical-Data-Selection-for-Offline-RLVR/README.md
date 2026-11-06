---
title: "GIST: Gibbs-Targeted Hierarchical Data Selection for Offline RLVR"
arxiv: "2611.06395"
url: https://arxiv.org/abs/2611.06395
authors: "Xuliang Huang, Tianxiang Zhao, Chengwei Qin, Yao Shu"
published: 2026-11-04
tagline: "离线RLVR只挑关键回答和关键token监督，省三分之二token还更准"
---

## 一句话概括

离线 RLVR 不必监督每条回答的每个 token：从理论上找出最有信息量的回答和 token，只训练它们，效果反而更好。

## 核心方法

作者把离线训练看成在拟合 KL 正则 RLVR 的最优目标策略，并用双向 KL 衡量当前策略与目标的差距。分析发现：正确回答主要贡献在"策略覆盖不足"的方向，信息集中在低概率 token；错误回答主要贡献在"策略过度自信"的方向，信息集中在策略常生成的回答及其高概率 token。

据此提出两级筛选方法 GIST，只用训练前就有的信号：
- **回答级**：正确回答取高温（on-policy）采样，错误回答取低温（贴近策略众数）采样，并只保留两类都有的 prompt；
- **token 级**：用初始策略的 token 概率，正确回答只监督低概率 token，错误回答只监督高概率 token。

## 关键结果

- 搭配 BOLT 和 SFT 两种离线目标，在三个模型上 GSM8K、MATH-500、MBPP 的平均准确率全部提升（30 组设置中 29 组提升）；
- Qwen3-0.6B/GSM8K 受控对比中，胜过 7 种同候选池筛选基线，比用全部候选训练高约 2 个点，同时监督 token 减少 66.6%、优化步数减少约一半。

## 为什么值得关注

它把"选哪些数据、监督哪些 token"从经验技巧变成有理论依据的规则，且无需额外打分模型，几乎零成本。对希望用离线数据低成本做推理强化的团队，是一个省算力又涨点的实用方案。
