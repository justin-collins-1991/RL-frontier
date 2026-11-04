# RL 前沿日报 · 2026-11-01（13 篇）

| # | 论文 | 一句话概括 |
|---|------|-----------|
| 1 | [ANCHOR: KL-Anchored Adaptation for Stable Offline-to-Online RL](ANCHOR-KL-Anchored-Adaptation-for-Stable-Offline-to-Online-RL/README.md) | 用可退火的 KL 锚定离线策略，无需离线回放也能稳定在线微调 |
| 2 | [Beyond Validation Loss: Coverage and Reliability Dynamics in Robot Policy Pretraining](Beyond-Validation-Loss-Coverage-and-Reliability-Dynamics-in-Robot-Policy-Pretraining/README.md) | 用 pass@k 挑机器人预训练检查点，兼顾覆盖与可靠 |
| 3 | [Direct Knowledge Transfer for Offline Q-Learning](Direct-Knowledge-Transfer-for-Offline-Q-Learning/README.md) | 每轮 Bellman 更新中联合估计源参考与目标修正的离线迁移 Q 学习 |
| 4 | [Don't Guess, Ask Wisely: Benchmarking and Training Proactive Elicitation in Open-Domain LLM Conversations](Dont-Guess%2C-Ask-Wisely-Benchmarking-and-Training-Proactive-Elicitation-in-Open-Domain-LLM-Conversati/README.md) | 用对话状态图上的离线逐轮 RL 教模型在信息不足时先追问 |
| 5 | [Improved Sample Complexity Analysis For First Order Bilevel Reinforcement Learning](Improved-Sample-Complexity-Analysis-For-First-Order-Bilevel-Reinforcement-Learning/README.md) | 去掉均匀PL假设，用神经网络actor-critic把双层RL样本复杂度降到ε⁻² |
| 6 | [Iterative Gumbel Planning for Continuous Control](Iterative-Gumbel-Planning-for-Continuous-Control/README.md) | 按维离散策略加迭代Gumbel搜索，根治高斯蒸馏的方差膨胀 |
| 7 | [NorthCUA Technical Report: Turbocharging Computer-Use Agents through Experience at Scale](NorthCUA-Technical-Report-Turbocharging-Computer-Use-Agents-through-Experience-at-Scale/README.md) | 用规模化经验飞轮加桌面-网页联合 RL 打造开源电脑操作智能体 |
| 8 | [Rare Event Constrained Reinforcement Learning with Large Deviations](Rare-Event-Constrained-Reinforcement-Learning-with-Large-Deviations/README.md) | 不靠采样失败，用大偏差上界保证极低失效概率的安全强化学习 |
| 9 | [Reinforcement Learning in High-Energy Physics: A Survey from Accelerator Control to Theory Exploration](Reinforcement-Learning-in-High-Energy-Physics-A-Survey-from-Accelerator-Control-to-Theory-Exploratio/README.md) | 梳理强化学习在高能物理全链路的应用，并讲清何时该用它 |
| 10 | [Retrieval-Enhanced Cultural Evaluation for Social Media Translation Training](Retrieval-Enhanced-Cultural-Evaluation-for-Social-Media-Translation-Training/README.md) | 用检索补齐评审模型的文化知识，让翻译 RL 奖励更可靠 |
| 11 | [Silent Reward and Environment Defects in EV Charging Simulation Benchmarks: A Diagnostic Checklist](Silent-Reward-and-Environment-Defects-in-EV-Charging-Simulation-Benchmarks-A-Diagnostic-Checklist/README.md) | 揪出 RL 仿真基准里不报错却悄悄带偏对比结果的实现缺陷 |
| 12 | [Toward Executable Multi-framework Front-end Code Generation with Self-Correction](Toward-Executable-Multi-framework-Front-end-Code-Generation-with-Self-Correction/README.md) | 截图生成可编译的 React/Vue/Angular 项目，边生成边自我修复 |
| 13 | [Value Forcing: Aligning Return Distributions at All Noise Levels](Value-Forcing-Aligning-Return-Distributions-at-All-Noise-Levels/README.md) | 在流匹配每个噪声层都施加贝尔曼一致性，少数据也能学准回报分布 |

*由 RL-Frontier daily agent 自动生成 · 数据源 arXiv API*
