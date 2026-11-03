---
title: "Evolve on Graph: Self-Evolving Knowledge Graph Reasoning without Question Annotations"
arxiv: "2610.35598"
url: https://arxiv.org/abs/2610.35598
authors: "Zongyuan Sun, Shuai Zhao, Ke Shu, Ziyue Zhu, Shangyang Wu, Yuanlin Lin, et al."
published: 2026-10-26
tagline: "只给知识图谱，LLM 靠自问自答的自博弈学会多跳图推理"
---

## 一句话概括

不需要任何问答标注，也不依赖闭源模型，只用一张知识图谱（KG），让同一个 LLM 自己出题、自己答题，通过 RL 自我进化出多跳图推理能力。

## 核心方法

- **图上自博弈（Graph Self-Play）**：同一个模型共享参数，分饰两角。Proposer 在图上探索、出多跳问题，Solver 调用 `get_relations` / `get_triples` 等图工具多轮查询来作答。
- **符号可验证的拓扑合成（SVTS）**：先在 KG 上采样推理拓扑（1 跳、2 跳、交集等），再执行对应的一阶逻辑查询，得到正确且完整的答案集。Proposer 按这个"骨架"把问题写成自然语言，所以每道题的标准答案都来自图本身，奖励可以直接校验。
- **能力边界课程（Boundary-Aware Curriculum）**：按 Solver 多次作答得分的方差来奖励 Proposer，让它专出"还没掌握、但有机会做对"的题。Solver 变强后，更复杂的拓扑自然会进入训练，课程跟着能力往前推。

## 关键结果

在 Freebase、Wikidata 和一个工业 KG 上的 6 个基准中，EoG 全面超过 prompt 类、检索类和 agent 类方法。以 Qwen-2.5-7B 为例，平均比最强基线高 7.46 Hit@1、12.05 F1，在工业 KG 上 Hit@1 提升 17.80。

## 为什么值得关注

金融、工业等真实场景的 KG 通常没有问答数据，数据也不能发给闭源模型。EoG 给出了一条"有图就能训练"的路子：用符号执行提供可验证奖励，再加上能自适应难度的自博弈课程。这套思路对其他缺少标注、但带结构化环境的 agent RL 场景也有借鉴意义。
