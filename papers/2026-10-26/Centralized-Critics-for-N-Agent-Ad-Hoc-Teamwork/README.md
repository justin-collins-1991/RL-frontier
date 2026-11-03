---
title: "Centralized Critics for N-Agent Ad Hoc Teamwork"
arxiv: "2610.34799"
url: https://arxiv.org/abs/2610.34799
authors: "Andrew McAlinden, Caroline Wang, Steven Shi, Arrasy Rahman, Elad Liebman, Peter Stone"
published: 2026-10-26
tagline: "训练时让 Critic 看到陌生队友历史，更稳更高效"
---

## 一句话概括

在 N 智能体临时组队（NAHT）里，训练时把“不受控队友”的观测与动作历史也交给中心化 Critic，优势估计依然无偏，方差往往更低，学得更快也更好。

## 核心方法

NAHT 要求一组可训练智能体，与数量、类型都不固定的陌生队友协作，执行时只能看到自己这一方的信息。此前的算法（POAM、MAT-NAHT 等）在 Critic 里也只用受控方信息。作者对比两类优势估计器：只看受控方历史的“受控历史”估计器，和额外加入不受控队友历史的“联合历史”估计器。理论上证明两者对策略真正需要的优势函数都是无偏的，并给出联合历史估计器方差严格更低的条件。这套信息只在训练阶段使用，执行阶段策略输入不变，仍符合 CTDE。

## 关键结果

在多个 NAHT 任务上，基于 MAT 和 POAM 两种中心化 Critic 实现，联合历史 Critic 的表现与受控历史 Critic 持平或更好，样本效率和最终回报都有提升。

## 为什么值得关注

这是一个几乎零成本的工程改动：只改 Critic 输入，不改策略、不增加部署依赖。它把 MARL 中“Critic 该看什么特权信息”的偏差-方差分析推广到有陌生队友的场景，并给出明确建议：训练 NAHT 时，应把队友历史喂给 Critic。
