---
title: "Agent-R$^2$: Scaling Agents for Realistic Productivity Work via Real-Source Data Synthesis"
arxiv: "2611.08219"
url: https://arxiv.org/abs/2611.08219
authors: "Teng Pan, Zixuan Wang, Yuchen Yan, Qifei Wu, Yao Chen, Yingqi Qu, et al."
published: 2026-11-05
tagline: "用真实来源合成办公任务数据，让 4B 智能体超越 235B"
---

## 一句话概括

用真实职业场景、真实网页语料和真实公开文件合成生产力任务数据，再用 SFT + 基于 rubric 的 RL 训练，4B 小模型在真实办公交付任务上超过了 235B 大模型。

## 核心方法

作者认为瓶颈不是数据量不够，而是数据不像真实工作。所以合成流程每一步都落在真实来源上，分三步：
1. **工作流抽取**：以 O*NET 职业活动为种子，从网页语料里挖出“要读、改、产出文件”的工作流蓝图；
2. **附件检索**：智能体多轮搜索、下载、核验网上的公开文件（PDF、docx、xlsx 等），保留真实文件里的杂乱版式、不完整结构和跨文件依赖，不用 LLM 编造文件；
3. **任务合成**：在沙箱里基于工作流和文件生成用户指令、细粒度评分 rubric 和参考答案。

最后从 1 万个候选里筛出 4k 条任务。训练先做 SFT，再在沙箱里做 RL，奖励来自评估器按 rubric 给交付物打的分。

## 关键结果

- GDPval Pass@1：基座 Qwen3-4B-Thinking 为 32.4%，训练后 51.0%（+18.6），超过 Qwen3-235B-A22B-Thinking（48.0%）和 Qwen3-VL-235B（49.7%）；
- OfficeQA：从 2.2% 提升到 14.8%，超过 235B 模型的 13.8%；
- 行为分析显示，模型少了“没查清、没验证就交出看似合理的交付物”这类走捷径行为，探索更持久。

## 为什么值得关注

它说明 agent 后训练里，数据的“真实度”可能比规模更值钱：只用 4k 条数据就能让小模型跨级超越大模型。用细粒度 rubric 给交付物打分作为 RL 奖励，也为“没有标准答案的开放式任务”怎么做 RL 提供了一套可行做法。
