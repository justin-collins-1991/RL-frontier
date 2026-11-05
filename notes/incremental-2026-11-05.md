---
title: "增量调研 2026-11-05：低精度 RL 集群浮现，RLVR 批判转向数据选择"
date: 2026-11-05
type: incremental-digest
papers: 56
base: 257
tagline: "FP4/FP8 后训练与端侧 RL 组成新集群；RLVR 机理批判深化为偏差诊断与题目选择"
---

# 增量调研：2026-11-05

相对上次调研（11-04，基线 201 篇）新增 56 篇，累计 257 篇。以下只看增量。

## 新集群：低精度与系统层 RL 后训练（上周零星，本周成势）

这是增量里最明显的**新方向**，四篇独立工作指向同一问题——RL 后训练太贵，往低精度和端侧压：

- [Aligning Training and Rollout Policies for End-to-End FP4 RL on MoE LLMs](https://arxiv.org/abs/2611.04376) —— MoE 上 FP4 RL 的核心是训练/推理两侧**对称纠偏**
- [FourSight: Stable FP4 RL Post-Training](https://arxiv.org/abs/2611.04887) —— 坏轨迹过滤 + 稀疏通道补偿，保 FP4 训练稳定
- [EpiLoRA](https://arxiv.org/abs/2611.03899) —— 多 LoRA 融入 FP8 GEMM，服务与 RL 共用一套底座
- [Training Specialist LLMs on Your Phone](https://arxiv.org/abs/2611.04797) —— 纯前向 + 可验证奖励，手机过夜训出 MB 级专用模型

与上周《RLVR 周报》里"训练-推理数值失配"主题衔接：当时是诊断，本周已经走到**工程方案**。判断：低精度 RL（FP4/FP8 训练链路）会是下阶段 infra 竞争点。

## 延续主题一：RLVR 机理批判 → 数据/偏差工程化

上周深读的"锐化而非增能"主题继续深化，但重点从"诊断"转向"怎么挑训练数据"：

- [On the Primacy Bias in RLVR Training](https://arxiv.org/abs/2611.04061) —— 用**首因偏差**解释 RLVR 为何偏爱易题：模型记住早期见过的解法风格。补上了我们上周"开放问题"里能力边界的一块拼图
- [ReSI-Math](https://arxiv.org/abs/2611.04787) —— 搜索"做错但可救回"的题目做 RLVR，直接呼应 pass@k 上尾保护
- [Density-Aware Reward Scaling](https://arxiv.org/abs/2611.04792) —— 按组内局部密度缩放奖励，解决 GRPO 收敛到单一模式（= 锐化的另一面）
- [On the Generalization Limitation of On-Policy Distillation](https://arxiv.org/abs/2611.05609) —— 蒸馏版泛化失败：分布内近乎完美，OOD 掉分，与上周 Not All Reasoning 呼应

## 延续主题二：Agentic RL 基建与经验内化

- [JHiMA-WebRL](https://arxiv.org/abs/2611.05263) —— 规划器/执行器分层 GRPO 联合训练，2×7B 胜 32B 单体
- [Harness-S](https://arxiv.org/abs/2611.04277) / [MDSKILL](https://arxiv.org/abs/2611.05313) —— 都是"把救援/技能经验内化进策略参数"
- [ModelBlaster](https://arxiv.org/abs/2611.04104) —— 经验库驱动的跨硬件算子优化智能体

## 具身/机器人小高峰

CRONOS（少重置 RL 微调基准）、PolicyIK（纯 RL 逆运动学毫米级）、OdorSpaces（视觉-嗅觉导航）、CANDO（双残差微调冻结生成式策略）——具身方向论文密度明显高于上周。

## 值得单独跟踪

1. **Policy Network Diffusion**（2611.04614）—— 扩散模型直接生成 RL 策略网络参数，思路罕见
2. **Suppressing Misaligned Behaviors, Durably**（2611.05358）—— 从"半途走偏的状态"起训，坏行为压制不复发；与上周 ShallowDefend 同属安全 RL，但切入角度不同
3. **Near-Minimax Multi-Objective RL**（2611.05562）—— 一份数据服务所有偏好，代价只随目标数对数增长，理论侧少见的好结果

## 一句话结论

增量画像：**RLVR 批判进入"工程化对策"阶段（数据选择、偏差校正），低精度/端侧 RL 后训练集群成型**；上周的判断"训练-推理失配将成为主线"正在被验证。

---
*注：本篇撰写时 GitHub 账户已被平台封禁（suspended），全部内容暂存于本地 git（含未推送 commit）；远端最后成功推送为 digest(2026-11-05) +49。*
