s = open('gen-site.py').read()
n0 = len(s)

# 1) L list entry
old = ' (12,"lesson-12-diffusion","12-diffusion","\U0001F4FA Diffusion &amp; multimodal","Un-blurring TV static, step by step, toward your words.",40,P2),\n]'
new = old[:-1] + ' (13,"lesson-13-mcp","13-mcp","\U0001F50C Bonus: MCP","The universal plug — any tool into any AI app, one standard socket.",40,P2),\n]'
assert old in s; s = s.replace(old, new)

# 2) SVG[13] inserted before "def dsec"
svg13 = (
"SVG[13]=(f'{D} x=\"40\" y=\"40\" width=\"250\" height=\"100\" rx=\"12\"/>{t(165,72,\"\U0001F35D before MCP\")}{sm(165,96,\"every app × every tool =\")}{sm(165,118,\"a hand-built adapter (N×M)\")}'\n"
" f'{B} x=\"360\" y=\"40\" width=\"250\" height=\"100\" rx=\"12\"/>{t(485,70,\"\U0001F3EB hosts - the rooms\")}{sm(485,94,\"Claude Desktop · IDE ·\")}{sm(485,116,\"your agent — standard sockets \U0001F50C\")}'\n"
" f'{B} x=\"680\" y=\"40\" width=\"230\" height=\"100\" rx=\"12\"/>{t(795,70,\"\U0001F52C MCP servers\")}{sm(795,94,\"files · GitHub · your DB —\")}{sm(795,116,\"standard plugs\")}'\n"
" f'{arr(290,90,356,90)}{num(323,73,1)}{arr(610,90,676,90)}{num(643,73,2)}'\n"
" f'{B} x=\"150\" y=\"180\" width=\"640\" height=\"60\" rx=\"12\"/>{t(470,205,\"each server announces: my TOOLS \U0001F9F0 · my RESOURCES \U0001F4C1 · my PROMPTS \U0001F4DC\")}{sm(470,227,\"discover (tools/list) → call (tools/call) → result lands on the desk — L11&#39;s loop, standardized\")}'\n"
" f'{arr(470,140,470,176)}{num(450,158,3)}'\n"
" f'{S} x=\"150\" y=\"255\" width=\"640\" height=\"40\" rx=\"10\"/>{sm(470,280,\"\U0001F6A7 a server runs with YOUR permissions — installing one = installing software; L11 guardrails apply double\")}{num(150,255,4)}')\n\n"
)
assert 'def dsec(n):' in s; s = s.replace('def dsec(n):', svg13 + 'def dsec(n):', 1)

# 3) ranges + headings
s = s.replace('ALL_DSECS = "".join(dsec(n) for n in range(1,13))', 'ALL_DSECS = "".join(dsec(n) for n in range(1,14))')
s = s.replace('{chr(10).join(card(n) for n in range(8,13))}', '{chr(10).join(card(n) for n in range(8,14))}')
s = s.replace('\U0001F9F0 Part 2 — using it for real (lessons 8–12)', '\U0001F9F0 Part 2 — using it for real (lessons 8–12 + bonus 13)')

# 4) diagrams page h1, toc, button
s = s.replace('The 12 lessons as diagrams', 'The 13 lessons as diagrams')
s = s.replace('<a href="#l12">12 Diffusion</a>', '<a href="#l12">12 Diffusion</a><a href="#l13">13 MCP</a>')
s = s.replace('\U0001F4D0 All 12 lesson diagrams', '\U0001F4D0 All 13 lesson diagrams')

# 5) study plan
s = s.replace('[10,11,12],', '[10,11,12,13],')
s = s.replace('12 lessons, 4 weeks', '13 lessons, 4 weeks')
s = s.replace('\U0001F393 12 / 12 — zero magic left!', '\U0001F393 13 / 13 — zero magic left, sockets included!')

# 6) trade-offs: toc chip + MCP term after openclosed term
s = s.replace('<a href="#openclosed">\U0001F513 Open vs closed</a>', '<a href="#openclosed">\U0001F513 Open vs closed</a><a href="#mcp">\U0001F50C MCP</a>')
anchor = '"closed for regulated data without a proper agreement in place"])}'
mcp_term = anchor + '''
{term("mcp", P2, "\U0001F50C MCP vs bespoke tool integrations — lesson 13",
  "Before MCP (pre-2025)",
  "Every AI app hand-wired every tool: one GitHub integration for the IDE, ANOTHER for the chatbot, a third for the agent — N apps × M tools = N×M adapters, none reusable. Capabilities were private wiring, not shareable parts.",
  ["write a server once → works in every MCP host (N+M)","growing ecosystem of ready-made servers to plug in","standard discovery: models find tools at connect time","swap AI apps without rewiring your integrations"],
  ["young standard — server quality varies wildly","each server = installed software with YOUR permissions","tool results can carry prompt injection — audit sources","local config friction (paths, env, versions) is real"],
  ["agents/apps needing several tools, today and tomorrow","your capability should work from many AI apps","teams sharing internal tools across assistants"],
  ["one hardcoded tool in one app — plain function calling is simpler","untrusted third-party servers on sensitive machines","a plain REST call from YOUR code does the job — no model needed"])}'''
assert anchor in s; s = s.replace(anchor, mcp_term, 1)

open('gen-site.py','w').write(s)
print("patched ok, delta bytes:", len(s) - n0)
