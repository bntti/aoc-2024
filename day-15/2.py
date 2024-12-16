import sys
import time
import math

INPUT = sys.argv[1]

grid = []
moves = ""
pos = (0, 0)
with open(INPUT, "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) == 0:
            continue
        if line[0] in "<>v^":
            moves += line
            continue

        if "@" in line:
            for x, c in enumerate(line):
                if c == "@":
                    pos = (x * 2, len(grid))

        row = []
        for c in line:
            if c == "#":
                row.append("#")
                row.append("#")
            elif c == ".":
                row.append(".")
                row.append(".")
            elif c == "@":
                row.append("@")
                row.append(".")
            else:
                row.append("[")
                row.append("]")
        grid.append(row)

h = len(grid)
w = len(grid[0])
grid[pos[1]][pos[0]] = "."


dirs = {">": (1, 0), "<": (-1, 0), "v": (0, 1), "^": (0, -1)}
for move in moves:

    # print(move)
    # for y in range(h):
    #     for x in range(w):
    #         if x == pos[0] and y == pos[1]:
    #             print("@", end="")
    #         else:
    #             print(grid[y][x], end="")
    #     print()
    # time.sleep(0.05)

    dir = dirs[move]
    x = pos[0] + dir[0]
    y = pos[1] + dir[1]
    if grid[y][x] == "#":
        continue
    if grid[y][x] == ".":
        pos = (x, y)
        continue

    if move == "<" or move == ">":
        for i in range(1, 100):
            new_x = x + dir[0] * i
            if grid[y][new_x] == "#":
                break
            elif grid[y][new_x] in "[]":
                continue

            for j in range(i, 0, -1):
                next_x = x + dir[0] * j

                prev_x = x + dir[0] * (j - 1)
                grid[y][next_x] = grid[y][prev_x]
            grid[y][x] = "."
            pos = (x, y)
            break
        continue

    # ^v movement
    wid = [x]
    if grid[y][x] == "[":
        wid.append(x + 1)
    else:
        wid.append(x - 1)

    widd = [wid[:]]
    for i in range(1, 100):
        new_y = y + dir[1] * i
        ok = True
        fail = False
        new_x = []
        for x2 in wid:
            if grid[new_y][x2] == "#":
                fail = True
            elif grid[new_y][x2] == "]":
                new_x.append(x2 - 1)
                new_x.append(x2)
                ok = False
            elif grid[new_y][x2] == "[":
                new_x.append(x2 + 1)
                new_x.append(x2)
                ok = False

        new_x = list(set(new_x))
        wid = new_x
        widd.append(wid[:])
        if fail:
            break
        if not ok:
            continue

        for j in range(i, 0, -1):
            next_y = y + dir[1] * j
            prev_y = y + dir[1] * (j - 1)
            for x2 in widd[j - 1]:
                grid[next_y][x2] = grid[prev_y][x2]
                grid[prev_y][x2] = "."
        for x2 in widd[0]:
            grid[y][x2] = "."
        pos = (x, y)
        break


for row in grid:
    print("".join(row))

res = 0
for y in range(h):
    for x in range(w):
        if grid[y][x] == "[":
            res += 100 * y + x
print(res)
