import sys
from itertools import chain

infile = sys.argv[1] if len(sys.argv) > 1 else "input"
with open(infile) as file:
    data = file.read().strip()

data = [int(x) for x in list(data)]

data_locs = list()
space_locs = list()
index = 0
capture_data = True
for d in data:
    if capture_data:
        data_locs.append(range(index, index + d))
    else:
        space_locs.append(range(index, index + d))
    index += d
    capture_data = not capture_data

# Part 1

disk = []
for i in range(0, len(data), 2):
    disk += [int(i / 2)] * data[i]
    if i + 1 >= len(data):
        break
    disk += [None] * data[i + 1]

data_indices = list(chain(*data_locs))
space_indices = list(chain(*space_locs))

for last_data_index, first_space_index in zip(reversed(data_indices), space_indices):
    if first_space_index > last_data_index:
        break
    data_element = disk[last_data_index]
    space_element = disk[first_space_index]
    disk[first_space_index] = data_element
    disk[last_data_index] = space_element

checksum = 0
for i, d in enumerate(disk):
    if d:
        checksum += i * d

print("Part1", checksum)

# Part 2

data_stays = []
data_moved = []

for data_index, data_loc in reversed([(i, loc) for i, loc in enumerate(data_locs)]):
    space_loc = None
    for space_cand in space_locs:
        if space_cand.start > data_loc.start:
            break
        if len(space_cand) < len(data_loc):
            continue
        space_loc = space_cand
        break
    if not space_loc:
        data_stays.append((data_index, data_loc))
        continue
    delta_len = len(space_loc) - len(data_loc)
    new_data = range(space_loc.start, space_loc.stop - delta_len)
    new_space = range(new_data.stop, space_loc.stop)
    data_moved.append((data_index, new_data))
    space_locs.remove(space_loc)
    space_locs.append(new_space)
    space_locs = sorted(space_locs, key=lambda x: x.start)

all_data_locs = data_stays + data_moved

checksum_2 = 0
for d_type, d_index_range in all_data_locs:
    for i in d_index_range:
        checksum_2 += d_type * i

print("Part2", checksum_2)
