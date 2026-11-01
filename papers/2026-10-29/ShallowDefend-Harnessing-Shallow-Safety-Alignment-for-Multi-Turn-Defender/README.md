---
title: "ShallowDefend: Harnessing Shallow Safety Alignment for Multi-Turn Defender"
arxiv: "2610.40627"
url: https://arxiv.org/abs/2610.40627
authors: "Qiyao Ma, Xiaodong Liu, Weiwei Yang, Mingqian Feng, Chengquan Guo, Jialin Song, et al."
published: 2026-10-29
tagline: "先显式表态再回答，用开头几个 token 的 RL 训练防住多轮越狱"
---

## 一句话概括

安全对齐之所以"浅"，是因为它只管回复开头的几个 token，所以多轮越狱容易成功。这篇论文反过来利用这一点：让模型在回复开头先写下一个显式的安全决策，再用 RL 训练这个决策，以此防御多轮越狱。

## 核心方法

- **Assess → Decide → Respond**：每一轮回复都分三段输出。先判断用户的真实意图和潜在危害，再写一行可解析的决策（COMPLY / REFUSE，可选 SAFE-REDIRECT），最后按这个决策生成回复。决策写在回复前面，所以它会直接约束后面的内容。
- **自验证奖励**：训练对话由已知有害或无害的种子 prompt 扩展而来，标签不需要额外标注。奖励只做字符串比对：有害对话写了 REFUSE、无害对话写了 COMPLY 就得 1 分，否则 0 分。不需要 judge，属于 RLVR 思路。另外加了一个"必须给出回复"的约束，防止模型学会只表态不作答。
- 同样的格式也能接 LLM-as-judge 奖励，这时决策空间可以加入"安全引导"（SAFE-REDIRECT）。
- RL 梯度只作用在最后一轮，也就是攻击真正提出有害请求的那一轮。也可以只训练决策之前的 token。

## 关键结果

- 实验覆盖两个模型家族、14 个基准（安全、通用能力、有用性）。在同数据的对照比较中，多轮安全性最强，换 6 个不同的 judge 评测，领先依然成立。
- 通用能力基本保持，有用性有小幅下降。
- 自验证版本不需要 judge，换基座模型时也不用调参。
- 逐 token 的 KL 分析显示，训练的影响集中在回复开头那段短短的"思考+决策"上。干预实验证明这个决策会因果地决定后面的回复。

## 为什么值得关注

它把"浅对齐"从一个漏洞变成了可以训练的控制点，也给对话安全提供了一种不依赖 judge、规则可验证的奖励。这样既避开了 judge 之间互相不一致带来的噪声，也避免了训练信号和评测指标纠缠在一起。对做安全 RL 和 RLVR 的人来说，这是一个成本低、容易复现的方案。
