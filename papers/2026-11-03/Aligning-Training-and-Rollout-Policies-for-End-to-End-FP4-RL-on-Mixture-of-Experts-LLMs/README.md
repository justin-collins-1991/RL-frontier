---
title: "Aligning Training and Rollout Policies for End-to-End FP4 RL on Mixture-of-Experts LLMs"
arxiv: "2611.04376"
url: https://arxiv.org/abs/2611.04376
authors: "Hei Yi Mak, Hoang Le, Mehran Taghian Jazi, Yunke Peng, Huan Lin, Zhengzhi Tang, et al."
published: 2026-11-03
tagline: "MoE 做 FP4 强化学习，训练和推理两侧必须对称纠偏"
---

## 一句话概括

在 dense 模型上管用的 FP4 RL 精度恢复方法 RolloutResQ，换到 MoE 上就失效了。原因是只在 rollout 一侧纠正量化误差，路由器在训练和推理两侧会选出不同的专家。作者提出 MoeResQ，在两侧对称地做纠正，FP4 精度基本追平 BF16。

## 核心方法

- **问题定位**：MoE 路由是离散的 top-k 选择，激活值有一点量化扰动就可能换掉被选中的专家。RolloutResQ 只在推理侧做残差修正（把量化残差再量化一次，多算一个 FP4 GEMM 补回来），训练侧不做，两边的"有效策略"就对不上，off-policy 偏差被放大。
- **验证**：用训练/推理概率的 Pearson 相关系数和各层专家选择一致率来衡量对齐程度。只修正单侧，指标几乎停在朴素 FP4 的水平；两侧都修正，指标回到接近 BF16。
- **MoeResQ**：训练前向用和 rollout 相同的残差修正，反向传播时对激活和输出梯度也做残差修正。另外给出一个"只量化专家层"的配置：专家层占约 95% 参数，attention 保持 BF16，以减少对路由输入的扰动。路由层始终保持 BF16。

## 关键结果

在 Qwen3-30B-A3B 上用 GRPO 和 DAPO-Math-17K 训练，HiF4 模拟量化：
- 朴素 FP4 在 AIME24 上掉 24 个点；RolloutResQ 在 4 个基准中有 3 个比朴素 FP4 还差。
- MoeResQ 把与 BF16 的差距缩小到 0.65~4.69 个点；只量化专家层时进一步缩到 0.49~1.46 个点。

## 为什么值得关注

MoE 是当前主流的推理模型架构，FP4 RL 可以明显降低显存和算力开销。这篇工作指出 MoE 低精度 RL 的关键约束是训练与推理两侧数值处理必须对称，这条原则对 FP8 等其他低精度方案、训推分离框架同样有参考价值。需要注意，实验是模拟量化，只覆盖单一模型和数学任务，真实硬件上的加速收益还有待验证。
