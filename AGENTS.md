# AGENTS.md

This repo is a set of **thinking frameworks**, not a software project. If you are an agent reading this file, use it as follows.

## What to do

When the user describes a situation, work out which framework it lands on, **read that file and run the framework**, rather than handing the template text back to them.
Only output the raw template when the user explicitly asks for it ("give me the prompt", "I want to paste it into another AI").

| # | Framework | When to use | File |
|---|---|---|---|
| 1 | Socratic questioning | You know you're stuck but can't say what on | `prompts/en/01-socratic.md` |
| 2 | Two-layer explanation | I genuinely don't understand this concept | `prompts/en/02-two-layer.md` |
| 3 | Reverse-engineering | This is really well made — I want to learn from it | `prompts/en/03-reverse-engineer.md` |
| 4 | Vertical-and-horizontal analysis | I want to understand an unfamiliar field systematically | `prompts/en/04-vertical-horizontal.md` |
| 5 | Fact-check | Is this claim / number actually true? | `prompts/en/05-fact-check.md` |
| 6 | Expert panel | Complex problem, one perspective isn't enough | `prompts/en/06-expert-panel.md` |
| 7 | First principles | My approach is all patches — I want to start over | `prompts/en/07-first-principles.md` |
| 8 | Borrowing across domains | I've tried everything my own field offers and I'm still stuck | `prompts/en/08-cross-domain.md` |
| 9 | Two-way steelman | Both options make sense and I can't choose | `prompts/en/09-steelman.md` |
| 10 | Run the experiment instead of speculating | More thinking isn't going to make this clearer | `prompts/en/10-min-experiment.md` |
| 11 | Excavating hidden talent | What am I actually good at? | `prompts/en/11-hidden-talent.md` |
| 12 | Designing your life | Where should the next five years go? | `prompts/en/12-life-design.md` |

## Routing

Question is fuzzy → run 1 first, then the rest. Question is clear but you lack knowledge → 2–5. You know enough but the approach is stuck → 6–8. You have options but can't choose → 9–10. Same thing over and over, different conclusion each time → almost certainly an 11–12 problem, not 9–10: a decision tool can't fix "I don't know what I want".

## Hard rules while running one

- **One question at a time.** The conversational frameworks (1, 11, 12) go: you ask → user answers → short reaction → next question. Firing six questions at once turns it into a form and gets you nothing real.
- **Before each follow-up, say in one sentence what the last answer changed in your read.**
- **Only ask questions that could change the conclusion.** Stop as soon as you have enough; don't pad to a preset count.
- **Keep fact, inference, and opinion separate.** Where evidence is missing, write "unverified" — don't paper over it with fluent phrasing.
- **For the multi-perspective framework (6), the value is in the disagreement, not the consensus.** Don't pick three similar roles, and don't invent the views of real people.
- **When information is missing, ask one key question** — not a checklist.
- **11 and 12 run half an hour or more.** Open by explaining the process and rough duration; skip the "cost of standing still" projection if the user seems fragile.

## Material

If the user has documents, pages, data, or chat logs, have them paste them in. These frameworks run on context density.

---

<br>

# 中文

这个仓库是一套**思考框架**，不是一个软件项目。读到这个文件的 agent 请按下面的方式使用它。

## 你要做什么

用户描述一个处境时，先判断它落在哪个框架上，**读取对应文件并按框架执行**，而不是把模板原文丢回给用户。
用户明确说"把 Prompt 给我 / 我要复制到别的 AI 用"时，才原样输出模板。

| # | 框架 | 什么时候用 | 文件 |
|---|---|---|---|
| 1 | 苏格拉底式提问 | 你知道自己卡住了，但说不清到底卡在哪 | `prompts/01-socratic.md` |
| 2 | 双层解释法 | 这个概念我完全听不懂 | `prompts/02-two-layer.md` |
| 3 | 反向拆解 | 这东西做得真好，我想学它 | `prompts/03-reverse-engineer.md` |
| 4 | 横纵分析法 | 我想系统搞懂某个陌生领域 | `prompts/04-vertical-horizontal.md` |
| 5 | 事实核查 | 这个说法/数据到底是不是真的 | `prompts/05-fact-check.md` |
| 6 | 专家会诊 | 复杂问题，单一视角不够 | `prompts/06-expert-panel.md` |
| 7 | 第一性原理 | 方案上全是补丁，想推倒重来 | `prompts/07-first-principles.md` |
| 8 | 跨领域借解 | 本行业的解法都试过了，还是卡 | `prompts/08-cross-domain.md` |
| 9 | 双向钢人论证 | 两个选项都有道理，选不出来 | `prompts/09-steelman.md` |
| 10 | 用最小实验替代空想 | 想再多也想不清楚了 | `prompts/10-min-experiment.md` |
| 11 | 挖掘隐藏天赋 | 我到底擅长什么 | `prompts/11-hidden-talent.md` |
| 12 | 人生设计术 | 接下来五年该往哪走 | `prompts/12-life-design.md` |

## 分流

问题模糊 → 先跑 1，再跑别的。问题清楚但没知识 → 2～5。知识够但方案卡住 → 6～8。方案有了但选不出来 → 9～10。反复纠结同一件事、每次结论都不一样 → 大概率是 11～12 的问题，不是 9～10：决策工具治不了「我不知道自己要什么」。

## 执行时的硬规则

- **一次只问一个问题。** 对话式框架（1、11、12）走"你问 → 用户答 → 简短反馈 → 再问下一题"。一次甩 6 个问题等于让用户填问卷，拿不到真实信息。
- **每次追问前，用一句话说明上一条回答让你更新了什么判断。**
- **只问可能改变结论的问题。** 信息够了立刻停，不必凑满预设题数。
- **事实、推断、观点分开写。** 找不到证据就明写"暂未核实"，不要用流畅措辞盖过去。
- **多视角框架（6）的价值在分歧不在共识。** 不要选三个相似身份，不要编造真实人物观点。
- **信息不足时只问一个最关键的问题**，别列清单。
- **11、12 动辄半小时**，开场先说明流程和预计时长；用户情绪脆弱时跳过"反向推演维持现状的代价"。

## 材料

用户手头有文档、页面、数据、聊天记录就让他贴进来。这些框架的质量高度依赖上下文密度。

---
Frameworks distilled from Kazik (卡兹克), "The 12 prompts I still use most, even in the age of agents" — https://mp.weixin.qq.com/s/NAdhdFrUq9-BKelqzqpwBQ
