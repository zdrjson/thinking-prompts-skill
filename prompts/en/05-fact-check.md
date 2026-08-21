---
id: fact-check
n: 5
lang: en
group: Learning
name: Fact-check
---

# Fact-check

**When to use:** Is this claim / number actually true?

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

**Note:** Turn web search on. Without it the model will mark things "confirmed" from memory, which is checking hallucination with hallucination. Works on arguments and proposals too, not just facts.

---
Frameworks distilled from Kazik (卡兹克), "The 12 prompts I still use most, even in the age of agents" — https://mp.weixin.qq.com/s/NAdhdFrUq9-BKelqzqpwBQ
