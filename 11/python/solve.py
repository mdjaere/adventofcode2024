import sys
from collections import Counter

infile = sys.argv[1] if len(sys.argv) > 1 else "input"
stones = [int(x) for x in open(infile).read().strip().split()]


def new_stones(n):
    new = []
    if n == 0:
        new.append(1)
    elif len(str(n)) % 2 == 0:
        n_str = str(n)
        new.append(int(n_str[0 : int(len(n_str) / 2)]))
        new.append(int(n_str[int(len(n_str) / 2) :]))
    else:
        new.append(n * 2024)
    return new


def get_count(stones, n):
    stone_count = dict(Counter(stones))
    for i in range(n):
        new_count = {}
        for k, v in stone_count.items():
            to_add = new_stones(k)
            for n in to_add:
                if n in new_count:
                    new_count[n] += v
                else:
                    new_count[n] = v
        stone_count = new_count
    return sum(stone_count.values())


part_1 = get_count(stones, 25)
part_2 = get_count(stones, 75)

print("Part1", part_1)
print("Part2", part_2)
