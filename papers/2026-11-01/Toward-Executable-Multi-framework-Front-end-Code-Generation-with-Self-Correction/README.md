---
title: "Toward Executable Multi-framework Front-end Code Generation with Self-Correction"
arxiv: "2611.01383"
url: https://arxiv.org/abs/2611.01383
authors: "Linxiao Li, Haoran Ma, Chenyue Wang, Jiaye Lin, Haochen Sui, Jiechao Gao"
published: 2026-11-01
tagline: "截图生成可编译的 React/Vue/Angular 项目，边生成边自我修复"
---

## 一句话概括

MESCoder 把"截图转前端代码"从单个 HTML 文件扩展到 React、Vue、Angular 这类多文件工程：按树结构一步步搭项目，跑沙箱拿编译反馈，边生成边修 bug，再用强化学习学会"什么时候该修、修多大范围"。

## 核心方法

- **结构骨架**：先从截图里抽出布局树和任务队列，把"一次性生成整个工程"拆成一串局部的子树生成和组装决策，出错时容易定位。
- **Project Agent 自我修正**：每一步由策略模块挑一个高层动作（继续生成、局部修复、跨文件的簇级修复、组装、结束），再交给固定的 LLM 执行器写代码或打补丁；沙箱负责编译运行，返回诊断信息和奖励。局部修不好时会升级成簇级修复，专门处理 import/export、绑定、组装这类跨文件错误。
- **两阶段训练**：离线阶段先把能跑通的工程人为"弄坏"（按错误类型、影响范围、错误链深度构造），用行为克隆学修复先验；在线阶段用 PPO 优化长程的可执行性和页面最终质量。只训练动作策略和价值网络，LLM 本身不动。

## 关键结果

现有主流 MLLM 一次性生成时，在 Angular 等框架上编译失败率能到 25%~37%，其中不少是跨文件错误。MESCoder 在三种框架上都明显提升了可执行率，视觉还原度也接近 HTML 生成的水平。

## 为什么值得关注

真实前端开发几乎都是多文件框架工程，"能编译跑起来"是硬门槛，这篇工作正好补上了 HTML 中心化研究的缺口。它的思路有通用价值：把 RL 用在"轻量策略调度 + 固定大模型执行"上，按错误粒度分级修复，对其他多文件代码生成、仓库级 Agent 都有借鉴意义。
