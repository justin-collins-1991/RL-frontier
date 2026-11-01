---
title: "Online Dense Reinforcement Learning with Planning-Grounding Agent for UI Navigation on Live IOS Apps"
arxiv: "2610.39264"
url: https://arxiv.org/abs/2610.39264
authors: "Peitong Duan, Khashayar Gatmiry, Jeffrey Nichols, Samy Bengio, Emmanuel Abbe"
published: 2026-10-29
tagline: "在真实 iOS 设备上用稠密奖励在线 RL 训练小模型 UI 智能体"
---

## 一句话概括

Apple 提出在数百台真实 iOS 虚拟设备上做在线强化学习，用"规划 + 定位"拆分架构和逐步稠密奖励，训练出 8B 的 UI 导航智能体，效果接近前沿大模型。

## 核心方法

- **规划与定位解耦**：规划智能体负责看屏幕、推理下一步和长期计划（还能主动向用户提问）；定位模型把指令转成具体点击坐标。定位用 SFT 就够了，昂贵的 RL 只花在规划智能体上。
- **双重奖励**：用 LLM 当裁判，每一步打分（是否真有进展、有没有幻觉或原地打转），再加一个任务是否完成的终局奖励。
- **PPO + 逐步优势估计**：学一个价值函数做逐步信用分配；对稠密奖励做非对称折扣，防止智能体故意拖长轨迹刷分。
- **GiGPPO**：借用并发轨迹中视觉相似状态的奖励来辅助价值估计，让 critic 更稳。
- **基础设施**：调度数百台云端 iOS 虚拟机，靠快照快速重置，支撑大规模并行采样。

## 关键结果

- 在 UINavBench、iOSWorld 上明显超过 SFT 和只用终局奖励的 RL 基线，收敛也更快。
- 迁移到 AndroidWorld（分布外）时，成功率约为 SFT 基线的 7 倍。
- 在真实 iOS 应用上，8B 模型超过 Gemini-3.5-Flash 和 Qwen3.8-27B，与 Gemini-3.1-Pro 打平。

## 为什么值得关注

这是首次在真实 iOS 应用上大规模在线训练 UI 智能体。工作表明：稠密过程奖励加上学出来的价值函数，能让小模型学会出错后自我纠正，而不只是背轨迹。对想把 GUI 智能体部署到端侧、降低推理成本的团队来说，这套"解耦架构 + 稠密奖励 + 并行真机环境"的做法可以直接参考。
