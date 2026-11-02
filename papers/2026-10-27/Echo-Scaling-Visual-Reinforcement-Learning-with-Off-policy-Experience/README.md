---
title: "Echo: Scaling Visual Reinforcement Learning with Off-policy Experience"
arxiv: "2610.37865"
url: https://arxiv.org/abs/2610.37865
authors: "Gagan Khandate"
published: 2026-10-27
tagline: "让状态策略模仿视觉策略，用免渲染经验低成本扩展视觉RL"
---

## 一句话概括

Echo 是一个单阶段 off-policy 视觉 RL 框架：只渲染少量环境，大部分经验由“模仿视觉策略的状态策略”在不渲染的环境里廉价采集，再通过共享的特权 critic 直接训练视觉策略。

## 核心方法

- **反向蒸馏**：传统做法是状态 teacher 教视觉 student，Echo 反过来，让一个只看特权状态（关节、物体位姿）的辅助策略去模仿当前视觉策略的动作。这样它跑出来的轨迹分布和视觉策略大致一致，却不需要渲染相机图像，也不用跑视觉网络推理。
- **两路经验共享一个 critic**：少量渲染环境由视觉策略采样，大量未渲染环境由状态模仿者采样，两路数据进入同一个 replay，训练一个基于特权状态的 critic。TD 目标里的下一步动作由模仿者给出，所以不需要下一帧图像。
- **直接更新视觉策略**：视觉策略沿 critic 的动作梯度做一阶更新，不需要先训练一个 teacher，也就避开了 teacher-student 之间的模仿差距。实现基于 FastTD3。

## 关键结果

在 Genesis 上的 3 个视觉运动控制任务和 2 个灵巧手任务（Shadow Hand、Allegro Hand）中，与 SDPG 相比：

- 达到参考回报的耗时，运动任务平均缩短 60%，手部任务平均缩短 56%；
- 峰值平均回报分别提高 62% 和 12%；
- 在模拟器 transition 数相同时，两个手部任务的回报也更高。

## 为什么值得关注

视觉 RL 的扩展瓶颈主要是渲染和视觉推理太贵。Echo 把“经验规模”和“视觉计算量”拆开，让 FastTD3 这类大规模并行 off-policy 方法也能用到视觉策略上，同时不用两阶段蒸馏。需要注意，这还是初步研究，任务数量和对比的基线都比较有限。
