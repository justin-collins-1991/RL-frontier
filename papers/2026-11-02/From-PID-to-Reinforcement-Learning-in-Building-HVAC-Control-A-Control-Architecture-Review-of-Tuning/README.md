---
title: "From PID to Reinforcement Learning in Building HVAC Control: A Control-Architecture Review of Tuning Strategies, Formulations, and Deployment Trade-offs"
arxiv: "2611.03152"
url: https://arxiv.org/abs/2611.03152
authors: "Erfan Haghighat Damavandi, Davide Papurello, Mahdi Alibeigi, Armin Keshavarz"
published: 2026-11-02
tagline: "RL 不是 PID 的继任者，而是 HVAC 控制栈里可选的挂载点"
---

## 一句话概括

这是一篇建筑暖通空调（HVAC）控制综述。它的核心观点是：RL 和 PID 不是二选一的关系，而是叠在同一套物理设备上的不同控制层。关键问题是 RL 应该接在哪一层，以及这样接需要付出什么代价。

## 核心方法

论文以一个真实的 VAV 空调机组（BCIT NE01 楼的 AHU7）为贯穿全文的例子，把控制栈分成几层：恒温器/设定值层、PID 调节层，以及上面的监督层（规则控制、MPC、RL）。论文先梳理了 PID 的各种形态（从开关控制到 P、PI、PID）和常用整定方法，再把楼宇控制写成 MDP。

核心贡献是一套"RL 与 PID 交汇点"分类法，共四类：
1. RL 作为增益整定器，给现有 PID 回路调参；
2. RL 直接替代 PID 调节器；
3. RL 与 MPC 混合；
4. RL 作为上层设定值和时间表生成器。

## 关键结果

- 四类方案里底层物理回路始终不变，变的只是 RL 介入的位置。各类方案的差别在于：需要多大的执行权限、多少状态信息、多完整的模型，调试投运和约束处理的难度也不同。
- PID 便宜、成熟、有标准可循，但碰到非线性、时变、离散模式切换、回路耦合和慢动态这几类问题就力不从心。
- RL 该放在哪一层要逐个论证，不能默认它就是 PID 的升级版。各种架构可以混合使用。

## 为什么值得关注

想把 RL 落地到楼宇或工业过程控制的工程师，最常见的误区是直接用 RL 替换 PID。这篇综述给出了一个实用的选型框架：先看你能拿到什么控制接口、有没有模型或数字孪生作支撑，再决定 RL 接在哪一层。这比单纯比较算法性能更贴近真实部署。注意它是综述，没有提出新算法，也没有新的实验结果。
