---
title: "Hindsight Credit Assignment over Trees for Agentic RL"
arxiv: "2611.02706"
url: https://arxiv.org/abs/2611.02706
authors: "Penghong Zhao, Yihao Chen, Maoheng Yuan, Yunjian Zhang, Abudukelimu Wuerkaixi, Haoran Xu, et al."
published: 2026-11-02
tagline: "把稀缺的成功经验在线注入树状 rollout，三组优势做细粒度信用分配"
---

## 一句话概括

TriGRPO 在训练过程中实时复用"已经成功过的动作"，用它在 rollout 树里主动分叉探索，再用三种比较分组给长程 Agent 提供更密的学习信号。

## 核心方法

- **事后引导分叉**：同一 prompt 下成功的轨迹会实时存进"成功库"。其他正在跑的轨迹走到相同决策状态、并且准备做不一样的动作时，就复用原有前缀，换上成功动作，分出一条兄弟分支，之后让策略自己接着跑。作者证明：在状态完全匹配的前提下，这种替换的期望收益不为负。
- **三组优势**：
  - Root 组：同一 prompt 内比较各轨迹的回报，和 GRPO 一样；
  - Node 组：在分叉点比较父分支和兄弟分支的结果差，把功劳精确记到那一步动作上；
  - Cross 组：同类任务的历史表现作为基线，解决整组都失败、优势为零的问题。
- 注入的动作只用行为克隆来学，策略自己做出的决策才走 RL。整个过程不需要外部示范，也不需要额外的预采样。

## 关键结果

在 Qwen2.5 1.5B/3B/7B 三个规模上，TriGRPO 都稳定超过 GRPO、GSPO、GiGPO、Tree-GRPO。成功率最多提升 6.2%，rollout token 消耗最多减少 39.4%，在"成功率-成本"这个维度上形成了更好的 Pareto 前沿。

## 为什么值得关注

长程 Agent RL 有个死结：策略要靠成功经验才能进步，可能力不够又很难采到成功。这篇论文不做离线回放，而是在线把偶尔的成功变成探索的起点，同时用它做步级信用分配，一举两得。另外，前缀共享直接降低了采样成本，工程上也容易落地。对做稀疏奖励多轮 Agent 训练的团队，这是一个值得借鉴的思路。
