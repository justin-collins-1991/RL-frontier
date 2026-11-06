---
title: "RAGAM-AI: A Hybrid Reinforcement Learning based Agentic approach powered by Generative AI for Edge Resource Management"
arxiv: "2611.06554"
url: https://arxiv.org/abs/2611.06554
authors: "Shreya K. Chari, John S. Vardakas, Kostas Ramantas, Christos Verikoukis"
published: 2026-11-04
tagline: "用 LLM 当奖励裁判，驱动多智能体 SAC 做边缘资源调度"
---

## 一句话概括

把 LLM（MathΣtral）当作"奖励裁判"，为多智能体 SAC 提供反馈，用于 MEC 边缘服务器上的 CPU、内存和带宽分配，以缓解手工奖励设计带来的偏差和泛化问题。

## 核心方法

- **多智能体 RL 做执行**：每个边缘服务器是一个 SAC 智能体，各自决定本地资源怎么分。多个智能体靠共享的环境目标和奖励协同更新。
- **LLM 做奖励（RLAIF）**：不再只靠固定的奖励公式，而是把系统状态交给 MathΣtral，由它权衡时延、利用率、需求波动等多个目标后给出奖励。思路是让奖励随场景变化，而不是死规则。
- **代理奖励模型降成本**：每一步都调用 LLM 太贵，所以用 LLM 的打分训练一个有监督的小奖励模型，训练时主要由它给奖励。
- 整套流程被包装成一个 Agentic AI 工作流：自主决策，接收反馈，分布式执行。

## 关键结果

与单智能体 SAC、REINFORCE 和随机策略对比（数值越低越好）：

- 资源分配偏差：CPU 23.65%（SAC 28.61%，随机 44.93%），内存 20.36%（SAC 24.35%），带宽 20.40%（SAC 25.27%）。
- 时延成本和数据速率成本也是最低的，但比 SAC 和 REINFORCE 只好一点点（例如时延成本 6.70e-3 对 6.72e-3）。明显的优势只体现在和随机策略的对比上。

## 为什么值得关注

"LLM 当奖励函数"正从对齐任务扩展到网络、系统调度这类工程控制问题，这篇是一个具体的落地样例。"LLM 打分 + 蒸馏出代理奖励模型"的做法，对任何奖励难以手写、又不想每步都调用大模型的 RL 场景都有参考价值。需要注意的是：实验基线较弱（没有和其他 LLM 奖励方法或手工奖励的多智能体方法对比），成本类指标的提升也很有限。所以结论更适合当作思路验证，不宜当作定量上的突破。
