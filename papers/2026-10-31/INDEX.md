# RL 前沿日报 · 2026-10-31（16 篇）

| # | 论文 | 一句话概括 |
|---|------|-----------|
| 1 | [Alignment Flywheel-Guided Suppression Patching for Interactionless Inverse Reinforcement Learning](Alignment-Flywheel-Guided-Suppression-Patching-for-Interactionless-Inverse-Reinforcement-Learning/README.md) | 不重训奖励模型，用局部抑制补丁修正学到的奖励 |
| 2 | [Behavioral Steering of Vision-Language-Action Models in the Low-Parameter Regime](Behavioral-Steering-of-Vision-Language-Action-Models-in-the-Low-Parameter-Regime/README.md) | 仅训练几百个参数，就能用 RL 改变 7B VLA 的动作风格 |
| 3 | [CheXPoT: Post-Hoc Visual Verification and Correction of VLM-Generated Radiology Reports](CheXPoT-Post-Hoc-Visual-Verification-and-Correction-of-VLM-Generated-Radiology-Reports/README.md) | 不重训生成模型，用视觉证据事后核查并删改放射报告幻觉 |
| 4 | [Dataset Mismatch Matters in Group Relative Policy Optimization for Reinforcement Learning from Verifiable Rewards](Dataset-Mismatch-Matters-in-Group-Relative-Policy-Optimization-for-Reinforcement-Learning-from-Verif/README.md) | 借目标域聚合反馈重加权GRPO采样，提效又提泛化 |
| 5 | [Enhancing Language Model Reasoning with Structured Multi-Level Modeling](Enhancing-Language-Model-Reasoning-with-Structured-Multi-Level-Modeling/README.md) | 把长思维链拆成规划与执行两层，用过程级偏好训练小模型推理 |
| 6 | [Entropy-Regularized Reinforcement Learning for the Regime-Switching Consumption-Investment Problem](Entropy-Regularized-Reinforcement-Learning-for-the-Regime-Switching-Consumption-Investment-Problem/README.md) | 用熵正则连续时间强化学习求解牛熊切换下的消费与投资决策 |
| 7 | [HALO: Hierarchical Evidence Selection and Reinforcement Learning for Allocating Budgeted Label Optimization from Longitudinal Clinical Records](HALO-Hierarchical-Evidence-Selection-and-Reinforcement-Learning-for-Allocating-Budgeted-Label-Optimi/README.md) | 用 RL 联合决定病历该读哪些、哪些病人值得花钱请专家标注 |
| 8 | [Learning Timeline-Preserving Speech-to-Speech Translation](Learning-Timeline-Preserving-Speech-to-Speech-Translation/README.md) | 让语音翻译在原声时间轴上说话，停顿和结束点都对齐 |
| 9 | [Pulse: Long-Horizon Tasks Need Streaming Personalization](Pulse-Long-Horizon-Tasks-Need-Streaming-Personalization/README.md) | 旁路记忆智能体全程盯梢，用 RL 学会何时提醒用户偏好 |
| 10 | [Reading Between the Chapters: A Graph-Free RAG Rebuilt With AI and Human Feedback](Reading-Between-the-Chapters-A-Graph-Free-RAG-Rebuilt-With-AI-and-Human-Feedback/README.md) | 用AI与人类反馈迭代架构而非权重，无图RAG跨章节召回翻倍 |
| 11 | [Steer, Don't Tell: Breaking Reasoning Plateaus with Reachability-Aligned Self-Distillation](Steer%2C-Dont-Tell-Breaking-Reasoning-Plateaus-with-Reachability-Aligned-Self-Distillation/README.md) | 让看过答案的自教师只在学生够得着的动作里指方向 |
| 12 | [Structural Dual Adaptation for Safe Reinforcement Learning](Structural-Dual-Adaptation-for-Safe-Reinforcement-Learning/README.md) | 把拉格朗日乘子的开关式跳变改成平滑反馈，安全RL更稳 |
| 13 | [UI-UG 2: Advancing Mobile UI Understanding and Generation with Fine-Grained Supervision and Reinforcement Learning](UI-UG-2-Advancing-Mobile-UI-Understanding-and-Generation-with-Fine-Grained-Supervision-and-Reinforce/README.md) | 4B 模型用渲染感知在线 GRPO 统一移动端 UI 理解与生成 |
| 14 | [When Does Exploration Prevent Collapse? Three Regimes and the Path of the Reward in Self-Consistency Training](When-Does-Exploration-Prevent-Collapse-Three-Regimes-and-the-Path-of-the-Reward-in-Self-Consistency/README.md) | 探索系数有两条临界线，奖励路径决定防坍缩所需强度 |
| 15 | [World Models Need Not Be Right to Rank Policies Right: Relative Bounds and Audit Limits](World-Models-Need-Not-Be-Right-to-Rank-Policies-Right-Relative-Bounds-and-Audit-Limits/README.md) | 世界模型估值不准也能排对策略，但省不了多少真实审计 |
| 16 | [Zeroth-Order Policy Optimization for Scheduling in Queueing Networks](Zeroth-Order-Policy-Optimization-for-Scheduling-in-Queueing-Networks/README.md) | 只看平均成本的零阶策略优化，带收敛保证地学排队调度 |

*由 RL-Frontier daily agent 自动生成 · 数据源 arXiv API*
