#!/usr/bin/env python3
"""Generate the learn-ai-school docs site: index, lesson-diagrams, before-and-tradeoffs, study-plan."""
GH = "https://github.com/BaluRaut/learn-ai-school/blob"
SITE = "https://baluraut.github.io/learn-ai-school/"
VIDEO = "https://www.youtube.com/watch?v=nVnxG10D5W0"
P1, P2 = "#7c3aed", "#0d9488"

L = [  # num, slug, folder, title, analogy, minutes, color
 (1,"lesson-01-what-is-ai","01-what-is-ai","📖 What is AI","Rulebooks vs learning from examples — the rules are grown, not written.",40,P1),
 (2,"lesson-02-training","02-training","✏️ Training","Practice tests + the red pen — loss and tiny downhill nudges.",40,P1),
 (3,"lesson-03-tokens","03-tokens","🧩 Tokens","Cutting text into puzzle pieces — why 'strawberry' is hard.",35,P1),
 (4,"lesson-04-embeddings","04-embeddings","🗺️ Embeddings","The seating chart of meanings — similar words sit together.",40,P1),
 (5,"lesson-05-next-token","05-next-token","🎲 Next-token prediction","The sentence-completion game, with a temperature dial.",40,P1),
 (6,"lesson-06-attention","06-attention","👀 Attention","Kids glancing around the class — who does 'it' refer to?",45,P1),
 (7,"lesson-07-rlhf-lora","07-rlhf-lora","⭐ RLHF &amp; LoRA","Library, etiquette class, gold stars — and sticky notes.",45,P1),
 (8,"lesson-08-prompting-context","08-prompting-context","🗣️ Prompting &amp; context","How you ask the librarian — and the small desk it fits on.",40,P2),
 (9,"lesson-09-hallucinations","09-hallucinations","🙋 Hallucinations","The confident kid who never says 'I don't know'.",35,P2),
 (10,"lesson-10-rag","10-rag","📖 RAG","The open-book exam, automated with the seating chart.",45,P2),
 (11,"lesson-11-agents","11-agents","📋 Agents &amp; tools","A student with a to-do list and a hall pass.",45,P2),
 (12,"lesson-12-diffusion","12-diffusion","📺 Diffusion &amp; multimodal","Un-blurring TV static, step by step, toward your words.",40,P2),
 (13,"lesson-13-mcp","13-mcp","🔌 Bonus: MCP","The universal plug — deep-dive course: <a href=\"https://baluraut.github.io/learn-mcp-school/\">learn-mcp-school</a> 🔌",40,P2),
]

BASE_CSS = """
  :root { --bg:#f8fafc; --card:#fff; --ink:#0f172a; --muted:#475569; --line:#e2e8f0; --accent:#7c3aed; --ok:#16a34a; --blue:#2563eb; --bad:#dc2626; }
  @media (prefers-color-scheme: dark) { :root { --bg:#0b1220; --card:#131c2e; --ink:#e2e8f0; --muted:#94a3b8; --line:#253349; } }
  * { margin:0; padding:0; box-sizing:border-box; }
  body { background:var(--bg); color:var(--ink); font-family:-apple-system,"Segoe UI",Helvetica,Arial,sans-serif; line-height:1.6; }
  .wrap { max-width:1280px; margin:0 auto; padding:28px 20px 60px; }
  @media (min-width: 1660px) { .wrap { max-width: 1580px; } }
  a { color:var(--blue); } h1 { font-size:2rem; line-height:1.25; } h2 { font-size:1.4rem; margin:44px 0 6px; }
  .sub { color:var(--muted); max-width:74ch; }
  .chips { display:flex; flex-wrap:wrap; gap:8px; margin:16px 0 8px; }
  .chip { border:1px solid var(--line); background:var(--card); border-radius:999px; padding:6px 14px; font-size:.85rem; color:var(--muted); }
  .grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(240px,1fr)); gap:14px; margin-top:16px; }
  .lesson { background:var(--card); border:1px solid var(--line); border-top:5px solid var(--c,var(--accent)); border-radius:14px; padding:16px; display:flex; flex-direction:column; gap:6px; }
  .lesson .top { display:flex; align-items:center; gap:10px; }
  .lesson .num { flex:none; width:30px; height:30px; border-radius:50%; background:var(--c,var(--accent)); color:#fff; display:inline-flex; align-items:center; justify-content:center; font-weight:800; font-size:.9rem; }
  .lesson h3 { font-size:1.02rem; line-height:1.3; } .lesson .ana { color:var(--muted); font-size:.9rem; }
  .lesson code { font-size:.78rem; background:var(--bg); border:1px solid var(--line); border-radius:6px; padding:1px 6px; }
  .lesson a.go { margin-top:auto; font-weight:600; font-size:.9rem; text-decoration:none; } .lesson a.go+a.go { margin-top:0; } .lesson a.go:hover { text-decoration:underline; }
  .callout { background:var(--card); border:1px solid var(--line); border-left:6px solid var(--ok); border-radius:14px; padding:18px 20px; margin-top:16px; }
  pre { background:var(--card); border:1px solid var(--line); border-radius:12px; padding:14px 16px; overflow-x:auto; font-size:.88rem; margin-top:12px; }
  .btn { display:inline-block; background:var(--accent); color:#fff; border-radius:10px; padding:10px 18px; text-decoration:none; font-weight:700; margin:14px 10px 0 0; }
  .btn.alt { background:transparent; color:var(--ink); border:1px solid var(--line); }
  .vs { display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:14px; margin-top:16px; }
  .vcol { background:var(--card); border:1px solid var(--line); border-radius:14px; padding:18px; } .vcol h3 { margin-bottom:8px; }
  .vcol ul { margin-left:18px; color:var(--muted); font-size:.93rem; }
  footer { margin-top:56px; border-top:1px solid var(--line); padding-top:18px; color:var(--muted); font-size:.88rem; }
"""
DSEC_CSS = """
  .dsec { background:var(--card); border:1px solid var(--line); border-top:6px solid var(--c,var(--accent)); border-radius:16px; padding:22px 22px 16px; margin-top:26px; scroll-margin-top:16px; }
  .dsec h2 { font-size:1.25rem; display:flex; align-items:center; gap:10px; }
  .dsec h2 .ln { flex:none; width:32px; height:32px; border-radius:50%; background:var(--c,var(--accent)); color:#fff; display:inline-flex; align-items:center; justify-content:center; font-size:.95rem; font-weight:800; }
  .dsec p.d { color:var(--muted); font-size:.95rem; margin:6px 0 4px; }
  .dsec svg { width:100%; height:auto; display:block; margin-top:10px; } .dsec .foot { margin-top:8px; font-size:.92rem; }
  .box { fill:var(--card); stroke:var(--c,var(--accent)); stroke-width:2; }
  .soft { fill:var(--bg); stroke:var(--line); stroke-width:1.5; }
  .dead { fill:var(--bg); stroke:var(--muted); stroke-width:1.5; stroke-dasharray:6 5; }
  .t { font:600 14px -apple-system,"Segoe UI",sans-serif; fill:var(--ink); }
  .s { font:12px -apple-system,"Segoe UI",sans-serif; fill:var(--muted); } .m { text-anchor:middle; }
  .arr { stroke:#64748b; stroke-width:2; fill:none; marker-end:url(#arw); } .dash { stroke-dasharray:6 5; }
  .nc { fill:var(--c,var(--accent)); } .nt { font:700 12px -apple-system,sans-serif; fill:#fff; text-anchor:middle; }
"""
MARKER = '<svg width="0" height="0" style="position:absolute"><defs><marker id="arw" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#64748b"/></marker></defs></svg>'
TOC_CSS = """
  .toc { display:flex; flex-wrap:wrap; gap:8px; margin:18px 0 6px; }
  .toc a { border:1px solid var(--line); background:var(--card); border-radius:999px; padding:5px 12px; font-size:.82rem; color:var(--muted); text-decoration:none; }
  .toc a:hover { color:var(--ink); border-color:var(--muted); }
"""

