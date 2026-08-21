#!/usr/bin/env python3
"""从 data/prompts.json 生成所有接入格式。改 prompt 只改 JSON，然后 python3 build.py。"""
import json, os, re, pathlib

ROOT = pathlib.Path(__file__).parent
D = json.load(open(ROOT/'data/prompts.json', encoding='utf-8'))
P, SRC = D['prompts'], D['source']
ATTR = f"框架蒸馏自{SRC['author']}《{SRC['title']}》 {SRC['url']}"

def w(p, s):
    p = ROOT/p; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding='utf-8'); print(' ', p.relative_to(ROOT))

# ---------- 1. 网页：标准页 + Artifact 版 ----------
tpl = (ROOT/'src/index.template.html').read_text(encoding='utf-8')
page = tpl.replace('__PROMPT_DATA__', json.dumps(D, ensure_ascii=False))
w('dist/artifact.html', page)          # Artifact 由宿主套 head，直接给内容
w('index.html', '<!doctype html>\n<html lang="zh-CN">\n<head>\n<meta charset="utf-8">\n'
  '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
  f'<meta name="description" content="12 个可直接复制的思考 Prompt，任何 AI 都能用。{ATTR}">\n'
  + page.replace('<title>', '<title>', 1) + '\n</html>\n')

# ---------- 2. prompts/：12 个独立 md ----------
for p in P:
    w(f"prompts/{p['n']:02d}-{p['id']}.md",
      f"---\nid: {p['id']}\nn: {p['n']}\ngroup: {p['groupName']}\nname: {p['name']}\n"
      f"when: {p['when']}\n---\n\n# {p['name']}\n\n**什么时候用：** {p['when']}\n\n"
      f"```text\n{p['body']}\n```\n\n**要点：** {p['note']}\n\n---\n{ATTR}\n")

# ---------- 3. AGENTS.md：跨 agent 标准 ----------
rows = '\n'.join(f"| {p['n']} | {p['name']} | {p['when']} | `prompts/{p['n']:02d}-{p['id']}.md` |" for p in P)
w('AGENTS.md', f"""# AGENTS.md

这个仓库是一套**思考框架**，不是一个软件项目。读到这个文件的 agent 请按下面的方式使用它。

## 你要做什么

用户描述一个处境时，先判断它落在哪个框架上，**读取对应文件并按框架执行**，而不是把模板原文丢回给用户。
用户明确说"把 Prompt 给我 / 我要复制到别的 AI 用"时，才原样输出模板。

| # | 框架 | 什么时候用 | 文件 |
|---|---|---|---|
{rows}

## 分流

{D['routing']}

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
{ATTR}
""")

# ---------- 4. Cursor rules ----------
w('.cursor/rules/thinking-prompts.mdc',
  f"---\ndescription: 12 个思考框架：问清问题/学习/解决问题/决策/认识自己。用户问题模糊、想搞懂陌生概念、卡在难题、在两个选项间摇摆时使用。\nalwaysApply: false\n---\n\n"
  + (ROOT/'AGENTS.md').read_text(encoding='utf-8'))

# ---------- 5. Claude Skill 的 references 保持与 JSON 同步（校验用） ----------
missing = [p['id'] for p in P if p['body'] not in (ROOT/'references').joinpath(
    {1:'01-ask.md',2:'02-learn.md',3:'03-solve.md',4:'04-decide.md',5:'05-self.md'}[p['group']]
).read_text(encoding='utf-8').replace('> ','').replace('\n>','\n')]
print('  skill references 同步检查：', '全部一致' if not missing else f'不一致 {missing}')

# ---------- 6. README ----------
PAGES = "https://zdrjson.github.io/thinking-prompts-skill/"
toc = []
for g in sorted({p['group'] for p in P}):
    gs = [p for p in P if p['group']==g]
    toc.append(f"**{g}、{gs[0]['groupName']}**\n" + "\n".join(
        f"{p['n']}. [{p['name']}](#{p['n']}-{p['id']}) —— {p['when']}" for p in gs))
secs = []
last = None
for p in P:
    if p['group'] != last:
        secs.append(f"\n---\n\n# {p['group']}、{p['groupName']}\n")
        last = p['group']
    secs.append(f"## {p['n']}. {p['name']}\n\n**什么时候用：** {p['when']}\n\n"
                f"```text\n{p['body']}\n```\n\n**要点：** {p['note']}\n")

w('README.md', f"""# 12 个思考 Prompt

覆盖 **问清问题 / 学习 / 解决问题 / 决策 / 认识自己**。不绑定任何一家 AI —— 网页直接用，或者接进你自己的 agent。

**[→ 打开网页版]({PAGES})**　填空直接在 Prompt 正文里填，复制出去的是填好的版本。

## 五种接法，同一份源

| 方式 | 给谁 | 怎么接 |
|---|---|---|
| **网页版** | 任何人，零安装 | [{PAGES}]({PAGES}) |
| **MCP server** | 任何 MCP 客户端<br>Claude Code / Claude Desktop / Cursor / Cline / Windsurf / Zed / Continue… | 见下方 |
| **AGENTS.md** | 读 AGENTS.md 的 agent<br>Codex / Cursor / Zed / Amp… | 把 `AGENTS.md` 放进项目根目录 |
| **Cursor rules** | Cursor | 复制 `.cursor/rules/thinking-prompts.mdc` |
| **Claude Skill** | Claude Code / Claude Desktop | `git clone … ~/.claude/skills/thinking-prompts` |
| **裸 Markdown** | 自己拼工作流 | `prompts/*.md`、`data/prompts.json` |

### 接 MCP

零依赖，只要有 Node。克隆后在客户端配置里加一段：

```json
{{
  "mcpServers": {{
    "thinking-prompts": {{
      "command": "node",
      "args": ["/绝对路径/thinking-prompts-skill/mcp/server.mjs"]
    }}
  }}
}}
```

接上以后有两个面向：12 个框架会出现在客户端的斜杠/提示菜单里（`【】` 变成可填参数），
同时 agent 自己也能调 `list_thinking_frameworks` / `get_thinking_framework` 判断该套哪个框架。

---

## 目录

{chr(10).join(chr(10)+t for t in toc)}

> **先分流：** {D['routing']}

用的时候把 `【】` 里的内容换成你自己的信息。手头有原始材料就一起贴上去 —— 这些框架吃上下文，说得越具体，结果差得越远。
{''.join(secs)}
---

# 改 Prompt

`data/prompts.json` 是唯一的源，其余全部由它生成：

```bash
python3 build.py
```

会重新吐出 `index.html`、`prompts/*.md`、`AGENTS.md`、`.cursor/rules/`、`README.md`，MCP server 直接读 JSON。
别手改生成物，下次 build 会覆盖。

---

{ATTR}

Prompt 原文版权归原作者{SRC['author']}所有，本仓库仅作整理、跨平台封装与可复制排版。
""")
