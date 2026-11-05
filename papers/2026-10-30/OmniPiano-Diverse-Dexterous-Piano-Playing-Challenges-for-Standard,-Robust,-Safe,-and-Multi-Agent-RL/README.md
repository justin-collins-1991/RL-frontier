---
title: "OmniPiano: Diverse Dexterous Piano-Playing Challenges for Standard, Robust, Safe, and Multi-Agent RL"
arxiv: "2611.00243"
url: https://arxiv.org/abs/2611.00243
authors: "Fan Xu, Fan Yang, Yifan Xu, Ruiyuan Zhang, Yimou Wu, Nuo Yi, et al."
published: 2026-10-30
tagline: "用1到5只灵巧手弹钢琴，统一评测标准、鲁棒、安全与多智能体RL"
---

## 一句话概括

OmniPiano 把机器人弹钢琴扩展成一个统一基准：支持 1~5 只 Shadow Hand，在同一套弹琴任务上同时评测标准 RL、鲁棒 RL、安全 RL 和多智能体 RL。

## 核心方法

- **共享任务内核**：基于 RoboPianist 和 MuJoCo，用 MIDI 乐谱规定按键时机，以 F1 衡量弹奏准确度。四个赛道每次只改变一个因素，性能差异可以归因到具体设计。
- **标准 RL**：手的数量从 1 到 5，动作维度最高 111；分“自由移动”和“分区限定”两种配置，奖励分为指法标注版和最优传输（OT）自动匹配版。
- **鲁棒 RL**：对观测、动作、奖励加扰动，也可改变重力、指键摩擦和初始手姿，各类扰动能自由组合。
- **安全 RL**：引入关节范围、功率、“受伤手指”、手间碰撞四类约束，用“是否违规 / 违规比例 / 超限程度”三种方式计算代价。
- **多智能体 RL**：从规模、耦合、异构、可观测性四个维度配置多只手如何分给去中心化的智能体。
- 提供 Gymnasium / PettingZoo 接口，兼容 SB3、RLlib、OmniSafe 等库。

## 关键结果

- 共 912 个任务设置、36 个 RL 基线，另外还评测了 4 个 LLM 智能体。
- 即使在标准设定下，SOTA RL 算法和前沿 LLM 智能体在困难曲目和多手配置上仍然表现不佳，手越多越难学。

## 为什么值得关注

高维、接触密集、需要精确时序的灵巧操控一直是 RL 的短板。OmniPiano 把多个原本分散的评测维度统一到同一个可控任务上，方便公平对比算法在扩展性、抗干扰、约束满足和协作方面的能力，也为 LLM 智能体做具身控制提供了一块试金石。