def head(title, desc, extra=""):
    return (f'<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
      f'<meta name="viewport" content="width=device-width, initial-scale=1">\n<title>{title}</title>\n'
      f'<meta name="description" content="{desc}">\n<meta property="og:title" content="{title}">\n<meta property="og:description" content="{desc}">\n<meta property="og:image" content="https://baluraut.github.io/learn-ai-school/images/big-picture-4k.png">\n<meta property="og:type" content="website">\n<meta name="twitter:card" content="summary_large_image">\n<style>{BASE_CSS}{extra}</style>\n</head>\n<body>\n')

B='<rect class="box"'; S='<rect class="soft"'; D='<rect class="dead"'; DASH=' dash'
def t(x,y,s): return f'<text class="t m" x="{x}" y="{y}">{s}</text>'
def sm(x,y,s): return f'<text class="s m" x="{x}" y="{y}">{s}</text>'
def num(x,y,n): return f'<g transform="translate({x},{y})"><circle r="11" class="nc"/><text class="nt" dy="4">{n}</text></g>'
def arr(a,b,c,d,dash=""): return f'<line class="arr{dash}" x1="{a}" y1="{b}" x2="{c}" y2="{d}"/>'

SVG = {}
SVG[1]=(f'{D} x="40" y="50" width="250" height="100" rx="12"/>{t(165,85,"📜 the rulebook way")}{sm(165,110,"if ears AND whiskers AND tail…")}{sm(165,132,"rule #41 breaks on cartoon cats 💥")}'
 f'{B} x="40" y="180" width="250" height="90" rx="12"/>{t(165,212,"🐱 the examples way")}{sm(165,236,"10,000 photos: cat / not-cat")}'
 f'{B} x="390" y="180" width="200" height="90" rx="12"/>{t(490,212,"✏️ training")}{sm(490,236,"rules GROW inside")}'
 f'{B} x="660" y="180" width="250" height="90" rx="12"/>{t(785,212,"🧠 model")}{sm(785,236,"answers even for NEW cats")}'
 f'{arr(290,225,386,225)}{num(338,208,1)}{arr(590,225,656,225)}{num(623,208,2)}'
 f'{arr(165,150,165,176,DASH)}{sm(470,290,"AI ⊃ machine learning ⊃ deep learning ⊃ LLMs — this course walks inward")}{num(120,290,3)}')
SVG[2]=(f'{B} x="40" y="90" width="200" height="90" rx="12"/>{t(140,122,"📚 examples")}{sm(140,146,"question + true answer")}'
 f'{B} x="310" y="90" width="180" height="90" rx="12"/>{t(400,122,"🧠 model")}{sm(400,146,"millions of dials")}'
 f'{B} x="560" y="90" width="160" height="90" rx="12"/>{t(640,122,"✍️ prediction")}'
 f'{B} x="780" y="90" width="130" height="90" rx="12"/>{t(845,122,"🔴 loss")}{sm(845,146,"HOW wrong?")}'
 f'{arr(240,135,306,135)}{arr(490,135,556,135)}{num(523,118,1)}{arr(720,135,776,135)}'
 f'{B} x="310" y="220" width="420" height="60" rx="12"/>{t(520,245,"⛰️ gradient descent: nudge EVERY dial slightly downhill")}'
 f'{arr(845,180,700,218)}{num(772,205,2)}{arr(310,250,400,184,DASH)}{sm(300,210,"repeat millions of times")}'
 f'{sm(470,297,"🧪 validation set = unseen questions — catches memorizers (overfitting)")}{num(150,297,3)}')
SVG[3]=(f'{B} x="40" y="100" width="220" height="90" rx="12"/>{t(150,132,"📝 text")}{sm(150,158,"&#39;the robot reads&#39;")}'
 f'{B} x="330" y="100" width="250" height="90" rx="12"/>{t(455,128,"🧩 tokenizer - BPE")}{sm(455,152,"glue the most frequent pair,")}{sm(455,174,"repeat thousands of times")}'
 f'{B} x="650" y="100" width="180" height="90" rx="12"/>{t(740,132,"🔢 token IDs")}{sm(740,158,"[464, 9379, 9743]")}'
 f'{arr(260,145,326,145)}{num(293,128,1)}{arr(580,145,646,145)}{num(613,128,2)}'
 f'{S} x="90" y="230" width="760" height="55" rx="10"/>{sm(470,253,"the model sees ONLY these pieces — never words, never letters:")}{sm(470,275,"why &#39;how many R&#39;s in strawberry&#39; is hard 🍓 · why pricing is per-token · why some languages cost 3×")}{num(90,230,3)}')
SVG[4]=(f'{B} x="40" y="100" width="180" height="90" rx="12"/>{t(130,132,"🧩 token &#39;cat&#39;")}'
 f'{B} x="290" y="100" width="240" height="90" rx="12"/>{t(410,128,"🗺️ its seat coordinates")}{sm(410,152,"[0.31, -1.2, 0.88, …] ×768")}{sm(410,174,"learned, not drawn")}'
 f'{S} x="600" y="40" width="310" height="220" rx="14"/>{t(755,70,"the seating hall - meaning space")}'
 f'{B} x="630" y="90" width="110" height="50" rx="10"/>{sm(685,120,"cat 🐱")}'
 f'{B} x="760" y="90" width="120" height="50" rx="10"/>{sm(820,120,"kitten")}'
 f'{B} x="690" y="150" width="110" height="50" rx="10"/>{sm(745,180,"dog 🐶")}'
 f'{D} x="760" y="205" width="130" height="45" rx="10"/>{sm(825,232,"📎 stapler - far")}'
 f'{arr(220,145,286,145)}{num(253,128,1)}{arr(530,145,596,145)}{num(563,128,2)}'
 f'{sm(300,250,"distance = similarity →")}{sm(300,272,"semantic search, RAG (L10), king−man+woman≈queen 👑")}{num(150,261,3)}')
