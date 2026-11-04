# RL 前沿日报 · 2026-10-30（21 篇）

| # | 论文 | 一句话概括 |
|---|------|-----------|
| 1 | [ART of PIV: Agentic Real-Time Particle Image Velocimetry for Active Flow Control](ART-of-PIV-Agentic-Real-Time-Particle-Image-Velocimetry-for-Active-Flow-Control/README.md) | 让小网络逐帧挑选PIV流程，又快又准地为流控提供反馈 |
| 2 | [CRoS: Causality Reward on Scrambled CoTs Improves Accuracy and Reasoning Faithfulness](CRoS-Causality-Reward-on-Scrambled-CoTs-Improves-Accuracy-and-Reasoning-Faithfulness/README.md) | 打乱推理步骤顺序衡量 CoT 因果性，作为 RL 辅助奖励 |
| 3 | [CausalXRL: Explainable Reinforcement Learning through Causal Graph Reasoning](CausalXRL-Explainable-Reinforcement-Learning-through-Causal-Graph-Reasoning/README.md) | 用因果图把 RL 智能体的决策逻辑讲清楚 |
| 4 | [Continual Reinforcement Learning Is an Integration Problem](Continual-Reinforcement-Learning-Is-an-Integration-Problem/README.md) | 持续强化学习的难点不在单项能力，而在把十项能力集成进一个智能体 |
| 5 | [From Representation to Readout: Mechanistic Analysis of Membership Signals in Language Models](From-Representation-to-Readout-Mechanistic-Analysis-of-Membership-Signals-in-Language-Models/README.md) | 成员信号由 SFT 写进表征，RL 主要改变读出 |
| 6 | [GRIT: Gradient Masking for Visually Misgrounded Tokens in Text-Rich Reasoning](GRIT-Gradient-Masking-for-Visually-Misgrounded-Tokens-in-Text-Rich-Reasoning/README.md) | 屏蔽看错图的 token 梯度，让 VLM 的 RLVR 不再奖励蒙对的推理 |
| 7 | [Hyperbolic Inverse Reinforcement Learning](Hyperbolic-Inverse-Reinforcement-Learning/README.md) | 用双曲空间距离定义奖励，让逆强化学习更省数据、更可解释 |
| 8 | [KEEPER: Learning Control-Sufficient Textual Memory for Long-Horizon LLM Agents](KEEPER-Learning-Control-Sufficient-Textual-Memory-for-Long-Horizon-LLM-Agents/README.md) | 对比四种辅助目标，奖励预测最能训好智能体的递归文本记忆 |
| 9 | [Latent Reasoning in Continuous Space for Unified Multimodal Models](Latent-Reasoning-in-Continuous-Space-for-Unified-Multimodal-Models/README.md) | 让多模态模型在连续隐空间里思考，生图也能测试时扩展 |
| 10 | [Multimodal In-Context Learning with Explicit Rule Induction](Multimodal-In-Context-Learning-with-Explicit-Rule-Induction/README.md) | 让多模态模型先从示例归纳规则再作答，SFT+RL 两阶段训练 |
| 11 | [Optimizing Stochastic Policy Geometry for Few-Step Flow Reinforcement Learning](Optimizing-Stochastic-Policy-Geometry-for-Few-Step-Flow-Reinforcement-Learning/README.md) | 为少步流模型 GRPO 选出几何最优的随机策略 |
| 12 | [Pinching Antennas for ISAC: Waveguide Architectures, Solutions, and Future Directions](Pinching-Antennas-for-ISAC-Waveguide-Architectures%2C-Solutions%2C-and-Future-Directions/README.md) | 用可移动的夹持天线做通感一体化，并以强化学习联合调控分段波导 |
| 13 | [RAMA: Retrieval-Augmented Multi-Agent Routing with Episodic Memory for LEO Satellite Networks](RAMA-Retrieval-Augmented-Multi-Agent-Routing-with-Episodic-Memory-for-LEO-Satellite-Networks/README.md) | 给每颗卫星配一本路由经验记忆，检索过往成功决策来选下一跳 |
| 14 | [RTL-Interact: Training EDA-Interactive Models for Multi-Task RTL Design](RTL-Interact-Training-EDA-Interactive-Models-for-Multi-Task-RTL-Design/README.md) | 让单个模型学会调用 EDA 工具自查自改 RTL 代码 |
| 15 | [Risk-Sensitive Mission Planning for Multi-Target On-Orbit Inspection via Distributional Reinforcement Learning](Risk-Sensitive-Mission-Planning-for-Multi-Target-On-Orbit-Inspection-via-Distributional-Reinforcemen/README.md) | 用分布式强化学习为在轨巡检规划调节风险偏好 |
| 16 | [Statistical Foundations of Reinforcement Learning: A Non-Asymptotic Perspective](Statistical-Foundations-of-Reinforcement-Learning-A-Non-Asymptotic-Perspective/README.md) | 系统梳理有限样本下强化学习样本复杂度理论的专著 |
| 17 | [TalentRL: Strategy-Guided Reinforcement Learning for Hierarchical Skill Routing](TalentRL-Strategy-Guided-Reinforcement-Learning-for-Hierarchical-Skill-Routing/README.md) | 先选策略再取技能，用对照干预给路由决策单独记功 |
| 18 | [Towards Understanding the Impact of Plasticity Loss on Reinforcement Learning in Stochastic Environments](Towards-Understanding-the-Impact-of-Plasticity-Loss-on-Reinforcement-Learning-in-Stochastic-Environm/README.md) | 噪声环境下，保住网络可塑性能让 RL 学得更稳 |
| 19 | [What Should LLMs Forget: Reinforcement Unlearning of Knowledge Associations](What-Should-LLMs-Forget-Reinforcement-Unlearning-of-Knowledge-Associations/README.md) | 只遗忘承载知识的关键 token，用强化学习做精准的 LLM 遗忘 |
| 20 | [When Is a Game a Markov Decision Process? Correspondences Between Game Theory and Reinforcement Learning](When-Is-a-Game-a-Markov-Decision-Process-Correspondences-Between-Game-Theory-and-Reinforcement-Learn/README.md) | 把博弈论与强化学习的对应关系从类比升级为定理的对照词典 |
| 21 | [rl_rob: A transparent, from-scratch Python library for teaching reinforcement learning from tabular methods to deep policy gradients](rlrob-A-transparent%2C-from-scratch-Python-library-for-teaching-reinforcement-learning-from-tabular-me/README.md) | 从表格法到 PPO 全程手写更新规则的 RL 教学库 |

*由 RL-Frontier daily agent 自动生成 · 数据源 arXiv API*
