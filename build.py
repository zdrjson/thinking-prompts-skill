#!/usr/bin/env python3
"""从 data/prompts.json 生成所有接入格式（中英双语）。
改 prompt 只改 JSON，然后 python3 build.py。别手改生成物。"""
import json, pathlib

ROOT = pathlib.Path(__file__).parent
D = json.load(open(ROOT / 'data/prompts.json', encoding='utf-8'))
P, SRC = D['prompts'], D['source']
PAGES = "https://zdrjson.github.io/thinking-prompts-skill/"

ATTR = {'zh': f"框架蒸馏自{SRC['author']}《{SRC['title']}》 {SRC['url']}",
        'en': f"Frameworks distilled from {SRC['author_en']}, \"{SRC['title_en']}\" — {SRC['url']}"}
F = lambda p, k, lang: p[k + '_en'] if lang == 'en' else p[k]


def w(p, s):
    p = ROOT / p; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding='utf-8'); print(' ', p.relative_to(ROOT))


def md_wrap(body, lang):
    """只给 Markdown 代码块用：软折行，避免 GitHub 上要横向拖动。
    网页版是 white-space:pre-wrap 自己会折，源数据不动。"""
    limit, breaks = (76, ' ') if lang == 'en' else (48, '。；，、：!?！？')
    out = []
    for line in body.split('\n'):
        while len(line) > limit:
            cut = max((line.rfind(c, 0, limit + 1) for c in breaks), default=-1)
            if cut < limit // 2: cut = limit - 1
            out.append(line[:cut + 1].rstrip()); line = line[cut + 1:].lstrip()
        out.append(line)
    return '\n'.join(out)


# ---------- 1. 网页 ----------
tpl = (ROOT / 'src/index.template.html').read_text(encoding='utf-8')
page = tpl.replace('__PROMPT_DATA__', json.dumps(D, ensure_ascii=False))
w('dist/artifact.html', page)                      # Artifact 由宿主套 head

cut = page.index('<header')                        # 独立页需要完整文档结构
w('index.html',
  '<!doctype html>\n<html lang="zh-CN">\n<head>\n<meta charset="utf-8">\n'
  '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
  f'<meta name="description" content="12 reusable thinking prompts, in English and Chinese. '
  f'Nothing to install — works with any AI. {ATTR["en"]}">\n'
  + page[:cut].rstrip() + '\n</head>\n<body>\n' + page[cut:].rstrip() + '\n</body>\n</html>\n')

# ---------- 2. prompts/ 单条 md ----------
LBL = {'zh': ('什么时候用', '要点'), 'en': ('When to use', 'Note')}
for lang in ('zh', 'en'):
    for p in P:
        when, note = LBL[lang]
        w(f"prompts/{'' if lang=='zh' else 'en/'}{p['n']:02d}-{p['id']}.md",
          f"---\nid: {p['id']}\nn: {p['n']}\nlang: {lang}\ngroup: {F(p,'groupName',lang)}\n"
          f"name: {F(p,'name',lang)}\n---\n\n# {F(p,'name',lang)}\n\n"
          f"**{when}:** {F(p,'when',lang)}\n\n```text\n{md_wrap(F(p,'body',lang), lang)}\n```\n\n"
          f"**{note}:** {F(p,'note',lang)}\n\n---\n{ATTR[lang]}\n")

# ---------- 3. AGENTS.md（英文优先，附中文） ----------
rows = lambda lang, d: '\n'.join(
    f"| {p['n']} | {F(p,'name',lang)} | {F(p,'when',lang)} | `prompts/{d}{p['n']:02d}-{p['id']}.md` |" for p in P)
w('AGENTS.md', f"""# AGENTS.md

This repo is a set of **thinking frameworks**, not a software project. If you are an agent reading this file, use it as follows.

## What to do

When the user describes a situation, work out which framework it lands on, **read that file and run the framework**, rather than handing the template text back to them.
Only output the raw template when the user explicitly asks for it ("give me the prompt", "I want to paste it into another AI").

| # | Framework | When to use | File |
|---|---|---|---|
{rows('en','en/')}

## Routing

{D['routing_en']}

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
{rows('zh','')}

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
{ATTR['en']}
""")

# ---------- 4. Cursor rules ----------
w('.cursor/rules/thinking-prompts.mdc',
  "---\ndescription: 12 thinking frameworks (EN/中文) for clarifying vague questions, learning unfamiliar "
  "things, breaking through stuck problems, making hard decisions, and self-discovery. "
  "12 个思考框架：问清问题/学习/解决问题/决策/认识自己。\nalwaysApply: false\n---\n\n"
  + (ROOT / 'AGENTS.md').read_text(encoding='utf-8'))

