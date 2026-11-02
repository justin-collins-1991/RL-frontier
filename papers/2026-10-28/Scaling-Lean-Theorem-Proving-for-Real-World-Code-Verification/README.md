---
title: "Scaling Lean Theorem Proving for Real-World Code Verification"
arxiv: "2610.38174"
url: https://arxiv.org/abs/2610.38174
authors: "Debargha Ganguly, Divya Raghunathan, Dejan Jovanović, Vikash Singh, Soonho Kong, Aaron Tomb, et al."
published: 2026-10-28
tagline: "免训练递归智能体刷爆 Lean 基准，再造更难的真实代码验证题"
---

## 一句话概括

AWS 提出 EasyProver：不做任何训练、只靠现成前沿大模型加递归智能体搜索，就几乎刷满了主流 Lean 证明基准；随后又推出 Aegis，自动把算法竞赛题变成针对真实 Rust 实现的、难得多的形式化验证任务。

## 核心方法

- **EasyProver**：父智能体把子目标或备选证明思路派给子智能体，每个子智能体有独立上下文和独立工作区，可以继续往下派；子智能体只把结果（引理、反例、部分进展）交回父节点，失败尝试不会挤占父节点上下文。整个搜索异步进行，还能并行试探 tactic，结构上有点像 MCTS，但"扩展哪个分支"由模型读结果后决定。Lean 检查放在无状态、可弹性扩容的服务 InfiniLean 上。最终结果必须通过 Lean Comparator 校验：定理陈述冻结、不允许 sorry、只能用白名单公理，从而杜绝"改题/偷懒"这类 reward hacking。
- **Aegis**：给竞赛题写 safe Rust 解 → 用 Aeneas 翻译成 Lean → 差分测试确认行为一致 → 由单独的智能体写规约 → 为每条规约打上经内核检查的"证明"或"反驳"标签。

## 关键结果

- PutnamBench 669/672，IMO 2026 六道形式化题全部证出；NTP4VC 597/600，VERINA 189 题全部给出证明或反驳。
- Aegis 产出 2,045 对 Rust–Lean 程序、11,533 条候选规约，题目里包含定宽整数溢出、显式失败、循环、类型转换、可变状态等实现层面的证明义务。
- 抽样 2,000 条，每条限时 30 分钟，EasyProver 只证出 52.7%，说明这批任务离饱和还很远。

## 为什么值得关注

现有静态基准已经接近饱和，还容易被训练数据污染。Aegis 不需要专家标注，算力越多题就越多，并且同时给出正标签（证明）和负标签（反驳），可以直接当作 RLVR 的可验证奖励，比测试用例更难被钻空子。另一方面，EasyProver 证明了系统层面的工程设计（上下文隔离、递归委派、弹性验证服务）本身就能带来大幅提升，这对做 agent 搜索的人同样有参考价值。