SVG[5]=(f'{B} x="40" y="90" width="220" height="90" rx="12"/>{t(150,122,"📝 pieces so far")}{sm(150,148,"&#39;The dog chased the&#39;")}'
 f'{B} x="330" y="70" width="250" height="130" rx="12"/>{t(455,100,"📊 scoreboard over ALL pieces")}{sm(455,126,"cat 24% · ball 17% · car 9%")}{sm(455,148,"… stapler 0.0001%")}{sm(455,176,"one full scoreboard per step")}'
 f'{B} x="640" y="90" width="200" height="90" rx="12"/>{t(740,118,"🎛️ temperature")}{sm(740,142,"0: more deterministic")}{sm(740,164,"1: balanced · 2: more random")}'
 f'{arr(260,135,326,135)}{num(293,118,1)}{arr(580,135,636,135)}{num(608,118,2)}'
 f'{B} x="330" y="230" width="250" height="55" rx="12"/>{t(455,258,"🧩 picked: &#39;cat&#39; — glue on")}'
 f'{arr(740,180,540,228)}{arr(330,255,150,184,DASH)}{num(240,225,3)}{sm(240,255,"repeat — that&#39;s why")}{sm(240,277,"answers STREAM")}')
SVG[6]=(f'{S} x="40" y="40" width="870" height="60" rx="10"/>{t(475,76,"&#39;The robot dropped the ball because IT was heavy&#39;")}'
 f'{B} x="80" y="140" width="240" height="110" rx="12"/>{t(200,170,"👀 &#39;it&#39; glances around")}{sm(200,196,"learned weights:")}{sm(200,218,"ball 69% · heavy 16% · robot 6%")}'
 f'{B} x="400" y="140" width="220" height="110" rx="12"/>{t(510,170,"🎨 blend")}{sm(510,196,"&#39;it&#39; comes out")}{sm(510,218,"BALL-flavored ⚽")}'
 f'{B} x="690" y="140" width="220" height="110" rx="12"/>{t(800,166,"🏗️ transformer")}{sm(800,190,"this, ×many heads,")}{sm(800,212,"×32 layers, ALL tokens")}{sm(800,234,"in parallel")}'
 f'{arr(200,100,200,136)}{num(180,118,1)}{arr(320,195,396,195)}{num(358,178,2)}{arr(620,195,686,195)}{num(653,178,3)}'
 f'{sm(475,290,"query·key similarity on the seats (L04) → softmax → weighted blend — demo prints these exact numbers")}')
SVG[7]=(f'{B} x="40" y="90" width="200" height="100" rx="12"/>{t(140,120,"📚 pretraining")}{sm(140,144,"read EVERYTHING")}{sm(140,166,"months · $$$M · once")}'
 f'{B} x="300" y="90" width="200" height="100" rx="12"/>{t(400,120,"🎓 fine-tuning")}{sm(400,144,"Q→A examples:")}{sm(400,166,"learn to ANSWER")}'
 f'{B} x="560" y="90" width="200" height="100" rx="12"/>{t(660,120,"⭐ RLHF")}{sm(660,144,"humans pick better →")}{sm(660,166,"taste-judge → nudge")}'
 f'{B} x="810" y="90" width="100" height="100" rx="12"/>{t(860,130,"🤖")}{sm(860,155,"the")}{sm(860,175,"assistant")}'
 f'{arr(240,140,296,140)}{num(268,123,1)}{arr(500,140,556,140)}{num(528,123,2)}{arr(760,140,806,140)}{num(783,123,3)}'
 f'{S} x="300" y="230" width="460" height="55" rx="12"/>{t(530,254,"🗒️ LoRA: freeze the brain, learn tiny sticky notes")}{sm(530,276,"tiny adapter · far fewer trainable parameters · base stays frozen")}'
 f'{arr(700,230,840,194,DASH)}{num(700,257,4)}')
SVG[8]=(f'{B} x="60" y="60" width="500" height="200" rx="14"/>{t(310,90,"🪑 the desk - context window: N tokens, that&#39;s ALL there is")}'
 f'{S} x="85" y="110" width="210" height="50" rx="8"/>{sm(190,140,"📜 role + rules (system)")}'
 f'{S} x="310" y="110" width="225" height="50" rx="8"/>{sm(422,140,"💬 conversation - oldest slides off")}'
 f'{S} x="85" y="175" width="210" height="50" rx="8"/>{sm(190,205,"📎 pasted docs + examples")}'
 f'{S} x="310" y="175" width="225" height="50" rx="8"/>{sm(422,205,"✍️ the answer itself - also here!")}'
 f'{B} x="640" y="60" width="270" height="110" rx="12"/>{t(775,88,"🗣️ the craft")}{sm(775,112,"say who to be · exact ask ·")}{sm(775,134,"show examples (few-shot) ·")}{sm(775,156,"constraints + output format")}'
 f'{arr(640,120,564,120)}{num(602,103,1)}'
 f'{D} x="640" y="200" width="270" height="92" rx="12"/>{sm(775,226,"🕳️ not in the current context = unavailable")}{sm(775,248,"past chats too, unless re-added ·")}{sm(775,270,"long context: harder to use reliably")}{num(620,235,2)}'
 f'{sm(310,290,"same model, 10× better output — prompting is iteration, not incantation")}{num(90,290,3)}')
SVG[9]=(f'{B} x="40" y="90" width="230" height="100" rx="12"/>{t(155,120,"❓ thin-shelf question")}{sm(155,144,"&#39;books about Mongolian")}{sm(155,166,"pirates?&#39;")}'
 f'{B} x="340" y="90" width="260" height="100" rx="12"/>{t(470,118,"🧠 the machine")}{sm(470,142,"produce the LIKELIEST continuation")}{sm(470,164,"truth was never in the loss (L02)")}'
 f'{D} x="670" y="90" width="240" height="100" rx="12"/>{t(790,118,"🙋 fluent · confident · WRONG")}{sm(790,142,"realistic fake title,")}{sm(790,164,"fake author, page count")}'
 f'{arr(270,140,336,140)}{num(303,123,1)}{arr(600,140,666,140)}{num(633,123,2)}'
 f'{S} x="60" y="225" width="260" height="60" rx="10"/>{sm(190,248,"📖 defense 1: facts ON the desk")}{sm(190,268,"(paste them — or RAG, L10)")}'
 f'{S} x="345" y="225" width="260" height="60" rx="10"/>{sm(475,248,"🧾 defense 2: &#39;quote the exact")}{sm(475,268,"sentence you base this on&#39;")}'
 f'{S} x="630" y="225" width="280" height="60" rx="10"/>{sm(770,248,"🤷 defense 3: &#39;if unsure, say so&#39;")}{sm(770,268,"+ verify anything you&#39;d act on")}{num(60,225,3)}')