# ---------- 5. README（中英各一份） ----------
COPY = {
 'zh': dict(file='README.md', other='README.en.md', otherlbl='English',
   sub='**问清问题　·　学习　·　解决问题　·　决策　·　认识自己**',
   lede='不绑定任何一家 AI。打开网页就能用，也能接进你自己的 agent。',
   openweb='→ 打开网页版', opensub='填空直接在 Prompt 正文里填，复制出去的是填好的版本',
   ways='五种接法，同一份源', w1='给谁', w2='怎么接',
   r_web=('网页版','任何人，零安装','[打开]'), r_mcp=('MCP server','任何 MCP 客户端','[见下方](#接-mcp)'),
   r_ag=('AGENTS.md','读 AGENTS.md 的 agent','把 [`AGENTS.md`](AGENTS.md) 放进项目根目录'),
   r_cur=('Cursor rules','Cursor','复制 [`.cursor/rules/`](.cursor/rules/)'),
   r_sk=('Claude Skill','Claude Code · Claude Desktop','`git clone` 进 `~/.claude/skills/`'),
   r_md=('裸 Markdown','自己拼工作流','[`prompts/`](prompts/) · [`data/prompts.json`](data/prompts.json)'),
   mcp='接 MCP', mcplede='零依赖，只要有 Node。克隆下来，在客户端配置里加一段：',
   mcpa='**给人** — 12 个框架出现在客户端的斜杠菜单里，`【】` 变成可填参数',
   mcpb='**给 agent** — 模型自己调 `list_thinking_frameworks` / `get_thinking_framework`，判断该套哪个框架',
   mcpc='两种语言都在：工具和提示都接受 `lang` 参数（`zh` / `en`）',
   anchor='十二个框架', idx='十二个框架', h_when='什么时候用', route='先分流',
   fill='用的时候把 `【】` 里的内容换成你自己的信息。手头有原始材料就一起贴上去 —— 这些框架吃上下文，说得越具体，结果差得越远。',
   edit='改 Prompt', editlede='[`data/prompts.json`](data/prompts.json) 是唯一的源，其余全部由它生成：',
   editnote='重新吐出 `index.html` · `prompts/` · `prompts/en/` · `AGENTS.md` · `.cursor/rules/` · 两份 README，MCP server 直接读 JSON。\n别手改生成物，下次 build 会覆盖。',
   note='要点', foot2=f"Prompt 原文版权归原作者{SRC['author']}所有，本仓库仅作整理、跨平台封装与可复制排版"),
 'en': dict(file='README.en.md', other='README.md', otherlbl='中文',
   sub='**ASK　·　LEARN　·　SOLVE　·　DECIDE　·　KNOW YOURSELF**',
   lede='Not tied to any one AI. Open the web version, or wire it into your own agent.',
   openweb='→ Open the web version', opensub='Fill the blanks right inside the prompt; what you copy is the filled-in version',
   ways='Five ways in, one source', w1='For', w2='How',
   r_web=('Web version','Anyone, nothing to install','[Open]'), r_mcp=('MCP server','Any MCP client','[Below](#connecting-mcp)'),
   r_ag=('AGENTS.md','Agents that read AGENTS.md','Drop [`AGENTS.md`](AGENTS.md) in your project root'),
   r_cur=('Cursor rules','Cursor','Copy [`.cursor/rules/`](.cursor/rules/)'),
   r_sk=('Claude Skill','Claude Code · Claude Desktop','`git clone` into `~/.claude/skills/`'),
   r_md=('Plain Markdown','Roll your own workflow','[`prompts/en/`](prompts/en/) · [`data/prompts.json`](data/prompts.json)'),
   mcp='Connecting MCP', mcplede='Zero dependencies — you just need Node. Clone it, then add this to your client config:',
   mcpa='**For people** — the 12 frameworks show up in your client\'s slash menu, with `【】` as fillable arguments',
   mcpb='**For agents** — the model calls `list_thinking_frameworks` / `get_thinking_framework` and picks the framework itself',
   mcpc='Both languages are served: tools and prompts take a `lang` argument (`zh` / `en`)',
   anchor='the-twelve-frameworks', idx='The twelve frameworks', h_when='When to use', route='START HERE',
   fill='Replace whatever sits inside `【】` with your own details. Paste in any raw material you have — these frameworks run on context, and the more specific you are the further the results diverge.',
   edit='Editing the prompts', editlede='[`data/prompts.json`](data/prompts.json) is the only source; everything else is generated from it:',
   editnote='That regenerates `index.html` · `prompts/` · `prompts/en/` · `AGENTS.md` · `.cursor/rules/` and both READMEs. The MCP server reads the JSON directly.\nDon\'t hand-edit generated files — the next build overwrites them.',
   note='Note', foot2=f"The prompt text remains the copyright of {SRC['author_en']}; this repo only organises, packages, and formats it")}

BADGE = ("[![Web](https://img.shields.io/badge/web-open-2E6B4C?style=flat-square)](%s)"
 "&nbsp;[![MCP](https://img.shields.io/badge/MCP-server-B5372B?style=flat-square)](#%s)"
 "&nbsp;[![AGENTS.md](https://img.shields.io/badge/AGENTS.md-any_agent-555?style=flat-square)](AGENTS.md)"
 "&nbsp;[![License](https://img.shields.io/badge/license-MIT-999?style=flat-square)](LICENSE)")

