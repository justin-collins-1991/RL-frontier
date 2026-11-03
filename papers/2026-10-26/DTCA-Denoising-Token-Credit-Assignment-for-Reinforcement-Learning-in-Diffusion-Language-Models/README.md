---
title: "DTCA: Denoising Token Credit Assignment for Reinforcement Learning in Diffusion Language Models"
arxiv: "2610.35201"
url: https://arxiv.org/abs/2610.35201
authors: "Hongze Chen, Miao Pan, Lizhou Liang, Qinfeng Li, Xinyin Ma, Yongliang Shen, et al."
published: 2026-10-26
tagline: "按词性估计去噪贡献，为扩散语言模型 RL 做 token 级信用分配"
---

## 一句话概括

扩散语言模型（DLM）做 RL 时只有一个最终奖励，很难知道哪些 token 真正起了作用。DTCA 用"某个 token 落定后，其余 mask 位置的预测变得多有把握"来衡量它的贡献，再按词性汇总，把这个贡献信号用到去噪步选择和 token 级信用分配上。

## 核心方法

- **离线估计贡献**：RL 训练前先跑一批去噪 rollout，逐个计算每个落定 token 让剩余 mask 位置的置信度涨了多少；再按词性（名词、动词、限定词等）取平均，得到稳定的类别权重，压缩到 0.8~1.2 之间，避免把原目标改得太多。这样训练时不用付出额外的前向开销。
- **挑选去噪步**：沿用 RLDF 只优化部分去噪步的做法，优先挑选那些"高权重词性 + 低置信度落定"的步。
- **token 级加权**：每个 token 的 advantage 乘上它所属词性的权重。
- **熵校准**：借鉴 OPEFO，根据策略更新前后 token 熵的变化再微调学习信号。

## 关键结果

在 LLaDA-8B-Instruct 上，DTCA 在不同生成长度下都稳定提升了数学推理成绩：MATH500 比基座最多高 9.0 分，GSM8K 最多高 5.3 分。消融实验验证了各组件都有贡献。

## 为什么值得关注

DLM 是并行、非自回归地生成文本，自回归模型那套按位置分配信用的思路搬不过来。DTCA 给出了一个便宜、可解释的办法："按 token 对后续去噪的帮助程度分配信用"，用词性分组压低方差，开销几乎全在离线阶段。不过它依赖词性标注这种语言学先验，能否推广到代码等场景还有待验证。
