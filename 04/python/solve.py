import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"
data = [line.strip() for line in open(infile)]
R = len(data)
C = len(data[0])


def p_func_one(ri, ci):
    return [
        [(ri, ci), (ri, ci + 1), (ri, ci + 2), (ri, ci + 3)],
        [(ri, ci), (ri + 1, ci), (ri + 2, ci), (ri + 3, ci)],
        [(ri, ci), (ri + 1, ci + 1), (ri + 2, ci + 2), (ri + 3, ci + 3)],
        [(ri, ci), (ri + 1, ci - 1), (ri + 2, ci - 2), (ri + 3, ci - 3)],
    ]


def p_func_two(ri, ci):
    return [
        [
            (ri - 1, ci - 1),
            (ri - 1, ci + 1),
            (ri, ci),
            (ri + 1, ci - 1),
            (ri + 1, ci + 1),
        ]
    ]


def search_for_christmas(pattern_func, to_match):
    score = 0
    for ri in range(0, R):
        for ci in range(0, C):
            patterns = pattern_func(ri, ci)
            for pattern in patterns:
                sample = []
                for ri_s, ci_s in pattern:
                    if ri_s in range(0, R) and ci_s in range(0, C):
                        sample.append(data[ri_s][ci_s])
                    else:
                        sample = []
                        break
                if sample:
                    if "".join(sample) in to_match:
                        score += 1

    return score


score_1 = search_for_christmas(p_func_one, ["XMAS", "SAMX"])
score_2 = search_for_christmas(p_func_two, ["SSAMM", "MSAMS", "MMASS", "SMASM"])

print("Part 1:", score_1)
print("Part 2:", score_2)
