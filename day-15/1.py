import sys
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
                    pos = (x, len(grid))
        grid.append([c for c in line])

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

    dir = dirs[move]
    x = pos[0] + dir[0]
    y = pos[1] + dir[1]
    if grid[y][x] == "#":
        continue
    if grid[y][x] == ".":
        pos = (x, y)
        continue

    assert grid[y][x] == "O"
    for i in range(1, 100):
        new_x = x + dir[0] * i
        new_y = y + dir[1] * i
        if grid[new_y][new_x] == "#":
            break
        elif grid[new_y][new_x] == "O":
            continue
        grid[new_y][new_x] = "O"
        grid[y][x] = "."
        pos = (x, y)
        break

for row in grid:
    print("".join(row))

res = 0
for y in range(h):
    for x in range(w):
        if grid[y][x] == "O":
            res += 100 * y + x
print(res)
