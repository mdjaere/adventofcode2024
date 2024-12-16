import sys
from itertools import product

infile = sys.argv[1] if len(sys.argv) > 1 else "input"
data = [list(line.strip()) for line in open(infile)]

RR = range(len(data))
CR = range(len(data[0]))

one_side = [(1, 1, 0, 0), (0, 1, 0, 1), (0, 0, 1, 1), (1, 0, 1, 0)]
one_corner = [
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
    (0, 1, 1, 1),
    (1, 0, 1, 1),
    (1, 1, 0, 1),
    (1, 1, 1, 0),
]
two_corners = [
    (1, 0, 0, 1),
    (0, 1, 1, 0),
]
no_sides_or_corners = [(0, 0, 0, 0), (1, 1, 1, 1)]


def count_sides_and_corners(field):
    # Marchy squary
    corner_count = 0
    side_count = 0
    rs, cs = zip(*field)
    for ri, ci in product(
        range(min(rs) - 1, max(rs) + 1), range(min(cs) - 1, max(cs) + 1)
    ):
        read_area = tuple(
            (ri + x, ci + y) in field for x, y in [(0, 0), (1, 0), (0, 1), (1, 1)]
        )
        if read_area in no_sides_or_corners:
            continue
        elif read_area in one_side:
            side_count += 1
        elif read_area in one_corner:
            corner_count += 1
        elif read_area in two_corners:
            corner_count += 2
        else:
            assert False
    return side_count, corner_count


seen = set()
sorted_fields = []

for ri, ci in product(RR, CR):
    if (ri, ci) in seen:
        continue
    seen.add((ri, ci))
    current_value = data[ri][ci]
    current_field = [(ri, ci)]
    to_search = [(ri, ci)]
    while to_search:
        s_ri, s_ci = to_search.pop()
        for n_ri, n_ci in [
            (s_ri + x, s_ci + y) for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]
        ]:
            if n_ri not in RR or n_ci not in CR:
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
