import sys
from collections import Counter

infile = sys.argv[1] if len(sys.argv) > 1 else "input"
list_a, list_b = zip(*[[int(x) for x in line.strip().split()] for line in open(infile)])

list_a = sorted(list_a)
list_b = sorted(list_b)
diffs = [abs(a - list_b[i]) for i, a in enumerate(list_a)]
print("Part1:", sum(diffs))

count_b = Counter(list_b)
sim_scores = [a * count_b[a] for a in list_a]
print("Part2:", sum(sim_scores))
