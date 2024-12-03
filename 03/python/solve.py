import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'input'
data = open(infile).read()
result_enabled, result_disabled = 0, 0
first, second = "", ""
state = 0
enabled = True
i = 0
while i < len(data):
    if state == 0:
        if data[i : i + 4] == "do()":
            enabled = True
            i += 4
        elif data[i : i + 7] == "don't()":
            enabled = False
            i += 7
        elif data[i : i + 4] == "mul(":
            first, second = "", ""
            state = 1
            i += 4
        else:
            i += 1
    if state == 1:
        c = data[i]
        if c.isdigit():
            first += c
        elif c == ",":
            state = 2
        else:
            state = 0
        i += 1
    if state == 2:
        c = data[i]
        if c.isdigit():
            second += c
        elif c == ")":
            res = int(first) * int(second)
            if enabled:
                result_enabled += res
            else:
                result_disabled += res
            state = 0
        else:
            state = 0
        i += 1

p1 = result_enabled + result_disabled
p2 = result_enabled
if infile == "input":
    assert p1 == 170807108
    assert p2 == 74838033
print("Part 1: ", p1)
print("Part 2: ", p2)