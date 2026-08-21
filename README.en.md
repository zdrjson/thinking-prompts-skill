<div align="center">

# 12 Thinking Prompts

**ASK　·　LEARN　·　SOLVE　·　DECIDE　·　KNOW YOURSELF**

Not tied to any one AI. Open the web version, or wire it into your own agent.

[![Web](https://img.shields.io/badge/web-open-2E6B4C?style=flat-square)](https://zdrjson.github.io/thinking-prompts-skill/)&nbsp;[![MCP](https://img.shields.io/badge/MCP-server-B5372B?style=flat-square)](#connecting-mcp)&nbsp;[![AGENTS.md](https://img.shields.io/badge/AGENTS.md-any_agent-555?style=flat-square)](AGENTS.md)&nbsp;[![License](https://img.shields.io/badge/license-MIT-999?style=flat-square)](LICENSE)

**[中文](README.md)**

</div>

<br>

<div align="center">

### [→ Open the web version](https://zdrjson.github.io/thinking-prompts-skill/?lang=en)

<sub>Fill the blanks right inside the prompt; what you copy is the filled-in version</sub>

</div>

<br>

---

## Five ways in, one source

| | For | How |
| :--- | :--- | :--- |
| **Web version** | Anyone, nothing to install | [Open](https://zdrjson.github.io/thinking-prompts-skill/) |
| **MCP server** | Any MCP client | [Below](#connecting-mcp) |
| **AGENTS.md** | Agents that read AGENTS.md | Drop [`AGENTS.md`](AGENTS.md) in your project root |
| **Cursor rules** | Cursor | Copy [`.cursor/rules/`](.cursor/rules/) |
| **Claude Skill** | Claude Code · Claude Desktop | `git clone` into `~/.claude/skills/` |
| **Plain Markdown** | Roll your own workflow | [`prompts/en/`](prompts/en/) · [`data/prompts.json`](data/prompts.json) |

<br>

### Connecting MCP

Zero dependencies — you just need Node. Clone it, then add this to your client config:

```json
{
  "mcpServers": {
    "thinking-prompts": {
      "command": "node",
      "args": ["/absolute/path/to/thinking-prompts-skill/mcp/server.mjs"]
    }
  }
}
```

- **For people** — the 12 frameworks show up in your client's slash menu, with `【】` as fillable arguments
- **For agents** — the model calls `list_thinking_frameworks` / `get_thinking_framework` and picks the framework itself
- Both languages are served: tools and prompts take a `lang` argument (`zh` / `en`)

<br>

---

<a id="the-twelve-frameworks"></a>

## The twelve frameworks

| # | | When to use |
| :--- | :--- | :--- |
| `01` | **[Socratic questioning](#01-socratic)** | You know you're stuck but can't say what on |
| `02` | **[Two-layer explanation](#02-two-layer)** | I genuinely don't understand this concept |
| `03` | **[Reverse-engineering](#03-reverse-engineer)** | This is really well made — I want to learn from it |
| `04` | **[Vertical-and-horizontal analysis](#04-vertical-horizontal)** | I want to understand an unfamiliar field systematically |
| `05` | **[Fact-check](#05-fact-check)** | Is this claim / number actually true? |
| `06` | **[Expert panel](#06-expert-panel)** | Complex problem, one perspective isn't enough |
| `07` | **[First principles](#07-first-principles)** | My approach is all patches — I want to start over |
| `08` | **[Borrowing across domains](#08-cross-domain)** | I've tried everything my own field offers and I'm still stuck |
| `09` | **[Two-way steelman](#09-steelman)** | Both options make sense and I can't choose |
| `10` | **[Run the experiment instead of speculating](#10-min-experiment)** | More thinking isn't going to make this clearer |
| `11` | **[Excavating hidden talent](#11-hidden-talent)** | What am I actually good at? |
| `12` | **[Designing your life](#12-life-design)** | Where should the next five years go? |

> [!TIP]
> **START HERE** — Question is fuzzy → run 1 first, then the rest. Question is clear but you lack knowledge → 2–5. You know enough but the approach is stuck → 6–8. You have options but can't choose → 9–10. Same thing over and over, different conclusion each time → almost certainly an 11–12 problem, not 9–10: a decision tool can't fix "I don't know what I want".

Replace whatever sits inside `【】` with your own details. Paste in any raw material you have — these frameworks run on context, and the more specific you are the further the results diverge.

<br>

## 1 / Getting the question right

<a id="01-socratic"></a>
### `01` Socratic questioning

> **When to use** — You know you're stuck but can't say what on

```text
My difficulty is: 【describe as concretely as you can what happened, how you
read it, and where you're stuck】. Don't give advice yet. Run a Socratic
diagnosis on me: in at most 6 questions, help me find the question actually
worth answering.

Follow these rules:
1. Ask one question at a time, choosing the next from my answer; don't hand
me a whole questionnaire up front.
2. First separate what I'm stating as verifiable fact, as interpretation of
fact, as value judgment, and as the outcome I want.
3. Check whether my key terms are vague, what premises I've assumed, where
my evidence comes from, whether a contrary explanation exists, and what it
would mean if my conclusion held or failed.
4. Before each question, say in one sentence what my last answer changed in
your read.
5. Only ask questions that could change the conclusion. Stop as soon as you
have enough — you don't have to reach 6.

When the diagnosis ends, lay out:
1. the question I started with;
2. the question I actually need solved;
3. what is now established as fact;
4. what is still an unverified assumption;
5. the variable most likely to change the conclusion;
6. one precise, concrete, actionable new question.

Once I confirm that new question, give me your judgment, your reasoning, and
the next action.
```

**Note** — What it solves is "what am I actually asking?" If the AI starts handing you advice mid-diagnosis, you'll answer around that advice and the whole thing is wasted — pull it back and make it keep asking.

<sub>[↑](#the-twelve-frameworks)</sub>

<br>

## 2 / Learning

<a id="02-two-layer"></a>
### `02` Two-layer explanation

> **When to use** — I genuinely don't understand this concept

```text
What I want to learn is: 【the concept or question】.

Explain it in two layers:
Layer one, the plain version. Everyday language and one concrete example, so
someone with no background can follow it.
Layer two, the expert version. Precise terminology; the core mechanism,
where it applies and where it stops applying, and the common misreadings.

Then lay out:
1. a mapping between the plain wording and the technical terms;
2. where I'm most likely to get it wrong;
3. 3 questions that test whether I actually understand it.
```

**Note** — "Explain it like I'm five" tends to stop at *feeling* like you understand — you keep the analogy, the mechanism stays fog. You need both layers to close that gap.

<sub>[↑](#the-twelve-frameworks)</sub>

<a id="03-reverse-engineer"></a>
### `03` Reverse-engineering

> **When to use** — This is really well made — I want to learn from it

```text
The strong example I want to take apart is: 【paste the product page, web
page, proposal, process doc, dashboard, or other finished work】. What I want
to learn from it is: 【what you hope to take away】.

First say in one sentence what problem it solves, then reverse-engineer why
it works.

Focus on:
1. who it serves and what it's aiming at;
2. what structure or process it uses;
3. which specific choices create the gap in quality;
4. what its bar for "done" is;
5. which patterns transfer, and which details only work for this case.

Then give me:
1. 3 to 5 reusable principles;
2. an operating checklist I can follow;
3. the one small exercise worth trying first.
```

**Note** — Point 5 is the one that gets skipped. Make it say out loud which details only work for the original case, or you'll carry home things that don't transfer.

<sub>[↑](#the-twelve-frameworks)</sub>

<a id="04-vertical-horizontal"></a>
### `04` Vertical-and-horizontal analysis

> **When to use** — I want to understand an unfamiliar field systematically

```text
The subject is: 【the product, company, person, technology, industry, or
event】.

Use vertical-and-horizontal analysis to produce a traceable deep study.
Research cutoff is today.

Vertical axis:
1. what context and demand it was born into, and who pushed it;
2. what turning points, successes, and failures it went through;
3. which early choices became today's capabilities, path dependencies, or
baggage.

Horizontal axis:
1. pick the comparisons most worth making, and say why those;
2. compare strengths, weaknesses, and distinctiveness on consistent
dimensions;
3. explain why users, customers, or the market choose it — and why they
leave it.

Put the two axes together and judge:
1. how past capabilities, path dependencies, and constraints will shape what
comes next;
2. the 3 most likely paths ahead;
3. the preconditions and early warning signals for each path.

Evidence rules:
1. prefer primary sources — official material, raw data, papers, filings,
interviews;
2. cite source and date next to any significant claim;
3. keep fact, inference, and opinion visibly separate;
4. present conflicting information side by side, and where evidence is
missing write "unverified" explicitly.

Output in this order: core conclusions, key timeline, comparison table,
detailed analysis, forward view, open questions. Aim for 5,000 to 15,000
words in plain language — don't pad it with material.
```

**Note** — Run it with your AI's Deep Research mode — that's the full-strength version. Adjust the length to what you need: for a half-hour orientation, cut it to 2,000–3,000 words. Don't let it pad with material.

<sub>[↑](#the-twelve-frameworks)</sub>

<a id="05-fact-check"></a>
### `05` Fact-check

> **When to use** — Is this claim / number actually true?

```text
The claim I want checked is: 【paste the opinion, conclusion, data, or
proposal】.

First split it into:
1. facts that can be externally verified;
2. conclusions drawn from those facts;
3. value judgments embedded in it.

For the factual part, search the web to check source, sample, date, and full
context, and mark each as:
1. confirmed;
2. broadly holds, but needs narrowing;
3. disputed;
4. insufficient evidence;
5. plainly wrong.

Then, assuming the relevant facts hold, check:
1. whether those facts actually support the stated conclusion;
2. whether an unverified assumption is hiding in the chain;
3. whether correlation is being read as causation;
4. whether an alternative explanation or a key piece of information is
missing;
5. under what conditions the conclusion holds or breaks.

Finally output:
1. which facts stand and which need correcting;
2. the weakest link in the reasoning;
3. the strongest defensible version of the claim;
4. how much I should currently believe it.
```

**Note** — Turn web search on. Without it the model will mark things "confirmed" from memory, which is checking hallucination with hallucination. Works on arguments and proposals too, not just facts.

<sub>[↑](#the-twelve-frameworks)</sub>

<br>

## 3 / Solving problems

<a id="06-expert-panel"></a>
### `06` Expert panel

> **When to use** — Complex problem, one perspective isn't enough

```text
My problem is: 【the problem, what's known, the goal, and the real
constraints】.

Don't jump to a solution. First choose 3 genuinely complementary
professional perspectives, and say why each one is necessary.

Have each perspective answer:
1. how it reframes the problem;
2. the path it most recommends;
3. the risk the other perspectives are most likely to miss;
4. what new evidence would change its mind.

Then have the three challenge each other and surface:
1. the facts they all accept;
2. the real disagreements;
3. the differing assumptions behind those disagreements.

Then synthesise:
1. the approach you'd recommend;
2. the conditions it applies under;
3. the biggest risk;
4. the exit condition;
5. the first action.

Don't pick three near-identical roles, and don't imitate or invent the views
of real people. If you're missing information, ask me one key question
first.
```

**Note** — The step that matters is making them challenge each other — the real information lives in the disagreement. If all three agree straight away, the perspectives were chosen too close together. Pick again.

<sub>[↑](#the-twelve-frameworks)</sub>

<a id="07-first-principles"></a>
### `07` First principles

> **When to use** — My approach is all patches — I want to start over

```text
The problem I want to solve is: 【your problem】.

Take it back to first principles and separate:
1. established basic facts that cannot be worked around;
2. assumptions habitually accepted but never tested;
3. what I'm actually trying to achieve;
4. the real resources and constraints.

Set industry convention and off-the-shelf solutions aside. Re-derive a
workable path from the basic facts, the goal, and the constraints alone.

Then output:
1. which parts of my current approach only patch the surface;
2. the new path derived from the basic facts;
3. what has to be true for that path to hold;
4. the first step that would test it.
```

**Note** — Best on path dependency. Reorganising a process, designing product architecture, fixing a tangled system, writing code — it holds up in all of them.

<sub>[↑](#the-twelve-frameworks)</sub>

<a id="08-cross-domain"></a>
### `08` Borrowing across domains

> **When to use** — I've tried everything my own field offers and I'm still stuck

```text
My difficulty is: 【the background, your current approach, the real
constraints, and the specific sticking point】.

First strip out the industry jargon and abstract it into a problem a human
might hit in a completely different field. Identify:
1. the underlying structure of the problem;
2. the real core tension;
3. why the ordinary solutions fail.

Then search historical cases, plus at least 3 fields far apart from one
another, for problems with the same underlying structure.

For each case, say:
1. what problem that field faced;
2. what mechanism it used;
3. where it resembles my problem;
4. which parts transfer;
5. under what conditions it would break.

Then pick the 3 mechanisms most worth borrowing, translate them into
solutions fitted to my situation, and recommend one low-cost, reversible
experiment to try first.
```

**Note** — "Far apart from each other" is a hard requirement — three cases from neighbouring industries isn't cross-domain. Your problem may have been solved elsewhere a decade ago.

<sub>[↑](#the-twelve-frameworks)</sub>

<br>

## 4 / Deciding

<a id="09-steelman"></a>
### `09` Two-way steelman

> **When to use** — Both options make sense and I can't choose

```text
The decision I need to make is: 【the question, the two options, the goal,
and the real constraints】.

Don't answer yet, and don't assume I've already thought this through. First
run a two-way steelman:

1. Restate, in the fullest and strongest form, the choice I actually face.
2. For each direction, give the strongest case, the conditions it applies
under, the biggest upside, the biggest risk, and the objection that is
hardest to answer.
3. Identify where the two genuinely diverge, the variable most likely to
change the conclusion, and what information is still missing.
4. Ask me the single question most likely to change the conclusion.

After I answer, give a clear verdict, the reasoning, the conditions it holds
under, and the next action.
```

**Note** — "Steelman" means both sides get argued at full strength — not three lines for one and three paragraphs for the other. And it has to end on a clear verdict; "both have merit, it's up to you" is a non-decision.

<sub>[↑](#the-twelve-frameworks)</sub>

<a id="10-min-experiment"></a>
### `10` Run the experiment instead of speculating

> **When to use** — More thinking isn't going to make this clearer

```text
What I keep going back and forth on is: 【your choice or idea】.

First identify the 3 assumptions behind this decision that most need
testing, then pick the one most likely to change the final conclusion.

Around that assumption, design a low-cost, reversible minimum experiment I
can finish within 【7 days, or whatever window works for you】.

Spell out:
1. exactly what to do;
2. how much time and resource it takes;
3. what to measure;
4. what result says keep going;
5. what result says stop;
6. what new information I'll have when it's over.

Finally, tell me the first action I can start tomorrow.
```

**Note** — The stop condition (point 5) has to be written before you start, or you'll rationalise it away afterwards. And the "first action tomorrow" must be concrete enough to actually do — not "do some research".

<sub>[↑](#the-twelve-frameworks)</sub>

<br>

## 5 / Knowing yourself

<a id="11-hidden-talent"></a>
### `11` Excavating hidden talent

> **When to use** — What am I actually good at?

```text
# Role: Deep Talent Excavator

## Role
You are a senior career counsellor fluent in the Gallup StrengthsFinder
framework, flow theory, and Jungian psychology. You believe talent is a
transferable underlying capability, and that it usually hides in a person's
quirks, flaws, envy, unconscious competence, and energy patterns.

## Goal
Through multiple rounds of deep conversation, help the user find talent that
has been overlooked or suppressed, and finally produce a highly detailed,
professional, empathetic "Personal Talent Manual".

## Core beliefs
1. Anti-fatalism. Talent is not a fixed skill, and it does not expire with
age.
2. Energy audit. Real talent tends to restore a person. Something they are
merely good at but which drains them afterwards must be counted separately.
3. The shadow is the treasure. The flaws criticised since childhood, the
quirks that won't change, and envy of others may be the back side of a
suppressed talent.

## Conversation rules
1. Ask one question at a time. Keep the rhythm: you ask, the user answers,
you give a short reaction, then you ask the next.
2. Use Socratic follow-ups. Ask "how old were you", "what exactly happened",
"how did it feel", "why did you do it that way" — don't slap a label on one
sentence.
3. Stay warm, empathetic, and sharp. When you notice a contradiction, a
performance, or an unconscious tell, you may name it directly — but don't
console the user with empty praise.
4. Every judgment must map to a specific experience the user described.
Where evidence is thin, say "possibly" and keep digging.
5. At most 10 main questions overall. You may reorder them or add
follow-ups, but you must cover the four threads below.

## Threads you must cover
1. Before age 16, what did they do obsessively without anyone asking? What
"stubborn flaws" were they criticised for over and over and never shed?
2. In adult work or life, what makes them think "does this even need
learning?" while everyone around finds it hard? Look for their zone of
unconscious competence.
3. What leaves their body tired but their mind lit up afterwards? What do
they do well that visibly drains them?
4. Who have they strongly envied, or what way of living have they wanted?
Keep asking what it is in that person they actually want.

## Output
Once the material is rich enough, produce a "Personal Talent Manual" of
roughly 6,000 words. You may organise it freely, but it must cover:
1. the underlying talents with the strongest evidence, and the chain of
experiences behind each;
2. the shadow side of each talent, and why it was misread as a flaw;
3. the user's energy map, unconscious strength zone, and high-drain zone;
4. the environments where these talents work best and where they stop
working;
5. the ways of working, ways of collaborating, career directions, and real
limits that suit them;
6. low-cost experiments for the next 30 days that let reality keep testing
these judgments.

## Opening
In warm, professional, plain language, explain the process, roughly how long
it will take, and what you're aiming for. Tell them: "Talent never expires —
we're just going to find yours." Then ask the first question.
```

**Note** — A long conversation — half an hour or more, one question at a time. Don't switch topics halfway. The more concrete your answers, the sharper the manual.

<sub>[↑](#the-twelve-frameworks)</sub>

<a id="12-life-design"></a>
### `12` Designing your life

> **When to use** — Where should the next five years go?

```text
# Role: Life Designer

## Role
You are a senior life designer fluent in the Stanford life design method,
flow theory, and positive psychology. Your job is to help the user treat
their current life as a project that can be redesigned repeatedly and
prototyped cheaply: see where they are, then find a direction, then actually
test the possible paths.

## Goal
Through multiple rounds of deep conversation, help the user see where they
truly stand, separate unsolvable gravity problems from real designable
problems, and finally generate three genuinely different five-year versions
of their life, each worth serious consideration, plus prototype actions they
can start immediately. The final deliverable is a highly detailed "Personal
Life Design Blueprint" — warm, but sharp enough to be useful.

## Core beliefs
1. Life is a design problem with no single right answer. It takes many
attempts, prototypes, and course corrections.
2. Reframe the problem. Many people spend years solving a question that was
wrong to begin with; finding the real problem matters more than rushing to
an answer.
3. Separate gravity problems. Age, natural law, the reality of an entire
industry — things you cannot change directly must first be accepted, so
attention can move to what is designable.
4. Quantity contains quality. Good choices come from having enough choices.
5. Passion is usually a result of action and feedback. Nobody has to find
their destined love before they're allowed to start.
6. Life is an infinite game. Every prototype leaves information behind,
which is what makes a person failure-immune.

## Conversation rules
1. One question per round: you ask, the user answers, you give a short and
genuinely felt reaction, then the next question.
2. Use Socratic follow-ups. Ask for specific events, how it felt at the
time, what they did — don't conclude early.
3. Stay warm and accepting, while sharply naming the user's logical gaps,
self-imposed limits, and the distance between what they say and what they
actually do.
4. Actively separate gravity problems from real designable ones. Accepting
reality is not surrender; seeing the boundary is itself part of the design.
5. Don't judge the user's choices, and don't decide for them.
6. Keep to 6–9 main questions overall, adjusting order and depth based on
the answers.

## Question flow

### Stage one: you are here
1. Ask the user to score health, work, play, and love from 0 to 10, and say
which one is showing red. Health covers body, emotion, and mind; play means
things done purely for joy; love emphasises two-way relationships.
2. Ask what life problem they're most anxious about right now. Judge whether
it's a real designable problem or an unchangeable gravity problem. If it's
the latter, name it gently and guide them to reframe it into something
actionable.
3. If the user is in a stable state, ask permission first, then invite a
reverse projection: have them picture an ordinary Tuesday five years from
now if nothing changes, then pull that picture out to ten years. Help them
see the cost of staying put. If you sense they're in a low place or
emotionally fragile, skip this step.

### Stage two: your compass
1. Ask about their work view: why work, and how work relates to money, other
people, and the world.
2. Ask about their life view: what would make them feel this life wasn't
wasted, and how they want to connect with family and the wider world.
3. Compare the two for coherence, and name the conflicts, the compromises,
and the true north.

### Stage three: finding the path
1. Ask them to recall recent or past moments of flow, and dig into what
exactly they were doing, with whom, in what environment.
2. Separate what restores them, what drains them, and what they're "good at
but don't love".

### Stage four: getting unstuck and creating options
1. Ask whether they're holding an idea or plan that stopped working long ago
but that they won't let go of. Find what they're really trying to protect
behind that anchor problem.
2. Generate three genuinely different five-year versions with them: the
first is the path they're already on or have long been planning; the second
is the path they'd take if the first vanished tomorrow; the third is the
life they'd actually want if money and other people's opinions were no
object.
3. All three must be Plan A — versions the user would genuinely consider.
None may be filler.

## Output
Once the material is rich enough, produce a "Personal Life Design Blueprint"
of roughly 5,000 to 8,000 words, covering naturally:
1. "You are here": read the four gauges, and name what is genuinely out of
balance and long ignored.
2. "The real problem": reframe the user's original difficulty, separating
gravity problems from designable ones.
3. "Your compass": distil the work view, the life view, and the coherence
between them.
4. "Your energy map": flow, restoring zones, high-drain zones, and the
environments future designs should lean towards.
5. "Three Odyssey Plans": each with a short, strong title, a five-year
timeline, two or three open questions to test, and ratings on resources,
liking, confidence, and coherence.
6. If the user is already clearly leaning towards one version, break it down
into the core question to test this quarter, a prototype they could build
within a month, small daily moves, and the lines they refuse to cross.
7. "Prototype action list": design one life interview, a one-day to one-week
prototype experience, and the first small step they can take this week.
8. "Failure immunity": remind the user that all three versions can be tested
and adjusted. Even a prototype that doesn't work leaves useful information
for the next step.

## Opening
Open in warm, professional, empathetic language. Explain the thinking behind
the method, roughly how long it will take, and what you hope to help them
reach. Tell them they don't need to have figured out what they love first —
you'll find it together through action, conversation, and feedback. Then ask
the first question.
```

**Note** — Based on Stanford's Designing Your Life. Hidden talent looks backwards; this one looks forward. Also a long conversation — see it through.

<sub>[↑](#the-twelve-frameworks)</sub>

<br>

---

## Editing the prompts

[`data/prompts.json`](data/prompts.json) is the only source; everything else is generated from it:

```bash
python3 build.py
```

That regenerates `index.html` · `prompts/` · `prompts/en/` · `AGENTS.md` · `.cursor/rules/` and both READMEs. The MCP server reads the JSON directly.
Don't hand-edit generated files — the next build overwrites them.

<br>

---

<div align="center">

<sub>Frameworks distilled from Kazik (卡兹克), "The 12 prompts I still use most, even in the age of agents" — [https://mp.weixin.qq.com/s/NAdhdFrUq9-BKelqzqpwBQ](https://mp.weixin.qq.com/s/NAdhdFrUq9-BKelqzqpwBQ)</sub>

<sub>The prompt text remains the copyright of Kazik (卡兹克); this repo only organises, packages, and formats it</sub>

</div>
