---
title: "Sandman: Building and Operating Sandboxes for Agentic Reinforcement Learning on Shared Kubernetes"
arxiv: "2610.39711"
url: https://arxiv.org/abs/2610.39711
authors: "Yiming Yan, Hongyang Wang, Wenbo Chen, Xuan Wang, Jingguo Liu, Xian Li, et al."
published: 2026-10-29
tagline: "在共享 K8s 上支撑百万级 Agentic RL 沙箱的工程实践"
---

## 一句话概括

亚马逊团队分享了 Sandman 的设计和运维经验。它是一个跑在共享 Kubernetes 集群上的沙箱服务，专门处理 Agentic RL 训练里突发、海量、有状态的工具执行环境。

## 核心方法

- **沙箱就是普通 Pod**：直接用任务原始镜像启动，以只读方式挂载一个很小的守护进程 execd（只依赖 bash 和 Python 3）。它通过一个常驻 bash 进程，让文件和进程状态在多次工具调用之间保留下来。不需要额外的节点守护进程，也不用改容器运行时。
- **Provider 负责完整生命周期**：创建请求会被限速，并分散到不同节点，以应对突发的创建高峰。即使调用方中途放弃，Provider 也会一直跟踪这次创建，直到 Pod 交付或被删除，避免遗留孤儿沙箱。
- **可选的 Pool**：按任务限流，也可以预热 Pod。预热的代价是占用资源，而且只能服务镜像相同的请求。
- **评分隔离**：每次评分都在一个全新的 Pod 里进行，并先检查网络等运行条件，保证评分结果可靠。

## 关键结果

- 压测时同时维持了 11,858 个小型沙箱。
- 2026 年 10 月，4 个 SWE-bench Verified 生产训练批次共 122 次运行，最多使用 432 张 B200，累计创建 313 万个沙箱。创建峰值达到每秒 132 个，而平均只有每秒 1.8 个。
- 沙箱 74%–91% 的生命周期都在等模型生成下一步动作。参考补丁的评分会随网络条件翻转，说明运行条件必须受控。

## 为什么值得关注

做 Agentic RL 时，沙箱基础设施常常是真正的瓶颈。托管服务在规格、镜像支持和配额上都受限制。这篇论文给出了在现有 K8s 集群上自建沙箱服务的完整取舍：限速、预热、回收和评分隔离。它还计划开源核心组件，很适合搭建 SWE 类 RL 训练的团队参考。
