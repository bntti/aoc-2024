INPUT = "input"
# INPUT = "test1.in"

grid = []
towers = {}
with open(INPUT, "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        grid.append(line)
        for j, c in enumerate(line):
            if c != ".":
                if c not in towers:
                    towers[c] = []
                towers[c].append((j, i))

h = len(grid)
w = len(grid[0])
found = [[False for _ in range(w)] for _ in range(h)]


def check(pos):
    global found
    x = pos[0]
    y = pos[1]
    if not (0 <= x < w) or not (0 <= y < h):
        return
    found[y][x] = True


for key in towers:
    for i in range(len(towers[key])):
        for j in range(i + 1, len(towers[key])):
            for x in range(100):
                pos0 = towers[key][i]
                pos1 = towers[key][j]
                diff = (pos1[0] - pos0[0], pos1[1] - pos0[1])
                check((pos0[0] - x * diff[0], pos0[1] - x * diff[1]))
                check((pos1[0] + x * diff[0], pos1[1] + x * diff[1]))


res = 0
for y in range(h):
    ff = ""
    for x in range(w):
        if found[y][x]:
            res += 1

        if grid[y][x] != ".":
            ff += grid[y][x]
        elif found[y][x]:
            ff += "#"
        else:
            ff += "."
    print(ff)

print(res)
