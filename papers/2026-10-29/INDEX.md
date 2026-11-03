# RL 前沿日报 · 2026-10-29（41 篇）

| # | 论文 | 一句话概括 |
|---|------|-----------|
| 1 | [Aligning Medical Vision Language Models at the Capability Boundary with Entropy Adaptive Rubric Grounding](Aligning-Medical-Vision-Language-Models-at-the-Capability-Boundary-with-Entropy-Adaptive-Rubric-Grou/README.md) | 在能力边界做偏好对齐，再用熵门控临床评分细则奖励推理过程 |
| 2 | [Appreciation Teaches Unauthorized Execution: Self-Evolution Degrades the Robustness of Personal Agents to Indirect Prompt Injection](Appreciation-Teaches-Unauthorized-Execution-Self-Evolution-Degrades-the-Robustness-of-Personal-Agent/README.md) | 用户的点赞会让自进化 Agent 更容易被间接提示注入劫持 |
| 3 | [Before We Adapt: The Zero-Shot Generalization Bottleneck in Continual World Models](Before-We-Adapt-The-Zero-Shot-Generalization-Bottleneck-in-Continual-World-Models/README.md) | 规则没变、地图变了，世界模型也可能复用失败，瓶颈在表征 |
| 4 | [Cheap Retrieval and Observation Credit Assignment from One Quantity: The Value of Information](Cheap-Retrieval-and-Observation-Credit-Assignment-from-One-Quantity-The-Value-of-Information/README.md) | 用信息价值统一解决记忆检索与观测信用分配 |
| 5 | [CoFiBreak: A Coarse-to-Fine Diversity Reward for Effective Multi-Turn Jailbreak](CoFiBreak-A-Coarse-to-Fine-Diversity-Reward-for-Effective-Multi-Turn-Jailbreak/README.md) | 用粗细两级多样性奖励防止红队攻击模型的 GRPO 训练坍缩 |
| 6 | [Communication-Efficient Private Federated Reinforcement Learning with Post-Quantum Authentication for Vehicular Networks](Communication-Efficient-Private-Federated-Reinforcement-Learning-with-Post-Quantum-Authentication-fo/README.md) | 车联网联邦强化学习：一比特相关隐私量化加抗量子签名 |
| 7 | [DYNAS: A Dynamic Network Penetration Testing Framework Using Deep Hierarchical Reinforcement Learning](DYNAS-A-Dynamic-Network-Penetration-Testing-Framework-Using-Deep-Hierarchical-Reinforcement-Learning/README.md) | 在带防御动态的仿真环境中用分层强化学习做自动化渗透测试 |
| 8 | [DeCoRL: Decomposed Consistency Reinforcement Learning for Multi-Image Composition](DeCoRL-Decomposed-Consistency-Reinforcement-Learning-for-Multi-Image-Composition/README.md) | 把多图合成一致性拆成逐物体打分，用 RL 修复身份错乱 |
| 9 | [Density-Guided Bootstrap Boundaries for Latent World-Model Reinforcement Learning](Density-Guided-Bootstrap-Boundaries-for-Latent-World-Model-Reinforcement-Learning/README.md) | 用密度信号逐条决定想象轨迹该在哪一步切回 critic |
| 10 | [EnvOS: Auditing Computer-Use Agents When the World Moves On : Phenomenon-Based Task Construction, Certification, and Evidence-Based Evaluation](EnvOS-Auditing-Computer-Use-Agents-When-the-World-Moves-On-Phenomenon-Based-Task-Construction%2C-Certi/README.md) | 先验证环境和评分器靠得住，再评测任务中途世界变化下的智能体 |
| 11 | [Escaping Path Mirages in Offline Goal-Conditioned Reinforcement Learning](Escaping-Path-Mirages-in-Offline-Goal-Conditioned-Reinforcement-Learning/README.md) | 把随机分叉点当图节点，绕开离线数据里的虚假成功路径 |
| 12 | [Event2Reward: Learning Robotic Rewards from Progress Relations](Event2Reward-Learning-Robotic-Rewards-from-Progress-Relations/README.md) | 用失败轨迹中的停滞、倒退事件教奖励模型识别真实进度 |
| 13 | [Grounding Multimodal Reasoning with Evidence-Ablated Negatives](Grounding-Multimodal-Reasoning-with-Evidence-Ablated-Negatives/README.md) | 遮挡关键视觉证据造难负样本，抑制多模态RL的语言先验捷径 |
| 14 | [H$^2$R: Hierarchical Hint-Based Reward for Mathematical Reasoning via Reinforcement Learning](H2R-Hierarchical-Hint-Based-Reward-for-Mathematical-Reasoning-via-Reinforcement-Learning/README.md) | 用子问题分层提示做中间监督，缩短数学RL推理链 |
| 15 | [Heterogeneous Co-Evolution Learning for Tool-Efficient Search Agents with Zero Labels](Heterogeneous-Co-Evolution-Learning-for-Tool-Efficient-Search-Agents-with-Zero-Labels/README.md) | 出题者与解题者协同进化，零标注训练少搜多对的搜索智能体 |
| 16 | [Improving the Intrinsic Interpretability of Differentiable Decision Trees through Euclidean Feature-Concentration Regularisation](Improving-the-Intrinsic-Interpretability-of-Differentiable-Decision-Trees-through-Euclidean-Feature/README.md) | 用欧氏集中度正则让可微决策树每个节点只看少数特征 |
| 17 | [Incentivizing Self-Learning in Large Language Models via Reinforcement Learning](Incentivizing-Self-Learning-in-Large-Language-Models-via-Reinforcement-Learning/README.md) | 用强化学习教大模型边翻教材边做证明的自学能力 |
| 18 | [LLM-guided Planar Loco-Manipulation for Quadruped Robots](LLM-guided-Planar-Loco-Manipulation-for-Quadruped-Robots/README.md) | 微调小模型规划技能、物体与目标，驱动四足推障导航 |
| 19 | [Learned Terminal Costs for Short-Horizon Model Predictive Control of Autonomous Trucks in Interactive Highway Traffic](Learned-Terminal-Costs-for-Short-Horizon-Model-Predictive-Control-of-Autonomous-Trucks-in-Interactiv/README.md) | 用DQN价值函数当终端代价，让短视MPC安全开卡车 |
| 20 | [Learning Calibrated Confidence for Multi-Agent Collaboration](Learning-Calibrated-Confidence-for-Multi-Agent-Collaboration/README.md) | 让多智能体交接时附带校准置信度，下游据此决定信任或复核 |
| 21 | [Li$^{2}$SAO: Lifting Light Singl-Rollout Asynchronous RL Optimization via Group-Relative Actor-Critic Bootstrapping](Li2SAO-Lifting-Light-Singl-Rollout-Asynchronous-RL-Optimization-via-Group-Relative-Actor-Critic-Boot/README.md) | 先用组内对比热启动 critic，再切单 rollout GAE 做异步 RL |
| 22 | [On the Origin and Evolution of Training-Inference Mismatch in LLM Reinforcement Learning](On-the-Origin-and-Evolution-of-Training-Inference-Mismatch-in-LLM-Reinforcement-Learning/README.md) | 把训推不一致拆成数值误差与策略滞后，分别对症修正 |
| 23 | [Online Dense Reinforcement Learning with Planning-Grounding Agent for UI Navigation on Live IOS Apps](Online-Dense-Reinforcement-Learning-with-Planning-Grounding-Agent-for-UI-Navigation-on-Live-IOS-Apps/README.md) | 在真实 iOS 设备上用稠密奖励在线 RL 训练小模型 UI 智能体 |
| 24 | [PIVOT: Progressive Intervention via Online Teacher Correction](PIVOT-Progressive-Intervention-via-Online-Teacher-Correction/README.md) | 教师在线纠错插入学生轨迹，并配合KL监督破解难题稀疏奖励 |
| 25 | [Reasoning or Pattern Exploitation? Mechanistic Insights from RL-Trained Language Models](Reasoning-or-Pattern-Exploitation-Mechanistic-Insights-from-RL-Trained-Language-Models/README.md) | 用井字棋拆解 GRPO：分数飙升，靠的是更会用提示信息而非真推理 |
| 26 | [Reinforcement Learning Under Runtime Confounding: Policy Learning and Off-Policy Evaluation](Reinforcement-Learning-Under-Runtime-Confounding-Policy-Learning-and-Off-Policy-Evaluation/README.md) | 训练时能看、部署时不能用的变量，如何做无偏的离线强化学习 |
| 27 | [Reinforcement learning for control of partial differential equations](Reinforcement-learning-for-control-of-partial-differential-equations/README.md) | 一篇把强化学习和 PDE 最优控制串起来讲的综述 |
| 28 | [Reward-Adaptive Co-Evolution of Policy and Rubric](Reward-Adaptive-Co-Evolution-of-Policy-and-Rubric/README.md) | 按奖励信息量决定何时练策略、何时改评分细则 |
| 29 | [SCARL: Sequence Confidence-Aligned Reinforcement Learning](SCARL-Sequence-Confidence-Aligned-Reinforcement-Learning/README.md) | 用序列置信度重塑优势，校准RLVR更新力度并缓解熵坍缩 |
| 30 | [Safe Multi-Objective Reinforcement Learning: Zero Constraint Violation and Primal-Averaging Convergence](Safe-Multi-Objective-Reinforcement-Learning-Zero-Constraint-Violation-and-Primal-Averaging-Convergen/README.md) | 多目标强化学习全程零违约，仍可高效逼近安全帕累托最优 |
| 31 | [Sandman: Building and Operating Sandboxes for Agentic Reinforcement Learning on Shared Kubernetes](Sandman-Building-and-Operating-Sandboxes-for-Agentic-Reinforcement-Learning-on-Shared-Kubernetes/README.md) | 在共享 K8s 上支撑百万级 Agentic RL 沙箱的工程实践 |
| 32 | [ShallowDefend: Harnessing Shallow Safety Alignment for Multi-Turn Defender](ShallowDefend-Harnessing-Shallow-Safety-Alignment-for-Multi-Turn-Defender/README.md) | 先显式表态再回答，用开头几个 token 的 RL 训练防住多轮越狱 |
| 33 | [Steering Vectors as a Training Signal in LLM Post-Training](Steering-Vectors-as-a-Training-Signal-in-LLM-Post-Training/README.md) | 把推理期的引导向量变成 SFT 与 GRPO 的训练信号 |
| 34 | [There Is No Free Lunch in RLVR: Every pass@1 Gain Has a pass@k Price](There-Is-No-Free-Lunch-in-RLVR-Every-pass1-Gain-Has-a-passk-Price/README.md) | RLVR提升pass@1必付pass@k代价 |
| 35 | [Timbre: Reliability-aware harmonic consensus for label-free multimodal test-time rexinforcement learning](Timbre-Reliability-aware-harmonic-consensus-for-label-free-multimodal-test-time-rexinforcement-learn/README.md) | 四视图加权调和共识，让多模态测试时RL伪标签更可靠 |
| 36 | [Training Foundation Models with a Single Algorithm](Training-Foundation-Models-with-a-Single-Algorithm/README.md) | 把预训练到 RL 统一成一个最大似然算法，只调数据配比 |
| 37 | [Training language models in simulation for psychiatric intake](Training-language-models-in-simulation-for-psychiatric-intake/README.md) | 在模拟病人环境中做多轮RL，让LLM学会精神科问诊 |
| 38 | [Uncertainty-aware Feedback Loop Diagnosis: integrating reinforcement learning and conformal prediction for reliable wafer defect classification](Uncertainty-aware-Feedback-Loop-Diagnosis-integrating-reinforcement-learning-and-conformal-predictio/README.md) | RL 挑区域扫描、共形预测定停止，晶圆检测省时四成 |
| 39 | [VeriCUA: Verification as Agentic Exploration for Computer-Using Agents](VeriCUA-Verification-as-Agentic-Exploration-for-Computer-Using-Agents/README.md) | 让验证器像智能体一样主动取证，判断电脑操作任务是否真完成 |
| 40 | [When Requirements Interact: Scaling Long-Horizon Coding via Interdependent Specifications](When-Requirements-Interact-Scaling-Long-Horizon-Coding-via-Interdependent-Specifications/README.md) | 用相互耦合的需求合成编码任务，训练并评测长程编码智能体 |
| 41 | [bf16 Rounding Silently Discards Most RL Policy Updates: A Hidden Training-Inference Mismatch and an Unbiased One-Line Fix](bf16-Rounding-Silently-Discards-Most-RL-Policy-Updates-A-Hidden-Training-Inference-Mismatch-and-an-U/README.md) | bf16 就近舍入吞掉多数 RL 更新，一行无偏舍入即可修复 |

*由 RL-Frontier daily agent 自动生成 · 数据源 arXiv API*
