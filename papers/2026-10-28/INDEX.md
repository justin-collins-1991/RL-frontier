# RL 前沿日报 · 2026-10-28（22 篇）

| # | 论文 | 一句话概括 |
|---|------|-----------|
| 1 | [AI-Driven Digital Twin Framework for Warehouse Logistics Automation Optimization](AI-Driven-Digital-Twin-Framework-for-Warehouse-Logistics-Automation-Optimization/README.md) | 在仓库数字孪生里训练 DQN，动态决定货品放哪个区 |
| 2 | [Aligning Autoresearch: Co-Improvement between Agents and Humans](Aligning-Autoresearch-Co-Improvement-between-Agents-and-Humans/README.md) | 让科研智能体与人类协同进化，而非单打独斗 |
| 3 | [CSO: Refining Robotic Policies via Skill Distribution Alignment and Skill-Grained Optimization](CSO-Refining-Robotic-Policies-via-Skill-Distribution-Alignment-and-Skill-Grained-Optimization/README.md) | 先拒绝采样微调稳住编码器，再按技能粒度做RL后训练 |
| 4 | [Co-Evolving Policy and Rubric via Capability Awareness for Open-Ended Generation](Co-Evolving-Policy-and-Rubric-via-Capability-Awareness-for-Open-Ended-Generation/README.md) | 让评分细则难度随策略能力动态演化的 Rubric RL |
| 5 | [Discovering Jailbreaks via Curriculum of Models](Discovering-Jailbreaks-via-Curriculum-of-Models/README.md) | 用由易到难的目标模型课程，缓解越狱发现的稀疏奖励 |
| 6 | [Discovery of Diverse and Realistic Financial Tail-Risk Using Generative Flow Networks](Discovery-of-Diverse-and-Realistic-Financial-Tail-Risk-Using-Generative-Flow-Networks/README.md) | 用连续 GFlowNet 按风险比例采样，生成多样且真实的金融尾部风险情景 |
| 7 | [Does 3D Pose Improve Action Valuation in Football? An Empirical Study of Pose Representations and Learning Objectives](Does-3D-Pose-Improve-Action-Valuation-in-Football-An-Empirical-Study-of-Pose-Representations-and-Lea/README.md) | 3D 姿态能预测下一动作，却难提升足球动作价值评估 |
| 8 | [Estimating Implicit Expected Log Density Ratios](Estimating-Implicit-Expected-Log-Density-Ratios/README.md) | 把期望对数密度比当作独立标量目标来估计，而非套用密度比估计 |
| 9 | [Game-Theoretic Foundations for Undiscounted Bisimulation Metrics](Game-Theoretic-Foundations-for-Undiscounted-Bisimulation-Metrics/README.md) | 用博弈值函数重建无折扣设定下的双模拟度量 |
| 10 | [Geometric Time Score Estimators: Bridging Self-Predictive Representations and Generative Occupancy Models For Reinforcement Learning](Geometric-Time-Score-Estimators-Bridging-Self-Predictive-Representations-and-Generative-Occupancy-Mo/README.md) | 沿概率路径学时间分数，把生成式占用模型变成准确的密度估计器 |
| 11 | [HEDGE: Gated Hypergraph Memory for Scalable Multi-Agent Debate](HEDGE-Gated-Hypergraph-Memory-for-Scalable-Multi-Agent-Debate/README.md) | 用超图记忆加RL门控，让多智能体辩论更准、更省 |
| 12 | [Latent Decision Flow Rewards for Clinical Guideline Reasoning](Latent-Decision-Flow-Rewards-for-Clinical-Guideline-Reasoning/README.md) | 用多条候选决策流加答案门控的过程奖励训练临床指南推理 |
| 13 | [Learning to Reason from Reference Samples Alone: Reinforced Adversarial Learning for Modern LLM Post-Training](Learning-to-Reason-from-Reference-Samples-Alone-Reinforced-Adversarial-Learning-for-Modern-LLM-Post/README.md) | 只靠参考答案和共训判别器，训练出比肩 RLVR 的推理模型 |
| 14 | [Nemotron 3.5 Super and Lightning: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Models for Agentic AI](Nemotron-3.5-Super-and-Lightning-Open%2C-Efficient-Mixture-of-Experts-Hybrid-Mamba-Transformer-Models/README.md) | NVIDIA 开源的高效 MoE 混合 Mamba 智能体模型，能力与推理吞吐兼顾 |
| 15 | [Post-Training Large Language Models with LLMON](Post-Training-Large-Language-Models-with-LLMON/README.md) | 用结构化标记加后训练，让模型只执行被显式指定的指令 |
| 16 | [Reinforcement Learning for the Game of Balatro: A Fast Simulator and Two-Policy Training Approach](Reinforcement-Learning-for-the-Game-of-Balatro-A-Fast-Simulator-and-Two-Policy-Training-Approach/README.md) | 高保真 Rust 模拟器加出牌/商店双策略 PPO，让 RL 玩转 Balatro |
| 17 | [SCOPE: Selective Critical-Step On-Policy Self-Distillation for Agentic Reinforcement Learning](SCOPE-Selective-Critical-Step-On-Policy-Self-Distillation-for-Agentic-Reinforcement-Learning/README.md) | 只在出错的关键步做自蒸馏，让智能体RL又准又省步 |
| 18 | [Scaling Lean Theorem Proving for Real-World Code Verification](Scaling-Lean-Theorem-Proving-for-Real-World-Code-Verification/README.md) | 免训练递归智能体刷爆 Lean 基准，再造更难的真实代码验证题 |
| 19 | [Skillful and realistic precipitation forecasting with reinforced diffusion](Skillful-and-realistic-precipitation-forecasting-with-reinforced-diffusion/README.md) | 用强化学习微调离散扩散模型，降水预报准确又不糊 |
| 20 | [Transportable Offline Reinforcement Learning in Presence of Unmeasured Confounding](Transportable-Offline-Reinforcement-Learning-in-Presence-of-Unmeasured-Confounding/README.md) | 融合多源混杂数据，因果可迁移地学习目标域离线策略 |
| 21 | [Two Birds with One Stone: Skill-Augmented Generation via Unified Retrieval and Utilization](Two-Birds-with-One-Stone-Skill-Augmented-Generation-via-Unified-Retrieval-and-Utilization/README.md) | 用一个模型端到端 RL 联合学会检索技能与使用技能 |
| 22 | [Variational Consequence-Driven Offline Reinforcement Learning](Variational-Consequence-Driven-Offline-Reinforcement-Learning/README.md) | 约束动作带来的后果，而不只约束动作本身 |

*由 RL-Frontier daily agent 自动生成 · 数据源 arXiv API*
