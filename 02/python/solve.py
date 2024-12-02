import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"
readings = [[int(x) for x in line.strip().split()] for line in open(infile)]


def test_reading(r):
    macro_movement = "inc" if r[0] < r[-1] else "dec"
    for a, b in zip(r[:-1], r[1:]):
        if not 1 <= abs(a - b) <= 3:
            return False
        current_dir = "inc" if a < b else "dec"
        if current_dir != macro_movement:
            return False
    return True


safe_count = sum(test_reading(r) for r in readings)

if infile == "input":
    assert safe_count == 670
print("Part 1:", safe_count)

safe_count = 0
for r in readings:
    for e_i in range(len(r)):
        safe = test_reading(r[:e_i] + r[e_i + 1 :])
        if safe:
            safe_count += 1
            break

if infile == "input":
    assert safe_count == 700
print("Part 2:", safe_count)
