# RL 前沿日报 · 2026-11-04（24 篇）

| # | 论文 | 一句话概括 |
|---|------|-----------|
| 1 | [Compositional Unalignment: Auditing Safety in Large Vision-Language Models](Compositional-Unalignment-Auditing-Safety-in-Large-Vision-Language-Models/README.md) | 用免训练反对齐审计多模态组合安全的真实鲁棒性 |
| 2 | [Cooperative Multi-Agent Reinforcement Learning via Epigraph-Form Guided Exploration](Cooperative-Multi-Agent-Reinforcement-Learning-via-Epigraph-Form-Guided-Exploration/README.md) | 用上镜图约束给多智能体探索设预算，探索不再拖垮团队任务 |
| 3 | [Diversity-Aware Experience Replay via Statistical Leverage Scores](Diversity-Aware-Experience-Replay-via-Statistical-Leverage-Scores/README.md) | 用统计杠杆分数挑出回放池中的稀有样本，无需标签与价值网络 |
| 4 | [EmoReward: Self-Evolving Reward Calibration for Emotional Video Generation RL](EmoReward-Self-Evolving-Reward-Calibration-for-Emotional-Video-Generation-RL/README.md) | 用上一轮训练的奖励轨迹自校准情感视频生成的多奖励权重 |
| 5 | [Finite-Time Convergence and Regret Guarantees for Neural Reinforcement Learning in POMDPs](Finite-Time-Convergence-and-Regret-Guarantees-for-Neural-Reinforcement-Learning-in-POMDPs/README.md) | 首个有限记忆POMDP下神经网络RL的亚线性遗憾保证 |
| 6 | [From Handcrafted to Generative: RLVR-Optimized Icon Generation for Alexa+](From-Handcrafted-to-Generative-RLVR-Optimized-Icon-Generation-for-Alexa%2B/README.md) | 用可验证奖励做 RL，让文生图模型画出合规线稿图标 |
| 7 | [GIST: Gibbs-Targeted Hierarchical Data Selection for Offline RLVR](GIST-Gibbs-Targeted-Hierarchical-Data-Selection-for-Offline-RLVR/README.md) | 离线RLVR只挑关键回答和关键token监督，省三分之二token还更准 |
| 8 | [Learning When to Think Aloud in Latent Reasoning](Learning-When-to-Think-Aloud-in-Latent-Reasoning/README.md) | 只把关键 token 说出口，其余推理留在隐空间 |
| 9 | [MAC-v2: Long-horizon model-based value expansion from pixels](MAC-v2-Long-horizon-model-based-value-expansion-from-pixels/README.md) | 免重建隐空间世界模型加动作分块，让像素离线RL能做百步级想象 |
| 10 | [Mass Producing Training Data with Surprising Side Effects](Mass-Producing-Training-Data-with-Surprising-Side-Effects/README.md) | 自动批量挖掘看似无害却暗中改变模型行为的训练数据 |
| 11 | [ModalSearcher: Weaving Visual Evidence into Autonomous Cross-Modal Deep Search](ModalSearcher-Weaving-Visual-Evidence-into-Autonomous-Cross-Modal-Deep-Search/README.md) | 让多模态搜索智能体自主决定何时搜文、何时搜图 |
| 12 | [PEARL: Prediction Error-Adaptive Regularized Learning for Selective Forgetting under Partial Preference Drift](PEARL-Prediction-Error-Adaptive-Regularized-Learning-for-Selective-Forgetting-under-Partial-Preferen/README.md) | 只遗忘预测出错的方向，让神经老虎机跟上局部偏好漂移 |
| 13 | [RAGAM-AI: A Hybrid Reinforcement Learning based Agentic approach powered by Generative AI for Edge Resource Management](RAGAM-AI-A-Hybrid-Reinforcement-Learning-based-Agentic-approach-powered-by-Generative-AI-for-Edge-Re/README.md) | 用 LLM 当奖励裁判，驱动多智能体 SAC 做边缘资源调度 |
| 14 | [Regulating Autonomous Mobility-on-Demand Operators with Fixed and Adaptive Penalties: A Multi-Agent Reinforcement Learning Approach](Regulating-Autonomous-Mobility-on-Demand-Operators-with-Fixed-and-Adaptive-Penalties-A-Multi-Agent-R/README.md) | 用多智能体强化学习让监管者动态罚款，约束逐利的自动驾驶出行平台 |
| 15 | [Reinforcement Learning Enables Scaling Generalist Robot Policy Improvement](Reinforcement-Learning-Enables-Scaling-Generalist-Robot-Policy-Improvement/README.md) | 多任务在线RL让机器人基座模型在未见任务上也变强 |
| 16 | [Resource-Efficient Reinforcement Learning Post-Training through Elastic Expert Parallelism](Resource-Efficient-Reinforcement-Learning-Post-Training-through-Elastic-Expert-Parallelism/README.md) | 弹性专家并行让MoE模型RL采样提前释放空闲GPU |
| 17 | [Rubric Curriculum RL: Exploiting the Generation-Verification Gap in Non-Verifiable Domains](Rubric-Curriculum-RL-Exploiting-the-Generation-Verification-Gap-in-Non-Verifiable-Domains/README.md) | 成对比较加评分标准课程，让模型自评自训持续变强 |
| 18 | [SPILLWAY: Separating Target Admission from Sanitization to Defend Tool-Using Agents against Prompt Injection](SPILLWAY-Separating-Target-Admission-from-Sanitization-to-Defend-Tool-Using-Agents-against-Prompt-In/README.md) | 用工具的类型化返回值确定性地拦截注入，让 Agent 的动作发不到攻击者那里 |
| 19 | [Teaching Agents the 'Principle', Not the 'Reward'](Teaching-Agents-the-Principle%2C-Not-the-Reward/README.md) | 不给奖励，直接教行为原则，样本更少、泛化更强 |
| 20 | [Traffic-VL: Reinforced Vision-Language Models for Generalizable End-to-End Traffic Signal Control](Traffic-VL-Reinforced-Vision-Language-Models-for-Generalizable-End-to-End-Traffic-Signal-Control/README.md) | 8B 视觉语言模型直接看路口监控画面做信号灯决策 |
| 21 | [Using Experience Twice: Dynamic Process Rubrics for Privileged Token-Level Credit Assignment](Using-Experience-Twice-Dynamic-Process-Rubrics-for-Privileged-Token-Level-Credit-Assignment/README.md) | 自生成过程评分标准作特权信息，实现token级信用分配 |
| 22 | [Vision Paper: Why Distributed LLM Post-Training and Decentralized Alignment Are Now Essential](Vision-Paper-Why-Distributed-LLM-Post-Training-and-Decentralized-Alignment-Are-Now-Essential/README.md) | 偏好数据无法集中，LLM 对齐应转向联邦与去中心化训练 |
| 23 | [What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?](What-Does-Multi-Turn-Reinforcement-Learning-Really-Improve-in-LLM-Agents/README.md) | 多轮 Agent RL 强在纠错续航，交互轮数一紧收益就缩水 |
| 24 | [Where It Breaks: Diagnosing Perception, Memory, and Decision Failures of a Vision-Language Agent in Pac-Man](Where-It-Breaks-Diagnosing-Perception%2C-Memory%2C-and-Decision-Failures-of-a-Vision-Language-Agent-in-P/README.md) | 拆开感知与决策，诊断VLM智能体玩吃豆人时到底哪里出了问题 |

*由 RL-Frontier daily agent 自动生成 · 数据源 arXiv API*
