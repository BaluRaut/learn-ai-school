# 🗣️ Lesson 08 — Prompting & the context window: the librarian and the small desk

**📍 You are here:** Lesson **08** of 12 — Part 2 begins! · Previous: `lesson-07-rlhf-lora` · Next: `lesson-09-hallucinations`

---

## 📦 What's in this branch

Lessons 01–07, **plus** the two facts that make or break every AI
interaction: **how you ask** (prompting) and **how much fits on the
desk** (the context window).

## 🧒 Explain like I'm 5

**The librarian** 🗣️: walk up and say *"books?"* — you'll get something
random. Say *"I need three beginner-friendly books about volcanoes, for
a 10-year-old, exciting ones, and tell me why you picked each"* — you
get exactly that. Same librarian, wildly different result. The model has
read everything and can imitate anyone; **your prompt decides which of
its thousand modes shows up.** The craft:

- **Say who to be**: "You are a strict code reviewer" (role).
- **Say exactly what you want**: format, length, audience, constraints.
- **Show, don't just tell**: one or two examples of the output you want
  (**few-shot**) beats paragraphs of description.
- **Let it think**: "work step by step, THEN answer" — remember
  lesson 05: each written token conditions the next, so writing the
  reasoning literally builds a ramp to better answers.

**The small desk** 🪑: the librarian is brilliant but the desk holds
only N pages (the **context window** — measured in lesson 03's tokens!).
Everything — your instructions, the conversation so far, pasted
documents, the answer being written — must fit on that ONE desk. Slide a
new page on and an old page slides off (why long chats "forget" the
beginning). And attention (lesson 06) means the middle of a crowded desk
gets skimmed — models recall best what's at the **start and end**.

## 🗺️ Diagram

```mermaid
flowchart TB
    subgraph desk["🪑 the desk - context window, N tokens, that's ALL there is"]
        sys["📜 role + rules - 'be a strict reviewer'"]
        conv["💬 conversation so far - oldest slides off first"]
        doc["📎 pasted docs/examples"]
        ans["✍️ the answer being written - also on the desk!"]
    end
    tips["🗣️ the craft: role · exact ask ·<br/>show examples · let it think first"]
    lost["🕳️ NOT on the desk = does not exist:<br/>no memory between chats,<br/>middle of a crowded desk gets skimmed"]
    tips -->|"1 shapes"| desk
    desk -.->|"2 the catch"| lost
```

## ❓ What

- Message anatomy: **system** (standing rules — strongest seat at the
  desk), **user**, **assistant** turns — all just tokens on the desk.
- Window sizes: ~128k tokens (≈ a 300-page book) is common; long ≠
  infinite, and quality degrades before limits ("lost in the middle").
- There is **no memory between conversations** — "it remembers me" =
  the app quietly re-pasting notes onto the desk each time.
- Prompting is **iteration, not incantation**: change one thing, compare
  outputs, keep what worked. "Prompt engineering" = that loop, done
  honestly.

## 🤔 Why

The cheapest, highest-leverage AI skill: same model, 10× better output,
zero cost. And the desk explains a whole family of mysteries — forgotten
instructions in long chats, degraded answers with huge pastes, why
"summarize then continue" revives a dying conversation, why apps have
system prompts. When output disappoints, ask first: *what was actually
on the desk?*

## 🧪 Try it (in any chatbot — the A/B lab)

```
A: "Write about our new coffee machine."
B: "You are a witty office-newsletter writer. Announce our new coffee
   machine in exactly 3 sentences: one joke, one real detail (it does
   oat milk), one call to action. Tone: friendly, no corporate-speak."
```

Run both. Then test the desk: paste a long article, ask *"what was my
first sentence?"* early and again much later — watch the page slide off.
Finally add "think step by step before answering" to a math question and
compare. Three experiments, three lessons, five minutes.

## ⏭️ Next

Sometimes the perfectly-asked librarian hands you a beautiful,
confident… fabrication. Why models make things up: **hallucinations**.

```bash
git checkout lesson-09-hallucinations
```
