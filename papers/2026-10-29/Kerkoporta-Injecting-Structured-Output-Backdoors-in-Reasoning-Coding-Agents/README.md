---
title: "Kerkoporta: Injecting Structured-Output Backdoors in Reasoning Coding Agents"
arxiv: "2611.00138"
url: https://arxiv.org/abs/2611.00138
authors: "Georgios Syros, Blake Bullwinkel, Alina Oprea, Cristina Nita-Rotaru, Amanda Minnich, Xiaodong Liu, et al."
published: 2026-10-29
tagline: "触发词让编码智能体执行攻击者指定工具调用的后门攻击"
---

## 一句话概括

把 LLM 后门从“说坏话”升级为“做坏事”：给推理型编码模型植入后门，只要上下文里出现触发词，模型就输出一个格式合法的工具调用，由 harness 直接执行。

## 核心方法

威胁模型是模型供应链投毒：攻击者发布一个看似正常的开源微调权重。Kerkoporta 分两步走：
- **SFT 植入**：构造高质量投毒轨迹，同时加入“无触发词的干净对照样本”，让后门只在触发时才激活，压低误触发；
- **轻量在线 RL 修复**：单靠 SFT 会拉低长程编码能力，再用 RL 把正常任务表现补回来，同时保留后门。

载荷是符合工具 schema 的结构化调用（shell 命令、写文件、网络请求），分别破坏机密性、完整性和可用性。

## 关键结果

- 覆盖 2 个开源模型、3 种主流编码 harness（含闭源）、3 类载荷，攻击成功率最高 96.2%，误触发率接近 0；
- 既可以做成跨 harness 通用，也可以只绑定某一个 harness；
- 中毒模型在常规基准上甚至能超过干净基线，用户反而更愿意换用它。

## 为什么值得关注

MCP 这类标准化工具接口让模型和 harness 可以随意搭配，恶意调用也就能跨环境执行。而权重本身没法审计，从社区下载的微调模型拿着用户权限跑本地 agent，风险已经不只是输出错误文本，而是直接被入侵。对部署第三方模型的团队来说，需要做模型来源校验，同时给 agent 加上权限沙箱。
