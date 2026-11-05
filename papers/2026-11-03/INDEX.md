# RL 前沿日报 · 2026-11-03（27 篇）

| # | 论文 | 一句话概括 |
|---|------|-----------|
| 1 | [Aligning Training and Rollout Policies for End-to-End FP4 RL on Mixture-of-Experts LLMs](Aligning-Training-and-Rollout-Policies-for-End-to-End-FP4-RL-on-Mixture-of-Experts-LLMs/README.md) | MoE 做 FP4 强化学习，训练和推理两侧必须对称纠偏 |
| 2 | [CANDO: Conservative Action-Noise Directional Optimization for Residual Reinforcement Learning](CANDO-Conservative-Action-Noise-Directional-Optimization-for-Residual-Reinforcement-Learning/README.md) | 噪声空间与动作空间双残差联合微调冻结生成式策略 |
| 3 | [CORA: Teacher-Guided Causal O-RAN Adaptation for Jamming Detection](CORA-Teacher-Guided-Causal-O-RAN-Adaptation-for-Jamming-Detection/README.md) | 用事后检测器当老师，无标签训练RL实时调参抓干扰 |
| 4 | [CRONOS: Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation](CRONOS-Benchmarking-Non-Episodic-Reinforcement-Learning-for-Robotic-Manipulation/README.md) | 首个研究VLA在少重置条件下做RL微调的仿真基准 |
| 5 | [Catalyzing Interactive HTML Generation Capabilities via High-Fidelity Reinforcement Learning](Catalyzing-Interactive-HTML-Generation-Capabilities-via-High-Fidelity-Reinforcement-Learning/README.md) | 用小游戏做试验场，靠高保真浏览器交互反馈强化学习，提升 HTML 生成能力 |
| 6 | [Cooperative Multi-Agent Reinforcement Learning with Submodular Trajectory Rewards](Cooperative-Multi-Agent-Reinforcement-Learning-with-Submodular-Trajectory-Rewards/README.md) | 用前窗曲率换取多智能体子模奖励RL的多项式近似保证 |
| 7 | [Density-Aware Reward Scaling: A Reinforcement Learning Framework for Reward-Proportional Sampling](Density-Aware-Reward-Scaling-A-Reinforcement-Learning-Framework-for-Reward-Proportional-Sampling/README.md) | 按组内局部密度缩放奖励，让 GRPO 不再只收敛到单一模式 |
| 8 | [Found by Search, Broken by a Shortcut: Transfer and Tampering of Searched Intrinsic Rewards](Found-by-Search%2C-Broken-by-a-Shortcut-Transfer-and-Tampering-of-Searched-Intrinsic-Rewards/README.md) | 搜索出的内在奖励能迁移，却挡不住搜索时没见过的捷径 |
| 9 | [FourSight: Stable FP4 RL Post-Training via Sequence Filtering and Sparse Channel Compensation](FourSight-Stable-FP4-RL-Post-Training-via-Sequence-Filtering-and-Sparse-Channel-Compensation/README.md) | 过滤坏轨迹加少量通道补精度，让 FP4 强化学习稳定训练 |
| 10 | [GSBR: Geometric Support Behavior Regularization for Online RL](GSBR-Geometric-Support-Behavior-Regularization-for-Online-RL/README.md) | 按动作到基策略支撑集的距离施加惩罚，兼顾选模与局部改进 |
| 11 | [Harness-S: Learning from Sibling Harnesses for Generalizable Agent Training](Harness-S-Learning-from-Sibling-Harnesses-for-Generalizable-Agent-Training/README.md) | 用兄弟 harness 救援失败样本，把能力内化进单一策略 |
| 12 | [JHiMA-WebRL: A Joint Hierarchical Multi-Agent Reinforcement Learning Framework for Long-Horizon Web Tasks](JHiMA-WebRL-A-Joint-Hierarchical-Multi-Agent-Reinforcement-Learning-Framework-for-Long-Horizon-Web-T/README.md) | 规划器与执行器用分层 GRPO 联合训练，两个 7B 胜过 32B 单体 |
| 13 | [LLMs as MDP Designers: A Dependency-Aware Agentic Framework for Automated Robot Policy Generation](LLMs-as-MDP-Designers-A-Dependency-Aware-Agentic-Framework-for-Automated-Robot-Policy-Generation/README.md) | 让 LLM 当 RL 设计师，从自然语言自动生成可训练的机器人策略 |
| 14 | [MDSKILL: Learning to Internalize Skill Memory through Multi-View Distillation for Efficient Dynamic Agent Self-Evolution](MDSKILL-Learning-to-Internalize-Skill-Memory-through-Multi-View-Distillation-for-Efficient-Dynamic-A/README.md) | 把技能记忆按功能拆成多视角再自蒸馏，让智能体把经验内化进参数 |
| 15 | [ModelBlaster: Closing the Performance Gap through Learning-Augmented Agents Across Models, Kernels and Hardware Backends](ModelBlaster-Closing-the-Performance-Gap-through-Learning-Augmented-Agents-Across-Models%2C-Kernels-an/README.md) | 用可持续积累的经验库让 LLM 智能体跨硬件优化算子与整模型 |
| 16 | [Near-Minimax Sample Complexity for Multi-Objective Reinforcement Learning under Generative Models](Near-Minimax-Sample-Complexity-for-Multi-Objective-Reinforcement-Learning-under-Generative-Models/README.md) | 一份数据服务所有偏好：多目标 RL 的代价只随目标数对数增长 |
| 17 | [OdorSpaces: Visual-Olfactory Embodied Navigation in 3D Environments](OdorSpaces-Visual-Olfactory-Embodied-Navigation-in-3D-Environments/README.md) | 给具身智能体装上“鼻子”：基于物理气味场的视觉-嗅觉导航基准 |
| 18 | [On the Generalization Limitation of On-Policy Distillation for Post-RL Consolidation](On-the-Generalization-Limitation-of-On-Policy-Distillation-for-Post-RL-Consolidation/README.md) | 在线策略蒸馏分布内近乎完美，分布外却在遗忘和组合上掉分 |
| 19 | [Policy Network Diffusion](Policy-Network-Diffusion/README.md) | 用扩散模型直接按任务生成 RL 策略网络参数 |
| 20 | [PolicyIK: High-Precision Inverse Kinematics for Robot Arms with Reinforcement Learning](PolicyIK-High-Precision-Inverse-Kinematics-for-Robot-Arms-with-Reinforcement-Learning/README.md) | 纯 RL 策略做逆运动学，机械臂毫米级到位并稳住 |
| 21 | [ReSI-Math: Exploring Recoverable Capability Frontiers for Efficient Reasoning Improvement](ReSI-Math-Exploring-Recoverable-Capability-Frontiers-for-Efficient-Reasoning-Improvement/README.md) | 用轨迹进化搜索找出模型做错但能救回来的题来做 RLVR |
| 22 | [Reconstructing Fraudulent Strategies in Online Payments via Interpretable Inverse Reinforcement Learning](Reconstructing-Fraudulent-Strategies-in-Online-Payments-via-Interpretable-Inverse-Reinforcement-Lear/README.md) | 用可解释逆强化学习还原欺诈者策略，生成样本增强反欺诈检测 |
| 23 | [Revisiting Critic Estimation in Soft Actor-Critic Algorithms](Revisiting-Critic-Estimation-in-Soft-Actor-Critic-Algorithms/README.md) | SAC 换评论家：回放数据上的多步 λ-return 最有效 |
| 24 | [Self-Privileged Fine-Tuning](Self-Privileged-Fine-Tuning/README.md) | 让看过答案的冻结自身模型为 SFT 逐 token 加权 |
| 25 | [Suppressing Misaligned Behaviors in Language Models, Durably](Suppressing-Misaligned-Behaviors-in-Language-Models%2C-Durably/README.md) | 从半途走偏的状态起练纠偏，让压制下去的坏行为不再复发 |
| 26 | [Training Specialist LLMs on Your Phone: Forward-Only Optimization via Block-Spectral Coordinates](Training-Specialist-LLMs-on-Your-Phone-Forward-Only-Optimization-via-Block-Spectral-Coordinates/README.md) | 只用前向传播和可验证奖励，在手机上一夜训出几MB的专用LLM |
| 27 | [Where Did the Update Go? Certifying Declared Change Envelopes for Model Updates](Where-Did-the-Update-Go-Certifying-Declared-Change-Envelopes-for-Model-Updates/README.md) | 无需标签，认证模型更新只改了事先声明的范围 |

*由 RL-Frontier daily agent 自动生成 · 数据源 arXiv API*
