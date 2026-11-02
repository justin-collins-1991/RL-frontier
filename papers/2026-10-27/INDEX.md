# RL 前沿日报 · 2026-10-27（36 篇）

| # | 论文 | 一句话概括 |
|---|------|-----------|
| 1 | [Action-Value Calibration via Continuation Sharing for Long-Horizon Agentic Reinforcement Learning](Action-Value-Calibration-via-Continuation-Sharing-for-Long-Horizon-Agentic-Reinforcement-Learning/README.md) | 复用同批次轨迹的后续经验校准动作价值，缓解长程智能体信用分配偏差 |
| 2 | [Autonomous fixed-wing interception using reinforcement learning](Autonomous-fixed-wing-interception-using-reinforcement-learning/README.md) | 单目视觉端到端RL策略，让固定翼拦截机实飞自主拦截目标 |
| 3 | [CONCUR: Concordant Auxiliary Rewards for Multi-Task, Multi-Reward Reinforcement Learning](CONCUR-Concordant-Auxiliary-Rewards-for-Multi-Task%2C-Multi-Reward-Reinforcement-Learning/README.md) | 修正辅助奖励的优势分数，让它不再推翻主奖励的排序 |
| 4 | [CoHARL: Co-Evolving Agent Policies and Executable Harnesses with Reinforcement Learning](CoHARL-Co-Evolving-Agent-Policies-and-Executable-Harnesses-with-Reinforcement-Learning/README.md) | 用RL让智能体策略与可执行Harness协同进化 |
| 5 | [Collective Dynamics of Self-Reinforcement: How Cross-Task Coupling Drives Policy Collapse in Unsupervised RLVR](Collective-Dynamics-of-Self-Reinforcement-How-Cross-Task-Coupling-Drives-Policy-Collapse-in-Unsuperv/README.md) | 无标签 RLVR 崩溃源于跨题共享参数的集体失稳 |
| 6 | [Echo: Scaling Visual Reinforcement Learning with Off-policy Experience](Echo-Scaling-Visual-Reinforcement-Learning-with-Off-policy-Experience/README.md) | 让状态策略模仿视觉策略，用免渲染经验低成本扩展视觉RL |
| 7 | [EnvSched: Environment-Aware Scheduling for Rollout-Efficient Agent Reinforcement Learning](EnvSched-Environment-Aware-Scheduling-for-Rollout-Efficient-Agent-Reinforcement-Learning/README.md) | 按环境调度训练任务，用三分之一步数追平随机选题的 Agent RL |
| 8 | [Frequency-Uniform Log-Regret Reinforcement Learning for Diffusions](Frequency-Uniform-Log-Regret-Reinforcement-Learning-for-Diffusions/README.md) | 时间步再细，扩散控制的值方法RL仍保持对数遗憾 |
| 9 | [From Solver Trajectories to Teaching Trajectories: Cognition-Aligned Reasoning Distillation](From-Solver-Trajectories-to-Teaching-Trajectories-Cognition-Aligned-Reasoning-Distillation/README.md) | 用RL把大模型解题轨迹改写成小模型学得会的教学轨迹 |
| 10 | [GARDEN: Generalist Autonomous Reward Design Through Evidence Navigation for Cooperative Multi-Agent Reinforcement Learning](GARDEN-Generalist-Autonomous-Reward-Design-Through-Evidence-Navigation-for-Cooperative-Multi-Agent-R/README.md) | 让 LLM 自主查证据设计一份奖励，跨多智能体场景直接复用 |
| 11 | [Guided-RLVR: Guided Exploration in Reinforcement Learning with Verifiable Rewards](Guided-RLVR-Guided-Exploration-in-Reinforcement-Learning-with-Verifiable-Rewards/README.md) | 在关键步骤注入引导词，让 RLVR 探索更多推理路径 |
| 12 | [Hyperparameter and Neural Architecture Search via Evolutionary Optimization for Reinforcement Learning: HPNAS-RL](Hyperparameter-and-Neural-Architecture-Search-via-Evolutionary-Optimization-for-Reinforcement-Learni/README.md) | 用进化算法同时搜网络结构和PPO超参，让自动驾驶RL更强更小 |
| 13 | [InfraDev: Can Coding Agents Develop AI Infrastructure, and How Can We Tell?](InfraDev-Can-Coding-Agents-Develop-AI-Infrastructure%2C-and-How-Can-We-Tell/README.md) | 用真实多卡 PR 加隐藏探针，检验编码智能体能否开发 AI 基础设施 |
| 14 | [Interpretable Meta-Policies for Neural Decision Making](Interpretable-Meta-Policies-for-Neural-Decision-Making/README.md) | 高层用符号规则选技能，底层用神经网络执行，兼顾可解释与性能 |
| 15 | [Learning from Relative Action Credit for Escaping Local Minima](Learning-from-Relative-Action-Credit-for-Escaping-Local-Minima/README.md) | 让 PPO 比较同状态下的动作优劣，走出奖励平台期 |
| 16 | [Learning to Look Beyond Screens: Transferable Visual Observation from GUI Grounding](Learning-to-Look-Beyond-Screens-Transferable-Visual-Observation-from-GUI-Grounding/README.md) | 用 GUI 定位数据训练会“裁剪细看”的视觉策略，并迁移到通用感知 |
| 17 | [Multi-Agent Reinforcement Learning for Global Climate Policy Cooperation](Multi-Agent-Reinforcement-Learning-for-Global-Climate-Policy-Cooperation/README.md) | 给 MARL 气候博弈加上谈判与违约惩罚，惩罚适中时合作最好 |
| 18 | [Multi-Agent Reinforcement Learning of Co-Adaptive Hip Exoskeleton Control (MARL-Exo) for Metabolic Energy Reduction](Multi-Agent-Reinforcement-Learning-of-Co-Adaptive-Hip-Exoskeleton-Control-MARL-Exo-for-Metabolic-Ene/README.md) | 人机在仿真中协同训练，免个人调参降低真人步行代谢 |
| 19 | [Noise Steering: Exploiting Wake Steering and Acoustic Directivity for Noise-Constrained Wind Farm Control via Reinforcement Learning](Noise-Steering-Exploiting-Wake-Steering-and-Acoustic-Directivity-for-Noise-Constrained-Wind-Farm-Con/README.md) | 用 RL 联合调偏航与功率，满足噪声限值且少损发电量 |
| 20 | [On the Sparsity of Direct Preference Optimization: Weight Disentanglement in the NTK Regime](On-the-Sparsity-of-Direct-Preference-Optimization-Weight-Disentanglement-in-the-NTK-Regime/README.md) | 从最大间隔视角解释 DPO 为何只改动少量参数且利于模型合并 |
| 21 | [PailitaoMMSearch2.0 Technical Report: Scaling Generative Retrieval to Unified End-to-End Multimodal Search](PailitaoMMSearch2.0-Technical-Report-Scaling-Generative-Retrieval-to-Unified-End-to-End-Multimodal-S/README.md) | 一个VLM直接从图文查询生成商品ID，统一拍立淘多意图搜索 |
| 22 | [RPSD: Retrieval-Privileged On-Policy Self-Distillation with Optimal Transport](RPSD-Retrieval-Privileged-On-Policy-Self-Distillation-with-Optimal-Transport/README.md) | 用相似用户行为当特权信息，让推荐 RL 获得 token 级信用分配 |
| 23 | [Repulsive Population Policy Gradients for Behaviorally Diverse Reinforcement Learning](Repulsive-Population-Policy-Gradients-for-Behaviorally-Diverse-Reinforcement-Learning/README.md) | 用带互斥奖励的 PPO 同时训练一小群又强又不同的策略 |
| 24 | [SetGRPO: Calibrating Grader-Induced Policy Optimization](SetGRPO-Calibrating-Grader-Induced-Policy-Optimization/README.md) | 把评分器噪声建模成优势集合，只执行方向可靠的GRPO更新 |
| 25 | [Strategyproof Deep Reinforcement Learning for Online Resource Allocation](Strategyproof-Deep-Reinforcement-Learning-for-Online-Resource-Allocation/README.md) | 单调神经网络加临界支付，首个严格防作弊的深度RL在线资源分配机制 |
| 26 | [TeamGym: A Gym for Team Decision-Making by AI Agents with Distributed Information](TeamGym-A-Gym-for-Team-Decision-Making-by-AI-Agents-with-Distributed-Information/README.md) | 量化并用RL弥补多智能体团队的信息沟通与检索短板 |
| 27 | [ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning](ThinkWorld-World-Imagination-Reinforces-Chain-of-Dynamics-Reasoning/README.md) | 用想象未来做奖励，让无动作标注的人类视频也能强化 VLA 动作推理 |
| 28 | [UCVE: Graph Structured Retrieval for Compliance Validation](UCVE-Graph-Structured-Retrieval-for-Compliance-Validation/README.md) | 用 RL 学合规要求图的边权，谱重排提升合规检索召回 |
| 29 | [Uncovering Shortcut Amplification in Video RLVR through the Lens of Perceptual Uncertainty Collapse](Uncovering-Shortcut-Amplification-in-Video-RLVR-through-the-Lens-of-Perceptual-Uncertainty-Collapse/README.md) | 视频RLVR会放大文本捷径，BSPO用双焦自蒸馏拉回视觉依据 |
| 30 | [VideoLVR: Latent Visual Reasoning over Grounded Video Evidence](VideoLVR-Latent-Visual-Reasoning-over-Grounded-Video-Evidence/README.md) | 推理时用隐式视觉 token 回看视频证据，并用 RL 联合优化 |
| 31 | [Vision-Language Agents Can Learn in Their Own Latent Worlds](Vision-Language-Agents-Can-Learn-in-Their-Own-Latent-Worlds/README.md) | 让 VLM 在自己的隐空间里想象未来，低成本做基于模型的强化学习 |
| 32 | [Watermark Basins: Black-Box Detection of Distilled LLMs](Watermark-Basins-Black-Box-Detection-of-Distilled-LLMs/README.md) | 在梯度空间里找水印盆地，只靠 API 就能抓出蒸馏模型 |
| 33 | [What a Weight Update Buys: Leverage Across Training Stages](What-a-Weight-Update-Buys-Leverage-Across-Training-Stages/README.md) | 用杠杆率衡量每单位权重改动换来多少行为变化 |
| 34 | [When, Where, and What to Correct: Human-Guided Adaptive Residual Correction for Robot Policies](When%2C-Where%2C-and-What-to-Correct-Human-Guided-Adaptive-Residual-Correction-for-Robot-Policies/README.md) | 用少量人类纠正圈定时机与方向，再靠 RL 学残差补精度 |
| 35 | [When All Rollouts Fail: Policy-Compatible Joint Decoding for Hard-Problem Reasoning](When-All-Rollouts-Fail-Policy-Compatible-Joint-Decoding-for-Hard-Problem-Reasoning/README.md) | 用专家引导的联合解码，让 RLVR 在全错难题上也能学 |
| 36 | [Zooming without Zooming v2: From Seeing Details to Connecting Evidence for Generalizable Multimodal Perception](Zooming-without-Zooming-v2-From-Seeing-Details-to-Connecting-Evidence-for-Generalizable-Multimodal-P/README.md) | 单图多区域合成题加RLVR，练出可泛化的证据串联能力 |

*由 RL-Frontier daily agent 自动生成 · 数据源 arXiv API*
