"""Attention in 40 lines: who is 'it' looking at? 👀 (Lesson 06)

Every word gets a tiny meaning-vector; each word then 'attends' to the
OTHER words — similar meanings get high scores. Watch 'it' look at 'ball':
the sentence says "it was heavy", and the ball is the heavy thing.

    python3 demo/attention_toy.py
"""
import math

# hand-made 4-number "embeddings" (lesson 04): [thing-ness, alive-ness, action-ness, heaviness]
EMB = {
    "the":    [0.1, 0.0, 0.0, 0.0],
    "robot":  [0.5, 0.7, 0.1, 0.1],   # a thing, alive-ish, light
    "dropped":[0.0, 0.1, 0.9, 0.1],
    "ball":   [0.8, 0.0, 0.1, 0.8],   # a thing, not alive, HEAVY
    "because":[0.0, 0.0, 0.1, 0.0],
    "it":     [0.6, 0.0, 0.0, 0.6],   # ← a heavy thing... which one? let's see
    "was":    [0.0, 0.1, 0.2, 0.0],
    "heavy":  [0.1, 0.0, 0.1, 0.9],
}
SENT = "the robot dropped the ball because it was heavy".split()

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

def softmax(xs):
    exps = [math.exp(x * 4) for x in xs]          # ×4 sharpens, like real scaling
    s = sum(exps)
    return [e / s for e in exps]

print('sentence: "the robot dropped the ball because it was heavy"\n')
print("👀 who does each word LOOK AT? (attention weights over the OTHER words)\n")
for w in ["it", "heavy", "dropped"]:
    others = [o for o in SENT if o != w]
    scores = [dot(EMB[w], EMB[o]) for o in others]
    weights = softmax(scores)
    merged = {}
    for o, p in zip(others, weights):             # 'the' appears twice — add it up
        merged[o] = merged.get(o, 0) + p
    row = sorted(merged.items(), key=lambda t: -t[1])[:3]
    pretty = " · ".join(f"{o}:{p:.0%}" for o, p in row)
    print(f"  {w!r:10} attends to → {pretty}")

print("\n💡 'it' looks hardest at 'ball' — the heavy thing — then at 'heavy' itself.")
print("   Make 'it' robot-shaped ([0.5, 0.6, 0.1, 0.1] — as if the sentence ended")
print("   '...because it was TIRED') and rerun: the glance flips to 'robot'.")
print("   A transformer does this for EVERY token, in parallel, many layers deep,")
print("   with LEARNED (not hand-made) vectors. That's the whole magic trick.")