for lang, c in COPY.items():
    gnames = {g: next(F(p,'groupName',lang) for p in P if p['group']==g) for g in sorted({p['group'] for p in P})}
    toc = "\n".join(f"| `{p['n']:02d}` | **[{F(p,'name',lang)}](#{p['n']:02d}-{p['id']})** | {F(p,'when',lang)} |" for p in P)
    secs, last = [], None
    for p in P:
        if p['group'] != last:
            last = p['group']; secs.append(f"\n<br>\n\n## {p['group']} / {gnames[p['group']]}\n")
        secs.append(f"\n<a id=\"{p['n']:02d}-{p['id']}\"></a>\n### `{p['n']:02d}` {F(p,'name',lang)}\n\n"
                    f"> **{c['h_when']}** — {F(p,'when',lang)}\n\n"
                    f"```text\n{md_wrap(F(p,'body',lang), lang)}\n```\n\n"
                    f"**{c['note']}** — {F(p,'note',lang)}\n\n<sub>[↑](#{c['anchor']})</sub>\n")
    rw = lambda r, how=None: f"| **{r[0]}** | {r[1]} | {how or r[2]} |"
    w(c['file'], f"""<div align="center">

# {D['title_en'] if lang=='en' else '12 个思考 Prompt'}

{c['sub']}

{c['lede']}

{BADGE % (PAGES, c['mcp'].lower().replace(' ','-'))}

**[{c['otherlbl']}]({c['other']})**

</div>

<br>

<div align="center">

### [{c['openweb']}]({PAGES}{'?lang=en' if lang=='en' else ''})

<sub>{c['opensub']}</sub>

</div>

<br>

---

## {c['ways']}

| | {c['w1']} | {c['w2']} |
| :--- | :--- | :--- |
{rw(c['r_web'], f"[{c['r_web'][2][1:-1]}]({PAGES})")}
{rw(c['r_mcp'])}
{rw(c['r_ag'])}
{rw(c['r_cur'])}
{rw(c['r_sk'])}
{rw(c['r_md'])}

<br>

### {c['mcp']}

{c['mcplede']}

```json
{{
  "mcpServers": {{
    "thinking-prompts": {{
      "command": "node",
      "args": ["/absolute/path/to/thinking-prompts-skill/mcp/server.mjs"]
    }}
  }}
}}
```

- {c['mcpa']}
- {c['mcpb']}
- {c['mcpc']}

<br>

---

<a id="{c['anchor']}"></a>

## {c['idx']}

| # | | {c['h_when']} |
| :--- | :--- | :--- |
{toc}

> [!TIP]
> **{c['route']}** — {D['routing_en'] if lang=='en' else D['routing']}

{c['fill']}
{''.join(secs)}
<br>

---

## {c['edit']}

{c['editlede']}

```bash
python3 build.py
```

{c['editnote']}

<br>

---

<div align="center">

<sub>{ATTR[lang].rsplit(' ',1)[0] if lang=='en' else f"框架蒸馏自{SRC['author']}《[{SRC['title']}]({SRC['url']})》"}{f" [{SRC['url']}]({SRC['url']})" if lang=='en' else ''}</sub>

<sub>{c['foot2']}</sub>

</div>
""")

# ---------- 6. Claude Skill（SKILL.md 直接指向 prompts/，不再另存一份副本） ----------
skill_rows = '\n'.join(
    f"| {F(p,'when','zh')}<br><sub>{F(p,'when','en')}</sub> | {F(p,'name','zh')} | `prompts/{p['n']:02d}-{p['id']}.md`<br><sub>`prompts/en/{p['n']:02d}-{p['id']}.md`</sub> |"
    for p in P)
w('SKILL.md', f"""---
name: thinking-prompts
description: "12 个高杠杆思考框架（中英双语）：问清问题（苏格拉底问诊）、学习（双层解释/反向拆解/横纵分析/事实核查）、解决问题（专家会诊/第一性原理/跨领域借解）、决策（双向钢人论证/最小实验）、认识自己（挖掘天赋/人生设计）。当用户的问题模糊、想搞懂陌生概念、卡在难题、在两个选项间摇摆、或想想清楚职业与人生方向时使用。Twelve reusable thinking frameworks in English and Chinese, for clarifying vague questions, learning unfamiliar things, breaking through stuck problems, making hard decisions, and self-discovery."
---

# 12 个思考 Prompt

{ATTR['zh']}

**核心用法：你自己按框架跑，而不是把模板丢回给用户。** 用户说"我不知道该选哪个"时，直接开始双向钢人论证，不要回一段"你可以用这个 Prompt"。只有用户明确说"把 Prompt 给我 / 我要复制到别的 AI 用"时，才原样输出模板正文。

**语言**：用户说中文就读 `prompts/`，说英文读 `prompts/en/`。两边是同一套框架。

## 先判断用户在哪一类，再取对应文件

| 用户的状态 | 框架 | 文件 |
|---|---|---|
{skill_rows}

一次只加载 1 个文件。用户的提问经常跨两类（比如"我该不该转行"既是决策也是认识自己），按他此刻最卡的那一步选。

## 用之前先分流

{D['routing']}

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
""")
