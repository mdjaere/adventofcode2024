import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"
data = [list(line.strip()) for line in open(infile)]

R = len(data)
C = len(data[0])

loc = None
start = None
V = [(-1, 0), (0, 1), (1, 0), (0, -1)]
view = V[0]


def change_view(view):
    return V[(V.index(view) + 1) % len(V)]


clear_tiles = []

for ri in range(0, R):
    for ci in range(0, C):
        if data[ri][ci] == ".":
            clear_tiles.append((ri, ci))
        if data[ri][ci] == "^":
            loc = (ri, ci)
            start = loc
            data[ri][ci] = "."


def check_map(o_loc=(-1, -1)):
    loc = start
    view = V[0]
    visited_states = set()
    while True:
        current_state = (loc, view)
        if current_state in visited_states:
            # Looping
            return True, len(visited_states)
        visited_states.add(current_state)
        loc_ahead = (loc[0] + view[0], loc[1] + view[1])
        if loc_ahead[0] not in range(0, R) or loc_ahead[1] not in range(0, C):
            # Outside, non-looping
            return False, len({a[0] for a in visited_states})
        tile_ahead = data[loc_ahead[0]][loc_ahead[1]]
        if tile_ahead == "#" or loc_ahead == o_loc:
            view = change_view(view)
            continue
        if tile_ahead == ".":
            loc = loc_ahead
            continue
        assert False


looping, locs = check_map()
if not looping:
    print(f"Part 1: {locs}")

loop_count = 0
for o_loc in clear_tiles:
    looping, locs = check_map(o_loc)
    loop_count += looping

print(f"Part 2: {loop_count}")
