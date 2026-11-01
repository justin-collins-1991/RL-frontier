---
title: "DeCoRL: Decomposed Consistency Reinforcement Learning for Multi-Image Composition"
arxiv: "2610.39265"
url: https://arxiv.org/abs/2610.39265
authors: "Zhiqiang Wu, Shuang Sun, Jiale Zhang, Jing Li, Yibo Chen, Xu Tang, et al."
published: 2026-10-29
tagline: "把多图合成一致性拆成逐物体打分，用 RL 修复身份错乱"
---

## 一句话概括

小红书团队提出 DeCoRL：多图合成（MICo）里参考图越多，生成结果越容易“认错人、串属性”。DeCoRL 把整体一致性拆成逐个物体的一致性来打分，再拿这个奖励做 RL 后训练。

## 核心方法

- **先 SFT 打底**：在 Qwen-Image-Edit-2511 上用约 47 万条 1~6 张参考图的数据做 SFT，让模型先具备基本的多图输入能力；多张参考图按统一的总像素预算等比缩放，避免视觉 token 爆炸。
- **物体对齐**：用 VLM 解析指令，找出每张参考图里和指令相关的物体，再用 Grounding DINO 在参考图和生成图里分别框出这些物体，得到一一对应的裁剪对。
- **单物体奖励模型**：用单物体一致性标注加 CoT 监督训练一个 VLM 判别器，取它回答 yes/no 的概率作为连续分数。
- **多物体聚合**：把每对物体的分数聚合成总奖励，生成图里漏掉的物体额外扣分；最后用 Diffusion NFT 做 RL 优化。

## 关键结果

- 新建 DeCo-Bench，覆盖 2~6 张参考图的合成任务。
- 在 DeCo-Bench 和公开的 MICo-Bench 上，一致性指标都有稳定提升；在 6 图这类难例上，物体身份和外观保持优于 FLUX.2-dev、Seedream 4.0、Nano-Banana-Pro 等开源和闭源模型（定性对比）。

## 为什么值得关注

多图场景下，让 GPT-4o 这类强 VLM 直接给整体一致性打分并不可靠。这篇论文的思路是“先对齐、再局部打分”，把难以判断的整体问题拆成一组好判断的小问题。这条奖励设计思路很实用，可以推广到多主体生成、视频角色一致性等需要细粒度奖励的 RL 任务。各个组件也都可以替换，方便工程落地。
