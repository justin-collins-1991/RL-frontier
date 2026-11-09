# RL 前沿日报 · 2026-11-05（25 篇）

| # | 论文 | 一句话概括 |
|---|------|-----------|
| 1 | [Accelerating Safe Reinforcement Learning with Massive Parallelism](Accelerating-Safe-Reinforcement-Learning-with-Massive-Parallelism/README.md) | 用相位聚合代价估计让安全RL跑上大规模并行仿真 |
| 2 | [Agent-R$^2$: Scaling Agents for Realistic Productivity Work via Real-Source Data Synthesis](Agent-R2-Scaling-Agents-for-Realistic-Productivity-Work-via-Real-Source-Data-Synthesis/README.md) | 用真实来源合成办公任务数据，让 4B 智能体超越 235B |
| 3 | [AttnSR: Attention Step Reward for Long-Horizon Agentic RL](AttnSR-Attention-Step-Reward-for-Long-Horizon-Agentic-RL/README.md) | 用策略模型自身注意力回溯分配步级奖励，无需奖励模型 |
| 4 | [Detecting Silent Faults at the Environment-Trainer Boundary in Reinforcement Learning](Detecting-Silent-Faults-at-the-Environment-Trainer-Boundary-in-Reinforcement-Learning/README.md) | 学习曲线看不出环境边界上的静默故障，两端逐步对账才能抓住 |
| 5 | [Discovering Learning Rules that Shape Others](Discovering-Learning-Rules-that-Shape-Others/README.md) | 元学习出只看自身经验、却能塑造对手的更新规则 |
| 6 | [Does a Trading Policy Need to Know What It Trades? Microstructure Invariance and Zero-Shot Transfer of Execution Policies](Does-a-Trading-Policy-Need-to-Know-What-It-Trades-Microstructure-Invariance-and-Zero-Shot-Transfer-o/README.md) | 用资产自身尺度归一化，一个执行策略零样本通吃数千只股票 |
| 7 | [Efficient Diffusion Policy Fine Tuning with Latent Noise Representation Bridging](Efficient-Diffusion-Policy-Fine-Tuning-with-Latent-Noise-Representation-Bridging/README.md) | 用共享表征桥接噪声与动作价值，只调初始噪声高效微调扩散策略 |
| 8 | [Enhancing Repository-Level Code Completion with Reinforcement Learning in Real-World Scenarios](Enhancing-Repository-Level-Code-Completion-with-Reinforcement-Learning-in-Real-World-Scenarios/README.md) | 用标识符意图奖励和选择性探索让7B模型学会跨文件补全 |
| 9 | [FewStepRL: Fine-tuning Few-step Diffusion Models with Reinforcement Learning](FewStepRL-Fine-tuning-Few-step-Diffusion-Models-with-Reinforcement-Learning/README.md) | 把主流扩散 RL 目标系统性迁移到少步生成模型的统一框架 |
| 10 | [Measuring the Marginal Value of Verifier-Based RL Beyond Supervised Fine-Tuning](Measuring-the-Marginal-Value-of-Verifier-Based-RL-Beyond-Supervised-Fine-Tuning/README.md) | SFT 之后再做 RLVR，几乎只剩不到半个点的边际收益 |
| 11 | [Monotone Viability Learning for Offline Safe Reinforcement Learning](Monotone-Viability-Learning-for-Offline-Safe-Reinforcement-Learning/README.md) | 用逐层收缩的二值可行集从离线数据学长时域安全，部署时为动作把关 |
| 12 | [Permanent and Transient Representations for Continual Reinforcement Learning](Permanent-and-Transient-Representations-for-Continual-Reinforcement-Learning/README.md) | 长期价值用神经网络，短期修正用非参数记忆，持续RL两全 |
| 13 | [Provable Zeroth-Order Safe Exploration for Reinforcement Learning from Human Feedback](Provable-Zeroth-Order-Safe-Exploration-for-Reinforcement-Learning-from-Human-Feedback/README.md) | 免奖励模型的 RLHF，训练全程每个策略都可证明安全 |
| 14 | [Q-OIL: Optimistic Exploration in Learning from Human Interventions](Q-OIL-Optimistic-Exploration-in-Learning-from-Human-Interventions/README.md) | 把人类接管当作乐观探索奖励，而非最优示范 |
| 15 | [RL-ATTACK: A Generalized Black-Box Adversarial Attack on Language Models via Reinforcement Learning](RL-ATTACK-A-Generalized-Black-Box-Adversarial-Attack-on-Language-Models-via-Reinforcement-Learning/README.md) | 用策略梯度训练黑盒攻击器，按目标模型定制文本对抗扰动 |
| 16 | [RLGPA: A Reinforcement Learning-Guided Granularity Planning Attack for Decision-Based Sparse Adversarial Examples](RLGPA-A-Reinforcement-Learning-Guided-Granularity-Planning-Attack-for-Decision-Based-Sparse-Adversar/README.md) | 用在线 DQN 调度还原粒度，让纯标签黑盒稀疏攻击更省查询 |
| 17 | [RM-VLM: From Natural-Language Task Descriptions to Vision-Grounded Reward Machines](RM-VLM-From-Natural-Language-Task-Descriptions-to-Vision-Grounded-Reward-Machines/README.md) | LLM 写奖励机、VLM 看图打标签，免手工做时序任务奖励 |
| 18 | [SHORE: Stability-Hybrid On-Policy Reinforcement Learning for Online Bin Packing](SHORE-Stability-Hybrid-On-Policy-Reinforcement-Learning-for-Online-Bin-Packing/README.md) | 把学到的堆叠稳定概率融进策略，让装箱RL权衡风险与装载率 |
| 19 | [Spectral and Subspace Dynamics of LoRA in Supervised Fine-Tuning and Reinforcement Learning](Spectral-and-Subspace-Dynamics-of-LoRA-in-Supervised-Fine-Tuning-and-Reinforcement-Learning/README.md) | 组均值基线让RL的LoRA更新谱更集中、子空间转得更快 |
| 20 | [The Blindfolded Controller: Decision Model-Guided Training for Reinforcement Learning](The-Blindfolded-Controller-Decision-Model-Guided-Training-for-Reinforcement-Learning/README.md) | 用零样本决策模型给 RL 开局，再靠奖励青出于蓝 |
| 21 | [Towards Foundation Decision Models: Drex](Towards-Foundation-Decision-Models-Drex/README.md) | 不做自回归生成，直接输出选项概率的开源决策模型 |
| 22 | [Training Stability under Adaptive Curricula](Training-Stability-under-Adaptive-Curricula/README.md) | 自适应课程会把学生练废，稳住学习者才能让课程发挥作用 |
| 23 | [Unpacking the Compute Efficiency of Strong-to-Weak OPD against GRPO](Unpacking-the-Compute-Efficiency-of-Strong-to-Weak-OPD-against-GRPO/README.md) | 按 FLOPs 算账：外部教师蒸馏不如 GRPO，先分域 RL 再多教师蒸馏才省 |
| 24 | [Value-oriented policy distillation for interpretable wind farm power control](Value-oriented-policy-distillation-for-interpretable-wind-farm-power-control/README.md) | 把 SAC 风场调度策略蒸馏成可解释的 EBM 加性模型 |
| 25 | [s$^3$: Simple Scaling of Swarms via Cooperative Multi-agent RL](s3-Simple-Scaling-of-Swarms-via-Cooperative-Multi-agent-RL/README.md) | 用团队共享奖励训练 LLM 蜂群，让分工与沟通自发涌现 |

*由 RL-Frontier daily agent 自动生成 · 数据源 arXiv API*
