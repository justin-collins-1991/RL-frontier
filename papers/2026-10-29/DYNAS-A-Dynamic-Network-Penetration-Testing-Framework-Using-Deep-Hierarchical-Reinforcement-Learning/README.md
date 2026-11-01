---
title: "DYNAS: A Dynamic Network Penetration Testing Framework Using Deep Hierarchical Reinforcement Learning"
arxiv: "2610.40214"
url: https://arxiv.org/abs/2610.40214
authors: "Md. Rakibul Hassan, Majedul Islam, Md. Ashraful Alam, Muhammad Iqbal Hossain, Swakkhar Shatabda"
published: 2026-10-29
tagline: "在带防御动态的仿真环境中用分层强化学习做自动化渗透测试"
---

## 一句话概括

DYNAS 是一个把入侵检测、扫描噪声等防御动态纳入训练的渗透测试仿真器，配套的分层策略 Pen-DHRL 在防御环境下明显优于扁平基线。

## 核心方法

DYNAS 基于 NASimEmu 扩展：用模板自动生成大规模参数化网络场景，并加入四类可配置动态——有状态的 IDS 响应、扫描误报/漏报、服务临时不可用、动作超时。Pen-DHRL 采用循环 manager–worker 结构：manager 结合各主机累积的检测信号，选择可持续多步的隐式子目标；worker 据此选择主机和动作。训练时还可用三阶段课程逐步加难。

## 关键结果

与 GNN、Invariant、Attention 基线在四种场景上对比。无 IDS 训练、有 IDS 评估时，Pen-DHRL 在 Bridge、Dynamic 上的单步奖励比次优基线高约 64%、24%，在 VarA、VarB 上多攻陷约 26%、30% 的主机。从头开启全部防御时，它在四个场景的平均回报均为正，而扁平基线 12 个组合全为负；改用课程训练后，全部 16 个组合均转正。

## 为什么值得关注

现有渗透测试 RL 环境大多简化了防御反应，训练出的策略容易显得过于乐观。DYNAS 把这些因素放进同一个可重复的框架，也说明了让智能体“看见”自身暴露程度、并分阶段接触防御的价值。不过结果仍来自仿真，且假设智能体能读取检测状态，真实网络上的效果有待验证。
