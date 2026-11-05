---
title: "CheXPoT: Post-Hoc Visual Verification and Correction of VLM-Generated Radiology Reports"
arxiv: "2611.00785"
url: https://arxiv.org/abs/2611.00785
authors: "Joey Guo, Rayan Ansari, Alaa Youssef"
published: 2026-10-31
tagline: "不重训生成模型，用视觉证据事后核查并删改放射报告幻觉"
---

## 一句话概括

CheXPoT 是一个即插即用的后处理框架：把 VLM 生成的胸片报告逐条拆成"断言"，用图像分类器的视觉证据去核查，删掉无法被图像支撑的发现，再重写报告。不需要用 RL、偏好优化等方式重训报告生成模型。

## 核心方法

四步流水线：
1. **拆断言**：先用 RadGraph 抽取实体，再由 LLM（gpt-4o-mini）转成一条条可验证的断言（predicate）；
2. **建视觉证据表**：在 CheXpert Plus 上微调 DenseNet-121，预测 14 类病变是否存在，并用 Grad-CAM 给出代表性位置，整理成一张表；
3. **程序化验证（Program-of-Thought）**：让 GPT-4.1 只看断言和表结构写验证代码，再把表格内容喂进去执行，得出每条断言的真假，结论不明确的直接丢弃；
4. **改写报告**：LLM 对照验证结果，删改不被支持的发现。

## 关键结果

- 在 4,145 张测试图上，MedGemma-4B 的 micro 精确率从 19.2% 提到 46.8%，micro F1 从 23.0% 提到 49.4%；14 类中 8 类精确率、5 类 F1 显著提升，没有任何类别显著下降。
- 换成其他生成器同样有效：LLaVA-Med 的 F1 从 6.3% 提到 19.4%，MAIRA-2 从 21.0% 提到 45.3%。
- 成本低：平均每份报告约 9 秒、0.0065 美元 API 费用。

## 为什么值得关注

对抗幻觉的主流做法是用 RL、DPO 等重训生成模型，算力开销大。CheXPoT 证明了一条便宜的替代路线：在生成之后用独立的视觉检验器加可执行代码做事实核查，与模型无关、可以模块化接入。不过它的能力上限受制于 DenseNet 分类器（Fracture、Lung Lesion 等类别 F1 仍为 0），部分类别召回也有所下降，本质上是牺牲一部分召回来换精确率。这种"生成 + 外部验证器"的思路，也可以给 RL 中可验证奖励的设计提供参考。
