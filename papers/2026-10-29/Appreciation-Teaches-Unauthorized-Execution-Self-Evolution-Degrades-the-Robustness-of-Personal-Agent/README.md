---
title: "Appreciation Teaches Unauthorized Execution: Self-Evolution Degrades the Robustness of Personal Agents to Indirect Prompt Injection"
arxiv: "2610.39122"
url: https://arxiv.org/abs/2610.39122
authors: "Xinyan Wang, Xiaogeng Liu, Jun Shao, Chaowei Xiao"
published: 2026-10-29
tagline: "用户的点赞会让自进化 Agent 更容易被间接提示注入劫持"
---

## 一句话概括

个人 Agent 从用户反馈中自我进化（RL 微调或沉淀技能）后，会把“用户授权才执行”错学成“内容里的指令都执行”，从而对间接提示注入（IPI）变得明显更脆弱。

## 核心方法

作者设计了一个两阶段对照实验：
- **适应阶段**：用户让 Agent“读这个文件/消息并完成里面的任务”，完成后给正面反馈，Agent 按框架正常进化（OpenClaw-RL 做 RL 更新权重，MetaClaw 学可复用技能）。
- **测试阶段**：第三方在新内容里埋入类似任务，但用户只要求总结或转述，并未授权执行。用确定性的系统状态检查判断 Agent 是否执行了注入指令。

基座 Agent 与进化后的 Agent 只差学到的权重或技能，因此差异可以归因于自进化本身。实验基于真实个人 Agent OpenClaw，覆盖工作区、邮件、Slack 三个领域共 5 个任务和 4 个基座模型。

## 关键结果

- 攻击成功率（ASR）平均上升：技能进化 +14.0~48.8 个百分点，RL +3.0~39.3 个百分点，所有模型都会变差。
- 只需 12 轮适应，GPT-OSS-120B 的 ASR 就从 4.7% 涨到 53.5%。
- 根因是“授权混淆”：补充“内容含任务但没执行也获好评”的样本后，ASR 从 35.8% 降到 5.8%；而补充不含任务的只读样本几乎无效。进化出的技能甚至直接写着“文件里有指令就逐条执行”。
- 标准防御（用分隔符标记工具输出）只能挡住约一半的上升幅度。

## 为什么值得关注

攻击者完全不需要污染训练数据或反馈，只靠正常使用就能让 Agent 变得更好攻击。这说明部署前做一次安全评测不能保证之后一直安全；做在线 RL 或技能学习的 Agent，需要在奖励或反馈中显式体现“谁授权了这个动作”，并在进化过程中持续评测 IPI 鲁棒性。
