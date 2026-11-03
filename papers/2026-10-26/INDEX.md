# RL 前沿日报 · 2026-10-26（26 篇）

| # | 论文 | 一句话概括 |
|---|------|-----------|
| 1 | [Audit Where Hacks Pay: Budgeted Strong-Verifier Audits Against Reward Hacking in GRPO](Audit-Where-Hacks-Pay-Budgeted-Strong-Verifier-Audits-Against-Reward-Hacking-in-GRPO/README.md) | 强验证预算优先审低通过组，用反射惩罚压制 GRPO 奖励作弊 |
| 2 | [Belief-Conditioned Multi-Agent Actor Critic for Decentralized LLM Collaboration](Belief-Conditioned-Multi-Agent-Actor-Critic-for-Decentralized-LLM-Collaboration/README.md) | 给每个 LLM 智能体加一个信念编码器，让多智能体协作训练更高效 |
| 3 | [Bridging Exploration and Loss of Plasticity in On-Policy Reinforcement Learning](Bridging-Exploration-and-Loss-of-Plasticity-in-On-Policy-Reinforcement-Learning/README.md) | PPO 塑性丧失的一大推手是高斯策略标准差坍缩 |
| 4 | [CalibraRL: Confidence-Calibrated Reinforcement Learning for Mitigating Hallucinations in RAG](CalibraRL-Confidence-Calibrated-Reinforcement-Learning-for-Mitigating-Hallucinations-in-RAG/README.md) | 让奖励看置信度和同题证据，重罚自信的错答、少做多余拒答 |
| 5 | [Causal DAG-Guided Reinforcement Learning for Long-Term Physical Activity Maintenance: Using Prior Data to Inform Future Deployment](Causal-DAG-Guided-Reinforcement-Learning-for-Long-Term-Physical-Activity-Maintenance-Using-Prior-Dat/README.md) | 用专家因果图驱动个性化在线RL，助力长期运动习惯养成 |
| 6 | [Centralized Critics for N-Agent Ad Hoc Teamwork](Centralized-Critics-for-N-Agent-Ad-Hoc-Teamwork/README.md) | 训练时让 Critic 看到陌生队友历史，更稳更高效 |
| 7 | [DTCA: Denoising Token Credit Assignment for Reinforcement Learning in Diffusion Language Models](DTCA-Denoising-Token-Credit-Assignment-for-Reinforcement-Learning-in-Diffusion-Language-Models/README.md) | 按词性估计去噪贡献，为扩散语言模型 RL 做 token 级信用分配 |
| 8 | [End-to-End MXFP8 Reinforcement Learning on Blackwell: What Matching Buys, When It Pays Off, and How It Fails](End-to-End-MXFP8-Reinforcement-Learning-on-Blackwell-What-Matching-Buys%2C-When-It-Pays-Off%2C-and-How-I/README.md) | 在 Blackwell 上实测端到端 MXFP8 强化学习的一致性、提速门槛与失效模式 |
| 9 | [EvoRouter: Cost-Efficient Multi-Agent Routing via Insight-Guided On-Policy Distillation](EvoRouter-Cost-Efficient-Multi-Agent-Routing-via-Insight-Guided-On-Policy-Distillation/README.md) | 把跨任务路由经验蒸馏进策略，多智能体配置更准更省 |
| 10 | [Evolve on Graph: Self-Evolving Knowledge Graph Reasoning without Question Annotations](Evolve-on-Graph-Self-Evolving-Knowledge-Graph-Reasoning-without-Question-Annotations/README.md) | 只给知识图谱，LLM 靠自问自答的自博弈学会多跳图推理 |
| 11 | [FOCUS: Active Critic Learning for Long-Horizon Language Model Agents](FOCUS-Active-Critic-Learning-for-Long-Horizon-Language-Model-Agents/README.md) | 把分支采样当主动学习，只在 critic 最不准的地方补 rollout |
| 12 | [Freeze, Don't Clone: Fine-Tuning with Expressive Policies Without Retaining Offline Data](Freeze%2C-Dont-Clone-Fine-Tuning-with-Expressive-Policies-Without-Retaining-Offline-Data/README.md) | 离线数据删除后冻结行为先验，只让价值学习继续改进 |
| 13 | [GPDPO: Learning from Reward Conflicts via Group Pareto-Dominance Policy Optimization](GPDPO-Learning-from-Reward-Conflicts-via-Group-Pareto-Dominance-Policy-Optimization/README.md) | 用帕累托支配关系，从被冲突过滤的样本里找回成对监督 |
| 14 | [Improving Reasoning with Rollout Agreement for Group-Based Policy Optimization](Improving-Reasoning-with-Rollout-Agreement-for-Group-Based-Policy-Optimization/README.md) | 奖励与同组推理一致的正确 rollout，减少蒙对式推理 |
| 15 | [InterQ-RL: Interaction-Aware Correction of Execution Mismatch in Quantized Agentic RL](InterQ-RL-Interaction-Aware-Correction-of-Execution-Mismatch-in-Quantized-Agentic-RL/README.md) | 沿动作历史纠偏，让 8bit 量化 rollout 的多轮 Agent RL 追平 BF16 |
| 16 | [Jaxnasium: Embracing PyTrees For Any-Agent, Cross-Suite Reinforcement Learning](Jaxnasium-Embracing-PyTrees-For-Any-Agent%2C-Cross-Suite-Reinforcement-Learning/README.md) | 用 PyTree 统一空间，一份算法代码跑遍 300+ 环境 |
| 17 | [Multi-Objective Reinforcement Learning Using Routed Ensembles and Trajectory Attribution](Multi-Objective-Reinforcement-Learning-Using-Routed-Ensembles-and-Trajectory-Attribution/README.md) | 用少量基策略路由和轨迹归因化解多目标冲突 |
| 18 | [Preference-Guided Cooperation in Multi-Objective Multi-Agent Reinforcement Learning](Preference-Guided-Cooperation-in-Multi-Objective-Multi-Agent-Reinforcement-Learning/README.md) | 用元梯度学习个体目标偏好，让多目标结构直接引导多智能体协作 |
| 19 | [Provably Efficient Q-learning for Robust Reinforcement Learning](Provably-Efficient-Q-learning-for-Robust-Reinforcement-Learning/README.md) | 单条轨迹上做鲁棒 Q-learning，样本效率逼近最优 |
| 20 | [Reinforcement Learning Done Right for Explicit Confidence Targets](Reinforcement-Learning-Done-Right-for-Explicit-Confidence-Targets/README.md) | 让单个大模型按提示里的置信度目标自主决定回答或弃答 |
| 21 | [S3AC: Stabilized, Selective, and Scalable Actor-Critic for LLM Reasoning](S3AC-Stabilized%2C-Selective%2C-and-Scalable-Actor-Critic-for-LLM-Reasoning/README.md) | 把 critic 训稳，让长 CoT 的 RLVR 重回 Actor-Critic |
| 22 | [SEMA-Auto: Sighted and Efficient Multi-Turn Attack with Autonomy](SEMA-Auto-Sighted-and-Efficient-Multi-Turn-Attack-with-Autonomy/README.md) | 用强化学习训练会看回复、能自己判断何时收手的多轮红队攻击模型 |
| 23 | [SimPOTrans: Self-Adaptation for Offline-to-Simultaneous Speech Translation via Reinforcement Learning](SimPOTrans-Self-Adaptation-for-Offline-to-Simultaneous-Speech-Translation-via-Reinforcement-Learning/README.md) | 用 GRPO 让离线语音翻译模型自适应成同传模型 |
| 24 | [Test-Time Confidence Adaptation under RL-Induced Trajectory Shift](Test-Time-Confidence-Adaptation-under-RL-Induced-Trajectory-Shift/README.md) | 用轨迹稳定性做无标签信号，修复 Agentic RL 后失效的置信度估计 |
| 25 | [Uncovering the Turing Test's Latent Signal: Indistinguishability as a Reward](Uncovering-the-Turing-Tests-Latent-Signal-Indistinguishability-as-a-Reward/README.md) | 让学生模型骗过老师的图灵测试，本身就是有效的RL奖励 |
| 26 | [When Fine-Grained Credit Assignment Helps and Hurts: Multimodal Agentic Reinforcement Learning through Video Editing](When-Fine-Grained-Credit-Assignment-Helps-and-Hurts-Multimodal-Agentic-Reinforcement-Learning-throug/README.md) | 细粒度信用分配只在超长程任务上有用，且要及时退场 |

*由 RL-Frontier daily agent 自动生成 · 数据源 arXiv API*
