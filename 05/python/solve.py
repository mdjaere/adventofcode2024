from collections import defaultdict
from copy import deepcopy
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'input'
lines = [line.strip() for line in open(infile)]
collect_pairs = True

series_list = []
data = defaultdict(list)

for line in lines:
    if not line:
        collect_pairs = False
        continue
    if collect_pairs:
        a, b = [int(x) for x in line.split("|")]
        data[a].append(b)
        if b not in data:
            data[b] = []
    else:
        series_list.append([int(x) for x in line.split(",")])


def check_series(series):
    for index, x in enumerate(series):
        first_pages = series[:index]
        downstream_pages = data[x]
        for ds_page in downstream_pages:
            if ds_page in first_pages:
                return False
    return True


def middle_item(series):
    return series[len(series) // 2]


to_fix = []

score_1 = 0
for series in series_list:
    valid = check_series(series)
    if valid:
        score_1 += middle_item(series)
    else:
        to_fix.append(series)

print("Part 1:", score_1)


def fix_order(series):
    data_copy = deepcopy(data)
    for k in data.keys():
        if k not in series:
            del data_copy[k]
        else:
            data_copy[k] = list(set(data_copy[k]).intersection(set(series)))
    reversed_sorted_series = [
        item[0]
        for item in sorted(
            zip(data_copy.keys(), [len(v) for v in data_copy.values()]),
            key=lambda item: item[1],
        )
    ]
    return list(reversed(reversed_sorted_series))


score_2 = 0
for series in to_fix:
    fixed_series = fix_order(series)
    assert check_series(fixed_series)
    score_2 += middle_item(fixed_series)

print("Part 2:", score_2)