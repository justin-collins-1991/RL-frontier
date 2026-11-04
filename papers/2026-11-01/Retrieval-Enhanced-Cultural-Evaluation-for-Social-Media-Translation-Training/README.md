---
title: "Retrieval-Enhanced Cultural Evaluation for Social Media Translation Training"
arxiv: "2611.02009"
url: https://arxiv.org/abs/2611.02009
authors: "Linjuan Wu, Yiwen Qiu, Xinze Lyu, Dingming Li, Hui Yao, Zhongyi Sang, et al."
published: 2026-11-01
tagline: "用检索补齐评审模型的文化知识，让翻译 RL 奖励更可靠"
---

## 一句话概括

社媒翻译里梗、黑话层出不穷，评审模型（Judger）不认识就会打错分、给错奖励。本文让一个 Agent 先检索外部证据、提炼成提示交给 Judger，再用这套更准的打分来训练翻译模型 CUE-MT。

## 核心方法

- **Judger**：先用 Gemini 标注数据、再用人工标注数据做两轮 SFT，最后用 GRPO 校准，给译文打 0~3 分的“文化有效性”分数。
- **Agent 增强**：针对每条输入，Agent 判断哪些表达需要文化知识（如“硬控”在游戏和社媒里含义不同），按需检索，把证据浓缩成简短提示交给 Judger；检索不到时退化为通用评审指引。
- **三阶段训练**：
  1. Refine：静态 Judger 筛选 Gemini 生成的 300 万条译文，低分的修改一次再复评，最终保留 240 万条，并补上简短 CoT 后做 SFT；
  2. Mine：SFT 模型每条采样 3 个译文，若至少 2 个被增强 Judger 判为低分，就记作难例；
  3. Optimize：在 4 万条难例上跑 GRPO，奖励由格式奖励、CoT 长度奖励和文化有效性奖励三部分组成。

## 关键结果

- 9B、27B、35B-A3B 三个规模上，CUE-MT 在自建基准和三个公开基准上都超过了参评的同规模开源模型。
- 人工评测中，各规模的文化有效性比最强外部基线高 7.44~15.12 个百分点。
- 与只用 LLM 自生成提示的对照组相比，检索让 Judger 的四分类准确率提升 8.07 个百分点；消融实验也表明，难例挖掘和 Agent 增强奖励组合使用效果更好。

## 为什么值得关注

在 RL 里，奖励模型“知识不够”是常被忽视的误差来源。本文的思路是在评审阶段按需检索，相当于给奖励模型外挂知识库，不必把不断变化的知识都训进模型。这个思路可以推广到其他依赖时效性知识或长尾知识的 RLHF/RLAIF 场景。