SVG[10]=(f'{S} x="40" y="40" width="360" height="115" rx="12"/>{t(220,66,"1 before exam season - once")}'
 f'{B} x="60" y="80" width="140" height="60" rx="10"/>{sm(130,105,"📚 handbook")}{sm(130,127,"→ ✂️ chunks")}'
 f'{B} x="230" y="80" width="150" height="60" rx="10"/>{sm(305,105,"🗺️ vector DB")}{sm(305,127,"seat per chunk")}'
 f'{arr(200,110,226,110)}'
 f'{B} x="40" y="200" width="180" height="80" rx="12"/>{t(130,230,"❓ question")}{sm(130,254,"embedded too")}'
 f'{B} x="290" y="200" width="220" height="80" rx="12"/>{t(400,228,"📍 nearest seats")}{sm(400,252,"= most relevant chunks")}'
 f'{B} x="580" y="180" width="330" height="110" rx="12"/>{t(745,208,"🪑 the desk")}{sm(745,232,"question + those chunks +")}{sm(745,254,"&#39;answer ONLY from these, cite&#39; 🧾")}'
 f'{arr(130,200,280,145,DASH)}{num(200,168,2)}{arr(220,240,286,240)}{num(253,223,3)}{arr(510,240,576,240)}{num(543,223,4)}'
 f'{sm(475,300,"changing / external facts → RAG · stable behaviour or style → fine-tuning (L07) — a rule of thumb")}')
SVG[11]=(f'{B} x="40" y="100" width="190" height="90" rx="12"/>{t(135,130,"📋 goal")}{sm(135,154,"&#39;organize the")}{sm(135,176,"class picnic&#39;")}'
 f'{B} x="300" y="100" width="180" height="90" rx="12"/>{t(390,130,"🧠 THINK")}{sm(390,154,"next-token planning")}{sm(390,176,"in words (L05!)")}'
 f'{B} x="550" y="100" width="170" height="90" rx="12"/>{t(635,130,"🧰 ACT")}{sm(635,154,"writes a tool call:")}{sm(635,176,"roster.count()")}'
 f'{B} x="790" y="100" width="120" height="90" rx="12"/>{t(850,130,"👀 LOOK")}{sm(850,154,"result → desk:")}{sm(850,176,"23 kids")}'
 f'{arr(230,145,296,145)}{num(263,128,1)}{arr(480,145,546,145)}{num(513,128,2)}{arr(720,145,786,145)}'
 f'{arr(850,190,390,230,DASH)}{arr(390,230,390,194,DASH)}{num(620,225,3)}{sm(620,250,"loop until the goal is met — or max steps · timeout · repeated failure")}'
 f'{S} x="60" y="255" width="850" height="40" rx="10"/>{sm(485,280,"🚧 guardrails: read-only tools by default · spending caps · human sign-off for field-trip forms · logs of every step")}{num(60,255,4)}')
SVG[12]=(f'{S} x="40" y="40" width="400" height="110" rx="12"/>{t(240,66,"🎨 homework, millions of times")}'
 f'{B} x="60" y="80" width="110" height="55" rx="10"/>{sm(115,105,"🐱 photo")}{sm(115,125,"+noise ×1000")}'
 f'{B} x="200" y="80" width="100" height="55" rx="10"/>{sm(250,112,"📺 static")}'
 f'{B} x="320" y="80" width="100" height="55" rx="10"/>{sm(370,105,"learn: predict")}{sm(370,125,"the noise")}'
 f'{arr(170,107,196,107)}{arr(300,107,316,107)}'
 f'{B} x="40" y="190" width="130" height="80" rx="12"/>{t(105,222,"📺 pure")}{t(105,244,"static")}'
 f'{B} x="240" y="190" width="270" height="80" rx="12"/>{t(375,218,"🌀 un-noise ×20-50 steps")}{sm(375,244,"prompt&#39;s meaning-seat (L04) steers each step")}'
 f'{B} x="580" y="190" width="150" height="80" rx="12"/>{t(655,222,"🐱👑 &#39;cat with")}{t(655,244,"a crown&#39;")}'
 f'{arr(170,230,236,230)}{num(203,213,1)}{arr(510,230,576,230)}{num(543,213,2)}'
 f'{S} x="760" y="150" width="150" height="140" rx="12"/>{sm(835,180,"👀 multimodal:")}{sm(835,202,"images/audio")}{sm(835,224,"become tokens too —")}{sm(835,246,"same desk, same")}{sm(835,268,"attention (L03/L06)")}{num(760,150,3)}')

SVG[13]=(f'{D} x="40" y="40" width="250" height="100" rx="12"/>{t(165,72,"🍝 before MCP")}{sm(165,96,"every app × every tool =")}{sm(165,118,"a hand-built adapter (N×M)")}'
 f'{B} x="360" y="40" width="250" height="100" rx="12"/>{t(485,70,"🏫 hosts - the rooms")}{sm(485,94,"Claude Desktop · IDE ·")}{sm(485,116,"your agent — standard sockets 🔌")}'
 f'{B} x="680" y="40" width="230" height="100" rx="12"/>{t(795,70,"🔬 MCP servers")}{sm(795,94,"files · GitHub · your DB —")}{sm(795,116,"standard plugs")}'
 f'{arr(290,90,356,90)}{num(323,73,1)}{arr(610,90,676,90)}{num(643,73,2)}'
 f'{B} x="150" y="180" width="640" height="60" rx="12"/>{t(470,205,"each server announces: my TOOLS 🧰 · my RESOURCES 📁 · my PROMPTS 📜")}{sm(470,227,"discover (tools/list) → call (tools/call) → result lands on the desk — L11&#39;s loop, standardized")}'
 f'{arr(470,140,470,176)}{num(450,158,3)}'
 f'{S} x="150" y="255" width="640" height="40" rx="10"/>{sm(470,280,"🚧 a server runs with YOUR permissions — installing one = installing software; L11 guardrails apply double")}{num(150,255,4)}')

def dsec(n):
    _,slug,folder,title,ana,_,color = L[n-1]
    return (f'\n<!-- {n:02d} -->\n<section class="dsec" id="l{n:02d}" style="--c:{color}">\n'
      f'  <h2><span class="ln">{n}</span> {title}</h2>\n  <p class="d">{ana}</p>\n'
      f'  <svg viewBox="0 0 940 305" role="img">{SVG[n]}\n  </svg>\n'
      f'  <p class="foot"><a href="{GH}/{slug}/lessons/{folder}/README.md">Read full lesson {n:02d} →</a></p>\n</section>\n')

