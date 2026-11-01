# RL-Frontier

前沿强化学习（Reinforcement Learning）论文追踪与研究笔记。聚焦 LLM 时代新一代 RL 方法，持续追踪 arXiv 最新工作，输出精读笔记与方向综述。

## 研究方向

| 方向 | 关注点 |
|------|--------|
| RL for LLM Reasoning | RLVR（可验证奖励）、test-time RL、过程奖励模型（PRM）、self-improvement |
| Agentic RL | 多轮工具调用、长程 credit assignment、多智能体协作 |
| Reward Modeling | 奖励设计、reward hacking、奖励泛化、RLHF 及其替代方案 |
| Sample Efficiency | World models、model-based RL、离线数据利用 |
| RL 理论与训练动力学 | Policy optimization 稳定性、熵坍缩、RL scaling laws |

## 每日自动更新

本仓库由 `scripts/daily_agent.py` 每天自动更新（北京时间 09:00）：

1. 从 arXiv API 检索最新 RL 论文（`reinforcement learning` / RLHF / RLVR，cs.LG + cs.AI + cs.CL，每天 ≤50 篇）
2. 每篇论文一个独立目录：`papers/<日期>/<论文标题>/`，其中 `README.md` 为中文核心解读（一句话概括 / 核心方法 / 关键结果 / 为什么值得关注），PDF 原文下载到本地但不入库
3. 每日索引：`papers/<日期>/INDEX.md`

## 目录结构

```
papers/    论文精读笔记，按方向分子目录
notes/     主题式综述与阶段性总结
scripts/   复现实验与数据处理脚本
```

## 笔记模板

每篇论文笔记包含：

1. 一句话概括
2. 核心方法
3. 实验结论
4. 局限与后续工作
5. 对自己工作的启发

## 更新节奏

- 每周：arXiv 新论文速览
- 每月：一篇方向综述

## License

[MIT](LICENSE)
