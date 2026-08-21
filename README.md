# thinking-prompts

一个 Claude Agent Skill：12 个高杠杆思考框架，覆盖 **问清问题 / 学习 / 解决问题 / 决策 / 认识自己** 五个场景。

方法蒸馏自卡兹克《都Agent时代了，我还是想分享给你这12个我最常用的Prompt。》
（<https://mp.weixin.qq.com/s/NAdhdFrUq9-BKelqzqpwBQ>）

## 和直接复制 Prompt 的区别

原文的 12 个 Prompt 是给人复制粘贴用的。这个 Skill 把它们变成 **Claude 自动触发的框架**：
你说"我不知道该选哪个"，Claude 直接开始跑双向钢人论证，而不是回你一段模板。
只有你明确说"把 Prompt 给我"时，才原样输出模板文本。

## 12 个框架

| 你的状态 | 框架 |
|---|---|
| 问题本身是混的，说不清想问什么 | 苏格拉底式提问 |
| 这个概念我完全听不懂 | 双层解释法 |
| 这东西做得真好，我想学它 | 反向拆解 |
| 我想系统搞懂某个领域 | 横纵分析法 |
| 这个说法是真的吗 | 事实核查 |
| 复杂问题，单一视角不够 | 专家会诊 |
| 方案全是补丁，想推倒重来 | 第一性原理 |
| 本行业解法都试过了还是卡 | 跨领域借解 |
| 两个选项都有道理，选不出来 | 双向钢人论证 |
| 想再多也想不清楚了 | 最小实验替代空想 |
| 我到底擅长什么 | 挖掘隐藏天赋 |
| 接下来五年该往哪走 | 人生设计术 |

## 安装

```bash
git clone https://github.com/zdrjson/thinking-prompts-skill.git ~/.claude/skills/thinking-prompts
```

或放进项目的 `.claude/skills/thinking-prompts/`。安装后 Claude 会在匹配场景时自动加载。

## 结构

```
SKILL.md                    分流逻辑 + 执行规则（始终加载）
references/00-sources.md    出处与延伸阅读
references/01-ask.md        问清问题
references/02-learn.md      学习（4 个框架）
references/03-solve.md      解决问题（3 个框架）
references/04-decide.md     决策（2 个框架）
references/05-self.md       认识自己（2 个框架）
```

模板原文版权归原作者卡兹克所有，本仓库仅作整理与 Skill 化。