ALL_DSECS = "".join(dsec(n) for n in range(1,14))

def card(n):
    _,slug,folder,title,ana,_,color = L[n-1]
    return (f'    <div class="lesson" style="--c:{color}"><div class="top"><span class="num">{n}</span><h3>{title}</h3></div>'
      f'<span class="ana">{ana}</span><code>{slug}</code>'
      f'<a class="go" href="{GH}/{slug}/lessons/{folder}/README.md">Read lesson →</a>'
      f'<a class="go" href="lesson-diagrams.html#l{n:02d}">See the diagram ↗</a></div>')

INDEX = head("Learn AI the school way — tokens to agents",
  "12 branch-by-branch AI lessons + bonus MCP: tokens, embeddings, attention, RLHF, LoRA, prompting, RAG, agents, diffusion — ELI5 school analogies, diagrams and zero-dependency Python labs.",
  DSEC_CSS) + MARKER + f'''
<div class="wrap">

  <header>
    <h1>🧠 Learn AI the school way</h1>
    <p class="sub">How models actually work (tokens → embeddings → attention → RLHF &amp; LoRA), then
    how to use them well (prompting, RAG, agents, diffusion) — every concept as a school story,
    every lesson with a numbered diagram and a hands-on lab. The labs are <b>zero-dependency
    Python</b>: no GPU, no API key, no pip install.</p>
    <p class="sub" style="margin-top:8px">🎬 <b>Companion video:</b>
    <a href="{VIDEO}">9 AI Concepts Explained in 7 minutes</a> (ByteByteAI) — the aerial view;
    this course is the slow ground tour of every concept it names.</p>
    <div class="chips">
      <span class="chip">🧩 tokens</span><span class="chip">🗺️ embeddings</span>
      <span class="chip">👀 attention</span><span class="chip">⭐ RLHF &amp; LoRA</span>
      <span class="chip">📖 RAG</span><span class="chip">📋 agents</span><span class="chip">📺 diffusion</span>
    </div>
  </header>

  <div class="vs">
    <div class="vcol" style="border-top:5px solid {P1}">
      <h3>🔬 Part 1 — INSIDE the model</h3>
      <ul>
        <li>rules are grown from examples, not written 📖</li>
        <li>text becomes puzzle pieces 🧩 seated by meaning 🗺️</li>
        <li>one game: guess the next piece 🎲 — with glancing 👀</li>
        <li>finishing school: etiquette, gold stars, sticky notes ⭐</li>
      </ul>
    </div>
    <div class="vcol" style="border-top:5px solid {P2}">
      <h3>🧰 Part 2 — USING it for real</h3>
      <ul>
        <li>ask the librarian well; mind the small desk 🗣️🪑</li>
        <li>the confident kid makes things up — defenses 🙋</li>
        <li>open-book exams (RAG) 📖 and hall passes (agents) 📋</li>
        <li>un-blur the static: diffusion &amp; multimodal 📺</li>
      </ul>
    </div>
  </div>

  <h2 id="big-picture">🗺️ The big picture — one diagram, both worlds</h2>
  <p class="sub">The whole course on one canvas. Click for the
  <a href="images/big-picture-4k.png">4K version</a>.</p>
  <figure style="background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px;margin-top:16px">
    <a href="images/big-picture-4k.png"><img src="images/big-picture.svg" alt="The big picture: inside the model (tokens, embeddings, attention, RLHF) and using it (prompting, RAG, agents, diffusion)" loading="lazy" style="width:100%;height:auto;border-radius:8px;background:#fff"></a>
  </figure>

  <h2 id="part1">🔬 Part 1 — inside the model (lessons 1–7)</h2>
  <p class="sub">One git branch = one idea; branch 05 contains lessons 01–05. Labs run with plain Python 3.</p>
  <div class="grid">
{chr(10).join(card(n) for n in range(1,8))}
  </div>

  <h2 id="part2">🧰 Part 2 — using it for real (lessons 8–12 + bonus 13)</h2>
  <p class="sub">No installs here either — the labs use any chatbot you already have, plus paper and honesty.</p>
  <div class="grid">
{chr(10).join(card(n) for n in range(8,14))}
  </div>

  <pre><code># take the course locally:
git clone https://github.com/BaluRaut/learn-ai-school.git
cd learn-ai-school
python3 demo/bigram_model.py            # a language model in 60 seconds
git checkout lesson-01-what-is-ai       # then lesson by lesson</code></pre>

  <div class="callout">🔌 <b>Went deep on lesson 13?</b> There is now a whole <a href="https://baluraut.github.io/learn-mcp-school/">MCP school</a> — with a real server &amp; client in the repo and 5 use cases with sequence diagrams. And for lesson 11: the <a href="https://baluraut.github.io/learn-agents-school/">Agents school</a> — a runnable agent, guardrails, failure modes, and 5 patterns. And for lessons 04 &amp; 10: the <a href="https://baluraut.github.io/learn-vectordb-school/">VectorDB school</a> — a runnable mini vector database and the RAG machine room.</div>

  <div class="callout">🎓 <b>From the same school:</b>
    <a href="https://baluraut.github.io/learn-docker-school/">Docker</a> ·
    <a href="https://baluraut.github.io/learn-kubernetes-school/">Kubernetes</a> ·
    <a href="https://baluraut.github.io/learn-aws-school/">AWS</a> ·
    <a href="https://baluraut.github.io/learn-argocd-school/">ArgoCD</a> — same analogies universe,
    same branch-by-branch method.</div>

  <h2 id="diagrams">📐 The lesson diagrams — follow the numbers</h2>
  <p class="sub">Every lesson as one numbered box-and-arrow diagram (purple = inside the model,
  teal = using it) — also on a <a href="lesson-diagrams.html">standalone page</a>.</p>
{ALL_DSECS}
  <a class="btn" href="{GH}/lesson-01-what-is-ai/lessons/01-what-is-ai/README.md">Start Lesson 01 →</a>
  <a class="btn alt" href="study-plan.html">🗓️ Study plan (4 weeks)</a>
  <a class="btn alt" href="lesson-diagrams.html">📐 All 13 lesson diagrams</a>
  <a class="btn alt" href="quiz.html">🧪 Quiz</a>
  <a class="btn alt" href="before-and-tradeoffs.html">⏮️ Before &amp; trade-offs</a>

  <footer>
    Learn AI School · zero magic left ·
    <a href="https://github.com/BaluRaut/learn-ai-school">github.com/BaluRaut/learn-ai-school</a> ·
    companion video: <a href="{VIDEO}">ByteByteAI — 9 AI Concepts</a>
   ·
  <a href="https://baluraut.github.io/school/">🏫 all schools</a>
 ·
  <a href="https://github.com/BaluRaut/learn-ai-school/issues">🐛 found a mistake?</a>
</footer>

</div>
</body>
</html>
'''

