import sys
from itertools import product

infile = sys.argv[1] if len(sys.argv) > 1 else "input"
data = [list(line.strip()) for line in open(infile)]

R = len(data)
C = len(data[0])


def count_sides_and_corners(field):
    corner_count = 0
    side_count = 0
    for ri, ci in product(range(-1, R), range(-1, C)):
        read_area = tuple(
            (ri + x, ci + y) in field for x, y in [(0, 0), (1, 0), (0, 1), (1, 1)]
        )
        if sum(read_area) in [1, 3]:
            corner_count += 1
        elif read_area in [
            (1, 0, 0, 1),
            (0, 1, 1, 0),
        ]:
            corner_count += 2
        elif sum(read_area) == 2:
            side_count += 1
    return side_count, corner_count


dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

seen = set()
sorted_fields = []

for ri, ci in product(range(R), range(C)):
    if (ri, ci) in seen:
        continue
    seen.add((ri, ci))
    current_value = data[ri][ci]
    current_field = [(ri, ci)]
    to_search = [(ri, ci)]
    while to_search:
        s_ri, s_ci = to_search.pop()
        for n_ri, n_ci in [(s_ri + x, s_ci + y) for x, y in dirs]:
            if n_ri not in range(R) or n_ci not in range(C):
                continue
            if data[n_ri][n_ci] != current_value or (n_ri, n_ci) in seen:
                continue
            current_field.append((n_ri, n_ci))
            seen.add((n_ri, n_ci))
            to_search.append((n_ri, n_ci))
    side_count, corner_count = count_sides_and_corners(current_field)
    sorted_fields.append((len(current_field), side_count, corner_count))

part_1 = sum(f * (s + c) for f, s, c in sorted_fields)
print("Part1", part_1)
part_2 = sum(f * c for f, s, c in sorted_fields)
print("Part2", part_2)
