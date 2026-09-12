"""Attention in 40 lines: who is 'it' looking at? 👀 (Lesson 06)

Every word gets a tiny meaning-vector; each word then 'attends' to the
others — similar meanings get high scores. Watch 'it' look at 'robot'.

    python3 demo/attention_toy.py
"""
import math

# hand-made 4-number "embeddings" (lesson 04): [thing-ness, alive-ness, action-ness, size]
EMB = {
    "the":    [0.1, 0.0, 0.0, 0.0],
    "robot":  [0.9, 0.7, 0.1, 0.6],
    "dropped":[0.0, 0.1, 0.9, 0.1],
    "ball":   [0.8, 0.0, 0.1, 0.2],
    "because":[0.0, 0.0, 0.1, 0.0],
    "it":     [0.8, 0.5, 0.0, 0.5],   # ← meaning-shaped like... what? let's see
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
print("👀 who does each word LOOK AT? (attention weights, one row per word)\n")
for w in ["it", "heavy", "dropped"]:
    scores = [dot(EMB[w], EMB[o]) for o in SENT]
    weights = softmax(scores)
    row = sorted(zip(SENT, weights), key=lambda t: -t[1])[:3]
    pretty = " · ".join(f"{o}:{p:.0%}" for o, p in row)
    print(f"  {w!r:10} attends to → {pretty}")

print("\n💡 'it' looks hardest at 'robot' and 'ball' — meaning-similarity decides.")
print("   A transformer does this for EVERY token, in parallel, many layers deep,")
print("   with LEARNED (not hand-made) vectors. That's the whole magic trick.")