DIAGRAMS = head("Lesson diagrams — Learn AI School",
  "All 12 AI lessons + bonus MCP as numbered entity diagrams — tokens, embeddings, attention, RLHF, RAG, agents, diffusion — on one page.",
  DSEC_CSS + TOC_CSS) + MARKER + f'''
<div class="wrap">
<header>
  <p><a href="index.html">← Back to the course home</a></p>
  <h1>📐 The 13 lessons as diagrams</h1>
  <p class="sub">Part 1: inside the model (purple, 1–7) · Part 2: using it (teal, 8–12).
  Follow the circled numbers <b>1 → 2 → 3</b>.</p>
  <nav class="toc">
    <a href="#l01">1 What is AI</a><a href="#l02">2 Training</a><a href="#l03">3 Tokens</a>
    <a href="#l04">4 Embeddings</a><a href="#l05">5 Next token</a><a href="#l06">6 Attention</a>
    <a href="#l07">7 RLHF/LoRA</a><a href="#l08">8 Prompting</a><a href="#l09">9 Hallucinations</a>
    <a href="#l10">10 RAG</a><a href="#l11">11 Agents</a><a href="#l12">12 Diffusion</a><a href="#l13">13 MCP</a>
  </nav>
</header>
{ALL_DSECS}
<footer>
  Learn AI School · <a href="index.html">Course home</a> ·
  <a href="https://github.com/BaluRaut/learn-ai-school">github.com/BaluRaut/learn-ai-school</a>
 ·
  <a href="https://baluraut.github.io/school/">🏫 all schools</a>
 ·
  <a href="https://github.com/BaluRaut/learn-ai-school/issues">🐛 found a mistake?</a>
</footer>
</div>
</body>
</html>
'''

# ---------------- before-and-tradeoffs ----------------
TRADE_CSS = """
  .term { background:var(--card); border:1px solid var(--line); border-top:6px solid var(--c,var(--accent)); border-radius:16px; padding:22px; margin-top:26px; scroll-margin-top:16px; }
  .term h2 { font-size:1.3rem; margin-bottom:10px; }
  .hist { background:var(--bg); border-left:5px solid var(--c,var(--accent)); border-radius:10px; padding:14px 16px; margin:10px 0 14px; }
  .hist b { display:block; margin-bottom:4px; } .hist p { color:var(--muted); font-size:.95rem; }
  .quad { display:grid; grid-template-columns:repeat(auto-fit,minmax(230px,1fr)); gap:12px; }
  .q { border:1px solid var(--line); border-radius:12px; padding:14px; }
  .q h4 { margin-bottom:6px; font-size:.98rem; } .q ul { margin-left:18px; color:var(--muted); font-size:.92rem; }
  .q.merit { border-top:4px solid var(--ok); } .q.demerit { border-top:4px solid var(--bad); }
  .q.use { border-top:4px solid var(--blue); } .q.avoid { border-top:4px solid #f59e0b; }
"""
def term(id_, color, title, before_t, before_p, merits, demerits, use, avoid):
    li = lambda xs: "".join(f"<li>{x}</li>" for x in xs)
    return f'''
<section class="term" id="{id_}" style="--c:{color}">
  <h2>{title}</h2>
  <div class="hist"><b>⏮️ {before_t}</b><p>{before_p}</p></div>
  <div class="quad">
    <div class="q merit"><h4>✅ Merits</h4><ul>{li(merits)}</ul></div>
    <div class="q demerit"><h4>❌ Demerits</h4><ul>{li(demerits)}</ul></div>
    <div class="q use"><h4>👍 Use when</h4><ul>{li(use)}</ul></div>
    <div class="q avoid"><h4>👎 Think twice when</h4><ul>{li(avoid)}</ul></div>
  </div>
</section>'''

