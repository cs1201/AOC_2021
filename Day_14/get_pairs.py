from collections import defaultdict

s = [
    "NNCB",
    "NCNBCHB",
    "NBCCNBBBCBHCB",
    "NBBBCNCCNBBNBNBBCHBHHBCHB",
    "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
]

for k, s in enumerate(s):
    contained_pairs = defaultdict(lambda: 0)
    # contained_letters = defaultdict(lambda:0)
    s = [x for x in s]
    for i, el in enumerate(s):
        if i < len(s)-1:
            contained_pairs[(el, s[i+1])] += 1
    print(f"Step {k+1}: {contained_pairs}")
        # contained_letters[el] += 1
