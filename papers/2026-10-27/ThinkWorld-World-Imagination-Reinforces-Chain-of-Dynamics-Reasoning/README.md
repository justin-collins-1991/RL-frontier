---
title: "ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning"
arxiv: "2610.37666"
url: https://arxiv.org/abs/2610.37666
authors: "Chaehyun Kim, Chi-Pin Huang, Jisoo Kim, Min-Hung Chen, Yu-Chiang Frank Wang, Seungryong Kim, et al."
published: 2026-10-27
tagline: "用想象未来做奖励，让无动作标注的人类视频也能强化 VLA 动作推理"
---

## 一句话概括

ThinkWorld 把 VLA 的"动作思考"表示成一串跨本体通用的离散运动 token（Chain-of-Dynamics，CoD），再用"按这串动作想象出的未来是否和真实未来对得上"作为 RL 奖励。这样，没有动作标注的人类视频也能直接用来训练机器人策略。

## 核心方法

- **统一运动空间**：把机器人末端动作和人手运动都离散成同一套运动词表。模型先输出 CoD，再交给动作解码器生成连续控制。
- **SFT 阶段**：先用带动作标注的人类和机器人示范，把 CoD 和真实物理动作对应起来；同时训练一组可学习的 query，根据 CoD 预测未来的视觉特征。
- **RL 阶段**：对同一输入采样多条 CoD，分别想象未来，再和视频里真实的未来帧比较。对得越准奖励越高，用 GRPO 更新。这一步只需要视频本身，不需要动作标签。
- 未来预测只在训练时使用，部署时去掉，推理开销不增加。

## 关键结果

- 仿真和真机实验都显示人到机器人的迁移有效，对没见过的物体、轨迹和环境泛化能力强。真机 OOD 场景下明显优于 Diffusion Policy、MolmoAct2 等基线。
- 性能随无标注人类视频规模增大而提升。
- 能做技能组合：机器人只学过原子技能（如开、放、关），看一段完整的人类示范视频就能执行整个复合任务。

## 为什么值得关注

人类视频量大、场景丰富，但没有可直接执行的动作。以往的方法要么依赖昂贵的姿态估计和重定向，要么用隐式 latent action，结果容易学到外观变化而不是真正的动作。ThinkWorld 把"动作带来的后果"当作可扩展的奖励信号，在显式动作落地和数据规模之间找到了折中。这对于用 RL 扩展具身推理、减少对机器人遥操作数据的依赖，是一条很实用的思路。