TRADEOFFS = head("Before & trade-offs — Learn AI School",
  "For every big AI idea: what the world looked like before it, its merits and demerits, and where to use it vs where not.",
  TRADE_CSS + TOC_CSS) + f'''
<div class="wrap">
<header>
  <p><a href="index.html">← Back to the course home</a></p>
  <h1>⏮️ Before &amp; trade-offs</h1>
  <p class="sub">Every tool replaced something worse — and is itself the wrong tool somewhere.
  For each big idea: what life was like <b>before</b>, honest <b>merits ✅ / demerits ❌</b>,
  and <b>where to use it 👍 vs not 👎</b>.</p>
  <nav class="toc">
    <a href="#ml">🧠 ML vs rulebooks</a><a href="#tune">🗒️ Tune vs RAG vs prompt</a>
    <a href="#rag">📖 RAG</a><a href="#agents">📋 Agents</a><a href="#diffusion">📺 Diffusion</a><a href="#openclosed">🔓 Open vs closed</a><a href="#mcp">🔌 MCP</a>
  </nav>
</header>
{term("ml", P1, "🧠 Machine learning (vs rulebooks) — lessons 01–02",
  "Before ML took over (pre-2012 for vision, pre-2020 for language)",
  "Software was rulebooks: expert systems, thousands of hand-written if-thens, brittle grammar engines. Spam filters listed bad words; translators stored phrase tables. Anything fuzzy — images, speech, natural language — stayed embarrassingly bad, because some rules simply cannot be written.",
  ["handles what rulebooks never could: fuzz, ambiguity, perception","improves with data instead of with more if-statements","one method spans images, speech, text, code"],
  ["rules are grown → hard to inspect or fully explain","inherits its data's gaps and biases","fails weirdly (stickers fool it), not gracefully","training costs compute; behavior isn't guaranteed"],
  ["patterns beyond writable rules: language, vision, recommendation","'roughly right, usually' is acceptable and checkable"],
  ["exact auditable logic: payroll, tax, safety interlocks — write code!","tiny data, huge stakes, no tolerance for surprises","a regex would do — the boring tool is allowed to win 😄"])}
{term("tune", P1, "🗒️ Fine-tuning &amp; LoRA vs RAG vs prompting — lessons 07, 08, 10",
  "Before this decision tree existed (~2022)",
  "If you wanted a model to know or behave differently, the only lever was full retraining — museum-budget territory. Today there are three ladders, and picking wrong burns months: prompting (free, per-request), RAG (fresh facts on the desk), fine-tuning/LoRA (bake in style).",
  ["prompting: instant, free, reversible — always try FIRST","RAG: fresh + auditable facts, update = re-index tonight","LoRA: real style/format/domain-voice gains with a small adapter"],
  ["prompting can't add knowledge or unbreakable habits","RAG lives and dies by retrieval quality (garbage in…)","tuning: costs, drifts stale, and CANNOT reliably add facts","teams routinely fine-tune when a better prompt would have done"],
  ["order of operations: prompt → RAG for facts → tune for style","tune when format/tone must be deep and consistent (and prompts maxed out)"],
  ["'let's fine-tune so it knows our docs' — that's RAG's job, always","before you've even written a decent system prompt"])}
{term("rag", P2, "📖 RAG — lesson 10",
  "Before RAG (pre-2023 for most teams)",
  "Company knowledge lived behind keyword search (exact-word-or-nothing), hand-curated FAQ bots that answered 12 questions, and 'ask Priya, she knows where the doc is'. Models answered company questions closed-book — i.e., they made things up (lesson 09).",
  ["grounded answers with citations — hallucination's best antidote","knowledge updates nightly (re-index), no retraining","semantic: finds meaning, not just matching words","per-question cost is pennies"],
  ["a real pipeline to build and monitor (chunking, top-k, rerank)","retrieval misses → confident closed-book nonsense returns","struggles with cross-document reasoning ('compare all 50 contracts')"],
  ["chat-with-your-docs, support bots, policy Q&amp;A — the classic wins","answers must cite sources (compliance loves RAG)"],
  ["the whole corpus fits comfortably on the desk — just paste it","questions need global aggregation, not lookup → databases/BI","your documents are wrong — RAG faithfully cites garbage 😅"])}
{term("agents", P2, "📋 Agents &amp; tool use — lesson 11",
  "Before agents (~2023)",
  "Automation meant brittle scripts and RPA bots that clicked pixel coordinates and shattered when a button moved. Chatbots could only TALK — every actual action returned to a human. The glue between 'model suggests' and 'something happens' was always a person.",
  ["turns advice into outcomes: looks things up, files, fixes, retries","handles fuzzy multi-step goals scripts never could","recovers from surprises by re-planning (scripts just crash)"],
  ["errors compound step by step — confidently wrong, with momentum","harder to test: same goal, different paths each run","token costs multiply (every think-act-look loop bills)","real permissions = real blast radius — guardrails are NOT optional"],
  ["multi-step work with verifiable outcomes (tests pass, ticket filed)","read-heavy research/triage where a human signs the final act"],
  ["one deterministic step — a plain API call is faster and safer","irreversible actions without human gates (payments, deletes, sends)","you can't yet MEASURE task success — build evals first"])}
{term("diffusion", P2, "📺 Diffusion image generation — lesson 12",
  "Before diffusion (~2021)",
  "Custom visuals meant stock-photo hunting, commissioning designers for every variant, or GANs — impressive but unstable to train and hard to steer with text. 'A cat astronaut in watercolor' was a commission, not a sentence.",
  ["any describable image in seconds; iterate by editing the sentence","steerable: style, composition, edits (inpainting), consistent characters","the same recipe scales to video and audio"],
  ["text inside images is letter-SHAPES (L03's revenge) — often gibberish","global constraints wobble: fingers, symmetry, object counts","training-data provenance and copyright remain contested","photoreal fakes demand disclosure norms — use them"],
  ["concepts, moods, storyboards, illustrations, product mockups","volume + iteration beat pixel-perfect fidelity"],
  ["brand-exact detail (logos, UI text) — designers still win","factual/technical figures (use real charts! — dataviz, not vibes)","anything passing off generated people/events as real"])}
{term("openclosed", P2, "🔓 Open-weights vs closed API models",
  "Before the choice existed (~2023)",
  "Frontier AI = a handful of closed APIs, take it or leave it. Then LLaMA-family leaks and releases created a genuine second lane: download the weights, run them yourself, tune them freely (LoRA, L07). Now every team faces the build-vs-rent question AWS taught you (EC2 course!) — for brains.",
  ["closed API: frontier quality, zero ops, pay-per-token","open weights: data stays home, cost-per-token can plummet at scale, tune anything, no vendor veto"],
  ["closed: data leaves, prices/models change under you, rate limits","open: you run the GPUs (ops!), usually behind frontier quality, security patches are your job"],
  ["closed: start here — validate the product before owning infra","open: privacy mandates, huge steady volume, deep customization"],
  ["open 'to save money' at small scale — GPU ops eats the savings","closed for regulated data without a proper agreement in place"])}
{term("mcp", P2, "🔌 MCP vs bespoke tool integrations — lesson 13",
  "Before MCP (pre-2025)",
  "Every AI app hand-wired every tool: one GitHub integration for the IDE, ANOTHER for the chatbot, a third for the agent — N apps × M tools = N×M adapters, none reusable. Capabilities were private wiring, not shareable parts.",
  ["write a server once → works in every MCP host (N+M)","growing ecosystem of ready-made servers to plug in","standard discovery: models find tools at connect time","swap AI apps without rewiring your integrations"],
  ["young standard — server quality varies wildly","each server = installed software with YOUR permissions","tool results can carry prompt injection — audit sources","local config friction (paths, env, versions) is real"],
  ["agents/apps needing several tools, today and tomorrow","your capability should work from many AI apps","teams sharing internal tools across assistants"],
  ["one hardcoded tool in one app — plain function calling is simpler","untrusted third-party servers on sensitive machines","a plain REST call from YOUR code does the job — no model needed"])}
<footer>
  Learn AI School · <a href="index.html">Course home</a> ·
  <a href="lesson-diagrams.html">Lesson diagrams</a> ·
  <a href="https://github.com/BaluRaut/learn-ai-school">github.com/BaluRaut/learn-ai-school</a>
 ·
  <a href="https://baluraut.github.io/school/">🏫 all schools</a>
 ·
  <a href="https://github.com/BaluRaut/learn-ai-school/issues">🐛 found a mistake?</a>
</footer>
</div>
</body>
</html>
'''

