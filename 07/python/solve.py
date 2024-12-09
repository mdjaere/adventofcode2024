import sys
from itertools import product
from operator import add, mul

infile = sys.argv[1] if len(sys.argv) > 1 else "input"
lines = [line.strip() for line in open(infile)]


def conc(a, b):
    return int(str(a) + str(b))


ops = [add, mul, conc]

good = []
good2 = []
for li, line in enumerate(lines):
    ans, nums = line.split(": ")
    ans = int(ans)
    nums = [int(x) for x in nums.split()]
    alts = product(ops, repeat=len(nums) - 1)
    for alt in alts:
        score = nums[0]
        for i in range(len(nums) - 1):
            x = nums[i + 1]
            op = alt[i]
            score = op(score, x)
        if score > ans:
            continue
        if score == ans:
            if conc in alt:
                good2.append(score)
            else:
                good.append(score)
            break

print(f"Part 1: {sum(good)}")
print(f"Part 2: {sum(good)+sum(good2)}")
