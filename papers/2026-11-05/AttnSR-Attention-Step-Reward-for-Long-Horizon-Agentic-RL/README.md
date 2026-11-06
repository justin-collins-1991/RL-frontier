---
title: "AttnSR: Attention Step Reward for Long-Horizon Agentic RL"
arxiv: "2611.07932"
url: https://arxiv.org/abs/2611.07932
authors: "Mengsong Wu, Tianchen Zhou, Zhaochen Su, Zhenhua Liu, Zhe Cui, Aimin Zhou"
published: 2026-11-05
tagline: "用策略模型自身注意力回溯分配步级奖励，无需奖励模型"
---

## 一句话概括

用策略模型自己的注意力，把长程 Agent 任务最终的成败"分摊"到中间各步，不用额外训练奖励模型，也不用额外 rollout。

## 核心方法

- **找相关步**：训练回放算旧 log-prob 时，顺手抓取注意力，构建"后一步关注前一步"的步级依赖图，再从最终一步沿图向后回溯，估计每个中间步的相关度。
- **修正与融合**：压低注意力天然偏向"最近几步"的倾向，多层结果取几何平均，保留各层一致支持的步。
- **置信门控**：按注意力覆盖量、集中度、跨层一致性打分，信号越弱，奖励幅度越小。
- **定正负**：最终结果高于滑动平均基线就奖励选中步，低于则惩罚。最终奖励保留不动，只在中间步末尾叠加奖励，PPO 其余部分不改。

## 关键结果

- Qwen2.5-7B-Instruct + PPO，ALFWorld 成功率从 91.2% 提升到 97.1%，所有 checkpoint 都优于基线，未见任务上提升更大。
- 消融：只按位置分配的版本仅 92.3%，说明收益来自"分给哪几步"，而不是简单多加奖励。
- ScienceWorld 每个 checkpoint 都有提升，环境交互步数减少 29.9%；短轨迹任务（如 WebShop）收益有限。

## 为什么值得关注

步级奖励一般要靠人工标注、PRM 或反事实 rollout，成本很高。AttnSR 复用训练中本来就有的前向计算，几乎零额外开销就能做时序信用分配，可以直接插进现有 PPO 流程，长程 Agent RL 训练可以低成本试用。作者也承认注意力不等于因果贡献，它只作为启发式先验使用。
