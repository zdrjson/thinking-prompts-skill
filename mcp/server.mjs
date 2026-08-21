#!/usr/bin/env node
/**
 * 十二个思考 Prompt —— MCP server（零依赖，stdio JSON-RPC）
 *
 * 同时暴露两种面向：
 *   prompts/*  —— 给人用。客户端把 12 个框架列进斜杠菜单，参数就是【】填空位。
 *   tools/*    —— 给 agent 用。让模型自己判断该套哪个框架并取回执行规则。
 *
 * 任何 MCP 客户端都能接：Claude Code / Claude Desktop / Cursor / Cline / Windsurf / Zed / Continue …
 *   { "command": "node", "args": ["<repo>/mcp/server.mjs"] }
 */
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const HERE = dirname(fileURLToPath(import.meta.url));
const D = JSON.parse(readFileSync(join(HERE, '..', 'data', 'prompts.json'), 'utf8'));
const BY_ID = Object.fromEntries(D.prompts.map(p => [p.id, p]));

const L = (x) => (x === 'en' ? 'en' : 'zh');
const G = (p, k, l) => (l === 'en' ? (p[k + '_en'] || p[k]) : p[k]);

const RULES_EN = `Hard rules while running one:
- One question at a time. Conversational frameworks go: you ask, the user answers, you react briefly, then the next question. Firing several at once gets you nothing real.
- Before each follow-up, say in one sentence what the last answer changed in your read.
- Only ask questions that could change the conclusion; stop as soon as you have enough.
- Keep fact, inference, and opinion separate; where evidence is missing, write "unverified".
- When information is missing, ask one key question, not a checklist.`;

const RULES = `执行时的硬规则：
- 一次只问一个问题。对话式框架走"你问 → 用户答 → 简短反馈 → 再问下一题"，一次甩多个问题拿不到真实信息。
- 每次追问前，用一句话说明上一条回答让你更新了什么判断。
- 只问可能改变结论的问题；信息够了立刻停，不必凑满预设题数。
- 事实、推断、观点分开写；找不到证据就明写"暂未核实"。
- 信息不足时只问一个最关键的问题，别列清单。`;

/* 【占位符】→ 参数名 slot1..slotN */
const slotsOf = (p, l) => [...G(p, 'body', l).matchAll(/【([^】]*)】/g)].map((m, i) => ({
  name: `slot${i + 1}`, description: m[1], required: false,
}));

function fill(p, args = {}, l = 'zh') {
  let i = 0;
  return G(p, 'body', l).replace(/【([^】]*)】/g, (_, ph) => {
    const v = args[`slot${++i}`];
    return v && String(v).trim() ? String(v) : `【${ph}】`;
  });
}

const index = (l = 'zh') => D.prompts
  .map(p => `${String(p.n).padStart(2, '0')}  ${p.id.padEnd(20)} ${G(p, 'name', l)} — ${G(p, 'when', l)}`)
  .join('\n');

const LANG_ARG = { type: 'string', enum: ['zh', 'en'], description: 'zh（默认）或 en / zh (default) or en' };

const TOOLS = [
  {
    name: 'list_thinking_frameworks',
    description:
      '列出 12 个思考框架及各自适用的处境。当用户的问题模糊、想搞懂陌生概念、卡在难题、在两个选项间摇摆、'
      + '或想想清楚职业与人生方向时，先调这个挑框架，再用 get_thinking_framework 取正文。',
    inputSchema: { type: 'object', properties: { lang: LANG_ARG } },
  },
  {
    name: 'get_thinking_framework',
    description:
      '按 id 取回某个框架的完整 Prompt 正文、要点和执行规则。取回后请你自己按框架执行，'
      + '而不是把模板原文丢回给用户——除非用户明确说要复制到别的 AI 用。',
    inputSchema: {
      type: 'object',
      properties: {
        id: { type: 'string', enum: D.prompts.map(p => p.id), description: '框架 id / framework id' },
        lang: LANG_ARG,
      },
      required: ['id'],
    },
  },
];

const ok = (id, result) => send({ jsonrpc: '2.0', id, result });
const err = (id, code, message) => send({ jsonrpc: '2.0', id, error: { code, message } });
const send = o => process.stdout.write(JSON.stringify(o) + '\n');
const txt = t => ({ content: [{ type: 'text', text: t }] });

function handle(msg) {
  const { id, method, params = {} } = msg;
  if (id === undefined) return;                       // notification

  switch (method) {
    case 'initialize':
      return ok(id, {
        protocolVersion: params.protocolVersion || '2025-06-18',
        capabilities: { tools: {}, prompts: {} },
        serverInfo: { name: 'thinking-prompts', version: '1.0.0' },
        instructions:
          `12 thinking frameworks, available in English and Chinese (pass lang: "en" | "zh").\n\n`
          + `Routing: ${D.routing_en}\n${RULES_EN}\n\n分流：${D.routing}\n${RULES}`,
      });

    case 'tools/list':
      return ok(id, { tools: TOOLS });

    case 'tools/call': {
      const { name, arguments: a = {} } = params;
      const l = L(a.lang);
      if (name === 'list_thinking_frameworks')
        return ok(id, txt(l === 'en'
          ? `12 thinking frameworks:\n\n${index(l)}\n\nRouting: ${D.routing_en}`
          : `12 个思考框架：\n\n${index(l)}\n\n分流：${D.routing}`));
      if (name === 'get_thinking_framework') {
        const p = BY_ID[a.id];
        if (!p) return ok(id, txt(`No framework with id "${a.id}". Available:\n\n${index(l)}`));
        return ok(id, txt(l === 'en'
          ? `# ${p.name_en} (${p.groupName_en})\n\nWhen to use: ${p.when_en}\n\n## Prompt\n\n${p.body_en}\n\n`
            + `## Note\n\n${p.note_en}\n\n## ${RULES_EN}`
          : `# ${p.name}（${p.groupName}）\n\n什么时候用：${p.when}\n\n## Prompt 正文\n\n${p.body}\n\n`
            + `## 要点\n\n${p.note}\n\n## ${RULES}`));
      }
      return err(id, -32602, `未知工具：${name}`);
    }

    case 'prompts/list':
      return ok(id, {
        prompts: D.prompts.map(p => ({
          name: p.id,
          title: `${p.n}. ${p.name} / ${p.name_en}`,
          description: `${p.when} — ${p.when_en}`,
          arguments: [...slotsOf(p, 'zh'),
            { name: 'lang', description: 'zh (default) or en', required: false }],
        })),
      });

    case 'prompts/get': {
      const p = BY_ID[params.name];
      if (!p) return err(id, -32602, `Unknown framework: ${params.name}`);
      const l = L(params.arguments && params.arguments.lang);
      return ok(id, {
        description: `${G(p, 'name', l)} — ${G(p, 'when', l)}`,
        messages: [{ role: 'user', content: { type: 'text', text: fill(p, params.arguments, l) } }],
      });
    }

    case 'ping':
      return ok(id, {});

    default:
      return err(id, -32601, `未实现的方法：${method}`);
  }
}

let buf = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', chunk => {
  buf += chunk;
  let nl;
  while ((nl = buf.indexOf('\n')) >= 0) {
    const line = buf.slice(0, nl).trim();
    buf = buf.slice(nl + 1);
    if (!line) continue;
    try { handle(JSON.parse(line)); }
    catch (e) { send({ jsonrpc: '2.0', id: null, error: { code: -32700, message: String(e) } }); }
  }
});
process.stdin.on('end', () => process.exit(0));
