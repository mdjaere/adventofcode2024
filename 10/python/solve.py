import sys
from itertools import product

infile = sys.argv[1] if len(sys.argv) > 1 else "input"
topomap = [[int(x) for x in line.strip()] for line in open(infile)]

RR = range(len(topomap))
CR = range(len(topomap[0]))
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def search_new_locs(loc):
    results = []
    for d in dirs:
        cand = (loc[0] + d[0], loc[1] + d[1])
        if cand[0] not in RR or cand[1] not in CR:
            continue
        results.append(cand)
    return results


incomplete = [[(ri, ci)] for ri, ci in product(RR, CR) if topomap[ri][ci] == 0]
complete = []
while incomplete:
    trail = incomplete.pop()
    current_loc = trail[-1]
    current_value = topomap[current_loc[0]][current_loc[1]]
    for next_loc in search_new_locs(trail[-1]):
        next_value = topomap[next_loc[0]][next_loc[1]]
        if next_value != current_value + 1:
            continue
        new_trail = trail + [next_loc]
        if next_value == 9:
            complete.append(new_trail)
            continue
        incomplete.append(new_trail)

part_1 = len({(trail[0], trail[-1]) for trail in complete})
print("Part1", part_1)

part_2 = len(complete)
print("Part2", part_2)
