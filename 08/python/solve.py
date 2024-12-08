import sys
from collections import defaultdict
from itertools import permutations
import numpy as np

infile = sys.argv[1] if len(sys.argv) > 1 else 'input'
data = [list(line.strip()) for line in open(infile)]

R = len(data)
C = len(data[0])

antennas_by_type = defaultdict(list)

for ri in range(R):
    for ci in range(C):
        tile = data[ri][ci]
        if tile != ".":
            antennas_by_type[tile].append((ri, ci))

antinodes_1 = set()
antinodes_2 = set()

for ants in antennas_by_type.values():
    for a_pair in permutations(ants, 2):
        node_a, node_b = [np.array(v) for v in a_pair]
        vec = node_b - node_a
        node_c = node_b + vec
        if node_c[0] in range(R) and node_c[1] in range(C):
            antinodes_1.add(tuple(node_c))
        node_x = node_b
        while node_x[0] in range(R) and node_x[1] in range(C):
            antinodes_2.add(tuple(node_x))
            node_x = node_x + vec

ans_1 = len(antinodes_1)
print(f"Part1: {ans_1}")

ans_2 = len(antinodes_2)
print(f"Part2: {ans_2}")