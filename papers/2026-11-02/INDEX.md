# RL 前沿日报 · 2026-11-02（35 篇）

| # | 论文 | 一句话概括 |
|---|------|-----------|
| 1 | [A Universal Policy Wrapper With Guarantees](A-Universal-Policy-Wrapper-With-Guarantees/README.md) | 部署时用critic切换RL与保底策略，继承目标可达保证 |
| 2 | [AffToM: Benchmarking Recursive Affective Theory of Mind in Dynamic Multi-Party Interactions](AffToM-Benchmarking-Recursive-Affective-Theory-of-Mind-in-Dynamic-Multi-Party-Interactions/README.md) | 考察多人视频里“我以为你以为他的感受”的递归情感推理 |
| 3 | [An Axiomatic Framework for Reinforcement Learning in Open Multi-Agent Systems](An-Axiomatic-Framework-for-Reinforcement-Learning-in-Open-Multi-Agent-Systems/README.md) | 用 Shapley 公理约束开放多智能体系统中的价值函数学习 |
| 4 | [Auditing Representation-Space Fraud Detection: A Bayesian IRL Framework for Calibrated Uncertainty and Its Limits](Auditing-Representation-Space-Fraud-Detection-A-Bayesian-IRL-Framework-for-Calibrated-Uncertainty-an/README.md) | 用贝叶斯IRL审计推荐刷单检测，揭示表征空间的盲区 |
| 5 | [Axion 1.0: Open Agent Foundation Models, Simplified](Axion-1.0-Open-Agent-Foundation-Models%2C-Simplified/README.md) | 两段轻量SFT加RL，极简配方训出全开源强Agent模型 |
| 6 | [BLPO: Beyond-Local Policy Optimization for Long-Horizon LLM Agents](BLPO-Beyond-Local-Policy-Optimization-for-Long-Horizon-LLM-Agents/README.md) | 跨任务共享经验做步级信用分配，提升长程 Agent RL |
| 7 | [Bayesian Sequential Optimal Experimental Design for Single-Pixel Imaging using Reinforcement Learning](Bayesian-Sequential-Optimal-Experimental-Design-for-Single-Pixel-Imaging-using-Reinforcement-Learnin/README.md) | 用强化学习为单像素成像自适应挑选最有信息量的照明图案 |
| 8 | [Beyond $L_\infty$-Norm Sets: Synthesizing Interpretable Non-Uniform Uncertainty Sets for Evaluation-Time State-Adversarial Robustness](Beyond-Linfty-Norm-Sets-Synthesizing-Interpretable-Non-Uniform-Uncertainty-Sets-for-Evaluation-Time/README.md) | 按性能损失容忍度，给每个状态维度定制扰动预算 |
| 9 | [Bridging Neural Tangent Kernel Analysis and Reinforcement Learning for Deep Function Approximation](Bridging-Neural-Tangent-Kernel-Analysis-and-Reinforcement-Learning-for-Deep-Function-Approximation/README.md) | 把 NTK 理论推广到 TD 学习，并用闭式解驱动求解器式探索 |
| 10 | [Controlling Sharpening in LLM Post-Training](Controlling-Sharpening-in-LLM-Post-Training/README.md) | 按题目难度调节学习压力，让普通 RL 获得 pass@k 的抗锐化效果 |
| 11 | [D&A: Decoupling Description and Assessment Enables VLMs as Zero-Shot Robotic Reward Models](DA-Decoupling-Description-and-Assessment-Enables-VLMs-as-Zero-Shot-Robotic-Reward-Models/README.md) | 先描述再打分，纯提示让 VLM 成为无偏的零样本机器人奖励模型 |
| 12 | [DeepWaveRL: Self-Supervised Full Waveform Inversion via Reinforcement Learning](DeepWaveRL-Self-Supervised-Full-Waveform-Inversion-via-Reinforcement-Learning/README.md) | 仅靠一个标量奖励、不求物理梯度，用 GRPO 做自监督地震波形反演 |
| 13 | [Do Visual RL Gains Scale at Test Time? A Quantile View of Post-Training](Do-Visual-RL-Gains-Scale-at-Test-Time-A-Quantile-View-of-Post-Training/README.md) | 视觉RL提升单样本质量，却可能削弱Best-of-N扩展能力 |
| 14 | [FADE: Factored Ability--Difficulty Filtering for Online RLVR Scheduling](FADE-Factored-Ability-Difficulty-Filtering-for-Online-RLVR-Scheduling/README.md) | 拆开技能漂移与题目难度，精准挑出有梯度的RLVR题 |
| 15 | [Forecasting How RLHF Responds to Reward-Model Edits Before Training](Forecasting-How-RLHF-Responds-to-Reward-Model-Edits-Before-Training/README.md) | 不跑 RL，用协方差提前预测奖励模型改动的效果 |
| 16 | [From PID to Reinforcement Learning in Building HVAC Control: A Control-Architecture Review of Tuning Strategies, Formulations, and Deployment Trade-offs](From-PID-to-Reinforcement-Learning-in-Building-HVAC-Control-A-Control-Architecture-Review-of-Tuning/README.md) | RL 不是 PID 的继任者，而是 HVAC 控制栈里可选的挂载点 |
| 17 | [Hindsight Credit Assignment over Trees for Agentic RL](Hindsight-Credit-Assignment-over-Trees-for-Agentic-RL/README.md) | 把稀缺的成功经验在线注入树状 rollout，三组优势做细粒度信用分配 |
| 18 | [Improved regret bounds in tabular RL under local differential privacy](Improved-regret-bounds-in-tabular-RL-under-local-differential-privacy/README.md) | 收紧本地差分隐私下表格型强化学习的遗憾上下界 |
| 19 | [Inferring Transferable Rewards via Active Inverse Reinforcement Learning](Inferring-Transferable-Rewards-via-Active-Inverse-Reinforcement-Learning/README.md) | 主动挑选环境动力学请专家示范，少量数据学到可迁移奖励 |
| 20 | [MIRA: Reinforcing Multimodal Reasoning via Deceptive Contextual Augmentation](MIRA-Reinforcing-Multimodal-Reasoning-via-Deceptive-Contextual-Augmentation/README.md) | 给 VLM 喂错误的看图描述，用 RL 练出视觉纠错能力 |
| 21 | [Meet Students Where They Are: Student-Prefix Teacher Adaptation for On-Policy Distillation](Meet-Students-Where-They-Are-Student-Prefix-Teacher-Adaptation-for-On-Policy-Distillation/README.md) | 蒸馏前先用 RLVR 让教师学会接住学生的半截推理 |
| 22 | [Not All Reasoning Generalizes: A Case Study on Learning Generalizable Reasoning Strategies in RLVR](Not-All-Reasoning-Generalizes-A-Case-Study-on-Learning-Generalizable-Reasoning-Strategies-in-RLVR/README.md) | RLVR 学会的推导策略遇到 OOD 会退化成暴力枚举 |
| 23 | [Offline Approximate Value Iteration: A Reinforcement Learning Approach for Satellite Constellation Deployment](Offline-Approximate-Value-Iteration-A-Reinforcement-Learning-Approach-for-Satellite-Constellation-De/README.md) | 用离线近似值迭代在故障不确定下规划卫星星座部署 |
| 24 | [OmniOPD: Stable On-Policy Distillation for Joint Audio-Video Generation](OmniOPD-Stable-On-Policy-Distillation-for-Joint-Audio-Video-Generation/README.md) | 借更干净的视频上下文稳住音频蒸馏，把音、视频 RL 专家合进一个模型 |
| 25 | [On Stochastic Continuous-Time Linear System Identification for Adaptive Stabilization](On-Stochastic-Continuous-Time-Linear-System-Identification-for-Adaptive-Stabilization/README.md) | 从数据学会镇定未知不稳定系统：总观测时长决定成败 |
| 26 | [RLVR Sharpens the Pencil, Not the Mind](RLVR-Sharpens-the-Pencil%2C-Not-the-Mind/README.md) | RLVR只让模型优先用好解法，不改变其内部推理表征 |
| 27 | [RLiD: Reinforcement Learning in the Decision Plane for Language Agents and LLMs](RLiD-Reinforcement-Learning-in-the-Decision-Plane-for-Language-Agents-and-LLMs/README.md) | 把RL从逐token生成搬到动作菜单上，一次前向直接选动作 |
| 28 | [Reap: Uncovering Monte Carlo proof search with a lightweight model](Reap-Uncovering-Monte-Carlo-proof-search-with-a-lightweight-model/README.md) | Lean 原生 MCTS 加 1.7B 模型，开源可观测的定理证明搜索 |
| 29 | [SGR-OPSD: Learning from Subgoal Plans with Graph-Regularized Credit Assignment for Agentic Reinforcement Learning](SGR-OPSD-Learning-from-Subgoal-Plans-with-Graph-Regularized-Credit-Assignment-for-Agentic-Reinforcem/README.md) | 子目标计划引导教师打分，进度图用真实回报校准轮次信用 |
| 30 | [SQLoom: Set-Contrastive Learning of Syntactic, Semantic, and Logical Dependencies for Text-to-SQL](SQLoom-Set-Contrastive-Learning-of-Syntactic%2C-Semantic%2C-and-Logical-Dependencies-for-Text-to-SQL/README.md) | 用集合对比监督教小模型写对 SQL 的语法、语义与逻辑 |
| 31 | [Spacetime Emergence in the Memory of a Learning Agent](Spacetime-Emergence-in-the-Memory-of-a-Learning-Agent/README.md) | 只靠量子互信息奖励，RL 智能体的记忆里自己长出了光锥结构 |
| 32 | [The Cost of Mismatch: Noise Amplification in Zeroth-Order Reinforcement Learning](The-Cost-of-Mismatch-Noise-Amplification-in-Zeroth-Order-Reinforcement-Learning/README.md) | 零阶优化做 RLVR 的瓶颈在数据不匹配，固定数据才能消噪 |
| 33 | [WebHarbor: Docking Real Websites for Evolving GUI Agent Environments](WebHarbor-Docking-Real-Websites-for-Evolving-GUI-Agent-Environments/README.md) | 把153个真实网站搬进Docker，给网页智能体做稳定评测与RL训练 |
| 34 | [What Drives the Zero-to-One Jump? Diagnosing and Steering Hard-Prompt Learning in RLVR](What-Drives-the-Zero-to-One-Jump-Diagnosing-and-Steering-Hard-Prompt-Learning-in-RLVR/README.md) | 用开头熵识别快做对的失败样本，让难题从零到一更快突破 |
| 35 | [Whitened Advantage Summation Policy Optimization: Correlation-Aware Aggregation for Multi-Reward Reinforcement Learning](Whitened-Advantage-Summation-Policy-Optimization-Correlation-Aware-Aggregation-for-Multi-Reward-Rein/README.md) | 先白化去相关再加权求和，让多奖励权重名副其实 |

*由 RL-Frontier daily agent 自动生成 · 数据源 arXiv API*
