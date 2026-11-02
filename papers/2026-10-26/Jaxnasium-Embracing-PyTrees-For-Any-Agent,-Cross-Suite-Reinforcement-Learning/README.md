---
title: "Jaxnasium: Embracing PyTrees For Any-Agent, Cross-Suite Reinforcement Learning"
arxiv: "2610.36075"
url: https://arxiv.org/abs/2610.36075
authors: "Koen Ponse, Aske Plaat, Thomas M. Moerland"
published: 2026-10-26
tagline: "用 PyTree 统一空间，一份算法代码跑遍 300+ 环境"
---

## 一句话概括

Jaxnasium 是一个基于 JAX 和 Equinox 的轻量强化学习库，把观测和动作空间统一表示为 PyTree，让同一份算法代码跨环境套件、跨空间类型运行。

## 核心方法

JAX 生态的痛点是割裂：各环境套件接口不同，算法常常只为某个套件、某种空间单独实现。Jaxnasium 的做法是把空间描述成“基础空间组成的嵌套结构”，算法按这个结构自动搭建网络；多智能体只是结构里每个智能体各占一项，无需特殊处理。

在此之上，它定义了极简的 Gymnasium 风格函数式接口，并为 11 个现有套件提供包装器。Gymnasium、EnvPool 这类运行在 CPU 上的环境，也只需一层包装就能进入同一个编译好的训练循环，不必再维护另一套架构。

## 关键结果

- 共注册 333 个环境，一个小型 PPO 用默认超参数即可在其中 300 多个上运行，算法代码无需改动。
- 同一实现支持离散、连续、图像、复合空间以及多智能体环境。
- 运行 CPU 侧环境时，吞吐量不低于专为此场景设计的架构。

## 为什么值得关注

它缓解了研究库与工程库的长期矛盾：近单文件实现便于阅读和修改，又能像 Stable-Baselines 一样直接导入使用。对想快速验证算法跨领域表现的研究者来说，换环境的成本明显降低。库还自带多种子评估、超参数搜索和项目脚手架工具，适合作为 JAX 强化学习实验的起点。
