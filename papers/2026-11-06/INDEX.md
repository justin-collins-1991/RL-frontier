# RL 前沿日报 · 2026-11-06（19 篇）

| # | 论文 | 一句话概括 |
|---|------|-----------|
| 1 | [AUTEUR: Acoustic Plan Learning for Red-Teaming Text-to-Audio Models](AUTEUR-Acoustic-Plan-Learning-for-Red-Teaming-Text-to-Audio-Models/README.md) | 用结构化声学计划加波形反馈 RL，自动红队测试文生音频模型 |
| 2 | [Adaptive Scheduling Pipeline for Multi-Instance Asynchronous Reinforcement Learning](Adaptive-Scheduling-Pipeline-for-Multi-Instance-Asynchronous-Reinforcement-Learning/README.md) | 离线调度 rollout，消除三类气泡，异步 RL 提速 3 倍 |
| 3 | [Autonomous Particle Image Velocimetry Using Zero-Shot Sim-to-Real Reinforcement Learning](Autonomous-Particle-Image-Velocimetry-Using-Zero-Shot-Sim-to-Real-Reinforcement-Learning/README.md) | 让机械臂相机用强化学习自己找到并拍清水翼尾流 |
| 4 | [CARGO: Causal Attribution and Responsibility-Guided Preventive Safe Multi-Agent Reinforcement Learning for Cooperative Driving](CARGO-Causal-Attribution-and-Responsibility-Guided-Preventive-Safe-Multi-Agent-Reinforcement-Learnin/README.md) | 用因果归因分清功劳与责任，让多车匝道汇入更安全 |
| 5 | [Designing Effective Monitor-Based Interventions for Mitigating Reward Hacking During RL](Designing-Effective-Monitor-Based-Interventions-for-Mitigating-Reward-Hacking-During-RL/README.md) | RL 中用监控器惩罚奖励作弊，怎样设计才不被模型绕过 |
| 6 | [Encoding Memory in World Models with Test-Time Model-Based Reinforcement Learning](Encoding-Memory-in-World-Models-with-Test-Time-Model-Based-Reinforcement-Learning/README.md) | 测试时用梯度下降把记忆写进世界模型参数 |
| 7 | [Grasp-TAGS: Task-Aware Grasp Selection via Critic Distillation for Prehensile Loco-Manipulation](Grasp-TAGS-Task-Aware-Grasp-Selection-via-Critic-Distillation-for-Prehensile-Loco-Manipulation/README.md) | 把 PPO 的 critic 蒸馏成抓取打分器，搬大件前先选对抓法 |
| 8 | [MARS: Training Multilingual Search Agents for Retriever-Free Evidence Acquisition](MARS-Training-Multilingual-Search-Agents-for-Retriever-Free-Evidence-Acquisition/README.md) | 用 grep 代替检索器，RL 训练多语言搜索智能体 |
| 9 | [Not All Entropy Is Equal: Reward-Conditioned Entropy Allocation in Reinforcement Learning with Verifiable Rewards](Not-All-Entropy-Is-Equal-Reward-Conditioned-Entropy-Allocation-in-Reinforcement-Learning-with-Verifi/README.md) | 熵塌缩要看去掉的是哪种不确定性，而不是熵的大小 |
| 10 | [On the Reliability of Majority-Vote Pseudo-Labels in Test-Time Reinforcement Learning](On-the-Reliability-of-Majority-Vote-Pseudo-Labels-in-Test-Time-Reinforcement-Learning/README.md) | 按投票可靠度逐题调节更新力度，让测试时 RL 少被噪声伪标签带偏 |
| 11 | [Probably Safe Sim-to-Real Transfer with Lifetime Validity](Probably-Safe-Sim-to-Real-Transfer-with-Lifetime-Validity/README.md) | 上线前用基线数据给仿真策略做安全认证，无限次更新都成立 |
| 12 | [RPEG: Training Reasoning Language Models Scalably and Cost-Effectively](RPEG-Training-Reasoning-Language-Models-Scalably-and-Cost-Effectively/README.md) | 用图表示统一优化 RL 训练流水线的结构与执行 |
| 13 | [RuACT: Recovering Inactive Rubrics as Adaptive Critics and Teachers](RuACT-Recovering-Inactive-Rubrics-as-Adaptive-Critics-and-Teachers/README.md) | 让全错或全对的失效评分项重新提供学习信号 |
| 14 | [STRIDE: Learning Humanoid Locomotion in Minutes with Acceleration-Based Rewards](STRIDE-Learning-Humanoid-Locomotion-in-Minutes-with-Acceleration-Based-Rewards/README.md) | 只用IMU加速度奖励，14分钟样本学会人形机器人行走 |
| 15 | [Safe Reinforcement Learning via Probabilistic Option Shielding](Safe-Reinforcement-Learning-via-Probabilistic-Option-Shielding/README.md) | 把概率逻辑护盾升级到选项层，无需环境模型也能保障长程安全 |
| 16 | [Safety-Focused Reinforcement Learning Using Risk-Sensitive Coupled Control](Safety-Focused-Reinforcement-Learning-Using-Risk-Sensitive-Coupled-Control/README.md) | 用风险敏感与平均成本双时间尺度Q学习实现状态级安全控制 |
| 17 | [Steerable Multi-Objective Group-Relative Preference Optimization with Jointly Trained Low-Rank Adapters](Steerable-Multi-Objective-Group-Relative-Preference-Optimization-with-Jointly-Trained-Low-Rank-Adapt/README.md) | 每个目标一个 LoRA 联合训练，推理时按偏好随意调配 |
| 18 | [TUGB: A Two-stage Uncertainty-aware Generative Auto-Bidding Framework](TUGB-A-Two-stage-Uncertainty-aware-Generative-Auto-Bidding-Framework/README.md) | 用不确定性感知的环境模型对生成式出价模型做 RL 微调 |
| 19 | [Towards Robust Reinforcement Learning Market Making: Lessons from Loss Function Experimentation](Towards-Robust-Reinforcement-Learning-Market-Making-Lessons-from-Loss-Function-Experimentation/README.md) | 给做市 RL 的损失加上库存与现金惩罚，策略更稳也更赚 |

*由 RL-Frontier daily agent 自动生成 · 数据源 arXiv API*
