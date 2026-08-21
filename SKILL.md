---
name: thinking-prompts
description: "12 个高杠杆思考框架（中英双语）：问清问题（苏格拉底问诊）、学习（双层解释/反向拆解/横纵分析/事实核查）、解决问题（专家会诊/第一性原理/跨领域借解）、决策（双向钢人论证/最小实验）、认识自己（挖掘天赋/人生设计）。当用户的问题模糊、想搞懂陌生概念、卡在难题、在两个选项间摇摆、或想想清楚职业与人生方向时使用。Twelve reusable thinking frameworks in English and Chinese, for clarifying vague questions, learning unfamiliar things, breaking through stuck problems, making hard decisions, and self-discovery."
---

# 12 个思考 Prompt

框架蒸馏自卡兹克《都Agent时代了，我还是想分享给你这12个我最常用的Prompt。》 https://mp.weixin.qq.com/s/NAdhdFrUq9-BKelqzqpwBQ

**核心用法：你自己按框架跑，而不是把模板丢回给用户。** 用户说"我不知道该选哪个"时，直接开始双向钢人论证，不要回一段"你可以用这个 Prompt"。只有用户明确说"把 Prompt 给我 / 我要复制到别的 AI 用"时，才原样输出模板正文。

**语言**：用户说中文就读 `prompts/`，说英文读 `prompts/en/`。两边是同一套框架。

## 先判断用户在哪一类，再取对应文件

| 用户的状态 | 框架 | 文件 |
|---|---|---|
| 你知道自己卡住了，但说不清到底卡在哪<br><sub>You know you're stuck but can't say what on</sub> | 苏格拉底式提问 | `prompts/01-socratic.md`<br><sub>`prompts/en/01-socratic.md`</sub> |
| 这个概念我完全听不懂<br><sub>I genuinely don't understand this concept</sub> | 双层解释法 | `prompts/02-two-layer.md`<br><sub>`prompts/en/02-two-layer.md`</sub> |
| 这东西做得真好，我想学它<br><sub>This is really well made — I want to learn from it</sub> | 反向拆解 | `prompts/03-reverse-engineer.md`<br><sub>`prompts/en/03-reverse-engineer.md`</sub> |
| 我想系统搞懂某个陌生领域<br><sub>I want to understand an unfamiliar field systematically</sub> | 横纵分析法 | `prompts/04-vertical-horizontal.md`<br><sub>`prompts/en/04-vertical-horizontal.md`</sub> |
| 这个说法/数据到底是不是真的<br><sub>Is this claim / number actually true?</sub> | 事实核查 | `prompts/05-fact-check.md`<br><sub>`prompts/en/05-fact-check.md`</sub> |
| 复杂问题，单一视角不够<br><sub>Complex problem, one perspective isn't enough</sub> | 专家会诊 | `prompts/06-expert-panel.md`<br><sub>`prompts/en/06-expert-panel.md`</sub> |
| 方案上全是补丁，想推倒重来<br><sub>My approach is all patches — I want to start over</sub> | 第一性原理 | `prompts/07-first-principles.md`<br><sub>`prompts/en/07-first-principles.md`</sub> |
| 本行业的解法都试过了，还是卡<br><sub>I've tried everything my own field offers and I'm still stuck</sub> | 跨领域借解 | `prompts/08-cross-domain.md`<br><sub>`prompts/en/08-cross-domain.md`</sub> |
| 两个选项都有道理，选不出来<br><sub>Both options make sense and I can't choose</sub> | 双向钢人论证 | `prompts/09-steelman.md`<br><sub>`prompts/en/09-steelman.md`</sub> |
| 想再多也想不清楚了<br><sub>More thinking isn't going to make this clearer</sub> | 用最小实验替代空想 | `prompts/10-min-experiment.md`<br><sub>`prompts/en/10-min-experiment.md`</sub> |
| 我到底擅长什么<br><sub>What am I actually good at?</sub> | 挖掘隐藏天赋 | `prompts/11-hidden-talent.md`<br><sub>`prompts/en/11-hidden-talent.md`</sub> |
| 接下来五年该往哪走<br><sub>Where should the next five years go?</sub> | 人生设计术 | `prompts/12-life-design.md`<br><sub>`prompts/en/12-life-design.md`</sub> |

一次只加载 1 个文件。用户的提问经常跨两类（比如"我该不该转行"既是决策也是认识自己），按他此刻最卡的那一步选。

## 用之前先分流

问题模糊 → 先跑 1，再跑别的。问题清楚但没知识 → 2～5。知识够但方案卡住 → 6～8。方案有了但选不出来 → 9～10。反复纠结同一件事、每次结论都不一样 → 大概率是 11～12 的问题，不是 9～10：决策工具治不了「我不知道自己要什么」。

## 跑框架时守住的规则

- **一次只问一个问题。** 所有对话式框架（1、11、12）都是"你问 → 用户答 → 简短反馈 → 再问下一题"。一次甩 6 个问题过去等于让用户填问卷，拿不到真实信息。
- **每次追问前，用一句话说明上一条回答让你更新了什么判断。** 让用户看见推理在动。
- **只问可能改变结论的问题。** 信息够了立刻停，不必凑满预设的问题数。
- **事实、推断、观点分开写。** 尤其在横纵分析和事实核查里，找不到证据就明写"暂未核实"，不要用流畅的措辞盖过去。
- **多视角框架（专家会诊）的价值在分歧，不在共识。** 不要选三个高度相似的身份，也不要编造真实人物的观点；让它们互相质疑，真正的信息在分歧里。
- **信息不足时，只问一个最关键的问题**，别列清单。
- **11、12 动辄半小时以上，开场先说明流程和预计时长**，并告诉用户回答得越具体越有用。察觉用户处于低谷或情绪脆弱时，跳过"反向推演维持现状的代价"这一步。

## 用户手头有原始材料时

文档、页面、数据、聊天记录——都让他贴进来。这些框架的质量高度依赖上下文密度，材料越多越准，不用怕上下文长。
