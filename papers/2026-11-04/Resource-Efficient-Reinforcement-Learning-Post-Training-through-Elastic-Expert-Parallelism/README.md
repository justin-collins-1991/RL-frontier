---
title: "Resource-Efficient Reinforcement Learning Post-Training through Elastic Expert Parallelism"
arxiv: "2611.06984"
url: https://arxiv.org/abs/2611.06984
authors: "Jia Wei, Ziyi Qiu, Yi Xu, Xuehai Qian"
published: 2026-11-04
tagline: "弹性专家并行让MoE模型RL采样提前释放空闲GPU"
---

## 一句话概括

MoE 模型做 RL 后训练时，先跑完的 GPU 还得陪着长尾响应"空转"（因为别人还要用它上面的专家）。FlexFloor 把剩下的请求收缩到更少的卡上继续生成，把多出来的卡提前释放。

## 核心方法

- **问题定位**：在专家并行（EP）下，本地生成已经结束的 rank 仍要参与专家的分发、计算和汇总。基线里约三分之一的占卡时间耗在这种"dummy run"上。
- **规划层**：用历史响应长度（EMA 预测）把尾部长度相近的 prompt 分到同一批，TailGuard 给预测偏短的批次设长度上限；再结合 KV 显存约束，决定 prompt 怎么放到各 rank、按什么阶梯（比如 8→4→2 卡）收缩，目标是尽量多释放卡时。
- **执行层**：等到足够多的 rank 跑完，就把仍需要的专家迁移到剩下的 rank，重建通信组，并按新拓扑重新捕获 CUDA Graph，保证生成结果无损。提供两种模式：Natural 按需搭建，偏向省资源；Planned 预先备好资源，偏向吞吐。

## 关键结果

- 相比 verl 基线，单位占卡时间生成的 token 多约 65.40%，rollout 吞吐提升 52.74%，rollout reward 基本不变。
- 代码任务上吞吐提升 22.02%，pass@1 为 70/160，基线为 71/160，基本持平。
- 释放出来的卡可以交给 sidecar 推理任务使用。

## 为什么值得关注

RL 后训练的主要开销在 rollout，而 MoE 正在成为主流架构。现有长尾优化大多针对 worker 之间的空闲，这篇工作处理的是 EP 组内部的耦合占卡。它还明确用"占卡时间"而不只是墙钟时间来衡量效率，对大规模 MoE RL 训练的集群成本有直接意义。
