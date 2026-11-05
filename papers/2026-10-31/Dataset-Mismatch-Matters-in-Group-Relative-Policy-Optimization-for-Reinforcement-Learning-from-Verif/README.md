---
title: "Dataset Mismatch Matters in Group Relative Policy Optimization for Reinforcement Learning from Verifiable Rewards"
arxiv: "2611.00586"
url: https://arxiv.org/abs/2611.00586
authors: "Zhen-Yu Zhang, Jiandong Zhang, Huaxiu Yao, Gang Niu, Masashi Sugiyama"
published: 2026-10-31
tagline: "借目标域聚合反馈重加权GRPO采样，提效又提泛化"
---

## 一句话概括

训练集与目标测试集常有分布差异。L2RR 不接触目标题目，只借目标方回传的聚合反馈来决定 GRPO 多采哪些训练题。

## 核心方法

- **设定**：目标数据因隐私不能外传，但数据方可在本地小验证集上计算梯度方向内积等聚合信号并回传。
- **学习采样分布**：给每道训练题一个采样概率，与 GRPO 交替更新。用双层优化的一步展开近似，上调"对目标域有帮助"的题。
- **惩罚无效 rollout**：连续多次整组奖励相同（优势为 0）的题，逐步降低采样权重。
- 理论上给出 O(T^-1/2) 的目标损失界。

## 关键结果

在 6 个数学基准、3 个模型（Qwen2.5-Math-1.5B/7B、R1-Distill-1.5B）上，L2RR 平均准确率均为最高，rollout 也少于 DAPO。例如 Qwen2.5-Math-1.5B 上，平均分从 47.7% 升到 50.3%，rollout 从 7.6M 降到 3.0M。只用训练侧信号的 GRESO、AR3PO 虽然省 rollout，但准确率基本没涨。

## 为什么值得关注

RLVR 落地时，数据错配加上数据不能出域是常态。本文给出一个实用接口：只回传聚合反馈，就能把 rollout 预算花在"对目标有用、且仍有学习信号"的题上。医疗、私有数据、盲测等场景都可借鉴。不过论文尚未给出形式化的隐私保证。
