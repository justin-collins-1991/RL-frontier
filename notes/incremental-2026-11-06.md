---
title: "增量调研 2026-11-06：RLVR 边际收益遭遇定量审计，Agentic RL 转向真实任务"
date: 2026-11-06
type: incremental-digest
papers: 42
base: 299
tagline: "SFT 之后再 RLVR 只值半点？边际收益审计成为批判新阶段；Agent RL 全面转向真实任务与工程化"
---

# 增量调研：2026-11-06

相对上次调研（11-05，基线 257 篇）新增 42 篇，累计 299 篇。以下只看增量。

## 头条：RLVR 批判进入"定量审计"阶段

上周集群给出的结论是"锐化而非增能"（见 `incremental-2026-11-05.md`），本周增量里出现了更尖锐的一击——从"学了什么"升级为"**值不值**"：

- [Measuring the Marginal Value of Verifier-Based RL Beyond SFT](https://arxiv.org/abs/2611.07639) —— 系统测量：SFT 之后再做 RLVR，边际收益**不到半个点**。这是对"RLVR 万能论"最直接的一次定量打击
- [Unpacking the Compute Efficiency of Strong-to-Weak OPD against GRPO](https://arxiv.org/abs/2611.08453) —— 按 FLOPs 算账：外部教师蒸馏在同等算力下不如 GRPO；省算力的正确姿势是先分域 RL 再多教师蒸馏
- [Mass Producing Training Data with Surprising Side Effects](https://arxiv.org/abs/2611.06324) —— 批量合成的训练数据会暗中改变模型行为（隐性副作用），数据规模化的风险被量化
- [Spectral and Subspace Dynamics of LoRA in SFT and RL](https://arxiv.org/abs/2611.08414) —— 谱分析显示 RL 的 LoRA 更新更集中、子空间迁移更快，为"RL 是重新分配"提供了参数空间的直接证据

**判断**：批判三部曲完整了——表征层没变（11-04）→ 概率质量重排（11-05）→ 边际收益定量审计（本周）。这个系列的下一问自然是："什么时候 RLVR 才真正值得做？"（本周已有部分答案：GIST、Rubric Curriculum 等从数据选择侧回答。）

## 主线一：Agentic RL 从基准转向真实任务

- [Agent-R²](https://arxiv.org/abs/2611.08219) —— 真实来源合成办公任务数据，4B 智能体超越 235B（生产力场景而非玩具基准）
- [What Does Multi-Turn RL Really Improve in LLM Agents?](https://arxiv.org/abs/2611.06483) —— 机理审视版：多轮 RL 的真实收益在**纠错续航**，交互轮数一收紧收益就缩水
- 信用分配继续内化：[AttnSR](https://arxiv.org/abs/2611.07932)（用策略自身注意力回溯分配步级奖励，免奖励模型）、[Using Experience Twice](https://arxiv.org/abs/2611.06543)（自生成过程评分标准做 token 级信用分配）
- 安全侧：[SPILLWAY](https://arxiv.org/abs/2611.07222) 用工具返回值类型化拦截提示注入，确定性防御
- [Traffic-VL](https://arxiv.org/abs/2611.06353) —— 8B VLM 直接看真实路口监控做信号灯控制，端到端落地样本

## 主线二：机器人 RL 的"泛化"叙事补强

- [RL Enables Scaling Generalist Robot Policy Improvement](https://arxiv.org/abs/2611.06905) —— 多任务在线 RL 让机器人基座在**未见任务**上变强，正面回应"RL 只是重排"的质疑（机器人模态给出了不一样的答案）
- [MAC-v2](https://arxiv.org/abs/2611.07245) —— 免重建世界模型 + 动作分块，像素离线 RL 做百步级想象
- [RM-VLM](https://arxiv.org/abs/2611.08308) —— 自然语言任务描述自动生成视觉接地的奖励机
- [Efficient Diffusion Policy Fine-Tuning](https://arxiv.org/abs/2611.07275) —— 只调初始噪声的扩散策略微调

## 主线三：安全 RL 三个独立成果

[Accelerating Safe RL with Massive Parallelism](https://arxiv.org/abs/2611.08273)（相位聚合代价估计上大规模并行）、[Monotone Viability Learning](https://arxiv.org/abs/2611.07616)（离线学长时域可行集）、[Provable Zeroth-Order Safe RLHF](https://arxiv.org/abs/2611.07561)（免奖励模型且全程可证明安全）——方法各异，都奔着"安全约束下的可扩展性"。

## 训练效率与数据选择

- [Resource-Efficient RL Post-Training](https://arxiv.org/abs/2611.06984) —— 弹性专家并行，MoE 采样时提前释放空闲 GPU（低精度集群的系统层延续）
- [GIST](https://arxiv.org/abs/2611.06395) —— 离线 RLVR 只挑关键回答/关键 token 监督，省 2/3 token 还更准（对上面"边际收益"问题的直接工程回答）
- [Rubric Curriculum RL](https://arxiv.org/abs/2611.06244) —— 用生成-验证差距在**不可验证域**做课程，绕开 RLVR 需要验证器的限制
- [Learning When to Think Aloud](https://arxiv.org/abs/2611.06108) —— 隐式推理中学习性地只把关键 token"说出口"，效率与可读性兼得

## 工业落地样本变多

[Alexa+ 图标生成](https://arxiv.org/abs/2611.06123)（RLVR 用于产品线稿图标，Amazon）、[EmoReward](https://arxiv.org/abs/2611.06518)（情感视频生成多奖励自校准）、[风场控制可解释蒸馏](https://arxiv.org/abs/2611.08245)——RLVR 从"刷数学题"走向真实产品约束，是这个增量的隐性趋势。

## 理论与奇作

- [Finite-Time Convergence for Neural RL in POMDPs](https://arxiv.org/abs/2611.07069) —— 首个有限记忆 POMDP 下神经 RL 的亚线性遗憾保证
- [Discovering Learning Rules that Shape Others](https://arxiv.org/abs/2611.08335) —— 元学习出能塑造对手行为的更新规则
- [Octopus](https://arxiv.org/abs/2611.06956) —— Latent-KV 多智能体共享一个大脑的 RL
- [Drex](https://arxiv.org/abs/2611.07854) —— 不做自回归生成、直接输出选项概率的开源决策基座

## 一句话结论

**RLVR 的批判完成"机理→分布→收益"三级跳，数据选择（GIST/Rubric Curriculum）成为正面回应；Agentic RL 和机器人 RL 用"真实任务 + 未见任务泛化"给出了另一侧的答案。** 上周判断"批判将工程化"已验证，且比预期来得更猛烈。

---
*待处理：iGC（抗体优化）因内容过滤两次失败（attempts 2/3），下次运行自动重试；此为已知问题（生物序列内容触发过滤），若三次失败将标记跳过。*
