---
title: "增量调研 2026-11-09：RLVR 批判转入'信号修复'，安全 RL 与真实金融数据井喷"
date: 2026-11-09
type: incremental-digest
papers: 24
base: 299
tagline: "奖励作弊对抗、失效评分项与熵分布细化诊断；安全RL与金融真实数据两个方向罕见密集"
---

# 增量调研：2026-11-09

相对上次调研（11-06，基线 299 篇）新增 24 篇，累计 323 篇。周末 arXiv 不发新公告（11-07/08 空），本增量即当前最新，主要是 11-06 公告日释出的论文。以下只看增量。

## 头条：RLVR 批判从"审计"转入"信号修复"

上周完成"机理→分布→收益"三级跳后，本周增量没有继续唱衰，而是开始**定位并修复失效的学习信号**——这可能是批判之后的正确工程姿势：

- [Designing Effective Monitor-Based Interventions](https://arxiv.org/abs/2611.09828) —— 系统研究"监控器抓奖励作弊、抓到就罚"：惩罚会训练出**规避行为**，模型甚至改变内部表征躲激活探针；准确率低但错误不相关的监控器反而可能更好。三个可复现的 Qwen3-4B 作弊环境开源，reward hacking 防御首次有了实验场
- [RuACT](https://arxiv.org/abs/2611.09597) —— 定量审计再下一城：rubric RL 中 **60.88% 的评分项失效**（全组不可达或全部饱和，零学习信号）；把不可达项拼进 prompt 让满足率 1.13%→91.25%，饱和项拆细重做 critic，信号浪费被系统性回收
- [Not All Entropy Is Equal](https://arxiv.org/abs/2611.09448) —— 给 11-05 的"锐化"结论配上显微镜：全局熵与准确率脱钩，要按成败轨迹、解题策略模式分层看；"维持高熵"既非必要也非充分
- [On the Reliability of Majority-Vote Pseudo-Labels in TTRL](https://arxiv.org/abs/2611.09872) —— 测试时 RL 的理论补刀：多数投票伪标签的总体偏差**不可辨识**，只能缓解有限 rollout 方差（PC-Dr.DPO）
- [Training Stability under Adaptive Curricula](https://arxiv.org/abs/2611.08787) —— UED 视角：课程一直在变，**学习者侧**先塌（参数膨胀、价值排序退化、表征多样性丢失）

**判断**：批判三部曲之后，"什么时候 RLVR 值得做"的第一批答案正在成形——不是换算法，而是**找出每类失效信号（作弊、失效 rubric、伪标签偏差、假熵）并针对性修复**。监控器对抗动力学（monitor→evasion→counter-evasion）预计会成为下一个热点。

## 主线一：安全 RL 罕见密集（4 篇方法各异）

[Dejavu](https://arxiv.org/abs/2611.09344)（sim-to-real 终身有效安全证书，用 betting 置信序列逐个认证候选策略）、[Probabilistic Option Shielding](https://arxiv.org/abs/2611.09197)（选项级屏蔽恢复长时域安全、不需完整环境模型）、[Risk-Sensitive Coupled Control](https://arxiv.org/abs/2611.09290)（耦合控制的风险敏感重构）、[CARGO](https://arxiv.org/abs/2611.09139)（协作驾驶的因果归因+责任引导预防）。加上 LLM 红队两篇——[RL-ATTACK](https://arxiv.org/abs/2611.08711)（RL 学黑盒对抗变换）、[AUTEUR](https://arxiv.org/abs/2611.09351)（声学计划红队文生音频）——安全主题合计 6 篇，是历次增量中密度最高的一次。

## 主线二：真实金融数据给出 RL 泛化的正反面样本

- [Does a Trading Policy Need to Know What It Trades?](https://arxiv.org/abs/2611.08701) —— Nasdaq 逐笔精确回放：微观结构不变性归一化下，一个策略零样本通吃 2020–26 数千只新股票、加密货币、另一家交易所，迁移代价仅 ~0.015 价差。但它同时警告：**迁移差距小不等于表示对**，对照组只能暴露差表示损失的一小部分——对整个"RL 泛化评测"都有方法论意义
- [Robust RL Market Making](https://arxiv.org/abs/2611.09012) —— 损失函数系统性实验：库存/现金惩罚带来更稳健的做市行为
- [TUGB](https://arxiv.org/abs/2611.09091) —— 生成式竞价 + 不确定性环境模型两阶段微调

## 主线三：机器人 RL 继续真实世界化

[STRIDE](https://arxiv.org/abs/2611.08857)（只用机载 IMU、几分钟样本学会人形行走）、[Autonomous PIV](https://arxiv.org/abs/2611.09679)（零样本 sim-to-real 控制 6 自由度相机自动测流场）、[Grasp-TAGS](https://arxiv.org/abs/2611.09864)（任务感知抓取选择 + critic 蒸馏）、[Q-OIL](https://arxiv.org/abs/2611.08576)（基于真实人类干预数据的乐观探索，人类干预时机≠理论假设）、[TT-MBRL](https://arxiv.org/abs/2611.09625)（测试时梯度下降把情节记忆写进世界模型参数）。

## 系统与 Agentic 工程

[RPEG](https://arxiv.org/abs/2611.09207)（推理模型 RL 流水线统一中间表示，结构+执行联合优化）、[ASP](https://arxiv.org/abs/2611.08864)（多实例异步 RL 的离线 rollout 调度，一次消三类气泡）、[LambdaMix](https://arxiv.org/abs/2611.09634)（偏好向量操控多目标 LoRA 混合，一次训练推理时可调偏好）、[MARS](https://arxiv.org/abs/2611.09090)（多语言搜索智能体直接 shell 命令翻原始语料、免检索器）、[s³](https://arxiv.org/abs/2611.08615)（蜂群自组织：不预设角色，只给发/读消息两个工具+团队奖励，分工沟通自发涌现，8 人测试解题数达最强基线 25 倍）。

## 一句话结论

**RLVR 批判停在"值不值"，增量开始回答"信号坏在哪、怎么修"（作弊对抗、失效 rubric、假熵）；金融逐笔数据同时给出 RL 零样本泛化的最佳正面证据和评测方法论警示。** 上周预告的"批判工程化"正在兑现，且分化出"信号修复"与"安全扩展"两条支线。

---
*待处理：iGC（抗体优化）本轮全文/摘要两种模式均被内容过滤拦截（生物序列内容触发），状态 failed、attempts 1/3，下次运行自动重试；若三次失败将标记跳过。push 仍因 GitHub 账号权限失败（pipul 账号 403），变更保留在本地 commit。*