# ---------------- study plan ----------------
SP_CSS = """
  .paces { display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:12px; margin:18px 0 8px; }
  .pace { background:var(--card); border:1px solid var(--line); border-radius:14px; padding:14px 16px; font-size:.93rem; color:var(--muted); }
  .pace b { color:var(--ink); }
  .progress-box { position:sticky; top:0; z-index:10; background:var(--bg); padding:12px 0; }
  .progress-inner { background:var(--card); border:1px solid var(--line); border-radius:14px; padding:12px 18px; display:flex; align-items:center; gap:16px; }
  .bar { flex:1; height:12px; background:var(--line); border-radius:999px; overflow:hidden; }
  .bar > div { height:100%; width:0%; background:var(--ok); border-radius:999px; transition:width .3s; }
  #ptext { font-weight:700; white-space:nowrap; }
  .week { background:var(--card); border:1px solid var(--line); border-left:6px solid var(--c,var(--accent)); border-radius:16px; padding:20px 22px; margin-top:22px; }
  .week h2 { font-size:1.15rem; display:flex; align-items:baseline; gap:10px; flex-wrap:wrap; margin:0; }
  .week h2 .wk { flex:none; font-size:.8rem; font-weight:800; color:#fff; background:var(--c,var(--accent)); border-radius:999px; padding:3px 12px; }
  .week .goal { color:var(--muted); font-size:.93rem; margin:6px 0 12px; }
  .lesson-row { display:flex; align-items:baseline; gap:10px; padding:7px 0; border-top:1px dashed var(--line); font-size:.95rem; }
  .lesson-row input { transform:scale(1.25); accent-color:var(--ok); flex:none; position:relative; top:2px; }
  .lesson-row .time { margin-left:auto; color:var(--muted); font-size:.85rem; white-space:nowrap; }
  .lesson-row a { text-decoration:none; font-weight:600; } .lesson-row a:hover { text-decoration:underline; }
  .milestone { margin-top:12px; background:var(--bg); border-left:4px solid var(--ok); border-radius:8px; padding:10px 14px; font-size:.92rem; }
  .milestone b { color:var(--ok); }
  #done { display:none; text-align:center; background:var(--card); border:2px solid var(--ok); border-radius:20px; padding:32px 24px; margin-top:26px; }
"""
def row(n):
    _,slug,folder,title,_,mins,_ = L[n-1]
    return (f'  <div class="lesson-row"><input type="checkbox" data-l="l{n:02d}" id="sl{n:02d}">'
      f'<label for="sl{n:02d}"><a href="{GH}/{slug}/lessons/{folder}/README.md">{n:02d} · {title}</a></label>'
      f'<span class="time">~{mins} min</span></div>')

def week(color, tag, title, goal, ns, milestone):
    return (f'<section class="week" style="--c:{color}">\n'
      f'  <h2><span class="wk">{tag}</span> {title}</h2>\n  <p class="goal">{goal}</p>\n'
      + "\n".join(row(n) for n in ns) +
      f'\n  <div class="milestone">🏁 <b>Checkpoint:</b> {milestone}</div>\n</section>')

STUDY = head("Study plan — Learn AI School",
  "A 4-week study plan for the 12-lesson AI course: sequence, time estimates, weekly milestones — progress saved in your browser.",
  SP_CSS) + f'''
<div class="wrap">
<header>
  <p><a href="index.html">← Back to the course home</a></p>
  <h1>🗓️ The study plan — 13 lessons, 4 weeks</h1>
  <p class="sub">~<b>3 sessions a week</b>: read the lesson (~15 min) + do its lab (~25 min).
  Tick lessons off — <b>progress is saved in this browser</b>. Watch the
  <a href="{VIDEO}">companion video</a> before Week 1 for the aerial view.</p>
  <div class="paces">
    <div class="pace">🐢 <b>Steady:</b> 3 sessions/week → done in 4 weeks.</div>
    <div class="pace">🐇 <b>Fast track:</b> a weekend per part → done in 2 weekends.</div>
    <div class="pace">💰 <b>Cost:</b> zero. Plain Python + any free chatbot.</div>
  </div>
</header>

<div class="progress-box"><div class="progress-inner">
  <span id="ptext">0 / 12</span>
  <div class="bar"><div id="pbar"></div></div>
</div></div>

{week(P1,"WEEK 1","📖 Foundations — how learning works",
  "The inversion (rules are grown), the red pen, and the puzzle pieces. Labs: two of the three demos.",
  [1,2,3],
  "run bigram_model.py and tokenizer_toy.py; explain 'data + answers → rules' and why 'strawberry' is hard — out loud, to someone.")}
{week(P1,"WEEK 2","🗺️ The engine — meaning, guessing, glancing",
  "Embeddings, the next-token game, attention. Lab: the attention demo, twice (once modified).",
  [4,5,6],
  "run attention_toy.py; flip 'it' to ball-shaped and predict the change before running; recite query/key/value in school words.")}
{week(P2,"WEEK 3","⭐ Finishing school &amp; asking well",
  "RLHF/LoRA, prompting on the small desk, and the confident kid. Labs: the A/B prompt test + hallucination hunt.",
  [7,8,9],
  "your B-prompt visibly beats your A-prompt; you caught (and verified!) one hallucination; you know when to fine-tune vs RAG — say the rule.")}
{week(P2,"WEEK 4","🧰 Building — open books, hall passes, static",
  "RAG by hand, being the agent's harness, diffusion probes — then the capstone.",
  [10,11,12,13],
  "🏆 <b>Capstone:</b> re-watch the <a href='{VIDEO}'>companion video</a> and pause after each of the 9 concepts — explain every one in YOUR school-analogy words. Bonus: build the 30-line RAG from lesson 10 for real.")}

<div id="done">
  <h2>🎓 13 / 13 — zero magic left, sockets included!</h2>
  <p class="sub" style="margin:10px auto 0">Next: build something — or tour the rest of the school:
  <a href="https://baluraut.github.io/learn-kubernetes-school/">Kubernetes</a> ·
  <a href="https://baluraut.github.io/learn-docker-school/">Docker</a> ·
  <a href="https://baluraut.github.io/learn-aws-school/">AWS</a> ·
  <a href="https://baluraut.github.io/learn-argocd-school/">ArgoCD</a>.</p>
</div>

<footer>
  Learn AI School · <a href="index.html">Course home</a> ·
  <a href="https://github.com/BaluRaut/learn-ai-school">GitHub</a>
 ·
  <a href="https://baluraut.github.io/school/">🏫 all schools</a>
 ·
  <a href="https://github.com/BaluRaut/learn-ai-school/issues">🐛 found a mistake?</a>
</footer>
</div>
<script>
(function(){{
  var KEY='ai-study-plan', state={{}};
  try{{state=JSON.parse(localStorage.getItem(KEY)||'{{}}')}}catch(e){{}}
  var boxes=[].slice.call(document.querySelectorAll('input[data-l]'));
  function render(){{
    var done=boxes.filter(function(b){{return b.checked}}).length;
    document.getElementById('ptext').textContent=done+' / '+boxes.length;
    document.getElementById('pbar').style.width=(100*done/boxes.length)+'%';
    document.getElementById('done').style.display=done===boxes.length?'block':'none';
  }}
  boxes.forEach(function(b){{
    b.checked=!!state[b.dataset.l];
    b.addEventListener('change',function(){{state[b.dataset.l]=b.checked;
      localStorage.setItem(KEY,JSON.stringify(state));render();}});
  }});
  render();
}})();
</script>
</body>
</html>
'''

import os
os.makedirs('docs', exist_ok=True)
open('docs/index.html','w').write(INDEX)
open('docs/lesson-diagrams.html','w').write(DIAGRAMS)
open('docs/before-and-tradeoffs.html','w').write(TRADEOFFS)
open('docs/study-plan.html','w').write(STUDY)
print("generated:",
  "index dsec =", INDEX.count('class="dsec"'),
  "| diagrams dsec =", DIAGRAMS.count('class="dsec"'),
  "| terms =", TRADEOFFS.count('class="term"'),
  "| study rows =", STUDY.count('lesson-row'))
