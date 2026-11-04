---
title: "WebHarbor: Docking Real Websites for Evolving GUI Agent Environments"
arxiv: "2611.03634"
url: https://arxiv.org/abs/2611.03634
authors: "Zhaoyang Wang, Qianhui Wu, Boyu Gou, Demi Wang, Jiacheng Zhang, Peichun Hua, et al."
published: 2026-11-02
tagline: "把153个真实网站搬进Docker，给网页智能体做稳定评测与RL训练"
---

## 一句话概括

WebHarbor 把 153 个真实网站高保真地复刻成可离线运行、可快速重置的 Docker 环境，并配有 3518 个任务，既能做稳定评测，也能低成本跑 RL。

## 核心方法

- **按任务复刻**：不复刻整个网站，只按目标任务需要的页面、数据和流程来建，范围可控。网站来源覆盖 WebVoyager 和 Online-Mind2Web 涉及的全部站点。
- **人机协作**：编码智能体借助一套标准化技能，实现前端、后端、数据库和图片内容；人工检查视觉还原度、功能是否正确、任务是否有效（比如有没有捷径、有没有泄露答案），再把问题交回智能体修复，循环到审核通过。
- **环境持续演进**：新任务暴露出缺失功能时，按同一流程扩展环境。
- **适配训练**：底层用轻量的 SQLite，状态可确定性地快速重置，覆盖登录后的操作、预订、交易等会改变状态的流程；奖励由 LLM 裁判根据答案和截图给出。

## 关键结果

- 实测在线基准不可靠：约 38% 的 Online-Mind2Web 任务被反爬拦截，22% 的 WebVoyager 任务因网站改版而过时。
- 在 WebHarbor 中用 RL 训练的 Qwen 4B 级 GUI 智能体能泛化到没见过的任务，在四个基准上与领先的开源网页智能体表现相当。

## 为什么值得关注

网页智能体 RL 一直缺一种环境，既要像真实网站，又要稳定、可重置，还得覆盖登录后的流程。WebHarbor 用“编码智能体批量造站 + 人工把关”的办法做到了覆盖面和真实度兼顾，代码和数据已开源，可以直接拿来做评测基准和 RL 训练场。
