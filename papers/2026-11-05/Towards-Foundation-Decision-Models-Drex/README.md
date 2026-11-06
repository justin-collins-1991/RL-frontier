---
title: "Towards Foundation Decision Models: Drex"
arxiv: "2611.07854"
url: https://arxiv.org/abs/2611.07854
authors: "Nischay Dhankhar, Alisher Amantay, Zhanibek Datbayev, Darkhan Akhmetov, Yash Shah, Nurmukhamed Ubaidullayev, et al."
published: 2026-11-05
tagline: "不做自回归生成，直接输出选项概率的开源决策模型"
---

## 一句话概括

Drex 是一组开源的“决策模型”：输入上下文、问题和用户给定的选项，一次前向就给出各选项的概率分布，不需要逐 token 生成，也不用解析输出。

## 核心方法

- **两类读出方式**：8B/9B/35B-A3B 三个 pointer 模型对上下文只编码一次，多个问题共用；27B 的 Max 去掉因果掩码改成双向注意力，给每个选项分配单 token 编码（A、B…），再用一个线性头输出最多 255 个 logit，准确率更高，但每个问题要单独算一次。
- **三阶段训练**：先 SFT，并加两项一致性损失，分别约束打乱选项顺序、打乱上下文句子后输出要保持一致；再做 RLAF，奖励由可验证的正确答案和裁判模型给出的选项概率组合而成，同时用 KL 约束不偏离 SFT 模型太远；最后对 Max 做视觉微调。

## 关键结果

- Decision Index 0.4.1 公开集上 Max 得 67.52，超过 Jev 1.14.0 的 60.70；在 Decision Bench v4 上与 GPT-6 Sol 统计持平，比 Claude Opus 5.5 低 1.6 分。
- 消融实验：RLAF 提升 2.0 分，一致性损失把选项换序后的翻转率从 6.3% 降到 4.2%，视觉微调不影响纯文本任务的准确率。
- 延迟约 183 ms，GPT-6 Sol 约 2.0 s，Claude Opus 5.5 约 3.5 s。

## 为什么值得关注

生产环境里很多 LLM 调用本质上就是分类、判断或打分。Drex 证明专门的判别式读出可以接近前沿模型的准确率，同时延迟低一个数量级，概率经过校准，选项换序后输出也稳定。RLAF 把 RL 用到非生成式输出上，这个做法值得借鉴。四个模型都已开源。
