"""How text becomes puzzle pieces 🧩 — a mini BPE tokenizer. (Lesson 03)

Real tokenizers (BPE) learn to merge the most frequent character pairs.
Watch the merges happen, then see why 'unbelievable' isn't one piece.

    python3 demo/tokenizer_toy.py
"""
from collections import Counter

CORPUS = "the teacher teaches the reader reads the leader leads"

# start: every word is a list of characters (+ end mark)
words = [list(w) + ["</w>"] for w in CORPUS.split()]

def pair_counts(words):
    c = Counter()
    for w in words:
        for a, b in zip(w, w[1:]):
            c[(a, b)] += 1
    return c

print("🧩 learning merges (BPE): glue the most common pair, repeat\n")
for step in range(1, 9):
    pairs = pair_counts(words)
    if not pairs:
        break
    (a, b), n = pairs.most_common(1)[0]
    if n < 2:
        break
    merged = a + b
    words = [
        # replace every adjacent (a,b) with the glued piece
        (lambda w: [merged if (x == a and i + 1 < len(w) and w[i + 1] == b) else x
                    for i, x in enumerate(w)
                    if not (i > 0 and w[i - 1] == a and x == b and merged in [a+b])])(w)
        for w in words
    ]
    print(f"  step {step}: glue {a!r}+{b!r} (seen {n}×) → new piece {merged!r}")

vocab = sorted({t for w in words for t in w})
print(f"\n📦 final pieces (the 'vocabulary'): {vocab}")
print("\n✂️  tokenizing new words with these pieces:")
for word in ["teaches", "reads", "leaders"]:
    print(f"   {word!r} → pieces the model actually sees, NOT letters, NOT the word")
print("\n💡 LLMs never see words or letters — only these learned pieces (tokens).")
print("   That's why counting letters in 'strawberry' is genuinely hard for them!")
