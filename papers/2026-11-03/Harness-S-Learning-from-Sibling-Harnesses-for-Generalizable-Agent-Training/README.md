---
title: "Harness-S: Learning from Sibling Harnesses for Generalizable Agent Training"
arxiv: "2611.04277"
url: https://arxiv.org/abs/2611.04277
authors: "Kangning Zhang, Wenxiang Jiao, Bowen Fang, Shuai Shao, Jiachen Zhu, Rong Shan, et al."
published: 2026-11-03
tagline: "用兄弟 harness 救援失败样本，把能力内化进单一策略"
---

## 一句话概括

不追求“万能 harness”，而是在 RL 训练中用一组各有专长的兄弟 harness 去救那些基础 harness 全部失败的任务。这样学到的能力会留在策略里，回到原始 harness 上依然有效。

## 核心方法

作者观察到 harness 改进有三个特点：局部性（修好一部分，弄坏另一部分）、互补性（不同变体能修彼此的错）和非平稳性（策略变强后，各变体的价值会变）。据此设计了三步：
- **定向演化**：先诊断失败轨迹，每个子 harness 只针对一类根因来修，所有能跑通的变体都留下，组成兄弟 harness 池。训练期间这个池子固定不变。
- **救援训练**：只有当某个任务在基础 harness 下的 rollout 全部失败时，才让同一策略在挑出的几个兄弟 harness 下重新 rollout，用这批轨迹替换失败组去做 GRPO 更新。
- **自适应路由**：根据各 harness 的行为画像，再让多个 LLM 投票，选出 Top-k 个 harness。画像会随策略训练定期刷新。

## 关键结果

在 AppWorld、SWE-Gym、DBBench 三个基准、两种模型规模上，训练好的策略回到原始 harness 评测时，都明显好于只训练策略的基线。行为分析和留出案例表明，提升来自策略本身学会了新行为，比如“翻完所有分页”。推理时再用路由选出排名第一的 harness，能在 rollout 次数不变的情况下带来额外提升；换成训练中没见过的 harness，收益仍然保留。

## 为什么值得关注

全组失败、没有学习信号是 agent RL 的常见瓶颈。这篇论文把“换个 harness 去探索”变成了打破瓶颈的手段，而且最后部署时不依赖辅助 harness，工程上更好落地。它也说明 harness 工程和 RL 训练可以低成本结合：harness 池只需离线演化一次，训练中反复复用。
