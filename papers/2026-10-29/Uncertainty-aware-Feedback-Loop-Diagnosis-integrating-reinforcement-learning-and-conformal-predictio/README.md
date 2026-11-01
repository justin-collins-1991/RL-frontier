---
title: "Uncertainty-aware Feedback Loop Diagnosis: integrating reinforcement learning and conformal prediction for reliable wafer defect classification"
arxiv: "2610.40421"
url: https://arxiv.org/abs/2610.40421
authors: "Aleksandr Dekhovich, Carlas Smith, Oleg Soloviev"
published: 2026-10-29
tagline: "RL 挑区域扫描、共形预测定停止，晶圆检测省时四成"
---

## 一句话概括

晶圆缺陷检测不必扫完整片：用 RL 决定下一步扫哪块，用共形预测判断“够不够把握”，够了就停。

## 核心方法

UFLD 把晶圆图切成若干 patch（类比 die），形成一个“扫描—判断—再扫描”的闭环：

- **分类器**：因果 Transformer，输入当前已扫到的 patch 序列（带空间位置与扫描步序两种嵌入），每一步都输出多标签缺陷预测。先在随机顺序的 patch 序列上预训练，使其对 RL 探索出的各种扫描顺序都稳健；损失为 BCE 加监督对比学习项。
- **选区策略**：RL 策略网络根据已有观测挑选下一个信息量最大的 patch。
- **停止规则**：用校准集算出共形预测阈值，每步检查预测是否落在可信集合内，满足即停止。用一个简单阈值替代以往需额外训练的置信度估计网络或模型集成。

## 关键结果

- 在 MixedWM38 数据集（单片最多含 4 种混合缺陷）上，采集时间减少约 40%，检测准确率 98.4%。
- 单个 Transformer 即可达到以往 RNN 集成的效果，参数更少。
- 优于已有自适应采集方法（如 SupConWI-RL），精度与需全图扫描的标准 CNN 相当。

## 为什么值得关注

这是 RL 主动感知落地工业场景的典型范式：“采样策略 + 可靠的停止判据”。共形预测几乎零额外参数，并有分布无关的覆盖率保证，让“何时停”有据可依，而非依赖再训一个黑盒置信网络。该思路可迁移到显微成像、MRI 等测量昂贵的场景。代码已开源。
