"""A COMPLETE language model in ~50 lines. Zero dependencies. (Lessons 01, 02, 05)

It "trains" by counting which word follows which (a bigram model), then
generates text by predicting the next word — with a TEMPERATURE dial.
Every giant LLM is this idea with vastly better statistics.

    python3 demo/bigram_model.py
"""
import random
from collections import defaultdict, Counter

TEXT = """
the school bell rings and the students run to the class .
the teacher opens the book and the class reads the story .
the story is about a robot that learns from the students .
the robot reads the book and the robot learns the lesson .
the students love the robot and the robot loves the school .
"""

# ---- "training": just count what follows what (lesson 02: learning = statistics)
counts = defaultdict(Counter)
words = TEXT.split()
for a, b in zip(words, words[1:]):
    counts[a][b] += 1

print("📚 what the model learned (a few rows of its 'brain'):")
for w in ["the", "robot", "students"]:
    top = ", ".join(f"{nxt}×{c}" for nxt, c in counts[w].most_common(3))
    print(f"   after {w!r:12} → {top}")

# ---- "inference": predict next word, one at a time (lesson 05: next-token loop)
def generate(start, n=14, temperature=1.0):
    out = [start]
    for _ in range(n):
        options = counts[out[-1]]
        if not options:
            break
        nxts, cs = zip(*options.items())
        # temperature: 0.01 = always the favorite; 2.0 = adventurous (lesson 05)
        weights = [c ** (1.0 / max(temperature, 0.01)) for c in cs]
        out.append(random.choices(nxts, weights=weights)[0])
    return " ".join(out)

print("\n🥶 temperature 0.01 — plays it safe (same every run):")
print("  ", generate("the", temperature=0.01))
print("\n😊 temperature 1.0 — natural:")
print("  ", generate("the", temperature=1.0))
print("\n🥵 temperature 2.0 — creative/chaotic:")
print("  ", generate("the", temperature=2.0))
print("\n💡 An LLM does EXACTLY this loop — with 'what follows what' learned")
print("   from trillions of words, across thousands of context words at once.")
